import { readInput } from "../util.js";

const inputArr = readInput().split("\n").filter(Boolean);

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

enum MatchResult {
  LOSE = 0,
  DRAW = 3,
  WIN = 6,
}

const MOVE_ARR = [1, 2, 3];

const getWinningMove = (move: number) => {
  // The winning move for each move is the next one in the map
  // ROCK = 1,
  // PAPER = 2,
  // SISSORS = 3,
  // 3 < 1 ;; 1 < 2 ;; 2 < 3

  const moveIndex = MOVE_ARR.findIndex((m) => m === move);

  const nextIndex = (moveIndex + 1) % MOVE_ARR.length;

  return MOVE_ARR[nextIndex];
};

const getLosingMove = (move: number) => {
  // The losing move for each move is the previos one in the map as explaned

  const moveIndex = MOVE_ARR.findIndex((m) => m === move);

  const nextIndex = moveIndex - 1;

  if (nextIndex < 0) return MOVE_ARR[MOVE_ARR.length - 1];
  else return MOVE_ARR[nextIndex];
};

// TODO: Advanced typescript string type in input and then use [number, number] instead of number[]
const getPointForEachMove = (moves: string) =>
  moves.split(" ").map((s) => movePointMap[s]);

const getMatchResult = (op: number, pl: number) => {
  if (op === pl) {
    return MatchResult.DRAW;
  } else if (getWinningMove(op) === pl) {
    return MatchResult.WIN;
  } else {
    return MatchResult.LOSE;
  }
};

const calcPointBasedOnPlayerMove = (movePoints: number[]) => {
  const [opponentPoint, playerPoint] = movePoints;

  return getMatchResult(opponentPoint, playerPoint) + playerPoint;
};

const calcPointBasedOnActionId = (movePoints: number[]) => {
  const [opponentPoint, actionId] = movePoints;

  if (actionId === 1 /* X, Lose */)
    return getLosingMove(opponentPoint) + MatchResult.LOSE;
  else if (actionId === 2 /* Y, Draw */)
    return opponentPoint + MatchResult.DRAW;
  /* Z, Win */ else return getWinningMove(opponentPoint) + MatchResult.WIN;
};

// --- PART 1 ---
const answer1 = inputArr
  .map(getPointForEachMove)
  .map(calcPointBasedOnPlayerMove)
  .reduce((p, c) => p + c, 0);

console.log("Part 1:", answer1); // 14531

// --- PART 2 ---
const answer2 = inputArr
  .map(getPointForEachMove)
  .map(calcPointBasedOnActionId)
  .reduce((p, c) => p + c, 0);

console.log("Part 2:", answer2); // 11258
