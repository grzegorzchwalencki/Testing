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
${email_login}            aaa
${selector_pass}          css:#password
${email_pass}             bbb
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
    Sleep                   1
Log into e-mail
    Click Button            ${selector_button_login}

Check if you are logged in


Close your browser
