# Section 12: BMI Calculator - Building Flutter UIs for Intermediates
## Use themes to share colors and font styles
- Themes allow me to share style across the entire application.
- there are two ways to share style (Colors, fonts etc..):
  - define app-wide themes.
  - use Theme() widget.

### Creating an app theme
- flutter create by default a theme that is shared across the entire app.
- to create my own theme that is shared to all screens inside app i provide ThemeData() to MaterialApp constructor(theme: ThemeData()).

```dart
MaterialApp(
  title: appName,
  theme: ThemeData(
    // Define the default brightness and colors.
    brightness: Brightness.dark,
    primaryColor: Colors.lightBlue[800],

    // Define the default font family.
    fontFamily: 'Georgia',

    // Define the default `TextTheme`. Use this to specify the default
    textTheme: TextTheme(
      // define the body text style
       bodyText2: TextStyle(fontSize: 14.0, fontFamily: 'Hind'),
      // define the title style
      headline1: TextStyle(fontSize: 72.0, fontWeight: FontWeight.bold),
    )
  )
)
```

### ThemeData class
- The MaterialApp **theme property** can be used to configure the appearance of the entire app.
- Widget subtree's within an app can override the app's theme by including a Theme widget at the top of the subtree.

##### Constructors
- `ThemeData()`
- `ThemeData.dark()`
    A default dark theme with a teal secondary ColorScheme color.
- `scrollbarTheme → ScrollbarThemeData`
    A theme for customizing the colors, thickness, and shape of Scrollbars.
- `ThemeData.light()`
A default light blue theme.

##### Properties
- `appBarTheme → AppBarTheme`
A theme for customizing the color, elevation, brightness, iconTheme and textTheme of AppBars.
- `applyElevationOverlayColor → bool`
Apply a semi-transparent overlay color on Material surfaces to indicate elevation for dark themes
- `backgroundColor → Color`
A color that contrasts with the primaryColor, e.g. used as the remaining part of a progress bar.
- `bannerTheme → MaterialBannerThemeData`
A theme for customizing the color and text style of a MaterialBanner.
- bottomAppBarColor → Color
The default color of the BottomAppBar.
- `bottomAppBarTheme → BottomAppBarTheme`
A theme for customizing the shape, elevation, and color of a BottomAppBar.
- `bottomNavigationBarTheme → BottomNavigationBarThemeData`
A theme for customizing the appearance and layout of BottomNavigationBar widgets.
- `buttonTheme → ButtonThemeData`
Defines the default configuration of button widgets.
- `cardTheme → CardTheme`
The colors and styles used to render Card.
- `checkboxTheme → CheckboxThemeData`
A theme for customizing the appearance and layout of Checkbox widgets.
- `dataTableTheme → DataTableThemeData`
A theme for customizing the appearance and layout of DataTable widgets.
- `dialogBackgroundColor → Color`
The background color of Dialog elements.
- `dialogTheme → DialogTheme`
A theme for customizing the shape of a dialog.
- `dividerColor → Color`
The color of Dividers and PopupMenuDividers, also used between ListTiles, between rows in DataTables, and so forth.
- `dividerTheme → DividerThemeData`
A theme for customizing the color, thickness, and indents of Dividers, VerticalDividers, etc.
- `elevatedButtonTheme → ElevatedButtonThemeData`
A theme for customizing the appearance and internal layout of ElevatedButtons.
- `errorColor → Color`
The color to use for input validation errors, e.g. in TextField fields.
- `focusColor → Color`
The focus color used indicate that a component has the input focus.
- `primaryColor → Color`
The background color for major parts of the app (toolbars, tab bars, etc)
- `primaryColorBrightness → Brightness`
The brightness of the primaryColor. Used to determine the color of text and icons placed on top of the primary color (e.g. toolbar text).
- `radioTheme → RadioThemeData`
A theme for customizing the appearance and layout of Radio widgets.
- `scaffoldBackgroundColor → Color`
The default color of the Material that underlies the Scaffold. The background color for a typical material app or a page within the app.
- `shadowColor → Color`
The color that the Material widget uses to draw elevation shadows.
- `snackBarTheme → SnackBarThemeData`
A theme for customizing colors, shape, elevation, and behavior of a SnackBar.
- `sliderTheme → SliderThemeData`
The colors and shapes used to render Slider.
- `tabBarTheme → TabBarTheme`
A theme for customizing the size, shape, and color of the tab bar indicator.
- `textButtonTheme → TextButtonThemeData`
A theme for customizing the appearance and internal layout of TextButtons.
- `textTheme → TextTheme`
Text with a color that contrasts with the card and canvas colors.

##### Methods:
- `.copyWith({}) → ThemeData`
Creates a copy of this theme but with the given fields replaced with the new values.

### Color class
- An immutable 32 bit color value in ARGB format.

##### Constructor
- Color(int value)
###### properties
- `opacity → double`
The alpha channel of this color as a double.


###  Final and Const
- final and const values are never changed oce declared.
- either instead of var or in addition to a type.
- Example:

```dart
final name = 'Bob'; // Without a type annotation
final String nickname = 'Bobby';

const bar = 1000000; // Unit of pressure (dynes/cm2)
const double atm = 1.01325 * bar; // Standard atmosphere
```
- **final**: a final variable not compile-time, it run time meaning i can run the app if final var have no value but once it's value declared it's never changed.
- **const**: a const variable is a compile-time constant, meaning I can't run the app if the const variable have no value because it will face error on compile.

### Font Awesome Flutter Package
- The Font Awesome Icon pack available as set of Flutter Icons.
- Font Awesome 5.15.4. Includes all free icons:
  - Regular.
  - Solid.
  - Brands.

###### Installation
- In the dependencies, section of pubspec.yaml, add the following line:
```yaml
dependencies:
  font_awesome_flutter: <latest_version>
```

##### Usage:
1. import it:
2. use it:
- example:
```dart
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

IconButton(
      // Use the FaIcon Widget + FontAwesomeIcons class for the IconData
      icon: FaIcon(FontAwesomeIcons.gamepad), 
      onPressed: () { print("Pressed"); }
     ),
```
###### Icon names
- Icon names equal those on the official website, but are written in lower camel case.
- Due to restrictions in dart, icons starting with numbers have those numbers written out.
- 