# Read: 33 - GraphQL @connection
### review: Intro to Serverless
- **def:** Serverless is a cloud computing execution model where the cloud provider dynamically manages the allocation and provisioning of servers.
- The Philosophy of servless is to focus on business and application and not care about infrastructure.
  - it will save a lot of time, effort, implementing things; so the point is i focus on business and UI and they provide me backend and infrastructure.
- it's provided by companies like Amazon.
- it's very beneficial since developers no longer have to work with infrastructure e.g. implementing, debugging.
- serverless is adopted by many companies like netflex.
- Serverless applications are event-driven cloud-based systems where application development rely on third-party services, client-side logic and cloud-hosted remote procedure calls.
- sometimes servless might be wrong choice.
- Here are some of the currently available cloud services:
  - AWS Lambda.
  - Google Cloud Functions.
  - Azure Functions.
  - IBM OpenWhisk.
  - Alibaba Function Compute.
  - Oracle Fn Project.

#### Pros & Cons
 - **Pricing**: **winner here is Serverless** .
 - **Networking**: To access these, must set up an API Gateway, meaning cannot be directly accessed. **winner is Traditional**
 - **3rd Party Dependencies**: winner here is based on the context:
   - For simple applications with few dependencies, Serverless is the winner.
   - for anything more complex, Traditional **Architecture is the winner**.
 - **Environments**:Setting up different environments for Serverless is as easy as setting up a single environment. **winner here is Serverless** .
 - **Timeout:** With Serverless computing, there’s a hard 300-second timeout limit, meaning complex or long-running functions aren’t good for Serverless. **winner is Traditional**
 - **Scale**: Serverless is automatic and seamless, but there is a lack of control or entire absence of control. **winner here is Serverless**
  
#### Functions as a Service (FaaS)
- engineers can deploy an individual function or a piece of business logic.
- they start within milliseconds (~100ms for AWS Lambda) and process individual requests within a 300-second timeout imposed by most cloud vendors.


##### Traditional vs. Serverless Architecture
 ![Traditional vs. Serverless Architecture](https://cdn.hackernoon.com/hn-images/1*x_v5NRC3TTMt1MaYl1gMUg.jpeg)
### review: AWS Amplify Kool-Aid
- tools and services that can be used together or on their own, to help front-end web and mobile developers build scalable full stack applications.
- I can configure app backend and connect app in minutes by AWS With Amplify.
- deploy static web apps in a few clicks, and easily manage app content outside the AWS console.
  - frontend frameworks that Amplify support:
    - React.
    - Angular.
    - Vue.
    - Next.js.
  - and mobile platforms:
    - Android.
    - iOS.
    - React Native.
    - Ionic.
    - Flutter.

### GraphQL @connection section

#####  Add relationships between types
- `@connection` specify relationships between `@model` types.
- supports one-to-one, one-to-many, and many-to-one relationships.
- implement **many-to-many** relationships using two **one-to-many** connections and a joining`@model`type.
- **Definition**: 
  ```GraphQl
  directive @connection(keyName: String, fields: [String!]) on FIELD_DEFINITION 
  ```


#### one to one
project have one team
```Graphql
type Project @model {
  id: ID!
  name: String
  team: Team @connection
}

type Team @model {
  id: ID!
  name: String!
}
```
#### one to many
post has many comments
```graphql
type Post @model {
  id: ID!
  title: String!
  comments: [Comment] @connection(keyName: "byPost", fields: ["id"])
}

type Comment @model
  @key(name: "byPost", fields: ["postID", "content"]) {
  id: ID!
  postID: ID!
  content: String!
}
```
#### many to many
- implement many to many using two 1-M` @connections`, an `@key`, and a joining `@model`. 
```graphql
type Post @model {
  id: ID!
  title: String!
  editors: [PostEditor] @connection(keyName: "byPost", fields: ["id"])
}

# Create a join model and disable queries as you don't need them
# and can query through Post.editors and User.posts
type PostEditor
  @model(queries: null)
  @key(name: "byPost", fields: ["postID", "editorID"])
  @key(name: "byEditor", fields: ["editorID", "postID"]) {
  id: ID!
  postID: ID!
  editorID: ID!
  post: Post! @connection(fields: ["postID"])
  editor: User! @connection(fields: ["editorID"])
}

type User @model {
  id: ID!
  username: String!
  posts: [PostEditor] @connection(keyName: "byEditor", fields: ["id"])
}
```

