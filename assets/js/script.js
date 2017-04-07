(function() {

    $('#tohash').on('click', function() {
        $('html, body').animate({ scrollTop: $(this.hash).offset().top - 5 }, 1000);
        return false;
    });

      $('#signup')
            .modal('hide');

        $('#sign').click(function() {
            $('#signup')
                .modal({
                    blurring: true
                })
                .modal('show')
                .modal({
                    backdrop: 'static',
                    keyboard: false
                });
        });

        $('#login')
            .modal('hide');

        $('#log').click(function() {
            $('#login')
                .modal({
                    blurring: true
                })
                .modal('show')
                .modal({
                    backdrop: 'static',
                    keyboard: false
                });
        });

      


        $('.special.cards .image').dimmer({
            on: 'hover'
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
        
})(jQuery)
