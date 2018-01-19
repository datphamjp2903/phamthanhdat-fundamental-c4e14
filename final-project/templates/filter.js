  $(document).ready(function() {
    $("button").click(function(event) {
      var city = $('#city option:selected').val();
      var section = $('#section option:selected').val();
      var a = $('a.center');

      console.log(city, section);

      for (i = 0; i < a.length; i++) {
        var centerSection = a[i].getElementsByTagName('p')[1].textContent;
        var centerCity = a[i].getElementsByTagName('p')[2].textContent;
        if (centerSection == section && centerCity == city || section == '' && centerCity == city || centerSection == section && city == '') {
          a.eq(i).show();
        }  else {
          a.eq(i).hide();
      };
    };
  });
});
