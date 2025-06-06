def custom_preprocessing_hook(endpoints):
    ordered_endpoints = []
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        ordered_endpoints.extend(
            [ep for ep in endpoints if ep[2] == method]
        )
    return ordered_endpoints
