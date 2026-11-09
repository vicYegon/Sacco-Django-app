# 1. Variable and data types
- str
- int
- float
- bool
- None
- list
- dict

# 2. Conditionals and loops
- if
- elif
- else
- while
- for

# 3. Functions
- arguments
- print & return
- input validation & type conversion
- returning None

# 4. Validation & Exception handling
- try & except
- 

# Regular expressions

# Decimal

# Classes and objects


# Dictionary unpacking
- ** | **kwags

# Lists and loops

# Duplicate detection

# Automated testing

# Mocking user input
-----------------------------------------------------------------
## Challenges encountered

##### Challenge 1: Contribution validation error

- The application raised:

 `AttributeError: 'str' object has no attribute 'is_finite'`

- Solution: `Investigated the contribution's data type, verified conversion to Decimal, and corrected the .as_tuple() method call.`

##### Challenge 2: Duplicate National ID detection occurred too late

- The application continued requesting member information even when the National ID already existed.

-  Solution: `Moved duplicate detection into the National ID input loop so the user receives immediate feedback.`

##### Challange 3: Automated registration test failed with StopIteration.

- Root cause: `The mocked phone number contained 11 digits instead of the expected 10.`

- Solution: `Corrected the test phone number from 07112345678 to 0712345678.`

#### Lessons learned:

- Automated tests can fail because of incorrect test data.
- StopIteration can occur when mocked inputs are exhausted.
- Retry loops can consume additional mocked values.
- Always validate test data against application requirements.
- Debugging should focus on identifying the root cause rather than just suppressing errors.

#### Lessons learned
- input() returns a string.
- Decimal is preferable to float for financial amounts.
- Validation checks business requirements.
- Exception handling manages errors during execution.
- None can indicate unsuccessful validation.
- continue restarts a loop iteration.
- break exits a loop.
- return exits a function.
- Classes organize related data and behavior.
- Automated tests reduce repetitive manual testing.
