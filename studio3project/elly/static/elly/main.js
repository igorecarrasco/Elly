// get CSRFCookie for post requests
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$(document).ready(function(){
var linkItems = $(".hits").length
	$('#startoptimization').AnyTime_picker( "field1",
		{ format: "%W, %M %D in the Year %z %E", firstDOW: 1 } );

	$('#scheduletime').AnyTime_picker( "field1",
		{ format: "%W, %M %D in the Year %z %E", firstDOW: 1 } );

	$('.reveal-if-active').hide();
	$('.reveal-if-active2').hide();

	$("input:radio").change(function(){
	if ($(".optimizefield").is(":not(:checked)")) {
		$('.reveal-if-active').hide();
		$('.mustsendbox').hide();
	} 

	if ($(".optimizefield").is(":checked")) {
		$('.reveal-if-active').show();
		$('.mustsendbox').show();

	}

	if ($(".schedulefield").is(":not(:checked)")) {
		$('.reveal-if-active2').hide();
	} 

	if ($(".schedulefield").is(":checked")) {
		$('.reveal-if-active2').show();
	}
});

// Make articles boxes change colors when checked, reflecting which social platform user selected
$('.checkbox').change(function(){ 
	var selectorstate = $('#socialselector').val()
	var socialstate = selectorstate.split(",")

	if(this.checked) {
		if (socialstate[0] == 'facebook_page') {
		var styles = {
		background : '#6d84b4',
		'-webkit-box-shadow': 'none',
		'-moz-box-shadow': 'none',
		'box-shadow': 'none', 
			};
	} else if (socialstate[0] == 'twitter') {
		var styles = {
		background : '#95D7F9',
		'-webkit-box-shadow': 'none',
		'-moz-box-shadow': 'none',
		'box-shadow': 'none', 	
	};
	}
	else if (socialstate[0] == 'linked_in_page') {
		var styles = {
		background : '#0077b5',
		'-webkit-box-shadow': 'none',
		'-moz-box-shadow': 'none',
		'box-shadow': 'none', 
	};
	}
	else if (socialstate[0] == 'google_plus_page') {
		var styles = {
		background : '#d34836',
		'-webkit-box-shadow': 'none',
		'-moz-box-shadow': 'none',
		'box-shadow': 'none', 
	};
	}
	$(this).parent('.ellybox').css( styles );
	}
	else {
		var styles = {
		background : 'white',
		'-webkit-box-shadow': '2px 2px 1px -1px rgba(0,0,0,0.33)',
		'-moz-box-shadow': '2px 2px 1px -1px rgba(0,0,0,0.33)',
		'box-shadow': '2px 2px 1px -1px rgba(0,0,0,0.33)',
	};
	$(this).parent('.ellybox').css( styles );
	}
});

// make radio and select boxes that control posting appear or disappear according to platform user selected
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
} 

else if (socialstate[0] == 'twitter') {
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
	}
}

elemento.parent('.ellybox').css( styles );

});
});

$(window).one('load',(function(){
	$.post({
	headers: { "X-CSRFToken": getCookie("csrftoken") },
	url:'socialflow',
	success: socialCallback,
});
	function socialCallback(data){
		var account = jQuery.parseJSON(data);
		var client_services = account.data.client_services;
		for (object in client_services) {
			var accounts = client_services[object].account_type;
			var userserviceid = client_services[object].service_user_id;
			if (accounts == "facebook_page") {
				var accname = client_services[object].name
				$("#socialselector").append("<option class=socialselector value='facebook_page,"+userserviceid+"'>Facebook: "+accname+"</option>")
				$( ".optimizefield" ).hide();
				$( ".mustsendbox").hide();
			}
			else if (accounts == "twitter"){
				var screenname = client_services[object].screen_name;
				$("#socialselector").append("<option class=socialselector value='twitter,"+userserviceid+"'>Twitter: "+screenname+"</option>")
			}
			else if (accounts == "google_plus_page"){
				$("#socialselector").append("<option class=socialselector value='google_plus_page,"+userserviceid+"'>Google+</option>")
			}
			else if (accounts == "linked_in_page"){
				var accname = client_services[object].name
				$("#socialselector").append("<option class=socialselector value='linked_in_page,"+userserviceid+"'>LinkedIn: "+accname+"</option>")
			}			
		}
}

// make post request to get Page Views from parse.ly
	$('.hits').each(function(linkItems){
		var $elemento = $(this);
		$.post({
			headers: { "X-CSRFToken": getCookie("csrftoken") },
			url: 'hits',
			data: $elemento.attr('href'),
			dataType: 'text',
			success: hitsCallback,
		});
		function hitsCallback(data){
			$elemento.append(data)
		}
	});

// make post request to get Facebook Likes from parse.ly
	$('.likes').each(function(linkItems){
		var $elemento = $(this);
		$.post({
			headers: { "X-CSRFToken": getCookie("csrftoken") },
			url: 'likes',
			data: $elemento.attr('href'),
			dataType: 'text',
			success: hitsCallback,
		});
		function hitsCallback(data){
			$elemento.append(data)
		}
	});

// make post request to get Twitter interactions from parse.ly
	$('.rts').each(function(linkItems){
		var $elemento = $(this);
		$.post({
			headers: { "X-CSRFToken": getCookie("csrftoken") },
			url: 'rts',
			data: $elemento.attr('href'),
			dataType: 'text',
			success: hitsCallback,
		});
		function hitsCallback(data){
			$elemento.append(data)
		}
	});
}));
