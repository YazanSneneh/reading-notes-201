# Read: 11 - Spring
* If I want to create a spring project i navigate to this website [https://start.spring.io/](https://start.spring.io/).
* it does most of configuration for me.
* all configurations in `gradle.build` file.

##### creating and downloading project.
1. In website mentioned I should navigate to it then.
2. choose java as language.
3. choose gradle build.
4. add dependencies Spring Web, Thymeleaf, and Spring Boot DevTools.
5. and generate.

### Create a Web Controller
* to handle web requests in java or spring I must identify method as controller. e `@Controller`
* inside controller `@GetMapping("/someUrl")` navigate get requests to the `/someUrl` to this controller.
* `@RequestParam` assign value to key, example `@RequestParam(age=20, name="whatever")`.
* the method implemented into html using templagte engine In our case **Thymeleaf**.

```
<!DOCTYPE HTML>

<head> 
    <title>card</title> 
</head>
<body>
    <p th:text="'Age: ' + ${age}" />
    <p th:text="'Hello, ' + ${name} + '!'" />
</body>
</html>
```

### Spring Boot Devtools 
*  spring-boot-devtools speed up development process.
*  for example part of developing applications is that always debugging and changing, so it's consuming a lot of time to keep running and stop application etc...

### SO what it does :
*  Enables hot swapping.
*  Switches template engines to disable caching.
*  Enables LiveReload to automatically refresh the browser.
*  Other reasonable defaults based on development instead of production.

### Run the Application
* Spring Initializr creates an application class for me.
* class contain following:
  * `@Configuration`: Tags the class as a source of for the application context.
  * `@EnableAutoConfiguration` : tell spring to add beans based on classpath.
  * `@ComponentScan` make spring to search for components, configs and services.
* `main()` method uses Spring Boot’s `SpringApplication.run()` method to launch an application.
  * like this : 
```
public static void main(String[] args) {
		SpringApplication.run(ServingWebContentApplication.class, args);
	}

```

### Build an executable JAR
* to run app from terminal I can use gradle or maven gradle.
* use **gradle** to run the app:
  * `./gradlew bootRun`
  

### Test the Application
* when i run `./gradlew bootRun` can open it in browser.
* to do so I can find it on this url http://localhost:8080/greeting
* If i want to change name i can change parameter value to do so I can hit this url :
  * http://localhost:8080/greeting?name=Yazan

##### Add a Home Page
* I can add Static resources, including HTML and JavaScript and CSS in resources file that in src folder.
* By default, Spring Boot serves static resources from resources in the classpath at `/static` or `/public`

## Spring MVC and Thymeleaf: how to access data from templates
* the spring app contain model and controller.
  * controller prepare the model with data then select a viewer to render it.
  * Model map make the process abstract.
  [resource](https://www.thymeleaf.org/doc/articles/springmvcaccessdata.html)

1. **Spring model attributes**
* during the execution the Spring get the data that found and inject it to the **thymeleaf or any rendering engine**.
  * there is variable should be in the view engine with **key** specified and connected with model in order for proper injection.
* That's wht it's called **model mapping**.
* **Ways of injecting data in thymeleaf:**
  * in any way i am injecting to thymeleaf I will add the variable in model and it should be available in thymeleaf or any template engine.
  1. **ddAttribute()** method.
```
 @RequestMapping(value = "message", method = RequestMethod.GET)
        public String messages(Model model) {
            model.addAttribute("messages", messageRepository.findAll());
            return "message/list";
        }
```
[resource](https://www.thymeleaf.org/doc/articles/springmvcaccessdata.html)

2. `ModelAndView class`
```
 @RequestMapping(value = "message", method = RequestMethod.GET)
        public ModelAndView messages() {
            ModelAndView mav = new ModelAndView("message/list");
            mav.addObject("messages", messageRepository.findAll());
            return mav;
        }
```
 
[resource](https://www.thymeleaf.org/doc/articles/springmvcaccessdata.html).

* now for data to be accessed in thymeleaf I must specify attribute  it should be between `${attributeVariable}` exactly like **Template literals** in javaScript.
example : 
```
 <tr th:each="message : ${messages}">
            <td th:text="${message.id}">1</td>
            <td><a href="#" th:text="${message.title}">Title ...</a></td>
            <td th:text="${message.text}">Text ...</td>
        </tr>
```
[resource](https://www.thymeleaf.org/doc/articles/springmvcaccessdata.html).

2. **Request parameters**
   * there parameters are coming from client (URL Query parameters).
   * in order to access these parameters i must type `<p th:text="${param.query}"></p>`.
   * if i have multi values in parameter I will be working with them like i am working with list.
     * `<p th:text="${param.query[0]}">`
3. **Session attributes**
   * the session attribute can be accessed like params.
   * in controller: `session.setAttribute("mySessionAttribute", "someValue");`
   * in thymeleaf to access it : `<p th:text="${session.mySessionAttribute}" th:unless="${session == null}">[...]</p>`
4. **ServletContext attributes**
 * since i dont know what exactly is this yet: [resource](https://www.thymeleaf.org/doc/articles/springmvcaccessdata.html)
* The ServletContext attributes are shared between requests and sessions. In order to access ServletContext attributes in Thymeleaf you can use the #servletContext. prefix: 
* Example:
```
  <table>
                <tr>
                    <td>My context attribute</td>
                    <!-- Retrieves the ServletContext attribute 'myContextAttribute' -->
                    <td th:text="${#servletContext.getAttribute('myContextAttribute')}">42</td>
                </tr>
                <tr th:each="attr : ${#servletContext.getAttributeNames()}">
                    <td th:text="${attr}">javax.servlet.context.tempdir</td>
                    <td th:text="${#servletContext.getAttribute(attr)}">/tmp</td>
                </tr>
            </table>
```