# Espresso
- Used to write android UI Tests.
- Example of an Espresso test:
```java
@Test
public void greeterSaysHello() {
    onView(withId(R.id.name_field)).perform(typeText("Steve"));
    onView(withId(R.id.greet_button)).perform(click());
    onView(withText("Hello Steve!")).check(matches(isDisplayed()));
}
```
- Espresso tests state expectations, interactions, and assertions clearly without the distraction of boilerplate content.
- 

### Target audience
- it's targeting developers who relay on automated testing.
- it can be used for black box testing.
- Espresso’s full power is unlocked by those who are familiar with the codebase under test, meaning those who implement this type of testing they know how to benefit from Espresso.

### Synchronization capabilities
- `onView()` is always used to invoke testing.
- expresso won't implement testing when 3 conditions occurs:
  - message queue is empty.
  -  no instances of AsyncTask currently executing a task.
  -  All developer-defined idling resources are idle.
- performing these checks, Espresso substantially increases the likelihood that only one UI action or assertion can occur at any given time. [resource](https://developer.android.com/training/testing/espresso).

### Packages
- `espresso-core` - Contains core and basic View matchers, actions, and assertions. See Basics and Recipes.
- `espresso-web` - Contains resources for WebView support.
- `espresso-idling`-resource - Espresso's mechanism for synchronization with background jobs.
- `espresso-contrib` - External contributions that contain DatePicker, RecyclerView and Drawer actions, accessibility checks, and CountingIdlingResource.
- `espresso-intents` - Extension to validate and stub intents for hermetic testing.
- `espresso-remote` - Location of Espresso's multi-process functionality.

- **Note to rememeber:** the reason i copied paseted here is because it's new topic and i might want to diec more into details [resource](https://developer.android.com/training/testing/espresso)

# Create UI tests with Espresso Test Recorder
- allow me to write tests for my app without writing any test case.
- this is done by recording interactions and add assertions to that snapshot.
- Test Recorder takes the saved recording and generate UI test.
- Test Recorder writes tests based on the Espresso Testing framework.
- Encourages developer to create UI tests based on user actions.
######  Turn off animations on your test device
- prevent unexpected results.

### Record an Espresso test
- Espresso tests consist of two primary components
  - UI interactions (include):
    - tap and type actions that a person may use to interact with app.
  - assertions on View elements.
    - Assertions verify contents of visual elements on the screen.

### Record UI interactions
- Recording a test with Espresso Test Recorder process:
  -  **Run > Record Espresso Test.**
  -  In the Select Deployment Target window.
     - choose the device on which you want to record the test.
     -  click ok.
  - Espresso Test Recorder triggers a build of project.
    - App shoudl be installed and launched before Espresso Test Recorder allow me to interact with it.
    - Record Your Test window appears after the app launches.
    - now i can start interact with the app.
    - recorded interactions appear in main panel.

#### Add assertions to verify UI elements
- Assertions verify the existence or contents of a View element through three main types:
  - **text**, check if the content of selected element exist.
  - **exists**, check if element picked is on screen.
  - **does not exist**, check if element does not exist in current screen.
- **add an assertion**
  - **Click Add Assertion**, Screen Capture dialog appears.
  - layout of current screen a panel on the right of the **Record Your Test**, **view element create asserion**, use the **first drop-down menu** in the **Edit assertion**, (selected View object is highlighted in a red box).
  - **Select the assertion**, from **drop-down**.
  - click **Save Assertion** or **Save Assertion to do another** asserion.

##### Save a recording
1. **Complete Recording**(Pick a test class name for your test).
2. Espresso Test Recorder gives test a unique name within its package based on the name of the launched activity.
   1. not added the Espresso **dependencies** to  app, a **Missing Espresso dependencies**.
3. file automatically opens after Espresso Test Recorder generates it.
#### Run an Espresso test locally
1. Open app module folder and navigate to the test you want to run.
2. Right-click on the test and click Run ‘testName.’
3. n the Select Deployment Target window, choose the device on which you want to run the test.