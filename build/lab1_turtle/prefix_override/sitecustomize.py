import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/christooo/mobile_robotics_ws/install/lab1_turtle'
