const carousel = document.querySelector('.carousel');
  const images = carousel.querySelectorAll('img');
  const totalImages = images.length;

  let currentIndex = 0;

  function showImage(index) {
    images.forEach((image, i) => {
      if (i === index) {
        image.style.display = 'block';
      } else {
        image.style.display = 'none';
      }
    });
  }

  function showNextImage() {
    currentIndex = (currentIndex + 1) % totalImages;
    showImage(currentIndex);
  }

  // Initial image display
  showImage(currentIndex);

  // Auto-slide every 3 seconds
  let interval = setInterval(showNextImage, 3000);

  // Stop auto-slide when hovering over the carousel
  carousel.addEventListener('mouseenter', () => {
    clearInterval(interval);
  });

  // Resume auto-slide when not hovering over the carousel
  carousel.addEventListener('mouseleave', () => {
    interval = setInterval(showNextImage, 3000);
  });