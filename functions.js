function draw(x, y, dx, dy,color){
	var c = document.getElementById("myCanvas");
	var ctx = c.getContext("2d");
	ctx.strokeStyle = color;
	ctx.beginPath();
	ctx.arc(x, y, 50, 0, 2 * Math.PI);
	ctx.stroke();
	ctx.beginPath();
	ctx.arc(x, y, 100, 0, 2 * Math.PI);
	ctx.stroke();
	setTimeout(draw, 300, x+dx, y+dy, dx+1, dy+1,color);
}

function random1(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
function random(min, max) {
  return (Math.random() * (max - min + 1) ) + min;
}

function end(color){
	setInterval(function(){draw(random(1,200),random(1,100),random(0,20),random(0,20),color);}, 150);
}
/*
function link(){
	var canvas = document.getElementById("myCanvas");
	var ctx = canvas.getContext("2d");
	ctx.fillStyle = "white";
	ctx.fillRect(0, 0, canvas.width, canvas.height);
	console.log("linkk")
}


function expand(x){
	a = document.getElementById(x);
	a.width=a.width+100;
	a.height=a.height+100;
	console.log("2")
}

function large(x){
	console.log("1")
	a = document.getElementById(x);
	console.log(a)
	// setTimeout(console.log("timeout"), 1000);
	while (a.width<1000 || a.height<1000){
		console.log(a.width);
		// setTimeout(console.log("timeout"), 1000);
		setTimeout(expand,1000,x);
		console.log(a.width)

	}
}
*/