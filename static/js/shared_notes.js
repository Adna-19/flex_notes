document.querySelector('#note-save-btn').addEventListener('click', (event) => {
  const slug = event.target.dataset.slug;
  const url = `/notes/shared/${slug}/save/note/`;
  const requesting_method = 'GET'
  var message_box = document.querySelector('#message-box');

  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      const response = JSON.parse(this.responseText);

      message_box.classList.remove('not-visible');
      message_box.classList.add(response.alert_class);
      message_box.textContent = response.message;

      // remove message box after 3 seconds
      setTimeout(() => {
        message_box.classList.add('not-visible');
      }, 3000)
    }
  }

  xhttp.open(requesting_method, url, true);
  xhttp.send();
})