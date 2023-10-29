document.addEventListener("DOMContentLoaded", function() {
    let tableRows = document.querySelectorAll(".clickable-row");
    tableRows.forEach(function(row) {
        let cells = row.getElementsByTagName("td");
        for (let i = 0; i < cells.length; i++) {
            cells[i].addEventListener("click", function() {
                let url = row.getAttribute("data-href");
                if (url) {
                    window.location.href = url;
                }
            });
        }
    });
});