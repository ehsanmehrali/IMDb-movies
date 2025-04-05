def print_emoji_chars_with_yellow_background(ann_msg_bg_yellow):
    ann_msg_bg_yellow = f"\033[30m\033[103m{ann_msg_bg_yellow:^104}\033[0m"
    print(ann_msg_bg_yellow)


def print_announcements_msgs_with_yellow_background(ann_msg_bg_yellow):
    ann_msg_bg_yellow = f"\033[30m\033[103m{ann_msg_bg_yellow:<110}\033[0m"
    print(ann_msg_bg_yellow)


def print_announcements_msgs_with_green_background_(ann_msg_bg_green):
    ann_msg_bg_green = f"\033[30m\033[102m{ann_msg_bg_green:<110}\033[0m"
    print(ann_msg_bg_green)


def print_announcements_with_blue_background(ann_msg_bg_blue):
    ann_msg_bg_blue = f"\033[30m\033[44m{ann_msg_bg_blue:<110}\033[0m"
    print(ann_msg_bg_blue)


def input_announcements_msgs_with_yellow_background(inp_msg_bg_yellow):
    return f"\033[30m\033[103m{inp_msg_bg_yellow:<110}\033[0m"


def input_announcements_msgs_with_blue_background(inp_msg_bg_green):
    return f"\033[30m\033[44m{inp_msg_bg_green:<110}\033[0m"


def print_result_with_green_background(list_output):
    list_output = f"\033[30m\033[102m{list_output:<110}\033[0m"
    print(list_output)


def print_red_color_alert_with_black_background(alert_message):
    alert_message = f"\033[91m\033[40m{alert_message:<110}\033[0m"
    print(alert_message)


def print_green_background_success_message(success_message):
    success_message = f"\033[32m\033[7m{success_message:<110}\033[0m"
    print(success_message)


def main():
    print("Terminal custom styles")


if __name__ == "__main__":
    main()