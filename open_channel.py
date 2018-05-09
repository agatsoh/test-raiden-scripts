import click
import rest_api_client


@click.command(help="Open a channel with a partner address ")
@click.option("--token-address", help="Address of underlying token", type=str, prompt=True)
@click.option("--partner-address", help="Address of the partner", type=str, prompt=True)
@click.option("--balance", help="Balance of the channel", type=int, prompt=True)
@click.option("--settle-timeout", help="Settle timeout of the channel", type=int, prompt=True)
def main(token_address, partner_address, balance, settle_timeout):
    print("Calling the Open Channel API: ")
    resp = rest_api_client.open_channel(token_address, partner_address, balance, settle_timeout)
    print(resp)

if __name__=='__main__':
    main()