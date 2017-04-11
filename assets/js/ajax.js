$(function(){


  $("#indexSearch").autocomplete({
    source: "/ajax/get_city/",
    minLength: 2,
  });


$.ajaxSetup({ headers: { 'csrfmiddlewaretoken' :$("input[name=csrfmiddlewaretoken]").val() } });
});

