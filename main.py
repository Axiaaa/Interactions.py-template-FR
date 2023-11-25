import interactions, os
from decouple import config


TOKEN = config('TOKEN')

bot = interactions.Client(token=TOKEN, intents=interactions.Intents.ALL)

@interactions.slash_command(
    name="ping",
    description="Ping",
    # scopes=[1172931641317019678],
    dm_permission=False,
    # default_member_permissions=interactions.Permissions.ADMINISTRATOR
)
async def ping(ctx : interactions.InteractionContext):
    """
    
    Cette commande permet de ping.
    
    Args:
        ctx (interactions.InteractionContext): Contexte de la commande
        
    Retourne :
        None
    """
    await ctx.respond("Pong!")
    # await ctx.send(f"{ctx.author.id}")


def load_extensions(bot, folder, folder_name="", exclude_files=[]):
    """
    Cette fonction permet de charger les extensions (fichers sources) du bot.

    Args:
        bot (interactions.Client): Client du bot
        folder (str): Dossier contenant les extensions
        folder_name (str, optional): Nom du dossier. Defaults to "".
        exclude_files (list, optional): Fichiers à exclure. Defaults to [].
    
    Retourne :
        None
    """
    extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
    for ext in extensions:
        print(f"{ext} a été chargé !")
        bot.load_extension(f"{folder_name}{ext}")

load_extensions(bot, "ext", "ext.")

bot.start()