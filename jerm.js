/* Jerm is designed to be a simple "commandline like" interface for new programmers.
 * The goal here is to give new learners the ability to have simple fun experiences like creating a
 * "if statement labyrinth" or classic "enter your name, enter your age" type programs.
 */

document.addEventListener('DOMContentLoaded', function() {
  var DOM = {
    filename: document.getElementById('prog-file'),
    button: document.getElementById('load-button'),
    store: document.getElementById('loaded-prog')
  }

  DOM.button.addEventListener('click', function(e) {
    load(DOM.filename.value);
  });

  DOM.filename.addEventListener('keyup', function(e) {
    var key = e.which || e.keyCode;
    if (key === 13) {
      load(DOM.filename.value);
      DOM.filename.value = '';
    }
  });

  function load(filename) {
    var program = document.createElement('script');
    var id = filename.toLowerCase().replace(' ', '-');
    program.id = id;
    program.src = "/programs/"+filename;
    DOM.store.appendChild(program);
  }
});

function terminal(programName) {
  // Variables and Init
  var DOM = {
    title: document.getElementById('page-title'),
    name: document.getElementById('prog-name'),
    term: document.getElementById('term-window'),
    input: document.getElementById('input-box')
  }

  var INNERS = {
    readCallback: function(val) { console.log("ReadCallback not set, value was: "+val); return; }
  }

  if (programName === undefined) {
    var programName = "Unnamed";
  }
  DOM.title.textContent = "TRMSR - "+programName;
  DOM.name.textContent = programName;

  DOM.input.addEventListener('keyup', function(e) {
    var key = e.which || e.keyCode;
    if (key === 13) {
      console.log("Got event");
      console.log(INNERS.readCallback);
      var fn = INNERS.readCallback;
      INNERS.readCallback = function(val) { return; };
      fn(DOM.input.value);
      write("<- " + DOM.input.value);

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
    console.log("Read callback about to be set");
    console.log(INNERS.readCallback);
    if (typeof callback !== 'function') {
      return {status:"error", code: 400, message: "Callback must be a function!"}
    }
    INNERS.readCallback = callback;
    console.log(INNERS.readCallback);
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
