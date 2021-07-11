"""
Derived from original JS function:
  s.encrypt = function (e) {
    if ('' == e || void 0 == e) return '';
    for (var t = 'e5dl12XYVggihggafXWf0f2YSf2Xngd1', a = [
    ], i = '', s = 0; s < e.length; s++) {
      var n = e.charAt(s),
      r = n.charCodeAt();
      a[2 * s] = 240 & t[s % t.length].charCodeAt() | 15 & r ^ 15 & t[s % t.length].charCodeAt(),
      a[2 * s + 1] = 240 & t[s % t.length].charCodeAt() | r >> 4 ^ 15 & t[s % t.length].charCodeAt()
    }
    for (var s = 0; s < a.length; s++) i += String.fromCharCode(a[s]);
    return i
"""
def encrypt(content):
    keyTable = "e5dl12XYVggihggafXWf0f2YSf2Xngd1"
    keyTableLength = len(keyTable)

    if(len(content) == 0):
        return ""

    result = ""
    
    for i in range(len(content)):
        inputCharacter = ord(content[i])
        outputByte = ord(keyTable[i % keyTableLength])
        firstChar = 240 & outputByte | 15 & inputCharacter ^ 15 & outputByte
        result += chr(firstChar)
        secondChar = 240 & outputByte | inputCharacter >> 4 ^ 15 & outputByte
        result += chr(secondChar)

    return result

