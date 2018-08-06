var modal = document.getElementById('myModal');
var images = document.getElementsByClassName('project-image');
var modalImage = document.getElementById('modal-image');
var captionText = document.getElementById('caption');

let img;
for (let i = 0; i < images.length; i++) {
	img = images[i];
	img.onclick = function() {
		modal.style.display = "block";
		modalImage.src = this.src;
	}
}

var span = document.getElementsByClassName("close")[0]

span.onclick = function() {
	modal.style.display = "none";
}