// script.js
function sprawdzTekst() {
    var tekstDoSkopiowania = document.getElementById('tekstDoSkopiowania').textContent;
    var wpisanyTekst = document.getElementById('poleWpisywania').value;

    if(tekstDoSkopiowania === wpisanyTekst) {
        alert("Doskonale! Tekst został prawidłowo skopiowany.");
    }
}
function myFunction() {
    alert("Hello from a static file!");
  }