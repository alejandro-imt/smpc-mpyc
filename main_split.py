# Program to check if a values is greater than other
from mpyc.runtime import mpc
import random

async def main():
    party = mpc.pid
    num_parties = mpc.parties
    orig_secret = random.randint(0, 100)
    
    print(f"\nOriginal value of P{party}: {orig_secret}")

    await mpc.start()

    secret_integer = mpc.SecInt(7)(orig_secret)
    secret = mpc.input(secret_integer, senders=0)
    print(f"\nSecret of P{party} has been distributed among {num_parties} parties.")

    if party == 1:
        rec_secret = await mpc.output(secret, receivers=1)
        print(f"\nSecret of P{party} recovered by P1: {rec_secret}")
    
    await mpc.shutdown()

if __name__ == '__main__':
    mpc.run(main())
