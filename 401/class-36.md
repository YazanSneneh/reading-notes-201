# Cognito
- [source - Cognito Auth plugin AWS ](https://docs.amplify.aws/lib/auth/getting-started/q/platform/android#initialize-amplify-auth)
- Amplify Auth provide interface for authinticating users.
-  Amplify CLI helps to create and configure the auth category with an authentication provider.

### Setup and configure application with Amplify Auth.

#### Prerequisites
- Android application at least Android SDK 16 with Amplify libraries integrated.

#### Configure Auth Category
- **inside project directory** execute the command:
  $ `amplify add auth`
- **when prompted**:
``` javascript
? Do you want to use the default authentication and security configuration?
    `Default configuration`
? How do you want users to be able to sign in?
    `Username`
? Do you want to configure advanced settings?
    `No, I am done.`
```
- push changes to the cloud:
   `amplify push`


### Install Amplify Libraries
- add dependency to app‘s **build.gradle**.
```java
dependencies {
    implementation 'com.amplifyframework:aws-auth-cognito:1.17.4'
}
```

### Initialize Amplify Auth
- Add the Auth plugin before calling **Amplify.configure**
```java
Amplify.addPlugin(new AWSCognitoAuthPlugin());
Amplify.configure(getApplicationContext());
```
### Check the current auth session
- run this from **MainActivity’s onCreate** method.
```java
  Amplify.Auth.fetchAuthSession(
    result -> Log.i("AmplifyQuickstart", result.toString()),
    error -> Log.e("AmplifyQuickstart", error.toString()));
```
-  **isSignedIn property** of the **authSession** will be **false** since we **haven’t signed in** to the category yet.

```java
Congratulations! You’ve successfully setup AWS Cognito Auth plugin
```