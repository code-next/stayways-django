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

// filtering room listview class=""
$('.filterCheck:checkbox').change(function(){

  params={
    type:"POST",
    url:"/ajax/roomfilter/",
    data:{},
    success:filterSuccess,
    dataType:'html'
  };

  content={}
  content.roomlistCity=$('#roomlistCity').val();
  if($('#roomlistPrivate').prop("checked") == true){content.roomlistPrivate=$('#roomlistPrivate').val();}
  if($('#roomlistShared').prop("checked") == true){content.roomlistShared=$('#roomlistShared').val();}
  if($('#roomlistHostel').prop("checked") == true){content.roomlistHostel=$('#roomlistHostel').val();}
  if($('#roomlistEntire').prop("checked") == true){content.roomlistEntire=$('#roomlistEntire').val();}
  if($('#roomlistWifi').prop("checked") == true){content.roomlistWifi=$('#roomlistWifi').val();}
  if($('#roomlistPets').prop("checked") == true){content.roomlistPets=$('#roomlistPets').val();}
  if($('#roomlistAc').prop("checked") == true){content.roomlistAc=$('#roomlistAc').val();}
  if($('#roomlistFurnitured').prop("checked") == true){content.roomlistFurnitured=$('#roomlistFurnitured').val();}
  if($('#roomlistKitchen').prop("checked") == true){content.roomlistKitchen=$('#roomlistKitchen').val();}
  content.csrfmiddlewaretoken=$("input[name=csrfmiddlewaretoken]").val();
  params.data=content;

  $.ajax(params);

    // $.ajax({
    //   type: "POST",
    //   url:"/ajax/roomfilter/",
    //   data:{
        
    //     'roomlistCity':$('#roomlistCity').val(),
    //     'roomlistPrivate':$('#roomlistPrivate').val(),
    //     'roomlistShared':$('#roomlistShared').val(),
    //     'roomlistHostel':$('#roomlistHostel').val(),
    //     'roomlistEntire':$('#roomlistEntire').val(),
    //     'roomlistWifi':$('#roomlistWifi').val(),
    //     'roomlistPets':$('#roomlistPets').val(),
    //     'roomlistAc':$('#roomlistAc').val(),
    //     'roomlistFurnitured':$('#roomlistFurnitured').val(),
    //     'roomlistKitchen':$('#roomlistKitchen').val(),
    //     'csrfmiddlewaretoken' :$("input[name=csrfmiddlewaretoken]").val()
    //   },
    //   success:filterSuccess,
    //   dataType:'html'
    // });
});


});

//review adding success
function reviewAddSuccess(data,textStatus,jqXHR) {  
  $('#reviewCollection').append(data);
  $('#reviewform').hide();
  $('#reviewform').removeClass('loading');
  $('#rvRating').rating({initialRating: 0,maxRating: 4});
  $('#reviewText').val(""); 
}

//room filtering success
function filterSuccess(data,textStatus,jqXHR) {
  $('#columns').html(data);
}