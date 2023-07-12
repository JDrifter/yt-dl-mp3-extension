chrome.browserAction.onClicked.addListener(function(tab) {
  var url = tab.url;

  if (isYouTubeUrl(url)) {
    sendRequest(url);
  } else {
    console.log('Not a YouTube video.');
  }
});

function isYouTubeUrl(url) {
  // You can implement your own validation logic here
  return url.includes('youtube.com') || url.includes('youtu.be');
}

function sendRequest(url) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:8000', true); // Here you can add your server ip if you want 
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      console.log('Request sent successfully.');
    }
  };

  url = url.substring(0, 43);
  console.log(url);
  xhr.send(JSON.stringify({url: url}));
}
