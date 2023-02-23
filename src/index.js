#!/usr/bin/env Node
require("dotenv").config();
const http = require("http");

const db = require("./app/db");

const hostname = process.env.hostname,
  port = process.env.port;

const app = require("./app/server");
app.set("port", port);

const server = http.createServer(app);

server.on("connection", (socket) => {
  server.once("close", () => {
    db.close();
  });
});

server.listen(port, hostname, () => {
  console.log(`server running at http://${hostname}:${port}/`);
});
