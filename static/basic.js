$().ready(function() {
    refreshList();
    $("#add").on("click", addTodo);
});

function addTodo(evt) {
    $.post("add", JSON.stringify($("#text").val()))
        .done(function (data) {
            refreshList();
        });
    $("#text").val('');
}

function removeTodo(todo) {
    $.post("remove", JSON.stringify(todo))
        .done(function (data) {
            refreshList();
        });
    $("#text").val('');
}

function refreshList() {
    $("#list").empty();
    $.get("show")
        .done(function (data) {
            for (item in data.items) {
                var x = $('<span class="remover"> x</span>');
                x.on("click", removeTodo.bind(undefined, data.items[item]));
                var elem = $(`<div class="item">${data.items[item]}</div>`);
                elem.append(x);
                $("#list").append(elem);
            }
            if (data.items.length === 0) {
                $("#list").append($("<div class='dim'>Nothing to see here ...</div>"));
            }
        });
}
