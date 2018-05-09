import click
import rest_api_client


@click.command(help="Transfer tokens to target address")
@click.option("--token-address", help="Address of the token that you want to transfer", type=str, prompt=True)
@click.option("--target-address", help="Address you want to transfer tokens to", type=str, prompt=True)
@click.option("--amount", help="Amount of tokens to transfer", type=int, prompt=True)
def main(token_address, target_address, amount):
    print("Calling the transfer tokens API: ")
    resp = rest_api_client.transfer_tokens(token_address, target_address, amount)
    print(resp)


if __name__ == '__main__':
    main()