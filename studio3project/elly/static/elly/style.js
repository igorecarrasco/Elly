
$('.checkbox').change(function(){ 
                        var selectorstate = $('#socialselector').val()
                        var socialstate = selectorstate.split(",")

                                if(this.checked) {
                                  if (socialstate[0] == 'facebook_page') {
                                  var styles = {
                                  background : '#6d84b4'
                                  };
                                } else if (socialstate[0] == 'twitter') {
                                  var styles = {
                                  background : '#95D7F9',
                                  };
                                }
                                  else if (socialstate[0] == 'linked_in_page') {
                                  var styles = {
                                  background : '#0077b5',
                                  };
                                }
                                  else if (socialstate[0] == 'google_plus_page') {
                                  var styles = {
                                  background : '#d34836',
                                  };
                                }
                     $(this).parent('.ellybox').css( styles );
                }
                else {
                      var styles = {
                      background : 'white',
                      };
                      $(this).parent('.ellybox').css( styles );
                }
});
$('#socialselector').change(function(){
                        var selectorstate = $('#socialselector').val()
                        var socialstate = selectorstate.split(",")
                        var elemento = $('.checkbox:checked')

                        if (socialstate[0] == 'facebook_page') {
                                  var styles = {
                                  background : '#6d84b4'
                                  };
                                  $( ".optimizefield" ).hide();
                                  $( ".reveal-if-active").hide();

                      } else if (socialstate[0] == 'twitter') {
                                  var styles = {
                                  background : '#95D7F9',
                                  };
                                  $( ".optimizefield" ).show();
                                 if ($(".optimizefield").is(":not(:checked)")){
                                    $('.reveal-if-active').hide();
                                    } 
                                    if ($(".optimizefield").is(":checked")) {
                                    $('.reveal-if-active').show();
                                  }
                      }
                        else if (socialstate[0] == 'linked_in_page') {
                                  var styles = {
                                  background : '#0077b5',
                                  };
                                  $( ".optimizefield" ).show();
                                    if ($(".optimizefield").is(":not(:checked)")){
                                    $('.reveal-if-active').hide();
                                    } 
                                    if ($(".optimizefield").is(":checked")) {
                                    $('.reveal-if-active').show();
                                  }
                      }
                        else if (socialstate[0] == 'google_plus_page') {
                                  var styles = {
                                  background : '#d34836',
                                  };
                                  $( ".optimizefield" ).show();  
                                  if ($(".optimizefield").is(":not(:checked)")){
                                    $('.reveal-if-active').hide();
                                    } 
                                    if ($(".optimizefield").is(":checked")) {
                                    $('.reveal-if-active').show();
                      }}
                      elemento.parent('.ellybox').css( styles );
});
$(document).ready(function(){
  $('#startoptimization').AnyTime_picker( "field1",
    { format: "%W, %M %D in the Year %z %E", firstDOW: 1 } );
    $('#scheduletime').AnyTime_picker( "field1",
    { format: "%W, %M %D in the Year %z %E", firstDOW: 1 } );
});
$(document).ready(function(){
  $('.reveal-if-active').hide();
  $('.reveal-if-active2').hide();
});
$("input:radio").change(function(){
  if ($(".optimizefield").is(":not(:checked)")){
      $('.reveal-if-active').hide();
      } 
      if ($(".optimizefield").is(":checked")) {
      $('.reveal-if-active').show();
    }
      if ($(".schedulefield").is(":not(:checked)")){
      $('.reveal-if-active2').hide();
      } 
      if ($(".schedulefield").is(":checked")) {
      $('.reveal-if-active2').show();
    }
  });

