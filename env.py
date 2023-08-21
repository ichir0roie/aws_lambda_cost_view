import sync_env


class Env(sync_env.SyncEnv):
    ACCOUNT_ID = None
    REPOSITORY_NAME = None
    REPOSITORY_REGION = None
    AWS_CLI_PROFILE = None

    SLACK_MESSAGE_TITLE = None
    SLACK_CHANNEL = None
    SLACK_XOXB = None


env = Env()


if __name__ == "__main__":
    env._generate()
