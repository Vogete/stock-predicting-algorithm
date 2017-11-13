"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Config = (function () {
    function Config() {
        this.defaultPort = 3000;
        this.globalPath = __dirname + "/../";
        this.paths = {
            root: this.globalPath,
            models: this.globalPath + 'models/',
            folders: {
                views: this.globalPath + 'views/',
                js: this.globalPath + 'js/',
                css: this.globalPath + 'css/',
                assets: this.globalPath + 'assets/'
            },
            views: {
                index: this.globalPath + 'index.html'
            }
        };
    }
    return Config;
}());
exports.default = new Config();
