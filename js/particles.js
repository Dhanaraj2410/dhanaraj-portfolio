/* =============================================
   PARTICLES.JS — Casual Floating Particles
   Soft, friendly dots that drift gently
   ============================================= */

(function () {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width, height;
  let particles = [];
  let mouse = { x: null, y: null };
  let animFrame;

  const CONFIG = {
    count: 55,
    minRadius: 2,
    maxRadius: 6,
    speed: 0.3,
    mouseRadius: 120,
    colors: [
      'rgba(124, 58, 237, 0.35)',   // purple
      'rgba(244, 114, 182, 0.3)',   // pink
      'rgba(45, 212, 191, 0.3)',    // teal
      'rgba(251, 146, 60, 0.25)',   // orange
      'rgba(96, 165, 250, 0.3)',    // blue
      'rgba(251, 191, 36, 0.25)',   // gold
    ],
    lineOpacity: 0.06,
    lineDistance: 140,
  };

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.radius = CONFIG.minRadius + Math.random() * (CONFIG.maxRadius - CONFIG.minRadius);
      this.color = CONFIG.colors[Math.floor(Math.random() * CONFIG.colors.length)];
      this.vx = (Math.random() - 0.5) * CONFIG.speed;
      this.vy = (Math.random() - 0.5) * CONFIG.speed;
      this.baseRadius = this.radius;
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;

      // Bounce off edges gently
      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;

      // Mouse interaction — gentle push
      if (mouse.x !== null) {
        const dx = this.x - mouse.x;
        const dy = this.y - mouse.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONFIG.mouseRadius) {
          const force = (CONFIG.mouseRadius - dist) / CONFIG.mouseRadius;
          this.x += dx * force * 0.02;
          this.y += dy * force * 0.02;
          this.radius = this.baseRadius + force * 2;
        } else {
          this.radius += (this.baseRadius - this.radius) * 0.05;
        }
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.fill();
    }
  }

  function init() {
    particles = [];
    const count = Math.min(CONFIG.count, Math.floor((width * height) / 20000));
    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }

  function drawLines() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONFIG.lineDistance) {
          const opacity = CONFIG.lineOpacity * (1 - dist / CONFIG.lineDistance);
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(124, 58, 237, ${opacity})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    drawLines();
    animFrame = requestAnimationFrame(animate);
  }

  // Event listeners
  window.addEventListener('resize', () => {
    resize();
    init();
  });

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  window.addEventListener('mouseout', () => {
    mouse.x = null;
    mouse.y = null;
  });

  // Start
  resize();
  init();
  animate();
})();
