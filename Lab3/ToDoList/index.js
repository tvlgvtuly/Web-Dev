const inputBox = document.getElementById("inputTask")
const listTask = document.getElementById("listInsertion")
const deleteAllBtn = document.getElementById("deleteAllBtn");

function addTask(){
    if(inputBox.value === ""){
        alert("write something!")
    }
    else{
        li = document.createElement("li")
        li.innerHTML = `
                <input type = "checkbox">
                <span class = "task-text">${inputBox.value}</span>
                <button class= "delete_btn">🗑</button>`
                listTask.prepend(li);
    }
    inputBox.value="";
    saveData();
}

listTask.addEventListener("click", function(e){
    if(e.target.tagName === "INPUT"){
        e.target.nextElementSibling.classList.toggle("completed");
        saveData();
    }
    else if(e.target.tagName === "BUTTON"){
        e.target.parentElement.remove();
        saveData();
    }
}, false)

function saveData(){
    localStorage.setItem("data", listTask.innerHTML)
}
function showTask(){
    listTask.innerHTML = localStorage.getItem("data");
}
// showTask();


deleteAllBtn.addEventListener("click", function() {
    listTask.innerHTML = ""; 
    saveData();
});
showTask();