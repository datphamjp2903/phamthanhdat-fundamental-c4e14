$(document).ready(function() {
  $(".flex-column").hide();
  $("button").click(function(event) {
    var city = $('#city').val();
    var section = $('#section').val();
    console.log(city + section);
  });
});
