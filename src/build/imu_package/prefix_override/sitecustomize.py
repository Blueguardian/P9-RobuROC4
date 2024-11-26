import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/roburoc/PycharmProjects/P9-RobuROC4/src/install/imu_package'
