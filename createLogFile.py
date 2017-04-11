filename = 'D:/qgis.log'

def write_log_message(message, tag, level):
    with open(filename, 'a') as logfile:
        logfile.write('{tag}({level}): {message}'.format(tag=tag, level=level, message=message.encode('utf-8')))

QgsMessageLog.instance().messageReceived.connect(write_log_message)