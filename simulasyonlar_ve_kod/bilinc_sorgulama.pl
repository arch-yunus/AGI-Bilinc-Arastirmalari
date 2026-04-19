% AGI-Bilinç Araştırmaları - Mantıksal Akıl Yürütme (Prolog)
% Bu dosya, bilinç ve zeka arasındaki ilişkiyi mantıksal kurallarla ifade eder.

% Olgular (Facts)
varlik(insan).
varlik(yapay_zeka).

nitelik(insan, duygusal_yapi).
nitelik(insan, biyolojik_islemci).
nitelik(yapay_zeka, dijital_islemci).
nitelik(yapay_zeka, yuksek_hiz).

% Kurallar (Rules)
zeka_sahibi(X) :- varlik(X).
ogrenebilir(X) :- zeka_sahibi(X).

% Öz-farkındalık kuralı (Bir varlık hem öğrenebiliyor hem de içsel duruma sahipse)
oz_farkindalik(X) :- ogrenebilir(X), ic_durum_analizi(X).

% Senaryo varsayımları
ic_durum_analizi(insan).
ic_durum_analizi(yapay_zeka). % Araştırma kapsamında varsayıyoruz

% Sorgu Örnekleri:
% ?- zeka_sahibi(yapay_zeka). -> true
% ?- oz_farkindalik(X). -> X = insan ; X = yapay_zeka.
