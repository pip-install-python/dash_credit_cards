# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashCreditCards(Component):
    """A DashCreditCards component.


Keyword arguments:

- id (string; optional)

- acceptedCards (list; optional)

- cvc (string | number; optional)

- expiry (string | number; optional)

- focused (string; optional)

- issuer (string; optional)

- locale (dict; optional)

- name (string | number; optional)

- number (string | number; optional)

- placeholders (dict; optional)

- preview (boolean; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_credit_cards'
    _type = 'DashCreditCards'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, name=Component.UNDEFINED, number=Component.UNDEFINED, expiry=Component.UNDEFINED, cvc=Component.UNDEFINED, focused=Component.UNDEFINED, locale=Component.UNDEFINED, placeholders=Component.UNDEFINED, preview=Component.UNDEFINED, issuer=Component.UNDEFINED, acceptedCards=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'acceptedCards', 'cvc', 'expiry', 'focused', 'issuer', 'locale', 'name', 'number', 'placeholders', 'preview']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'acceptedCards', 'cvc', 'expiry', 'focused', 'issuer', 'locale', 'name', 'number', 'placeholders', 'preview']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashCreditCards, self).__init__(**args)
