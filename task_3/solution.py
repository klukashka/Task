def appearance(intervals: dict[str, list[int]]) -> int:
    pupil = [
        (intervals["pupil"][i], intervals["pupil"][i+1])
        for i in range(0, len(intervals["pupil"]), 2)
    ]
    tutor = [
        (intervals["tutor"][i], intervals["tutor"][i+1])
        for i in range(0, len(intervals["tutor"]), 2)
    ]
    lesson = intervals["lesson"]


    pupil_time_set = set()
    [pupil_time_set.update(set(range(elem[0], elem[1]))) for elem in pupil]  # sets of ranges

    tutor_time_set = set()
    [tutor_time_set.update(set(range(elem[0], elem[1]))) for elem in tutor]  # sets of ranges

    lesson_time_set = set(range(lesson[0], lesson[1]))  # set of ranges

    # Find the intersection of these three sets
    common_lesson_time = lesson_time_set.intersection(tutor_time_set).intersection(pupil_time_set)

    return len(common_lesson_time)
