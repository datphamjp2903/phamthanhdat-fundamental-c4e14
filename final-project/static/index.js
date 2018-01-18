$(document).ready(function() {
  $('.district_list a').hide();
  $("#dropdownHN").click(function(event) {
    $('.district_list a').hide();
    $('.district_list a').filter(".hn-district").show();
  });

  $("#dropdownHCM").click(function(event) {
    $('.district_list a').hide();
    $('.district_list a').filter(".hcm-district").show();
  });

  $("#dropdownDN").click(function(event) {
    $('.district_list a').hide();
    $('.district_list a').filter(".dn-district").show();
  });
});


// $(document).ready(function() {
//   $("#dropdownHN").click(function(event) {
//     disList = "";
//     for (var i = 0; i < HNdistricts.length; i++) {
//       disList += '<a class="dropdown-item district" href="#">' + HNdistricts[i] + '</a>';
//     };
//     $(".district_list").replaceWith('<div class="district_list">' + disList + '</div>');
//   });
//
//   $("#dropdownDN").click(function(event) {
//     disList = "";
//     for (var i = 0; i < DNdistricts.length; i++) {
//       disList += '<a class="dropdown-item district" href="#">' + DNdistricts[i] + '</a>';
//     };
//     $(".district_list").replaceWith('<div class="district_list">' + disList + '</div>');
//   });
//
//   $("#dropdownHCM").click(function(event) {
//     disList = "";
//     for (var i = 0; i < HCMdistricts.length; i++) {
//       disList += '<a class="dropdown-item district" href="#">' + HCMdistricts[i] + '</a>';
//     };
//     $(".district_list").replaceWith('<div class="district_list">' + disList + '</div>');
//   });
// });
//

//
//
// $(document).ready(function() {
//   $("#dropdownDN").click(function(event) {
//     disList = "";
//     for (var i = 0; i < DNdistricts.length; i++) {
//       disList += '<a class="dropdown-item district" href="#">' + DNdistricts[i] + '</a>';
//     };
//     $(disList).replaceAll('.district')
//   });
// });
