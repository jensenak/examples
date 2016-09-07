/* Termowser is designed to be a simple "commandline like" interface for new programmers.
 * The goal here is to give new learners the ability to have simple fun experiences like creating a
 * "if statement labyrinth" or classic "enter your name, enter your age" type programs.
 *
 * Basic functions are:
 *  - Load a file
 *  - Write output to the "terminal"
 *  - Read input from the "user"
 *  - Unload a file
 */
(function () {
  // Onload things
  return;
})();

function terminal() {
  function load(filename) {
    var program = document.createElement('script');
    var store = document.getElementById('loaded-prog');
    program.src = filename;
    program.addEventListener('load', function () {});
    store.appendChild(program);
  }

  function write(message) {
    return {status: "ok", code: 200};
  }

  function read() {
    return 0;
  }

  function unload(filename) {
    return {status: "error", code: 500, message: "Not Implemented"};
  }

  return {
    load: load,
    write: write,
    read: read,
    unload: unload
  }
}
