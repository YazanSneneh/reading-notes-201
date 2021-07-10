# Android REST Client using Spring REST

### Method to deserialize generic collection with Gson.
```java
Type listType = new TypeToken<ArrayList<YourClass>>(){}.getType();
List<YourClass> yourClassList = new Gson().fromJson(jsonArray, listType);
```

- **explanation**:
  - 