# -*- coding: utf-8 -*-
def imprime():

    # paleta de 48 cores produzida de um arquivo XPM.
    colors = {
        " ": "09080E", ".": "0E0906", "+": "210D0D", "@": "1F191F",
        "#": "251914", "$": "362220", "j": "551A17", "&": "2A262B",
        "*": "2F2622", "=": "2C2538", "-": "422E21", ";": "48302F",
        ">": "393345", ",": "3E342E", "'": "3A353C", ")": "523D3D",
        "!": "863128", "~": "484141", "{": "4E4238", "]": "45434E",
        "^": "663C33", "/": "594938", "(": "5D4B4E", "_": "9E3D33",
        ":": "575351", "<": "5E5247", "[": "635F66", "}": "6A5F5A",
        "|": "60625A", "1": "775F53", "2": "756656", "3": "67725B",
        "4": "7B6E68", "5": "6F7369", "6": "717177", "7": "897B7C",
        "8": "8D7D6F", "9": "7D8085", "0": "80817B", "a": "828775",
        "b": "9E8C80", "c": "8C918C", "d": "978E8D", "e": "9FA09E",
        "f": "B09F99", "g": "AEA38B", "h": "ADB3B1", "i": "CACECE",
    }

    # tabela de atributos produzida de um arquiovo XPM.
    attributes = [
        ">>]>]]>>'>>']']]]]'=>='@@~~:'@&'@'=]]']]']~~'~~~~']]]'&&~~~'~'''''~[|5e9:a5|5===",
        ">>>>>''>>>>'''>>'''@=    'iiii@@&==]]~~~'''~,~,,~~'&&. '({(<)<:}}4}::95[]chc[>>>",
        "]]]]~']>')))''~]]]~'=    $-$-$~&&==>~~::~{{{{{))~;&   .::::<::}}|}[}[::]]]:[>>>>",
        "[[|[||:[|:}[::}((:(&=   @~..##,*.===~:(::|<|<}<:}:'@  .{{<<<}}}||||||:::~~~]>'=>",
        "69996469666990dcd70'@   &::{,;,  ===33333|}}[}|}' @..  @=&:<|<|:|}||||::::~:]~::",
        "[[::[[[[[~]:[[5|c|5'&&@:{||<--{  ===~5||{:::[66[ $.j!. .. }|}}[}}44}455||33055[[",
        "6[[[[[[[6[6699de00~$+j;::ci#$-/  @===aa0a0cc9c9: _!_! .. ~0444}55553a55574746}||",
        "66696666669990cc:6&;@~~hh05*$--e  ===cccceeee9e  +jjj ...eacacaaaaa3a3a3333333|[",
        "6966664966666470|:,$*&~$hc5|$$/e &>>>([::569|99.    . ...hieefeddeecdefhehedd999",
        "[[[[[[[[[79|[[[['  @'*&$#00c|##}[ ([4444}656|}.       .. eeddd7cdac07ddddddd9d99",
        "[[([[[[[[}[}{}:::~'& ..#-+&~~@-/,.,:|444422484    ..  .. d0cccddabd0070047676[6[",
        "~''~~::|{{***&*#*,*,,*,,<ihc5||../{{:|28};<<48..      .. 5ac0cedeec0000447494696",
        ".+@.*@#.+$*,#.. ... &**,<hcca50:.-/2<<,5g2aag}d,.  . ... b583a|80a5}|0hid77}0666",
        "+.@#.$$*;,,#.#..#...*...#hhc5e0<,.+<{,{,{<<<4{0b.   .... bgb4}|}}4}8{,,,<||<:,$*",
        ";,,#;$-,{,{;,,{;,**,*  .-hec0hc||,{#,*<*{}|:{<07...<{...b8bb828ec:}45<32ab4}{#$+",
        "*+#,,*{,{{{{,{;{{,,* #..5ehcchc55e8|<{<{,*...:22..*1<8..*b422<8|a4,**{)(},;{1<){",
        ".....##*##,*$$*,#.$$-+##heh0eie05e$##{*.*,-,,.4d  2122,.@884abb85{25{;.    . {<{",
        "  .... ..........#..#,#*chh0hie55d(*..,*,$*#4.*. .24088..8888242}})d0)27b}){)<))",
        "((}();~}~(}}74ffffffffbf0hi9iih99cd2{{#,$;$++,<@.*1b282. 4a2228}<}}*+)<{d}67}(7(",
        "4444[7dddd787dbfffbbdbdb..<f.-#..b8828b88bbb2<  -11{)11. ;;{)<$$$==@@$;))););)'~",
        "44}484411444188f888b88bf..b8<b{..2128bbb828f82</$^^;^^j+;^;^((]   ....+$;$()$()(",
        "44}}44444444248844bb72b1..84221.+22422421/<1<<1/21//^^^^^@] .. &$;$;;$$$);;);;((",
    ]

    # tabela de padrões produzida via AALib.
    pattern = [
        "zgzzzzaazzaazggg:gaC/oj:\":::2\"j3o2j:2azzgzggzgzzzaujajj2g::c:r2c:K@@jjzpjjj@p2jj",
        "22222222222uauaaaau::@@@{QzQz_\\\"\\jja:gzzzaazzzzzzau&\\g@1:::::::QQQQQjj2bQa2\\pz2:",
        "Q:zggazaaaaaaazzaaz\\:@@N(?M5p1njj\\jag::Q:::zgzgzza{@@a@Q$@$$$@@j@@j@@@QzQQ@@ga2a",
        "@@$@Q$QQQQQQQQQQQQQj:QNN12-N:\"c2:j{2QQ$$$Q$NNNQQ$Q};j22Q$Q@@@@@@@j$@QQ::::Qnz2j&",
        "jjj@jjjjjjjjjjj2jj$/:Z@N1Q._;j2@Q\\\"jQ@@Q@@@@@$@@P\"@2:jQ\"jG$$@$@@@@@@@@@NQQQQQ:::",
        "@@@@@Q@$QQQQ@@jj2j$u\\::QQj@@@EIzZ\\\\\"Qj@jA@@@jj@pj.q._zjj:qQ@@@@@@@@@jj@@@pj\\pj@Q",
        "@@@@@@j@Q\\Qjjj22jjbj\"2.@Q\\/j2gQjZ\"jjqj2j2222jj2}q:c:;j':;qjjjj@jjjjjjjjQ2jjjj@$@",
        "jjjj@j@jj2222222j$j1jgqQgx$;\"a:;g:2jd2222u2zzj2 z{j\\$:;:'2u2a222jjjj2jj2j@j@j@Q@",
        "jjjjjjjjjjj\\jjjj@:ru2ZM@z2@:\"jQ\\q:u2j@j@jj2jQa}a7-':;;;;1gggazzaaaaaazzzzz22jj2j",
        "@@$@@jj@jjj$@@@@f@-1c:j;@22j::uJ}\":QQj@j@jjQj$!:2jj::j::(zaaza2a2aa22aazaauu2a2j",
        "@@@@@@@$@$$@Q@QNQQuj#QN{J8_._\"jSdYM@jj2jj2@2j$z;:;.;;;::za2u2uu2222j22j2jjjjjjjj",
        "QQQQQN$@QA000\\\"C{2:__._j1Qga2$y@(Q::::\\p:Q@j@j:72;.;';;; j222a2z222j2j2jjjjjjjjj",
        "\"\"\"=\"C\"\"\"jj;\\--\":{o\"2\\2j3Za22jp\\@nQ@p:A22j\\jjQ_}g:..';.;{22j2j@2jj2jozzz2j2j2j@@",
        "Nqq.:.j_ajj>q\"Q:Q:7z.--\"ugz2jzrQ}:(Q::ajg@@@QQapj:;'';;;(222@$@@@QjpQR@@Cj$@:o&Y",
        "a\\jj\\jj2a2jj2j2j;__jpQj::gz2jz\\QL.jGnZ:0:Q@ppj2jj..._;;{jaa2cQj22Qj@@QQQjjpQz\"\":",
        ":\":2jjazZ:Qggzj\\2\\j:@@'qjgz2zg2@j\\\\:::::\\.\"=C$Qp2'qj$Lj7@2j2r@jQ2p:o\\2@j@@@CQQ::",
        "Q@#\"@::j\"jajjj2z\"Cj\\j::qagz2zgajjcp@j:75Caj\\J:jpQ:Qjj2,jq22\\j\\2j@QQQ2a\"--::-oQQ:",
        "zzZQj.:@:#$:Q@N#::@::2\"{zgz2ggzjjg_;@#r:jjj;;-Y+z1j2jjpj1jjjjj\\j$@C2p:Q__._..QQQ",
        "..._.J....._____\\_122jjgzZguQgQjjz\\pQ.\"jjjj1t..$jqQjjjj:1jpjjjjj@jQ0HKjC2j\\jjQ\\$",
        "jjjjj2au2222j2azzzau2uar-\"q2=5\">4j2auuajjj\\2@#+q_:$@@$;gQ2::j;\"o9090=u:e@AsAKEEQ",
        "jrjjjjjjjjj2C2222j22222pNquu.2}2{uj2j222j2j2jjQMA2:c2r::_a1zQ:y#zaj::7\"uS&::2:Qg",
        "Q@j@jjjQjjj2jj\\jj2222j2$2-jjj@lg{jQj@j@p@@j$QQQQQQ::QgzZ2jy=!.j_._\\\\j2j\\:2zg:K:Q",
    ]

    knight = ""

    for lin in range(0, len(pattern)):
        for col in range(0, len(pattern[lin])):
            atr = colors[attributes[lin][col]]
            (red, green, blue) = (int(atr[i:i+2], base=16)
                                  for i in range(0, 6, 2))
            knight += "\x1b[38;2;{};{};{}m{}\x1b[0m".format(
                red, green, blue, pattern[lin][col])
        knight += "\n"

    return knight
