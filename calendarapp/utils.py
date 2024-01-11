def check_overlap(start_time, end_time, model, instance_id=None):
    """ Check if there is an overlap between the start and end time of an event """
    # If instance_id is provided, exclude it from the query
    if instance_id:
        overlap = model.objects.exclude(id=instance_id)
        overlap = overlap.filter(start_time__lt=end_time, end_time__gt=start_time)
        return overlap.exists()
    else:
        overlap = model.objects.filter(start_time__lt=end_time, end_time__gt=start_time)
        return overlap.exists()