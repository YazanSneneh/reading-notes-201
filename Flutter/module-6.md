# Section 6: MiCard - How to Build Beautiful UIs with Flutter Widgets
- I can explore and learn flutter widgets in many ways.
  - flutter indexing, a page show flutter widgets by alhpabatic index.
  - flutter catalog, a page show flutter by the nature of the widget e.g. a list of widgets responsible for dealing with animations or widget responsible for dealing with aynsc operations or capertino widgets for iso applications style.
  - Videos, flutter have a website contains widget of the day.

## Layout in flutter
### Container Widget
- a widget that is used to surround given widget.
- i can use it to apply specific style to widget such as margin, padding color and more.

##### Container Widget layout
-  Container tries, in order: to honor alignment, to size itself to the child, to honor the width, height, and constraints, to expand to fit the parent, to be as small as possible.
-  If the widget has no child, no height, no width, no constraints, and the parent provides unbounded constraints, then Container tries to size as small as possible.
-  If the widget has no child and no alignment, but a height, width, or constraints are provided, then the Container tries to be as small as possible given the combination of those constraints and the parent's constraints.
-  If the widget has no child, no height, no width, no constraints, and no alignment, but the parent provides bounded constraints, then Container expands to fit the constraints provided by the parent.

##### more to affect the layout
- The margin and padding properties also affect the layout, as described in the documentation for those properties. 
- The decoration can implicitly increase the padding (e.g. borders in a BoxDecoration contribute to the padding).

#### Properties
- alignment.
  - Align the child within the container
- child 
  - The child contained by the container.
- color
  - The color to paint the container behind the child.
- decoration 
  - The decoration to paint behind the child.
- margin 
  - Empty space to surround the decoration and child.
- padding
  - Empty space to inscribe inside the decoration. The child, if any, is placed inside this padding.
- transform
  - The transformation matrix to apply before painting the container
- transformAlignment
  - The alignment of the origin, relative to the size of the container, if transform is specified.


### Column class
- widget display 1 or more items aligned vertically.
- it take list of children.
- The Column widget does not scroll.

##### Properties
- children.
- crossAxisAlignment
å
### Row class
- widget display 1 or more items aligned horizontally.
- it take list of children.
- The Row widget does not scroll.

##### Properties
- children.
- crossAxisAlignment


## Fonts in Flutter
- I can declare a font as part of a separate package.
- This way I can share the same font across several different projects.


#### how to add Font to flutter project
- I can add font to my project in two ways first is to add it as assets and thesecond is to make it as package.
###### Assets
- i need to do the following steps in order to add it as assets:
    1. inside the main project folder **my_project/** I create folder snf name it **fonts** or any name of my choose.
    2. get the font file name with extention **.ttf** and add it inside **font/font.tff**
    3. tell the project about it inside **pubspec.yaml**
       1. specify the font family name.   family: family
       2. add the location of the file:  **fonts/font.tff**
    4. reload project.
    5. use it inside project using the name of the font family i used inside **pubspec.yaml**

#### Icons class
- Identifiers for the supported material design icons.

- Use with the Icon class to show specific icons.

- Icons **are identified by their name** as listed in [Icon class](https://api.flutter.dev/flutter/material/Icons-class.html). 

- To use this class, set uses-material-design: true in project's **pubspec.yaml file in the flutter section.**
- This ensures that the MaterialIcons font is included in application.
-  This font is used to display the icons. For example:
```yaml
flutter:
  uses-material-design: true
```

#### Card class
- A material design card: a panel with slightly rounded corners and an elevation shadow.
- A card is a sheet of Material used to **represent some related information**, for example an album, a geographical location, a meal, contact details, etc.

###### Properties
- borderOnForeground → bool
  Whether to paint the shape border in front of the child. 
- child → Widget?
  The widget below this widget in the tree.
- clipBehavior → Clip?
The content will be clipped (or not) according to this option.
- color → Color?
  The card's background color.
  elevation → double?
- The **z-coordinate** at which to place this card. This controls the size of the shadow below the card.
- margin.
- shadowColor → Color?
  The color to paint the shadow below the card.

#### Padding class
- A widget that insets its child by the given padding.
- When passing **layout constraints** to it's child, **padding shrinks** the constraints by the given padding, **causing the child to layout at a smaller size**. **Padding then sizes itself to its child's size**, inflated by the padding, effectively **creating empty space around the child.**

###### Why use a Padding widget rather than a Container with a Container.padding property?
- There isn't really any difference between the two, but container doesn't implement its properties directly.

#### Divider class
- A thin horizontal line, with padding on either side.
- In the material design language, this represents a divider.
- Dividers can be used in lists, Drawers, and elsewhere **to separate content.**
- To create a divider between ListTile items, **use ListTile.divideTiles**, which is optimized for this case.

##### Properties
- thickness → double?
The thickness of the line drawn within the divider.
- color → Color?
The color to use when painting the line.
- endIndent → double?
The amount of empty space to the trailing edge of the divider.
- height → double?
The divider's height extent.
- indent → double?
The amount of empty space to the leading edge of the divider.

#### ListTile class
- A single fixed-height row that typically **contains** text as well as a leading or trailing icon.
