const input = document.getElementById("noteInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("noteList");

let notes = JSON.parse(localStorage.getItem("notes")) || [];

function displayNotes() {
  list.innerHTML = "";
  notes.forEach((note, index) => {
    let li = document.createElement("li");
    li.innerHTML = `${note} <span class="remove" onclick="removeNote(${index})">x</span>`;
    list.appendChild(li);
  });
}

function addNote() {
  if (input.value.trim() === "") return;
  notes.push(input.value);
  input.value = "";
  save();
}

function removeNote(index) {
  notes.splice(index, 1);
  save();
}

function save() {
  localStorage.setItem("notes", JSON.stringify(notes));
  displayNotes();
}

addBtn.addEventListener("click", addNote);
displayNotes();

let theme = localStorage.getItem("theme") || "light";

document.body.classList.toggle("dark", theme === "dark");

themeBtn.textContent = (theme === "dark") ? "light" : "dark";

themeBtn.onclick = () => {
  theme = (theme === "light") ? "dark" : "light";
  document.body.classList.toggle("dark", theme === "dark");
  themeBtn.textContent = (theme === "dark") ? "☀️" : "🌙";
  localStorage.setItem("theme", theme);
};


