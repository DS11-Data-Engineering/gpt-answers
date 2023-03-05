function handleKeyDown(event) {
  if (event.keyCode === 13 && !event.shiftKey) {
    event.preventDefault();
    document.getElementById('request_form').submit()
  }
}

function updateMsgs() {
  $.getJSON('/messages', function(data) {
    var list = $('#msg-list');
    list.empty();

    for (var i = 0; i < data.length; i++) {
      list.append($(''))
    }
  })
}