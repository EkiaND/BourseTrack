document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("dark-mode-toggle");
    const body = document.body;
    const table = document.querySelector("table");
    const h1 = document.querySelector("h1");
    const h2 = document.querySelector("h2");

    toggle.addEventListener("click", function () {
        body.classList.toggle("dark-mode");
        h1.classList.toggle("dark-mode");
        h2.classList.toggle("dark-mode");
        table.classList.toggle("dark-mode");
    });
});
