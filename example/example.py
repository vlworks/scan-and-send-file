import sys

sys.path.append('..')

from scan_and_send_file import ScanAndSendFile

scanner = ScanAndSendFile('qwerty')
scanner.go('directory', 'https://python-scripts.com/requests')
scanner.go('directory_empty', 'https://python-scripts.com/requests')