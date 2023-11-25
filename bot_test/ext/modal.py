import interactions

class Modal(interactions.Extension):

    @interactions.slash_command(name="test")
    async def command(self, ctx: interactions.InteractionContext):
        """
        Ce modal permet de tester les modals.

        Args:
            ctx (interactions.InteractionContext): Contexte de la commande

        Retourne :
            None
    
        """
        my_modal = interactions.Modal(
            interactions.ShortText(label="Short Input Text", custom_id="short_text"),
            interactions.ParagraphText(label="Long Input Text", custom_id="long_text"),
            title="My Modal",
            custom_id="pouet"
            )
        await ctx.send_modal(modal=my_modal)

    @interactions.modal_callback("pouet")
    async def on_modal_answer(self, ctx: interactions.ModalContext, short_text: str, long_text: str):
        """
        Ce listener permet de récupérer les réponses d'un modal.

        Args:
            ctx (interactions.ModalContext): Contexte du modal
            short_text (str): Case "Short Input Text"
            long_text (str): Case "Long Input Text"

        Retourne :
            None
        """
        await ctx.send(f"Custom id: {ctx.custom_id}Short text: {short_text}, Paragraph text: {long_text}")

def setup(bot):
    Modal(bot)