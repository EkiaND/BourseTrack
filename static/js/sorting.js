document.addEventListener("DOMContentLoaded", function () {
    const table = document.getElementById("tableau-indicateurs");
    const headers = table.querySelectorAll("th.sortable");

    headers.forEach(header => {
        header.addEventListener("click", function () {
            const columnIndex = Array.from(this.parentNode.children).indexOf(this);
            const order = this.dataset.order === "asc" ? "desc" : "asc";
            this.dataset.order = order;

            headers.forEach(h => h.classList.remove("active")); // Retirer l'état actif des autres colonnes
            this.classList.add("active"); // Marquer la colonne triée comme active

            const rows = Array.from(table.querySelectorAll("tbody > tr"));

            rows.sort((rowA, rowB) => {
                const cellA = rowA.children[columnIndex].innerText;
                const cellB = rowB.children[columnIndex].innerText;

                const valueA = isNaN(cellA) ? cellA : parseFloat(cellA);
                const valueB = isNaN(cellB) ? cellB : parseFloat(cellB);

                if (order === "asc") {
                    return valueA > valueB ? 1 : -1;
                } else {
                    return valueA < valueB ? 1 : -1;
                }
            });

            const tbody = table.querySelector("tbody");
            tbody.innerHTML = "";
            rows.forEach(row => tbody.appendChild(row));
        });
    });

    // Coloration dynamique en fonction du rendement moyen journalier
    const rows = table.querySelectorAll("tbody > tr");
    rows.forEach(row => {
        const rendementCell = row.children[row.children.length - 1];
        const rendement = parseFloat(rendementCell.innerText);
        if (rendement > 0) {
            row.classList.add("positive");
        } else if (rendement < 0) {
            row.classList.add("negative");
        }
    });
});
