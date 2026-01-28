// 1
function maxDifference(...nums) {
    let max = Math.max(...nums);
    let min = Math.min(...nums);
    return max - min;
  }
  
  
  // 2
  function mergeAndFilter(min, ...arrays) {
    let merged = [];
    for (let arr of arrays) {
      for (let num of arr) {
        if (num > min) merged.push(num);
      }
    }
    return merged;
  }
  
  
  // 3
  function updateUser(user, ...updates) {
    let result = { ...user };
    for (let upd of updates) {
      result = { ...result, ...upd };
    }
    return result;
  }
  
  
  // 4
  const words = ["level", "world", "radar", "hello"];
  const palindromes = [];
  
  for (let word of words) {
    let reversed = word.split("").reverse().join("");
    if (word === reversed) palindromes.push(word);
  }
  
  
  // 5
  const arr = [10, 0, 15, 20, 0, 5];
  let zeroCount = 0;
  
  for (let num of arr) {
    if (num === 0) zeroCount++;
  }
  
  
  // 6
  const nums = [2, 5, 3, 4, 1];
  const cumulative = [];
  let sum = 0;
  
  for (let n of nums) {
    sum += n;
    cumulative.push(sum);
  }
  