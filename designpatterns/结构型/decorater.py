from functools import wraps

HOST_DOCKER = 0


def decorater(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0].type != HOST_DOCKER:
            raise Exception("not docker host")
        else:
            return f(*args, **kwargs)

    return wrapper


class Host:
    def __init__(self, host_type):
        self.type = host_type

    @decorater
    def create_container(self):
        print("create container success")


if __name__ == '__main__':
    host_1 = Host(host_type=HOST_DOCKER)
    host_1.create_container()
    print("===============================")
    host_2 = Host(1)
    host_2.create_container()
