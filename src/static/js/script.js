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

   // Function to read and display the selected image
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#uploaded-image').attr('src', e.target.result);
                $('.file-upload-content').show();
                $('.image-upload-wrap').hide();
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    // Function to remove the uploaded image
    function removeUpload() {
        $('#uploaded-image').attr('src', '/Themes/Zoommer/assets/images/noun_User.svg');
        $('.file-upload-input').val(null);
        $('.file-upload-content').hide();
        $('.image-upload-wrap').show();
    }