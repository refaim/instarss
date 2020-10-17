import os
import sys

import dotenv
import sentry_sdk


def main():
    return 0


if __name__ == '__main__':
    dotenv.load_dotenv(verbose=True)

    sentry_dsn = os.getenv('SENTRY_DSN')
    if sentry_dsn:
        sentry_sdk.init(sentry_dsn, traces_sample_rate=1.0)

    sys.exit(main())
