$(document).ready(function(){

// menu
    $('.ui .item').on('click', function() {
        $('.ui .item').removeClass('active');
        $(this).addClass('active');
    });   

// model
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

    $('.special.cards .image').dimmer({
        on: 'hover'
    });

// rating
    $('.ui.rating')
  .rating({
    initialRating: 0,
    maxRating: 5
  }).rating('disable');


});