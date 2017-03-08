from CSWrapper import CSWrapper, CSWrapperError

class CSWrapperLibrary(object):
    """Test library for testing *CSWrapper* business logic.

    Interacts with the CSWrapper directly using its ``run`` method.
    """
    def __init__(self):
        self._wrapper = CSWrapper()
        self._result = ''

    def run_resource_command(self, resource, cmd, resid, serveraddr, adminuser, adminpw, admindom):
        """Runs the specified ``cmd`` on a given ``resource`` in a specific ``resid``.

        The given value is passed to the calculator directly. Valid buttons
        are everything that the calculator accepts.

        Examples:
        | Run resource command  | Dummy |   HelloWorld  |   b4f0e958-52bb-4bd3-81f9-a020bb040bb1 |  localhost   | admin | admin | Global |

        """
        self._result = self._wrapper.run(resource, cmd, resid, serveraddr, adminuser, adminpw, admindom)
        print self._result

    def result_should_contain(self, containsstr):
        """Verifies that the current result is ``containsstr``.

        Example:
        | Run resource command  | Dummy |   HelloWorld  |   b4f0e958-52bb-4bd3-81f9-a020bb040bb1 |
        | Result should contain | Hello |
        """
        if containsstr not in self._result:
            raise AssertionError('%s not in %s' % (containsstr, self._result))