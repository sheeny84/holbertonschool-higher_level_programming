document.getElementById("add_item").addEventListener("click", () => {
    // Get first node in list off all my_list class elements
    const myList = document.getElementsByClassName("my_list").item(0)
    // create new list element
    const listItem = document.createElement('li');
    // Add text 'Item'
    listItem.textContent = 'Item';
    // Append listItem to myList
    myList.  appendChild(listItem)  
})
