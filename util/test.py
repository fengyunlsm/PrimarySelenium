#code=utf-8
import re
inputStr = '//p[contains(text(), "KUHASHI 细萃系列 18K红色黄金项链")]//parent::div//following-sibling::div[@class="numPromotion"]//button[contains(text(), "-")]'
replacedStr = re.sub(r".*contains\(text\(\), (.*)\".*", "222", inputStr)
print (replacedStr)
