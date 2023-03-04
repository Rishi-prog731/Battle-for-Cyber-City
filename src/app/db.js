const path = require("path");
const fs = require("fs");

// Main databases
const sqlite3 = require("sqlite3").verbose();
const sqlite = require("sqlite");

var database;
const setupDb = async () => {
  database = await sqlite.open({
    filename: path.join("database.db"),
    driver: sqlite3.Database,
  });

  await hackerAbility.createTable();
  await hackerEvent.createTable();
  await defenderAbility.createTable();
  await defenderEvent.createTable();
  await matchup.createTable();
  await district.createTable();
};

// District Table
const district = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS district (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        health INTEGER NOT NULL,
        active_hacker_abilities INTEGER,
        active_defender_abilities INTEGER,
        FOREIGN KEY (active_hacker_abilities) REFERENCES hacker_ability(id),
        FOREIGN KEY (active_defender_abilities) REFERENCES defender_ability(id)
      );`);
  },
};

// Match_Up Table
const matchup = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS matchup (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hacker_id INTEGER NOT NULL,
        defender_id INTEGER NOT NULL,
        FOREIGN KEY (hacker_id) REFERENCES hacker(id),
        FOREIGN KEY (defender_id) REFERENCES defender(id)
      );`);
  },
};

// Hacker - Ability Table
const hackerAbility = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS hacker_ability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        value INTEGER NOT NULL
      );`);
  },

  clear: async () => {
    database.run(`DELETE FROM hacker_ability`);
  },

  remove: async (id) => {
    database.run(`DELETE FROM hacker_ability WHERE id = ?`, [id]);
  },

  insertAbility: async (name, description, value) => {
    database.run(
      `INSERT INTO hacker_ability (name, description, value) VALUES (?, ?, ?)`,
      [name, description, value]
    );
  },

  getAll: async () => {
    return await database.all(`SELECT * FROM hacker_ability`);
  },

  get: async (id) => {
    return await database.get(`SELECT * FROM hacker_ability WHERE id = ?`, [
      id,
    ]);
  },
};

// Hacker - Event Table
const hackerEvent = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS hacker_event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        extra_ability_count INTEGER NOT NULL
      );`);
  },

  clear: async () => {
    database.run(`DELETE FROM hacker_event`);
  },

  remove: async (id) => {
    database.run(`DELETE FROM hacker_event WHERE id = ?`, [id]);
  },

  insertEvent: async (name, description, extraAbilityCount) => {
    database.run(
      `INSERT INTO hacker_event (name, description, extra_ability_count) VALUES (?, ?, ?)`,
      [name, description, extraAbilityCount]
    );
  },

  getAll: async () => {
    database.all(`SELECT * FROM hacker_event`);
  },

  get: async (id) => {
    database.get(`SELECT * FROM hacker_event WHERE id = ?`, [id]);
  },
};

// Defender - Ability Table
const defenderAbility = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS defender_ability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        value INTEGER NOT NULL
      );`);
  },

  clear: async () => {
    database.run(`DELETE FROM defender_ability`);
  },

  remove: async (id) => {
    database.run(`DELETE FROM defender_ability WHERE id = ?`, [id]);
  },

  insertAbility: async (name, description, value) => {
    database.run(
      `INSERT INTO defender_ability (name, description, value) VALUES (?, ?, ?)`,
      [name, description, value]
    );
  },

  getAll: async () => {
    database.all(`SELECT * FROM defender_ability`);
  },

  get: async () => {
    database.run(`SELECT * FROM defender_ability WHERE id = ?`, [id]);
  },
};

// Defender - Event Table
const defenderEvent = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS defender_event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        extra_ability_count INTEGER NOT NULL
      );`);
  },

  clear: async () => {
    database.run(`DELETE FROM defender_event`);
  },

  remove: async (id) => {
    database.run(`DELETE FROM defender_event WHERE id = ?`, [id]);
  },

  insertEvent: async (name, description, extraAbilityCount) => {
    database.run(
      `INSERT INTO defender_event (name, description, extra_ability_count) VALUES (?, ?, ?)`,
      [name, description, extraAbilityCount]
    );
  },

  getAll: async () => {
    database.all(`SELECT * FROM defender_event`);
  },

  get: async (id) => {
    database.get(`SELECT * FROM defender_event WHERE id = ?`, [id]);
  },
};

module.exports = {
  database,
  setupDb,

  matchup,
  district,
  hackerAbility,
  hackerEvent,
  defenderAbility,
  defenderEvent,
};
