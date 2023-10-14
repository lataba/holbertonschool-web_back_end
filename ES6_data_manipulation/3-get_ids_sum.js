export default function getStudentIdsSum(students) {
  // check if students is an array
  if (Object.getPrototypeOf(students) === Array.prototype) {
    // get all ids from students
    const ids = students.map((items) => items.id);
    // reducer function to add all ids
    const reducer = (accumlator, currentValue) => accumlator + currentValue;
    return ids.reduce(reducer);
  }
  return [];
}
