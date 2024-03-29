"""
Parses all custom options and arguments
"""
import argparse

def parse():
    """
    Handles the arguments and options.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        "-w", "--what", dest="what",
        help="REQUIRED - The absolute path to the folder containing the tests"
    )

    parser.add_argument(
        "-f", "--failfast", dest="failfast", default=False,
        action="store_true", help="Stop executing tests on the first error or failure."
    )

    parser.add_argument(
        "-t", "--tags", dest="tags", default=[],
        help="Run only tests with specific tags\n" + \
            "USAGE: -t=tag1 || -t=tag1,tag2"
    )

    parser.add_argument(
        "-s", "--showtags", dest="show_tags", default=False,
        action="store_true",
        help="Show what tags are available for the tests. Won't run any tests!"
    )

    parser.add_argument(
        "-e", "--extra", dest="extra_assignments", default=False,
        action="store_true", help="Includes tests for extra assignments"
    )

    parser.add_argument(
        "--trace", dest="trace_assertion_error", default=False,
        action="store_true", help="Adds a traceback option for assertion errors"
    )

    parser.add_argument(
        "--exam", dest="exam", default=False,
        action="store_true", help="Use when running test for an exam"
    )

    parser.add_argument(
        "--sentry", dest="sentry", default=True,
        action="store_false", help="Use to to disable sending anonymous metrics to Sentry"
    )

    parser.add_argument(
        "--sentry_url", dest="sentry_url",
        help="REQUIRED unless using --sentry. - URL for sending sentry metrics"
    )

    parser.add_argument(
        "--sentry_release", dest="sentry_release",
        help="REQUIRED unless using --sentry. - Release to use in sentry"
    )

    parser.add_argument(
        "--sentry_sample_rate", dest="sentry_sample_rate",
        help="REQUIRED unless using --sentry. - sample_rate to use in sentry"
    )

    parser.add_argument(
        "--sentry_user", dest="sentry_user", default="Jane Doe",
        help="String to identify user in Sentry logs."
    )

    args, _empty = parser.parse_known_args()

    if args.tags:
        args.tags = args.tags.split(",")

    return args
