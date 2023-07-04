document.addEventListener('DOMContentLoaded', function() {
  var downloadBtn = document.getElementById('downloadBtn');
  
  downloadBtn.addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      var tab = tabs[0];
      var url = tab.url;
      
      if (isYouTubeUrl(url)) {
        sendRequest(url);
      } else {
        console.log('Not a YouTube video.');
      }
    });
  });
});

function isYouTubeUrl(url) {
  // You can implement your own validation logic here
  return url.includes('youtube.com') || url.includes('youtu.be');
}

function sendRequest(url) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:8000', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      console.log('Request sent successfully.');
    }
  };
  xhr.send(JSON.stringify({url: url}));
}
