(function() {

    $('#tohash').on('click', function() {
        $('html, body').animate({ scrollTop: $(this.hash).offset().top - 5 }, 1000);
        return false;
    });

   
      


  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });

//   $('.ui.rating')
//         .rating('setting', 'onRate', function(value) {
//       // your amazing code here
//   });

$('.ui.rating')
  .rating({
    initialRating: 3,
    maxRating: 5
  })
;
   
})(jQuery)
