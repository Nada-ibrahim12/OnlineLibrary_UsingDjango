

////////////////LOGOUT///////////////////////
const logoutBtn = document.querySelector(".logout-btn")

logoutBtn.addEventListener("click", () => {
    window.location.replace("/")
})

/////////////////VIEW_BUTTON///////////////////
document.addEventListener("DOMContentLoaded", function() {
    var viewButtons = document.querySelectorAll(".view-button");

    viewButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            var bookId = event.target.getAttribute("data-book-id");
            var url = "view.html?id=" + bookId; // Constructing the URL
            window.location.href = url; // Redirecting to the book details page
        });
    });
});
