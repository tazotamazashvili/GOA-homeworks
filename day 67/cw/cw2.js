function compare(student1, student2) {
    if (student1.grade > student2.grade) {
        return student1.name;
    } else if (student1.grade < student2.grade) {
        return student2.name;
    } else {
        if (student1.id > student2.id) {
            return student1.name;
        } else if (student1.id < student2.id) {
            return student2.name;
        } else {
            return 'tolia';
        }
    }
}


const s1 = { name: "ana", id: 5, grade: 90 };
const s2 = { name: "gio", id: 7, grade: 90 };

console.log(compare(s1, s2));