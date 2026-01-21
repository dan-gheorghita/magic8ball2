```python
# Import the random module to generate random numbers
import random

# Define a list of possible fortune cookie messages
messages = [
    'It is certain',  # A positive and definitive message
    'It is decidedly so',  # An even more positive and definitive message
    'Yes definitely',  # A simple and positive message
    'Reply hazy try again',  # A message suggesting the answer is unclear
    'Ask again later',  # A message suggesting the answer is not ready yet
    'Concentrate and ask again',  # A message suggesting the answer is hidden
    'My reply is no',  # A negative message
    'Outlook not so good',  # A pessimistic message
    'Very doubtful'  # A highly negative message
]

# Generate a random index to select a random message from the list
# Use len(messages) - 1 to ensure the index is within the list's bounds
print(messages[random.randint(0, len(messages) - 1)])
```