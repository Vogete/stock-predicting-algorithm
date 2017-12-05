var request = require('request');
var jsonfile = require('jsonfile');
var common = require('../common.js');


function getDailyNYTArticles(begin_date, end_date, pageOffset = 0) {
    //Documentation: http://developer.nytimes.com/article_search_v2.json#/Documentation/GET/articlesearch.json

    var dataFile = "./data/"+common.dateConverter(begin_date) + "-" + common.dateConverter(end_date)+'_nytimes.json';

    // options
    var URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json';
    // var API_KEY = '9d8594dce0f14204a8d25d50428b3387'; //original
    // var API_KEY = '58cdd37324864d8996857fbbe30000ce';
    // var API_KEY = '7450b068d8754af696609dd65e115aee';
    var API_KEY = '4cde56a0f68b4e709b563bff50098fd1';
    var searchTerm = "apple";
    var fq = '("apple" or "iphone" or "mac") and -"fruit"';


    request.get({
        url: URL,
        qs: {
            'api-key': API_KEY,
            'q': searchTerm,
            'fq': fq,
            'begin_date': common.dateConverter(begin_date),
            'end_date': common.dateConverter(end_date),
            'page': pageOffset

        },
    }, function (err, response, body) {
        var data = JSON.parse(body);

        console.log(data);

        if (data.response.meta.hits > 10) {
            console.log("WARNING: " + data.response.meta.hits + " results found!");
        }

        // NYTimes JSON format: data.response.docs
        jsonfile.writeFileSync(dataFile, data.response.docs);
        console.log(data);

    });

}


(function main () {
    var from = new Date();
    var until = new Date();
    var dayInterval = 1;

    from.setFullYear(2016, 6-1, 6);
    until.setFullYear(2016, 6-1, 9);

    console.log("Full Interval: " + common.dateConverter(until) + " - " + common.dateConverter(from));
    console.log('------------------------');

    var currentDay = new Date(until);

    var apiCallInterval = setInterval(function () {
        var intervalStartDate = new Date();
        intervalStartDate = common.subtractDay(currentDay, dayInterval);

        console.log(common.dateConverter(currentDay) + "-" + common.dateConverter(intervalStartDate));
        getDailyNYTArticles(intervalStartDate, currentDay);

        currentDay = common.subtractDay(currentDay, dayInterval);

        if (currentDay < from) {
            clearInterval(apiCallInterval);
        }
    }, 1000); // interval for API Should be at least 1000, otherwise the system will lock it



})();
