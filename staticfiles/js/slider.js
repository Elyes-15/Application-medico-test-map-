document.addEventListener('DOMContentLoaded', function () {
  const slide = document.querySelector('.slide');
  const items = document.querySelectorAll('.item');
  const total = items.length;
  let index = 0;

  if (!slide) return;
  const goNext = () => {
    index = (index + 1) % total;
    slide.style.transform = `translateX(-${index * 100}%)`;
  };

  const goPrev = () => {
    index = (index - 1 + total) % total;
    slide.style.transform = `translateX(-${index * 100}%)`;
  };

  const nextBtn = document.querySelector('.next');
  const prevBtn = document.querySelector('.prev');
  if (nextBtn) nextBtn.addEventListener('click', goNext);
  if (prevBtn) prevBtn.addEventListener('click', goPrev);

  setInterval(goNext, 3000);
});
