def coverage(records, dimensions):
    if not records:
        return 0.0
    complete = 0
    for record in records:
        if all(str(getattr(record, d, "")).strip() for d in dimensions):
            complete += 1
    return complete / len(records)


def collision_rate(architecture, dimensions):
    groups = architecture.group(dimensions)
    if not architecture.records:
        return 0.0
    collided = sum(len(ids) for ids in groups.values() if len(ids) > 1)
    return collided / len(architecture.records)


def distinguishability(architecture, dimensions):
    if not architecture.records:
        return 0.0
    unique = len(architecture.group(dimensions))
    return unique / len(architecture.records)
