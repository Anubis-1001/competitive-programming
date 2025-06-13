def wordBreak(s, wordDict, start, splits):
    if start >= len(s):
        return [config[1:] for config in splits]

    result=[]
    for w in wordDict:
        if len(w)+start < len(s)+1 and s[start:start+len(w)] == w:
            res=wordBreak(s, wordDict, start+len(w), [split+" "+w for split in splits])
            result+=res

    return result


print(wordBreak("catsanddog", ["cat","cats","and","sand","dog"], 0, [""]))
