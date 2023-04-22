const textElement = document.querySelector('.text');

textElement.addEventListener('click', () => {
  const original = textElement.getAttribute('data-original');
  const leet = textElement.getAttribute('data-leet');

  if (textElement.textContent === original) {
    textElement.style.transform = 'rotateY(360deg)';
    setTimeout(() => {
      textElement.textContent = leet;
      textElement.style.transform = 'rotateY(360deg)';
    }, 500);
  } else {
    textElement.style.transform = 'rotateY(360deg)';
    setTimeout(() => {
      textElement.textContent = original;
      textElement.style.transform = 'rotateY(360deg)';
    }, 500);
  }
});
