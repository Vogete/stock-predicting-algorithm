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

function searchStockForArticle(stocks, article) {
    var dateHeader = {
        article: "pub_date_epoch",
        stock: "utc"
    };

    var currArticleEpoch = article[dateHeader.article];

    for (let i = 0; i < stocks.length; i++) {
        var currStockEpoch = common.dateToEpoch( stocks[i][dateHeader.stock] );

        if (parseInt(currStockEpoch) < parseInt(currArticleEpoch)) {
            // move on baby

        } else if (parseInt(currStockEpoch) >= parseInt(currArticleEpoch)) {
            console.log("match found");
            console.log(currArticleEpoch);
            console.log(currStockEpoch);
            return;
        }

    }


}

function main() {

    var articlePath = "../../assets/news_articles/nytimes/nytimes-articles.csv";
    var stockPath = "../../assets/stock/AAPL/datetime-utc-close-8ma-change/AAPL-60min.csv";
    var stockOptions = {
        delimiter: ";"
    };

    var promiseArticle = common.readFromCSVFile(articlePath);
    var promiseStock = common.readFromCSVFile(stockPath, stockOptions);

    Promise.all([promiseArticle, promiseStock]).then(results => {
        // console.log(results[1]);
        searchStockForArticle(results[1], results[0][1]);
    });




}

main();
