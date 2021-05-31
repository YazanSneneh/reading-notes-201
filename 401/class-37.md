# Introduction to Amazon S3
- Simple Storage Service is storage for the Internet. It is designed to make web-scale computing easier.
- I can use to store and retrieve any amount of data

### Advantages of using Amazon S3
- **Creating buckets**: bucket stores data, they are containers in Amazon S3 for data storage.
- **Storing data**: infinite amount of data in a bucket, I can Upload as many objects as I like into an Amazon S3 bucket, object can contain up to 5 TB of data.
- **Downloading data**: Download data or enable others to do it.
- **Permissions**: Grant or deny access to others who want to use data into Amazon S3 bucket.

### Amazon S3 concepts
- **Buckets**
  - bucket is a container of objects stored in S3.
  - Buckets purpose: play role in access control, used for usage reporting, identify account responsible for storage and data transfer.
- **Objects**
  - entities stored in Amazon S3.
  - object consist of data and metadata.
  - metadata is **name-value** pairs describe the object.
  - identified in a bucket by a key and a version ID.
- **Keys**
  - identify object within a bucket.
  - object in a bucket has one key.
- Regions
  - geographical AWS Region where Amazon S3 will store the buckets created.
  - Region can optimize latency, minimize costs, or address regulatory requirements.
  - Objects stored in a Region never leave the Region to another one unless explicitly transferd.
- Amazon S3 data consistency model
  - provides strong consistency for PUTs and DELETEs of objects in Amazon S3 bucket in all AWS Regions.

### Amazon S3 features
- Storage classes.
  - offers a range of storage classes designed for different cases.
- Bucket policies.
  - provide access control to buckets and objects based on conditions.
  - permissions attached to a bucket apply to all of the bucket's objects that are owned by the bucket owner account.
- AWS Identity and Access Management.
  - **AWS Identity and Access Management (IAM)** manage access to Amazon S3 resources.
- Access control lists
  - control access to each bucket and object using an access control list.
- Versioning.
  - versioning keep multiple versions of an object in the same bucket.
- Operations, Common operations:
  - Create a bucket.
  - Write an object.
  - Read an object.
  - delete an object.
  - List keys.

### Amazon S3 application programming interfaces (API)
 - provides a REST and a SOAP interface.

#### The REST interface
- HTTP interface to Amazon S3. 
- Using REST, use standard HTTP requests to **create**, **fetch**, and **delete** buckets and objects.
- REST API uses the standard HTTP headers and status codes, so that standard browsers and toolkits work as expected. 
#### The SOAP interface
- use document literal encoding. 
- to use SOAP, download the WSDL.


# Getting started
- go to your project directory and execute the command:
`amplify add storage`
- a screen will prompt to fill info (I will do it ofc).
- push changes to the cloud, execute the command:
`amplify push`
