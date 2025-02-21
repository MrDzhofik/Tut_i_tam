function getCSRFToken() {
    let cookieValue = null;
    const cookies = document.cookie.split('; ');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].split('=');
        if (cookie[0] === 'csrftoken') {
            cookieValue = cookie[1];
            break;
        }
    }
    return cookieValue;
}


document.getElementById("ContactForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let formData = new FormData(this);

    let name = document.getElementById("name")
    formData.append("name", name.innerText);

    fetch("", {
        headers: {
            'X-CSRFToken': getCSRFToken(),  // Добавляем CSRF-токен
        },
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                document.getElementById("responseMessage").innerText = data.message;
                document.getElementById("ContactForm").reset();
            } else {
                document.getElementById("responseMessage").innerText = "Ошибка: " + JSON.stringify(data.errors);
            }
        })
        .catch(error => console.error("Ошибка:", error));
});
