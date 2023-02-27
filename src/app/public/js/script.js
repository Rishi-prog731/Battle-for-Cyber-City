async function connectToServer() {
  const ws = new WebSocket(`ws://${hostname}:${port}/`);
  return new Promise((resolve, reject) => {
    const timer = setInterval(() => {
      if (ws.readyState === 1) {
        clearInterval(timer);
        resolve(ws);
      }
    }, 10);
  });
}

const ws = await connectToServer();

document.body.onmousemove = (evt) => {
  const messageBody = { x: evt.clientX, y: evt.clientY };
  ws.send(JSON.stringify(messageBody));
};
