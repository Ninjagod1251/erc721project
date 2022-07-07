import ape


def test_erc165(nft):
    # ERC165 interface ID of ERC165
    assert nft.supportsInterface("0x01ffc9a7")

    # ERC165 specifies that this is never supported
    assert not nft.supportsInterface("0xffffffff")

    # ERC165 interface ID of ERC721
    assert nft.supportsInterface("0x80ac58cd")

    # ERC165 interface ID of ERC721 Metadata Extension
    assert nft.supportsInterface("0x5b5e139f")

    # ERC165 interface ID of ERC4494
    assert nft.supportsInterface("0x5604e225")


def test_init(nft, owner):
    assert nft.balanceOf(owner) == 0
    with ape.reverts():
        assert nft.ownerOf(0)
