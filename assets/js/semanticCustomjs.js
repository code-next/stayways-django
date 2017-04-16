$(document).ready(function(){

// menu
    $('.ui .item').on('click', function() {
        $('.ui .item').removeClass('active');
        $(this).addClass('active');
    });   

 $('#signup')
        .modal('hide');

    $('#sign').click(function () {
        $('#signup')
            .modal({
                blurring: true
            })
            .modal('show')
            .modal({ backdrop: 'static', keyboard: false });
    });

    $('#login')
        .modal('hide');

    $('#log').click(function () {
        $('#login')
            .modal({
                blurring: true
            })
            .modal('show')
            .modal({ backdrop: 'static', keyboard: false });
    });


// rating
    $('.ui.rating')
  .rating({
    initialRating: 0,
    maxRating: 5
  }).rating('disable');

  $('.form .rating').rating('enable');
// sticky card
  $('.ui.sticky')
  .sticky({
    context: '#roomOverview',
    offset       : 100,
    bottomOffset : 100,
    pushing: true
  });


});