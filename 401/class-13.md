# Read: 13 - Related Resources and Integration Testing
* **Important Note**  all code copied is resourced.
## Working with Relationships in Spring Data REST
how to create relationships in spring mvc.
### One-to-One Relationship
1. **the data mode:**
  *  `@OneToOne` allow me to associate a relation between 2 classes 1 to 1 (I will be using the example from the read).
* and can have the optional` @RestResource` annotation to customize the association resource.
`class Library` : 
```
@OneToOne
    @JoinColumn(name = "address_id")
    @RestResource(path = "libraryAddress", rel="address")
    private Address address;
```

`class Address`
```
 @OneToOne(mappedBy = "address")
  private Library library;
```
* explination: the example create a relation 1 to 1 between adress and library.
  * example used the `address id column` to add it inside library as column that refer to address entity inside adress class.
  * and inside the Address class added mappedby to tell the springMVC I am making 1 to 1 relation to library.


* **Important Note**: We must be careful to have different names for each association resource. Otherwise, will encounter a **JsonMappingException** with the message: “Detected multiple association links with same relation type! Disambiguate association”.

2. **The Repositories:**: now I will create repository for each class and extended it from CrudRepository so they are exposed as resources

### One-to-many Relationship
* A one-to-many relationship is created using the `@OneToMany` and `@ManyToOne` annotations.
* and can have the optional` @RestResource` annotation to customize the association resource.
1. **The Data Model**
* example (also from read to save time):

```
@ManyToOne
    @JoinColumn(name="library_id")
    private Library library;
```

```
@OneToMany(mappedBy = "library")
    private List<Book> books;
```
* explination:
  * Book entity that will represent the **many** end of a relationship with the Library entity:

2. **The Repository**
   * `public interface BookRepository extends CrudRepository<Book, Long> { }`
   * the book resource entity also exposed to make the relation of many books inside our library in the db.

### Many-to-Many Relationship
1. data model
* A many-to-many relationship is extablished with `@ManyToMany` annotation.
* example : 

```
@ManyToMany(cascade = CascadeType.ALL)
    @JoinTable(name = "book_author", 
      joinColumns = @JoinColumn(name = "book_id", referencedColumnName = "id"), 
      inverseJoinColumns = @JoinColumn(name = "author_id", 
      referencedColumnName = "id"))
    private List<Book> books;
```

```
@ManyToMany(mappedBy = "books")
    private List<Author> authors;
```
* explination : the relation between authors and books a book can have many authors and vice versa.

2. The Repository
 * `public interface AuthorRepository extends CrudRepository<Author, Long> { }`
 * expose the authors resource to establish the relationship
## Integration Testing in Spring
* we use it to test the controllers behaviour

1. **Preparation**
* required dependencies `junit-jupiter-engine`, `junit-jupiter-api`, and `Spring test`.
* for asserting results :  `Hamcrest` and `JSON path`
2. **Spring MVC Test Configuration**
   1. Enable Spring in Tests with JUnit 5.
      1. JUnit defines an extension interface through which classes can integrate with the JUnit test. 
      2.  adding the `@ExtendWith` annotation to test classes and specifying the extension class to load. To run the Spring test, use `SpringExtension.class`.
      3.  `@ContextConfiguration` provide the `ApplicationConfig.class` config class, which loads the configuration needed for test test.
      4.  `@WebAppConfiguration`, will load the web application context, it search from root and to override it i provide `value=""`
      5. example :
```
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = { ApplicationConfig.class })
@WebAppConfiguration
public class GreetControllerIntegrationTest {
    ....
}
```
[resource](https://www.baeldung.com/integration-testing-in-spring#1-enable-spring-in-tests-with-junit-5).
3. **The WebApplicationContext Object**
   1. provides a web application configuration, it load app beans and controllers into context.
4. **Mocking Web Context Beans**
   1. encapsulate app beans and make them available for testing.
   2. usage:
   3. **Note :** initialize the `mockMvc` object in the `@BeforeEach` annotated method so I don't have to initialize it inside every test.


```
private MockMvc mockMvc;
@BeforeEach
public void setup() throws Exception {
    this.mockMvc = MockMvcBuilders.webAppContextSetup(this.webApplicationContext).build();
}
```
[resource](https://www.baeldung.com/integration-testing-in-spring#3-mocking-web-context-beans)

5. **Verify Test Configuration**

```
@Test
public void givenWac_whenServletContext_thenItProvidesGreetController() {
    ServletContext servletContext = webApplicationContext.getServletContext();
    
    Assert.assertNotNull(servletContext);
    Assert.assertTrue(servletContext instanceof MockServletContext);
    Assert.assertNotNull(webApplicationContext.getBean("greetController"));
}
```
[resource](https://www.baeldung.com/integration-testing-in-spring#4-verify-test-configuration).

### Writing Integration Tests
```
@Test
public void givenHomePageURI_whenMockMVC_thenReturnsIndexJSPViewName() {
    this.mockMvc.perform(get("/homePage")).andDo(print())
      .andExpect(view().name("index"));
}
```
* explination: 
  * **perform()** call a GET request, return result and then I can create assertion.
  * `andDo(print())`  print the request and response.
  * `andExpect()` expect the provided argument from requesting the **url**, for example on `/homePage` will load the `inedx.html`.

## MockMvc Limitations
*  uses a subclass of the `DispatcherServlet` to handle test requests.
