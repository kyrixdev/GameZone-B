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
