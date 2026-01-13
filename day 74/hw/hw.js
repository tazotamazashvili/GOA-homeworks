// 1. 
const arr = [5, 10, 15, 20];
arr.forEach((element, index) => {
  console.log(index, element);
});

// 2. 
const words = ["ana", "mari", "ana"];
words.forEach(word => {
  console.log(word.length);
});

// 3.
const nums = [5, 10, 15, 20];
let sum = 0;
nums.forEach(num => {
  sum += num;
});
console.log("jami:", sum);

// 4. 
const users = [
  {name: "gialo", age: 25},
  {name: "lomi", age: 21}
];
users.forEach(user => {
  console.log(`${user.name}: ${user.age}`);
});

// 5.
const letters = ["a", "b", "c"];
letters.forEach(letter => {
  console.log("#" + letter);
});
// 1.
const isEven = (num) => num % 2 === 0;
console.log(isEven(10)); 
console.log(isEven(7));  


// 2.
const add = (a, b) => a + b;
console.log(add(5, 3)); // 8

// 2) ახსენით რა არის callback.
// funqcia romelic sxva funqcias gadaecema da sxva dros eshveba
function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

const sayBye = () => console.log("byee!");

greet("tazo", sayBye);


// 3.
const square = (n) => n * n;
console.log(square(5));