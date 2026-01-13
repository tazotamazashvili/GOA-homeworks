// 1. 
const arr = [5, 10, 15, 20];
arr.forEach((element, index) => {
  console.log(index, element);
});

// 2. 
const words = ["nanuka", "nika", "andria"];
words.forEach(word => {
  console.log(word.length);
});

// 3.
const nums = [5, 10, 15, 20];
let sum = 0;
nums.forEach(num => {
  sum += num;
});
console.log("sum:", sum);

// 4. 
const users = [
  {name: "lasha", age: 85},
  {name: "giorgi", age: 71}
];
users.forEach(user => {
  console.log(`${user.name}: ${user.age}`);
});

// 5.
const letters = ["a", "b", "c"];
letters.forEach(letter => {
  console.log("#" + letter);
});

