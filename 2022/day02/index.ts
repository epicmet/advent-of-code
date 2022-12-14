import { readInput } from "../util.js"

const fileContent = readInput();

// ROCK = 1,
// PAPER = 2,
// SISSORS = 3,
const movePointMap: { [Key: string]: number } = {
  // Opponent:
  A: 1,
  B: 2,
  C: 3,
  // Player:
  X: 1,
  Y: 2,
  Z: 3,
};

enum winPointMap {
  LOSE = 0,
  DRAW = 3,
  WIN = 6,
}

const getWinningMove = (move: number) => {
  // The winning move for each move is the next one in the map
  // ROCK = 1,
  // PAPER = 2,
  // SISSORS = 3,
  // 3 < 1 ;; 1 < 2 ;; 2 < 3

  const moveArr = [1, 2, 3];

  const moveIndex = moveArr.findIndex(m => m === move)

  const nextIndex = (moveIndex + 1) % moveArr.length;

  return moveArr[nextIndex];
}

// TODO: Advanced typescript string type in input and then use [number, number] instead of number[]
const getPointFromMove = (moves: string) => moves.split(" ").map(s => movePointMap[s]);

const getWinPoint = (op: number, pl: number) => {
  const {
    LOSE,
    DRAW,
    WIN
  } = winPointMap;

  if (op === pl) return DRAW;

  if (getWinningMove(op) === pl) return WIN;
  else return LOSE;
};

const getMatchPoint = (movePoints: number[]) => {
  const [opponentPoint, playerPoint] = movePoints;

  return getWinPoint(opponentPoint, playerPoint) + playerPoint;
};

const answer1 = fileContent
  .split("\n")
  .filter(Boolean)
  .map(getPointFromMove)
  // .map(([o, p]) => console.log(getWinPoint(o, p)))
  .map(getMatchPoint)
  .reduce((p, c) => p + c, 0);

console.log(answer1);
