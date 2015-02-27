(function() {
    function loadSubmissions() {
        $.get('/load_submissions', {
            'problem_id': $('#problem_id').val()
        }).done(function(data) {
            var table = $('#submissions');
            table.html('');
            data.submissions.forEach(function (submission) {
                var row = $('<tr>');
                row.append($('<td>').text(submission.id));
                row.append($('<td>').text(submission.user));
                row.append($('<td>').html($('<pre>').text(submission.code)));
                row.append($('<td>').text(submission.status));
                row.append($('<td>').text(submission.info));
                table.prepend(row);
            });
            table.prepend($('<tr> <th>#</th> <th>Пользователь</th> <th>Код</th> <th>Статус</th> <th>Комментарий</th> </tr>'));
        });
    }

    loadSubmissions();

    setInterval(loadSubmissions, 5000);
})();