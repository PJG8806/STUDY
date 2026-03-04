
class PageReplacementFIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []

    def access_page(self, page):
        if page not in self.pages:
            # 수용량 보다 페이지가 길어 버릴때
            if len(self.pages) >= self.capacity:
                self.pages.pop(0)
                # 제일 먼저 들어온 요소를 뺀다
            self.pages.append(page)

    def status(self):
        print("현재 페이지 상태 :", self.pages)

page__replacement = PageReplacementFIFO(capacity=3)

page__replacement.status()

page__replacement.access_page(3)
page__replacement.status()
page__replacement.access_page(2)
page__replacement.status()
page__replacement.access_page(1)
page__replacement.status()

page__replacement.access_page(4)
page__replacement.status()