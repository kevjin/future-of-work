const canvas = document.getElementById("app")
canvas.setAttribute("width", 1000)
canvas.setAttribute("height", 1000)
const context = canvas.getContext('2d');
const canvasId = context.getImageData(0, 0, 1000, 1000);
const d = canvasId.data;
let unsavedLines = []

// When true, moving the mouse draws on the canvas
let isDrawing = false;

let x = 0;
let y = 0;
canvas.addEventListener('mousedown', e => {
  isDrawing = true;
  x = e.offsetX;
  y = e.offsetY;
});

canvas.addEventListener('mousemove', e => {
  if (isDrawing === true) {
    drawLine(context, x, y, e.offsetX, e.offsetY);
    x = e.offsetX;
    y = e.offsetY;
  }
});

window.addEventListener('mouseup', e => {
  if (isDrawing === true) {
    x = 0;
    y = 0;
    isDrawing = false;
    pushLines()
  }
});

function drawLine(context, x1, y1, x2, y2) {
  context.beginPath();
  context.strokeStyle = 'black';
  context.lineWidth = 3;
  context.moveTo(x1, y1);
  context.lineTo(x2, y2);
  context.stroke();
  context.closePath();
  unsavedLines.push([x1, y1, x2, y2])
}

function pushLines() {
  console.log("push lines" + unsavedLines.length)
  console.log(unsavedLines)

  fetch("http://localhost:5000/new_strokes", {
    headers: {
      'Content-Type': 'application/json'
    },
    method : "POST",
    body : JSON.stringify({
        strokes: unsavedLines
    })
  }).then(
      response => response.text()
  ).then(
      html => console.log(html)
  );

  unsavedLines = []
}

function fetchRecentLines() {
  fetch("http://localhost:5000/new_strokes", {
    headers: {
      'Content-Type': 'application/json'
    },
    method : "GET"
  }).then(
      response => response.json()
  ).then(
      respData => populateLines(respData["strokes"])
  );
}

setInterval(fetchRecentLines, 1000)

function populateLines(lines) {
  lines.forEach((line) => {
    drawLine(context, ...line)
  })
}
