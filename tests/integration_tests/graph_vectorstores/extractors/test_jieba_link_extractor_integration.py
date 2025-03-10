import pytest
from langchain_community.graph_vectorstores.links import Link

from langchain_jieba import JiebaLinkExtractor

CONTENT1 = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
CONTENT2 = "我来到北京清华大学"


@pytest.mark.requires("jieba")
def test_one_from_keywords() -> None:
    "extract_one method testing"
    extractor = JiebaLinkExtractor()
    results = extractor.extract_one(
        "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
    )
    assert results == {
        Link.bidir(kind="kw", tag="小明"),
        Link.bidir(kind="kw", tag="日本京都大学"),
        Link.bidir(kind="kw", tag="计算所"),
    }


@pytest.mark.requires("jieba")
def test_many_from_keywords() -> None:
    "extract_many method testing"
    extractor = JiebaLinkExtractor()
    results = list(extractor.extract_many([CONTENT1, CONTENT2]))
    assert results[0] == {
        Link.bidir(kind="kw", tag="小明"),
        Link.bidir(kind="kw", tag="日本京都大学"),
        Link.bidir(kind="kw", tag="计算所"),
    }
    assert results[1] == {
        Link.bidir(kind="kw", tag="清华大学"),
        Link.bidir(kind="kw", tag="来到"),
        Link.bidir(kind="kw", tag="北京"),
    }
