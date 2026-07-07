import datetime
import webbrowser


def get_current_time():
    """Return the current time as a formatted string."""
    return datetime.datetime.now().strftime("%I:%M %p")


def get_current_date():
    """Return the current date as a formatted string."""
    return datetime.datetime.now().strftime("%A, %d %B %Y")


def open_web_search(topic):
    """
    Open a Google search for the given topic.
    """
    query = topic.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)