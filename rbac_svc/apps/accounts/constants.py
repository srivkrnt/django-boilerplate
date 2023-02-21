from apps.base.enum import ConstantEnum


class Stakeholders(ConstantEnum):
    """
    Stakeholders
    """

    PLATFORM = 'platform'
    LSP = 'lsp'
    BANK = 'bank'
    SELLER = 'seller'


class UserType(Stakeholders):
    """
    same as stakeholders, just for better comprehension use UserType when talking about users
    """


class Errors:
    """
    Errors
    """

    INVALID_PLATFORM_ID = "Platform ID is not valid"
    INVALID_EMAIL = "EMAIL :: {email} doesn't correspond to any user"
    INVALID_PASSWORD = "Password provided is not valid"

    # Kafka Errors
    NO_PRODUCER_FOUND = "No Producer found"
    NO_TOPIC_FOUND = "No topic found"


class KeyLabels(ConstantEnum):
    """
    Keylabels
    """

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    META = "meta"
    PAYLOAD = "payload"
    JOB_TYPE = "job_type"
    STAKEHOLDER_TYPE = "stakeholder_type"
    EMAIL = "email"
    PASSWORD = "password"
    LOGIN = "login"
    LOGOUT = "logout"


class KafkaTopics(ConstantEnum):
    """
    Kafka Topics
    """

    SELLER_SYNC = "seller_sync"
    PLATFORM_SYNC = "platform_sync"


class KafkaActions(ConstantEnum):
    """
    Kafka actions
    """

    CREATE_SELLER = "create_seller"
    UPDATE_SELLER = "update_seller"
    CREATE_PLATFORM = "create_platform"
    UPDATE_PLATFORM = "update_platform"
    CREATE_PLATFORM_USER = "create_platform_user"
    UPDATE_PLATFORM_USER = "update_platform_user"
