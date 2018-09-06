function responsiveMenu(x) {
	var menuClass = document.getElementById("responsive-menu");
	menuClass.classList.toggle("menu-on");
}

$(document).ready(function(){
	var contactForm = $('#contact-form');
	contactForm.submit(function(event){
		event.preventDefault();
		var name = $('#id_full_name');
		var email = $('#id_email');
		var subject = $('#id_subject');
		var message = $('#id_message');
	    console.log(name.val(), email.val(), subject.val(), message.val())

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
	    		alert('Thank you for the email.')
	    		if (data.success) {
			        name.val('')
			        email.val('');
			        subject.val('');
			        message.val('Thank you. Your request has been submitted. We will be contacting you shortly.');
			    }
		    }
		});
	});


	$('main-carousel').flickity({		
	});
});

