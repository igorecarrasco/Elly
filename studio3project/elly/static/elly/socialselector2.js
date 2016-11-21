$(window).on('load',(function(){
                        var selectorstate = $('#socialselector').val()
                        var socialstate = selectorstate.split(",");
                        if (socialstate[0] == 'facebook_page') {
                                                          $( ".optimizefield" ).hide();
                                              } else if (socialstate[0] == 'twitter','google_plus_page','linked_in_page') {
                                                          $( ".optimizefield" ).show();
                                              }
}));