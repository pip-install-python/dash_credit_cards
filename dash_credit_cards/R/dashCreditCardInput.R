# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashCreditCardInput <- function(children=NULL, id=NULL, acceptedCards=NULL, callback=NULL, cardCVCInputProps=NULL, cardCVCInputRenderer=NULL, cardExpiryInputProps=NULL, cardExpiryInputRenderer=NULL, cardImageClassName=NULL, cardImageStyle=NULL, cardNumber=NULL, cardNumberInputProps=NULL, cardNumberInputRenderer=NULL, className=NULL, containerClassName=NULL, containerStyle=NULL, customTextLabels=NULL, cvc=NULL, dangerTextClassName=NULL, dangerTextStyle=NULL, expiry=NULL, fieldClassName=NULL, fieldStyle=NULL, inputClassName=NULL, inputComponent=NULL, inputStyle=NULL, invalidClassName=NULL, invalidStyle=NULL, issuer=NULL, onError=NULL, placeholders=NULL, preview=NULL, style=NULL) {
    
    props <- list(children=children, id=id, acceptedCards=acceptedCards, callback=callback, cardCVCInputProps=cardCVCInputProps, cardCVCInputRenderer=cardCVCInputRenderer, cardExpiryInputProps=cardExpiryInputProps, cardExpiryInputRenderer=cardExpiryInputRenderer, cardImageClassName=cardImageClassName, cardImageStyle=cardImageStyle, cardNumber=cardNumber, cardNumberInputProps=cardNumberInputProps, cardNumberInputRenderer=cardNumberInputRenderer, className=className, containerClassName=containerClassName, containerStyle=containerStyle, customTextLabels=customTextLabels, cvc=cvc, dangerTextClassName=dangerTextClassName, dangerTextStyle=dangerTextStyle, expiry=expiry, fieldClassName=fieldClassName, fieldStyle=fieldStyle, inputClassName=inputClassName, inputComponent=inputComponent, inputStyle=inputStyle, invalidClassName=invalidClassName, invalidStyle=invalidStyle, issuer=issuer, onError=onError, placeholders=placeholders, preview=preview, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashCreditCardInput',
        namespace = 'dash_credit_cards',
        propNames = c('children', 'id', 'acceptedCards', 'callback', 'cardCVCInputProps', 'cardCVCInputRenderer', 'cardExpiryInputProps', 'cardExpiryInputRenderer', 'cardImageClassName', 'cardImageStyle', 'cardNumber', 'cardNumberInputProps', 'cardNumberInputRenderer', 'className', 'containerClassName', 'containerStyle', 'customTextLabels', 'cvc', 'dangerTextClassName', 'dangerTextStyle', 'expiry', 'fieldClassName', 'fieldStyle', 'inputClassName', 'inputComponent', 'inputStyle', 'invalidClassName', 'invalidStyle', 'issuer', 'onError', 'placeholders', 'preview', 'style'),
        package = 'dashCreditCards'
        )

    structure(component, class = c('dash_component', 'list'))
}
