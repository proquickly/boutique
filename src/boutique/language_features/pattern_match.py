def do_something():
    pass

def parse_json_example(event):
    match event:
        case {
            "issue": {"closed_at": closed},
            "comment": {"created_at": commented},
            } if closed == commented:
            pass

        case {"sender": {"login": who}} if who == get_bot_username():
            pass

        case {"issue": {"pull_request": _}}:
            # The comment is on a pull request. Process it.
            return do_something(event)