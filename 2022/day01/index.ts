import { readInput } from "../util.js"

/** Usage: yarn ts-node day01 */
const fileContent = readInput();

const answer = fileContent
  .split("\n")
  .reduce<number[]>((arr, curr) => {
    if(curr === "") {
      arr.push(0);
    } else {
      arr.push((arr.pop() || 0) + parseInt(curr));
    }

    return arr;
  }, [])
  .sort((a, b) => b - a);

console.log("First part: ");
console.log(answer[0]);
console.log("--------");
console.log("Second part: ");
console.log(answer[0])
