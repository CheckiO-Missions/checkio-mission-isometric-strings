"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["add", "egg"],
            "answer": True
        },
        {
            "input": ["foo", "bar"],
            "answer": False
        },
        {
            "input": ["bar", "foo"],
            "answer": True
        },
        {
            "input": ["", ""],
            "answer": True
        },
        {
            "input": ["all", "all"],
            "answer": True
        },
        {
            "input": ["gogopy", "doodle"],
            "answer": False
        },

    ],
    "Extra": [
        {
            "input": ["paper", "title"],
            "answer": True
        },
        {
            "input": ["paper", "words"],
            "answer": False
        },
        {
            "input": ["hall", "hoop"],
            "answer": False
        }
    ]
}
