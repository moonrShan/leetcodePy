class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        num = n
        count = 0
        while num > 0:
            num = num // 10
            count += 1
        result = []
        if count == 0:
            return 1
        if count == 1:
            return 22
        if count == 2:
            if 22 > n:
                result.append(22)
            else:
                result.append(122)
        if count == 3:
            if 122 > n:  result.append(122)
            if 212 > n:  result.append(212)
            if 221 > n:  result.append(221)
            if 333 > n:  result.append(333)
            result.append(1333)
        if count == 4:
            if 1333 > n:  result.append(1333)
            if 3133 > n:  result.append(3133)
            if 3313 > n:  result.append(3313)
            if 3331 > n:  result.append(3331)
            if 4444 > n:  result.append(4444)
            result.append(14444)

        if count == 5:
            if 14444 > n:  result.append(14444)
            if 22333 > n:  result.append(22333)
            if 23233 > n:  result.append(23233)
            if 23323 > n:  result.append(23323)
            if 23332 > n:  result.append(23332)
            if 32233 > n:  result.append(32233)
            if 32323 > n:  result.append(32323)
            if 32332 > n:  result.append(32332)
            if 33223 > n:  result.append(33223)
            if 33232 > n:  result.append(33232)
            if 33322 > n:  result.append(33322)
            if 41444 > n:  result.append(41444)
            if 44144 > n:  result.append(44144)
            if 44414 > n:  result.append(44414)
            if 44441 > n:  result.append(44441)
            if 55555 > n:  result.append(55555)
            result.append(122333)

        if count == 6:
            if 122333 > n:  result.append(122333)
            if 123233 > n:  result.append(123233)
            if 123323 > n:  result.append(123323)
            if 123332 > n:  result.append(123332)
            if 132233 > n:  result.append(132233)
            if 132323 > n:  result.append(132323)
            if 132332 > n:  result.append(132332)
            if 133223 > n:  result.append(133223)
            if 133232 > n:  result.append(133232)
            if 133322 > n:  result.append(133322)

            if 212333 > n:  result.append(212333)
            if 213233 > n:  result.append(213233)
            if 213323 > n:  result.append(213323)
            if 213332 > n:  result.append(213332)
            if 312233 > n:  result.append(312233)
            if 312323 > n:  result.append(312323)
            if 312332 > n:  result.append(312332)
            if 313223 > n:  result.append(313223)
            if 313232 > n:  result.append(313232)
            if 313322 > n:  result.append(313322)

            if 221333 > n:  result.append(221333)
            if 231233 > n:  result.append(231233)
            if 231323 > n:  result.append(231323)
            if 231332 > n:  result.append(231332)
            if 321233 > n:  result.append(321233)
            if 321323 > n:  result.append(321323)
            if 321332 > n:  result.append(321332)
            if 331223 > n:  result.append(331223)
            if 331232 > n:  result.append(331232)
            if 331322 > n:  result.append(331322)

            if 223133 > n:  result.append(223133)
            if 232133 > n:  result.append(232133)
            if 233123 > n:  result.append(233123)
            if 233132 > n:  result.append(233132)
            if 322133 > n:  result.append(322133)
            if 323123 > n:  result.append(323123)
            if 323132 > n:  result.append(323132)
            if 332123 > n:  result.append(332123)
            if 332132 > n:  result.append(332132)
            if 333122 > n:  result.append(333122)

            if 223313 > n:  result.append(223313)
            if 232313 > n:  result.append(232313)
            if 233213 > n:  result.append(233213)
            if 233312 > n:  result.append(233312)
            if 322313 > n:  result.append(322313)
            if 323213 > n:  result.append(323213)
            if 323312 > n:  result.append(323312)
            if 332213 > n:  result.append(332213)
            if 332312 > n:  result.append(332312)
            if 333212 > n:  result.append(333212)

            if 223331 > n:  result.append(223331)
            if 232331 > n:  result.append(232331)
            if 233231 > n:  result.append(233231)
            if 233321 > n:  result.append(233321)
            if 322331 > n:  result.append(322331)
            if 323231 > n:  result.append(323231)
            if 323321 > n:  result.append(323321)
            if 332231 > n:  result.append(332231)
            if 332321 > n:  result.append(332321)
            if 333221 > n:  result.append(333221)

            if 155555 > n:  result.append(155555)
            if 224444 > n:  result.append(224444)
            if 242444 > n:  result.append(242444)
            if 244244 > n:  result.append(244244)
            if 244424 > n:  result.append(244424)
            if 244442 > n:  result.append(244442)
            if 242444 > n:  result.append(242444)
            if 244244 > n:  result.append(244244)
            if 244424 > n:  result.append(244424)
            if 244442 > n:  result.append(244442)
            if 422444 > n:  result.append(422444)
            if 424244 > n:  result.append(424244)
            if 424424 > n:  result.append(424424)
            if 424442 > n:  result.append(424442)
            if 442244 > n:  result.append(442244)
            if 442424 > n:  result.append(442424)
            if 442442 > n:  result.append(442442)
            if 444224 > n:  result.append(444224)
            if 444242 > n:  result.append(444242)
            if 444422 > n:  result.append(444422)
            if 515555 > n:  result.append(515555)
            if 551555 > n:  result.append(551555)
            if 555155 > n:  result.append(555155)
            if 555515 > n:  result.append(555515)
            if 555551 > n:  result.append(555551)
            if 666666 > n:  result.append(666666)
        result.append(1224444)
        return min(result)


