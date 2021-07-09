let data;

function getRandomQuote() {
    return $.ajax({
        url: "https://raw.githubusercontent.com/abhi00o7/hindi-quotes-web-crawler/main/hindiMotivationalQuotes.json",
        type: "GET",
        dataType: "json",
        success: function (res) {
            data = res;
        },
        error: function (err) {
            $("#text").text("Sorry, cannot retrieve quote right now. Please, try again in a moment...");
            console.log(err);
        }
    });
}

function append() {
    let random = data.quotes[Math.floor(Math.random() * data.quotes.length)];
    let quote = random.quote;
    let author = random.author;
    $(".quote").animate({
        opacity: 0
    }, 500, function () {
        $(this).animate({
            opacity: 1
        }, 500);
        $("#text").text(quote);
    });
    $(".quote-author").animate({
        opacity: 0
    }, 500, function () {
        $(this).animate({
            opacity: 1
        }, 500);
        $("#author").html(author);
    });
    $("#tweet-quote").attr("href", "twitter.com/intent/tweet?text=" + quote + " -" + author);
}

$(document).ready(function () {
    getRandomQuote().then(() => {
        append();
    });
    $("#new-quote").on("click", append);
});