function responsiveMenu(x) {
	var menuClass = document.getElementById("responsive-menu");
	menuClass.classList.toggle("menu-on");
}

// Contact form

$(document).ready(function(){
	var contactForm = $('#contact-form');
	contactForm.submit(function(event){
		event.preventDefault();
		var name = $('#id_full_name');
		var email = $('#id_email');
		var subject = $('#id_subject');
		var message = $('#id_message');

	    $.ajax({
	    	type: 'POST',
	    	url: '/contact-submit/',
	    	data: {
	    		'full_name': name.val(),
	    		'email': email.val(),
	    		'subject': subject.val(),
	    		'message': message.val(),
	    		'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
	    	},
	    	dataType: 'json',
	    	success:function(data){
	    		if (data.success) {
			        name.val('')
			        email.val('');
			        subject.val('');
			        message.val('Thank you. Your request has been submitted. I will be contacting you shortly.');
			    }
		    }
		});
	});
});

