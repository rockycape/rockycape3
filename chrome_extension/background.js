chrome.webNavigation.onCompleted.addListener(function(details) {
    chrome.tabs.get(details.tabId, function(tab) {
      if (tab.url.includes("smh.com.au")) {
        const newUrl = tab.url.replace("smh.com.au", "theage.com.au");
        chrome.tabs.update(tab.id, {url: newUrl});
      }
    });
  }, {url: [{hostContains: "smh.com.au"}]});