function toggle(id) {
    const el = document.getElementById(id);
    el.style.display = (el.style.display === "block") ? "none" : "block";
}

function set(inputId, textId, value) {
    document.getElementById(inputId).value = value;
    document.getElementById(textId).innerText = value;

    document.querySelectorAll('.dropdown-list').forEach(el => {
        el.style.display = "none";
    });
}

document.addEventListener("click", function(e) {
    if (!e.target.closest(".dropdown")) {
        document.querySelectorAll(".dropdown-list").forEach(el => {
            el.style.display = "none";
        });
    }
});