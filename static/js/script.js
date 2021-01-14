$(document).ready(function(){
    $('.sidenav').sidenav({edge: "left"});
    $('.datepicker').datepicker();
    M.updateTextFields();
    $('select').formSelect();
    $('.carousel').carousel();
    $('.tabs').tabs();
    $(".dropdown-trigger").dropdown({
      constrainWidth: false,
    });
    $('.modal').modal();
    $("input#isbn, textarea#synopsis").characterCounter();
  }); 

  $('.carousel.carousel-slider').carousel({
    fullWidth: true
  });

