#!/usr/bin/env Node
require("dotenv").config();
const http = require("http");
const ws = require("ws");

const game = require("./app/game").test();

const hostname = process.env.hostname,
  port = process.env.port;

const app = require("./app/server");
app.set("port", port);

const server = http.createServer(app);
const wss = new ws.WebSocket.Server({ server });

wss.on("connection", (ws) => {
  ws.on("message", (message) => {
    ws.send(`Hello, you sent -> ${message}`);
  });

  ws.send("Hi there, I am a WebSocket server");
});

server.on("connection", (socket) => {});

server.listen(port, hostname, () => {
  console.log(`server running at http://${hostname}:${port}/`);
});
