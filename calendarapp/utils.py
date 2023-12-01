


def check_overlap(start_time, end_time, model, instance_id=None):
    # If instance_id is provided, exclude it from the query
    if instance_id:
        return model.objects.exclude(id=instance_id).filter(start_time__lt=end_time, end_time__gt=start_time).exists()
    else:
        return model.objects.filter(start_time__lt=end_time, end_time__gt=start_time).exists()
