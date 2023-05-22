const headsButton = document.getElementById('headsButton');
const tailsButton = document.getElementById('tailsButton');
const result = document.getElementById('result');

function flipCoin() {
    // Return 'heads' or 'tails' randomly.
    return Math.random() < 0.5 ? 'heads' : 'tails';
}

headsButton.onclick = function() {
    const coinResult = flipCoin();
    if (coinResult === 'heads') {
        result.textContent = 'The coin landed on heads. You win!';
    } else {
        result.textContent = 'The coin landed on tails. You lose.';
    }
};

tailsButton.onclick = function() {
    const coinResult = flipCoin();
    if (coinResult === 'tails') {
        result.textContent = 'The coin landed on tails. You win!';
    } else {
        result.textContent = 'The coin landed on heads. You lose.';
    }
};

