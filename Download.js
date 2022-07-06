const { app, BrowserWindow } = require('electron');
const electronDl = require('electron-dl');

electronDl();

let win;
(async() => {
    await app.whenReady();
    win = new BrowserWindow();
})();