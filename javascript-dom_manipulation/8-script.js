// Wait for the document to fully load
document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')    
        .then(response => response.json())
        .then(data => {   
            document.getElementById("hello").textContent = data.hello;
        })
});
