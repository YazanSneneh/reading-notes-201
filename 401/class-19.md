# Using WebSocket to build an interactive web application

* WebSoecket is a protocol work differently from http.
  * http depend on the rquest response cycle.
  * so the communication is one direction.
    * either request.
    * or response.
  * webSocket on the other hand:
    * when a user send a request, it open a connection with server known as hand shake.
    * the server will open a connection and hold it.
    * the connection will remain opened until someone close it.

### Spring Initializr
* Gradle:

```java
dependencies {
implementation 'org.webjars:webjars-locator-core'
implementation 'org.webjars:sockjs-client:1.0.2'
implementation 'org.webjars:stomp-websocket:2.3.3'
implementation 'org.webjars:bootstrap:3.3.7'
implementation 'org.webjars:jquery:3.1.1-1'
}

```

### Create a Resource Representation Class
* after set up the project and build system, I can Create STOMP message service.

* **Service Interaction**
  * service will accept messages that contain a name in a **STOMP** message body as a **JSON object**.
  * To model the message create a plain old Java object with a name of property and a corresponding getPropertyName().
  * receiving the message and extracting the property, the service will process it by creating a greeting and publishing that greeting on a separate queue to which the client is subscribed.
  * Spring uses **Jackson JSON** library to automatically marshal instances of type Greeting into JSON.


### Create a Message-handling Controller
* STOMP messages can be routed to @Controller classes.

example : 
 ```java
 @Controller
public class GreetingController {


  @MessageMapping("/hello")
  @SendTo("/topic/greetings")
  public Greeting greeting(HelloMessage message) throws Exception {
    Thread.sleep(1000); // simulated delay
    return new Greeting("Hello, " + HtmlUtils.htmlEscape(message.getName()) + "!");
  }

}
 
 ```

 ### Configure Spring for STOMP messaging
 * we can configure Spring to enable WebSocket and STOMP messaging.
  1. Create a Java class named WebSocketConfig.

example : 
 ```java
 @Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

  @Override
  public void configureMessageBroker(MessageBrokerRegistry config) {
    config.enableSimpleBroker("/topic");
    config.setApplicationDestinationPrefixes("/app");
  }

  @Override
  public void registerStompEndpoints(StompEndpointRegistry registry) {
    registry.addEndpoint("/gs-guide-websocket").withSockJS();
  }

 ```

* on the client side We need javascript to comeplete the process.