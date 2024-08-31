document.addEventListener("DOMContentLoaded", function() {
    // Create a falling container
    const container = document.createElement("div");
    container.className = "falling-container";
    container.innerHTML = "<h1>HNDRX$</h1>";

    // Append the falling container to the body
    document.body.appendChild(container);

    // Listen for the animation end to remove the falling container and show the main content
    container.addEventListener("animationend", function() {
        container.style.display = "none";
        document.querySelector(".container").style.display = "block";
    });
});
