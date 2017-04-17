$(function(){


  $("#indexSearch").autocomplete({
    source: "/ajax/get_city/",
    minLength: 2,
  });

$.ajaxSetup({ headers: { 'csrfmiddlewaretoken' :$("input[name=csrfmiddlewaretoken]").val() } });

// review add post

    $('#reviewfinish').click(function(){

      $('#reviewform').addClass('loading');
      $.ajax({
        type: "POST",
        url:"/addreview/",
        data:{
          'rating':$('#rvRating').rating('get rating'),
          'roomId':$('#room_id').val(),
          'review':$('#reviewText').val(),
          'csrfmiddlewaretoken' :$("input[name=csrfmiddlewaretoken]").val()
        },
        success:reviewAddSuccess,
        dataType:'html'
      });
  });

});


function reviewAddSuccess(data,textStatus,jqXHR) {
  
  
  $('#reviewCollection').append(data);
  $('#reviewform').hide();
  $('#reviewform').removeClass('loading');
  $('#rvRating').rating({initialRating: 0,maxRating: 4});
  $('#reviewText').val("");
  
}

