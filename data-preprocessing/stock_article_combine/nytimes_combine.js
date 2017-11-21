var common = require("../common.js");


// - title
// - descripton (vagy snippet vagy mi)
// - pubdate_epoch
// - pubdate_human
// - stock_date_epoch
// - stock_date_human
// - close
// - 8ma_close
// - change
var stockPath = "../../assets/stock/AAPL/datetime-utc-close-8ma-change/AAPL-60min.csv";
var articlePath = "../../assets/news_articles/nytimes/nytimes-articles.csv";

function main() {

    var stockOptions = {
        delimiter: ";"
    };

    var promiseArticle = common.readFromCSVFile(articlePath);
    var promiseStock = common.readFromCSVFile(stockPath, stockOptions);

    Promise.all([promiseArticle, promiseStock]).then(results => {
        console.log(results[0]);
    });



}

main();
