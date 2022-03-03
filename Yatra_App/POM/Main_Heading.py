class Main_Heading:

    research = "//div[contains(@class, 'popular_destination')][1]/h2"
    researchText = "Recent Search"

    openTravel = "//div[@id = 'ytTavel-restrictions']/h2"
    openTravelText = "Countries Open for Travel"

    yatSpecial = "//div[@class = 'titleBox']/h2"
    yatSpecialText = "Yatra Specials"

    popDomestic = "//div/span[contains(text(),'Popular domestic')]"
    popDomesticText = "Popular Domestic Flight Routes"

    popInternational = "//div/span[contains(text(),'Popular International')]"
    popInternationalText = "Popular International Flight Routes"


    copyR = "//div[contains(@class, 'copyright')]/p"
    copyRText = "Copyright © 2022 Yatra Online Private Limited, India. All rights reserved"
    scrollBottom = "window.scrollTo(0, document.body.scrollHeight);"

    aPass = "Assertion pass"
    aFail = "Element not present assertion fail"
