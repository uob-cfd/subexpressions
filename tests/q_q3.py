test = {
  'name': 'Question q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'q3'
          >>> 'q3' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'q3'
          >>> # from its initial state (of ...)
          >>> q3 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # a + 5 * b is the whole expression, and not a sub-expression.
          >>> q3 == 3
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Ah no - remember BODMAS.  Python will evaluate 5 * b first
          >>> # and then a + <the result>.  So Python does not evaluate (a + 5)
          >>> # in the process of evaluating this expression.
          >>> q3 == 1
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> q3 == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
