$(document).ready(function(){
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
				$("#socialselector").append("<option class=socialselector value='facebook_page,"+userserviceid+"'>Send to Facebook: "+accname+"</option>")
			}
			else if (accounts == "twitter"){
				var screenname = client_services[object].screen_name;
				$("#socialselector").append("<option class=socialselector value='twitter,"+userserviceid+"'>Send to Twitter: "+screenname+"</option>")
			}
			else if (accounts == "google_plus_page"){
				$("#socialselector").append("<option class=socialselector value='google_plus_page,"+userserviceid+"'>Send to Google+</option>")
			}
			else if (accounts == "linked_in_page"){
				$("#socialselector").append("<option class=socialselector value='linked_in_page,"+userserviceid+"'>Send to LinkedIn</option>")
			}			
			}
	}
})
