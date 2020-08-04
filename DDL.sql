insert into scipapers
select title, journal, authors, url ,refid from json_populate_recordset(null::scipapers, 
        '[
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 1,
            "title": "RadioComics \u2013 Santa Claus and the future of radiology",
            "authors": "Lombardo P, Boehm I, Nairz K ",
            "Published Date": "2020",
            "journal": "Eur J Radiol",
            "refid": -1560926826
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 2,
            "title": "CiteSeerX",
            "authors": "Samuel, A. L. ",
            "Published Date": "July 1959",
            "journal": "IBM journal of Research and Development",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 3,
            "title": "Siri, Siri, in my hand: Whos the fairest in the land? On the interpretations, illustrations, and implications of artificial intelligence",
            "authors": "Kaplan, Andreas; Haenlein, Michael ",
            "Published Date": "1 January 2019",
            "journal": "Business Horizons",
            "refid": 1617588388
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 4,
            "title": "Correction to ",
            "authors": "Hart, P. E.; Nilsson, N. J.; Raphael, B. ",
            "Published Date": "1972",
            "journal": "SIGART Newsletter",
            "refid": 1842133093
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 5,
            "title": "Commonsense reasoning and commonsense knowledge in artificial intelligence",
            "authors": "Davis, Ernest; Marcus, Gary ",
            "Published Date": "24 August 2015",
            "journal": "Communications of the ACM",
            "refid": -1348341202
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 6,
            "title": "Understanding natural language",
            "authors": "Winograd, Terry ",
            "Published Date": "January 1972",
            "journal": "Cognitive Psychology",
            "refid": 1882687108
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 7,
            "title": "On the problem of making autonomous vehicles conform to traffic law",
            "authors": "Prakken, Henry ",
            "Published Date": "31 August 2017",
            "journal": "Artificial Intelligence and Law",
            "refid": 1067815295
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 8,
            "title": "The knowledge level in cognitive architectures: Current limitations and possible developments",
            "authors": "Lieto, Antonio ",
            "Published Date": "May 2018",
            "journal": "Cognitive Systems Research",
            "refid": 1757859096
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 9,
            "title": "Content based video indexing and retrieval",
            "authors": "Smoliar, Stephen W.; Zhang, HongJiang ",
            "Published Date": "1994",
            "journal": "IEEE Multimedia",
            "refid": -1147194485
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 10,
            "title": "On scene interpretation with description logics",
            "authors": "Neumann, Bernd; M\u00f6ller, Ralf ",
            "Published Date": "January 2008",
            "journal": "Image and Vision Computing",
            "refid": 1774439198
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 11,
            "title": "Using Commercial Knowledge Bases for Clinical Decision Support: Opportunities, Hurdles, and Recommendations",
            "authors": "Kuperman, G. J.; Reichley, R. M.; Bailey, T. C. ",
            "Published Date": "1 July 2006",
            "journal": "journal of the American Medical Informatics Association",
            "refid": 168196597
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 12,
            "title": "A survey of interestingness measures for knowledge discovery",
            "authors": "MCGARRY, KEN ",
            "Published Date": "1 December 2005",
            "journal": "The Knowledge Engineering Review",
            "refid": -1218825205
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 13,
            "title": "Machine learning: Trends, perspectives, and prospects",
            "authors": "Jordan, M. I.; Mitchell, T. M. ",
            "Published Date": "16 July 2015",
            "journal": "Science",
            "refid": -1543233824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 14,
            "title": "Jumping NLP Curves: A Review of Natural Language Processing Research [Review Article]",
            "authors": "Cambria, Erik; White, Bebo ",
            "Published Date": "May 2014",
            "journal": "IEEE Computational Intelligence Magazine",
            "refid": 1031599022
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 15,
            "title": "Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age",
            "authors": "Cadena, Cesar; Carlone, Luca; Carrillo, Henry; Latif, Yasir; Scaramuzza, Davide; Neira, Jose; Reid, Ian; Leonard, John J. ",
            "Published Date": "December 2016",
            "journal": "IEEE Transactions on Robotics",
            "refid": 582310459
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 16,
            "title": "Theory of mind for a humanoid robot",
            "authors": "Scassellati, Brian ",
            "Published Date": "2002",
            "journal": "Autonomous Robots",
            "refid": -501358663
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 17,
            "title": "An Overview of Recent Progress in the Study of Distributed Multi-Agent Coordination",
            "authors": "Cao, Yongcan; Yu, Wenwu; Ren, Wei; Chen, Guanrong ",
            "Published Date": "February 2013",
            "journal": "IEEE Transactions on Industrial Informatics",
            "refid": -1058638613
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 18,
            "title": "A review of affective computing: From unimodal analysis to multimodal fusion",
            "authors": "Poria, Soujanya; Cambria, Erik; Bajpai, Rajiv; Hussain, Amir ",
            "Published Date": "September 2017",
            "journal": "Information Fusion",
            "refid": 627151320
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 19,
            "title": "Human-level control through deep reinforcement learning",
            "authors": "Mnih, Volodymyr; Kavukcuoglu, Koray; Silver, David; Rusu, Andrei A.; Veness, Joel; Bellemare, Marc G.; Graves, Alex; Riedmiller, Martin; Fidjeland, Andreas K.; Ostrovski, Georg; Petersen, Stig; Beattie, Charles; Sadik, Amir; Antonoglou, ",
            "Published Date": "26 February 2015",
            "journal": "Nature",
            "refid": -48894007
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 20,
            "title": "A world survey of artificial brain projects, Part II: Biologically inspired cognitive architectures",
            "authors": "Goertzel, Ben; Lian, Ruiting; Arel, Itamar; de Garis, Hugo; Chen, Shuo ",
            "Published Date": "December 2010",
            "journal": "Neurocomputing",
            "refid": 350396391
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 21,
            "title": "Expert systems",
            "authors": "Frederick, Hayes-Roth; William, Murray; Leonard, Adelman. \"Expert systems\". ",
            "Published Date": "NULL",
            "journal": "AccessScience",
            "refid": 962290857
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 22,
            "title": "The knowledge level in cognitive architectures: Current limitations and possibile developments",
            "authors": "Lieto, Antonio; Lebiere, Christian; Oltramari, Alessandro ",
            "Published Date": "May 2018",
            "journal": "Cognitive Systems Research",
            "refid": -189891733
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 23,
            "title": "The role of cognitive architectures in general artificial intelligence",
            "authors": "Lieto, Antonio; Bhatt, Mehul; Oltramari, Alessandro; Vernon, David ",
            "Published Date": "May 2018",
            "journal": "Cognitive Systems Research",
            "refid": -1495508794
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 24,
            "title": "CiteSeerX",
            "authors": "Elkan, Charles ",
            "Published Date": "1994",
            "journal": "IEEE Expert",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 25,
            "title": "Deep Neural Networks for Acoustic Modeling in Speech Recognition \u2013 The shared views of four research groups",
            "authors": "Hinton, G.; Deng, L.; Yu, D.; Dahl, G.; Mohamed, A.; Jaitly, N.; Senior, A.; Vanhoucke, V.; Nguyen, P.; Sainath, T.; Kingsbury, B. ",
            "Published Date": "2012",
            "journal": "IEEE Signal Processing Magazine",
            "refid": -341543822
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 26,
            "title": "Deep Learning in Neural Networks: An Overview",
            "authors": "Schmidhuber, J. ",
            "Published Date": "2015",
            "journal": "Neural Networks",
            "refid": 1040503092
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 27,
            "title": "Schmidhuber, J\u00fcrgen",
            "authors": "Schmidhuber, J\u00fcrgen",
            "Published Date": "NULL",
            "journal": "Scholarpedia",
            "refid": 1864369681
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 28,
            "title": "Polynomial Theory of Complex Systems",
            "authors": "Ivakhnenko, A. G. ",
            "Published Date": "1971",
            "journal": "IEEE Transactions on Systems, Man, and Cybernetics",
            "refid": 896583758
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 29,
            "title": "Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position",
            "authors": "Fukushima, K. ",
            "Published Date": "1980",
            "journal": "Biological Cybernetics",
            "refid": 281887415
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 30,
            "title": "Silver, David",
            "authors": "Silver, David",
            "Published Date": "NULL",
            "journal": "Nature",
            "refid": -250761552
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 31,
            "title": "CiteSeerX",
            "authors": "Schmidhuber, J. ",
            "Published Date": "1992",
            "journal": "Neural Computation",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 32,
            "title": "CiteSeerX",
            "authors": "Ontanon, Santiago; Synnaeve, Gabriel; Uriarte, Alberto; Richoux, Florian; Churchill, David; Preuss, Mike ",
            "Published Date": "December 2013",
            "journal": "IEEE Transactions on Computational Intelligence and AI in Games",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 33,
            "title": "Moving beyond the Turing Test with the Allen AI Science Challenge",
            "authors": "Schoenick, Carissa; Clark, Peter; Tafjord, Oyvind; Turney, Peter; Etzioni, Oren ",
            "Published Date": "23 August 2017",
            "journal": "Communications of the ACM",
            "refid": -417223964
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 34,
            "title": "Universal psychometrics: Measuring cognitive abilities in the machine kingdom",
            "authors": "Hern\u00e1ndez-Orallo, Jos\u00e9; Dowe, David L.; Hern\u00e1ndez-Lloreda, M.Victoria ",
            "Published Date": "March 2014",
            "journal": "Cognitive Systems Research",
            "refid": -200861221
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 35,
            "title": "Predicting judicial decisions of the European Court of Human Rights: a Natural Language Processing perspective",
            "authors": "N. Aletras; D. Tsarapatsanis; D. Preotiuc-Pietro; V. Lampos ",
            "Published Date": "2016",
            "journal": "PeerJ Computer Science",
            "refid": -2127534596
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 36,
            "title": "Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning",
            "authors": "Kermany, D; Goldbaum, M; Zhang, Kang ",
            "Published Date": "2018",
            "journal": "Cell",
            "refid": 1207420053
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 37,
            "title": "Technical Inefficiency, Allocative Inefficiency, and Audit Pricing",
            "authors": "Chang, Hsihui; Kao, Yi-Ching; Mashruwala, Raj; Sorensen, Susan M. ",
            "Published Date": "10 April 2017",
            "journal": "journal of Accounting, Auditing & Finance",
            "refid": 1685028739
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 38,
            "title": "Future Progress in Artificial Intelligence: A Poll Among Experts",
            "authors": "M\u00fcller, Vincent C.; Bostrom, Nick ",
            "Published Date": "2014",
            "journal": "AI Matters",
            "refid": -66610173
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 39,
            "title": "CiteSeerX",
            "authors": "Frey, Carl Benedikt; Osborne, Michael A ",
            "Published Date": "1 January 2017",
            "journal": "Technological Forecasting and Social Change",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 40,
            "title": "Regulating artificial intelligence and robotics: ethics by design in a digital society",
            "authors": "Iphofen, Ron; Kritikos, Mihalis ",
            "Published Date": "3 January 2019",
            "journal": "Contemporary Social Science",
            "refid": -1271124272
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 41,
            "title": "Evans, Woody",
            "authors": "Evans, Woody",
            "Published Date": "NULL",
            "journal": "Teknokultura",
            "refid": -2089905935
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 42,
            "title": "Artificial Intelligence and the Public Sector\u2014Applications and Challenges",
            "authors": "Wirtz, Bernd W.; Weyerer, Jan C.; Geyer, Carolin ",
            "Published Date": "24 July 2018",
            "journal": "International journal of Public Administration",
            "refid": -159860253
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 43,
            "title": "Computer",
            "authors": "Buttazzo, G. ",
            "Published Date": "July 2001",
            "journal": "Computer",
            "refid": 401143592
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 44,
            "title": "CiteSeerX",
            "authors": "McCauley, Lee ",
            "Published Date": "2007",
            "journal": "Ethics and Information Technology",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 45,
            "title": "Cognitive developmental robotics: a survey",
            "authors": "Asada, M.; Hosoda, K.; Kuniyoshi, Y.; Ishiguro, H.; Inui, T.; Yoshikawa, Y.; Ogino, M.; Yoshida, C. ",
            "Published Date": "2009",
            "journal": "IEEE Transactions on Autonomous Mental Development",
            "refid": 426951199
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 46,
            "title": "Brooks, Rodney",
            "authors": "Brooks, Rodney",
            "Published Date": "NULL",
            "journal": "Robotics and Autonomous Systems",
            "refid": 904759822
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 47,
            "title": "Beyond the Turing Test",
            "authors": "Hernandez-Orallo, Jose ",
            "Published Date": "2000",
            "journal": "journal of Logic, Language and Information",
            "refid": 236020733
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 48,
            "title": "CiteSeerX",
            "authors": "Hernandez-Orallo, J.; Dowe, D. L. ",
            "Published Date": "2010",
            "journal": "Artificial Intelligence",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 49,
            "title": "Learning multiple layers of representation",
            "authors": "Hinton, G. E. ",
            "Published Date": "2007",
            "journal": "Trends in Cognitive Sciences",
            "refid": 1269836226
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 50,
            "title": "Siri, Siri in my Hand, whos the Fairest in the Land? On the Interpretations, Illustrations and Implications of Artificial Intelligence",
            "authors": "Kaplan, Andreas; Haenlein, Michael ",
            "Published Date": "2019",
            "journal": "Business Horizons",
            "refid": 2110243271
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 51,
            "title": "How can computers get common sense?",
            "authors": "Kolata, G. ",
            "Published Date": "1982",
            "journal": "Science",
            "refid": 101213749
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 52,
            "title": "The Use of Artificial-Intelligence-Based Ensembles for Intrusion Detection: A Review",
            "authors": "Kumar, Gulshan; Kumar, Krishan ",
            "Published Date": "2012",
            "journal": "Applied Computational Intelligence and Soft Computing",
            "refid": 2044854856
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 53,
            "title": "The changing science of machine learning",
            "authors": "Langley, Pat ",
            "Published Date": "2011",
            "journal": "Machine Learning",
            "refid": -1515712164
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 54,
            "title": "CiteSeerX",
            "authors": "Lungarella, M.; Metta, G.; Pfeifer, R.; Sandini, G. ",
            "Published Date": "2003",
            "journal": "Connection Science",
            "refid": 1625570824
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 55,
            "title": "Newell, Allen",
            "authors": "Newell, Allen",
            "Published Date": "NULL",
            "journal": "Communications of the ACM",
            "refid": 297236318
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 56,
            "title": "On the impact of robotics in behavioral and cognitive sciences: from insect navigation to human cognitive development",
            "authors": "Oudeyer, P-Y. ",
            "Published Date": "2010",
            "journal": "IEEE Transactions on Autonomous Mental Development",
            "refid": -1574895739
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 57,
            "title": "Searle, John",
            "authors": "Searle, John",
            "Published Date": "NULL",
            "journal": "Behavioral and Brain Sciences",
            "refid": -398477796
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 58,
            "title": "Artificial Intelligence",
            "authors": "Tecuci, Gheorghe ",
            "Published Date": "March\u2013April 2012",
            "journal": "Wiley Interdisciplinary Reviews: Computational Statistics",
            "refid": -1493094531
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 59,
            "title": "Autonomous mental development by robots and animals",
            "authors": "Weng, J.; McClelland; Pentland, A.; Sporns, O.; Stockman, I.; Sur, M.; Thelen, E. ",
            "Published Date": "2001",
            "journal": "Science",
            "refid": -26390423
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 60,
            "title": "The development of an AI journal ranking based on the revealed preference approach",
            "authors": "Serenko, Alexander ",
            "Published Date": "2010",
            "journal": "journal of Informetrics",
            "refid": -1998179916
        },
        {
            "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "count": 61,
            "title": "Comparing the expert survey and citation impact journal ranking methods: Example from the field of Artificial Intelligence",
            "authors": "Serenko, Alexander; Michael Dohan ",
            "Published Date": "2011",
            "journal": "journal of Informetrics",
            "refid": 152258738
        }
    ]'
);