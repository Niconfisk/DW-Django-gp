document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    forms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            const inputs = form.querySelectorAll("input[required]");
            let valid = true;
            inputs.forEach((input) => {
                if (!input.value.trim()) {
                    valid = false;
                    input.style.borderColor = "red";
                } else {
                    input.style.borderColor = "";
                }
            });
            if (!valid) {
                event.preventDefault();
                alert("Preencha todos os campos obrigatórios!");
            }
        });
    });
});
