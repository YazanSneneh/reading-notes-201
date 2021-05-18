#  Room
- Allow me to presist application data locally.
### Save data in a local database using Room
- room is useful when device can't connect to network, user can still browse while it's offline.
- Room persistence library provides a layer over SQLite to allow database access.
- Room provides the following benefits:
  - `Compile-time verification of SQL queries`.
  - annotations that minimize repetitive and boilerplate code.

##### Setup to use room
- add dependecy to gradle:
```java
 def room_version = "2.3.0"

    implementation "androidx.room:room-runtime:$room_version"
    annotationProcessor "androidx.room:room-compiler:$room_version"

    // optional - RxJava2 support for Room
    implementation "androidx.room:room-rxjava2:$room_version"

    // optional - RxJava3 support for Room
    implementation "androidx.room:room-rxjava3:$room_version"

    // optional - Guava support for Room, including Optional and ListenableFuture
    implementation "androidx.room:room-guava:$room_version"

    // optional - Test helpers
    testImplementation "androidx.room:room-testing:$room_version"
```
##### Primary components
- **Database** Class
  - holds the database and serve as the main access point.
- **Data Entities**
  - tables in my database (Model Class in my android app)
- **Data Access Object**
  - provide my application methods that i can use to query on db like select, update delete and insert.

**Explination:**
- database class provides the app an instances of the Data Access Object associated with the database.
- the application can use the object to presist the database.

#### Sample implementation
1. **Data entity**
 ```java
 @Entity
public class User {
    @PrimaryKey
    public int uid;

    @ColumnInfo(name = "first_name")
    public String firstName;

    @ColumnInfo(name = "last_name")
    public String lastName;
}
 ```
 2. **Data access object (DAO)**
    - like i mentioned eariler it provide me the methods i need to perform crud operations on database.

```java
@Dao
public interface UserDao {
    @Query("SELECT * FROM user")
    List<User> getAll();

    @Query("SELECT * FROM user WHERE uid IN (:userIds)")
    List<User> loadAllByIds(int[] userIds);

    @Query("SELECT * FROM user WHERE first_name LIKE :first AND " +
           "last_name LIKE :last LIMIT 1")
    User findByName(String first, String last);

    @Insert
    void insertAll(User... users);

    @Delete
    void delete(User user);
}
```
 3. **Database**
- the class should have following:
  - must be annotated with a `@Database` annotation that includes an entities array that lists all of the data entities associated with the database.
  - must be an abstract class that extends `RoomDatabase`.
  - For each DAO class that is associated with the database, the database class must define an abstract method that has zero arguments and returns an instance of the DAO class.

```java
@Database(entities = {User.class})
public abstract class AppDatabase extends RoomDatabase {
    public abstract UserDao userDao();
}
```

### Usage of created classes.
- now db is setup and ready to use, lets do it.
  - 1st i need instance of that db.
  ```java
  AppDatabase db = Room.databaseBuilder(getApplicationContext(),
        AppDatabase.class, "database-name").build();
  ```
  - and then i use the instance to get instance of data access object.
  - then use the data access object to get data.
```java
UserDao userDao = db.userDao();
List<User> users = userDao.getAll();
```

## Anatomy of an entity
-  class that is annotated with `@Entity`
-  contain fields and one of them is primary key annotated with pk.
-  **Define a primary key** with `@PrimaryKey`.
-  composite primary key:
   - ` @Entity(primaryKeys = {"firstName", "lastName"})`.

## Define relationships between objects
- use the @Embedded annotation to represent an object  represents a composition of fields.

#### Define relationships
###### Define one-to-one relationships
```java
@Entity
public class User {
    @PrimaryKey public long userId;
    public String name;
    public int age;
}

@Entity
public class Library {
    @PrimaryKey public long libraryId;
    public long userOwnerId;
}
```
###### Define one-to-many relationships
```java
@Entity
public class User {
    @PrimaryKey public long userId;
    public String name;
    public int age;
}

@Entity
public class Playlist {
    @PrimaryKey public long playlistId;
    public long userCreatorId;
    public String playlistName;
}
```
###### Define many-to-many relationships
```java
@Entity
public class Playlist {
    @PrimaryKey public long playlistId;
    public String playlistName;
}

@Entity
public class Song {
    @PrimaryKey public long songId;
    public String songName;
    public String artist;
}

@Entity(primaryKeys = {"playlistId", "songId"})
public class PlaylistSongCrossRef {
    public long playlistId;
    public long songId;
}
```
## Accessing data using Room DAOs
- daos include methods that I can use to access the database.
- the application create these objects at compile time.

#### Anatomy of a DAO
- it should be annotated with @Dao.
- it either can be abstract or interface.
- it does not contain proerties but contain methods (CRUD methods) for my entities.

```java
@Dao
public interface UserDao {
    @Insert
    void insertAll(User... users);

    @Delete
    void delete(User user);

    @Query("SELECT * FROM user")
    List<User> getAll();
}
```
- there are two types of data access object methods.
- query which is i write my own methods.
- Convenience method provide me insert, delete, update and select