import genanki

normal_styling = """
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}
"""
reverseable_model = genanki.Model(
    2052354127,
    "Reverseable Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Deck}}<br><br>{{Question}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
        {
            "name": "Card 2",
            "qfmt": "{{Answer}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Question}}',
        },
    ],
    css=normal_styling,
)
print(reverseable_model)
