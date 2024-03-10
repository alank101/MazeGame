// Fetch the maze data from the server
fetch('/maze_data')
    .then(response => response.json())
    .then(data => {
        // Once the data is received, call the renderMaze function with the received data
        renderMaze(data);
    })
    .catch(error => {
        // Handle errors
        console.error('Error fetching maze data:', error);
    });

// Render maze on canvas with grid lines
function renderMaze(maze) {
    var canvas = document.getElementById('mazeCanvas');
    var ctx = canvas.getContext('2d');
    
    var cellWidth = canvas.width / maze[0].length;
    var cellHeight = canvas.height / maze.length;
    
    // Clear the canvas before rendering
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw maze cells
    for (var row = 0; row < maze.length; row++) {
        for (var col = 0; col < maze[row].length; col++) {
            if (maze[row][col] === 1) {
                canvas.classList.add('wall')
                ctx.fillStyle = 'black'; // Wall
            } else if (maze[row][col] === 2) {
                ctx.fillStyle = 'red'; // Start point
            } else {
                canvas.classList.add('empty-space')
                ctx.fillStyle = 'white'; // Empty space
            }
            ctx.fillRect(col * cellWidth, row * cellHeight, cellWidth, cellHeight);
        }
    }
    
    // Draw vertical grid lines
    ctx.beginPath();
    for (var col = 0; col < maze[0].length + 1; col++) {
        ctx.moveTo(col * cellWidth, 0);
        ctx.lineTo(col * cellWidth, canvas.height);
    }
    ctx.strokeStyle = 'gray';
    ctx.stroke();
    
    // Draw horizontal grid lines
    ctx.beginPath();
    for (var row = 0; row < maze.length + 1; row++) {
        ctx.moveTo(0, row * cellHeight);
        ctx.lineTo(canvas.width, row * cellHeight);
    }
    ctx.strokeStyle = 'gray';
    ctx.stroke();
}
