from solana.rpc.api import Client
from solders.pubkey import Pubkey

def main():
    # Ambil alamat akun dan jaringan dari pengguna
    account_address = input("Masukkan alamat akun Solana: ")
    network = input("Masukkan jaringan (mainnet/devnet): ")

    # Tentukan endpoint berdasarkan jaringan
    if network.lower() == "mainnet":
        endpoint = "https://api.mainnet-beta.solana.com"
    elif network.lower() == "devnet":
        endpoint = "https://api.devnet.solana.com"
    else:
        print("Jaringan tidak valid. Silakan tentukan 'mainnet' atau 'devnet'.")
        return

    # Buat klien yang terhubung ke endpoint yang dipilih
    client = Client(endpoint)

    try:
        # Konversi alamat akun (string) ke objek Pubkey
        pubkey = Pubkey.from_string(account_address)

        # Dapatkan saldo dalam lamports
        balance_response = client.get_balance(pubkey)

        # Periksa apakah terdapat error dalam respons
        if getattr(balance_response, "error", None):
            print(f"Gagal mengambil saldo: {balance_response.error}")
        else:
            balance_lamports = balance_response.value
            balance_sol = balance_lamports / 1_000_000_000
            print(f"Saldo adalah {balance_sol:.9f} SOL")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
