# generated from rosidl_generator_py/resource/_idl.py.em
# with input from canopen_interfaces:srv/CANRead.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'indices'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CANRead_Request(type):
    """Metaclass of message 'CANRead_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('canopen_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'canopen_interfaces.srv.CANRead_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__can_read__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__can_read__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__can_read__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__can_read__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__can_read__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'COMMAND__DEFAULT': 'SDO',
        }

    @property
    def COMMAND__DEFAULT(cls):
        """Return default value for message field 'command'."""
        return 'SDO'


class CANRead_Request(metaclass=Metaclass_CANRead_Request):
    """Message class 'CANRead_Request'."""

    __slots__ = [
        '_command',
        '_cobid',
        '_node_id',
        '_indices',
    ]

    _fields_and_field_types = {
        'command': 'string',
        'cobid': 'int16',
        'node_id': 'int8',
        'indices': 'sequence<int32>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.command = kwargs.get(
            'command', CANRead_Request.COMMAND__DEFAULT)
        self.cobid = kwargs.get('cobid', int())
        self.node_id = kwargs.get('node_id', int())
        self.indices = array.array('i', kwargs.get('indices', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.command != other.command:
            return False
        if self.cobid != other.cobid:
            return False
        if self.node_id != other.node_id:
            return False
        if self.indices != other.indices:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def command(self):
        """Message field 'command'."""
        return self._command

    @command.setter
    def command(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'command' field must be of type 'str'"
        self._command = value

    @builtins.property
    def cobid(self):
        """Message field 'cobid'."""
        return self._cobid

    @cobid.setter
    def cobid(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cobid' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'cobid' field must be an integer in [-32768, 32767]"
        self._cobid = value

    @builtins.property
    def node_id(self):
        """Message field 'node_id'."""
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'node_id' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'node_id' field must be an integer in [-128, 127]"
        self._node_id = value

    @builtins.property
    def indices(self):
        """Message field 'indices'."""
        return self._indices

    @indices.setter
    def indices(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'indices' array.array() must have the type code of 'i'"
            self._indices = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'indices' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._indices = array.array('i', value)


# Import statements for member types

# Member 'indices'
# Member 'data'
# already imported above
# import array

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CANRead_Response(type):
    """Metaclass of message 'CANRead_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('canopen_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'canopen_interfaces.srv.CANRead_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__can_read__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__can_read__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__can_read__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__can_read__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__can_read__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CANRead_Response(metaclass=Metaclass_CANRead_Response):
    """Message class 'CANRead_Response'."""

    __slots__ = [
        '_indices',
        '_data',
        '_success',
    ]

    _fields_and_field_types = {
        'indices': 'sequence<int32>',
        'data': 'sequence<int32>',
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.indices = array.array('i', kwargs.get('indices', []))
        self.data = array.array('i', kwargs.get('data', []))
        self.success = kwargs.get('success', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.indices != other.indices:
            return False
        if self.data != other.data:
            return False
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def indices(self):
        """Message field 'indices'."""
        return self._indices

    @indices.setter
    def indices(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'indices' array.array() must have the type code of 'i'"
            self._indices = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'indices' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._indices = array.array('i', value)

    @builtins.property
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'data' array.array() must have the type code of 'i'"
            self._data = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'data' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._data = array.array('i', value)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


class Metaclass_CANRead(type):
    """Metaclass of service 'CANRead'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('canopen_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'canopen_interfaces.srv.CANRead')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__can_read

            from canopen_interfaces.srv import _can_read
            if _can_read.Metaclass_CANRead_Request._TYPE_SUPPORT is None:
                _can_read.Metaclass_CANRead_Request.__import_type_support__()
            if _can_read.Metaclass_CANRead_Response._TYPE_SUPPORT is None:
                _can_read.Metaclass_CANRead_Response.__import_type_support__()


class CANRead(metaclass=Metaclass_CANRead):
    from canopen_interfaces.srv._can_read import CANRead_Request as Request
    from canopen_interfaces.srv._can_read import CANRead_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
