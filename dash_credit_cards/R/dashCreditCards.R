# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashCreditCards <- function(id=NULL, acceptedCards=NULL, cvc=NULL, expiry=NULL, focused=NULL, issuer=NULL, locale=NULL, name=NULL, number=NULL, placeholders=NULL, preview=NULL) {
    
    props <- list(id=id, acceptedCards=acceptedCards, cvc=cvc, expiry=expiry, focused=focused, issuer=issuer, locale=locale, name=name, number=number, placeholders=placeholders, preview=preview)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashCreditCards',
        namespace = 'dash_credit_cards',
        propNames = c('id', 'acceptedCards', 'cvc', 'expiry', 'focused', 'issuer', 'locale', 'name', 'number', 'placeholders', 'preview'),
        package = 'dashCreditCards'
        )

    structure(component, class = c('dash_component', 'list'))
}
