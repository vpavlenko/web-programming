// client
function addNewTask() {
    $todo.attr('data-id');
    socket.emit('add task', );
}

function onChangeTodoContent($todo) {
    var id = $todo.attr('data-id');
    .emit('change task', [id, $todo.text()]);
}

.on('add task', function(data) {
    var $newTask = $('<div>').text(data.content);
    $('#tasks').append($newTask);
}

unsubmittedChanges = [];

// server
var numIDs;
var tasks = [];

.on('add task', function (data) {
    tasks.push({content: data.content, id: numIDs++});
    socket.broadcast.emit('add task',
        tasks[tasks.length - 1]);
})

построить дерево
поступить в универ
купить машину