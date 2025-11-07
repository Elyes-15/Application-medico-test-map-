document.addEventListener('DOMContentLoaded', function () {
  const next = document.querySelector('.next');
  const prev = document.querySelector('.prev');
  const slide = document.querySelector('.slide');

  if (!slide) return;

  next.addEventListener('click', () => {
    const items = document.querySelectorAll('.item');
    slide.appendChild(items[0]);
  });

  prev.addEventListener('click', () => {
    const items = document.querySelectorAll('.item');
    slide.prepend(items[items.length - 1]);
  });
});
