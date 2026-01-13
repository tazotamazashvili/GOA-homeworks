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