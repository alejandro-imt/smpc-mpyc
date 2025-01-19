# Program to compute the dot product in MPC
from mpyc.runtime import mpc
import random

async def main():
    party = mpc.pid
    num_parties = len(mpc.parties)
    orig_a = random.randint(0, 100)
    orig_b = random.randint(0, 100)

    # Starting the MPC runtime
    await mpc.start()

    integer_a = mpc.SecInt(7)(orig_a)
    integer_b = mpc.SecInt(7)(orig_b)
    
    secret_a = mpc.input(integer_a, senders=0)
    secret_b = mpc.input(integer_b, senders=0)

    # Product
    secret_prod = mpc.mul(secret_a, secret_b)
    result = await mpc.output(secret_prod)
    print(f"\nProduct of a={orig_a} and b={orig_b}: {result}")
    
    if party == 0:
        i = 0
        
    # Terminating the MPC runtime
    await mpc.shutdown()

if __name__ == "__main__":
    mpc.run(main())
