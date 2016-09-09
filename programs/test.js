var term = terminal("Test");
term.write('Enter your name');
term.read(getName);

function getName(name) {
  term.write("You entered: "+name);
  next();
}

function next() {
  term.write('Enter a positive number');
  r = term.read(getNumber);
}

function getNumber(n) {
  var num = parseInt(n);
  if (num < 1) {
    term.write("That's not a positive number!");
    return;
  }
  for (var i = 0; i < num; i++) {
    term.write("This is number "+i);
  }
  term.write("Done!");
  return;
}
