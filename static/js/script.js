$(document).ready(function(){
    $('.sidenav').sidenav({edge: "left"});
    $('.datepicker').datepicker();
    M.updateTextFields();
    $('select').formSelect();
    $('.carousel').carousel();
  }); 

  $('.carousel.carousel-slider').carousel({
    fullWidth: true
  });


var swiper = new Swiper(".swiper-container", {
  direction: "horizontal",
  loop: true,

  // Adds arrows for the user to scroll through if they don't want to swipe
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  // Autoplay the carousel / swiper 
  autoplay: {
    delay: 5000,
  },

  // Disable preloading of all images to speed up load times
  preloadImages: false,

  lazy: true,

  slidesPerView: 1,
  spaceBetween: 10,

  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 50,
    },
  },
});
