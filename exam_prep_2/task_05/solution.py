import sys
from urllib.parse import urlparse
from collections import defaultdict


RESPONSE_TIME_FIELD_PREFIX = 'resp_t="'
URL_FIELD_PREFIX = 'url="'

FIELD_SUFFIX = '"'

IGNORE_ENDING_WITH = '/ws/'


def main():
    try:
        log_filename = input()

        log_dict = defaultdict(list)
        for resp_t, url_path in load_log_lines(log_filename):
            log_dict[url_path].append(resp_t)

        if log_dict:
            for url_path, resp_times in log_dict.items():
                # Convert response times to average response time
                log_dict[url_path] = sum(resp_times) / len(resp_times)

            max_resp_t_url, max_resp_t = max(
                log_dict.items(),
                key=lambda kv: kv[1]
            )

            print(max_resp_t_url)
            print('{:.3f}'.format(max_resp_t))
        else:
            print('NO DATA.')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_log_lines(log_filename: str) -> tuple:
    with open(log_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line:
                resp_t = get_field(line, prefix=RESPONSE_TIME_FIELD_PREFIX)
                resp_t = float(resp_t)

                url = get_field(line, prefix=URL_FIELD_PREFIX)
                url_path = urlparse(url).path

                if not url_path.endswith(IGNORE_ENDING_WITH):
                    yield resp_t, url_path


def get_field(line: str, prefix: str, suffix: str=FIELD_SUFFIX) -> str:
    prefix_len = len(prefix)
    prefix_index = line.find(prefix)

    if prefix_index >= 0:
        suffix_index = line.find(suffix, prefix_index + prefix_len)
        if suffix_index >= 0:
            return line[prefix_index + prefix_len: suffix_index]

if __name__ == '__main__':
    sys.exit(main())
