# Sending form data 
 * data is sent over http server to a server e.g. Apache and the server will response using http as well.
 * when user want to view something they send it over the url.
 * but forms allow user to send data over the http.
 * so it's basically a way that enable user to send data to server.

##  Client side.
 * so basically the user need a form to send data as mentioned earlier.
 * the most important properties needed when user submit a form are action and method.
 * **action**: specify where the data will be sedn, to which **URL** or a (route on that path to handle the request). 
     * **NOTE:** if action method is not specified, data from will be sent to the same page where the form live e.g. (/home)
     * **Absolute URL** is an external url live on a different server, lets say i will redirect user to google.com.
     * **relative URL**: it's a url or a path live on the same server where the form live.
 * **method attribute**: define how data will be sent.
     * **get:** it will be sent over in the url, or lets say i am **requesting data from server or page to view**. 
     * **post**: i am asking server to store data and this data should be secret, e.g. credit card data, and it's sent to the body.


## On the server side: retrieving the data
  * Whichever HTTP method I choose, the server receives a string that will be parsed in order to get the data as a list of key/value pairs.
  *  The way you access this list depends on the development platform i use and on any specific frameworks i use.
  *  **EXPRESS** in my case which is going to be recieved in the query object or the body object