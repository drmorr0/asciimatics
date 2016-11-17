from asciimatics.screen import Screen

# Colour palette for the widgets within the Frame.
DEFAULT_PALETTE = {
    "background":
        (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "shadow":
        (Screen.COLOUR_BLACK, None, Screen.COLOUR_BLACK),
    "disabled":
        (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_BLUE),
    "label":
        (Screen.COLOUR_GREEN, Screen.A_BOLD, Screen.COLOUR_BLUE),
    "borders":
        (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_BLUE),
    "scroll":
        (Screen.COLOUR_CYAN, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "title":
        (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_BLUE),
    "edit_text":
        (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "focus_edit_text":
        (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_CYAN),
    "button":
        (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "focus_button":
        (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_CYAN),
    "control":
        (Screen.COLOUR_YELLOW, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "selected_control":
        (Screen.COLOUR_YELLOW, Screen.A_BOLD, Screen.COLOUR_BLUE),
    "focus_control":
        (Screen.COLOUR_YELLOW, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "selected_focus_control":
        (Screen.COLOUR_YELLOW, Screen.A_BOLD, Screen.COLOUR_CYAN),
    "field":
        (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "selected_field":
        (Screen.COLOUR_YELLOW, Screen.A_BOLD, Screen.COLOUR_BLUE),
    "focus_field":
        (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLUE),
    "selected_focus_field":
        (Screen.COLOUR_WHITE, Screen.A_BOLD, Screen.COLOUR_CYAN),
}
