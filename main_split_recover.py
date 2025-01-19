# Program to check if a values is greater than other
from mpyc.runtime import mpc
import random


async def main():
    party = mpc.pid

    await mpc.start()

    secret_rec = await mpc.output()

    print(f"\nParty P{party} recovered the secret: {secret_rec}.")

    await mpc.shutdown()

if __name__ == "__main__":
    mpc.run(main())
