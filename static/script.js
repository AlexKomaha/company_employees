function trimInput() {
  var inputValue = document.getElementById("name").value;
  var trimmedValue = inputValue.trim();
  document.getElementById("name").value = trimmedValue
}

function trimInputCountry() {
  var inputValue = document.getElementById("country").value;
  var trimmedValue = inputValue.trim();
  document.getElementById("country").value = trimmedValue
}

var button = document.getElementById('button');
button.style.marginLeft = '10px';
