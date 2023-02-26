const path = require("path");
const fs = require("fs");

const DATA_PATH = "./data.json";
const getData = async () => {
  return JSON.parse(fs.readFileSync(DATA_PATH, "utf8"));
};

const sqlite3 = require("sqlite3").verbose();
const sqlite = require("sqlite");

async function openUserDatabase() {
  const a = await sqlite
    .open({
      filename: "./users.db",
      driver: sqlite3.Database,
    })
    .then((db) => {
      db.exec(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, game_token TEXT)"
      );
      return db;
    });
  console.log(a);

  return a;
}

module.exports = {
  openUserDatabase,
  getData,
};
