# -*-coding:UTF-8-*-

import docx


def main():
    POS = './test-word.docx'
    file = docx.Document(POS)
    for para in file.paragraphs:
        if len(para.text) > 1:
            print(para.text)


if __name__ == '__main__':
    main()
