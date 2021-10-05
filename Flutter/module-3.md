# Section 3: I Am Rich - How to Create Flutter Apps from Scratch

## intro to material design:
- material design was created by google to help developers create high quality systems (themes, colors system, components etc....)
- these designs can be used in web, and mobile development such as android, iso and Flutter.

#### Principles of material design
    - Material is the metaphor:
      - Material Design is inspired by the physical world and its textures(the feel, appearance, or consistency).
    - Bold, graphic, intentional: Material Design is guided by print design methods
      - typography, grids, space, scale, color, and imagery, to focus on experience and meaning.
    - Motion provides meaning:
      - Motion focuses attention and maintains continuity through subtle feedback and coherent transitions.
      - elements appear on screen, they transform and reorganize the environment with interactions generating new transformations

#### Components
- Components are interactive building blocks for creating a user interface.
- include a built-in states system to communicate focus, selection, activation, error, hover, press, drag, and disabled states.
- Component libraries are available for Android, iOS, Flutter, and the web.

##### Components cover a range of interface needs, including:
- **Display**: Organize content using components like cards, lists and sheets.
- **Navigation**: help user navigate or move inside product and move between screens using components like tabs and navigation drawers.
- **Actions**: allow users to perform actions using components like floating action button.
- **Input**: allow user to enter texts and make selections using components like textfield and selection controls.
- **Communication**: alert users to inform and message usiing components such as banners, snackbars and dialogs.


## Scaffold class
- this class act as API that allow me to build the material design visual layout structure.

##### Scaffold layout, the keyboard, and display
- scaffold will expand to fill the available space, means that it will occupy its entire window or device screen.
- When the device's keyboard appears the Scaffold's ancestor MediaQuery changes and the Scaffold will be rebuilt
- By default the scaffold's body is resized to make room for the keyboard.

##### Nested Scaffolds
- Scaffold is designed to be a top level container for a MaterialApp.
- This means that adding a Scaffold to each route on a Material app will provide the app with Material's basic visual layout structure.
- it's best to avoid nesting scaffolds.

##### Constructors
- Creates a visual scaffold for material design widgets.
- how to declare or create a Scaffold ? 
```Dart
 Scaffold(Key?key)
 Scaffold(appbar: appBar())
```
#### Properties
- **appBar**: -----> PrefferedSizeWidget?
  - to show top level bar inside the scaffold.
- **backgroundColor**: ----->  Color?
  -  the color of the material widgets inside the Scaffold
- **body**: -----> Widget?
- **buttomNavigationBar**. -----> Widget?
  - buttom navigation bar, it display the buttom of the Scaffold
- **drawer**: -----> Widget?
  - a panel (size navigation bar ) that display the side of the body.
- **floatingActionButton**: -----> Widget?
  - a button created on the top of scaffold
- **floatingActionButtonAnimator** ----->  FloatingActionButtonAnimator?
  - animator to move the floating action button to a new location.
- **floatingActionButtonLocation** -----> FloatingActionButtonLocation?
  - determine where the action button will be on screen.

[Visit Scaffold class for more about Scaffolds](https://api.flutter.dev/flutter/material/Scaffold-class.html)

## AppBar class

## Image class
- A widget to display images.

##### Several constructors are provided for the various ways that an image can be specified:
- **Image**: --------------> ImageProvider? **'required'**
  - to load image from image provider
- **Image.asset** --------> String:name
  - to load image from asset bundle.
- **Image.network** -----> String:name
  - to lead image from url
- **Image.file** -----------> File file
  - to read image from file


##### image formats are supported
- JPEG, PNG, GIF, Animated GIF, WebP, Animated WebP, BMP, and WBMP.
- Additional formats may be supported by the underlying platform. 
- Flutter will attempt to call platform API to decode unrecognized formats.
- if the platform API supports decoding the image Flutter will be able to render it.
- The Image.asset, Image.network & Image.file constructors allow a custom decode size to be specified through cacheWidth and cacheHeight parameters.
- The engine will decode the image to the specified size, which is primarily intended to reduce the memory usage of ImageCache.
- A network image is used on the Web platform, the cacheWidth and cacheHeight parameters are ignored as the Web engine delegates image decoding of network images to the Web, which does not support custom decode sizes.

#### Constructors
- Image(Key?key? required ImageProvider?)
- Image.asset(String name)
- Image.file(File file)
- Image.network(String url)


