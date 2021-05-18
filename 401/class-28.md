# Create dynamic lists with RecyclerView
- RecyclerViewdisplay set of data.
- i provide data and tell it to show n number of items, e.g. want only 5 to show.
- - RecyclerView resue view.

#### Key classes 
to build dynamic list, i need following classes:
1. `RecyclerView` : it contains data, and i can only add it to screen.
2. for each element in layout element holder will be created, and RecyclerView bind it to it's data `RecyclerView.ViewHolder.`
3. RecyclerView bind views to data by calling `RecyclerView.Adapter` method.
4. layout manager arranges the individual elements in list.

#### Steps for implementing your RecyclerView
 - Design how each element in the list is going to look and behave.
 - define Adapter to associates data with the ViewHolder.

#### Plan your layout
- items in RecyclerView are arranged by a LayoutManager class.
- RecyclerView library provides three layout managers:
  1. `LinearLayoutManager`. arrange items in one dimentional list.
  2. `GridLayoutManager`. arrange items in two dimentional view which is grid view.
  3. `StaggeredGridLayoutManager` similar to grid but the different is that my items don't have to have the same height or width.

#### Implementing adapter and view holder
Adapter and ViewHolder work together to define how data is displayed
    - The **ViewHolder** is a **wrapper** **around a View** that contains the layout for an individual item in the list.
    - The **Adapter** **creates ViewHolder objects as needed**, and also sets the data for those views.
    - The process of associating views to their data is called binding.
  - I need three methods to define adapter:
    - `onCreateViewHolder()`
    - `onBindViewHolder()`
    - `getItemCount()`