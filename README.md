# CeneoScraper

## Single  opinion structure

|Element|Selector|Variable|
|---|---|---|
|Opinion|div.js_product-review|opinion|
|Opinion ID|div\["data-entry-id"\]|opinion_id|
|Author|span.user-post__author-name|author|
|Recommendation|span.user-post__author-recomendation- > em| rcmd |
|Stars score|span.user-post__score-count|score|
|Content|div.user-post__text|content|
|List of advantages|div.review-feature__title--positives ~ div.review-feature__title|pros|
|List of disadvantages|div.review-feature__title--negatives ~ div.review-feature__title|cons|
|Date of posting opinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|
|Date of purchasing product|span.user-post__published > time:nth-child(2)\["datetime"\] |bought_on|
|For how many users usefull|button.js_vote-yes > span|usefull|
|For how many users useless|button.js_vote-no > span|useless|

## Stages of project

1)Extraction of elements for a single opinion to separate variables
2)Extraction of elements for a single opinion to separate variables(directory)
3)Extraction of all opinions form a single page to list
4)Extraction of all opinions for certainproduct and saving it to file
5)Code refactoring and optimization
    a)Definition of function for extracting single elements of page from HTML code
    b)Creation of dictionary that describes opinions with selectors for particular opinion's elements
    c)Using dictionary comprehension to eextract all opinion's elements on the basis of opinion's structure dictionary
6)
