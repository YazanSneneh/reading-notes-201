# Location
#### Get the last known location
- Using the Google Play services location APIs, app can request the last known location of the user's device.
- The fused location provider is one of the location APIs in Google Play services, It manages the underlying location technology and provides a simple API.
  
#### Set up Google Play services
- To access the fused location provider, project must include Google Play services.
- Download and install the Google Play services component using the SDK Manager.
  - then add the library to your project.
- **Specify app permissions** Apps features use location services must request location permissions.

##### Create location services client
1. **In activity's onCreate() method**.
2. **create an instance of the Fused Location Provider Client**.

```java
private FusedLocationProviderClient fusedLocationClient;

// ..

@Override
protected void onCreate(Bundle savedInstanceState) {
    // ...

    fusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
}
```
3. **Get the last known location**
 - To request the last known location, call the getLastLocation() method.
 -  returns a Task that I use to get a Location object with the latitude and longitude coordinates of a geographic location.

``` java
fusedLocationClient.getLastLocation()
        .addOnSuccessListener(this, new OnSuccessListener<Location>() {
            @Override
            public void onSuccess(Location location) {
                // Got last known location. In some rare situations this can be null.
                if (location != null) {
                    // Logic to handle location object
                }
            }
        });
```
