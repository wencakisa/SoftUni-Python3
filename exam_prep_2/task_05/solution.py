from urllib.parse import urlparse

IGNORE_ENDING_WITH = '/ws/'


def main():
    input_filename = input()

    url_times = {}  # key: url / value: [total_count, total_time]
    for url_path, resp_t in load_log_lines(input_filename):
        if url_path not in url_times:
            url_times[url_path] = [0, 0]

        url_times[url_path][0] += 1
        url_times[url_path][1] += resp_t

    if url_times:
        max_avg_time_url = max(
            url_times.items(),
            key=lambda kv: kv[1][1] / kv[1][0]
        )

        print(max_avg_time_url[0])
        print('{:.3f}'.format(max_avg_time_url[1][1] / max_avg_time_url[1][0]))


def load_log_lines(input_filename: str):
    with open(input_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            url = get_field(line, prefix='url="', suffix='"')
            resp_t = float(get_field(line, prefix='resp_t="', suffix='"'))

            url_parse_result = urlparse(url)
            url_path = url_parse_result.path

            if not url_path.endswith(IGNORE_ENDING_WITH):
                yield url_path, resp_t


def get_field(line, prefix, suffix):
    """
    >>> get_field('.... resp_t="2.34" neshto drugo we', prefix='resp_t="', suffix='"')
    '2.34'
    """
    prefix_len = len(prefix)
    idx_prefix = line.find(prefix)

    if idx_prefix >= 0:
        idx_suffix = line.find(suffix, idx_prefix + prefix_len)
        if idx_suffix >= 0:
            return line[idx_prefix + prefix_len: idx_suffix]

if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod()
