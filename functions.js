function draw(x, y, dx, dy){
	var c = document.getElementById("myCanvas");
	var ctx = c.getContext("2d");
	ctx.strokeStyle = "#FF0000";
	ctx.beginPath();
	ctx.arc(x, y, 50, 0, 2 * Math.PI);
	ctx.stroke();
	ctx.beginPath();
	ctx.arc(x, y, 100, 0, 2 * Math.PI);
	ctx.stroke();
	setTimeout(draw, 300, x+dx, y+dy, dx+1, dy+1);
}
