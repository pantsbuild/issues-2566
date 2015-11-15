from pants.backend.python.targets.python_tests import PythonTests
from pants.build_graph.build_file_aliases import BuildFileAliases


def python_tests(parse_context, dependencies=None, **kwargs):
  pytest_timeout_req = parse_context.create_object('python_requirement',
                                                   requirement='pytest-timeout<1')
  parse_context.create_object('python_requirement_library',
                              name='_issue_2556_workaround_',
                              requirements=[pytest_timeout_req])
  dependencies = dependencies or []
  dependencies.append(':_issue_2556_workaround_')
  parse_context.create_object(PythonTests, dependencies=dependencies, **kwargs)


def build_file_aliases():
  fixed_python_tests = BuildFileAliases.curry_context(python_tests)
  return BuildFileAliases(context_aware_object_factories={'python_tests': fixed_python_tests})
