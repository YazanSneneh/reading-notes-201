# Serverless and Amplify

## Intro to Serverless
What is Serverless Architecture? What are its Pros and Cons?
- The Philosophy of servless is to focus on business and application and not care about infrastructure.
- it's provided by companies like Amazon.
- it's very beneficial since developers no longer have to work with infrastructure e.g. implementing, debugging.
- serverless is adopted by many companies like netflex.
- sometimes servless might be wrong choice.

####  What is Serverless?
- Serverless is a cloud computing execution model(managed by cloud provided).
- Pricing is based on the number of executions.
- Serverless applications are event-driven.
- cloud-based systems where application development rely on a combination of third-party services.
- client-side logic and cloud-hosted remote procedure calls (Functions as a Service).
some of the currently available cloud services: **AWS Lambda and Google Cloud Functions**.
- Networking: Serverless functions are accessed only as private APIs. To access these you must set up an API Gateway.


## AWS Amplify
-  tools and services that can be used together or on their own, to help front-end web and mobile developers build scalable full stack applications.
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


##### Benefits:
- Configure backends fast.
- Seamlessly connect frontends.
- Deploy fast and easy.
- Easily manage content

## GraphQL Intro
- help create backend for web and mobile apps quickly on AWS.
- GraphQL Definition Schema Lanugauge help me create database schema 

#### Create a GraphQL API
- **Navigate into the root** of android project and run following:
  - `amplify init`
- **Follow the wizard** to create a new app and when finish:
  - `amplify add api`
- Select the options to create schema.
- `amplify push` to deply application
- **update schema**:
  - amplify api gql-compile
  - amplify push.


