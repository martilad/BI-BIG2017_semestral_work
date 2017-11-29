
# Semestrální práce z předmětu BI-BIG
Jedná se o implementaci a předvedení fukčnosti dotazů a řešení nad námi zvolenými technologiemi. Jedná se především o dotazy a agregace a indexování. Nutné zpracovat důkladnou dokumentaci.

>>>
## Zadání semestrální úlohy

Semestrální práce může být na libovolné téma, důležité je dodržet následující požadavky.

### Požadavky

-  vybrat si min. 3 různé datasety (možno i vygenerovat smysluplná data náhodně)
  -  každý vstupní dataset bude mít nejméně 5.000 záznamů (pokud budete předvádět v učebně, zvolte data tak, aby bylo časově reálné úlohu ukázat)
-  tyto (min.) 3 datasety naimportovat do databáze
-  vytvořit nový dataset, který bude agregovat data z jednoho původního datasetu
-  vytvořit nový dataset, který bude agregovat data ze dvou původních datasetů najednou
-  vytvořit nad kterýmkoliv datasetem index a připravit 3 různé dotazy do tohoto indexu
  -  využit filtrování
  -  využít třídění
  -  použít wildcard hledání (www.*soft*.com)
-  jako technologii lze použít kteroukoliv distribuovanou noSQL databázi a nad ní postavený index
  -  doporučené technologie jsou Cassandra, Hive, Solr (či Elasticsearch)
-  k semestrální práci je potřeba zpracovat kompletní dokumentaci (odevzdat ve formátu PDF), která bude obsahovat minimálně:
  -  klasickou strukturu včetně hlavičky, rejstříku, úvodu, hlavní části, závěru
  -  popis databáze (businessový pohled na to, jaká data se budou používat)
  -  popis a ukázku dat z použitých datasetů
  -  kompletní příkazy použité pro jednotlivé transformace
  -  popis použitých technologií (high-level, jaké nástroje jsou použity)
  -  v příloze použité konfigurační soubory (např. pro search engine)
  -  na základě dokumentace by mělo být možné se vstupními datasety kompletně replikovat vaší práci!
>>>