test = {
  'name': 'Question q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'q1'
          >>> 'q1' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'q1'
          >>> # from its initial state (of ...)
          >>> q1 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # 55 + 92 is the full expression, so it is not a sub-expression.
          >>> q1 == 2
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> q1
          1
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
