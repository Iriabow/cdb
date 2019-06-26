
from tensorflow import keras
from source_data import SourceData
import pickle

# Loading a neural network already trained and using it to evaluate and derive what is its ontological classification.
model = keras.models.load_model("model.h5")
print("Loaded model from disk")
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

# Loading the word index
word_index = []
with open('word_index.pkl', 'rb') as f:
    word_index = pickle.load(f)

# The text to classify:
data_to_evaluate = [



    ["""Luis Miguel González Bosé (born April 3, 1956), usually known as Miguel Bosé, is a Panamanian-born Spanish pop new wave musician and actor. Bosé became an honorary Colombian citizen in 2010. """, "Person"],
    ["""Slayers (Japanese: スレイヤーズ Hepburn: Sureiyāzu) is a Japanese light novel series written by Hajime Kanzaka and illustrated by Rui Araizumi. The novels had been serialized in Dragon Magazine, and were later adapted into several manga titles, anime television series, anime films, OVA series, role-playing video games, and other media. Slayers follows the adventures of teenage sorceress Lina Inverse and her companions as they journey through their world. Using powerful magic and swordsmanship they battle overreaching wizards, demons seeking to destroy the world, and an occasional hapless gang of bandits. The anime series is considered to be one of the most popular of the 1990s.""", "Work"],
    ["""Innovation economics is a growing economic theory that emphasizes entrepreneurship and innovation. Innovation economics is based on two fundamental tenets: that the central goal of economic policy should be to spur higher productivity through greater innovation, and that markets relying on input resources and price signals alone will not always be as effective in spurring higher productivity, and thereby economic growth. This is in contrast to the two other conventional economic doctrines, neoclassical economics and Keynesian economics.""", "Work"],
    ["""The Mona Lisa (/ˌmoʊnə ˈliːsə/; Italian: Monna Lisa [ˈmɔnna ˈliːza] or La Gioconda [la dʒoˈkonda], French: La Joconde [la ʒɔkɔ̃d]) is a half-length portrait of a woman by the Italian artist Leonardo da Vinci, which has been acclaimed as "the best known, the most visited, the most written about, the most sung about, the most parodied work of art in the world". The painting, thought to be a portrait of Lisa Gherardini, the wife of Francesco del Giocondo, is in oil on a white Lombardy poplar panel, and is believed to have been painted between 1503 and 1506. Leonardo may have continued working on it as late as 1517. It was acquired by King Francis I of France and is now the property of the French Republic, on permanent display at the Louvre Museum in Paris since 1797. The subject's expression, which is frequently described as enigmatic, the monumentality of the composition, the subtle modelling of forms, and the atmospheric illusionism were novel qualities that have contributed to the continuing fascination and study of the work.""", "Person"],
    ["""The Fairy Feller's Master-Stroke is a painting by English artist Richard Dadd. It was commissioned by own mononymously as Rosalía, is a Spanish singer, songwritGeorge Henry Haydon, who was head steward at Bethlem Royal Hospital at the time. He was impressed by Dadd's artistic efforts and asked for a fairy painting of his own. Dadd worked on the painting for nine years, paying microscopic attention to detail and using a layering technique to produce 3D-like results. Although it is generally regarded as his most important work, Dadd himself considered the painting to be unfinished (the background of the lower left corner is only sketched in), and as such added the suffix of "Quasi" to its title. In order to give context to his work, Dadd subsequently wrote a long poem by the name of Elimination of a Picture & its Subject—called The Fellers' Master Stroke in which each of the characters appearing in the picture is given a name and purpose—including myriad references to old English folklore and Shakespeare—in an apparent attempt to show that the painting's unique composition was not merely a product of random, wild inspiration. The painting is in the Tate Britain collection. It was presented to the Tate by the war poet Siegfried Sassoon in memory of his friend and fellow officer Julian Dadd, a great-nephew of the artist, and of his two brothers who gave their lives in the First World War.""", "Work"],
    ["""Rosalía Vila Tobella (born September 25, 1993), kner, actress and record producer.[1][2] Known for her modern interpretations of flamenco music, Rosalía crossed language boundaries after receiving praise from international influencers and after several collaborations with artists such as J Balvin, Pharrell Williams and James Blake. """, "Person"],
    ["""Brian Harold May, CBE (born 19 July 1947) is an English musician, singer, songwriter and astrophysicist, best known as the lead guitarist of the rock band Queen. He uses a home-built electric guitar, called the Red Special. His compositions for the band include "We Will Rock You", "Tie Your Mother Down", "I Want It All", "Fat Bottomed Girls", "Flash", "Hammer to Fall", "Save Me", "Who Wants to Live Forever" and "The Show Must Go On". May was a co-founder of Queen with lead singer Freddie Mercury and drummer Roger Taylor, having previously performed with Taylor in the band Smile, which he had joined while he was at university. Within five years of their formation in 1970 and the recruitment of bass player John Deacon completing the lineup, Queen had become established as one of the biggest rock bands in Britain with the album A Night at the Opera and its single "Bohemian Rhapsody". From the mid-1970s until the early 1990s, Queen were an almost constant presence in the UK charts and played some of the biggest venues in the world, most notably giving an acclaimed performance at Live Aid in 1985. As a member of Queen, May became regarded as a virtuoso musician and he was identified with a distinctive sound created through his layered guitar work. Following the death of Mercury in 1991, Queen were put on hiatus for several years but were eventually reconvened by May and Taylor for further performances featuring other vocalists. In 2005, a Planet Rock poll saw May voted the 7th greatest guitarist of all time. He was ranked at No. 26 on Rolling Stone magazine's list of the "100 Greatest Guitarists of All Time". In 2012, May was ranked the 2nd greatest guitarist of all time by a Guitar World magazine readers poll. He was appointed a Commander of the Most Excellent Order of the British Empire (CBE) in 2005 for "services to the music industry and for charity work". May attained a PhD in astrophysics from Imperial College London in 2007 and was Chancellor of Liverpool John Moores University from 2008 to 2013. He was a "science team collaborator" with NASA's New Horizons Pluto mission. He is also a co-founder of the awareness campaign, Asteroid Day. Asteroid 52665 Brianmay was named after him. May is also an animal rights activist, campaigning against the hunting of foxes and the culling of badgers in the UK.""", "Person"],



    ["""Robert John Arthur "Rob" Halford (born 25 August 1951) is an English singer and songwriter, who is best known as the lead vocalist for the Grammy Award-winning heavy metal band Judas Priest and famed for his powerful wide ranging operatic voice. AllMusic says of Halford: "There have been few vocalists in the history of heavy metal whose singing style has been as influential and instantly recognizable", possessing a voice which is "able to effortlessly alternate between a throaty growl and an ear-splitting falsetto". Halford was voted number 33 in the greatest voices in rock by Planet Rock listeners in 2009. In addition to his work with Judas Priest, he has been involved with several side projects, including Fight, 2wo and Halford. In 1998, he came out as gay in an interview with MTV news making him the first openly gay singer in heavy metal music.""", "Person"],
    ["""Kenneth "K. K." Downing Jr. (born 27 October 1951) is a retired British guitarist and songwriter, co-founder of the heavy metal band, and an author. """, "Person"],
    ["""Freddie Mercury (born Farrokh Bulsara; 5 September 1946 – 24 November 1991) was a British singer, songwriter and record producer, known as the lead vocalist and co-principal songwriter of the rock band Queen. He also became known for his flamboyant stage persona and four-octave vocal range. Mercury wrote and composed numerous hits for Queen (including "Bohemian Rhapsody," "Killer Queen," "Somebody to Love," "Don't Stop Me Now," "Crazy Little Thing Called Love," and "We Are the Champions"); occasionally served as a producer and guest musician (piano or vocals) for other artists; and concurrently led a solo career while performing with Queen. Mercury was born of Parsi descent in the Sultanate of Zanzibar and grew up there and in India until his mid-teens, before moving with his family to Middlesex, England — ultimately forming the band Queen in 1970 with Brian May and Roger Taylor. Mercury died in 1991 at age 45 due to complications from AIDS, having acknowledged the day before his death that he had contracted the disease. In 1992 Mercury was posthumously awarded the Brit Award for Outstanding Contribution to British Music, with a tribute concert held at Wembley Stadium, London. As a member of Queen, he was inducted into the Rock and Roll Hall of Fame in 2001, the Songwriters Hall of Fame in 2003, the UK Music Hall of Fame in 2004, and the band received a star on the Hollywood Walk of Fame in 2002. In 2002, he was placed at number 58 in the BBC's poll of the 100 Greatest Britons. Consistently voted one of the greatest singers in the history of popular music, Mercury was voted best male singer of all time in a 2005 poll organised by Blender and MTV2; was ranked at 18 on the 2008 Rolling Stone list of the 100 greatest singers ever; was elected in 2009 as the best rock singer of all time by Classic Rock; — and was described by AllMusic as "one of rock's greatest all-time entertainers," with "one of the greatest voices in all of music.""", "Person"],
    ["""Napoleon Bonaparte (Napoléon Bonaparte; /nəˈpoʊliən, -ˈpoʊljən/; French: [napɔleɔ̃ bɔnapaʁt], Italian: [napoleoŋe bɔŋaparte], born Napoleone di Buonaparte; 15 August 1769 – 5 May 1821) was a French military and political leader who rose to prominence during the French Revolution and led several successful campaigns during the Revolutionary Wars. As Napoleon I, he was Emperor of the French from 1804 until 1814, and again in 1815. Napoleon dominated European and global affairs for more than a decade while leading France against a series of coalitions in the Napoleonic Wars. He won most of these wars and the vast majority of his battles, building a large empire that ruled over continental Europe before its final collapse in 1815. One of the greatest commanders in history, his wars and campaigns are studied at military schools worldwide. He also remains one of the most celebrated and controversial political figures in human history. He was born in Corsica to a relatively modest family from the minor nobility. When the Revolution broke out in 1789, Napoleon was serving as an artillery officer in the French army. He quickly capitalized on the new political situation by returning to Corsica in hopes of starting a political career. After that venture failed, he came back to the military and rose rapidly through the ranks, ending up as commander of the Army of Italy after saving the governing Directory by suppressing a revolt from royalist insurgents. At age 26, he began his first military campaign against the Austrians and their Italian allies, scoring a series of decisive victories, conquering the Italian Peninsula in a year, and becoming a national hero. In 1798, he led a military expedition to Egypt that served as a springboard to political power. He engineered a coup in November 1799 and became First Consul of the Republic. His rising ambition inspired him to go further, and in 1804 he became the first Emperor of the French. Intractable differences with the British meant that the French were facing a Third Coalition by 1805. Napoleon shattered this coalition with decisive victories in the Ulm Campaign and a historic triumph over Russia and Austria at the Battle of Austerlitz, which led to the elimination of the Holy Roman Empire. In 1806, the Fourth Coalition took up arms against him because Prussia became worried about growing French influence on the continent. Napoleon quickly knocked out Prussia at the battles of Jena and Auerstedt, then marched the Grand Army deep into Eastern Europe and annihilated the Russians in June 1807 at the Battle of Friedland. France then forced the defeated nations of the Fourth Coalition to sign the Treaties of Tilsit in July 1807, bringing an uneasy peace to the continent. Tilsit signified the high watermark of the French Empire. In 1809, the Austrians challenged the French again during the War of the Fifth Coalition, but Napoleon solidified his grip over Europe after triumphing at the Battle of Wagram in July. Hoping to extend the Continental System meant to choke off British goods from the European mainland, Napoleon invaded Iberia and declared his brother Joseph the King of Spain in 1808. The Spanish and the Portuguese revolted with British support. The Peninsular War lasted six years, featured extensive guerrilla warfare, and ended in victory for the Allies. The Continental System caused recurring diplomatic conflicts between France and its client states, especially Russia. Unwilling to bear the economic consequences of reduced trade, the Russians routinely violated the Continental System and enticed Napoleon into another war. The French launched a major invasion of Russia in the summer of 1812. The resulting campaign witnessed the collapse of the Grand Army, the destruction of Russian lands and cities, and inspired a renewed push against Napoleon by his enemies. In 1813, Prussia and Austria joined Russian forces in a Sixth Coalition against France. A lengthy military campaign culminated in a large Allied army defeating Napoleon at the Battle of Leipzig in October 1813. The Allies then invaded France and captured Paris in the spring of 1814, forcing Napoleon to abdicate in April. He was exiled to the island of Elba near Rome and the Bourbons were restored to power. However, Napoleon escaped from Elba in February 1815 and took control of France once again. The Allies responded by forming a Seventh Coalition, which defeated Napoleon at the Battle of Waterloo in June. The British exiled him to the remote island of Saint Helena in the South Atlantic, where he spent the remainder of his years. His death in 1821 at the age of 51 was received with surprise, shock, and grief throughout Europe, leaving behind a memory that still persists. Napoleon had an extensive and powerful influence on the modern world, bringing liberal reforms to the numerous territories that he conquered and controlled, such as the Low Countries, Switzerland, and large parts of modern Italy and Germany. He implemented fundamental liberal policies in France and throughout Western Europe. His legal achievement, the Napoleonic Code, has influenced the legal systems of more than 70 nations around the world. British historian Andrew Roberts stated, "The ideas that underpin our modern world—meritocracy, equality before the law, property rights, religious toleration, modern secular education, sound finances, and so on—were championed, consolidated, codified and geographically extended by Napoleon. To them he added a rational and efficient local administration, an end to rural banditry, the encouragement of science and the arts, the abolition of feudalism and the greatest codification of laws since the fall of the Roman Empire.""", "Person"],
    ["""(This name uses Spanish naming customs: the first or paternal family name is Rajoy and the second or maternal family name is Brey.) Mariano Rajoy Brey (Spanish: [maˈɾjano raˈxoi ˈβɾei]; born 27 March 1955) is a Spanish politician who is the acting Prime Minister of Spain. He became leader of the People's Party in 2004 and Prime Minister in 2011 following the People's Party landslide victory in that year's general election. His party lost their majority in the 2015 general election and currently he is the acting Prime Minister of a caretaker government. Rajoy was a Minister under the José María Aznar administration, occupying different leading roles in different Ministries between 1996 and 2003, and he also was the Deputy Prime Minister between 2000 and 2003. He was the Leader of the Opposition between 2004 and 2011 under José Luis Rodríguez Zapatero's government.""", "Person"]
]

for i in range(len(data_to_evaluate) - 1):
    text = data_to_evaluate[i][0]
    expected_result = data_to_evaluate[i][1]

    vectorized_text = SourceData.vectorize_text(word_index, text)

    data_preprocessed = keras.preprocessing.sequence.pad_sequences([vectorized_text, ],
                                                                   value=word_index["<PAD>"],
                                                                   padding='post',
                                                                   maxlen=256)

    final_result = model.predict_classes(data_preprocessed)

    # 0 is a work and 1 is a person
    print("Text" + str(i) + " - Value expected: " + expected_result + "; Value returned: " + str(final_result[0]) + "\n")
