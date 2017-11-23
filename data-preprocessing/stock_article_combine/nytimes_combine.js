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
var headers = {
    article: {
        datetime: "pub_date",
        epoch: "pub_date_epoch",
        description: "snippet",
        headline: "headline_main"
    },
    stock: {
        date: "date",
        time: "time",
        datetime: "utc",
        close: "close",
        close_8ma: "close_8ma",
        change: "change"
    }
}


function searchStockForSingleArticle(stocks, article) {
    var currArticleEpoch = parseInt( article[headers.article.epoch] );

    // for (let i = 0; i < stocks.length; i++) {
    //     var currStockEpoch = common.dateToEpoch( stocks[i][headers.article.date] );

    //     if (parseInt(currStockEpoch) < parseInt(currArticleEpoch)) {
    //         // move on baby
    //     } else if (parseInt(currStockEpoch) >= parseInt(currArticleEpoch)) {
    //         console.log("match found");
    //         console.log(currArticleEpoch);
    //         console.log(currStockEpoch);
    //         return;
    //     }

    // }

    var diff = Infinity;
    var stockMatch;

    for (let i = 0; i < stocks.length; i++) {
        var currStockEpoch = common.dateToEpoch( stocks[i][headers.stock.datetime] );
        currStockEpoch = parseInt(currStockEpoch);


        var currDiff = currStockEpoch - currArticleEpoch;
        // console.log(currDiff);

        if (currDiff < diff && currDiff >= 0) {
            diff = currDiff;
            stockMatch = stocks[i];
            // console.log("match found");

        }

    }

    return stockMatch;

}

function combineStocksWithArticles(stocks, articles) {
    var combinedData = [];

    for (let i = 0; i < articles.length; i++) {
        var currentArticle = articles[i];
        var matchedStock = searchStockForSingleArticle(stocks, currentArticle);
        var matchedStock_epoch = common.dateToEpoch(matchedStock[headers.stock.datetime]);

        var articleStock = {
            title: currentArticle[headers.article.headline],
            description: currentArticle[headers.article.description],
            article_datetime: currentArticle[headers.article.datetime],
            article_epoch: currentArticle[headers.article.epoch],
            stock_datetime: matchedStock[headers.stock.datetime],
            stock_epoch: matchedStock_epoch,
            stock_close: matchedStock[headers.stock.close],
            stock_8ma_close: matchedStock[headers.stock.close_8ma],
            stock_change: matchedStock[headers.stock.change]
        };
        combinedData.push(articleStock);

    }

    return combinedData;
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
        // var combined = searchStockForSingleArticle(results[1], results[0][0]);
        // console.log(combined);

        var combinedData = combineStocksWithArticles(results[1], results[0]);

        columns = ["title", "description", "article_datetime", "article_epoch", "stock_datetime", "stock_epoch", "stock_close", "stock_8ma_close", "stock_change"];
        var csvCombined = common.convertToCSV(combinedData, columns);
        common.writeToCSVFile("./combined.csv", csvCombined);
    });




}

main();
