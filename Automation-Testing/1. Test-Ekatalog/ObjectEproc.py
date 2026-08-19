from playwright.sync_api import Page, expect

class Peproc_v1 : 

    def __init__(self, page : Page) :
        self.page = page
        self.username = page.get_by_role("textbox",name="username")
        self.password = page.get_by_role("textbox",name="password")
        self.button_login = page.locator('button[data-title="Login"]')
        self.kode_otp = page.locator(".token-input")
        self.button_pilih = page.get_by_role("button",name="Pilih")
        self.nodin = page.locator("#reqNotaDinas")
        self.pr = page.locator("#reqNomorPPA")

    def open_url(self) :
        self.page.goto("https://secure-ho-d01.pelindo.co.id/login")
        expect(self.page).to_have_url("https://secure-ho-d01.pelindo.co.id/login")

    def fill_account(self,username,password) :
        self.username.fill(username)
        self.password.fill(password)
        expect(self.button_login).to_be_enabled()
        self.button_login.click()

    def fill_otp(self,otp) : 
        for a, kode in enumerate(otp):
            self.kode_otp.nth(a).fill(kode)

    def role_option(self,role) :
        expect(self.page).to_have_url("https://secure-ho-d01.pelindo.co.id/role")
        self.page.get_by_role("radio",name=role).check()

    def click_pilih(self) :
        self.button_pilih.click()
        expect(self.page).to_have_url("https://secure-ho-d01.pelindo.co.id/app/index/purchase_order_list")

    def permohonan_paket(self) :
        self.page.get_by_text("Permohonan Paket").click()
        self.page.get_by_role("button",name="Tambah").click()
        self.nodin.click()
        self.nodin.fill("Pekerjaan Testing 2026")
        self.pr.click()
        self.pr.fill("80000129")
        