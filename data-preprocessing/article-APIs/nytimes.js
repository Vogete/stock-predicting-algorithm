var request = require('request');
var jsonfile = require('jsonfile')

//Documentation: http://developer.nytimes.com/article_search_v2.json#/Documentation/GET/articlesearch.json

// settings
var dataFile = 'data_nytimes.json';

var URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json';
var API_KEY = '9d8594dce0f14204a8d25d50428b3387';

var fromDate = 20171112;
var untilDate = 20171113;
var pageOffset = 0;
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
