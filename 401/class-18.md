# Web App Security

### Hibernate Many to Many Annotation Tutorial
* many to many relation occurs when I have 2 entities that can have each one of them, the other entity as many registers in both sides.
* for example, lets say i have a projects and i have employees.
  * many employees can work on a project.
  * and many projects can have many employees.


### Database Setup
1. entities setup
* so to implement it I create a 3rd table have following fields:
*  primary key.
* foreign_Key contain primary key for employee.
* foreign_Key contain primary key for projects.

### The Model Classes

* JPA annotations to join many to many in a new table.
* `@ManyToMany` annotation should be used for both classes to create relationship between the entities.
* So relation between both classes, one is main and one is is not, in this case the employee is main because once project is finished, project can be removed but employee is remaining.
* which means the join table should be on the employee entity.
* **Project class**, the mappedBy attribute is used in the `@ManyToMany` to tell that the employees collection is mapped by the projects collection 
* `@JoinColumn` annotation is used to specify the join/linking column.

```java
@ManyToMany
@JoinTable 
@JoinColumn 
```

```java

    @ManyToMany(cascade = { CascadeType.ALL })
    @JoinTable(
        name = "Employee_Project", 
        joinColumns = { @JoinColumn(name = "employee_id") }, 
        inverseJoinColumns = { @JoinColumn(name = "project_id") }
    )
      Set<Project> projects = new HashSet<>();


@Entity
@Table(name = "Project")
public class Project {    
    // ...  
 
    @ManyToMany(mappedBy = "projects")
    private Set<Employee> employees = new HashSet<>();
    
    // standard constructors/getters/setters   
}
```