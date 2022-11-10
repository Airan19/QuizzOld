<script
  src=" https://code.jquery.com/jquery-3.6.1.js"
  integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI="
  crossorigin="anonymous "
></script>;

const splash = document.querySelector(".splash");

document.addEventListener("DOMContentLoader", (e) => {
  setTimeout(() => {
    splash.classList.add("display-none");
  }, 3000);
});

$(function () {
  $(".toggle").on("click", function () {
    if ($(".menu").hasClass("active")) {
      $(".menu").removeClass("active");
      $(this).find("a").html("<ion-icon name='menu-outline'></ion-icon>");
    } else {
      $(".menu").addClass("active");
      $(this).find("a").html("<ion-icon name='close-outline'></ion-icon>");
    }
  });
});
