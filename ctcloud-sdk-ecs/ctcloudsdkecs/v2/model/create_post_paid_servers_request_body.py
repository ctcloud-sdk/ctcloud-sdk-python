# coding: utf-8

import six

from ctcloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePostPaidServersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'server': 'PostPaidServer'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'server': 'server'
    }

    def __init__(self, dry_run=None, server=None):
        """CreatePostPaidServersRequestBody

        The model defined in ctcloud sdk

        :param dry_run: The param of the CreatePostPaidServersRequestBody
        :type dry_run: bool
        :param server: The param of the CreatePostPaidServersRequestBody
        :type server: :class:`ctcloudsdkecs.v2.PostPaidServer`
        """
        
        

        self._dry_run = None
        self._server = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.server = server

    @property
    def dry_run(self):
        """Gets the dry_run of this CreatePostPaidServersRequestBody.

        :return: The dry_run of this CreatePostPaidServersRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreatePostPaidServersRequestBody.

        :param dry_run: The dry_run of this CreatePostPaidServersRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def server(self):
        """Gets the server of this CreatePostPaidServersRequestBody.

        :return: The server of this CreatePostPaidServersRequestBody.
        :rtype: :class:`ctcloudsdkecs.v2.PostPaidServer`
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreatePostPaidServersRequestBody.

        :param server: The server of this CreatePostPaidServersRequestBody.
        :type server: :class:`ctcloudsdkecs.v2.PostPaidServer`
        """
        self._server = server

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePostPaidServersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
