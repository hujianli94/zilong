#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
Zilong base exception handling.
"""
import six
from oslo_utils import excutils


class ZilongException(Exception):
    """Base Zilong Exception."""

    message = "An unknown exception occurred."

    def __init__(self, **kwargs):
        try:
            super(ZilongException, self).__init__(self.message % kwargs)
            self.msg = self.message % kwargs
        except Exception:
            with excutils.save_and_reraise_exception() as ctxt:
                if not self.use_fatal_exceptions():
                    ctxt.reraise = False
                    # at least get the core message out if something happened
                    super(ZilongException, self).__init__(self.message)

    def __str__(self):
        return six.text_type(self.msg)

    def use_fatal_exceptions(self):
        """Is the instance using fatal exceptions.

        :returns: Always returns False.
        """
        return False


class BadRequest(ZilongException):
    message = 'Bad %(resource)s request'


class NotImplemented(ZilongException):
    message = ("Not yet implemented in RSC  %(func_name)s: ")


class NotFound(ZilongException):
    message = ("URL not Found")


class Conflict(ZilongException):
    pass


class ServiceUnavailable(ZilongException):
    message = "The service is unavailable"


class ConnectionRefused(ZilongException):
    message = "Connection to the service endpoint is refused"


class TimeOut(ZilongException):
    message = "Timeout when connecting to OpenStack Service"


class InternalError(ZilongException):
    message = "Error when performing operation"


class InvalidInputError(ZilongException):
    message = ("An invalid value was provided for %(opt_name)s: "
               "%(opt_value)s")


class InvalidValue(ZilongException):
    message = ("An invalid value was provided for %(opt_name)s: "
               "%(opt_value)s")
