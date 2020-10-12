import json
from datetime import datetime
from tanner import config
from urllib.parse import urlencode

class Reporting:
    @staticmethod
    def create_session(session_data):
        report_file = config.TannerConfig.get('LOCALLOG', 'PATH')
        with open(report_file, 'a') as out:
            session_data["timestamp"] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
            if session_data.get('post_data', None):
                session_data['post_data'] = urlencode(session_data['post_data'])
            else:
                session_data['post_data'] = ''
            json.dump(session_data, out)
            out.write('\n')
