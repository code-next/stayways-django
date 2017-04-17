(function($) {

//fixed nav
  var slideHeight = $(window).height();

  $(window).on('scroll', function(){
      if( $(window).scrollTop()>slideHeight ){
        $('.pointing.menu').addClass('fixed');
      } else {
        $('.pointing.menu').removeClass('fixed');
      }
    });
//pushing active nav
$(window).scroll(function(event) {
		Scroll();
	});

function Scroll() {
		var contentTop      =   [];
		var contentBottom   =   [];
		var winTop      =   $(window).scrollTop();
		var rangeTop    =   200;
		var rangeBottom =   500;
		$('.pointing.menu').find('.item').each(function(){
			contentTop.push( $( $(this).attr('href') ).offset().top);
			contentBottom.push( $( $(this).attr('href') ).offset().top + $( $(this).attr('href') ).height() );
		})
		$.each( contentTop, function(i){
			if ( winTop > contentTop[i] - rangeTop ){
				$('.pointing.menu .item')
				.removeClass('active')
				.eq(i).addClass('active');			
			}
		})
	};



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



// wow animation
new WOW().init();



})(jQuery)

// reveiw adder

$("#reviewformview").click(function(){
    $("#reviewform").show();
});


	//room form view
$("#hostRoomViewer").click(function(){
    $("#roomHostForm").show();
});

//tooltips

$('#hostRoomUpload').qtip({ // Grab some elements to apply the tooltip to
    content: {
        text: 'you can select multiple files on here'
    },
    position: {
        my: 'top left',  // Position my top left...
        at: 'bottom right', // at the bottom right of...
        target: $('#hostRoomUpload') // my target
    }
})

