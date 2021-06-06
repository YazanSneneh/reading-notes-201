# Allowing Other Apps to Start Activity
- To allow other apps to start activity in this way, I need to add an `<intent-filter>` element in manifest file for the corresponding `<activity>` element.
- the system identifies intent filters and adds the information to an internal catalog of intents supported by all installed apps.

### Add an Intent Filter
- system may send a given Intent to an activity if that activity has an intent filter fulfills the following criteria.
  - Action: platform-defined values such as `ACTION_SEND` or `ACTION_VIEW`.
  - Data: A description of the data associated with the intent.

```kotlin
<activity android:name="ShareActivity">
    <intent-filter>
        <action android:name="android.intent.action.SEND"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:mimeType="text/plain"/>
        <data android:mimeType="image/*"/>
    </intent-filter>
</activity>
```
### Handle the Intent in Your Activity
- In order to decide what action to take in activity, I can read the Intent that was used to start it.
- activity starts, call getIntent() to retrieve the Intent that started the activity.
- add following code in avtivity class file.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    setContentView(R.layout.main);

    // Get the intent that started this activity
    Intent intent = getIntent();
    Uri data = intent.getData();

    // Figure out what to do based on the intent type
    if (intent.getType().indexOf("image/") != -1) {
        // Handle intents with image data ...
    } else if (intent.getType().equals("text/plain")) {
        // Handle intents with text ...
    }
}
```