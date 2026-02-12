function showFileName(event) {
    const file = event.target.files[0];
    if (file) {
        const fileName = document.getElementById("fileName");
        const area = document.querySelector(".upload-area");

        fileName.textContent = "📎 " + file.name;
        area.classList.add("selected");
    }
}
