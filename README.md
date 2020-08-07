# Deep Writing

A multi-layer Recurrent Neural Networks (RNN, LTSM, and GRU) for word-level language models in Python using TensorFlow.

Mostly reused code from https://github.com/sherjilozair/char-rnn-tensorflow which was inspired by Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

## Requirements
- [Tensorflow 1.0](http://www.tensorflow.org)

## Basic Usage

To train with default parameters on the Harry Potter books, run:
```bash
python train.py
```

To continue training after interruption or to run on more epochs, run:
```bash
python train.py --init_from=save
```

To sample from a trained model, run:
```bash
python sample.py
```

To pick a specific starting word (for example, "Harry"), run:
```bash
python sample.py --prime "Harry"
````

## Sample Output
Note: I added a bit of formatting to aid readability.

```
Harry was his eyes of dragons. He said the gale under the last way to squeal 
on the whole of the Gryffindor wall, tapped the steering wheel over the grassy 
desks and went very themselves so gamekeeper. 

"I'm fine," said Harry, darting flat on his chest into a Quidditch field. 
He raised and fell silently across the corridor, looking depressed. Harry's neck 
seemed to believe too far-fetched solid. He felt something drained Hermione. 
"But it's not for, though, is not all a human, so I must insist." The only one 
became yet at eleven o'clock where the hippogriff swung off the grounds, trying to 
get on the death of being interesting everywhere he moaned, attacked. 

"Well, I'll know older lessons, Harry. You're all more sparks and they told the right. 
I'll do the believe I was likely to be scrapped answer by the only evening of breath." 
Crookshanks opened his arm and pulled out his chin. Sirius asked Voldemort if he had 
a great game of people else keep talking on this mail happy. 

"You sent me about how not to put these classes at its books at Gryffindor than witnesses 
at the thing itself. Get it, rubbish," said Harry to keep the map all open, but pulled 
out the door. "Are you stupid, Harry? Would make out of your best just to add with a 
Time-Turner," Hermione said, with her fist. "I'll just look at the breakneck only-too-familiar 
name, before the sword onto the scene." Caught in them and tried to cry it quickly in the 
scruff of small pop, and glaring at the tank. "Fascinating," said rather deeply rules, 
because Harry jumped upstairs quietly to start with every direction.
```

## Projects
If you have any project using this deep writing model, please let me know. I'll list up your project here.


## Contribution
Please feel free to:
- Leave feedback in the issues
- Open a Pull Request
