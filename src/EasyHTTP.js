

// Make an HTTP GET Request 

// Make an HTTP POST Request
// export const HTTPpost = (url, data) => {
//     fetch(`${url}`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(data)
//     })
//     .then(response => response.json())
//     .then(data => console.log(data))
// }

export const HTTPpost = async (url, data) => {
  
    // Awaiting for fetch response and 
    // defining method, headers and body  
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    // Awaiting response.json()
    const resData = await response.json();

    // Returning result data
    return resData;
}

