# Intents, Activities, and SharedPreferences

### Tasks and Back Stack
* when a user is doing a task, a collections of activities gets fired up.
* these activites are arranged in the back stack.
* and when it's finished it will be poped off the stack.
* when my application push a notification a new activity opens.
    * when i click on that button an activity open.
* when i press the back button it will be poped out of stack.

###### app tasks in stack.
* when user open application in the home screen, the application task is brought to the front of the screen.
*  open a task and fire another task from this task it will add new activity on top of previous activity in the stack.
* when the activity is stopped it will be removed from stack and previous one continue.
* activity in back stack only pushed and poped from stack.
* for example when i open what's app then go to status and open one status.
* these were 3 activites added to a stack and ther application is a task.
* when i press back it will take me back to list of status and kill previous activity and so on.
* when i back to home page, task back to background activities are poped out but task remain.
* when i give user chance to open ativity from different places, it will create instance each time user click on it

##### Managing Tasks
- earlier summary actually is how things gets managed in android system.


##### Defining launch modes
- i can specify how activity associated to task.
-  i can define lunch mode in two ways.
   -  manifest file.
      -  when i declare activity, i can specify how activity is assoicated with the task.
   -  Using Intent flags.
        - on calling startActivity intent flag specify how activity associated.

##### the manifest file
- using the `<activity>` element's launchMode attribute allow me to specify how activity is assoicated with task.
- There are four launch modes can assign to the launchMode attribute:
  - standard.
  - singleTop.
  - singleTask.
  - singleInstance

##### the Intent flags
- When starting an activity, you can modify the default association of an activity to its task by including flags in the intent that you deliver to startActivity().
- flags can be used to modify the default behavior are:  
  - FLAG_ACTIVITY_NEW_TASK.
  - FLAG_ACTIVITY_SINGLE_TOP.
  - FLAG_ACTIVITY_CLEAR_TOP

##### Handling affinities
- affinity indicates which task an activity prefers to belong to.
-  By default, all the activities from the same app have an affinity for each other.
-  we can modify that, and activities in different apps can have the same affinity or activity in task can do different tasks.
-  The taskAffinity attribute takes unique string value

###### affinity comes into play in two circumstances
- When the intent that launches an activity contains the `FLAG_ACTIVITY_NEW_TASK flag`.
- when activity has its `allowTaskReparenting` attribute true

##### Clearing the back stack
- when user leave his system for a while, the system will clear all tasks except for root.
- when user back to system, only root is restored.

###### to modify this behaviour
- alwaysRetainTaskState:
- clearTaskOnLaunch
- finishOnTaskLaunch

##### Starting a task
- intent filter allow me to setup activity to be entry point.
- intent filter of this kind causes an icon and label for the activity to be displayed in the app launcher.
- Users must be able to leave a task and then come back to it later using activity launcher.
- singleTask" and "singleInstance", should be used only when the activity has an `ACTION_MAIN` and a `CATEGORY_LAUNCHER` filter.
- 

## Save key-value data
- SharedPreferences APIs is used to save **key - value** pairs.
-  **SharedPreferences** object points to a file containing key-value pairs and provides methods to read and write them.
-  SharedPreferences file is managed by the framework and can be private or shared.

#### Get a handle to shared preferences
- to create or access shared preference, following method i should use:
  - `getSharedPreferences()`
    - Use it when i need multiple shared preference files identified by name.
    - 
  - `getPreferences()`
    - Use it from an Activity if i need to use only one shared preference file for the activity.
    - code:
```java
Context context = getActivity();
SharedPreferences sharedPref = context.getSharedPreferences(
        getString(R.string.preference_file_key), Context.MODE_PRIVATE);
```

#### Write to shared preferences
- To write to a shared preferences file, create a `SharedPreferences.Editor`.
- to do so i must call `edit()` on `SharedPreferences`.
- Pass the keys and values with methods `putInt()` and `putString()`.
-  Then call `apply()` or `commit()` to save the changes.

```java
SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
SharedPreferences.Editor editor = sharedPref.edit();
editor.putInt(getString(R.string.saved_high_score_key), newHighScore);
editor.apply();
```

###### Read from shared preferences
- call methods such as `getInt()` and `getString()` to read from shared preference.

```java
SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
int defaultValue = getResources().getInteger(R.integer.saved_high_score_default_key);
int highScore = sharedPref.getInt(getString(R.string.saved_high_score_key), defaultValue);
```