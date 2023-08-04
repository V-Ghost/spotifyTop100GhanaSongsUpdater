import requests
import json
data = {
    "0": [
        "All My Life (feat. J. Cole)",
        "LilDurk"
    ],
    "1": [
        "Charm",
        "Rema"
    ],
    "2": [
        "Terminator",
        "KingPromise"
    ],
    "3": [
        "Into The Future",
        "Stonebwoy"
    ],
    "4": [
        "UNAVAILABLE (feat. Musa Keys)",
        "Davido"
    ],
    "5": [
        "FEEL",
        "Davido"
    ],
    "6": [
        "NO COMPETITION (feat. Asake)",
        "Davido"
    ],
    "7": [
        "Party No Dey Stop",
        "AdekunleGold,Zinoleesky"
    ],
    "8": [
        "Body & Soul",
        "Joeboy"
    ],
    "9": [
        "Life & Money (feat. Stormzy)",
        "Stonebwoy"
    ],
    "10": [
        "Soweto (feat. Don Toliver)",
        "Victony,Rema,Tempoe"
    ],
    "11": [
        "Butta My Bread (feat. Lasmid)",
        "JZyNO"
    ],
    "12": [
        "soso",
        "OmahLay"
    ],
    "13": [
        "Oh Ma Linda",
        "Reggie,O'Kenneth,JayBahd,KwakuDMC"
    ],
    "14": [
        "SCAR",
        "SongBird,Gyakie,JBEE"
    ],
    "15": [
        "Amapiano",
        "Asake,Olamide"
    ],
    "16": [
        "Duffel Bag",
        "Joeboy"
    ],
    "17": [
        "OVER DEM",
        "Davido"
    ],
    "18": [
        "PRAY",
        "BNXNfkaBuju"
    ],
    "19": [
        "AWAY",
        "Davido"
    ],
    "20": [
        "Aseda",
        "Nacee"
    ],
    "21": [
        "In Control (feat. Jaz Karis)",
        "Stonebwoy"
    ],
    "22": [
        "Holiday",
        "Rema"
    ],
    "23": [
        "Therapy (feat. Oxlade & Tiwa Savage)",
        "Stonebwoy"
    ],
    "24": [
        "Forget",
        "Stonebwoy"
    ],
    "25": [
        "Asiwaju",
        "Ruger"
    ],
    "26": [
        "Normally",
        "Joeboy,BNXNfkaBuju,ODUMODUBLVCK"
    ],
    "27": [
        "Konongo Zongo",
        "BlackSherif"
    ],
    "28": [
        "2:30",
        "Asake"
    ],
    "29": [
        "Stamina",
        "TiwaSavage,AyraStarr,YoungJonn"
    ],
    "30": [
        "Oil in my Head",
        "BlackSherif"
    ],
    "31": [
        "Aquafina",
        "YoungJonn"
    ],
    "32": [
        "Firm Foundation (He Wont) [feat. Chandler Moore & Cody Carnes]",
        "MaverickCityMusic"
    ],
    "33": [
        "More Of You",
        "Stonebwoy"
    ],
    "34": [
        "GWAGWALADA",
        "BNXNfkaBuju,KizzDaniel,SeyiVibez"
    ],
    "35": [
        "Rush",
        "AyraStarr"
    ],
    "36": [
        "45",
        "BlackSherif"
    ],
    "37": [
        "Xtra Cool",
        "YoungJonn"
    ],
    "38": [
        "Who Is Your Guy? (Remix)",
        "Spyro,TiwaSavage"
    ],
    "39": [
        "Far Away",
        "Stonebwoy"
    ],
    "40": [
        "KANTE (feat. Fave)",
        "Davido"
    ],
    "41": [
        "Secret Lover (feat. Dexta Daps)",
        "Stonebwoy"
    ],
    "42": [
        "Apotheke",
        "Stonebwoy,DJMaphorisa"
    ],
    "43": [
        "Bandana",
        "FireboyDML,Asake"
    ],
    "44": [
        "Last Last",
        "BurnaBoy"
    ],
    "45": [
        "Activate",
        "Stonebwoy,Davido"
    ],
    "46": [
        "Soja",
        "BlackSherif"
    ],
    "47": [
        "E PAIN ME",
        "Davido"
    ],
    "48": [
        "Terminator",
        "Asake"
    ],
    "49": [
        "NA MONEY (feat. The Cavemen. & Angelique Kidjo)",
        "Davido"
    ],
    "50": [
        "Ava Wum Lo",
        "Stonebwoy"
    ],
    "51": [
        "Sad Boys Don't Fold",
        "BlackSherif"
    ],
    "52": [
        "IN THE GARDEN (feat. Morravey)",
        "Davido"
    ],
    "53": [
        "Carry Me Go",
        "Khaid,BoySpyce"
    ],
    "54": [
        "Sability",
        "AyraStarr"
    ],
    "55": [
        "Believe Me",
        "JohnnyDrille"
    ],
    "56": [
        "Run AM (feat. Mereba)",
        "Stonebwoy"
    ],
    "57": [
        "The Homeless Song",
        "BlackSherif"
    ],
    "58": [
        "Wasteman",
        "BlackSherif"
    ],
    "59": [
        "GODFATHER",
        "Davido"
    ],
    "60": [
        "People (feat. Ayra Starr & Omah Lay)",
        "Libianca"
    ],
    "61": [
        "It's Plenty",
        "BurnaBoy"
    ],
    "62": [
        "Organise",
        "Asake"
    ],
    "63": [
        "Kwaku the Traveller",
        "BlackSherif"
    ],
    "64": [
        "Many Things",
        "Zinoleesky"
    ],
    "65": [
        "For My Hand (feat. Ed Sheeran)",
        "BurnaBoy"
    ],
    "66": [
        "Country Side (feat. Black Sherif)",
        "Sarkodie"
    ],
    "67": [
        "Prey Da Youngsta",
        "BlackSherif"
    ],
    "68": [
        "OVAMI",
        "Oxlade,Flavour"
    ],
    "69": [
        "Manodzi (feat. Angelique Kidjo)",
        "Stonebwoy"
    ],
    "70": [
        "Shu-Peru",
        "KizzDaniel"
    ],
    "71": [
        "soso",
        "OmahLay,Ozuna"
    ],
    "72": [
        "Toxic Love City",
        "BlackSherif"
    ],
    "73": [
        "Philo",
        "BellaShmurda,OmahLay"
    ],
    "74": [
        "My Sound (feat. Shaggy)",
        "Stonebwoy"
    ],
    "75": [
        "FOR THE ROAD",
        "Davido"
    ],
    "76": [
        "Jireh (feat. Chandler Moore & Naomi Raine)",
        "ElevationWorship,MaverickCityMusic"
    ],
    "77": [
        "iâm a mess",
        "OmahLay"
    ],
    "78": [
        "Real Life (feat. Stormzy)",
        "BurnaBoy"
    ],
    "79": [
        "Under the Influence",
        "ChrisBrown"
    ],
    "80": [
        "HALLELUJAH (feat. Blaqbonez)",
        "CKay"
    ],
    "81": [
        "Spirit Chant",
        "VictoriaOrenze"
    ],
    "82": [
        "Oh Paradise",
        "BlackSherif"
    ],
    "83": [
        "African System",
        "Stonebwoy"
    ],
    "84": [
        "KU LO SA - A COLORS SHOW",
        "Oxlade"
    ],
    "85": [
        "Ebelebe (feat. Wizkid)",
        "WandeCoal"
    ],
    "86": [
        "Electricity",
        "Pheelz,Davido"
    ],
    "87": [
        "Obaa Hemaa (feat. O'Kenneth, Reggie, Beeztrap Kotm, Kwaku DMC & Jay Bahd)",
        "SkyfaceSDW"
    ],
    "88": [
        "We Up",
        "BlackSherif"
    ],
    "89": [
        "Jabo (feat. Fireboy DML)",
        "WandeCoal"
    ],
    "90": [
        "Where Is The Love",
        "Stonebwoy"
    ],
    "91": [
        "Non-Stop",
        "Stonebwoy"
    ],
    "92": [
        "PRECISION",
        "Davido"
    ],
    "93": [
        "Joha",
        "Asake"
    ],
    "94": [
        "BOP (feat. Dexta Daps)",
        "Davido"
    ],
    "95": [
        "U (JUJU) [feat. Skepta]",
        "Davido"
    ],
    "96": [
        "Don't Forget Me",
        "BlackSherif"
    ],
    "97": [
        "I Will Pray",
        "EbukaSongs"
    ],
    "98": [
        "Second Sermon (Remix)",
        "BlackSherif,BurnaBoy"
    ],
    "99": [
        "Contour",
        "Joeboy"
    ]
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post('http://52.23.174.181:5000/', data=json.dumps(data), headers=headers)
print(response)