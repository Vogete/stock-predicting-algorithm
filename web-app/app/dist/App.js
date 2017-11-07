"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var config_1 = require("./config/config");
var express = require("express");
var logger = require("morgan");
var bodyParser = require("body-parser");
var fs = require("file-system");
var App = (function () {
    function App() {
        this.app = express();
        this.middleware();
        this.routes();
    }
    App.prototype.middleware = function () {
        this.app.use(logger('dev'));
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({ extended: false }));
    };
    App.prototype.routes = function () {
        var router = express.Router();
        router.get('/', function (req, res, next) {
            var indexHtml = fs.readFileSync(config_1.default.paths.views.index, "utf8");
            console.log("test2");
            res.send(indexHtml);
        });
        this.app.use('/', router);
        this.app.use('/js', express.static(config_1.default.paths.folders.js));
        this.app.use('/css', express.static(config_1.default.paths.folders.css));
        this.app.use('/assets', express.static(config_1.default.paths.folders.assets));
    };
    return App;
}());
exports.default = new App().app;
