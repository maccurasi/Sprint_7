class ResponseMessages:
    """Ожидаемые тела ответов с ошибками — по документации сервиса."""

    CREATE_COURIER_MISSING_DATA = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи",
    }
    COURIER_LOGIN_ALREADY_EXISTS = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой.",
    }
    LOGIN_MISSING_DATA = {
        "code": 400,
        "message": "Недостаточно данных для входа",
    }
    ACCOUNT_NOT_FOUND = {
        "code": 404,
        "message": "Учетная запись не найдена",
    }


class TestData:
    """Наборы данных для параметризации."""

    # firstName сознательно не проверяется: сервис создаёт курьера без него,
    # хотя документация помечает поле обязательным (дефект зафиксирован в README).
    REQUIRED_COURIER_FIELDS = ("login", "password")

    REQUIRED_LOGIN_FIELDS = ("login",)

    ORDER_COLOURS = (
        ("black", ["BLACK"]),
        ("grey", ["GREY"]),
        ("black_and_grey", ["BLACK", "GREY"]),
        ("without_colour", None),
    )

    ORDERS_LIST_PARAMS = {"limit": 5, "page": 0}
