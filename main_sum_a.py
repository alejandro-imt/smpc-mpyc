from mpyc.runtime import mpc
import random

async def main():
    party = mpc.pid
    orig_secret = random.randint(0, 100)
    
    print("\nProgram: main_a.py")
    print(f"\nOriginal secret of P{party}: {orig_secret}")

    await mpc.start()

    secret_integer = mpc.SecInt(7)(orig_secret)
    secret = mpc.input(secret_integer)
    secret_sum = mpc.sum(secret)
    result = await mpc.output(secret_sum)
    print(f"Sum of secrets according to {party}: {result}")

    await mpc.shutdown()

if __name__ == '__main__':
    mpc.run(main())
