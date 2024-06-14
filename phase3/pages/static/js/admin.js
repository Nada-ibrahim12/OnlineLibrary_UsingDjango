

// function addBooks() {
//     var formData = new FormData(document.getElementById("addBookForm"));

//     fetch('/add_book/', {  // Corrected URL
//         method: 'POST',
//         body: formData
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error('Network response was not ok');
//         }
//         // You can remove this part if you don't need to handle JSON responses
//         // return response.json();
//         // Instead, you can directly redirect
//         window.location.href = "View_list_admin.html";
//     })
//     .catch(error => {
//         console.error('There was an error!', error);
//         alert("An error occurred while adding the book.");
//     });

//     // Prevent the form from submitting normally
//     return false;
// }


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
