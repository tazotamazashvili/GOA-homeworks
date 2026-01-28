const form = document.getElementById("mortgage-form");
const loanInput = document.getElementById("loan-amount");
const rateInput = document.getElementById("interest-rate");
const termInput = document.getElementById("term-years");

const monthlyOutput = document.getElementById("monthly-payment");
const totalOutput = document.getElementById("total-payment");

function validateField(field) {
  const error = field.nextElementSibling;
  if (!field.value || isNaN(field.value) || Number(field.value) <= 0) {
    error.style.display = "block";
    return false;
  }
  error.style.display = "none";
  return true;
}

function calculateMortgage(principal, annualRate, years) {
  const monthlyRate = annualRate / 100 / 12;
  const n = years * 12;
  const numerator = principal * monthlyRate * Math.pow(1 + monthlyRate, n);
  const denominator = Math.pow(1 + monthlyRate, n) - 1;
  const monthly = denominator === 0 ? 0 : numerator / denominator;

  return monthly;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const isLoanValid = validateField(loanInput);
  const isRateValid = validateField(rateInput);
  const isTermValid = validateField(termInput);

  if (!isLoanValid || !isRateValid || !isTermValid) return;

  const principal = parseFloat(loanInput.value);
  const annualRate = parseFloat(rateInput.value);
  const years = parseInt(termInput.value, 10);

  const monthlyPayment = calculateMortgage(principal, annualRate, years);
  const totalPayment = monthlyPayment * years * 12;

  monthlyOutput.textContent = monthlyPayment.toFixed(2) + " €";
  totalOutput.textContent = totalPayment.toFixed(2) + " €";
});
