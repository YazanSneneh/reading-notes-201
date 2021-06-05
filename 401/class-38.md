# Notifications
- **SNS** is **AWS** plugin allow me to push notification to users.
### SNS with Amplify (and Firebase)
##### Requirements
-  to use Amazon Pinpoint I need to setup credentials (keys or certificates) for targeted mobile platform, e.g. Android.
-  Testing Push Notifications requires a physical device
##### Setup for Android
1. have a Firebase Project and app setup.
2. Get push messaging credentials for Android in Firebase console.
3. Install dependencies:
    ` npm install aws-amplify @aws-amplify/pushnotification`.
4. Add push messaging credentials (Server key) with Amplify CLI by using commands:
  ` amplify add notifications`
  then choose **FCM**
5. Enable app in Firebase.
6. Open **android/build.gradle** file and edit:
   1. add to dependency:
  ```java
   dependencies {
      classpath("com.google.gms:google-services:4.3.3")
  }
```
   2. Open **android/app/build.gradle** and perform following edits:
- Add firebase libs to the dependencies section:

```java
dependencies {
  implementation "com.google.firebase:firebase-core:15.0.2"
  implementation "com.google.firebase:firebase-messaging:15.0.2"
}
```
##### Configure App
- The Push Notifications category is integrated with Analytics module to be able to track notifications.
- meaning analytics must be configured 
