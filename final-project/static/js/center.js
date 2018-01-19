if (wScroll > $('.dong-san-pham').offset().top - ($(window).height() / 1.3)) {
    $('.dong-san-pham figure').each(function(i) {
      setTimeout(function() {
        $('.dong-san-pham figure').eq(i).addClass('dang-chay');
      }, 200 * (i + 1));
    })
  }
})
