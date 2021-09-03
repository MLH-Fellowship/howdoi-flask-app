from howdoi import howdoi

def send_output(user_input):
    # calling howdoi CLI for get_parser function in howdoi package 
    parser = howdoi.get_parser()
    # distributing the input by user and parsing it
    tokens = vars(parser.parse_args(user_input.split(' ')))
    running howdoi
    output = howdoi.howdoi(tokens)
    return output