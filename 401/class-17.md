# Spring Boot and OAuth2
* use Spring Security dependency to make the app secured when I want to make a login (Auth 2.0).
## Single Sign On With GitHub
* github providce us a way to use their authintication by going to this page and [make a new app.](https://github.com/settings/developers).
* to make the auth it should be similar to this.
  *  home page, for example `http://localhost:8080`
  *  then indicate the Authorization callback URL as `http://localhost:8080/login/oauth2/code/github`

* render content on the condition that the user is authenticated, options available of either server-side or client-side.

##### code : 
html
```html
<div class="container unauthenticated">
    With GitHub: <a href="/oauth2/authorization/github">click here</a>
</div>
<div class="container authenticated" style="display:none">
    Logged in as: <span id="user"></span>
</div>

```
**JQUERY**

```jquery
<script type="text/javascript">
    $.get("/user", function(data) {
        $("#user").html(data.name);
        $(".unauthenticated").hide()
        $(".authenticated").show()
    });
</script>

```

**Java Application** 
```java
SpringBootApplication
@RestController
public class SocialApplication {

    @GetMapping("/user")
    public Map<String, Object> user(@AuthenticationPrincipal OAuth2User principal) {
        return Collections.singletonMap("name", principal.getAttribute("name"));
    }

    public static void main(String[] args) {
        SpringApplication.run(SocialApplication.class, args);
    }

}
```

### Making the Home Page Public
* To make the link visible, from file `WebSecurityConfigurerAdapter` change off the security on the home page.
```java
.authorizeRequests(a -> a
                .antMatchers("/", "/error", "/webjars/**").permitAll()
                .anyRequest().authenticated()
            )
```
* @SpringBootApplication amnnotation use WebSecurityConfigurerAdapter to configure security.


#### Add a Logout Button
1. we need the logout button for sure.

so the **html** :
```html

 <button onClick="logout()" class="btn btn-primary">Logout</button>

```

**javascipt** :
```javascript
 then a javascript code:
 var logout = function() {
    $.post("/logout", function() {
        $("#user").html('');
        $(".unauthenticated").show();
        $(".authenticated").hide();
    })
    return true;
}

```

#####  Logout Endpoint
- Spring Security has built in support for a /logout endpoint. that clear the session and invalidate the cookie.
- in `WebSecurityConfigurerAdapter` using a method called `configure()`

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
	// @formatter:off
    http
        // ... existing code here
        .logout(l -> l
            .logoutSuccessUrl("/").permitAll()
        )
        // ... existing code here
    // @formatter:on
}
```