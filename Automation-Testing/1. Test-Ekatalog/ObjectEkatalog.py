from playwright.sync_api import Page, expect

class Ekatalog_v1 :

    def __init__(self, page : Page) :
        self.page = page
       
    def open_ekatalog(self) :
        expect(self.page.get_by_text("Tanggal")).to_be_visible()
        with self.page.expect_popup() as new_tab :
            self.page.locator('a[href="sso/ekatalog"]').click()

            self.ekatalog_tab = new_tab.value  
            # expect(ekatalog_tab).to_have_url("https://e-katalog-dev.ilcs.co.id/ekatalog/produk")
        
            expect(self.ekatalog_tab.get_by_text("Produk")).to_be_visible
            self.ekatalog_tab.get_by_text("Gearbox Hoist Heavy Duty Crane Pelabuhan 5 Ton").click()

    def cost_center(self) : 
        self.ekatalog_tab.get_by_placeholder("Pilih Cost Center...").click()
        self.ekatalog_tab.get_by_placeholder("Pilih Cost Center...").fill("Departemen Pengadaan (2030105511)")
        expect(self.ekatalog_tab.get_by_placeholder("Pilih Cost Center")).to_be_visible()
        # get_by_role("option",name= "Departemen Pengadaan (2030105511)").click()

    def gl_account(self) :
        self.ekatalog_tab.get_by_placeholder("Pilih GL Account...").click()
        self.ekatalog_tab.get_by_placeholder("Pilih GL Account...").fill("Beban SDPK Sharing Revenue Pelindo Grup (Afiliasi) (5061300000)")

    def plant(self) : 
        self.ekatalog_tab.locator("select").select_option("1")

    def quantity(self,jumlah) : 
        for _ in range(jumlah) :
            self.ekatalog_tab.locator('button:has(svg.lucide-plus)').click()

    def check_out(self) :
        self.ekatalog_tab.get_by_role("button",name="Check Budget").click()
        self.ekatalog_tab.get_by_role("button",name="Tutup").click()
        self.ekatalog_tab.get_by_role("button",name="Beli Sekarang").click()

    def preview_co(self) : 
        expect(self.ekatalog_tab).to_have_url("https://e-katalog-dev.ilcs.co.id/ekatalog/checkout-preview")
        


        