/* Termowser is designed to be a simple "commandline like" interface for new programmers.
 * The goal here is to give new learners the ability to have simple fun experiences like creating a
 * "if statement labyrinth" or classic "enter your name, enter your age" type programs.
 *
 * Basic functions are:
 *  - Load a file
 *  - Write output to the "terminal"
 *  - Read input from the "user"
 *  - Clear the "terminal"
 *  - Unload a file
 */

(function() {
  function load(filename) {
    var program = document.createElement('script');
    var store = document.getElementById('loaded-prog');
    program.src = filename;
    program.addEventListener('load', function () {});
    store.appendChild(program);
  }

  function unload(filename) {
    return {status: "error", code: 500, message: "Not Implemented"};
  }
})();

function terminal() {
  // Variables and Init
  var DOM = {
    title: document.getElementById('prog-title'),
    name: document.getElementById('prog-name'),
    term: document.getElementById('term-window'),
    input: document.getElementById('input-box'),
    prog: document.getElementById('prog-file'),
    loaded: document.getElementById('loaded-prog'),
    list: document.getElementById('prog-list')
  }

  var INNERS = {
    readCallback: function(val) { return; }
  }

  DOM.input.addEventListener('keyup', function(e) {
    var key = e.which || e.keyCode;
    if (key === 13) {
      INNERS.readCallback(DOM.input.value);
      write("<- " + DOM.input.value);
      INNERS.readCallback = function(val) { return; };
      DOM.input.value = "";
    }
  });

  function write(message) {
    var el = document.createElement("div");
    el.textContent = message;
    DOM.term.appendChild(el);
    return {status: "ok", code: 200};
  }

  function read(callback) {
    if (typeof callback !== 'function') {
      return {status:"error", code: 400, message: "Callback must be a function!"}
    }
    INNERS.readCallback = callback;
  }

  function clear() {
    while (DOM.term.firstChild) {
      DOM.term.removeChild(DOM.term.firstChild);
    }
    return {status: "ok", code: 200};
  }

  return {
    write: write,
    read: read,
    clear: clear
  }
}
