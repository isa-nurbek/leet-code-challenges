# Problem Description:

"""

                                            Calendar Matching

Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar and your
co-worker's calendar (both of which contain your respective meetings for the day, in the form of `[start_time, end_time]`),
as well as both of your daily bounds (i.e., the earliest and latest times at which you're available for meetings every day,
in the form of `[earliest_time, latest_time]`).

Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily bounds, and
the duration of the meeting that you want to schedule, and that returns a list of all the time blocks (in the form of `[start_time,
end_time]`) during which you could schedule the meeting, ordered from earliest time block to latest.

> Note that times will be given and should be returned in military time. For example: `8:30`, `9:01`, and `23:56`.
> Also note that the given calendar times will be sorted by start time in ascending order, as you would expect them to appear in a
calendar application like `Google Calendar`.



## Sample Input
```
calendar_1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
daily_bounds_1 = ['9:00', '20:00']
calendar_2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
daily_bounds_2 = ['10:00', '18:30']
meeting_duration = 30
```

## Sample Output
```
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
```

## Optimal Time & Space Complexity:
```
O(c1 + c2) time | O(c1 + c2) space - where `c1` and `c2` are the respective numbers of meetings in `calendar_1` and `calendar_2`.
```
"""

# =========================================================================================================================== #

# Solution:


# O(c1 + c2) time | O(c1 + c2) space
def calendar_matching(
    calendar_1, daily_bounds_1, calendar_2, daily_bounds_2, meeting_duration
):
    """
    Main function to find available meeting times between two calendars.

    Args:
        calendar_1: List of meetings for person 1, each as [start_time, end_time] strings
        daily_bounds_1: Daily availability bounds for person 1 as [start_time, end_time]
        calendar_2: List of meetings for person 2, each as [start_time, end_time] strings
        daily_bounds_2: Daily availability bounds for person 2 as [start_time, end_time]
        meeting_duration: Required duration for the meeting in minutes

    Returns:
        List of available time slots that fit the meeting duration
    """
    # Update calendars with daily bounds and convert times to minutes
    updated_calendar_1 = update_calendar(calendar_1, daily_bounds_1)
    updated_calendar_2 = update_calendar(calendar_2, daily_bounds_2)

    # Merge both calendars together in sorted order
    merge_calendar = merge_calendars(updated_calendar_1, updated_calendar_2)

    # Flatten overlapping or adjacent meetings in the merged calendar
    flattened_calendar = flatten_calendar(merge_calendar)

    # Find available slots that can fit the meeting duration
    return get_matching_availabilities(flattened_calendar, meeting_duration)


def update_calendar(calendar, daily_bounds):
    """
    Adds daily bounds to the calendar and converts all times to minutes.

    Args:
        calendar: List of meetings in time string format
        daily_bounds: Daily availability bounds in time string format

    Returns:
        New calendar with bounds added and all times converted to minutes
    """
    updated_calendar = calendar[:]
    # Add daily bounds as meetings at start and end of day
    updated_calendar.insert(0, ["0:00", daily_bounds[0]])
    updated_calendar.append([daily_bounds[1], "23:59"])

    # Convert all time strings to minute values
    return list(
        map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], updated_calendar)
    )


def merge_calendars(calendar_1, calendar_2):
    """
    Merges two calendars together in sorted order by start time.

    Args:
        calendar_1: First calendar in minutes format
        calendar_2: Second calendar in minutes format

    Returns:
        Single merged calendar sorted by meeting start times
    """
    merged = []
    i, j = 0, 0

    # Merge the two calendars like in merge sort
    while i < len(calendar_1) and j < len(calendar_2):
        meeting_1, meeting_2 = calendar_1[i], calendar_2[j]

        if meeting_1[0] < meeting_2[0]:
            merged.append(meeting_1)
            i += 1
        else:
            merged.append(meeting_2)
            j += 1

    # Add any remaining meetings from either calendar
    while i < len(calendar_1):
        merged.append(calendar_1[i])
        i += 1

    while j < len(calendar_2):
        merged.append(calendar_2[j])
        j += 1

    return merged


def flatten_calendar(calendar):
    """
    Combines overlapping or adjacent meetings in a calendar.

    Args:
        calendar: List of meetings in minutes format

    Returns:
        New calendar with overlapping/adjacent meetings merged
    """
    if not calendar:
        return []

    flattened = [calendar[0][:]]  # Start with first meeting

    for i in range(1, len(calendar)):
        current_meeting = calendar[i]
        previous_meeting = flattened[-1]

        current_start, current_end = current_meeting
        previous_start, previous_end = previous_meeting

        # If meetings overlap or are adjacent, merge them
        if previous_end >= current_start:
            new_previous_meeting = [previous_start, max(previous_end, current_end)]
            flattened[-1] = new_previous_meeting
        else:
            flattened.append(current_meeting[:])

    return flattened


def get_matching_availabilities(calendar, meeting_duration):
    """
    Finds available time slots between meetings that can fit the required duration.

    Args:
        calendar: Flattened calendar in minutes format
        meeting_duration: Required meeting duration in minutes

    Returns:
        List of available time slots in time string format
    """
    matching_availabilities = []

    # Check the gaps between consecutive meetings
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]  # End of previous meeting
        end = calendar[i][0]  # Start of next meeting

        availability_duration = end - start
        if availability_duration >= meeting_duration:
            matching_availabilities.append([start, end])

    # Convert minute values back to time strings
    return list(
        map(
            lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])],
            matching_availabilities,
        )
    )


def time_to_minutes(time):
    """
    Converts time string (HH:MM) to minutes since midnight.

    Args:
        time: Time string in HH:MM format

    Returns:
        Integer representing total minutes
    """
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


def minutes_to_time(minutes):
    """
    Converts minutes since midnight to time string (HH:MM).

    Args:
        minutes: Integer representing total minutes

    Returns:
        Time string in HH:MM format
    """
    hours = minutes // 60
    mins = minutes % 60

    hours_string = str(hours)
    minutes_string = "0" + str(mins) if mins < 10 else str(mins)

    return hours_string + ":" + minutes_string


# Test Case:

calendar_1 = [
    ["9:00", "10:30"],
    ["12:00", "13:00"],
    ["16:00", "18:00"],
]
daily_bounds_1 = ["9:00", "20:00"]
calendar_2 = [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"],
]
daily_bounds_2 = ["10:00", "18:30"]
meeting_duration = 30

print(
    calendar_matching(
        calendar_1, daily_bounds_1, calendar_2, daily_bounds_2, meeting_duration
    )
)

# Output: [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
