var i = 0;
var txt = 'NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN, NEVER GONNA RUN AROUND AND DESERT YOU, NEVER GONNA MAKE YOU CRY, NEVER GONNA SAY GOODBYE, NEVER GONNA TELL A LIE AND HURT YOU';

function typeWriter() {
  if (i < txt.length) {
    document.getElementsByClassName('js-typewrite')[0].innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, 65);
  }
}
setTimeout(typeWriter, 1000);
