$('.checkbox').change(function(){ 
                        var selectorstate = $('#socialselector').val()
                        var socialstate = selectorstate.split(",")

                                if(this.checked) {
                                  if (socialstate[0] == 'facebook_page') {
                                  var styles = {
                                  background : '#3b5998'
                                  };
                                } else if (socialstate[0] == 'twitter') {
                                  var styles = {
                                  background : '#95D7F9',
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

// $('#socialselector').change(function(){
//                         var selectorstate = $('#socialselector').val()
//                         var socialstate = selectorstate.split(",")
//                         var socialstate = socialstate[0]
//                         var elemento = $('.checkbox:checked')

//                         if (socialstate[0] == 'facebook_page') {
//                                   var styles = {
//                                   background : '#3b5998'
//                                   };
//                       } else if (socialstate[0] == 'twitter') {
//                                   var styles = {
//                                   background : '#95D7F9',
//                                   };
//                       };
//                       // for (object in elemento) {
//                         console.log(elemento);
//                       // }
//           // .parent('.ellybox').append("lol wtf");

//                       });