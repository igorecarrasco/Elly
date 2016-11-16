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

var linkItems = $(".hits").length

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

$('.pubdate').each(function(linkItems){
	var $elemento = $(this);
	$.post({
		headers: { "X-CSRFToken": getCookie("csrftoken") },
		url: 'pubdate',
		data: $elemento.attr('href'),
		dataType: 'text',
		success: hitsCallback,
	});
	function hitsCallback(data){
		$elemento.append(data)
		console.log()
	}
});