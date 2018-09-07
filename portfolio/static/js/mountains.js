var canvas = document.querySelector('canvas');
var c = canvas.getContext('2d');

canvas.width = innerWidth;
canvas.height = innerHeight;

// If the screen width is less than 375px -- iPhone X -- 
// then don't run the event listener.
// When viewing the canvas on a mobile browser there is jitter due to resizing
// but it is not present on a laptop screen. 
// There might be jitter on a tablet screen.
if(screen.width > 375) {
    addEventListener('resize', () => {
        canvas.width = innerWidth;
        canvas.height = innerHeight;
        init();
    });
};


var colors = [
    '#732F67',
    '#612B3C',
    '#610035'
];

function randomIntFromRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function background() {
    let gradient = c.createLinearGradient(0, 0, 0, canvas.height);
    gradient.addColorStop(0, '#424FCC');
    gradient.addColorStop(0.6, '#FF6A32');
    c.fillStyle = gradient;
    c.fillRect(0, 0, canvas.width, canvas.height);
    c.beginPath();
}


function ground() {
    c.fill();
    c.fillStyle = '#913A33';
    c.fillRect(0, canvas.height/1.2, canvas.width, canvas.height);
}

function Mountain(x, y, color, peaks) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.peaks = peaks;
    this.speed = -1;
    this.dx = 0;
    this.dy = 0;

    this.update = () => {
        // this.dx = 1;
        // this.x += this.dx;
        this.draw();
    };

    this.draw = () => {
        // Mountains
        c.beginPath();
        c.moveTo(this.x, this.y);
        for (var i = 0; i < peaks; i++) {
            this.dx = (Math.random() * canvas.width/50) + 220;
            this.dy = (Math.random() * canvas.height/4);
            this.x += this.dx;
            this.y += this.dy;
            if(this.y < 0 || this.y > canvas.height) {
                this.y = this.y - 2 * this.dy;
            } else if(this.x > canvas.width) {
                this.x = canvas.width;
            }
            c.lineTo(this.x, this.y);
        }
        c.lineTo(canvas.width, canvas.height);
        c.lineTo(0, canvas.height);
        c.fillStyle = this.color;
        c.fill();        
    };
}


let mountains;
function init() {
    background();
    
    mountains = [];
    for(var i = 0; i < colors.length; i++) {
        const y = randomIntFromRange(500, canvas.height/1.2 + 100);
        const x = randomIntFromRange(-500, canvas.height);
        const peaks = randomIntFromRange(50, 100);
        mountains.push(new Mountain(x, y, colors[i], peaks));
    }
    for(var j = 0; j < mountains.length; j++) {
        mountains[j].update();
    }
    ground();
}

function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0, 0, canvas.width, canvas.height);
    mountains.forEach(mountain => {
        background();
        mountain.update();
        ground();
    });

}

init();
// animate();


