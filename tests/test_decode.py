import pytest

import src.pi5ir as pi5ir

test_vector = [
    # Chinese HDMI Switch (NEC procotol)
    [
        """9155 4470 635 500 635 500 615 530 635 500 665 475 611 554 635 475 635
    1620 630 1640 610 1615 610 1640 635 1635 585 1641 614 1635 640 1635 585
    525 665 475 635 505 610 555 585 1641 609 530 610 525 610 530 610 530 610
    1665 611 1609 615 1645 600 530 610 1665 585 1640 610 1640 610 1665 585
    39985 9125 2220 610 96355 9170 2245 590 96336 9189 2196 605""",
        [
            {
                "preamble": [16, 8],
                "coding": "ppm",
                "zero": [1, 1],
                "one": [1, 3],
                "byte_separator": None,
                "msb_first": False,
                "bits": 32,
                "data": b"\x80\x7f\x08\xf7",
                "postamble": [1],
                "timebase": 570,
                "gap": 96000,
            }
        ],
    ],
    # Panasonic Light (AEHA)
    [
        """3510 1710 465 400 465 400 465 1275 465 1270 465 400 491 1249 465 400 466
    400 464 405 470 1265 465 401 464 405 465 1270 466 399 465 1270 470 405 460
    1270 465 380 495 396 465 1269 466 399 470 401 464 400 465 400 466 1275 464
    400 465 1270 490 1250 465 400 465 1270 490 380 465 400 465 400 471 399 490
    1245 465 401 489 375 470 1270 465 400 465 405 490 74701 3510 1705 465 400
    499 371 490 1245 495 1245 465 400 494 1246 490 375 490 380 490 375 494 1241
    470 400 490 379 490 1250 486 375 490 1225 490 400 490 1245 495 375 490 375
    490 1250 490 375 465 400 491 379 490 375 490 1250 465 405 485 1245 490 1250
    490 375 490 1250 490 375 466 404 490 375 490 375 465 1280 485 375 490 380
    465 1270 490 375 490 380 490""",
        [
            {
                "preamble": [8, 4],
                "coding": "ppm",
                "zero": [1, 1],
                "one": [1, 3],
                "byte_separator": None,
                "msb_first": False,
                "bits": 40,
                "data": b",R\t-$",
                "postamble": [1],
                "timebase": 430,
                "gap": 75000,
            }
        ],
    ],
    # Hitach Air Conditioner (AEHA like)
    [
        """29820 49326 3400 1630 455 1220 450 385 480 360 450 395 445 385 450 385 
    450 390 450 390 450 385 450 385 475 365 475 360 450 1225 450 390 450 
    385 450 390 450 385 450 385 450 390 450 385 450 390 470 365 450 390 
    450 390 450 380 455 385 450 385 450 390 450 390 450 385 450 1225 450 
    390 475 1195 455 1220 450 1225 450 1225 450 1225 450 1225 450 385 450 
    1230 450 1220 475 1200 450 1225 475 1200 475 1200 450 1220 455 1220 
    450 1230 450 385 450 385 455 385 450 385 455 385 450 385 450 390 450 
    390 450 385 450 385 450 1225 450 1225 470 365 455 385 450 1225 450 
    1225 455 1220 475 1195 455 385 450 385 450 1225 475 1200 450 390 450 
    390 450 1220 450 1225 450 385 455 385 450 385 450 1225 480 360 450 
    1225 450 385 450 390 450 1225 450 1220 450 1225 450 390 450 1225 450 
    390 450 1220 450 1225 450 390 450 385 450 1225 450 385 450 390 450 390 
    450 385 450 385 450 1225 450 1225 450 385 455 1225 450 1220 450 1230 
    450 385 450 385 451 389 450 385 450 385 455 1220 455 1220 450 390 455 
    1220 450 1225 450 1220 455 1220 450 1225 450 390 450 385 450 1230 450 
    385 450 385 450 385 455 385 450 385 457 383 450 390 450 390 450 1220 
    450 1225 450 1225 476 1194 455 1225 450 1225 445 1225 450 1230 450 385 
    450 385 450 390 450 386 449 390 450 385 450 390 450 390 445 1225 450 
    1225 450 1220 455 1225 450 1226 444 1225 455 1222 473 1205 450 385 450 
    385 451 389 450 385 450 390 450 385 451 390 444 395 450 1220 455 1220 
    450 1225 450 1226 449 1220 455 1220 460 1215 450 1230 450 386 449 385 
    450 390 450 385 450 390 451 384 450 385 475 370 450 1220 450 1225 450 
    1225 452 1223 450 1225 450 1225 450 1220 450 1230 450 385 450 385 455 
    385 450 385 450 390 450 385 450 385 455 390 455 1215 450 1225 450 1220 
    455 1225 450 1225 450 1225 450 1225 445 1230 451 1219 455 1220 450 390 
    475 360 450 1225 450 385 451 1225 451 393 450 385 445 390 451 1225 454 
    1215 455 385 450 1230 446 389 445 1230 450 1221 449 395 450 380 450 
    391 449 1226 449 1225 450 1225 450 1225 450 385 450 1225 451 1225 444 
    1231 449 385 450 385 456 385 454 385 450 385 451 389 450 390 445 390 
    446 389 450 386 449 395 445 390 455 1215 450 1226 450 1224 450 1230 
    445 1226 454 1220 445 1230 455 1221 450 389 446 385 449 390 451 385 
    454 386 449 390 446 390 449 391 450 1220 454 1221 450 1225 450 1225 
    454 1225 450 1221 445 1230 449 1230 446 390 445 389 446 389 455 1221 
    450 385 450 390 445 394 446 1235 445 1220 450 1225 454 1221 450 385 
    454 1221 450 1225 450 1225 450 390 450 1219 455 1221 450 390 454 381 
    450 389 451 385 450 390 450 394 450 376 450 390 450 1225 449 1226 450 
    1225 450 1225 450 1225 450 1225 450 1220 450 390 450 385 450 390 450 
    389 471 365 450 385 450 395 450 380 450 1225 450 1225 450 1225 450 
    1225 450 1225 450 1220 455 1225 450 385 450 390 445 390 450 1225 450 
    385 450 390 450 385 450 1230 475 1195 450 1225 450 1225 450 385 450 
    1225 450 1225 450 1225 450 390 450 385 450 385 450 390 450 390 445 390 
    450 385 450 390 450 390 450 1220 450 1225 450 1225 450 1225 450 1225 
    450 1225 450 1225 445 1230 450 385 450 390 450 385 450 385 475 365 450 
    385 450 390 450 390 450 1220 450 1225 450 1225 450 1225 450 1225 450 
    1225 450 1225 445 1230 450 1225 445 1225 450 1230 445 1225 450 1225 
    450 1225 450 1225 450 1230 450 385 445 390 450 385 450 390 450 385 450 
    390 445 390 450 390 450 1220 450 1225 450 1225 450 1225 450 1225 450 
    1225 451 1224 450 1230 445 385 450 390 450 385 450 390 450 385 451 389 
    450 385 450 390 450 1221 449 1230 445 1225 450 1225 450 1225 450 1225 
    450 1225 450 1230 450 385 445 390 450 385 450 390 450 385 450 390 450 
    385 450 390 451 1224 445 1230 445 1225 450 1225 450 1225 450 1225 450 
    1226 449 1230 450 385 445 390 451 384 450 390 450 385 450 390 450 386 
    449 390 450""",
        [
            {
                "preamble": [8, 4],
                "coding": "ppm",
                "zero": [1, 1],
                "one": [1, 3],
                "byte_separator": None,
                "msb_first": False,
                "bits": 424,
                "data": b"\x01\x10\x00@\xbf\xff\x00\xcc3\xa3\\\x13\xec`\x9f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xffS\xac\xf1\x0e\x00\xff\x00\xff\x88w\x03\xfc\x01\xfe\x88w\x00\xff\x00\xff\xff\x00\xff\x00\xff\x00\xff\x00",
                "postamble": [1],
                "timebase": 420,
                "gap": 49000,
            }
        ],
    ],
    # Philips DVD (RC6)
    [
        """2705 800 495 780 495 355 495 365 1360 1215 495 350 495 355 495 350 495
    355 925 785 495 370 490 355 495 350 930 780 925 355 495 785 495 350 495
    88100 2705 805 495 785 495 355 495 370 1355 1220 490 360 490 350 495 350
    495 355 925 785 495 350 496 359 490 350 925 785 931 349 495 785 485 360
    495""",
        [
            {
                "preamble": [6, 2, 1, 1],
                "coding": "manchester",
                "zero": [0, 1],
                "one": [1, 0],
                "long_bit": 3,
                "msb_first": True,
                "bits": 20,
                "data": b"\x10B\xc0",
                "timebase": 420,
                "gap": 88000,
            }
        ],
    ],
    # Sony TV
    [
        """2435 550 1240 555 630 570 1231 544 631 564 1235 555 631 564 636 565 
    1235 555 635 565 639 555 635 555 631 26005 2435 560 1235 550 635 550 
    1235 555 635 565 1230 545 639 556 640 560 1239 551 635 550 635 560 640 
    560 635 26010 2430 575 1235 540 635 565 1235 555 635 550 1230 560 635 
    560 640 560 1235 540 635 565 635 560 635 565 660""",
        [
            {
                "preamble": [4],
                "coding": "ppm",
                "zero": [1, 1],
                "one": [1, 2],
                "byte_separator": None,
                "msb_first": False,
                "bits": 12,
                "data": b"\x95\x00",
                "postamble": [],
                "timebase": 600,
                "gap": 26000,
            }
        ],
    ],
    # Mitsubishi BD
    [
        """8320 4085 555 1505 555 445 580 465 555 455 555 1525 550 1530 550 1510 
    550 1525 555 4095 555 455 550 1530 550 470 555 450 555 470 555 470 550 
    470 555 450 555 22460 8320 4075 555 1520 555 470 555 450 555 470 555 
    1525 550 1510 555 1525 550 1510 555 4082 553 470 550 1510 555 470 555 
    470 555 465 556 449 555 470 555 455 550 22460 8321 4089 555 1505 555 
    470 550 475 550 470 555 1505 555 1525 550 1510 560 1520 550 4085 556 
    449 555 1525 555 465 555 475 550 455 550 470 555 470 550 455 555""",
        [
            {
                "preamble": [16, 8],
                "coding": "ppm",
                "zero": [1, 1],
                "one": [1, 3],
                "byte_separator": (1, 8),
                "msb_first": False,
                "bits": 16,
                "data": b"\xf1\x02",
                "postamble": [1],
                "timebase": 510,
                "gap": 22000,
            }
        ],
    ],
    # The following is taken (and slightly modified) from raw codes in
    # the LIRC remote database.
    # SHARP
    [
        """
              342    1789     324    1789     324     732
              327     728     322     733     328     768
              363     729     319     733     328    1784
              324     730     351    1765     327     728
              322     732     325    1788     320     733
              326
    """,
        [
            {
                "preamble": [],
                "coding": "ppm",
                "zero": [1, 2],
                "one": [1, 5],
                "byte_separator": None,
                "msb_first": False,
                "bits": 15,
                "data": b"\x03%",
                "postamble": [1],
                "timebase": 350,
                "gap": None,
            }
        ],
    ],
    # RC5
    [
        """
              955     842    1816    1728    1816    1727
             1817     842     930     843     927     843
              928    1729     929     842    1817     841
              930
    """,
        [
            {
                "preamble": [1],
                "coding": "manchester",
                "zero": [1, 0],
                "one": [0, 1],
                "long_bit": None,
                "msb_first": True,
                "bits": 13,
                "data": b"\xa8`",
                "timebase": 890,
                "gap": None,
            }
        ],
    ],
    # NOKIA
    [
        """
              569    2489     568     915    1062     429
              543     453     543     453     562     434
              570     427     543     453     543     453
              543     453     543     453     568     428
              568     428     543     454     543     453
              568     429     543   19825     570    2490
              542     941     568     428     567     429
              543     453     543     453     570     427
              542     454     543     453     568     429
             1037     947    1037     948     564     432
             1037     948     569
    """,
        [
            {
                "preamble": [1, 5, 1, 1],
                "coding": "manchester",
                "zero": [0, 1],
                "one": [1, 0],
                "long_bit": None,
                "msb_first": False,
                "bits": 16,
                "data": b"\xfe\xff",
                "timebase": 500,
                "gap": 20000,
            },
            {
                "preamble": [1, 5, 1, 1],
                "coding": "manchester",
                "zero": [0, 1],
                "one": [1, 0],
                "long_bit": None,
                "msb_first": False,
                "bits": 16,
                "data": b"\x00J",
                "timebase": 500,
                "gap": 20000,
            },
        ],
    ],
]


@pytest.mark.parametrize("pulses, expected", test_vector)
def test_decode(pulses, expected):
    pulses = [int(x) for x in pulses.strip().split()]
    decoded = pi5ir.decode(pulses)
    assert decoded == expected


@pytest.mark.parametrize("_, data", test_vector)
def test_encode(_, data):
    encoded = pi5ir.encode(data)
    decoded = pi5ir.decode(encoded)
    for a, b in zip(decoded, data):
        a["gap"] = b["gap"]
    assert decoded == data
