import interactions

class Extensions(interactions.Extension):

    """
    Insérer du code ici

    /!\ Ne pas oublier le keyword self dans les fonction qui représentera la variable "bot". Ex :
    async def ping(self, event : interactions.InteractionContext):
    """

def setup(bot):
    Extensions(bot)