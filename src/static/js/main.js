function handleKeyDown(event) {
  if (event.keyCode === 13 && !event.shiftKey) {
    event.preventDefault();
    document.getElementById('request_form').submit()
  }
}