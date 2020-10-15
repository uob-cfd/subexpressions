test = {
  'name': 'Question q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'q4'
          >>> 'q4' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'q4'
          >>> # from its initial state (of ...)
          >>> q4 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There is at least one sub-expression missing.
          >>> q4 == 4
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Less than three missing.
          >>> q4 == 3
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Only '3 / 4' is missing.
          >>> q4 == 1
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
