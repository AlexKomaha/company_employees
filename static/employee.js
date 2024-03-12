document.addEventListener("DOMContentLoaded", function () {

  function styleFormGroups() {
      var formGroups = document.querySelectorAll('.form-group');
      formGroups.forEach(function (group) {
          group.style.maxWidth = '400px';
          group.style.marginBottom = '15px';
      });
  }
  styleFormGroups();
});
