

// Make an HTTP GET Request 
export const HTTPget = async (url) => {
  
    // Awaiting for fetch response
    const response = await fetch(url, {
        method: 'GET',
    });

    // Awaiting for response.json()
    const resData = await response.json();

    // Returning result data
    return resData;
}


export const HTTPpost = async (url, data) => {
  
    // Awaiting for fetch response and defining method, headers and body  
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

