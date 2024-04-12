![Optional Alt Text](assets/github/example_dash_cards.gif)

# Dash Credit Cards

This project provides credit card templates and forms for Dash applications. It includes components for credit card input, display, and a parallax tilt effect.

## Components

### DashCreditCardInput

This component provides an input form for credit card information. It includes fields for the card number, expiry date, and CVC.
based off: https://www.npmjs.com/package/react-credit-card-input

### DashCreditCards

This component displays a credit card with the provided details. It supports different card issuers and can be used in preview mode.
based off: https://github.com/amaroteam/react-credit-cards?tab=readme-ov-file
### DashParallaxTilt

This component provides a parallax tilt effect for its children. It can be used to add interactive tilt effects to your components.
based off: https://mkosir.github.io/react-parallax-tilt/?path=/story/react-parallax-tilt--event-params

## Installation

```pip install dash-credit-cards```

## Usage

Here is a basic example of how to use these components in a Dash application:
- also note it was built using dash_mantine_components which can be replaced with a little work and know how: 

```pip install dash-mantine-components```
```python
from dash import *
from dash_credit_cards import DashCreditCards, DashParallaxTilt, DashCreditCardInput
import dash_mantine_components as dmc
import json

app = Dash(__name__)

app.layout = html.Div([
    DashParallaxTilt(
        id='input',
        children=[
            DashCreditCards(
                id='credit_card',
                name='',
                number='',
                expiry='',
                cvc='',
                focused='',
                preview=True,
                issuer='visa',
                locale={"valid": "VALID THRU"},
            )
        ],
        tiltReverse=True,
        glareEnable=True,
        glareMaxOpacity=0.8,
        glareColor='#ffffff',
        glareBorderRadius='20px',
        glarePosition='bottom',
        glareReverse=True,
    ),
    dmc.Space(h=10),
    dmc.Grid([
        dmc.Col(lg=4, md=2, sm=1),
        dmc.Col(dmc.TextInput(
            id='first_name_form',
            # label="First Name",
            # style={"width": 200},
            placeholder="Your First Name",
        ), lg=2, md=4, sm=5),
        dmc.Col(dmc.TextInput(
            id='last_name_form',
            # label="Last Name",
            # style={"width": 200},
            placeholder="Your Last Name",
        ), lg=2, md=4, sm=5),
        dmc.Col(lg=4, md=2, sm=1)
    ]),
    dmc.Space(h=10),
    html.Center(
        DashCreditCardInput(
            id='credit_card_input',
            cardNumber='',
            cvc='',
            expiry='',
            cardNumberInputProps={'value': ''},
            cardExpiryInputProps={'value': ''},
            cardCVCInputProps={'value': ''},
            fieldClassName="input",
        )
    ),
    dmc.Space(h=10),
    dmc.Grid([
        dmc.Button("Clear", color="red", id="clear"),
        dmc.Space(w=10),
        dmc.Button("Submit", color="green", id="submit")
    ], justify="center"),
    dmc.Space(h=10),
    html.Center(
    dmc.JsonInput(
        id='json_output',
        label="Your json data",
        placeholder="This component will auto-size to fit the content.",
        validationError="Invalid json",
        formatOnBlur=True,
        autosize=True,
        minRows=4,
        style={"width": "20vw"}
    ))

], style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'height': '100vh'})


@callback(
    Output('credit_card', 'name', allow_duplicate=True),
    Output('credit_card', 'number', allow_duplicate=True),
    Output('credit_card', 'expiry', allow_duplicate=True),
    Output('credit_card', 'cvc', allow_duplicate=True),
    Output('credit_card', 'issuer', allow_duplicate=True),
    Output('credit_card', 'focused', allow_duplicate=True),
    Input('first_name_form', 'value'),
    Input('last_name_form', 'value'),
    Input('credit_card_input', 'cardNumber'),
    Input('credit_card_input', 'expiry'),
    Input('credit_card_input', 'cvc'),
    prevent_initial_call=True,
)
def update_credit_card(first_name, last_name, card_input, expiry, cvc):
    if not any([card_input, expiry, cvc, first_name, last_name]):
        return no_update
    # Remove spaces and slash from expiry
    expiry = expiry.replace(" ", "").replace("/", "")

    first_digit = card_input[0] if card_input else ''
    if first_digit == '2' or first_digit == '5':
        issuer = 'mastercard'
    elif first_digit == '4':
        issuer = 'visa'
    elif first_digit == '3':
        issuer = 'amex'
    elif first_digit == '6':
        issuer = 'discover'
    else:
        issuer = ''

    # print(expiry, cvc)
    ctx = callback_context
    triggered_component = ctx.triggered[0]["prop_id"].split(".")[0]

    input_focus = None
    if triggered_component == 'credit_card_input':
        input_field = ctx.triggered[0]["prop_id"].split(".")[1]
        if input_field == 'cvc':
            input_focus = "cvc"
        else:
            input_focus = "name"

    name = f"{first_name} {last_name}"
    return name, card_input, expiry, cvc, issuer, input_focus


@callback(
    Output('json_output', 'value'),
    Output('first_name_form', 'value'),
    Output('last_name_form', 'value'),
    Output('credit_card_input', 'cardNumber'),
    Output('credit_card_input', 'expiry'),
    Output('credit_card_input', 'cvc'),
    Output('credit_card', 'name'),
    Output('credit_card', 'number'),
    Output('credit_card', 'expiry'),
    Output('credit_card', 'cvc'),
    Output('credit_card', 'focused'),
    Output('credit_card', 'issuer'),
    Input('submit', 'n_clicks'),
    Input('clear', 'n_clicks'),
    State('first_name_form', 'value'),
    State('last_name_form', 'value'),
    State('credit_card_input', 'cardNumber'),
    State('credit_card_input', 'expiry'),
    State('credit_card_input', 'cvc'),
    prevent_initial_call=True,
)
def update_output(submit_n_clicks, clear_n_clicks, first_name, last_name, card_number, expiry, cvc):
    ctx = callback_context
    if not ctx.triggered:
        return no_update
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'submit':
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'card_number': card_number,
            'expiry': expiry,
            'cvc': cvc,
        }
        return (json.dumps(data, indent=2), no_update, no_update, no_update, no_update, no_update, no_update, no_update,
                no_update, no_update, no_update, no_update)
    elif button_id == 'clear':
        return '', '', '', '', '', '', '', '', '', '', '', ''


if __name__ == '__main__':
    app.run_server(debug=True, port='2123')
```

## Contributing
look in dash_credit_cards/README.md for more information on how to contribute to this project.

## License
This project is licensed under the MIT License.

[![Pip Install Python GitHub stats](https://github-readme-stats.vercel.app/api?username=pip-install-python&show_icons=true&theme=radical)](https://github.com/pip-install-python)