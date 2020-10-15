test = {
  'name': 'Question q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'q2'
          >>> 'q2' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'q2'
          >>> # from its initial state (of ...)
          >>> q2 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # "a" is a variable, which is an expression.
          >>> q2 == 1
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # "b" is a variable, which is an expression.
          >>> q2 == 6
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # "3" is a expression giving a number.
          >>> q2 == 2
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # "a + 3" is the same as "(a + 3)".  Python will evaluate this
          >>> # bracketed expression in the process of evaluating the whole
          >>> # expression, so it is a sub-expression.
          >>> q2 == 4
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There are four sub-expressions.  They are all listed in
          >>> # the options - along with the single incorrect sub-expression.
          >>> q2 == 5
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> q2 == 3
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
