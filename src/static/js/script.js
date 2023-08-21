  const carouselContent = document.querySelector('.carousel-content');
  let currentIndex = 0;

  function slideCarousel() {
    currentIndex = (currentIndex + 1) % 3;
    carouselContent.style.transform = `translateX(-${currentIndex * 310}px)`;
  }

  setInterval(slideCarousel, 3000);