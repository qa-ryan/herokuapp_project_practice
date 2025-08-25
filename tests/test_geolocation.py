def test_geolocation_allow(allow_page):
    allow_page.goto("https://the-internet.herokuapp.com/geolocation")
    allow_page.click("text=Where am I?")

    # Expect coordinates to show up
    allow_page.wait_for_selector("#lat-value", timeout=5000)
    latitude = allow_page.inner_text("#lat-value")
    longitude = allow_page.inner_text("#long-value")

    print(f"\n[ALLOW] Latitude: {latitude}, Longitude: {longitude}")

    assert latitude.strip() != ""
    assert longitude.strip() != ""


def test_geolocation_deny(deny_page):
    deny_page.goto("https://the-internet.herokuapp.com/geolocation")
    deny_page.click("text=Where am I?")

    # Expect no coordinates because permission denied
    deny_page.wait_for_timeout(3000)
    lat_exists = deny_page.locator("#lat-value").count()
    long_exists = deny_page.locator("#long-value").count()

    print("\n[DENY] Geolocation not available (permission blocked).")
    assert lat_exists == 0 and long_exists == 0
