class Config {

    public defaultPort = 3000;

    private globalPath = __dirname + "/../";

    public paths = {
        root: this.globalPath,
        models: this.globalPath + 'models/',
        folders:{
            views: this.globalPath + 'views/',
            js: this.globalPath + 'js/',
            css: this.globalPath + 'css/',
            assets: this.globalPath + 'assets/'
        },
        views: {
            index: this.globalPath + 'index.html'
        }
    };


    constructor() {

    }

}

export default new Config();
