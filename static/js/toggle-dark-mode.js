document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("dark-mode-toggle");
    const body = document.body;
    const table = document.querySelector("table");

    toggle.addEventListener("click", function () {
        body.classList.toggle("dark-mode");
        table.classList.toggle("dark-mode");
    });
});
