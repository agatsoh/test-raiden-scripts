import click
import pprint
from requests import put, get, post


@click.command(help="Join an existing token network")
@click.option("--token", help="Address of the token that you want to connect", type=str, prompt=True)
@click.option("--funds", help="Funds to keep in Escrow to open channels", type=int, prompt=True)
@click.option("--initial-channel-target", help="Number of nodes to connect", type=int)
@click.option("--joinable-funds-target", help="percentage of funds to leave unassigned", type=float)
@click.option("--host", help="host ip of the raiden machine", default="localhost", type=str)
@click.option("--port", help="port raiden api's are hosted", default=5001, type=int)
def main(token, funds, initial_channel_target, joinable_funds_target, host, port):

    payload = {
        "funds": funds
    }
    if initial_channel_target:
        payload["initial_channel_target"] = initial_channel_target
    if joinable_funds_target:
        payload["joinable_funds_target"] = joinable_funds_target

    join_network_url = "http://{}:{}/api/1/connections/{}".format(host, port, token)
    print("Calling Enpoint: ", join_network_url)
    put_request = put(join_network_url, data=payload)
    assert put_request.status_code == 204
    print("Joining token network successful")

if __name__ == '__main__':
    main()