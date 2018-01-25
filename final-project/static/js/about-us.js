$(document).ready(function(){
  console.log('buzz');
  $("#about-us-button").click(function(event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: $("#about-us").offset().top
    }, 2000);
  });
})
