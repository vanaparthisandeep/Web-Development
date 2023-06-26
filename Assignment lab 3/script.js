let final_answer = "";
let calculation = "";

function appendNumber(number) {
  final_answer += number;
  updateDisplay();
}

function solve_calculation(operator) {
  calculation = operator;
  final_answer += operator;
  updateDisplay();
}

function final_res() {
  final_answer = eval(final_answer);
  updateDisplay();
}

function solvingsqrroot() {
  final_answer = Math.sqrt(eval(final_answer));
  updateDisplay();
}

function solve_Trignometry_Func(func) {
  const radianValue = eval(final_answer) * (Math.PI / 180); 
  let result;
  
  if (func === "sin") {
    result = Math.sin(radianValue);
  } else if (func === "cos") {
    result = Math.cos(radianValue);
  } else if (func === "tan") {
    result = Math.tan(radianValue);
  }
  
  final_answer = result;
  updateDisplay();
}

function solvepower() {
  final_answer = Math.pow(eval(final_answer), eval(final_answer));
  updateDisplay();
}

function vanish() {
  final_answer = "";
  updateDisplay();
}

function updateDisplay() {
  document.getElementById("result").value = final_answer;
}

