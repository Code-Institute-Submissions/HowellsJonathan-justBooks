$(document).ready(function(){
    $('.sidenav').sidenav({edge: "left"});
    $('.datepicker').datepicker();
    M.updateTextFields();
    $('select').formSelect();
    $('.carousel').carousel();
    $('.tabs').tabs();
    $(".dropdown-trigger").dropdown({
      constrainWidth: false,
      hover: true,
    });
  }); 

  $('.carousel.carousel-slider').carousel({
    fullWidth: true
  });

