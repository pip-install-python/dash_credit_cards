# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashCreditCardInput(Component):
    """A DashCreditCardInput component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- acceptedCards (list; optional)

- cardCVCInputProps (dict; optional)

- cardExpiryInputProps (dict; optional)

- cardImageClassName (string; optional)

- cardImageStyle (dict; optional)

- cardNumber (string; default '')

- cardNumberInputProps (dict; optional)

- className (string; optional)

- containerClassName (string; optional)

- containerStyle (dict; optional)

- customTextLabels (dict; optional)

- cvc (string; default '')

- dangerTextClassName (string; optional)

- dangerTextStyle (dict; optional)

- expiry (string; default '')

- fieldClassName (string; optional)

- fieldStyle (dict; optional)

- inputClassName (string; optional)

- inputComponent (string; optional)

- inputStyle (dict; optional)

- invalidClassName (string; optional)

- invalidStyle (dict; optional)

- issuer (string; optional)

- placeholders (dict; optional)

- preview (boolean; optional)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_credit_cards'
    _type = 'DashCreditCardInput'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, cardNumberInputProps=Component.UNDEFINED, cardExpiryInputProps=Component.UNDEFINED, cardCVCInputProps=Component.UNDEFINED, fieldClassName=Component.UNDEFINED, inputComponent=Component.UNDEFINED, containerClassName=Component.UNDEFINED, customTextLabels=Component.UNDEFINED, placeholders=Component.UNDEFINED, issuer=Component.UNDEFINED, preview=Component.UNDEFINED, acceptedCards=Component.UNDEFINED, callback=Component.UNDEFINED, onError=Component.UNDEFINED, cardNumberInputRenderer=Component.UNDEFINED, cardExpiryInputRenderer=Component.UNDEFINED, cardCVCInputRenderer=Component.UNDEFINED, cardImageClassName=Component.UNDEFINED, cardImageStyle=Component.UNDEFINED, containerStyle=Component.UNDEFINED, dangerTextClassName=Component.UNDEFINED, dangerTextStyle=Component.UNDEFINED, fieldStyle=Component.UNDEFINED, inputClassName=Component.UNDEFINED, inputStyle=Component.UNDEFINED, invalidClassName=Component.UNDEFINED, invalidStyle=Component.UNDEFINED, cardNumber=Component.UNDEFINED, expiry=Component.UNDEFINED, cvc=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'acceptedCards', 'cardCVCInputProps', 'cardExpiryInputProps', 'cardImageClassName', 'cardImageStyle', 'cardNumber', 'cardNumberInputProps', 'className', 'containerClassName', 'containerStyle', 'customTextLabels', 'cvc', 'dangerTextClassName', 'dangerTextStyle', 'expiry', 'fieldClassName', 'fieldStyle', 'inputClassName', 'inputComponent', 'inputStyle', 'invalidClassName', 'invalidStyle', 'issuer', 'placeholders', 'preview', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'acceptedCards', 'cardCVCInputProps', 'cardExpiryInputProps', 'cardImageClassName', 'cardImageStyle', 'cardNumber', 'cardNumberInputProps', 'className', 'containerClassName', 'containerStyle', 'customTextLabels', 'cvc', 'dangerTextClassName', 'dangerTextStyle', 'expiry', 'fieldClassName', 'fieldStyle', 'inputClassName', 'inputComponent', 'inputStyle', 'invalidClassName', 'invalidStyle', 'issuer', 'placeholders', 'preview', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DashCreditCardInput, self).__init__(children=children, **args)
