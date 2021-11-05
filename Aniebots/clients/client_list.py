import telethon.utils

from .session import mew, H2 H3, H4, H5
from Aniebots.config import Config


async def clients_list(Config, mew,):
    user_ids = list(Config.SUDO_USERS) or []
    main_id = await Hell.get_me()
    user_ids.append(main_id.id)

    try:
        if H2 is not None:
            id2 = await H2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if H3 is not None:
            id3 = await H3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if H4 is not None:
            id4 = await H4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if H5 is not None:
            id5 = await H5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event):
    client = await event.client.get_me()
    uid = telethon.utils.get_peer_id(client)
    D3NVIL = uid
    mew_USER = client.first_name
    mew_mention = f"[{Anie_USER}](tg://user?id={d3nvil})"
    return d3nvil, Anie_USER, Anie_mention
