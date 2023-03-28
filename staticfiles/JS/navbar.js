let count = true;

function activBtn() {
    const burg1 = document.getElementById("burg1");
    const burg2 = document.getElementById("burg2");
    const burg3 = document.getElementById("burg3");
    const list = document.getElementById("navList");
    
    if (count) {
        burg1.classList.add("open");
        burg2.classList.add("open");
        burg3.classList.add("open");
        list.classList.add("open");
        count = false;
    } else {
        burg1.classList.remove("open");
        burg2.classList.remove("open");
        burg3.classList.remove("open");
        list.classList.remove("open");
        count = true;
    }
}