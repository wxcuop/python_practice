Introduction
------------

### Comparisons

Python supports the following basic comparison operators:

| Operator | Operation | Description |
| --- | --- | --- |
| `>` | "greater than" | `a > b` is `True` if `a` is strictly greater in value than `b` |
| `<` | "less than" | `a < b` is `True` if `a` is strictly less in value than `b` |
| `==` | "equal to" | `a == b` is `True` if `a` is strictly equal to `b` in value |
| `>=` | "greater than or equal to" | `a >= b` is `True` if `a > b` OR `a == b` in value |
| `<=` | "less than or equal to" | `a <= b` is `True` if `a < b` or `a == b` in value |
| `!=` | "not equal to" | `a != b` is `True` if `a == b` is `False` |
| `is` | "identity" | `a is b` is `True` if *and only if* `a` and `b` are the same *object* |
| `is not` | "negated identity" | `a is not b` is `True` if `a` and `b` are not the same *object* |
| `in` | "containment test" | `a in b` is `True` if `a` is member, subset, or element of `b` |
| `not in` | "negated containment test" | `a not in b` is `True` if `a` is not a member, subset, or element of `b` |

They all have the same priority (*which is higher than that of [Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not), but lower than that of arithmetic or bitwise operations*).

### Comparison between different data types

Objects that are different types (*except numeric types*) never compare equal by default. Non-identical instances of a `class` will also *not* compare as equal unless the `class` defines special [rich comparison](https://docs.python.org/3/reference/datamodel.html#object.__lt__) methods that customize the default `object` comparison behavior. Customizing via `rich comparisons` will be covered in a follow-on exercise. For (much) more detail on this topic, see [Value comparisons](https://docs.python.org/3/reference/expressions.html?highlight=nan#value-comparisons) in the Python documentation.

Numeric types are (mostly) an exception to this type matching rule. An `integer` can be considered equal to a `float` (*or an [`octal`](https://docs.python.org/3/library/functions.html?#oct) equal to a [`hexadecimal`](https://docs.python.org/3/library/functions.html?highlight=hex#hex)*), as long as the types can be implicitly converted for comparison.

For the other numeric types in the Python standard library ([complex](https://docs.python.org/3/library/functions.html#complex), [decimal](https://docs.python.org/3/library/decimal.html), [fractions](https://docs.python.org/3/library/fractions.html)), comparison operators are defined where they "make sense" (*where implicit conversion does not change the outcome*), but throw a `TypeError` if the underlying objects cannot be accurately converted for comparison. For more information on the rules that python uses for *numeric conversion*, see [arithmetic conversions](https://docs.python.org/3/reference/expressions.html?highlight=number%20conversion#arithmetic-conversions) in the Python documentation.

```
>>> import fractions

# A string cannot be converted to an int.
>>> 17 == '17'
False

# An int can be converted to float for comparison.
>>> 17 == 17.0
True

# The fraction 6/3 can be converted to the int 2
# The int 2 can be converted to 0b10 in binary.
>>> 6/3 == 0b10
True

# An int can be converted to a complex number with a 0 imaginary part.
>>> 17 == complex(17)
True

# The fraction 2/5 can be converted to the float 0.4
>>> 0.4 == 2/5
True

>>> complex(2/5, 1/2) == complex(0.4, 0.5)
True

```

Any ordered comparison of a number to a `NaN` (*not a number*) type is `False`. A confusing side effect of Python's `NaN` definition is that `NaN` never compares equal to `NaN`.

```
>>> x = float('NaN')

>>> 3 < x
False

>>> x < 3
False

# NaN never compares equal to NaN
>>> x == x
False

```

### Comparing Strings

Unlike numbers, strings (`str`) are compared [*lexicographically*](https://en.wikipedia.org/wiki/Lexicographic_order), using their individual Unicode code points (*the result of passing each code point in the `str` to the built-in function [`ord()`](https://docs.python.org/3/library/functions.html#ord), which returns an `int`*). If all code points in both strings match and are *in the same order*, the two strings are considered equal. This comparison is done in a 'pair-wise' fashion - first-to-first, second-to-second, etc. In Python 3.x, `str` and `bytes` cannot be directly coerced/compared.

```
>>> 'Python' > 'Rust'
False

>>> 'Python' > 'JavaScript'
True

# Examples with Mandarin.
# hello < goodbye
>>> '你好' < '再见'
True

# ord() of first characters
>>> ord('你'), ord('再')
(20320, 20877)

# ord() of second characters
>>> ord('好'), ord('见')
(22909, 35265)

# And with Korean words.
# Pretty < beautiful.
>>> '예쁜' < '아름다운'
False

>>> ord('예'), ord('아')
(50696, 50500)

```

### Comparison Chaining

Comparison operators can be chained *arbitrarily* -- meaning that they can be used in any combination of any length. Note that the evaluation of an expression takes place from `left` to `right`.

As an example, `x < y <= z` is equivalent to `x < y` `and` `y <= z`, except that `y` is evaluated only once. In both cases, `z` is *not* evaluated at all when `x < y` is found to be `False`. This is often called `short-circuit evaluation` - the evaluation stops if the truth value of the expression has already been determined.

`Short circuiting` is supported by various boolean operators, functions, and also by comparison chaining in Python. Unlike many other programming languages, including `C`, `C++`, `C#`, and `Java`, chained expressions like `a < b < c` in Python have a conventional [mathematical interpretation](https://en.wikipedia.org/wiki/Three-way_comparison) and precedence.

```
>>> x = 2
>>> y = 5
>>> z = 10

>>> x < y < z
True

>>> x < y > z
False

>>> x > y < z
False

```

### Comparing object identity

The operators `is` and `is not` test for object [*identity*](https://docs.python.org/3/reference/datamodel.html), as opposed to object *value*. An object's identity never changes after creation and can be found by using the [`id()`](https://docs.python.org/3/library/functions.html#id) function.

`<apple> is <orange>` evaluates to `True` if *and only if* `id(<apple>)` == `id(<orange>)`. `<apple> is not <orange>` yields the inverse.

Due to their singleton status, `None` and `NotImplemented` should always be compared to items using `is` and `is not`. See the Python reference docs on [value comparisons](https://docs.python.org/3/reference/expressions.html?highlight=none#value-comparisons) and [PEP8](https://pep8.org/#programming-recommendations) for more details on this convention.

```
>>> my_fav_numbers = [1, 2, 3]

>>> your_fav_numbers = my_fav_numbers

>>> my_fav_numbers is your_fav_numbers
True

# The returned id will differ by system and python version.
>>> id(my_fav_numbers)
4517478208

# your_fav_numbers is only an alias pointing to the original my_fav_numbers object.
# Assigning a new name does not create a new object.
>>> id(your_fav_numbers)
4517478208

>>> my_fav_numbers is not your_fav_numbers
False

>>> my_fav_numbers is not None
True

>>> my_fav_numbers is NotImplemented
False

```

### Membership comparisons

The operators `in` and `not in` test for *membership*. `<fish> in <soup>` evaluates to `True` if `<fish>` is a member of `<soup>` (*if `<fish>` is a subset of or is contained within `<soup>`*), and evaluates `False` otherwise. `<fish> not in <soup>` returns the negation, or *opposite of* `<fish> in <soup>`.

For string and bytes types, `<name> in <fullname>` is `True` *if and only if* `<name>` is a substring of `<fullname>`.

```
# A set of lucky numbers.
>>> lucky_numbers = {11, 22, 33}
>>> 22 in lucky_numbers
True

>>> 44 in lucky_numbers
False

# A dictionary of employee information.
>>> employee = {'name': 'John Doe',
                'id': 67826, 'age': 33,
                'title': 'ceo'}

# Checking for the membership of certain keys.
>>> 'age' in employee
True

>>> 33 in employee
False

>>> 'lastname' not in employee
True

# Checking for substring membership
>>> name = 'Super Batman'
>>> 'Bat' in name
True

>>> 'Batwoman' in name
False

```

Instructions
------------

In this exercise you are going to implement some rules of [Blackjack](https://bicyclecards.com/how-to-play/blackjack/), such as the way the game is played and scored.

Note : In this exercise, *`A`* means ace, *`J`* means jack, *`Q`* means queen, and *`K`* means king. Jokers are discarded. A [standard French-suited 52-card deck](https://en.wikipedia.org/wiki/Standard_52-card_deck) is assumed, but in most versions, several decks are shuffled together for play.




In Blackjack, it is up to each individual player if an ace is worth 1 or 11 points (*more on that later*). Face cards (`J`, `Q`, `K`) are scored at 10 points and any other card is worth its "pip" (*numerical*) value.

Define the `value_of_card(<card>)` function with parameter `card`. The function should return the *numerical value* of the passed-in card string. Since an ace can take on multiple values (1 or 11), this function should fix the value of an ace card at 1 for the time being. Later on, you will implement a function to determine the value of an ace card, given an existing hand.

```
>>> value_of_card('K')
10

>>> value_of_card('4')
4

>>> value_of_card('A')
1
```


Define the `higher_card(<card_one>, <card_two>)` function having parameters `card_one` and `card_two`. For scoring purposes, the value of `J`, `Q` or `K` is 10. The function should return which card has the higher value for scoring. If both cards have an equal value, return both. Returning both cards can be done by using a comma in the `return` statement:

```
# Using a comma in a return creates a Tuple.  Tuples will be covered in a later exercise.
>>> def returning_two_values(value_one, value_two):
        return value_one, value_two

>>> returning_two_values('K', '3')
('K', '3')

```

An ace can take on multiple values, so we will fix `A` cards to a value of 1 for this task.

```
>>> higher_card('K', '10')
('K', '10')

>>> higher_card('4', '6')
'6'

>>> higher_card('K', 'A')
'K'
```

As mentioned before, an ace can be worth *either* 1 or 11 points. Players try to get as close as possible to a score of 21, without going *over* 21 (*going "bust"*).

Define the `value_of_ace(<card_one>, <card_two>)` function with parameters `card_one` and `card_two`, which are a pair of cards already in the hand *before* getting an ace card. Your function will have to decide if the upcoming ace will get a value of 1 or a value of 11, and return that value. Remember: the value of the hand with the ace needs to be as high as possible *without* going over 21.

Hint: if we already have an ace in hand, then the value for the upcoming ace would be 1.

```
>>> value_of_ace('6', 'K')
1

>>> value_of_ace('7', '3')
11

```

If a player is dealt an ace (`A`) and a ten-card (10, `K`, `Q`, or `J`) as their first two cards, then the player has a score of 21. This is known as a blackjack hand.

Define the `is_blackjack(<card_one>, <card_two>)` function with parameters `card_one` and `card_two`, which are a pair of cards. Determine if the two-card hand is a blackjack, and return the boolean `True` if it is, `False` otherwise.

Note : The score *calculation* can be done in many ways. But if possible, we'd like you to check if there is an ace and a ten-card *in* the hand (*or at a certain position*), as opposed to *summing* the hand values.

```
>>> is_blackjack('A', 'K')
True

>>> is_blackjack('10', '9')
False

```

If the players first two cards are of the same value, such as two sixes, or a `Q` and `K` a player may choose to treat them as two separate hands. This is known as "splitting pairs".

Define the `can_split_pairs(<card_one>, <card_two>)` function with parameters `card_one` and `card_two`, which are a pair of cards. Determine if this two-card hand can be split into two pairs. If the hand can be split, return the boolean `True` otherwise, return `False`

```
>>> can_split_pairs('Q', 'K')
True

>>> can_split_pairs('10', 'A')
False

```

When the original two cards dealt total 9, 10, or 11 points, a player can place an additional bet equal to their original bet. This is known as "doubling down".

Define the `can_double_down(<card_one>, <card_two>)` function with parameters `card_one` and `card_two`, which are a pair of cards. Determine if the two-card hand can be "doubled down", and return the boolean `True` if it can, `False` otherwise.

```
>>> can_double_down('A', '9')
True

>>> can_double_down('10', '2')
False

```


