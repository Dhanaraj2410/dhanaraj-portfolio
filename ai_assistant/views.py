"""
AI Assistant API views with rate limiting.
"""
import time
from collections import defaultdict
from django.conf import settings
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status
from .services import chat_with_ai, analyze_resume_match


class AIRateThrottle(AnonRateThrottle):
    rate = '10/minute'


@api_view(['POST'])
@throttle_classes([AIRateThrottle])
def ai_chat(request):
    """
    AI Chatbot endpoint.
    POST /api/ai/chat/
    Body: {"message": "What projects has Dhanaraj built?"}
    """
    message = request.data.get('message', '').strip()
    if not message:
        return Response(
            {'success': False, 'error': 'Please provide a message.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if len(message) > 1000:
        return Response(
            {'success': False, 'error': 'Message is too long (max 1000 characters).'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    result = chat_with_ai(message)
    return Response(result)


@api_view(['POST'])
@throttle_classes([AIRateThrottle])
def ai_resume_analysis(request):
    """
    Resume Analyzer endpoint.
    POST /api/ai/resume-analysis/
    Body: {"job_description": "We are looking for a Python developer..."}
    """
    job_description = request.data.get('job_description', '').strip()
    if not job_description:
        return Response(
            {'success': False, 'error': 'Please provide a job description.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if len(job_description) > 5000:
        return Response(
            {'success': False, 'error': 'Job description is too long (max 5000 characters).'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    result = analyze_resume_match(job_description)
    return Response(result)
