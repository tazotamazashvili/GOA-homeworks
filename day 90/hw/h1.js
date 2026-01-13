const person = {
  name: "ilia",
  age: 19,
  city: "rustavi"
};

const { name, age } = person;

console.log(name); 
console.log(age);



const colors = ["red", "green", "blue"];

const [firstColor, , thirdColor] = colors;

console.log(firstColor); 
console.log(thirdColor); 
