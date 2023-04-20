*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    SSHLibrary
Library    SeleniumLibrary

*** Variables ***
${BROWSER}                Firefox
${email_page}             https://poczta.wp.pl/login/login.html
${selector_RODO}          //*[contains(text(), "AKCEPTUJ")]
${selector_login}         //*[@id="login"]
${email_login}            grzegorz123test
${selector_pass}          css:#password
${email_pass}             pasta!@#BANANA$%^ravioli
${selector_button_login}    css:button.sc-bczRLJ



*** Test Cases ***

1. Test log in wp e-mail website
    Enter to e-mail wp.pl website by fierfox browser
    Accept RODO
    Enter login and password to e-maill account
    Log in to e-mail
    Check if you are logged in
    Close your browser

*** Keywords ***

Enter to e-mail wp.pl website by fierfox browser
    Open Browser            ${email_page}        ${BROWSER}

Accept RODO
    Click Button            ${selector_RODO}      

Enter login and password to e-maill account
    Input Text              ${selector_login}    ${email_login}
    Input Text              ${selector_pass}    ${email_pass}
    Sleep                   2
Log into e-mail
    Click Button            ${selector_button_login}
    Sleep                   2
Check if you are logged in
    Page Should Contain    Odebrane

Close your browser
    Close All Browsers