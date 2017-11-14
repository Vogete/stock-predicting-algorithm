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



var from = new Date();
var until = new Date();
var dayInterval = 1;


function getDailyNYTArticles(begin_date, end_date, pageOffset = 0) {
    //Documentation: http://developer.nytimes.com/article_search_v2.json#/Documentation/GET/articlesearch.json

    var dataFile = dateConverter(begin_date) + "-" + dateConverter(end_date)+'_nytimes.json';

    // options
    var URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json';
    var API_KEY = '9d8594dce0f14204a8d25d50428b3387';
    var searchTerm = "Apple Inc";


    request.get({
        url: URL,
        qs: {
            'api-key': API_KEY,
            'q': searchTerm,
            'begin_date': dateConverter(begin_date),
            'end_date': dateConverter(end_date),
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

function dateConverter(date) {
    return date.yyyymmdd();
}




(function main () {
    until.setDate(until.getDate());
    from.setFullYear(2017, 10, 1);

    console.log(dateConverter(from) + " - " + dateConverter(until));
    console.log('------------------------');

    var currentDay = new Date(until);

    var apiCallInterval = setInterval(function () {
        var intervalStartDate = new Date();
        intervalStartDate.setDate(currentDay.getDate()-dayInterval);

        console.log(dateConverter(currentDay) + "-" + dateConverter(intervalStartDate));
        getDailyNYTArticles(intervalStartDate, currentDay);

        currentDay.setDate(currentDay.getDate() - 1 );

        if (currentDay < from) {
            clearInterval(apiCallInterval)
        }
    }, 1000);

    // do {

    // } while (currentDay >= from);

})();
