# What Is Node.js?
 * Node Is Built on Google Chrome’s V8 JavaScript Engine.
 * The V8 engine is JavaScript engine that runs in Google Chrome and other Chromium-based web browsers.
 * V8 engine was designed with performance in mind and is responsible for compiling JavaScript directly to native machine code that your computer can execute, for details go to [class10- read : 10 - JS Debugging](../class-10.md).
 * Ryan Dahl took advantage of V8 engine, took it and enhanced it and added libraries to it such as http library and file system etc.
 * in another word, now I can write javaScript code out of the browser and ineract directly with the machine.

## How to Install Node.js?
to install Node.js go to the [Node download page](https://nodejs.org/en/download/) and follow instructions.

##### Use Node.js
 * to check Node version go to terminal or CLI and type `node -v`.
 * then create a file `file.js`.
 * use simple `console.log('Hello Node!')`.
 * inside terminal in file directory `node file.js`.

##### Node.js Has Excellent Support for Modern JavaScript
 * Node support ECMA Script ES15 and beyond.
 * this means that I can write JavaScript using the latest and most modern syntax.
 * also means that you don’t generally have to worry about compatibility issues — as you would if you were writing JavaScript that would run in different browsers.


## Introducing npm, the JavaScript Package Manager
  * Node comes bundled with a package manager called npm.
  * To check which version installed on system, type in CLI `npm -v`.
  *  npm is also the world’s largest software registry. There are over 1,000,000 packages of JavaScript code available to download.
  * **frameworks** (and many, many related packages) are **all available via npm** and **rely on Node** to create a sensible development environment in which they can **run**.


##### Installing a Package Globally
  * Open terminal and type the following:
  * `npm install -g jshint` it will install jshint globally on the system.
##### Installing a Package Locally
  * install packages locally to a project, as opposed to globally.
  * `npm init` will create a **json file**
  * `npm install lodash --save`.


## Working with the package.json File
  * `/node_modules` folder is where npm has saved any libraries that pachage i downloaded depends on. e.g. if i download express the libraries express use will be in `/node_modules` directory.
  * The `node_modules` folder shouldn’t be checked in to **version control**, and can, in fact, be re-created at any time by running `npm install` from within the **project’s root**.

  **Note : If you open the package.json file, you’ll see libraries listed under the dependencies field. By specifying project’s dependencies in this way, you allow any developer anywhere to clone your project and use npm to install whatever packages it needs to run.**.

## What Is Node.js and npm Used For?
    * we can turn our attention to the first of their common uses: **installing** (via npm) and **running** (via Node) various **build tools** — **designed **to **automate** the **process** of **developing** a modern JavaScript **application**.
    * build tools come in all shapes and sizes, you won’t get far in a modern JavaScript landscape without bumping into them.
    * build tools can be **used** for anything from **bundling your JavaScript files** and **dependencies into static assets**, to **running tests**, or **automatic code** **linting** and **style checking**.


## Node.js Lets Us Run JavaScript on the Server
  * one of the biggest use cases for Node.js — running JavaScript on the server.
  * Node now plays a critical role in the technology stack of many high-profile companies.
  * Benefits of using Node.js technology are:

### The Node.js Execution Model
##### Multi thread
 * when you connect to a traditional server, such as Apache, it will spawn a new thread to handle the request.
 * In a language such as PHP or Ruby, any subsequent **I/O operations** (for example, interacting with a **database**) **block** the **execution** of your code** until the operation has completed**.
 * the server has to wait for the database lookup to complete before it can move on to processing the result.
 * If new requests come in while this is happening, the server will spawn new threads to deal with them.
 * as a large number of threads can cause a system to become sluggish — and, in the worst case, for the **site to go down**. 
 * **The most common way to support more connections is to add more servers.**
  
##### Single Thread
 * Node.js, is single-threaded also event-driven, which means that everything that happens in Node is in reaction to an event.
 * For example, when a new request comes in (one kind of event) the server will start processing it.
 * If it then encounters a blocking I/O operation, instead of waiting for this to complete, it will register a callback before continuing to process the next event.
 * When the I/O operation has finished (another kind of event), the server will execute the callback and continue working on the original request.
 * Under the hood, **Node uses the libuv library to implement this asynchronous** (that is, **non-blocking**) behavior.
 * Node’s execution model causes the server very little overhead, and consequently it’s capable of handling a large number of simultaneous connections.
 * The traditional approach to **scaling a Node app** is to **clone it** and **have the cloned instances** share the workload.
 * Node.js has a built-in module to help you implement a cloning strategy on a single server.

##### Downsides of single threaded
  * The fact that Node runs in a single thread does impose some limitations.
  * blocking I/O calls should be avoided.
  * **CPU-intensive** operations should be handed off **to a worker thread**.
  * **errors** should always be **handled correctly** for fear of **crashing the entire process**.
  * **Very Important warning**,  it’s important to handle errors correctly.

## Apps Is Node.js Suited for:
 * Node is particularly suited to building applications that require some form of real-time interaction or collaboration **e.g.** Real time applications (chat sites).
 * It’s also a good fit for building **APIs** where you’re **handling** lots of **requests that are I/O driven** (such as those needing to perform operations on a database).
 * ites involving **data streaming**, as Node makes it possible to **process files** **while they’re still being uploaded**.
 * There are various **frameworks** you can use to reduce the boilerplate, with **Express**.
 * Even a solution such as **Express is minimal**, **meaning** that if you want to do anything slightly out of the ordinary, you’ll need to **pull** in **additional modules** from npm.

## Advantages of Node.js
  * speed.
  * scalability.
  * You can do everything in the same language, you can easily share code between the server and the client.
  * Node’s big pluses is that it speaks **JSON**(data exchange format on the Web) and for interacting with object databases (such as MongoDB).
  * JSON is suited for **consumption** by a JavaScript program, meaning that when you’re working with Node, data can **flow** neatly between layers **without the need for reformatting**.
  * most of developers familiar with JavaScript meaning, transitioning to Node development is potentially easier than to other server-side languages.

#### Other Uses of Node
  * it can be used as a scripting language to automate repetitive or error prone tasks on PC.
  * Node.js can also can be used to build cross-platform desktop apps and even to create robots.