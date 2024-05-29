document.addEventListener("DOMContentLoaded", function () {
    var alerts = document.querySelectorAll("#messages .alert");

    alerts.forEach(function (alert) {
        window.setTimeout(function () {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";
            window.setTimeout(function () {
                alert.remove();
            }, 500);
        }, 5000);
    });
});
