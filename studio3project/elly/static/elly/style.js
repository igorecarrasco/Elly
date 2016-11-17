$(document).ready(function() { 
	$('.checkbox').change(function(){ 
		if(this.checked) {
			var styles = {
      			background : '#95D7F9',
    //   			'-webkit-box-shadow': 'none',
				// '-moz-box-shadow': 'none',
				// 'box-shadow': 'none'
   				 };
        $(this).parent('.ellybox').css( styles );
    }
        else {
        var styles = {
      			background : 'white',
    //   			'-webkit-box-shadow': '1px 1px 4px 1px #bbb',
				// '-moz-box-shadow': '1px 1px 4px 1px #bbb',
				// 'box-shadow': '1px 1px 4px 1px #bbb'
   				 };
        $(this).parent('.ellybox').css( styles );
    }
    })
});

