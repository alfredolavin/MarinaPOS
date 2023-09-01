function resizeInput() {
  this.style.width = Math.max(this.value.length, 13) + "ch";
}

if (document.location.search.match(/type=embed/gi)) {
  window.parent.postMessage("resize", "*");
}

$(document).ready(function() {
  var input = document.querySelector('input');
  input.addEventListener('input', resizeInput);
  resizeInput.call(input);

  /*document.getElementById('entrada').focus();
  document.addEventListener("mousedown", event => {
    event.preventDefault();
    event.stopPropagation();
    document.getElementById('entrada').focus()});*/
});
