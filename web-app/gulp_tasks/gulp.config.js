// Global paths for client
var globalPath = {
    dist : "app/dist/",
    src: "app/src/",
    npm : "node_modules/"
};

module.exports = {
    libs: {
        // JavaScript Libraries (libs.js)
        js: [

        ],

        // Typescript definition types
        types: [

        ],

        // CSS Libraries
        css: [

        ]
    },

    src: {
        root: globalPath.src,
        copy_index: globalPath.src + 'views/index/index.html',
        copy_assets: globalPath.src + 'assets/**/*.*',

        clientTS: [
            // TS files to compile. Order matters!

            globalPath.src + "views/index/main.ts"
        ],

        serverTS: [
            globalPath.src + "config/config.ts",
            globalPath.src + "server.ts",
            globalPath.src + "App.ts"
        ],

        // JavaScript to watch
        js: [
            globalPath.src + "App.js",
            globalPath.src + "server.js",
            globalPath.src + "views/**/*.js",
            globalPath.src + "config/**/*.js"
        ],

        // sass to compile
        sass: [
            globalPath.src + "sass/**/*.scss"
        ]

    },

    dist: {
        root: globalPath.dist,
        js: globalPath.dist + "js/",
        css: globalPath.dist + "css/",
        assets: globalPath.dist + "assets/"
    }

};
