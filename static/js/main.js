const mobileMenuBtn = document.getElementById("mobileMenuBtn");
const mainNav = document.getElementById("mainNav");

if (mobileMenuBtn && mainNav) {
    mobileMenuBtn.addEventListener("click", () => {
        mainNav.classList.toggle("active");
    });

    mainNav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            mainNav.classList.remove("active");
        });
    });
}