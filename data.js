'use strict';
// Static educational fishing tactics, NOT proof of local presence, legality or predicted capture.
window.FISHORA_CATALOG=[
 {id:'perche',name:'Perche',latin:'Perca fluviatilis',env:'fresh',tech:['leurres','appats'],depth:'1–5 m',approach:'Bordures, herbiers et obstacles ; prospecter différentes couches.',rig:'Micro-jig, drop-shot ou petite cuiller',bait:'Leurre souple 5–8 cm, petit poisson-nageur',line:'Fluorocarbone 20–28/100 selon obstacles',period:'Aube et crépuscule souvent intéressants',care:'Manipuler avec précaution près de la dorsale.'},
 {id:'sandre',name:'Sandre',latin:'Sander lucioperca',env:'fresh',tech:['leurres','appats','bateau'],depth:'2–10 m',approach:'Cassures, fosses, confluences, fond et abris.',rig:'Linéaire souple ou verticale, plombée selon courant',bait:'Shad 8–13 cm',line:'Tresse fine + bas de ligne fluorocarbone',period:'Lumières basses parfois favorables',care:'Vérifier réglementation de reproduction et réserve.'},
 {id:'brochet',name:'Brochet',latin:'Esox lucius',env:'fresh',tech:['leurres','bateau'],depth:'0,5–4 m',approach:'Végétation, herbiers, bordures et postes d’embuscade.',rig:'Spinnerbait, shad ou jerkbait',bait:'Leurres 12–20 cm selon saison',line:'Avançon résistant aux dents (acier/titane)',period:'Conditions modérées, comportements variables',care:'Épuisette adaptée, pince, remise à l’eau rapide si choisie.'},
 {id:'carpe',name:'Carpe',latin:'Cyprinus carpio',env:'fresh',tech:['appats','bord'],depth:'1–6 m',approach:'Plateaux, bordures, zones calmes et passages.',rig:'Montage au cheveu ou feeder sécurisé',bait:'Maïs, pellets, bouillettes selon règlement',line:'Nylon ou tresse résistants adaptés au fond',period:'Longues sessions et observation importantes',care:'Tapis de réception humidifié et hameçon adapté.'},
 {id:'truite',name:'Truite',latin:'Salmo trutta',env:'fresh',tech:['mouche','leurres','bord'],depth:'0,3–2 m',approach:'Veines d’eau, radiers, blocs et fosses oxygénées.',rig:'Nymphe, toc, cuiller légère',bait:'Mouches, petits leurres adaptés',line:'Bas de ligne fin proportionné au courant',period:'Eau fraîche, périodes légales impératives',care:'Mains mouillées et exposition hors eau minimale.'},
 {id:'silure',name:'Silure',latin:'Silurus glanis',env:'fresh',tech:['leurres','appats','bateau'],depth:'3–15 m',approach:'Fosses, piles, zones profondes et grands courants.',rig:'Montage fort, leurre vertical ou au fond',bait:'Leurres robustes ou appâts légaux',line:'Tresse et hameçons haute résistance',period:'Activité variable selon température',care:'Sécuriser les manipulations des grands individus.'},
 {id:'blackbass',name:'Black-bass',latin:'Micropterus salmoides',env:'fresh',tech:['leurres','bord','bateau'],depth:'0,5–5 m',approach:'Bois immergé, herbiers, ombre et obstacles.',rig:'Texas rig, jig, topwater',bait:'Créatures souples, leurres de surface',line:'Bas de ligne selon structures',period:'À ajuster à l’activité observée',care:'Attention aux périodes de reproduction et aux règles locales.'},
 {id:'bar',name:'Bar / Loup',latin:'Dicentrarchus labrax',env:'sea',tech:['leurres','appats','bord','bateau'],depth:'0,5–20 m',approach:'Courants, écumes, roches, plages et estuaires.',rig:'Leurre souple, stickbait, surfcasting',bait:'Shad 10–15 cm, leurres de surface ou appâts autorisés',line:'Tresse PE 0.8–1.5 + fluoro selon fond',period:'Activité parfois liée aux changements de courant',care:'Tailles, quotas et période locales à vérifier.'},
 {id:'dorade',name:'Daurade royale',latin:'Sparus aurata',env:'sea',tech:['appats','bord','bateau'],depth:'1–30 m',approach:'Fonds mixtes, herbiers, bordures rocheuses.',rig:'Coulissant discret / montage fond',bait:'Crustacés et vers autorisés',line:'Fluorocarbone selon abrasivité',period:'Fenêtres variables suivant saison et météo',care:'Tailles et règles locales à vérifier.'},
 {id:'maquereau',name:'Maquereau',latin:'Scomber scombrus',env:'sea',tech:['leurres','bateau','bord'],depth:'0–40 m',approach:'Bancs mobiles, chasses, oiseaux plongeurs.',rig:'Petite mitraillette autorisée, jig ou cuiller',bait:'Jigs et plumes selon réglementation',line:'Tresse légère et empile adaptée',period:'Bancs très mobiles, présence non garantie',care:'Mettre rapidement au frais si conservé.'},
 {id:'lieu',name:'Lieu jaune',latin:'Pollachius pollachius',env:'sea',tech:['leurres','bateau'],depth:'5–80 m',approach:'Roches, laminaires, cassures, épaves accessibles.',rig:'Jig, shad animé dans le courant',bait:'Jig métallique et leurre souple',line:'Tresse + fluorocarbone résistant',period:'Courants adaptés à la technique',care:'Respecter tailles, zones et limitations locales.'},
 {id:'thon',name:'Thon rouge',latin:'Thunnus thynnus',env:'sea',tech:['bateau','leurres'],depth:'Surface–profondeur variable',approach:'Pélagique, fortes mobilités, détection en surface.',rig:'Matériel haut de gamme spécifique',bait:'Leurres de surface et jigs adaptés',line:'Ensembles puissants conformes au cadre local',period:'Fortement dépendant des mouvements de bancs',care:'Pêche soumise à autorisations et règles strictes selon pays.'}
];
window.FISHORA_TYPES=['Canne','Moulinet','Leurre','Fil / bas de ligne','Hameçon','Plomb','Appât','Électronique','Sécurité','Accessoire','Autre'];
window.FISHORA_ESSENTIALS=[
 {name:'Canne adaptée',type:'Canne',match:['Canne'],required:true},
 {name:'Moulinet',type:'Moulinet',match:['Moulinet'],required:true},
 {name:'Fil ou bas de ligne',type:'Fil / bas de ligne',match:['Fil / bas de ligne'],required:true},
 {name:'Leurre ou appât adapté',type:'Leurre / Appât',match:['Leurre','Appât'],required:true},
 {name:'Hameçons / montage',type:'Hameçon',match:['Hameçon','Accessoire'],required:true},
 {name:'Équipement de sécurité',type:'Sécurité',match:['Sécurité'],required:true},
 {name:'Pince de décrochage',type:'Accessoire',match:['Accessoire'],required:false}
];
window.FISHORA_SOURCES=[
 ['Prévisions météo','Open-Meteo','https://open-meteo.com/en/docs'],
 ['Prévisions marines','Open-Meteo Marine','https://open-meteo.com/en/docs/marine-weather-api'],
 ['Fond de carte','© OpenStreetMap contributors','https://www.openstreetmap.org/copyright'],
 ['Observations biologiques','iNaturalist (communauté)','https://www.inaturalist.org/'],
 ['Géocodage','Open-Meteo Geocoding','https://open-meteo.com/en/docs/geocoding-api'],
 ['Cartographie / points utiles','OpenStreetMap Overpass','https://wiki.openstreetmap.org/wiki/Overpass_API']
];
