# coding: utf-8

import six

from ctcloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRebootServersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reboot': 'BatchRebootSeversOption'
    }

    attribute_map = {
        'reboot': 'reboot'
    }

    def __init__(self, reboot=None):
        """BatchRebootServersRequestBody

        The model defined in ctcloud sdk

        :param reboot: The param of the BatchRebootServersRequestBody
        :type reboot: :class:`ctcloudsdkecs.v2.BatchRebootSeversOption`
        """
        
        

        self._reboot = None
        self.discriminator = None

        self.reboot = reboot

    @property
    def reboot(self):
        """Gets the reboot of this BatchRebootServersRequestBody.

        :return: The reboot of this BatchRebootServersRequestBody.
        :rtype: :class:`ctcloudsdkecs.v2.BatchRebootSeversOption`
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this BatchRebootServersRequestBody.

        :param reboot: The reboot of this BatchRebootServersRequestBody.
        :type reboot: :class:`ctcloudsdkecs.v2.BatchRebootSeversOption`
        """
        self._reboot = reboot

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
        if not isinstance(other, BatchRebootServersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
