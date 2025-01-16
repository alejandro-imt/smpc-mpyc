import numpy as np
from mpyc.runtime import mpc

async def main():
    mpc.parties = mpc.parties[:3]  # restrict to first three parties
    await mpc.start()  # connect to all other parties
    print("".join(await mpc.transfer("Hello world!")))
    await mpc.shutdown()  # disconnect, but only once all other parties reached this point

# Run the main function
if __name__ == "__main__":
    mpc.run(main())
    
# Compare this snippet from test_palm_codes.py


        
