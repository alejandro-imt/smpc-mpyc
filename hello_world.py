from mpyc.runtime import mpc


async def main():
    await mpc.start()
    print("".join(await mpc.transfer("Hello world!")))
    await mpc.shutdown()


if __name__ == "__main__":
    mpc.run(main())
