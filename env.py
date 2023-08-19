import sync_env


class Env(sync_env.SyncEnv):
    ACCOUNT_ID = None
    REPOSITORY_NAME = None
    REPOSITORY_REGION = None
    TOPIC_ARN = None


env = Env()


if __name__ == "__main__":
    env._generate()
