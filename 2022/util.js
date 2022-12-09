const fs = require("fs");
const path = require("path");

export const readInput = (filename = "input.txt") => {
  const dayDir = process.argv["1"];
  const filepath = path.resolve(__dirname, dayDir, filename);

  return fs.readFileSync(filepath).toString();
};


// TODO: Make a reusable readline interface
