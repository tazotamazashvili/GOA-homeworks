// 1
const divEl = document.querySelector("div");
const parent = divEl.parentElement;
parent.style.background = "lightblue";

// 2
const ulEl = document.querySelector("ul");
const firstLi = ulEl.firstElementChild;
firstLi.textContent = "First LI changed!";

// 3
const btn = document.querySelector("button");
const nextSibling = btn.nextElementSibling;
nextSibling.textContent = "Changed by DOM navigation";

// 4
const someElement = document.querySelector(".target"); 
const children = someElement.children;
for (let child of children) {
  child.classList.add("new-class");
}

// 5
const card = document.querySelector(".card");
const cardClone = card.cloneNode(true);
document.body.appendChild(cardClone);

// 6
const p = document.querySelector("p");
const pClone = p.cloneNode(true);
const section = document.querySelector("section");
section.appendChild(pClone);

// 7
const cloneBtn = document.querySelector(".clone-btn"); 
const cloneTarget = document.querySelector(".clone-target");
cloneBtn.addEventListener("click", () => {
  const c = cloneTarget.cloneNode(true);
  cloneTarget.parentElement.appendChild(c);
});

// 8
const img = document.querySelector("img");
console.log("Image source:", img.getAttribute("src"));

// 9
const dataBtn = document.querySelector(".data-btn"); 
const dataTarget = document.querySelector(".data-target");
dataBtn.addEventListener("click", () => {
  dataTarget.setAttribute("data-id", "123");
});

// 10
const link = document.querySelector("a");
link.setAttribute("href", "https://google.com");
