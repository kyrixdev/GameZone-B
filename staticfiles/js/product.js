document.addEventListener("DOMContentLoaded", function() {
    const mainImage = document.getElementById("mainImage");
    const zoomCircle = document.getElementById("zoomCircle");
    const mainImageContainer = document.getElementById("mainImageContainer");

    mainImageContainer.addEventListener("mousemove", function(event) {
        const rect = mainImage.getBoundingClientRect();
        const mouseX = event.clientX - rect.left;
        const mouseY = event.clientY - rect.top;

        // Set the position of the circle
        zoomCircle.style.left = mouseX - 50 + "px"; // Adjust 50 based on the circle size
        zoomCircle.style.top = mouseY - 50 + "px";

        // Set the background position of the main image to simulate zoom
        mainImage.style.backgroundPosition = `-${mouseX * 2}px -${mouseY * 2}px`;
    });

    mainImageContainer.addEventListener("mouseenter", function() {
        zoomCircle.style.display = "block";
    });

    mainImageContainer.addEventListener("mouseleave", function() {
        zoomCircle.style.display = "none";
    });
});