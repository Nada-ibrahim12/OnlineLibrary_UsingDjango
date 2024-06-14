document.addEventListener("DOMContentLoaded", function() {
    var viewDButtons = document.querySelectorAll(".viewD-button");

    viewDButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            var bookId = event.target.getAttribute("data-book-id");
            var url = "BookDetailsUser.html?id=" + bookId; // Constructing the URL
            window.location.href = url;
        });
    });
});

// ////////////////////LOG_OUT///////////////////////////
const logoutBtn = document.querySelector(".logout-btn")

logoutBtn.addEventListener("click", () => {
    window.location.replace("/")
})