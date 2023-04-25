# Challenge_porfolio_Kinga
 ## Zadanie 1: Konfiguracja oprogramowania
### Podzadanie 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?
Podjełam się wyzwania ponieważ odkąd ukończyłam kurs na testera manualnego, cały czas myślę o automatyzacji. Dzięki udziałowi w tym challengu będę mogła zdobyć niezbędną wiedzę w tym zakresie, poznać nowe narzędzia oraz przyswoić język programowania Python. Jestem pewna, że to mi ułatwi wejście do świata automatyzacji testów. 

## Zadanie 2:Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania.
### listbox_xpath
//*[@id="__next"]/form/div/div[2]/div/div
//*[contains(@class, "MuiSelect-root MuiSelect")]
//*[text()="English"]
### GutterBottom_xpath
//*[@id="__next"]/form/div/div[1]/h5
//*[text()="Scouts Panel"]
//*[contains(@class, "MuiTypography-root MuiTypography")]
### sign_in_button_xpath
//*[@id="__next"]/form/div/div[2]/button/span[1]
//*[text()="Sign in"]
//*[contains(@class, "MuiButton-label")]
### Login_xpath
//*[@id="login"]
//*[text()="Login"]
//*[contains(@class, "MuiInputBase-input")]
### password_field_xpath
//*[@id="password"]
//*[text()="Password"]
//*[contains(@class, "MuiInputBase-input MuiInput-input")]
### remaind_password_hyperlink_xpath
//*[@id="__next"]/form/div/div[1]/a
//*[text()="Remind password"]
//child::div/a

## Zadanie 3: Pierwszy test automatyczny i asserty
### To zadanie pozwoliło mi :
- poznać dogłębnie framework, na którym będziemy pracować,
- klikać w elementy na stronie,
- wypełniać pola tekstem,
- wykorzystać assert title, 
- uruchomić test

## Zadanie 4: Refactor, debugger i przypadki testowe
### To zadanie pozwoliło mi :
- wykonać refactor naszego kodu,
- dowiedzieć się jak pracować z debuggerem,
- rozwinąć skrzydła wyobraźni- zaprojektujesz i napiszesz test case’y,
- zautomatyzować stronę internetową na podstawie swoich TC
Film z automatyzacji przypadków testowych: https://drive.google.com/drive/u/1/folders/1I_vh__vYzXIorcLUy-cDt65qDaxwi_eE