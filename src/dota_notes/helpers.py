import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def get_steam_live_game_stats(api_key, server_id):
    """Fetch game live information using the Steam WEB API and knowing the server the game is played on.
    Args:
        api_key: str Steam WEB API key
        server_id: int Server ID where the match is played
    """
    try:
        s = requests.Session()
        retries = Retry(total=8, backoff_jitter=1, status_forcelist=[400])
        s.mount("https://", HTTPAdapter(max_retries=retries))
        url = f"https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1/?key={api_key}&server_steam_id={str(server_id)}"
        response = s.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        return None


def exec_stratz_graphql_query(token: str, query: str):
    """Execute a graphql query on stratz endpoint.

    Args:
        token: Stratz auth bearer token
        query: query to execute
    """
    if token == "":
        return None

    try:
        s = requests.Session()
        retries = Retry(total=8, backoff_jitter=1, status_forcelist=[400, 403])
        s.mount("https://", HTTPAdapter(max_retries=retries))
        url = "https://api.stratz.com/graphql"
        response = s.get(url, headers={"Authorization": f"Bearer {token}"}, params={"query": query})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while executing stratz query: {e}")
        return None


def stratz_get_players_info(token: str, players: list[int]):
    """Request the information for target players using Stratz API

    Args:
        token: Stratz auth bearer token
        players: list of players to fetch
    Returns
        json of the http response or None if error
    """
    if len(players) == 0:
        return None
    player_queries = ""
    for player in players:
        player_queries = player_queries + f"p{player}:player(steamAccountId: {player}){{ ...playerProfile }}"
    full_query = f"""fragment playerProfile on PlayerType {{
                       steamAccountId
                       matchCount
                       performance {{
                         rank
                       }}
                       steamAccount {{
                         avatar
                         name
                         isAnonymous
                         dotaAccountLevel
                         smurfFlag
                         countryCode
                         proSteamAccount{{
                           name
                           position
                         }}
                       }}
                    }}
                    {{
                      {player_queries}
                    }}"""
    return exec_stratz_graphql_query(token, full_query)


def stratz_get_last_game(token: str, player: int):
    """Request the last game played by someone using Stratz

    Args:
        token: Stratz auth bearer token
        player: 32bit steam ID
    Returns
        json of the http response or None if error
    """
    if player == 0:
        return None
    query = f"""{{
                   player(steamAccountId: {player}){{
                     steamAccountId
                     matches(request: {{
                       orderBy: DESC
                       take: 1
                     }}) {{
                       id
                       players {{
                         steamAccount {{
                           id
                           avatar
                           name
                           dotaAccountLevel
                           smurfFlag
                           countryCode
                           proSteamAccount {{
                             name
                             position
                           }}  
                         }}
                       }}
                     }}
                   }}
                }}"""
    return exec_stratz_graphql_query(token, query)


def stratz_get_live_game(token: str, match_id: int):
    """Request the info of a live game using Stratz

    Args:
        token: Stratz auth bearer token
        match_id: live game match id
    Returns
        json of the http response or None if error
    """
    print(match_id)
    if match_id == 0:
        return None
    query = f"""{{
                  live {{
                    match(id: {match_id}) {{
                      matchId
                      players {{
                        steamAccount {{
                          id
                          avatar
                          dotaAccountLevel
                          smurfFlag
                          proSteamAccount {{
                            name
                            position
                          }}
                          countryCode
                          name
                          isAnonymous
                        }}
                      }}
                    }}
                  }}
                }}"""
    json = exec_stratz_graphql_query(token, query)
    if ("data" not in json
            or "live" not in json["data"]
            or "match" not in json["data"]["live"]
            or json["data"]["live"]["match"] is None):
        return None
    return json


ISO_3166_COUNTRIES = {
    "AF": "Afghanistan",
    "AX": "Åland Islands",
    "AL": "Albania",
    "DZ": "Algeria",
    "AS": "American Samoa",
    "AD": "Andorra",
    "AO": "Angola",
    "AI": "Anguilla",
    "AQ": "Antarctica",
    "AG": "Antigua and Barbuda",
    "AR": "Argentina",
    "AM": "Armenia",
    "AW": "Aruba",
    "AU": "Australia",
    "AT": "Austria",
    "AZ": "Azerbaijan",
    "BS": "Bahamas",
    "BH": "Bahrain",
    "BD": "Bangladesh",
    "BB": "Barbados",
    "BY": "Belarus",
    "BE": "Belgium",
    "BZ": "Belize",
    "BJ": "Benin",
    "BM": "Bermuda",
    "BT": "Bhutan",
    "BO": "Bolivia",
    "BQ": "Bonaire, Sint Eustatius and Saba",
    "BA": "Bosnia and Herzegovina",
    "BW": "Botswana",
    "BV": "Bouvet Island",
    "BR": "Brazil",
    "IO": "British Indian Ocean Territory",
    "BN": "Brunei Darussalam",
    "BG": "Bulgaria",
    "BF": "Burkina Faso",
    "BI": "Burundi",
    "CV": "Cabo Verde",
    "KH": "Cambodia",
    "CM": "Cameroon",
    "CA": "Canada",
    "KY": "Cayman Islands",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CL": "Chile",
    "CN": "China",
    "CX": "Christmas Island",
    "CC": "Cocos Islands",
    "CO": "Colombia",
    "KM": "Comoros",
    "CG": "Congo",
    "CD": "Congo, Democratic Republic of the",
    "CK": "Cook Islands",
    "CR": "Costa Rica",
    "CI": "Côte d'Ivoire",
    "HR": "Croatia",
    "CU": "Cuba",
    "CW": "Curaçao",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "DJ": "Djibouti",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "EC": "Ecuador",
    "EG": "Egypt",
    "SV": "El Salvador",
    "GQ": "Equatorial Guinea",
    "ER": "Eritrea",
    "EE": "Estonia",
    "SZ": "Eswatini",
    "ET": "Ethiopia",
    "FK": "Falkland Islands",
    "FO": "Faroe Islands",
    "FJ": "Fiji",
    "FI": "Finland",
    "FR": "France",
    "GF": "French Guiana",
    "PF": "French Polynesia",
    "TF": "French Southern Territories",
    "GA": "Gabon",
    "GM": "Gambia",
    "GE": "Georgia",
    "DE": "Germany",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GR": "Greece",
    "GL": "Greenland",
    "GD": "Grenada",
    "GP": "Guadeloupe",
    "GU": "Guam",
    "GT": "Guatemala",
    "GG": "Guernsey",
    "GN": "Guinea",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HT": "Haiti",
    "HM": "Heard Island and McDonald Islands",
    "VA": "Holy See",
    "HN": "Honduras",
    "HK": "Hong Kong",
    "HU": "Hungary",
    "IS": "Iceland",
    "IN": "India",
    "ID": "Indonesia",
    "IR": "Iran",
    "IQ": "Iraq",
    "IE": "Ireland",
    "IM": "Isle of Man",
    "IL": "Israel",
    "IT": "Italy",
    "JM": "Jamaica",
    "JP": "Japan",
    "JE": "Jersey",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "KE": "Kenya",
    "KI": "Kiribati",
    "KP": "Korea, Democratic People's Republic of",
    "KR": "Korea, Republic of",
    "KW": "Kuwait",
    "KG": "Kyrgyzstan",
    "LA": "Lao People's Democratic Republic",
    "LV": "Latvia",
    "LB": "Lebanon",
    "LS": "Lesotho",
    "LR": "Liberia",
    "LY": "Libya",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MO": "Macao",
    "MG": "Madagascar",
    "MW": "Malawi",
    "MY": "Malaysia",
    "MV": "Maldives",
    "ML": "Mali",
    "MT": "Malta",
    "MH": "Marshall Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "YT": "Mayotte",
    "MX": "Mexico",
    "FM": "Micronesia",
    "MD": "Moldova",
    "MC": "Monaco",
    "MN": "Mongolia",
    "ME": "Montenegro",
    "MS": "Montserrat",
    "MA": "Morocco",
    "MZ": "Mozambique",
    "MM": "Myanmar",
    "NA": "Namibia",
    "NR": "Nauru",
    "NP": "Nepal",
    "NL": "Netherlands",
    "NC": "New Caledonia",
    "NZ": "New Zealand",
    "NI": "Nicaragua",
    "NE": "Niger",
    "NG": "Nigeria",
    "NU": "Niue",
    "NF": "Norfolk Island",
    "MK": "North Macedonia",
    "MP": "Northern Mariana Islands",
    "NO": "Norway",
    "OM": "Oman",
    "PK": "Pakistan",
    "PW": "Palau",
    "PS": "Palestine",
    "PA": "Panama",
    "PG": "Papua New Guinea",
    "PY": "Paraguay",
    "PE": "Peru",
    "PH": "Philippines",
    "PN": "Pitcairn",
    "PL": "Poland",
    "PT": "Portugal",
    "PR": "Puerto Rico",
    "QA": "Qatar",
    "RE": "Réunion",
    "RO": "Romania",
    "RU": "Russian Federation",
    "RW": "Rwanda",
    "BL": "Saint Barthélemy",
    "SH": "Saint Helena",
    "KN": "Saint Kitts and Nevis",
    "LC": "Saint Lucia",
    "MF": "Saint Martin",
    "PM": "Saint Pierre and Miquelon",
    "VC": "Saint Vincent and the Grenadines",
    "WS": "Samoa",
    "SM": "San Marino",
    "ST": "Sao Tome and Principe",
    "SA": "Saudi Arabia",
    "SN": "Senegal",
    "RS": "Serbia",
    "SC": "Seychelles",
    "SL": "Sierra Leone",
    "SG": "Singapore",
    "SX": "Sint Maarten",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "SB": "Solomon Islands",
    "SO": "Somalia",
    "ZA": "South Africa",
    "GS": "South Georgia and the South Sandwich Islands",
    "SS": "South Sudan",
    "ES": "Spain",
    "LK": "Sri Lanka",
    "SD": "Sudan",
    "SR": "Suriname",
    "SJ": "Svalbard and Jan Mayen",
    "SE": "Sweden",
    "CH": "Switzerland",
    "SY": "Syrian Arab Republic",
    "TW": "Taiwan",
    "TJ": "Tajikistan",
    "TZ": "Tanzania",
    "TH": "Thailand",
    "TL": "Timor-Leste",
    "TG": "Togo",
    "TK": "Tokelau",
    "TO": "Tonga",
    "TT": "Trinidad and Tobago",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TM": "Turkmenistan",
    "TC": "Turks and Caicos Islands",
    "TV": "Tuvalu",
    "UG": "Uganda",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "GB": "United Kingdom",
    "US": "United States",
    "UM": "United States Minor Outlying Islands",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VU": "Vanuatu",
    "VE": "Venezuela",
    "VN": "Vietnam",
    "VG": "Virgin Islands, British",
    "VI": "Virgin Islands, U.S.",
    "WF": "Wallis and Futuna",
    "EH": "Western Sahara",
    "YE": "Yemen",
    "ZM": "Zambia",
    "ZW": "Zimbabwe"
}
