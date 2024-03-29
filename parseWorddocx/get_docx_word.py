from docx import Document

document = Document("D:/project/parseTestplan/5940 CFD_Production Test Plan_C0464_20231011_test.docx")

#获取所有段落
all_paragraphs = document.paragraphs
#打印看看all_paragraphs是什么东西
print(all_paragraphs)
print(type(all_paragraphs)) #，打印后发现是列表

# for paragraph in all_paragraphs:
#     #打印每一个段落的文字
#     print(paragraph)
#     print(paragraph.text)
