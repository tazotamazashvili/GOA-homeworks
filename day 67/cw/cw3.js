function newk(obj, value) {
    obj.new = value;
    return obj;
  }
  
  const person = { name: "tazo", age: 16 };
  console.log(newk(person, "student"));