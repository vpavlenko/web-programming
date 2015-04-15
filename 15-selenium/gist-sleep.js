var webdriver = require('selenium-webdriver');
var browser = new webdriver.Builder().usingServer().
    withCapabilities({'browserName': 'chrome'}).build();

var TEXT = 'webdriver rocks!';

browser.get('https://gist.github.com/');

browser.findElement({css: '.input'}).click();

browser.switchTo().activeElement().sendKeys(TEXT);

browser.findElement({css: '.js-create-gist'}).click();

browser.sleep(10000);

browser.findElement({css: '#file-gistfile1-txt-LC1'}).getText().then(function(value) {
    console.log(value);
    browser.quit();
});
