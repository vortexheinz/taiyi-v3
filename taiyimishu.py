# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:15:56 2020
@author: hooki
"""

yang = ['● 第一局 甲子 丙子 戊子 庚子 壬子',
 '太乙在一宮，天目武德，主算七，主大將七宮，客目掩，主參將一宮囚，始擊將大武掩主大將，客算十三，和。客大將三宮發，客參將九宮格，計神寅。此局客算長和、門具、將發，利為客，見陣利先動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從北來，客勝，聞賊備西南，奇兵西南，伏兵利戌亥時。太乙雖助主，主大將為客目掩之，算短不和，不利為主，聞賊備西南。',
 '● 第二局 乙丑 丁卯 己丑 辛丑 癸丑',
 '太乙在一宮，天目大簇，主算六不和，主大將六宮內迫，主參將八宮外迫，始擊將陰主擊，客算一，不和，客大將一宮囚，主挾，客參將三宮，客利，計神丑。此客主大小將挾客大將，客大將囚，主客俱不利，客宜固守，主聞賊備正西，客聞賊備西北。',
 '● 第三局 丙寅 戊寅 庚寅 壬寅 甲寅',
 '太乙在一宮，天目陰主，辰迫主算單一，不和，主大將一宮囚，主參將三宮發，始擊將大義，辰迫，客算四十，不和，客大將四宮發，客參將三宮發，計神子。此局客算長、門具、將發，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備西北，奇兵西北，伏兵利戌亥時。主目辰迫，不和，算短，大將囚，不利為主，宜固守，聞賊備正東。',
 '● 第四局 丁卯 己卯 辛卯 癸卯 乙卯',
 '太乙在二宮，天目陰德，主算二十五，八門杜，主大將參將不出中宮，始擊將陽德。客算十七，不和，客大將七宮，內迫，客參將二宮發，計神亥。此局主人杜塞無門，客算不和，大將迫，主客俱不利，主聞賊備西北，客聞賊備東北。',
 '● 第五局 戊辰 庚辰 壬辰 甲辰 丙辰',
 '太乙在二宮，天目陰德，主算二十五，八門杜，主大將參將不出中宮，始擊將呂申。客算十四，不和，大將四宮發，客參將二宮囚，計神戌。此局太乙助客，客算不和，大將發，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備，東北奇兵，東北伏兵，利巳午未時，主人杜塞不利，宜固守，聞賊備西北、正東。',
 '● 第六局 己巳 辛巳 癸巳 乙巳 丁巳',
 '太乙在二宮，天目大義，主算二十五，八門杜，主大將參將不出中宮，始擊將大陽陰。客算十，孤陽，客大將一宮發，客參將三宮發，計神酉。此局太乙助客，客大小將發，利為客，見陣利先動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備東南，奇兵東南，伏兵利巳午未時，主人杜塞無門不利，宜固守，聞賊備西北，為客赤雲至，疾戰勝。',
 '● 第七局 庚午 壬午 甲午 丙午 戊午',
 '太乙在三宮，天目地主，主算八，不和，主大將八宮，內迫，主參將四宮，外迫，始擊將大神。客算二十五，八門杜，客大將參將不出中宮，計神申。此局主人大小將迫，客杜塞無門，主客俱不利，各宜固守，主聞賊備正北，客聞賊備東南。',
 '● 第八局 辛未 癸未 乙未 丁未 己未',
 '太乙在三宮，天目陽德，辰迫，主算單一，不和，主大將一宮發，主參將三宮囚，始擊將臨大武。客算二十二，長和，客大將二宮發，客參將六宮發，計神未。此局客算長和，門具將發，利為客，見陣利先動，出軍宜正南，戰利正北，用圓陣，舉黃旗，雲氣從正南來參，客勝，聞賊備西南，奇兵西南，伏兵利丑寅時。主目迫算短，參將囚，主人不利，宜固守，聞賊備西北。',
 '● 第九局 壬申 甲申 丙申 戊申 庚申',
 '太乙在三宮，天目和德，囚，主算三，不和，主大將三宮，囚，主參將九宮發，始擊將大簇。客算十五，八門杜，客大將參將不出中宮，計神午。此局主目、主大將囚，客杜塞無門，主客俱不利，宜固守，主聞賊備東北，客聞賊備正西。',
 '● 第十局 癸酉 乙酉 丁酉 己酉 辛酉',
 '太乙在四宮，天目呂申，辰迫，主算一，和，主大將一宮發，主參將三宮，內迫，始擊將陰德。客算十二，長和，客大將二宮發，客參將六宮格，計神巳。此局客算長和，大將發利，為客見陣利先動，出軍宜正南，戰利正北，用圓陣，舉黃旗，雲氣從南來，客勝，聞賊備西北，奇兵西北，伏兵利寅卯辰時。主目、參將迫太乙，雖助主，主人算短不和，利固守，聞賊備東北。',
 '● 第十一局 甲戌 丙戌 戊戌 庚戌 壬戌',
 '太乙在四宮，天目高叢，囚，主算四，不和，主大將四宮囚，主參將二宮發，始擊將陽德。客算四，不和，客大將四宮囚，客參將二宮發，計神辰。此局主客大將囚關，主客俱不利，各宜固守，主聞賊備正東，客聞賊備東北。',
 '● 第十二局 乙亥 丁亥 己亥 辛亥 癸亥',
 '太乙在四宮，天目太陽，辰迫，主算三十七，長和，主大將七宮發，主參將一宮發，始擊將呂申，辰擊。客算一，客大將一宮發將，參將三宮，內迫，計神卯。此局太乙助主，主人算長和，大小將門具將發，利為主，見陣利後動，出軍宜西南，戰利東北，用方陣，舉白旗，雲氣從西南來，主勝，聞賊備東南，奇兵東南，伏兵利寅卯辰時。客算短不和，客目辰擊。參將內迫，不利為客，宜固守，聞賊備東北。',
 '● 第十三局 丙子 戊子 庚子 壬子 六紀甲子',
 '太乙在六宮，天目大炅，主算十八，短和，主大將八宮發，主參將四宮格，始擊將太陽宮。客算十九，長和，客大將九宮發，客參將七宮發，計神寅。此局太乙助客，大小將利主，見陣利後動，出軍宜正北，戰利正南，戰利曲陣，舉黑旗，雲氣從北來，主勝，聞賊備東南，奇兵東南，伏兵利申酉戌時，客見陣利先行動，出軍宜東南，戰利西北，利銳陣，舉赤旗，雲氣從東南來，客勝，聞賊備東南，奇兵東南，伏兵利申酉戌時。',
 '● 第十四局 丁丑 己丑 辛丑 癸丑 乙丑',
 '太乙在六宮，天目大神，主算十，孤陽，主大將一宮，外迫，主參將三宮發。客算九，和，客大將九宮發，客參將七宮，內迫，計神丑。此局太乙助客，算長和，大將發，利為客，見陣利先動，出軍宜東南，戰利西北，利銳陣，舉赤旗，雲氣從東南來，客勝，聞賊備正南，奇兵正南，伏兵利申酉戌時，主大將迫，不利為主，宜固守，聞賊備東南。',
 '● 第十五局 戊寅 庚寅 壬寅 甲寅 丙寅',
 '太乙在六宮，天目大威，主算九，和，主大將九宮發，主參將七宮，內迫，始擊將大武，擊。客算七，不和，客大將七宮，內迫，客參將一宮，外迫，計神子。此局主人門具將發，利為主，見陣利後動，出軍宜東南，戰利西北，利銳陣，舉赤旗，雲氣從東南來，主勝，聞賊備正南，奇兵正南，伏兵利申酉戌時。客目擊太乙，主目挾客大將，客大小將迫，不利為客，宜固守，聞賊備正南。',
 '● 第十六局 己卯 辛卯 癸卯 乙卯 丁卯',
 '太乙在七宮，天目天道，辰迫，主算一，和，主大將二宮發，主參將三宮格，始擊將大簇。客算三十三，長和，客大將三宮格，客參將九宮發，計神亥。此局太乙助客，雖大將格，參將發，客算長和，利為客，見陣利先動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東北來，客勝，聞賊備正西，奇兵正西，伏兵利未申時。主目辰迫，算短，參將格，不利為主，宜固守，聞賊備西南、東北。',
 '● 第十七局 庚辰 壬辰 甲辰 丙辰 戊辰',
 '太乙在七宮，天目大武，囚，主算七，不和，主大將七宮囚，主參將一宮發，始擊將大義。客算三十七，不和，客大將七宮囚，客參將一宮發，計神戌。此局文昌將囚，主客大將相關，客主人關客，主客俱不利，各宜固守，主人聞賊備西南，客聞賊備正西。',
 '● 第十八局 辛巳 癸巳 乙巳 丁巳 己巳',
 '太乙在七宮，天目大武，囚，主算七，不和，主大將七宮囚，主參將一宮發，客挾，始擊將地主。客算二十六，不和，客大將六宮外迫，客參將八宮發，計神酉。此局主人大小將挾客大小將，又挾主人參將，主客俱不利，各宜固守，主人聞賊備正西，客聞賊備西南。',
 '● 第十九局 壬午 甲午 丙午 戊午 庚午',
 '太乙在八宮，天目武德，客挾，主算八，不和，主大將八宮囚，主參將四宮發，始擊將和德。客算三十二，長和，客大將二宮格，客參將六宮發，計神申。此局客大將雖格，算長和，大小將挾文昌，利客，見陣利先動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，客勝，聞賊備東北，奇兵東北，伏兵利亥子丑時，主人算短，主目為客挾之，太將囚太乙，雖助主，不利為主，宜固守，聞賊備西南。',
 '● 第二十局 癸未 乙未 丁未 己未 辛未',
 '太乙在八宮，天目大簇，主算七，不和，主大將七宮發，主參將一宮內迫，始擊將太陽。客算二十六，客大將六宮，主挾，客參將八宮囚，計神未。此局太乙助主，主大小將挾客，主算和，大將發，利為主，見陣利後動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南方來，主勝，聞賊備西南，奇兵正西，伏兵利亥子丑時。客大將為主人大小將挾之，不利為客，宜固守，聞賊備西南、北。',
 '● 第二十一局 甲申 丙申 戊申 庚申 壬申',
 '太乙在八宮，天目陰主，主算二，算短，主大將二宮格，主參將六宮發，始擊將大神。客算十七，長和，客大將七宮發，客參將一宮內迫，計神午。此局主人大小將挾客大將，客不利，主大將格，算短，主客勢均，各宜固守，主人聞賊備西北，客聞賊備正南。',
 '● 第二十二局 乙酉 丁酉 己酉 辛酉 癸酉',
 '太乙在九宮，天目陰德，主算十六，和，主大將六宮發，主參將八宮發，始擊將天道。客算三十，孤陽不和，客大將三宮發，客參將九宮囚，計神巳。此局主人大小將門具將發，利為主，見陣利後動，出軍主宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，主人勝，聞賊備西北，奇兵西北，伏兵利辰巳時。客算孤陽不和，參將囚，不利為客，宜固守，聞賊備西南。',
 '● 第二十三局 丙戌 戊戌 庚戌 壬戌 甲戌',
 '太乙在九宮，天目陰德，主算十六，和，主大將六宮發，主參將八宮發，始擊將武德。客算二十三，長和，客大將三宮發，客參將九宮囚，計神辰。此局主客具利，主人算和，門具將發，利為主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，主勝，聞賊備西北，奇兵西北，伏兵利辰巳時。客算長，太乙助，客參將雖囚，大將發，利客，見陣利先動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東北來，客勝，聞賊備西南，奇兵西南，伏兵利辰巳時。',
 '● 第二十四局 丁亥 己亥 辛亥 癸亥 乙亥',
 '太乙在九宮，天目大義，主算十六，短，大將六宮發，主參將八宮發，始擊將陰主。客算十七，長和，客大將七宮發，客參將一宮格，計神卯。此局客大小將挾主大將，太乙助，客算長和，利為客，見陣利先動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，客勝，聞賊備西北，奇兵西北，伏兵利辰巳時。主人算短，客大小將挾主大將，不利為主，宜固守，聞賊備西北。',
 '● 第二十五局 戊子 庚子 壬子 五紀甲子 丙子',
 '太乙在一宮，天目地主，主算三十九，主大將九宮格，客挾，主參將七宮發，始擊將大義，辰擊。客算四十，孤陰，客大將四宮發，參將三宮發，計神寅。此局客算長，大小將門具將發，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備西北，奇兵西北，伏兵利戌亥時。主大將格，太乙雖助，主大將為客大小將挾之，主人不利，宜固守，聞賊備東北。',
 '● 第二十六局 己丑 辛丑 癸丑 乙丑 丁丑',
 '太乙在一宮，天目陽德，主算三十二，主大將一宮發，主參將六宮內迫，始擊將和德。客算三十一，長，客大將六宮發，客參將三宮發，計神丑。此局太乙助主，主算長，大將發，利為主，見陣利後動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從正南來，主人勝，聞賊備東北，奇兵東北，伏兵利戌亥時。客大將囚，算短，不利為客，宜固守，聞賊備東北。',
 '● 第二十七局 庚寅 壬寅 甲寅 丙寅 戊寅',
 '太乙在一宮，天目和德，主算三十一，主大將一宮囚，主參將三宮與天目囚，始擊將高叢。客算二十八，和，客大將八宮，主挾，客參將四宮發，計神子。此局太乙雖助主，主人大將囚，參將又與天目囚，主大小將挾客大將，客大小將挾主參將，主客俱不利，各宜固守。主聞賊備東北，客聞賊備正東。',
 '● 第二十八局 辛卯 癸卯 乙卯 丁卯 己卯',
 '太乙在二宮，天目呂申，主算十四，長，主參將四宮發，主參將二宮囚，始擊將大炅。客算九，客大將九宮，內迫，主挾，客參將七宮，外迫，計神亥。此局太乙雖助客，主人大小將與太乙俱挾客大將，客大將挾太乙、主參將，主客俱不利，各宜固守，主聞賊備東北，客聞賊備東南。',
 '● 第二十九局 壬辰 甲辰 丙辰 戊辰 庚辰',
 '太乙在二宮，天目高叢，主算十三，主大將三宮發，主參將九宮，內迫，始擊將天道，擊。客算三十九，客大將九宮內迫，客參將七宮外迫，計神戌。此局主算和，大將發，利為主，見陣利後動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東北來，主勝，聞賊備正東，奇兵正東，伏兵利巳午未時。客目擊，大小將迫，太乙雖助，客擊，客不利，宜固守，聞賊備西南。',
 '● 第三十局 癸巳 乙巳 丁巳 己巳 辛巳',
 '太乙在二宮，天目太陽，主算十，孤陽，主大將一宮發，主參將三宮發，始擊將武德。客算三十二，客大將二宮囚，客參將六宮發，計神酉。此局主人門具將發，利為主，見陣利後動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，主勝，聞賊備東南，奇兵東南，伏兵利巳午未時。太乙雖助，客大將囚，客不利，宜固守，聞賊備西南。',
 '● 第三十一局 甲午 丙午 戊午 庚午 壬午',
 '太乙在三宮，天目大炅，主算三十三，主大將三宮囚，主參將九宮與主目囚，始擊將陰主。客算十，和，孤陽，客大將一宮發，客參將三宮囚，計神申。此局客算和，大將發，利為客，見陣利先動，出軍宜向西北，戰利東南，用曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備西北，奇兵西北，伏兵利丑寅時。太乙雖助主，主算不和，大將囚，參將與主目囚，主人不利，宜固守，聞賊備東南。',
 '● 第三十二局 乙未 丁未 己未 辛未 癸未',
 '太乙在三宮，天目大神，主算二十五，八門杜，主大將、參將不出中宮，始擊將地主，宮擊。客算八，短，客大將八宮，內迫，客參將四宮，外迫，計神未。此局主人杜塞，無門不利，客大小將迫，算短，主客俱不利，各宜固守，主聞賊備東南，客聞賊備正北。',
 '● 第三十三局 丙申 戊申 庚申 壬申 甲申',
 '太乙在三宮，天目大威，主算二十四，長，主大將四宮外迫，客挾，主參將二宮發，始擊將和德，掩、擊。客算三，大將三宮囚，參將九宮，主挾，計神午。此局太乙雖助主，主算不和，大將迫，大小將挾主人大將，主大小將挾客參將，主客俱不利，各宜固守，主聞賊備正南，客聞賊備東北。',
 '● 第三十四局 丁酉 己酉 辛酉 癸酉 乙酉',
 '太乙在四宮，天目天道，主算二十四，長和，主大將六宮格，主參將八宮發，始擊將高叢，掩。客算四，客大將四宮囚，客參將二宮發，計神巳。此局太乙助主，大將雖格，算長和，參將發，利主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從正西來，主勝，聞賊備西南，奇兵西南，伏兵利寅卯辰時，客大將囚，不利為客，宜固守，聞賊備正東。',
 '● 第三十五局 戊戌 庚戌 壬戌 甲戌 丙戌',
 '太乙在四宮，天目大武，主算二十五，八門杜，主大將、參將不出中宮，始擊將大神。客算二十八，長，客大將八宮發，客參將四宮囚，計神辰。此局客算長，大將發，利為客，見陣利先動，出軍宜正北，戰利正南，用曲陣，舉黑旗，雲氣從正北來，客勝，聞賊備東南，奇兵東南，伏兵利寅卯辰時。主人杜塞，無門不利，宜固守，聞賊備西南。',
 '● 第三十六局 己亥 辛亥 癸亥 乙亥 丁亥',
 '太乙在四宮，天目大武，主算二十五，八門杜，主大將、參將不出中宮，始擊將大威。客算二十七，長和，客大將七宮發，客參將一宮發，計神卯。此局客算長和，大小將發，利為客，見陣利先動，出軍宜西南，戰利東北，用方陣，舉白旗，雲氣從西南來，客勝，聞賊備正南，奇兵正南，伏兵利寅卯辰時。主人杜塞，無門不利，宜固守，聞賊備西南。',
 '● 第三十七局 庚子 壬子 四紀甲子 丙子 戊子',
 '太乙在六宮，客挾，天目武德神，辰迫，主算一，主大將一宮，外迫，主參將三宮發，始擊將大武，擊。客算七，客大將七宮，內迫，客參將一宮，外迫，計神寅。此局主大將迫，與客參將并，主客俱不利，各宜固守，主聞賊備西南，客聞賊備西南。',
 '● 第三十八局 辛丑 癸丑 乙丑 丁丑 己丑',
 '太乙在六宮，天目大簇，囚，主算六，主大將六宮，囚，主參將八宮發，始擊將陰主，客算三十五，八門杜，客大將、參將不出中宮，計神丑。此局主目、主大將囚，客杜塞無門，主客俱不利，各宜固守，主聞賊備正西，客聞賊備西北。',
 '● 第三十九局 壬寅 甲寅 丙寅 戊寅 庚寅',
 '太乙在六宮，天目陰主，辰迫，主算三十五，八門杜，主大將、參將不出中宮，始擊將大義。客算三十四，長和，客大將四宮格，客參將二宮發，計神子。此局客大將雖格，客算和，太乙助客，利為客，見陣利先動，出軍宜向正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備西北，伏兵利申酉戌時。主人杜塞無門，不利為主，宜固守，聞賊備西北。',
 '● 第四十局 癸卯 乙卯 丁卯 己卯 辛卯',
 '太乙在七宮，天目陰德，主算二十七，不和，主大將七宮囚，主參將一宮發，始擊將臨陰德。客算十九，長和，客大將九宮發，客參將七宮囚，計神亥。此局太乙助客，算長和，大將發，利為客，見陣利先動，出軍宜東南，戰利西北，利銳陣，舉赤旗，雲氣從東南來，客勝，聞賊備東北，奇兵利未申時。主人算不和，大將囚，不利為主，聞賊備西北。',
 '● 第四十一局 甲辰 丙辰 戊辰 庚辰 壬辰',
 '太乙在七宮，天目陰德，客挾，主算二十七，不和，主大將七宮囚，主參將一宮，客挾，始擊將呂申。客算十六，不和，天目六宮迫，主挾，客參將八宮發，計神戌。此局主大將迫，主人大小將挾客大將，客大小將又挾主目及參將，主客俱不利，各宜固守，主聞賊備西北，客聞賊備東北。',
 '● 第四十二局 乙巳 丁巳 己巳 辛巳 癸巳',
 '太乙在七宮，客挾，天目大義，主算二十七，主人大將在七宮囚，客挾，主參將一宮發，始擊將太陽。客算十二，客大將二宮內迫，客參將六宮外迫，主挾，計神酉。此局客大將挾太乙，主大將囚，客大小將挾主大將，客大小將迫，主客俱不利，各宜固守。主聞賊備西北，客聞賊備東南。',
 '● 第四十三局 丙午 戊午 庚午 壬午 甲午',
 '太乙在八宮，天目地主，囚，主算八，不和，主大將八宮囚，主參將四宮發，始擊將大神。客算十七，長和，客大將七宮發，客參將一宮內迫，計神申。此局客算長和，客大將發，利為客，見陣利先動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，客勝，聞賊備東南，奇兵東南，伏兵利亥子丑時。主人算短，主目、大將囚，不利為主，宜固守，聞賊備正北。',
 '● 第四十四局 丁未 己未 辛未 癸未 乙未',
 '太乙在八宮，天目陽德。主算三十三，長，主大將三宮，外迫，主參將九宮，客挾，始擊將大武。客算十四，客大將四宮發，主挾，客參將二宮格，計神未。此局主目、大將迫，參將為客挾，不利為主，客大將為主大小將挾之，參將格，不利為客，主客俱不利，各宜固守。主聞賊備東北，客聞賊備西南。',
 '● 第四十五局 戊申 庚申 壬申 甲申 丙申',
 '太乙在八宮，天目和德，宮迫，主算三十二，長和，主大將一宮格，主參將六宮發，始擊將臨大簇。客算七，短，客大將七宮，主挾，客參將一宮，內迫，計神午。此局主大將雖格，參將發，主算長和，利為主，太乙助主，見陣利後動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從正南來，主人勝，聞賊備東北，奇兵東北，伏兵利亥子丑時。客大將為主大小將挾之，參將內迫，算短，不利為客，宜固守，聞賊備正西。',
 '● 第四十六局 己酉 辛酉 癸酉 乙酉 丁酉',
 '太乙在九宮，天目呂申，主算五，八門杜，主大將、參將不出中宮，始擊將陰德，客算十六，長和，客大將六宮發，客參將八宮發，計神巳。此局客算長和，大小將門具將發，利為客，見陣利先動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備西北，奇兵西北，伏兵利辰巳時。主人杜塞，無門不利，宜固守，聞賊備東北。',
 '● 第四十七局 庚戌 壬戌 甲戌 丙戌 戊戌',
 '太乙在九宮，主挾，天目高叢，宮迫，主算四，不和，主大將四宮內迫，主參將二宮外迫，始擊將陽德。客算八，不和，算長，客大將八宮發，客參將四宮內迫，計神辰。此局客算長，大將發，太乙助客，利為客，見陣利先動，出軍宜正北，戰利正南，利曲陣，舉黑旗，雲氣從北來，客勝，聞賊備東北，奇兵東北，伏兵利辰巳時，主人大小將迫挾太乙，算短不和，不利為主，宜固守，聞賊備正東。',
 '● 第四十八局 辛亥 癸亥 乙亥 丁亥 己亥',
 '太乙在九宮，天目太陽，辰迫，主算一，主大將一宮格，主參將三宮發，始擊將呂申，客算五，八門杜，客大將、參將不出中宮，計神卯。此局主目迫，客大小將杜塞無門，主客俱不利，各宜固守，主聞賊備東南，客聞賊備東北。',
 '● 第四十九局 壬子 甲子 丙子 戊子 庚子',
 '太乙在一宮，天目大炅，主算二十四，長和，主大將四宮發，主參將二宮發，始擊將太陽，客算二十五，八門杜，客大將、參將不出中宮，計辰寅。此局太乙助主，算長和，大小將門具將發，利為主，見陣利後動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，主勝，聞賊備東南，奇兵東南，伏兵利戌亥時，客杜塞無門不利，宜固守，聞賊備東南。',
 '● 第五十局 癸丑 乙丑 丁丑 己丑 辛丑',
 '太乙在一宮，天目大神，主算三十六，長和，主大將六宮內迫，主參將八宮外迫，始擊將大威。客算十五，八門杜，客大將、參將不出中宮，計神丑。此局太乙雖助主大小將，迫，客杜塞無門，主客俱不利，各宜固守。主聞賊備東南，客聞賊備西南。',
 '● 第五十一局 甲寅 丙寅 戊寅 庚寅 壬寅',
 '太乙在一宮，天目大威，主算十五，八門杜，主大將、參將不出中宮，始擊將大武。客算十六，和，客大將三宮發，客參將九宮格，計神子。此局客算長和，大將發，利為客，見陣利先動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東北來，客勝，聞賊備西南，奇兵西南，伏兵利戌亥時。主人杜塞，無門不利，宜固守，聞賊備正南。',
 '● 第五十二局 乙卯 丁卯 己卯 辛卯 癸卯',
 '太乙在二宮，主挾，天目天道，辰迫主算三十九，主大將九宮，內迫，主參將七宮，外迫，始擊將大簇。客算三十一和，客大將一宮發，客參將三宮發，計神亥。此局太乙助客，算和，門具將發，利為客，見陣利先動，出軍宜北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備正西，奇兵正西，伏兵利巳午未時。主人大小將迫，不利主，宜固守，聞賊備西南。',
 '● 第五十三局 丙辰 戊辰 庚辰 壬辰 甲辰',
 '太乙在二宮，天目大武，宮迫主算三十八長，主大將八宮格，主參將四宮發，始擊將大義。客算二十五，八門杜，客大將、參將不出中宮，計神戌。此局主算長，大將雖格，參將發，利主，見陣利後動，出軍宜正北，戰利正南，利曲陣，舉黑旗，雲氣從北來，主勝，聞賊備西南，奇兵西南，伏兵利巳午未時。客杜塞，無門不利，宜固守，聞賊備西北。',
 '● 第五十四局 丁巳 己巳 辛巳 癸巳 乙巳',
 '太乙在二宮，天目大武，宮迫主算三十八，主大將八宮格，主參將四宮發，始擊將地主。客算二十四，和，客大將四宮發，客參將二宮囚，計神酉。此局太乙助客，大將發，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備正北，奇兵正北，伏兵利巳午未時。主人大將格，主目迫，不利為主，宜固守，聞賊備西南。',
 '● 第五十五局 戊午 庚午 壬午 甲午 丙午',
 '太乙在三宮，天目武德，主算十六，長和，主大將六宮發，主參將八宮，內迫，始擊將和德，掩擊。客算三，不和，客大將三宮囚，客參將九宮發，計神申。此局太乙助主，主算長和，大將發，利為主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，主勝，聞賊備西南，奇兵西南，伏兵西南，利寅卯辰時。客目掩擊，大將囚，不利為客，宜固守，聞賊備東北。',
 '● 第五十六局 己未 辛未 癸未 乙未 丁未',
 '太乙在三宮，天目大簇，主算十五，八門杜，主大將、參將不出中宮，始擊將太陽。客算三十四，長，客大將四宮，外迫，客參將二宮發，計神未。此局主人杜塞無門，客大將迫，主客俱不利，各宜固守，主聞賊備正東，客聞賊備東南。',
 '● 第五十七局 庚申 壬申 甲申 丙申 戊申',
 '太乙在三宮，天目陰主，主算十，孤陽和，主大將一宮發，主參將三宮，始擊將大神。客算二十五，八門杜，客大將、參將不出中宮，計神午。此局太乙助主，主算和，大將發，利為主，見陣利後動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，主勝，聞賊備西北，奇兵西北，伏兵利丑寅時。客杜塞，無門不利，宜固守，聞賊備東南。',
 '● 第五十八局 辛酉 癸酉 乙酉 丁酉 己酉',
 '太乙在四宮，天目陰德，主算十三，和，主大將二宮發，主參將六宮格，與客大將關，始擊將天道。客算二十六，客大將六宮格，與主參將關，參將八宮發，計神巳。此局太乙助主，主算和，大將發，利為主，見陣利後動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，主勝，聞賊備西北，奇兵西北，伏兵利寅卯辰時。客大將格，不利，宜固守，聞賊備西南。',
 '● 第五十九局 壬戌 甲戌 丙戌 戊戌 庚戌',
 '太乙在四宮，天目陰德，主算十二，短，主大將二宮，客挾，主參將六宮格，始擊將武德。客算十九，長，客大將九宮，外迫，客參將七宮，主挾，計神辰。此局太乙雖助主，主人大將為客大小將挾之，客大將迫，主大小將挾客參將，主客俱不利，各宜固守。主聞賊備西北，客聞賊備西南。',
 '● 第六十局 癸亥 乙亥 丁亥 己亥 辛亥',
 '太乙在四宮，客挾天目大義。主算十二，和，主大將二宮發，主參將六宮格始擊將陰主。客算十三，不和，客大將三宮內迫參將九宮外迫計神卯。此局太乙助主。主人算和，大將發利，為主見陣利，後動出軍宜正南戰，利正北，利員陣舉黃旗，雲氣從南來，主勝。賊備西北奇兵西北伏兵利寅卯辰時。客算不和，大小將迫不利，宜固守聞，賊備西北。',   
 '● 第六十一局 甲子 丙子 戊子 庚子 壬子',
 '太乙在六宮，天目地主，主算三十三，長和，主大將三宮髮，主參將九宮挾，始擊將大義。客算三十四，客大將四宮，主挾，客參將二宮發，計神寅。此局主算和，主參將雖為客挾之，主大小將挾客大將，利為主，見陣利後動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東北來，主勝，聞賊備正北，奇兵正北，伏兵利申酉戌時。客大將格，太乙雖助客，客不利，聞賊備西北。',
 '● 第六十二局 乙丑 丁卯 己丑 辛丑 癸丑',
 '太乙在六宮，天目陽德，主算二十六，主大將六宮囚，主參將八宮發，始擊將和德。客算二十五，八門杜，客大將、參將不出中宮，計神丑。此局主大將囚，客杜塞無門，主客俱不利，各宜固守。主聞賊備東北，客聞賊備正北。',
 '● 第六十三局 丙寅 戊寅 庚寅 壬寅 甲寅',
 '太乙在六宮，天目和德，主算二十五，八門杜，主大將、參將不出中宮，始擊將高叢。客算二十二，客大將二宮發，客參將六宮囚，計神子。此局太乙助客，客大將發，見陣利先動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，客勝，聞賊備正東，奇兵正東，伏兵利申酉戌時。主人杜塞無門，不利為主，宜固守，聞賊備東北。',
 '● 第六十四局 丁卯 己卯 辛卯 癸卯 乙卯',
 '太乙在七宮，天目呂申，主算十六，不和，主大將六宮外迫，主參將八宮發，始擊將大炅。客算十一，客大將一宮，主挾，客參將三宮格，計神亥。此局主人大小將挾客大將，主算不和，大將迫，主客俱不利，各宜固守。主聞賊備東北，客聞賊備東南。',
 '● 第六十五局 戊辰 庚辰 壬辰 甲辰 丙辰',
 '太乙在七宮，天目高叢，主算十五，八門杜，主大將、參將不出中宮，始擊將天道，辰擊。客算一，客大將一宮發，客參將三宮格，計神戌。此局雖客目擊，太乙助客，大將發，利客，見陣利先動，出軍宜西北，戰利東南，利方陣，舉白旗，雲氣從西北來，客勝，聞賊備西南，奇兵西南，伏兵利未申時。主人杜塞，無門不利，宜固守，聞賊備正東。',
 '● 第六十六局 己巳 辛巳 癸巳 乙巳 丁巳',
 '太乙在七宮，主挾，天目太陽，主算十二，主大將二宮，內迫，主參將六宮，外迫，始擊將武德，辰擊。客算三十四，長和，客大將四宮發，客參將二宮，內迫，計神酉。此局太乙助客，客算長，大將發，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備西南，奇兵西南，伏兵利未申時，主人大小將迫，不利，宜固守，聞賊備東南。',
 '● 第六十七局 庚午 壬午 甲午 丙午 戊午',
 '太乙在八宮，天目大炅，主算二十五，八門杜，主大將、參將不出中宮，始擊將陰主。客算二，和，客大將二宮格，客參將六宮發，計神申。此局太乙助客，算和，大將雖格，參將發，利為客，見陣利先動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，客勝，聞賊備西北，奇兵西北，利亥子時。主人杜塞，無門不利，宜固守，聞賊備東南。',
 '● 第六十八局 辛未 癸未 乙未 丁未 己未',
 '太乙在八宮，天目大神，主算十七，長和，主大將七宮發，主參將一宮，內迫，始擊將地主，掩。客算八，不和，客大將八宮囚，客參將四宮發，計神未。此局太乙助主，主人算長和，大將發，參將雖迫，利為主，見陣利後動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，主勝，聞賊備東南，奇兵東南，伏兵利亥子丑時。客目掩，算短不和，大將囚，不利，宜固守，聞賊備正北。',
 '● 第六十九局 壬申 甲申 丙申 戊申 庚申',
 '太乙在八宮，天目文昌，將臨大威，主算十六，和，主大將六宮發，主參將八宮囚，始擊將和德，宮擊。客算三十二，客大將二宮格，客參將六宮發，計神午。此局太乙助主，主大將發，利主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，主勝，聞賊備正南，奇兵正南，伏兵利亥子丑時。挾客目，大將格，不利為客，宜固守，聞賊備東北。',
 '● 第七十局 癸酉 乙酉 丁酉 己酉 辛酉',
 '太乙在九宮，天目天道，主算三十，長，主大將三宮發，主參將九宮囚，始擊將高叢，宮擊。客算四，不和，客大將四宮，內迫，主挾，客參將二宮，外迫，計神巳。此局主大將發，算長，大小將挾客目大將，利為主，見陣利後動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東北來，主勝，聞賊備西南，奇兵西南，伏兵利辰巳時。客目擊，大小將迫，主挾客大將，不利為客，宜固守，聞賊備正東。',
 '● 第七十一局 甲戌 丙戌 戊戌 庚戌 壬戌',
 '太乙在九宮，天目大武，主算二十九，主大將九宮囚，主參將七宮，客挾，始擊將大神，辰擊。客算三十二，客大將二宮，外迫太乙、天目，主挾，客參將六宮發，計神辰。此局太乙、天目、主人大小將挾客大，客大小將挾主參將，主人大將囚，客大將迫，主客俱不利，各宜固守。主聞賊備西南，客聞賊備東南。',
 '● 第七十二局 乙亥 丁亥 己亥 辛亥 癸亥',
 '太乙在九宮，天目大武，主算二十九，主大將九宮，主參將七宮，與主目囚，始擊將大威，宮擊。客算二十二，客大將一宮格，客參將三宮發，計神卯。此局太乙助客，客算長和，大將雖格，參將發，利客，見陣利先動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備正南，奇兵正南，伏兵利辰巳時，主目、主大小將囚，不利為主，宜固守，聞賊備西南']

ying = ['● 第一局 甲子 丙子 戊子 庚子 壬子',
 '太乙在九宮，天目文昌，將臨呂申，主算五，八門杜，主大將、參將不出中宮發，計神申。此局主人杜塞無門，客大將囚，主客俱不利，各宜固守，主聞賊備東北，客聞賊備西南。',
 '● 第二局 乙丑 丁卯 己丑 辛丑 癸丑',
 '太乙在九宮，天目高叢，主算四不和，主大將四宮內迫，主參將二宮外迫，始擊將臨陰主，客算十七，長和，客大將七宮發，客參將一宮格，計神未。此局太乙助主，客算長和，大將發，利為客，見陣利先動，出軍宜向西南，戰利東北，利方陣，舉白旗，雲氣從西南來，客勝，聞賊備西北，奇兵西北，伏兵利辰巳時。主人大小將迫，算短不和，不利為主，宜固守，聞賊備正東。',
 '● 第三局 丙寅 戊寅 庚寅 壬寅 甲寅',
 '太乙在九宮，天目太陽，辰迫主算一，主大將一宮格，主參將三宮發，始擊將大義。客算十六，長和，客大將八宮發，計神午。此局客算長和，大小將發，利為客，見陣利先動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備西北，奇兵西北，伏兵利辰巳時，主目辰迫，雖太乙助主，大將格，不利為主，宜固守，聞賊備東南。',
 '● 第四局 丁卯 己卯 辛卯 癸卯 乙卯',
 '太乙在八宮，天目太昊，主算二十五，八門杜，主大將、參將不出中宮，始擊將陽德，辰擊。客算三十三，客大將三宮外迫，客參將九宮發，計神巳。此局主人杜塞無門，客目擊，大將外迫，主客俱不利，各宜固守，主聞賊備東南，客聞賊備東北。',
 '● 第五局 戊辰 庚辰 壬辰 甲辰 丙辰',
 '太乙在八宮，天目太靈，主算二十五，八門杜，主大將、參將不出中宮，始擊將呂申。客算三十，孤陽不和，客大將三宮外迫，客參將九宮發，計神辰。此局主人杜塞，無門不利，客算孤陽不利，大將迫，主客俱不利，各宜固守，主聞賊備東南，客聞賊備東北。',
 '● 第六局 己巳 辛巳 癸巳 乙巳 丁巳',
 '太乙在八宮，天目太神，主算十七和，主大將七宮發，主參將一宮，客挾，始擊將太陽。客算二十六，長和，客大將六宮，主挾，客參將八宮囚，計神卯。此局太乙助主，算長和，大小將挾客大將，利為主，見陣利後動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，主勝，聞賊備東南，奇兵東南，伏兵利亥子丑時。客算雖長和，大將為主人大小將挾之，參將囚，不利為客，各宜固守，聞賊備東南。',
 '● 第七局 庚午 壬午 甲午 丙午 戊午',
 '太乙在七宮，主將文昌大威，主算二，不和，主大將二宮內迫，主參將六宮外迫，始擊將大神。客算三，長和，客大將三宮格，客參將九宮發，計神寅。此局太乙助客，客算長和，大將雖格，參將發，利客，見陣利先動，出軍宜東北，戰利西南，利直陣，舉青旗，雲氣從東來，客勝，聞賊備東南，奇兵東南，伏兵利未申時，主人算不和，太小將迫，挾太乙，不利為主，各宜固守，聞賊備正南。',
 '● 第八局 辛未 癸未 乙未 丁未 己未',
 '太乙在七宮，天目天道，辰迫，主算一，短，不利，主大將一宮與客參將關，主參將三宮格，客參將一宮與主大將關，計神丑。此局主人算短不利，主目辰迫，大將與客參將相關、相格，客目掩，算不和，大將囚，主客俱不利，各宜固守，主聞賊備西南，客聞賊備西南。',
 '● 第九局 壬申 甲申 丙申 戊申 庚申',
 '太乙在七宮，天目大武，囚，主算七，短不和，主大將七宮囚，主參將一宮發，始擊將太簇，宮擊。客算三十四，長和，客大將四宮發，客參將二宮內迫，計神子。此局太乙助客，算長和，大將發，參將雖迫，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備正西，奇兵正西，伏兵利未申時。主目大將囚，算短不和，參將發，不利為主，宜固守，聞賊備西南。',
 '● 第十局 癸酉 乙酉 丁酉 己酉 辛酉',
 '太乙在六宮，天目武德，辰迫主算一短，主大將一宮外迫，主參將三宮發，始擊將陰德，宮擊。客算二十四，長和，客大將四宮格，客參將二宮發，計神亥。此局太乙助客，客算長和，大將雖格，參將發，利客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，客勝，聞賊備西北，奇兵西北，伏兵利申酉戌時，主算短，主目大將迫，參將雖發，不利為主人，宜固守，聞賊備西南。',
 '● 第十一局 甲戌 丙戌 戊戌 庚戌 壬戌',
 '太乙在六宮，天目太簇，囚，主算六，主大將六宮，主參將八宮，與客參將關，始擊將陽德。客算二十六，不和，客大將六宮囚，客參將八宮，與主參將關，計神戌。此局主目囚，主客參將相關，主客俱不利，各宜固守，主聞賊備正西南，客聞賊備正東北。',
 '● 第十二局 乙亥 丁亥 己亥 辛亥 癸亥',
 '太乙在六宮，天目陰主，辰迫，主算二十五，八門杜，主大將、參將不出中宮，始擊將呂申。客算二十三，長和，客大將三宮發，客參將九宮發，計神酉。始局太乙助客，客算長和，大小將門具將發，利為客，見陣利先動，出軍一東北，戰利西南，利直陣，舉青旗，雲氣從東北來，客勝，聞賊備東北，奇兵東北，伏兵利申酉戌時。主人杜塞，無門不利，宜固守，聞賊備東北。',
 '● 第十三局 丙子 戊子 庚子 壬子 甲子',
 '太乙在四宮，天目陰德，主算十二短，主大將六宮發，主參將六宮，客挾，始擊將太陽，辰擊。客算三十七，長和，客大將七宮，主挾，客參將一宮發，計神申。始局主人算短，大將雖發，參將為客挾之，客目擊，參將雖發，大將為主挾之，主客俱不利，各宜固守。主聞賊備西南，客聞賊備東北。',
 '● 第十四局 丁丑 己丑 辛丑 癸丑 乙丑',
 '太乙在四宮，天目大義，主算十二，短和，主大將二宮發，參將六宮，客挾，始擊將大感。客算二十七，長和，大將七宮，主挾，客參將一宮發，計神未。此局主算短，主人大小將挾客大將，客大小將挾主參將，主客俱不利，各宜固守。主聞賊備西南，客聞賊備正南。',
 '● 第十五局 戊寅 庚寅 壬寅 甲寅 丙寅',
 '太乙在四宮，天目地主，主算十一，主大將一宮發，主參將三宮，內迫，始擊將大武。客算二十五，八門杜，客大將、參將不出中宮，計神午。此局主參將雖迫大將，利為主，見陣利後動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，主勝，聞賊備正北，奇兵正北，伏兵利寅卯辰時。客杜塞，無門不利，宜固守，聞賊備西南。',
 '● 第十六局 己卯 辛卯 癸卯 乙卯 丁卯',
 '太乙在三宮，天目陽德，辰迫，主算一，主大將一宮發，主參將三宮，始擊將大簇。客算十五，八門杜塞，大將、參將不出中宮，計神巳。此局主參將雖囚，太乙助主，大將發，利主，見陣利後動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，主勝，聞賊備東北，奇兵東北，伏兵利丑寅時。客杜塞，無門不利，宜固守，客聞賊備正西。',
 '● 第十七局 庚辰 壬辰 甲辰 丙辰 戊辰',
 '太乙在三宮，天目和德，囚，主算三，短，主大將三宮囚，主參將九宮，與客大將相關，始擊將大義。客算九，和，客大將九宮，與主參將關，客參將七宮格，計神辰。此局主參將與客大將關，主大將囚，主客將相主人關客，客算不和，主客俱不利，各宜固守。主聞賊備東北，客聞賊備西北。',
 '● 第十八局 辛巳 癸巳 乙巳 丁巳 己巳',
 '太乙在三宮，天目和德，囚主算三，主大將三宮，客挾，囚，主參將九宮發，始擊將地主，宮擊。客算八，不和，客大將八宮，內迫，客參將四宮，外迫，主挾，計神卯。此局主目大將囚，客挾之，客目迫，大將擊，參將主挾迫，主客俱不利，各宜固守。主聞賊備正北，客聞賊備東北。',
 '● 第十九局 壬午 甲午 丙午 戊午 庚午',
 '太乙在二宮，天目呂申，主算十四，短和，主大將四宮發，主參將二宮格，始擊將和德。客算十六，長不和，客大將六宮發，客參將八宮格，計神寅。此局主客俱利，太乙助客，客算長不和，大將發，利為客，見陣利先動，出軍宜正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備東北，奇兵利巳午未時。主算和，參將雖格，大將發，利為主，見陣利後動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，主勝，聞賊備東北，奇兵東北，伏兵利巳午未時。',
 '● 第二十局 癸未 乙未 丁未 己未 辛未',
 '太乙在二宮，天目高叢，關客，主算十三，長和，主大將三宮，與客參將關，主將九宮，內迫，始擊將太陽。客算十，孤陽，客大將一宮發，客參將三宮，與主大將關，計神丑。此局算長和，主大將與客參將相關，主人關客，客敗，主人勝，見陣利後動，出軍宜正北，戰利西南，利直陣，舉青旗，雲氣從東北來，主勝，聞賊備正東，奇兵正東，伏兵利巳午未時。客勝短，參將與主大將相關，主人關客，客不利，宜固守，聞賊備東南。',
 '● 第二十一局 甲申 丙申 戊申 庚申 壬申',
 '太乙在二宮，天目太陽，主算十，孤陽，主大將一宮，與客大將關，主參將三宮，與客參將關，始擊將大神。客算一，客大將一宮，與主大將關，客參將關，計神子。此局主客俱不利，各宜固守，主聞賊備東南，客聞賊備東北。',
 '● 第二十二局 乙酉 丁酉 己酉 辛酉 癸酉',
 '太乙在一宮，天目太炅，關客，主算二十四，長，主大將四宮，與客大將關，主參將二宮，與客參將關，始擊將天道。客算十四，客大將四宮，與主大將關，客參將二宮，與主參將關，計神亥。此局太乙助主，主人關客，客敗，主勝，利為主，見陣利後動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，主勝，聞賊備東南，奇兵東南，伏兵利戌亥時。客為主人關，不利，宜固守，聞賊備西南。',
 '● 第二十三局 丙戌 戊戌 庚戌 壬戌 甲戌',
 '太乙在一宮，天目太炅，主算二十，長，主大將四宮發，主參將二宮發，始擊將武德。客算七，短和，客大將七宮發，參將一宮囚，計神戌。始局太乙助主，算長，大小將門具將發，利為主，見陣利後動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東來，主勝，聞賊備東南，奇兵東南，伏兵利戌亥時。客算短，參將囚，不利為客，宜固守，聞賊備正南。',
 '● 第二十四局 丁亥 己亥 辛亥 癸亥 乙亥',
 '太乙在一宮，天目大神，主算十六，長和，大將六宮內迫，主參將三宮發，計神酉。此局太乙雖助，主算長和，大將迫，參將為客挾之，主人不利，客算短，大將迫，主挾之，參將雖發，不利，為客主俱不利，各宜固守，主聞賊備東南，客聞賊備西北。',
 '● 第二十五局 戊子 庚子 壬子 甲子 丙子',
 '太乙在九宮，天目大威，宮迫，主算三十一，長和，主大將一宮，客挾格，主參將三宮發，始擊將大義。客算十六，客大將六宮發，客參將八宮，主挾，計神申。此局太乙助客，大將發，大小將挾，主敗客勝，見陣利先動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備西北，奇兵西北，伏兵利辰巳時。主大將為客挾之，天目迫，大將格，不利為主，宜固守，聞賊備正南。',
 '● 第二十六局 己丑 辛丑 癸丑 乙丑 丁丑',
 '太乙在九宮，天目天道，主算三十，孤陽不和，主大將三宮，客目掩之，主參將九宮發，始擊將和德，掩主大將。客算七和，大將七宮發，客參將一宮格，計神未。此局太乙助客，客目掩主大將，客大將發，利為客，見陣利先動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，客勝，聞賊備東北，奇兵東北，伏兵利辰巳時。主算孤陽不和，主大將為客目掩之，不利為主，宜固守，聞賊備西南。',
 '● 第二十七局 庚寅 壬寅 甲寅 丙寅 戊寅',
 '太乙在九宮，天目大武，主算二十九，長不利和，主大將九宮囚，客挾，主參將七宮發，始擊將高叢掩大將。客算四，客大將四宮，客目掩擊，客參將二宮，主挾，計神午。此局太乙助客，客目大將掩，參將為主挾，客大小將挾主大將囚，主客俱不利，各宜固守，主聞賊備西南，客聞賊備正東。',
 '● 第二十八局 辛卯 癸卯 乙卯 丁卯 己卯',
 '太乙在八宮，天目武德，主算八，不和，主大將八宮囚，主參將四宮發，始擊將大炅。客算二十五，八門杜，客大將、參將不出中宮，計神巳。此局主大將囚，客杜塞無門，主客俱不利，各宜固守。',
 '● 第二十九局 壬辰 甲辰 丙辰 戊辰 庚辰',
 '太乙在八宮，天目太簇，主算七，和，主大將七宮發，主參將一宮內迫，始擊將天道。客算十五，八門杜，客大將、參將不出中宮，計神辰。此局太乙助客，主算和，參將雖迫，大將發，利為主，見陣利後動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，主勝，聞賊備正西，奇兵正西，伏兵利亥子丑時。客杜塞無門不利，宜固守，聞賊備西南。',
 '● 第三十局 癸巳 乙巳 丁巳 己巳 辛巳',
 '太乙在八宮，天目陰主，主算二，主大將二宮格，主參將六宮發，始擊將武德。客算八，客大將八宮囚，客參將四宮發，計神卯。此局太乙助主，大將雖格，參將發，利主，見陣利後動，出軍宜向正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，主勝，聞賊備西北，奇兵西北，伏兵利亥子丑時。客大將囚，參將雖發，不利，宜固守，聞賊備西南。',
 '● 第三十一局 甲午 丙午 戊午 庚午 壬午',
 '太乙在七宮，天目陰德，主算二十七，主大將七宮囚，主參將一宮，與主目囚，始擊將囚。客算二十八長和，客大將八宮發，客參將四宮發，計神寅。此局太乙助客，客算長和，大將將門具將發，利為客，見陣利先動，出軍宜正北，戰利正南，利曲陣，舉黑旗，雲氣從北來，客勝，聞賊備西北，奇兵西北，伏兵利未申時。主大將囚，參將與主目囚，不利為主，宜固守，聞賊備西北。',
 '● 第三十二局 乙未 丁未 己未 辛未 癸未',
 '太乙在七宮，天目大義，主算二十七，不和，主大將七宮囚，主參將一宮，客挾，始擊將地主。客算二十六不和，客大將六宮，外迫，主挾，客參將八宮，客目掩，計神丑。此局太乙助客，客大將迫，主挾之，客目掩不利，為主將囚，主參將挾之，主客俱不利，各宜固守，主聞賊備西北，客聞賊備正北。',
 '● 第三十三局 丙申 戊申 庚申 壬申 甲申',
 '太乙在七宮，天目地主，主算二十六，不和，主大將六宮外迫，主參將八宮，與客大將關，始擊將和德。客算三十八和，客大將八宮，與主參將關，客參將四宮發，計神子。此局太乙助客，客大將、主參將相關，主大將內迫，主客俱不利，各宜固守，主聞賊備正北，客聞賊備東北。',
 '● 第三十四局 丁酉 己酉 辛酉 癸酉 乙酉',
 '太乙在六宮，天目陽德，主算二十六，不和，主大將六宮囚，與客參將關，主參將八宮發，始擊將高叢。客算二十二和，客大將二宮發，客參將六宮，與主大將關，計神亥。此局太乙助客，客參將與主大將相關，客大將發，利為客，見陣利先動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，客勝，聞賊備正東，奇兵正東，伏兵利申酉戌時。主大將囚，客關，主人不利，為主宜固守，聞賊備東北。',
 '● 第三十五局 戊戌 庚戌 壬戌 甲戌 丙戌',
 '太乙在六宮，天目和德，主算二十五，八門杜，主大將、參將不出中宮，始擊將大神。客算十孤陽，客大將一宮外迫，客參將三宮發，計神戌。此局主算杜塞無門，客算孤陽，參將雖發，大將外迫，主客俱不利，各宜固守，主聞賊備東北，客聞賊備東南。',
 '● 第三十六局 己亥 辛亥 癸亥 乙亥 丁亥',
 '太乙在六宮，天目和德，主算二十五，八門杜，主大將、參將不出中宮，始擊將大威。客算九，客大將九宮發，客參將七宮內迫，計神酉。此局太乙助客，客大將發，利為客，見陣利先動，出軍宜東北，戰利西北，利銳陣，舉赤旗，雲氣從東南來，主勝，聞賊備正南，奇兵正南，伏兵利申酉戌時。主人杜塞，無門不利，宜固守，聞賊備東北。',
 '● 第三十七局 庚子 壬子 甲子 丙子 戊子',
 '太乙在四宮，天目呂申，辰迫主算一，主大將一宮發，主參將三宮內迫，始擊將大武。客算三十五，八門杜，客大將、參將不出中宮，計神申。此局太乙助主，主大將發，參將雖迫，利主，見陣利後動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備東北，奇兵東北，伏兵利寅卯辰時。客杜塞無門不利，宜固守，聞賊備西南。',
 '● 第三十八局 辛丑 癸丑 乙丑 丁丑 己丑',
 '太乙在四宮，天目高叢，囚主算四，主大將四宮，客挾，主參將二宮發，始擊將陰主。客算十三，客大將三宮內迫，客參將九宮發，主挾，計神未。此局太乙助主，主大將囚，為客挾主目，客大迫，參將為主挾，主客俱不利，各宜固守，主聞賊備正東北，客聞賊備西北。',
 '● 第三十九局 壬寅 甲寅 丙寅 戊寅 庚寅',
 '太乙在四宮，天目太陽，主算三十七，長和，主大將七宮，客挾，主參將一宮發，始擊將太義。客算十二短和，客大將一宮內迫，客參將六宮挾主大將，計神午。此局太乙雖助主，大將為客挾，客大將內迫，參將為主挾，主客俱不利，各宜固守，主聞賊備東北，客聞賊備西北。',
 '● 第四十局 癸卯 乙卯 丁卯 己卯 辛卯',
 '太乙在三宮，天目太炅，主算二十三，長不和，主大將三宮囚，主參將九宮發，始擊將陽德。客算一，客大將一宮發，客參將三宮囚，計神巳。此局太乙助主，主算不和，參將雖發，大將囚，客目辰擊，算短，參將囚，主客俱不利，各宜固守，主聞賊備東南，客聞賊備東北。',
 '● 第四十一局 甲辰 丙辰 戊辰 庚辰 壬辰',
 '太乙在三宮，天目太炅，主算三十三，主大將三宮，客挾，囚，主參將九宮，始擊將呂申。客算三十八，客大將八宮內迫，客參將四宮主挾，計神辰。此局主大將囚，客挾之，客大將迫，參將為主挾之，主客俱不利，各宜固守。主聞賊備東南，客聞賊備東北。',
 '● 第四十二局 乙巳 丁巳 己巳 辛巳 癸巳',
 '太乙在三宮，天目太神，主算二十五，八門杜，主大將五宮，參將不出中宮，始擊將太陽。客算三十四，客大將四宮外迫，客參將二宮發，計神卯。此局主算短，杜塞無門，客大將迫，主客俱不利，各宜固守，主聞賊備東南，客聞賊備東南北。',
 '● 第四十三局 丙午 戊午 庚午 壬午 甲午',
 '太乙在二宮，天目大威，囚，主算二，不和，主大將二宮囚，主參將六宮發，始擊將大神。客算一，客大將一宮發，客參將三宮發，計神寅。始局太乙助客，客大小將門具將發，利為客，見陣利先動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備東北，奇兵東北，伏兵利巳午未時。主目、主大將囚，不利為主，宜固守，聞賊備正南。',
 '● 第四十四局 丁未 己未 辛未 癸未 乙未',
 '太乙在二宮，天目天道，辰迫，主算三十九，主大將九宮，內迫，主參將七宮，外迫，始擊將大武。客算三十八，客大將八宮格，客參將四宮發，計神丑。此局太乙助客，客大將雖格，參將發，利客，見陣利先動，出軍宜正北，戰利正南，利曲陣，舉黑旗，雲氣從北來，客勝，聞賊備西南，奇兵西南，伏兵利午未時。矚目大小將迫，不利，宜固守，聞賊備西南。',
 '● 第四十五局 戊申 庚申 壬申 甲申 丙申',
 '太乙在二宮，天目大武，宮迫，主算三十八，主大將八宮格，客挾，主參將四宮發，始擊將大簇。客算三十一，客大將一宮發，客參將三宮，主挾，計神子。此局太乙助客，客大將發，大小將挾，主敗客勝，見陣利先動，出軍宜西北，戰利東南，利曲陣，舉黑旗，雲氣從西北來，客勝，聞賊備正西，奇兵正西，伏兵利巳午未時。主目迫，大將格，客挾之，不利為主，宜固守，聞賊備西南。',
 '● 第四十六局 己酉 辛酉 癸酉 乙酉 丁酉',
 '太乙在一宮，天目武德，主算七，主大將七宮發，主參將一宮囚，始擊將陰德。客算一，客大將一宮囚，客參將三宮發，計神亥。此局太乙助主，主大將發，利為主，見陣利後動，出軍宜西南，戰利東北，利方陣，舉白旗，雲氣從西南來，主勝，聞賊備西南，奇兵西南，伏兵利戌亥時。客參將雖發，大將囚，不利為客，宜固守，聞賊備西北。',
 '● 第四十七局 庚戌 壬戌 甲戌 丙戌 戊戌',
 '太乙在一宮，天目大簇，宮迫，主算六，主大將六宮，內迫，主參將八宮，外迫，始擊將陽德。客算三十二長，客大將二宮發，客參將六宮內迫，計神戌。始局客算長，大將發，利為客，見陣利先動，出軍宜正西南，戰利北，利圓陣，舉黃旗，雲氣從南來，客勝，聞賊備東北，奇兵東北，伏兵利戌亥時。主目大小將迫，太乙雖助，不利，宜固守，聞賊備正西。',
 '● 第四十八局 辛亥 癸亥 乙亥 丁亥 己亥',
 '太乙在一宮，天目陰德，辰迫，主算一，主大將一宮囚，主參將三宮發，始擊將呂申。客算十九長和，客大將九宮格，客參將七宮發，計神酉。此局太乙助客，客算長和，客大將雖格，參將發，利為客，見陣利先動，出軍宜東南，戰利西北，利銳陣，舉赤旗，雲氣從東南來，客勝，聞賊備東北，奇兵東北，伏兵利戌亥時。主大將囚，算短，不利為主，宜固守，聞賊備西北。',
 '● 第四十九局 壬子 甲子 丙子 戊子 庚子',
 '太乙在九宮，天目陰德，主算十六，長和，主大將六宮發，主參將八宮，客挾，始擊將太陽。客算一，客大將一宮，主挾，客參將三宮發，計神申。此局主算長和，大將發，參將雖為客挾，利主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備西北，奇兵西北，伏兵利辰巳時。客算短，客參將雖發，大將格，為主挾，不利為客，宜固守，聞賊備東南。',
 '● 第五十局 癸丑 乙丑 丁丑 己丑 辛丑',
 '太乙在九宮，天目大義，主算十六，長和，主大將六宮發，主參將八宮，挾客，始擊將大威。客算三十一，客大將一宮，主挾格，客參將三宮發，計神未。此局主算長和，大小將門具將發，挾客大將，客敗主勝，利為主，見陣利後動，出軍宜正西，戰利正東。利方陣，舉白旗，雲氣從西來，客勝，聞賊備正西北，奇兵正西，伏兵利辰巳時。客目擊，參將雖發，大將為主挾，不利為客，宜固守，聞賊備正南。',
 '● 第五十一局 甲寅 丙寅 戊寅 庚寅 壬寅',
 '太乙在九宮，天目地主，主算二十五，八門杜，主大將、參將不出中宮，始擊將大武。客算二十九，客大將九宮囚，客參將七宮發，計神午。此局主算杜塞無門，客大將囚，主客俱不利，各宜固守，主聞賊備正北，客聞賊備西南。',
 '● 第五十二局 乙卯 丁卯 己卯 辛卯 癸卯',
 '太乙在八宮，天目陽德，辰擊，主算三十三，長不和，主大將三宮，內迫，主參將九宮，與客大將關，始擊將大簇。客算九，客大將九宮，與主參將關，客參將七宮發，計神巳。此局主目辰迫，客相關，主客俱不利，各宜固守，大將與主參將相關，主聞賊備東南，客聞賊備正西南。',
 '● 第五十三局 丙辰 戊辰 庚辰 壬辰 甲辰',
 '太乙在八宮，天目和德，宮迫，主算三十二，長，主大將二宮格，主參將六宮發，始擊將大義，辰擊。客算一，客大將一宮內迫，客參將三宮發，計神辰。此局太乙助主，主算長，大將雖格，參將發，利主，見陣利後動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，主敗客勝，聞賊備東北，奇兵東北，伏兵利亥子丑時。客算短，大將迫，不利為客，宜固守，聞賊備西北。',
 '● 第五十四局 丁巳 己巳 辛巳 癸巳 乙巳',
 '太乙在八宮，天目和德，辰迫，主算三十二，長，主大將二宮格，主參將六宮發，始擊將地主，掩。客算八，客大將八宮囚，參將四宮發，計神卯。此局太乙助主，主算長，大將雖格，參將發，利主，見陣利後動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從南來，主勝，聞賊備東北，奇兵東北，伏兵利亥子丑時。客目掩，大將囚，不利為客，宜固守，聞賊備正北。',
 '● 第五十五局 戊午 庚午 壬午 甲午 丙午',
 '太乙在七宮，天目呂申，主算十六，主大將六宮，外迫，主參將八宮，與客大將關，始擊將和德。客算十八，客大將八宮，與主參將關，客參將四宮發，計神寅。此局主大將迫，參將與客大將關，主人關客，主客俱不利，各宜固守，主聞賊備東北，客聞賊備東南北。',
 '● 第五十六局 己未 辛未 癸未 乙未 丁未',
 '太乙在七宮，天目高叢，主算十五，八門杜，主大小將不出中宮，始擊將太陽。客算十二，客大將二宮內迫，參將六宮外迫，計神丑。此局主算短，大將內外杜塞無門，客大小將迫，主客俱不利，各宜固守，主聞賊備正北，客聞賊備東北。',
 '● 第五十七局 庚申 壬申 甲申 丙申 戊申',
 '太乙在七宮，天目太陽，主算十二，不和，主大將二宮內迫，主參將六宮外迫，始擊將太神。客算三和，客大將三宮格，客參將九宮發，計神子。此局客算和，太乙助客，大將雖格，參將發，利客，見陣利先動，出軍宜東南，戰利西南，利直陣，舉青旗，雲氣從東北來，客勝，聞賊備東南，奇兵東南，伏兵利未申時。主算不和，大小將迫，不利為主，宜固守，聞賊備東南。',
 '● 第五十八局 辛酉 癸酉 乙酉 丁酉 己酉',
 '太乙在六宮，天目太炅，主算十八，主大將八宮，與客大將關，主參將四宮，與客參將關，始擊將天道。客算八，客大將八宮，與主大將關，客參將四宮，與主參將為關，計神亥。此局主人關客，客敗主人勝，利為主，見陣利後動，出軍宜正北，戰利正南，利曲陣，舉黑旗，雲氣從北來，主勝，聞賊備東南，奇兵東南，伏兵利申酉戌時。客大將為主關，不利為客，宜固守，聞賊備西南。',
 '● 第五十九局 壬戌 甲戌 丙戌 戊戌 庚戌',
 '太乙在六宮，天目太炅，主算十八，主大將八宮，客挾，主參將四宮格，始擊將武德。客算一，客大將一宮，外迫，客參將三宮，主挾，計神戌。此局主客大小將相關，主人敗，客大將迫，參將主挾之，客亦不利，各宜固守，主聞賊備東南，客聞賊備西南。',
 '● 第六十局 癸亥 乙亥 丁亥 己亥 辛亥',
 '太乙在六宮，天目大神，主算十，主大將一宮外迫，主參將三宮發將，始擊，將陰主。客算二十五，入門杜，客大將、參將不出中宮，計神酉。此局主大將迫客杜塞無門，主客俱不利，各宜固守。主聞賊備東南，客聞賊備西北。',       
 '● 第六十一局 甲子 丙子 戊子 庚子 壬子',
 '太乙在四宮，天目大威，主算二十七，主大將七宮，客挾，主參將一宮發，始擊將大義。客算十二，客大將二宮，擊主目，客參將六宮，主挾，計神申。此局主大將為客挾之，主客俱不利，各宜固守，主聞賊備正南，客聞賊備西北。',
 '● 第六十二局 乙丑 丁卯 己丑 辛丑 癸丑',
 '太乙在四宮，天目天道，主算二十六，主大將六宮格，主參將八宮發，始擊將和德，宮擊。客算三十，客大將三宮，內迫，客參將九宮，外迫，計神未。此局太乙助主，大將雖格，參將發，利主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，主勝，聞賊備西南，奇兵西南，伏兵利寅卯辰時。客大小將迫，客目擊，不利為客，宜固守，聞賊備東北。',
 '● 第六十三局 丙寅 戊寅 庚寅 壬寅 甲寅',
 '太乙在四宮，天目大武，主算二十五，八門杜，主大將、參將不出中宮，始擊將臨高叢掩。客算四，客大將四宮擊，客參將二宮發，計神午。此局主算杜塞無門，客目掩，大將擊，主客俱不利，各宜固守，主聞賊備西南，客聞賊備正東。',
 '● 第六十四局 丁卯 己卯 辛卯 癸卯 乙卯',
 '太乙在三宮，天目武德，主算十六和，主大將六宮發，主參將八宮內迫，始擊將大炅。客算三，不和，客大將三宮囚，客參將九宮發，計神巳。此局太乙助主，大將發，算和，利為主，見陣利後動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，主勝，聞賊備西南，奇兵西南，伏兵利丑寅時。客算不和，大將囚，不利為客，宜固守，聞賊備東南北。',
 '● 第六十五局 戊辰 庚辰 壬辰 甲辰 丙辰',
 '太乙在三宮，天目大族，主算十五，八門杜，主大將、參將不出中宮，始擊將天道。客算二十三，不和，客大將三宮囚，客參將九宮發，計神辰。主聞賊備正西，客聞賊備西南。',
 '● 第六十六局 己巳 辛巳 癸巳 乙巳 丁巳',
 '太乙在三宮，天目陰主，主算十，孤陽，主大將一宮，客挾，主參將三宮囚，始擊將武德。客算十六，長和，客大將六宮發，客參將八宮，主挾，計神卯。此局客算長和，參將雖為主挾，大將發，利為客，見陣利先動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備西南，奇兵西南，伏兵利丑寅時。主大將為客大小將挾之，主參將囚，不利為主，宜固守，聞賊備西北。',
 '● 第六十七局 庚午 壬午 甲午 丙午 戊午',
 '太乙在二宮，天目陰德，客目掩，主算二十五，八門杜，主大將、參將不出中宮，始擊將陰德，掩主目。客算二十六，客大將六宮發，客參將八宮格，計神寅。此局太乙助客，客目掩主目，參將雖格，大將發，利為客，見陣利先動，出軍宜正西，戰利正東，利方陣，舉白旗，雲氣從西來，客勝，聞賊備西北，旗兵西北，伏兵利巳午未時。主算杜塞無門，主目為客目掩，不利為主，宜固守，聞賊備西北。',
 '● 第六十八局 辛未 癸未 乙未 丁未 己未',
 '太乙在二宮，天目大義，主算二十五，八門杜，主大將、參將不出中宮，始擊將地主。客算二十四，和，客大將四宮發，客參將二宮囚，計神丑。此局客算和，參將雖囚，大將發，利為客，見陣利先動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從東北來，客勝，聞賊備正東，奇兵正東，伏兵利巳午未時。主算杜塞無門，不利為主，宜固守，聞賊備西北。',
 '● 第六十九局 壬申 甲申 丙申 戊申 庚申',
 '太乙在二宮，天目地主，主算二十四，長和，主大將四宮發，主參將二宮囚，始擊將臨和德。客算十六，不和算短，客大將六宮發，客參將八宮格，計神子。此局主算長和，大將發，利為主，見陣利後動，出軍宜正東，戰利正西，利銳陣，舉赤旗，雲氣從正東來，主勝，聞賊備正北，奇兵正北，伏兵利巳午未時。客算短不和，參將格，不利為客，宜固守，聞賊備東北。',
 '● 第七十局 癸酉 乙酉 丁酉 己酉 辛酉',
 '太乙在一宮，天目陽德，主算十算長，主大將二宮發，主參將六宮外迫，始擊將臨高叢。客算二十八，算短，客大將八宮外迫，客參將四宮發，計神亥。此局主算長和，大將發，利為主，見陣利後動，出軍宜正南，戰利正北，利圓陣，舉黃旗，雲氣從正南來，主勝，聞賊備東北，奇兵東北，伏兵利戌亥時。客算短，大將外迫，不利為客，宜固守，聞賊備正東。',
 '● 第七十一局 甲戌 丙戌 戊戌 庚戌 壬戌',
 '太乙在一宮，天目和德，主算三十一，主大將一宮，客挾囚，主參將三宮發，始擊將臨大神。客算十六，客大將六宮外迫，客參將八宮主挾，計神戌。此局主大將客挾之，客大將外迫，參將主挾之，主客俱不利，各宜固守，主聞賊備東北，客聞賊備東南。',
 '● 第七十二局 乙亥 丁亥 己亥 辛亥 癸亥',
 '太乙在一宮，天目和德，主算三十一，主大將一宮囚，主參將三宮發，始擊將臨大義。客算二十五，八門杜，客大將、參將不出中宮，計神酉。此局主大將囚，客杜塞無門，主客俱不利，各宜固守，主聞賊備東北，客聞賊備正南。']


taiyi_yingyang = {
 **{"陽遁":dict(zip(list(range(1,73)), yang[1::2]))},
 **{"陰遁":dict(zip(list(range(1,73)), ying[1::2]))}
}
