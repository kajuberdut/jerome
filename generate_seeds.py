from pathlib import Path
from jerome.markov import Markov, SEED_PATHS



BLACK_GATE = """Hold your ground! Hold your ground!
Sons of Gondor, of Rohan, my brothers, I see in your eyes the same fear that would take the heart of me.
A day may come when the courage of men fails, when we forsake our friends and break all bonds of fellowship, but it is not this day.
An hour of wolves and shattered shields, when the age of men comes crashing down, but it is not this day!
This day we fight!
By all that you hold dear on this good Earth, I bid you stand, Men of the West!"""
with SEED_PATHS["Black Gate Speech"] as f:
    Markov.from_corpus(BLACK_GATE).save(f)

LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
with SEED_PATHS["Lorem Ipsum"] as f:
    Markov.from_corpus(LOREM_IPSUM).save(f)

PRIDE_AND_PREJUDICE = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.
The day passed much as the day before had done. 
Mrs. Hurst and Miss Bingley had spent some hours of the morning with the invalid, who continued though slowly to mend;
and in the evening Elizabeth joined their party in the drawing-room.
Vanity and pride are different things, though the words are often used synonymously.
A person may be proud without being vain.
Pride relates more to our opinion of ourselves, vanity to what we would have others think of us.
There are few people whom I really love, and still fewer of whom I think well.
The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency of all human characters, and of the little dependence that can be placed on the appearance of merit or sense.
There is, I believe, in every disposition a tendency to some particular evil—a natural defect, which not even the best education can overcome.
Nothing is more deceitful than the appearance of humility.
A person who can write a long letter with ease, cannot write ill.
Is not general incivility the very essence of love?
Those who do not complain are never pitied.
To be fond of dancing was a certain step towards falling in love.
For what do we live, but to make sport for our neighbors, and laugh at them in our turn?
Angry people are not always wise.
But people themselves alter so much, that there is something new to be observed in them for ever.
The distance is nothing when one has motive."""
with SEED_PATHS["Pride and Prejudice"] as f:
    Markov.from_corpus(PRIDE_AND_PREJUDICE).save(f)
