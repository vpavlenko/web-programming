function switch_stations() {
    var from = document.getElementById('from');
    var to = document.getElementById('to');
    var tmp = from.value;
    from.value = to.value;
    to.value = tmp;
}

$(document).ready(function () {
    $('.suggest').click(function() {
        $(this).parent().find('input[type=text]').val($(this).text());
    });
});
