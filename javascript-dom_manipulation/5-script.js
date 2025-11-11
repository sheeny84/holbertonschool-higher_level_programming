document.getElementById("update_header").addEventListener("click", () => {
    const myHeader = document.getElementsByTagName("header").item(0);
    myHeader.textContent = "New Header!!!"
})
