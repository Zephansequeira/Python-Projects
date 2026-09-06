'use strict';

let secretNumber = Math.trunc(Math.random() * 50) + 1;
let score = 20;
let highScore = 0;

const displayMessage = function (message) {
  document.querySelector('.message').textContent = message;
};

console.log(secretNumber);

document.querySelector('.again').addEventListener('click', function () {
  secretNumber = Math.trunc(Math.random() * 50) + 1;
  score = 20;
  document.querySelector('.score').textContent = score;
  displayMessage('Start guessing...');
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').textContent = '?';
  document.querySelector('.guess').value = '';
});

document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);

  // No input
  if (!guess) {
    displayMessage('⛔ No number!');
  }

  // Player wins
  else if (guess === secretNumber) {
    displayMessage('Correct Answer!! ');
    document.querySelector('body').style.backgroundColor = 'lightgreen';
    document.querySelector('.number').textContent = secretNumber;

    if (score > highScore) {
      highScore = score;
      document.querySelector('.highscore').textContent = highScore;
    }
  }

  // Guess is wrong
  else if (guess !== secretNumber) {
    if (score > 1) {
      let scoreVal = guess > secretNumber ? '📈 Too high!' : '📉 Too low!';
      displayMessage(scoreVal);

      score--;
      document.querySelector('.score').textContent = score;
    } else {
      displayMessage('You lost the Game');
      document.querySelector('.score').textContent = 0;
    }
  }
});
