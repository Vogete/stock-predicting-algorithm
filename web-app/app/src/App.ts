import Config from './config/config';

import * as path from 'path';
import * as express from 'express';
import * as logger from 'morgan';
import * as bodyParser from 'body-parser';
import * as fs from "file-system";


// Creates and configures an ExpressJS web server.
class App {

    // ref to Express instance
    public app: express.Application;

    //Run configuration methods on the Express instance.
    constructor() {
        this.app = express();
        this.middleware();
        this.routes();
    }

    // Configure Express middleware.
    private middleware(): void {
        this.app.use(logger('dev'));
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({ extended: false }));
    }

    // Configure API endpoints.
    private routes(): void {

        /* This is just to get up and running, and to make sure what we've got is
         * working so far. This function will change when we start to add more
         * API endpoints */

         let router = express.Router();

        // Main route handler
        router.get('/', (req, res, next) => {
            var indexHtml = fs.readFileSync(Config.paths.views.index, "utf8");
            console.log("test2");

            res.send(indexHtml);

        });
        this.app.use('/', router);



        // Setting JS, CSS and assets folder to be served as regular folders, not routes
        this.app.use('/js', express.static(Config.paths.folders.js));
        this.app.use('/css', express.static(Config.paths.folders.css));
        this.app.use('/assets', express.static(Config.paths.folders.assets));


    }

}

export default new App().app;
