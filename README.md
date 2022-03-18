# REST API Assignment Purpose

The purpose of this simple exercise is to understand how a simple REST API can be tested.

In evaluating the response, we look for:
- the types of test cases.
- what edge cases may be covered.
- positive and negative test cases.
- inputs for tests.
- naming conventions for readability.
- documentation on how you frame your response and instructions on executing the tests.

Feel free to write a response in the language/framework of your choice.

This API was written using NodeJS, Express

### API

We have a very simple API with two endpoints.
1. `GET` /get-users will return the number of active users.
2. `POST` /create-user will create a new user.
   - You will need to provide the following body:
    `{ username: "jsmith", "firstName": "John", "lastName": "Smith"}`
   - This endpoint returns two responses: `200`, `400`.

Some things to note:
- The API mocks responses. 
- It is not backed by a data source.
- No actual data persists in any form.
- The implementation of this API is deliberately left out to gather your feedback on how it could be improved.

#### Running the API
API will run on port `8888`.

- Clone `git@github.com:afarooqs/qe-assessment.git`
- Install `npm install`
- Run `node index`

### Assignment
1. Please write your response and either zip your response  or upload on github.
2. Provide a small write-up on how endpoints could be improved (hint: data source).
3. Write a README on how to execute your tests and view the results.
4. Please clearly label the negative and positive test cases you have automated.

### Questions? 
Please reach out to ahmed@narmitech.com for any questions or clarifications.

