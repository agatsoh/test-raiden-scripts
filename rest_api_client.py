from requests import put, get, post


def transfer_tokens(token, partner, amount, host="localhost", port=5001):
    transfer_token_url = "http://{}:{}/api/1/transfers/{}/{}".format(host, port, token, partner)
    payload = {
        "amount": amount,
        "identifier": 1
    }
    print(transfer_token_url)
    transfer_resp = post(transfer_token_url, data=payload)
    return transfer_resp.json() if transfer_resp.status_code == 200 \
        else "Got Status {}".format(transfer_resp.status_code)


def open_channel(token, partner, balance, settle_timeout, host="localhost", port=5001):
    open_channel_url = "http://{}:{}/api/1/channels".format(host, port)
    payload = {
        "partner_address": partner,
        "token_address": token,
        "balance": balance,
        "settle_timeout": settle_timeout
    }
    print(open_channel_url)
    open_channel_resp = put(open_channel_url, data=payload)
    return open_channel_resp.json() if open_channel_resp.status_code == 201 \
        else "Got Status {}".format(open_channel_resp.status_code)
