const db = require("./db");

class Ability {
  constructor(name, description)
  {
    this.name = name;
    this.description = description;
  }
}

class CityAbility extends Ability {
  constructor(name, description, matchup) {
    super(name, description);
    this.matchup = matchup;
  }
}

class HackerAbility extends Ability {
  constructor(name, description, damage) {
    super(name, description)
    this.damage = damage
  }
}

class Event {

}

async function test() {
  console.log(await db.getData())
  console.log("Game Test!");
}

module.exports = {
  test,
};
 