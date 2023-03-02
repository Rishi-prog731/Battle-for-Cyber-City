#!/usr/bin/env Node
require("dotenv").config();
const http = require("http");

const hostname = process.env.hostname,
  port = process.env.port;

const app = require("./app/server");
app.set("port", port);

const server = http.createServer(app);

const expressWs = require("express-ws")(app, server);

server.on("connection", (socket) => {});

server.listen(port, hostname, () => {
  console.log(`server running at http://${hostname}:${port}/`);
});
