if IN_DOCKER:  # type: ignore
    # print("Running in docker")
    assert MIDDLEWARE[:1] == [  # type: ignore
        'django.middleware.security.SecurityMiddleware',
    ]
