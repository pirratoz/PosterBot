from uvloop import run as uvloop_run

from source.services import ServiceApiSession


async def main() -> None:
    api = ServiceApiSession()

    await api.session.close()


if __name__ == "__main__":
    uvloop_run(main())
