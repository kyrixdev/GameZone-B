let lastScrollTop = 0;

const HeaderCatagories = document.querySelector(".header__categories");

// Function to handle scroll event
function handleScroll() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        // Scrolling down
        HeaderCatagories.style.opacity = "1";
        HeaderCatagories.style.transform = "translateY(-50px)";
    } else {
        // Scrolling up
        HeaderCatagories.style.opacity = "1";
        HeaderCatagories.style.transform = "translateY(0px)";
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
}

// Add scroll event listener
window.addEventListener('scroll', handleScroll);


// SideBarMenu JS
document.addEventListener("DOMContentLoaded", function () {
    const body = document.querySelector("body");
    const button = document.querySelector(".sidemenu_btn");
    const menu = document.querySelector(".sidemenu_wrapper");
    const close = document.querySelector(".sidemenu_close");
    const closeOverlay = document.querySelector(".overlay_close");
    const subMenuLinks = document.querySelectorAll(".category_link");
    const back = document.querySelector(".sidemenu_back");
    const menuOverlay = document.querySelector(".sidemenu_overlay");
    const subSubMenuLinks = document.querySelectorAll(".sub_category_link");

    // Toggle menu when button is clicked
    button.addEventListener("click", function () {
        menu.style.display = (menu.style.display === "none" || menu.style.display === "") ? "block" : "none";
        body.style.overflowY = menu.style.display === "none" ? "auto" : "hidden";
    });

    // Handle clicks on category links
    subMenuLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default link behavior
            menuOverlay.style.display = "block";
            body.style.overflowY = "hidden";
        });
    });

    subSubMenuLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default link behavior
            menuOverlay.style.display = "none";
            menu.style.display = "none";
            body.style.overflowY = "auto";
        });
    });
    // Handle clicks on back button
    back.addEventListener("click", function () {
        menuOverlay.style.display = "none";
        menu.style.display = "block";
    });

    // Close menu when close button is clicked
    close.addEventListener("click", function () {
        menuOverlay.style.display = "none";
        menu.style.display = "none";
        body.style.overflowY = "auto";
    });
    // Close Overlay when close button is clicked
    closeOverlay.addEventListener("click", function () {
        menuOverlay.style.display = "none";
        menu.style.display = "none";
        body.style.overflowY = "auto";
    });
    // Close menu when clicking outside of it
    document.addEventListener("click", function (event) {
        if (!menu.contains(event.target) && !button.contains(event.target) && !back.contains(event.target) && !menuOverlay.contains(event.target) ) {
            menu.style.display = "none";
            menuOverlay.style.display = "none";
            body.style.overflowY = "auto";
        }
    });
});



document.addEventListener("DOMContentLoaded", function () {
    var body = document.querySelector("body");
    var user_sidemenu_wrapper = document.querySelector(".user_sidemenu_wrapper");
    var user_sidemenu_btn = document.querySelector(".user__signed");
    var user_sidemenu_close = document.querySelector(".user_sidemenu_close");

    // Toggle menu when button is clicked
    user_sidemenu_btn.addEventListener("click", function () {
        user_sidemenu_wrapper.style.display = (user_sidemenu_wrapper.style.display === "none" || user_sidemenu_wrapper.style.display === "") ? "block" : "none";
        body.style.overflowY = user_sidemenu_wrapper.style.display === "none" ? "auto" : "hidden";
    });

    // Close menu when close button is clicked
    user_sidemenu_close.addEventListener("click", function () {
        user_sidemenu_wrapper.style.display = "none";
        body.style.overflowY = "auto";
    });

    // Close menu when clicking outside of it
    document.addEventListener("click", function (event) {
        if (!user_sidemenu_wrapper.contains(event.target) && !user_sidemenu_btn.contains(event.target)) {
            user_sidemenu_wrapper.style.display = "none";
            body.style.overflowY = "auto";
        }
    });
}
);