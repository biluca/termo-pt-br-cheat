# Termo PT-BR Cheater

This is a Python Script wich make your life easier when you're playing [Termo](https://term.ooo/)

This project was made specific for [Termo (PT-BR)](https://termo.pt/). 

However, once you change the `words.txt` file, which contains a **portuguese words collection**, to a any-language words collection the script should work just fine. *Reminder: Termo uses 5 letters words*

## How to use?

First of all, you need to define your search rule. You can follow the `rules_sample.json` file as an example. But here it goes: as you can see on the code bellow, there are 2 types of rules `known_letters` and `unknown_letters`.

The `known_letters` are the rules for letter that I **know** the position in advance.

The `unknown_letters` are the rules for letter that I **don't know** the position in advance.

Reading the rules you can say that the word must have:

* The letter `I` as the 4th letter (position 3)
* The letter `A` as the 1th letter (position 0)
* The letter `S` as any letter of the word.

```
{
    "known_letters": [
        {
            "letter": "I",
            "position": 3
        },
        {
            "letter": "A",
            "position": 0
        }
    ],
    "unknown_letters": [
        {
            "letter": "S"
        }
    ]
}
```

Once you define your rules, you can run:

```
python3 main.py
```


For testing you can run:

```
pytest test_searcher.py
```
You can update the unit test scenarios inside the `test\` folder.