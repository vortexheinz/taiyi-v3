# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:56:55 2023

@author: kinyeah
"""

graph_gongs =  ['巳', '午', '未', '申', '酉', '戌', '亥', '子', '丑', '寅','卯', '辰']

twelve_gong_stars = {"命宮":{"五福":"五福居旺，有福壽，主貴顯。享五福之造化，若會凶及臨空亡陷地，乃九流僧道，清福孤高。會吉曜，主貴極人臣。五福包藏，財帛冠世，當四季之位，身多福壽。天元屬水，命居東，那更梟符卯宮守，言在卯宮無壽也。又云：福曜不喜孤臨。",
"君基":"君基臨命，乘旺位，得吉曜相扶，乃一品之貴，寬德多仁不狡詐，君基尊重，福祿資生，為人惜言語，尊重，在女則少春風。",
"臣基":"臣基有吉星，侍從有輔佐之才，處己純正，位極人臣，若見始擊，必貪財利，己多無厭之求，主專任按法為執。古之人為人本分謹言多猶豫。已上見主目虧，或血疾，至老心身不寧，依享他人之福。",
"民基":"民基逢吉星臨旺，主富祿，金玉滿堂，名聞朝野，主好德去災，享悠長之福。在辰吉福德宮有福星，六戊生人，主遠涉發福，大富。",
"文昌":"文昌與君福相會，館閣之貴，臨陷會凶，為吏書或僧道，主仁識義理。在時元化詞館星，如在福伐，在官祿，身居天干水，主艱於仕進。",
"計神":"計神主計較多端，百事成就。若在陷宮，貪財利己，沒仁義。若立旺會吉星，為館閣之貴，或監司武臣，主倉庫之職任。",
"小游":"小游立旺會吉，主科甲一品之貴，天資出眾，處己高邁，善於記識，在身命則誠偽莫搖。",
"主大":"主大立旺，必高貴有權；更逢君福，主公侯之貴。逢凶立陷，多為僧道。或身似蛇形，多貪財利己；秉性清奇，為人清秀。又云：立陷身空帶馬，主為軍兵。",
"客大":"客大立旺，會吉，主君王待之以禮，官高極品，化達諸邦，或掛冠樂道修真，為應運真仙。主性華麗，喜賓朋，近貴，利官高顯，會民主蓋世英雄。",
"主參":"主參主依人成事，假貴人之力而發福。會吉星主有權，只貪人財物，若會凶星，多下賤之流，好潔淨風流，在申利忌小游，及五凶同宮，皆下賤也。",
"客參":"客參逢吉星，主近貴發福，遇凶則漂流，旺則為商，好潔淨風流。",
"始擊":"若在旺鄉，戊癸人遇之，貴極，人臣居陷，亦為邊帥，主大惡，為人膽小怯眾，在時元主幼年，離父母，在身命日時，立陷，惡死非刑。",
"飛符":"飛符臨命，主聰明伶俐，慷慨成性，喜符法，爐火陷則孤貧困苦，如身居德時遇吉，主大貴，又云：主偃蹇。一云：因何富中破產？飛符之來，命元又云：離祖傷妻身至孤，命宮多應帶飛符。",
"四神":"四神主孤獨，疏六親，背父母，刑妻剋子。逢旺會吉，主得魚鹽酒水之利，或舟船橋閘之任。逢凶值陷，則飄蓬四方九流也。主為人清秀，女人秉性貞潔，合臣基，有賢節之名，主清貧。",
"天乙":"天乙主為人剛介平心，逢三基五福，更立旺鄉多邊帥。武職主為人性剛，富貴不淫，與人寡合，遇三刑六害主橫亡，號孤星。",
"地乙":"地乙逢旺會吉，主守土邊隅食祿：主為人性剛，富貴不淫，與人寡合，在午上主愁困，如歲中飛刃相逢，主顛狂身苦。",
"":"主虛花詐偽，困懶磨陀，欺誑浮泛，恍惚無心，守靜安樂。"},
"兄弟":{"五福":"五福在兄弟宮，反為不美。此宮名「極閑宮」，兄弟富貴，我必卑微，將我福祿分減也。此宮若逢關囚迫格，必因兄弟致禍喪家，身必占長。",
"君基":"君基立旺，主棠棣生華，外合內差蓋。兄弟貴，我定微弱，奪我福祿，分我財產。",
"臣基":"必有姊而無兄，或姊妹多，兄弟少。",
"民基":"主兄弟成家，合德合心，亦是外房富庶。",
"文昌":"文昌主文秀才美，兄弟聯芳，臨陷舞文刀筆。",
"計神":"主兄弟兩母無益。",
"小游":"主長上多修仁德，兄弟和睦，亦主晚年弟眾。",
"主大":"必居長，難言兄弟，立陷分房不義。",
"主參":"主參主原和睦。有隔脈。兩苗之手足。",
"客大":"客大主兩苗異母，不相和睦。多主嫉妒",
"客參":"客參主隔苗異穗，兩母重出。",
"始擊":"始擊主妨兄弟，各自離散，孤兄獨弟，不得力也。",
"飛符":"主兩苗隔脈，異居不義，或多刑剋，或二姓。",
"四神":"主離異不睦，或主兄弟沉淪。",
"天乙":"主兄弟壽不長，苗裔停脈，長兄刑剋。",
"地乙":"主過房隔脈，孤立成人，於長不利，或自占長。",
"":"主刑害奸惡，兄弟各居，酒友花朋，游蕩流走，剋薄不義。"},
"妻妾":{"五福":"五福主得妻力，內助成家，更得外家財產資助。",
"君基":"君基臨之，德隆位尊，有人君之象。若是閥閱之家，乃極貴之妻，方應此星，不然定剋首妻。如有四神同宮臨貴妻之本命，主妻性潔淨，好道奉佛，心慈樂善。",
"臣基":"臣基主能內治，必奪夫權，家業充實，在陷宮，主剋妻。",
"民基":"民基主善治家，有蓄積得外家財，民基男女不相妨。又云：少陰居旺妻財盛，只恐妻家名不稱。",
"文昌":"文昌若在號孤星，男則無傷女有刑，若在陷宮還不礙，恐臨丑未與申辰，文昌要與計神齊，若到妻宮妻早宜，主內治材美，婚詩禮之門，女命雖在陷宮，夫亦為文士。",
"計神":"計神主能內治，多才德，積蓄財物，亦防中道傷剋。",
"小游":"小游主妻性愛清潔，尊貴，立陷必妨剋。又云：小游女子多清潔，一生處世多狂惑。",
"主大":"主大必擅夫權，立旺主諧老，失陷逢凶苦重剋。",
"主參":"主參乘旺，必納寵扶正，掌家會吉星，因妻財致富，陷主剋妻兩三妻方不剋，又必須小配方美，亦主入贅。《經》云：主參參客兩三次，旺宮無剋亦無收。",
"客大":"客大主贅婿他門，不然重婚離散。",
"客參":"客參主入贅，或納寵妻妾二人，旺宮無剋。",
"始擊":"始擊主妨三四妻。又云：始擊守妻宮，飛符卻更會。不奴須是婢，繾綣起淫風。吉星不臨照，知是不善終。始擊飛符會四凶，不相和順又貧窮。三夫剋盡為重配，三室俱亡還是凶。又曰：始擊在妻宮，主好色。",
"飛符":"飛符主初婚刑剋，年長，方諧白首，亦主不相和睦。",
"四神":"四神主清潔德性，沉靜，必剋不宜會水星，亦主流蕩好淫，又主妨三五妻，或有妓尼之妻。又云四神臨之一生寡，若更逢凶三五妻。",
"天乙":"天乙主中道，刑妻，外家衰敗，但善能持家，可謂中饋得人，有貞烈之風，年長則不剋天乙金神與地乙，琴瑟不和長戚戚，不然殘疾亦相傷，妻若年高方配敵，又云：「樞從天地三合見，停了妻時再娶妻。",
"地乙":"地乙到妻宮，為人必有凶，不妨三兩個，不與己身同，地乙女良男有剋，說與人間會者，知主宜長配，不然有病刑傷。二三妻見吉則不剋，如不剋則不和。"},
"子孫":{"五福":"主子孫貴顯，晚景安樂。在日時有二子。",
"君基":"君基止一子，主極貴，若有三四個，則秀氣散，反不能貴，更會凶，得子艱。又云得兒雖早長須刑。",
"臣基":"主女多男少，女長男小，方宜失陷，逢凶則子難育。",
"民基":"民基主子孫富厚，勤儉成家，逢旺有三子。又云：如落陷宮中道危。又云：民基子愚。",
"文昌":"文昌主子孫博文榮貴顯達，逢旺有四子。又云文昌在女號孤星，巳亥之間立外房。",
"計神":"計神主才學出眾，二子多能，若立旺宮，必子息蕃衍。又云隔脈。",
"小游":"小游主大一子為貴，又云小游主大一子富貴，多者不秀，在巳午子宮中道相拋。",
"主大":"主大，主男女精神立旺，主得五子不旺，只一子一子必貴。",
"主參":"主客二參如合窠，兩苗三姓可諧和。不是重時難得力。多生二子是無訛。若非妻有前夫子。也是前妻兒子多。主參主二子良貴。有兩苗之兒、隔脈之子，或長大而幼小。或庶出偏生，然晚年亦多子。",
"客大":"客大主寄養過房，庶出宜先育螟蛉，方存佳兒，旺則撐門頂戶陷，必敗業破家。又云：主生逆子，不然身是過房子。《又》云：客大兩苗方保。",
"客參":"主客二參如合窠，兩苗三姓可諧和。不是重時難得力。多生二子是無訛。若非妻有前夫子。也是前妻兒子多。客參，主庶出遲生，兩苗隔脈。又云可得二子或過房。",
"始擊":"始擊主剋子，猶可召義；男主剋子息無數，又云：剋一二方保。",
"飛符":"飛符來併亦堪憂，言同五福、三基相併，初得子而後喪之也。又云：主男女早年。刑剋或一子，必女多富貴。又云主絕後。",
"四神":"四神申子一兒安，不在兒宮子也難，主早生難育，後得方保平安，仍是長子必剋，又云剋三方",
"天乙":"天乙，主長子不利，寄名釋道方保。",
"地乙":"地乙主多災，早生難育，地乙陷時子癃殘。又云四中保一。",
"":"主傷夭，庶出過房，殘疾瘋癲，不肖不仁，假名走閃，無依無靠。"},
"財帛":{"五福":"五福逢旺，有吉星輔佐。金玉滿堂，粟陳貫朽。",
"君基":"主食君祿，得貴人恩惠財帛，作富翁。",
"臣基":"主財物豐盛，多得陰人之利，或外家之財。",
"民基":"主資財豐盛，粟陳貫朽，稱大富翁。",
"文昌":"主因文字發財，書寫獲利，近貴成家，逢吉星則貴。",
"計神":"主財帛充實，善能計度生財利。",
"小游":"主財帛豐盛，只愁日用不足，此為隔年愁星也。立陷主成敗。",
"主大":"主大主財，發如湧泉，乃錦上添花也。",
"主參":"主參主外郡人扶持得財，因人成事，假力獲利。",
"客大":"客大主游商得外財，經營得厚利，或夥計生財。",
"客參":"客參主得外人財，因人成事，或因貿易而獲利。",
"始擊":"始擊必多，是財帛聚散無常。當慎盜賊，若居旺宮，又主驟然而發，亦主蓄積不久長，蓋火星有始無終也。",
"飛符":"主蓄財，聚散不常，會始擊，防賊盜之咎，旺又驟發。",
"四神":"主成敗聚散不常，立旺主財帛豐盈。",
"天乙":"主成敗無常，虛而不實，先散後聚，此星名為隔年愁。星經云：富足饒餘，只愁日用不足，立旺地亦多積蓄。",
"地乙":"主得田園之利，多成敗，先散後聚。",
"":"主家計蕭索，財帛失喪，賊盜劫掠，走閃拐 帶，非橫破敗，六畜傷損。"},
"田宅":{"五福":"祖業光榮，父母厚產，安享久逸。",
"君基":"更有吉星相輔，主良田萬頃，大廈高堂，最怕空亡。",
"臣基":"臣基必寬大，資產基業壯茂，宜朝北房宅。",
"民基":"最利民基，主財富田多，若會凶，主成敗，主大第高門之宅。又云安身若有客星來，不受祖宗立錐地。",
"文昌":"必因讀書起家，或因文物書畫立業。",
"計神":"主宅舍華麗，美觀資業興隆，如在陷宮多暗計，無成無敗福來稀。",
"小游":"立旺，主家業田茂；地盛值陷，先盛後蕭條。",
"主大":"主大主基業高聳，煥然日新，田宅得利，如湧泉之發。",
"主參":"主參主基業壯盛，或依附祖父豪貴事業。",
"客大":"客大主遷移更改，離祖成家；逢旺，產業興隆。有外人主家陷，則因人破產。",
"客參":"客參主離祖移家，依人享福。",
"始擊":"始擊主破祖業，而遭水火之厄，立旺地則無礙。",
"飛符":"飛符主祖業更遷，應遭火厄，或有徙產之咎。",
"四神":"四神主近水歪曲不平，更改門戶，離祖成家，享天廚之樂。",
"天乙":"主祖業消散，更立成家，生涯蕭索。若立旺宮，必近山林，得五金之利。",
"地乙":"地乙立旺，主事業悠久，祖孫相繼，陷則更遷。",
"":"主借貸，賃房店舍、旅邸，荒門草舍，籬斜壁倒，火燒水溺，爭奪廢棄。"},
"官祿":{"五福":"主官祿崇高，一生無驚懼，若居陷祿利難成，亦多困厄，名輕祿薄。",
"君基":"主功名早發，科甲聯登，亦要立旺吉星相輔，女人身元逢之，主金冠鳳珮，早光榮也。",
"臣基":"會吉星，必主大貴，逢陷多陰人，是非聒絮。",
"民基":"會吉星，主納粟求名，同凶星，則百無一成，喜辰巳申酉宮。",
"文昌":"主文章冠世，朝野聞名，臨陷因名敗身。",
"計神":"為圖計之職，與民興利除害，名高位顯，主早年聲名。",
"小游":"小游在旺，一路功名到白頭，喜生春夏秋冬蹭蹬。",
"主大":"主大主清顯，節大名高朝野聞名，擢簡第一，早年必發。",
"主參":"主參主得貴人提挈，成就功名，然要在旺鄉，陷則不能自立。",
"客大":"客大主遊宦發福，或歷邊隅之任，或封王外國，同民貴不可言。",
"客參":"客參旺主，依貴食祿，事業須傍貴而成，陷則夭亡，同游而乘旺，反居僚佐。",
"始擊":"文士休逞名，為災為禍信非輕，火局旺宮官節制，英雄韜略鎮邊城。主文士不宜，而武弁最喜，亦要立於旺鄉方吉。",
"飛符":"逢旺會吉，主功名驟發，立陷必因名破家，此星名剝官煞，人士大忌，文名難就，惟利武途。",
"四神":"四神逢吉星，功名悠久，逢凶不利，庶人凶夭。",
"天乙":"凶星忌在官，如逢旺位吉多般，更得奇星在五馬，佇看詔命下朝端。主武強文弱，傲上不和。",
"地乙":"主祿位悠長，但不得大顯，必文武雙全。",
"":"主狐假虎威，羊質虎皮，停罷宮觀，私通求幹，巧言歇滅，除減遠缺。"},
"奴僕":{"五福":"最不相宜主兄弟朋友奴僕有福，己身卻無福矣。若臨身日時旺鄉，又主奴僕忠良，甚得力也。",
"君基":"君基必因僕人致禍敗家，以尊星落賤宮故也。若得吉曜，又是白屋變成朱戶。",
"臣基":"多遭親友陷害，小人欺凌，因僕人致禍敗家",
"民基":"主親友扶持，得外郡人財。",
"文昌":"主親友輔佐，文章成就，奴僕得力，臨陷遭敗。",
"計神":"主扶助家長，百計出眾，在外相成。",
"小游":"立旺，主作事威猛有利。",
"主大":"主人陷宮招非破敗，主大主得親友扶助，奴婢自服，不敢外心，夥計得利生財，因外人成事權，氣高豪強。",
"主參":"主參臨旺主得力，立陷主愚蠢。",
"客大":"客大主得僕人之力，在外經營獲利。",
"客參":"主得僕人之力，親友扶持，交相助益。",
"始擊":"主因奴破財，僕馬有傷，親友交情不長，多是非。",
"飛符":"主因親友破財，或僕人生禍受害，僕馬有傷。",
"四神":"主招親友口舌是非，奴僕逃亡。",
"天乙":"主親友寡情，施恩多怨。平生不負人，反多累己。旺位得他人，扶持立陷宮，僕人多狼籍。",
"地乙":"主操心勞力，不和順而有損傷，立旺，得他人扶持。",
"":"主病亡衰敗，奸詐侵欺，出尖禍頭，為非作歹，走閃轉變。"},
"疾厄":{"五福":"主一生疾厄，最少即有疾，亦無大害，逢難有救，亦多安樂。",
"君基":"主一生安康，災除疾去，逢難即解。",
"臣基":"主陰盛陽衰，下元虛冷，胃中有火。",
"民基":"主五穀傷食不成大患，逢災有解。",
"文昌":"主有預防之備，災不近身，立陷，有心胃之疾。",
"計神":"主心性多思多慮生災，或因酒色厚味作疾。",
"小游":"慎目疾立陷，防木石所傷，肺肝之患。",
"主大":"主肺經受患大腸之疾，因氣作惱成病。",
"主參":"主參主有氣疾偏疝，下元虛冷，或因酒色成癆。",
"客大":"客大必因酒色成下元虛損之咎。",
"客參":"客參主肝家受傷，患眼目之疾，或因在外染病。",
"始擊":"始擊慎血光之厄，或心肺瘋疾癱瘓之咎，老來多病。",
"飛符":"主眼目有傷殘，或痰嗽癆瘵，手足有損。",
"四神":"主下元虛冷，逢火星逢陷，眼目不明，血疾之患，多主小人拮据，一生困滯，形影孤單，亦多脾胃及瘋疥之疾。",
"天乙":"主肝經之疾，眼目不明，血虛及瘋癱之咎。見臣基於午位，耳聾目閉，為殃尤甚。立於子位，主腳疾頭風，不可當也。飛符同宮，主大腸痔患，及癬疥湯火之厄。",
"地乙":"主有脾胃之患，風疾之咎。",
"":"主虛狂磨難，口眼喎斜，手足跛躄，麻瘢龜背，瘋瘂聾痴，癱癆蠱癩，六指脣缺。"},
"福德":{"五福":"主五福兼全，晚年榮貴。立陷宮空地，亦主平安有福。",
"君基":"主平生康泰，子孫貴顯，老景榮華而無驚擾。",
"臣基":"主子貴孫賢，晚景清幽，福壽高強。",
"民基":"主一生操持勞碌，至老不得安閒。若會吉星，必享富貴之福，而晚景榮華。",
"文昌":"主文章富貴，享福悠久，上人見喜，子孝孫賢。",
"計神":"主心中常不足，性多貪逸。",
"小游":"享福清幽，名擅史籍，德冠鄉閭。",
"主大":"主大主享用無窮，晚景剛正發福而氣雄威。",
"主參":"主參主福壽，依貴人之蔭庇，立陷則福薄，主飄泊東西。",
"客大":"客大主享福，因人身心操持，亦因更改獲福，喜怒不常，又得義子之力而享福。",
"客參":"主相隨，游宦發福，或在外獲利。",
"始擊":"主男不孝，一生操持，到老不閒，立旺宮，稍高強。",
"飛符":"主出身微弱，勞力勞心，終身操持，災福並行。",
"四神":"主孤獨無靠，至老不得安閒，非僧道即九流。",
"天乙":"主孤高耿介，寡合清淨不染，是非能果斷，若居辰戌位，將來離祖，自立規模。",
"地乙":"立旺，主祖業相承不移。",
"":"主僧尼道家，醫術游謁，寒儒蕩士，隱居閒散逍遙，清虛淡泊，浮祿游藝岐路，倚貴托富。"},
"相貌":{"五福":"主容貌威儀，春風和氣，清奇雄偉",
"君基":"相貌魁偉，秉性尊嚴，服眾逢陷則面長而麻。",
"臣基":"主身體厚重，寬洪，大量而不俗，或面有麻。",
"民基":"主威儀重厚，立心勤儉。",
"文昌":"必清華文秀，高尚不俗。",
"計神":"主體相淳厚，喜愛潔淨新鮮，度量寬大。",
"小游":"",
"主大":"體正，剛烈魁偉，威儀服眾，容貌尊嚴，非俗格。",
"主參":"主清奇自重，斯文之象。",
"客大":"主威嚴清秀，作事口直心慈，常招小人嫉妬，色亦常變。",
"客參":"客參主骨格清奇，言辭利便，通人肺腑，啟人幽深。",
"始擊":"主相貌赤色，性急躁，立陷主五岳有刑傷。",
"飛符":"飛符主性急躁，塵俗愚蒙，立陷，身體手足有傷。",
"四神":"四神主清奇風流；臨陷會凶主頭面下元有傷。",
"天乙":"主清白，方面，骨格清奇。旺相主白色，立陷；帶黑色，頭面有傷而重濁見。",
"地乙":"地乙主純厚，簡言語，面帶黑黃，立陷則相貌有傷",
"":"主談虛說空。形容破陋。肌體尪羸。短舟小楫。孤行獨走。多憂多屈。偃蹇平生。"},
"父母":{"五福":"主雙親遐筭，三代一門，得父母厚產，立陷地，又是有名而無實，或得而自費。",
"君基":"主祖業興隆，得父母遺產，最忌空亡。",
"臣基":"主母德高賢，家道嚴肅。",
"民基":"主得父母財產厚業，逢空陷則不實。",
"文昌":"主三代文華、詩書根本，宗派聲名。",
"計神":"主得父母財，或外家財物。若陷剋母離祖。",
"小游":"主祖業悠久，父母厚蔭。在旺相，主祖孫相繼，立陷，家業漂流。入土位，父先傷。",
"主大":"主大立旺，主壽永福全，家業豐盛，值子年月三代，名家入。身命日時立旺，必主力大而武勇過人。",
"主參":"主參主重拜父母，或過房庶出。",
"客大":"主過房庶出，或兩姓成人。又云客大來，父母飛伐更相逢，生時必是離鄉井，四野紛紛兵火中。",
"客參":"主主重拜父母。",
"始擊":"主父母不利，若立旺父母不善終。",
"飛符":"主父母早年離別，或不得蔭庇。",
"四神":"主少失父母，或庶出過房，及有異母之別。",
"天乙":"主過房庶出，或先剋母。",
"地乙":"主父母賢德，教子有方，或重母，或庶出。一云先剋父。",
"":"主傷剋，不利六親；過房異姓，拋棄分離；詐冒邪偽，隱匿不明。"}}

#五福臨十二宮
wufu_twelve="子宮五福號天奇，遇之身命日時宜，只怕木神相聚合，一生作事不逢時。喜生春夏，秀氣所鍾，秋冬逢陷，窮困夭亡。,丑宮五福最清幽，此位從來拱斗牛，身命逢之多福壽，管教一世享優游。,寅宮五福曰天喪，衰陷難教福壽昌，若有伐星符會此，縱然富貴亦難長。主被山林惡物所傷。及膿血之疾。若同地乙。主安貧樂道。,卯宮五福號天休，福淺災深怨與愁。任是同宮臨吉曜，資財星散總難留。主祖業難居，身多流落，雖同吉星，財亦難聚。,辰宮五福號天昌，富貴榮華姓氏香，若得三基文宿合，青衫脫卻換黃裳。辛壬丙午生人，遇之必貴顯，主一生少疾病，亦多安樂。,巳宮五福主遠游，清閑嬾散亦風流，情和只是口頭惡，離祖方能遂所求。主離祖發福，丙辛生人則貴。,午宮福到號天明，身命逢之心志靈，只為火炎成土燥，得成名處卻無成。主遠離父母，或父母不全。,未宮五福號天權，吉曜加時富貴全，易姓更名定榮顯，他年侍御在金鑾。日生則貴，夜生平平，亦要更姓改名。,申宮五福實為強，若會文昌更顯揚。年少青燈苦勤讀，傳臚及第錦衣郎。主稟性正直，深謀遠慮，化為科名星，更得吉聚，主黃甲先登，康寧壽考。,酉宮五福號天榮，赫奕聲名眾所宗。君宿文星更同住，豹變龍驤上九重。會君基王侯之尊，文昌宰輔之貴，強星混雜，破格不貴，凶星尤忌。,戌宮五福名極旺，化成大吉號天忠，不惟名利俱昌大，抑且身安衣祿豐。必得祖宗蔭下富貴，名高利厚。,亥宮五福最為安，天門得地乃朝元。獨行定是英雄客，職任元戎鎮九邊。獨行為權謀星，乃英雄豪傑，文武全才。最忌飛始，混雜，則減福力矣。".split(",")
#君基十二宮
kingbase_twelve="子位君基號正崇，偏生別室喜相逢，若加參從同宮位，父正須教母異蹤。主科名榮貴，雖無吉星相扶，亦是衣祿自然，又同丑宮論。,丑位君基號殿元，如心稱意足田園，平生操履無虧欠，夫婦榮華子息全。同文昌則入相，腰金衣紫，清華重祿。無吉星，亦衣食豐餘，且有後福。,寅位君基號毛頭，家計徒誇富者儔，始積金珠終久敗，更兼名位亦難求。稟性剛烈，多主軍門橫死。有吉星，亦主兵權。,卯位君基號天虧，百計俱無亦何施，名利到頭成就晚，親情不協更分離。主恩殘義薄，喜怒不常，衰廢無壽，不利遠行。,辰位君基號天璿，清厚為人享福緣，念寡憐貧猶自可，又能寬大保長年。必是異路驟發，功名久遠。,巳上君基號地官，吉曜同此性偏寬。若逢五福來同位，富貴功名聳眾觀。若逢始擊，不免勞碌。,午宮君基號天基，興廢從來火旺離，土到此宮多燥暴，謀心未息貴心機。士子館閣清職，庶人主財豐。,因何弒逆與離宮，游伐符星天厄同，自是數窮來惡運，伐高何處覓元兇。丑未寅卯是離宮，縱有伐星果何用。身宮池醉伐星高，國破家亡因女寵。,未位君基號天垣，素有家資享福緣，若與文臣相會合，曰名曰祿兩俱全。主貴食天祿，臨事威猛，性達市井得之驟發無後。,申位君基號玉堂，官宮旺相主文章，文昌主大相加會，綠鬢聲名四海香。化科名貴人，必登黃甲，主清華之職，黑頭宰相。,酉位君基號天罡，秋夜生人元氣強，志大心勞何日了，儘教名利兩相妨。生於夏秋則安寧。春冬勞碌。或為醫卜方士丹客。,戌位君基號玉華，謨謀自是合中佳。吉星相助資財厚，天使聲名播遠遐。主財豐富，清高慕仙，子孫功名，福祿得君眷顧。,亥上君基號天權，不管人間福祿緣。若遇周天諸忌宿，又防身壽不長綿。甲己生人則多福祿卯宮福至號天休，福淺災深怨與愁。任是同宮臨吉曜，資財星散總難留。主祖業難居，身多流落，雖同吉星，財亦難聚。".split(",")
#臣基臨十二宮分歌
officerbase_twelve="子宮臣基名天逸，作事疏通親少力，縱然名利早如心，不若勤求厚利積。富貴深謀，亦云寡合。,丑位臣基號碧光，生來榮耀便非常。身雖閑散心多慮，主作員郎與監郎。甲己生人貴顯；夜生性不躁；日生多憂不寧。,寅上臣基木益榮，自如一宿好安身。半清半濁半文雅，方得平生聚寶珍。會吉星，男科名，女封號，春夏永壽，秋冬貧夭。,卯位臣基入木宮，稟性原來不眾同，言辭磊落聲名秀，只利移居不利宗。必是早離父母，剋害六親，或刑父母，限數忌之，喪禍之應，中防夭折。,辰宮臣宿掛金章，生氣相逢喜倍常，自是精神不塵俗，更逢吉曜富田莊。,巳上臣基不合宜，天廢為名主目虧，身命逢之憂血疾，若居疾厄更凶危。主當權無功，依享他人之福，至老身心不寧，在身命有血光之疾。,午位臣基對君基，地道無成不得宜。百倍威風當減等，先虛後實可前知。生於秋冬之間則貴顯，主持帥權。,未上臣基曰貴桓，生來端的是英賢。吉星相會功名顯，飛始相逢福力偏。不問男女，主清孤剋子，若會吉星則貴顯。,申位臣基曰黃堂，稟性虛靈終莫強，聲譽藹然騰海內，女清男貴壽而昌。主少年發達，三方星雜照，作富論。,酉位臣基曰不周，生愁口眼見虧休，為人作事多成敗，且見心高未有頭。會吉星方，豐衣食，喜玩好。,戌位臣基曰薦文，文昌相會動乾坤，清閑燕逸無榮辱，權國經邦節鉞存。主文武兼備，威烈酷刑。,亥位天門臣入宮，營謀指畫滿胸中。若逢君宿同宮分，清朝早入位三公。主剛烈正直，位極人臣。".split(",")
#民基臨十二宮分歌
pplbase_twelve="子位民基號天通，財寶豐盈府庫充，身命日時如相遇，家財山積永無窮。財祿豐而功名薄。,丑位民基號碧精，平生作事更能成，福文若也來相會，祿顯名高職更清。主福祿雙全，富貴清顯。,寅位民基號少財，勞碌身心事難遂，六親無靠致奔波，吉星如會亦可貴。勞力勞心，自幼創業。逢吉星亦可小貴。,卯位民基號通疏，滿屋金珠莫道無。只因刻薄無情義，致令破敗室空虛。主為人刻薄無情，以致破敗，到老無成。,辰位民基號天權，素有家資享福緣，若得吉星同立旺，必然富貴涉他鄉。民基臨辰生六戊，積玉堆金財必厚，還須身命不空亡，福德之宮福星在。,巳上民基可安身，地戶原來屬萬民，名為天遁閑宮分，職掌資財帝闕親。主幼年有權，職司財賦，然不免勞心力，只是有子不得力。,午位民基號土光，精神灑灑秀聲揚，多因徵姓成家計，吉曜相扶乃積倉。與吉星，主遠徙，雖仕不近君，旅途安康，因徵姓人發達。,未位民基守樞宮，多是經邦掌籍官，外郡亦當為祿吏，君基相助有恩封。主義尊難交，交人不長，恩人不足。小輩反怨，口大心小，言不及行。,申位民基號太常，男人俊秀女人強，成家多得陰人力，橫發資財富貴長。,酉位民基人皆忌，作事無成多困滯。平生力役尚無尋，更往他鄉離祖地。日生主清秀近貴發福。夜生衣祿不備。,戌位民基名陰晦，作事不成多窒礙。不惟顛倒任西東，若是子宮憂後代。一生勞力有虛名，陰命損胎陽命腰疾。,亥位民基號天清，作事多應要速成。俊士遇之聲價重，帝王親問用調羹。只是多好淫慾，遇災即解。".split(",")
#文昌臨十二宮分歌
wangcheong_twelve="子位文昌難得逢，君子亨嘉名利通，若有四神來會合，定當清絕冠文雄。若合照福君諸吉神，主文章冠世。,丑位文昌輔帝君，筆端三峽顯文明，更逢春夏旺生處，凌煙閣上立功勳。若同君福在命，侯伯之貴，喜生春夏，不利秋冬。小游同文而不秀。,寅上文昌果何如，好學無成未足奇。若是夜生仍富貴，姓名終必達天墀。夜生安享福壽，日生多憂，再同土神，六親離散，財物成敗，勞碌苦辛。,卯上文昌未足忻，天敗為名志未伸。主大相扶方吉利，守分方安晚自榮。,辰上文昌重闕開，少年平步上雲階。計神更與同宮分，職掌天書傅御才。主聰明英俊。如逢計神，必清貴顯達。,巳位文昌天祿名，如逢旺火卻光榮，小游若也來相剋，蓋世文章總不成。若生春夏，富貴榮遷；秋冬貧賤，孤蹇帶疾。父母宮遇，必先剋父。,午位文昌號上班，獨得錦繡耀鄉關，四神設要相會立，多好棲身泉石間。夜生名顯，日生，多憂而病，少樂不遂。與四神仝，多為修行之人。,未位文昌最吉祥，豹變榮為晝錦堂。若得吉神來聚會，少年高折桂枝香。日生智識明遠，貴祿重重。,申位文昌都吏名，生平涵養氣津津，福君相會位高顯，早發榮華耀二親。若會君福負不世之才，立非常之功，歷任清華。,酉位文昌獨自居，自專自是性拘拘。若無吉宿相資助，至老終為一腐儒。主自為妄大，若會福君，仍是大貴，獨行必秀而不實。,戌上文昌禁苑稱，平生作事速於成。文章早發聞朝野，豈特青衫遇一經。夜生必權貴顯達，日生主破祖勞神，多辛苦。,亥上文昌輔帝王，生來伶俐飽文章。若得吉星來相助，看取榮身步玉堂。主文章冠世，入翰苑，精學天文術數，名利兩全，終身富貴。".split(",")
#計神臨十二宮分歌
jigod_twelve="子位天機果是奇，吉曜同臨世所稀。金玉滿堂還壽考，曰名曰利總相宜。,為人機巧直捷，又文雅，男女皆然。主財祿豐盈，田園廣厚，逢吉星大貴。,丑位計神名天侍，計較有餘人莫比。奉公取利利名榮，更遇吉星尤發貴。秋冬生人，驟發榮貴，官高極品，深謀遠慮。,寅位計神曰陰鬼，千謀百計不榮身，只宜掌握他人物，少年偃蹇不由心。,卯上計神天耗星，多思多慮漫紛紛。公私阻阨時時有，親戚無依骨肉分。在襁褓家業失散，作事千謀百變難逃困苦。財散而後聚。,辰位計神最榮昌，入廟安然號月堂，曰士與農皆吉利，民豐財物士文章。主機謀遠慮，作事聰明，科甲早發，貴顯朝堂，必先貧後富。,巳上計神偏不喜，雖曰天聰終有慮。半生作事一無成，多為終身運數否。必先成後敗，作事奸詐，剋妻傷子，晚景悽惶，仕途困窮遭貶。,午宮計宿守邊宮，名利資財不甚豐。用盡機謀方吉泰，但交親友不從容。主孤獨歇滅，作事奸巧，見他人之財帛如己物，百計搜求。,未宮計宿號琴堂，富貴名高四海香。家道興隆財豐盛，更多權柄服他方。主財物豐盈，利路通達，生有廕庇，至家不艱難，會吉星，貴顯出眾。,申宮計宿偏多福，天庾為名是若何？富貴不求隨分得，英名洋溢遍山河。主科名高顯，富貴雙全，夜生多為權帥。,酉宮計宿號淹延，撓亂疑謀在中年。晚景卻教膺福壽，鎡基隨分富田園。日生不利夜生好主財物耗散，家業漂流，心性狂蕩，言語不實。,戌宮計宿號都堂，衣祿豐盈姓氏香，權重志高人欽仰，一生安樂又榮昌。必作財庫之職，錢穀之任。日生不吉，夜生多富貴。,亥宮計宿拱君臺，動作勤謀事有成，只利功名權祿位，百年豐富又光榮。主機謀出眾，為豪傑之士。帝王親問，名達天廷。".split(",")
#小游臨十二宮分歌
smallyo_twelve="子上小游天足名，不清不秀不安平。化為祿主猶之可，若遇凶星壽早傾。春夏生人，衣食安寧，若生秋冬，帶疾傷神，會吉神，可免凶星口舌。,丑上小游號華堂，中歲功名亦奮揚。閑暇優游情性急，衣冠嚴雅姓名香。主愛潔淨新鮮，好修飾，財物虛耗，聚散不常，甲己人遇之，頭面破相。,小游之星最喜寅，旺相榮華異眾人，且是襟懷不塵俗，功名富貴得全身。日生貴顯，甲第高科；夜生近貴，掌財招好子。,小游居卯最清奇，金殿文章四海知。若是祿元尤妙甚，榮華挺特應昌期。春夏生人享福發貴有權，秋冬時逄四墓。主高壽。若女人身命逢之。好為嬉恥不相宜。,小游辰位碧文星，文學清高過眾人。若是丁壬人值此，中年榮貴作朝臣。日生清貴，發福於異鄉。,小游居巳乃為良，景福為名衣祿昌。若是丁壬值祿位，少年當作紫衣郎。主有陰權，或符籙法師，鬼神自伏，藝精孤獨，秋冬生力，穡辛苦。,小游午上號天章，作事威權一世昌。舉措定教無滯礙，清閑學道也相當。主藝精技巧而孤獨，秋冬生勞碌辛苦。,玉輦未宮遇小游，此宮遇吉主封侯，權高爵貴人間少，紫綬金章第一流。主權高清，善明刑獄法不亂，用會吉星方大貴。,小游申宮最不喜，金來伐木豈相宜。淹蹇無聊多執滯，公門休向作生涯。主多是非，不利公門，作事上下不睦。若天元官星、干元星，亦可免咎。,小游酉上不堪逢，作事謀為欠始終；早歲巳遭肝腎病，刑流難免貯財空。主自幼艱難，有肝腎之疾，至老無成，望大心高，所行不實。,孤宿游星戌上安，病符為客一般看。天輪亦化分車宿，少剋男兒女不常。常帶目疾。智拙多憂。心田暗毒。有不明之禍。,亥上小游天爵名，化作科名尤最妙。少年平步玉常中，更喜文昌同入廟。與文昌同，功名貴顯，若逢飛始終難貴，雖貴亦不佳。小游偏喜亥宮臨，掌握人間富與貧。年月日時倘相遇，定為世上箇中人。".split(",")
#主大將臨十二宮分歌
homegeneral_twelve="主大子宮號富潤，守靜安閑是宿緣。經籍未嘗違左右，執持生殺鎮三邊。主掌機密之權，日生必大貴。,主大丑宮名總持，厚重端嚴不妄為，文治邦家武專閫，清名富貴兩相宜。主鎮靜之權，與君福同會者，兵權萬里。,寅宮主大名天損，縱然先富後須貧。平生作事多屯蹇，若遇飛符損壽齡。主泛濫多貪，離鄉之應。凶星衝破主水厄。,卯宮主大號天塵，志氣飄飄人仰欽。限遇運逢財祿進，身臨坐鎮福威深。,主大辰宮名庫珠，富貴榮華可自如，謀為更改多宜外，暗合那堪寄積儲。會吉星主吉，會凶星主凶。,天統星居巳上宜，乃文乃武運謀機。安邊鎮國成功績，若見文昌衣錦歸。主文武兩全，先貧後富。,主大偏嫌守午宮，若逢飛始更加凶。主客參來人習詭，不犯徒流也是窮。不問男女，主爭鬥盜傷，身體虧殘。,未上名為上吉星，壽齡自是吉相親，飛符若不同宮分，名重英豪冠世人。主聰明智慧。秀氣所鍾。,主大申宮號紫陽，文居臺閣武邊疆。為人多是精神俊，富貴聲名遠播揚。主兵權萬里機密生殺之權。,酉宮主大實堪誇，玉仲為名積富奢。若遇文昌同此位，香名四海接黃麻。同五福為兩府之格。,主大堪憐在戌方，名為弔客主刑傷。薄親損己多成敗，財物猶如雪見湯。主破祖離鄉，若會凶星，不得善終。,亥宮主大本來佳，益壽令人作事奢，立德平生多富貴，更兼名利不虛花。主子孫成行、貴顯。".split(",")
#客大將臨十二宮分歌
awaygeneral_twelve="子宮客大為入廟，英名揚顯多榮耀，君基五福若相逢，將相功勳人罕到。若獨立，主動中有靜，靜中有動，經商得財，有吉星輔，一品之貴。,丑宮客大名暗陋，作事多疑難輻輳，奔波勞苦主遷移，祖有鎡基亦消瘦。,寅宮客大號厄星，平生衣祿仗他人，一生貧困無依藉，謀望徒多辛與勤。主財帛耗散多，招官非有耳腎疾若逢飛，始主死於非命。,卯宮客大晦多迍，寶鏡塵埋不遇春。暗裡不知人面目，乍興乍廢總無成。主困窮，言語不實，富而後貧，破祖流落，父子異苗會吉，可保富貴。,辰宮客大稱最賢，名顯家豪號金鞭，若無飛始同臨會，名利俱成福祿全。逢福君主科甲及第，官居憲臺兩府之命。日生如是，夜生則否。,巳宮客大無所利，多動多疑多執滯。空門若也得逢他，或出或居多得地。利為僧道，主強悍，視他人之財如己之物，性偏好勝，成敗不一。,午上名為玉輦來，命宮見此喜安排，隨緣名利人多羨，家有珍珠進橫財。有非常之名不測之災，侍御外帥得權有心肺之疾，或作九流之業。,未宮客大未為良，百計千謀總未強。散盡資財還未了，一生奔走受凄涼。主一生困苦，或為僧道遊藝、歌舞。,申宮客大號玉堂，還宜出入走江鄉，資財厚載多如意，富貴清高不可量。主英俊顯達，或為邊帥，文武全才，一品之貴，文為臺諫，武任邊方。,酉宮客大不相和，變幻無端號激波，定有水災當戒慎，早宜修禳莫蹉跎。日生吉，夜生性弱，有始無終。若貴，必有大災。,戌宮客大號平權，遇吉惟須積善緣，衣祿豐盈名利盛，滔滔安享鎮長年。為四海遊說之客，作事成敗不長，有始無終。,客大榮居亥上名，生來福祿自相成。衣冠不但誇鮮麗，馬上傳呼號玉嬰。主掌生殺，撫鎮邊隅，定亂除奸，為當時權帥。".split(",")
#主小將臨十二宮分歌
vhomegeneral_twelve="子宮最利是主參，乘旺身居紫綬間，名利定依官貴發，文為詞館武安邊。會五福、三基、諸吉星，主登科甲；見凶星，主武貴，冬生尤大貴。,丑宮號曰玉門安，只利於民不利官。飛始臨之為敗絕，喜神同處卻多歡日生夭折勞苦，夜生男女皆榮貴。,寅宮參將號超群，到處為家到處親，官宦多遷民別祖，吉凶還向數中分。主氣血自用，好搬是非。,卯宮參將不宜逢，天晦為名便不終。凡事多成更多敗，可憐骨肉又西東。主陰謀損官，性僻執拗，或貌有虧。若丙辛生人，名萬水朝宗，主貴。,主參玉輦到辰宮，自是依人得顯榮。若問成家宜在外，不拘南北與西東。名水歸東海格，更有吉星相扶，主掌絲綸之任，會凶則貧窮夭折。,主參已上不曾閑，潦倒營謀道路間。士庶逢之多廢產，先成後敗立身難。主眼目之疾，是非日有。,午宮水宿喜相隨，福祿來亨更足財。管幹多因貴人力，虛而不實行多乖。主得外財，但為人狂詐不實，亦多心血不足之疾。,主參到未惡難當。孤苦伶仃走異鄉。技藝之能因餬口。貧窮方免入緇黃。,主參最喜入申宮，化了科名福祿榮。曰武曰文推吉助，五凶最忌與之逢。得吉星相輔乃貴。文星為文，武星為武，若會凶，又為下賤之格。,主參酉宮名沐浴，陰貴人扶方發福。雖勞心力福悠長，一見凶神又不足。主得陰貴人力，而享福悠久，只是身心多操持。,戌宮參將不可居，破祖離鄉失所依，更見始飛同位住，牽連盜賊起災非。會吉星，主得他鄉人力扶持；逢凶則有盜賊牽連之害。,翼居亥上號天魁，說道談元眾所推。自有高人為薦拔，敬他妙用好施為。逢福君主科甲之貴，必提攜上進。日生文武出群，夜生貧困夭折。".split(",")
#客小將臨十二宮分歌
vawaygeneral_twelve="客參居子名天否，作事無終亦無始。縱然名利在身宮，多不到頭中路止。會吉星近貴發福上人，成就異路功名。,客參居丑號天經，足計多謀人所欽。衣食從容財更足，還因游藝得功名。參將本來吉，逢凶始見乖。聰明為活計，伶俐作生涯逢凶主言不實，行不果，乃僭偽之徒。,客參寅位貴而昌，近貴成名號玉堂，基業本來稱富厚，於今名利兩相當。主英發聰敏。得貴人成就功名。春夏生。主早貴。秋冬生主孤獨。多疾病。,客參在卯號官星，廟旺何愁不顯名。衣錦不須歸故國，東西南北好安身。主近貴及出入王侯之家，掌權發號施令，侍從參謀，或為家臣，及兵符印信首領之職。喜春夏日間，忌秋冬夜間。同上斷。,客參辰位最相宜，立業還宜近水居，若遇飛符為下賤，飄流無定總支離。主依貴成家，為人聰明利便，但是僭偽之徒，言行不實。,客參巳位曰天傷，只見蕭條不見昌，困苦多般難度日，仍教流落在他鄉。,客參午位號天休，百事無成到白頭，淹蹇更多災與疾，一生衣食不能周。,客參居未號天瓊，官貴相扶獲顯榮，中末限星臨此處，命身凶會必貧窮。主得貴人之力而獲名利，在窮途亦好辨。,客參臨申實可悲，肢體傷殘面目虧，若在九流還不礙，自甘清苦利毛錐。主肢體有傷。面目不全。或為醫卜九流。,萍蹤四海轉飄蓬，蓋為參星到酉宮。只好作奴常近貴，不然勞碌受孤窮。主隸卒近貴，或在市廛，碌碌貧苦。,客參福力本無多，戌上安身沒奈何。縱有吉星來護助，平生惟有受奔波。,客參居亥福星饒，富貴榮華是爾曹。公子宴閒談笑共，要求名利敢辭勞。主侍貴顯，或為監押、差遣公吏。日生秀而不實，夜生貴顯智高。".split(",")
#始擊臨十二宮分歌
shiji_twelve="子宮始擊號為囚，身命逢之百種憂，撓括是非公府患，又防父母不相投。主家業耗散，平生孤苦，貧乏，強頑而虛假，陰謀害物，有湯火毒疾。,始擊來居丑位中，名為赤道帶祥容。仍防骨肉無恩眷，吉宿相資家道豐。主財物先見耗散，祖業凋零，一生勞苦，晚年方得資財有餘。,始擊偏宜寅上藏，變凶為吉號黃堂，不惟祿厚人多福，職顯身高意亦強。若獨立，主科甲貴顯，兩府之格，戊癸生人更佳。,始擊卯宮號太華，半憂半吉也亨嘉。不利運逢併限遇，恐防公訴起私家。主先敗後成，早年貧苦，晚景安樂，發財發福，大限臨之，孝服連綿。,始擊辰宮暴敗名，平生多是犯官刑。若為戊癸天元主，福祿多應致顯榮。主性傲、無知、愚魯，志大心高，有官刑之辱，到老無成，戊癸生，因禍得福。,始擊星宜在巳宮，福神添集喜相逢。仍嫌限數會於此，不免官司口舌中。主富貴雙全，福祿安享。,午上始擊號天沖，福祿逢之自顯榮，武鎮邊疆能保國，化為祿主福尤隆。主功名富貴驟然而發。,始擊未宮未為喜，家資破散餘無幾，蹇滯蕭條受苦辛，不是刑妻定剋子。,申宮始擊號改端，災禍臨頭何日安。百計千謀總虛假，貪心無厭定遭官。主性強悍，視他人之財如己物，貪心不厭。,酉宮始擊未為祥，遲鈍多因學不強。清淡家貧方可守，若還富足主顛狂。主一生成敗，作事多虛不實。,始擊平安占戌宮，榮華威重號天堂，吉星相與同宮住，名利相期服四方。主良田萬頃，金玉千箱，富貴兩全，更食天祿。,始擊之星臨亥方，名高業重忌親房。是非當見災危甚，縱讀詩書名不香。主貧賤，一生飄流，多招災禍，病不離身。".split(",")
#飛符臨十二宮分歌
flyfu_twelve="飛符在子名天哭，衣食不多無顯祿，家居改革祖基遷，若逢吉宿災不足。主離鄉背井，六親無靠，見五福三基，可免凶咎。,飛符入丑最堪娛，天乙為名主身孤，身若帶時血滯疾，或傷脾胃或癰疽。主為小校兵隸，或宰殺，亦是破祖孤獨。,飛符寅位號天旋，變禍為祥衣祿全，運若逢時仍忌擾，或生瘡毒苦憂煎。主握總戎之職，日生功名清顯，夜生夭折多敗。,飛符臨卯名沐浴，作事不成多不足，生人身命或逢之，僧道九流妨骨肉。主衣食勞碌，歇滅多凶，必遭刑獄撓括，小人侵害。,飛符辰上號天滯，是非家計湯澆雪。若還從參來相會，作事無成又窘迫。主鎔鑄爐冶，得火之利，有刑害，多是非。,飛符巳上號天醫，只利功名不利私。官貴值之多得意，庶人何以慰心思。主兵權驟發，不久亦退敗，或為提調班首。,飛符午上最難逢，元帥威名自不同。福祿自然天與足，但防骨肉有西東。主強項威猛，足計多謀，為兵符宣制。首領日生，貴顯有權。,飛符未上名天失，作事多廢無定日。宜為僧道方無害，士庶聞之遭辱叱。主臨事不密，能說他人，不能自慮，或為軍營書吏，司總。,飛符申上號破星，直須仙籙保全身。更逢吉曜來相助，亦可名為善守人。主財物破散不常，多成敗，若會吉星，主得外人財帛。,飛符酉上號暗堂，若逢身命有刑傷。平生多晦何時了，家事渾如雪見湯。又主身孤離鄉。,飛符戌上寶閣稱，不惟去禍且榮身，福君同到尢為吉，作事無疑名利成。主邊帥、方面首領，日生有功名，亦不長多暗昧，子少女多。,飛符亥上多不喜，敗壞財物皆如此。一生作事更多疑，果是凶神名絕體。主孤獨刑傷見，吉星亦難免，縱有二三子，傳家惟一見。".split(",")
#四神臨十二宮分歌
fourgod_twelve="四神居子號天宜，伶俐聰明性格奇。更有吉星相聚會，平生衣祿自饒餘。主聰明穎悟，逢五福、三基，主爵祿豐厚，丙辛生人尤美。,四神居丑名天喜，賦性多能復多藝。若逢吉宿到斯宮，限數逢之身亦貴。主得商販魚鹽之利，及舟船水洋之財。,四神寅上不相宜，淹蹇蕭條作事遲，天乙更來同位處，凶行橫禍日相隨。主性凶好殺，流落他鄉，修船補漏，竹木雇載之工。,四神卯上號燒爐，當改根基別處圖，若是獨行無大患，何憂疾病與悲呼。主得水利，及舟船雇覓、行商之類，逢飛始主癆疾傷殘。,四神辰位主榮華，名號金鞍實可誇，心性聰明人莫及，只防子息見虛花。會吉星有調羹之美，主酒肆茶鹽，巨商大賈，財富豐盈。,四神巳上號天淵，絕氣為名合此言，不利六親併子息，宜僧宜道守當年。少年離親隨聘，或庶出，主下賤。弄巧歌舞、調笑之輩。日生主富貴。,四神午位號幽微，水火相和財穀宜，旺地逢之多顯達，文昌到也更何疑。利口才舌辯，日生，乃富貴，情性忠良財帛多，主先散後聚。,四神居未不相成，別祖離宗號失榮，身命逢之多改革，游年當此弟兄分。主裁剪、技巧、匠作、走富貴之家，夜生辛苦無依，日生亦貴，相貌異常。,四神申位喜相臨，秀氣所鍾人敬欽，若是文昌來會合，清閑富貴福悠深。會吉功名顯達。,四神酉上天月星，多成多敗不安寧，家財散後聲名淡，語默施為假似真。主善言語，作事機巧，貴人敬愛，日生衣祿綿遠，夜生貧困傷殘。,漂蓬無依號天休，戌上四神多詭謀，祖業得來如瓦解，是非難定莫貪求。奔波四方。,亥上四神名本源，初歲伶仃老自安，若是文昌在三合，骨肉榮華得異緣。主近天顏，祿位高顯，善談笑，好下問，臨險成福。".split(",")
#天乙臨十二宮分歌
tianyi_twelve="子上名曰天驥星，人生遇著有虛名，三基五福同三合，富貴榮華馳令名。主破祖虛花，中年成敗，剋子刑妻，游方食祿逢飛始，諸凶則困苦勞神。,丑宮天乙實清奇，天帥威權最所宜。志氣昂昂人敬服，果然豪傑不卑微。主武職貴顯，陰謀有毒，五金中得利，女命有災厄。,天乙寅方號怒濤，若同飛始壽難高。江鄉蹤跡無依靠，別立門庭方富饒。求謀有利，主得外財。春夏生則多富，而相貌甚美。會凶星，主漂流下賤。,卯宮天乙名暗財，勞力勞心善作為。若遇飛始臨其地，金谷資財似火吹。主技藝及繡造、裁剪、針匠求利生財，夜生須謹防因財受害之事，不則饑寒。,天乙辰宮號天憲，舞文弄法多更變。若非身病與人傷，終值公非殘首面。主爐冶得利，或山林採取，五金八石生財，會吉星，主貴，但奸猾。,巳宮天乙號金章，百計千謀力量強，不特聲名揚四海，生平浩氣姓名芳。秋冬氣秀，館閣之貴，主爐火燒煉，顯名成就興家。,天乙凶星在午方，名為天戳，主殘傷。獨行自是宜屠宰，若見凶星有禍殃。主幼失父母，蹇滯憔悴，不得善終。日生有生殺之權，夜生貧困夭折。未為天暴受苦辛，生來成敗費經營。播遷事業方安定，只是為人性不平。主九流巫術，得大人敬愛，然多小人是非，憎嫌拮据。,天乙申宮號玉旌，吉星同會稱心情。邊陲武術威名重，千載黃河一鑑清。主武職、邊將，會三基五福，主科甲、臺諫，春夏榮華，秋冬偃蹇，女命如之。,酉宮天乙在金方，凜凜威風肅紀綱。凶曜不來相混雜，縱有微災亦吉昌。威鎮邊疆，武貴之格。,天乙戌宮為望雲，生來無利亦無名。為人狂妄還遭謗，虛詐偏多災禍侵。主幼失父母，剋子害妻，老見孤單破相。,亥宮天乙號名星，吉宿如臨事事亨，士宦逢之臨大限，前程顯耀樂昇平。主祖業耗散，中年成敗。".split(",")
#地乙臨十二宮分歌
earthyi_twelve="子宮地乙號貪官，利己傷人定不安，還加眾惡同相濟，離背親婚禍患牽。日生貴，夜生不利，主明天文、地理、術數亦與辰宮同論。,轉禍為祥丑上安，平生衣祿有何難。金章紫綬功名顯，莫作寒窗冷眼看。因遠游發福，或鎮守邊隅之職。,寅上名曰厄會孤，宗親不利歎窮途。為人性烈多權變，虛詐難交情義疏。縱見吉星，亦主貧困孤單，多災疾，或庶出鰥寡。,卯宮地乙最傷心，死別生離禍患侵。仁義乖疏下流輩，四神若會疾相侵。主家破財散，到老辛苦，或癆疾，或僧道會吉星，衣食稍豐。,地乙辰宮玉騎飛，化凶為福理精微。吉星會也方稱妙，不見凶星始道奇。主耿介孤高，中年發福，為富貴格，或為守土之官；會凶星，衣食不足。,巳宮地乙謾嗟咨，勞力勞神過慮思。兄弟不堪情誼薄，到頭名利晚成遲。吉星扶助當驟發，或為醫卜之流，逢凶則無倚。,午宮地乙不宜臨，陶鑄生涯多苦辛。若要清閑身自在，不戴黃冠定作僧。主裝塑窯內狊馱g物，或為僧道醫士。,未宮地乙號班頭，利己還須苦志求。竭力經營成事業，從來祖業不曾留。幹辦食祿自立貴顯。,地乙居申號紫微，聲名不薄少災非。若還五福來相會，衣食豐盈造帝扉。主秉性重厚。能言語。多風流。財帛耗散而不聚。,酉宮地乙名宮怨，妻子不全家業變。飛符始擊或來同，不惟抱疾還貧賤。主游藝流蕩，賭嫖猖狂，刑剋妻子，下賤之輩。,戌宮地乙若相逢，玉樹為名氣象雄。衣祿到頭終有望，也成名利也成功。主富厚，財穀豐盈，通天文、地理、曆數。,亥宮地乙號清臺，曆數通靈不妄裁，食祿天廚權職重，吉神聚會乃英才。主貴顯豐富，若妄自尊大，貪名戀祿，反受辱矣詐，衰宮貧困奈如何。".split(",")


