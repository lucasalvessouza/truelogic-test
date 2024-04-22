from index import count_spellings

def test_pennymac_word_once():
  assert count_spellings('AABCEMNPNYYE', 'PENNYMAC') == 1

def test_pennymac_word_twice():
  assert count_spellings('AABCEMNPNYYENYNMACP', 'PENNYMAC') == 2

def test_pennymac_word_NEVER():
  assert count_spellings('AABCMNPNYYNYNMACP', 'PENNYMAC') == 0