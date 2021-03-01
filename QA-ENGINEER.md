# QA Engineer

## Frontend Focused

### Problem Statement
Write end-to-end (E2E) functional tests which emulates the behaviour of **Personalize Your Plan** component on HelloFresh websites.

#### Context
- HelloFresh currently operates in 14 countries. Each country has it's own HelloFresh website but content and DOM structure generally the same.
- Each website has a **Personalize Your Plan** component but each country has diffearent set of preferences, per serving pricing and shipping cost.
  - See plan page for [HelloFresh Au](https://www.hellofresh.com.au/plans)
  - See plan page for [HelloFresh US](https://www.hellofresh.com/plans)

#### Tasks

- Create a Github repo which will contain E2E tests and Github actions created for this exercise
- Create functional test for **Personalize Your Plan** component where as a user I can 
  - select my preference 
  - customize my plan size
  - based-on selection view price per serving and shipping cost

- Ensure test is data-driven and can be run for following 
  - [HelloFresh Au](https://www.hellofresh.com.au/plans)
  - [HelloFresh US](https://www.hellofresh.com/plans)
 
- Create a CI/CD pipeline using Github actions whichs run test automatically one every new commit (PR or merge to master branch).
  - Run E2E test for HelloFresh Au and HelloFresh US
  - Generate the test report for HelloFresh Au and HelloFresh US
  - Publish the test report to Github Pages

### Recommended Technology Stack
Choose the one you are most familiar. 

- Testcafe
- Cypress

### Recommended Best-Practices

#### E2E Test
- Use of Page Models/Objects
- Use of Helpfer functions
- Test Setup and Teardown
- Data-Driven Tests
- Selector Strategy

#### CI/CD
- Organize pipeline as Jobs and Tasks

