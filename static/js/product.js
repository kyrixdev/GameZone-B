document.addEventListener("DOMContentLoaded", function() {
    const mainImage = document.getElementById("mainImage");
    const zoomCircle = document.getElementById("zoomCircle");
    const mainImageContainer = document.getElementById("mainImageContainer");
    const sideImages = document.querySelectorAll(".sideImages__sideImage img");

    // Function to change main image and reset zoom on side image click
    function changeMainImage(imageSrc) {
        mainImage.src = imageSrc;
        mainImage.style.backgroundPosition = "0 0"; // Reset background position for zoom
        zoomCircle.style.display = "none"; // Hide zoom circle
    }

    // Event listener for side image click
    sideImages.forEach(function(sideImage) {
        sideImage.addEventListener("click", function() {
            const newImageSrc = sideImage.src;
            changeMainImage(newImageSrc);
        });
    });

    mainImageContainer.addEventListener("mousemove", function(event) {
        const rect = mainImageContainer.getBoundingClientRect();
        const mouseX = event.clientX - rect.left;
        const mouseY = event.clientY - rect.top;

        // Calculate the position of the circle
        const circleSize = 100; // Adjust based on the circle size
        const circleX = mouseX - circleSize / 2;
        const circleY = mouseY - circleSize / 2;

        // Set the position of the circle
        zoomCircle.style.left = circleX + "px";
        zoomCircle.style.top = circleY + "px";

        // Calculate the background position for zoom effect
        const bgPosX = (mouseX / rect.width) * 100;
        const bgPosY = (mouseY / rect.height) * 100;

        // Calculate the zoomed area position
        const zoomScale = 2; // Adjust the zoom scale as needed
        const bgPosZoomX = -((mouseX - rect.width / 2) * zoomScale - rect.width / 2);
        const bgPosZoomY = -((mouseY - rect.height / 2) * zoomScale - rect.height / 2);

        // Set the background position of the main image for zoom effect
        mainImage.style.backgroundSize = `${rect.width * zoomScale}px ${rect.height * zoomScale}px`;
        mainImage.style.backgroundPosition = `${bgPosZoomX}px ${bgPosZoomY}px`;
    });

    // Show zoom circle on mouse enter
    mainImageContainer.addEventListener("mouseenter", function() {
        zoomCircle.style.display = "block";
    });

    // Hide zoom circle on mouse leave
    mainImageContainer.addEventListener("mouseleave", function() {
        zoomCircle.style.display = "none";
    });
});

$(document).ready(function() {
    // Function to handle color selection
    $(".divs__div.color").click(function() {
        $(".divs__div.color").removeClass("selected"); // Remove 'selected' class from all colors
        $(this).addClass("selected"); // Add 'selected' class to the clicked color

        // Set the selected color ID to the hidden input
        var selectedColorId = $(this).data("color-id");
        $("#selectedColorInput").val(selectedColorId);
    });

    // Prevent form submission on button click if no color is selected
    $("form#colorForm").submit(function(e) {
        if ($("#selectedColorInput").val() === "") {
            e.preventDefault();
            alert("Please select a color before submitting.");
        }
    });
});
