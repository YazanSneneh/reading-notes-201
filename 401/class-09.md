# Read: 09 - WRRC and Java

## The HTTP Request Lifecycle
1. **Local Processing**: it's what happen when i perform an action over the internet like enter a query to go to google.com.
   * `<protocol>://<host><:optional port>/<path/to/resource><?query>`, in the url feild.
   * When I make a request the browser extract the request information, these information are:
     * the protocol which is the http.
     * port and it's optional.
     * destination, (www.google.com) for example.
     * the query string whatever come after **?** in **key=pair** value.
   * Browser now have the hostName (that is google.com) Then the browser will look for IP address of it in the it's cache then cache of the router, then the DNS cache(as far as i know it store the last 10 Addresses request).
2. **Resolve an IP**:
   * resolving IP locally process:
        1. browser look for IP in it's cache.
           * when it fail it make a DNS request using UDP, that request contain the DNS configuration of my DNS server and my IP adress(to send me back the result) in it's header.
        2. The request walk throught many devices to reach my DNS server.
           * each layer my request arrive, route my request to the next device that concerned in my request.
        3. when the request reach the DNS server, it will start looking for an IP adress that hold the host name I provided.
           * when it fail it will send it to another DNS server.
           * when it fail it will send a failure response.
           * if it sucess
        4. when Sucess it send back the requested IP adress.

3. **Establish a TCP Connection**
   *  when i successfully have IP adress, I will make a TCP connection so i be able to make an http request.
   * The TCP connection processed in 3 steps.
     1. Send a random request, the server with the ip recieve it and there is passive port is open and listening for this kind of request.
     2. the server receive it and it confirm it, send confirmation message.
     3. then data is being send, and 3rd message send back that connection confirmed.

4. **Send an HTTP Request**
   1. when client have IP address and TCP connection can send an http request.
   2. The request is being send and consist of two parts:
      1. the request header, contain information about the request.
      2. the request body (optional but usually json data).

   3. when request is received, and confirm, Server will start looking for requested data.
      1. it will prepare a response that contain also header and body:
      2. the header contain response info like status code indicate success or failure, and a message.
      3. the body contain optional json data.
   4. when the response is generated, it will be sent back throught the TCP protocol.
5. **Tearing Down and Cleaning Up**
* when response is recieve, my the browser will close the TCP connection.
* then it will start proccessing the data if it's html or external resources like links, so it will parse the files for example html to generate html page.

[Article resource](https://dev.to/dangolant/things-i-brushed-up-on-this-week-the-http-request-lifecycle-)

## Simple HTTP Request in Java
 * HttpUrlConnection:
   * a class in java allow me to make http request.
   * disadvantage of using this library, the code written can be a large.

 * Creating a Request:
   * openConnection() allow me to create an instance of the class **HttpUrlConnection**
   * I can use it for all kind of requests (get, put, delete, add).
   * example: of making a request.

```
URL url = new URL("http://example.com");
HttpURLConnection connection = (HttpURLConnection) url.openConnection();
connection.setRequestMethod("GET");

```

* Adding Request Parameters
  * `con.setDoOutPut(true);` a method allow me to add params to request by setting it to true.

* Setting Request Headers
  * `setRequestProperty() ` allow me to add header to my request.

* Configuring Timeouts
  * **HttpUrlConnection**  allow me to set interval to determine time waiting for connection to be done to read data.
  *  `setConnectTimeout() and setReadTimeout()`  can be used to do the job.

```
con.setConnectTimeout(5000);
con.setReadTimeout(5000);

```

* Reading the Response
  * to read the response, i should set java to parse the input stream of the **HttpUrlConnection** 
  * To execute the request, we can use the `getResponseCode(), connect(), getInputStream() or getOutputStream()` methods.
