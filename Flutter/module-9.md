# Xylophone - Using Flutter and Dart Packages to Speed Up Development

## Guide to Using Flutter Packages
- Flutter and Dart allow developers to add packages and plugins into Flutter and Dart ecosystems.
- this benefit developers by building an app without the need to build apps from scratch.
- Existing packages enable many use cases—for example:
  -  making network requests (http).
  -  custom navigation/route handling (fluro).
  -  integration with device APIs (url_launcher and battery).
  -  using third-party platform SDKs like Firebase (FlutterFire).


##### What is the difference between a package and a plugin?
- A plugin is a type of package.
- plugin is shortend for plugin package.

###### Packages
- a Dart package is a directory containing a pubspec file.
- a package can contain dependencies (listed in the pubspec).
- Dart libraries, apps, resources, tests, images, and examples.
- The [pub.dev](https://pub.dev/) site lists many packages—developed by Google engineers and Flutter and Dart community.
- I can use these packages in my application.
###### Plugins
- A plugin package is type of package that makes platform functionality available to the app.
- Plugin packages can be written for Android, iOS, web, macOS, Windows, Linux, or any combination thereof.
- plugin might provide Flutter apps with the ability to use a device’s camera.

### Using packages
some things to be done in order to use flutter package.

#### Searching for packages
- Packages are published to [pub.dev](https://pub.dev/).
- The [Flutter landing page](https://pub.dev/flutter/packages) on [pub.dev](https://pub.dev/) displays top packages that are compatible with Flutter.
- The [Flutter Favorites page](https://pub.dev/flutter/favorites) on pub.dev lists the plugins and packages that have been identified as packages should first consider using when writing Flutter app.
- browse the packages on pub.dev by filtering on [Android plugins](https://pub.dev/flutter/packages?platform=android), [iOS plugins](https://pub.dev/flutter/packages?platform=ios), [web plugins](https://pub.dev/flutter/packages?platform=web), or any combination thereof.

#### Adding a package dependency to an app
how To add the package, to an app?
1. Depend on it:
   - inside the **pubspec.yaml** file located inside the app folder, and add **package** under dependencies.
2. Install it:
   * From the terminal Run:
```bash 
flutter pub get
```
   - From **Android Studio/IntelliJ**: Click **Packages get** in the action ribbon at the top of pubspec.yaml.
   - From **VS Code:** Click **Get Packages** located in right side of the action ribbon at the top of pubspec.yaml.

3. Import it
   - Add a corresponding import statement in the Dart code.

4. Stop and restart the app, if necessary
   - If the package brings platform-specific code (Kotlin/Java for Android, Swift/Objective-C for iOS), code must be built into app.
   - Hot reload and hot restart only update the Dart code.
   - **full** restart of the app might be required to avoid errors like `MissingPluginException` when using the package.

#### Conflict resolution
- Suppose the app use package and another package and both depend on specific package but with different version.
- it causes a potential conflict.
- To avoid this is for package to use version **ranges** rather than **specific versions** when **specifying dependencies**.
- example of ranged:
```yaml
url_launcher: ^5.4.0    # Good, any version >= 5.4.0 but < 6.0.0
```