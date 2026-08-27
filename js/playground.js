/* =============================================
   PLAYGROUND.JS — ML Simulation Engines
   Loan Approval & Insurance Cost Predictors
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ========== LOAN APPROVAL SIMULATOR ========== */
  const loanInputs = {
    income:  document.getElementById('loan-income'),
    amount:  document.getElementById('loan-amount'),
    term:    document.getElementById('loan-term'),
    credit:  document.getElementById('loan-credit'),
    area:    document.getElementById('loan-area'),
  };

  const loanDisplays = {
    incomeVal:  document.getElementById('loan-income-val'),
    amountVal:  document.getElementById('loan-amount-val'),
    termVal:    document.getElementById('loan-term-val'),
    resultValue: document.getElementById('loan-result-value'),
    resultDetail: document.getElementById('loan-result-detail'),
    resultBar:   document.getElementById('loan-result-bar'),
    resultBox:   document.getElementById('loan-result'),
  };

  function formatCurrency(n) {
    return '₹' + Number(n).toLocaleString('en-IN');
  }

  function predictLoan() {
    const income = parseInt(loanInputs.income.value);
    const amount = parseInt(loanInputs.amount.value);
    const term   = parseInt(loanInputs.term.value);
    const credit = parseInt(loanInputs.credit.value);
    const area   = loanInputs.area.value;

    // Update display values
    loanDisplays.incomeVal.textContent = formatCurrency(income);
    loanDisplays.amountVal.textContent = formatCurrency(amount);
    loanDisplays.termVal.textContent = term;

    // Simulated prediction logic (mimics real ML model behavior)
    let score = 0;

    // Income-to-loan ratio (most important factor)
    const ratio = income / (amount / term);
    if (ratio > 4)      score += 35;
    else if (ratio > 2) score += 25;
    else if (ratio > 1) score += 15;
    else                score += 5;

    // Credit history (huge factor)
    score += credit === 1 ? 30 : 5;

    // Property area
    if (area === 'semiurban')      score += 15;
    else if (area === 'urban')     score += 12;
    else                           score += 8;

    // Income bracket bonus
    if (income > 100000)      score += 12;
    else if (income > 50000)  score += 8;
    else if (income > 30000)  score += 4;

    // Term preference (longer terms are slightly better for approval)
    if (term >= 360)     score += 8;
    else if (term >= 180) score += 5;
    else                  score += 2;

    // Clamp to 0–100
    score = Math.min(100, Math.max(0, score));

    // Display result
    const approved = score >= 55;
    loanDisplays.resultValue.textContent = score + '%';
    loanDisplays.resultBar.style.width = score + '%';

    if (approved) {
      loanDisplays.resultBox.className = 'playground-sim__result playground-sim__result--approved';
      loanDisplays.resultDetail.textContent = '✅ Likely Approved — Strong eligibility profile';
      loanDisplays.resultBar.style.background = 'linear-gradient(90deg, #34d399, #2dd4bf)';
    } else {
      loanDisplays.resultBox.className = 'playground-sim__result playground-sim__result--rejected';
      loanDisplays.resultDetail.textContent = '⚠️ At Risk — Consider improving credit or adjusting loan amount';
      loanDisplays.resultBar.style.background = 'linear-gradient(90deg, #f87171, #fb923c)';
    }
  }

  // Bind inputs
  Object.values(loanInputs).forEach(input => {
    input.addEventListener('input', predictLoan);
    input.addEventListener('change', predictLoan);
  });

  // Initial prediction
  predictLoan();


  /* ========== INSURANCE COST SIMULATOR ========== */
  const insInputs = {
    age:      document.getElementById('ins-age'),
    bmi:      document.getElementById('ins-bmi'),
    children: document.getElementById('ins-children'),
    smoker:   document.getElementById('ins-smoker'),
    region:   document.getElementById('ins-region'),
  };

  const insDisplays = {
    ageVal:      document.getElementById('ins-age-val'),
    bmiVal:      document.getElementById('ins-bmi-val'),
    childrenVal: document.getElementById('ins-children-val'),
    smokerLabel: document.getElementById('ins-smoker-label'),
    resultValue: document.getElementById('ins-result-value'),
    resultDetail: document.getElementById('ins-result-detail'),
    resultBar:   document.getElementById('ins-result-bar'),
    resultBox:   document.getElementById('ins-result'),
  };

  // Smoker toggle
  insInputs.smoker.addEventListener('click', () => {
    const isActive = insInputs.smoker.dataset.active === 'true';
    insInputs.smoker.dataset.active = (!isActive).toString();
    insInputs.smoker.classList.toggle('active', !isActive);
    insDisplays.smokerLabel.textContent = !isActive ? 'Yes' : 'No';
    predictInsurance();
  });

  function predictInsurance() {
    const age      = parseInt(insInputs.age.value);
    const bmi      = parseFloat(insInputs.bmi.value);
    const children = parseInt(insInputs.children.value);
    const smoker   = insInputs.smoker.dataset.active === 'true';
    const region   = insInputs.region.value;

    // Update display values
    insDisplays.ageVal.textContent = age;
    insDisplays.bmiVal.textContent = bmi.toFixed(1);
    insDisplays.childrenVal.textContent = children;

    // Simulated prediction (inspired by real insurance dataset regression coefficients)
    // Base cost
    let cost = 2500;

    // Age factor (strong positive correlation)
    cost += age * 260;

    // BMI factor
    if (bmi > 30) {
      cost += (bmi - 30) * 500 + 2000; // Obese surcharge
    } else {
      cost += bmi * 50;
    }

    // Children
    cost += children * 800;

    // Smoker (biggest factor — roughly 4x multiplier)
    if (smoker) {
      cost *= 3.8;
      cost += 2500;
    }

    // Region adjustments
    const regionMult = {
      southeast: 1.05,
      southwest: 1.0,
      northeast: 1.08,
      northwest: 0.98,
    };
    cost *= regionMult[region] || 1.0;

    // Round to nearest 100
    cost = Math.round(cost / 100) * 100;

    // Calculate bar percentage (max ~60000 for extreme case)
    const barPct = Math.min(100, (cost / 60000) * 100);

    // Cost tier
    let tier, tierColor;
    if (cost < 8000) {
      tier = '💚 Low Premium';
      tierColor = 'linear-gradient(90deg, #34d399, #2dd4bf)';
    } else if (cost < 20000) {
      tier = '💛 Moderate Premium';
      tierColor = 'linear-gradient(90deg, #fbbf24, #fb923c)';
    } else {
      tier = '❤️ High Premium';
      tierColor = 'linear-gradient(90deg, #f87171, #ef4444)';
    }

    // Display
    insDisplays.resultValue.textContent = '$' + cost.toLocaleString('en-US');
    insDisplays.resultDetail.textContent = tier + ' — Annual estimate based on features';
    insDisplays.resultBar.style.width = barPct + '%';
    insDisplays.resultBar.style.background = tierColor;
    insDisplays.resultBox.className = 'playground-sim__result';
  }

  // Bind inputs
  ['age', 'bmi', 'children', 'region'].forEach(key => {
    insInputs[key].addEventListener('input', predictInsurance);
    insInputs[key].addEventListener('change', predictInsurance);
  });

  // Initial prediction
  predictInsurance();
});
