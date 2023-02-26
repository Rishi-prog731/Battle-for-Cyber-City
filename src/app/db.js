const path = require("path");
const fs = require("fs");

const DATA_PATH = "./data.json";
const getData = async () => {
  return JSON.parse(fs.readFileSync(DATA_PATH, "utf8"));
};

const sqlite3 = require("sqlite3").verbose();
const sqlite = require("sqlite");

var db_users;
var db_game;

const init = async () => {
  [db_users, db_game] = await Promise.all([
    sqlite.open({
      filename: "./users.db",
      driver: sqlite3.Database,
    }),
    sqlite.open({
      filename: "./game.db",
      driver: sqlite3.Database,
    }),
  ]);

  await userDatabase_setup();
  await userDatabase_clear();
};

/**
 *
 * @param {string} username
 * @param {string} email
 * @param {string} game_token
 */
const userDatabase_add = async (username, email, game_token) => {
  console.log("addUser", username, email, game_token);
  await db_users.run(
    `INSERT INTO users (username, email, game_token) VALUES (?, ?, ?)`,
    [username, email, game_token]
  );
};

const userDatabase_setup = async () => {
  await db_users.run(
    `CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      email TEXT NOT NULL,
      game_token TEXT NOT NULL
    )`
  );
};

/**
 *
 * @param {string} username
 * @param {string} game_token
 * @returns
 */
const userDatabase_get = async (username, game_token) => {
  return await db_users.get(
    `SELECT * FROM users WHERE username = ? AND game_token = ?`,
    [username, game_token]
  );
};

/**
 *
 * @param {string} username
 * @param {string} email
 * @param {string} game_token
 * @returns
 */
const userDatabase_check = async (username, email, game_token) => {
  return await db_users.get(
    `SELECT * FROM users WHERE username = ? AND email = ? AND game_token = ?`,
    [username, email, game_token]
  );
};

const userDatabase_clear = async () => {
  await db_users.run(`DELETE FROM users`);
};

module.exports = {
  getData,
  init,

  userDatabase_add,
  userDatabase_setup,
  userDatabase_clear,
  userDatabase_get,
  userDatabase_check,

  db_game,
  db_users,
};
