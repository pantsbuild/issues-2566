## An example of a pants plugin to work around issue 2566.

Pants python support has a floating dependency on `pytest-timeout` in
its unit test runner. This causes an action-at-a-distance breakage for
users who run `./pants test` against `python_tests` targets. More
details about the break can be found
[here](https://github.com/pantsbuild/pants/issues/2566).

There are 3 workarounds.

1. Upgrade to `pantsbuild.pants>=0.0.59`.
2. Add a dependency to each of your `python_tests` targets to
   `pytest-timeout<1`.
3. Add a plugin like the one demonstrated in this repo.

The 3rd option is the focus of this example repo and it allows running
`./pants clean-all test tests/` green.  To use this solution in your
repo you need both the contents of the `pants-plugins/` directory and
the `pythonpath` and `backend_plugins` entries from `pants.ini`.

