from jerome.wordbuilder import WordBuilder


def test_word_build():
    word = "something"
    count = 10
    word_chain = " ".join([word for i in range(count)])
    c = WordBuilder(text=word_chain)
    assert c[word] == count


def test_word_builder_ingest():
    c = WordBuilder()
    c.ingest("bob")
    c.ingest("bob")
    for w in c.top():
        assert w[0] == "bob"