// Canvas context
canvas = document.getElementById('canvas2');
var c2 = canvas.getContext('2d');

// Set canvas window size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var maxRadius = 50;

// Mouse
var mouse = {
	x: undefined,
	y: undefined
}

// Colors
var colorArray = [
	'#69FFF1',
	'#63D471',
	'#63A46C',
	'#6A7152',
	'#233329'
]

// Mouse position
window.addEventListener('mousemove', 
	function(event) {
		mouse.x = event.x
		mouse.y = event.y
	})

// Resize the canvas according to viewport
window.addEventListener('resize', function(){
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;

	init();
});

// Circle object
function Circle(x, y, dx, dy, radius) {
	this.x = x;
	this.y = y;
	this.dx = dx;
	this.dy = dy;
	this.radius = radius;
	this.minRadius = radius;
	this.color = colorArray[Math.floor(Math.random() * colorArray.length)];

	// Draw the circles
	this.draw1 = function() {
		c2.beginPath();
		c2.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
		c2.fillStyle = this.color;
		c2.fill();
	}

	// Updats the circles position
	this.update1 = function() {
		if (this.x + this.radius > innerWidth || this.x - this.radius < 0) {
			this.dx = -this.dx
		}

		if (this.y + this.radius > innerHeight || this.y - this.radius < 0) {
			this.dy = -this.dy
		}

		this.x += this.dx;
		this.y += this.dy;

		// interactivity
		if (mouse.x - this.x < 50 && mouse.x - this.x > -50 
			&& mouse.y - this.y < 50  && mouse.y - this.y > -50) {
			if (this.radius < maxRadius) {				
				this.radius += 1;
			}
		} else if (this.radius > this.minRadius) {
			this.radius -= 1;
		}

		this.draw1();
	}

}

// Initialize the circles
var circleArray = [];
function init1() {
	circleArray = [];
	for (var i = 0; i < 750; i++) {
		var radius = Math.random() * 3 + 1;
		var x = Math.random() * (innerWidth - radius * 2) + radius;
		var y = Math.random() * (innerHeight - radius * 2) + radius;
		var dx = (Math.random() - 0.5);
		var dy = (Math.random() - 0.5);		
		circleArray.push(new Circle(x, y, dx, dy, radius));
	}
}

// Engine that gives the cirlces life
function animate1() {
	requestAnimationFrame(animate);
	c2.clearRect(0, 0, innerWidth, innerHeight);

	for (var i = 0; i < circleArray.length; i++) {
		circleArray[i].update1();
	}

}

init1();
animate1()
