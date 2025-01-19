import mpyc.runtime
import configparser

# Number of parties
m = 3

# List of addresses for parties
addresses = [("127.0.0.1", "6001"), ("127.0.0.1", "6002"), ("127.0.0.1", "6003")]

# Create a ConfigParser for parties addresses
output = mpyc.runtime.generate_configs(m, addresses)

# Write each ConfigParser to an ini file
for i in range(m):
    config = configparser.ConfigParser()
    config = output[i]
    with open(f"config_P{i+1}.ini", "w") as configfile:
        config.write(configfile)

