chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.url) {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');

    let requestOptions = {
      method: 'POST',
      headers: headers,
      body: JSON.stringify({url: changeInfo.url}),
      redirect: 'follow'
    };

    fetch('http://localhost:5000/report', requestOptions)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
      })
      .catch(error => console.log('Fetch error: ', error));
  }
});
