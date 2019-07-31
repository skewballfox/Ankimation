import genanki

reverseable_model = genanki.Model(
  2052314127,
  'Reverseable Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
    {
      'name': 'Card 2',
      'qfmt': '{{Answer}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Question}}',
    }
  ])