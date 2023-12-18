# coding: utf-8

import six

from ctcloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaDisassociateSecurityGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'body': 'NovaDisassociateSecurityGroupRequestBody'
    }

    attribute_map = {
        'server_id': 'server_id',
        'body': 'body'
    }

    def __init__(self, server_id=None, body=None):
        """NovaDisassociateSecurityGroupRequest

        The model defined in ctcloud sdk

        :param server_id: The param of the NovaDisassociateSecurityGroupRequest
        :type server_id: str
        :param body: The param of the NovaDisassociateSecurityGroupRequest
        :type body: :class:`ctcloudsdkecs.v2.NovaDisassociateSecurityGroupRequestBody`
        """
        
        

        self._server_id = None
        self._body = None
        self.discriminator = None

        self.server_id = server_id
        if body is not None:
            self.body = body

    @property
    def server_id(self):
        """Gets the server_id of this NovaDisassociateSecurityGroupRequest.

        :return: The server_id of this NovaDisassociateSecurityGroupRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this NovaDisassociateSecurityGroupRequest.

        :param server_id: The server_id of this NovaDisassociateSecurityGroupRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def body(self):
        """Gets the body of this NovaDisassociateSecurityGroupRequest.

        :return: The body of this NovaDisassociateSecurityGroupRequest.
        :rtype: :class:`ctcloudsdkecs.v2.NovaDisassociateSecurityGroupRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NovaDisassociateSecurityGroupRequest.

        :param body: The body of this NovaDisassociateSecurityGroupRequest.
        :type body: :class:`ctcloudsdkecs.v2.NovaDisassociateSecurityGroupRequestBody`
        """
        self._body = body

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
        if not isinstance(other, NovaDisassociateSecurityGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other