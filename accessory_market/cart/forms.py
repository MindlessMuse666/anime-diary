from django.forms import Form, TypedChoiceField, BooleanField, HiddenInput


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(Form):
    quantity: int = TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    override = BooleanField(
        required=False,
        initial=False,
        widget=HiddenInput
    )