$(document).ready(function(){
    $('.sidenav').sidenav({edge: "left"});
    $('.datepicker').datepicker();
    M.updateTextFields();
    $('select').formSelect();
    $('.carousel').carousel();
    $('.tabs').tabs();
    $(".dropdown-trigger").dropdown();
  }); 

  $('.carousel.carousel-slider').carousel({
    fullWidth: true
  });

