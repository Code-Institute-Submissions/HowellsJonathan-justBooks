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

import Swiper from "swiper/bundle";
import "swiper/swiper-bundle.css";

const swiper = new Swiper(".swiper-container", {
  direction: "horizontal",
  loop: true,

  // Adds arrows for the user to scroll through if they don't want to swipe
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  }

  // Autoplay the carousel / swiper 
  autoplay: {
    delay: 5000,
  }

  // Disable preloading of all images to speed up load times
  preloadImages: false,

  lazy: true,
});
