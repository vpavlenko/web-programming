var webdriver = require('selenium-webdriver');
var browser = new webdriver.Builder().usingServer().
    withCapabilities({'browserName': 'chrome'}).build();

var TEXT = 'webdriver rocks!';

browser.get('https://gist.github.com/');

browser.findElement({css: '.input'}).click();

browser.switchTo().activeElement().sendKeys(TEXT);

browser.findElement({css: '.js-create-gist'}).click();

var FIRST_LINE_SELECTOR = {css: '#file-gistfile1-txt-LC1'};

browser.wait(function() {
    return browser.isElementPresent(FIRST_LINE_SELECTOR);
}, 10000);

browser.findElement(FIRST_LINE_SELECTOR).getText().then(function(savedText) {
    console.log(savedText);
    browser.quit();
});
