var request = require('request');
var jsonfile = require('jsonfile');

Date.prototype.yyyymmdd = function () {
    var mm = this.getMonth() + 1; // getMonth() is zero-based
    var dd = this.getDate();

    return [this.getFullYear(),
        (mm > 9 ? '' : '0') + mm,
        (dd > 9 ? '' : '0') + dd
    ].join('');
};


//Documentation: http://developer.nytimes.com/article_search_v2.json#/Documentation/GET/articlesearch.json


function getDailyNYTArticles(fromDate, untilDate, pageOffset = 0) {
    var dataFile = 'data_nytimes.json';

    var URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json';
    var API_KEY = '9d8594dce0f14204a8d25d50428b3387';
    var searchTerm = "Apple Inc";

    request.get({
        url: URL,
        qs: {
            'api-key': API_KEY,
            'q': searchTerm,
            'end_date': fromDate,
            'begin_date': untilDate,
            'page': pageOffset

        },
    }, function (err, response, body) {
        data = JSON.parse(body);
        jsonfile.writeFileSync(dataFile, data.response);
        console.log(data);
    });

}



var from = new Date();
var until = new Date();
from.setDate(from.getDate() - 0);
until.setDate(from.getDate() - 1 );


console.log(from.yyyymmdd() + " - " + until.yyyymmdd());
getDailyNYTArticles(from.yyyymmdd(), until.yyyymmdd());
