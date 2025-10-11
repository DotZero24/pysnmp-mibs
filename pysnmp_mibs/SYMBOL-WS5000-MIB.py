# SNMP MIB module (SYMBOL-WS5000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/symbol/SYMBOL-WS5000-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:50 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ccModuleId = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1000, 1)
)


# Types definitions



class DoActionNow(Integer32):
    """Custom type DoActionNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class MultiPointer63(Bits):
    """Custom type MultiPointer63 based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("referToEntry001", 1),
          ("referToEntry002", 2),
          ("referToEntry003", 3),
          ("referToEntry004", 4),
          ("referToEntry005", 5),
          ("referToEntry006", 6),
          ("referToEntry007", 7),
          ("referToEntry008", 8),
          ("referToEntry009", 9),
          ("referToEntry010", 10),
          ("referToEntry011", 11),
          ("referToEntry012", 12),
          ("referToEntry013", 13),
          ("referToEntry014", 14),
          ("referToEntry015", 15),
          ("referToEntry016", 16),
          ("referToEntry017", 17),
          ("referToEntry018", 18),
          ("referToEntry019", 19),
          ("referToEntry020", 20),
          ("referToEntry021", 21),
          ("referToEntry022", 22),
          ("referToEntry023", 23),
          ("referToEntry024", 24),
          ("referToEntry025", 25),
          ("referToEntry026", 26),
          ("referToEntry027", 27),
          ("referToEntry028", 28),
          ("referToEntry029", 29),
          ("referToEntry030", 30),
          ("referToEntry031", 31),
          ("referToEntry032", 32),
          ("referToEntry033", 33),
          ("referToEntry034", 34),
          ("referToEntry035", 35),
          ("referToEntry036", 36),
          ("referToEntry037", 37),
          ("referToEntry038", 38),
          ("referToEntry039", 39),
          ("referToEntry040", 40),
          ("referToEntry041", 41),
          ("referToEntry042", 42),
          ("referToEntry043", 43),
          ("referToEntry044", 44),
          ("referToEntry045", 45),
          ("referToEntry046", 46),
          ("referToEntry047", 47),
          ("referToEntry048", 48),
          ("referToEntry049", 49),
          ("referToEntry050", 50),
          ("referToEntry051", 51),
          ("referToEntry052", 52),
          ("referToEntry053", 53),
          ("referToEntry054", 54),
          ("referToEntry055", 55),
          ("referToEntry056", 56),
          ("referToEntry057", 57),
          ("referToEntry058", 58),
          ("referToEntry059", 59),
          ("referToEntry060", 60),
          ("referToEntry061", 61),
          ("referToEntry062", 62),
          ("referToEntry063", 63))
    )




class AbbrevRowStatus(Integer32):
    """Custom type AbbrevRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )





class PartsPer10k(Unsigned32):
    """Custom type PartsPer10k based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )





class Password(OctetString):
    """Custom type Password based on OctetString"""




class HexPassword(OctetString):
    """Custom type HexPassword based on OctetString"""




class RadioType(Integer32):
    """Custom type RadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("radio802dot11A", 1),
          ("radio802dot11B", 2),
          ("radio802dot11G", 3),
          ("radio802dot11FH", 4))
    )





class StaticRowEnable(Integer32):
    """Custom type StaticRowEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )





class MultiPointer255(Bits):
    """Custom type MultiPointer255 based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("referToEntry001", 1),
          ("referToEntry002", 2),
          ("referToEntry003", 3),
          ("referToEntry004", 4),
          ("referToEntry005", 5),
          ("referToEntry006", 6),
          ("referToEntry007", 7),
          ("referToEntry008", 8),
          ("referToEntry009", 9),
          ("referToEntry010", 10),
          ("referToEntry011", 11),
          ("referToEntry012", 12),
          ("referToEntry013", 13),
          ("referToEntry014", 14),
          ("referToEntry015", 15),
          ("referToEntry016", 16),
          ("referToEntry017", 17),
          ("referToEntry018", 18),
          ("referToEntry019", 19),
          ("referToEntry020", 20),
          ("referToEntry021", 21),
          ("referToEntry022", 22),
          ("referToEntry023", 23),
          ("referToEntry024", 24),
          ("referToEntry025", 25),
          ("referToEntry026", 26),
          ("referToEntry027", 27),
          ("referToEntry028", 28),
          ("referToEntry029", 29),
          ("referToEntry030", 30),
          ("referToEntry031", 31),
          ("referToEntry032", 32),
          ("referToEntry033", 33),
          ("referToEntry034", 34),
          ("referToEntry035", 35),
          ("referToEntry036", 36),
          ("referToEntry037", 37),
          ("referToEntry038", 38),
          ("referToEntry039", 39),
          ("referToEntry040", 40),
          ("referToEntry041", 41),
          ("referToEntry042", 42),
          ("referToEntry043", 43),
          ("referToEntry044", 44),
          ("referToEntry045", 45),
          ("referToEntry046", 46),
          ("referToEntry047", 47),
          ("referToEntry048", 48),
          ("referToEntry049", 49),
          ("referToEntry050", 50),
          ("referToEntry051", 51),
          ("referToEntry052", 52),
          ("referToEntry053", 53),
          ("referToEntry054", 54),
          ("referToEntry055", 55),
          ("referToEntry056", 56),
          ("referToEntry057", 57),
          ("referToEntry058", 58),
          ("referToEntry059", 59),
          ("referToEntry060", 60),
          ("referToEntry061", 61),
          ("referToEntry062", 62),
          ("referToEntry063", 63),
          ("referToEntry064", 64),
          ("referToEntry065", 65),
          ("referToEntry066", 66),
          ("referToEntry067", 67),
          ("referToEntry068", 68),
          ("referToEntry069", 69),
          ("referToEntry070", 70),
          ("referToEntry071", 71),
          ("referToEntry072", 72),
          ("referToEntry073", 73),
          ("referToEntry074", 74),
          ("referToEntry075", 75),
          ("referToEntry076", 76),
          ("referToEntry077", 77),
          ("referToEntry078", 78),
          ("referToEntry079", 79),
          ("referToEntry080", 80),
          ("referToEntry081", 81),
          ("referToEntry082", 82),
          ("referToEntry083", 83),
          ("referToEntry084", 84),
          ("referToEntry085", 85),
          ("referToEntry086", 86),
          ("referToEntry087", 87),
          ("referToEntry088", 88),
          ("referToEntry089", 89),
          ("referToEntry090", 90),
          ("referToEntry091", 91),
          ("referToEntry092", 92),
          ("referToEntry093", 93),
          ("referToEntry094", 94),
          ("referToEntry095", 95),
          ("referToEntry096", 96),
          ("referToEntry097", 97),
          ("referToEntry098", 98),
          ("referToEntry099", 99),
          ("referToEntry100", 100),
          ("referToEntry101", 101),
          ("referToEntry102", 102),
          ("referToEntry103", 103),
          ("referToEntry104", 104),
          ("referToEntry105", 105),
          ("referToEntry106", 106),
          ("referToEntry107", 107),
          ("referToEntry108", 108),
          ("referToEntry109", 109),
          ("referToEntry110", 110),
          ("referToEntry111", 111),
          ("referToEntry112", 112),
          ("referToEntry113", 113),
          ("referToEntry114", 114),
          ("referToEntry115", 115),
          ("referToEntry116", 116),
          ("referToEntry117", 117),
          ("referToEntry118", 118),
          ("referToEntry119", 119),
          ("referToEntry120", 120),
          ("referToEntry121", 121),
          ("referToEntry122", 122),
          ("referToEntry123", 123),
          ("referToEntry124", 124),
          ("referToEntry125", 125),
          ("referToEntry126", 126),
          ("referToEntry127", 127),
          ("referToEntry128", 128),
          ("referToEntry129", 129),
          ("referToEntry130", 130),
          ("referToEntry131", 131),
          ("referToEntry132", 132),
          ("referToEntry133", 133),
          ("referToEntry134", 134),
          ("referToEntry135", 135),
          ("referToEntry136", 136),
          ("referToEntry137", 137),
          ("referToEntry138", 138),
          ("referToEntry139", 139),
          ("referToEntry140", 140),
          ("referToEntry141", 141),
          ("referToEntry142", 142),
          ("referToEntry143", 143),
          ("referToEntry144", 144),
          ("referToEntry145", 145),
          ("referToEntry146", 146),
          ("referToEntry147", 147),
          ("referToEntry148", 148),
          ("referToEntry149", 149),
          ("referToEntry150", 150),
          ("referToEntry151", 151),
          ("referToEntry152", 152),
          ("referToEntry153", 153),
          ("referToEntry154", 154),
          ("referToEntry155", 155),
          ("referToEntry156", 156),
          ("referToEntry157", 157),
          ("referToEntry158", 158),
          ("referToEntry159", 159),
          ("referToEntry160", 160),
          ("referToEntry161", 161),
          ("referToEntry162", 162),
          ("referToEntry163", 163),
          ("referToEntry164", 164),
          ("referToEntry165", 165),
          ("referToEntry166", 166),
          ("referToEntry167", 167),
          ("referToEntry168", 168),
          ("referToEntry169", 169),
          ("referToEntry170", 170),
          ("referToEntry171", 171),
          ("referToEntry172", 172),
          ("referToEntry173", 173),
          ("referToEntry174", 174),
          ("referToEntry175", 175),
          ("referToEntry176", 176),
          ("referToEntry177", 177),
          ("referToEntry178", 178),
          ("referToEntry179", 179),
          ("referToEntry180", 180),
          ("referToEntry181", 181),
          ("referToEntry182", 182),
          ("referToEntry183", 183),
          ("referToEntry184", 184),
          ("referToEntry185", 185),
          ("referToEntry186", 186),
          ("referToEntry187", 187),
          ("referToEntry188", 188),
          ("referToEntry189", 189),
          ("referToEntry190", 190),
          ("referToEntry191", 191),
          ("referToEntry192", 192),
          ("referToEntry193", 193),
          ("referToEntry194", 194),
          ("referToEntry195", 195),
          ("referToEntry196", 196),
          ("referToEntry197", 197),
          ("referToEntry198", 198),
          ("referToEntry199", 199),
          ("referToEntry200", 200),
          ("referToEntry201", 201),
          ("referToEntry202", 202),
          ("referToEntry203", 203),
          ("referToEntry204", 204),
          ("referToEntry205", 205),
          ("referToEntry206", 206),
          ("referToEntry207", 207),
          ("referToEntry208", 208),
          ("referToEntry209", 209),
          ("referToEntry210", 210),
          ("referToEntry211", 211),
          ("referToEntry212", 212),
          ("referToEntry213", 213),
          ("referToEntry214", 214),
          ("referToEntry215", 215),
          ("referToEntry216", 216),
          ("referToEntry217", 217),
          ("referToEntry218", 218),
          ("referToEntry219", 219),
          ("referToEntry220", 220),
          ("referToEntry221", 221),
          ("referToEntry222", 222),
          ("referToEntry223", 223),
          ("referToEntry224", 224),
          ("referToEntry225", 225),
          ("referToEntry226", 226),
          ("referToEntry227", 227),
          ("referToEntry228", 228),
          ("referToEntry229", 229),
          ("referToEntry230", 230),
          ("referToEntry231", 231),
          ("referToEntry232", 232),
          ("referToEntry233", 233),
          ("referToEntry234", 234),
          ("referToEntry235", 235),
          ("referToEntry236", 236),
          ("referToEntry237", 237),
          ("referToEntry238", 238),
          ("referToEntry239", 239),
          ("referToEntry240", 240),
          ("referToEntry241", 241),
          ("referToEntry242", 242),
          ("referToEntry243", 243),
          ("referToEntry244", 244),
          ("referToEntry245", 245),
          ("referToEntry246", 246),
          ("referToEntry247", 247),
          ("referToEntry248", 248),
          ("referToEntry249", 249),
          ("referToEntry250", 250),
          ("referToEntry251", 251),
          ("referToEntry252", 252),
          ("referToEntry253", 253),
          ("referToEntry254", 254),
          ("referToEntry255", 255))
    )




class SinglePointer(Integer32):
    """Custom type SinglePointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class TransmitRate(Bits):
    """Custom type TransmitRate based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("rate1Mb", 1),
          ("rate2Mb", 2),
          ("rate5pt5Mb", 3),
          ("rate6Mb", 4),
          ("rate9Mb", 5),
          ("rate11Mb", 6),
          ("rate12Mb", 7),
          ("rate18Mb", 8),
          ("rate22Mb", 9),
          ("rate24Mb", 10),
          ("rate36Mb", 11),
          ("rate48Mb", 12),
          ("rate54Mb", 13))
    )




class DoActionShowProgress(Integer32):
    """Custom type DoActionShowProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class ScaleBy100(Unsigned32):
    """Custom type ScaleBy100 based on Unsigned32"""



# TEXTUAL-CONVENTIONS



class SnmpOpers(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("softkill", 0),
          ("hardkill", 1),
          ("restart", 2),
          ("updatecfg", 3))
    )



class TruthValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )



class FHAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ieee", 0),
          ("hopdelta", 1))
    )



class SnmpAdminString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class APOnlineStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("active", 1),
          ("inactive", 2),
          ("alert", 3),
          ("reset", 4))
    )



class EncrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("open", 1),
          ("wep40", 2),
          ("wep104", 4),
          ("keyguard", 8),
          ("tkip", 16),
          ("aesCcmp", 32))
    )



class MCValueOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("srcMacAddr", 0),
          ("desMacAddr", 1),
          ("etherType", 2),
          ("vlanID", 3),
          ("userPriority", 4),
          ("protocol", 5),
          ("tos", 6),
          ("srcIPAddr", 7),
          ("desIPAddr", 8),
          ("srcPort", 9),
          ("desPort", 10),
          ("multicastMask", 11))
    )



class HsbState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("startup", 1),
          ("findStandby", 2),
          ("waitingForConnectivity", 3),
          ("connected", 4),
          ("halted", 5),
          ("monitoring", 6),
          ("actingAsPrimary", 7),
          ("tryingtoReconnect", 8),
          ("reconnected", 9),
          ("autoreverting", 10))
    )



class MUDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 0),
          ("voice", 1),
          ("wirelessAP", 2))
    )



class APStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("away", 0),
          ("associated", 1))
    )



class MUSecurityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noEncryption", 0),
          ("wepPerMUKey", 1),
          ("wepSharedKey", 2),
          ("tkipPerMUKey", 3),
          ("tkipSharedKey", 4))
    )



class CurrentRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rt1Mbps", 0),
          ("rt2Mbps", 1),
          ("rt55Mbps", 2),
          ("rt11Mbps", 3))
    )



class SupportedRates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rt1Mbps", 1),
          ("rt2Mbps", 2),
          ("rt1and2Mbps", 3),
          ("rt55Mbps", 4),
          ("rt1and55Mbps", 5),
          ("rt2and55Mbps", 6),
          ("rt1and2and55Mbps", 7),
          ("rt11Mbps", 8),
          ("rt1and11Mbps", 9),
          ("rt2and11Mbps", 10),
          ("rt1and2and11Mbps", 11),
          ("rt55and11Mbps", 12),
          ("rt1and55and11Mbps", 13),
          ("rt2and55and11Mbps", 14),
          ("rt1and2and55and11Mbps", 15))
    )



class PSPowerMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cam", 0),
          ("psp", 1))
    )



class AuthState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notauthenticated", 0),
          ("authenticated", 1))
    )



class AuthMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("open", 1),
          ("preshared", 2),
          ("eap8021x", 4),
          ("kerberos", 8))
    )



class StorageType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("volatile", 2),
          ("nonVolatile", 3),
          ("permanent", 4),
          ("readOnly", 5))
    )



class RowStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )



class TargetOptions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



# MIB Managed Objects in the order of their OIDs

_Symbol_ObjectIdentity = ObjectIdentity
symbol = _Symbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388)
)
_SymbolCC_ObjectIdentity = ObjectIdentity
symbolCC = _SymbolCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6)
)
_Ws5000_ObjectIdentity = ObjectIdentity
ws5000 = _Ws5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 0)
)
if mibBuilder.loadTexts:
    ws5000.setStatus("current")
_Ws5100_ObjectIdentity = ObjectIdentity
ws5100 = _Ws5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 0, 1)
)
if mibBuilder.loadTexts:
    ws5100.setStatus("current")
_SymbolCCSystem_ObjectIdentity = ObjectIdentity
symbolCCSystem = _SymbolCCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1)
)
_CcSysCfg_ObjectIdentity = ObjectIdentity
ccSysCfg = _CcSysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1)
)


class _CcModuleName_Type(DisplayString):
    """Custom type ccModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcModuleName_Type.__name__ = "DisplayString"
_CcModuleName_Object = MibScalar
ccModuleName = _CcModuleName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 1),
    _CcModuleName_Type()
)
ccModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccModuleName.setStatus("current")


class _CcModuleDesc_Type(DisplayString):
    """Custom type ccModuleDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcModuleDesc_Type.__name__ = "DisplayString"
_CcModuleDesc_Object = MibScalar
ccModuleDesc = _CcModuleDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 2),
    _CcModuleDesc_Type()
)
ccModuleDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccModuleDesc.setStatus("current")


class _CcManufacture_Type(DisplayString):
    """Custom type ccManufacture based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcManufacture_Type.__name__ = "DisplayString"
_CcManufacture_Object = MibScalar
ccManufacture = _CcManufacture_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 3),
    _CcManufacture_Type()
)
ccManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccManufacture.setStatus("current")


class _CcCopyright_Type(DisplayString):
    """Custom type ccCopyright based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcCopyright_Type.__name__ = "DisplayString"
_CcCopyright_Object = MibScalar
ccCopyright = _CcCopyright_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 4),
    _CcCopyright_Type()
)
ccCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyright.setStatus("current")


class _CcModuleVer_Type(DisplayString):
    """Custom type ccModuleVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcModuleVer_Type.__name__ = "DisplayString"
_CcModuleVer_Object = MibScalar
ccModuleVer = _CcModuleVer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 5),
    _CcModuleVer_Type()
)
ccModuleVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccModuleVer.setStatus("current")


class _CcMaxNumAP_Type(Integer32):
    """Custom type ccMaxNumAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CcMaxNumAP_Type.__name__ = "Integer32"
_CcMaxNumAP_Object = MibScalar
ccMaxNumAP = _CcMaxNumAP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 6),
    _CcMaxNumAP_Type()
)
ccMaxNumAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMaxNumAP.setStatus("current")


class _CcMaxNumMu_Type(Integer32):
    """Custom type ccMaxNumMu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CcMaxNumMu_Type.__name__ = "Integer32"
_CcMaxNumMu_Object = MibScalar
ccMaxNumMu = _CcMaxNumMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 7),
    _CcMaxNumMu_Type()
)
ccMaxNumMu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMaxNumMu.setStatus("current")


class _CcActivePolicy_Type(DisplayString):
    """Custom type ccActivePolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcActivePolicy_Type.__name__ = "DisplayString"
_CcActivePolicy_Object = MibScalar
ccActivePolicy = _CcActivePolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 8),
    _CcActivePolicy_Type()
)
ccActivePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccActivePolicy.setStatus("current")


class _CcTaf_Type(DisplayString):
    """Custom type ccTaf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcTaf_Type.__name__ = "DisplayString"
_CcTaf_Object = MibScalar
ccTaf = _CcTaf_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 9),
    _CcTaf_Type()
)
ccTaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTaf.setStatus("current")
_CcSnmpOpers_Type = SnmpOpers
_CcSnmpOpers_Object = MibScalar
ccSnmpOpers = _CcSnmpOpers_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 10),
    _CcSnmpOpers_Type()
)
ccSnmpOpers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpOpers.setStatus("current")


class _CcUptime_Type(DisplayString):
    """Custom type ccUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcUptime_Type.__name__ = "DisplayString"
_CcUptime_Object = MibScalar
ccUptime = _CcUptime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 11),
    _CcUptime_Type()
)
ccUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccUptime.setStatus("current")
_CcFTP_Type = TruthValue
_CcFTP_Object = MibScalar
ccFTP = _CcFTP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 12),
    _CcFTP_Type()
)
ccFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFTP.setStatus("current")
_CcTelnet_Type = TruthValue
_CcTelnet_Object = MibScalar
ccTelnet = _CcTelnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 13),
    _CcTelnet_Type()
)
ccTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTelnet.setStatus("current")


class _CcWeb_Type(DisplayString):
    """Custom type ccWeb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_CcWeb_Type.__name__ = "DisplayString"
_CcWeb_Object = MibScalar
ccWeb = _CcWeb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 14),
    _CcWeb_Type()
)
ccWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWeb.setStatus("current")
_CcSNMPFlag_Type = TruthValue
_CcSNMPFlag_Object = MibScalar
ccSNMPFlag = _CcSNMPFlag_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 15),
    _CcSNMPFlag_Type()
)
ccSNMPFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSNMPFlag.setStatus("current")


class _CcTime_Type(DisplayString):
    """Custom type ccTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 30),
    )


_CcTime_Type.__name__ = "DisplayString"
_CcTime_Object = MibScalar
ccTime = _CcTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 16),
    _CcTime_Type()
)
ccTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTime.setStatus("current")
_CcSNMPKdc_Type = TruthValue
_CcSNMPKdc_Object = MibScalar
ccSNMPKdc = _CcSNMPKdc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 17),
    _CcSNMPKdc_Type()
)
ccSNMPKdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSNMPKdc.setStatus("current")
_CcCliKdc_Type = TruthValue
_CcCliKdc_Object = MibScalar
ccCliKdc = _CcCliKdc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 18),
    _CcCliKdc_Type()
)
ccCliKdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCliKdc.setStatus("current")


class _CcPolicyAddObj_Type(DisplayString):
    """Custom type ccPolicyAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPolicyAddObj_Type.__name__ = "DisplayString"
_CcPolicyAddObj_Object = MibScalar
ccPolicyAddObj = _CcPolicyAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 19),
    _CcPolicyAddObj_Type()
)
ccPolicyAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyAddObj.setStatus("current")


class _CcPolicyRemObj_Type(DisplayString):
    """Custom type ccPolicyRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPolicyRemObj_Type.__name__ = "DisplayString"
_CcPolicyRemObj_Object = MibScalar
ccPolicyRemObj = _CcPolicyRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 20),
    _CcPolicyRemObj_Type()
)
ccPolicyRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyRemObj.setStatus("current")
_CcLicenseCount_Type = Integer32
_CcLicenseCount_Object = MibScalar
ccLicenseCount = _CcLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 23),
    _CcLicenseCount_Type()
)
ccLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLicenseCount.setStatus("current")


class _CcEmergencyPolicy_Type(DisplayString):
    """Custom type ccEmergencyPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CcEmergencyPolicy_Type.__name__ = "DisplayString"
_CcEmergencyPolicy_Object = MibScalar
ccEmergencyPolicy = _CcEmergencyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 24),
    _CcEmergencyPolicy_Type()
)
ccEmergencyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEmergencyPolicy.setStatus("current")
_CcEmergencyMode_Type = TruthValue
_CcEmergencyMode_Object = MibScalar
ccEmergencyMode = _CcEmergencyMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 25),
    _CcEmergencyMode_Type()
)
ccEmergencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEmergencyMode.setStatus("current")
_CcRunACS_Type = TruthValue
_CcRunACS_Object = MibScalar
ccRunACS = _CcRunACS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 26),
    _CcRunACS_Type()
)
ccRunACS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRunACS.setStatus("current")
_CcEnableSNMPTrap_Type = TruthValue
_CcEnableSNMPTrap_Object = MibScalar
ccEnableSNMPTrap = _CcEnableSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 27),
    _CcEnableSNMPTrap_Type()
)
ccEnableSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEnableSNMPTrap.setStatus("current")
_CcEnableWVPNSupport_Type = OctetString
_CcEnableWVPNSupport_Object = MibScalar
ccEnableWVPNSupport = _CcEnableWVPNSupport_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 28),
    _CcEnableWVPNSupport_Type()
)
ccEnableWVPNSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEnableWVPNSupport.setStatus("current")
_CcEnableRap_Type = TruthValue
_CcEnableRap_Object = MibScalar
ccEnableRap = _CcEnableRap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 29),
    _CcEnableRap_Type()
)
ccEnableRap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEnableRap.setStatus("current")


class _CcAPTxPPS_Type(Integer32):
    """Custom type ccAPTxPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAPTxPPS_Type.__name__ = "Integer32"
_CcAPTxPPS_Object = MibScalar
ccAPTxPPS = _CcAPTxPPS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 30),
    _CcAPTxPPS_Type()
)
ccAPTxPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAPTxPPS.setStatus("current")


class _CcAPRxPPS_Type(Integer32):
    """Custom type ccAPRxPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAPRxPPS_Type.__name__ = "Integer32"
_CcAPRxPPS_Object = MibScalar
ccAPRxPPS = _CcAPRxPPS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 31),
    _CcAPRxPPS_Type()
)
ccAPRxPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAPRxPPS.setStatus("current")


class _CcAvgTxRetry_Type(Integer32):
    """Custom type ccAvgTxRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAvgTxRetry_Type.__name__ = "Integer32"
_CcAvgTxRetry_Object = MibScalar
ccAvgTxRetry = _CcAvgTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 32),
    _CcAvgTxRetry_Type()
)
ccAvgTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAvgTxRetry.setStatus("current")


class _CcAvgRSSI_Type(Integer32):
    """Custom type ccAvgRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAvgRSSI_Type.__name__ = "Integer32"
_CcAvgRSSI_Object = MibScalar
ccAvgRSSI = _CcAvgRSSI_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 33),
    _CcAvgRSSI_Type()
)
ccAvgRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAvgRSSI.setStatus("current")


class _CcAvgSNR_Type(Integer32):
    """Custom type ccAvgSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAvgSNR_Type.__name__ = "Integer32"
_CcAvgSNR_Object = MibScalar
ccAvgSNR = _CcAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 34),
    _CcAvgSNR_Type()
)
ccAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAvgSNR.setStatus("current")
_CcConfigChangeLast_Type = DisplayString
_CcConfigChangeLast_Object = MibScalar
ccConfigChangeLast = _CcConfigChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 49),
    _CcConfigChangeLast_Type()
)
ccConfigChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccConfigChangeLast.setStatus("current")
_CcNTP_ObjectIdentity = ObjectIdentity
ccNTP = _CcNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 60)
)
_CcNtpPrefTimeServer_Type = IpAddress
_CcNtpPrefTimeServer_Object = MibScalar
ccNtpPrefTimeServer = _CcNtpPrefTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 60, 1),
    _CcNtpPrefTimeServer_Type()
)
ccNtpPrefTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpPrefTimeServer.setStatus("current")
_CcNtpFirstAltTimeServer_Type = IpAddress
_CcNtpFirstAltTimeServer_Object = MibScalar
ccNtpFirstAltTimeServer = _CcNtpFirstAltTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 60, 2),
    _CcNtpFirstAltTimeServer_Type()
)
ccNtpFirstAltTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpFirstAltTimeServer.setStatus("current")
_CcNtpSecondAltTimeServer_Type = IpAddress
_CcNtpSecondAltTimeServer_Object = MibScalar
ccNtpSecondAltTimeServer = _CcNtpSecondAltTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 60, 3),
    _CcNtpSecondAltTimeServer_Type()
)
ccNtpSecondAltTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpSecondAltTimeServer.setStatus("current")
_CcNtpGroupSetTimeServer_Type = DisplayString
_CcNtpGroupSetTimeServer_Object = MibScalar
ccNtpGroupSetTimeServer = _CcNtpGroupSetTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 60, 4),
    _CcNtpGroupSetTimeServer_Type()
)
ccNtpGroupSetTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpGroupSetTimeServer.setStatus("current")
_CcNtpDelAll_Type = TruthValue
_CcNtpDelAll_Object = MibScalar
ccNtpDelAll = _CcNtpDelAll_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 1, 60, 5),
    _CcNtpDelAll_Type()
)
ccNtpDelAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpDelAll.setStatus("current")
_CcPolicyTable_Object = MibTable
ccPolicyTable = _CcPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ccPolicyTable.setStatus("current")
_CcPolicyEntry_Object = MibTableRow
ccPolicyEntry = _CcPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1)
)
ccPolicyEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPolicyIndex"),
)
if mibBuilder.loadTexts:
    ccPolicyEntry.setStatus("current")


class _CcPolicyIndex_Type(Integer32):
    """Custom type ccPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcPolicyIndex_Type.__name__ = "Integer32"
_CcPolicyIndex_Object = MibTableColumn
ccPolicyIndex = _CcPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 1),
    _CcPolicyIndex_Type()
)
ccPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccPolicyIndex.setStatus("current")


class _CcPolicyName_Type(DisplayString):
    """Custom type ccPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPolicyName_Type.__name__ = "DisplayString"
_CcPolicyName_Object = MibTableColumn
ccPolicyName = _CcPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 2),
    _CcPolicyName_Type()
)
ccPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyName.setStatus("current")


class _CcPolicyDesc_Type(DisplayString):
    """Custom type ccPolicyDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcPolicyDesc_Type.__name__ = "DisplayString"
_CcPolicyDesc_Object = MibTableColumn
ccPolicyDesc = _CcPolicyDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 3),
    _CcPolicyDesc_Type()
)
ccPolicyDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDesc.setStatus("current")


class _CcPolicyCountry_Type(DisplayString):
    """Custom type ccPolicyCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CcPolicyCountry_Type.__name__ = "DisplayString"
_CcPolicyCountry_Object = MibTableColumn
ccPolicyCountry = _CcPolicyCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 4),
    _CcPolicyCountry_Type()
)
ccPolicyCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyCountry.setStatus("current")


class _CcPolicyDefAdoptAPPolicy_Type(DisplayString):
    """Custom type ccPolicyDefAdoptAPPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcPolicyDefAdoptAPPolicy_Type.__name__ = "DisplayString"
_CcPolicyDefAdoptAPPolicy_Object = MibTableColumn
ccPolicyDefAdoptAPPolicy = _CcPolicyDefAdoptAPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 5),
    _CcPolicyDefAdoptAPPolicy_Type()
)
ccPolicyDefAdoptAPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefAdoptAPPolicy.setStatus("deprecated")


class _CcPolicyAPPolicyCount_Type(Integer32):
    """Custom type ccPolicyAPPolicyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcPolicyAPPolicyCount_Type.__name__ = "Integer32"
_CcPolicyAPPolicyCount_Object = MibTableColumn
ccPolicyAPPolicyCount = _CcPolicyAPPolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 6),
    _CcPolicyAPPolicyCount_Type()
)
ccPolicyAPPolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPolicyAPPolicyCount.setStatus("current")


class _CcPolicyAPNameOfPolicy_Type(DisplayString):
    """Custom type ccPolicyAPNameOfPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcPolicyAPNameOfPolicy_Type.__name__ = "DisplayString"
_CcPolicyAPNameOfPolicy_Object = MibTableColumn
ccPolicyAPNameOfPolicy = _CcPolicyAPNameOfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 7),
    _CcPolicyAPNameOfPolicy_Type()
)
ccPolicyAPNameOfPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPolicyAPNameOfPolicy.setStatus("current")


class _CcPolicyAddAPPolicy_Type(DisplayString):
    """Custom type ccPolicyAddAPPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPolicyAddAPPolicy_Type.__name__ = "DisplayString"
_CcPolicyAddAPPolicy_Object = MibTableColumn
ccPolicyAddAPPolicy = _CcPolicyAddAPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 8),
    _CcPolicyAddAPPolicy_Type()
)
ccPolicyAddAPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyAddAPPolicy.setStatus("current")


class _CcPolicyRmvAPPolicy_Type(DisplayString):
    """Custom type ccPolicyRmvAPPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPolicyRmvAPPolicy_Type.__name__ = "DisplayString"
_CcPolicyRmvAPPolicy_Object = MibTableColumn
ccPolicyRmvAPPolicy = _CcPolicyRmvAPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 9),
    _CcPolicyRmvAPPolicy_Type()
)
ccPolicyRmvAPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyRmvAPPolicy.setStatus("current")


class _CcPolicyExcludeInfo_Type(DisplayString):
    """Custom type ccPolicyExcludeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CcPolicyExcludeInfo_Type.__name__ = "DisplayString"
_CcPolicyExcludeInfo_Object = MibTableColumn
ccPolicyExcludeInfo = _CcPolicyExcludeInfo_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 10),
    _CcPolicyExcludeInfo_Type()
)
ccPolicyExcludeInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyExcludeInfo.setStatus("current")


class _CcPolicyExcludeEdit_Type(DisplayString):
    """Custom type ccPolicyExcludeEdit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CcPolicyExcludeEdit_Type.__name__ = "DisplayString"
_CcPolicyExcludeEdit_Object = MibTableColumn
ccPolicyExcludeEdit = _CcPolicyExcludeEdit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 11),
    _CcPolicyExcludeEdit_Type()
)
ccPolicyExcludeEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyExcludeEdit.setStatus("current")


class _CcPolicyExcludeRmv_Type(DisplayString):
    """Custom type ccPolicyExcludeRmv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CcPolicyExcludeRmv_Type.__name__ = "DisplayString"
_CcPolicyExcludeRmv_Object = MibTableColumn
ccPolicyExcludeRmv = _CcPolicyExcludeRmv_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 12),
    _CcPolicyExcludeRmv_Type()
)
ccPolicyExcludeRmv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyExcludeRmv.setStatus("current")


class _CcPolicyIncludeInfo_Type(DisplayString):
    """Custom type ccPolicyIncludeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CcPolicyIncludeInfo_Type.__name__ = "DisplayString"
_CcPolicyIncludeInfo_Object = MibTableColumn
ccPolicyIncludeInfo = _CcPolicyIncludeInfo_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 13),
    _CcPolicyIncludeInfo_Type()
)
ccPolicyIncludeInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyIncludeInfo.setStatus("current")


class _CcPolicyIncludeEdit_Type(DisplayString):
    """Custom type ccPolicyIncludeEdit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 225),
    )


_CcPolicyIncludeEdit_Type.__name__ = "DisplayString"
_CcPolicyIncludeEdit_Object = MibTableColumn
ccPolicyIncludeEdit = _CcPolicyIncludeEdit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 14),
    _CcPolicyIncludeEdit_Type()
)
ccPolicyIncludeEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyIncludeEdit.setStatus("current")


class _CcPolicyIncludeRmv_Type(DisplayString):
    """Custom type ccPolicyIncludeRmv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CcPolicyIncludeRmv_Type.__name__ = "DisplayString"
_CcPolicyIncludeRmv_Object = MibTableColumn
ccPolicyIncludeRmv = _CcPolicyIncludeRmv_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 15),
    _CcPolicyIncludeRmv_Type()
)
ccPolicyIncludeRmv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyIncludeRmv.setStatus("current")


class _CcPolicyEtherPolicy_Type(DisplayString):
    """Custom type ccPolicyEtherPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcPolicyEtherPolicy_Type.__name__ = "DisplayString"
_CcPolicyEtherPolicy_Object = MibTableColumn
ccPolicyEtherPolicy = _CcPolicyEtherPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 16),
    _CcPolicyEtherPolicy_Type()
)
ccPolicyEtherPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyEtherPolicy.setStatus("current")
_CcPolicyTrap_Type = TruthValue
_CcPolicyTrap_Object = MibTableColumn
ccPolicyTrap = _CcPolicyTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 17),
    _CcPolicyTrap_Type()
)
ccPolicyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyTrap.setStatus("current")


class _CcPolicyDefChannel_Type(Integer32):
    """Custom type ccPolicyDefChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CcPolicyDefChannel_Type.__name__ = "Integer32"
_CcPolicyDefChannel_Object = MibTableColumn
ccPolicyDefChannel = _CcPolicyDefChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 18),
    _CcPolicyDefChannel_Type()
)
ccPolicyDefChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefChannel.setStatus("deprecated")


class _CcPolicyDefPower_Type(Integer32):
    """Custom type ccPolicyDefPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcPolicyDefPower_Type.__name__ = "Integer32"
_CcPolicyDefPower_Object = MibTableColumn
ccPolicyDefPower = _CcPolicyDefPower_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 19),
    _CcPolicyDefPower_Type()
)
ccPolicyDefPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefPower.setStatus("deprecated")


class _CcPolicyChannel11a_Type(DisplayString):
    """Custom type ccPolicyChannel11a based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcPolicyChannel11a_Type.__name__ = "DisplayString"
_CcPolicyChannel11a_Object = MibTableColumn
ccPolicyChannel11a = _CcPolicyChannel11a_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 20),
    _CcPolicyChannel11a_Type()
)
ccPolicyChannel11a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyChannel11a.setStatus("current")


class _CcPolicyPower11a_Type(DisplayString):
    """Custom type ccPolicyPower11a based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcPolicyPower11a_Type.__name__ = "DisplayString"
_CcPolicyPower11a_Object = MibTableColumn
ccPolicyPower11a = _CcPolicyPower11a_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 21),
    _CcPolicyPower11a_Type()
)
ccPolicyPower11a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyPower11a.setStatus("current")


class _CcPolicyChannel11b_Type(DisplayString):
    """Custom type ccPolicyChannel11b based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcPolicyChannel11b_Type.__name__ = "DisplayString"
_CcPolicyChannel11b_Object = MibTableColumn
ccPolicyChannel11b = _CcPolicyChannel11b_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 22),
    _CcPolicyChannel11b_Type()
)
ccPolicyChannel11b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyChannel11b.setStatus("current")


class _CcPolicyPower11b_Type(DisplayString):
    """Custom type ccPolicyPower11b based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcPolicyPower11b_Type.__name__ = "DisplayString"
_CcPolicyPower11b_Object = MibTableColumn
ccPolicyPower11b = _CcPolicyPower11b_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 23),
    _CcPolicyPower11b_Type()
)
ccPolicyPower11b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyPower11b.setStatus("current")
_CcPolicyDSCoExistence_Type = TruthValue
_CcPolicyDSCoExistence_Object = MibTableColumn
ccPolicyDSCoExistence = _CcPolicyDSCoExistence_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 24),
    _CcPolicyDSCoExistence_Type()
)
ccPolicyDSCoExistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDSCoExistence.setStatus("current")


class _CcPolicyDefAdoptAPPolicy11a_Type(DisplayString):
    """Custom type ccPolicyDefAdoptAPPolicy11a based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CcPolicyDefAdoptAPPolicy11a_Type.__name__ = "DisplayString"
_CcPolicyDefAdoptAPPolicy11a_Object = MibTableColumn
ccPolicyDefAdoptAPPolicy11a = _CcPolicyDefAdoptAPPolicy11a_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 25),
    _CcPolicyDefAdoptAPPolicy11a_Type()
)
ccPolicyDefAdoptAPPolicy11a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefAdoptAPPolicy11a.setStatus("current")


class _CcPolicyDefAdoptAPPolicy11b_Type(DisplayString):
    """Custom type ccPolicyDefAdoptAPPolicy11b based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CcPolicyDefAdoptAPPolicy11b_Type.__name__ = "DisplayString"
_CcPolicyDefAdoptAPPolicy11b_Object = MibTableColumn
ccPolicyDefAdoptAPPolicy11b = _CcPolicyDefAdoptAPPolicy11b_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 26),
    _CcPolicyDefAdoptAPPolicy11b_Type()
)
ccPolicyDefAdoptAPPolicy11b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefAdoptAPPolicy11b.setStatus("current")


class _CcPolicyDefAdoptAPPolicyFH_Type(DisplayString):
    """Custom type ccPolicyDefAdoptAPPolicyFH based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CcPolicyDefAdoptAPPolicyFH_Type.__name__ = "DisplayString"
_CcPolicyDefAdoptAPPolicyFH_Object = MibTableColumn
ccPolicyDefAdoptAPPolicyFH = _CcPolicyDefAdoptAPPolicyFH_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 27),
    _CcPolicyDefAdoptAPPolicyFH_Type()
)
ccPolicyDefAdoptAPPolicyFH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefAdoptAPPolicyFH.setStatus("current")


class _CcPolicyDefAdoptAPPolicy11g_Type(DisplayString):
    """Custom type ccPolicyDefAdoptAPPolicy11g based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CcPolicyDefAdoptAPPolicy11g_Type.__name__ = "DisplayString"
_CcPolicyDefAdoptAPPolicy11g_Object = MibTableColumn
ccPolicyDefAdoptAPPolicy11g = _CcPolicyDefAdoptAPPolicy11g_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 28),
    _CcPolicyDefAdoptAPPolicy11g_Type()
)
ccPolicyDefAdoptAPPolicy11g.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyDefAdoptAPPolicy11g.setStatus("current")


class _CcPolicyChannel11g_Type(DisplayString):
    """Custom type ccPolicyChannel11g based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcPolicyChannel11g_Type.__name__ = "DisplayString"
_CcPolicyChannel11g_Object = MibTableColumn
ccPolicyChannel11g = _CcPolicyChannel11g_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 29),
    _CcPolicyChannel11g_Type()
)
ccPolicyChannel11g.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyChannel11g.setStatus("current")


class _CcPolicyPower11g_Type(DisplayString):
    """Custom type ccPolicyPower11g based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcPolicyPower11g_Type.__name__ = "DisplayString"
_CcPolicyPower11g_Object = MibTableColumn
ccPolicyPower11g = _CcPolicyPower11g_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 2, 1, 30),
    _CcPolicyPower11g_Type()
)
ccPolicyPower11g.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyPower11g.setStatus("current")
_CcCountryInfoTable_Object = MibTable
ccCountryInfoTable = _CcCountryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3)
)
if mibBuilder.loadTexts:
    ccCountryInfoTable.setStatus("current")
_CcCountryInfoEntry_Object = MibTableRow
ccCountryInfoEntry = _CcCountryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1)
)
ccCountryInfoEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccCCIndex"),
)
if mibBuilder.loadTexts:
    ccCountryInfoEntry.setStatus("current")


class _CcCCIndex_Type(Integer32):
    """Custom type ccCCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCCIndex_Type.__name__ = "Integer32"
_CcCCIndex_Object = MibTableColumn
ccCCIndex = _CcCCIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 1),
    _CcCCIndex_Type()
)
ccCCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCCIndex.setStatus("current")


class _CcCCode_Type(DisplayString):
    """Custom type ccCCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CcCCode_Type.__name__ = "DisplayString"
_CcCCode_Object = MibTableColumn
ccCCode = _CcCCode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 2),
    _CcCCode_Type()
)
ccCCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCCode.setStatus("current")


class _CcFullName_Type(DisplayString):
    """Custom type ccFullName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcFullName_Type.__name__ = "DisplayString"
_CcFullName_Object = MibTableColumn
ccFullName = _CcFullName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 3),
    _CcFullName_Type()
)
ccFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFullName.setStatus("current")


class _Cc11aChannels_Type(DisplayString):
    """Custom type cc11aChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_Cc11aChannels_Type.__name__ = "DisplayString"
_Cc11aChannels_Object = MibTableColumn
cc11aChannels = _Cc11aChannels_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 6),
    _Cc11aChannels_Type()
)
cc11aChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc11aChannels.setStatus("current")


class _Cc11bChannels_Type(DisplayString):
    """Custom type cc11bChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_Cc11bChannels_Type.__name__ = "DisplayString"
_Cc11bChannels_Object = MibTableColumn
cc11bChannels = _Cc11bChannels_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 7),
    _Cc11bChannels_Type()
)
cc11bChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc11bChannels.setStatus("current")


class _CcFHTableNum_Type(Integer32):
    """Custom type ccFHTableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CcFHTableNum_Type.__name__ = "Integer32"
_CcFHTableNum_Object = MibTableColumn
ccFHTableNum = _CcFHTableNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 8),
    _CcFHTableNum_Type()
)
ccFHTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFHTableNum.setStatus("current")


class _CcFHChannels_Type(DisplayString):
    """Custom type ccFHChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CcFHChannels_Type.__name__ = "DisplayString"
_CcFHChannels_Object = MibTableColumn
ccFHChannels = _CcFHChannels_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 9),
    _CcFHChannels_Type()
)
ccFHChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFHChannels.setStatus("current")
_CcFHAlgorithm_Type = FHAlgorithm
_CcFHAlgorithm_Object = MibTableColumn
ccFHAlgorithm = _CcFHAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 10),
    _CcFHAlgorithm_Type()
)
ccFHAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFHAlgorithm.setStatus("current")


class _CcFHContiguous_Type(Integer32):
    """Custom type ccFHContiguous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcFHContiguous_Type.__name__ = "Integer32"
_CcFHContiguous_Object = MibTableColumn
ccFHContiguous = _CcFHContiguous_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 11),
    _CcFHContiguous_Type()
)
ccFHContiguous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFHContiguous.setStatus("current")


class _CcFHHopSequence_Type(DisplayString):
    """Custom type ccFHHopSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_CcFHHopSequence_Type.__name__ = "DisplayString"
_CcFHHopSequence_Object = MibTableColumn
ccFHHopSequence = _CcFHHopSequence_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 12),
    _CcFHHopSequence_Type()
)
ccFHHopSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFHHopSequence.setStatus("current")


class _Cc11gChannels_Type(DisplayString):
    """Custom type cc11gChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_Cc11gChannels_Type.__name__ = "DisplayString"
_Cc11gChannels_Object = MibTableColumn
cc11gChannels = _Cc11gChannels_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 3, 1, 13),
    _Cc11gChannels_Type()
)
cc11gChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc11gChannels.setStatus("current")
_CcOnBoardKerberos_ObjectIdentity = ObjectIdentity
ccOnBoardKerberos = _CcOnBoardKerberos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4)
)
_KerbCfgKDC_ObjectIdentity = ObjectIdentity
kerbCfgKDC = _KerbCfgKDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3)
)


class _KdcType_Type(DisplayString):
    """Custom type kdcType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_KdcType_Type.__name__ = "DisplayString"
_KdcType_Object = MibScalar
kdcType = _KdcType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 1),
    _KdcType_Type()
)
kdcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kdcType.setStatus("current")


class _MasterHost_Type(DisplayString):
    """Custom type masterHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MasterHost_Type.__name__ = "DisplayString"
_MasterHost_Object = MibScalar
masterHost = _MasterHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 7),
    _MasterHost_Type()
)
masterHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterHost.setStatus("current")
_MasterIPAddress_Type = IpAddress
_MasterIPAddress_Object = MibScalar
masterIPAddress = _MasterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 8),
    _MasterIPAddress_Type()
)
masterIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterIPAddress.setStatus("current")


class _CreateMsKdc_Type(DisplayString):
    """Custom type createMsKdc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_CreateMsKdc_Type.__name__ = "DisplayString"
_CreateMsKdc_Object = MibScalar
createMsKdc = _CreateMsKdc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 9),
    _CreateMsKdc_Type()
)
createMsKdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    createMsKdc.setStatus("current")
_DelMsKdc_Type = TruthValue
_DelMsKdc_Object = MibScalar
delMsKdc = _DelMsKdc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 10),
    _DelMsKdc_Type()
)
delMsKdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delMsKdc.setStatus("current")


class _CreateSlvKdc_Type(DisplayString):
    """Custom type createSlvKdc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_CreateSlvKdc_Type.__name__ = "DisplayString"
_CreateSlvKdc_Object = MibScalar
createSlvKdc = _CreateSlvKdc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 11),
    _CreateSlvKdc_Type()
)
createSlvKdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    createSlvKdc.setStatus("current")
_DelSlvKdc_Type = TruthValue
_DelSlvKdc_Object = MibScalar
delSlvKdc = _DelSlvKdc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 12),
    _DelSlvKdc_Type()
)
delSlvKdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delSlvKdc.setStatus("current")


class _KdcRealm_Type(DisplayString):
    """Custom type kdcRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KdcRealm_Type.__name__ = "DisplayString"
_KdcRealm_Object = MibScalar
kdcRealm = _KdcRealm_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 13),
    _KdcRealm_Type()
)
kdcRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kdcRealm.setStatus("current")
_InterfaceNumber_Type = DisplayString
_InterfaceNumber_Object = MibScalar
interfaceNumber = _InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 14),
    _InterfaceNumber_Type()
)
interfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumber.setStatus("current")
_AddkdcMu_Type = DisplayString
_AddkdcMu_Object = MibScalar
addkdcMu = _AddkdcMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 15),
    _AddkdcMu_Type()
)
addkdcMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addkdcMu.setStatus("current")
_RemkdcMu_Type = DisplayString
_RemkdcMu_Object = MibScalar
remkdcMu = _RemkdcMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 3, 16),
    _RemkdcMu_Type()
)
remkdcMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remkdcMu.setStatus("current")
_KerbCfgSlave_ObjectIdentity = ObjectIdentity
kerbCfgSlave = _KerbCfgSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4)
)


class _AddSlave_Type(DisplayString):
    """Custom type addSlave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AddSlave_Type.__name__ = "DisplayString"
_AddSlave_Object = MibScalar
addSlave = _AddSlave_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 1),
    _AddSlave_Type()
)
addSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addSlave.setStatus("current")


class _DelSlave_Type(DisplayString):
    """Custom type delSlave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DelSlave_Type.__name__ = "DisplayString"
_DelSlave_Object = MibScalar
delSlave = _DelSlave_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 2),
    _DelSlave_Type()
)
delSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delSlave.setStatus("current")
_SlaveCount_Type = Integer32
_SlaveCount_Object = MibScalar
slaveCount = _SlaveCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 3),
    _SlaveCount_Type()
)
slaveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveCount.setStatus("current")
_SlaveTable_Object = MibTable
slaveTable = _SlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    slaveTable.setStatus("current")
_SlaveEntry_Object = MibTableRow
slaveEntry = _SlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4, 1)
)
slaveEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "slaveIndex"),
)
if mibBuilder.loadTexts:
    slaveEntry.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4, 1, 1),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _RealM_Type(DisplayString):
    """Custom type realM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RealM_Type.__name__ = "DisplayString"
_RealM_Object = MibTableColumn
realM = _RealM_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4, 1, 2),
    _RealM_Type()
)
realM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realM.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4, 1, 3),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")


class _DomainName_Type(DisplayString):
    """Custom type domainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DomainName_Type.__name__ = "DisplayString"
_DomainName_Object = MibTableColumn
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4, 1, 4),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("current")


class _SlaveIndex_Type(Integer32):
    """Custom type slaveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SlaveIndex_Type.__name__ = "Integer32"
_SlaveIndex_Object = MibTableColumn
slaveIndex = _SlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 4, 1, 5),
    _SlaveIndex_Type()
)
slaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaveIndex.setStatus("current")


class _SyncDB_Type(DisplayString):
    """Custom type syncDB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SyncDB_Type.__name__ = "DisplayString"
_SyncDB_Object = MibScalar
syncDB = _SyncDB_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 4, 5),
    _SyncDB_Type()
)
syncDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncDB.setStatus("current")
_KerbCfgNTP_ObjectIdentity = ObjectIdentity
kerbCfgNTP = _KerbCfgNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5)
)
_PrefTimeServer_Type = IpAddress
_PrefTimeServer_Object = MibScalar
prefTimeServer = _PrefTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5, 1),
    _PrefTimeServer_Type()
)
prefTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefTimeServer.setStatus("current")
_FirstAltTimeServer_Type = IpAddress
_FirstAltTimeServer_Object = MibScalar
firstAltTimeServer = _FirstAltTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5, 2),
    _FirstAltTimeServer_Type()
)
firstAltTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstAltTimeServer.setStatus("current")
_SecondAltTimeServer_Type = IpAddress
_SecondAltTimeServer_Object = MibScalar
secondAltTimeServer = _SecondAltTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5, 3),
    _SecondAltTimeServer_Type()
)
secondAltTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondAltTimeServer.setStatus("current")


class _GroupSetTimeServer_Type(DisplayString):
    """Custom type groupSetTimeServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_GroupSetTimeServer_Type.__name__ = "DisplayString"
_GroupSetTimeServer_Object = MibScalar
groupSetTimeServer = _GroupSetTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5, 4),
    _GroupSetTimeServer_Type()
)
groupSetTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupSetTimeServer.setStatus("current")
_DelAll_Type = TruthValue
_DelAll_Object = MibScalar
delAll = _DelAll_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5, 5),
    _DelAll_Type()
)
delAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delAll.setStatus("current")


class _DelTimeServer_Type(DisplayString):
    """Custom type delTimeServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DelTimeServer_Type.__name__ = "DisplayString"
_DelTimeServer_Object = MibScalar
delTimeServer = _DelTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 5, 6),
    _DelTimeServer_Type()
)
delTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delTimeServer.setStatus("deprecated")
_KerbKDCUsers_ObjectIdentity = ObjectIdentity
kerbKDCUsers = _KerbKDCUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6)
)
_KdcUserTable_Object = MibTable
kdcUserTable = _KdcUserTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    kdcUserTable.setStatus("current")
_KdcUserEntry_Object = MibTableRow
kdcUserEntry = _KdcUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 1, 1)
)
kdcUserEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "kdcUserIndex"),
)
if mibBuilder.loadTexts:
    kdcUserEntry.setStatus("current")


class _KdcUserIndex_Type(Integer32):
    """Custom type kdcUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_KdcUserIndex_Type.__name__ = "Integer32"
_KdcUserIndex_Object = MibTableColumn
kdcUserIndex = _KdcUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 1, 1, 1),
    _KdcUserIndex_Type()
)
kdcUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kdcUserIndex.setStatus("current")


class _KdcUserName_Type(DisplayString):
    """Custom type kdcUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_KdcUserName_Type.__name__ = "DisplayString"
_KdcUserName_Object = MibTableColumn
kdcUserName = _KdcUserName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 1, 1, 2),
    _KdcUserName_Type()
)
kdcUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kdcUserName.setStatus("current")
_KdcUserTlife_Type = Integer32
_KdcUserTlife_Object = MibTableColumn
kdcUserTlife = _KdcUserTlife_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 1, 1, 3),
    _KdcUserTlife_Type()
)
kdcUserTlife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kdcUserTlife.setStatus("current")
_KdcWLANTable_Object = MibTable
kdcWLANTable = _KdcWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 2)
)
if mibBuilder.loadTexts:
    kdcWLANTable.setStatus("current")
_KdcWLANEntry_Object = MibTableRow
kdcWLANEntry = _KdcWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 2, 1)
)
kdcWLANEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "kdcWLANIndex"),
)
if mibBuilder.loadTexts:
    kdcWLANEntry.setStatus("current")


class _KdcWLANIndex_Type(Integer32):
    """Custom type kdcWLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_KdcWLANIndex_Type.__name__ = "Integer32"
_KdcWLANIndex_Object = MibTableColumn
kdcWLANIndex = _KdcWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 2, 1, 1),
    _KdcWLANIndex_Type()
)
kdcWLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kdcWLANIndex.setStatus("current")


class _KdcWLANName_Type(DisplayString):
    """Custom type kdcWLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_KdcWLANName_Type.__name__ = "DisplayString"
_KdcWLANName_Object = MibTableColumn
kdcWLANName = _KdcWLANName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 2, 1, 2),
    _KdcWLANName_Type()
)
kdcWLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kdcWLANName.setStatus("current")
_KdcWLANTlife_Type = Integer32
_KdcWLANTlife_Object = MibTableColumn
kdcWLANTlife = _KdcWLANTlife_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 4, 6, 2, 1, 3),
    _KdcWLANTlife_Type()
)
kdcWLANTlife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kdcWLANTlife.setStatus("current")
_RadiusAuthentication_ObjectIdentity = ObjectIdentity
radiusAuthentication = _RadiusAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5)
)
_RadiusAuthClientMIB_ObjectIdentity = ObjectIdentity
radiusAuthClientMIB = _RadiusAuthClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2)
)
_RadiusAuthClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBObjects = _RadiusAuthClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1)
)
_RadiusAuthClient_ObjectIdentity = ObjectIdentity
radiusAuthClient = _RadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1)
)
_RadiusAuthClientInvalidServerAddresses_Type = Counter32
_RadiusAuthClientInvalidServerAddresses_Object = MibScalar
radiusAuthClientInvalidServerAddresses = _RadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 1),
    _RadiusAuthClientInvalidServerAddresses_Type()
)
radiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientInvalidServerAddresses.setStatus("current")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("current")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("current")


class _RadiusAuthServerIndex_Type(Integer32):
    """Custom type radiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAuthServerIndex_Type.__name__ = "Integer32"
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("current")
_RadiusAuthServerAddress_Type = DisplayString
_RadiusAuthServerAddress_Object = MibTableColumn
radiusAuthServerAddress = _RadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 2),
    _RadiusAuthServerAddress_Type()
)
radiusAuthServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerAddress.setStatus("current")


class _RadiusAuthClientServerPortNumber_Type(Integer32):
    """Custom type radiusAuthClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusAuthClientServerPortNumber_Type.__name__ = "Integer32"
_RadiusAuthClientServerPortNumber_Object = MibTableColumn
radiusAuthClientServerPortNumber = _RadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 3),
    _RadiusAuthClientServerPortNumber_Type()
)
radiusAuthClientServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthClientServerPortNumber.setStatus("current")
_RadiusAuthClientRoundTripTime_Type = TimeTicks
_RadiusAuthClientRoundTripTime_Object = MibTableColumn
radiusAuthClientRoundTripTime = _RadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 4),
    _RadiusAuthClientRoundTripTime_Type()
)
radiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientRoundTripTime.setStatus("current")
_RadiusAuthClientAccessRequests_Type = Counter32
_RadiusAuthClientAccessRequests_Object = MibTableColumn
radiusAuthClientAccessRequests = _RadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 5),
    _RadiusAuthClientAccessRequests_Type()
)
radiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRequests.setStatus("current")


class _RadiusAuthClientAccessRetransmissions_Type(Integer32):
    """Custom type radiusAuthClientAccessRetransmissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadiusAuthClientAccessRetransmissions_Type.__name__ = "Integer32"
_RadiusAuthClientAccessRetransmissions_Object = MibTableColumn
radiusAuthClientAccessRetransmissions = _RadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 6),
    _RadiusAuthClientAccessRetransmissions_Type()
)
radiusAuthClientAccessRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRetransmissions.setStatus("current")
_RadiusAuthClientAccessAccepts_Type = Counter32
_RadiusAuthClientAccessAccepts_Object = MibTableColumn
radiusAuthClientAccessAccepts = _RadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 7),
    _RadiusAuthClientAccessAccepts_Type()
)
radiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessAccepts.setStatus("current")
_RadiusAuthClientAccessRejects_Type = Counter32
_RadiusAuthClientAccessRejects_Object = MibTableColumn
radiusAuthClientAccessRejects = _RadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 8),
    _RadiusAuthClientAccessRejects_Type()
)
radiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRejects.setStatus("current")
_RadiusAuthClientAccessChallenges_Type = Counter32
_RadiusAuthClientAccessChallenges_Object = MibTableColumn
radiusAuthClientAccessChallenges = _RadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 9),
    _RadiusAuthClientAccessChallenges_Type()
)
radiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessChallenges.setStatus("current")
_RadiusAuthClientMalformedAccessResponses_Type = Counter32
_RadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
radiusAuthClientMalformedAccessResponses = _RadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 10),
    _RadiusAuthClientMalformedAccessResponses_Type()
)
radiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientMalformedAccessResponses.setStatus("current")
_RadiusAuthClientBadAuthenticators_Type = Counter32
_RadiusAuthClientBadAuthenticators_Object = MibTableColumn
radiusAuthClientBadAuthenticators = _RadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 11),
    _RadiusAuthClientBadAuthenticators_Type()
)
radiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientBadAuthenticators.setStatus("current")
_RadiusAuthClientPendingRequests_Type = Gauge32
_RadiusAuthClientPendingRequests_Object = MibTableColumn
radiusAuthClientPendingRequests = _RadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 12),
    _RadiusAuthClientPendingRequests_Type()
)
radiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientPendingRequests.setStatus("current")


class _RadiusAuthClientTimeouts_Type(Integer32):
    """Custom type radiusAuthClientTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_RadiusAuthClientTimeouts_Type.__name__ = "Integer32"
_RadiusAuthClientTimeouts_Object = MibTableColumn
radiusAuthClientTimeouts = _RadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 13),
    _RadiusAuthClientTimeouts_Type()
)
radiusAuthClientTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthClientTimeouts.setStatus("current")
_RadiusAuthClientUnknownTypes_Type = Counter32
_RadiusAuthClientUnknownTypes_Object = MibTableColumn
radiusAuthClientUnknownTypes = _RadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 14),
    _RadiusAuthClientUnknownTypes_Type()
)
radiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientUnknownTypes.setStatus("current")
_RadiusAuthClientPacketsDropped_Type = Counter32
_RadiusAuthClientPacketsDropped_Object = MibTableColumn
radiusAuthClientPacketsDropped = _RadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 15),
    _RadiusAuthClientPacketsDropped_Type()
)
radiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientPacketsDropped.setStatus("current")
_RadiusAuthClientIdentifier_Type = SnmpAdminString
_RadiusAuthClientIdentifier_Object = MibTableColumn
radiusAuthClientIdentifier = _RadiusAuthClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 1, 1, 3, 1, 16),
    _RadiusAuthClientIdentifier_Type()
)
radiusAuthClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientIdentifier.setStatus("current")
_RadiusAuthClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBConformance = _RadiusAuthClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 2)
)
_RadiusAuthClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBCompliances = _RadiusAuthClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 2, 1)
)
_RadiusAuthClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBGroups = _RadiusAuthClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 2, 2)
)
_CcEventsObjects_ObjectIdentity = ObjectIdentity
ccEventsObjects = _CcEventsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6)
)
_CcEventsAllLocalLog_Type = TruthValue
_CcEventsAllLocalLog_Object = MibScalar
ccEventsAllLocalLog = _CcEventsAllLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 1),
    _CcEventsAllLocalLog_Type()
)
ccEventsAllLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventsAllLocalLog.setStatus("current")
_CcEventsAllSNMPTrap_Type = TruthValue
_CcEventsAllSNMPTrap_Object = MibScalar
ccEventsAllSNMPTrap = _CcEventsAllSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 2),
    _CcEventsAllSNMPTrap_Type()
)
ccEventsAllSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventsAllSNMPTrap.setStatus("current")


class _CcEventsAllSyslog_Type(DisplayString):
    """Custom type ccEventsAllSyslog based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_CcEventsAllSyslog_Type.__name__ = "DisplayString"
_CcEventsAllSyslog_Object = MibScalar
ccEventsAllSyslog = _CcEventsAllSyslog_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 3),
    _CcEventsAllSyslog_Type()
)
ccEventsAllSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventsAllSyslog.setStatus("current")
_CcEventsAllDefault_Type = TruthValue
_CcEventsAllDefault_Object = MibScalar
ccEventsAllDefault = _CcEventsAllDefault_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 4),
    _CcEventsAllDefault_Type()
)
ccEventsAllDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventsAllDefault.setStatus("current")
_CcEventTable_Object = MibTable
ccEventTable = _CcEventTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5)
)
if mibBuilder.loadTexts:
    ccEventTable.setStatus("current")
_CcEventEntry_Object = MibTableRow
ccEventEntry = _CcEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1)
)
ccEventEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccEventIndex"),
)
if mibBuilder.loadTexts:
    ccEventEntry.setStatus("current")


class _CcEventIndex_Type(Integer32):
    """Custom type ccEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcEventIndex_Type.__name__ = "Integer32"
_CcEventIndex_Object = MibTableColumn
ccEventIndex = _CcEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1, 1),
    _CcEventIndex_Type()
)
ccEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccEventIndex.setStatus("current")


class _CcEventDescr_Type(DisplayString):
    """Custom type ccEventDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcEventDescr_Type.__name__ = "DisplayString"
_CcEventDescr_Object = MibTableColumn
ccEventDescr = _CcEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1, 2),
    _CcEventDescr_Type()
)
ccEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEventDescr.setStatus("current")
_CcEventDefault_Type = TruthValue
_CcEventDefault_Object = MibTableColumn
ccEventDefault = _CcEventDefault_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1, 3),
    _CcEventDefault_Type()
)
ccEventDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventDefault.setStatus("current")


class _CcEventSyslog_Type(DisplayString):
    """Custom type ccEventSyslog based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcEventSyslog_Type.__name__ = "DisplayString"
_CcEventSyslog_Object = MibTableColumn
ccEventSyslog = _CcEventSyslog_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1, 4),
    _CcEventSyslog_Type()
)
ccEventSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventSyslog.setStatus("current")
_CcEventSNMPTrap_Type = TruthValue
_CcEventSNMPTrap_Object = MibTableColumn
ccEventSNMPTrap = _CcEventSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1, 5),
    _CcEventSNMPTrap_Type()
)
ccEventSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventSNMPTrap.setStatus("current")
_CcEventLocalLog_Type = TruthValue
_CcEventLocalLog_Object = MibTableColumn
ccEventLocalLog = _CcEventLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 5, 1, 6),
    _CcEventLocalLog_Type()
)
ccEventLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEventLocalLog.setStatus("current")
_CcSyslogObjects_ObjectIdentity = ObjectIdentity
ccSyslogObjects = _CcSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6)
)
_CcSysLogStatus_Type = TruthValue
_CcSysLogStatus_Object = MibScalar
ccSysLogStatus = _CcSysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 1),
    _CcSysLogStatus_Type()
)
ccSysLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSysLogStatus.setStatus("current")
_CcSyslogHosts_ObjectIdentity = ObjectIdentity
ccSyslogHosts = _CcSyslogHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2)
)


class _CcSyslogAddHost_Type(DisplayString):
    """Custom type ccSyslogAddHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSyslogAddHost_Type.__name__ = "DisplayString"
_CcSyslogAddHost_Object = MibScalar
ccSyslogAddHost = _CcSyslogAddHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 1),
    _CcSyslogAddHost_Type()
)
ccSyslogAddHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSyslogAddHost.setStatus("current")


class _CcSyslogRemHost_Type(DisplayString):
    """Custom type ccSyslogRemHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcSyslogRemHost_Type.__name__ = "DisplayString"
_CcSyslogRemHost_Object = MibScalar
ccSyslogRemHost = _CcSyslogRemHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 2),
    _CcSyslogRemHost_Type()
)
ccSyslogRemHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSyslogRemHost.setStatus("current")
_CcSyslogHostsTable_Object = MibTable
ccSyslogHostsTable = _CcSyslogHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3)
)
if mibBuilder.loadTexts:
    ccSyslogHostsTable.setStatus("current")
_CcSyslogHostsEntry_Object = MibTableRow
ccSyslogHostsEntry = _CcSyslogHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1)
)
ccSyslogHostsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccSyslogHostIndex"),
)
if mibBuilder.loadTexts:
    ccSyslogHostsEntry.setStatus("current")


class _CcSyslogHostIndex_Type(Integer32):
    """Custom type ccSyslogHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcSyslogHostIndex_Type.__name__ = "Integer32"
_CcSyslogHostIndex_Object = MibTableColumn
ccSyslogHostIndex = _CcSyslogHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1, 1),
    _CcSyslogHostIndex_Type()
)
ccSyslogHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccSyslogHostIndex.setStatus("current")


class _CcSyslogHostName_Type(DisplayString):
    """Custom type ccSyslogHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSyslogHostName_Type.__name__ = "DisplayString"
_CcSyslogHostName_Object = MibTableColumn
ccSyslogHostName = _CcSyslogHostName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1, 2),
    _CcSyslogHostName_Type()
)
ccSyslogHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSyslogHostName.setStatus("current")
_CcSyslogHostIPAddr_Type = IpAddress
_CcSyslogHostIPAddr_Object = MibTableColumn
ccSyslogHostIPAddr = _CcSyslogHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1, 3),
    _CcSyslogHostIPAddr_Type()
)
ccSyslogHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSyslogHostIPAddr.setStatus("current")


class _CcSyslogHostDomain_Type(DisplayString):
    """Custom type ccSyslogHostDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSyslogHostDomain_Type.__name__ = "DisplayString"
_CcSyslogHostDomain_Object = MibTableColumn
ccSyslogHostDomain = _CcSyslogHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1, 4),
    _CcSyslogHostDomain_Type()
)
ccSyslogHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSyslogHostDomain.setStatus("current")


class _CcSyslogHostSetSeverity_Type(DisplayString):
    """Custom type ccSyslogHostSetSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSyslogHostSetSeverity_Type.__name__ = "DisplayString"
_CcSyslogHostSetSeverity_Object = MibTableColumn
ccSyslogHostSetSeverity = _CcSyslogHostSetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1, 5),
    _CcSyslogHostSetSeverity_Type()
)
ccSyslogHostSetSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSyslogHostSetSeverity.setStatus("current")


class _CcSyslogHostSeverityList_Type(DisplayString):
    """Custom type ccSyslogHostSeverityList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSyslogHostSeverityList_Type.__name__ = "DisplayString"
_CcSyslogHostSeverityList_Object = MibTableColumn
ccSyslogHostSeverityList = _CcSyslogHostSeverityList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 6, 6, 2, 3, 1, 6),
    _CcSyslogHostSeverityList_Type()
)
ccSyslogHostSeverityList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSyslogHostSeverityList.setStatus("current")
_CcSystemHosts_ObjectIdentity = ObjectIdentity
ccSystemHosts = _CcSystemHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7)
)


class _CcSystemAddHost_Type(DisplayString):
    """Custom type ccSystemAddHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSystemAddHost_Type.__name__ = "DisplayString"
_CcSystemAddHost_Object = MibScalar
ccSystemAddHost = _CcSystemAddHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 1),
    _CcSystemAddHost_Type()
)
ccSystemAddHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSystemAddHost.setStatus("current")


class _CcSystemRemHost_Type(DisplayString):
    """Custom type ccSystemRemHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSystemRemHost_Type.__name__ = "DisplayString"
_CcSystemRemHost_Object = MibScalar
ccSystemRemHost = _CcSystemRemHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 2),
    _CcSystemRemHost_Type()
)
ccSystemRemHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSystemRemHost.setStatus("current")
_CcSystemHostsTable_Object = MibTable
ccSystemHostsTable = _CcSystemHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ccSystemHostsTable.setStatus("current")
_CcSystemHostsEntry_Object = MibTableRow
ccSystemHostsEntry = _CcSystemHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 3, 1)
)
ccSystemHostsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccSystemHostIndex"),
)
if mibBuilder.loadTexts:
    ccSystemHostsEntry.setStatus("current")


class _CcSystemHostIndex_Type(Integer32):
    """Custom type ccSystemHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcSystemHostIndex_Type.__name__ = "Integer32"
_CcSystemHostIndex_Object = MibTableColumn
ccSystemHostIndex = _CcSystemHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 3, 1, 1),
    _CcSystemHostIndex_Type()
)
ccSystemHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccSystemHostIndex.setStatus("current")


class _CcSystemHostName_Type(DisplayString):
    """Custom type ccSystemHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSystemHostName_Type.__name__ = "DisplayString"
_CcSystemHostName_Object = MibTableColumn
ccSystemHostName = _CcSystemHostName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 3, 1, 2),
    _CcSystemHostName_Type()
)
ccSystemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSystemHostName.setStatus("current")
_CcSystemHostIPAddr_Type = IpAddress
_CcSystemHostIPAddr_Object = MibTableColumn
ccSystemHostIPAddr = _CcSystemHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 3, 1, 3),
    _CcSystemHostIPAddr_Type()
)
ccSystemHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSystemHostIPAddr.setStatus("current")


class _CcSystemHostDomain_Type(DisplayString):
    """Custom type ccSystemHostDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcSystemHostDomain_Type.__name__ = "DisplayString"
_CcSystemHostDomain_Object = MibTableColumn
ccSystemHostDomain = _CcSystemHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 7, 3, 1, 4),
    _CcSystemHostDomain_Type()
)
ccSystemHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSystemHostDomain.setStatus("current")
_CcPolicyRCObjects_ObjectIdentity = ObjectIdentity
ccPolicyRCObjects = _CcPolicyRCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8)
)
_CcPolicyRCAddRemTable_Object = MibTable
ccPolicyRCAddRemTable = _CcPolicyRCAddRemTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ccPolicyRCAddRemTable.setStatus("current")
_CcPolicyRCAddRemEntry_Object = MibTableRow
ccPolicyRCAddRemEntry = _CcPolicyRCAddRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 1, 1)
)
ccPolicyRCAddRemEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPolicyIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccPolicyRadioType"),
)
if mibBuilder.loadTexts:
    ccPolicyRCAddRemEntry.setStatus("current")


class _CcPolicyRadioType_Type(Integer32):
    """Custom type ccPolicyRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcPolicyRadioType_Type.__name__ = "Integer32"
_CcPolicyRadioType_Object = MibTableColumn
ccPolicyRadioType = _CcPolicyRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 1, 1, 1),
    _CcPolicyRadioType_Type()
)
ccPolicyRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccPolicyRadioType.setStatus("current")


class _CcPolicyRCAdd_Type(DisplayString):
    """Custom type ccPolicyRCAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_CcPolicyRCAdd_Type.__name__ = "DisplayString"
_CcPolicyRCAdd_Object = MibTableColumn
ccPolicyRCAdd = _CcPolicyRCAdd_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 1, 1, 2),
    _CcPolicyRCAdd_Type()
)
ccPolicyRCAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyRCAdd.setStatus("current")


class _CcPolicyRCRem_Type(DisplayString):
    """Custom type ccPolicyRCRem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 300),
    )


_CcPolicyRCRem_Type.__name__ = "DisplayString"
_CcPolicyRCRem_Object = MibTableColumn
ccPolicyRCRem = _CcPolicyRCRem_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 1, 1, 3),
    _CcPolicyRCRem_Type()
)
ccPolicyRCRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPolicyRCRem.setStatus("current")
_CcPolicyRCTable_Object = MibTable
ccPolicyRCTable = _CcPolicyRCTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ccPolicyRCTable.setStatus("current")
_CcPolicyRCEntry_Object = MibTableRow
ccPolicyRCEntry = _CcPolicyRCEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 2, 1)
)
ccPolicyRCEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPolicyIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccPolicyRadioType"),
    (0, "SYMBOL-WS5000-MIB", "ccPolicyRcIndex"),
)
if mibBuilder.loadTexts:
    ccPolicyRCEntry.setStatus("current")


class _CcPolicyRcIndex_Type(Integer32):
    """Custom type ccPolicyRcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CcPolicyRcIndex_Type.__name__ = "Integer32"
_CcPolicyRcIndex_Object = MibTableColumn
ccPolicyRcIndex = _CcPolicyRcIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 2, 1, 1),
    _CcPolicyRcIndex_Type()
)
ccPolicyRcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccPolicyRcIndex.setStatus("current")


class _CcPolicyRCChannelDescr_Type(DisplayString):
    """Custom type ccPolicyRCChannelDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_CcPolicyRCChannelDescr_Type.__name__ = "DisplayString"
_CcPolicyRCChannelDescr_Object = MibTableColumn
ccPolicyRCChannelDescr = _CcPolicyRCChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 8, 2, 1, 2),
    _CcPolicyRCChannelDescr_Type()
)
ccPolicyRCChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPolicyRCChannelDescr.setStatus("current")
_CcPolicyObject_ObjectIdentity = ObjectIdentity
ccPolicyObject = _CcPolicyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 9)
)
_CcPolicyAPPolicyTable_Object = MibTable
ccPolicyAPPolicyTable = _CcPolicyAPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ccPolicyAPPolicyTable.setStatus("current")
_CcPolicyAPPolicyEntry_Object = MibTableRow
ccPolicyAPPolicyEntry = _CcPolicyAPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 9, 2, 1)
)
ccPolicyAPPolicyEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPolicyIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccPolicyAPPolicyIndex"),
)
if mibBuilder.loadTexts:
    ccPolicyAPPolicyEntry.setStatus("current")


class _CcPolicyAPPolicyIndex_Type(Integer32):
    """Custom type ccPolicyAPPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcPolicyAPPolicyIndex_Type.__name__ = "Integer32"
_CcPolicyAPPolicyIndex_Object = MibTableColumn
ccPolicyAPPolicyIndex = _CcPolicyAPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 9, 2, 1, 1),
    _CcPolicyAPPolicyIndex_Type()
)
ccPolicyAPPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccPolicyAPPolicyIndex.setStatus("current")


class _CcPolicyAPPolicyName_Type(DisplayString):
    """Custom type ccPolicyAPPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPolicyAPPolicyName_Type.__name__ = "DisplayString"
_CcPolicyAPPolicyName_Object = MibTableColumn
ccPolicyAPPolicyName = _CcPolicyAPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 9, 2, 1, 2),
    _CcPolicyAPPolicyName_Type()
)
ccPolicyAPPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPolicyAPPolicyName.setStatus("current")
_SymbolCCInterfaces_ObjectIdentity = ObjectIdentity
symbolCCInterfaces = _SymbolCCInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 2)
)


class _CcAPPolicyAddObj_Type(DisplayString):
    """Custom type ccAPPolicyAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcAPPolicyAddObj_Type.__name__ = "DisplayString"
_CcAPPolicyAddObj_Object = MibScalar
ccAPPolicyAddObj = _CcAPPolicyAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 1),
    _CcAPPolicyAddObj_Type()
)
ccAPPolicyAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyAddObj.setStatus("current")


class _CcAPPolicyRemObj_Type(DisplayString):
    """Custom type ccAPPolicyRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcAPPolicyRemObj_Type.__name__ = "DisplayString"
_CcAPPolicyRemObj_Object = MibScalar
ccAPPolicyRemObj = _CcAPPolicyRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 2),
    _CcAPPolicyRemObj_Type()
)
ccAPPolicyRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyRemObj.setStatus("current")


class _CcEPPAddObj_Type(DisplayString):
    """Custom type ccEPPAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcEPPAddObj_Type.__name__ = "DisplayString"
_CcEPPAddObj_Object = MibScalar
ccEPPAddObj = _CcEPPAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 3),
    _CcEPPAddObj_Type()
)
ccEPPAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPAddObj.setStatus("current")


class _CcEPPRemObj_Type(DisplayString):
    """Custom type ccEPPRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcEPPRemObj_Type.__name__ = "DisplayString"
_CcEPPRemObj_Object = MibScalar
ccEPPRemObj = _CcEPPRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 4),
    _CcEPPRemObj_Type()
)
ccEPPRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPRemObj.setStatus("current")


class _CcAccessPortAddObj_Type(DisplayString):
    """Custom type ccAccessPortAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcAccessPortAddObj_Type.__name__ = "DisplayString"
_CcAccessPortAddObj_Object = MibScalar
ccAccessPortAddObj = _CcAccessPortAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 5),
    _CcAccessPortAddObj_Type()
)
ccAccessPortAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAccessPortAddObj.setStatus("current")


class _CcAccessPortRemObj_Type(DisplayString):
    """Custom type ccAccessPortRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcAccessPortRemObj_Type.__name__ = "DisplayString"
_CcAccessPortRemObj_Object = MibScalar
ccAccessPortRemObj = _CcAccessPortRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 6),
    _CcAccessPortRemObj_Type()
)
ccAccessPortRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAccessPortRemObj.setStatus("current")


class _CcFWLanAddObj_Type(DisplayString):
    """Custom type ccFWLanAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcFWLanAddObj_Type.__name__ = "DisplayString"
_CcFWLanAddObj_Object = MibScalar
ccFWLanAddObj = _CcFWLanAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 7),
    _CcFWLanAddObj_Type()
)
ccFWLanAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccFWLanAddObj.setStatus("current")


class _CcFWLanRemObj_Type(DisplayString):
    """Custom type ccFWLanRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcFWLanRemObj_Type.__name__ = "DisplayString"
_CcFWLanRemObj_Object = MibScalar
ccFWLanRemObj = _CcFWLanRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 8),
    _CcFWLanRemObj_Type()
)
ccFWLanRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccFWLanRemObj.setStatus("current")
_CcAPTable_Object = MibTable
ccAPTable = _CcAPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10)
)
if mibBuilder.loadTexts:
    ccAPTable.setStatus("current")
_CcAPEntry_Object = MibTableRow
ccAPEntry = _CcAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1)
)
ccAPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadioIndex"),
)
if mibBuilder.loadTexts:
    ccAPEntry.setStatus("current")


class _CcRadioIndex_Type(Integer32):
    """Custom type ccRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CcRadioIndex_Type.__name__ = "Integer32"
_CcRadioIndex_Object = MibTableColumn
ccRadioIndex = _CcRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 28),
    _CcRadioIndex_Type()
)
ccRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccRadioIndex.setStatus("current")


class _CcRadioName_Type(DisplayString):
    """Custom type ccRadioName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcRadioName_Type.__name__ = "DisplayString"
_CcRadioName_Object = MibTableColumn
ccRadioName = _CcRadioName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 29),
    _CcRadioName_Type()
)
ccRadioName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioName.setStatus("current")


class _CcRadioDesc_Type(DisplayString):
    """Custom type ccRadioDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadioDesc_Type.__name__ = "DisplayString"
_CcRadioDesc_Object = MibTableColumn
ccRadioDesc = _CcRadioDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 30),
    _CcRadioDesc_Type()
)
ccRadioDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioDesc.setStatus("current")
_CcRadioOnlineStatus_Type = APOnlineStatus
_CcRadioOnlineStatus_Object = MibTableColumn
ccRadioOnlineStatus = _CcRadioOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 31),
    _CcRadioOnlineStatus_Type()
)
ccRadioOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioOnlineStatus.setStatus("current")
_CcRadioMAC_Type = DisplayString
_CcRadioMAC_Object = MibTableColumn
ccRadioMAC = _CcRadioMAC_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 32),
    _CcRadioMAC_Type()
)
ccRadioMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioMAC.setStatus("current")
_CcDeviceMAC_Type = DisplayString
_CcDeviceMAC_Object = MibTableColumn
ccDeviceMAC = _CcDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 33),
    _CcDeviceMAC_Type()
)
ccDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDeviceMAC.setStatus("current")


class _CcDeviceLocation_Type(DisplayString):
    """Custom type ccDeviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CcDeviceLocation_Type.__name__ = "DisplayString"
_CcDeviceLocation_Object = MibTableColumn
ccDeviceLocation = _CcDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 34),
    _CcDeviceLocation_Type()
)
ccDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDeviceLocation.setStatus("current")


class _CcRadioType_Type(DisplayString):
    """Custom type ccRadioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadioType_Type.__name__ = "DisplayString"
_CcRadioType_Object = MibTableColumn
ccRadioType = _CcRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 35),
    _CcRadioType_Type()
)
ccRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioType.setStatus("current")


class _CcRadioChannel_Type(DisplayString):
    """Custom type ccRadioChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcRadioChannel_Type.__name__ = "DisplayString"
_CcRadioChannel_Object = MibTableColumn
ccRadioChannel = _CcRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 36),
    _CcRadioChannel_Type()
)
ccRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioChannel.setStatus("current")


class _CcRadioPower_Type(DisplayString):
    """Custom type ccRadioPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcRadioPower_Type.__name__ = "DisplayString"
_CcRadioPower_Object = MibTableColumn
ccRadioPower = _CcRadioPower_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 37),
    _CcRadioPower_Type()
)
ccRadioPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioPower.setStatus("deprecated")


class _CcRadioPolicy_Type(DisplayString):
    """Custom type ccRadioPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CcRadioPolicy_Type.__name__ = "DisplayString"
_CcRadioPolicy_Object = MibTableColumn
ccRadioPolicy = _CcRadioPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 38),
    _CcRadioPolicy_Type()
)
ccRadioPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioPolicy.setStatus("current")


class _CcDeviceNic_Type(Integer32):
    """Custom type ccDeviceNic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcDeviceNic_Type.__name__ = "Integer32"
_CcDeviceNic_Object = MibTableColumn
ccDeviceNic = _CcDeviceNic_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 39),
    _CcDeviceNic_Type()
)
ccDeviceNic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDeviceNic.setStatus("current")


class _CcDeviceType_Type(DisplayString):
    """Custom type ccDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDeviceType_Type.__name__ = "DisplayString"
_CcDeviceType_Object = MibTableColumn
ccDeviceType = _CcDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 40),
    _CcDeviceType_Type()
)
ccDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDeviceType.setStatus("current")


class _CcRadioCCAmode_Type(Integer32):
    """Custom type ccRadioCCAmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CcRadioCCAmode_Type.__name__ = "Integer32"
_CcRadioCCAmode_Object = MibTableColumn
ccRadioCCAmode = _CcRadioCCAmode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 41),
    _CcRadioCCAmode_Type()
)
ccRadioCCAmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioCCAmode.setStatus("current")


class _CcRadioCCAthresh_Type(Integer32):
    """Custom type ccRadioCCAthresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CcRadioCCAthresh_Type.__name__ = "Integer32"
_CcRadioCCAthresh_Object = MibTableColumn
ccRadioCCAthresh = _CcRadioCCAthresh_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 42),
    _CcRadioCCAthresh_Type()
)
ccRadioCCAthresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioCCAthresh.setStatus("current")


class _CcRadioDiversity_Type(Integer32):
    """Custom type ccRadioDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcRadioDiversity_Type.__name__ = "Integer32"
_CcRadioDiversity_Object = MibTableColumn
ccRadioDiversity = _CcRadioDiversity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 43),
    _CcRadioDiversity_Type()
)
ccRadioDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioDiversity.setStatus("current")


class _CcDeviceVlanid_Type(Integer32):
    """Custom type ccDeviceVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CcDeviceVlanid_Type.__name__ = "Integer32"
_CcDeviceVlanid_Object = MibTableColumn
ccDeviceVlanid = _CcDeviceVlanid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 44),
    _CcDeviceVlanid_Type()
)
ccDeviceVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDeviceVlanid.setStatus("current")


class _CcDeviceVlanTagsSeen_Type(DisplayString):
    """Custom type ccDeviceVlanTagsSeen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcDeviceVlanTagsSeen_Type.__name__ = "DisplayString"
_CcDeviceVlanTagsSeen_Object = MibTableColumn
ccDeviceVlanTagsSeen = _CcDeviceVlanTagsSeen_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 45),
    _CcDeviceVlanTagsSeen_Type()
)
ccDeviceVlanTagsSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDeviceVlanTagsSeen.setStatus("current")


class _CcRadioUptime_Type(DisplayString):
    """Custom type ccRadioUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadioUptime_Type.__name__ = "DisplayString"
_CcRadioUptime_Object = MibTableColumn
ccRadioUptime = _CcRadioUptime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 46),
    _CcRadioUptime_Type()
)
ccRadioUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioUptime.setStatus("current")


class _CcRadioTxpps_Type(Integer32):
    """Custom type ccRadioTxpps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_CcRadioTxpps_Type.__name__ = "Integer32"
_CcRadioTxpps_Object = MibTableColumn
ccRadioTxpps = _CcRadioTxpps_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 47),
    _CcRadioTxpps_Type()
)
ccRadioTxpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioTxpps.setStatus("current")


class _CcRadioMUs_Type(Integer32):
    """Custom type ccRadioMUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CcRadioMUs_Type.__name__ = "Integer32"
_CcRadioMUs_Object = MibTableColumn
ccRadioMUs = _CcRadioMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 48),
    _CcRadioMUs_Type()
)
ccRadioMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioMUs.setStatus("current")
_CcRadioGatherStatistics_Type = TruthValue
_CcRadioGatherStatistics_Object = MibTableColumn
ccRadioGatherStatistics = _CcRadioGatherStatistics_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 49),
    _CcRadioGatherStatistics_Type()
)
ccRadioGatherStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioGatherStatistics.setStatus("current")
_CcRadioReset_Type = TruthValue
_CcRadioReset_Object = MibTableColumn
ccRadioReset = _CcRadioReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 50),
    _CcRadioReset_Type()
)
ccRadioReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioReset.setStatus("current")
_CcDeviceClearSeenVlanTags_Type = TruthValue
_CcDeviceClearSeenVlanTags_Object = MibTableColumn
ccDeviceClearSeenVlanTags = _CcDeviceClearSeenVlanTags_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 51),
    _CcDeviceClearSeenVlanTags_Type()
)
ccDeviceClearSeenVlanTags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDeviceClearSeenVlanTags.setStatus("deprecated")
_CcDeviceReset_Type = TruthValue
_CcDeviceReset_Object = MibTableColumn
ccDeviceReset = _CcDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 52),
    _CcDeviceReset_Type()
)
ccDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDeviceReset.setStatus("current")
_CcRadioAuto_Type = TruthValue
_CcRadioAuto_Object = MibTableColumn
ccRadioAuto = _CcRadioAuto_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 53),
    _CcRadioAuto_Type()
)
ccRadioAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioAuto.setStatus("deprecated")


class _CcRadioMUPower_Type(DisplayString):
    """Custom type ccRadioMUPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcRadioMUPower_Type.__name__ = "DisplayString"
_CcRadioMUPower_Object = MibTableColumn
ccRadioMUPower = _CcRadioMUPower_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 54),
    _CcRadioMUPower_Type()
)
ccRadioMUPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioMUPower.setStatus("deprecated")


class _CcRadioProtection_Type(DisplayString):
    """Custom type ccRadioProtection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CcRadioProtection_Type.__name__ = "DisplayString"
_CcRadioProtection_Object = MibTableColumn
ccRadioProtection = _CcRadioProtection_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 55),
    _CcRadioProtection_Type()
)
ccRadioProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioProtection.setStatus("current")


class _CcRadioShortSlot_Type(DisplayString):
    """Custom type ccRadioShortSlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CcRadioShortSlot_Type.__name__ = "DisplayString"
_CcRadioShortSlot_Object = MibTableColumn
ccRadioShortSlot = _CcRadioShortSlot_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 56),
    _CcRadioShortSlot_Type()
)
ccRadioShortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioShortSlot.setStatus("current")


class _CcRadioAntenna_Type(DisplayString):
    """Custom type ccRadioAntenna based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CcRadioAntenna_Type.__name__ = "DisplayString"
_CcRadioAntenna_Object = MibTableColumn
ccRadioAntenna = _CcRadioAntenna_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 57),
    _CcRadioAntenna_Type()
)
ccRadioAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioAntenna.setStatus("current")


class _CcRadioCurrentChannel_Type(DisplayString):
    """Custom type ccRadioCurrentChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcRadioCurrentChannel_Type.__name__ = "DisplayString"
_CcRadioCurrentChannel_Object = MibTableColumn
ccRadioCurrentChannel = _CcRadioCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 58),
    _CcRadioCurrentChannel_Type()
)
ccRadioCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioCurrentChannel.setStatus("current")


class _CcRadioAllChannels_Type(DisplayString):
    """Custom type ccRadioAllChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcRadioAllChannels_Type.__name__ = "DisplayString"
_CcRadioAllChannels_Object = MibTableColumn
ccRadioAllChannels = _CcRadioAllChannels_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 59),
    _CcRadioAllChannels_Type()
)
ccRadioAllChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioAllChannels.setStatus("current")


class _CcRadioPowerdBm_Type(DisplayString):
    """Custom type ccRadioPowerdBm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcRadioPowerdBm_Type.__name__ = "DisplayString"
_CcRadioPowerdBm_Object = MibTableColumn
ccRadioPowerdBm = _CcRadioPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 60),
    _CcRadioPowerdBm_Type()
)
ccRadioPowerdBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioPowerdBm.setStatus("current")


class _CcRadioCurrentPower_Type(DisplayString):
    """Custom type ccRadioCurrentPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcRadioCurrentPower_Type.__name__ = "DisplayString"
_CcRadioCurrentPower_Object = MibTableColumn
ccRadioCurrentPower = _CcRadioCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 61),
    _CcRadioCurrentPower_Type()
)
ccRadioCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioCurrentPower.setStatus("current")


class _CcRadioAllPower_Type(DisplayString):
    """Custom type ccRadioAllPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcRadioAllPower_Type.__name__ = "DisplayString"
_CcRadioAllPower_Object = MibTableColumn
ccRadioAllPower = _CcRadioAllPower_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 62),
    _CcRadioAllPower_Type()
)
ccRadioAllPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioAllPower.setStatus("current")


class _CcRadioMUPowerdBm_Type(DisplayString):
    """Custom type ccRadioMUPowerdBm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadioMUPowerdBm_Type.__name__ = "DisplayString"
_CcRadioMUPowerdBm_Object = MibTableColumn
ccRadioMUPowerdBm = _CcRadioMUPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 63),
    _CcRadioMUPowerdBm_Type()
)
ccRadioMUPowerdBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioMUPowerdBm.setStatus("current")


class _CcRadioAntCorrection_Type(Integer32):
    """Custom type ccRadioAntCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CcRadioAntCorrection_Type.__name__ = "Integer32"
_CcRadioAntCorrection_Object = MibTableColumn
ccRadioAntCorrection = _CcRadioAntCorrection_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 64),
    _CcRadioAntCorrection_Type()
)
ccRadioAntCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioAntCorrection.setStatus("current")


class _CcRadioIndoor_Type(DisplayString):
    """Custom type ccRadioIndoor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcRadioIndoor_Type.__name__ = "DisplayString"
_CcRadioIndoor_Object = MibTableColumn
ccRadioIndoor = _CcRadioIndoor_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 65),
    _CcRadioIndoor_Type()
)
ccRadioIndoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioIndoor.setStatus("current")


class _CcRadioDFS_Type(DisplayString):
    """Custom type ccRadioDFS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadioDFS_Type.__name__ = "DisplayString"
_CcRadioDFS_Object = MibTableColumn
ccRadioDFS = _CcRadioDFS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 66),
    _CcRadioDFS_Type()
)
ccRadioDFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioDFS.setStatus("current")


class _CcRadioTPC_Type(DisplayString):
    """Custom type ccRadioTPC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadioTPC_Type.__name__ = "DisplayString"
_CcRadioTPC_Object = MibTableColumn
ccRadioTPC = _CcRadioTPC_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 67),
    _CcRadioTPC_Type()
)
ccRadioTPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioTPC.setStatus("current")


class _CcRadioRadarChannels_Type(DisplayString):
    """Custom type ccRadioRadarChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcRadioRadarChannels_Type.__name__ = "DisplayString"
_CcRadioRadarChannels_Object = MibTableColumn
ccRadioRadarChannels = _CcRadioRadarChannels_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 68),
    _CcRadioRadarChannels_Type()
)
ccRadioRadarChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadioRadarChannels.setStatus("current")
_CcDetectorAp_Type = TruthValue
_CcDetectorAp_Object = MibTableColumn
ccDetectorAp = _CcDetectorAp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 69),
    _CcDetectorAp_Type()
)
ccDetectorAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDetectorAp.setStatus("current")


class _CcRadioMaxMUs_Type(Integer32):
    """Custom type ccRadioMaxMUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CcRadioMaxMUs_Type.__name__ = "Integer32"
_CcRadioMaxMUs_Object = MibTableColumn
ccRadioMaxMUs = _CcRadioMaxMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 70),
    _CcRadioMaxMUs_Type()
)
ccRadioMaxMUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioMaxMUs.setStatus("current")
_CcSimulateRadar_Type = DoActionNow
_CcSimulateRadar_Object = MibTableColumn
ccSimulateRadar = _CcSimulateRadar_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 71),
    _CcSimulateRadar_Type()
)
ccSimulateRadar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSimulateRadar.setStatus("current")
_CcRadioUser802x_Type = OctetString
_CcRadioUser802x_Object = MibTableColumn
ccRadioUser802x = _CcRadioUser802x_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 10, 1, 72),
    _CcRadioUser802x_Type()
)
ccRadioUser802x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadioUser802x.setStatus("current")
_CcAPPolicyTable_Object = MibTable
ccAPPolicyTable = _CcAPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11)
)
if mibBuilder.loadTexts:
    ccAPPolicyTable.setStatus("current")
_CcAPPolicyEntry_Object = MibTableRow
ccAPPolicyEntry = _CcAPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1)
)
ccAPPolicyEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyIndex"),
)
if mibBuilder.loadTexts:
    ccAPPolicyEntry.setStatus("current")


class _CcAPPolicyIndex_Type(Integer32):
    """Custom type ccAPPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcAPPolicyIndex_Type.__name__ = "Integer32"
_CcAPPolicyIndex_Object = MibTableColumn
ccAPPolicyIndex = _CcAPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 1),
    _CcAPPolicyIndex_Type()
)
ccAPPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAPPolicyIndex.setStatus("current")
_CcAPPolicyName_Type = DisplayString
_CcAPPolicyName_Object = MibTableColumn
ccAPPolicyName = _CcAPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 2),
    _CcAPPolicyName_Type()
)
ccAPPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyName.setStatus("current")


class _CcAPPolicyDesc_Type(DisplayString):
    """Custom type ccAPPolicyDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAPPolicyDesc_Type.__name__ = "DisplayString"
_CcAPPolicyDesc_Object = MibTableColumn
ccAPPolicyDesc = _CcAPPolicyDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 3),
    _CcAPPolicyDesc_Type()
)
ccAPPolicyDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyDesc.setStatus("current")


class _CcAPPolicyPreAmble_Type(DisplayString):
    """Custom type ccAPPolicyPreAmble based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_CcAPPolicyPreAmble_Type.__name__ = "DisplayString"
_CcAPPolicyPreAmble_Object = MibTableColumn
ccAPPolicyPreAmble = _CcAPPolicyPreAmble_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 10),
    _CcAPPolicyPreAmble_Type()
)
ccAPPolicyPreAmble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyPreAmble.setStatus("current")


class _CcAPPolicyBeaconInterval_Type(Integer32):
    """Custom type ccAPPolicyBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_CcAPPolicyBeaconInterval_Type.__name__ = "Integer32"
_CcAPPolicyBeaconInterval_Object = MibTableColumn
ccAPPolicyBeaconInterval = _CcAPPolicyBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 11),
    _CcAPPolicyBeaconInterval_Type()
)
ccAPPolicyBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyBeaconInterval.setStatus("current")


class _CcAPPolicyRTSThreshold_Type(Integer32):
    """Custom type ccAPPolicyRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_CcAPPolicyRTSThreshold_Type.__name__ = "Integer32"
_CcAPPolicyRTSThreshold_Object = MibTableColumn
ccAPPolicyRTSThreshold = _CcAPPolicyRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 12),
    _CcAPPolicyRTSThreshold_Type()
)
ccAPPolicyRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyRTSThreshold.setStatus("current")


class _CcAPPolicyDTIM_Type(Integer32):
    """Custom type ccAPPolicyDTIM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CcAPPolicyDTIM_Type.__name__ = "Integer32"
_CcAPPolicyDTIM_Object = MibTableColumn
ccAPPolicyDTIM = _CcAPPolicyDTIM_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 13),
    _CcAPPolicyDTIM_Type()
)
ccAPPolicyDTIM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyDTIM.setStatus("current")


class _CcAPPolicyBasicRates11a_Type(DisplayString):
    """Custom type ccAPPolicyBasicRates11a based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicyBasicRates11a_Type.__name__ = "DisplayString"
_CcAPPolicyBasicRates11a_Object = MibTableColumn
ccAPPolicyBasicRates11a = _CcAPPolicyBasicRates11a_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 14),
    _CcAPPolicyBasicRates11a_Type()
)
ccAPPolicyBasicRates11a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyBasicRates11a.setStatus("current")


class _CcAPPolicySupportedRates11a_Type(DisplayString):
    """Custom type ccAPPolicySupportedRates11a based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicySupportedRates11a_Type.__name__ = "DisplayString"
_CcAPPolicySupportedRates11a_Object = MibTableColumn
ccAPPolicySupportedRates11a = _CcAPPolicySupportedRates11a_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 15),
    _CcAPPolicySupportedRates11a_Type()
)
ccAPPolicySupportedRates11a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicySupportedRates11a.setStatus("current")


class _CcAPPolicyBasicRates11b_Type(DisplayString):
    """Custom type ccAPPolicyBasicRates11b based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicyBasicRates11b_Type.__name__ = "DisplayString"
_CcAPPolicyBasicRates11b_Object = MibTableColumn
ccAPPolicyBasicRates11b = _CcAPPolicyBasicRates11b_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 16),
    _CcAPPolicyBasicRates11b_Type()
)
ccAPPolicyBasicRates11b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyBasicRates11b.setStatus("current")


class _CcAPPolicySupportedRates11b_Type(DisplayString):
    """Custom type ccAPPolicySupportedRates11b based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicySupportedRates11b_Type.__name__ = "DisplayString"
_CcAPPolicySupportedRates11b_Object = MibTableColumn
ccAPPolicySupportedRates11b = _CcAPPolicySupportedRates11b_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 17),
    _CcAPPolicySupportedRates11b_Type()
)
ccAPPolicySupportedRates11b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicySupportedRates11b.setStatus("current")


class _CcAPPolicyBasicRatesFH_Type(DisplayString):
    """Custom type ccAPPolicyBasicRatesFH based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicyBasicRatesFH_Type.__name__ = "DisplayString"
_CcAPPolicyBasicRatesFH_Object = MibTableColumn
ccAPPolicyBasicRatesFH = _CcAPPolicyBasicRatesFH_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 18),
    _CcAPPolicyBasicRatesFH_Type()
)
ccAPPolicyBasicRatesFH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyBasicRatesFH.setStatus("current")


class _CcAPPolicySupportedRatesFH_Type(DisplayString):
    """Custom type ccAPPolicySupportedRatesFH based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicySupportedRatesFH_Type.__name__ = "DisplayString"
_CcAPPolicySupportedRatesFH_Object = MibTableColumn
ccAPPolicySupportedRatesFH = _CcAPPolicySupportedRatesFH_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 19),
    _CcAPPolicySupportedRatesFH_Type()
)
ccAPPolicySupportedRatesFH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicySupportedRatesFH.setStatus("current")


class _CcAPPolicyBasicRates11g_Type(DisplayString):
    """Custom type ccAPPolicyBasicRates11g based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicyBasicRates11g_Type.__name__ = "DisplayString"
_CcAPPolicyBasicRates11g_Object = MibTableColumn
ccAPPolicyBasicRates11g = _CcAPPolicyBasicRates11g_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 20),
    _CcAPPolicyBasicRates11g_Type()
)
ccAPPolicyBasicRates11g.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyBasicRates11g.setStatus("current")


class _CcAPPolicySupportedRates11g_Type(DisplayString):
    """Custom type ccAPPolicySupportedRates11g based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicySupportedRates11g_Type.__name__ = "DisplayString"
_CcAPPolicySupportedRates11g_Object = MibTableColumn
ccAPPolicySupportedRates11g = _CcAPPolicySupportedRates11g_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 21),
    _CcAPPolicySupportedRates11g_Type()
)
ccAPPolicySupportedRates11g.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicySupportedRates11g.setStatus("current")


class _CcAPPolicyNonSpectrumMgmt_Type(DisplayString):
    """Custom type ccAPPolicyNonSpectrumMgmt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicyNonSpectrumMgmt_Type.__name__ = "DisplayString"
_CcAPPolicyNonSpectrumMgmt_Object = MibTableColumn
ccAPPolicyNonSpectrumMgmt = _CcAPPolicyNonSpectrumMgmt_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 22),
    _CcAPPolicyNonSpectrumMgmt_Type()
)
ccAPPolicyNonSpectrumMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyNonSpectrumMgmt.setStatus("current")


class _CcAPPolicyAddAllWlan_Type(DisplayString):
    """Custom type ccAPPolicyAddAllWlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcAPPolicyAddAllWlan_Type.__name__ = "DisplayString"
_CcAPPolicyAddAllWlan_Object = MibTableColumn
ccAPPolicyAddAllWlan = _CcAPPolicyAddAllWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 23),
    _CcAPPolicyAddAllWlan_Type()
)
ccAPPolicyAddAllWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyAddAllWlan.setStatus("current")


class _CcAPPolicyRemAllWlan_Type(DisplayString):
    """Custom type ccAPPolicyRemAllWlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcAPPolicyRemAllWlan_Type.__name__ = "DisplayString"
_CcAPPolicyRemAllWlan_Object = MibTableColumn
ccAPPolicyRemAllWlan = _CcAPPolicyRemAllWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 24),
    _CcAPPolicyRemAllWlan_Type()
)
ccAPPolicyRemAllWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyRemAllWlan.setStatus("current")
_CcAPPolicyWMEEnable_Type = DisplayString
_CcAPPolicyWMEEnable_Object = MibTableColumn
ccAPPolicyWMEEnable = _CcAPPolicyWMEEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 25),
    _CcAPPolicyWMEEnable_Type()
)
ccAPPolicyWMEEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyWMEEnable.setStatus("current")
_CcAPPolicyWMEProfile_Type = DisplayString
_CcAPPolicyWMEProfile_Object = MibTableColumn
ccAPPolicyWMEProfile = _CcAPPolicyWMEProfile_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 26),
    _CcAPPolicyWMEProfile_Type()
)
ccAPPolicyWMEProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyWMEProfile.setStatus("current")


class _CcAPPolicyDTIM2_Type(Integer32):
    """Custom type ccAPPolicyDTIM2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcAPPolicyDTIM2_Type.__name__ = "Integer32"
_CcAPPolicyDTIM2_Object = MibTableColumn
ccAPPolicyDTIM2 = _CcAPPolicyDTIM2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 27),
    _CcAPPolicyDTIM2_Type()
)
ccAPPolicyDTIM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyDTIM2.setStatus("current")


class _CcAPPolicyDTIM3_Type(Integer32):
    """Custom type ccAPPolicyDTIM3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcAPPolicyDTIM3_Type.__name__ = "Integer32"
_CcAPPolicyDTIM3_Object = MibTableColumn
ccAPPolicyDTIM3 = _CcAPPolicyDTIM3_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 28),
    _CcAPPolicyDTIM3_Type()
)
ccAPPolicyDTIM3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyDTIM3.setStatus("current")


class _CcAPPolicyDTIM4_Type(Integer32):
    """Custom type ccAPPolicyDTIM4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcAPPolicyDTIM4_Type.__name__ = "Integer32"
_CcAPPolicyDTIM4_Object = MibTableColumn
ccAPPolicyDTIM4 = _CcAPPolicyDTIM4_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 11, 1, 29),
    _CcAPPolicyDTIM4_Type()
)
ccAPPolicyDTIM4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyDTIM4.setStatus("current")
_CcEPTable_Object = MibTable
ccEPTable = _CcEPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12)
)
if mibBuilder.loadTexts:
    ccEPTable.setStatus("current")
_CcEPEntry_Object = MibTableRow
ccEPEntry = _CcEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1)
)
ccEPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccEPIndex"),
)
if mibBuilder.loadTexts:
    ccEPEntry.setStatus("current")


class _CcEPIndex_Type(Integer32):
    """Custom type ccEPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcEPIndex_Type.__name__ = "Integer32"
_CcEPIndex_Object = MibTableColumn
ccEPIndex = _CcEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 1),
    _CcEPIndex_Type()
)
ccEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPIndex.setStatus("current")


class _CcEPNic_Type(Integer32):
    """Custom type ccEPNic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcEPNic_Type.__name__ = "Integer32"
_CcEPNic_Object = MibTableColumn
ccEPNic = _CcEPNic_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 2),
    _CcEPNic_Type()
)
ccEPNic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPNic.setStatus("current")


class _CcEPName_Type(DisplayString):
    """Custom type ccEPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcEPName_Type.__name__ = "DisplayString"
_CcEPName_Object = MibTableColumn
ccEPName = _CcEPName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 3),
    _CcEPName_Type()
)
ccEPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPName.setStatus("current")


class _CcEPDesc_Type(DisplayString):
    """Custom type ccEPDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcEPDesc_Type.__name__ = "DisplayString"
_CcEPDesc_Object = MibTableColumn
ccEPDesc = _CcEPDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 4),
    _CcEPDesc_Type()
)
ccEPDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDesc.setStatus("current")
_CcEPMacAddr_Type = DisplayString
_CcEPMacAddr_Object = MibTableColumn
ccEPMacAddr = _CcEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 5),
    _CcEPMacAddr_Type()
)
ccEPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPMacAddr.setStatus("current")
_CcEPEnable_Type = DisplayString
_CcEPEnable_Object = MibTableColumn
ccEPEnable = _CcEPEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 6),
    _CcEPEnable_Type()
)
ccEPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPEnable.setStatus("current")


class _CcEPSpeed_Type(Integer32):
    """Custom type ccEPSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcEPSpeed_Type.__name__ = "Integer32"
_CcEPSpeed_Object = MibTableColumn
ccEPSpeed = _CcEPSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 7),
    _CcEPSpeed_Type()
)
ccEPSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPSpeed.setStatus("deprecated")
_CcEPEnableDHCP_Type = TruthValue
_CcEPEnableDHCP_Object = MibTableColumn
ccEPEnableDHCP = _CcEPEnableDHCP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 8),
    _CcEPEnableDHCP_Type()
)
ccEPEnableDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPEnableDHCP.setStatus("current")
_CcEPIPAddr_Type = IpAddress
_CcEPIPAddr_Object = MibTableColumn
ccEPIPAddr = _CcEPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 9),
    _CcEPIPAddr_Type()
)
ccEPIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPIPAddr.setStatus("current")
_CcEPNetMask_Type = IpAddress
_CcEPNetMask_Object = MibTableColumn
ccEPNetMask = _CcEPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 10),
    _CcEPNetMask_Type()
)
ccEPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPNetMask.setStatus("current")


class _CcEPDnsCount_Type(Integer32):
    """Custom type ccEPDnsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CcEPDnsCount_Type.__name__ = "Integer32"
_CcEPDnsCount_Object = MibTableColumn
ccEPDnsCount = _CcEPDnsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 13),
    _CcEPDnsCount_Type()
)
ccEPDnsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPDnsCount.setStatus("current")


class _CcEPDnsList_Type(DisplayString):
    """Custom type ccEPDnsList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1042),
    )


_CcEPDnsList_Type.__name__ = "DisplayString"
_CcEPDnsList_Object = MibTableColumn
ccEPDnsList = _CcEPDnsList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 14),
    _CcEPDnsList_Type()
)
ccEPDnsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPDnsList.setStatus("current")


class _CcEPPrimaryVid_Type(Integer32):
    """Custom type ccEPPrimaryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CcEPPrimaryVid_Type.__name__ = "Integer32"
_CcEPPrimaryVid_Object = MibTableColumn
ccEPPrimaryVid = _CcEPPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 15),
    _CcEPPrimaryVid_Type()
)
ccEPPrimaryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPrimaryVid.setStatus("current")
_CcEPOnline_Type = TruthValue
_CcEPOnline_Object = MibTableColumn
ccEPOnline = _CcEPOnline_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 16),
    _CcEPOnline_Type()
)
ccEPOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPOnline.setStatus("current")


class _CcEPDisplayName_Type(DisplayString):
    """Custom type ccEPDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcEPDisplayName_Type.__name__ = "DisplayString"
_CcEPDisplayName_Object = MibTableColumn
ccEPDisplayName = _CcEPDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 17),
    _CcEPDisplayName_Type()
)
ccEPDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPDisplayName.setStatus("current")


class _CcEPUptime_Type(DisplayString):
    """Custom type ccEPUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcEPUptime_Type.__name__ = "DisplayString"
_CcEPUptime_Object = MibTableColumn
ccEPUptime = _CcEPUptime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 18),
    _CcEPUptime_Type()
)
ccEPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPUptime.setStatus("current")
_CcEPTx_Type = Counter32
_CcEPTx_Object = MibTableColumn
ccEPTx = _CcEPTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 19),
    _CcEPTx_Type()
)
ccEPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPTx.setStatus("current")
_CcEPRx_Type = Counter32
_CcEPRx_Object = MibTableColumn
ccEPRx = _CcEPRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 20),
    _CcEPRx_Type()
)
ccEPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPRx.setStatus("current")


class _CcEPDomain_Type(DisplayString):
    """Custom type ccEPDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcEPDomain_Type.__name__ = "DisplayString"
_CcEPDomain_Object = MibTableColumn
ccEPDomain = _CcEPDomain_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 21),
    _CcEPDomain_Type()
)
ccEPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDomain.setStatus("current")
_CcEPGateway_Type = IpAddress
_CcEPGateway_Object = MibTableColumn
ccEPGateway = _CcEPGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 22),
    _CcEPGateway_Type()
)
ccEPGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPGateway.setStatus("current")


class _CcEPCFGMode_Type(DisplayString):
    """Custom type ccEPCFGMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_CcEPCFGMode_Type.__name__ = "DisplayString"
_CcEPCFGMode_Object = MibTableColumn
ccEPCFGMode = _CcEPCFGMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 23),
    _CcEPCFGMode_Type()
)
ccEPCFGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPCFGMode.setStatus("current")


class _CcEPDuplex_Type(DisplayString):
    """Custom type ccEPDuplex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_CcEPDuplex_Type.__name__ = "DisplayString"
_CcEPDuplex_Object = MibTableColumn
ccEPDuplex = _CcEPDuplex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 24),
    _CcEPDuplex_Type()
)
ccEPDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPDuplex.setStatus("current")


class _CcEPMode_Type(DisplayString):
    """Custom type ccEPMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_CcEPMode_Type.__name__ = "DisplayString"
_CcEPMode_Object = MibTableColumn
ccEPMode = _CcEPMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 25),
    _CcEPMode_Type()
)
ccEPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPMode.setStatus("current")
_CcEPDhcpPriVlan_Type = TruthValue
_CcEPDhcpPriVlan_Object = MibTableColumn
ccEPDhcpPriVlan = _CcEPDhcpPriVlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 26),
    _CcEPDhcpPriVlan_Type()
)
ccEPDhcpPriVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDhcpPriVlan.setStatus("current")
_CcEPDDNSStatus_Type = TruthValue
_CcEPDDNSStatus_Object = MibTableColumn
ccEPDDNSStatus = _CcEPDDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 27),
    _CcEPDDNSStatus_Type()
)
ccEPDDNSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDDNSStatus.setStatus("current")
_CcEPDDNSttl_Type = Integer32
_CcEPDDNSttl_Object = MibTableColumn
ccEPDDNSttl = _CcEPDDNSttl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 28),
    _CcEPDDNSttl_Type()
)
ccEPDDNSttl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDDNSttl.setStatus("current")
_CcEPDDNSUpdateAll_Type = DisplayString
_CcEPDDNSUpdateAll_Object = MibTableColumn
ccEPDDNSUpdateAll = _CcEPDDNSUpdateAll_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 29),
    _CcEPDDNSUpdateAll_Type()
)
ccEPDDNSUpdateAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDDNSUpdateAll.setStatus("current")
_CcEPDDNSMUserStatus_Type = TruthValue
_CcEPDDNSMUserStatus_Object = MibTableColumn
ccEPDDNSMUserStatus = _CcEPDDNSMUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 30),
    _CcEPDDNSMUserStatus_Type()
)
ccEPDDNSMUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDDNSMUserStatus.setStatus("current")
_CcEPDDNSDomainName_Type = DisplayString
_CcEPDDNSDomainName_Object = MibTableColumn
ccEPDDNSDomainName = _CcEPDDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 12, 1, 31),
    _CcEPDDNSDomainName_Type()
)
ccEPDDNSDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPDDNSDomainName.setStatus("current")
_CcEPPTable_Object = MibTable
ccEPPTable = _CcEPPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13)
)
if mibBuilder.loadTexts:
    ccEPPTable.setStatus("current")
_CcEPPEntry_Object = MibTableRow
ccEPPEntry = _CcEPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1)
)
ccEPPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccEPPIndex"),
)
if mibBuilder.loadTexts:
    ccEPPEntry.setStatus("current")


class _CcEPPIndex_Type(Integer32):
    """Custom type ccEPPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcEPPIndex_Type.__name__ = "Integer32"
_CcEPPIndex_Object = MibTableColumn
ccEPPIndex = _CcEPPIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 1),
    _CcEPPIndex_Type()
)
ccEPPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPPIndex.setStatus("current")


class _CcEPPName_Type(DisplayString):
    """Custom type ccEPPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcEPPName_Type.__name__ = "DisplayString"
_CcEPPName_Object = MibTableColumn
ccEPPName = _CcEPPName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 2),
    _CcEPPName_Type()
)
ccEPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPPName.setStatus("current")


class _CcEPPAlias_Type(DisplayString):
    """Custom type ccEPPAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcEPPAlias_Type.__name__ = "DisplayString"
_CcEPPAlias_Object = MibTableColumn
ccEPPAlias = _CcEPPAlias_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 3),
    _CcEPPAlias_Type()
)
ccEPPAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPAlias.setStatus("current")


class _CcEPPDesc_Type(DisplayString):
    """Custom type ccEPPDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcEPPDesc_Type.__name__ = "DisplayString"
_CcEPPDesc_Object = MibTableColumn
ccEPPDesc = _CcEPPDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 4),
    _CcEPPDesc_Type()
)
ccEPPDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPDesc.setStatus("current")


class _CcEPPRonnic_Type(Integer32):
    """Custom type ccEPPRonnic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CcEPPRonnic_Type.__name__ = "Integer32"
_CcEPPRonnic_Object = MibTableColumn
ccEPPRonnic = _CcEPPRonnic_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 5),
    _CcEPPRonnic_Type()
)
ccEPPRonnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPRonnic.setStatus("current")


class _CcEPPVlanCount_Type(Integer32):
    """Custom type ccEPPVlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CcEPPVlanCount_Type.__name__ = "Integer32"
_CcEPPVlanCount_Object = MibTableColumn
ccEPPVlanCount = _CcEPPVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 6),
    _CcEPPVlanCount_Type()
)
ccEPPVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPPVlanCount.setStatus("current")


class _CcEPPVlanList_Type(DisplayString):
    """Custom type ccEPPVlanList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CcEPPVlanList_Type.__name__ = "DisplayString"
_CcEPPVlanList_Object = MibTableColumn
ccEPPVlanList = _CcEPPVlanList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 7),
    _CcEPPVlanList_Type()
)
ccEPPVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccEPPVlanList.setStatus("current")


class _CcEPPCreateNewVlan_Type(DisplayString):
    """Custom type ccEPPCreateNewVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcEPPCreateNewVlan_Type.__name__ = "DisplayString"
_CcEPPCreateNewVlan_Object = MibTableColumn
ccEPPCreateNewVlan = _CcEPPCreateNewVlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 8),
    _CcEPPCreateNewVlan_Type()
)
ccEPPCreateNewVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPCreateNewVlan.setStatus("current")


class _CcEPPRemVlan_Type(DisplayString):
    """Custom type ccEPPRemVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcEPPRemVlan_Type.__name__ = "DisplayString"
_CcEPPRemVlan_Object = MibTableColumn
ccEPPRemVlan = _CcEPPRemVlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 9),
    _CcEPPRemVlan_Type()
)
ccEPPRemVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPRemVlan.setStatus("current")
_CcEPPDropVlan_Type = TruthValue
_CcEPPDropVlan_Object = MibTableColumn
ccEPPDropVlan = _CcEPPDropVlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 13, 1, 10),
    _CcEPPDropVlan_Type()
)
ccEPPDropVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccEPPDropVlan.setStatus("current")
_Ccdot11FHPhyTable_Object = MibTable
ccdot11FHPhyTable = _Ccdot11FHPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14)
)
if mibBuilder.loadTexts:
    ccdot11FHPhyTable.setStatus("current")
_Ccdot11FHPhyEntry_Object = MibTableRow
ccdot11FHPhyEntry = _Ccdot11FHPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1)
)
ccdot11FHPhyEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccdot11FHIndex"),
)
if mibBuilder.loadTexts:
    ccdot11FHPhyEntry.setStatus("current")


class _Ccdot11FHIndex_Type(Integer32):
    """Custom type ccdot11FHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ccdot11FHIndex_Type.__name__ = "Integer32"
_Ccdot11FHIndex_Object = MibTableColumn
ccdot11FHIndex = _Ccdot11FHIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 1),
    _Ccdot11FHIndex_Type()
)
ccdot11FHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccdot11FHIndex.setStatus("current")
_Ccdot11FHHopTime_Type = Integer32
_Ccdot11FHHopTime_Object = MibTableColumn
ccdot11FHHopTime = _Ccdot11FHHopTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 2),
    _Ccdot11FHHopTime_Type()
)
ccdot11FHHopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdot11FHHopTime.setStatus("current")
_Ccdot11FHCurrentChannelNumber_Type = Integer32
_Ccdot11FHCurrentChannelNumber_Object = MibTableColumn
ccdot11FHCurrentChannelNumber = _Ccdot11FHCurrentChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 3),
    _Ccdot11FHCurrentChannelNumber_Type()
)
ccdot11FHCurrentChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdot11FHCurrentChannelNumber.setStatus("current")
_Ccdot11FHMaxDwellTime_Type = Integer32
_Ccdot11FHMaxDwellTime_Object = MibTableColumn
ccdot11FHMaxDwellTime = _Ccdot11FHMaxDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 4),
    _Ccdot11FHMaxDwellTime_Type()
)
ccdot11FHMaxDwellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdot11FHMaxDwellTime.setStatus("current")
_Ccdot11FHCurrentDwellTime_Type = Integer32
_Ccdot11FHCurrentDwellTime_Object = MibTableColumn
ccdot11FHCurrentDwellTime = _Ccdot11FHCurrentDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 5),
    _Ccdot11FHCurrentDwellTime_Type()
)
ccdot11FHCurrentDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccdot11FHCurrentDwellTime.setStatus("current")
_Ccdot11FHCurrentSet_Type = Integer32
_Ccdot11FHCurrentSet_Object = MibTableColumn
ccdot11FHCurrentSet = _Ccdot11FHCurrentSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 6),
    _Ccdot11FHCurrentSet_Type()
)
ccdot11FHCurrentSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccdot11FHCurrentSet.setStatus("current")
_Ccdot11FHCurrentPattern_Type = Integer32
_Ccdot11FHCurrentPattern_Object = MibTableColumn
ccdot11FHCurrentPattern = _Ccdot11FHCurrentPattern_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 7),
    _Ccdot11FHCurrentPattern_Type()
)
ccdot11FHCurrentPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccdot11FHCurrentPattern.setStatus("current")
_Ccdot11FHCurrentIndex_Type = Integer32
_Ccdot11FHCurrentIndex_Object = MibTableColumn
ccdot11FHCurrentIndex = _Ccdot11FHCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 14, 1, 8),
    _Ccdot11FHCurrentIndex_Type()
)
ccdot11FHCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdot11FHCurrentIndex.setStatus("current")
_CcAPPolicyObjects_ObjectIdentity = ObjectIdentity
ccAPPolicyObjects = _CcAPPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16)
)
_CcAPPolicyAddRemWLANTable_Object = MibTable
ccAPPolicyAddRemWLANTable = _CcAPPolicyAddRemWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2)
)
if mibBuilder.loadTexts:
    ccAPPolicyAddRemWLANTable.setStatus("current")
_CcAPPolicyAddRemWLANEntry_Object = MibTableRow
ccAPPolicyAddRemWLANEntry = _CcAPPolicyAddRemWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2, 1)
)
ccAPPolicyAddRemWLANEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyDeviceType"),
)
if mibBuilder.loadTexts:
    ccAPPolicyAddRemWLANEntry.setStatus("current")


class _CcAPPolicyDeviceType_Type(Integer32):
    """Custom type ccAPPolicyDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcAPPolicyDeviceType_Type.__name__ = "Integer32"
_CcAPPolicyDeviceType_Object = MibTableColumn
ccAPPolicyDeviceType = _CcAPPolicyDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2, 1, 1),
    _CcAPPolicyDeviceType_Type()
)
ccAPPolicyDeviceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAPPolicyDeviceType.setStatus("current")


class _CcAPPolicyAddWLAN_Type(DisplayString):
    """Custom type ccAPPolicyAddWLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcAPPolicyAddWLAN_Type.__name__ = "DisplayString"
_CcAPPolicyAddWLAN_Object = MibTableColumn
ccAPPolicyAddWLAN = _CcAPPolicyAddWLAN_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2, 1, 2),
    _CcAPPolicyAddWLAN_Type()
)
ccAPPolicyAddWLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAPPolicyAddWLAN.setStatus("deprecated")


class _CcAPPolicyRemWLAN_Type(DisplayString):
    """Custom type ccAPPolicyRemWLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcAPPolicyRemWLAN_Type.__name__ = "DisplayString"
_CcAPPolicyRemWLAN_Object = MibTableColumn
ccAPPolicyRemWLAN = _CcAPPolicyRemWLAN_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2, 1, 3),
    _CcAPPolicyRemWLAN_Type()
)
ccAPPolicyRemWLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAPPolicyRemWLAN.setStatus("deprecated")


class _CcAPPolicySelectWLAN_Type(DisplayString):
    """Custom type ccAPPolicySelectWLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcAPPolicySelectWLAN_Type.__name__ = "DisplayString"
_CcAPPolicySelectWLAN_Object = MibTableColumn
ccAPPolicySelectWLAN = _CcAPPolicySelectWLAN_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2, 1, 4),
    _CcAPPolicySelectWLAN_Type()
)
ccAPPolicySelectWLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicySelectWLAN.setStatus("current")


class _CcAPPolicyUnselectWLAN_Type(DisplayString):
    """Custom type ccAPPolicyUnselectWLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcAPPolicyUnselectWLAN_Type.__name__ = "DisplayString"
_CcAPPolicyUnselectWLAN_Object = MibTableColumn
ccAPPolicyUnselectWLAN = _CcAPPolicyUnselectWLAN_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 2, 1, 5),
    _CcAPPolicyUnselectWLAN_Type()
)
ccAPPolicyUnselectWLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyUnselectWLAN.setStatus("current")
_CcAPPolicyWLANTable_Object = MibTable
ccAPPolicyWLANTable = _CcAPPolicyWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3)
)
if mibBuilder.loadTexts:
    ccAPPolicyWLANTable.setStatus("current")
_CcAPPolicyWLANEntry_Object = MibTableRow
ccAPPolicyWLANEntry = _CcAPPolicyWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3, 1)
)
ccAPPolicyWLANEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyDeviceType"),
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyWLANIndex"),
)
if mibBuilder.loadTexts:
    ccAPPolicyWLANEntry.setStatus("current")


class _CcAPPolicyWLANIndex_Type(Integer32):
    """Custom type ccAPPolicyWLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcAPPolicyWLANIndex_Type.__name__ = "Integer32"
_CcAPPolicyWLANIndex_Object = MibTableColumn
ccAPPolicyWLANIndex = _CcAPPolicyWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3, 1, 1),
    _CcAPPolicyWLANIndex_Type()
)
ccAPPolicyWLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAPPolicyWLANIndex.setStatus("current")


class _CcAPPolicyWLAN_Type(DisplayString):
    """Custom type ccAPPolicyWLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcAPPolicyWLAN_Type.__name__ = "DisplayString"
_CcAPPolicyWLAN_Object = MibTableColumn
ccAPPolicyWLAN = _CcAPPolicyWLAN_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3, 1, 2),
    _CcAPPolicyWLAN_Type()
)
ccAPPolicyWLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAPPolicyWLAN.setStatus("current")


class _CcAPPolicyWLANBW_Type(DisplayString):
    """Custom type ccAPPolicyWLANBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcAPPolicyWLANBW_Type.__name__ = "DisplayString"
_CcAPPolicyWLANBW_Object = MibTableColumn
ccAPPolicyWLANBW = _CcAPPolicyWLANBW_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3, 1, 3),
    _CcAPPolicyWLANBW_Type()
)
ccAPPolicyWLANBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyWLANBW.setStatus("current")


class _CcAPPolicyWLANNP_Type(DisplayString):
    """Custom type ccAPPolicyWLANNP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CcAPPolicyWLANNP_Type.__name__ = "DisplayString"
_CcAPPolicyWLANNP_Object = MibTableColumn
ccAPPolicyWLANNP = _CcAPPolicyWLANNP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3, 1, 4),
    _CcAPPolicyWLANNP_Type()
)
ccAPPolicyWLANNP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyWLANNP.setStatus("current")


class _CcAPPolicyWLANBSS_Type(DisplayString):
    """Custom type ccAPPolicyWLANBSS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcAPPolicyWLANBSS_Type.__name__ = "DisplayString"
_CcAPPolicyWLANBSS_Object = MibTableColumn
ccAPPolicyWLANBSS = _CcAPPolicyWLANBSS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 3, 1, 5),
    _CcAPPolicyWLANBSS_Type()
)
ccAPPolicyWLANBSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyWLANBSS.setStatus("current")
_CcAPPolicyBSSTable_Object = MibTable
ccAPPolicyBSSTable = _CcAPPolicyBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 4)
)
if mibBuilder.loadTexts:
    ccAPPolicyBSSTable.setStatus("current")
_CcAPPolicyBSSEntry_Object = MibTableRow
ccAPPolicyBSSEntry = _CcAPPolicyBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 4, 1)
)
ccAPPolicyBSSEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyDeviceType"),
    (0, "SYMBOL-WS5000-MIB", "ccAPPolicyBSS"),
)
if mibBuilder.loadTexts:
    ccAPPolicyBSSEntry.setStatus("current")


class _CcAPPolicyBSS_Type(DisplayString):
    """Custom type ccAPPolicyBSS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CcAPPolicyBSS_Type.__name__ = "DisplayString"
_CcAPPolicyBSS_Object = MibTableColumn
ccAPPolicyBSS = _CcAPPolicyBSS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 4, 1, 1),
    _CcAPPolicyBSS_Type()
)
ccAPPolicyBSS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAPPolicyBSS.setStatus("current")


class _CcAPPolicyPrimaryWLAN_Type(DisplayString):
    """Custom type ccAPPolicyPrimaryWLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcAPPolicyPrimaryWLAN_Type.__name__ = "DisplayString"
_CcAPPolicyPrimaryWLAN_Object = MibTableColumn
ccAPPolicyPrimaryWLAN = _CcAPPolicyPrimaryWLAN_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 16, 4, 1, 2),
    _CcAPPolicyPrimaryWLAN_Type()
)
ccAPPolicyPrimaryWLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAPPolicyPrimaryWLAN.setStatus("current")
_CcFWLANTable_Object = MibTable
ccFWLANTable = _CcFWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17)
)
if mibBuilder.loadTexts:
    ccFWLANTable.setStatus("current")
_CcFWLANEntry_Object = MibTableRow
ccFWLANEntry = _CcFWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1)
)
ccFWLANEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccEPPIndex"),
)
if mibBuilder.loadTexts:
    ccFWLANEntry.setStatus("current")


class _CcLANIndex_Type(Integer32):
    """Custom type ccLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CcLANIndex_Type.__name__ = "Integer32"
_CcLANIndex_Object = MibTableColumn
ccLANIndex = _CcLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 1),
    _CcLANIndex_Type()
)
ccLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLANIndex.setStatus("current")


class _CcLANName_Type(OctetString):
    """Custom type ccLANName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcLANName_Type.__name__ = "OctetString"
_CcLANName_Object = MibTableColumn
ccLANName = _CcLANName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 2),
    _CcLANName_Type()
)
ccLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLANName.setStatus("current")


class _CcLANDesc_Type(OctetString):
    """Custom type ccLANDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcLANDesc_Type.__name__ = "OctetString"
_CcLANDesc_Object = MibTableColumn
ccLANDesc = _CcLANDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 3),
    _CcLANDesc_Type()
)
ccLANDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANDesc.setStatus("current")


class _CcLANNATCount_Type(Integer32):
    """Custom type ccLANNATCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CcLANNATCount_Type.__name__ = "Integer32"
_CcLANNATCount_Object = MibTableColumn
ccLANNATCount = _CcLANNATCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 4),
    _CcLANNATCount_Type()
)
ccLANNATCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLANNATCount.setStatus("current")


class _CcLANAddNAT_Type(OctetString):
    """Custom type ccLANAddNAT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcLANAddNAT_Type.__name__ = "OctetString"
_CcLANAddNAT_Object = MibTableColumn
ccLANAddNAT = _CcLANAddNAT_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 5),
    _CcLANAddNAT_Type()
)
ccLANAddNAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANAddNAT.setStatus("current")


class _CcLANRemNAT_Type(OctetString):
    """Custom type ccLANRemNAT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcLANRemNAT_Type.__name__ = "OctetString"
_CcLANRemNAT_Object = MibTableColumn
ccLANRemNAT = _CcLANRemNAT_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 6),
    _CcLANRemNAT_Type()
)
ccLANRemNAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANRemNAT.setStatus("current")


class _CcLANEp_Type(Integer32):
    """Custom type ccLANEp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CcLANEp_Type.__name__ = "Integer32"
_CcLANEp_Object = MibTableColumn
ccLANEp = _CcLANEp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 7),
    _CcLANEp_Type()
)
ccLANEp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANEp.setStatus("current")


class _CcLANNp_Type(OctetString):
    """Custom type ccLANNp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcLANNp_Type.__name__ = "OctetString"
_CcLANNp_Object = MibTableColumn
ccLANNp = _CcLANNp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 8),
    _CcLANNp_Type()
)
ccLANNp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANNp.setStatus("current")


class _CcLANPfAllow_Type(DisplayString):
    """Custom type ccLANPfAllow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcLANPfAllow_Type.__name__ = "DisplayString"
_CcLANPfAllow_Object = MibTableColumn
ccLANPfAllow = _CcLANPfAllow_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 9),
    _CcLANPfAllow_Type()
)
ccLANPfAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANPfAllow.setStatus("current")
_CcLANPfDeny_Type = DisplayString
_CcLANPfDeny_Object = MibTableColumn
ccLANPfDeny = _CcLANPfDeny_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 17, 1, 10),
    _CcLANPfDeny_Type()
)
ccLANPfDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLANPfDeny.setStatus("current")
_CcFWLANNATTable_Object = MibTable
ccFWLANNATTable = _CcFWLANNATTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 18)
)
if mibBuilder.loadTexts:
    ccFWLANNATTable.setStatus("current")
_CcFWLANNATEntry_Object = MibTableRow
ccFWLANNATEntry = _CcFWLANNATEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 18, 1)
)
ccFWLANNATEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccEPPIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccLANNATIndex"),
)
if mibBuilder.loadTexts:
    ccFWLANNATEntry.setStatus("current")


class _CcLANNATIndex_Type(OctetString):
    """Custom type ccLANNATIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcLANNATIndex_Type.__name__ = "OctetString"
_CcLANNATIndex_Object = MibTableColumn
ccLANNATIndex = _CcLANNATIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 18, 1, 1),
    _CcLANNATIndex_Type()
)
ccLANNATIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLANNATIndex.setStatus("current")
_CcLANNATRemoteRealIP_Type = IpAddress
_CcLANNATRemoteRealIP_Object = MibTableColumn
ccLANNATRemoteRealIP = _CcLANNATRemoteRealIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 18, 1, 2),
    _CcLANNATRemoteRealIP_Type()
)
ccLANNATRemoteRealIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLANNATRemoteRealIP.setStatus("current")
_CcLANNATLocalNatIP_Type = IpAddress
_CcLANNATLocalNatIP_Object = MibTableColumn
ccLANNATLocalNatIP = _CcLANNATLocalNatIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 18, 1, 3),
    _CcLANNATLocalNatIP_Type()
)
ccLANNATLocalNatIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLANNATLocalNatIP.setStatus("current")
_CcRouteTable_Object = MibTable
ccRouteTable = _CcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19)
)
if mibBuilder.loadTexts:
    ccRouteTable.setStatus("current")
_CcRouteEntry_Object = MibTableRow
ccRouteEntry = _CcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1)
)
ccRouteEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRouteIndex"),
)
if mibBuilder.loadTexts:
    ccRouteEntry.setStatus("current")


class _CcRouteIndex_Type(Integer32):
    """Custom type ccRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcRouteIndex_Type.__name__ = "Integer32"
_CcRouteIndex_Object = MibTableColumn
ccRouteIndex = _CcRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 1),
    _CcRouteIndex_Type()
)
ccRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteIndex.setStatus("current")


class _CcRouteDest_Type(OctetString):
    """Custom type ccRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRouteDest_Type.__name__ = "OctetString"
_CcRouteDest_Object = MibTableColumn
ccRouteDest = _CcRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 2),
    _CcRouteDest_Type()
)
ccRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteDest.setStatus("current")


class _CcRouteGateway_Type(OctetString):
    """Custom type ccRouteGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRouteGateway_Type.__name__ = "OctetString"
_CcRouteGateway_Object = MibTableColumn
ccRouteGateway = _CcRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 3),
    _CcRouteGateway_Type()
)
ccRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteGateway.setStatus("current")


class _CcRouteFlags_Type(OctetString):
    """Custom type ccRouteFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CcRouteFlags_Type.__name__ = "OctetString"
_CcRouteFlags_Object = MibTableColumn
ccRouteFlags = _CcRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 4),
    _CcRouteFlags_Type()
)
ccRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteFlags.setStatus("current")


class _CcRouteRefs_Type(Integer32):
    """Custom type ccRouteRefs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcRouteRefs_Type.__name__ = "Integer32"
_CcRouteRefs_Object = MibTableColumn
ccRouteRefs = _CcRouteRefs_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 5),
    _CcRouteRefs_Type()
)
ccRouteRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteRefs.setStatus("current")


class _CcRouteUse_Type(Integer32):
    """Custom type ccRouteUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcRouteUse_Type.__name__ = "Integer32"
_CcRouteUse_Object = MibTableColumn
ccRouteUse = _CcRouteUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 6),
    _CcRouteUse_Type()
)
ccRouteUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteUse.setStatus("current")


class _CcRouteInterface_Type(OctetString):
    """Custom type ccRouteInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRouteInterface_Type.__name__ = "OctetString"
_CcRouteInterface_Object = MibTableColumn
ccRouteInterface = _CcRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 7),
    _CcRouteInterface_Type()
)
ccRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteInterface.setStatus("current")
_CcRouteGenMask_Type = OctetString
_CcRouteGenMask_Object = MibTableColumn
ccRouteGenMask = _CcRouteGenMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 19, 1, 8),
    _CcRouteGenMask_Type()
)
ccRouteGenMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouteGenMask.setStatus("current")


class _CcRouteAddObj_Type(OctetString):
    """Custom type ccRouteAddObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcRouteAddObj_Type.__name__ = "OctetString"
_CcRouteAddObj_Object = MibScalar
ccRouteAddObj = _CcRouteAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 20),
    _CcRouteAddObj_Type()
)
ccRouteAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouteAddObj.setStatus("current")


class _CcRouteRemObj_Type(OctetString):
    """Custom type ccRouteRemObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcRouteRemObj_Type.__name__ = "OctetString"
_CcRouteRemObj_Object = MibScalar
ccRouteRemObj = _CcRouteRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 21),
    _CcRouteRemObj_Type()
)
ccRouteRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouteRemObj.setStatus("current")
_CcRouteFlush_Type = DoActionNow
_CcRouteFlush_Object = MibScalar
ccRouteFlush = _CcRouteFlush_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 22),
    _CcRouteFlush_Type()
)
ccRouteFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouteFlush.setStatus("current")
_CcDhcpSrvNIC1_ObjectIdentity = ObjectIdentity
ccDhcpSrvNIC1 = _CcDhcpSrvNIC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23)
)


class _CcDhcp1Srv_Type(Integer32):
    """Custom type ccDhcp1Srv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CcDhcp1Srv_Type.__name__ = "Integer32"
_CcDhcp1Srv_Object = MibScalar
ccDhcp1Srv = _CcDhcp1Srv_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 1),
    _CcDhcp1Srv_Type()
)
ccDhcp1Srv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1Srv.setStatus("current")
_CcDhcp1Subnet_Type = IpAddress
_CcDhcp1Subnet_Object = MibScalar
ccDhcp1Subnet = _CcDhcp1Subnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 2),
    _CcDhcp1Subnet_Type()
)
ccDhcp1Subnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1Subnet.setStatus("current")
_CcDhcp1Netmask_Type = IpAddress
_CcDhcp1Netmask_Object = MibScalar
ccDhcp1Netmask = _CcDhcp1Netmask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 3),
    _CcDhcp1Netmask_Type()
)
ccDhcp1Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1Netmask.setStatus("current")
_CcDhcp1BcastIP_Type = IpAddress
_CcDhcp1BcastIP_Object = MibScalar
ccDhcp1BcastIP = _CcDhcp1BcastIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 4),
    _CcDhcp1BcastIP_Type()
)
ccDhcp1BcastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1BcastIP.setStatus("current")
_CcDhcp1RouterIP_Type = IpAddress
_CcDhcp1RouterIP_Object = MibScalar
ccDhcp1RouterIP = _CcDhcp1RouterIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 5),
    _CcDhcp1RouterIP_Type()
)
ccDhcp1RouterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1RouterIP.setStatus("current")
_CcDhcp1PriDNSIP_Type = IpAddress
_CcDhcp1PriDNSIP_Object = MibScalar
ccDhcp1PriDNSIP = _CcDhcp1PriDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 6),
    _CcDhcp1PriDNSIP_Type()
)
ccDhcp1PriDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1PriDNSIP.setStatus("current")
_CcDhcp1SecDNSIP_Type = IpAddress
_CcDhcp1SecDNSIP_Object = MibScalar
ccDhcp1SecDNSIP = _CcDhcp1SecDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 7),
    _CcDhcp1SecDNSIP_Type()
)
ccDhcp1SecDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1SecDNSIP.setStatus("current")


class _CcDhcp1DomainName_Type(OctetString):
    """Custom type ccDhcp1DomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcDhcp1DomainName_Type.__name__ = "OctetString"
_CcDhcp1DomainName_Object = MibScalar
ccDhcp1DomainName = _CcDhcp1DomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 8),
    _CcDhcp1DomainName_Type()
)
ccDhcp1DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1DomainName.setStatus("current")


class _CcDhcp1DefLease_Type(Integer32):
    """Custom type ccDhcp1DefLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_CcDhcp1DefLease_Type.__name__ = "Integer32"
_CcDhcp1DefLease_Object = MibScalar
ccDhcp1DefLease = _CcDhcp1DefLease_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 9),
    _CcDhcp1DefLease_Type()
)
ccDhcp1DefLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1DefLease.setStatus("current")
if mibBuilder.loadTexts:
    ccDhcp1DefLease.setUnits("seconds")


class _CcDhcp1MaxLease_Type(Integer32):
    """Custom type ccDhcp1MaxLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_CcDhcp1MaxLease_Type.__name__ = "Integer32"
_CcDhcp1MaxLease_Object = MibScalar
ccDhcp1MaxLease = _CcDhcp1MaxLease_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 10),
    _CcDhcp1MaxLease_Type()
)
ccDhcp1MaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1MaxLease.setStatus("current")
if mibBuilder.loadTexts:
    ccDhcp1MaxLease.setUnits("seconds")
_CcDhcp1IPRangeTable_Object = MibTable
ccDhcp1IPRangeTable = _CcDhcp1IPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 11)
)
if mibBuilder.loadTexts:
    ccDhcp1IPRangeTable.setStatus("current")
_CcDhcp1IPRangeEntry_Object = MibTableRow
ccDhcp1IPRangeEntry = _CcDhcp1IPRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 11, 1)
)
ccDhcp1IPRangeEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp1RangeIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp1IPRangeEntry.setStatus("current")


class _CcDhcp1RangeIndex_Type(Integer32):
    """Custom type ccDhcp1RangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp1RangeIndex_Type.__name__ = "Integer32"
_CcDhcp1RangeIndex_Object = MibTableColumn
ccDhcp1RangeIndex = _CcDhcp1RangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 11, 1, 1),
    _CcDhcp1RangeIndex_Type()
)
ccDhcp1RangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1RangeIndex.setStatus("current")


class _CcDhcp1RangeStartIP_Type(OctetString):
    """Custom type ccDhcp1RangeStartIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1RangeStartIP_Type.__name__ = "OctetString"
_CcDhcp1RangeStartIP_Object = MibTableColumn
ccDhcp1RangeStartIP = _CcDhcp1RangeStartIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 11, 1, 2),
    _CcDhcp1RangeStartIP_Type()
)
ccDhcp1RangeStartIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1RangeStartIP.setStatus("current")


class _CcDhcp1RangeEndIP_Type(OctetString):
    """Custom type ccDhcp1RangeEndIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1RangeEndIP_Type.__name__ = "OctetString"
_CcDhcp1RangeEndIP_Object = MibTableColumn
ccDhcp1RangeEndIP = _CcDhcp1RangeEndIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 11, 1, 3),
    _CcDhcp1RangeEndIP_Type()
)
ccDhcp1RangeEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1RangeEndIP.setStatus("current")


class _CcDhcp1AddIPRangeObj_Type(OctetString):
    """Custom type ccDhcp1AddIPRangeObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1AddIPRangeObj_Type.__name__ = "OctetString"
_CcDhcp1AddIPRangeObj_Object = MibScalar
ccDhcp1AddIPRangeObj = _CcDhcp1AddIPRangeObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 12),
    _CcDhcp1AddIPRangeObj_Type()
)
ccDhcp1AddIPRangeObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1AddIPRangeObj.setStatus("current")


class _CcDhcp1RemIPRangeObj_Type(OctetString):
    """Custom type ccDhcp1RemIPRangeObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1RemIPRangeObj_Type.__name__ = "OctetString"
_CcDhcp1RemIPRangeObj_Object = MibScalar
ccDhcp1RemIPRangeObj = _CcDhcp1RemIPRangeObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 13),
    _CcDhcp1RemIPRangeObj_Type()
)
ccDhcp1RemIPRangeObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1RemIPRangeObj.setStatus("current")
_CcDhcp1StaticIPTable_Object = MibTable
ccDhcp1StaticIPTable = _CcDhcp1StaticIPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 14)
)
if mibBuilder.loadTexts:
    ccDhcp1StaticIPTable.setStatus("current")
_CcDhcp1StaticIPEntry_Object = MibTableRow
ccDhcp1StaticIPEntry = _CcDhcp1StaticIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 14, 1)
)
ccDhcp1StaticIPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp1StaticIPIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp1StaticIPEntry.setStatus("current")


class _CcDhcp1StaticIPIndex_Type(Integer32):
    """Custom type ccDhcp1StaticIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp1StaticIPIndex_Type.__name__ = "Integer32"
_CcDhcp1StaticIPIndex_Object = MibTableColumn
ccDhcp1StaticIPIndex = _CcDhcp1StaticIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 14, 1, 1),
    _CcDhcp1StaticIPIndex_Type()
)
ccDhcp1StaticIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1StaticIPIndex.setStatus("current")


class _CcDhcp1StaticIP_Type(OctetString):
    """Custom type ccDhcp1StaticIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1StaticIP_Type.__name__ = "OctetString"
_CcDhcp1StaticIP_Object = MibTableColumn
ccDhcp1StaticIP = _CcDhcp1StaticIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 14, 1, 2),
    _CcDhcp1StaticIP_Type()
)
ccDhcp1StaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1StaticIP.setStatus("current")


class _CcDhcp1StaticMac_Type(OctetString):
    """Custom type ccDhcp1StaticMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1StaticMac_Type.__name__ = "OctetString"
_CcDhcp1StaticMac_Object = MibTableColumn
ccDhcp1StaticMac = _CcDhcp1StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 14, 1, 3),
    _CcDhcp1StaticMac_Type()
)
ccDhcp1StaticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1StaticMac.setStatus("current")


class _CcDhcp1StaticHost_Type(OctetString):
    """Custom type ccDhcp1StaticHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1StaticHost_Type.__name__ = "OctetString"
_CcDhcp1StaticHost_Object = MibTableColumn
ccDhcp1StaticHost = _CcDhcp1StaticHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 14, 1, 4),
    _CcDhcp1StaticHost_Type()
)
ccDhcp1StaticHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1StaticHost.setStatus("current")


class _CcDhcp1AddStaticIPObj_Type(OctetString):
    """Custom type ccDhcp1AddStaticIPObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1AddStaticIPObj_Type.__name__ = "OctetString"
_CcDhcp1AddStaticIPObj_Object = MibScalar
ccDhcp1AddStaticIPObj = _CcDhcp1AddStaticIPObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 15),
    _CcDhcp1AddStaticIPObj_Type()
)
ccDhcp1AddStaticIPObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1AddStaticIPObj.setStatus("current")


class _CcDhcp1RemStaticIPObj_Type(OctetString):
    """Custom type ccDhcp1RemStaticIPObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1RemStaticIPObj_Type.__name__ = "OctetString"
_CcDhcp1RemStaticIPObj_Object = MibScalar
ccDhcp1RemStaticIPObj = _CcDhcp1RemStaticIPObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 16),
    _CcDhcp1RemStaticIPObj_Type()
)
ccDhcp1RemStaticIPObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1RemStaticIPObj.setStatus("current")
_CcDhcp1OptionTable_Object = MibTable
ccDhcp1OptionTable = _CcDhcp1OptionTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17)
)
if mibBuilder.loadTexts:
    ccDhcp1OptionTable.setStatus("current")
_CcDhcp1OptionEntry_Object = MibTableRow
ccDhcp1OptionEntry = _CcDhcp1OptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17, 1)
)
ccDhcp1OptionEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp1OptionIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp1OptionEntry.setStatus("current")


class _CcDhcp1OptionIndex_Type(Integer32):
    """Custom type ccDhcp1OptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp1OptionIndex_Type.__name__ = "Integer32"
_CcDhcp1OptionIndex_Object = MibTableColumn
ccDhcp1OptionIndex = _CcDhcp1OptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17, 1, 1),
    _CcDhcp1OptionIndex_Type()
)
ccDhcp1OptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1OptionIndex.setStatus("current")


class _CcDhcp1OptionName_Type(OctetString):
    """Custom type ccDhcp1OptionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1OptionName_Type.__name__ = "OctetString"
_CcDhcp1OptionName_Object = MibTableColumn
ccDhcp1OptionName = _CcDhcp1OptionName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17, 1, 2),
    _CcDhcp1OptionName_Type()
)
ccDhcp1OptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1OptionName.setStatus("current")


class _CcDhcp1OptionCode_Type(OctetString):
    """Custom type ccDhcp1OptionCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1OptionCode_Type.__name__ = "OctetString"
_CcDhcp1OptionCode_Object = MibTableColumn
ccDhcp1OptionCode = _CcDhcp1OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17, 1, 3),
    _CcDhcp1OptionCode_Type()
)
ccDhcp1OptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1OptionCode.setStatus("current")


class _CcDhcp1OptionType_Type(OctetString):
    """Custom type ccDhcp1OptionType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1OptionType_Type.__name__ = "OctetString"
_CcDhcp1OptionType_Object = MibTableColumn
ccDhcp1OptionType = _CcDhcp1OptionType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17, 1, 4),
    _CcDhcp1OptionType_Type()
)
ccDhcp1OptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1OptionType.setStatus("current")


class _CcDhcp1OptionValue_Type(OctetString):
    """Custom type ccDhcp1OptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1OptionValue_Type.__name__ = "OctetString"
_CcDhcp1OptionValue_Object = MibTableColumn
ccDhcp1OptionValue = _CcDhcp1OptionValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 17, 1, 5),
    _CcDhcp1OptionValue_Type()
)
ccDhcp1OptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1OptionValue.setStatus("current")


class _CcDhcp1AddOptionObj_Type(OctetString):
    """Custom type ccDhcp1AddOptionObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1AddOptionObj_Type.__name__ = "OctetString"
_CcDhcp1AddOptionObj_Object = MibScalar
ccDhcp1AddOptionObj = _CcDhcp1AddOptionObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 18),
    _CcDhcp1AddOptionObj_Type()
)
ccDhcp1AddOptionObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1AddOptionObj.setStatus("current")


class _CcDhcp1RemOptionObj_Type(OctetString):
    """Custom type ccDhcp1RemOptionObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1RemOptionObj_Type.__name__ = "OctetString"
_CcDhcp1RemOptionObj_Object = MibScalar
ccDhcp1RemOptionObj = _CcDhcp1RemOptionObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 19),
    _CcDhcp1RemOptionObj_Type()
)
ccDhcp1RemOptionObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1RemOptionObj.setStatus("current")
_CcDhcp1LeasesTable_Object = MibTable
ccDhcp1LeasesTable = _CcDhcp1LeasesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20)
)
if mibBuilder.loadTexts:
    ccDhcp1LeasesTable.setStatus("current")
_CcDhcp1LeasesEntry_Object = MibTableRow
ccDhcp1LeasesEntry = _CcDhcp1LeasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20, 1)
)
ccDhcp1LeasesEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp1LeaseIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp1LeasesEntry.setStatus("current")


class _CcDhcp1LeaseIndex_Type(Integer32):
    """Custom type ccDhcp1LeaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp1LeaseIndex_Type.__name__ = "Integer32"
_CcDhcp1LeaseIndex_Object = MibTableColumn
ccDhcp1LeaseIndex = _CcDhcp1LeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20, 1, 1),
    _CcDhcp1LeaseIndex_Type()
)
ccDhcp1LeaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1LeaseIndex.setStatus("current")


class _CcDhcp1LeaseIP_Type(OctetString):
    """Custom type ccDhcp1LeaseIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1LeaseIP_Type.__name__ = "OctetString"
_CcDhcp1LeaseIP_Object = MibTableColumn
ccDhcp1LeaseIP = _CcDhcp1LeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20, 1, 2),
    _CcDhcp1LeaseIP_Type()
)
ccDhcp1LeaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1LeaseIP.setStatus("current")


class _CcDhcp1LeaseMac_Type(OctetString):
    """Custom type ccDhcp1LeaseMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1LeaseMac_Type.__name__ = "OctetString"
_CcDhcp1LeaseMac_Object = MibTableColumn
ccDhcp1LeaseMac = _CcDhcp1LeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20, 1, 3),
    _CcDhcp1LeaseMac_Type()
)
ccDhcp1LeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1LeaseMac.setStatus("current")


class _CcDhcp1LeaseStartTime_Type(OctetString):
    """Custom type ccDhcp1LeaseStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1LeaseStartTime_Type.__name__ = "OctetString"
_CcDhcp1LeaseStartTime_Object = MibTableColumn
ccDhcp1LeaseStartTime = _CcDhcp1LeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20, 1, 4),
    _CcDhcp1LeaseStartTime_Type()
)
ccDhcp1LeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1LeaseStartTime.setStatus("current")


class _CcDhcp1LeaseEndTime_Type(OctetString):
    """Custom type ccDhcp1LeaseEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp1LeaseEndTime_Type.__name__ = "OctetString"
_CcDhcp1LeaseEndTime_Object = MibTableColumn
ccDhcp1LeaseEndTime = _CcDhcp1LeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 20, 1, 5),
    _CcDhcp1LeaseEndTime_Type()
)
ccDhcp1LeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp1LeaseEndTime.setStatus("current")


class _CcDhcp1RemLeaseObj_Type(OctetString):
    """Custom type ccDhcp1RemLeaseObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp1RemLeaseObj_Type.__name__ = "OctetString"
_CcDhcp1RemLeaseObj_Object = MibScalar
ccDhcp1RemLeaseObj = _CcDhcp1RemLeaseObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 21),
    _CcDhcp1RemLeaseObj_Type()
)
ccDhcp1RemLeaseObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1RemLeaseObj.setStatus("current")
_CcDhcp1RemStaticHost_Type = DisplayString
_CcDhcp1RemStaticHost_Object = MibScalar
ccDhcp1RemStaticHost = _CcDhcp1RemStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 23, 22),
    _CcDhcp1RemStaticHost_Type()
)
ccDhcp1RemStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp1RemStaticHost.setStatus("current")
_CcDhcpSrvNIC2_ObjectIdentity = ObjectIdentity
ccDhcpSrvNIC2 = _CcDhcpSrvNIC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24)
)


class _CcDhcp2Srv_Type(Integer32):
    """Custom type ccDhcp2Srv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CcDhcp2Srv_Type.__name__ = "Integer32"
_CcDhcp2Srv_Object = MibScalar
ccDhcp2Srv = _CcDhcp2Srv_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 1),
    _CcDhcp2Srv_Type()
)
ccDhcp2Srv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2Srv.setStatus("current")
_CcDhcp2Subnet_Type = IpAddress
_CcDhcp2Subnet_Object = MibScalar
ccDhcp2Subnet = _CcDhcp2Subnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 2),
    _CcDhcp2Subnet_Type()
)
ccDhcp2Subnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2Subnet.setStatus("current")
_CcDhcp2Netmask_Type = IpAddress
_CcDhcp2Netmask_Object = MibScalar
ccDhcp2Netmask = _CcDhcp2Netmask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 3),
    _CcDhcp2Netmask_Type()
)
ccDhcp2Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2Netmask.setStatus("current")
_CcDhcp2BcastIP_Type = IpAddress
_CcDhcp2BcastIP_Object = MibScalar
ccDhcp2BcastIP = _CcDhcp2BcastIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 4),
    _CcDhcp2BcastIP_Type()
)
ccDhcp2BcastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2BcastIP.setStatus("current")
_CcDhcp2RouterIP_Type = IpAddress
_CcDhcp2RouterIP_Object = MibScalar
ccDhcp2RouterIP = _CcDhcp2RouterIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 5),
    _CcDhcp2RouterIP_Type()
)
ccDhcp2RouterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2RouterIP.setStatus("current")
_CcDhcp2PriDNSIP_Type = IpAddress
_CcDhcp2PriDNSIP_Object = MibScalar
ccDhcp2PriDNSIP = _CcDhcp2PriDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 6),
    _CcDhcp2PriDNSIP_Type()
)
ccDhcp2PriDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2PriDNSIP.setStatus("current")
_CcDhcp2SecDNSIP_Type = IpAddress
_CcDhcp2SecDNSIP_Object = MibScalar
ccDhcp2SecDNSIP = _CcDhcp2SecDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 7),
    _CcDhcp2SecDNSIP_Type()
)
ccDhcp2SecDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2SecDNSIP.setStatus("current")


class _CcDhcp2DomainName_Type(OctetString):
    """Custom type ccDhcp2DomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcDhcp2DomainName_Type.__name__ = "OctetString"
_CcDhcp2DomainName_Object = MibScalar
ccDhcp2DomainName = _CcDhcp2DomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 8),
    _CcDhcp2DomainName_Type()
)
ccDhcp2DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2DomainName.setStatus("current")


class _CcDhcp2DefLease_Type(Integer32):
    """Custom type ccDhcp2DefLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_CcDhcp2DefLease_Type.__name__ = "Integer32"
_CcDhcp2DefLease_Object = MibScalar
ccDhcp2DefLease = _CcDhcp2DefLease_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 9),
    _CcDhcp2DefLease_Type()
)
ccDhcp2DefLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2DefLease.setStatus("current")
if mibBuilder.loadTexts:
    ccDhcp2DefLease.setUnits("seconds")


class _CcDhcp2MaxLease_Type(Integer32):
    """Custom type ccDhcp2MaxLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_CcDhcp2MaxLease_Type.__name__ = "Integer32"
_CcDhcp2MaxLease_Object = MibScalar
ccDhcp2MaxLease = _CcDhcp2MaxLease_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 10),
    _CcDhcp2MaxLease_Type()
)
ccDhcp2MaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2MaxLease.setStatus("current")
if mibBuilder.loadTexts:
    ccDhcp2MaxLease.setUnits("seconds")
_CcDhcp2IPRangeTable_Object = MibTable
ccDhcp2IPRangeTable = _CcDhcp2IPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 11)
)
if mibBuilder.loadTexts:
    ccDhcp2IPRangeTable.setStatus("current")
_CcDhcp2IPRangeEntry_Object = MibTableRow
ccDhcp2IPRangeEntry = _CcDhcp2IPRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 11, 1)
)
ccDhcp2IPRangeEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp2RangeIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp2IPRangeEntry.setStatus("current")


class _CcDhcp2RangeIndex_Type(Integer32):
    """Custom type ccDhcp2RangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp2RangeIndex_Type.__name__ = "Integer32"
_CcDhcp2RangeIndex_Object = MibTableColumn
ccDhcp2RangeIndex = _CcDhcp2RangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 11, 1, 1),
    _CcDhcp2RangeIndex_Type()
)
ccDhcp2RangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2RangeIndex.setStatus("current")


class _CcDhcp2RangeStartIP_Type(OctetString):
    """Custom type ccDhcp2RangeStartIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2RangeStartIP_Type.__name__ = "OctetString"
_CcDhcp2RangeStartIP_Object = MibTableColumn
ccDhcp2RangeStartIP = _CcDhcp2RangeStartIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 11, 1, 2),
    _CcDhcp2RangeStartIP_Type()
)
ccDhcp2RangeStartIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2RangeStartIP.setStatus("current")


class _CcDhcp2RangeEndIP_Type(OctetString):
    """Custom type ccDhcp2RangeEndIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2RangeEndIP_Type.__name__ = "OctetString"
_CcDhcp2RangeEndIP_Object = MibTableColumn
ccDhcp2RangeEndIP = _CcDhcp2RangeEndIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 11, 1, 3),
    _CcDhcp2RangeEndIP_Type()
)
ccDhcp2RangeEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2RangeEndIP.setStatus("current")


class _CcDhcp2AddIPRangeObj_Type(OctetString):
    """Custom type ccDhcp2AddIPRangeObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2AddIPRangeObj_Type.__name__ = "OctetString"
_CcDhcp2AddIPRangeObj_Object = MibScalar
ccDhcp2AddIPRangeObj = _CcDhcp2AddIPRangeObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 12),
    _CcDhcp2AddIPRangeObj_Type()
)
ccDhcp2AddIPRangeObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2AddIPRangeObj.setStatus("current")


class _CcDhcp2RemIPRangeObj_Type(OctetString):
    """Custom type ccDhcp2RemIPRangeObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2RemIPRangeObj_Type.__name__ = "OctetString"
_CcDhcp2RemIPRangeObj_Object = MibScalar
ccDhcp2RemIPRangeObj = _CcDhcp2RemIPRangeObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 13),
    _CcDhcp2RemIPRangeObj_Type()
)
ccDhcp2RemIPRangeObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2RemIPRangeObj.setStatus("current")
_CcDhcp2StaticIPTable_Object = MibTable
ccDhcp2StaticIPTable = _CcDhcp2StaticIPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 14)
)
if mibBuilder.loadTexts:
    ccDhcp2StaticIPTable.setStatus("current")
_CcDhcp2StaticIPEntry_Object = MibTableRow
ccDhcp2StaticIPEntry = _CcDhcp2StaticIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 14, 1)
)
ccDhcp2StaticIPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp2StaticIPIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp2StaticIPEntry.setStatus("current")


class _CcDhcp2StaticIPIndex_Type(Integer32):
    """Custom type ccDhcp2StaticIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp2StaticIPIndex_Type.__name__ = "Integer32"
_CcDhcp2StaticIPIndex_Object = MibTableColumn
ccDhcp2StaticIPIndex = _CcDhcp2StaticIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 14, 1, 1),
    _CcDhcp2StaticIPIndex_Type()
)
ccDhcp2StaticIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2StaticIPIndex.setStatus("current")


class _CcDhcp2StaticIP_Type(OctetString):
    """Custom type ccDhcp2StaticIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2StaticIP_Type.__name__ = "OctetString"
_CcDhcp2StaticIP_Object = MibTableColumn
ccDhcp2StaticIP = _CcDhcp2StaticIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 14, 1, 2),
    _CcDhcp2StaticIP_Type()
)
ccDhcp2StaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2StaticIP.setStatus("current")


class _CcDhcp2StaticMac_Type(OctetString):
    """Custom type ccDhcp2StaticMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2StaticMac_Type.__name__ = "OctetString"
_CcDhcp2StaticMac_Object = MibTableColumn
ccDhcp2StaticMac = _CcDhcp2StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 14, 1, 3),
    _CcDhcp2StaticMac_Type()
)
ccDhcp2StaticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2StaticMac.setStatus("current")


class _CcDhcp2StaticHost_Type(OctetString):
    """Custom type ccDhcp2StaticHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2StaticHost_Type.__name__ = "OctetString"
_CcDhcp2StaticHost_Object = MibTableColumn
ccDhcp2StaticHost = _CcDhcp2StaticHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 14, 1, 4),
    _CcDhcp2StaticHost_Type()
)
ccDhcp2StaticHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2StaticHost.setStatus("current")


class _CcDhcp2AddStaticIPObj_Type(OctetString):
    """Custom type ccDhcp2AddStaticIPObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2AddStaticIPObj_Type.__name__ = "OctetString"
_CcDhcp2AddStaticIPObj_Object = MibScalar
ccDhcp2AddStaticIPObj = _CcDhcp2AddStaticIPObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 15),
    _CcDhcp2AddStaticIPObj_Type()
)
ccDhcp2AddStaticIPObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2AddStaticIPObj.setStatus("current")


class _CcDhcp2RemStaticIPObj_Type(OctetString):
    """Custom type ccDhcp2RemStaticIPObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2RemStaticIPObj_Type.__name__ = "OctetString"
_CcDhcp2RemStaticIPObj_Object = MibScalar
ccDhcp2RemStaticIPObj = _CcDhcp2RemStaticIPObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 16),
    _CcDhcp2RemStaticIPObj_Type()
)
ccDhcp2RemStaticIPObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2RemStaticIPObj.setStatus("current")
_CcDhcp2OptionTable_Object = MibTable
ccDhcp2OptionTable = _CcDhcp2OptionTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17)
)
if mibBuilder.loadTexts:
    ccDhcp2OptionTable.setStatus("current")
_CcDhcp2OptionEntry_Object = MibTableRow
ccDhcp2OptionEntry = _CcDhcp2OptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17, 1)
)
ccDhcp2OptionEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp2OptionIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp2OptionEntry.setStatus("current")


class _CcDhcp2OptionIndex_Type(Integer32):
    """Custom type ccDhcp2OptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp2OptionIndex_Type.__name__ = "Integer32"
_CcDhcp2OptionIndex_Object = MibTableColumn
ccDhcp2OptionIndex = _CcDhcp2OptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17, 1, 1),
    _CcDhcp2OptionIndex_Type()
)
ccDhcp2OptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2OptionIndex.setStatus("current")


class _CcDhcp2OptionName_Type(OctetString):
    """Custom type ccDhcp2OptionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2OptionName_Type.__name__ = "OctetString"
_CcDhcp2OptionName_Object = MibTableColumn
ccDhcp2OptionName = _CcDhcp2OptionName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17, 1, 2),
    _CcDhcp2OptionName_Type()
)
ccDhcp2OptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2OptionName.setStatus("current")


class _CcDhcp2OptionCode_Type(OctetString):
    """Custom type ccDhcp2OptionCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2OptionCode_Type.__name__ = "OctetString"
_CcDhcp2OptionCode_Object = MibTableColumn
ccDhcp2OptionCode = _CcDhcp2OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17, 1, 3),
    _CcDhcp2OptionCode_Type()
)
ccDhcp2OptionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2OptionCode.setStatus("current")


class _CcDhcp2OptionType_Type(OctetString):
    """Custom type ccDhcp2OptionType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2OptionType_Type.__name__ = "OctetString"
_CcDhcp2OptionType_Object = MibTableColumn
ccDhcp2OptionType = _CcDhcp2OptionType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17, 1, 4),
    _CcDhcp2OptionType_Type()
)
ccDhcp2OptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2OptionType.setStatus("current")


class _CcDhcp2OptionValue_Type(OctetString):
    """Custom type ccDhcp2OptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2OptionValue_Type.__name__ = "OctetString"
_CcDhcp2OptionValue_Object = MibTableColumn
ccDhcp2OptionValue = _CcDhcp2OptionValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 17, 1, 5),
    _CcDhcp2OptionValue_Type()
)
ccDhcp2OptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2OptionValue.setStatus("current")


class _CcDhcp2AddOptionObj_Type(OctetString):
    """Custom type ccDhcp2AddOptionObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2AddOptionObj_Type.__name__ = "OctetString"
_CcDhcp2AddOptionObj_Object = MibScalar
ccDhcp2AddOptionObj = _CcDhcp2AddOptionObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 18),
    _CcDhcp2AddOptionObj_Type()
)
ccDhcp2AddOptionObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2AddOptionObj.setStatus("current")


class _CcDhcp2RemOptionObj_Type(OctetString):
    """Custom type ccDhcp2RemOptionObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2RemOptionObj_Type.__name__ = "OctetString"
_CcDhcp2RemOptionObj_Object = MibScalar
ccDhcp2RemOptionObj = _CcDhcp2RemOptionObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 19),
    _CcDhcp2RemOptionObj_Type()
)
ccDhcp2RemOptionObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2RemOptionObj.setStatus("current")
_CcDhcp2LeasesTable_Object = MibTable
ccDhcp2LeasesTable = _CcDhcp2LeasesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20)
)
if mibBuilder.loadTexts:
    ccDhcp2LeasesTable.setStatus("current")
_CcDhcp2LeasesEntry_Object = MibTableRow
ccDhcp2LeasesEntry = _CcDhcp2LeasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20, 1)
)
ccDhcp2LeasesEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccDhcp1LeaseIndex"),
)
if mibBuilder.loadTexts:
    ccDhcp2LeasesEntry.setStatus("current")


class _CcDhcp2LeaseIndex_Type(Integer32):
    """Custom type ccDhcp2LeaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcDhcp2LeaseIndex_Type.__name__ = "Integer32"
_CcDhcp2LeaseIndex_Object = MibTableColumn
ccDhcp2LeaseIndex = _CcDhcp2LeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20, 1, 1),
    _CcDhcp2LeaseIndex_Type()
)
ccDhcp2LeaseIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2LeaseIndex.setStatus("current")


class _CcDhcp2LeaseIP_Type(OctetString):
    """Custom type ccDhcp2LeaseIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2LeaseIP_Type.__name__ = "OctetString"
_CcDhcp2LeaseIP_Object = MibTableColumn
ccDhcp2LeaseIP = _CcDhcp2LeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20, 1, 2),
    _CcDhcp2LeaseIP_Type()
)
ccDhcp2LeaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2LeaseIP.setStatus("current")


class _CcDhcp2LeaseMac_Type(OctetString):
    """Custom type ccDhcp2LeaseMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2LeaseMac_Type.__name__ = "OctetString"
_CcDhcp2LeaseMac_Object = MibTableColumn
ccDhcp2LeaseMac = _CcDhcp2LeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20, 1, 3),
    _CcDhcp2LeaseMac_Type()
)
ccDhcp2LeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2LeaseMac.setStatus("current")


class _CcDhcp2LeaseStartTime_Type(OctetString):
    """Custom type ccDhcp2LeaseStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2LeaseStartTime_Type.__name__ = "OctetString"
_CcDhcp2LeaseStartTime_Object = MibTableColumn
ccDhcp2LeaseStartTime = _CcDhcp2LeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20, 1, 4),
    _CcDhcp2LeaseStartTime_Type()
)
ccDhcp2LeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcp2LeaseStartTime.setStatus("current")


class _CcDhcp2LeaseEndTime_Type(OctetString):
    """Custom type ccDhcp2LeaseEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcDhcp2LeaseEndTime_Type.__name__ = "OctetString"
_CcDhcp2LeaseEndTime_Object = MibTableColumn
ccDhcp2LeaseEndTime = _CcDhcp2LeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 20, 1, 5),
    _CcDhcp2LeaseEndTime_Type()
)
ccDhcp2LeaseEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2LeaseEndTime.setStatus("current")


class _CcDhcp2RemLeaseObj_Type(OctetString):
    """Custom type ccDhcp2RemLeaseObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcDhcp2RemLeaseObj_Type.__name__ = "OctetString"
_CcDhcp2RemLeaseObj_Object = MibScalar
ccDhcp2RemLeaseObj = _CcDhcp2RemLeaseObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 21),
    _CcDhcp2RemLeaseObj_Type()
)
ccDhcp2RemLeaseObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2RemLeaseObj.setStatus("current")
_CcDhcp2RemStaticHost_Type = DisplayString
_CcDhcp2RemStaticHost_Object = MibScalar
ccDhcp2RemStaticHost = _CcDhcp2RemStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 2, 24, 22),
    _CcDhcp2RemStaticHost_Type()
)
ccDhcp2RemStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcp2RemStaticHost.setStatus("current")
_SymbolCCMgmt_ObjectIdentity = ObjectIdentity
symbolCCMgmt = _SymbolCCMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3)
)


class _CcWLANAddObj_Type(DisplayString):
    """Custom type ccWLANAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcWLANAddObj_Type.__name__ = "DisplayString"
_CcWLANAddObj_Object = MibScalar
ccWLANAddObj = _CcWLANAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 1),
    _CcWLANAddObj_Type()
)
ccWLANAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANAddObj.setStatus("current")


class _CcWLANRemObj_Type(DisplayString):
    """Custom type ccWLANRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcWLANRemObj_Type.__name__ = "DisplayString"
_CcWLANRemObj_Object = MibScalar
ccWLANRemObj = _CcWLANRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 2),
    _CcWLANRemObj_Type()
)
ccWLANRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANRemObj.setStatus("current")


class _CcUserAddObj_Type(DisplayString):
    """Custom type ccUserAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcUserAddObj_Type.__name__ = "DisplayString"
_CcUserAddObj_Object = MibScalar
ccUserAddObj = _CcUserAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 3),
    _CcUserAddObj_Type()
)
ccUserAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserAddObj.setStatus("current")


class _CcUserRemObj_Type(DisplayString):
    """Custom type ccUserRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcUserRemObj_Type.__name__ = "DisplayString"
_CcUserRemObj_Object = MibScalar
ccUserRemObj = _CcUserRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 4),
    _CcUserRemObj_Type()
)
ccUserRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserRemObj.setStatus("current")


class _CcGraphAddObj_Type(DisplayString):
    """Custom type ccGraphAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcGraphAddObj_Type.__name__ = "DisplayString"
_CcGraphAddObj_Object = MibScalar
ccGraphAddObj = _CcGraphAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 5),
    _CcGraphAddObj_Type()
)
ccGraphAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccGraphAddObj.setStatus("current")


class _CcGraphRemObj_Type(DisplayString):
    """Custom type ccGraphRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcGraphRemObj_Type.__name__ = "DisplayString"
_CcGraphRemObj_Object = MibScalar
ccGraphRemObj = _CcGraphRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 6),
    _CcGraphRemObj_Type()
)
ccGraphRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccGraphRemObj.setStatus("current")


class _CcSecAddObj_Type(DisplayString):
    """Custom type ccSecAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcSecAddObj_Type.__name__ = "DisplayString"
_CcSecAddObj_Object = MibScalar
ccSecAddObj = _CcSecAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 11),
    _CcSecAddObj_Type()
)
ccSecAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecAddObj.setStatus("current")


class _CcSecRemObj_Type(DisplayString):
    """Custom type ccSecRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcSecRemObj_Type.__name__ = "DisplayString"
_CcSecRemObj_Object = MibScalar
ccSecRemObj = _CcSecRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 12),
    _CcSecRemObj_Type()
)
ccSecRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRemObj.setStatus("current")


class _CcACLAddObj_Type(DisplayString):
    """Custom type ccACLAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcACLAddObj_Type.__name__ = "DisplayString"
_CcACLAddObj_Object = MibScalar
ccACLAddObj = _CcACLAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 13),
    _CcACLAddObj_Type()
)
ccACLAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLAddObj.setStatus("current")


class _CcACLRemObj_Type(DisplayString):
    """Custom type ccACLRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcACLRemObj_Type.__name__ = "DisplayString"
_CcACLRemObj_Object = MibScalar
ccACLRemObj = _CcACLRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 14),
    _CcACLRemObj_Type()
)
ccACLRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLRemObj.setStatus("current")
_CcUserTable_Object = MibTable
ccUserTable = _CcUserTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21)
)
if mibBuilder.loadTexts:
    ccUserTable.setStatus("current")
_CcUserEntry_Object = MibTableRow
ccUserEntry = _CcUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1)
)
ccUserEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccUserIndex"),
)
if mibBuilder.loadTexts:
    ccUserEntry.setStatus("current")


class _CcUserID_Type(DisplayString):
    """Custom type ccUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcUserID_Type.__name__ = "DisplayString"
_CcUserID_Object = MibTableColumn
ccUserID = _CcUserID_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 1),
    _CcUserID_Type()
)
ccUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccUserID.setStatus("current")


class _CcUserFullName_Type(DisplayString):
    """Custom type ccUserFullName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcUserFullName_Type.__name__ = "DisplayString"
_CcUserFullName_Object = MibTableColumn
ccUserFullName = _CcUserFullName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 2),
    _CcUserFullName_Type()
)
ccUserFullName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserFullName.setStatus("current")


class _CcUserPwd_Type(DisplayString):
    """Custom type ccUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 20),
    )


_CcUserPwd_Type.__name__ = "DisplayString"
_CcUserPwd_Object = MibTableColumn
ccUserPwd = _CcUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 3),
    _CcUserPwd_Type()
)
ccUserPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserPwd.setStatus("current")


class _CcUserAdminRight_Type(TruthValue):
    """Custom type ccUserAdminRight based on TruthValue"""
    defaultValue = 1


_CcUserAdminRight_Type.__name__ = "TruthValue"
_CcUserAdminRight_Object = MibTableColumn
ccUserAdminRight = _CcUserAdminRight_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 4),
    _CcUserAdminRight_Type()
)
ccUserAdminRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserAdminRight.setStatus("deprecated")


class _CcUserProfileMgmtRight_Type(TruthValue):
    """Custom type ccUserProfileMgmtRight based on TruthValue"""
    defaultValue = 1


_CcUserProfileMgmtRight_Type.__name__ = "TruthValue"
_CcUserProfileMgmtRight_Object = MibTableColumn
ccUserProfileMgmtRight = _CcUserProfileMgmtRight_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 5),
    _CcUserProfileMgmtRight_Type()
)
ccUserProfileMgmtRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserProfileMgmtRight.setStatus("current")


class _CcUserSysAdminRight_Type(TruthValue):
    """Custom type ccUserSysAdminRight based on TruthValue"""
    defaultValue = 2


_CcUserSysAdminRight_Type.__name__ = "TruthValue"
_CcUserSysAdminRight_Object = MibTableColumn
ccUserSysAdminRight = _CcUserSysAdminRight_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 6),
    _CcUserSysAdminRight_Type()
)
ccUserSysAdminRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserSysAdminRight.setStatus("current")


class _CcUserSNMPAdminRight_Type(TruthValue):
    """Custom type ccUserSNMPAdminRight based on TruthValue"""
    defaultValue = 1


_CcUserSNMPAdminRight_Type.__name__ = "TruthValue"
_CcUserSNMPAdminRight_Object = MibTableColumn
ccUserSNMPAdminRight = _CcUserSNMPAdminRight_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 7),
    _CcUserSNMPAdminRight_Type()
)
ccUserSNMPAdminRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserSNMPAdminRight.setStatus("current")


class _CcUserSecurityAdminRight_Type(TruthValue):
    """Custom type ccUserSecurityAdminRight based on TruthValue"""
    defaultValue = 1


_CcUserSecurityAdminRight_Type.__name__ = "TruthValue"
_CcUserSecurityAdminRight_Object = MibTableColumn
ccUserSecurityAdminRight = _CcUserSecurityAdminRight_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 8),
    _CcUserSecurityAdminRight_Type()
)
ccUserSecurityAdminRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUserSecurityAdminRight.setStatus("current")


class _CcUserIndex_Type(Integer32):
    """Custom type ccUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcUserIndex_Type.__name__ = "Integer32"
_CcUserIndex_Object = MibTableColumn
ccUserIndex = _CcUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 21, 1, 10),
    _CcUserIndex_Type()
)
ccUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccUserIndex.setStatus("current")
_CcWLANTable_Object = MibTable
ccWLANTable = _CcWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22)
)
if mibBuilder.loadTexts:
    ccWLANTable.setStatus("current")
_CcWLANEntry_Object = MibTableRow
ccWLANEntry = _CcWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1)
)
ccWLANEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccWLANIndex"),
)
if mibBuilder.loadTexts:
    ccWLANEntry.setStatus("current")


class _CcWLANIndex_Type(Integer32):
    """Custom type ccWLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcWLANIndex_Type.__name__ = "Integer32"
_CcWLANIndex_Object = MibTableColumn
ccWLANIndex = _CcWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 1),
    _CcWLANIndex_Type()
)
ccWLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWLANIndex.setStatus("current")


class _CcWLANName_Type(DisplayString):
    """Custom type ccWLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcWLANName_Type.__name__ = "DisplayString"
_CcWLANName_Object = MibTableColumn
ccWLANName = _CcWLANName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 2),
    _CcWLANName_Type()
)
ccWLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANName.setStatus("current")


class _CcESSID_Type(DisplayString):
    """Custom type ccESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcESSID_Type.__name__ = "DisplayString"
_CcESSID_Object = MibTableColumn
ccESSID = _CcESSID_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 3),
    _CcESSID_Type()
)
ccESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccESSID.setStatus("current")


class _CcSecurity_Type(DisplayString):
    """Custom type ccSecurity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcSecurity_Type.__name__ = "DisplayString"
_CcSecurity_Object = MibTableColumn
ccSecurity = _CcSecurity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 4),
    _CcSecurity_Type()
)
ccSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecurity.setStatus("current")
_CcACLEnabled_Type = TruthValue
_CcACLEnabled_Object = MibTableColumn
ccACLEnabled = _CcACLEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 5),
    _CcACLEnabled_Type()
)
ccACLEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLEnabled.setStatus("current")


class _CcMaxMus_Type(Integer32):
    """Custom type ccMaxMus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CcMaxMus_Type.__name__ = "Integer32"
_CcMaxMus_Object = MibTableColumn
ccMaxMus = _CcMaxMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 14),
    _CcMaxMus_Type()
)
ccMaxMus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMaxMus.setStatus("current")


class _CcKerberosAuthName_Type(DisplayString):
    """Custom type ccKerberosAuthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcKerberosAuthName_Type.__name__ = "DisplayString"
_CcKerberosAuthName_Object = MibTableColumn
ccKerberosAuthName = _CcKerberosAuthName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 15),
    _CcKerberosAuthName_Type()
)
ccKerberosAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccKerberosAuthName.setStatus("current")


class _CcKerberosAuthPass_Type(DisplayString):
    """Custom type ccKerberosAuthPass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_CcKerberosAuthPass_Type.__name__ = "DisplayString"
_CcKerberosAuthPass_Object = MibTableColumn
ccKerberosAuthPass = _CcKerberosAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 16),
    _CcKerberosAuthPass_Type()
)
ccKerberosAuthPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccKerberosAuthPass.setStatus("current")


class _CcWLANACL_Type(DisplayString):
    """Custom type ccWLANACL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcWLANACL_Type.__name__ = "DisplayString"
_CcWLANACL_Object = MibTableColumn
ccWLANACL = _CcWLANACL_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 17),
    _CcWLANACL_Type()
)
ccWLANACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANACL.setStatus("current")
_CcWLANIsAuthenticated_Type = TruthValue
_CcWLANIsAuthenticated_Object = MibTableColumn
ccWLANIsAuthenticated = _CcWLANIsAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 18),
    _CcWLANIsAuthenticated_Type()
)
ccWLANIsAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWLANIsAuthenticated.setStatus("current")


class _CcWLANMUTraffic_Type(Integer32):
    """Custom type ccWLANMUTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CcWLANMUTraffic_Type.__name__ = "Integer32"
_CcWLANMUTraffic_Object = MibTableColumn
ccWLANMUTraffic = _CcWLANMUTraffic_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 19),
    _CcWLANMUTraffic_Type()
)
ccWLANMUTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANMUTraffic.setStatus("current")
_CcWLANSecuredBeacon_Type = TruthValue
_CcWLANSecuredBeacon_Object = MibTableColumn
ccWLANSecuredBeacon = _CcWLANSecuredBeacon_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 20),
    _CcWLANSecuredBeacon_Type()
)
ccWLANSecuredBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANSecuredBeacon.setStatus("current")


class _CcWLANCurrentMU_Type(Integer32):
    """Custom type ccWLANCurrentMU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CcWLANCurrentMU_Type.__name__ = "Integer32"
_CcWLANCurrentMU_Object = MibTableColumn
ccWLANCurrentMU = _CcWLANCurrentMU_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 21),
    _CcWLANCurrentMU_Type()
)
ccWLANCurrentMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWLANCurrentMU.setStatus("current")
_CcWLANNetMask_Type = IpAddress
_CcWLANNetMask_Object = MibTableColumn
ccWLANNetMask = _CcWLANNetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 22),
    _CcWLANNetMask_Type()
)
ccWLANNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANNetMask.setStatus("current")
_CcWLANDefaultRoute_Type = IpAddress
_CcWLANDefaultRoute_Object = MibTableColumn
ccWLANDefaultRoute = _CcWLANDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 23),
    _CcWLANDefaultRoute_Type()
)
ccWLANDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANDefaultRoute.setStatus("current")
_CcWLANBCMC11A_Type = EncrType
_CcWLANBCMC11A_Object = MibTableColumn
ccWLANBCMC11A = _CcWLANBCMC11A_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 24),
    _CcWLANBCMC11A_Type()
)
ccWLANBCMC11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWLANBCMC11A.setStatus("current")
_CcWLANBCMC11B_Type = EncrType
_CcWLANBCMC11B_Object = MibTableColumn
ccWLANBCMC11B = _CcWLANBCMC11B_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 25),
    _CcWLANBCMC11B_Type()
)
ccWLANBCMC11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWLANBCMC11B.setStatus("current")
_CcWLANBCMCFH_Type = EncrType
_CcWLANBCMCFH_Object = MibTableColumn
ccWLANBCMCFH = _CcWLANBCMCFH_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 26),
    _CcWLANBCMCFH_Type()
)
ccWLANBCMCFH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWLANBCMCFH.setStatus("current")
_CcBroadcastEss_Type = TruthValue
_CcBroadcastEss_Object = MibTableColumn
ccBroadcastEss = _CcBroadcastEss_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 27),
    _CcBroadcastEss_Type()
)
ccBroadcastEss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccBroadcastEss.setStatus("current")


class _CcWLANDesc_Type(DisplayString):
    """Custom type ccWLANDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcWLANDesc_Type.__name__ = "DisplayString"
_CcWLANDesc_Object = MibTableColumn
ccWLANDesc = _CcWLANDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 28),
    _CcWLANDesc_Type()
)
ccWLANDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWLANDesc.setStatus("current")
_CcWlanWMEEnable_Type = DisplayString
_CcWlanWMEEnable_Object = MibTableColumn
ccWlanWMEEnable = _CcWlanWMEEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 29),
    _CcWlanWMEEnable_Type()
)
ccWlanWMEEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanWMEEnable.setStatus("current")
_CcWlanWMEProfile_Type = DisplayString
_CcWlanWMEProfile_Object = MibTableColumn
ccWlanWMEProfile = _CcWlanWMEProfile_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 22, 1, 30),
    _CcWlanWMEProfile_Type()
)
ccWlanWMEProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanWMEProfile.setStatus("current")
_CcKnownCCTable_Object = MibTable
ccKnownCCTable = _CcKnownCCTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 23)
)
if mibBuilder.loadTexts:
    ccKnownCCTable.setStatus("current")
_CcKnownCCEntry_Object = MibTableRow
ccKnownCCEntry = _CcKnownCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 23, 1)
)
ccKnownCCEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccKnownCCIndex"),
)
if mibBuilder.loadTexts:
    ccKnownCCEntry.setStatus("current")


class _CcKnownCCIndex_Type(Integer32):
    """Custom type ccKnownCCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CcKnownCCIndex_Type.__name__ = "Integer32"
_CcKnownCCIndex_Object = MibTableColumn
ccKnownCCIndex = _CcKnownCCIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 23, 1, 1),
    _CcKnownCCIndex_Type()
)
ccKnownCCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownCCIndex.setStatus("current")


class _CcKnownCCName_Type(DisplayString):
    """Custom type ccKnownCCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcKnownCCName_Type.__name__ = "DisplayString"
_CcKnownCCName_Object = MibTableColumn
ccKnownCCName = _CcKnownCCName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 23, 1, 2),
    _CcKnownCCName_Type()
)
ccKnownCCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownCCName.setStatus("current")


class _CcKnownCCMac_Type(DisplayString):
    """Custom type ccKnownCCMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_CcKnownCCMac_Type.__name__ = "DisplayString"
_CcKnownCCMac_Object = MibTableColumn
ccKnownCCMac = _CcKnownCCMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 23, 1, 3),
    _CcKnownCCMac_Type()
)
ccKnownCCMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownCCMac.setStatus("current")
_CcKnownAPTable_Object = MibTable
ccKnownAPTable = _CcKnownAPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24)
)
if mibBuilder.loadTexts:
    ccKnownAPTable.setStatus("current")
_CcKnownAPEntry_Object = MibTableRow
ccKnownAPEntry = _CcKnownAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1)
)
ccKnownAPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccKnownAPIndex"),
)
if mibBuilder.loadTexts:
    ccKnownAPEntry.setStatus("current")


class _CcKnownAPIndex_Type(Integer32):
    """Custom type ccKnownAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_CcKnownAPIndex_Type.__name__ = "Integer32"
_CcKnownAPIndex_Object = MibTableColumn
ccKnownAPIndex = _CcKnownAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 1),
    _CcKnownAPIndex_Type()
)
ccKnownAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPIndex.setStatus("current")


class _CcKnownAPMac_Type(DisplayString):
    """Custom type ccKnownAPMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_CcKnownAPMac_Type.__name__ = "DisplayString"
_CcKnownAPMac_Object = MibTableColumn
ccKnownAPMac = _CcKnownAPMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 2),
    _CcKnownAPMac_Type()
)
ccKnownAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPMac.setStatus("current")


class _CcKnownAPVer_Type(Integer32):
    """Custom type ccKnownAPVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcKnownAPVer_Type.__name__ = "Integer32"
_CcKnownAPVer_Object = MibTableColumn
ccKnownAPVer = _CcKnownAPVer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 3),
    _CcKnownAPVer_Type()
)
ccKnownAPVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPVer.setStatus("current")
_CcKnownAPIP_Type = IpAddress
_CcKnownAPIP_Object = MibTableColumn
ccKnownAPIP = _CcKnownAPIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 4),
    _CcKnownAPIP_Type()
)
ccKnownAPIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPIP.setStatus("current")


class _CcKnownAPPriority_Type(Integer32):
    """Custom type ccKnownAPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcKnownAPPriority_Type.__name__ = "Integer32"
_CcKnownAPPriority_Object = MibTableColumn
ccKnownAPPriority = _CcKnownAPPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 5),
    _CcKnownAPPriority_Type()
)
ccKnownAPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPPriority.setStatus("current")


class _CcKnownAPMus_Type(Integer32):
    """Custom type ccKnownAPMus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcKnownAPMus_Type.__name__ = "Integer32"
_CcKnownAPMus_Object = MibTableColumn
ccKnownAPMus = _CcKnownAPMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 6),
    _CcKnownAPMus_Type()
)
ccKnownAPMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPMus.setStatus("current")


class _CcKnownAPType_Type(Integer32):
    """Custom type ccKnownAPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcKnownAPType_Type.__name__ = "Integer32"
_CcKnownAPType_Object = MibTableColumn
ccKnownAPType = _CcKnownAPType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 7),
    _CcKnownAPType_Type()
)
ccKnownAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPType.setStatus("current")


class _CcKnownAPAPVer_Type(Integer32):
    """Custom type ccKnownAPAPVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcKnownAPAPVer_Type.__name__ = "Integer32"
_CcKnownAPAPVer_Object = MibTableColumn
ccKnownAPAPVer = _CcKnownAPAPVer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 8),
    _CcKnownAPAPVer_Type()
)
ccKnownAPAPVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPAPVer.setStatus("current")


class _CcKnownAPEssid_Type(DisplayString):
    """Custom type ccKnownAPEssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcKnownAPEssid_Type.__name__ = "DisplayString"
_CcKnownAPEssid_Object = MibTableColumn
ccKnownAPEssid = _CcKnownAPEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 24, 1, 9),
    _CcKnownAPEssid_Type()
)
ccKnownAPEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccKnownAPEssid.setStatus("current")
_CcGraphTable_Object = MibTable
ccGraphTable = _CcGraphTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 25)
)
if mibBuilder.loadTexts:
    ccGraphTable.setStatus("current")
_CcGraphEntry_Object = MibTableRow
ccGraphEntry = _CcGraphEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 25, 1)
)
ccGraphEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccGraphIndex"),
)
if mibBuilder.loadTexts:
    ccGraphEntry.setStatus("current")


class _CcGraphIndex_Type(Integer32):
    """Custom type ccGraphIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcGraphIndex_Type.__name__ = "Integer32"
_CcGraphIndex_Object = MibTableColumn
ccGraphIndex = _CcGraphIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 25, 1, 1),
    _CcGraphIndex_Type()
)
ccGraphIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccGraphIndex.setStatus("current")


class _CcGraphName_Type(DisplayString):
    """Custom type ccGraphName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcGraphName_Type.__name__ = "DisplayString"
_CcGraphName_Object = MibTableColumn
ccGraphName = _CcGraphName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 25, 1, 2),
    _CcGraphName_Type()
)
ccGraphName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccGraphName.setStatus("current")


class _CcGraphWlanId_Type(DisplayString):
    """Custom type ccGraphWlanId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcGraphWlanId_Type.__name__ = "DisplayString"
_CcGraphWlanId_Object = MibTableColumn
ccGraphWlanId = _CcGraphWlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 25, 1, 7),
    _CcGraphWlanId_Type()
)
ccGraphWlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccGraphWlanId.setStatus("current")
_CcVLANTable_Object = MibTable
ccVLANTable = _CcVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26)
)
if mibBuilder.loadTexts:
    ccVLANTable.setStatus("current")
_CcVLANEntry_Object = MibTableRow
ccVLANEntry = _CcVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1)
)
ccVLANEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccVLANIndex"),
)
if mibBuilder.loadTexts:
    ccVLANEntry.setStatus("current")


class _CcVLANIndex_Type(Integer32):
    """Custom type ccVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcVLANIndex_Type.__name__ = "Integer32"
_CcVLANIndex_Object = MibTableColumn
ccVLANIndex = _CcVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 1),
    _CcVLANIndex_Type()
)
ccVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVLANIndex.setStatus("current")


class _CcVLANName_Type(DisplayString):
    """Custom type ccVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcVLANName_Type.__name__ = "DisplayString"
_CcVLANName_Object = MibTableColumn
ccVLANName = _CcVLANName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 2),
    _CcVLANName_Type()
)
ccVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVLANName.setStatus("current")


class _CcVLANDesc_Type(DisplayString):
    """Custom type ccVLANDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcVLANDesc_Type.__name__ = "DisplayString"
_CcVLANDesc_Object = MibTableColumn
ccVLANDesc = _CcVLANDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 3),
    _CcVLANDesc_Type()
)
ccVLANDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccVLANDesc.setStatus("current")


class _CcVLANVid_Type(Integer32):
    """Custom type ccVLANVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcVLANVid_Type.__name__ = "Integer32"
_CcVLANVid_Object = MibTableColumn
ccVLANVid = _CcVLANVid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 4),
    _CcVLANVid_Type()
)
ccVLANVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVLANVid.setStatus("current")


class _CcVLANPriority_Type(Integer32):
    """Custom type ccVLANPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CcVLANPriority_Type.__name__ = "Integer32"
_CcVLANPriority_Object = MibTableColumn
ccVLANPriority = _CcVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 5),
    _CcVLANPriority_Type()
)
ccVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccVLANPriority.setStatus("current")


class _CcVLANPorts_Type(Integer32):
    """Custom type ccVLANPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CcVLANPorts_Type.__name__ = "Integer32"
_CcVLANPorts_Object = MibTableColumn
ccVLANPorts = _CcVLANPorts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 6),
    _CcVLANPorts_Type()
)
ccVLANPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccVLANPorts.setStatus("current")


class _CcVLANEtherPolicy_Type(DisplayString):
    """Custom type ccVLANEtherPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcVLANEtherPolicy_Type.__name__ = "DisplayString"
_CcVLANEtherPolicy_Object = MibTableColumn
ccVLANEtherPolicy = _CcVLANEtherPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 7),
    _CcVLANEtherPolicy_Type()
)
ccVLANEtherPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVLANEtherPolicy.setStatus("current")


class _CcVLANWlan_Type(Integer32):
    """Custom type ccVLANWlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcVLANWlan_Type.__name__ = "Integer32"
_CcVLANWlan_Object = MibTableColumn
ccVLANWlan = _CcVLANWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 8),
    _CcVLANWlan_Type()
)
ccVLANWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVLANWlan.setStatus("current")


class _CcVLANWlanList_Type(DisplayString):
    """Custom type ccVLANWlanList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcVLANWlanList_Type.__name__ = "DisplayString"
_CcVLANWlanList_Object = MibTableColumn
ccVLANWlanList = _CcVLANWlanList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 9),
    _CcVLANWlanList_Type()
)
ccVLANWlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVLANWlanList.setStatus("current")


class _CcVLANAddWlan_Type(DisplayString):
    """Custom type ccVLANAddWlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcVLANAddWlan_Type.__name__ = "DisplayString"
_CcVLANAddWlan_Object = MibTableColumn
ccVLANAddWlan = _CcVLANAddWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 10),
    _CcVLANAddWlan_Type()
)
ccVLANAddWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccVLANAddWlan.setStatus("current")


class _CcVLANRemWlan_Type(DisplayString):
    """Custom type ccVLANRemWlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcVLANRemWlan_Type.__name__ = "DisplayString"
_CcVLANRemWlan_Object = MibTableColumn
ccVLANRemWlan = _CcVLANRemWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 26, 1, 11),
    _CcVLANRemWlan_Type()
)
ccVLANRemWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccVLANRemWlan.setStatus("current")
_CcSecurityTable_Object = MibTable
ccSecurityTable = _CcSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28)
)
if mibBuilder.loadTexts:
    ccSecurityTable.setStatus("current")
_CcSecurityEntry_Object = MibTableRow
ccSecurityEntry = _CcSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1)
)
ccSecurityEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccSecIndex"),
)
if mibBuilder.loadTexts:
    ccSecurityEntry.setStatus("current")


class _CcSecIndex_Type(Integer32):
    """Custom type ccSecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcSecIndex_Type.__name__ = "Integer32"
_CcSecIndex_Object = MibTableColumn
ccSecIndex = _CcSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 1),
    _CcSecIndex_Type()
)
ccSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSecIndex.setStatus("current")


class _CcSecName_Type(DisplayString):
    """Custom type ccSecName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcSecName_Type.__name__ = "DisplayString"
_CcSecName_Object = MibTableColumn
ccSecName = _CcSecName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 2),
    _CcSecName_Type()
)
ccSecName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecName.setStatus("current")


class _CcSecDesc_Type(DisplayString):
    """Custom type ccSecDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcSecDesc_Type.__name__ = "DisplayString"
_CcSecDesc_Object = MibTableColumn
ccSecDesc = _CcSecDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 3),
    _CcSecDesc_Type()
)
ccSecDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecDesc.setStatus("current")
_CcSecBeaconEssid_Type = TruthValue
_CcSecBeaconEssid_Object = MibTableColumn
ccSecBeaconEssid = _CcSecBeaconEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 4),
    _CcSecBeaconEssid_Type()
)
ccSecBeaconEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecBeaconEssid.setStatus("deprecated")
_CcSecPreSharedAuthEnabled_Type = TruthValue
_CcSecPreSharedAuthEnabled_Object = MibTableColumn
ccSecPreSharedAuthEnabled = _CcSecPreSharedAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 5),
    _CcSecPreSharedAuthEnabled_Type()
)
ccSecPreSharedAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecPreSharedAuthEnabled.setStatus("current")
_CcSecWEPEnabled_Type = TruthValue
_CcSecWEPEnabled_Object = MibTableColumn
ccSecWEPEnabled = _CcSecWEPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 6),
    _CcSecWEPEnabled_Type()
)
ccSecWEPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecWEPEnabled.setStatus("current")


class _CcSecWEPKeyBitSize_Type(Integer32):
    """Custom type ccSecWEPKeyBitSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_CcSecWEPKeyBitSize_Type.__name__ = "Integer32"
_CcSecWEPKeyBitSize_Object = MibTableColumn
ccSecWEPKeyBitSize = _CcSecWEPKeyBitSize_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 7),
    _CcSecWEPKeyBitSize_Type()
)
ccSecWEPKeyBitSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecWEPKeyBitSize.setStatus("current")


class _CcSecWEPKey_Type(DisplayString):
    """Custom type ccSecWEPKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 50),
    )


_CcSecWEPKey_Type.__name__ = "DisplayString"
_CcSecWEPKey_Object = MibTableColumn
ccSecWEPKey = _CcSecWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 8),
    _CcSecWEPKey_Type()
)
ccSecWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecWEPKey.setStatus("current")


class _CcSecWEPKeyUse_Type(Integer32):
    """Custom type ccSecWEPKeyUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CcSecWEPKeyUse_Type.__name__ = "Integer32"
_CcSecWEPKeyUse_Object = MibTableColumn
ccSecWEPKeyUse = _CcSecWEPKeyUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 9),
    _CcSecWEPKeyUse_Type()
)
ccSecWEPKeyUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecWEPKeyUse.setStatus("current")
_CcSecKerberosEnabled_Type = TruthValue
_CcSecKerberosEnabled_Object = MibTableColumn
ccSecKerberosEnabled = _CcSecKerberosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 10),
    _CcSecKerberosEnabled_Type()
)
ccSecKerberosEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosEnabled.setStatus("current")


class _CcSecKerberosRealm_Type(DisplayString):
    """Custom type ccSecKerberosRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcSecKerberosRealm_Type.__name__ = "DisplayString"
_CcSecKerberosRealm_Object = MibTableColumn
ccSecKerberosRealm = _CcSecKerberosRealm_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 11),
    _CcSecKerberosRealm_Type()
)
ccSecKerberosRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosRealm.setStatus("current")


class _CcSecKerberosServer1_Type(DisplayString):
    """Custom type ccSecKerberosServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcSecKerberosServer1_Type.__name__ = "DisplayString"
_CcSecKerberosServer1_Object = MibTableColumn
ccSecKerberosServer1 = _CcSecKerberosServer1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 12),
    _CcSecKerberosServer1_Type()
)
ccSecKerberosServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosServer1.setStatus("current")


class _CcSecKerberosServer2_Type(DisplayString):
    """Custom type ccSecKerberosServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcSecKerberosServer2_Type.__name__ = "DisplayString"
_CcSecKerberosServer2_Object = MibTableColumn
ccSecKerberosServer2 = _CcSecKerberosServer2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 13),
    _CcSecKerberosServer2_Type()
)
ccSecKerberosServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosServer2.setStatus("current")


class _CcSecKerberosServer3_Type(DisplayString):
    """Custom type ccSecKerberosServer3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcSecKerberosServer3_Type.__name__ = "DisplayString"
_CcSecKerberosServer3_Object = MibTableColumn
ccSecKerberosServer3 = _CcSecKerberosServer3_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 14),
    _CcSecKerberosServer3_Type()
)
ccSecKerberosServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosServer3.setStatus("current")


class _CcSecKerberosPort1_Type(Integer32):
    """Custom type ccSecKerberosPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcSecKerberosPort1_Type.__name__ = "Integer32"
_CcSecKerberosPort1_Object = MibTableColumn
ccSecKerberosPort1 = _CcSecKerberosPort1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 15),
    _CcSecKerberosPort1_Type()
)
ccSecKerberosPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosPort1.setStatus("current")


class _CcSecKerberosPort2_Type(Integer32):
    """Custom type ccSecKerberosPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcSecKerberosPort2_Type.__name__ = "Integer32"
_CcSecKerberosPort2_Object = MibTableColumn
ccSecKerberosPort2 = _CcSecKerberosPort2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 16),
    _CcSecKerberosPort2_Type()
)
ccSecKerberosPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosPort2.setStatus("current")


class _CcSecKerberosPort3_Type(Integer32):
    """Custom type ccSecKerberosPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcSecKerberosPort3_Type.__name__ = "Integer32"
_CcSecKerberosPort3_Object = MibTableColumn
ccSecKerberosPort3 = _CcSecKerberosPort3_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 17),
    _CcSecKerberosPort3_Type()
)
ccSecKerberosPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKerberosPort3.setStatus("current")


class _CcSecRadiusServer1_Type(DisplayString):
    """Custom type ccSecRadiusServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcSecRadiusServer1_Type.__name__ = "DisplayString"
_CcSecRadiusServer1_Object = MibTableColumn
ccSecRadiusServer1 = _CcSecRadiusServer1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 18),
    _CcSecRadiusServer1_Type()
)
ccSecRadiusServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusServer1.setStatus("current")


class _CcSecRadiusPort1_Type(Integer32):
    """Custom type ccSecRadiusPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcSecRadiusPort1_Type.__name__ = "Integer32"
_CcSecRadiusPort1_Object = MibTableColumn
ccSecRadiusPort1 = _CcSecRadiusPort1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 19),
    _CcSecRadiusPort1_Type()
)
ccSecRadiusPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusPort1.setStatus("current")


class _CcSecRadiusSecret1_Type(DisplayString):
    """Custom type ccSecRadiusSecret1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcSecRadiusSecret1_Type.__name__ = "DisplayString"
_CcSecRadiusSecret1_Object = MibTableColumn
ccSecRadiusSecret1 = _CcSecRadiusSecret1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 20),
    _CcSecRadiusSecret1_Type()
)
ccSecRadiusSecret1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusSecret1.setStatus("current")


class _CcSecRadiusServer2_Type(DisplayString):
    """Custom type ccSecRadiusServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcSecRadiusServer2_Type.__name__ = "DisplayString"
_CcSecRadiusServer2_Object = MibTableColumn
ccSecRadiusServer2 = _CcSecRadiusServer2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 21),
    _CcSecRadiusServer2_Type()
)
ccSecRadiusServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusServer2.setStatus("current")


class _CcSecRadiusPort2_Type(Integer32):
    """Custom type ccSecRadiusPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcSecRadiusPort2_Type.__name__ = "Integer32"
_CcSecRadiusPort2_Object = MibTableColumn
ccSecRadiusPort2 = _CcSecRadiusPort2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 22),
    _CcSecRadiusPort2_Type()
)
ccSecRadiusPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusPort2.setStatus("current")


class _CcSecRadiusSecret2_Type(DisplayString):
    """Custom type ccSecRadiusSecret2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcSecRadiusSecret2_Type.__name__ = "DisplayString"
_CcSecRadiusSecret2_Object = MibTableColumn
ccSecRadiusSecret2 = _CcSecRadiusSecret2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 23),
    _CcSecRadiusSecret2_Type()
)
ccSecRadiusSecret2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusSecret2.setStatus("current")


class _CcSecRadiusHostname_Type(DisplayString):
    """Custom type ccSecRadiusHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcSecRadiusHostname_Type.__name__ = "DisplayString"
_CcSecRadiusHostname_Object = MibTableColumn
ccSecRadiusHostname = _CcSecRadiusHostname_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 24),
    _CcSecRadiusHostname_Type()
)
ccSecRadiusHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecRadiusHostname.setStatus("current")
_CcSecEapEnabled_Type = TruthValue
_CcSecEapEnabled_Object = MibTableColumn
ccSecEapEnabled = _CcSecEapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 25),
    _CcSecEapEnabled_Type()
)
ccSecEapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapEnabled.setStatus("current")


class _CcSecEapQuietPeriod_Type(Integer32):
    """Custom type ccSecEapQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcSecEapQuietPeriod_Type.__name__ = "Integer32"
_CcSecEapQuietPeriod_Object = MibTableColumn
ccSecEapQuietPeriod = _CcSecEapQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 26),
    _CcSecEapQuietPeriod_Type()
)
ccSecEapQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapQuietPeriod.setStatus("current")


class _CcSecEapTxPeriod_Type(Integer32):
    """Custom type ccSecEapTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcSecEapTxPeriod_Type.__name__ = "Integer32"
_CcSecEapTxPeriod_Object = MibTableColumn
ccSecEapTxPeriod = _CcSecEapTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 27),
    _CcSecEapTxPeriod_Type()
)
ccSecEapTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapTxPeriod.setStatus("current")
_CcSecEapReauth_Type = TruthValue
_CcSecEapReauth_Object = MibTableColumn
ccSecEapReauth = _CcSecEapReauth_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 28),
    _CcSecEapReauth_Type()
)
ccSecEapReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapReauth.setStatus("current")


class _CcSecEapReauthPeriod_Type(Integer32):
    """Custom type ccSecEapReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_CcSecEapReauthPeriod_Type.__name__ = "Integer32"
_CcSecEapReauthPeriod_Object = MibTableColumn
ccSecEapReauthPeriod = _CcSecEapReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 29),
    _CcSecEapReauthPeriod_Type()
)
ccSecEapReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapReauthPeriod.setStatus("current")


class _CcSecEapReauthMaxRetries_Type(Integer32):
    """Custom type ccSecEapReauthMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcSecEapReauthMaxRetries_Type.__name__ = "Integer32"
_CcSecEapReauthMaxRetries_Object = MibTableColumn
ccSecEapReauthMaxRetries = _CcSecEapReauthMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 30),
    _CcSecEapReauthMaxRetries_Type()
)
ccSecEapReauthMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapReauthMaxRetries.setStatus("current")


class _CcSecEapSupplTimeout_Type(Integer32):
    """Custom type ccSecEapSupplTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcSecEapSupplTimeout_Type.__name__ = "Integer32"
_CcSecEapSupplTimeout_Object = MibTableColumn
ccSecEapSupplTimeout = _CcSecEapSupplTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 31),
    _CcSecEapSupplTimeout_Type()
)
ccSecEapSupplTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapSupplTimeout.setStatus("current")


class _CcSecEapMaxreqRetries_Type(Integer32):
    """Custom type ccSecEapMaxreqRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcSecEapMaxreqRetries_Type.__name__ = "Integer32"
_CcSecEapMaxreqRetries_Object = MibTableColumn
ccSecEapMaxreqRetries = _CcSecEapMaxreqRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 32),
    _CcSecEapMaxreqRetries_Type()
)
ccSecEapMaxreqRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecEapMaxreqRetries.setStatus("current")


class _CcSecGroupRekeyPeriod_Type(Integer32):
    """Custom type ccSecGroupRekeyPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_CcSecGroupRekeyPeriod_Type.__name__ = "Integer32"
_CcSecGroupRekeyPeriod_Object = MibTableColumn
ccSecGroupRekeyPeriod = _CcSecGroupRekeyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 33),
    _CcSecGroupRekeyPeriod_Type()
)
ccSecGroupRekeyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecGroupRekeyPeriod.setStatus("current")


class _CcSecPreSharedKeyMaterial_Type(DisplayString):
    """Custom type ccSecPreSharedKeyMaterial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcSecPreSharedKeyMaterial_Type.__name__ = "DisplayString"
_CcSecPreSharedKeyMaterial_Object = MibTableColumn
ccSecPreSharedKeyMaterial = _CcSecPreSharedKeyMaterial_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 34),
    _CcSecPreSharedKeyMaterial_Type()
)
ccSecPreSharedKeyMaterial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecPreSharedKeyMaterial.setStatus("current")
_CcSecOpenEncryptEnabled_Type = TruthValue
_CcSecOpenEncryptEnabled_Object = MibTableColumn
ccSecOpenEncryptEnabled = _CcSecOpenEncryptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 35),
    _CcSecOpenEncryptEnabled_Type()
)
ccSecOpenEncryptEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecOpenEncryptEnabled.setStatus("current")
_CcSecKeyGuardEnabled_Type = TruthValue
_CcSecKeyGuardEnabled_Object = MibTableColumn
ccSecKeyGuardEnabled = _CcSecKeyGuardEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 36),
    _CcSecKeyGuardEnabled_Type()
)
ccSecKeyGuardEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecKeyGuardEnabled.setStatus("current")
_CcSecTKIPEnabled_Type = TruthValue
_CcSecTKIPEnabled_Object = MibTableColumn
ccSecTKIPEnabled = _CcSecTKIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 37),
    _CcSecTKIPEnabled_Type()
)
ccSecTKIPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecTKIPEnabled.setStatus("current")
_CcSecBCMCEncrType_Type = EncrType
_CcSecBCMCEncrType_Object = MibTableColumn
ccSecBCMCEncrType = _CcSecBCMCEncrType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 38),
    _CcSecBCMCEncrType_Type()
)
ccSecBCMCEncrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSecBCMCEncrType.setStatus("deprecated")


class _CcSecCheckValidity_Type(DisplayString):
    """Custom type ccSecCheckValidity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1000),
    )


_CcSecCheckValidity_Type.__name__ = "DisplayString"
_CcSecCheckValidity_Object = MibTableColumn
ccSecCheckValidity = _CcSecCheckValidity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 39),
    _CcSecCheckValidity_Type()
)
ccSecCheckValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSecCheckValidity.setStatus("current")
_CcSecCCMPEnabled_Type = TruthValue
_CcSecCCMPEnabled_Object = MibTableColumn
ccSecCCMPEnabled = _CcSecCCMPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 40),
    _CcSecCCMPEnabled_Type()
)
ccSecCCMPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecCCMPEnabled.setStatus("current")
_CcSecPreAuthentication_Type = TruthValue
_CcSecPreAuthentication_Object = MibTableColumn
ccSecPreAuthentication = _CcSecPreAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 41),
    _CcSecPreAuthentication_Type()
)
ccSecPreAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecPreAuthentication.setStatus("current")
_CcSecPMKCaching_Type = TruthValue
_CcSecPMKCaching_Object = MibTableColumn
ccSecPMKCaching = _CcSecPMKCaching_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 42),
    _CcSecPMKCaching_Type()
)
ccSecPMKCaching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecPMKCaching.setStatus("current")
_CcSecVPNEnabled_Type = TruthValue
_CcSecVPNEnabled_Object = MibTableColumn
ccSecVPNEnabled = _CcSecVPNEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 28, 1, 43),
    _CcSecVPNEnabled_Type()
)
ccSecVPNEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSecVPNEnabled.setStatus("current")
_CcACLTable_Object = MibTable
ccACLTable = _CcACLTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29)
)
if mibBuilder.loadTexts:
    ccACLTable.setStatus("current")
_CcACLEntry_Object = MibTableRow
ccACLEntry = _CcACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1)
)
ccACLEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccACLIndex"),
)
if mibBuilder.loadTexts:
    ccACLEntry.setStatus("current")


class _CcACLIndex_Type(Integer32):
    """Custom type ccACLIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcACLIndex_Type.__name__ = "Integer32"
_CcACLIndex_Object = MibTableColumn
ccACLIndex = _CcACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 1),
    _CcACLIndex_Type()
)
ccACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccACLIndex.setStatus("current")


class _CcACLName_Type(DisplayString):
    """Custom type ccACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcACLName_Type.__name__ = "DisplayString"
_CcACLName_Object = MibTableColumn
ccACLName = _CcACLName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 2),
    _CcACLName_Type()
)
ccACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLName.setStatus("current")


class _CcACLDefaultAction_Type(DisplayString):
    """Custom type ccACLDefaultAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_CcACLDefaultAction_Type.__name__ = "DisplayString"
_CcACLDefaultAction_Object = MibTableColumn
ccACLDefaultAction = _CcACLDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 3),
    _CcACLDefaultAction_Type()
)
ccACLDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLDefaultAction.setStatus("current")


class _CcACLAction_Type(DisplayString):
    """Custom type ccACLAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 100),
    )


_CcACLAction_Type.__name__ = "DisplayString"
_CcACLAction_Object = MibTableColumn
ccACLAction = _CcACLAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 4),
    _CcACLAction_Type()
)
ccACLAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLAction.setStatus("current")


class _CcACLGetItemCount_Type(Integer32):
    """Custom type ccACLGetItemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcACLGetItemCount_Type.__name__ = "Integer32"
_CcACLGetItemCount_Object = MibTableColumn
ccACLGetItemCount = _CcACLGetItemCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 5),
    _CcACLGetItemCount_Type()
)
ccACLGetItemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccACLGetItemCount.setStatus("current")


class _CcACLGetItem_Type(DisplayString):
    """Custom type ccACLGetItem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CcACLGetItem_Type.__name__ = "DisplayString"
_CcACLGetItem_Object = MibTableColumn
ccACLGetItem = _CcACLGetItem_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 6),
    _CcACLGetItem_Type()
)
ccACLGetItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccACLGetItem.setStatus("deprecated")


class _CcACLAddItem_Type(DisplayString):
    """Custom type ccACLAddItem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CcACLAddItem_Type.__name__ = "DisplayString"
_CcACLAddItem_Object = MibTableColumn
ccACLAddItem = _CcACLAddItem_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 7),
    _CcACLAddItem_Type()
)
ccACLAddItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLAddItem.setStatus("current")


class _CcACLRemItem_Type(DisplayString):
    """Custom type ccACLRemItem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CcACLRemItem_Type.__name__ = "DisplayString"
_CcACLRemItem_Object = MibTableColumn
ccACLRemItem = _CcACLRemItem_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 29, 1, 8),
    _CcACLRemItem_Type()
)
ccACLRemItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccACLRemItem.setStatus("current")
_CcNPolicyMgmt_ObjectIdentity = ObjectIdentity
ccNPolicyMgmt = _CcNPolicyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30)
)


class _CcNumNPRec_Type(Integer32):
    """Custom type ccNumNPRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcNumNPRec_Type.__name__ = "Integer32"
_CcNumNPRec_Object = MibScalar
ccNumNPRec = _CcNumNPRec_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 1),
    _CcNumNPRec_Type()
)
ccNumNPRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNumNPRec.setStatus("current")


class _CcNumPORec_Type(Integer32):
    """Custom type ccNumPORec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcNumPORec_Type.__name__ = "Integer32"
_CcNumPORec_Object = MibScalar
ccNumPORec = _CcNumPORec_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 2),
    _CcNumPORec_Type()
)
ccNumPORec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNumPORec.setStatus("current")


class _CcNumCGRec_Type(Integer32):
    """Custom type ccNumCGRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcNumCGRec_Type.__name__ = "Integer32"
_CcNumCGRec_Object = MibScalar
ccNumCGRec = _CcNumCGRec_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 3),
    _CcNumCGRec_Type()
)
ccNumCGRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNumCGRec.setStatus("current")


class _CcNumCFRec_Type(Integer32):
    """Custom type ccNumCFRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcNumCFRec_Type.__name__ = "Integer32"
_CcNumCFRec_Object = MibScalar
ccNumCFRec = _CcNumCFRec_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 4),
    _CcNumCFRec_Type()
)
ccNumCFRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNumCFRec.setStatus("current")


class _CcCFAddObj_Type(DisplayString):
    """Custom type ccCFAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCFAddObj_Type.__name__ = "DisplayString"
_CcCFAddObj_Object = MibScalar
ccCFAddObj = _CcCFAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 5),
    _CcCFAddObj_Type()
)
ccCFAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFAddObj.setStatus("current")


class _CcCFRemObj_Type(DisplayString):
    """Custom type ccCFRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCFRemObj_Type.__name__ = "DisplayString"
_CcCFRemObj_Object = MibScalar
ccCFRemObj = _CcCFRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 6),
    _CcCFRemObj_Type()
)
ccCFRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFRemObj.setStatus("current")


class _CcCGAddObj_Type(DisplayString):
    """Custom type ccCGAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCGAddObj_Type.__name__ = "DisplayString"
_CcCGAddObj_Object = MibScalar
ccCGAddObj = _CcCGAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 7),
    _CcCGAddObj_Type()
)
ccCGAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGAddObj.setStatus("current")


class _CcCGRemObj_Type(DisplayString):
    """Custom type ccCGRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCGRemObj_Type.__name__ = "DisplayString"
_CcCGRemObj_Object = MibScalar
ccCGRemObj = _CcCGRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 8),
    _CcCGRemObj_Type()
)
ccCGRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGRemObj.setStatus("current")


class _CcPOAddObj_Type(DisplayString):
    """Custom type ccPOAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPOAddObj_Type.__name__ = "DisplayString"
_CcPOAddObj_Object = MibScalar
ccPOAddObj = _CcPOAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 9),
    _CcPOAddObj_Type()
)
ccPOAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOAddObj.setStatus("current")


class _CcPORemObj_Type(DisplayString):
    """Custom type ccPORemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPORemObj_Type.__name__ = "DisplayString"
_CcPORemObj_Object = MibScalar
ccPORemObj = _CcPORemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 10),
    _CcPORemObj_Type()
)
ccPORemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPORemObj.setStatus("current")


class _CcNPAddObj_Type(DisplayString):
    """Custom type ccNPAddObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcNPAddObj_Type.__name__ = "DisplayString"
_CcNPAddObj_Object = MibScalar
ccNPAddObj = _CcNPAddObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 11),
    _CcNPAddObj_Type()
)
ccNPAddObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNPAddObj.setStatus("current")


class _CcNPRemObj_Type(DisplayString):
    """Custom type ccNPRemObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcNPRemObj_Type.__name__ = "DisplayString"
_CcNPRemObj_Object = MibScalar
ccNPRemObj = _CcNPRemObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 12),
    _CcNPRemObj_Type()
)
ccNPRemObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNPRemObj.setStatus("current")
_CcNPTable_Object = MibTable
ccNPTable = _CcNPTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13)
)
if mibBuilder.loadTexts:
    ccNPTable.setStatus("current")
_CcNPEntry_Object = MibTableRow
ccNPEntry = _CcNPEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13, 1)
)
ccNPEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccNPIndex"),
)
if mibBuilder.loadTexts:
    ccNPEntry.setStatus("current")


class _CcNPIndex_Type(Integer32):
    """Custom type ccNPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcNPIndex_Type.__name__ = "Integer32"
_CcNPIndex_Object = MibTableColumn
ccNPIndex = _CcNPIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13, 1, 1),
    _CcNPIndex_Type()
)
ccNPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNPIndex.setStatus("current")


class _CcNPName_Type(DisplayString):
    """Custom type ccNPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcNPName_Type.__name__ = "DisplayString"
_CcNPName_Object = MibTableColumn
ccNPName = _CcNPName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13, 1, 2),
    _CcNPName_Type()
)
ccNPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNPName.setStatus("current")


class _CcNPDesc_Type(DisplayString):
    """Custom type ccNPDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcNPDesc_Type.__name__ = "DisplayString"
_CcNPDesc_Object = MibTableColumn
ccNPDesc = _CcNPDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13, 1, 3),
    _CcNPDesc_Type()
)
ccNPDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNPDesc.setStatus("current")


class _CcNPInName_Type(DisplayString):
    """Custom type ccNPInName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcNPInName_Type.__name__ = "DisplayString"
_CcNPInName_Object = MibTableColumn
ccNPInName = _CcNPInName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13, 1, 4),
    _CcNPInName_Type()
)
ccNPInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNPInName.setStatus("current")


class _CcNPOutName_Type(DisplayString):
    """Custom type ccNPOutName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcNPOutName_Type.__name__ = "DisplayString"
_CcNPOutName_Object = MibTableColumn
ccNPOutName = _CcNPOutName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 13, 1, 5),
    _CcNPOutName_Type()
)
ccNPOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNPOutName.setStatus("current")
_CcPOTable_Object = MibTable
ccPOTable = _CcPOTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14)
)
if mibBuilder.loadTexts:
    ccPOTable.setStatus("current")
_CcPOEntry_Object = MibTableRow
ccPOEntry = _CcPOEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1)
)
ccPOEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPOIndex"),
)
if mibBuilder.loadTexts:
    ccPOEntry.setStatus("current")


class _CcPOIndex_Type(Integer32):
    """Custom type ccPOIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcPOIndex_Type.__name__ = "Integer32"
_CcPOIndex_Object = MibTableColumn
ccPOIndex = _CcPOIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 1),
    _CcPOIndex_Type()
)
ccPOIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccPOIndex.setStatus("current")


class _CcPOName_Type(DisplayString):
    """Custom type ccPOName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPOName_Type.__name__ = "DisplayString"
_CcPOName_Object = MibTableColumn
ccPOName = _CcPOName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 2),
    _CcPOName_Type()
)
ccPOName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOName.setStatus("current")


class _CcPODesc_Type(DisplayString):
    """Custom type ccPODesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcPODesc_Type.__name__ = "DisplayString"
_CcPODesc_Object = MibTableColumn
ccPODesc = _CcPODesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 3),
    _CcPODesc_Type()
)
ccPODesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPODesc.setStatus("current")


class _CcPOCgCount_Type(Integer32):
    """Custom type ccPOCgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcPOCgCount_Type.__name__ = "Integer32"
_CcPOCgCount_Object = MibTableColumn
ccPOCgCount = _CcPOCgCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 4),
    _CcPOCgCount_Type()
)
ccPOCgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPOCgCount.setStatus("current")


class _CcPOAddCg_Type(DisplayString):
    """Custom type ccPOAddCg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPOAddCg_Type.__name__ = "DisplayString"
_CcPOAddCg_Object = MibTableColumn
ccPOAddCg = _CcPOAddCg_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 11),
    _CcPOAddCg_Type()
)
ccPOAddCg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOAddCg.setStatus("current")


class _CcPORemCg_Type(DisplayString):
    """Custom type ccPORemCg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPORemCg_Type.__name__ = "DisplayString"
_CcPORemCg_Object = MibTableColumn
ccPORemCg = _CcPORemCg_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 12),
    _CcPORemCg_Type()
)
ccPORemCg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPORemCg.setStatus("current")


class _CcPOType_Type(Integer32):
    """Custom type ccPOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcPOType_Type.__name__ = "Integer32"
_CcPOType_Object = MibTableColumn
ccPOType = _CcPOType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 13),
    _CcPOType_Type()
)
ccPOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPOType.setStatus("current")


class _CcPOPacketModifier_Type(DisplayString):
    """Custom type ccPOPacketModifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcPOPacketModifier_Type.__name__ = "DisplayString"
_CcPOPacketModifier_Object = MibTableColumn
ccPOPacketModifier = _CcPOPacketModifier_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 14, 1, 14),
    _CcPOPacketModifier_Type()
)
ccPOPacketModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPOPacketModifier.setStatus("deprecated")
_CcCGTable_Object = MibTable
ccCGTable = _CcCGTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15)
)
if mibBuilder.loadTexts:
    ccCGTable.setStatus("current")
_CcCGEntry_Object = MibTableRow
ccCGEntry = _CcCGEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1)
)
ccCGEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccCGIndex"),
)
if mibBuilder.loadTexts:
    ccCGEntry.setStatus("current")


class _CcCGIndex_Type(Integer32):
    """Custom type ccCGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCGIndex_Type.__name__ = "Integer32"
_CcCGIndex_Object = MibTableColumn
ccCGIndex = _CcCGIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1, 1),
    _CcCGIndex_Type()
)
ccCGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCGIndex.setStatus("current")


class _CcCGName_Type(DisplayString):
    """Custom type ccCGName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCGName_Type.__name__ = "DisplayString"
_CcCGName_Object = MibTableColumn
ccCGName = _CcCGName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1, 2),
    _CcCGName_Type()
)
ccCGName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGName.setStatus("current")


class _CcCGDesc_Type(DisplayString):
    """Custom type ccCGDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcCGDesc_Type.__name__ = "DisplayString"
_CcCGDesc_Object = MibTableColumn
ccCGDesc = _CcCGDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1, 3),
    _CcCGDesc_Type()
)
ccCGDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGDesc.setStatus("current")


class _CcCGCfCount_Type(Integer32):
    """Custom type ccCGCfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCGCfCount_Type.__name__ = "Integer32"
_CcCGCfCount_Object = MibTableColumn
ccCGCfCount = _CcCGCfCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1, 4),
    _CcCGCfCount_Type()
)
ccCGCfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCGCfCount.setStatus("current")


class _CcCGAddCf_Type(DisplayString):
    """Custom type ccCGAddCf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCGAddCf_Type.__name__ = "DisplayString"
_CcCGAddCf_Object = MibTableColumn
ccCGAddCf = _CcCGAddCf_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1, 7),
    _CcCGAddCf_Type()
)
ccCGAddCf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGAddCf.setStatus("current")


class _CcCGRemCf_Type(DisplayString):
    """Custom type ccCGRemCf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCGRemCf_Type.__name__ = "DisplayString"
_CcCGRemCf_Object = MibTableColumn
ccCGRemCf = _CcCGRemCf_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 15, 1, 8),
    _CcCGRemCf_Type()
)
ccCGRemCf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGRemCf.setStatus("current")
_CcCFTable_Object = MibTable
ccCFTable = _CcCFTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16)
)
if mibBuilder.loadTexts:
    ccCFTable.setStatus("current")
_CcCFEntry_Object = MibTableRow
ccCFEntry = _CcCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1)
)
ccCFEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccCFIndex"),
)
if mibBuilder.loadTexts:
    ccCFEntry.setStatus("current")


class _CcCFIndex_Type(Integer32):
    """Custom type ccCFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCFIndex_Type.__name__ = "Integer32"
_CcCFIndex_Object = MibTableColumn
ccCFIndex = _CcCFIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1, 1),
    _CcCFIndex_Type()
)
ccCFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCFIndex.setStatus("current")


class _CcCFName_Type(DisplayString):
    """Custom type ccCFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCFName_Type.__name__ = "DisplayString"
_CcCFName_Object = MibTableColumn
ccCFName = _CcCFName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1, 2),
    _CcCFName_Type()
)
ccCFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFName.setStatus("current")


class _CcCFDesc_Type(DisplayString):
    """Custom type ccCFDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcCFDesc_Type.__name__ = "DisplayString"
_CcCFDesc_Object = MibTableColumn
ccCFDesc = _CcCFDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1, 3),
    _CcCFDesc_Type()
)
ccCFDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFDesc.setStatus("current")


class _CcCFMcCount_Type(Integer32):
    """Custom type ccCFMcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCFMcCount_Type.__name__ = "Integer32"
_CcCFMcCount_Object = MibTableColumn
ccCFMcCount = _CcCFMcCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1, 4),
    _CcCFMcCount_Type()
)
ccCFMcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCFMcCount.setStatus("current")
_CcCFAddMc_Type = MCValueOffset
_CcCFAddMc_Object = MibTableColumn
ccCFAddMc = _CcCFAddMc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1, 10),
    _CcCFAddMc_Type()
)
ccCFAddMc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFAddMc.setStatus("current")
_CcCFRemMc_Type = MCValueOffset
_CcCFRemMc_Object = MibTableColumn
ccCFRemMc = _CcCFRemMc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 16, 1, 11),
    _CcCFRemMc_Type()
)
ccCFRemMc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFRemMc.setStatus("current")
_CcPOObjects_ObjectIdentity = ObjectIdentity
ccPOObjects = _CcPOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17)
)
_CcPOCGTable_Object = MibTable
ccPOCGTable = _CcPOCGTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2)
)
if mibBuilder.loadTexts:
    ccPOCGTable.setStatus("current")
_CcPOCGEntry_Object = MibTableRow
ccPOCGEntry = _CcPOCGEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1)
)
ccPOCGEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPOCGIndex"),
)
if mibBuilder.loadTexts:
    ccPOCGEntry.setStatus("current")


class _CcPOCGIndex_Type(Integer32):
    """Custom type ccPOCGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcPOCGIndex_Type.__name__ = "Integer32"
_CcPOCGIndex_Object = MibTableColumn
ccPOCGIndex = _CcPOCGIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 1),
    _CcPOCGIndex_Type()
)
ccPOCGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccPOCGIndex.setStatus("current")


class _CcPOCGName_Type(DisplayString):
    """Custom type ccPOCGName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcPOCGName_Type.__name__ = "DisplayString"
_CcPOCGName_Object = MibTableColumn
ccPOCGName = _CcPOCGName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 2),
    _CcPOCGName_Type()
)
ccPOCGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPOCGName.setStatus("current")


class _CcPOCGNewIP_Type(DisplayString):
    """Custom type ccPOCGNewIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CcPOCGNewIP_Type.__name__ = "DisplayString"
_CcPOCGNewIP_Object = MibTableColumn
ccPOCGNewIP = _CcPOCGNewIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 3),
    _CcPOCGNewIP_Type()
)
ccPOCGNewIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOCGNewIP.setStatus("current")


class _CcPOCGVlanPriority_Type(DisplayString):
    """Custom type ccPOCGVlanPriority based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcPOCGVlanPriority_Type.__name__ = "DisplayString"
_CcPOCGVlanPriority_Object = MibTableColumn
ccPOCGVlanPriority = _CcPOCGVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 4),
    _CcPOCGVlanPriority_Type()
)
ccPOCGVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOCGVlanPriority.setStatus("current")


class _CcPOCGTos_Type(DisplayString):
    """Custom type ccPOCGTos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcPOCGTos_Type.__name__ = "DisplayString"
_CcPOCGTos_Object = MibTableColumn
ccPOCGTos = _CcPOCGTos_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 5),
    _CcPOCGTos_Type()
)
ccPOCGTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOCGTos.setStatus("current")


class _CcPOCGBw_Type(Integer32):
    """Custom type ccPOCGBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcPOCGBw_Type.__name__ = "Integer32"
_CcPOCGBw_Object = MibTableColumn
ccPOCGBw = _CcPOCGBw_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 6),
    _CcPOCGBw_Type()
)
ccPOCGBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOCGBw.setStatus("current")


class _CcPOCGTxProfile_Type(Integer32):
    """Custom type ccPOCGTxProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CcPOCGTxProfile_Type.__name__ = "Integer32"
_CcPOCGTxProfile_Object = MibTableColumn
ccPOCGTxProfile = _CcPOCGTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 7),
    _CcPOCGTxProfile_Type()
)
ccPOCGTxProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPOCGTxProfile.setStatus("current")


class _CcPOCGPacketModifier_Type(DisplayString):
    """Custom type ccPOCGPacketModifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcPOCGPacketModifier_Type.__name__ = "DisplayString"
_CcPOCGPacketModifier_Object = MibTableColumn
ccPOCGPacketModifier = _CcPOCGPacketModifier_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 17, 2, 1, 8),
    _CcPOCGPacketModifier_Type()
)
ccPOCGPacketModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPOCGPacketModifier.setStatus("current")
_CcCGObjects_ObjectIdentity = ObjectIdentity
ccCGObjects = _CcCGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 18)
)
_CcCGCFTable_Object = MibTable
ccCGCFTable = _CcCGCFTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 18, 2)
)
if mibBuilder.loadTexts:
    ccCGCFTable.setStatus("current")
_CcCGCFEntry_Object = MibTableRow
ccCGCFEntry = _CcCGCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 18, 2, 1)
)
ccCGCFEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccCGIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccCGCFIndex"),
)
if mibBuilder.loadTexts:
    ccCGCFEntry.setStatus("current")


class _CcCGCFIndex_Type(Integer32):
    """Custom type ccCGCFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcCGCFIndex_Type.__name__ = "Integer32"
_CcCGCFIndex_Object = MibTableColumn
ccCGCFIndex = _CcCGCFIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 18, 2, 1, 1),
    _CcCGCFIndex_Type()
)
ccCGCFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCGCFIndex.setStatus("current")


class _CcCGCFAction_Type(DisplayString):
    """Custom type ccCGCFAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_CcCGCFAction_Type.__name__ = "DisplayString"
_CcCGCFAction_Object = MibTableColumn
ccCGCFAction = _CcCGCFAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 18, 2, 1, 2),
    _CcCGCFAction_Type()
)
ccCGCFAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCGCFAction.setStatus("current")


class _CcCGCFName_Type(DisplayString):
    """Custom type ccCGCFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCGCFName_Type.__name__ = "DisplayString"
_CcCGCFName_Object = MibTableColumn
ccCGCFName = _CcCGCFName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 18, 2, 1, 3),
    _CcCGCFName_Type()
)
ccCGCFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCGCFName.setStatus("current")
_CcCFObjects_ObjectIdentity = ObjectIdentity
ccCFObjects = _CcCFObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19)
)
_CcCFMcTable_Object = MibTable
ccCFMcTable = _CcCFMcTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2)
)
if mibBuilder.loadTexts:
    ccCFMcTable.setStatus("current")
_CcCFMcEntry_Object = MibTableRow
ccCFMcEntry = _CcCFMcEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2, 1)
)
ccCFMcEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccCFIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccCFMCIndex"),
)
if mibBuilder.loadTexts:
    ccCFMcEntry.setStatus("current")


class _CcCFMCIndex_Type(Integer32):
    """Custom type ccCFMCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcCFMCIndex_Type.__name__ = "Integer32"
_CcCFMCIndex_Object = MibTableColumn
ccCFMCIndex = _CcCFMCIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2, 1, 1),
    _CcCFMCIndex_Type()
)
ccCFMCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCFMCIndex.setStatus("current")
_CcCFMCOffset_Type = MCValueOffset
_CcCFMCOffset_Object = MibTableColumn
ccCFMCOffset = _CcCFMCOffset_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2, 1, 2),
    _CcCFMCOffset_Type()
)
ccCFMCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCFMCOffset.setStatus("current")


class _CcCFMCValueCount_Type(Integer32):
    """Custom type ccCFMCValueCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcCFMCValueCount_Type.__name__ = "Integer32"
_CcCFMCValueCount_Object = MibTableColumn
ccCFMCValueCount = _CcCFMCValueCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2, 1, 3),
    _CcCFMCValueCount_Type()
)
ccCFMCValueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCFMCValueCount.setStatus("current")
_CcCFAddMCValue_Type = DisplayString
_CcCFAddMCValue_Object = MibTableColumn
ccCFAddMCValue = _CcCFAddMCValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2, 1, 4),
    _CcCFAddMCValue_Type()
)
ccCFAddMCValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFAddMCValue.setStatus("current")


class _CcCFRemMCValue_Type(DisplayString):
    """Custom type ccCFRemMCValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcCFRemMCValue_Type.__name__ = "DisplayString"
_CcCFRemMCValue_Object = MibTableColumn
ccCFRemMCValue = _CcCFRemMCValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 2, 1, 5),
    _CcCFRemMCValue_Type()
)
ccCFRemMCValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCFRemMCValue.setStatus("current")
_CcCFMcValTable_Object = MibTable
ccCFMcValTable = _CcCFMcValTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 3)
)
if mibBuilder.loadTexts:
    ccCFMcValTable.setStatus("current")
_CcCFMcValEntry_Object = MibTableRow
ccCFMcValEntry = _CcCFMcValEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 3, 1)
)
ccCFMcValEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccCFIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccCFMCIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccCFMcValIndex"),
)
if mibBuilder.loadTexts:
    ccCFMcValEntry.setStatus("current")


class _CcCFMcValIndex_Type(Integer32):
    """Custom type ccCFMcValIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CcCFMcValIndex_Type.__name__ = "Integer32"
_CcCFMcValIndex_Object = MibTableColumn
ccCFMcValIndex = _CcCFMcValIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 3, 1, 1),
    _CcCFMcValIndex_Type()
)
ccCFMcValIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCFMcValIndex.setStatus("current")


class _CcCFMCValue_Type(DisplayString):
    """Custom type ccCFMCValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CcCFMCValue_Type.__name__ = "DisplayString"
_CcCFMCValue_Object = MibTableColumn
ccCFMCValue = _CcCFMCValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 30, 19, 3, 1, 2),
    _CcCFMCValue_Type()
)
ccCFMCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCFMCValue.setStatus("current")
_CcHSBConfigure_ObjectIdentity = ObjectIdentity
ccHSBConfigure = _CcHSBConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31)
)
_CcHsbEnabled_Type = TruthValue
_CcHsbEnabled_Object = MibScalar
ccHsbEnabled = _CcHsbEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 1),
    _CcHsbEnabled_Type()
)
ccHsbEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbEnabled.setStatus("current")


class _CcHsbMode_Type(DisplayString):
    """Custom type ccHsbMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcHsbMode_Type.__name__ = "DisplayString"
_CcHsbMode_Object = MibScalar
ccHsbMode = _CcHsbMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 2),
    _CcHsbMode_Type()
)
ccHsbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbMode.setStatus("current")


class _CcHsbMacAddress1_Type(DisplayString):
    """Custom type ccHsbMacAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcHsbMacAddress1_Type.__name__ = "DisplayString"
_CcHsbMacAddress1_Object = MibScalar
ccHsbMacAddress1 = _CcHsbMacAddress1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 3),
    _CcHsbMacAddress1_Type()
)
ccHsbMacAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbMacAddress1.setStatus("current")


class _CcHsbMacAddress2_Type(DisplayString):
    """Custom type ccHsbMacAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcHsbMacAddress2_Type.__name__ = "DisplayString"
_CcHsbMacAddress2_Object = MibScalar
ccHsbMacAddress2 = _CcHsbMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 4),
    _CcHsbMacAddress2_Type()
)
ccHsbMacAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbMacAddress2.setStatus("current")
_CcHsbHeartbeatEnabledOnInterface1_Type = TruthValue
_CcHsbHeartbeatEnabledOnInterface1_Object = MibScalar
ccHsbHeartbeatEnabledOnInterface1 = _CcHsbHeartbeatEnabledOnInterface1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 5),
    _CcHsbHeartbeatEnabledOnInterface1_Type()
)
ccHsbHeartbeatEnabledOnInterface1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbHeartbeatEnabledOnInterface1.setStatus("current")
_CcHsbHeartbeatEnabledOnInterface2_Type = TruthValue
_CcHsbHeartbeatEnabledOnInterface2_Object = MibScalar
ccHsbHeartbeatEnabledOnInterface2 = _CcHsbHeartbeatEnabledOnInterface2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 6),
    _CcHsbHeartbeatEnabledOnInterface2_Type()
)
ccHsbHeartbeatEnabledOnInterface2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbHeartbeatEnabledOnInterface2.setStatus("current")
_CcHsbConnectivityFlag_Type = TruthValue
_CcHsbConnectivityFlag_Object = MibScalar
ccHsbConnectivityFlag = _CcHsbConnectivityFlag_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 7),
    _CcHsbConnectivityFlag_Type()
)
ccHsbConnectivityFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHsbConnectivityFlag.setStatus("current")
_CcHsbFailoverState_Type = HsbState
_CcHsbFailoverState_Object = MibScalar
ccHsbFailoverState = _CcHsbFailoverState_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 8),
    _CcHsbFailoverState_Type()
)
ccHsbFailoverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHsbFailoverState.setStatus("current")


class _CcHsbFailoverReason_Type(DisplayString):
    """Custom type ccHsbFailoverReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcHsbFailoverReason_Type.__name__ = "DisplayString"
_CcHsbFailoverReason_Object = MibScalar
ccHsbFailoverReason = _CcHsbFailoverReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 9),
    _CcHsbFailoverReason_Type()
)
ccHsbFailoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHsbFailoverReason.setStatus("current")


class _CcHsbResetCode_Type(Integer32):
    """Custom type ccHsbResetCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CcHsbResetCode_Type.__name__ = "Integer32"
_CcHsbResetCode_Object = MibScalar
ccHsbResetCode = _CcHsbResetCode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 10),
    _CcHsbResetCode_Type()
)
ccHsbResetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHsbResetCode.setStatus("current")
_CcHsbRevert_Type = TruthValue
_CcHsbRevert_Object = MibScalar
ccHsbRevert = _CcHsbRevert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 11),
    _CcHsbRevert_Type()
)
ccHsbRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbRevert.setStatus("current")
_CcHsbautorevert_Type = TruthValue
_CcHsbautorevert_Object = MibScalar
ccHsbautorevert = _CcHsbautorevert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 12),
    _CcHsbautorevert_Type()
)
ccHsbautorevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbautorevert.setStatus("current")


class _CcHsbautorevertdelay_Type(Integer32):
    """Custom type ccHsbautorevertdelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CcHsbautorevertdelay_Type.__name__ = "Integer32"
_CcHsbautorevertdelay_Object = MibScalar
ccHsbautorevertdelay = _CcHsbautorevertdelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 31, 13),
    _CcHsbautorevertdelay_Type()
)
ccHsbautorevertdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHsbautorevertdelay.setStatus("current")
_CcMUInfoTable_Object = MibTable
ccMUInfoTable = _CcMUInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32)
)
if mibBuilder.loadTexts:
    ccMUInfoTable.setStatus("current")
_CcMUInfoEntry_Object = MibTableRow
ccMUInfoEntry = _CcMUInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1)
)
ccMUInfoEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMUInfoIndex"),
)
if mibBuilder.loadTexts:
    ccMUInfoEntry.setStatus("current")


class _CcMUInfoIndex_Type(Integer32):
    """Custom type ccMUInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcMUInfoIndex_Type.__name__ = "Integer32"
_CcMUInfoIndex_Object = MibTableColumn
ccMUInfoIndex = _CcMUInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 1),
    _CcMUInfoIndex_Type()
)
ccMUInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoIndex.setStatus("current")
_CcMUInfoType_Type = MUDeviceType
_CcMUInfoType_Object = MibTableColumn
ccMUInfoType = _CcMUInfoType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 2),
    _CcMUInfoType_Type()
)
ccMUInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoType.setStatus("current")


class _CcMUInfoMac_Type(DisplayString):
    """Custom type ccMUInfoMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcMUInfoMac_Type.__name__ = "DisplayString"
_CcMUInfoMac_Object = MibTableColumn
ccMUInfoMac = _CcMUInfoMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 3),
    _CcMUInfoMac_Type()
)
ccMUInfoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoMac.setStatus("current")


class _CcMUInfoIP_Type(DisplayString):
    """Custom type ccMUInfoIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcMUInfoIP_Type.__name__ = "DisplayString"
_CcMUInfoIP_Object = MibTableColumn
ccMUInfoIP = _CcMUInfoIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 4),
    _CcMUInfoIP_Type()
)
ccMUInfoIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoIP.setStatus("current")


class _CcMUInfoWlan_Type(DisplayString):
    """Custom type ccMUInfoWlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoWlan_Type.__name__ = "DisplayString"
_CcMUInfoWlan_Object = MibTableColumn
ccMUInfoWlan = _CcMUInfoWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 5),
    _CcMUInfoWlan_Type()
)
ccMUInfoWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoWlan.setStatus("current")


class _CcMUInfoEssid_Type(DisplayString):
    """Custom type ccMUInfoEssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoEssid_Type.__name__ = "DisplayString"
_CcMUInfoEssid_Object = MibTableColumn
ccMUInfoEssid = _CcMUInfoEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 6),
    _CcMUInfoEssid_Type()
)
ccMUInfoEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoEssid.setStatus("current")
_CcMUInfoAP_Type = DisplayString
_CcMUInfoAP_Object = MibTableColumn
ccMUInfoAP = _CcMUInfoAP_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 7),
    _CcMUInfoAP_Type()
)
ccMUInfoAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoAP.setStatus("current")
_CcMUInfoAPState_Type = APStatus
_CcMUInfoAPState_Object = MibTableColumn
ccMUInfoAPState = _CcMUInfoAPState_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 8),
    _CcMUInfoAPState_Type()
)
ccMUInfoAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoAPState.setStatus("current")
_CcMUInfoSecState_Type = MUSecurityStatus
_CcMUInfoSecState_Object = MibTableColumn
ccMUInfoSecState = _CcMUInfoSecState_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 9),
    _CcMUInfoSecState_Type()
)
ccMUInfoSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoSecState.setStatus("current")
_CcMUInfoCurRate_Type = CurrentRate
_CcMUInfoCurRate_Object = MibTableColumn
ccMUInfoCurRate = _CcMUInfoCurRate_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 10),
    _CcMUInfoCurRate_Type()
)
ccMUInfoCurRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoCurRate.setStatus("current")


class _CcMUInfoSupRates_Type(DisplayString):
    """Custom type ccMUInfoSupRates based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CcMUInfoSupRates_Type.__name__ = "DisplayString"
_CcMUInfoSupRates_Object = MibTableColumn
ccMUInfoSupRates = _CcMUInfoSupRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 11),
    _CcMUInfoSupRates_Type()
)
ccMUInfoSupRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoSupRates.setStatus("current")


class _CcMUInfoRssi_Type(DisplayString):
    """Custom type ccMUInfoRssi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CcMUInfoRssi_Type.__name__ = "DisplayString"
_CcMUInfoRssi_Object = MibTableColumn
ccMUInfoRssi = _CcMUInfoRssi_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 12),
    _CcMUInfoRssi_Type()
)
ccMUInfoRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoRssi.setStatus("current")
_CcMUInfoPsp_Type = PSPowerMode
_CcMUInfoPsp_Object = MibTableColumn
ccMUInfoPsp = _CcMUInfoPsp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 13),
    _CcMUInfoPsp_Type()
)
ccMUInfoPsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoPsp.setStatus("current")


class _CcMUInfoIntf_Type(DisplayString):
    """Custom type ccMUInfoIntf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoIntf_Type.__name__ = "DisplayString"
_CcMUInfoIntf_Object = MibTableColumn
ccMUInfoIntf = _CcMUInfoIntf_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 14),
    _CcMUInfoIntf_Type()
)
ccMUInfoIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoIntf.setStatus("current")


class _CcMUInfoAsscUptime_Type(DisplayString):
    """Custom type ccMUInfoAsscUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoAsscUptime_Type.__name__ = "DisplayString"
_CcMUInfoAsscUptime_Object = MibTableColumn
ccMUInfoAsscUptime = _CcMUInfoAsscUptime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 15),
    _CcMUInfoAsscUptime_Type()
)
ccMUInfoAsscUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoAsscUptime.setStatus("current")


class _CcMUInfoTktExp_Type(DisplayString):
    """Custom type ccMUInfoTktExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoTktExp_Type.__name__ = "DisplayString"
_CcMUInfoTktExp_Object = MibTableColumn
ccMUInfoTktExp = _CcMUInfoTktExp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 16),
    _CcMUInfoTktExp_Type()
)
ccMUInfoTktExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoTktExp.setStatus("current")


class _CcMUInfoUserName_Type(DisplayString):
    """Custom type ccMUInfoUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoUserName_Type.__name__ = "DisplayString"
_CcMUInfoUserName_Object = MibTableColumn
ccMUInfoUserName = _CcMUInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 17),
    _CcMUInfoUserName_Type()
)
ccMUInfoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoUserName.setStatus("current")


class _CcMUInfoPktTx_Type(DisplayString):
    """Custom type ccMUInfoPktTx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoPktTx_Type.__name__ = "DisplayString"
_CcMUInfoPktTx_Object = MibTableColumn
ccMUInfoPktTx = _CcMUInfoPktTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 18),
    _CcMUInfoPktTx_Type()
)
ccMUInfoPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoPktTx.setStatus("current")


class _CcMUInfoPktRx_Type(DisplayString):
    """Custom type ccMUInfoPktRx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoPktRx_Type.__name__ = "DisplayString"
_CcMUInfoPktRx_Object = MibTableColumn
ccMUInfoPktRx = _CcMUInfoPktRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 19),
    _CcMUInfoPktRx_Type()
)
ccMUInfoPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoPktRx.setStatus("current")


class _CcMUInfoBytesTx_Type(DisplayString):
    """Custom type ccMUInfoBytesTx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoBytesTx_Type.__name__ = "DisplayString"
_CcMUInfoBytesTx_Object = MibTableColumn
ccMUInfoBytesTx = _CcMUInfoBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 20),
    _CcMUInfoBytesTx_Type()
)
ccMUInfoBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoBytesTx.setStatus("current")


class _CcMUInfoBytesRx_Type(DisplayString):
    """Custom type ccMUInfoBytesRx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoBytesRx_Type.__name__ = "DisplayString"
_CcMUInfoBytesRx_Object = MibTableColumn
ccMUInfoBytesRx = _CcMUInfoBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 21),
    _CcMUInfoBytesRx_Type()
)
ccMUInfoBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoBytesRx.setStatus("current")


class _CcMUInfoLastAct_Type(DisplayString):
    """Custom type ccMUInfoLastAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoLastAct_Type.__name__ = "DisplayString"
_CcMUInfoLastAct_Object = MibTableColumn
ccMUInfoLastAct = _CcMUInfoLastAct_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 22),
    _CcMUInfoLastAct_Type()
)
ccMUInfoLastAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoLastAct.setStatus("current")


class _CcMUInfoVlan_Type(DisplayString):
    """Custom type ccMUInfoVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_CcMUInfoVlan_Type.__name__ = "DisplayString"
_CcMUInfoVlan_Object = MibTableColumn
ccMUInfoVlan = _CcMUInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 23),
    _CcMUInfoVlan_Type()
)
ccMUInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoVlan.setStatus("current")
_CcMUInfoAuthState_Type = AuthState
_CcMUInfoAuthState_Object = MibTableColumn
ccMUInfoAuthState = _CcMUInfoAuthState_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 24),
    _CcMUInfoAuthState_Type()
)
ccMUInfoAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoAuthState.setStatus("current")
_CcMUInfoAuthMethod_Type = AuthMethod
_CcMUInfoAuthMethod_Object = MibTableColumn
ccMUInfoAuthMethod = _CcMUInfoAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 25),
    _CcMUInfoAuthMethod_Type()
)
ccMUInfoAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoAuthMethod.setStatus("current")
_CcMUInfoEncrMethod_Type = EncrType
_CcMUInfoEncrMethod_Object = MibTableColumn
ccMUInfoEncrMethod = _CcMUInfoEncrMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 26),
    _CcMUInfoEncrMethod_Type()
)
ccMUInfoEncrMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoEncrMethod.setStatus("current")
_CcMUInfoBCMCEncrType_Type = EncrType
_CcMUInfoBCMCEncrType_Object = MibTableColumn
ccMUInfoBCMCEncrType = _CcMUInfoBCMCEncrType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 27),
    _CcMUInfoBCMCEncrType_Type()
)
ccMUInfoBCMCEncrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoBCMCEncrType.setStatus("current")
_CcMUInfoRoamCount_Type = Integer32
_CcMUInfoRoamCount_Object = MibTableColumn
ccMUInfoRoamCount = _CcMUInfoRoamCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 32, 1, 28),
    _CcMUInfoRoamCount_Type()
)
ccMUInfoRoamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMUInfoRoamCount.setStatus("current")
_CcACLObjects_ObjectIdentity = ObjectIdentity
ccACLObjects = _CcACLObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 33)
)
_CcACLItemsTable_Object = MibTable
ccACLItemsTable = _CcACLItemsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 33, 2)
)
if mibBuilder.loadTexts:
    ccACLItemsTable.setStatus("current")
_CcACLItemsEntry_Object = MibTableRow
ccACLItemsEntry = _CcACLItemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 33, 2, 1)
)
ccACLItemsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccACLIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccACLItemIndex"),
)
if mibBuilder.loadTexts:
    ccACLItemsEntry.setStatus("current")


class _CcACLItemIndex_Type(Integer32):
    """Custom type ccACLItemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CcACLItemIndex_Type.__name__ = "Integer32"
_CcACLItemIndex_Object = MibTableColumn
ccACLItemIndex = _CcACLItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 33, 2, 1, 1),
    _CcACLItemIndex_Type()
)
ccACLItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccACLItemIndex.setStatus("current")


class _CcACLItem_Type(DisplayString):
    """Custom type ccACLItem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CcACLItem_Type.__name__ = "DisplayString"
_CcACLItem_Object = MibTableColumn
ccACLItem = _CcACLItem_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 33, 2, 1, 2),
    _CcACLItem_Type()
)
ccACLItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccACLItem.setStatus("current")
_CcWVPNConfigure_ObjectIdentity = ObjectIdentity
ccWVPNConfigure = _CcWVPNConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34)
)
_WvpnGeneralSettings_ObjectIdentity = ObjectIdentity
wvpnGeneralSettings = _WvpnGeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1)
)
_WvpnServerEnable_Type = DoActionNow
_WvpnServerEnable_Object = MibScalar
wvpnServerEnable = _WvpnServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 1),
    _WvpnServerEnable_Type()
)
wvpnServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnServerEnable.setStatus("current")
_WvpnServerDisable_Type = DoActionNow
_WvpnServerDisable_Object = MibScalar
wvpnServerDisable = _WvpnServerDisable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 2),
    _WvpnServerDisable_Type()
)
wvpnServerDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnServerDisable.setStatus("current")
_WvpnServerRestart_Type = DoActionNow
_WvpnServerRestart_Object = MibScalar
wvpnServerRestart = _WvpnServerRestart_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 3),
    _WvpnServerRestart_Type()
)
wvpnServerRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnServerRestart.setStatus("current")


class _WvpnIpAddress_Type(DisplayString):
    """Custom type wvpnIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_WvpnIpAddress_Type.__name__ = "DisplayString"
_WvpnIpAddress_Object = MibScalar
wvpnIpAddress = _WvpnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 4),
    _WvpnIpAddress_Type()
)
wvpnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnIpAddress.setStatus("current")


class _WvpnPort_Type(Integer32):
    """Custom type wvpnPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_WvpnPort_Type.__name__ = "Integer32"
_WvpnPort_Object = MibScalar
wvpnPort = _WvpnPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 5),
    _WvpnPort_Type()
)
wvpnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnPort.setStatus("current")
_WvpnUnusedTimeout_Type = Integer32
_WvpnUnusedTimeout_Object = MibScalar
wvpnUnusedTimeout = _WvpnUnusedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 6),
    _WvpnUnusedTimeout_Type()
)
wvpnUnusedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnUnusedTimeout.setStatus("current")


class _WvpnStatus_Type(DisplayString):
    """Custom type wvpnStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnStatus_Type.__name__ = "DisplayString"
_WvpnStatus_Object = MibScalar
wvpnStatus = _WvpnStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 7),
    _WvpnStatus_Type()
)
wvpnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnStatus.setStatus("current")
_DosEnable_Type = TruthValue
_DosEnable_Object = MibScalar
dosEnable = _DosEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 8),
    _DosEnable_Type()
)
dosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosEnable.setStatus("current")


class _DosPort_Type(Integer32):
    """Custom type dosPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_DosPort_Type.__name__ = "Integer32"
_DosPort_Object = MibScalar
dosPort = _DosPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 9),
    _DosPort_Type()
)
dosPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPort.setStatus("current")


class _ClientKeepAlive_Type(DisplayString):
    """Custom type clientKeepAlive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClientKeepAlive_Type.__name__ = "DisplayString"
_ClientKeepAlive_Object = MibScalar
clientKeepAlive = _ClientKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 10),
    _ClientKeepAlive_Type()
)
clientKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    clientKeepAlive.setUnits("seconds")


class _VpnLicenseMax_Type(Integer32):
    """Custom type vpnLicenseMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VpnLicenseMax_Type.__name__ = "Integer32"
_VpnLicenseMax_Object = MibScalar
vpnLicenseMax = _VpnLicenseMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 11),
    _VpnLicenseMax_Type()
)
vpnLicenseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnLicenseMax.setStatus("current")


class _VpnLicenseInUse_Type(Integer32):
    """Custom type vpnLicenseInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VpnLicenseInUse_Type.__name__ = "Integer32"
_VpnLicenseInUse_Object = MibScalar
vpnLicenseInUse = _VpnLicenseInUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 1, 12),
    _VpnLicenseInUse_Type()
)
vpnLicenseInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnLicenseInUse.setStatus("current")
_WvpnWtlsSettings_ObjectIdentity = ObjectIdentity
wvpnWtlsSettings = _WvpnWtlsSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2)
)


class _MaxClientRsaKeySize_Type(Integer32):
    """Custom type maxClientRsaKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 15360),
    )


_MaxClientRsaKeySize_Type.__name__ = "Integer32"
_MaxClientRsaKeySize_Object = MibScalar
maxClientRsaKeySize = _MaxClientRsaKeySize_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 1),
    _MaxClientRsaKeySize_Type()
)
maxClientRsaKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxClientRsaKeySize.setStatus("current")


class _MinClientRsaKeySize_Type(Integer32):
    """Custom type minClientRsaKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 15360),
    )


_MinClientRsaKeySize_Type.__name__ = "Integer32"
_MinClientRsaKeySize_Object = MibScalar
minClientRsaKeySize = _MinClientRsaKeySize_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 2),
    _MinClientRsaKeySize_Type()
)
minClientRsaKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minClientRsaKeySize.setStatus("current")


class _MaxRsaKeySize_Type(Integer32):
    """Custom type maxRsaKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 15360),
    )


_MaxRsaKeySize_Type.__name__ = "Integer32"
_MaxRsaKeySize_Object = MibScalar
maxRsaKeySize = _MaxRsaKeySize_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 3),
    _MaxRsaKeySize_Type()
)
maxRsaKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxRsaKeySize.setStatus("current")


class _MinRsaKeySize_Type(Integer32):
    """Custom type minRsaKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 15360),
    )


_MinRsaKeySize_Type.__name__ = "Integer32"
_MinRsaKeySize_Object = MibScalar
minRsaKeySize = _MinRsaKeySize_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 4),
    _MinRsaKeySize_Type()
)
minRsaKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minRsaKeySize.setStatus("current")


class _Cipher_Type(DisplayString):
    """Custom type cipher based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Cipher_Type.__name__ = "DisplayString"
_Cipher_Object = MibScalar
cipher = _Cipher_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 5),
    _Cipher_Type()
)
cipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipher.setStatus("current")


class _Mac_Type(DisplayString):
    """Custom type mac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Mac_Type.__name__ = "DisplayString"
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 6),
    _Mac_Type()
)
mac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac.setStatus("current")
_RequireClientCertificate_Type = TruthValue
_RequireClientCertificate_Object = MibScalar
requireClientCertificate = _RequireClientCertificate_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 7),
    _RequireClientCertificate_Type()
)
requireClientCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    requireClientCertificate.setStatus("current")


class _KeyRefresh_Type(Integer32):
    """Custom type keyRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_KeyRefresh_Type.__name__ = "Integer32"
_KeyRefresh_Object = MibScalar
keyRefresh = _KeyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 8),
    _KeyRefresh_Type()
)
keyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyRefresh.setStatus("current")


class _WantedFipsMode_Type(DisplayString):
    """Custom type wantedFipsMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WantedFipsMode_Type.__name__ = "DisplayString"
_WantedFipsMode_Object = MibScalar
wantedFipsMode = _WantedFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 9),
    _WantedFipsMode_Type()
)
wantedFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wantedFipsMode.setStatus("current")


class _SecurityMode_Type(DisplayString):
    """Custom type securityMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SecurityMode_Type.__name__ = "DisplayString"
_SecurityMode_Object = MibScalar
securityMode = _SecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 10),
    _SecurityMode_Type()
)
securityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMode.setStatus("current")


class _ServerNumber_Type(Integer32):
    """Custom type serverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ServerNumber_Type.__name__ = "Integer32"
_ServerNumber_Object = MibScalar
serverNumber = _ServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 11),
    _ServerNumber_Type()
)
serverNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverNumber.setStatus("current")


class _HandshakeTimeout_Type(DisplayString):
    """Custom type handshakeTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HandshakeTimeout_Type.__name__ = "DisplayString"
_HandshakeTimeout_Object = MibScalar
handshakeTimeout = _HandshakeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 12),
    _HandshakeTimeout_Type()
)
handshakeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    handshakeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    handshakeTimeout.setUnits("seconds")
_AllowSessionResume_Type = TruthValue
_AllowSessionResume_Object = MibScalar
allowSessionResume = _AllowSessionResume_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 2, 13),
    _AllowSessionResume_Type()
)
allowSessionResume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowSessionResume.setStatus("current")
_WvpnAuthServerSettings_ObjectIdentity = ObjectIdentity
wvpnAuthServerSettings = _WvpnAuthServerSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3)
)
_UseSimpleAuthentication_Type = TruthValue
_UseSimpleAuthentication_Object = MibScalar
useSimpleAuthentication = _UseSimpleAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 1),
    _UseSimpleAuthentication_Type()
)
useSimpleAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useSimpleAuthentication.setStatus("current")
_UseRadiusAuthentication_Type = TruthValue
_UseRadiusAuthentication_Object = MibScalar
useRadiusAuthentication = _UseRadiusAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 2),
    _UseRadiusAuthentication_Type()
)
useRadiusAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useRadiusAuthentication.setStatus("current")
_UseLdapAuthentication_Type = TruthValue
_UseLdapAuthentication_Object = MibScalar
useLdapAuthentication = _UseLdapAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 3),
    _UseLdapAuthentication_Type()
)
useLdapAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useLdapAuthentication.setStatus("current")
_UseLocalDatabaseAuthentication_Type = TruthValue
_UseLocalDatabaseAuthentication_Object = MibScalar
useLocalDatabaseAuthentication = _UseLocalDatabaseAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 4),
    _UseLocalDatabaseAuthentication_Type()
)
useLocalDatabaseAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useLocalDatabaseAuthentication.setStatus("current")
_SimpleAuthentication_ObjectIdentity = ObjectIdentity
simpleAuthentication = _SimpleAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 5)
)


class _SimpleAuthUserName_Type(DisplayString):
    """Custom type simpleAuthUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_SimpleAuthUserName_Type.__name__ = "DisplayString"
_SimpleAuthUserName_Object = MibScalar
simpleAuthUserName = _SimpleAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 5, 1),
    _SimpleAuthUserName_Type()
)
simpleAuthUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    simpleAuthUserName.setStatus("current")


class _SimpleAuthPassword_Type(DisplayString):
    """Custom type simpleAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_SimpleAuthPassword_Type.__name__ = "DisplayString"
_SimpleAuthPassword_Object = MibScalar
simpleAuthPassword = _SimpleAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 5, 2),
    _SimpleAuthPassword_Type()
)
simpleAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    simpleAuthPassword.setStatus("current")


class _SimpleAuthDomain_Type(DisplayString):
    """Custom type simpleAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_SimpleAuthDomain_Type.__name__ = "DisplayString"
_SimpleAuthDomain_Object = MibScalar
simpleAuthDomain = _SimpleAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 5, 3),
    _SimpleAuthDomain_Type()
)
simpleAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    simpleAuthDomain.setStatus("current")
_WvpnRadiusAuthentication_ObjectIdentity = ObjectIdentity
wvpnRadiusAuthentication = _WvpnRadiusAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6)
)
_RadiusAuthPrimaryServer_ObjectIdentity = ObjectIdentity
radiusAuthPrimaryServer = _RadiusAuthPrimaryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1)
)


class _RadiusAuthPrimaryHost_Type(DisplayString):
    """Custom type radiusAuthPrimaryHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RadiusAuthPrimaryHost_Type.__name__ = "DisplayString"
_RadiusAuthPrimaryHost_Object = MibScalar
radiusAuthPrimaryHost = _RadiusAuthPrimaryHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1, 1),
    _RadiusAuthPrimaryHost_Type()
)
radiusAuthPrimaryHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryHost.setStatus("current")


class _RadiusAuthPrimaryPort_Type(Integer32):
    """Custom type radiusAuthPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAuthPrimaryPort_Type.__name__ = "Integer32"
_RadiusAuthPrimaryPort_Object = MibScalar
radiusAuthPrimaryPort = _RadiusAuthPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1, 2),
    _RadiusAuthPrimaryPort_Type()
)
radiusAuthPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryPort.setStatus("current")


class _RadiusAuthPrimaryMaxRetries_Type(Integer32):
    """Custom type radiusAuthPrimaryMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadiusAuthPrimaryMaxRetries_Type.__name__ = "Integer32"
_RadiusAuthPrimaryMaxRetries_Object = MibScalar
radiusAuthPrimaryMaxRetries = _RadiusAuthPrimaryMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1, 3),
    _RadiusAuthPrimaryMaxRetries_Type()
)
radiusAuthPrimaryMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryMaxRetries.setStatus("current")


class _RadiusAuthPrimaryTimeOut_Type(Integer32):
    """Custom type radiusAuthPrimaryTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_RadiusAuthPrimaryTimeOut_Type.__name__ = "Integer32"
_RadiusAuthPrimaryTimeOut_Object = MibScalar
radiusAuthPrimaryTimeOut = _RadiusAuthPrimaryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1, 4),
    _RadiusAuthPrimaryTimeOut_Type()
)
radiusAuthPrimaryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryTimeOut.setStatus("current")


class _RadiusAuthPrimaryUserPassword_Type(DisplayString):
    """Custom type radiusAuthPrimaryUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RadiusAuthPrimaryUserPassword_Type.__name__ = "DisplayString"
_RadiusAuthPrimaryUserPassword_Object = MibScalar
radiusAuthPrimaryUserPassword = _RadiusAuthPrimaryUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1, 5),
    _RadiusAuthPrimaryUserPassword_Type()
)
radiusAuthPrimaryUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryUserPassword.setStatus("current")


class _RadiusAuthPrimarySecret_Type(DisplayString):
    """Custom type radiusAuthPrimarySecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RadiusAuthPrimarySecret_Type.__name__ = "DisplayString"
_RadiusAuthPrimarySecret_Object = MibScalar
radiusAuthPrimarySecret = _RadiusAuthPrimarySecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 1, 6),
    _RadiusAuthPrimarySecret_Type()
)
radiusAuthPrimarySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimarySecret.setStatus("current")
_RadiusAuthSecondaryServer_ObjectIdentity = ObjectIdentity
radiusAuthSecondaryServer = _RadiusAuthSecondaryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2)
)


class _RadiusAuthSecondaryHost_Type(DisplayString):
    """Custom type radiusAuthSecondaryHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_RadiusAuthSecondaryHost_Type.__name__ = "DisplayString"
_RadiusAuthSecondaryHost_Object = MibScalar
radiusAuthSecondaryHost = _RadiusAuthSecondaryHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2, 1),
    _RadiusAuthSecondaryHost_Type()
)
radiusAuthSecondaryHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryHost.setStatus("current")


class _RadiusAuthSecondaryPort_Type(Integer32):
    """Custom type radiusAuthSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAuthSecondaryPort_Type.__name__ = "Integer32"
_RadiusAuthSecondaryPort_Object = MibScalar
radiusAuthSecondaryPort = _RadiusAuthSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2, 2),
    _RadiusAuthSecondaryPort_Type()
)
radiusAuthSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryPort.setStatus("current")


class _RadiusAuthSecondaryMaxRetries_Type(Integer32):
    """Custom type radiusAuthSecondaryMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadiusAuthSecondaryMaxRetries_Type.__name__ = "Integer32"
_RadiusAuthSecondaryMaxRetries_Object = MibScalar
radiusAuthSecondaryMaxRetries = _RadiusAuthSecondaryMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2, 3),
    _RadiusAuthSecondaryMaxRetries_Type()
)
radiusAuthSecondaryMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryMaxRetries.setStatus("current")


class _RadiusAuthSecondaryTimeOut_Type(Integer32):
    """Custom type radiusAuthSecondaryTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_RadiusAuthSecondaryTimeOut_Type.__name__ = "Integer32"
_RadiusAuthSecondaryTimeOut_Object = MibScalar
radiusAuthSecondaryTimeOut = _RadiusAuthSecondaryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2, 4),
    _RadiusAuthSecondaryTimeOut_Type()
)
radiusAuthSecondaryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryTimeOut.setStatus("current")


class _RadiusAuthSecondaryUserPassword_Type(DisplayString):
    """Custom type radiusAuthSecondaryUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RadiusAuthSecondaryUserPassword_Type.__name__ = "DisplayString"
_RadiusAuthSecondaryUserPassword_Object = MibScalar
radiusAuthSecondaryUserPassword = _RadiusAuthSecondaryUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2, 5),
    _RadiusAuthSecondaryUserPassword_Type()
)
radiusAuthSecondaryUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryUserPassword.setStatus("current")


class _RadiusAuthSecondarySecret_Type(DisplayString):
    """Custom type radiusAuthSecondarySecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RadiusAuthSecondarySecret_Type.__name__ = "DisplayString"
_RadiusAuthSecondarySecret_Object = MibScalar
radiusAuthSecondarySecret = _RadiusAuthSecondarySecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 3, 6, 2, 6),
    _RadiusAuthSecondarySecret_Type()
)
radiusAuthSecondarySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondarySecret.setStatus("current")
_WvpnIpPoolsSettings_ObjectIdentity = ObjectIdentity
wvpnIpPoolsSettings = _WvpnIpPoolsSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4)
)


class _WvpnAddIpPoolObj_Type(DisplayString):
    """Custom type wvpnAddIpPoolObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_WvpnAddIpPoolObj_Type.__name__ = "DisplayString"
_WvpnAddIpPoolObj_Object = MibScalar
wvpnAddIpPoolObj = _WvpnAddIpPoolObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 1),
    _WvpnAddIpPoolObj_Type()
)
wvpnAddIpPoolObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnAddIpPoolObj.setStatus("current")


class _WvpnRemIpPoolObj_Type(DisplayString):
    """Custom type wvpnRemIpPoolObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnRemIpPoolObj_Type.__name__ = "DisplayString"
_WvpnRemIpPoolObj_Object = MibScalar
wvpnRemIpPoolObj = _WvpnRemIpPoolObj_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 2),
    _WvpnRemIpPoolObj_Type()
)
wvpnRemIpPoolObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnRemIpPoolObj.setStatus("current")


class _WvpnAddIpPoolRange_Type(DisplayString):
    """Custom type wvpnAddIpPoolRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_WvpnAddIpPoolRange_Type.__name__ = "DisplayString"
_WvpnAddIpPoolRange_Object = MibScalar
wvpnAddIpPoolRange = _WvpnAddIpPoolRange_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 3),
    _WvpnAddIpPoolRange_Type()
)
wvpnAddIpPoolRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnAddIpPoolRange.setStatus("current")


class _WvpnRemIpPoolRange_Type(DisplayString):
    """Custom type wvpnRemIpPoolRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnRemIpPoolRange_Type.__name__ = "DisplayString"
_WvpnRemIpPoolRange_Object = MibScalar
wvpnRemIpPoolRange = _WvpnRemIpPoolRange_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 4),
    _WvpnRemIpPoolRange_Type()
)
wvpnRemIpPoolRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnRemIpPoolRange.setStatus("current")
_UseDhcpGateway_Type = TruthValue
_UseDhcpGateway_Object = MibScalar
useDhcpGateway = _UseDhcpGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 5),
    _UseDhcpGateway_Type()
)
useDhcpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDhcpGateway.setStatus("current")
_WvpnIpPoolsTable_Object = MibTable
wvpnIpPoolsTable = _WvpnIpPoolsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6)
)
if mibBuilder.loadTexts:
    wvpnIpPoolsTable.setStatus("current")
_WvpnIpPoolsEntry_Object = MibTableRow
wvpnIpPoolsEntry = _WvpnIpPoolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1)
)
wvpnIpPoolsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "wvpnIpPoolIndex"),
)
if mibBuilder.loadTexts:
    wvpnIpPoolsEntry.setStatus("current")


class _WvpnIpPoolIndex_Type(Integer32):
    """Custom type wvpnIpPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WvpnIpPoolIndex_Type.__name__ = "Integer32"
_WvpnIpPoolIndex_Object = MibTableColumn
wvpnIpPoolIndex = _WvpnIpPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 1),
    _WvpnIpPoolIndex_Type()
)
wvpnIpPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnIpPoolIndex.setStatus("current")


class _ClientIpPoolName_Type(DisplayString):
    """Custom type clientIpPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClientIpPoolName_Type.__name__ = "DisplayString"
_ClientIpPoolName_Object = MibTableColumn
clientIpPoolName = _ClientIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 2),
    _ClientIpPoolName_Type()
)
clientIpPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIpPoolName.setStatus("current")
_ClientNetMask_Type = IpAddress
_ClientNetMask_Object = MibTableColumn
clientNetMask = _ClientNetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 3),
    _ClientNetMask_Type()
)
clientNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientNetMask.setStatus("current")
_ClientDhcpServerAddress_Type = IpAddress
_ClientDhcpServerAddress_Object = MibTableColumn
clientDhcpServerAddress = _ClientDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 4),
    _ClientDhcpServerAddress_Type()
)
clientDhcpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDhcpServerAddress.setStatus("current")
_ClientDefaultGatewayAddress_Type = IpAddress
_ClientDefaultGatewayAddress_Object = MibTableColumn
clientDefaultGatewayAddress = _ClientDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 5),
    _ClientDefaultGatewayAddress_Type()
)
clientDefaultGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDefaultGatewayAddress.setStatus("current")
_ClientDnsAddress_Type = IpAddress
_ClientDnsAddress_Object = MibTableColumn
clientDnsAddress = _ClientDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 6),
    _ClientDnsAddress_Type()
)
clientDnsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDnsAddress.setStatus("current")
_ClientWinsAddress_Type = IpAddress
_ClientWinsAddress_Object = MibTableColumn
clientWinsAddress = _ClientWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 7),
    _ClientWinsAddress_Type()
)
clientWinsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientWinsAddress.setStatus("current")


class _ClientDomainName_Type(DisplayString):
    """Custom type clientDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ClientDomainName_Type.__name__ = "DisplayString"
_ClientDomainName_Object = MibTableColumn
clientDomainName = _ClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 8),
    _ClientDomainName_Type()
)
clientDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDomainName.setStatus("current")


class _ClientNetBiosNodeType_Type(DisplayString):
    """Custom type clientNetBiosNodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClientNetBiosNodeType_Type.__name__ = "DisplayString"
_ClientNetBiosNodeType_Object = MibTableColumn
clientNetBiosNodeType = _ClientNetBiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 9),
    _ClientNetBiosNodeType_Type()
)
clientNetBiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientNetBiosNodeType.setStatus("current")


class _ClientDhcpLeaseTime_Type(DisplayString):
    """Custom type clientDhcpLeaseTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClientDhcpLeaseTime_Type.__name__ = "DisplayString"
_ClientDhcpLeaseTime_Object = MibTableColumn
clientDhcpLeaseTime = _ClientDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 10),
    _ClientDhcpLeaseTime_Type()
)
clientDhcpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientDhcpLeaseTime.setStatus("current")


class _ReuseAddrTime_Type(Integer32):
    """Custom type reuseAddrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ReuseAddrTime_Type.__name__ = "Integer32"
_ReuseAddrTime_Object = MibTableColumn
reuseAddrTime = _ReuseAddrTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 11),
    _ReuseAddrTime_Type()
)
reuseAddrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reuseAddrTime.setStatus("current")
if mibBuilder.loadTexts:
    reuseAddrTime.setUnits("seconds")
_IpRangeCount_Type = Integer32
_IpRangeCount_Object = MibTableColumn
ipRangeCount = _IpRangeCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 12),
    _IpRangeCount_Type()
)
ipRangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRangeCount.setStatus("current")


class _ClientIpRanges_Type(DisplayString):
    """Custom type clientIpRanges based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_ClientIpRanges_Type.__name__ = "DisplayString"
_ClientIpRanges_Object = MibTableColumn
clientIpRanges = _ClientIpRanges_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 6, 1, 13),
    _ClientIpRanges_Type()
)
clientIpRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIpRanges.setStatus("current")
_WvpnIpPoolsCount_Type = Integer32
_WvpnIpPoolsCount_Object = MibScalar
wvpnIpPoolsCount = _WvpnIpPoolsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 7),
    _WvpnIpPoolsCount_Type()
)
wvpnIpPoolsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnIpPoolsCount.setStatus("current")


class _WvpnIpPoolsNames_Type(DisplayString):
    """Custom type wvpnIpPoolsNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_WvpnIpPoolsNames_Type.__name__ = "DisplayString"
_WvpnIpPoolsNames_Object = MibScalar
wvpnIpPoolsNames = _WvpnIpPoolsNames_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 4, 8),
    _WvpnIpPoolsNames_Type()
)
wvpnIpPoolsNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnIpPoolsNames.setStatus("current")
_WvpnCertificateSettings_ObjectIdentity = ObjectIdentity
wvpnCertificateSettings = _WvpnCertificateSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5)
)
_WvpnServerCertificateTable_Object = MibTable
wvpnServerCertificateTable = _WvpnServerCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1)
)
if mibBuilder.loadTexts:
    wvpnServerCertificateTable.setStatus("current")
_WvpnServerCertificateEntry_Object = MibTableRow
wvpnServerCertificateEntry = _WvpnServerCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1)
)
wvpnServerCertificateEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "wvpnCertIndex"),
)
if mibBuilder.loadTexts:
    wvpnServerCertificateEntry.setStatus("current")


class _WvpnCertIndex_Type(Integer32):
    """Custom type wvpnCertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WvpnCertIndex_Type.__name__ = "Integer32"
_WvpnCertIndex_Object = MibTableColumn
wvpnCertIndex = _WvpnCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 1),
    _WvpnCertIndex_Type()
)
wvpnCertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCertIndex.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 3),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _Subject_Type(DisplayString):
    """Custom type subject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Subject_Type.__name__ = "DisplayString"
_Subject_Object = MibTableColumn
subject = _Subject_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 4),
    _Subject_Type()
)
subject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subject.setStatus("current")


class _Version_Type(Integer32):
    """Custom type version based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Version_Type.__name__ = "Integer32"
_Version_Object = MibTableColumn
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 5),
    _Version_Type()
)
version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    version.setStatus("current")


class _Issuer_Type(DisplayString):
    """Custom type issuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Issuer_Type.__name__ = "DisplayString"
_Issuer_Object = MibTableColumn
issuer = _Issuer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 6),
    _Issuer_Type()
)
issuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issuer.setStatus("current")


class _KeyLength_Type(Integer32):
    """Custom type keyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_KeyLength_Type.__name__ = "Integer32"
_KeyLength_Object = MibTableColumn
keyLength = _KeyLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 7),
    _KeyLength_Type()
)
keyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyLength.setStatus("current")


class _ValidFrom_Type(DisplayString):
    """Custom type validFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ValidFrom_Type.__name__ = "DisplayString"
_ValidFrom_Object = MibTableColumn
validFrom = _ValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 8),
    _ValidFrom_Type()
)
validFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    validFrom.setStatus("current")


class _ValidTo_Type(DisplayString):
    """Custom type validTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ValidTo_Type.__name__ = "DisplayString"
_ValidTo_Object = MibTableColumn
validTo = _ValidTo_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 9),
    _ValidTo_Type()
)
validTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    validTo.setStatus("current")


class _Certificate_Type(DisplayString):
    """Custom type certificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_Certificate_Type.__name__ = "DisplayString"
_Certificate_Object = MibTableColumn
certificate = _Certificate_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 10),
    _Certificate_Type()
)
certificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificate.setStatus("current")


class _Binary_Type(DisplayString):
    """Custom type binary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_Binary_Type.__name__ = "DisplayString"
_Binary_Object = MibTableColumn
binary = _Binary_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 11),
    _Binary_Type()
)
binary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binary.setStatus("current")


class _FingerPrint_Type(DisplayString):
    """Custom type fingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_FingerPrint_Type.__name__ = "DisplayString"
_FingerPrint_Object = MibTableColumn
fingerPrint = _FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 12),
    _FingerPrint_Type()
)
fingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fingerPrint.setStatus("current")


class _AuthFingerPrint_Type(DisplayString):
    """Custom type authFingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_AuthFingerPrint_Type.__name__ = "DisplayString"
_AuthFingerPrint_Object = MibTableColumn
authFingerPrint = _AuthFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 1, 1, 13),
    _AuthFingerPrint_Type()
)
authFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authFingerPrint.setStatus("current")


class _ServerCertCount_Type(Integer32):
    """Custom type serverCertCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ServerCertCount_Type.__name__ = "Integer32"
_ServerCertCount_Object = MibScalar
serverCertCount = _ServerCertCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 2),
    _ServerCertCount_Type()
)
serverCertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCertCount.setStatus("current")


class _ServerCertUserNames_Type(DisplayString):
    """Custom type serverCertUserNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ServerCertUserNames_Type.__name__ = "DisplayString"
_ServerCertUserNames_Object = MibScalar
serverCertUserNames = _ServerCertUserNames_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 3),
    _ServerCertUserNames_Type()
)
serverCertUserNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCertUserNames.setStatus("current")
_WvpnCaCertificateTable_Object = MibTable
wvpnCaCertificateTable = _WvpnCaCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4)
)
if mibBuilder.loadTexts:
    wvpnCaCertificateTable.setStatus("current")
_WvpnCaCertificateEntry_Object = MibTableRow
wvpnCaCertificateEntry = _WvpnCaCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1)
)
wvpnCaCertificateEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "wvpnCaCertIndex"),
)
if mibBuilder.loadTexts:
    wvpnCaCertificateEntry.setStatus("current")


class _WvpnCaCertIndex_Type(Integer32):
    """Custom type wvpnCaCertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WvpnCaCertIndex_Type.__name__ = "Integer32"
_WvpnCaCertIndex_Object = MibTableColumn
wvpnCaCertIndex = _WvpnCaCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 1),
    _WvpnCaCertIndex_Type()
)
wvpnCaCertIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnCaCertIndex.setStatus("current")


class _WvpnCaSerialNumber_Type(DisplayString):
    """Custom type wvpnCaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnCaSerialNumber_Type.__name__ = "DisplayString"
_WvpnCaSerialNumber_Object = MibTableColumn
wvpnCaSerialNumber = _WvpnCaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 2),
    _WvpnCaSerialNumber_Type()
)
wvpnCaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaSerialNumber.setStatus("current")


class _WvpnCaSubject_Type(DisplayString):
    """Custom type wvpnCaSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnCaSubject_Type.__name__ = "DisplayString"
_WvpnCaSubject_Object = MibTableColumn
wvpnCaSubject = _WvpnCaSubject_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 3),
    _WvpnCaSubject_Type()
)
wvpnCaSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaSubject.setStatus("current")


class _WvpnCaVersion_Type(Integer32):
    """Custom type wvpnCaVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WvpnCaVersion_Type.__name__ = "Integer32"
_WvpnCaVersion_Object = MibTableColumn
wvpnCaVersion = _WvpnCaVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 4),
    _WvpnCaVersion_Type()
)
wvpnCaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaVersion.setStatus("current")


class _WvpnCaIssuer_Type(DisplayString):
    """Custom type wvpnCaIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnCaIssuer_Type.__name__ = "DisplayString"
_WvpnCaIssuer_Object = MibTableColumn
wvpnCaIssuer = _WvpnCaIssuer_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 5),
    _WvpnCaIssuer_Type()
)
wvpnCaIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaIssuer.setStatus("current")


class _WvpnCaKeyLength_Type(DisplayString):
    """Custom type wvpnCaKeyLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnCaKeyLength_Type.__name__ = "DisplayString"
_WvpnCaKeyLength_Object = MibTableColumn
wvpnCaKeyLength = _WvpnCaKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 6),
    _WvpnCaKeyLength_Type()
)
wvpnCaKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaKeyLength.setStatus("current")


class _WvpnCaValidFrom_Type(DisplayString):
    """Custom type wvpnCaValidFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnCaValidFrom_Type.__name__ = "DisplayString"
_WvpnCaValidFrom_Object = MibTableColumn
wvpnCaValidFrom = _WvpnCaValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 7),
    _WvpnCaValidFrom_Type()
)
wvpnCaValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaValidFrom.setStatus("current")


class _WvpnCaValidTo_Type(DisplayString):
    """Custom type wvpnCaValidTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnCaValidTo_Type.__name__ = "DisplayString"
_WvpnCaValidTo_Object = MibTableColumn
wvpnCaValidTo = _WvpnCaValidTo_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 8),
    _WvpnCaValidTo_Type()
)
wvpnCaValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaValidTo.setStatus("current")


class _WvpnCaBinary_Type(DisplayString):
    """Custom type wvpnCaBinary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_WvpnCaBinary_Type.__name__ = "DisplayString"
_WvpnCaBinary_Object = MibTableColumn
wvpnCaBinary = _WvpnCaBinary_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 9),
    _WvpnCaBinary_Type()
)
wvpnCaBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaBinary.setStatus("current")


class _WvpnCaFingerPrint_Type(DisplayString):
    """Custom type wvpnCaFingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_WvpnCaFingerPrint_Type.__name__ = "DisplayString"
_WvpnCaFingerPrint_Object = MibTableColumn
wvpnCaFingerPrint = _WvpnCaFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 10),
    _WvpnCaFingerPrint_Type()
)
wvpnCaFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaFingerPrint.setStatus("current")


class _WvpnCaAuthFingerPrint_Type(DisplayString):
    """Custom type wvpnCaAuthFingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_WvpnCaAuthFingerPrint_Type.__name__ = "DisplayString"
_WvpnCaAuthFingerPrint_Object = MibTableColumn
wvpnCaAuthFingerPrint = _WvpnCaAuthFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 4, 1, 11),
    _WvpnCaAuthFingerPrint_Type()
)
wvpnCaAuthFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnCaAuthFingerPrint.setStatus("current")


class _CaCertCount_Type(Integer32):
    """Custom type caCertCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CaCertCount_Type.__name__ = "Integer32"
_CaCertCount_Object = MibScalar
caCertCount = _CaCertCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 5),
    _CaCertCount_Type()
)
caCertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caCertCount.setStatus("current")


class _CertSerialNumbers_Type(DisplayString):
    """Custom type certSerialNumbers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_CertSerialNumbers_Type.__name__ = "DisplayString"
_CertSerialNumbers_Object = MibScalar
certSerialNumbers = _CertSerialNumbers_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 6),
    _CertSerialNumbers_Type()
)
certSerialNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSerialNumbers.setStatus("current")


class _ImportServerCert_Type(DisplayString):
    """Custom type importServerCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_ImportServerCert_Type.__name__ = "DisplayString"
_ImportServerCert_Object = MibScalar
importServerCert = _ImportServerCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 7),
    _ImportServerCert_Type()
)
importServerCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importServerCert.setStatus("current")


class _RemoveServerCert_Type(DisplayString):
    """Custom type removeServerCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RemoveServerCert_Type.__name__ = "DisplayString"
_RemoveServerCert_Object = MibScalar
removeServerCert = _RemoveServerCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 8),
    _RemoveServerCert_Type()
)
removeServerCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removeServerCert.setStatus("current")


class _ImportCaCert_Type(DisplayString):
    """Custom type importCaCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ImportCaCert_Type.__name__ = "DisplayString"
_ImportCaCert_Object = MibScalar
importCaCert = _ImportCaCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 9),
    _ImportCaCert_Type()
)
importCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importCaCert.setStatus("current")


class _RemoveCaCert_Type(Integer32):
    """Custom type removeCaCert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RemoveCaCert_Type.__name__ = "Integer32"
_RemoveCaCert_Object = MibScalar
removeCaCert = _RemoveCaCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 10),
    _RemoveCaCert_Type()
)
removeCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removeCaCert.setStatus("current")


class _ImportTftpServerCert_Type(DisplayString):
    """Custom type importTftpServerCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_ImportTftpServerCert_Type.__name__ = "DisplayString"
_ImportTftpServerCert_Object = MibScalar
importTftpServerCert = _ImportTftpServerCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 11),
    _ImportTftpServerCert_Type()
)
importTftpServerCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importTftpServerCert.setStatus("current")


class _ImportTftpCaCert_Type(DisplayString):
    """Custom type importTftpCaCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )


_ImportTftpCaCert_Type.__name__ = "DisplayString"
_ImportTftpCaCert_Object = MibScalar
importTftpCaCert = _ImportTftpCaCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 12),
    _ImportTftpCaCert_Type()
)
importTftpCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importTftpCaCert.setStatus("current")


class _DirCert_Type(DisplayString):
    """Custom type dirCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1000),
    )


_DirCert_Type.__name__ = "DisplayString"
_DirCert_Object = MibScalar
dirCert = _DirCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 13),
    _DirCert_Type()
)
dirCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirCert.setStatus("current")


class _DumpCert_Type(DisplayString):
    """Custom type dumpCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_DumpCert_Type.__name__ = "DisplayString"
_DumpCert_Object = MibScalar
dumpCert = _DumpCert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 5, 14),
    _DumpCert_Type()
)
dumpCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpCert.setStatus("current")
_WvpnDDNSSettings_ObjectIdentity = ObjectIdentity
wvpnDDNSSettings = _WvpnDDNSSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6)
)
_ClearClientDNS_Type = DoActionNow
_ClearClientDNS_Object = MibScalar
clearClientDNS = _ClearClientDNS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 1),
    _ClearClientDNS_Type()
)
clearClientDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearClientDNS.setStatus("current")
_UpdateClientDNS_Type = DoActionNow
_UpdateClientDNS_Object = MibScalar
updateClientDNS = _UpdateClientDNS_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 2),
    _UpdateClientDNS_Type()
)
updateClientDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateClientDNS.setStatus("current")
_AddDNSAddr_Type = IpAddress
_AddDNSAddr_Object = MibScalar
addDNSAddr = _AddDNSAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 3),
    _AddDNSAddr_Type()
)
addDNSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addDNSAddr.setStatus("current")
_DeleteDNSAddr_Type = IpAddress
_DeleteDNSAddr_Object = MibScalar
deleteDNSAddr = _DeleteDNSAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 4),
    _DeleteDNSAddr_Type()
)
deleteDNSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deleteDNSAddr.setStatus("current")
_Enable_Type = TruthValue
_Enable_Object = MibScalar
enable = _Enable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 5),
    _Enable_Type()
)
enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable.setStatus("current")


class _Ttl_Type(Integer32):
    """Custom type ttl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ttl_Type.__name__ = "Integer32"
_Ttl_Object = MibScalar
ttl = _Ttl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 6),
    _Ttl_Type()
)
ttl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ttl.setStatus("current")


class _ForwardZone_Type(DisplayString):
    """Custom type forwardZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ForwardZone_Type.__name__ = "DisplayString"
_ForwardZone_Object = MibScalar
forwardZone = _ForwardZone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 7),
    _ForwardZone_Type()
)
forwardZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardZone.setStatus("current")


class _ReverseZone_Type(DisplayString):
    """Custom type reverseZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ReverseZone_Type.__name__ = "DisplayString"
_ReverseZone_Object = MibScalar
reverseZone = _ReverseZone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 8),
    _ReverseZone_Type()
)
reverseZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseZone.setStatus("current")


class _ClientNameString_Type(DisplayString):
    """Custom type clientNameString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ClientNameString_Type.__name__ = "DisplayString"
_ClientNameString_Object = MibScalar
clientNameString = _ClientNameString_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 9),
    _ClientNameString_Type()
)
clientNameString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientNameString.setStatus("current")
_WvpnDDNSAddressTable_Object = MibTable
wvpnDDNSAddressTable = _WvpnDDNSAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 10)
)
if mibBuilder.loadTexts:
    wvpnDDNSAddressTable.setStatus("current")
_WvpnDDNSAddressEntry_Object = MibTableRow
wvpnDDNSAddressEntry = _WvpnDDNSAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 10, 1)
)
wvpnDDNSAddressEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "wvpnDDNSAddressIndex"),
)
if mibBuilder.loadTexts:
    wvpnDDNSAddressEntry.setStatus("current")


class _WvpnDDNSAddressIndex_Type(Integer32):
    """Custom type wvpnDDNSAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WvpnDDNSAddressIndex_Type.__name__ = "Integer32"
_WvpnDDNSAddressIndex_Object = MibTableColumn
wvpnDDNSAddressIndex = _WvpnDDNSAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 10, 1, 1),
    _WvpnDDNSAddressIndex_Type()
)
wvpnDDNSAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnDDNSAddressIndex.setStatus("current")
_WvpnDDNSipAddress_Type = IpAddress
_WvpnDDNSipAddress_Object = MibTableColumn
wvpnDDNSipAddress = _WvpnDDNSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 10, 1, 2),
    _WvpnDDNSipAddress_Type()
)
wvpnDDNSipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnDDNSipAddress.setStatus("current")


class _CleanupTimeout_Type(Integer32):
    """Custom type cleanupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CleanupTimeout_Type.__name__ = "Integer32"
_CleanupTimeout_Object = MibScalar
cleanupTimeout = _CleanupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 11),
    _CleanupTimeout_Type()
)
cleanupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cleanupTimeout.setStatus("current")


class _ReverseZoneList_Type(DisplayString):
    """Custom type reverseZoneList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ReverseZoneList_Type.__name__ = "DisplayString"
_ReverseZoneList_Object = MibScalar
reverseZoneList = _ReverseZoneList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 12),
    _ReverseZoneList_Type()
)
reverseZoneList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reverseZoneList.setStatus("current")


class _ReverseZoneAdd_Type(DisplayString):
    """Custom type reverseZoneAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ReverseZoneAdd_Type.__name__ = "DisplayString"
_ReverseZoneAdd_Object = MibScalar
reverseZoneAdd = _ReverseZoneAdd_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 13),
    _ReverseZoneAdd_Type()
)
reverseZoneAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseZoneAdd.setStatus("current")


class _ReverseZoneDel_Type(DisplayString):
    """Custom type reverseZoneDel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ReverseZoneDel_Type.__name__ = "DisplayString"
_ReverseZoneDel_Object = MibScalar
reverseZoneDel = _ReverseZoneDel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 6, 14),
    _ReverseZoneDel_Type()
)
reverseZoneDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseZoneDel.setStatus("current")
_WvpnRuntimeStats_ObjectIdentity = ObjectIdentity
wvpnRuntimeStats = _WvpnRuntimeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7)
)
_WvpnSessionTable_Object = MibTable
wvpnSessionTable = _WvpnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1)
)
if mibBuilder.loadTexts:
    wvpnSessionTable.setStatus("current")
_WvpnSessionEntry_Object = MibTableRow
wvpnSessionEntry = _WvpnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1)
)
wvpnSessionEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "wvpnSessionIndex"),
)
if mibBuilder.loadTexts:
    wvpnSessionEntry.setStatus("current")


class _WvpnSessionIndex_Type(Integer32):
    """Custom type wvpnSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WvpnSessionIndex_Type.__name__ = "Integer32"
_WvpnSessionIndex_Object = MibTableColumn
wvpnSessionIndex = _WvpnSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 1),
    _WvpnSessionIndex_Type()
)
wvpnSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnSessionIndex.setStatus("current")


class _WvpnSessionId_Type(DisplayString):
    """Custom type wvpnSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnSessionId_Type.__name__ = "DisplayString"
_WvpnSessionId_Object = MibTableColumn
wvpnSessionId = _WvpnSessionId_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 2),
    _WvpnSessionId_Type()
)
wvpnSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnSessionId.setStatus("current")


class _WvpnVpnIp_Type(DisplayString):
    """Custom type wvpnVpnIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnVpnIp_Type.__name__ = "DisplayString"
_WvpnVpnIp_Object = MibTableColumn
wvpnVpnIp = _WvpnVpnIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 3),
    _WvpnVpnIp_Type()
)
wvpnVpnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnVpnIp.setStatus("current")


class _WvpnRealIp_Type(DisplayString):
    """Custom type wvpnRealIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnRealIp_Type.__name__ = "DisplayString"
_WvpnRealIp_Object = MibTableColumn
wvpnRealIp = _WvpnRealIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 4),
    _WvpnRealIp_Type()
)
wvpnRealIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnRealIp.setStatus("current")


class _WvpnLoginTime_Type(DisplayString):
    """Custom type wvpnLoginTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnLoginTime_Type.__name__ = "DisplayString"
_WvpnLoginTime_Object = MibTableColumn
wvpnLoginTime = _WvpnLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 5),
    _WvpnLoginTime_Type()
)
wvpnLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnLoginTime.setStatus("current")


class _WvpnRoamTime_Type(DisplayString):
    """Custom type wvpnRoamTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnRoamTime_Type.__name__ = "DisplayString"
_WvpnRoamTime_Object = MibTableColumn
wvpnRoamTime = _WvpnRoamTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 6),
    _WvpnRoamTime_Type()
)
wvpnRoamTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnRoamTime.setStatus("current")


class _WvpnLastActive_Type(DisplayString):
    """Custom type wvpnLastActive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnLastActive_Type.__name__ = "DisplayString"
_WvpnLastActive_Object = MibTableColumn
wvpnLastActive = _WvpnLastActive_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 7),
    _WvpnLastActive_Type()
)
wvpnLastActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnLastActive.setStatus("current")


class _WvpnPoolName_Type(DisplayString):
    """Custom type wvpnPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnPoolName_Type.__name__ = "DisplayString"
_WvpnPoolName_Object = MibTableColumn
wvpnPoolName = _WvpnPoolName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 8),
    _WvpnPoolName_Type()
)
wvpnPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnPoolName.setStatus("current")


class _WvpnMacAddr_Type(DisplayString):
    """Custom type wvpnMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WvpnMacAddr_Type.__name__ = "DisplayString"
_WvpnMacAddr_Object = MibTableColumn
wvpnMacAddr = _WvpnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 1, 1, 9),
    _WvpnMacAddr_Type()
)
wvpnMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnMacAddr.setStatus("current")
_WvpnSessionCount_Type = Integer32
_WvpnSessionCount_Object = MibScalar
wvpnSessionCount = _WvpnSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 2),
    _WvpnSessionCount_Type()
)
wvpnSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnSessionCount.setStatus("current")


class _WvpnRefreshSession_Type(DisplayString):
    """Custom type wvpnRefreshSession based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1000),
    )


_WvpnRefreshSession_Type.__name__ = "DisplayString"
_WvpnRefreshSession_Object = MibScalar
wvpnRefreshSession = _WvpnRefreshSession_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 3),
    _WvpnRefreshSession_Type()
)
wvpnRefreshSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvpnRefreshSession.setStatus("current")


class _WvpnKillSession_Type(Integer32):
    """Custom type wvpnKillSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WvpnKillSession_Type.__name__ = "Integer32"
_WvpnKillSession_Object = MibScalar
wvpnKillSession = _WvpnKillSession_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 3, 34, 7, 4),
    _WvpnKillSession_Type()
)
wvpnKillSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvpnKillSession.setStatus("current")
_SymbolCCPerformance_ObjectIdentity = ObjectIdentity
symbolCCPerformance = _SymbolCCPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 4)
)
_SymbolCCFault_ObjectIdentity = ObjectIdentity
symbolCCFault = _SymbolCCFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 5)
)
_CcTargetObjects_ObjectIdentity = ObjectIdentity
ccTargetObjects = _CcTargetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1)
)


class _CcTargetTrapString_Type(DisplayString):
    """Custom type ccTargetTrapString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CcTargetTrapString_Type.__name__ = "DisplayString"
_CcTargetTrapString_Object = MibScalar
ccTargetTrapString = _CcTargetTrapString_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 1),
    _CcTargetTrapString_Type()
)
ccTargetTrapString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTargetTrapString.setStatus("current")
_CcTargetAddrTable_Object = MibTable
ccTargetAddrTable = _CcTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ccTargetAddrTable.setStatus("current")
_CcTargetAddrEntry_Object = MibTableRow
ccTargetAddrEntry = _CcTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1)
)
ccTargetAddrEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccTargetAddrName"),
)
if mibBuilder.loadTexts:
    ccTargetAddrEntry.setStatus("current")


class _CcTargetAddrName_Type(Integer32):
    """Custom type ccTargetAddrName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CcTargetAddrName_Type.__name__ = "Integer32"
_CcTargetAddrName_Object = MibTableColumn
ccTargetAddrName = _CcTargetAddrName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 1),
    _CcTargetAddrName_Type()
)
ccTargetAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccTargetAddrName.setStatus("current")


class _CcTargetAddrSecName_Type(DisplayString):
    """Custom type ccTargetAddrSecName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcTargetAddrSecName_Type.__name__ = "DisplayString"
_CcTargetAddrSecName_Object = MibTableColumn
ccTargetAddrSecName = _CcTargetAddrSecName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 2),
    _CcTargetAddrSecName_Type()
)
ccTargetAddrSecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrSecName.setStatus("current")


class _CcTargetAddrHost_Type(DisplayString):
    """Custom type ccTargetAddrHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcTargetAddrHost_Type.__name__ = "DisplayString"
_CcTargetAddrHost_Object = MibTableColumn
ccTargetAddrHost = _CcTargetAddrHost_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 3),
    _CcTargetAddrHost_Type()
)
ccTargetAddrHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrHost.setStatus("current")


class _CcTargetAddrCommunity_Type(DisplayString):
    """Custom type ccTargetAddrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcTargetAddrCommunity_Type.__name__ = "DisplayString"
_CcTargetAddrCommunity_Object = MibTableColumn
ccTargetAddrCommunity = _CcTargetAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 4),
    _CcTargetAddrCommunity_Type()
)
ccTargetAddrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrCommunity.setStatus("current")


class _CcTargetAddrPort_Type(Integer32):
    """Custom type ccTargetAddrPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_CcTargetAddrPort_Type.__name__ = "Integer32"
_CcTargetAddrPort_Object = MibTableColumn
ccTargetAddrPort = _CcTargetAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 5),
    _CcTargetAddrPort_Type()
)
ccTargetAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrPort.setStatus("current")


class _CcTargetAddrStorageType_Type(StorageType):
    """Custom type ccTargetAddrStorageType based on StorageType"""
    defaultValue = 3


_CcTargetAddrStorageType_Type.__name__ = "StorageType"
_CcTargetAddrStorageType_Object = MibTableColumn
ccTargetAddrStorageType = _CcTargetAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 6),
    _CcTargetAddrStorageType_Type()
)
ccTargetAddrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrStorageType.setStatus("current")
_CcTargetAddrRowStatus_Type = RowStatus
_CcTargetAddrRowStatus_Object = MibTableColumn
ccTargetAddrRowStatus = _CcTargetAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 7),
    _CcTargetAddrRowStatus_Type()
)
ccTargetAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrRowStatus.setStatus("current")
_CcTargetAddrOption_Type = TargetOptions
_CcTargetAddrOption_Object = MibTableColumn
ccTargetAddrOption = _CcTargetAddrOption_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 1, 2, 1, 8),
    _CcTargetAddrOption_Type()
)
ccTargetAddrOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTargetAddrOption.setStatus("current")
_CcTrapInfos_ObjectIdentity = ObjectIdentity
ccTrapInfos = _CcTrapInfos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2)
)
_CcTrapInfoEnableTrap_Type = TruthValue
_CcTrapInfoEnableTrap_Object = MibScalar
ccTrapInfoEnableTrap = _CcTrapInfoEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 1),
    _CcTrapInfoEnableTrap_Type()
)
ccTrapInfoEnableTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapInfoEnableTrap.setStatus("current")


class _CcTrapInfoMaxNumSendOneTrap_Type(Integer32):
    """Custom type ccTrapInfoMaxNumSendOneTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcTrapInfoMaxNumSendOneTrap_Type.__name__ = "Integer32"
_CcTrapInfoMaxNumSendOneTrap_Object = MibScalar
ccTrapInfoMaxNumSendOneTrap = _CcTrapInfoMaxNumSendOneTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 2),
    _CcTrapInfoMaxNumSendOneTrap_Type()
)
ccTrapInfoMaxNumSendOneTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoMaxNumSendOneTrap.setStatus("current")


class _CcTrapInfoInterval_Type(Integer32):
    """Custom type ccTrapInfoInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CcTrapInfoInterval_Type.__name__ = "Integer32"
_CcTrapInfoInterval_Object = MibScalar
ccTrapInfoInterval = _CcTrapInfoInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 3),
    _CcTrapInfoInterval_Type()
)
ccTrapInfoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoInterval.setStatus("current")
_CcTrapInfoAclViolation_Type = TruthValue
_CcTrapInfoAclViolation_Object = MibScalar
ccTrapInfoAclViolation = _CcTrapInfoAclViolation_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 4),
    _CcTrapInfoAclViolation_Type()
)
ccTrapInfoAclViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoAclViolation.setStatus("current")
_CcTrapInfoDenyAdoption_Type = TruthValue
_CcTrapInfoDenyAdoption_Object = MibScalar
ccTrapInfoDenyAdoption = _CcTrapInfoDenyAdoption_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 5),
    _CcTrapInfoDenyAdoption_Type()
)
ccTrapInfoDenyAdoption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoDenyAdoption.setStatus("current")
_CcTrapInfoAPMUMaxExceed_Type = TruthValue
_CcTrapInfoAPMUMaxExceed_Object = MibScalar
ccTrapInfoAPMUMaxExceed = _CcTrapInfoAPMUMaxExceed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 6),
    _CcTrapInfoAPMUMaxExceed_Type()
)
ccTrapInfoAPMUMaxExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoAPMUMaxExceed.setStatus("current")
_CcTrapInfoWLANMUMaxExceed_Type = TruthValue
_CcTrapInfoWLANMUMaxExceed_Object = MibScalar
ccTrapInfoWLANMUMaxExceed = _CcTrapInfoWLANMUMaxExceed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 7),
    _CcTrapInfoWLANMUMaxExceed_Type()
)
ccTrapInfoWLANMUMaxExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoWLANMUMaxExceed.setStatus("current")
_CcTrapInfoApDetected_Type = TruthValue
_CcTrapInfoApDetected_Object = MibScalar
ccTrapInfoApDetected = _CcTrapInfoApDetected_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 8),
    _CcTrapInfoApDetected_Type()
)
ccTrapInfoApDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoApDetected.setStatus("current")
_CcTrapInfoApAdopted_Type = TruthValue
_CcTrapInfoApAdopted_Object = MibScalar
ccTrapInfoApAdopted = _CcTrapInfoApAdopted_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 9),
    _CcTrapInfoApAdopted_Type()
)
ccTrapInfoApAdopted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoApAdopted.setStatus("current")
_CcTrapInfoApReset_Type = TruthValue
_CcTrapInfoApReset_Object = MibScalar
ccTrapInfoApReset = _CcTrapInfoApReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 10),
    _CcTrapInfoApReset_Type()
)
ccTrapInfoApReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoApReset.setStatus("current")
_CcTrapInfoApUnavailable_Type = TruthValue
_CcTrapInfoApUnavailable_Object = MibScalar
ccTrapInfoApUnavailable = _CcTrapInfoApUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 11),
    _CcTrapInfoApUnavailable_Type()
)
ccTrapInfoApUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoApUnavailable.setStatus("current")
_CcTrapInfoKDCUserAuthFail_Type = TruthValue
_CcTrapInfoKDCUserAuthFail_Object = MibScalar
ccTrapInfoKDCUserAuthFail = _CcTrapInfoKDCUserAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 13),
    _CcTrapInfoKDCUserAuthFail_Type()
)
ccTrapInfoKDCUserAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoKDCUserAuthFail.setStatus("current")
_CcTrapInfoRadiusAuthFail_Type = TruthValue
_CcTrapInfoRadiusAuthFail_Object = MibScalar
ccTrapInfoRadiusAuthFail = _CcTrapInfoRadiusAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 14),
    _CcTrapInfoRadiusAuthFail_Type()
)
ccTrapInfoRadiusAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoRadiusAuthFail.setStatus("current")
_CcTrapInfoLowFlashSpace_Type = TruthValue
_CcTrapInfoLowFlashSpace_Object = MibScalar
ccTrapInfoLowFlashSpace = _CcTrapInfoLowFlashSpace_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 16),
    _CcTrapInfoLowFlashSpace_Type()
)
ccTrapInfoLowFlashSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoLowFlashSpace.setStatus("current")
_CcTrapInfoNicDropping_Type = TruthValue
_CcTrapInfoNicDropping_Object = MibScalar
ccTrapInfoNicDropping = _CcTrapInfoNicDropping_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 17),
    _CcTrapInfoNicDropping_Type()
)
ccTrapInfoNicDropping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoNicDropping.setStatus("current")
_CcTrapInfoApAlert_Type = TruthValue
_CcTrapInfoApAlert_Object = MibScalar
ccTrapInfoApAlert = _CcTrapInfoApAlert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 19),
    _CcTrapInfoApAlert_Type()
)
ccTrapInfoApAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoApAlert.setStatus("current")
_CcTrapInfoUserAuthFail_Type = TruthValue
_CcTrapInfoUserAuthFail_Object = MibScalar
ccTrapInfoUserAuthFail = _CcTrapInfoUserAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 20),
    _CcTrapInfoUserAuthFail_Type()
)
ccTrapInfoUserAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoUserAuthFail.setStatus("current")
_CcTrapInfoHsbPrimaryNoHeartbeat_Type = TruthValue
_CcTrapInfoHsbPrimaryNoHeartbeat_Object = MibScalar
ccTrapInfoHsbPrimaryNoHeartbeat = _CcTrapInfoHsbPrimaryNoHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 21),
    _CcTrapInfoHsbPrimaryNoHeartbeat_Type()
)
ccTrapInfoHsbPrimaryNoHeartbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoHsbPrimaryNoHeartbeat.setStatus("current")
_CcTrapInfoHsbStandbyEntersFailover_Type = TruthValue
_CcTrapInfoHsbStandbyEntersFailover_Object = MibScalar
ccTrapInfoHsbStandbyEntersFailover = _CcTrapInfoHsbStandbyEntersFailover_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 22),
    _CcTrapInfoHsbStandbyEntersFailover_Type()
)
ccTrapInfoHsbStandbyEntersFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoHsbStandbyEntersFailover.setStatus("current")
_CcTrapInfoPrimaryFailedResetting_Type = TruthValue
_CcTrapInfoPrimaryFailedResetting_Object = MibScalar
ccTrapInfoPrimaryFailedResetting = _CcTrapInfoPrimaryFailedResetting_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 23),
    _CcTrapInfoPrimaryFailedResetting_Type()
)
ccTrapInfoPrimaryFailedResetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoPrimaryFailedResetting.setStatus("current")
_CcTrapInfoKDCPropagationFail_Type = TruthValue
_CcTrapInfoKDCPropagationFail_Object = MibScalar
ccTrapInfoKDCPropagationFail = _CcTrapInfoKDCPropagationFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 25),
    _CcTrapInfoKDCPropagationFail_Type()
)
ccTrapInfoKDCPropagationFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoKDCPropagationFail.setStatus("current")
_CcTrapInfoHighDecryptFail_Type = TruthValue
_CcTrapInfoHighDecryptFail_Object = MibScalar
ccTrapInfoHighDecryptFail = _CcTrapInfoHighDecryptFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 26),
    _CcTrapInfoHighDecryptFail_Type()
)
ccTrapInfoHighDecryptFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoHighDecryptFail.setStatus("current")
_CcTrapInfoHighReplyFail_Type = TruthValue
_CcTrapInfoHighReplyFail_Object = MibScalar
ccTrapInfoHighReplyFail = _CcTrapInfoHighReplyFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 27),
    _CcTrapInfoHighReplyFail_Type()
)
ccTrapInfoHighReplyFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoHighReplyFail.setStatus("current")
_CcTrapInfoTKIPMICFail_Type = TruthValue
_CcTrapInfoTKIPMICFail_Object = MibScalar
ccTrapInfoTKIPMICFail = _CcTrapInfoTKIPMICFail_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 28),
    _CcTrapInfoTKIPMICFail_Type()
)
ccTrapInfoTKIPMICFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoTKIPMICFail.setStatus("current")
_CcTrapInfoWPACounterMeasureStart_Type = TruthValue
_CcTrapInfoWPACounterMeasureStart_Object = MibScalar
ccTrapInfoWPACounterMeasureStart = _CcTrapInfoWPACounterMeasureStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 29),
    _CcTrapInfoWPACounterMeasureStart_Type()
)
ccTrapInfoWPACounterMeasureStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoWPACounterMeasureStart.setStatus("current")
_LicenseChangedControl_Type = TruthValue
_LicenseChangedControl_Object = MibScalar
licenseChangedControl = _LicenseChangedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 31),
    _LicenseChangedControl_Type()
)
licenseChangedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseChangedControl.setStatus("current")
_ClockChangedControl_Type = TruthValue
_ClockChangedControl_Object = MibScalar
clockChangedControl = _ClockChangedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 32),
    _ClockChangedControl_Type()
)
clockChangedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockChangedControl.setStatus("current")
_PktDiscWrongNICControl_Type = TruthValue
_PktDiscWrongNICControl_Object = MibScalar
pktDiscWrongNICControl = _PktDiscWrongNICControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 33),
    _PktDiscWrongNICControl_Type()
)
pktDiscWrongNICControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktDiscWrongNICControl.setStatus("current")
_PktDiscWrongVLANControl_Type = TruthValue
_PktDiscWrongVLANControl_Object = MibScalar
pktDiscWrongVLANControl = _PktDiscWrongVLANControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 34),
    _PktDiscWrongVLANControl_Type()
)
pktDiscWrongVLANControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktDiscWrongVLANControl.setStatus("current")
_ApAdoptFailPolControl_Type = TruthValue
_ApAdoptFailPolControl_Object = MibScalar
apAdoptFailPolControl = _ApAdoptFailPolControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 35),
    _ApAdoptFailPolControl_Type()
)
apAdoptFailPolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdoptFailPolControl.setStatus("current")
_ApAdoptFailACLControl_Type = TruthValue
_ApAdoptFailACLControl_Object = MibScalar
apAdoptFailACLControl = _ApAdoptFailACLControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 36),
    _ApAdoptFailACLControl_Type()
)
apAdoptFailACLControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdoptFailACLControl.setStatus("current")
_ApAdoptFailLimitControl_Type = TruthValue
_ApAdoptFailLimitControl_Object = MibScalar
apAdoptFailLimitControl = _ApAdoptFailLimitControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 37),
    _ApAdoptFailLimitControl_Type()
)
apAdoptFailLimitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdoptFailLimitControl.setStatus("current")
_ApAdoptFailLicControl_Type = TruthValue
_ApAdoptFailLicControl_Object = MibScalar
apAdoptFailLicControl = _ApAdoptFailLicControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 38),
    _ApAdoptFailLicControl_Type()
)
apAdoptFailLicControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdoptFailLicControl.setStatus("current")
_ApAdoptFailNoImgControl_Type = TruthValue
_ApAdoptFailNoImgControl_Object = MibScalar
apAdoptFailNoImgControl = _ApAdoptFailNoImgControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 39),
    _ApAdoptFailNoImgControl_Type()
)
apAdoptFailNoImgControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdoptFailNoImgControl.setStatus("current")
_ApCfgFailESSControl_Type = TruthValue
_ApCfgFailESSControl_Object = MibScalar
apCfgFailESSControl = _ApCfgFailESSControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 40),
    _ApCfgFailESSControl_Type()
)
apCfgFailESSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCfgFailESSControl.setStatus("current")
_DevDropInfoMsgControl_Type = TruthValue
_DevDropInfoMsgControl_Object = MibScalar
devDropInfoMsgControl = _DevDropInfoMsgControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 41),
    _DevDropInfoMsgControl_Type()
)
devDropInfoMsgControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDropInfoMsgControl.setStatus("current")
_DevdropLoadmeMsgControl_Type = TruthValue
_DevdropLoadmeMsgControl_Object = MibScalar
devdropLoadmeMsgControl = _DevdropLoadmeMsgControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 42),
    _DevdropLoadmeMsgControl_Type()
)
devdropLoadmeMsgControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devdropLoadmeMsgControl.setStatus("current")
_EtherConnectControl_Type = TruthValue
_EtherConnectControl_Object = MibScalar
etherConnectControl = _EtherConnectControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 43),
    _EtherConnectControl_Type()
)
etherConnectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherConnectControl.setStatus("current")
_MuAssocFailControl_Type = TruthValue
_MuAssocFailControl_Object = MibScalar
muAssocFailControl = _MuAssocFailControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 44),
    _MuAssocFailControl_Type()
)
muAssocFailControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muAssocFailControl.setStatus("current")
_MuAssocOKControl_Type = TruthValue
_MuAssocOKControl_Object = MibScalar
muAssocOKControl = _MuAssocOKControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 45),
    _MuAssocOKControl_Type()
)
muAssocOKControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muAssocOKControl.setStatus("current")
_MuRoamedControl_Type = TruthValue
_MuRoamedControl_Object = MibScalar
muRoamedControl = _MuRoamedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 46),
    _MuRoamedControl_Type()
)
muRoamedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muRoamedControl.setStatus("current")
_MuDisassocControl_Type = TruthValue
_MuDisassocControl_Object = MibScalar
muDisassocControl = _MuDisassocControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 47),
    _MuDisassocControl_Type()
)
muDisassocControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muDisassocControl.setStatus("current")
_MuEAPAuthFailControl_Type = TruthValue
_MuEAPAuthFailControl_Object = MibScalar
muEAPAuthFailControl = _MuEAPAuthFailControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 48),
    _MuEAPAuthFailControl_Type()
)
muEAPAuthFailControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muEAPAuthFailControl.setStatus("current")
_MuEAPAuthOKControl_Type = TruthValue
_MuEAPAuthOKControl_Object = MibScalar
muEAPAuthOKControl = _MuEAPAuthOKControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 49),
    _MuEAPAuthOKControl_Type()
)
muEAPAuthOKControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muEAPAuthOKControl.setStatus("current")
_MuKDCAuthOKControl_Type = TruthValue
_MuKDCAuthOKControl_Object = MibScalar
muKDCAuthOKControl = _MuKDCAuthOKControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 50),
    _MuKDCAuthOKControl_Type()
)
muKDCAuthOKControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muKDCAuthOKControl.setStatus("current")
_WlanAuthOKControl_Type = TruthValue
_WlanAuthOKControl_Object = MibScalar
wlanAuthOKControl = _WlanAuthOKControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 51),
    _WlanAuthOKControl_Type()
)
wlanAuthOKControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthOKControl.setStatus("current")
_WlanAuthFailControl_Type = TruthValue
_WlanAuthFailControl_Object = MibScalar
wlanAuthFailControl = _WlanAuthFailControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 52),
    _WlanAuthFailControl_Type()
)
wlanAuthFailControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthFailControl.setStatus("current")
_UserAuthOKControl_Type = TruthValue
_UserAuthOKControl_Object = MibScalar
userAuthOKControl = _UserAuthOKControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 53),
    _UserAuthOKControl_Type()
)
userAuthOKControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthOKControl.setStatus("current")
_RadiusSrvTimeoutControl_Type = TruthValue
_RadiusSrvTimeoutControl_Object = MibScalar
radiusSrvTimeoutControl = _RadiusSrvTimeoutControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 54),
    _RadiusSrvTimeoutControl_Type()
)
radiusSrvTimeoutControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvTimeoutControl.setStatus("current")
_KdcPrincAddControl_Type = TruthValue
_KdcPrincAddControl_Object = MibScalar
kdcPrincAddControl = _KdcPrincAddControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 55),
    _KdcPrincAddControl_Type()
)
kdcPrincAddControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kdcPrincAddControl.setStatus("current")
_KdcPrincChgdControl_Type = TruthValue
_KdcPrincChgdControl_Object = MibScalar
kdcPrincChgdControl = _KdcPrincChgdControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 56),
    _KdcPrincChgdControl_Type()
)
kdcPrincChgdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kdcPrincChgdControl.setStatus("current")
_KdcPrincDelControl_Type = TruthValue
_KdcPrincDelControl_Object = MibScalar
kdcPrincDelControl = _KdcPrincDelControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 57),
    _KdcPrincDelControl_Type()
)
kdcPrincDelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kdcPrincDelControl.setStatus("current")
_KdcDBReplacedControl_Type = TruthValue
_KdcDBReplacedControl_Object = MibScalar
kdcDBReplacedControl = _KdcDBReplacedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 58),
    _KdcDBReplacedControl_Type()
)
kdcDBReplacedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kdcDBReplacedControl.setStatus("current")
_HsbStdbyAutoRevControl_Type = TruthValue
_HsbStdbyAutoRevControl_Object = MibScalar
hsbStdbyAutoRevControl = _HsbStdbyAutoRevControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 59),
    _HsbStdbyAutoRevControl_Type()
)
hsbStdbyAutoRevControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsbStdbyAutoRevControl.setStatus("current")
_HsbPrimAutoRevControl_Type = TruthValue
_HsbPrimAutoRevControl_Object = MibScalar
hsbPrimAutoRevControl = _HsbPrimAutoRevControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 60),
    _HsbPrimAutoRevControl_Type()
)
hsbPrimAutoRevControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsbPrimAutoRevControl.setStatus("current")
_AcsErrorControl_Type = TruthValue
_AcsErrorControl_Object = MibScalar
acsErrorControl = _AcsErrorControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 61),
    _AcsErrorControl_Type()
)
acsErrorControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsErrorControl.setStatus("current")
_EopActiveControl_Type = TruthValue
_EopActiveControl_Object = MibScalar
eopActiveControl = _EopActiveControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 62),
    _EopActiveControl_Type()
)
eopActiveControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eopActiveControl.setStatus("current")
_EopInactiveControl_Type = TruthValue
_EopInactiveControl_Object = MibScalar
eopInactiveControl = _EopInactiveControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 63),
    _EopInactiveControl_Type()
)
eopInactiveControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eopInactiveControl.setStatus("current")
_DebugEventControl_Type = TruthValue
_DebugEventControl_Object = MibScalar
debugEventControl = _DebugEventControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 64),
    _DebugEventControl_Type()
)
debugEventControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugEventControl.setStatus("current")
_HsbStartUpControl_Type = TruthValue
_HsbStartUpControl_Object = MibScalar
hsbStartUpControl = _HsbStartUpControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 65),
    _HsbStartUpControl_Type()
)
hsbStartUpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsbStartUpControl.setStatus("current")
_HsbPeerConnectControl_Type = TruthValue
_HsbPeerConnectControl_Object = MibScalar
hsbPeerConnectControl = _HsbPeerConnectControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 66),
    _HsbPeerConnectControl_Type()
)
hsbPeerConnectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsbPeerConnectControl.setStatus("current")
_CcFanAndTempControl_Type = TruthValue
_CcFanAndTempControl_Object = MibScalar
ccFanAndTempControl = _CcFanAndTempControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 67),
    _CcFanAndTempControl_Type()
)
ccFanAndTempControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccFanAndTempControl.setStatus("current")
_CcAccessChangedControl_Type = TruthValue
_CcAccessChangedControl_Object = MibScalar
ccAccessChangedControl = _CcAccessChangedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 68),
    _CcAccessChangedControl_Type()
)
ccAccessChangedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAccessChangedControl.setStatus("current")
_TpcPowerReducedControl_Type = TruthValue
_TpcPowerReducedControl_Object = MibScalar
tpcPowerReducedControl = _TpcPowerReducedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 69),
    _TpcPowerReducedControl_Type()
)
tpcPowerReducedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpcPowerReducedControl.setStatus("current")
_DfsRadarDetectControl_Type = TruthValue
_DfsRadarDetectControl_Object = MibScalar
dfsRadarDetectControl = _DfsRadarDetectControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 70),
    _DfsRadarDetectControl_Type()
)
dfsRadarDetectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsRadarDetectControl.setStatus("current")
_DfsChannelSelectControl_Type = TruthValue
_DfsChannelSelectControl_Object = MibScalar
dfsChannelSelectControl = _DfsChannelSelectControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 71),
    _DfsChannelSelectControl_Type()
)
dfsChannelSelectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsChannelSelectControl.setStatus("current")
_DfsChannelSwitchControl_Type = TruthValue
_DfsChannelSwitchControl_Object = MibScalar
dfsChannelSwitchControl = _DfsChannelSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 72),
    _DfsChannelSwitchControl_Type()
)
dfsChannelSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsChannelSwitchControl.setStatus("current")
_DfsChannelRevertControl_Type = TruthValue
_DfsChannelRevertControl_Object = MibScalar
dfsChannelRevertControl = _DfsChannelRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 73),
    _DfsChannelRevertControl_Type()
)
dfsChannelRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsChannelRevertControl.setStatus("current")
_RadioSuspendControl_Type = TruthValue
_RadioSuspendControl_Object = MibScalar
radioSuspendControl = _RadioSuspendControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 74),
    _RadioSuspendControl_Type()
)
radioSuspendControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioSuspendControl.setStatus("current")
_RadioResumeControl_Type = TruthValue
_RadioResumeControl_Object = MibScalar
radioResumeControl = _RadioResumeControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 75),
    _RadioResumeControl_Type()
)
radioResumeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioResumeControl.setStatus("current")
_RadioRandomChannelControl_Type = TruthValue
_RadioRandomChannelControl_Object = MibScalar
radioRandomChannelControl = _RadioRandomChannelControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 76),
    _RadioRandomChannelControl_Type()
)
radioRandomChannelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRandomChannelControl.setStatus("current")
_CcRapNewRogueApControl_Type = TruthValue
_CcRapNewRogueApControl_Object = MibScalar
ccRapNewRogueApControl = _CcRapNewRogueApControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 77),
    _CcRapNewRogueApControl_Type()
)
ccRapNewRogueApControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapNewRogueApControl.setStatus("current")
_CcRapNewApprovedApControl_Type = TruthValue
_CcRapNewApprovedApControl_Object = MibScalar
ccRapNewApprovedApControl = _CcRapNewApprovedApControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 78),
    _CcRapNewApprovedApControl_Type()
)
ccRapNewApprovedApControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapNewApprovedApControl.setStatus("current")
_CcTrapInfoWVPNAlert_Type = TruthValue
_CcTrapInfoWVPNAlert_Object = MibScalar
ccTrapInfoWVPNAlert = _CcTrapInfoWVPNAlert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 79),
    _CcTrapInfoWVPNAlert_Type()
)
ccTrapInfoWVPNAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoWVPNAlert.setStatus("current")
_CcTrapInfoWVPNInfo_Type = TruthValue
_CcTrapInfoWVPNInfo_Object = MibScalar
ccTrapInfoWVPNInfo = _CcTrapInfoWVPNInfo_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 80),
    _CcTrapInfoWVPNInfo_Type()
)
ccTrapInfoWVPNInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoWVPNInfo.setStatus("current")
_CcTrapInfoRadiusAcct_Type = TruthValue
_CcTrapInfoRadiusAcct_Object = MibScalar
ccTrapInfoRadiusAcct = _CcTrapInfoRadiusAcct_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 81),
    _CcTrapInfoRadiusAcct_Type()
)
ccTrapInfoRadiusAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapInfoRadiusAcct.setStatus("current")
_CcInfoRadiusServerControl_Type = TruthValue
_CcInfoRadiusServerControl_Object = MibScalar
ccInfoRadiusServerControl = _CcInfoRadiusServerControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 82),
    _CcInfoRadiusServerControl_Type()
)
ccInfoRadiusServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccInfoRadiusServerControl.setStatus("current")
_ConfigChangeUpdateControl_Type = TruthValue
_ConfigChangeUpdateControl_Object = MibScalar
configChangeUpdateControl = _ConfigChangeUpdateControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 83),
    _ConfigChangeUpdateControl_Type()
)
configChangeUpdateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configChangeUpdateControl.setStatus("current")
_TunnelStatusChangedControl_Type = TruthValue
_TunnelStatusChangedControl_Object = MibScalar
tunnelStatusChangedControl = _TunnelStatusChangedControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 84),
    _TunnelStatusChangedControl_Type()
)
tunnelStatusChangedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelStatusChangedControl.setStatus("current")
_TunnelUnknownProtocolControl_Type = TruthValue
_TunnelUnknownProtocolControl_Object = MibScalar
tunnelUnknownProtocolControl = _TunnelUnknownProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 85),
    _TunnelUnknownProtocolControl_Type()
)
tunnelUnknownProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelUnknownProtocolControl.setStatus("current")
_CcSumStatsApControl_Type = TruthValue
_CcSumStatsApControl_Object = MibScalar
ccSumStatsApControl = _CcSumStatsApControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 86),
    _CcSumStatsApControl_Type()
)
ccSumStatsApControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSumStatsApControl.setStatus("current")
_CcSumStatsMuControl_Type = TruthValue
_CcSumStatsMuControl_Object = MibScalar
ccSumStatsMuControl = _CcSumStatsMuControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 87),
    _CcSumStatsMuControl_Type()
)
ccSumStatsMuControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSumStatsMuControl.setStatus("current")
_CcSumStatsWlanControl_Type = TruthValue
_CcSumStatsWlanControl_Object = MibScalar
ccSumStatsWlanControl = _CcSumStatsWlanControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 88),
    _CcSumStatsWlanControl_Type()
)
ccSumStatsWlanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSumStatsWlanControl.setStatus("current")
_CcSumStatsSwitchControl_Type = TruthValue
_CcSumStatsSwitchControl_Object = MibScalar
ccSumStatsSwitchControl = _CcSumStatsSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 89),
    _CcSumStatsSwitchControl_Type()
)
ccSumStatsSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSumStatsSwitchControl.setStatus("current")
_SensorConvertControl_Type = TruthValue
_SensorConvertControl_Object = MibScalar
sensorConvertControl = _SensorConvertControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 90),
    _SensorConvertControl_Type()
)
sensorConvertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorConvertControl.setStatus("current")
_SensorRevertControl_Type = TruthValue
_SensorRevertControl_Object = MibScalar
sensorRevertControl = _SensorRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 91),
    _SensorRevertControl_Type()
)
sensorRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorRevertControl.setStatus("current")
_SensorFailureControl_Type = TruthValue
_SensorFailureControl_Object = MibScalar
sensorFailureControl = _SensorFailureControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 92),
    _SensorFailureControl_Type()
)
sensorFailureControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorFailureControl.setStatus("current")
_SensorOfflineControl_Type = TruthValue
_SensorOfflineControl_Object = MibScalar
sensorOfflineControl = _SensorOfflineControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 2, 93),
    _SensorOfflineControl_Type()
)
sensorOfflineControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorOfflineControl.setStatus("current")
_SymbolCCTraps_ObjectIdentity = ObjectIdentity
symbolCCTraps = _SymbolCCTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3)
)
_SymbolCCNewInV1dot2dot5_ObjectIdentity = ObjectIdentity
symbolCCNewInV1dot2dot5 = _SymbolCCNewInV1dot2dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6)
)
_CcIdentfication_ObjectIdentity = ObjectIdentity
ccIdentfication = _CcIdentfication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1)
)
_CcIdHwVersion_Type = DisplayString
_CcIdHwVersion_Object = MibScalar
ccIdHwVersion = _CcIdHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 1),
    _CcIdHwVersion_Type()
)
ccIdHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdHwVersion.setStatus("current")
_CcIdFwVersion_Type = DisplayString
_CcIdFwVersion_Object = MibScalar
ccIdFwVersion = _CcIdFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 2),
    _CcIdFwVersion_Type()
)
ccIdFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdFwVersion.setStatus("current")
_CcIdSwVersion_Type = DisplayString
_CcIdSwVersion_Object = MibScalar
ccIdSwVersion = _CcIdSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 3),
    _CcIdSwVersion_Type()
)
ccIdSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdSwVersion.setStatus("current")
_CcIdMibVersion_Type = DisplayString
_CcIdMibVersion_Object = MibScalar
ccIdMibVersion = _CcIdMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 4),
    _CcIdMibVersion_Type()
)
ccIdMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdMibVersion.setStatus("current")
_CcIdCliVersion_Type = DisplayString
_CcIdCliVersion_Object = MibScalar
ccIdCliVersion = _CcIdCliVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 5),
    _CcIdCliVersion_Type()
)
ccIdCliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdCliVersion.setStatus("current")
_CcIdXmlVersion_Type = DisplayString
_CcIdXmlVersion_Object = MibScalar
ccIdXmlVersion = _CcIdXmlVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 6),
    _CcIdXmlVersion_Type()
)
ccIdXmlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdXmlVersion.setStatus("current")
_CcIdSerialNumber_Type = DisplayString
_CcIdSerialNumber_Object = MibScalar
ccIdSerialNumber = _CcIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 7),
    _CcIdSerialNumber_Type()
)
ccIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdSerialNumber.setStatus("current")
_CcIdSwBuildDate_Type = DisplayString
_CcIdSwBuildDate_Object = MibScalar
ccIdSwBuildDate = _CcIdSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 8),
    _CcIdSwBuildDate_Type()
)
ccIdSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdSwBuildDate.setStatus("current")
_CcIdSwBuildInfo_Type = DisplayString
_CcIdSwBuildInfo_Object = MibScalar
ccIdSwBuildInfo = _CcIdSwBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 9),
    _CcIdSwBuildInfo_Type()
)
ccIdSwBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdSwBuildInfo.setStatus("current")
_CcIdProductFamily_Type = DisplayString
_CcIdProductFamily_Object = MibScalar
ccIdProductFamily = _CcIdProductFamily_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 10),
    _CcIdProductFamily_Type()
)
ccIdProductFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdProductFamily.setStatus("current")
_CcIdProductModel_Type = DisplayString
_CcIdProductModel_Object = MibScalar
ccIdProductModel = _CcIdProductModel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1, 11),
    _CcIdProductModel_Type()
)
ccIdProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdProductModel.setStatus("current")
_CcHwSensors_ObjectIdentity = ObjectIdentity
ccHwSensors = _CcHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2)
)
_CcHwSensorsReset_Type = DoActionNow
_CcHwSensorsReset_Object = MibScalar
ccHwSensorsReset = _CcHwSensorsReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 1),
    _CcHwSensorsReset_Type()
)
ccHwSensorsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHwSensorsReset.setStatus("current")
_CcHwSensorsTable_Object = MibTable
ccHwSensorsTable = _CcHwSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2)
)
if mibBuilder.loadTexts:
    ccHwSensorsTable.setStatus("current")
_CcHwSensorsEntry_Object = MibTableRow
ccHwSensorsEntry = _CcHwSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1)
)
ccHwSensorsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccHwSensorsIndex"),
)
if mibBuilder.loadTexts:
    ccHwSensorsEntry.setStatus("current")


class _CcHwSensorsIndex_Type(Integer32):
    """Custom type ccHwSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcHwSensorsIndex_Type.__name__ = "Integer32"
_CcHwSensorsIndex_Object = MibTableColumn
ccHwSensorsIndex = _CcHwSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 1),
    _CcHwSensorsIndex_Type()
)
ccHwSensorsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccHwSensorsIndex.setStatus("current")


class _CcHwSensorsType_Type(Integer32):
    """Custom type ccHwSensorsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tempInDegC", 2),
          ("variableSpeedFanInRpm", 3),
          ("onOffFanInDutyCycle", 4))
    )


_CcHwSensorsType_Type.__name__ = "Integer32"
_CcHwSensorsType_Object = MibTableColumn
ccHwSensorsType = _CcHwSensorsType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 2),
    _CcHwSensorsType_Type()
)
ccHwSensorsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHwSensorsType.setStatus("current")
_CcHwSensorsDescr_Type = DisplayString
_CcHwSensorsDescr_Object = MibTableColumn
ccHwSensorsDescr = _CcHwSensorsDescr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 3),
    _CcHwSensorsDescr_Type()
)
ccHwSensorsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHwSensorsDescr.setStatus("current")
_CcHwSensorsCurrentReading_Type = Integer32
_CcHwSensorsCurrentReading_Object = MibTableColumn
ccHwSensorsCurrentReading = _CcHwSensorsCurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 4),
    _CcHwSensorsCurrentReading_Type()
)
ccHwSensorsCurrentReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHwSensorsCurrentReading.setStatus("current")
_CcHwSensorsMinimum_Type = Gauge32
_CcHwSensorsMinimum_Object = MibTableColumn
ccHwSensorsMinimum = _CcHwSensorsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 5),
    _CcHwSensorsMinimum_Type()
)
ccHwSensorsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHwSensorsMinimum.setStatus("current")
_CcHwSensorsMaximum_Type = Gauge32
_CcHwSensorsMaximum_Object = MibTableColumn
ccHwSensorsMaximum = _CcHwSensorsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 6),
    _CcHwSensorsMaximum_Type()
)
ccHwSensorsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccHwSensorsMaximum.setStatus("current")
_CcHwSensorsNotifyIfAbove_Type = Integer32
_CcHwSensorsNotifyIfAbove_Object = MibTableColumn
ccHwSensorsNotifyIfAbove = _CcHwSensorsNotifyIfAbove_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 2, 2, 1, 7),
    _CcHwSensorsNotifyIfAbove_Type()
)
ccHwSensorsNotifyIfAbove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccHwSensorsNotifyIfAbove.setStatus("current")
_CcSsh_ObjectIdentity = ObjectIdentity
ccSsh = _CcSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 3)
)
_CcSshEnabled_Type = TruthValue
_CcSshEnabled_Object = MibScalar
ccSshEnabled = _CcSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 3, 1),
    _CcSshEnabled_Type()
)
ccSshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSshEnabled.setStatus("current")


class _CcSshProtocolVersion_Type(Integer32):
    """Custom type ccSshProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sshV1orV2", 1),
          ("sshV2", 2))
    )


_CcSshProtocolVersion_Type.__name__ = "Integer32"
_CcSshProtocolVersion_Object = MibScalar
ccSshProtocolVersion = _CcSshProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 3, 2),
    _CcSshProtocolVersion_Type()
)
ccSshProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSshProtocolVersion.setStatus("current")
_CcSshPort_Type = Integer32
_CcSshPort_Object = MibScalar
ccSshPort = _CcSshPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 3, 3),
    _CcSshPort_Type()
)
ccSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSshPort.setStatus("current")
_CcSshAuthenticationTimeout_Type = Integer32
_CcSshAuthenticationTimeout_Object = MibScalar
ccSshAuthenticationTimeout = _CcSshAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 3, 4),
    _CcSshAuthenticationTimeout_Type()
)
ccSshAuthenticationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSshAuthenticationTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccSshAuthenticationTimeout.setUnits("seconds")
_CcSshInactivityTimeout_Type = Integer32
_CcSshInactivityTimeout_Object = MibScalar
ccSshInactivityTimeout = _CcSshInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 3, 5),
    _CcSshInactivityTimeout_Type()
)
ccSshInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSshInactivityTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccSshInactivityTimeout.setUnits("minutes")
_CcAccessMethods_ObjectIdentity = ObjectIdentity
ccAccessMethods = _CcAccessMethods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 4)
)


class _CcAccessMethodsPermitted_Type(Bits):
    """Custom type ccAccessMethodsPermitted based on Bits"""
    namedValues = NamedValues(
        *(("accessViaTelnetAllowed", 0),
          ("accessViaSshAllowed", 1),
          ("accessViaXmlAllowed", 2),
          ("accessViaSnmpV12Allowed", 3),
          ("accessViaSnmpV3Allowed", 4))
    )

_CcAccessMethodsPermitted_Type.__name__ = "Bits"
_CcAccessMethodsPermitted_Object = MibScalar
ccAccessMethodsPermitted = _CcAccessMethodsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 4, 1),
    _CcAccessMethodsPermitted_Type()
)
ccAccessMethodsPermitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAccessMethodsPermitted.setStatus("deprecated")
_CcV1dot2dot5Groups_ObjectIdentity = ObjectIdentity
ccV1dot2dot5Groups = _CcV1dot2dot5Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1000)
)
_CcRadiusServer_ObjectIdentity = ObjectIdentity
ccRadiusServer = _CcRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9)
)
_CcRadius_ObjectIdentity = ObjectIdentity
ccRadius = _CcRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1)
)


class _CcRadiusDataSource_Type(Integer32):
    """Custom type ccRadiusDataSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("ldap", 2))
    )


_CcRadiusDataSource_Type.__name__ = "Integer32"
_CcRadiusDataSource_Object = MibScalar
ccRadiusDataSource = _CcRadiusDataSource_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 1),
    _CcRadiusDataSource_Type()
)
ccRadiusDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusDataSource.setStatus("current")


class _CcRadiusDefaultEapType_Type(Integer32):
    """Custom type ccRadiusDefaultEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ttls", 1),
          ("peap", 2))
    )


_CcRadiusDefaultEapType_Type.__name__ = "Integer32"
_CcRadiusDefaultEapType_Object = MibScalar
ccRadiusDefaultEapType = _CcRadiusDefaultEapType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 2),
    _CcRadiusDefaultEapType_Type()
)
ccRadiusDefaultEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusDefaultEapType.setStatus("current")


class _CcRadiusAuthTypePeap_Type(Integer32):
    """Custom type ccRadiusAuthTypePeap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gtc", 1),
          ("mschapv2", 2))
    )


_CcRadiusAuthTypePeap_Type.__name__ = "Integer32"
_CcRadiusAuthTypePeap_Object = MibScalar
ccRadiusAuthTypePeap = _CcRadiusAuthTypePeap_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 3),
    _CcRadiusAuthTypePeap_Type()
)
ccRadiusAuthTypePeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAuthTypePeap.setStatus("current")


class _CcRadiusAuthTypeTtls_Type(Integer32):
    """Custom type ccRadiusAuthTypeTtls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("pap", 2),
          ("mschapv2", 3))
    )


_CcRadiusAuthTypeTtls_Type.__name__ = "Integer32"
_CcRadiusAuthTypeTtls_Object = MibScalar
ccRadiusAuthTypeTtls = _CcRadiusAuthTypeTtls_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 4),
    _CcRadiusAuthTypeTtls_Type()
)
ccRadiusAuthTypeTtls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAuthTypeTtls.setStatus("current")


class _CcRadiusServerCertificate_Type(DisplayString):
    """Custom type ccRadiusServerCertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CcRadiusServerCertificate_Type.__name__ = "DisplayString"
_CcRadiusServerCertificate_Object = MibScalar
ccRadiusServerCertificate = _CcRadiusServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 5),
    _CcRadiusServerCertificate_Type()
)
ccRadiusServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusServerCertificate.setStatus("current")


class _CcRadiusCACertificate_Type(DisplayString):
    """Custom type ccRadiusCACertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CcRadiusCACertificate_Type.__name__ = "DisplayString"
_CcRadiusCACertificate_Object = MibScalar
ccRadiusCACertificate = _CcRadiusCACertificate_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 6),
    _CcRadiusCACertificate_Type()
)
ccRadiusCACertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusCACertificate.setStatus("current")
_CcRadiusClientAuthTable_Object = MibTable
ccRadiusClientAuthTable = _CcRadiusClientAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7)
)
if mibBuilder.loadTexts:
    ccRadiusClientAuthTable.setStatus("current")
_CcRadiusClientAuthEntry_Object = MibTableRow
ccRadiusClientAuthEntry = _CcRadiusClientAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7, 1)
)
ccRadiusClientAuthEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadiusClientAuthIndex"),
)
if mibBuilder.loadTexts:
    ccRadiusClientAuthEntry.setStatus("current")
_CcRadiusClientAuthIndex_Type = DisplayString
_CcRadiusClientAuthIndex_Object = MibTableColumn
ccRadiusClientAuthIndex = _CcRadiusClientAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7, 1, 1),
    _CcRadiusClientAuthIndex_Type()
)
ccRadiusClientAuthIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusClientAuthIndex.setStatus("current")
_CcRadiusClientAuthIpAddr_Type = DisplayString
_CcRadiusClientAuthIpAddr_Object = MibTableColumn
ccRadiusClientAuthIpAddr = _CcRadiusClientAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7, 1, 2),
    _CcRadiusClientAuthIpAddr_Type()
)
ccRadiusClientAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusClientAuthIpAddr.setStatus("current")
_CcRadiusClientAuthMask_Type = DisplayString
_CcRadiusClientAuthMask_Object = MibTableColumn
ccRadiusClientAuthMask = _CcRadiusClientAuthMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7, 1, 3),
    _CcRadiusClientAuthMask_Type()
)
ccRadiusClientAuthMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusClientAuthMask.setStatus("current")


class _CcRadiusClientAuthSharedSecret_Type(DisplayString):
    """Custom type ccRadiusClientAuthSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadiusClientAuthSharedSecret_Type.__name__ = "DisplayString"
_CcRadiusClientAuthSharedSecret_Object = MibTableColumn
ccRadiusClientAuthSharedSecret = _CcRadiusClientAuthSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7, 1, 4),
    _CcRadiusClientAuthSharedSecret_Type()
)
ccRadiusClientAuthSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusClientAuthSharedSecret.setStatus("current")
_CcRadiusClientAuthRowStatus_Type = AbbrevRowStatus
_CcRadiusClientAuthRowStatus_Object = MibTableColumn
ccRadiusClientAuthRowStatus = _CcRadiusClientAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 7, 1, 5),
    _CcRadiusClientAuthRowStatus_Type()
)
ccRadiusClientAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusClientAuthRowStatus.setStatus("current")
_CcRadiusServerEnable_Type = TruthValue
_CcRadiusServerEnable_Object = MibScalar
ccRadiusServerEnable = _CcRadiusServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 8),
    _CcRadiusServerEnable_Type()
)
ccRadiusServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusServerEnable.setStatus("current")


class _CcRadiusSaveStatus_Type(Integer32):
    """Custom type ccRadiusSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CcRadiusSaveStatus_Type.__name__ = "Integer32"
_CcRadiusSaveStatus_Object = MibScalar
ccRadiusSaveStatus = _CcRadiusSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 9),
    _CcRadiusSaveStatus_Type()
)
ccRadiusSaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusSaveStatus.setStatus("current")


class _CcRadiusEapPasswd_Type(OctetString):
    """Custom type ccRadiusEapPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcRadiusEapPasswd_Type.__name__ = "OctetString"
_CcRadiusEapPasswd_Object = MibScalar
ccRadiusEapPasswd = _CcRadiusEapPasswd_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 1, 10),
    _CcRadiusEapPasswd_Type()
)
ccRadiusEapPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusEapPasswd.setStatus("current")
_CcRadiusProxy_ObjectIdentity = ObjectIdentity
ccRadiusProxy = _CcRadiusProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2)
)


class _CcRadiusProxyRetryCount_Type(Integer32):
    """Custom type ccRadiusProxyRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_CcRadiusProxyRetryCount_Type.__name__ = "Integer32"
_CcRadiusProxyRetryCount_Object = MibScalar
ccRadiusProxyRetryCount = _CcRadiusProxyRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 1),
    _CcRadiusProxyRetryCount_Type()
)
ccRadiusProxyRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyRetryCount.setStatus("current")


class _CcRadiusProxyTimeout_Type(Integer32):
    """Custom type ccRadiusProxyTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 6),
    )


_CcRadiusProxyTimeout_Type.__name__ = "Integer32"
_CcRadiusProxyTimeout_Object = MibScalar
ccRadiusProxyTimeout = _CcRadiusProxyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 2),
    _CcRadiusProxyTimeout_Type()
)
ccRadiusProxyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccRadiusProxyTimeout.setUnits("seconds")
_CcRadiusProxyServerTable_Object = MibTable
ccRadiusProxyServerTable = _CcRadiusProxyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3)
)
if mibBuilder.loadTexts:
    ccRadiusProxyServerTable.setStatus("current")
_CcRadiusProxyServerEntry_Object = MibTableRow
ccRadiusProxyServerEntry = _CcRadiusProxyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1)
)
ccRadiusProxyServerEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadiusProxyServerIndex"),
)
if mibBuilder.loadTexts:
    ccRadiusProxyServerEntry.setStatus("current")


class _CcRadiusProxyServerIndex_Type(DisplayString):
    """Custom type ccRadiusProxyServerIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcRadiusProxyServerIndex_Type.__name__ = "DisplayString"
_CcRadiusProxyServerIndex_Object = MibTableColumn
ccRadiusProxyServerIndex = _CcRadiusProxyServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1, 1),
    _CcRadiusProxyServerIndex_Type()
)
ccRadiusProxyServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusProxyServerIndex.setStatus("current")


class _CcRadiusProxyServerPrefixOrSuffix_Type(DisplayString):
    """Custom type ccRadiusProxyServerPrefixOrSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CcRadiusProxyServerPrefixOrSuffix_Type.__name__ = "DisplayString"
_CcRadiusProxyServerPrefixOrSuffix_Object = MibTableColumn
ccRadiusProxyServerPrefixOrSuffix = _CcRadiusProxyServerPrefixOrSuffix_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1, 2),
    _CcRadiusProxyServerPrefixOrSuffix_Type()
)
ccRadiusProxyServerPrefixOrSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusProxyServerPrefixOrSuffix.setStatus("current")
_CcRadiusProxyServerIp_Type = IpAddress
_CcRadiusProxyServerIp_Object = MibTableColumn
ccRadiusProxyServerIp = _CcRadiusProxyServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1, 3),
    _CcRadiusProxyServerIp_Type()
)
ccRadiusProxyServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusProxyServerIp.setStatus("current")


class _CcRadiusProxyServerPort_Type(Integer32):
    """Custom type ccRadiusProxyServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcRadiusProxyServerPort_Type.__name__ = "Integer32"
_CcRadiusProxyServerPort_Object = MibTableColumn
ccRadiusProxyServerPort = _CcRadiusProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1, 4),
    _CcRadiusProxyServerPort_Type()
)
ccRadiusProxyServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusProxyServerPort.setStatus("current")


class _CcRadiusProxyServerSharedSecret_Type(DisplayString):
    """Custom type ccRadiusProxyServerSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadiusProxyServerSharedSecret_Type.__name__ = "DisplayString"
_CcRadiusProxyServerSharedSecret_Object = MibTableColumn
ccRadiusProxyServerSharedSecret = _CcRadiusProxyServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1, 5),
    _CcRadiusProxyServerSharedSecret_Type()
)
ccRadiusProxyServerSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusProxyServerSharedSecret.setStatus("current")
_CcRadiusProxyServerRowStatus_Type = AbbrevRowStatus
_CcRadiusProxyServerRowStatus_Object = MibTableColumn
ccRadiusProxyServerRowStatus = _CcRadiusProxyServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 2, 3, 1, 6),
    _CcRadiusProxyServerRowStatus_Type()
)
ccRadiusProxyServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusProxyServerRowStatus.setStatus("current")
_CcRadiusLdap_ObjectIdentity = ObjectIdentity
ccRadiusLdap = _CcRadiusLdap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3)
)
_CcRadiusLdap1Server_ObjectIdentity = ObjectIdentity
ccRadiusLdap1Server = _CcRadiusLdap1Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1)
)
_CcRadiusLdap1ServerIp_Type = IpAddress
_CcRadiusLdap1ServerIp_Object = MibScalar
ccRadiusLdap1ServerIp = _CcRadiusLdap1ServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 1),
    _CcRadiusLdap1ServerIp_Type()
)
ccRadiusLdap1ServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1ServerIp.setStatus("current")


class _CcRadiusLdap1ServerPort_Type(Integer32):
    """Custom type ccRadiusLdap1ServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcRadiusLdap1ServerPort_Type.__name__ = "Integer32"
_CcRadiusLdap1ServerPort_Object = MibScalar
ccRadiusLdap1ServerPort = _CcRadiusLdap1ServerPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 2),
    _CcRadiusLdap1ServerPort_Type()
)
ccRadiusLdap1ServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1ServerPort.setStatus("current")


class _CcRadiusLdap1LoginAttribute_Type(DisplayString):
    """Custom type ccRadiusLdap1LoginAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcRadiusLdap1LoginAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdap1LoginAttribute_Object = MibScalar
ccRadiusLdap1LoginAttribute = _CcRadiusLdap1LoginAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 3),
    _CcRadiusLdap1LoginAttribute_Type()
)
ccRadiusLdap1LoginAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1LoginAttribute.setStatus("current")


class _CcRadiusLdap1PasswordAttribute_Type(Password):
    """Custom type ccRadiusLdap1PasswordAttribute based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcRadiusLdap1PasswordAttribute_Type.__name__ = "Password"
_CcRadiusLdap1PasswordAttribute_Object = MibScalar
ccRadiusLdap1PasswordAttribute = _CcRadiusLdap1PasswordAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 4),
    _CcRadiusLdap1PasswordAttribute_Type()
)
ccRadiusLdap1PasswordAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1PasswordAttribute.setStatus("current")


class _CcRadiusLdap1BindDistinguishedName_Type(DisplayString):
    """Custom type ccRadiusLdap1BindDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcRadiusLdap1BindDistinguishedName_Type.__name__ = "DisplayString"
_CcRadiusLdap1BindDistinguishedName_Object = MibScalar
ccRadiusLdap1BindDistinguishedName = _CcRadiusLdap1BindDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 5),
    _CcRadiusLdap1BindDistinguishedName_Type()
)
ccRadiusLdap1BindDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1BindDistinguishedName.setStatus("current")


class _CcRadiusLdap1BindDistinguishedPassword_Type(Password):
    """Custom type ccRadiusLdap1BindDistinguishedPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadiusLdap1BindDistinguishedPassword_Type.__name__ = "Password"
_CcRadiusLdap1BindDistinguishedPassword_Object = MibScalar
ccRadiusLdap1BindDistinguishedPassword = _CcRadiusLdap1BindDistinguishedPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 6),
    _CcRadiusLdap1BindDistinguishedPassword_Type()
)
ccRadiusLdap1BindDistinguishedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1BindDistinguishedPassword.setStatus("current")


class _CcRadiusLdap1BaseDistinguishedName_Type(DisplayString):
    """Custom type ccRadiusLdap1BaseDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CcRadiusLdap1BaseDistinguishedName_Type.__name__ = "DisplayString"
_CcRadiusLdap1BaseDistinguishedName_Object = MibScalar
ccRadiusLdap1BaseDistinguishedName = _CcRadiusLdap1BaseDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 7),
    _CcRadiusLdap1BaseDistinguishedName_Type()
)
ccRadiusLdap1BaseDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1BaseDistinguishedName.setStatus("current")


class _CcRadiusLdap1GroupAttribute_Type(DisplayString):
    """Custom type ccRadiusLdap1GroupAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadiusLdap1GroupAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdap1GroupAttribute_Object = MibScalar
ccRadiusLdap1GroupAttribute = _CcRadiusLdap1GroupAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 8),
    _CcRadiusLdap1GroupAttribute_Type()
)
ccRadiusLdap1GroupAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1GroupAttribute.setStatus("current")


class _CcRadiusLdap1GroupFilter_Type(DisplayString):
    """Custom type ccRadiusLdap1GroupFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CcRadiusLdap1GroupFilter_Type.__name__ = "DisplayString"
_CcRadiusLdap1GroupFilter_Object = MibScalar
ccRadiusLdap1GroupFilter = _CcRadiusLdap1GroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 9),
    _CcRadiusLdap1GroupFilter_Type()
)
ccRadiusLdap1GroupFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1GroupFilter.setStatus("current")


class _CcRadiusLdap1GroupMembershipAttribute_Type(DisplayString):
    """Custom type ccRadiusLdap1GroupMembershipAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcRadiusLdap1GroupMembershipAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdap1GroupMembershipAttribute_Object = MibScalar
ccRadiusLdap1GroupMembershipAttribute = _CcRadiusLdap1GroupMembershipAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 1, 10),
    _CcRadiusLdap1GroupMembershipAttribute_Type()
)
ccRadiusLdap1GroupMembershipAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap1GroupMembershipAttribute.setStatus("current")
_CcRadiusLdap2Server_ObjectIdentity = ObjectIdentity
ccRadiusLdap2Server = _CcRadiusLdap2Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2)
)
_CcRadiusLdap2ServerIp_Type = DisplayString
_CcRadiusLdap2ServerIp_Object = MibScalar
ccRadiusLdap2ServerIp = _CcRadiusLdap2ServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 1),
    _CcRadiusLdap2ServerIp_Type()
)
ccRadiusLdap2ServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2ServerIp.setStatus("current")


class _CcRadiusLdap2ServerPort_Type(Integer32):
    """Custom type ccRadiusLdap2ServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CcRadiusLdap2ServerPort_Type.__name__ = "Integer32"
_CcRadiusLdap2ServerPort_Object = MibScalar
ccRadiusLdap2ServerPort = _CcRadiusLdap2ServerPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 2),
    _CcRadiusLdap2ServerPort_Type()
)
ccRadiusLdap2ServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2ServerPort.setStatus("current")


class _CcRadiusLdap2LoginAttribute_Type(DisplayString):
    """Custom type ccRadiusLdap2LoginAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcRadiusLdap2LoginAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdap2LoginAttribute_Object = MibScalar
ccRadiusLdap2LoginAttribute = _CcRadiusLdap2LoginAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 3),
    _CcRadiusLdap2LoginAttribute_Type()
)
ccRadiusLdap2LoginAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2LoginAttribute.setStatus("current")


class _CcRadiusLdap2PasswordATtribute_Type(Password):
    """Custom type ccRadiusLdap2PasswordATtribute based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcRadiusLdap2PasswordATtribute_Type.__name__ = "Password"
_CcRadiusLdap2PasswordATtribute_Object = MibScalar
ccRadiusLdap2PasswordATtribute = _CcRadiusLdap2PasswordATtribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 4),
    _CcRadiusLdap2PasswordATtribute_Type()
)
ccRadiusLdap2PasswordATtribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2PasswordATtribute.setStatus("current")


class _CcRadiusLdap2BindDistinguishedName_Type(DisplayString):
    """Custom type ccRadiusLdap2BindDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadiusLdap2BindDistinguishedName_Type.__name__ = "DisplayString"
_CcRadiusLdap2BindDistinguishedName_Object = MibScalar
ccRadiusLdap2BindDistinguishedName = _CcRadiusLdap2BindDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 5),
    _CcRadiusLdap2BindDistinguishedName_Type()
)
ccRadiusLdap2BindDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2BindDistinguishedName.setStatus("current")


class _CcRadiusLdap2BindDistinguishedPassword_Type(Password):
    """Custom type ccRadiusLdap2BindDistinguishedPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcRadiusLdap2BindDistinguishedPassword_Type.__name__ = "Password"
_CcRadiusLdap2BindDistinguishedPassword_Object = MibScalar
ccRadiusLdap2BindDistinguishedPassword = _CcRadiusLdap2BindDistinguishedPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 6),
    _CcRadiusLdap2BindDistinguishedPassword_Type()
)
ccRadiusLdap2BindDistinguishedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2BindDistinguishedPassword.setStatus("current")


class _CcRadiusLdap2BaseDistinguishedName_Type(DisplayString):
    """Custom type ccRadiusLdap2BaseDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadiusLdap2BaseDistinguishedName_Type.__name__ = "DisplayString"
_CcRadiusLdap2BaseDistinguishedName_Object = MibScalar
ccRadiusLdap2BaseDistinguishedName = _CcRadiusLdap2BaseDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 7),
    _CcRadiusLdap2BaseDistinguishedName_Type()
)
ccRadiusLdap2BaseDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2BaseDistinguishedName.setStatus("current")


class _CcRadiusLdap2GroupAttribute_Type(DisplayString):
    """Custom type ccRadiusLdap2GroupAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CcRadiusLdap2GroupAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdap2GroupAttribute_Object = MibScalar
ccRadiusLdap2GroupAttribute = _CcRadiusLdap2GroupAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 8),
    _CcRadiusLdap2GroupAttribute_Type()
)
ccRadiusLdap2GroupAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2GroupAttribute.setStatus("current")


class _CcRadiusLdap2GroupFilter_Type(DisplayString):
    """Custom type ccRadiusLdap2GroupFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadiusLdap2GroupFilter_Type.__name__ = "DisplayString"
_CcRadiusLdap2GroupFilter_Object = MibScalar
ccRadiusLdap2GroupFilter = _CcRadiusLdap2GroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 9),
    _CcRadiusLdap2GroupFilter_Type()
)
ccRadiusLdap2GroupFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2GroupFilter.setStatus("current")


class _CcRadiusLdap2GroupMembershipAttribute_Type(DisplayString):
    """Custom type ccRadiusLdap2GroupMembershipAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcRadiusLdap2GroupMembershipAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdap2GroupMembershipAttribute_Object = MibScalar
ccRadiusLdap2GroupMembershipAttribute = _CcRadiusLdap2GroupMembershipAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 3, 2, 10),
    _CcRadiusLdap2GroupMembershipAttribute_Type()
)
ccRadiusLdap2GroupMembershipAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdap2GroupMembershipAttribute.setStatus("current")
_CcRadiusUsers_ObjectIdentity = ObjectIdentity
ccRadiusUsers = _CcRadiusUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4)
)
_CcRadiusGroupsTable_Object = MibTable
ccRadiusGroupsTable = _CcRadiusGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 1)
)
if mibBuilder.loadTexts:
    ccRadiusGroupsTable.setStatus("current")
_CcRadiusGroupsEntry_Object = MibTableRow
ccRadiusGroupsEntry = _CcRadiusGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 1, 1)
)
ccRadiusGroupsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadiusGroup"),
)
if mibBuilder.loadTexts:
    ccRadiusGroupsEntry.setStatus("current")


class _CcRadiusGroup_Type(DisplayString):
    """Custom type ccRadiusGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CcRadiusGroup_Type.__name__ = "DisplayString"
_CcRadiusGroup_Object = MibTableColumn
ccRadiusGroup = _CcRadiusGroup_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 1, 1, 1),
    _CcRadiusGroup_Type()
)
ccRadiusGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusGroup.setStatus("current")
_CcRadiusGroupRowStatus_Type = AbbrevRowStatus
_CcRadiusGroupRowStatus_Object = MibTableColumn
ccRadiusGroupRowStatus = _CcRadiusGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 1, 1, 2),
    _CcRadiusGroupRowStatus_Type()
)
ccRadiusGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusGroupRowStatus.setStatus("current")
_CcRadiusUsersTable_Object = MibTable
ccRadiusUsersTable = _CcRadiusUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 2)
)
if mibBuilder.loadTexts:
    ccRadiusUsersTable.setStatus("current")
_CcRadiusUsersEntry_Object = MibTableRow
ccRadiusUsersEntry = _CcRadiusUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 2, 1)
)
ccRadiusUsersEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadiusUsersId"),
)
if mibBuilder.loadTexts:
    ccRadiusUsersEntry.setStatus("current")


class _CcRadiusUsersId_Type(DisplayString):
    """Custom type ccRadiusUsersId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcRadiusUsersId_Type.__name__ = "DisplayString"
_CcRadiusUsersId_Object = MibTableColumn
ccRadiusUsersId = _CcRadiusUsersId_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 2, 1, 1),
    _CcRadiusUsersId_Type()
)
ccRadiusUsersId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersId.setStatus("current")


class _CcRadiusUsersPassword_Type(Password):
    """Custom type ccRadiusUsersPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 64),
    )


_CcRadiusUsersPassword_Type.__name__ = "Password"
_CcRadiusUsersPassword_Object = MibTableColumn
ccRadiusUsersPassword = _CcRadiusUsersPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 2, 1, 2),
    _CcRadiusUsersPassword_Type()
)
ccRadiusUsersPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersPassword.setStatus("current")


class _CcRadiusUsersGroups_Type(Bits):
    """Custom type ccRadiusUsersGroups based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("g1", 1),
          ("g2", 2),
          ("g3", 3),
          ("g4", 4),
          ("g5", 5),
          ("g6", 6),
          ("g7", 7),
          ("g8", 8),
          ("g9", 9),
          ("g10", 10),
          ("g11", 11),
          ("g12", 12),
          ("g13", 13),
          ("g14", 14),
          ("g15", 15),
          ("g16", 16),
          ("g17", 17),
          ("g18", 18),
          ("g19", 19),
          ("g20", 20),
          ("g21", 21),
          ("g22", 22),
          ("g23", 23),
          ("g24", 24),
          ("g25", 25),
          ("g26", 26),
          ("g27", 27),
          ("g28", 28),
          ("g29", 29),
          ("g30", 30),
          ("g31", 31),
          ("g32", 32),
          ("g33", 33),
          ("g34", 34),
          ("g35", 35),
          ("g36", 36),
          ("g37", 37),
          ("g38", 38),
          ("g39", 39),
          ("g40", 40),
          ("g41", 41),
          ("g42", 42),
          ("g43", 43),
          ("g44", 44),
          ("g45", 45),
          ("g46", 46),
          ("g47", 47),
          ("g48", 48),
          ("g49", 49),
          ("g50", 50),
          ("g51", 51),
          ("g52", 52),
          ("g53", 53),
          ("g54", 54),
          ("g55", 55),
          ("g56", 56),
          ("g57", 57),
          ("g58", 58),
          ("g59", 59),
          ("g60", 60),
          ("g61", 61),
          ("g62", 62),
          ("g63", 63),
          ("g64", 64),
          ("g65", 65),
          ("g66", 66),
          ("g67", 67),
          ("g68", 68),
          ("g69", 69),
          ("g70", 70),
          ("g71", 71),
          ("g72", 72),
          ("g73", 73),
          ("g74", 74),
          ("g75", 75),
          ("g76", 76),
          ("g77", 77),
          ("g78", 78),
          ("g79", 79),
          ("g80", 80),
          ("g81", 81),
          ("g82", 82),
          ("g83", 83),
          ("g84", 84),
          ("g85", 85),
          ("g86", 86),
          ("g87", 87),
          ("g88", 88),
          ("g89", 89),
          ("g90", 90),
          ("g91", 91),
          ("g92", 92),
          ("g93", 93),
          ("g94", 94),
          ("g95", 95),
          ("g96", 96),
          ("g97", 97),
          ("g98", 98),
          ("g99", 99),
          ("g100", 100))
    )

_CcRadiusUsersGroups_Type.__name__ = "Bits"
_CcRadiusUsersGroups_Object = MibTableColumn
ccRadiusUsersGroups = _CcRadiusUsersGroups_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 2, 1, 3),
    _CcRadiusUsersGroups_Type()
)
ccRadiusUsersGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersGroups.setStatus("current")
_CcRadiusUsersRowStatus_Type = AbbrevRowStatus
_CcRadiusUsersRowStatus_Object = MibTableColumn
ccRadiusUsersRowStatus = _CcRadiusUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 4, 2, 1, 4),
    _CcRadiusUsersRowStatus_Type()
)
ccRadiusUsersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersRowStatus.setStatus("current")
_CcRadiusAccess_ObjectIdentity = ObjectIdentity
ccRadiusAccess = _CcRadiusAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 5)
)
_CcRadiusAccessTable_Object = MibTable
ccRadiusAccessTable = _CcRadiusAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 5, 1)
)
if mibBuilder.loadTexts:
    ccRadiusAccessTable.setStatus("current")
_CcRadiusAccessEntry_Object = MibTableRow
ccRadiusAccessEntry = _CcRadiusAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 5, 1, 1)
)
ccRadiusAccessEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadiusGroup"),
)
if mibBuilder.loadTexts:
    ccRadiusAccessEntry.setStatus("current")
_CcRadiusAccessGroupId_Type = DisplayString
_CcRadiusAccessGroupId_Object = MibTableColumn
ccRadiusAccessGroupId = _CcRadiusAccessGroupId_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 5, 1, 1, 1),
    _CcRadiusAccessGroupId_Type()
)
ccRadiusAccessGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadiusAccessGroupId.setStatus("current")


class _CcRadiusAccessWlanPtrs_Type(Bits):
    """Custom type ccRadiusAccessWlanPtrs based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("wlan1", 1),
          ("wlan2", 2),
          ("wlan3", 3),
          ("wlan4", 4),
          ("wlan5", 5),
          ("wlan6", 6),
          ("wlan7", 7),
          ("wlan8", 8),
          ("wlan9", 9),
          ("wlan10", 10),
          ("wlan11", 11),
          ("wlan12", 12),
          ("wlan13", 13),
          ("wlan14", 14),
          ("wlan15", 15),
          ("wlan16", 16),
          ("wlan17", 17),
          ("wlan18", 18),
          ("wlan19", 19),
          ("wlan20", 20),
          ("wlan21", 21),
          ("wlan22", 22),
          ("wlan23", 23),
          ("wlan24", 24),
          ("wlan25", 25),
          ("wlan26", 26),
          ("wlan27", 27),
          ("wlan28", 28),
          ("wlan29", 29),
          ("wlan30", 30),
          ("wlan31", 31),
          ("wlan32", 32),
          ("wlan33", 33),
          ("wlan34", 34),
          ("wlan35", 35),
          ("wlan36", 36),
          ("wlan37", 37),
          ("wlan38", 38),
          ("wlan39", 39),
          ("wlan40", 40),
          ("wlan41", 41),
          ("wlan42", 42),
          ("wlan43", 43),
          ("wlan44", 44),
          ("wlan45", 45),
          ("wlan46", 46),
          ("wlan47", 47),
          ("wlan48", 48),
          ("wlan49", 49),
          ("wlan50", 50),
          ("wlan51", 51),
          ("wlan52", 52),
          ("wlan53", 53),
          ("wlan54", 54),
          ("wlan55", 55),
          ("wlan56", 56),
          ("wlan57", 57),
          ("wlan58", 58),
          ("wlan59", 59),
          ("wlan60", 60),
          ("wlan61", 61),
          ("wlan62", 62),
          ("wlan63", 63),
          ("wlan64", 64),
          ("wlan65", 65),
          ("wlan66", 66),
          ("wlan67", 67),
          ("wlan68", 68),
          ("wlan69", 69),
          ("wlan70", 70),
          ("wlan71", 71),
          ("wlan72", 72),
          ("wlan73", 73),
          ("wlan74", 74),
          ("wlan75", 75),
          ("wlan76", 76),
          ("wlan77", 77),
          ("wlan78", 78),
          ("wlan79", 79),
          ("wlan80", 80))
    )

_CcRadiusAccessWlanPtrs_Type.__name__ = "Bits"
_CcRadiusAccessWlanPtrs_Object = MibTableColumn
ccRadiusAccessWlanPtrs = _CcRadiusAccessWlanPtrs_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 5, 1, 1, 2),
    _CcRadiusAccessWlanPtrs_Type()
)
ccRadiusAccessWlanPtrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAccessWlanPtrs.setStatus("current")
_CcRadiusAcct_ObjectIdentity = ObjectIdentity
ccRadiusAcct = _CcRadiusAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 6)
)
_CcRadiusAcctIPAddress_Type = IpAddress
_CcRadiusAcctIPAddress_Object = MibScalar
ccRadiusAcctIPAddress = _CcRadiusAcctIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 6, 1),
    _CcRadiusAcctIPAddress_Type()
)
ccRadiusAcctIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAcctIPAddress.setStatus("current")


class _CcRadiusAcctPort_Type(Integer32):
    """Custom type ccRadiusAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CcRadiusAcctPort_Type.__name__ = "Integer32"
_CcRadiusAcctPort_Object = MibScalar
ccRadiusAcctPort = _CcRadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 6, 2),
    _CcRadiusAcctPort_Type()
)
ccRadiusAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAcctPort.setStatus("current")


class _CcRadiusAcctTimeout_Type(Integer32):
    """Custom type ccRadiusAcctTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_CcRadiusAcctTimeout_Type.__name__ = "Integer32"
_CcRadiusAcctTimeout_Object = MibScalar
ccRadiusAcctTimeout = _CcRadiusAcctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 6, 3),
    _CcRadiusAcctTimeout_Type()
)
ccRadiusAcctTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAcctTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccRadiusAcctTimeout.setUnits("seconds")
_CcRadiusAcctMaxRetry_Type = Integer32
_CcRadiusAcctMaxRetry_Object = MibScalar
ccRadiusAcctMaxRetry = _CcRadiusAcctMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 6, 4),
    _CcRadiusAcctMaxRetry_Type()
)
ccRadiusAcctMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAcctMaxRetry.setStatus("current")
_CcRadiusAcctSharedSecret_Type = OctetString
_CcRadiusAcctSharedSecret_Object = MibScalar
ccRadiusAcctSharedSecret = _CcRadiusAcctSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 6, 5),
    _CcRadiusAcctSharedSecret_Type()
)
ccRadiusAcctSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAcctSharedSecret.setStatus("current")
_CcRadiusTimeRestriction_ObjectIdentity = ObjectIdentity
ccRadiusTimeRestriction = _CcRadiusTimeRestriction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 8)
)
_CcRadiusTimeRestrictionTable_Object = MibTable
ccRadiusTimeRestrictionTable = _CcRadiusTimeRestrictionTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 8, 1)
)
if mibBuilder.loadTexts:
    ccRadiusTimeRestrictionTable.setStatus("current")
_CcRadiusTimeRestrictionEntry_Object = MibTableRow
ccRadiusTimeRestrictionEntry = _CcRadiusTimeRestrictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 8, 1, 1)
)
ccRadiusTimeRestrictionEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRadiusGroup"),
)
if mibBuilder.loadTexts:
    ccRadiusTimeRestrictionEntry.setStatus("current")


class _CcRadiusTimeRestrictionStart_Type(DisplayString):
    """Custom type ccRadiusTimeRestrictionStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CcRadiusTimeRestrictionStart_Type.__name__ = "DisplayString"
_CcRadiusTimeRestrictionStart_Object = MibTableColumn
ccRadiusTimeRestrictionStart = _CcRadiusTimeRestrictionStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 8, 1, 1, 1),
    _CcRadiusTimeRestrictionStart_Type()
)
ccRadiusTimeRestrictionStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusTimeRestrictionStart.setStatus("current")


class _CcRadiusTimeRestrictionEnd_Type(DisplayString):
    """Custom type ccRadiusTimeRestrictionEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CcRadiusTimeRestrictionEnd_Type.__name__ = "DisplayString"
_CcRadiusTimeRestrictionEnd_Object = MibTableColumn
ccRadiusTimeRestrictionEnd = _CcRadiusTimeRestrictionEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 8, 1, 1, 2),
    _CcRadiusTimeRestrictionEnd_Type()
)
ccRadiusTimeRestrictionEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusTimeRestrictionEnd.setStatus("current")


class _CcRadiusTimeRestrictionDays_Type(DisplayString):
    """Custom type ccRadiusTimeRestrictionDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_CcRadiusTimeRestrictionDays_Type.__name__ = "DisplayString"
_CcRadiusTimeRestrictionDays_Object = MibTableColumn
ccRadiusTimeRestrictionDays = _CcRadiusTimeRestrictionDays_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 9, 8, 1, 1, 3),
    _CcRadiusTimeRestrictionDays_Type()
)
ccRadiusTimeRestrictionDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusTimeRestrictionDays.setStatus("current")
_CcRap_ObjectIdentity = ObjectIdentity
ccRap = _CcRap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10)
)
_CcRapControl_ObjectIdentity = ObjectIdentity
ccRapControl = _CcRapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1)
)
_CcRapControlPollSymbolMus_ObjectIdentity = ObjectIdentity
ccRapControlPollSymbolMus = _CcRapControlPollSymbolMus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 1)
)
_CcRapPollSymbolMusEnable_Type = TruthValue
_CcRapPollSymbolMusEnable_Object = MibScalar
ccRapPollSymbolMusEnable = _CcRapPollSymbolMusEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 1, 1),
    _CcRapPollSymbolMusEnable_Type()
)
ccRapPollSymbolMusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPollSymbolMusEnable.setStatus("current")
_CcRapPollSymbolMusInterval_Type = Integer32
_CcRapPollSymbolMusInterval_Object = MibScalar
ccRapPollSymbolMusInterval = _CcRapPollSymbolMusInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 1, 2),
    _CcRapPollSymbolMusInterval_Type()
)
ccRapPollSymbolMusInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPollSymbolMusInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRapPollSymbolMusInterval.setUnits("minutes")
_CcRapControlOnChannel_ObjectIdentity = ObjectIdentity
ccRapControlOnChannel = _CcRapControlOnChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 2)
)
_CcRapOnChannelEnable_Type = TruthValue
_CcRapOnChannelEnable_Object = MibScalar
ccRapOnChannelEnable = _CcRapOnChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 2, 1),
    _CcRapOnChannelEnable_Type()
)
ccRapOnChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapOnChannelEnable.setStatus("current")
_CcRapOnChannelInterval_Type = Integer32
_CcRapOnChannelInterval_Object = MibScalar
ccRapOnChannelInterval = _CcRapOnChannelInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 2, 2),
    _CcRapOnChannelInterval_Type()
)
ccRapOnChannelInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapOnChannelInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRapOnChannelInterval.setUnits("minutes")
_CcRapControlDetectors_ObjectIdentity = ObjectIdentity
ccRapControlDetectors = _CcRapControlDetectors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 3)
)
_CcRapDetectorsEnable_Type = TruthValue
_CcRapDetectorsEnable_Object = MibScalar
ccRapDetectorsEnable = _CcRapDetectorsEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 3, 1),
    _CcRapDetectorsEnable_Type()
)
ccRapDetectorsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapDetectorsEnable.setStatus("current")
_CcRapDetectorsInterval_Type = Integer32
_CcRapDetectorsInterval_Object = MibScalar
ccRapDetectorsInterval = _CcRapDetectorsInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 1, 3, 2),
    _CcRapDetectorsInterval_Type()
)
ccRapDetectorsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapDetectorsInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRapDetectorsInterval.setUnits("minutes")
_CcRapAuth_ObjectIdentity = ObjectIdentity
ccRapAuth = _CcRapAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2)
)
_CcRapAuthList_ObjectIdentity = ObjectIdentity
ccRapAuthList = _CcRapAuthList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1)
)
_CcRapAuthAllSymbolMac_Type = TruthValue
_CcRapAuthAllSymbolMac_Object = MibScalar
ccRapAuthAllSymbolMac = _CcRapAuthAllSymbolMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 1),
    _CcRapAuthAllSymbolMac_Type()
)
ccRapAuthAllSymbolMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthAllSymbolMac.setStatus("current")
_CcRapAuthTable_Object = MibTable
ccRapAuthTable = _CcRapAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ccRapAuthTable.setStatus("current")
_CcRapAuthEntry_Object = MibTableRow
ccRapAuthEntry = _CcRapAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 2, 1)
)
ccRapAuthEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRapAuthIndex"),
)
if mibBuilder.loadTexts:
    ccRapAuthEntry.setStatus("current")


class _CcRapAuthIndex_Type(Unsigned32):
    """Custom type ccRapAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CcRapAuthIndex_Type.__name__ = "Unsigned32"
_CcRapAuthIndex_Object = MibTableColumn
ccRapAuthIndex = _CcRapAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 2, 1, 1),
    _CcRapAuthIndex_Type()
)
ccRapAuthIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapAuthIndex.setStatus("current")
_CcRapAuthMacFilter_Type = DisplayString
_CcRapAuthMacFilter_Object = MibTableColumn
ccRapAuthMacFilter = _CcRapAuthMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 2, 1, 2),
    _CcRapAuthMacFilter_Type()
)
ccRapAuthMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthMacFilter.setStatus("current")
_CcRapAuthEssidFilter_Type = DisplayString
_CcRapAuthEssidFilter_Object = MibTableColumn
ccRapAuthEssidFilter = _CcRapAuthEssidFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 2, 1, 3),
    _CcRapAuthEssidFilter_Type()
)
ccRapAuthEssidFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthEssidFilter.setStatus("current")
_CcRapAuthRowExists_Type = TruthValue
_CcRapAuthRowExists_Object = MibTableColumn
ccRapAuthRowExists = _CcRapAuthRowExists_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 2, 1, 4),
    _CcRapAuthRowExists_Type()
)
ccRapAuthRowExists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthRowExists.setStatus("current")
_CcRapAuthErase_Type = DoActionNow
_CcRapAuthErase_Object = MibScalar
ccRapAuthErase = _CcRapAuthErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 3),
    _CcRapAuthErase_Type()
)
ccRapAuthErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthErase.setStatus("current")
_CcRapAuthCopyAllApproved_Type = DoActionNow
_CcRapAuthCopyAllApproved_Object = MibScalar
ccRapAuthCopyAllApproved = _CcRapAuthCopyAllApproved_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 4),
    _CcRapAuthCopyAllApproved_Type()
)
ccRapAuthCopyAllApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthCopyAllApproved.setStatus("current")
_CcRapAuthCopyAllRogue_Type = DoActionNow
_CcRapAuthCopyAllRogue_Object = MibScalar
ccRapAuthCopyAllRogue = _CcRapAuthCopyAllRogue_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 2, 1, 5),
    _CcRapAuthCopyAllRogue_Type()
)
ccRapAuthCopyAllRogue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthCopyAllRogue.setStatus("current")
_CcRapResults_ObjectIdentity = ObjectIdentity
ccRapResults = _CcRapResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3)
)
_CcRapResultsApproved_ObjectIdentity = ObjectIdentity
ccRapResultsApproved = _CcRapResultsApproved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1)
)
_CcRapResultsApprovedAgeOut_Type = Integer32
_CcRapResultsApprovedAgeOut_Object = MibScalar
ccRapResultsApprovedAgeOut = _CcRapResultsApprovedAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 1),
    _CcRapResultsApprovedAgeOut_Type()
)
ccRapResultsApprovedAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedAgeOut.setStatus("current")
if mibBuilder.loadTexts:
    ccRapResultsApprovedAgeOut.setUnits("minutes")
_CcRapResultsApprovedTable_Object = MibTable
ccRapResultsApprovedTable = _CcRapResultsApprovedTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccRapResultsApprovedTable.setStatus("current")
_CcRapResultsApprovedEntry_Object = MibTableRow
ccRapResultsApprovedEntry = _CcRapResultsApprovedEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1)
)
ccRapResultsApprovedEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRapResultsApprovedIndex"),
)
if mibBuilder.loadTexts:
    ccRapResultsApprovedEntry.setStatus("current")


class _CcRapResultsApprovedIndex_Type(Unsigned32):
    """Custom type ccRapResultsApprovedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcRapResultsApprovedIndex_Type.__name__ = "Unsigned32"
_CcRapResultsApprovedIndex_Object = MibTableColumn
ccRapResultsApprovedIndex = _CcRapResultsApprovedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 1),
    _CcRapResultsApprovedIndex_Type()
)
ccRapResultsApprovedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapResultsApprovedIndex.setStatus("current")
_CcRapResultsApprovedApMac_Type = DisplayString
_CcRapResultsApprovedApMac_Object = MibTableColumn
ccRapResultsApprovedApMac = _CcRapResultsApprovedApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 2),
    _CcRapResultsApprovedApMac_Type()
)
ccRapResultsApprovedApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedApMac.setStatus("current")
_CcRapResultsApprovedEssid_Type = DisplayString
_CcRapResultsApprovedEssid_Object = MibTableColumn
ccRapResultsApprovedEssid = _CcRapResultsApprovedEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 3),
    _CcRapResultsApprovedEssid_Type()
)
ccRapResultsApprovedEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedEssid.setStatus("current")
_CcRapResultsApprovedCopyToAuthTable_Type = DoActionNow
_CcRapResultsApprovedCopyToAuthTable_Object = MibTableColumn
ccRapResultsApprovedCopyToAuthTable = _CcRapResultsApprovedCopyToAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 4),
    _CcRapResultsApprovedCopyToAuthTable_Type()
)
ccRapResultsApprovedCopyToAuthTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedCopyToAuthTable.setStatus("current")
_CcRapResultsApprovedFirstHeard_Type = DisplayString
_CcRapResultsApprovedFirstHeard_Object = MibTableColumn
ccRapResultsApprovedFirstHeard = _CcRapResultsApprovedFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 5),
    _CcRapResultsApprovedFirstHeard_Type()
)
ccRapResultsApprovedFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedFirstHeard.setStatus("current")
_CcRapResultsApprovedLastHeard_Type = DisplayString
_CcRapResultsApprovedLastHeard_Object = MibTableColumn
ccRapResultsApprovedLastHeard = _CcRapResultsApprovedLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 6),
    _CcRapResultsApprovedLastHeard_Type()
)
ccRapResultsApprovedLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedLastHeard.setStatus("current")
_CcRapResultsApprovedPortalPtr_Type = MultiPointer255
_CcRapResultsApprovedPortalPtr_Object = MibTableColumn
ccRapResultsApprovedPortalPtr = _CcRapResultsApprovedPortalPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 7),
    _CcRapResultsApprovedPortalPtr_Type()
)
ccRapResultsApprovedPortalPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedPortalPtr.setStatus("current")
_CcRapResultsApprovedHowFound_Type = DisplayString
_CcRapResultsApprovedHowFound_Object = MibTableColumn
ccRapResultsApprovedHowFound = _CcRapResultsApprovedHowFound_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 8),
    _CcRapResultsApprovedHowFound_Type()
)
ccRapResultsApprovedHowFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedHowFound.setStatus("current")
_CcRapResultsApprovedHowAuth_Type = DisplayString
_CcRapResultsApprovedHowAuth_Object = MibTableColumn
ccRapResultsApprovedHowAuth = _CcRapResultsApprovedHowAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 9),
    _CcRapResultsApprovedHowAuth_Type()
)
ccRapResultsApprovedHowAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedHowAuth.setStatus("current")
_CcRapResultsApprovedRowErase_Type = DoActionNow
_CcRapResultsApprovedRowErase_Object = MibTableColumn
ccRapResultsApprovedRowErase = _CcRapResultsApprovedRowErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 2, 1, 10),
    _CcRapResultsApprovedRowErase_Type()
)
ccRapResultsApprovedRowErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedRowErase.setStatus("current")
_CcRapResultsApprovedErase_Type = DoActionNow
_CcRapResultsApprovedErase_Object = MibScalar
ccRapResultsApprovedErase = _CcRapResultsApprovedErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 1, 3),
    _CcRapResultsApprovedErase_Type()
)
ccRapResultsApprovedErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedErase.setStatus("current")
_CcRapResultsRogue_ObjectIdentity = ObjectIdentity
ccRapResultsRogue = _CcRapResultsRogue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2)
)
_CcRapResultsRogueAgeOut_Type = Integer32
_CcRapResultsRogueAgeOut_Object = MibScalar
ccRapResultsRogueAgeOut = _CcRapResultsRogueAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 1),
    _CcRapResultsRogueAgeOut_Type()
)
ccRapResultsRogueAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsRogueAgeOut.setStatus("current")
if mibBuilder.loadTexts:
    ccRapResultsRogueAgeOut.setUnits("minutes")
_CcRapResultsRogueTable_Object = MibTable
ccRapResultsRogueTable = _CcRapResultsRogueTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ccRapResultsRogueTable.setStatus("current")
_CcRapResultsRogueEntry_Object = MibTableRow
ccRapResultsRogueEntry = _CcRapResultsRogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1)
)
ccRapResultsRogueEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRapResultsRogueIndex"),
)
if mibBuilder.loadTexts:
    ccRapResultsRogueEntry.setStatus("current")


class _CcRapResultsRogueIndex_Type(Unsigned32):
    """Custom type ccRapResultsRogueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcRapResultsRogueIndex_Type.__name__ = "Unsigned32"
_CcRapResultsRogueIndex_Object = MibTableColumn
ccRapResultsRogueIndex = _CcRapResultsRogueIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 1),
    _CcRapResultsRogueIndex_Type()
)
ccRapResultsRogueIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapResultsRogueIndex.setStatus("current")
_CcRapResultsRogueApMac_Type = DisplayString
_CcRapResultsRogueApMac_Object = MibTableColumn
ccRapResultsRogueApMac = _CcRapResultsRogueApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 2),
    _CcRapResultsRogueApMac_Type()
)
ccRapResultsRogueApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueApMac.setStatus("current")
_CcRapResultsRogueEssid_Type = DisplayString
_CcRapResultsRogueEssid_Object = MibTableColumn
ccRapResultsRogueEssid = _CcRapResultsRogueEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 3),
    _CcRapResultsRogueEssid_Type()
)
ccRapResultsRogueEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueEssid.setStatus("current")
_CcRapResultsRogueCopyToAuthTable_Type = DoActionNow
_CcRapResultsRogueCopyToAuthTable_Object = MibTableColumn
ccRapResultsRogueCopyToAuthTable = _CcRapResultsRogueCopyToAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 4),
    _CcRapResultsRogueCopyToAuthTable_Type()
)
ccRapResultsRogueCopyToAuthTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsRogueCopyToAuthTable.setStatus("current")
_CcRapResultsRogueFirstHeard_Type = DisplayString
_CcRapResultsRogueFirstHeard_Object = MibTableColumn
ccRapResultsRogueFirstHeard = _CcRapResultsRogueFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 5),
    _CcRapResultsRogueFirstHeard_Type()
)
ccRapResultsRogueFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueFirstHeard.setStatus("current")
_CcRapResultsRogueLastHeard_Type = DisplayString
_CcRapResultsRogueLastHeard_Object = MibTableColumn
ccRapResultsRogueLastHeard = _CcRapResultsRogueLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 6),
    _CcRapResultsRogueLastHeard_Type()
)
ccRapResultsRogueLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueLastHeard.setStatus("current")
_CcRapResultsRoguePortalPtr_Type = MultiPointer255
_CcRapResultsRoguePortalPtr_Object = MibTableColumn
ccRapResultsRoguePortalPtr = _CcRapResultsRoguePortalPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 7),
    _CcRapResultsRoguePortalPtr_Type()
)
ccRapResultsRoguePortalPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRoguePortalPtr.setStatus("current")
_CcRapResultsRogueHowFound_Type = DisplayString
_CcRapResultsRogueHowFound_Object = MibTableColumn
ccRapResultsRogueHowFound = _CcRapResultsRogueHowFound_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 8),
    _CcRapResultsRogueHowFound_Type()
)
ccRapResultsRogueHowFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueHowFound.setStatus("current")
_CcRapResultsRogueClosestPortalPtr_Type = DisplayString
_CcRapResultsRogueClosestPortalPtr_Object = MibTableColumn
ccRapResultsRogueClosestPortalPtr = _CcRapResultsRogueClosestPortalPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 9),
    _CcRapResultsRogueClosestPortalPtr_Type()
)
ccRapResultsRogueClosestPortalPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueClosestPortalPtr.setStatus("current")
_CcRapResultsRogueClosestPortalRssi_Type = Integer32
_CcRapResultsRogueClosestPortalRssi_Object = MibTableColumn
ccRapResultsRogueClosestPortalRssi = _CcRapResultsRogueClosestPortalRssi_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 2, 1, 10),
    _CcRapResultsRogueClosestPortalRssi_Type()
)
ccRapResultsRogueClosestPortalRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueClosestPortalRssi.setStatus("current")
_CcRapResultsRogueErase_Type = DoActionNow
_CcRapResultsRogueErase_Object = MibScalar
ccRapResultsRogueErase = _CcRapResultsRogueErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 10, 3, 2, 3),
    _CcRapResultsRogueErase_Type()
)
ccRapResultsRogueErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsRogueErase.setStatus("current")
_CcImageDload_ObjectIdentity = ObjectIdentity
ccImageDload = _CcImageDload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 11)
)
_CcRestore_Type = DisplayString
_CcRestore_Object = MibScalar
ccRestore = _CcRestore_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 11, 1),
    _CcRestore_Type()
)
ccRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRestore.setStatus("current")
_CcFtp_Type = DisplayString
_CcFtp_Object = MibScalar
ccFtp = _CcFtp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 11, 2),
    _CcFtp_Type()
)
ccFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccFtp.setStatus("current")
_CcTftp_Type = DisplayString
_CcTftp_Object = MibScalar
ccTftp = _CcTftp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 11, 3),
    _CcTftp_Type()
)
ccTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTftp.setStatus("current")
_CcListFiles_Type = DisplayString
_CcListFiles_Object = MibScalar
ccListFiles = _CcListFiles_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 11, 4),
    _CcListFiles_Type()
)
ccListFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccListFiles.setStatus("current")
_CcDeleteFiles_Type = DisplayString
_CcDeleteFiles_Object = MibScalar
ccDeleteFiles = _CcDeleteFiles_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 11, 5),
    _CcDeleteFiles_Type()
)
ccDeleteFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDeleteFiles.setStatus("current")
_CcRFStatistics_ObjectIdentity = ObjectIdentity
ccRFStatistics = _CcRFStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 16)
)
_CcAp_ObjectIdentity = ObjectIdentity
ccAp = _CcAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1)
)
_CcApTable_Object = MibTable
ccApTable = _CcApTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1)
)
if mibBuilder.loadTexts:
    ccApTable.setStatus("current")
_CcApEntry_Object = MibTableRow
ccApEntry = _CcApEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1)
)
ccApEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccApIndex"),
)
if mibBuilder.loadTexts:
    ccApEntry.setStatus("current")


class _CcApIndex_Type(Integer32):
    """Custom type ccApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcApIndex_Type.__name__ = "Integer32"
_CcApIndex_Object = MibTableColumn
ccApIndex = _CcApIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 1),
    _CcApIndex_Type()
)
ccApIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccApIndex.setStatus("current")
_CcApNicMac_Type = DisplayString
_CcApNicMac_Object = MibTableColumn
ccApNicMac = _CcApNicMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 2),
    _CcApNicMac_Type()
)
ccApNicMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApNicMac.setStatus("current")
_CcApModelNumber_Type = DisplayString
_CcApModelNumber_Object = MibTableColumn
ccApModelNumber = _CcApModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 3),
    _CcApModelNumber_Type()
)
ccApModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApModelNumber.setStatus("current")
_CcApSerialNumber_Type = DisplayString
_CcApSerialNumber_Object = MibTableColumn
ccApSerialNumber = _CcApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 4),
    _CcApSerialNumber_Type()
)
ccApSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApSerialNumber.setStatus("current")
_CcApPcbRevision_Type = DisplayString
_CcApPcbRevision_Object = MibTableColumn
ccApPcbRevision = _CcApPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 5),
    _CcApPcbRevision_Type()
)
ccApPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApPcbRevision.setStatus("current")
_CcApBootLoaderRev_Type = DisplayString
_CcApBootLoaderRev_Object = MibTableColumn
ccApBootLoaderRev = _CcApBootLoaderRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 6),
    _CcApBootLoaderRev_Type()
)
ccApBootLoaderRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApBootLoaderRev.setStatus("current")
_CcApWispVersion_Type = DisplayString
_CcApWispVersion_Object = MibTableColumn
ccApWispVersion = _CcApWispVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 7),
    _CcApWispVersion_Type()
)
ccApWispVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApWispVersion.setStatus("current")
_CcApRuntimeFwVersion_Type = DisplayString
_CcApRuntimeFwVersion_Object = MibTableColumn
ccApRuntimeFwVersion = _CcApRuntimeFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 8),
    _CcApRuntimeFwVersion_Type()
)
ccApRuntimeFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApRuntimeFwVersion.setStatus("current")
_CcApNumPortals_Type = Unsigned32
_CcApNumPortals_Object = MibTableColumn
ccApNumPortals = _CcApNumPortals_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 9),
    _CcApNumPortals_Type()
)
ccApNumPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApNumPortals.setStatus("current")
_CcApPointersToPortals_Type = MultiPointer255
_CcApPointersToPortals_Object = MibTableColumn
ccApPointersToPortals = _CcApPointersToPortals_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 1, 1, 1, 10),
    _CcApPointersToPortals_Type()
)
ccApPointersToPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApPointersToPortals.setStatus("current")
_CcPortal_ObjectIdentity = ObjectIdentity
ccPortal = _CcPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2)
)
_CcPortalTable_Object = MibTable
ccPortalTable = _CcPortalTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    ccPortalTable.setStatus("current")
_CcPortalEntry_Object = MibTableRow
ccPortalEntry = _CcPortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1)
)
ccPortalEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalEntry.setStatus("current")


class _CcPortalIndex_Type(Integer32):
    """Custom type ccPortalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcPortalIndex_Type.__name__ = "Integer32"
_CcPortalIndex_Object = MibTableColumn
ccPortalIndex = _CcPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 1),
    _CcPortalIndex_Type()
)
ccPortalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccPortalIndex.setStatus("current")
_CcPortalPointerToAp_Type = SinglePointer
_CcPortalPointerToAp_Object = MibTableColumn
ccPortalPointerToAp = _CcPortalPointerToAp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 2),
    _CcPortalPointerToAp_Type()
)
ccPortalPointerToAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalPointerToAp.setStatus("current")
_CcPortalPointersToWlans_Type = MultiPointer63
_CcPortalPointersToWlans_Object = MibTableColumn
ccPortalPointersToWlans = _CcPortalPointersToWlans_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 3),
    _CcPortalPointersToWlans_Type()
)
ccPortalPointersToWlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalPointersToWlans.setStatus("current")
_CcPortalName_Type = DisplayString
_CcPortalName_Object = MibTableColumn
ccPortalName = _CcPortalName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 4),
    _CcPortalName_Type()
)
ccPortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalName.setStatus("current")
_CcPortalLocation_Type = DisplayString
_CcPortalLocation_Object = MibTableColumn
ccPortalLocation = _CcPortalLocation_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 5),
    _CcPortalLocation_Type()
)
ccPortalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLocation.setStatus("current")


class _CcPortalOptions_Type(Bits):
    """Custom type ccPortalOptions based on Bits"""
    namedValues = NamedValues(
        *(("undefined00", 0),
          ("undefined01", 1),
          ("undefined02", 2),
          ("undefined03", 3),
          ("undefined04", 4),
          ("undefined05", 5),
          ("undefined06", 6),
          ("undefined07", 7),
          ("undefined08", 8),
          ("undefined09", 9),
          ("undefined10", 10),
          ("undefined11", 11),
          ("externalSecondaryAntInstalled", 12),
          ("internalSecondaryAntInstalled", 13),
          ("externalPrimaryAntInstalled", 14),
          ("internalPrimaryAntInstalled", 15))
    )

_CcPortalOptions_Type.__name__ = "Bits"
_CcPortalOptions_Object = MibTableColumn
ccPortalOptions = _CcPortalOptions_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 6),
    _CcPortalOptions_Type()
)
ccPortalOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalOptions.setStatus("current")
_CcPortalMac_Type = DisplayString
_CcPortalMac_Object = MibTableColumn
ccPortalMac = _CcPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 7),
    _CcPortalMac_Type()
)
ccPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalMac.setStatus("current")
_CcPortalNumberofEss_Type = Integer32
_CcPortalNumberofEss_Object = MibTableColumn
ccPortalNumberofEss = _CcPortalNumberofEss_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 8),
    _CcPortalNumberofEss_Type()
)
ccPortalNumberofEss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalNumberofEss.setStatus("current")
_CcPortalNumberOfBss_Type = Integer32
_CcPortalNumberOfBss_Object = MibTableColumn
ccPortalNumberOfBss = _CcPortalNumberOfBss_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 9),
    _CcPortalNumberOfBss_Type()
)
ccPortalNumberOfBss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalNumberOfBss.setStatus("current")
_CcPortalAssociatedMus_Type = Integer32
_CcPortalAssociatedMus_Object = MibTableColumn
ccPortalAssociatedMus = _CcPortalAssociatedMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 10),
    _CcPortalAssociatedMus_Type()
)
ccPortalAssociatedMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalAssociatedMus.setStatus("current")
_CcPortalRadioType_Type = RadioType
_CcPortalRadioType_Object = MibTableColumn
ccPortalRadioType = _CcPortalRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 11),
    _CcPortalRadioType_Type()
)
ccPortalRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRadioType.setStatus("current")


class _CcPortalChannel_Type(Integer32):
    """Custom type ccPortalChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11bChannel01", 1),
          ("ieee802dot11bChannel02", 2),
          ("ieee802dot11bChannel03", 3),
          ("ieee802dot11bChannel04", 4),
          ("ieee802dot11bChannel05", 5),
          ("ieee802dot11bChannel06", 6),
          ("ieee802dot11bChannel07", 7),
          ("ieee802dot11bChannel08", 8),
          ("ieee802dot11bChannel09", 9),
          ("ieee802dot11bChannel10", 10),
          ("ieee802dot11bChannel11", 11),
          ("ieee802dot11bChannel12", 12),
          ("ieee802dot11bChannel13", 13),
          ("ieee802dot11bChannel14", 14),
          ("ieee802dot11aChannel036", 36),
          ("ieee802dot11aChannel040", 40),
          ("ieee802dot11aChannel044", 44),
          ("ieee802dot11aChannel048", 48),
          ("ieee802dot11aChannel052", 52),
          ("ieee802dot11aChannel056", 56),
          ("ieee802dot11aChannel060", 60),
          ("ieee802dot11aChannel064", 64),
          ("ieee802dot11aChannel149", 149),
          ("ieee802dot11aChannel153", 153),
          ("ieee802dot11aChannel157", 157),
          ("ieee802dot11aChannel161", 161))
    )


_CcPortalChannel_Type.__name__ = "Integer32"
_CcPortalChannel_Object = MibTableColumn
ccPortalChannel = _CcPortalChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 12),
    _CcPortalChannel_Type()
)
ccPortalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalChannel.setStatus("current")


class _CcPortalTxPowerLevel_Type(Integer32):
    """Custom type ccPortalTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcPortalTxPowerLevel_Type.__name__ = "Integer32"
_CcPortalTxPowerLevel_Object = MibTableColumn
ccPortalTxPowerLevel = _CcPortalTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 13),
    _CcPortalTxPowerLevel_Type()
)
ccPortalTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalTxPowerLevel.setUnits("milli-Watts")
_CcPortalLastAdoption_Type = TimeTicks
_CcPortalLastAdoption_Object = MibTableColumn
ccPortalLastAdoption = _CcPortalLastAdoption_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 14),
    _CcPortalLastAdoption_Type()
)
ccPortalLastAdoption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastAdoption.setStatus("current")


class _CcPortalState_Type(Integer32):
    """Custom type ccPortalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("active", 1),
          ("alert", 3),
          ("reset", 4))
    )


_CcPortalState_Type.__name__ = "Integer32"
_CcPortalState_Object = MibTableColumn
ccPortalState = _CcPortalState_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 15),
    _CcPortalState_Type()
)
ccPortalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalState.setStatus("current")
_CcPortalBackgroundNoiseNumSamples_Type = Counter32
_CcPortalBackgroundNoiseNumSamples_Object = MibTableColumn
ccPortalBackgroundNoiseNumSamples = _CcPortalBackgroundNoiseNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 16),
    _CcPortalBackgroundNoiseNumSamples_Type()
)
ccPortalBackgroundNoiseNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseNumSamples.setStatus("current")
_CcPortalBackgroundNoiseBest_Type = Integer32
_CcPortalBackgroundNoiseBest_Object = MibTableColumn
ccPortalBackgroundNoiseBest = _CcPortalBackgroundNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 17),
    _CcPortalBackgroundNoiseBest_Type()
)
ccPortalBackgroundNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseBest.setUnits("dBm")
_CcPortalBackgroundNoiseWorst_Type = Integer32
_CcPortalBackgroundNoiseWorst_Object = MibTableColumn
ccPortalBackgroundNoiseWorst = _CcPortalBackgroundNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 18),
    _CcPortalBackgroundNoiseWorst_Type()
)
ccPortalBackgroundNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseWorst.setUnits("dBm")
_CcPortalBackgroundNoiseSum_Type = Integer32
_CcPortalBackgroundNoiseSum_Object = MibTableColumn
ccPortalBackgroundNoiseSum = _CcPortalBackgroundNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 19),
    _CcPortalBackgroundNoiseSum_Type()
)
ccPortalBackgroundNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSum.setUnits("dBm")
_CcPortalBackgroundNoiseSumSquares_Type = Counter64
_CcPortalBackgroundNoiseSumSquares_Object = MibTableColumn
ccPortalBackgroundNoiseSumSquares = _CcPortalBackgroundNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 1, 1, 20),
    _CcPortalBackgroundNoiseSumSquares_Type()
)
ccPortalBackgroundNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSumSquares.setUnits("dBm")
_CcPortalLastMac_Type = DisplayString
_CcPortalLastMac_Object = MibScalar
ccPortalLastMac = _CcPortalLastMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 2),
    _CcPortalLastMac_Type()
)
ccPortalLastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastMac.setStatus("current")


class _CcPortalLastReason_Type(Integer32):
    """Custom type ccPortalLastReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("aclViolation", 2),
          ("timeout", 3))
    )


_CcPortalLastReason_Type.__name__ = "Integer32"
_CcPortalLastReason_Object = MibScalar
ccPortalLastReason = _CcPortalLastReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 3),
    _CcPortalLastReason_Type()
)
ccPortalLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastReason.setStatus("current")
_CcPortalSystemStatsTable_Object = MibTable
ccPortalSystemStatsTable = _CcPortalSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5)
)
if mibBuilder.loadTexts:
    ccPortalSystemStatsTable.setStatus("current")
_CcPortalSystemStatsEntry_Object = MibTableRow
ccPortalSystemStatsEntry = _CcPortalSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1)
)
ccPortalSystemStatsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSystemStatsEntry.setStatus("current")
_CcPortalSystemStatsBeaconTx_Type = Integer32
_CcPortalSystemStatsBeaconTx_Object = MibTableColumn
ccPortalSystemStatsBeaconTx = _CcPortalSystemStatsBeaconTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 1),
    _CcPortalSystemStatsBeaconTx_Type()
)
ccPortalSystemStatsBeaconTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsBeaconTx.setStatus("current")
_CcPortalSystemStatsBeaconsTxOctets_Type = Unsigned32
_CcPortalSystemStatsBeaconsTxOctets_Object = MibTableColumn
ccPortalSystemStatsBeaconsTxOctets = _CcPortalSystemStatsBeaconsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 2),
    _CcPortalSystemStatsBeaconsTxOctets_Type()
)
ccPortalSystemStatsBeaconsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsBeaconsTxOctets.setStatus("current")
_CcPortalSystemStatsProbeReqRx_Type = Unsigned32
_CcPortalSystemStatsProbeReqRx_Object = MibTableColumn
ccPortalSystemStatsProbeReqRx = _CcPortalSystemStatsProbeReqRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 3),
    _CcPortalSystemStatsProbeReqRx_Type()
)
ccPortalSystemStatsProbeReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeReqRx.setStatus("current")
_CcPortalSystemStatsProbeReqRxOctets_Type = Unsigned32
_CcPortalSystemStatsProbeReqRxOctets_Object = MibTableColumn
ccPortalSystemStatsProbeReqRxOctets = _CcPortalSystemStatsProbeReqRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 4),
    _CcPortalSystemStatsProbeReqRxOctets_Type()
)
ccPortalSystemStatsProbeReqRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeReqRxOctets.setStatus("current")
_CcPortalSystemStatsProbeRespRetriesNone_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetriesNone_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetriesNone = _CcPortalSystemStatsProbeRespRetriesNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 5),
    _CcPortalSystemStatsProbeRespRetriesNone_Type()
)
ccPortalSystemStatsProbeRespRetriesNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetriesNone.setStatus("current")
_CcPortalSystemStatsProbeRespRetries1_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetries1_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetries1 = _CcPortalSystemStatsProbeRespRetries1_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 6),
    _CcPortalSystemStatsProbeRespRetries1_Type()
)
ccPortalSystemStatsProbeRespRetries1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetries1.setStatus("current")
_CcPortalSystemStatsProbeRespRetries2_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetries2_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetries2 = _CcPortalSystemStatsProbeRespRetries2_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 7),
    _CcPortalSystemStatsProbeRespRetries2_Type()
)
ccPortalSystemStatsProbeRespRetries2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetries2.setStatus("current")
_CcPortalSystemStatsProbeRespRetries3OrMore_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetries3OrMore_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetries3OrMore = _CcPortalSystemStatsProbeRespRetries3OrMore_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 8),
    _CcPortalSystemStatsProbeRespRetries3OrMore_Type()
)
ccPortalSystemStatsProbeRespRetries3OrMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetries3OrMore.setStatus("current")
_CcPortalSystemStatsProbeRespRetriesFailed_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetriesFailed_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetriesFailed = _CcPortalSystemStatsProbeRespRetriesFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 9),
    _CcPortalSystemStatsProbeRespRetriesFailed_Type()
)
ccPortalSystemStatsProbeRespRetriesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetriesFailed.setStatus("current")
_CcPortalSystemStatsProbeRespTxOctets_Type = Unsigned32
_CcPortalSystemStatsProbeRespTxOctets_Object = MibTableColumn
ccPortalSystemStatsProbeRespTxOctets = _CcPortalSystemStatsProbeRespTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 5, 1, 10),
    _CcPortalSystemStatsProbeRespTxOctets_Type()
)
ccPortalSystemStatsProbeRespTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespTxOctets.setStatus("current")
_CcPortalRfSum_ObjectIdentity = ObjectIdentity
ccPortalRfSum = _CcPortalRfSum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6)
)
_CcPortalStatsTable_Object = MibTable
ccPortalStatsTable = _CcPortalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ccPortalStatsTable.setStatus("current")
_CcPortalStatsEntry_Object = MibTableRow
ccPortalStatsEntry = _CcPortalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1)
)
ccPortalStatsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalStatsEntry.setStatus("current")
_CcPortalTxPktsUcast_Type = Counter32
_CcPortalTxPktsUcast_Object = MibTableColumn
ccPortalTxPktsUcast = _CcPortalTxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 1),
    _CcPortalTxPktsUcast_Type()
)
ccPortalTxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsUcast.setStatus("current")
_CcPortalRxPktsUcast_Type = Counter32
_CcPortalRxPktsUcast_Object = MibTableColumn
ccPortalRxPktsUcast = _CcPortalRxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 2),
    _CcPortalRxPktsUcast_Type()
)
ccPortalRxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsUcast.setStatus("current")
_CcPortalRxPktsNUcast_Type = Counter32
_CcPortalRxPktsNUcast_Object = MibTableColumn
ccPortalRxPktsNUcast = _CcPortalRxPktsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 3),
    _CcPortalRxPktsNUcast_Type()
)
ccPortalRxPktsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsNUcast.setStatus("current")
_CcPortalTxOctetsUcast_Type = Counter32
_CcPortalTxOctetsUcast_Object = MibTableColumn
ccPortalTxOctetsUcast = _CcPortalTxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 4),
    _CcPortalTxOctetsUcast_Type()
)
ccPortalTxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsUcast.setStatus("current")
_CcPortalRxOctetsUcast_Type = Counter32
_CcPortalRxOctetsUcast_Object = MibTableColumn
ccPortalRxOctetsUcast = _CcPortalRxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 5),
    _CcPortalRxOctetsUcast_Type()
)
ccPortalRxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsUcast.setStatus("current")
_CcPortalRxOctetsNUcast_Type = Counter32
_CcPortalRxOctetsNUcast_Object = MibTableColumn
ccPortalRxOctetsNUcast = _CcPortalRxOctetsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 6),
    _CcPortalRxOctetsNUcast_Type()
)
ccPortalRxOctetsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsNUcast.setStatus("current")
_CcPortalRxUndecryptablePkts_Type = Counter32
_CcPortalRxUndecryptablePkts_Object = MibTableColumn
ccPortalRxUndecryptablePkts = _CcPortalRxUndecryptablePkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 7),
    _CcPortalRxUndecryptablePkts_Type()
)
ccPortalRxUndecryptablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxUndecryptablePkts.setStatus("current")
_CcPortalLastActivity_Type = TimeTicks
_CcPortalLastActivity_Object = MibTableColumn
ccPortalLastActivity = _CcPortalLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 1, 1, 8),
    _CcPortalLastActivity_Type()
)
ccPortalLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastActivity.setStatus("current")
_CcPortalRxPktsTable_Object = MibTable
ccPortalRxPktsTable = _CcPortalRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2)
)
if mibBuilder.loadTexts:
    ccPortalRxPktsTable.setStatus("current")
_CcPortalRxPktsEntry_Object = MibTableRow
ccPortalRxPktsEntry = _CcPortalRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1)
)
ccPortalRxPktsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalRxPktsEntry.setStatus("current")
_CcPortalRxPktsAt1Mb_Type = Counter32
_CcPortalRxPktsAt1Mb_Object = MibTableColumn
ccPortalRxPktsAt1Mb = _CcPortalRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 1),
    _CcPortalRxPktsAt1Mb_Type()
)
ccPortalRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt1Mb.setStatus("current")
_CcPortalRxPktsAt2Mb_Type = Counter32
_CcPortalRxPktsAt2Mb_Object = MibTableColumn
ccPortalRxPktsAt2Mb = _CcPortalRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 2),
    _CcPortalRxPktsAt2Mb_Type()
)
ccPortalRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt2Mb.setStatus("current")
_CcPortalRxPktsAt5pt5Mb_Type = Counter32
_CcPortalRxPktsAt5pt5Mb_Object = MibTableColumn
ccPortalRxPktsAt5pt5Mb = _CcPortalRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 3),
    _CcPortalRxPktsAt5pt5Mb_Type()
)
ccPortalRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt5pt5Mb.setStatus("current")
_CcPortalRxPktsAt6Mb_Type = Counter32
_CcPortalRxPktsAt6Mb_Object = MibTableColumn
ccPortalRxPktsAt6Mb = _CcPortalRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 4),
    _CcPortalRxPktsAt6Mb_Type()
)
ccPortalRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt6Mb.setStatus("current")
_CcPortalRxPktsAt9Mb_Type = Counter32
_CcPortalRxPktsAt9Mb_Object = MibTableColumn
ccPortalRxPktsAt9Mb = _CcPortalRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 5),
    _CcPortalRxPktsAt9Mb_Type()
)
ccPortalRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt9Mb.setStatus("current")
_CcPortalRxPktsAt11Mb_Type = Counter32
_CcPortalRxPktsAt11Mb_Object = MibTableColumn
ccPortalRxPktsAt11Mb = _CcPortalRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 6),
    _CcPortalRxPktsAt11Mb_Type()
)
ccPortalRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt11Mb.setStatus("current")
_CcPortalRxPktsAt12Mb_Type = Counter32
_CcPortalRxPktsAt12Mb_Object = MibTableColumn
ccPortalRxPktsAt12Mb = _CcPortalRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 7),
    _CcPortalRxPktsAt12Mb_Type()
)
ccPortalRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt12Mb.setStatus("current")
_CcPortalRxPktsAt18Mb_Type = Counter32
_CcPortalRxPktsAt18Mb_Object = MibTableColumn
ccPortalRxPktsAt18Mb = _CcPortalRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 8),
    _CcPortalRxPktsAt18Mb_Type()
)
ccPortalRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt18Mb.setStatus("current")
_CcPortalRxPktsAt22Mb_Type = Counter32
_CcPortalRxPktsAt22Mb_Object = MibTableColumn
ccPortalRxPktsAt22Mb = _CcPortalRxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 9),
    _CcPortalRxPktsAt22Mb_Type()
)
ccPortalRxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt22Mb.setStatus("current")
_CcPortalRxPktsAt24Mb_Type = Counter32
_CcPortalRxPktsAt24Mb_Object = MibTableColumn
ccPortalRxPktsAt24Mb = _CcPortalRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 10),
    _CcPortalRxPktsAt24Mb_Type()
)
ccPortalRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt24Mb.setStatus("current")
_CcPortalRxPktsAt36Mb_Type = Counter32
_CcPortalRxPktsAt36Mb_Object = MibTableColumn
ccPortalRxPktsAt36Mb = _CcPortalRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 11),
    _CcPortalRxPktsAt36Mb_Type()
)
ccPortalRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt36Mb.setStatus("current")
_CcPortalRxPktsAt48Mb_Type = Counter32
_CcPortalRxPktsAt48Mb_Object = MibTableColumn
ccPortalRxPktsAt48Mb = _CcPortalRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 12),
    _CcPortalRxPktsAt48Mb_Type()
)
ccPortalRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt48Mb.setStatus("current")
_CcPortalRxPktsAt54Mb_Type = Counter32
_CcPortalRxPktsAt54Mb_Object = MibTableColumn
ccPortalRxPktsAt54Mb = _CcPortalRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 2, 1, 13),
    _CcPortalRxPktsAt54Mb_Type()
)
ccPortalRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt54Mb.setStatus("current")
_CcPortalTxPktsTable_Object = MibTable
ccPortalTxPktsTable = _CcPortalTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3)
)
if mibBuilder.loadTexts:
    ccPortalTxPktsTable.setStatus("current")
_CcPortalTxPktsEntry_Object = MibTableRow
ccPortalTxPktsEntry = _CcPortalTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1)
)
ccPortalTxPktsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxPktsEntry.setStatus("current")
_CcPortalTxPktsAt1Mb_Type = Counter32
_CcPortalTxPktsAt1Mb_Object = MibTableColumn
ccPortalTxPktsAt1Mb = _CcPortalTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 1),
    _CcPortalTxPktsAt1Mb_Type()
)
ccPortalTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt1Mb.setStatus("current")
_CcPortalTxPktsAt2Mb_Type = Counter32
_CcPortalTxPktsAt2Mb_Object = MibTableColumn
ccPortalTxPktsAt2Mb = _CcPortalTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 2),
    _CcPortalTxPktsAt2Mb_Type()
)
ccPortalTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt2Mb.setStatus("current")
_CcPortalTxPktsAt5pt5Mb_Type = Counter32
_CcPortalTxPktsAt5pt5Mb_Object = MibTableColumn
ccPortalTxPktsAt5pt5Mb = _CcPortalTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 3),
    _CcPortalTxPktsAt5pt5Mb_Type()
)
ccPortalTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt5pt5Mb.setStatus("current")
_CcPortalTxPktsAt6Mb_Type = Counter32
_CcPortalTxPktsAt6Mb_Object = MibTableColumn
ccPortalTxPktsAt6Mb = _CcPortalTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 4),
    _CcPortalTxPktsAt6Mb_Type()
)
ccPortalTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt6Mb.setStatus("current")
_CcPortalTxPktsAt9Mb_Type = Counter32
_CcPortalTxPktsAt9Mb_Object = MibTableColumn
ccPortalTxPktsAt9Mb = _CcPortalTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 5),
    _CcPortalTxPktsAt9Mb_Type()
)
ccPortalTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt9Mb.setStatus("current")
_CcPortalTxPktsAt11Mb_Type = Counter32
_CcPortalTxPktsAt11Mb_Object = MibTableColumn
ccPortalTxPktsAt11Mb = _CcPortalTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 6),
    _CcPortalTxPktsAt11Mb_Type()
)
ccPortalTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt11Mb.setStatus("current")
_CcPortalTxPktsAt12Mb_Type = Counter32
_CcPortalTxPktsAt12Mb_Object = MibTableColumn
ccPortalTxPktsAt12Mb = _CcPortalTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 7),
    _CcPortalTxPktsAt12Mb_Type()
)
ccPortalTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt12Mb.setStatus("current")
_CcPortalTxPktsAt18Mb_Type = Counter32
_CcPortalTxPktsAt18Mb_Object = MibTableColumn
ccPortalTxPktsAt18Mb = _CcPortalTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 8),
    _CcPortalTxPktsAt18Mb_Type()
)
ccPortalTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt18Mb.setStatus("current")
_CcPortalTxPktsAt22Mb_Type = Counter32
_CcPortalTxPktsAt22Mb_Object = MibTableColumn
ccPortalTxPktsAt22Mb = _CcPortalTxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 9),
    _CcPortalTxPktsAt22Mb_Type()
)
ccPortalTxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt22Mb.setStatus("current")
_CcPortalTxPktsAt24Mb_Type = Counter32
_CcPortalTxPktsAt24Mb_Object = MibTableColumn
ccPortalTxPktsAt24Mb = _CcPortalTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 10),
    _CcPortalTxPktsAt24Mb_Type()
)
ccPortalTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt24Mb.setStatus("current")
_CcPortalTxPktsAt36Mb_Type = Counter32
_CcPortalTxPktsAt36Mb_Object = MibTableColumn
ccPortalTxPktsAt36Mb = _CcPortalTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 11),
    _CcPortalTxPktsAt36Mb_Type()
)
ccPortalTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt36Mb.setStatus("current")
_CcPortalTxPktsAt48Mb_Type = Counter32
_CcPortalTxPktsAt48Mb_Object = MibTableColumn
ccPortalTxPktsAt48Mb = _CcPortalTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 12),
    _CcPortalTxPktsAt48Mb_Type()
)
ccPortalTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt48Mb.setStatus("current")
_CcPortalTxPktsAt54Mb_Type = Counter32
_CcPortalTxPktsAt54Mb_Object = MibTableColumn
ccPortalTxPktsAt54Mb = _CcPortalTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 3, 1, 13),
    _CcPortalTxPktsAt54Mb_Type()
)
ccPortalTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt54Mb.setStatus("current")
_CcPortalRxOctetsTable_Object = MibTable
ccPortalRxOctetsTable = _CcPortalRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4)
)
if mibBuilder.loadTexts:
    ccPortalRxOctetsTable.setStatus("current")
_CcPortalRxOctetsEntry_Object = MibTableRow
ccPortalRxOctetsEntry = _CcPortalRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1)
)
ccPortalRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalRxOctetsEntry.setStatus("current")
_CcPortalRxOctetsAt1Mb_Type = Counter32
_CcPortalRxOctetsAt1Mb_Object = MibTableColumn
ccPortalRxOctetsAt1Mb = _CcPortalRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 1),
    _CcPortalRxOctetsAt1Mb_Type()
)
ccPortalRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt1Mb.setStatus("current")
_CcPortalRxOctetsAt2Mb_Type = Counter32
_CcPortalRxOctetsAt2Mb_Object = MibTableColumn
ccPortalRxOctetsAt2Mb = _CcPortalRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 2),
    _CcPortalRxOctetsAt2Mb_Type()
)
ccPortalRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt2Mb.setStatus("current")
_CcPortalRxOctetsAt5pt5Mb_Type = Counter32
_CcPortalRxOctetsAt5pt5Mb_Object = MibTableColumn
ccPortalRxOctetsAt5pt5Mb = _CcPortalRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 3),
    _CcPortalRxOctetsAt5pt5Mb_Type()
)
ccPortalRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt5pt5Mb.setStatus("current")
_CcPortalRxOctetsAt6Mb_Type = Counter32
_CcPortalRxOctetsAt6Mb_Object = MibTableColumn
ccPortalRxOctetsAt6Mb = _CcPortalRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 4),
    _CcPortalRxOctetsAt6Mb_Type()
)
ccPortalRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt6Mb.setStatus("current")
_CcPortalRxOctetsAt9Mb_Type = Counter32
_CcPortalRxOctetsAt9Mb_Object = MibTableColumn
ccPortalRxOctetsAt9Mb = _CcPortalRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 5),
    _CcPortalRxOctetsAt9Mb_Type()
)
ccPortalRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt9Mb.setStatus("current")
_CcPortalRxOctetsAt11Mb_Type = Counter32
_CcPortalRxOctetsAt11Mb_Object = MibTableColumn
ccPortalRxOctetsAt11Mb = _CcPortalRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 6),
    _CcPortalRxOctetsAt11Mb_Type()
)
ccPortalRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt11Mb.setStatus("current")
_CcPortalRxOctetsAt12Mb_Type = Counter32
_CcPortalRxOctetsAt12Mb_Object = MibTableColumn
ccPortalRxOctetsAt12Mb = _CcPortalRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 7),
    _CcPortalRxOctetsAt12Mb_Type()
)
ccPortalRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt12Mb.setStatus("current")
_CcPortalRxOctetsAt18Mb_Type = Counter32
_CcPortalRxOctetsAt18Mb_Object = MibTableColumn
ccPortalRxOctetsAt18Mb = _CcPortalRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 8),
    _CcPortalRxOctetsAt18Mb_Type()
)
ccPortalRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt18Mb.setStatus("current")
_CcPortalRxOctetsAt22Mb_Type = Counter32
_CcPortalRxOctetsAt22Mb_Object = MibTableColumn
ccPortalRxOctetsAt22Mb = _CcPortalRxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 9),
    _CcPortalRxOctetsAt22Mb_Type()
)
ccPortalRxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt22Mb.setStatus("current")
_CcPortalRxOctetsAt24Mb_Type = Counter32
_CcPortalRxOctetsAt24Mb_Object = MibTableColumn
ccPortalRxOctetsAt24Mb = _CcPortalRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 10),
    _CcPortalRxOctetsAt24Mb_Type()
)
ccPortalRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt24Mb.setStatus("current")
_CcPortalRxOctetsAt36Mb_Type = Counter32
_CcPortalRxOctetsAt36Mb_Object = MibTableColumn
ccPortalRxOctetsAt36Mb = _CcPortalRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 11),
    _CcPortalRxOctetsAt36Mb_Type()
)
ccPortalRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt36Mb.setStatus("current")
_CcPortalRxOctetsAt48Mb_Type = Counter32
_CcPortalRxOctetsAt48Mb_Object = MibTableColumn
ccPortalRxOctetsAt48Mb = _CcPortalRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 12),
    _CcPortalRxOctetsAt48Mb_Type()
)
ccPortalRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt48Mb.setStatus("current")
_CcPortalRxOctetsAt54Mb_Type = Counter32
_CcPortalRxOctetsAt54Mb_Object = MibTableColumn
ccPortalRxOctetsAt54Mb = _CcPortalRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 4, 1, 13),
    _CcPortalRxOctetsAt54Mb_Type()
)
ccPortalRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt54Mb.setStatus("current")
_CcPortalTxOctetsTable_Object = MibTable
ccPortalTxOctetsTable = _CcPortalTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5)
)
if mibBuilder.loadTexts:
    ccPortalTxOctetsTable.setStatus("current")
_CcPortalTxOctetsEntry_Object = MibTableRow
ccPortalTxOctetsEntry = _CcPortalTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1)
)
ccPortalTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxOctetsEntry.setStatus("current")
_CcPortalTxOctetsAt1Mb_Type = Counter32
_CcPortalTxOctetsAt1Mb_Object = MibTableColumn
ccPortalTxOctetsAt1Mb = _CcPortalTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 1),
    _CcPortalTxOctetsAt1Mb_Type()
)
ccPortalTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt1Mb.setStatus("current")
_CcPortalTxOctetsAt2Mb_Type = Counter32
_CcPortalTxOctetsAt2Mb_Object = MibTableColumn
ccPortalTxOctetsAt2Mb = _CcPortalTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 2),
    _CcPortalTxOctetsAt2Mb_Type()
)
ccPortalTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt2Mb.setStatus("current")
_CcPortalTxOctetsAt5pt5Mb_Type = Counter32
_CcPortalTxOctetsAt5pt5Mb_Object = MibTableColumn
ccPortalTxOctetsAt5pt5Mb = _CcPortalTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 3),
    _CcPortalTxOctetsAt5pt5Mb_Type()
)
ccPortalTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt5pt5Mb.setStatus("current")
_CcPortalTxOctetsAt6Mb_Type = Counter32
_CcPortalTxOctetsAt6Mb_Object = MibTableColumn
ccPortalTxOctetsAt6Mb = _CcPortalTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 4),
    _CcPortalTxOctetsAt6Mb_Type()
)
ccPortalTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt6Mb.setStatus("current")
_CcPortalTxOctetsAt9Mb_Type = Counter32
_CcPortalTxOctetsAt9Mb_Object = MibTableColumn
ccPortalTxOctetsAt9Mb = _CcPortalTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 5),
    _CcPortalTxOctetsAt9Mb_Type()
)
ccPortalTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt9Mb.setStatus("current")
_CcPortalTxOctetsAt11Mb_Type = Counter32
_CcPortalTxOctetsAt11Mb_Object = MibTableColumn
ccPortalTxOctetsAt11Mb = _CcPortalTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 6),
    _CcPortalTxOctetsAt11Mb_Type()
)
ccPortalTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt11Mb.setStatus("current")
_CcPortalTxOctetsAt12Mb_Type = Counter32
_CcPortalTxOctetsAt12Mb_Object = MibTableColumn
ccPortalTxOctetsAt12Mb = _CcPortalTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 7),
    _CcPortalTxOctetsAt12Mb_Type()
)
ccPortalTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt12Mb.setStatus("current")
_CcPortalTxOctetsAt18Mb_Type = Counter32
_CcPortalTxOctetsAt18Mb_Object = MibTableColumn
ccPortalTxOctetsAt18Mb = _CcPortalTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 8),
    _CcPortalTxOctetsAt18Mb_Type()
)
ccPortalTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt18Mb.setStatus("current")
_CcPortalTxOctetsAt22Mb_Type = Counter32
_CcPortalTxOctetsAt22Mb_Object = MibTableColumn
ccPortalTxOctetsAt22Mb = _CcPortalTxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 9),
    _CcPortalTxOctetsAt22Mb_Type()
)
ccPortalTxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt22Mb.setStatus("current")
_CcPortalTxOctetsAt24Mb_Type = Counter32
_CcPortalTxOctetsAt24Mb_Object = MibTableColumn
ccPortalTxOctetsAt24Mb = _CcPortalTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 10),
    _CcPortalTxOctetsAt24Mb_Type()
)
ccPortalTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt24Mb.setStatus("current")
_CcPortalTxOctetsAt36Mb_Type = Counter32
_CcPortalTxOctetsAt36Mb_Object = MibTableColumn
ccPortalTxOctetsAt36Mb = _CcPortalTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 11),
    _CcPortalTxOctetsAt36Mb_Type()
)
ccPortalTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt36Mb.setStatus("current")
_CcPortalTxOctetsAt48Mb_Type = Counter32
_CcPortalTxOctetsAt48Mb_Object = MibTableColumn
ccPortalTxOctetsAt48Mb = _CcPortalTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 12),
    _CcPortalTxOctetsAt48Mb_Type()
)
ccPortalTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt48Mb.setStatus("current")
_CcPortalTxOctetsAt54Mb_Type = Counter32
_CcPortalTxOctetsAt54Mb_Object = MibTableColumn
ccPortalTxOctetsAt54Mb = _CcPortalTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 5, 1, 13),
    _CcPortalTxOctetsAt54Mb_Type()
)
ccPortalTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt54Mb.setStatus("current")
_CcPortalTxRetriesPktsTable_Object = MibTable
ccPortalTxRetriesPktsTable = _CcPortalTxRetriesPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6)
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsTable.setStatus("current")
_CcPortalTxRetriesPktsEntry_Object = MibTableRow
ccPortalTxRetriesPktsEntry = _CcPortalTxRetriesPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1)
)
ccPortalTxRetriesPktsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsEntry.setStatus("current")
_CcPortalTxRetriesPktsNone_Type = Counter32
_CcPortalTxRetriesPktsNone_Object = MibTableColumn
ccPortalTxRetriesPktsNone = _CcPortalTxRetriesPktsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 1),
    _CcPortalTxRetriesPktsNone_Type()
)
ccPortalTxRetriesPktsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsNone.setStatus("current")
_CcPortalTxRetriesPkts01_Type = Counter32
_CcPortalTxRetriesPkts01_Object = MibTableColumn
ccPortalTxRetriesPkts01 = _CcPortalTxRetriesPkts01_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 2),
    _CcPortalTxRetriesPkts01_Type()
)
ccPortalTxRetriesPkts01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts01.setStatus("current")
_CcPortalTxRetriesPkts02_Type = Counter32
_CcPortalTxRetriesPkts02_Object = MibTableColumn
ccPortalTxRetriesPkts02 = _CcPortalTxRetriesPkts02_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 3),
    _CcPortalTxRetriesPkts02_Type()
)
ccPortalTxRetriesPkts02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts02.setStatus("current")
_CcPortalTxRetriesPkts03_Type = Counter32
_CcPortalTxRetriesPkts03_Object = MibTableColumn
ccPortalTxRetriesPkts03 = _CcPortalTxRetriesPkts03_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 4),
    _CcPortalTxRetriesPkts03_Type()
)
ccPortalTxRetriesPkts03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts03.setStatus("current")
_CcPortalTxRetriesPkts04_Type = Counter32
_CcPortalTxRetriesPkts04_Object = MibTableColumn
ccPortalTxRetriesPkts04 = _CcPortalTxRetriesPkts04_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 5),
    _CcPortalTxRetriesPkts04_Type()
)
ccPortalTxRetriesPkts04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts04.setStatus("current")
_CcPortalTxRetriesPkts05_Type = Counter32
_CcPortalTxRetriesPkts05_Object = MibTableColumn
ccPortalTxRetriesPkts05 = _CcPortalTxRetriesPkts05_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 6),
    _CcPortalTxRetriesPkts05_Type()
)
ccPortalTxRetriesPkts05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts05.setStatus("current")
_CcPortalTxRetriesPkts06_Type = Counter32
_CcPortalTxRetriesPkts06_Object = MibTableColumn
ccPortalTxRetriesPkts06 = _CcPortalTxRetriesPkts06_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 7),
    _CcPortalTxRetriesPkts06_Type()
)
ccPortalTxRetriesPkts06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts06.setStatus("current")
_CcPortalTxRetriesPkts07_Type = Counter32
_CcPortalTxRetriesPkts07_Object = MibTableColumn
ccPortalTxRetriesPkts07 = _CcPortalTxRetriesPkts07_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 8),
    _CcPortalTxRetriesPkts07_Type()
)
ccPortalTxRetriesPkts07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts07.setStatus("current")
_CcPortalTxRetriesPkts08_Type = Counter32
_CcPortalTxRetriesPkts08_Object = MibTableColumn
ccPortalTxRetriesPkts08 = _CcPortalTxRetriesPkts08_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 9),
    _CcPortalTxRetriesPkts08_Type()
)
ccPortalTxRetriesPkts08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts08.setStatus("current")
_CcPortalTxRetriesPkts09_Type = Counter32
_CcPortalTxRetriesPkts09_Object = MibTableColumn
ccPortalTxRetriesPkts09 = _CcPortalTxRetriesPkts09_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 10),
    _CcPortalTxRetriesPkts09_Type()
)
ccPortalTxRetriesPkts09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts09.setStatus("current")
_CcPortalTxRetriesPkts10_Type = Counter32
_CcPortalTxRetriesPkts10_Object = MibTableColumn
ccPortalTxRetriesPkts10 = _CcPortalTxRetriesPkts10_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 11),
    _CcPortalTxRetriesPkts10_Type()
)
ccPortalTxRetriesPkts10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts10.setStatus("current")
_CcPortalTxRetriesPkts11_Type = Counter32
_CcPortalTxRetriesPkts11_Object = MibTableColumn
ccPortalTxRetriesPkts11 = _CcPortalTxRetriesPkts11_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 12),
    _CcPortalTxRetriesPkts11_Type()
)
ccPortalTxRetriesPkts11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts11.setStatus("current")
_CcPortalTxRetriesPkts12_Type = Counter32
_CcPortalTxRetriesPkts12_Object = MibTableColumn
ccPortalTxRetriesPkts12 = _CcPortalTxRetriesPkts12_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 13),
    _CcPortalTxRetriesPkts12_Type()
)
ccPortalTxRetriesPkts12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts12.setStatus("current")
_CcPortalTxRetriesPkts13_Type = Counter32
_CcPortalTxRetriesPkts13_Object = MibTableColumn
ccPortalTxRetriesPkts13 = _CcPortalTxRetriesPkts13_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 14),
    _CcPortalTxRetriesPkts13_Type()
)
ccPortalTxRetriesPkts13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts13.setStatus("current")
_CcPortalTxRetriesPkts14_Type = Counter32
_CcPortalTxRetriesPkts14_Object = MibTableColumn
ccPortalTxRetriesPkts14 = _CcPortalTxRetriesPkts14_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 15),
    _CcPortalTxRetriesPkts14_Type()
)
ccPortalTxRetriesPkts14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts14.setStatus("current")
_CcPortalTxRetriesPkts15_Type = Counter32
_CcPortalTxRetriesPkts15_Object = MibTableColumn
ccPortalTxRetriesPkts15 = _CcPortalTxRetriesPkts15_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 16),
    _CcPortalTxRetriesPkts15_Type()
)
ccPortalTxRetriesPkts15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts15.setStatus("deprecated")
_CcPortalTxRetriesPktsFailed_Type = Counter32
_CcPortalTxRetriesPktsFailed_Object = MibTableColumn
ccPortalTxRetriesPktsFailed = _CcPortalTxRetriesPktsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 6, 1, 17),
    _CcPortalTxRetriesPktsFailed_Type()
)
ccPortalTxRetriesPktsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsFailed.setStatus("current")
_CcPortalTxRetriesOctetsTable_Object = MibTable
ccPortalTxRetriesOctetsTable = _CcPortalTxRetriesOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7)
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsTable.setStatus("current")
_CcPortalTxRetriesOctetsEntry_Object = MibTableRow
ccPortalTxRetriesOctetsEntry = _CcPortalTxRetriesOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1)
)
ccPortalTxRetriesOctetsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsEntry.setStatus("current")
_CcPortalTxRetriesOctetsNone_Type = Counter32
_CcPortalTxRetriesOctetsNone_Object = MibTableColumn
ccPortalTxRetriesOctetsNone = _CcPortalTxRetriesOctetsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 1),
    _CcPortalTxRetriesOctetsNone_Type()
)
ccPortalTxRetriesOctetsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsNone.setStatus("current")
_CcPortalTxRetriesOctets01_Type = Counter32
_CcPortalTxRetriesOctets01_Object = MibTableColumn
ccPortalTxRetriesOctets01 = _CcPortalTxRetriesOctets01_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 2),
    _CcPortalTxRetriesOctets01_Type()
)
ccPortalTxRetriesOctets01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets01.setStatus("current")
_CcPortalTxRetriesOctets02_Type = Counter32
_CcPortalTxRetriesOctets02_Object = MibTableColumn
ccPortalTxRetriesOctets02 = _CcPortalTxRetriesOctets02_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 3),
    _CcPortalTxRetriesOctets02_Type()
)
ccPortalTxRetriesOctets02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets02.setStatus("current")
_CcPortalTxRetriesOctets03_Type = Counter32
_CcPortalTxRetriesOctets03_Object = MibTableColumn
ccPortalTxRetriesOctets03 = _CcPortalTxRetriesOctets03_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 4),
    _CcPortalTxRetriesOctets03_Type()
)
ccPortalTxRetriesOctets03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets03.setStatus("current")
_CcPortalTxRetriesOctets04_Type = Counter32
_CcPortalTxRetriesOctets04_Object = MibTableColumn
ccPortalTxRetriesOctets04 = _CcPortalTxRetriesOctets04_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 5),
    _CcPortalTxRetriesOctets04_Type()
)
ccPortalTxRetriesOctets04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets04.setStatus("current")
_CcPortalTxRetriesOctets05_Type = Counter32
_CcPortalTxRetriesOctets05_Object = MibTableColumn
ccPortalTxRetriesOctets05 = _CcPortalTxRetriesOctets05_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 6),
    _CcPortalTxRetriesOctets05_Type()
)
ccPortalTxRetriesOctets05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets05.setStatus("current")
_CcPortalTxRetriesOctets06_Type = Counter32
_CcPortalTxRetriesOctets06_Object = MibTableColumn
ccPortalTxRetriesOctets06 = _CcPortalTxRetriesOctets06_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 7),
    _CcPortalTxRetriesOctets06_Type()
)
ccPortalTxRetriesOctets06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets06.setStatus("current")
_CcPortalTxRetriesOctets07_Type = Counter32
_CcPortalTxRetriesOctets07_Object = MibTableColumn
ccPortalTxRetriesOctets07 = _CcPortalTxRetriesOctets07_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 8),
    _CcPortalTxRetriesOctets07_Type()
)
ccPortalTxRetriesOctets07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets07.setStatus("current")
_CcPortalTxRetriesOctets08_Type = Counter32
_CcPortalTxRetriesOctets08_Object = MibTableColumn
ccPortalTxRetriesOctets08 = _CcPortalTxRetriesOctets08_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 9),
    _CcPortalTxRetriesOctets08_Type()
)
ccPortalTxRetriesOctets08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets08.setStatus("current")
_CcPortalTxRetriesOctets09_Type = Counter32
_CcPortalTxRetriesOctets09_Object = MibTableColumn
ccPortalTxRetriesOctets09 = _CcPortalTxRetriesOctets09_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 10),
    _CcPortalTxRetriesOctets09_Type()
)
ccPortalTxRetriesOctets09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets09.setStatus("current")
_CcPortalTxRetriesOctets10_Type = Counter32
_CcPortalTxRetriesOctets10_Object = MibTableColumn
ccPortalTxRetriesOctets10 = _CcPortalTxRetriesOctets10_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 11),
    _CcPortalTxRetriesOctets10_Type()
)
ccPortalTxRetriesOctets10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets10.setStatus("current")
_CcPortalTxRetriesOctets11_Type = Counter32
_CcPortalTxRetriesOctets11_Object = MibTableColumn
ccPortalTxRetriesOctets11 = _CcPortalTxRetriesOctets11_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 12),
    _CcPortalTxRetriesOctets11_Type()
)
ccPortalTxRetriesOctets11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets11.setStatus("current")
_CcPortalTxRetriesOctets12_Type = Counter32
_CcPortalTxRetriesOctets12_Object = MibTableColumn
ccPortalTxRetriesOctets12 = _CcPortalTxRetriesOctets12_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 13),
    _CcPortalTxRetriesOctets12_Type()
)
ccPortalTxRetriesOctets12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets12.setStatus("current")
_CcPortalTxRetriesOctets13_Type = Counter32
_CcPortalTxRetriesOctets13_Object = MibTableColumn
ccPortalTxRetriesOctets13 = _CcPortalTxRetriesOctets13_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 14),
    _CcPortalTxRetriesOctets13_Type()
)
ccPortalTxRetriesOctets13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets13.setStatus("current")
_CcPortalTxRetriesOctets14_Type = Counter32
_CcPortalTxRetriesOctets14_Object = MibTableColumn
ccPortalTxRetriesOctets14 = _CcPortalTxRetriesOctets14_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 15),
    _CcPortalTxRetriesOctets14_Type()
)
ccPortalTxRetriesOctets14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets14.setStatus("current")
_CcPortalTxRetriesOctets15_Type = Counter32
_CcPortalTxRetriesOctets15_Object = MibTableColumn
ccPortalTxRetriesOctets15 = _CcPortalTxRetriesOctets15_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 16),
    _CcPortalTxRetriesOctets15_Type()
)
ccPortalTxRetriesOctets15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets15.setStatus("deprecated")
_CcPortalTxRetriesOctetsFailed_Type = Counter32
_CcPortalTxRetriesOctetsFailed_Object = MibTableColumn
ccPortalTxRetriesOctetsFailed = _CcPortalTxRetriesOctetsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 7, 1, 17),
    _CcPortalTxRetriesOctetsFailed_Type()
)
ccPortalTxRetriesOctetsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsFailed.setStatus("current")
_CcPortalSigStatsTable_Object = MibTable
ccPortalSigStatsTable = _CcPortalSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8)
)
if mibBuilder.loadTexts:
    ccPortalSigStatsTable.setStatus("current")
_CcPortalSigStatsEntry_Object = MibTableRow
ccPortalSigStatsEntry = _CcPortalSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1)
)
ccPortalSigStatsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSigStatsEntry.setStatus("current")
_CcPortalSigStatsNumPkts_Type = Counter32
_CcPortalSigStatsNumPkts_Object = MibTableColumn
ccPortalSigStatsNumPkts = _CcPortalSigStatsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 1),
    _CcPortalSigStatsNumPkts_Type()
)
ccPortalSigStatsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNumPkts.setStatus("current")
_CcPortalSigStatsSignalBest_Type = Integer32
_CcPortalSigStatsSignalBest_Object = MibTableColumn
ccPortalSigStatsSignalBest = _CcPortalSigStatsSignalBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 2),
    _CcPortalSigStatsSignalBest_Type()
)
ccPortalSigStatsSignalBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalBest.setUnits("dBm")
_CcPortalSigStatsSignalWorst_Type = Integer32
_CcPortalSigStatsSignalWorst_Object = MibTableColumn
ccPortalSigStatsSignalWorst = _CcPortalSigStatsSignalWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 3),
    _CcPortalSigStatsSignalWorst_Type()
)
ccPortalSigStatsSignalWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalWorst.setUnits("dBm")
_CcPortalSigStatsSignalSum_Type = Integer32
_CcPortalSigStatsSignalSum_Object = MibTableColumn
ccPortalSigStatsSignalSum = _CcPortalSigStatsSignalSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 4),
    _CcPortalSigStatsSignalSum_Type()
)
ccPortalSigStatsSignalSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSum.setUnits("dBm")
_CcPortalSigStatsSignalSumSquares_Type = Counter64
_CcPortalSigStatsSignalSumSquares_Object = MibTableColumn
ccPortalSigStatsSignalSumSquares = _CcPortalSigStatsSignalSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 5),
    _CcPortalSigStatsSignalSumSquares_Type()
)
ccPortalSigStatsSignalSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSumSquares.setUnits("dBm")
_CcPortalSigStatsSignalMostRecent_Type = Integer32
_CcPortalSigStatsSignalMostRecent_Object = MibTableColumn
ccPortalSigStatsSignalMostRecent = _CcPortalSigStatsSignalMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 6),
    _CcPortalSigStatsSignalMostRecent_Type()
)
ccPortalSigStatsSignalMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalMostRecent.setUnits("dBm")
_CcPortalSigStatsNoiseBest_Type = Integer32
_CcPortalSigStatsNoiseBest_Object = MibTableColumn
ccPortalSigStatsNoiseBest = _CcPortalSigStatsNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 7),
    _CcPortalSigStatsNoiseBest_Type()
)
ccPortalSigStatsNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseBest.setUnits("dBm")
_CcPortalSigStatsNoiseWorst_Type = Integer32
_CcPortalSigStatsNoiseWorst_Object = MibTableColumn
ccPortalSigStatsNoiseWorst = _CcPortalSigStatsNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 8),
    _CcPortalSigStatsNoiseWorst_Type()
)
ccPortalSigStatsNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseWorst.setUnits("dBm")
_CcPortalSigStatsNoiseSum_Type = Integer32
_CcPortalSigStatsNoiseSum_Object = MibTableColumn
ccPortalSigStatsNoiseSum = _CcPortalSigStatsNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 9),
    _CcPortalSigStatsNoiseSum_Type()
)
ccPortalSigStatsNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSum.setUnits("dBm")
_CcPortalSigStatsNoiseSumSquares_Type = Counter64
_CcPortalSigStatsNoiseSumSquares_Object = MibTableColumn
ccPortalSigStatsNoiseSumSquares = _CcPortalSigStatsNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 10),
    _CcPortalSigStatsNoiseSumSquares_Type()
)
ccPortalSigStatsNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSumSquares.setUnits("dBm")
_CcPortalSigStatsNoiseMostRecent_Type = Integer32
_CcPortalSigStatsNoiseMostRecent_Object = MibTableColumn
ccPortalSigStatsNoiseMostRecent = _CcPortalSigStatsNoiseMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 11),
    _CcPortalSigStatsNoiseMostRecent_Type()
)
ccPortalSigStatsNoiseMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseMostRecent.setUnits("dBm")
_CcPortalSigStatsSnrBest_Type = Integer32
_CcPortalSigStatsSnrBest_Object = MibTableColumn
ccPortalSigStatsSnrBest = _CcPortalSigStatsSnrBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 12),
    _CcPortalSigStatsSnrBest_Type()
)
ccPortalSigStatsSnrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrBest.setUnits("dB")
_CcPortalSigStatsSnrWorst_Type = Integer32
_CcPortalSigStatsSnrWorst_Object = MibTableColumn
ccPortalSigStatsSnrWorst = _CcPortalSigStatsSnrWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 13),
    _CcPortalSigStatsSnrWorst_Type()
)
ccPortalSigStatsSnrWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrWorst.setUnits("dB")
_CcPortalSigStatsSnrSum_Type = Counter64
_CcPortalSigStatsSnrSum_Object = MibTableColumn
ccPortalSigStatsSnrSum = _CcPortalSigStatsSnrSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 14),
    _CcPortalSigStatsSnrSum_Type()
)
ccPortalSigStatsSnrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSum.setUnits("dB")
_CcPortalSigStatsSnrSumSquares_Type = Counter64
_CcPortalSigStatsSnrSumSquares_Object = MibTableColumn
ccPortalSigStatsSnrSumSquares = _CcPortalSigStatsSnrSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 15),
    _CcPortalSigStatsSnrSumSquares_Type()
)
ccPortalSigStatsSnrSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSumSquares.setUnits("dB")
_CcPortalSigStatsSnrMostRecent_Type = Integer32
_CcPortalSigStatsSnrMostRecent_Object = MibTableColumn
ccPortalSigStatsSnrMostRecent = _CcPortalSigStatsSnrMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 8, 1, 16),
    _CcPortalSigStatsSnrMostRecent_Type()
)
ccPortalSigStatsSnrMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrMostRecent.setUnits("dB")
_CcPortalSumStatsShortTable_Object = MibTable
ccPortalSumStatsShortTable = _CcPortalSumStatsShortTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9)
)
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTable.setStatus("current")
_CcPortalSumStatsShortEntry_Object = MibTableRow
ccPortalSumStatsShortEntry = _CcPortalSumStatsShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1)
)
ccPortalSumStatsShortEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSumStatsShortEntry.setStatus("current")
_CcPortalSumStatsShortTimestamp_Type = TimeTicks
_CcPortalSumStatsShortTimestamp_Object = MibTableColumn
ccPortalSumStatsShortTimestamp = _CcPortalSumStatsShortTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 1),
    _CcPortalSumStatsShortTimestamp_Type()
)
ccPortalSumStatsShortTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTimestamp.setStatus("current")
_CcPortalSumStatsShortNumPkts_Type = Unsigned32
_CcPortalSumStatsShortNumPkts_Object = MibTableColumn
ccPortalSumStatsShortNumPkts = _CcPortalSumStatsShortNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 2),
    _CcPortalSumStatsShortNumPkts_Type()
)
ccPortalSumStatsShortNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortNumPkts.setUnits("packets")
_CcPortalSumStatsShortPktsPerSec100_Type = ScaleBy100
_CcPortalSumStatsShortPktsPerSec100_Object = MibTableColumn
ccPortalSumStatsShortPktsPerSec100 = _CcPortalSumStatsShortPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 3),
    _CcPortalSumStatsShortPktsPerSec100_Type()
)
ccPortalSumStatsShortPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSec100.setUnits("pkts per sec x100")
_CcPortalSumStatsShortPktsPerSecTx100_Type = ScaleBy100
_CcPortalSumStatsShortPktsPerSecTx100_Object = MibTableColumn
ccPortalSumStatsShortPktsPerSecTx100 = _CcPortalSumStatsShortPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 4),
    _CcPortalSumStatsShortPktsPerSecTx100_Type()
)
ccPortalSumStatsShortPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecTx100.setUnits("pkts per sec x100")
_CcPortalSumStatsShortPktsPerSecRx100_Type = ScaleBy100
_CcPortalSumStatsShortPktsPerSecRx100_Object = MibTableColumn
ccPortalSumStatsShortPktsPerSecRx100 = _CcPortalSumStatsShortPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 5),
    _CcPortalSumStatsShortPktsPerSecRx100_Type()
)
ccPortalSumStatsShortPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecRx100.setUnits("pkts per sec x100")
_CcPortalSumStatsShortThroughput_Type = Unsigned32
_CcPortalSumStatsShortThroughput_Object = MibTableColumn
ccPortalSumStatsShortThroughput = _CcPortalSumStatsShortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 6),
    _CcPortalSumStatsShortThroughput_Type()
)
ccPortalSumStatsShortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughput.setUnits("bits per second")
_CcPortalSumStatsShortThroughputTx_Type = Unsigned32
_CcPortalSumStatsShortThroughputTx_Object = MibTableColumn
ccPortalSumStatsShortThroughputTx = _CcPortalSumStatsShortThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 7),
    _CcPortalSumStatsShortThroughputTx_Type()
)
ccPortalSumStatsShortThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputTx.setUnits("bits per second")
_CcPortalSumStatsShortThroughputRx_Type = Unsigned32
_CcPortalSumStatsShortThroughputRx_Object = MibTableColumn
ccPortalSumStatsShortThroughputRx = _CcPortalSumStatsShortThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 8),
    _CcPortalSumStatsShortThroughputRx_Type()
)
ccPortalSumStatsShortThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputRx.setUnits("bits per second")
_CcPortalSumStatsShortAvgBitSpeed_Type = Unsigned32
_CcPortalSumStatsShortAvgBitSpeed_Object = MibTableColumn
ccPortalSumStatsShortAvgBitSpeed = _CcPortalSumStatsShortAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 9),
    _CcPortalSumStatsShortAvgBitSpeed_Type()
)
ccPortalSumStatsShortAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgBitSpeed.setUnits("bits per second")
_CcPortalSumStatsShortAvgMuSignal_Type = Integer32
_CcPortalSumStatsShortAvgMuSignal_Object = MibTableColumn
ccPortalSumStatsShortAvgMuSignal = _CcPortalSumStatsShortAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 10),
    _CcPortalSumStatsShortAvgMuSignal_Type()
)
ccPortalSumStatsShortAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSignal.setUnits("dBm")
_CcPortalSumStatsShortAvgMuNoise_Type = Integer32
_CcPortalSumStatsShortAvgMuNoise_Object = MibTableColumn
ccPortalSumStatsShortAvgMuNoise = _CcPortalSumStatsShortAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 11),
    _CcPortalSumStatsShortAvgMuNoise_Type()
)
ccPortalSumStatsShortAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuNoise.setUnits("dBm")
_CcPortalSumStatsShortAvgMuSnr_Type = Integer32
_CcPortalSumStatsShortAvgMuSnr_Object = MibTableColumn
ccPortalSumStatsShortAvgMuSnr = _CcPortalSumStatsShortAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 12),
    _CcPortalSumStatsShortAvgMuSnr_Type()
)
ccPortalSumStatsShortAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSnr.setUnits("dB")
_CcPortalSumStatsShortPp10kNUcastPkts_Type = PartsPer10k
_CcPortalSumStatsShortPp10kNUcastPkts_Object = MibTableColumn
ccPortalSumStatsShortPp10kNUcastPkts = _CcPortalSumStatsShortPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 13),
    _CcPortalSumStatsShortPp10kNUcastPkts_Type()
)
ccPortalSumStatsShortPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kNUcastPkts.setUnits("parts-per-10000")
_CcPortalSumStatsShortPp10kTxWithRetries_Type = PartsPer10k
_CcPortalSumStatsShortPp10kTxWithRetries_Object = MibTableColumn
ccPortalSumStatsShortPp10kTxWithRetries = _CcPortalSumStatsShortPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 14),
    _CcPortalSumStatsShortPp10kTxWithRetries_Type()
)
ccPortalSumStatsShortPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxWithRetries.setUnits("parts-per-10000")
_CcPortalSumStatsShortPp10kTxMaxRetries_Type = PartsPer10k
_CcPortalSumStatsShortPp10kTxMaxRetries_Object = MibTableColumn
ccPortalSumStatsShortPp10kTxMaxRetries = _CcPortalSumStatsShortPp10kTxMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 15),
    _CcPortalSumStatsShortPp10kTxMaxRetries_Type()
)
ccPortalSumStatsShortPp10kTxMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxMaxRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxMaxRetries.setUnits("parts-per-10000")
_CcPortalSumStatsShortTxAvgRetries100_Type = ScaleBy100
_CcPortalSumStatsShortTxAvgRetries100_Object = MibTableColumn
ccPortalSumStatsShortTxAvgRetries100 = _CcPortalSumStatsShortTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 16),
    _CcPortalSumStatsShortTxAvgRetries100_Type()
)
ccPortalSumStatsShortTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTxAvgRetries100.setUnits("average x100")
_CcPortalSumStatsShortPp10kRxUndecrypt_Type = PartsPer10k
_CcPortalSumStatsShortPp10kRxUndecrypt_Object = MibTableColumn
ccPortalSumStatsShortPp10kRxUndecrypt = _CcPortalSumStatsShortPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 17),
    _CcPortalSumStatsShortPp10kRxUndecrypt_Type()
)
ccPortalSumStatsShortPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRxUndecrypt.setUnits("parts-per-10000")


class _CcPortalSumStatsShortTotalMus_Type(Unsigned32):
    """Custom type ccPortalSumStatsShortTotalMus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcPortalSumStatsShortTotalMus_Type.__name__ = "Unsigned32"
_CcPortalSumStatsShortTotalMus_Object = MibTableColumn
ccPortalSumStatsShortTotalMus = _CcPortalSumStatsShortTotalMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 18),
    _CcPortalSumStatsShortTotalMus_Type()
)
ccPortalSumStatsShortTotalMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTotalMus.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTotalMus.setUnits("number of MUs")
_CcPortalSumStatsShortPp10kRfUtil_Type = PartsPer10k
_CcPortalSumStatsShortPp10kRfUtil_Object = MibTableColumn
ccPortalSumStatsShortPp10kRfUtil = _CcPortalSumStatsShortPp10kRfUtil_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 19),
    _CcPortalSumStatsShortPp10kRfUtil_Type()
)
ccPortalSumStatsShortPp10kRfUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRfUtil.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRfUtil.setUnits("parts-per-10000")
_CcPortalSumStatsShortPp10kDropped_Type = PartsPer10k
_CcPortalSumStatsShortPp10kDropped_Object = MibTableColumn
ccPortalSumStatsShortPp10kDropped = _CcPortalSumStatsShortPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 9, 1, 20),
    _CcPortalSumStatsShortPp10kDropped_Type()
)
ccPortalSumStatsShortPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kDropped.setStatus("current")
_CcPortalSumStatsLongTable_Object = MibTable
ccPortalSumStatsLongTable = _CcPortalSumStatsLongTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10)
)
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTable.setStatus("current")
_CcPortalSumStatsLongEntry_Object = MibTableRow
ccPortalSumStatsLongEntry = _CcPortalSumStatsLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1)
)
ccPortalSumStatsLongEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSumStatsLongEntry.setStatus("current")
_CcPortalSumStatsLongTimestamp_Type = TimeTicks
_CcPortalSumStatsLongTimestamp_Object = MibTableColumn
ccPortalSumStatsLongTimestamp = _CcPortalSumStatsLongTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 1),
    _CcPortalSumStatsLongTimestamp_Type()
)
ccPortalSumStatsLongTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTimestamp.setStatus("current")
_CcPortalSumStatsLongNumPkts_Type = Unsigned32
_CcPortalSumStatsLongNumPkts_Object = MibTableColumn
ccPortalSumStatsLongNumPkts = _CcPortalSumStatsLongNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 2),
    _CcPortalSumStatsLongNumPkts_Type()
)
ccPortalSumStatsLongNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongNumPkts.setUnits("packets")
_CcPortalSumStatsLongPktsPerSec100_Type = ScaleBy100
_CcPortalSumStatsLongPktsPerSec100_Object = MibTableColumn
ccPortalSumStatsLongPktsPerSec100 = _CcPortalSumStatsLongPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 3),
    _CcPortalSumStatsLongPktsPerSec100_Type()
)
ccPortalSumStatsLongPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSec100.setUnits("pkts per sec x100")
_CcPortalSumStatsLongPktsPerSecTx100_Type = ScaleBy100
_CcPortalSumStatsLongPktsPerSecTx100_Object = MibTableColumn
ccPortalSumStatsLongPktsPerSecTx100 = _CcPortalSumStatsLongPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 4),
    _CcPortalSumStatsLongPktsPerSecTx100_Type()
)
ccPortalSumStatsLongPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecTx100.setUnits("pkts per sec x100")
_CcPortalSumStatsLongPktsPerSecRx100_Type = ScaleBy100
_CcPortalSumStatsLongPktsPerSecRx100_Object = MibTableColumn
ccPortalSumStatsLongPktsPerSecRx100 = _CcPortalSumStatsLongPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 5),
    _CcPortalSumStatsLongPktsPerSecRx100_Type()
)
ccPortalSumStatsLongPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecRx100.setUnits("pkts per sec x100")
_CcPortalSumStatsLongThroughput_Type = Unsigned32
_CcPortalSumStatsLongThroughput_Object = MibTableColumn
ccPortalSumStatsLongThroughput = _CcPortalSumStatsLongThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 6),
    _CcPortalSumStatsLongThroughput_Type()
)
ccPortalSumStatsLongThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughput.setUnits("bits per second")
_CcPortalSumStatsLongThroughputTx_Type = Unsigned32
_CcPortalSumStatsLongThroughputTx_Object = MibTableColumn
ccPortalSumStatsLongThroughputTx = _CcPortalSumStatsLongThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 7),
    _CcPortalSumStatsLongThroughputTx_Type()
)
ccPortalSumStatsLongThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputTx.setUnits("bits per second")
_CcPortalSumStatsLongThroughputRx_Type = Unsigned32
_CcPortalSumStatsLongThroughputRx_Object = MibTableColumn
ccPortalSumStatsLongThroughputRx = _CcPortalSumStatsLongThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 8),
    _CcPortalSumStatsLongThroughputRx_Type()
)
ccPortalSumStatsLongThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputRx.setUnits("bits per second")
_CcPortalSumStatsLongAvgBitSpeed_Type = Unsigned32
_CcPortalSumStatsLongAvgBitSpeed_Object = MibTableColumn
ccPortalSumStatsLongAvgBitSpeed = _CcPortalSumStatsLongAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 9),
    _CcPortalSumStatsLongAvgBitSpeed_Type()
)
ccPortalSumStatsLongAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgBitSpeed.setUnits("bits per second")
_CcPortalSumStatsLongAvgMuSignal_Type = Integer32
_CcPortalSumStatsLongAvgMuSignal_Object = MibTableColumn
ccPortalSumStatsLongAvgMuSignal = _CcPortalSumStatsLongAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 10),
    _CcPortalSumStatsLongAvgMuSignal_Type()
)
ccPortalSumStatsLongAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSignal.setUnits("dBm")
_CcPortalSumStatsLongAvgMuNoise_Type = Integer32
_CcPortalSumStatsLongAvgMuNoise_Object = MibTableColumn
ccPortalSumStatsLongAvgMuNoise = _CcPortalSumStatsLongAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 11),
    _CcPortalSumStatsLongAvgMuNoise_Type()
)
ccPortalSumStatsLongAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuNoise.setUnits("dBm")
_CcPortalSumStatsLongAvgMuSnr_Type = Integer32
_CcPortalSumStatsLongAvgMuSnr_Object = MibTableColumn
ccPortalSumStatsLongAvgMuSnr = _CcPortalSumStatsLongAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 12),
    _CcPortalSumStatsLongAvgMuSnr_Type()
)
ccPortalSumStatsLongAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSnr.setUnits("dB")
_CcPortalSumStatsLongPp10kNUcastPkts_Type = PartsPer10k
_CcPortalSumStatsLongPp10kNUcastPkts_Object = MibTableColumn
ccPortalSumStatsLongPp10kNUcastPkts = _CcPortalSumStatsLongPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 13),
    _CcPortalSumStatsLongPp10kNUcastPkts_Type()
)
ccPortalSumStatsLongPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kNUcastPkts.setUnits("parts-per-10000")
_CcPortalSumStatsLongPp10kTxWithRetries_Type = PartsPer10k
_CcPortalSumStatsLongPp10kTxWithRetries_Object = MibTableColumn
ccPortalSumStatsLongPp10kTxWithRetries = _CcPortalSumStatsLongPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 14),
    _CcPortalSumStatsLongPp10kTxWithRetries_Type()
)
ccPortalSumStatsLongPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxWithRetries.setUnits("parts-per-10000")
_CcPortalSumStatsLongPp10kTxMaxRetries_Type = PartsPer10k
_CcPortalSumStatsLongPp10kTxMaxRetries_Object = MibTableColumn
ccPortalSumStatsLongPp10kTxMaxRetries = _CcPortalSumStatsLongPp10kTxMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 15),
    _CcPortalSumStatsLongPp10kTxMaxRetries_Type()
)
ccPortalSumStatsLongPp10kTxMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxMaxRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxMaxRetries.setUnits("parts-per-10000")
_CcPortalSumStatsLongTxAvgRetries100_Type = ScaleBy100
_CcPortalSumStatsLongTxAvgRetries100_Object = MibTableColumn
ccPortalSumStatsLongTxAvgRetries100 = _CcPortalSumStatsLongTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 16),
    _CcPortalSumStatsLongTxAvgRetries100_Type()
)
ccPortalSumStatsLongTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTxAvgRetries100.setUnits("average x100")
_CcPortalSumStatsLongPp10kRxUndecrypt_Type = PartsPer10k
_CcPortalSumStatsLongPp10kRxUndecrypt_Object = MibTableColumn
ccPortalSumStatsLongPp10kRxUndecrypt = _CcPortalSumStatsLongPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 17),
    _CcPortalSumStatsLongPp10kRxUndecrypt_Type()
)
ccPortalSumStatsLongPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRxUndecrypt.setUnits("parts-per-10000")


class _CcPortalSumStatsLongTotalMus_Type(Unsigned32):
    """Custom type ccPortalSumStatsLongTotalMus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcPortalSumStatsLongTotalMus_Type.__name__ = "Unsigned32"
_CcPortalSumStatsLongTotalMus_Object = MibTableColumn
ccPortalSumStatsLongTotalMus = _CcPortalSumStatsLongTotalMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 18),
    _CcPortalSumStatsLongTotalMus_Type()
)
ccPortalSumStatsLongTotalMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTotalMus.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTotalMus.setUnits("number of MUs")
_CcPortalSumStatsLongPp10kRfUtil_Type = PartsPer10k
_CcPortalSumStatsLongPp10kRfUtil_Object = MibTableColumn
ccPortalSumStatsLongPp10kRfUtil = _CcPortalSumStatsLongPp10kRfUtil_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 19),
    _CcPortalSumStatsLongPp10kRfUtil_Type()
)
ccPortalSumStatsLongPp10kRfUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRfUtil.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRfUtil.setUnits("parts-per-10000")
_CcPortalSumStatsLongPp10kDropped_Type = PartsPer10k
_CcPortalSumStatsLongPp10kDropped_Object = MibTableColumn
ccPortalSumStatsLongPp10kDropped = _CcPortalSumStatsLongPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 2, 6, 10, 1, 20),
    _CcPortalSumStatsLongPp10kDropped_Type()
)
ccPortalSumStatsLongPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kDropped.setStatus("current")
_CcMus_ObjectIdentity = ObjectIdentity
ccMus = _CcMus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3)
)
_CcMuInfoTable_Object = MibTable
ccMuInfoTable = _CcMuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1)
)
if mibBuilder.loadTexts:
    ccMuInfoTable.setStatus("current")
_CcMuInfoEntry_Object = MibTableRow
ccMuInfoEntry = _CcMuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1)
)
ccMuInfoEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuInfoEntry.setStatus("current")
_CcMuMac_Type = DisplayString
_CcMuMac_Object = MibTableColumn
ccMuMac = _CcMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 1),
    _CcMuMac_Type()
)
ccMuMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccMuMac.setStatus("current")


class _CcMuWlanIndex_Type(Integer32):
    """Custom type ccMuWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CcMuWlanIndex_Type.__name__ = "Integer32"
_CcMuWlanIndex_Object = MibTableColumn
ccMuWlanIndex = _CcMuWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 2),
    _CcMuWlanIndex_Type()
)
ccMuWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuWlanIndex.setStatus("current")
_CcMuWlanName_Type = DisplayString
_CcMuWlanName_Object = MibTableColumn
ccMuWlanName = _CcMuWlanName_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 3),
    _CcMuWlanName_Type()
)
ccMuWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuWlanName.setStatus("current")
_CcMuIsDataReady_Type = TruthValue
_CcMuIsDataReady_Object = MibTableColumn
ccMuIsDataReady = _CcMuIsDataReady_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 4),
    _CcMuIsDataReady_Type()
)
ccMuIsDataReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuIsDataReady.setStatus("current")


class _CcMuPortalIndex_Type(Integer32):
    """Custom type ccMuPortalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CcMuPortalIndex_Type.__name__ = "Integer32"
_CcMuPortalIndex_Object = MibTableColumn
ccMuPortalIndex = _CcMuPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 5),
    _CcMuPortalIndex_Type()
)
ccMuPortalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuPortalIndex.setStatus("current")
_CcMuPortalMac_Type = DisplayString
_CcMuPortalMac_Object = MibTableColumn
ccMuPortalMac = _CcMuPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 6),
    _CcMuPortalMac_Type()
)
ccMuPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuPortalMac.setStatus("current")
_CcMuSymbolRogueApEna_Type = TruthValue
_CcMuSymbolRogueApEna_Object = MibTableColumn
ccMuSymbolRogueApEna = _CcMuSymbolRogueApEna_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 7),
    _CcMuSymbolRogueApEna_Type()
)
ccMuSymbolRogueApEna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSymbolRogueApEna.setStatus("current")
_CcMuIpAddr_Type = IpAddress
_CcMuIpAddr_Object = MibTableColumn
ccMuIpAddr = _CcMuIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 8),
    _CcMuIpAddr_Type()
)
ccMuIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuIpAddr.setStatus("current")


class _CcMuType_Type(Integer32):
    """Custom type ccMuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2),
          ("accessPoint", 3))
    )


_CcMuType_Type.__name__ = "Integer32"
_CcMuType_Object = MibTableColumn
ccMuType = _CcMuType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 9),
    _CcMuType_Type()
)
ccMuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuType.setStatus("current")
_CcMuRadioType_Type = RadioType
_CcMuRadioType_Object = MibTableColumn
ccMuRadioType = _CcMuRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 10),
    _CcMuRadioType_Type()
)
ccMuRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRadioType.setStatus("current")


class _CcMuSupportedRates_Type(Bits):
    """Custom type ccMuSupportedRates based on Bits"""
    namedValues = NamedValues(
        *(("supports1Mb", 0),
          ("supports2Mb", 1),
          ("supports5dot5Mb", 2),
          ("supports6Mb", 3),
          ("supports9Mb", 4),
          ("supports11Mb", 5),
          ("supports12Mb", 6),
          ("supports18Mb", 7),
          ("supports22Mb", 8),
          ("supports24Mb", 9),
          ("supports36Mb", 10),
          ("supports48Mb", 11),
          ("supports54Mb", 12))
    )

_CcMuSupportedRates_Type.__name__ = "Bits"
_CcMuSupportedRates_Object = MibTableColumn
ccMuSupportedRates = _CcMuSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 11),
    _CcMuSupportedRates_Type()
)
ccMuSupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSupportedRates.setStatus("current")


class _CcMuPowerMode_Type(Integer32):
    """Custom type ccMuPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuousAccessMode", 1),
          ("powerSavePolling", 2))
    )


_CcMuPowerMode_Type.__name__ = "Integer32"
_CcMuPowerMode_Object = MibTableColumn
ccMuPowerMode = _CcMuPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 12),
    _CcMuPowerMode_Type()
)
ccMuPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuPowerMode.setStatus("current")


class _CcMuAuthenticationMethod_Type(Integer32):
    """Custom type ccMuAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eap802dot1x", 2),
          ("kerberos", 3))
    )


_CcMuAuthenticationMethod_Type.__name__ = "Integer32"
_CcMuAuthenticationMethod_Object = MibTableColumn
ccMuAuthenticationMethod = _CcMuAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 13),
    _CcMuAuthenticationMethod_Type()
)
ccMuAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuAuthenticationMethod.setStatus("current")


class _CcMuEncryptionMethod_Type(Integer32):
    """Custom type ccMuEncryptionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep40", 2),
          ("wep128", 3),
          ("keyGuardMCM", 4),
          ("wpaTKIP", 5),
          ("wpa2AesCcmp", 6))
    )


_CcMuEncryptionMethod_Type.__name__ = "Integer32"
_CcMuEncryptionMethod_Object = MibTableColumn
ccMuEncryptionMethod = _CcMuEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 14),
    _CcMuEncryptionMethod_Type()
)
ccMuEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuEncryptionMethod.setStatus("current")


class _CcMuVlanId_Type(Unsigned32):
    """Custom type ccMuVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcMuVlanId_Type.__name__ = "Unsigned32"
_CcMuVlanId_Object = MibTableColumn
ccMuVlanId = _CcMuVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 1, 1, 15),
    _CcMuVlanId_Type()
)
ccMuVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuVlanId.setStatus("current")
_CcMuStatsTable_Object = MibTable
ccMuStatsTable = _CcMuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2)
)
if mibBuilder.loadTexts:
    ccMuStatsTable.setStatus("current")
_CcMuStatsEntry_Object = MibTableRow
ccMuStatsEntry = _CcMuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1)
)
ccMuStatsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuStatsEntry.setStatus("current")
_CcMuTxPktsUcast_Type = Counter32
_CcMuTxPktsUcast_Object = MibTableColumn
ccMuTxPktsUcast = _CcMuTxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 1),
    _CcMuTxPktsUcast_Type()
)
ccMuTxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsUcast.setStatus("current")
_CcMuRxPktsUcast_Type = Counter32
_CcMuRxPktsUcast_Object = MibTableColumn
ccMuRxPktsUcast = _CcMuRxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 2),
    _CcMuRxPktsUcast_Type()
)
ccMuRxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsUcast.setStatus("current")
_CcMuRxPktsNUcast_Type = Counter32
_CcMuRxPktsNUcast_Object = MibTableColumn
ccMuRxPktsNUcast = _CcMuRxPktsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 3),
    _CcMuRxPktsNUcast_Type()
)
ccMuRxPktsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsNUcast.setStatus("current")
_CcMuTxOctetsUcast_Type = Counter32
_CcMuTxOctetsUcast_Object = MibTableColumn
ccMuTxOctetsUcast = _CcMuTxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 4),
    _CcMuTxOctetsUcast_Type()
)
ccMuTxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsUcast.setStatus("current")
_CcMuRxOctetsUcast_Type = Counter32
_CcMuRxOctetsUcast_Object = MibTableColumn
ccMuRxOctetsUcast = _CcMuRxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 5),
    _CcMuRxOctetsUcast_Type()
)
ccMuRxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsUcast.setStatus("current")
_CcMuRxOctetsNUcast_Type = Counter32
_CcMuRxOctetsNUcast_Object = MibTableColumn
ccMuRxOctetsNUcast = _CcMuRxOctetsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 6),
    _CcMuRxOctetsNUcast_Type()
)
ccMuRxOctetsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsNUcast.setStatus("current")
_CcMuRxUndecryptablePkts_Type = Counter32
_CcMuRxUndecryptablePkts_Object = MibTableColumn
ccMuRxUndecryptablePkts = _CcMuRxUndecryptablePkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 7),
    _CcMuRxUndecryptablePkts_Type()
)
ccMuRxUndecryptablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxUndecryptablePkts.setStatus("current")
_CcMuRxRssiNumPkts_Type = Counter32
_CcMuRxRssiNumPkts_Object = MibTableColumn
ccMuRxRssiNumPkts = _CcMuRxRssiNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 8),
    _CcMuRxRssiNumPkts_Type()
)
ccMuRxRssiNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiNumPkts.setStatus("current")
_CcMuRxRssiSum_Type = Integer32
_CcMuRxRssiSum_Object = MibTableColumn
ccMuRxRssiSum = _CcMuRxRssiSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 9),
    _CcMuRxRssiSum_Type()
)
ccMuRxRssiSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiSum.setStatus("current")
_CcMuRxRssiSumSquares_Type = Counter64
_CcMuRxRssiSumSquares_Object = MibTableColumn
ccMuRxRssiSumSquares = _CcMuRxRssiSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 10),
    _CcMuRxRssiSumSquares_Type()
)
ccMuRxRssiSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiSumSquares.setStatus("current")


class _CcMuRxRssiMostRecent_Type(Integer32):
    """Custom type ccMuRxRssiMostRecent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcMuRxRssiMostRecent_Type.__name__ = "Integer32"
_CcMuRxRssiMostRecent_Object = MibTableColumn
ccMuRxRssiMostRecent = _CcMuRxRssiMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 11),
    _CcMuRxRssiMostRecent_Type()
)
ccMuRxRssiMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiMostRecent.setStatus("current")
_CcMuLastActivity_Type = TimeTicks
_CcMuLastActivity_Object = MibTableColumn
ccMuLastActivity = _CcMuLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 2, 1, 12),
    _CcMuLastActivity_Type()
)
ccMuLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastActivity.setStatus("current")
_CcMuRxPktsTable_Object = MibTable
ccMuRxPktsTable = _CcMuRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3)
)
if mibBuilder.loadTexts:
    ccMuRxPktsTable.setStatus("current")
_CcMuRxPktsEntry_Object = MibTableRow
ccMuRxPktsEntry = _CcMuRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1)
)
ccMuRxPktsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuRxPktsEntry.setStatus("current")
_CcMuRxPktsAt1Mb_Type = Counter32
_CcMuRxPktsAt1Mb_Object = MibTableColumn
ccMuRxPktsAt1Mb = _CcMuRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 1),
    _CcMuRxPktsAt1Mb_Type()
)
ccMuRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt1Mb.setStatus("current")
_CcMuRxPktsAt2Mb_Type = Counter32
_CcMuRxPktsAt2Mb_Object = MibTableColumn
ccMuRxPktsAt2Mb = _CcMuRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 2),
    _CcMuRxPktsAt2Mb_Type()
)
ccMuRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt2Mb.setStatus("current")
_CcMuRxPktsAt5pt5Mb_Type = Counter32
_CcMuRxPktsAt5pt5Mb_Object = MibTableColumn
ccMuRxPktsAt5pt5Mb = _CcMuRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 3),
    _CcMuRxPktsAt5pt5Mb_Type()
)
ccMuRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt5pt5Mb.setStatus("current")
_CcMuRxPktsAt6Mb_Type = Counter32
_CcMuRxPktsAt6Mb_Object = MibTableColumn
ccMuRxPktsAt6Mb = _CcMuRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 4),
    _CcMuRxPktsAt6Mb_Type()
)
ccMuRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt6Mb.setStatus("current")
_CcMuRxPktsAt9Mb_Type = Counter32
_CcMuRxPktsAt9Mb_Object = MibTableColumn
ccMuRxPktsAt9Mb = _CcMuRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 5),
    _CcMuRxPktsAt9Mb_Type()
)
ccMuRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt9Mb.setStatus("current")
_CcMuRxPktsAt11Mb_Type = Counter32
_CcMuRxPktsAt11Mb_Object = MibTableColumn
ccMuRxPktsAt11Mb = _CcMuRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 6),
    _CcMuRxPktsAt11Mb_Type()
)
ccMuRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt11Mb.setStatus("current")
_CcMuRxPktsAt12Mb_Type = Counter32
_CcMuRxPktsAt12Mb_Object = MibTableColumn
ccMuRxPktsAt12Mb = _CcMuRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 7),
    _CcMuRxPktsAt12Mb_Type()
)
ccMuRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt12Mb.setStatus("current")
_CcMuRxPktsAt18Mb_Type = Counter32
_CcMuRxPktsAt18Mb_Object = MibTableColumn
ccMuRxPktsAt18Mb = _CcMuRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 8),
    _CcMuRxPktsAt18Mb_Type()
)
ccMuRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt18Mb.setStatus("current")
_CcMuRxPktsAt22Mb_Type = Counter32
_CcMuRxPktsAt22Mb_Object = MibTableColumn
ccMuRxPktsAt22Mb = _CcMuRxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 9),
    _CcMuRxPktsAt22Mb_Type()
)
ccMuRxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt22Mb.setStatus("current")
_CcMuRxPktsAt24Mb_Type = Counter32
_CcMuRxPktsAt24Mb_Object = MibTableColumn
ccMuRxPktsAt24Mb = _CcMuRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 10),
    _CcMuRxPktsAt24Mb_Type()
)
ccMuRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt24Mb.setStatus("current")
_CcMuRxPktsAt36Mb_Type = Counter32
_CcMuRxPktsAt36Mb_Object = MibTableColumn
ccMuRxPktsAt36Mb = _CcMuRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 11),
    _CcMuRxPktsAt36Mb_Type()
)
ccMuRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt36Mb.setStatus("current")
_CcMuRxPktsAt48Mb_Type = Counter32
_CcMuRxPktsAt48Mb_Object = MibTableColumn
ccMuRxPktsAt48Mb = _CcMuRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 12),
    _CcMuRxPktsAt48Mb_Type()
)
ccMuRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt48Mb.setStatus("current")
_CcMuRxPktsAt54Mb_Type = Counter32
_CcMuRxPktsAt54Mb_Object = MibTableColumn
ccMuRxPktsAt54Mb = _CcMuRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 3, 1, 13),
    _CcMuRxPktsAt54Mb_Type()
)
ccMuRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt54Mb.setStatus("current")
_CcMuTxPktsTable_Object = MibTable
ccMuTxPktsTable = _CcMuTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4)
)
if mibBuilder.loadTexts:
    ccMuTxPktsTable.setStatus("current")
_CcMuTxPktsEntry_Object = MibTableRow
ccMuTxPktsEntry = _CcMuTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1)
)
ccMuTxPktsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxPktsEntry.setStatus("current")
_CcMuTxPktsAt1Mb_Type = Counter32
_CcMuTxPktsAt1Mb_Object = MibTableColumn
ccMuTxPktsAt1Mb = _CcMuTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 1),
    _CcMuTxPktsAt1Mb_Type()
)
ccMuTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt1Mb.setStatus("current")
_CcMuTxPktsAt2Mb_Type = Counter32
_CcMuTxPktsAt2Mb_Object = MibTableColumn
ccMuTxPktsAt2Mb = _CcMuTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 2),
    _CcMuTxPktsAt2Mb_Type()
)
ccMuTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt2Mb.setStatus("current")
_CcMuTxPktsAt5pt5Mb_Type = Counter32
_CcMuTxPktsAt5pt5Mb_Object = MibTableColumn
ccMuTxPktsAt5pt5Mb = _CcMuTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 3),
    _CcMuTxPktsAt5pt5Mb_Type()
)
ccMuTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt5pt5Mb.setStatus("current")
_CcMuTxPktsAt6Mb_Type = Counter32
_CcMuTxPktsAt6Mb_Object = MibTableColumn
ccMuTxPktsAt6Mb = _CcMuTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 4),
    _CcMuTxPktsAt6Mb_Type()
)
ccMuTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt6Mb.setStatus("current")
_CcMuTxPktsAt9Mb_Type = Counter32
_CcMuTxPktsAt9Mb_Object = MibTableColumn
ccMuTxPktsAt9Mb = _CcMuTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 5),
    _CcMuTxPktsAt9Mb_Type()
)
ccMuTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt9Mb.setStatus("current")
_CcMuTxPktsAt11Mb_Type = Counter32
_CcMuTxPktsAt11Mb_Object = MibTableColumn
ccMuTxPktsAt11Mb = _CcMuTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 6),
    _CcMuTxPktsAt11Mb_Type()
)
ccMuTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt11Mb.setStatus("current")
_CcMuTxPktsAt12Mb_Type = Counter32
_CcMuTxPktsAt12Mb_Object = MibTableColumn
ccMuTxPktsAt12Mb = _CcMuTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 7),
    _CcMuTxPktsAt12Mb_Type()
)
ccMuTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt12Mb.setStatus("current")
_CcMuTxPktsAt18Mb_Type = Counter32
_CcMuTxPktsAt18Mb_Object = MibTableColumn
ccMuTxPktsAt18Mb = _CcMuTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 8),
    _CcMuTxPktsAt18Mb_Type()
)
ccMuTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt18Mb.setStatus("current")
_CcMuTxPktsAt22Mb_Type = Counter32
_CcMuTxPktsAt22Mb_Object = MibTableColumn
ccMuTxPktsAt22Mb = _CcMuTxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 9),
    _CcMuTxPktsAt22Mb_Type()
)
ccMuTxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt22Mb.setStatus("current")
_CcMuTxPktsAt24Mb_Type = Counter32
_CcMuTxPktsAt24Mb_Object = MibTableColumn
ccMuTxPktsAt24Mb = _CcMuTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 10),
    _CcMuTxPktsAt24Mb_Type()
)
ccMuTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt24Mb.setStatus("current")
_CcMuTxPktsAt36Mb_Type = Counter32
_CcMuTxPktsAt36Mb_Object = MibTableColumn
ccMuTxPktsAt36Mb = _CcMuTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 11),
    _CcMuTxPktsAt36Mb_Type()
)
ccMuTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt36Mb.setStatus("current")
_CcMuTxPktsAt48Mb_Type = Counter32
_CcMuTxPktsAt48Mb_Object = MibTableColumn
ccMuTxPktsAt48Mb = _CcMuTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 12),
    _CcMuTxPktsAt48Mb_Type()
)
ccMuTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt48Mb.setStatus("current")
_CcMuTxPktsAt54Mb_Type = Counter32
_CcMuTxPktsAt54Mb_Object = MibTableColumn
ccMuTxPktsAt54Mb = _CcMuTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 4, 1, 13),
    _CcMuTxPktsAt54Mb_Type()
)
ccMuTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt54Mb.setStatus("current")
_CcMuRxOctetsTable_Object = MibTable
ccMuRxOctetsTable = _CcMuRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5)
)
if mibBuilder.loadTexts:
    ccMuRxOctetsTable.setStatus("current")
_CcMuRxOctetsEntry_Object = MibTableRow
ccMuRxOctetsEntry = _CcMuRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1)
)
ccMuRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuRxOctetsEntry.setStatus("current")
_CcMuRxOctetsAt1Mb_Type = Counter32
_CcMuRxOctetsAt1Mb_Object = MibTableColumn
ccMuRxOctetsAt1Mb = _CcMuRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 1),
    _CcMuRxOctetsAt1Mb_Type()
)
ccMuRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt1Mb.setStatus("current")
_CcMuRxOctetsAt2Mb_Type = Counter32
_CcMuRxOctetsAt2Mb_Object = MibTableColumn
ccMuRxOctetsAt2Mb = _CcMuRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 2),
    _CcMuRxOctetsAt2Mb_Type()
)
ccMuRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt2Mb.setStatus("current")
_CcMuRxOctetsAt5pt5Mb_Type = Counter32
_CcMuRxOctetsAt5pt5Mb_Object = MibTableColumn
ccMuRxOctetsAt5pt5Mb = _CcMuRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 3),
    _CcMuRxOctetsAt5pt5Mb_Type()
)
ccMuRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt5pt5Mb.setStatus("current")
_CcMuRxOctetsAt6Mb_Type = Counter32
_CcMuRxOctetsAt6Mb_Object = MibTableColumn
ccMuRxOctetsAt6Mb = _CcMuRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 4),
    _CcMuRxOctetsAt6Mb_Type()
)
ccMuRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt6Mb.setStatus("current")
_CcMuRxOctetsAt9Mb_Type = Counter32
_CcMuRxOctetsAt9Mb_Object = MibTableColumn
ccMuRxOctetsAt9Mb = _CcMuRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 5),
    _CcMuRxOctetsAt9Mb_Type()
)
ccMuRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt9Mb.setStatus("current")
_CcMuRxOctetsAt11Mb_Type = Counter32
_CcMuRxOctetsAt11Mb_Object = MibTableColumn
ccMuRxOctetsAt11Mb = _CcMuRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 6),
    _CcMuRxOctetsAt11Mb_Type()
)
ccMuRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt11Mb.setStatus("current")
_CcMuRxOctetsAt12Mb_Type = Counter32
_CcMuRxOctetsAt12Mb_Object = MibTableColumn
ccMuRxOctetsAt12Mb = _CcMuRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 7),
    _CcMuRxOctetsAt12Mb_Type()
)
ccMuRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt12Mb.setStatus("current")
_CcMuRxOctetsAt18Mb_Type = Counter32
_CcMuRxOctetsAt18Mb_Object = MibTableColumn
ccMuRxOctetsAt18Mb = _CcMuRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 8),
    _CcMuRxOctetsAt18Mb_Type()
)
ccMuRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt18Mb.setStatus("current")
_CcMuRxOctetsAt22Mb_Type = Counter32
_CcMuRxOctetsAt22Mb_Object = MibTableColumn
ccMuRxOctetsAt22Mb = _CcMuRxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 9),
    _CcMuRxOctetsAt22Mb_Type()
)
ccMuRxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt22Mb.setStatus("current")
_CcMuRxOctetsAt24Mb_Type = Counter32
_CcMuRxOctetsAt24Mb_Object = MibTableColumn
ccMuRxOctetsAt24Mb = _CcMuRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 10),
    _CcMuRxOctetsAt24Mb_Type()
)
ccMuRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt24Mb.setStatus("current")
_CcMuRxOctetsAt36Mb_Type = Counter32
_CcMuRxOctetsAt36Mb_Object = MibTableColumn
ccMuRxOctetsAt36Mb = _CcMuRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 11),
    _CcMuRxOctetsAt36Mb_Type()
)
ccMuRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt36Mb.setStatus("current")
_CcMuRxOctetsAt48Mb_Type = Counter32
_CcMuRxOctetsAt48Mb_Object = MibTableColumn
ccMuRxOctetsAt48Mb = _CcMuRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 12),
    _CcMuRxOctetsAt48Mb_Type()
)
ccMuRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt48Mb.setStatus("current")
_CcMuRxOctetsAt54Mb_Type = Counter32
_CcMuRxOctetsAt54Mb_Object = MibTableColumn
ccMuRxOctetsAt54Mb = _CcMuRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 5, 1, 13),
    _CcMuRxOctetsAt54Mb_Type()
)
ccMuRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt54Mb.setStatus("current")
_CcMuTxOctetsTable_Object = MibTable
ccMuTxOctetsTable = _CcMuTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6)
)
if mibBuilder.loadTexts:
    ccMuTxOctetsTable.setStatus("current")
_CcMuTxOctetsEntry_Object = MibTableRow
ccMuTxOctetsEntry = _CcMuTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1)
)
ccMuTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxOctetsEntry.setStatus("current")
_CcMuTxOctetsAt1Mb_Type = Counter32
_CcMuTxOctetsAt1Mb_Object = MibTableColumn
ccMuTxOctetsAt1Mb = _CcMuTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 1),
    _CcMuTxOctetsAt1Mb_Type()
)
ccMuTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt1Mb.setStatus("current")
_CcMuTxOctetsAt2Mb_Type = Counter32
_CcMuTxOctetsAt2Mb_Object = MibTableColumn
ccMuTxOctetsAt2Mb = _CcMuTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 2),
    _CcMuTxOctetsAt2Mb_Type()
)
ccMuTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt2Mb.setStatus("current")
_CcMuTxOctetsAt5pt5Mb_Type = Counter32
_CcMuTxOctetsAt5pt5Mb_Object = MibTableColumn
ccMuTxOctetsAt5pt5Mb = _CcMuTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 3),
    _CcMuTxOctetsAt5pt5Mb_Type()
)
ccMuTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt5pt5Mb.setStatus("current")
_CcMuTxOctetsAt6Mb_Type = Counter32
_CcMuTxOctetsAt6Mb_Object = MibTableColumn
ccMuTxOctetsAt6Mb = _CcMuTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 4),
    _CcMuTxOctetsAt6Mb_Type()
)
ccMuTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt6Mb.setStatus("current")
_CcMuTxOctetsAt9Mb_Type = Counter32
_CcMuTxOctetsAt9Mb_Object = MibTableColumn
ccMuTxOctetsAt9Mb = _CcMuTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 5),
    _CcMuTxOctetsAt9Mb_Type()
)
ccMuTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt9Mb.setStatus("current")
_CcMuTxOctetsAt11Mb_Type = Counter32
_CcMuTxOctetsAt11Mb_Object = MibTableColumn
ccMuTxOctetsAt11Mb = _CcMuTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 6),
    _CcMuTxOctetsAt11Mb_Type()
)
ccMuTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt11Mb.setStatus("current")
_CcMuTxOctetsAt12Mb_Type = Counter32
_CcMuTxOctetsAt12Mb_Object = MibTableColumn
ccMuTxOctetsAt12Mb = _CcMuTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 7),
    _CcMuTxOctetsAt12Mb_Type()
)
ccMuTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt12Mb.setStatus("current")
_CcMuTxOctetsAt18Mb_Type = Counter32
_CcMuTxOctetsAt18Mb_Object = MibTableColumn
ccMuTxOctetsAt18Mb = _CcMuTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 8),
    _CcMuTxOctetsAt18Mb_Type()
)
ccMuTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt18Mb.setStatus("current")
_CcMuTxOctetsAt22Mb_Type = Counter32
_CcMuTxOctetsAt22Mb_Object = MibTableColumn
ccMuTxOctetsAt22Mb = _CcMuTxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 9),
    _CcMuTxOctetsAt22Mb_Type()
)
ccMuTxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt22Mb.setStatus("current")
_CcMuTxOctetsAt24Mb_Type = Counter32
_CcMuTxOctetsAt24Mb_Object = MibTableColumn
ccMuTxOctetsAt24Mb = _CcMuTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 10),
    _CcMuTxOctetsAt24Mb_Type()
)
ccMuTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt24Mb.setStatus("current")
_CcMuTxOctetsAt36Mb_Type = Counter32
_CcMuTxOctetsAt36Mb_Object = MibTableColumn
ccMuTxOctetsAt36Mb = _CcMuTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 11),
    _CcMuTxOctetsAt36Mb_Type()
)
ccMuTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt36Mb.setStatus("current")
_CcMuTxOctetsAt48Mb_Type = Counter32
_CcMuTxOctetsAt48Mb_Object = MibTableColumn
ccMuTxOctetsAt48Mb = _CcMuTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 12),
    _CcMuTxOctetsAt48Mb_Type()
)
ccMuTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt48Mb.setStatus("current")
_CcMuTxOctetsAt54Mb_Type = Counter32
_CcMuTxOctetsAt54Mb_Object = MibTableColumn
ccMuTxOctetsAt54Mb = _CcMuTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 6, 1, 13),
    _CcMuTxOctetsAt54Mb_Type()
)
ccMuTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt54Mb.setStatus("current")
_CcMuTxRetriesTable_Object = MibTable
ccMuTxRetriesTable = _CcMuTxRetriesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7)
)
if mibBuilder.loadTexts:
    ccMuTxRetriesTable.setStatus("current")
_CcMuTxRetriesEntry_Object = MibTableRow
ccMuTxRetriesEntry = _CcMuTxRetriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1)
)
ccMuTxRetriesEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxRetriesEntry.setStatus("current")
_CcMuTxRetriesNone_Type = Counter32
_CcMuTxRetriesNone_Object = MibTableColumn
ccMuTxRetriesNone = _CcMuTxRetriesNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 1),
    _CcMuTxRetriesNone_Type()
)
ccMuTxRetriesNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesNone.setStatus("current")
_CcMuTxRetries01_Type = Counter32
_CcMuTxRetries01_Object = MibTableColumn
ccMuTxRetries01 = _CcMuTxRetries01_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 2),
    _CcMuTxRetries01_Type()
)
ccMuTxRetries01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries01.setStatus("current")
_CcMuTxRetries02_Type = Counter32
_CcMuTxRetries02_Object = MibTableColumn
ccMuTxRetries02 = _CcMuTxRetries02_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 3),
    _CcMuTxRetries02_Type()
)
ccMuTxRetries02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries02.setStatus("current")
_CcMuTxRetries03_Type = Counter32
_CcMuTxRetries03_Object = MibTableColumn
ccMuTxRetries03 = _CcMuTxRetries03_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 4),
    _CcMuTxRetries03_Type()
)
ccMuTxRetries03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries03.setStatus("current")
_CcMuTxRetries04_Type = Counter32
_CcMuTxRetries04_Object = MibTableColumn
ccMuTxRetries04 = _CcMuTxRetries04_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 5),
    _CcMuTxRetries04_Type()
)
ccMuTxRetries04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries04.setStatus("current")
_CcMuTxRetries05_Type = Counter32
_CcMuTxRetries05_Object = MibTableColumn
ccMuTxRetries05 = _CcMuTxRetries05_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 6),
    _CcMuTxRetries05_Type()
)
ccMuTxRetries05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries05.setStatus("current")
_CcMuTxRetries06_Type = Counter32
_CcMuTxRetries06_Object = MibTableColumn
ccMuTxRetries06 = _CcMuTxRetries06_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 7),
    _CcMuTxRetries06_Type()
)
ccMuTxRetries06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries06.setStatus("current")
_CcMuTxRetries07_Type = Counter32
_CcMuTxRetries07_Object = MibTableColumn
ccMuTxRetries07 = _CcMuTxRetries07_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 8),
    _CcMuTxRetries07_Type()
)
ccMuTxRetries07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries07.setStatus("current")
_CcMuTxRetries08_Type = Counter32
_CcMuTxRetries08_Object = MibTableColumn
ccMuTxRetries08 = _CcMuTxRetries08_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 9),
    _CcMuTxRetries08_Type()
)
ccMuTxRetries08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries08.setStatus("current")
_CcMuTxRetries09_Type = Counter32
_CcMuTxRetries09_Object = MibTableColumn
ccMuTxRetries09 = _CcMuTxRetries09_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 10),
    _CcMuTxRetries09_Type()
)
ccMuTxRetries09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries09.setStatus("current")
_CcMuTxRetries10_Type = Counter32
_CcMuTxRetries10_Object = MibTableColumn
ccMuTxRetries10 = _CcMuTxRetries10_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 11),
    _CcMuTxRetries10_Type()
)
ccMuTxRetries10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries10.setStatus("current")
_CcMuTxRetries11_Type = Counter32
_CcMuTxRetries11_Object = MibTableColumn
ccMuTxRetries11 = _CcMuTxRetries11_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 12),
    _CcMuTxRetries11_Type()
)
ccMuTxRetries11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries11.setStatus("current")
_CcMuTxRetries12_Type = Counter32
_CcMuTxRetries12_Object = MibTableColumn
ccMuTxRetries12 = _CcMuTxRetries12_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 13),
    _CcMuTxRetries12_Type()
)
ccMuTxRetries12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries12.setStatus("current")
_CcMuTxRetries13_Type = Counter32
_CcMuTxRetries13_Object = MibTableColumn
ccMuTxRetries13 = _CcMuTxRetries13_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 14),
    _CcMuTxRetries13_Type()
)
ccMuTxRetries13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries13.setStatus("current")
_CcMuTxRetries14_Type = Counter32
_CcMuTxRetries14_Object = MibTableColumn
ccMuTxRetries14 = _CcMuTxRetries14_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 15),
    _CcMuTxRetries14_Type()
)
ccMuTxRetries14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries14.setStatus("current")
_CcMuTxRetries15_Type = Counter32
_CcMuTxRetries15_Object = MibTableColumn
ccMuTxRetries15 = _CcMuTxRetries15_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 16),
    _CcMuTxRetries15_Type()
)
ccMuTxRetries15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries15.setStatus("deprecated")
_CcMuTxRetriesFailed_Type = Counter32
_CcMuTxRetriesFailed_Object = MibTableColumn
ccMuTxRetriesFailed = _CcMuTxRetriesFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 17),
    _CcMuTxRetriesFailed_Type()
)
ccMuTxRetriesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesFailed.setStatus("current")
_CcMuTxRetriesTotal_Type = Counter32
_CcMuTxRetriesTotal_Object = MibTableColumn
ccMuTxRetriesTotal = _CcMuTxRetriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 18),
    _CcMuTxRetriesTotal_Type()
)
ccMuTxRetriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesTotal.setStatus("current")


class _CcMuTxRetriesMostRecent_Type(Integer32):
    """Custom type ccMuTxRetriesMostRecent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CcMuTxRetriesMostRecent_Type.__name__ = "Integer32"
_CcMuTxRetriesMostRecent_Object = MibTableColumn
ccMuTxRetriesMostRecent = _CcMuTxRetriesMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 7, 1, 19),
    _CcMuTxRetriesMostRecent_Type()
)
ccMuTxRetriesMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesMostRecent.setStatus("current")
_CcMuLastMac_Type = DisplayString
_CcMuLastMac_Object = MibScalar
ccMuLastMac = _CcMuLastMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 8),
    _CcMuLastMac_Type()
)
ccMuLastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastMac.setStatus("current")


class _CcMuLastReason_Type(Integer32):
    """Custom type ccMuLastReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("aclViolation", 2),
          ("timeout", 3),
          ("associationFailed", 4),
          ("authenticationFailedOn802dot1x", 5),
          ("kerberosWrongUsername", 6))
    )


_CcMuLastReason_Type.__name__ = "Integer32"
_CcMuLastReason_Object = MibScalar
ccMuLastReason = _CcMuLastReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 9),
    _CcMuLastReason_Type()
)
ccMuLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastReason.setStatus("current")
_CcMuLastPortal_Type = DisplayString
_CcMuLastPortal_Object = MibScalar
ccMuLastPortal = _CcMuLastPortal_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 10),
    _CcMuLastPortal_Type()
)
ccMuLastPortal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastPortal.setStatus("current")
_CcMuRfSum_ObjectIdentity = ObjectIdentity
ccMuRfSum = _CcMuRfSum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100)
)
_CcMuTxRetriesOctetsTable_Object = MibTable
ccMuTxRetriesOctetsTable = _CcMuTxRetriesOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1)
)
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsTable.setStatus("current")
_CcMuTxRetriesOctetsEntry_Object = MibTableRow
ccMuTxRetriesOctetsEntry = _CcMuTxRetriesOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1)
)
ccMuTxRetriesOctetsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsEntry.setStatus("current")
_CcMuTxRetriesOctetsNone_Type = Counter32
_CcMuTxRetriesOctetsNone_Object = MibTableColumn
ccMuTxRetriesOctetsNone = _CcMuTxRetriesOctetsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 1),
    _CcMuTxRetriesOctetsNone_Type()
)
ccMuTxRetriesOctetsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsNone.setStatus("current")
_CcMuTxRetriesOctets01_Type = Counter32
_CcMuTxRetriesOctets01_Object = MibTableColumn
ccMuTxRetriesOctets01 = _CcMuTxRetriesOctets01_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 2),
    _CcMuTxRetriesOctets01_Type()
)
ccMuTxRetriesOctets01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets01.setStatus("current")
_CcMuTxRetriesOctets02_Type = Counter32
_CcMuTxRetriesOctets02_Object = MibTableColumn
ccMuTxRetriesOctets02 = _CcMuTxRetriesOctets02_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 3),
    _CcMuTxRetriesOctets02_Type()
)
ccMuTxRetriesOctets02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets02.setStatus("current")
_CcMuTxRetriesOctets03_Type = Counter32
_CcMuTxRetriesOctets03_Object = MibTableColumn
ccMuTxRetriesOctets03 = _CcMuTxRetriesOctets03_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 4),
    _CcMuTxRetriesOctets03_Type()
)
ccMuTxRetriesOctets03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets03.setStatus("current")
_CcMuTxRetriesOctets04_Type = Counter32
_CcMuTxRetriesOctets04_Object = MibTableColumn
ccMuTxRetriesOctets04 = _CcMuTxRetriesOctets04_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 5),
    _CcMuTxRetriesOctets04_Type()
)
ccMuTxRetriesOctets04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets04.setStatus("current")
_CcMuTxRetriesOctets05_Type = Counter32
_CcMuTxRetriesOctets05_Object = MibTableColumn
ccMuTxRetriesOctets05 = _CcMuTxRetriesOctets05_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 6),
    _CcMuTxRetriesOctets05_Type()
)
ccMuTxRetriesOctets05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets05.setStatus("current")
_CcMuTxRetriesOctets06_Type = Counter32
_CcMuTxRetriesOctets06_Object = MibTableColumn
ccMuTxRetriesOctets06 = _CcMuTxRetriesOctets06_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 7),
    _CcMuTxRetriesOctets06_Type()
)
ccMuTxRetriesOctets06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets06.setStatus("current")
_CcMuTxRetriesOctets07_Type = Counter32
_CcMuTxRetriesOctets07_Object = MibTableColumn
ccMuTxRetriesOctets07 = _CcMuTxRetriesOctets07_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 8),
    _CcMuTxRetriesOctets07_Type()
)
ccMuTxRetriesOctets07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets07.setStatus("current")
_CcMuTxRetriesOctets08_Type = Counter32
_CcMuTxRetriesOctets08_Object = MibTableColumn
ccMuTxRetriesOctets08 = _CcMuTxRetriesOctets08_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 9),
    _CcMuTxRetriesOctets08_Type()
)
ccMuTxRetriesOctets08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets08.setStatus("current")
_CcMuTxRetriesOctets09_Type = Counter32
_CcMuTxRetriesOctets09_Object = MibTableColumn
ccMuTxRetriesOctets09 = _CcMuTxRetriesOctets09_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 10),
    _CcMuTxRetriesOctets09_Type()
)
ccMuTxRetriesOctets09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets09.setStatus("current")
_CcMuTxRetriesOctets10_Type = Counter32
_CcMuTxRetriesOctets10_Object = MibTableColumn
ccMuTxRetriesOctets10 = _CcMuTxRetriesOctets10_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 11),
    _CcMuTxRetriesOctets10_Type()
)
ccMuTxRetriesOctets10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets10.setStatus("current")
_CcMuTxRetriesOctets11_Type = Counter32
_CcMuTxRetriesOctets11_Object = MibTableColumn
ccMuTxRetriesOctets11 = _CcMuTxRetriesOctets11_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 12),
    _CcMuTxRetriesOctets11_Type()
)
ccMuTxRetriesOctets11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets11.setStatus("current")
_CcMuTxRetriesOctets12_Type = Counter32
_CcMuTxRetriesOctets12_Object = MibTableColumn
ccMuTxRetriesOctets12 = _CcMuTxRetriesOctets12_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 13),
    _CcMuTxRetriesOctets12_Type()
)
ccMuTxRetriesOctets12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets12.setStatus("current")
_CcMuTxRetriesOctets13_Type = Counter32
_CcMuTxRetriesOctets13_Object = MibTableColumn
ccMuTxRetriesOctets13 = _CcMuTxRetriesOctets13_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 14),
    _CcMuTxRetriesOctets13_Type()
)
ccMuTxRetriesOctets13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets13.setStatus("current")
_CcMuTxRetriesOctets14_Type = Counter32
_CcMuTxRetriesOctets14_Object = MibTableColumn
ccMuTxRetriesOctets14 = _CcMuTxRetriesOctets14_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 15),
    _CcMuTxRetriesOctets14_Type()
)
ccMuTxRetriesOctets14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets14.setStatus("current")
_CcMuTxRetriesOctets15_Type = Counter32
_CcMuTxRetriesOctets15_Object = MibTableColumn
ccMuTxRetriesOctets15 = _CcMuTxRetriesOctets15_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 16),
    _CcMuTxRetriesOctets15_Type()
)
ccMuTxRetriesOctets15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets15.setStatus("deprecated")
_CcMuTxRetriesOctetsFailed_Type = Counter32
_CcMuTxRetriesOctetsFailed_Object = MibTableColumn
ccMuTxRetriesOctetsFailed = _CcMuTxRetriesOctetsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 1, 1, 17),
    _CcMuTxRetriesOctetsFailed_Type()
)
ccMuTxRetriesOctetsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsFailed.setStatus("current")
_CcMuSigStatsTable_Object = MibTable
ccMuSigStatsTable = _CcMuSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2)
)
if mibBuilder.loadTexts:
    ccMuSigStatsTable.setStatus("current")
_CcMuSigStatsEntry_Object = MibTableRow
ccMuSigStatsEntry = _CcMuSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1)
)
ccMuSigStatsEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuSigStatsEntry.setStatus("current")
_CcMuSigStatsNumPkts_Type = Counter32
_CcMuSigStatsNumPkts_Object = MibTableColumn
ccMuSigStatsNumPkts = _CcMuSigStatsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 1),
    _CcMuSigStatsNumPkts_Type()
)
ccMuSigStatsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNumPkts.setStatus("current")
_CcMuSigStatsSignalBest_Type = Integer32
_CcMuSigStatsSignalBest_Object = MibTableColumn
ccMuSigStatsSignalBest = _CcMuSigStatsSignalBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 2),
    _CcMuSigStatsSignalBest_Type()
)
ccMuSigStatsSignalBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalBest.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalBest.setUnits("dBm")
_CcMuSigStatsSignalWorst_Type = Integer32
_CcMuSigStatsSignalWorst_Object = MibTableColumn
ccMuSigStatsSignalWorst = _CcMuSigStatsSignalWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 3),
    _CcMuSigStatsSignalWorst_Type()
)
ccMuSigStatsSignalWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalWorst.setUnits("dBm")
_CcMuSigStatsSignalSum_Type = Integer32
_CcMuSigStatsSignalSum_Object = MibTableColumn
ccMuSigStatsSignalSum = _CcMuSigStatsSignalSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 4),
    _CcMuSigStatsSignalSum_Type()
)
ccMuSigStatsSignalSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSum.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSum.setUnits("dBm")
_CcMuSigStatsSignalSumSquares_Type = Counter64
_CcMuSigStatsSignalSumSquares_Object = MibTableColumn
ccMuSigStatsSignalSumSquares = _CcMuSigStatsSignalSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 5),
    _CcMuSigStatsSignalSumSquares_Type()
)
ccMuSigStatsSignalSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSumSquares.setUnits("dBm")
_CcMuSigStatsSignalMostRecent_Type = Integer32
_CcMuSigStatsSignalMostRecent_Object = MibTableColumn
ccMuSigStatsSignalMostRecent = _CcMuSigStatsSignalMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 6),
    _CcMuSigStatsSignalMostRecent_Type()
)
ccMuSigStatsSignalMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalMostRecent.setUnits("dBm")
_CcMuSigStatsNoiseBest_Type = Integer32
_CcMuSigStatsNoiseBest_Object = MibTableColumn
ccMuSigStatsNoiseBest = _CcMuSigStatsNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 7),
    _CcMuSigStatsNoiseBest_Type()
)
ccMuSigStatsNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseBest.setUnits("dBm")
_CcMuSigStatsNoiseWorst_Type = Integer32
_CcMuSigStatsNoiseWorst_Object = MibTableColumn
ccMuSigStatsNoiseWorst = _CcMuSigStatsNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 8),
    _CcMuSigStatsNoiseWorst_Type()
)
ccMuSigStatsNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseWorst.setUnits("dBm")
_CcMuSigStatsNoiseSum_Type = Integer32
_CcMuSigStatsNoiseSum_Object = MibTableColumn
ccMuSigStatsNoiseSum = _CcMuSigStatsNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 9),
    _CcMuSigStatsNoiseSum_Type()
)
ccMuSigStatsNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSum.setUnits("dBm")
_CcMuSigStatsNoiseSumSquares_Type = Counter64
_CcMuSigStatsNoiseSumSquares_Object = MibTableColumn
ccMuSigStatsNoiseSumSquares = _CcMuSigStatsNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 10),
    _CcMuSigStatsNoiseSumSquares_Type()
)
ccMuSigStatsNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSumSquares.setUnits("dBm")
_CcMuSigStatsNoiseMostRecent_Type = Integer32
_CcMuSigStatsNoiseMostRecent_Object = MibTableColumn
ccMuSigStatsNoiseMostRecent = _CcMuSigStatsNoiseMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 11),
    _CcMuSigStatsNoiseMostRecent_Type()
)
ccMuSigStatsNoiseMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseMostRecent.setUnits("dBm")
_CcMuSigStatsSnrBest_Type = Integer32
_CcMuSigStatsSnrBest_Object = MibTableColumn
ccMuSigStatsSnrBest = _CcMuSigStatsSnrBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 12),
    _CcMuSigStatsSnrBest_Type()
)
ccMuSigStatsSnrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrBest.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrBest.setUnits("dB")
_CcMuSigStatsSnrWorst_Type = Integer32
_CcMuSigStatsSnrWorst_Object = MibTableColumn
ccMuSigStatsSnrWorst = _CcMuSigStatsSnrWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 13),
    _CcMuSigStatsSnrWorst_Type()
)
ccMuSigStatsSnrWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrWorst.setUnits("dB")
_CcMuSigStatsSnrSum_Type = Counter64
_CcMuSigStatsSnrSum_Object = MibTableColumn
ccMuSigStatsSnrSum = _CcMuSigStatsSnrSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 14),
    _CcMuSigStatsSnrSum_Type()
)
ccMuSigStatsSnrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSum.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSum.setUnits("dB")
_CcMuSigStatsSnrSumSquares_Type = Counter64
_CcMuSigStatsSnrSumSquares_Object = MibTableColumn
ccMuSigStatsSnrSumSquares = _CcMuSigStatsSnrSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 15),
    _CcMuSigStatsSnrSumSquares_Type()
)
ccMuSigStatsSnrSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSumSquares.setUnits("dB")
_CcMuSigStatsSnrMostRecent_Type = Integer32
_CcMuSigStatsSnrMostRecent_Object = MibTableColumn
ccMuSigStatsSnrMostRecent = _CcMuSigStatsSnrMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 2, 1, 16),
    _CcMuSigStatsSnrMostRecent_Type()
)
ccMuSigStatsSnrMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrMostRecent.setUnits("dB")
_CcMuSumStatsShortTable_Object = MibTable
ccMuSumStatsShortTable = _CcMuSumStatsShortTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3)
)
if mibBuilder.loadTexts:
    ccMuSumStatsShortTable.setStatus("current")
_CcMuSumStatsShortEntry_Object = MibTableRow
ccMuSumStatsShortEntry = _CcMuSumStatsShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1)
)
ccMuSumStatsShortEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuSumStatsShortEntry.setStatus("current")
_CcMuSumStatsShortTimestamp_Type = TimeTicks
_CcMuSumStatsShortTimestamp_Object = MibTableColumn
ccMuSumStatsShortTimestamp = _CcMuSumStatsShortTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 1),
    _CcMuSumStatsShortTimestamp_Type()
)
ccMuSumStatsShortTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortTimestamp.setStatus("current")
_CcMuSumStatsShortNumPkts_Type = Unsigned32
_CcMuSumStatsShortNumPkts_Object = MibTableColumn
ccMuSumStatsShortNumPkts = _CcMuSumStatsShortNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 2),
    _CcMuSumStatsShortNumPkts_Type()
)
ccMuSumStatsShortNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortNumPkts.setUnits("packets")
_CcMuSumStatsShortPktsPerSec100_Type = ScaleBy100
_CcMuSumStatsShortPktsPerSec100_Object = MibTableColumn
ccMuSumStatsShortPktsPerSec100 = _CcMuSumStatsShortPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 3),
    _CcMuSumStatsShortPktsPerSec100_Type()
)
ccMuSumStatsShortPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSec100.setUnits("pkts per sec x100")
_CcMuSumStatsShortPktsPerSecTx100_Type = ScaleBy100
_CcMuSumStatsShortPktsPerSecTx100_Object = MibTableColumn
ccMuSumStatsShortPktsPerSecTx100 = _CcMuSumStatsShortPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 4),
    _CcMuSumStatsShortPktsPerSecTx100_Type()
)
ccMuSumStatsShortPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecTx100.setUnits("pkts per sec x100")
_CcMuSumStatsShortPktsPerSecRx100_Type = ScaleBy100
_CcMuSumStatsShortPktsPerSecRx100_Object = MibTableColumn
ccMuSumStatsShortPktsPerSecRx100 = _CcMuSumStatsShortPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 5),
    _CcMuSumStatsShortPktsPerSecRx100_Type()
)
ccMuSumStatsShortPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecRx100.setUnits("pkts per sec x100")
_CcMuSumStatsShortThroughput_Type = Unsigned32
_CcMuSumStatsShortThroughput_Object = MibTableColumn
ccMuSumStatsShortThroughput = _CcMuSumStatsShortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 6),
    _CcMuSumStatsShortThroughput_Type()
)
ccMuSumStatsShortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughput.setUnits("bits per second")
_CcMuSumStatsShortThroughputTx_Type = Unsigned32
_CcMuSumStatsShortThroughputTx_Object = MibTableColumn
ccMuSumStatsShortThroughputTx = _CcMuSumStatsShortThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 7),
    _CcMuSumStatsShortThroughputTx_Type()
)
ccMuSumStatsShortThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputTx.setUnits("bits per second")
_CcMuSumStatsShortThroughputRx_Type = Unsigned32
_CcMuSumStatsShortThroughputRx_Object = MibTableColumn
ccMuSumStatsShortThroughputRx = _CcMuSumStatsShortThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 8),
    _CcMuSumStatsShortThroughputRx_Type()
)
ccMuSumStatsShortThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputRx.setUnits("bits per second")
_CcMuSumStatsShortAvgBitSpeed_Type = Unsigned32
_CcMuSumStatsShortAvgBitSpeed_Object = MibTableColumn
ccMuSumStatsShortAvgBitSpeed = _CcMuSumStatsShortAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 9),
    _CcMuSumStatsShortAvgBitSpeed_Type()
)
ccMuSumStatsShortAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgBitSpeed.setUnits("bits per second")
_CcMuSumStatsShortAvgMuSignal_Type = Integer32
_CcMuSumStatsShortAvgMuSignal_Object = MibTableColumn
ccMuSumStatsShortAvgMuSignal = _CcMuSumStatsShortAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 10),
    _CcMuSumStatsShortAvgMuSignal_Type()
)
ccMuSumStatsShortAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSignal.setUnits("dBm")
_CcMuSumStatsShortAvgMuNoise_Type = Integer32
_CcMuSumStatsShortAvgMuNoise_Object = MibTableColumn
ccMuSumStatsShortAvgMuNoise = _CcMuSumStatsShortAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 11),
    _CcMuSumStatsShortAvgMuNoise_Type()
)
ccMuSumStatsShortAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuNoise.setUnits("dBm")
_CcMuSumStatsShortAvgMuSnr_Type = Integer32
_CcMuSumStatsShortAvgMuSnr_Object = MibTableColumn
ccMuSumStatsShortAvgMuSnr = _CcMuSumStatsShortAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 12),
    _CcMuSumStatsShortAvgMuSnr_Type()
)
ccMuSumStatsShortAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSnr.setUnits("dB")
_CcMuSumStatsShortPp10kNUcastPkts_Type = PartsPer10k
_CcMuSumStatsShortPp10kNUcastPkts_Object = MibTableColumn
ccMuSumStatsShortPp10kNUcastPkts = _CcMuSumStatsShortPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 13),
    _CcMuSumStatsShortPp10kNUcastPkts_Type()
)
ccMuSumStatsShortPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kNUcastPkts.setUnits("parts-per-10000")
_CcMuSumStatsShortPp10kTxWithRetries_Type = PartsPer10k
_CcMuSumStatsShortPp10kTxWithRetries_Object = MibTableColumn
ccMuSumStatsShortPp10kTxWithRetries = _CcMuSumStatsShortPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 14),
    _CcMuSumStatsShortPp10kTxWithRetries_Type()
)
ccMuSumStatsShortPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kTxWithRetries.setUnits("parts-per-10000")
_CcMuSumStatsShortPp10kDropped_Type = PartsPer10k
_CcMuSumStatsShortPp10kDropped_Object = MibTableColumn
ccMuSumStatsShortPp10kDropped = _CcMuSumStatsShortPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 15),
    _CcMuSumStatsShortPp10kDropped_Type()
)
ccMuSumStatsShortPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kDropped.setUnits("parts-per-10000")
_CcMuSumStatsShortTxAvgRetries100_Type = ScaleBy100
_CcMuSumStatsShortTxAvgRetries100_Object = MibTableColumn
ccMuSumStatsShortTxAvgRetries100 = _CcMuSumStatsShortTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 16),
    _CcMuSumStatsShortTxAvgRetries100_Type()
)
ccMuSumStatsShortTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortTxAvgRetries100.setUnits("average x100")
_CcMuSumStatsShortPp10kRxUndecrypt_Type = PartsPer10k
_CcMuSumStatsShortPp10kRxUndecrypt_Object = MibTableColumn
ccMuSumStatsShortPp10kRxUndecrypt = _CcMuSumStatsShortPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 3, 1, 17),
    _CcMuSumStatsShortPp10kRxUndecrypt_Type()
)
ccMuSumStatsShortPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kRxUndecrypt.setUnits("parts-per-10000")
_CcMuSumStatsLongTable_Object = MibTable
ccMuSumStatsLongTable = _CcMuSumStatsLongTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4)
)
if mibBuilder.loadTexts:
    ccMuSumStatsLongTable.setStatus("current")
_CcMuSumStatsLongEntry_Object = MibTableRow
ccMuSumStatsLongEntry = _CcMuSumStatsLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1)
)
ccMuSumStatsLongEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuSumStatsLongEntry.setStatus("current")
_CcMuSumStatsLongTimestamp_Type = TimeTicks
_CcMuSumStatsLongTimestamp_Object = MibTableColumn
ccMuSumStatsLongTimestamp = _CcMuSumStatsLongTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 1),
    _CcMuSumStatsLongTimestamp_Type()
)
ccMuSumStatsLongTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongTimestamp.setStatus("current")
_CcMuSumStatsLongNumPkts_Type = Unsigned32
_CcMuSumStatsLongNumPkts_Object = MibTableColumn
ccMuSumStatsLongNumPkts = _CcMuSumStatsLongNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 2),
    _CcMuSumStatsLongNumPkts_Type()
)
ccMuSumStatsLongNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongNumPkts.setUnits("packets")
_CcMuSumStatsLongPktsPerSec100_Type = ScaleBy100
_CcMuSumStatsLongPktsPerSec100_Object = MibTableColumn
ccMuSumStatsLongPktsPerSec100 = _CcMuSumStatsLongPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 3),
    _CcMuSumStatsLongPktsPerSec100_Type()
)
ccMuSumStatsLongPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSec100.setUnits("pkts per sec x100")
_CcMuSumStatsLongPktsPerSecTx100_Type = ScaleBy100
_CcMuSumStatsLongPktsPerSecTx100_Object = MibTableColumn
ccMuSumStatsLongPktsPerSecTx100 = _CcMuSumStatsLongPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 4),
    _CcMuSumStatsLongPktsPerSecTx100_Type()
)
ccMuSumStatsLongPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecTx100.setUnits("pkts per sec x100")
_CcMuSumStatsLongPktsPerSecRx100_Type = ScaleBy100
_CcMuSumStatsLongPktsPerSecRx100_Object = MibTableColumn
ccMuSumStatsLongPktsPerSecRx100 = _CcMuSumStatsLongPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 5),
    _CcMuSumStatsLongPktsPerSecRx100_Type()
)
ccMuSumStatsLongPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecRx100.setUnits("pkts per sec x100")
_CcMuSumStatsLongThroughput_Type = Unsigned32
_CcMuSumStatsLongThroughput_Object = MibTableColumn
ccMuSumStatsLongThroughput = _CcMuSumStatsLongThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 6),
    _CcMuSumStatsLongThroughput_Type()
)
ccMuSumStatsLongThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughput.setUnits("bits per second")
_CcMuSumStatsLongThroughputTx_Type = Unsigned32
_CcMuSumStatsLongThroughputTx_Object = MibTableColumn
ccMuSumStatsLongThroughputTx = _CcMuSumStatsLongThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 7),
    _CcMuSumStatsLongThroughputTx_Type()
)
ccMuSumStatsLongThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputTx.setUnits("bits per second")
_CcMuSumStatsLongThroughputRx_Type = Unsigned32
_CcMuSumStatsLongThroughputRx_Object = MibTableColumn
ccMuSumStatsLongThroughputRx = _CcMuSumStatsLongThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 8),
    _CcMuSumStatsLongThroughputRx_Type()
)
ccMuSumStatsLongThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputRx.setUnits("bits per second")
_CcMuSumStatsLongAvgBitSpeed_Type = Unsigned32
_CcMuSumStatsLongAvgBitSpeed_Object = MibTableColumn
ccMuSumStatsLongAvgBitSpeed = _CcMuSumStatsLongAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 9),
    _CcMuSumStatsLongAvgBitSpeed_Type()
)
ccMuSumStatsLongAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgBitSpeed.setUnits("bits per second")
_CcMuSumStatsLongAvgMuSignal_Type = Integer32
_CcMuSumStatsLongAvgMuSignal_Object = MibTableColumn
ccMuSumStatsLongAvgMuSignal = _CcMuSumStatsLongAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 10),
    _CcMuSumStatsLongAvgMuSignal_Type()
)
ccMuSumStatsLongAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSignal.setUnits("dBm")
_CcMuSumStatsLongAvgMuNoise_Type = Integer32
_CcMuSumStatsLongAvgMuNoise_Object = MibTableColumn
ccMuSumStatsLongAvgMuNoise = _CcMuSumStatsLongAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 11),
    _CcMuSumStatsLongAvgMuNoise_Type()
)
ccMuSumStatsLongAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuNoise.setUnits("dBm")
_CcMuSumStatsLongAvgMuSnr_Type = Integer32
_CcMuSumStatsLongAvgMuSnr_Object = MibTableColumn
ccMuSumStatsLongAvgMuSnr = _CcMuSumStatsLongAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 12),
    _CcMuSumStatsLongAvgMuSnr_Type()
)
ccMuSumStatsLongAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSnr.setUnits("dB")
_CcMuSumStatsLongPp10kNUcastPkts_Type = PartsPer10k
_CcMuSumStatsLongPp10kNUcastPkts_Object = MibTableColumn
ccMuSumStatsLongPp10kNUcastPkts = _CcMuSumStatsLongPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 13),
    _CcMuSumStatsLongPp10kNUcastPkts_Type()
)
ccMuSumStatsLongPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kNUcastPkts.setUnits("parts-per-10000")
_CcMuSumStatsLongPp10kTxWithRetries_Type = PartsPer10k
_CcMuSumStatsLongPp10kTxWithRetries_Object = MibTableColumn
ccMuSumStatsLongPp10kTxWithRetries = _CcMuSumStatsLongPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 14),
    _CcMuSumStatsLongPp10kTxWithRetries_Type()
)
ccMuSumStatsLongPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kTxWithRetries.setUnits("parts-per-10000")
_CcMuSumStatsLongPp10kDropped_Type = PartsPer10k
_CcMuSumStatsLongPp10kDropped_Object = MibTableColumn
ccMuSumStatsLongPp10kDropped = _CcMuSumStatsLongPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 15),
    _CcMuSumStatsLongPp10kDropped_Type()
)
ccMuSumStatsLongPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kDropped.setUnits("parts-per-10000")
_CcMuSumStatsLongTxAvgRetries100_Type = ScaleBy100
_CcMuSumStatsLongTxAvgRetries100_Object = MibTableColumn
ccMuSumStatsLongTxAvgRetries100 = _CcMuSumStatsLongTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 16),
    _CcMuSumStatsLongTxAvgRetries100_Type()
)
ccMuSumStatsLongTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongTxAvgRetries100.setUnits("average x100")
_CcMuSumStatsLongPp10kRxUndecrypt_Type = PartsPer10k
_CcMuSumStatsLongPp10kRxUndecrypt_Object = MibTableColumn
ccMuSumStatsLongPp10kRxUndecrypt = _CcMuSumStatsLongPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 16, 3, 100, 4, 1, 17),
    _CcMuSumStatsLongPp10kRxUndecrypt_Type()
)
ccMuSumStatsLongPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kRxUndecrypt.setUnits("parts-per-10000")
_CcWME_ObjectIdentity = ObjectIdentity
ccWME = _CcWME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 18)
)
_CcWMEprofileTable_Object = MibTable
ccWMEprofileTable = _CcWMEprofileTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5)
)
if mibBuilder.loadTexts:
    ccWMEprofileTable.setStatus("current")
_CcWMEprofileEntry_Object = MibTableRow
ccWMEprofileEntry = _CcWMEprofileEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1)
)
ccWMEprofileEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccWMEprofileIndex"),
)
if mibBuilder.loadTexts:
    ccWMEprofileEntry.setStatus("current")


class _CcWMEprofileIndex_Type(Integer32):
    """Custom type ccWMEprofileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcWMEprofileIndex_Type.__name__ = "Integer32"
_CcWMEprofileIndex_Object = MibTableColumn
ccWMEprofileIndex = _CcWMEprofileIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 1),
    _CcWMEprofileIndex_Type()
)
ccWMEprofileIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWMEprofileIndex.setStatus("current")
_CcWMEprofilename_Type = DisplayString
_CcWMEprofilename_Object = MibTableColumn
ccWMEprofilename = _CcWMEprofilename_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 2),
    _CcWMEprofilename_Type()
)
ccWMEprofilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofilename.setStatus("current")
_CcWMEprofileDesc_Type = DisplayString
_CcWMEprofileDesc_Object = MibTableColumn
ccWMEprofileDesc = _CcWMEprofileDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 3),
    _CcWMEprofileDesc_Type()
)
ccWMEprofileDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileDesc.setStatus("current")


class _CcWMEprofileAc1VoEcwmin_Type(Integer32):
    """Custom type ccWMEprofileAc1VoEcwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc1VoEcwmin_Type.__name__ = "Integer32"
_CcWMEprofileAc1VoEcwmin_Object = MibTableColumn
ccWMEprofileAc1VoEcwmin = _CcWMEprofileAc1VoEcwmin_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 4),
    _CcWMEprofileAc1VoEcwmin_Type()
)
ccWMEprofileAc1VoEcwmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc1VoEcwmin.setStatus("current")


class _CcWMEprofileAc1VoEcwmax_Type(Integer32):
    """Custom type ccWMEprofileAc1VoEcwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc1VoEcwmax_Type.__name__ = "Integer32"
_CcWMEprofileAc1VoEcwmax_Object = MibTableColumn
ccWMEprofileAc1VoEcwmax = _CcWMEprofileAc1VoEcwmax_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 5),
    _CcWMEprofileAc1VoEcwmax_Type()
)
ccWMEprofileAc1VoEcwmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc1VoEcwmax.setStatus("current")


class _CcWMEprofileAc1VoTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc1VoTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc1VoTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc1VoTxopLimit_Object = MibTableColumn
ccWMEprofileAc1VoTxopLimit = _CcWMEprofileAc1VoTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 6),
    _CcWMEprofileAc1VoTxopLimit_Type()
)
ccWMEprofileAc1VoTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc1VoTxopLimit.setStatus("current")


class _CcWMEprofileAc1VoAgTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc1VoAgTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc1VoAgTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc1VoAgTxopLimit_Object = MibTableColumn
ccWMEprofileAc1VoAgTxopLimit = _CcWMEprofileAc1VoAgTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 7),
    _CcWMEprofileAc1VoAgTxopLimit_Type()
)
ccWMEprofileAc1VoAgTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc1VoAgTxopLimit.setStatus("current")


class _CcWMEprofileAc1VoAifsn_Type(Integer32):
    """Custom type ccWMEprofileAc1VoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc1VoAifsn_Type.__name__ = "Integer32"
_CcWMEprofileAc1VoAifsn_Object = MibTableColumn
ccWMEprofileAc1VoAifsn = _CcWMEprofileAc1VoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 8),
    _CcWMEprofileAc1VoAifsn_Type()
)
ccWMEprofileAc1VoAifsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc1VoAifsn.setStatus("current")


class _CcWMEprofileAc2ViEcwmin_Type(Integer32):
    """Custom type ccWMEprofileAc2ViEcwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc2ViEcwmin_Type.__name__ = "Integer32"
_CcWMEprofileAc2ViEcwmin_Object = MibTableColumn
ccWMEprofileAc2ViEcwmin = _CcWMEprofileAc2ViEcwmin_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 9),
    _CcWMEprofileAc2ViEcwmin_Type()
)
ccWMEprofileAc2ViEcwmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc2ViEcwmin.setStatus("current")


class _CcWMEprofileAc2ViEcwmax_Type(Integer32):
    """Custom type ccWMEprofileAc2ViEcwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc2ViEcwmax_Type.__name__ = "Integer32"
_CcWMEprofileAc2ViEcwmax_Object = MibTableColumn
ccWMEprofileAc2ViEcwmax = _CcWMEprofileAc2ViEcwmax_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 10),
    _CcWMEprofileAc2ViEcwmax_Type()
)
ccWMEprofileAc2ViEcwmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc2ViEcwmax.setStatus("current")


class _CcWMEprofileAc2ViTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc2ViTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc2ViTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc2ViTxopLimit_Object = MibTableColumn
ccWMEprofileAc2ViTxopLimit = _CcWMEprofileAc2ViTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 11),
    _CcWMEprofileAc2ViTxopLimit_Type()
)
ccWMEprofileAc2ViTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc2ViTxopLimit.setStatus("current")


class _CcWMEprofileAc2ViAgTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc2ViAgTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc2ViAgTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc2ViAgTxopLimit_Object = MibTableColumn
ccWMEprofileAc2ViAgTxopLimit = _CcWMEprofileAc2ViAgTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 12),
    _CcWMEprofileAc2ViAgTxopLimit_Type()
)
ccWMEprofileAc2ViAgTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc2ViAgTxopLimit.setStatus("current")


class _CcWMEprofileAc2ViAifsn_Type(Integer32):
    """Custom type ccWMEprofileAc2ViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc2ViAifsn_Type.__name__ = "Integer32"
_CcWMEprofileAc2ViAifsn_Object = MibTableColumn
ccWMEprofileAc2ViAifsn = _CcWMEprofileAc2ViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 13),
    _CcWMEprofileAc2ViAifsn_Type()
)
ccWMEprofileAc2ViAifsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc2ViAifsn.setStatus("current")


class _CcWMEprofileAc3BeEcwmin_Type(Integer32):
    """Custom type ccWMEprofileAc3BeEcwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc3BeEcwmin_Type.__name__ = "Integer32"
_CcWMEprofileAc3BeEcwmin_Object = MibTableColumn
ccWMEprofileAc3BeEcwmin = _CcWMEprofileAc3BeEcwmin_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 14),
    _CcWMEprofileAc3BeEcwmin_Type()
)
ccWMEprofileAc3BeEcwmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc3BeEcwmin.setStatus("current")


class _CcWMEprofileAc3BeEcwmax_Type(Integer32):
    """Custom type ccWMEprofileAc3BeEcwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc3BeEcwmax_Type.__name__ = "Integer32"
_CcWMEprofileAc3BeEcwmax_Object = MibTableColumn
ccWMEprofileAc3BeEcwmax = _CcWMEprofileAc3BeEcwmax_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 15),
    _CcWMEprofileAc3BeEcwmax_Type()
)
ccWMEprofileAc3BeEcwmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc3BeEcwmax.setStatus("current")


class _CcWMEprofileAc3BeTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc3BeTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc3BeTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc3BeTxopLimit_Object = MibTableColumn
ccWMEprofileAc3BeTxopLimit = _CcWMEprofileAc3BeTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 16),
    _CcWMEprofileAc3BeTxopLimit_Type()
)
ccWMEprofileAc3BeTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc3BeTxopLimit.setStatus("current")


class _CcWMEprofileAc3BeAgTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc3BeAgTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc3BeAgTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc3BeAgTxopLimit_Object = MibTableColumn
ccWMEprofileAc3BeAgTxopLimit = _CcWMEprofileAc3BeAgTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 17),
    _CcWMEprofileAc3BeAgTxopLimit_Type()
)
ccWMEprofileAc3BeAgTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc3BeAgTxopLimit.setStatus("current")


class _CcWMEprofileAc3BeAifsn_Type(Integer32):
    """Custom type ccWMEprofileAc3BeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc3BeAifsn_Type.__name__ = "Integer32"
_CcWMEprofileAc3BeAifsn_Object = MibTableColumn
ccWMEprofileAc3BeAifsn = _CcWMEprofileAc3BeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 18),
    _CcWMEprofileAc3BeAifsn_Type()
)
ccWMEprofileAc3BeAifsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc3BeAifsn.setStatus("current")


class _CcWMEprofileAc4BkEcwmin_Type(Integer32):
    """Custom type ccWMEprofileAc4BkEcwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc4BkEcwmin_Type.__name__ = "Integer32"
_CcWMEprofileAc4BkEcwmin_Object = MibTableColumn
ccWMEprofileAc4BkEcwmin = _CcWMEprofileAc4BkEcwmin_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 19),
    _CcWMEprofileAc4BkEcwmin_Type()
)
ccWMEprofileAc4BkEcwmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc4BkEcwmin.setStatus("current")


class _CcWMEprofileAc4BkEcwmax_Type(Integer32):
    """Custom type ccWMEprofileAc4BkEcwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc4BkEcwmax_Type.__name__ = "Integer32"
_CcWMEprofileAc4BkEcwmax_Object = MibTableColumn
ccWMEprofileAc4BkEcwmax = _CcWMEprofileAc4BkEcwmax_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 20),
    _CcWMEprofileAc4BkEcwmax_Type()
)
ccWMEprofileAc4BkEcwmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc4BkEcwmax.setStatus("current")


class _CcWMEprofileAc4BkTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc4BkTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc4BkTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc4BkTxopLimit_Object = MibTableColumn
ccWMEprofileAc4BkTxopLimit = _CcWMEprofileAc4BkTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 21),
    _CcWMEprofileAc4BkTxopLimit_Type()
)
ccWMEprofileAc4BkTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc4BkTxopLimit.setStatus("current")


class _CcWMEprofileAc4BkAgTxopLimit_Type(Integer32):
    """Custom type ccWMEprofileAc4BkAgTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcWMEprofileAc4BkAgTxopLimit_Type.__name__ = "Integer32"
_CcWMEprofileAc4BkAgTxopLimit_Object = MibTableColumn
ccWMEprofileAc4BkAgTxopLimit = _CcWMEprofileAc4BkAgTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 22),
    _CcWMEprofileAc4BkAgTxopLimit_Type()
)
ccWMEprofileAc4BkAgTxopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc4BkAgTxopLimit.setStatus("current")


class _CcWMEprofileAc4BkAifsn_Type(Integer32):
    """Custom type ccWMEprofileAc4BkAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CcWMEprofileAc4BkAifsn_Type.__name__ = "Integer32"
_CcWMEprofileAc4BkAifsn_Object = MibTableColumn
ccWMEprofileAc4BkAifsn = _CcWMEprofileAc4BkAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 23),
    _CcWMEprofileAc4BkAifsn_Type()
)
ccWMEprofileAc4BkAifsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileAc4BkAifsn.setStatus("current")
_CcWMEprofileQosParam_Type = Integer32
_CcWMEprofileQosParam_Object = MibTableColumn
ccWMEprofileQosParam = _CcWMEprofileQosParam_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 24),
    _CcWMEprofileQosParam_Type()
)
ccWMEprofileQosParam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileQosParam.setStatus("current")
_CcWMEprofileRowStatus_Type = AbbrevRowStatus
_CcWMEprofileRowStatus_Object = MibTableColumn
ccWMEprofileRowStatus = _CcWMEprofileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 18, 5, 1, 25),
    _CcWMEprofileRowStatus_Type()
)
ccWMEprofileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccWMEprofileRowStatus.setStatus("current")
_CcPortalBeacon_ObjectIdentity = ObjectIdentity
ccPortalBeacon = _CcPortalBeacon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 19)
)
_CcPortalBeaconRptTable_Object = MibTable
ccPortalBeaconRptTable = _CcPortalBeaconRptTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5)
)
if mibBuilder.loadTexts:
    ccPortalBeaconRptTable.setStatus("current")
_CcPortalBeaconRptEntry_Object = MibTableRow
ccPortalBeaconRptEntry = _CcPortalBeaconRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1)
)
ccPortalBeaconRptEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccRapResultsRogueIndex"),
    (0, "SYMBOL-WS5000-MIB", "ccPortalBeaconRptPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalBeaconRptEntry.setStatus("current")


class _CcPortalBeaconRptPortalIndex_Type(Integer32):
    """Custom type ccPortalBeaconRptPortalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcPortalBeaconRptPortalIndex_Type.__name__ = "Integer32"
_CcPortalBeaconRptPortalIndex_Object = MibTableColumn
ccPortalBeaconRptPortalIndex = _CcPortalBeaconRptPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 1),
    _CcPortalBeaconRptPortalIndex_Type()
)
ccPortalBeaconRptPortalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccPortalBeaconRptPortalIndex.setStatus("current")
_CcPortalBeaconRptNumBeaconsHeard_Type = Integer32
_CcPortalBeaconRptNumBeaconsHeard_Object = MibTableColumn
ccPortalBeaconRptNumBeaconsHeard = _CcPortalBeaconRptNumBeaconsHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 2),
    _CcPortalBeaconRptNumBeaconsHeard_Type()
)
ccPortalBeaconRptNumBeaconsHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptNumBeaconsHeard.setStatus("current")
_CcPortalBeaconRptBest_Type = Integer32
_CcPortalBeaconRptBest_Object = MibTableColumn
ccPortalBeaconRptBest = _CcPortalBeaconRptBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 3),
    _CcPortalBeaconRptBest_Type()
)
ccPortalBeaconRptBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBeaconRptBest.setUnits("dBm")
_CcPortalBeaconRptWorst_Type = Integer32
_CcPortalBeaconRptWorst_Object = MibTableColumn
ccPortalBeaconRptWorst = _CcPortalBeaconRptWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 4),
    _CcPortalBeaconRptWorst_Type()
)
ccPortalBeaconRptWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBeaconRptWorst.setUnits("dBm")
_CcPortalBeaconRptSum_Type = Integer32
_CcPortalBeaconRptSum_Object = MibTableColumn
ccPortalBeaconRptSum = _CcPortalBeaconRptSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 5),
    _CcPortalBeaconRptSum_Type()
)
ccPortalBeaconRptSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptSum.setStatus("current")
_CcPortalBeaconRptSumSquares_Type = Integer32
_CcPortalBeaconRptSumSquares_Object = MibTableColumn
ccPortalBeaconRptSumSquares = _CcPortalBeaconRptSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 6),
    _CcPortalBeaconRptSumSquares_Type()
)
ccPortalBeaconRptSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptSumSquares.setStatus("current")
_CcPortalBeaconRptMostRecent_Type = Integer32
_CcPortalBeaconRptMostRecent_Object = MibTableColumn
ccPortalBeaconRptMostRecent = _CcPortalBeaconRptMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 7),
    _CcPortalBeaconRptMostRecent_Type()
)
ccPortalBeaconRptMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptMostRecent.setStatus("current")
_CcPortalBeaconRptLastHeard_Type = DisplayString
_CcPortalBeaconRptLastHeard_Object = MibTableColumn
ccPortalBeaconRptLastHeard = _CcPortalBeaconRptLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 8),
    _CcPortalBeaconRptLastHeard_Type()
)
ccPortalBeaconRptLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRptLastHeard.setStatus("current")
_CcPortalBeaconRpFinderMac_Type = DisplayString
_CcPortalBeaconRpFinderMac_Object = MibTableColumn
ccPortalBeaconRpFinderMac = _CcPortalBeaconRpFinderMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 9),
    _CcPortalBeaconRpFinderMac_Type()
)
ccPortalBeaconRpFinderMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRpFinderMac.setStatus("current")
_CcPortalBeaconRpFoundMac_Type = DisplayString
_CcPortalBeaconRpFoundMac_Object = MibTableColumn
ccPortalBeaconRpFoundMac = _CcPortalBeaconRpFoundMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 5, 1, 10),
    _CcPortalBeaconRpFoundMac_Type()
)
ccPortalBeaconRpFoundMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBeaconRpFoundMac.setStatus("current")
_CcMuProbeRptTable_Object = MibTable
ccMuProbeRptTable = _CcMuProbeRptTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 6)
)
if mibBuilder.loadTexts:
    ccMuProbeRptTable.setStatus("current")
_CcMuProbeRptEntry_Object = MibTableRow
ccMuProbeRptEntry = _CcMuProbeRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 6, 1)
)
ccMuProbeRptEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccMuMac"),
    (0, "SYMBOL-WS5000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccMuProbeRptEntry.setStatus("current")
_CcMuProbeRptSignalMostRecent_Type = Integer32
_CcMuProbeRptSignalMostRecent_Object = MibTableColumn
ccMuProbeRptSignalMostRecent = _CcMuProbeRptSignalMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 6, 1, 1),
    _CcMuProbeRptSignalMostRecent_Type()
)
ccMuProbeRptSignalMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuProbeRptSignalMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuProbeRptSignalMostRecent.setUnits("dbm")
_CcMuProbeRptLastHeard_Type = DisplayString
_CcMuProbeRptLastHeard_Object = MibTableColumn
ccMuProbeRptLastHeard = _CcMuProbeRptLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 6, 1, 2),
    _CcMuProbeRptLastHeard_Type()
)
ccMuProbeRptLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuProbeRptLastHeard.setStatus("current")
_CcMuProbeRptFinderMac_Type = DisplayString
_CcMuProbeRptFinderMac_Object = MibTableColumn
ccMuProbeRptFinderMac = _CcMuProbeRptFinderMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 6, 1, 3),
    _CcMuProbeRptFinderMac_Type()
)
ccMuProbeRptFinderMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuProbeRptFinderMac.setStatus("current")
_CcMuProbeRptFoundMac_Type = DisplayString
_CcMuProbeRptFoundMac_Object = MibTableColumn
ccMuProbeRptFoundMac = _CcMuProbeRptFoundMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 19, 6, 1, 4),
    _CcMuProbeRptFoundMac_Type()
)
ccMuProbeRptFoundMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuProbeRptFoundMac.setStatus("current")
_CcSensor_ObjectIdentity = ObjectIdentity
ccSensor = _CcSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 20)
)
_CcSensorList_Type = DisplayString
_CcSensorList_Object = MibScalar
ccSensorList = _CcSensorList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 1),
    _CcSensorList_Type()
)
ccSensorList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSensorList.setStatus("current")
_CcApList_Type = DisplayString
_CcApList_Object = MibScalar
ccApList = _CcApList_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 2),
    _CcApList_Type()
)
ccApList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApList.setStatus("current")
_CcSensorRevert_Type = DisplayString
_CcSensorRevert_Object = MibScalar
ccSensorRevert = _CcSensorRevert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 3),
    _CcSensorRevert_Type()
)
ccSensorRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSensorRevert.setStatus("current")
_CcSensorConvert_Type = DisplayString
_CcSensorConvert_Object = MibScalar
ccSensorConvert = _CcSensorConvert_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 4),
    _CcSensorConvert_Type()
)
ccSensorConvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSensorConvert.setStatus("current")
_CcSensorEnable_Type = TruthValue
_CcSensorEnable_Object = MibScalar
ccSensorEnable = _CcSensorEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 5),
    _CcSensorEnable_Type()
)
ccSensorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSensorEnable.setStatus("current")
_CcApSensorTable_Object = MibTable
ccApSensorTable = _CcApSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6)
)
if mibBuilder.loadTexts:
    ccApSensorTable.setStatus("current")
_CcApSensorEntry_Object = MibTableRow
ccApSensorEntry = _CcApSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1)
)
ccApSensorEntry.setIndexNames(
    (0, "SYMBOL-WS5000-MIB", "ccApSensorIndex"),
)
if mibBuilder.loadTexts:
    ccApSensorEntry.setStatus("current")


class _CcApSensorIndex_Type(Integer32):
    """Custom type ccApSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CcApSensorIndex_Type.__name__ = "Integer32"
_CcApSensorIndex_Object = MibTableColumn
ccApSensorIndex = _CcApSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 1),
    _CcApSensorIndex_Type()
)
ccApSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApSensorIndex.setStatus("current")
_CcApSensorMask_Type = IpAddress
_CcApSensorMask_Object = MibTableColumn
ccApSensorMask = _CcApSensorMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 2),
    _CcApSensorMask_Type()
)
ccApSensorMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSensorMask.setStatus("current")
_CcApSensorGateWay_Type = IpAddress
_CcApSensorGateWay_Object = MibTableColumn
ccApSensorGateWay = _CcApSensorGateWay_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 3),
    _CcApSensorGateWay_Type()
)
ccApSensorGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSensorGateWay.setStatus("current")
_CcApSensorPrimary_Type = IpAddress
_CcApSensorPrimary_Object = MibTableColumn
ccApSensorPrimary = _CcApSensorPrimary_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 4),
    _CcApSensorPrimary_Type()
)
ccApSensorPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSensorPrimary.setStatus("current")
_CcApSensorSecondary_Type = IpAddress
_CcApSensorSecondary_Object = MibTableColumn
ccApSensorSecondary = _CcApSensorSecondary_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 5),
    _CcApSensorSecondary_Type()
)
ccApSensorSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSensorSecondary.setStatus("current")
_CcApSensorDhcp_Type = TruthValue
_CcApSensorDhcp_Object = MibTableColumn
ccApSensorDhcp = _CcApSensorDhcp_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 6),
    _CcApSensorDhcp_Type()
)
ccApSensorDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSensorDhcp.setStatus("current")
_CcApSensorIpaddress_Type = IpAddress
_CcApSensorIpaddress_Object = MibTableColumn
ccApSensorIpaddress = _CcApSensorIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 7),
    _CcApSensorIpaddress_Type()
)
ccApSensorIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSensorIpaddress.setStatus("current")
_CcApSensorMac_Type = DisplayString
_CcApSensorMac_Object = MibTableColumn
ccApSensorMac = _CcApSensorMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 6, 20, 6, 1, 8),
    _CcApSensorMac_Type()
)
ccApSensorMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApSensorMac.setStatus("current")
_CcV2dot0Groups_ObjectIdentity = ObjectIdentity
ccV2dot0Groups = _CcV2dot0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000)
)

# Managed Objects groups

radiusAuthClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 2, 2, 1)
)
radiusAuthClientMIBGroup.setObjects(
      *(("SYMBOL-WS5000-MIB", "radiusAuthClientInvalidServerAddresses"),
        ("SYMBOL-WS5000-MIB", "radiusAuthServerAddress"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientServerPortNumber"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientRoundTripTime"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessRequests"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessRetransmissions"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessAccepts"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessRejects"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessChallenges"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientMalformedAccessResponses"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientBadAuthenticators"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientPendingRequests"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientTimeouts"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientUnknownTypes"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientPacketsDropped"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientIdentifier"))
)
if mibBuilder.loadTexts:
    radiusAuthClientMIBGroup.setStatus("current")

v1dot2dot5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1000, 2)
)
v1dot2dot5Group.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccPolicyAPPolicyCount"),
        ("SYMBOL-WS5000-MIB", "ccEPCFGMode"),
        ("SYMBOL-WS5000-MIB", "ccEPDuplex"),
        ("SYMBOL-WS5000-MIB", "ccEPMode"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoEncrMethod"),
        ("SYMBOL-WS5000-MIB", "ccTargetTrapString"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoEnableTrap"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoMaxNumSendOneTrap"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoInterval"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoAclViolation"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoDenyAdoption"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoAPMUMaxExceed"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoWLANMUMaxExceed"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoApDetected"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoApAdopted"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoApReset"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoApUnavailable"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoKDCUserAuthFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoRadiusAuthFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoLowFlashSpace"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoNicDropping"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoApAlert"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoUserAuthFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoHsbPrimaryNoHeartbeat"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoHsbStandbyEntersFailover"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoPrimaryFailedResetting"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoKDCPropagationFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoHighDecryptFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoHighReplyFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoTKIPMICFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoWPACounterMeasureStart"),
        ("SYMBOL-WS5000-MIB", "hsbStartUpControl"),
        ("SYMBOL-WS5000-MIB", "hsbPeerConnectControl"),
        ("SYMBOL-WS5000-MIB", "ccModuleName"),
        ("SYMBOL-WS5000-MIB", "ccModuleDesc"),
        ("SYMBOL-WS5000-MIB", "ccManufacture"),
        ("SYMBOL-WS5000-MIB", "ccCopyright"),
        ("SYMBOL-WS5000-MIB", "ccModuleVer"),
        ("SYMBOL-WS5000-MIB", "ccMaxNumAP"),
        ("SYMBOL-WS5000-MIB", "ccMaxNumMu"),
        ("SYMBOL-WS5000-MIB", "ccActivePolicy"),
        ("SYMBOL-WS5000-MIB", "ccTaf"),
        ("SYMBOL-WS5000-MIB", "ccSnmpOpers"),
        ("SYMBOL-WS5000-MIB", "ccUptime"),
        ("SYMBOL-WS5000-MIB", "ccFTP"),
        ("SYMBOL-WS5000-MIB", "ccTelnet"),
        ("SYMBOL-WS5000-MIB", "ccWeb"),
        ("SYMBOL-WS5000-MIB", "ccSNMPFlag"),
        ("SYMBOL-WS5000-MIB", "ccTime"),
        ("SYMBOL-WS5000-MIB", "ccSNMPKdc"),
        ("SYMBOL-WS5000-MIB", "ccCliKdc"),
        ("SYMBOL-WS5000-MIB", "ccPolicyAddObj"),
        ("SYMBOL-WS5000-MIB", "ccPolicyRemObj"),
        ("SYMBOL-WS5000-MIB", "ccLicenseCount"),
        ("SYMBOL-WS5000-MIB", "ccEmergencyPolicy"),
        ("SYMBOL-WS5000-MIB", "ccEmergencyMode"),
        ("SYMBOL-WS5000-MIB", "ccRunACS"),
        ("SYMBOL-WS5000-MIB", "ccEnableSNMPTrap"),
        ("SYMBOL-WS5000-MIB", "ccPolicyName"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDesc"),
        ("SYMBOL-WS5000-MIB", "ccPolicyCountry"),
        ("SYMBOL-WS5000-MIB", "ccPolicyAddAPPolicy"),
        ("SYMBOL-WS5000-MIB", "ccPolicyRmvAPPolicy"),
        ("SYMBOL-WS5000-MIB", "ccPolicyExcludeInfo"),
        ("SYMBOL-WS5000-MIB", "ccPolicyExcludeEdit"),
        ("SYMBOL-WS5000-MIB", "ccPolicyExcludeRmv"),
        ("SYMBOL-WS5000-MIB", "ccPolicyIncludeInfo"),
        ("SYMBOL-WS5000-MIB", "ccPolicyIncludeEdit"),
        ("SYMBOL-WS5000-MIB", "ccPolicyIncludeRmv"),
        ("SYMBOL-WS5000-MIB", "ccPolicyEtherPolicy"),
        ("SYMBOL-WS5000-MIB", "ccPolicyTrap"),
        ("SYMBOL-WS5000-MIB", "ccPolicyChannel11a"),
        ("SYMBOL-WS5000-MIB", "ccPolicyPower11a"),
        ("SYMBOL-WS5000-MIB", "ccPolicyChannel11b"),
        ("SYMBOL-WS5000-MIB", "ccPolicyPower11b"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDSCoExistence"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDefAdoptAPPolicy11a"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDefAdoptAPPolicy11b"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDefAdoptAPPolicyFH"),
        ("SYMBOL-WS5000-MIB", "ccCCIndex"),
        ("SYMBOL-WS5000-MIB", "ccCCode"),
        ("SYMBOL-WS5000-MIB", "ccFullName"),
        ("SYMBOL-WS5000-MIB", "cc11aChannels"),
        ("SYMBOL-WS5000-MIB", "cc11bChannels"),
        ("SYMBOL-WS5000-MIB", "ccFHTableNum"),
        ("SYMBOL-WS5000-MIB", "ccFHChannels"),
        ("SYMBOL-WS5000-MIB", "ccFHAlgorithm"),
        ("SYMBOL-WS5000-MIB", "ccFHContiguous"),
        ("SYMBOL-WS5000-MIB", "ccFHHopSequence"),
        ("SYMBOL-WS5000-MIB", "kdcType"),
        ("SYMBOL-WS5000-MIB", "masterHost"),
        ("SYMBOL-WS5000-MIB", "masterIPAddress"),
        ("SYMBOL-WS5000-MIB", "createMsKdc"),
        ("SYMBOL-WS5000-MIB", "delMsKdc"),
        ("SYMBOL-WS5000-MIB", "createSlvKdc"),
        ("SYMBOL-WS5000-MIB", "delSlvKdc"),
        ("SYMBOL-WS5000-MIB", "kdcRealm"),
        ("SYMBOL-WS5000-MIB", "interfaceNumber"),
        ("SYMBOL-WS5000-MIB", "addSlave"),
        ("SYMBOL-WS5000-MIB", "delSlave"),
        ("SYMBOL-WS5000-MIB", "slaveCount"),
        ("SYMBOL-WS5000-MIB", "hostName"),
        ("SYMBOL-WS5000-MIB", "realM"),
        ("SYMBOL-WS5000-MIB", "ipAddress"),
        ("SYMBOL-WS5000-MIB", "domainName"),
        ("SYMBOL-WS5000-MIB", "syncDB"),
        ("SYMBOL-WS5000-MIB", "prefTimeServer"),
        ("SYMBOL-WS5000-MIB", "firstAltTimeServer"),
        ("SYMBOL-WS5000-MIB", "secondAltTimeServer"),
        ("SYMBOL-WS5000-MIB", "groupSetTimeServer"),
        ("SYMBOL-WS5000-MIB", "delAll"),
        ("SYMBOL-WS5000-MIB", "kdcUserName"),
        ("SYMBOL-WS5000-MIB", "kdcUserTlife"),
        ("SYMBOL-WS5000-MIB", "kdcWLANName"),
        ("SYMBOL-WS5000-MIB", "kdcWLANTlife"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientInvalidServerAddresses"),
        ("SYMBOL-WS5000-MIB", "radiusAuthServerAddress"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientServerPortNumber"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientRoundTripTime"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessRequests"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessRetransmissions"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessAccepts"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessRejects"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientAccessChallenges"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientMalformedAccessResponses"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientBadAuthenticators"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientPendingRequests"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientTimeouts"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientUnknownTypes"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientPacketsDropped"),
        ("SYMBOL-WS5000-MIB", "radiusAuthClientIdentifier"),
        ("SYMBOL-WS5000-MIB", "ccEventsAllLocalLog"),
        ("SYMBOL-WS5000-MIB", "ccEventsAllSNMPTrap"),
        ("SYMBOL-WS5000-MIB", "ccEventsAllSyslog"),
        ("SYMBOL-WS5000-MIB", "ccEventsAllDefault"),
        ("SYMBOL-WS5000-MIB", "ccEventDescr"),
        ("SYMBOL-WS5000-MIB", "ccEventDefault"),
        ("SYMBOL-WS5000-MIB", "ccEventSyslog"),
        ("SYMBOL-WS5000-MIB", "ccEventSNMPTrap"),
        ("SYMBOL-WS5000-MIB", "ccEventLocalLog"),
        ("SYMBOL-WS5000-MIB", "ccSysLogStatus"),
        ("SYMBOL-WS5000-MIB", "ccSyslogAddHost"),
        ("SYMBOL-WS5000-MIB", "ccSyslogRemHost"),
        ("SYMBOL-WS5000-MIB", "ccSyslogHostName"),
        ("SYMBOL-WS5000-MIB", "ccSyslogHostIPAddr"),
        ("SYMBOL-WS5000-MIB", "ccSyslogHostDomain"),
        ("SYMBOL-WS5000-MIB", "ccSyslogHostSetSeverity"),
        ("SYMBOL-WS5000-MIB", "ccSyslogHostSeverityList"),
        ("SYMBOL-WS5000-MIB", "ccSystemAddHost"),
        ("SYMBOL-WS5000-MIB", "ccSystemRemHost"),
        ("SYMBOL-WS5000-MIB", "ccSystemHostName"),
        ("SYMBOL-WS5000-MIB", "ccSystemHostIPAddr"),
        ("SYMBOL-WS5000-MIB", "ccSystemHostDomain"),
        ("SYMBOL-WS5000-MIB", "ccPolicyRCAdd"),
        ("SYMBOL-WS5000-MIB", "ccPolicyRCRem"),
        ("SYMBOL-WS5000-MIB", "ccPolicyRCChannelDescr"),
        ("SYMBOL-WS5000-MIB", "ccPolicyAPPolicyName"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyAddObj"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyRemObj"),
        ("SYMBOL-WS5000-MIB", "ccEPPAddObj"),
        ("SYMBOL-WS5000-MIB", "ccEPPRemObj"),
        ("SYMBOL-WS5000-MIB", "ccAccessPortAddObj"),
        ("SYMBOL-WS5000-MIB", "ccAccessPortRemObj"),
        ("SYMBOL-WS5000-MIB", "ccRadioName"),
        ("SYMBOL-WS5000-MIB", "ccRadioDesc"),
        ("SYMBOL-WS5000-MIB", "ccRadioOnlineStatus"),
        ("SYMBOL-WS5000-MIB", "ccRadioMAC"),
        ("SYMBOL-WS5000-MIB", "ccDeviceMAC"),
        ("SYMBOL-WS5000-MIB", "ccDeviceLocation"),
        ("SYMBOL-WS5000-MIB", "ccRadioType"),
        ("SYMBOL-WS5000-MIB", "ccRadioChannel"),
        ("SYMBOL-WS5000-MIB", "ccRadioPolicy"),
        ("SYMBOL-WS5000-MIB", "ccDeviceNic"),
        ("SYMBOL-WS5000-MIB", "ccDeviceType"),
        ("SYMBOL-WS5000-MIB", "ccRadioCCAmode"),
        ("SYMBOL-WS5000-MIB", "ccRadioCCAthresh"),
        ("SYMBOL-WS5000-MIB", "ccRadioDiversity"),
        ("SYMBOL-WS5000-MIB", "ccDeviceVlanid"),
        ("SYMBOL-WS5000-MIB", "ccDeviceVlanTagsSeen"),
        ("SYMBOL-WS5000-MIB", "ccRadioUptime"),
        ("SYMBOL-WS5000-MIB", "ccRadioTxpps"),
        ("SYMBOL-WS5000-MIB", "ccRadioMUs"),
        ("SYMBOL-WS5000-MIB", "ccRadioGatherStatistics"),
        ("SYMBOL-WS5000-MIB", "ccRadioReset"),
        ("SYMBOL-WS5000-MIB", "ccDeviceReset"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyDesc"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyPreAmble"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyBeaconInterval"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyRTSThreshold"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyDTIM"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyBasicRates11a"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicySupportedRates11a"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyBasicRates11b"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicySupportedRates11b"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyBasicRatesFH"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicySupportedRatesFH"),
        ("SYMBOL-WS5000-MIB", "ccEPIndex"),
        ("SYMBOL-WS5000-MIB", "ccEPNic"),
        ("SYMBOL-WS5000-MIB", "ccEPName"),
        ("SYMBOL-WS5000-MIB", "ccEPDesc"),
        ("SYMBOL-WS5000-MIB", "ccEPMacAddr"),
        ("SYMBOL-WS5000-MIB", "ccEPEnable"),
        ("SYMBOL-WS5000-MIB", "ccEPEnableDHCP"),
        ("SYMBOL-WS5000-MIB", "ccEPIPAddr"),
        ("SYMBOL-WS5000-MIB", "ccEPNetMask"),
        ("SYMBOL-WS5000-MIB", "ccEPDnsCount"),
        ("SYMBOL-WS5000-MIB", "ccEPDnsList"),
        ("SYMBOL-WS5000-MIB", "ccEPPrimaryVid"),
        ("SYMBOL-WS5000-MIB", "ccEPOnline"),
        ("SYMBOL-WS5000-MIB", "ccEPDisplayName"),
        ("SYMBOL-WS5000-MIB", "ccEPUptime"),
        ("SYMBOL-WS5000-MIB", "ccEPTx"),
        ("SYMBOL-WS5000-MIB", "ccEPRx"),
        ("SYMBOL-WS5000-MIB", "ccEPDomain"),
        ("SYMBOL-WS5000-MIB", "ccEPGateway"),
        ("SYMBOL-WS5000-MIB", "ccEPPIndex"),
        ("SYMBOL-WS5000-MIB", "ccEPPName"),
        ("SYMBOL-WS5000-MIB", "ccEPPAlias"),
        ("SYMBOL-WS5000-MIB", "ccEPPDesc"),
        ("SYMBOL-WS5000-MIB", "ccEPPRonnic"),
        ("SYMBOL-WS5000-MIB", "ccEPPVlanCount"),
        ("SYMBOL-WS5000-MIB", "ccEPPVlanList"),
        ("SYMBOL-WS5000-MIB", "ccEPPCreateNewVlan"),
        ("SYMBOL-WS5000-MIB", "ccEPPRemVlan"),
        ("SYMBOL-WS5000-MIB", "ccEPPDropVlan"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHHopTime"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHCurrentChannelNumber"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHMaxDwellTime"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHCurrentDwellTime"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHCurrentSet"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHCurrentPattern"),
        ("SYMBOL-WS5000-MIB", "ccdot11FHCurrentIndex"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyWLAN"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyWLANBW"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyWLANNP"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyWLANBSS"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyPrimaryWLAN"),
        ("SYMBOL-WS5000-MIB", "ccWLANAddObj"),
        ("SYMBOL-WS5000-MIB", "ccWLANRemObj"),
        ("SYMBOL-WS5000-MIB", "ccUserAddObj"),
        ("SYMBOL-WS5000-MIB", "ccUserRemObj"),
        ("SYMBOL-WS5000-MIB", "ccGraphAddObj"),
        ("SYMBOL-WS5000-MIB", "ccGraphRemObj"),
        ("SYMBOL-WS5000-MIB", "ccSecAddObj"),
        ("SYMBOL-WS5000-MIB", "ccSecRemObj"),
        ("SYMBOL-WS5000-MIB", "ccACLAddObj"),
        ("SYMBOL-WS5000-MIB", "ccACLRemObj"),
        ("SYMBOL-WS5000-MIB", "ccUserID"),
        ("SYMBOL-WS5000-MIB", "ccUserFullName"),
        ("SYMBOL-WS5000-MIB", "ccUserPwd"),
        ("SYMBOL-WS5000-MIB", "ccUserProfileMgmtRight"),
        ("SYMBOL-WS5000-MIB", "ccUserSysAdminRight"),
        ("SYMBOL-WS5000-MIB", "ccUserSNMPAdminRight"),
        ("SYMBOL-WS5000-MIB", "ccUserSecurityAdminRight"),
        ("SYMBOL-WS5000-MIB", "ccWLANIndex"),
        ("SYMBOL-WS5000-MIB", "ccWLANName"),
        ("SYMBOL-WS5000-MIB", "ccESSID"),
        ("SYMBOL-WS5000-MIB", "ccSecurity"),
        ("SYMBOL-WS5000-MIB", "ccACLEnabled"),
        ("SYMBOL-WS5000-MIB", "ccMaxMus"),
        ("SYMBOL-WS5000-MIB", "ccKerberosAuthName"),
        ("SYMBOL-WS5000-MIB", "ccKerberosAuthPass"),
        ("SYMBOL-WS5000-MIB", "ccWLANACL"),
        ("SYMBOL-WS5000-MIB", "ccWLANIsAuthenticated"),
        ("SYMBOL-WS5000-MIB", "ccWLANMUTraffic"),
        ("SYMBOL-WS5000-MIB", "ccWLANSecuredBeacon"),
        ("SYMBOL-WS5000-MIB", "ccWLANCurrentMU"),
        ("SYMBOL-WS5000-MIB", "ccWLANNetMask"),
        ("SYMBOL-WS5000-MIB", "ccWLANDefaultRoute"),
        ("SYMBOL-WS5000-MIB", "ccWLANBCMC11A"),
        ("SYMBOL-WS5000-MIB", "ccWLANBCMC11B"),
        ("SYMBOL-WS5000-MIB", "ccWLANBCMCFH"),
        ("SYMBOL-WS5000-MIB", "ccBroadcastEss"),
        ("SYMBOL-WS5000-MIB", "ccWLANDesc"),
        ("SYMBOL-WS5000-MIB", "ccKnownCCIndex"),
        ("SYMBOL-WS5000-MIB", "ccKnownCCName"),
        ("SYMBOL-WS5000-MIB", "ccKnownCCMac"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPIndex"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPMac"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPVer"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPIP"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPPriority"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPMus"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPType"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPAPVer"),
        ("SYMBOL-WS5000-MIB", "ccKnownAPEssid"),
        ("SYMBOL-WS5000-MIB", "ccGraphIndex"),
        ("SYMBOL-WS5000-MIB", "ccGraphName"),
        ("SYMBOL-WS5000-MIB", "ccGraphWlanId"),
        ("SYMBOL-WS5000-MIB", "ccVLANIndex"),
        ("SYMBOL-WS5000-MIB", "ccVLANName"),
        ("SYMBOL-WS5000-MIB", "ccVLANDesc"),
        ("SYMBOL-WS5000-MIB", "ccVLANVid"),
        ("SYMBOL-WS5000-MIB", "ccVLANPriority"),
        ("SYMBOL-WS5000-MIB", "ccVLANPorts"),
        ("SYMBOL-WS5000-MIB", "ccVLANEtherPolicy"),
        ("SYMBOL-WS5000-MIB", "ccVLANWlan"),
        ("SYMBOL-WS5000-MIB", "ccVLANWlanList"),
        ("SYMBOL-WS5000-MIB", "ccVLANAddWlan"),
        ("SYMBOL-WS5000-MIB", "ccVLANRemWlan"),
        ("SYMBOL-WS5000-MIB", "ccSecIndex"),
        ("SYMBOL-WS5000-MIB", "ccSecName"),
        ("SYMBOL-WS5000-MIB", "ccSecDesc"),
        ("SYMBOL-WS5000-MIB", "ccSecPreSharedAuthEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecWEPEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecWEPKeyBitSize"),
        ("SYMBOL-WS5000-MIB", "ccSecWEPKey"),
        ("SYMBOL-WS5000-MIB", "ccSecWEPKeyUse"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosRealm"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosServer1"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosServer2"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosServer3"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosPort1"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosPort2"),
        ("SYMBOL-WS5000-MIB", "ccSecKerberosPort3"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusServer1"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusPort1"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusSecret1"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusServer2"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusPort2"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusSecret2"),
        ("SYMBOL-WS5000-MIB", "ccSecRadiusHostname"),
        ("SYMBOL-WS5000-MIB", "ccSecEapEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecEapQuietPeriod"),
        ("SYMBOL-WS5000-MIB", "ccSecEapTxPeriod"),
        ("SYMBOL-WS5000-MIB", "ccSecEapReauth"),
        ("SYMBOL-WS5000-MIB", "ccSecEapReauthPeriod"),
        ("SYMBOL-WS5000-MIB", "ccSecEapReauthMaxRetries"),
        ("SYMBOL-WS5000-MIB", "ccSecEapSupplTimeout"),
        ("SYMBOL-WS5000-MIB", "ccSecEapMaxreqRetries"),
        ("SYMBOL-WS5000-MIB", "ccSecGroupRekeyPeriod"),
        ("SYMBOL-WS5000-MIB", "ccSecPreSharedKeyMaterial"),
        ("SYMBOL-WS5000-MIB", "ccSecOpenEncryptEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecKeyGuardEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecTKIPEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecCheckValidity"),
        ("SYMBOL-WS5000-MIB", "ccACLName"),
        ("SYMBOL-WS5000-MIB", "ccACLDefaultAction"),
        ("SYMBOL-WS5000-MIB", "ccACLAction"),
        ("SYMBOL-WS5000-MIB", "ccACLGetItemCount"),
        ("SYMBOL-WS5000-MIB", "ccACLAddItem"),
        ("SYMBOL-WS5000-MIB", "ccACLRemItem"),
        ("SYMBOL-WS5000-MIB", "ccNumNPRec"),
        ("SYMBOL-WS5000-MIB", "ccNumPORec"),
        ("SYMBOL-WS5000-MIB", "ccNumCGRec"),
        ("SYMBOL-WS5000-MIB", "ccNumCFRec"),
        ("SYMBOL-WS5000-MIB", "ccCFAddObj"),
        ("SYMBOL-WS5000-MIB", "ccCFRemObj"),
        ("SYMBOL-WS5000-MIB", "ccCGAddObj"),
        ("SYMBOL-WS5000-MIB", "ccCGRemObj"),
        ("SYMBOL-WS5000-MIB", "ccPOAddObj"),
        ("SYMBOL-WS5000-MIB", "ccPORemObj"),
        ("SYMBOL-WS5000-MIB", "ccNPAddObj"),
        ("SYMBOL-WS5000-MIB", "ccNPRemObj"),
        ("SYMBOL-WS5000-MIB", "ccNPIndex"),
        ("SYMBOL-WS5000-MIB", "ccNPName"),
        ("SYMBOL-WS5000-MIB", "ccNPDesc"),
        ("SYMBOL-WS5000-MIB", "ccNPInName"),
        ("SYMBOL-WS5000-MIB", "ccNPOutName"),
        ("SYMBOL-WS5000-MIB", "ccPOName"),
        ("SYMBOL-WS5000-MIB", "ccPODesc"),
        ("SYMBOL-WS5000-MIB", "ccPOCgCount"),
        ("SYMBOL-WS5000-MIB", "ccPOAddCg"),
        ("SYMBOL-WS5000-MIB", "ccPORemCg"),
        ("SYMBOL-WS5000-MIB", "ccPOType"),
        ("SYMBOL-WS5000-MIB", "ccCGName"),
        ("SYMBOL-WS5000-MIB", "ccCGDesc"),
        ("SYMBOL-WS5000-MIB", "ccCGCfCount"),
        ("SYMBOL-WS5000-MIB", "ccCGAddCf"),
        ("SYMBOL-WS5000-MIB", "ccCGRemCf"),
        ("SYMBOL-WS5000-MIB", "ccCFName"),
        ("SYMBOL-WS5000-MIB", "ccCFDesc"),
        ("SYMBOL-WS5000-MIB", "ccCFMcCount"),
        ("SYMBOL-WS5000-MIB", "ccCFAddMc"),
        ("SYMBOL-WS5000-MIB", "ccCFRemMc"),
        ("SYMBOL-WS5000-MIB", "ccPOCGName"),
        ("SYMBOL-WS5000-MIB", "ccPOCGNewIP"),
        ("SYMBOL-WS5000-MIB", "ccPOCGVlanPriority"),
        ("SYMBOL-WS5000-MIB", "ccPOCGTos"),
        ("SYMBOL-WS5000-MIB", "ccPOCGBw"),
        ("SYMBOL-WS5000-MIB", "ccPOCGTxProfile"),
        ("SYMBOL-WS5000-MIB", "ccPOCGPacketModifier"),
        ("SYMBOL-WS5000-MIB", "ccCGCFAction"),
        ("SYMBOL-WS5000-MIB", "ccCGCFName"),
        ("SYMBOL-WS5000-MIB", "ccCFMCOffset"),
        ("SYMBOL-WS5000-MIB", "ccCFMCValueCount"),
        ("SYMBOL-WS5000-MIB", "ccCFAddMCValue"),
        ("SYMBOL-WS5000-MIB", "ccCFRemMCValue"),
        ("SYMBOL-WS5000-MIB", "ccCFMCValue"),
        ("SYMBOL-WS5000-MIB", "ccHsbEnabled"),
        ("SYMBOL-WS5000-MIB", "ccHsbMode"),
        ("SYMBOL-WS5000-MIB", "ccHsbMacAddress1"),
        ("SYMBOL-WS5000-MIB", "ccHsbMacAddress2"),
        ("SYMBOL-WS5000-MIB", "ccHsbHeartbeatEnabledOnInterface1"),
        ("SYMBOL-WS5000-MIB", "ccHsbHeartbeatEnabledOnInterface2"),
        ("SYMBOL-WS5000-MIB", "ccHsbConnectivityFlag"),
        ("SYMBOL-WS5000-MIB", "ccHsbFailoverState"),
        ("SYMBOL-WS5000-MIB", "ccHsbFailoverReason"),
        ("SYMBOL-WS5000-MIB", "ccHsbResetCode"),
        ("SYMBOL-WS5000-MIB", "ccHsbRevert"),
        ("SYMBOL-WS5000-MIB", "ccHsbautorevert"),
        ("SYMBOL-WS5000-MIB", "ccHsbautorevertdelay"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoIndex"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoType"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoMac"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoIP"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoWlan"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoEssid"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoAP"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoAPState"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoSecState"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoCurRate"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoSupRates"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoRssi"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoPsp"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoIntf"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoAsscUptime"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoTktExp"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoUserName"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoPktTx"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoPktRx"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoBytesTx"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoBytesRx"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoLastAct"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoVlan"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoAuthState"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoAuthMethod"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoBCMCEncrType"),
        ("SYMBOL-WS5000-MIB", "ccACLItem"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrSecName"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrHost"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrCommunity"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrPort"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrStorageType"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrRowStatus"),
        ("SYMBOL-WS5000-MIB", "ccTargetAddrOption"),
        ("SYMBOL-WS5000-MIB", "licenseChangedControl"),
        ("SYMBOL-WS5000-MIB", "clockChangedControl"),
        ("SYMBOL-WS5000-MIB", "pktDiscWrongNICControl"),
        ("SYMBOL-WS5000-MIB", "pktDiscWrongVLANControl"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailPolControl"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailACLControl"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailLimitControl"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailLicControl"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailNoImgControl"),
        ("SYMBOL-WS5000-MIB", "apCfgFailESSControl"),
        ("SYMBOL-WS5000-MIB", "devDropInfoMsgControl"),
        ("SYMBOL-WS5000-MIB", "devdropLoadmeMsgControl"),
        ("SYMBOL-WS5000-MIB", "etherConnectControl"),
        ("SYMBOL-WS5000-MIB", "muAssocFailControl"),
        ("SYMBOL-WS5000-MIB", "muAssocOKControl"),
        ("SYMBOL-WS5000-MIB", "muRoamedControl"),
        ("SYMBOL-WS5000-MIB", "muDisassocControl"),
        ("SYMBOL-WS5000-MIB", "muEAPAuthFailControl"),
        ("SYMBOL-WS5000-MIB", "muEAPAuthOKControl"),
        ("SYMBOL-WS5000-MIB", "muKDCAuthOKControl"),
        ("SYMBOL-WS5000-MIB", "wlanAuthOKControl"),
        ("SYMBOL-WS5000-MIB", "wlanAuthFailControl"),
        ("SYMBOL-WS5000-MIB", "userAuthOKControl"),
        ("SYMBOL-WS5000-MIB", "radiusSrvTimeoutControl"),
        ("SYMBOL-WS5000-MIB", "kdcPrincAddControl"),
        ("SYMBOL-WS5000-MIB", "kdcPrincChgdControl"),
        ("SYMBOL-WS5000-MIB", "kdcPrincDelControl"),
        ("SYMBOL-WS5000-MIB", "kdcDBReplacedControl"),
        ("SYMBOL-WS5000-MIB", "hsbStdbyAutoRevControl"),
        ("SYMBOL-WS5000-MIB", "hsbPrimAutoRevControl"),
        ("SYMBOL-WS5000-MIB", "acsErrorControl"),
        ("SYMBOL-WS5000-MIB", "eopActiveControl"),
        ("SYMBOL-WS5000-MIB", "eopInactiveControl"),
        ("SYMBOL-WS5000-MIB", "debugEventControl"),
        ("SYMBOL-WS5000-MIB", "ccIdHwVersion"),
        ("SYMBOL-WS5000-MIB", "ccIdFwVersion"),
        ("SYMBOL-WS5000-MIB", "ccIdSwVersion"),
        ("SYMBOL-WS5000-MIB", "ccIdMibVersion"),
        ("SYMBOL-WS5000-MIB", "ccIdCliVersion"),
        ("SYMBOL-WS5000-MIB", "ccIdXmlVersion"),
        ("SYMBOL-WS5000-MIB", "ccIdSerialNumber"),
        ("SYMBOL-WS5000-MIB", "ccSshEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSshProtocolVersion"),
        ("SYMBOL-WS5000-MIB", "ccSshPort"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyName"),
        ("SYMBOL-WS5000-MIB", "ccAccessChangedControl"),
        ("SYMBOL-WS5000-MIB", "ccFanAndTempControl"),
        ("SYMBOL-WS5000-MIB", "ccIdSwBuildInfo"),
        ("SYMBOL-WS5000-MIB", "ccIdSwBuildDate"),
        ("SYMBOL-WS5000-MIB", "ccIdProductModel"),
        ("SYMBOL-WS5000-MIB", "ccIdProductFamily"),
        ("SYMBOL-WS5000-MIB", "cc11gChannels"),
        ("SYMBOL-WS5000-MIB", "ccPolicyPower11g"),
        ("SYMBOL-WS5000-MIB", "ccPolicyChannel11g"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDefAdoptAPPolicy11g"),
        ("SYMBOL-WS5000-MIB", "ccRadioAllPower"),
        ("SYMBOL-WS5000-MIB", "ccRadioCurrentPower"),
        ("SYMBOL-WS5000-MIB", "ccRadioPowerdBm"),
        ("SYMBOL-WS5000-MIB", "ccRadioAllChannels"),
        ("SYMBOL-WS5000-MIB", "ccRadioCurrentChannel"),
        ("SYMBOL-WS5000-MIB", "ccRadioAntenna"),
        ("SYMBOL-WS5000-MIB", "ccRadioShortSlot"),
        ("SYMBOL-WS5000-MIB", "ccRadioProtection"),
        ("SYMBOL-WS5000-MIB", "ccRadioRadarChannels"),
        ("SYMBOL-WS5000-MIB", "ccRadioTPC"),
        ("SYMBOL-WS5000-MIB", "ccRadioDFS"),
        ("SYMBOL-WS5000-MIB", "ccRadioIndoor"),
        ("SYMBOL-WS5000-MIB", "ccRadioAntCorrection"),
        ("SYMBOL-WS5000-MIB", "ccRadioMUPowerdBm"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyRemAllWlan"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyAddAllWlan"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyNonSpectrumMgmt"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicySupportedRates11g"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyBasicRates11g"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyUnselectWLAN"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicySelectWLAN"),
        ("SYMBOL-WS5000-MIB", "radioRandomChannelControl"),
        ("SYMBOL-WS5000-MIB", "radioResumeControl"),
        ("SYMBOL-WS5000-MIB", "radioSuspendControl"),
        ("SYMBOL-WS5000-MIB", "dfsChannelRevertControl"),
        ("SYMBOL-WS5000-MIB", "dfsChannelSwitchControl"),
        ("SYMBOL-WS5000-MIB", "dfsChannelSelectControl"),
        ("SYMBOL-WS5000-MIB", "dfsRadarDetectControl"),
        ("SYMBOL-WS5000-MIB", "ccSecCCMPEnabled"),
        ("SYMBOL-WS5000-MIB", "ccSecPreAuthentication"),
        ("SYMBOL-WS5000-MIB", "ccSecPMKCaching"),
        ("SYMBOL-WS5000-MIB", "tpcPowerReducedControl"),
        ("SYMBOL-WS5000-MIB", "ccPolicyAPNameOfPolicy"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsReset"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsIndex"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsType"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsDescr"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsCurrentReading"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsMinimum"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsMaximum"),
        ("SYMBOL-WS5000-MIB", "ccHwSensorsNotifyIfAbove"))
)
if mibBuilder.loadTexts:
    v1dot2dot5Group.setStatus("current")

v1dot2dot5GroupOfDepricated = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1000, 4)
)
v1dot2dot5GroupOfDepricated.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccPolicyDefAdoptAPPolicy"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDefChannel"),
        ("SYMBOL-WS5000-MIB", "ccPolicyDefPower"),
        ("SYMBOL-WS5000-MIB", "ccEPSpeed"),
        ("SYMBOL-WS5000-MIB", "ccSecBeaconEssid"),
        ("SYMBOL-WS5000-MIB", "ccSecBCMCEncrType"),
        ("SYMBOL-WS5000-MIB", "ccACLGetItem"),
        ("SYMBOL-WS5000-MIB", "ccRadioPower"),
        ("SYMBOL-WS5000-MIB", "ccRadioMUPower"),
        ("SYMBOL-WS5000-MIB", "ccRadioAuto"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyRemWLAN"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyAddWLAN"),
        ("SYMBOL-WS5000-MIB", "ccSshAuthenticationTimeout"),
        ("SYMBOL-WS5000-MIB", "ccSshInactivityTimeout"),
        ("SYMBOL-WS5000-MIB", "ccUserAdminRight"),
        ("SYMBOL-WS5000-MIB", "ccDeviceClearSeenVlanTags"),
        ("SYMBOL-WS5000-MIB", "ccPOPacketModifier"),
        ("SYMBOL-WS5000-MIB", "delTimeServer"))
)
if mibBuilder.loadTexts:
    v1dot2dot5GroupOfDepricated.setStatus("deprecated")

v2dot0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 1)
)
v2dot0Group.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccLANIndex"),
        ("SYMBOL-WS5000-MIB", "ccLANName"),
        ("SYMBOL-WS5000-MIB", "ccLANDesc"),
        ("SYMBOL-WS5000-MIB", "ccLANNATCount"),
        ("SYMBOL-WS5000-MIB", "ccLANAddNAT"),
        ("SYMBOL-WS5000-MIB", "ccLANRemNAT"),
        ("SYMBOL-WS5000-MIB", "ccLANEp"),
        ("SYMBOL-WS5000-MIB", "ccLANNp"),
        ("SYMBOL-WS5000-MIB", "ccLANNATIndex"),
        ("SYMBOL-WS5000-MIB", "ccRouteIndex"),
        ("SYMBOL-WS5000-MIB", "ccRouteDest"),
        ("SYMBOL-WS5000-MIB", "ccRouteGateway"),
        ("SYMBOL-WS5000-MIB", "ccRouteFlags"),
        ("SYMBOL-WS5000-MIB", "ccRouteRefs"),
        ("SYMBOL-WS5000-MIB", "ccRouteUse"),
        ("SYMBOL-WS5000-MIB", "ccRouteInterface"),
        ("SYMBOL-WS5000-MIB", "ccRouteAddObj"),
        ("SYMBOL-WS5000-MIB", "ccRouteRemObj"),
        ("SYMBOL-WS5000-MIB", "ccRouteFlush"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1Srv"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1Subnet"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1Netmask"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1BcastIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RouterIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1PriDNSIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1SecDNSIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1DomainName"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1DefLease"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1MaxLease"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RangeIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RangeStartIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RangeEndIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1AddIPRangeObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RemIPRangeObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1StaticIPIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1StaticIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1StaticMac"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1StaticHost"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1AddStaticIPObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RemStaticIPObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1OptionIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1OptionName"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1OptionCode"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1OptionType"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1OptionValue"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1AddOptionObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RemOptionObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1LeaseIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1LeaseIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1LeaseMac"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1LeaseStartTime"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1LeaseEndTime"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RemLeaseObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2Srv"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2Subnet"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2Netmask"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2BcastIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RouterIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2PriDNSIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2SecDNSIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2DomainName"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2DefLease"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2MaxLease"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RangeIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RangeStartIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RangeEndIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2AddIPRangeObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RemIPRangeObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2StaticIPIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2StaticIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2StaticMac"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2StaticHost"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2AddStaticIPObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RemStaticIPObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2OptionIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2OptionName"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2OptionCode"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2OptionType"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2OptionValue"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2AddOptionObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RemOptionObj"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2LeaseIndex"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2LeaseIP"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2LeaseMac"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2LeaseStartTime"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2LeaseEndTime"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RemLeaseObj"),
        ("SYMBOL-WS5000-MIB", "wvpnServerEnable"),
        ("SYMBOL-WS5000-MIB", "wvpnServerDisable"),
        ("SYMBOL-WS5000-MIB", "wvpnServerRestart"),
        ("SYMBOL-WS5000-MIB", "wvpnIpAddress"),
        ("SYMBOL-WS5000-MIB", "wvpnPort"),
        ("SYMBOL-WS5000-MIB", "wvpnUnusedTimeout"),
        ("SYMBOL-WS5000-MIB", "wvpnStatus"),
        ("SYMBOL-WS5000-MIB", "dosEnable"),
        ("SYMBOL-WS5000-MIB", "dosPort"),
        ("SYMBOL-WS5000-MIB", "clientKeepAlive"),
        ("SYMBOL-WS5000-MIB", "vpnLicenseMax"),
        ("SYMBOL-WS5000-MIB", "vpnLicenseInUse"),
        ("SYMBOL-WS5000-MIB", "maxClientRsaKeySize"),
        ("SYMBOL-WS5000-MIB", "minClientRsaKeySize"),
        ("SYMBOL-WS5000-MIB", "maxRsaKeySize"),
        ("SYMBOL-WS5000-MIB", "minRsaKeySize"),
        ("SYMBOL-WS5000-MIB", "cipher"),
        ("SYMBOL-WS5000-MIB", "mac"),
        ("SYMBOL-WS5000-MIB", "requireClientCertificate"),
        ("SYMBOL-WS5000-MIB", "keyRefresh"),
        ("SYMBOL-WS5000-MIB", "wantedFipsMode"),
        ("SYMBOL-WS5000-MIB", "securityMode"),
        ("SYMBOL-WS5000-MIB", "serverNumber"),
        ("SYMBOL-WS5000-MIB", "handshakeTimeout"),
        ("SYMBOL-WS5000-MIB", "allowSessionResume"),
        ("SYMBOL-WS5000-MIB", "useSimpleAuthentication"),
        ("SYMBOL-WS5000-MIB", "useRadiusAuthentication"),
        ("SYMBOL-WS5000-MIB", "useLdapAuthentication"),
        ("SYMBOL-WS5000-MIB", "useLocalDatabaseAuthentication"),
        ("SYMBOL-WS5000-MIB", "simpleAuthUserName"),
        ("SYMBOL-WS5000-MIB", "simpleAuthPassword"),
        ("SYMBOL-WS5000-MIB", "simpleAuthDomain"),
        ("SYMBOL-WS5000-MIB", "radiusAuthPrimaryHost"),
        ("SYMBOL-WS5000-MIB", "radiusAuthPrimaryPort"),
        ("SYMBOL-WS5000-MIB", "radiusAuthPrimaryMaxRetries"),
        ("SYMBOL-WS5000-MIB", "radiusAuthPrimaryTimeOut"),
        ("SYMBOL-WS5000-MIB", "radiusAuthPrimaryUserPassword"),
        ("SYMBOL-WS5000-MIB", "radiusAuthPrimarySecret"),
        ("SYMBOL-WS5000-MIB", "radiusAuthSecondaryHost"),
        ("SYMBOL-WS5000-MIB", "radiusAuthSecondaryPort"),
        ("SYMBOL-WS5000-MIB", "radiusAuthSecondaryMaxRetries"),
        ("SYMBOL-WS5000-MIB", "radiusAuthSecondaryTimeOut"),
        ("SYMBOL-WS5000-MIB", "radiusAuthSecondaryUserPassword"),
        ("SYMBOL-WS5000-MIB", "radiusAuthSecondarySecret"),
        ("SYMBOL-WS5000-MIB", "wvpnAddIpPoolObj"),
        ("SYMBOL-WS5000-MIB", "wvpnRemIpPoolObj"),
        ("SYMBOL-WS5000-MIB", "wvpnAddIpPoolRange"),
        ("SYMBOL-WS5000-MIB", "wvpnRemIpPoolRange"),
        ("SYMBOL-WS5000-MIB", "useDhcpGateway"),
        ("SYMBOL-WS5000-MIB", "wvpnIpPoolIndex"),
        ("SYMBOL-WS5000-MIB", "clientIpPoolName"),
        ("SYMBOL-WS5000-MIB", "clientNetMask"),
        ("SYMBOL-WS5000-MIB", "clientDhcpServerAddress"),
        ("SYMBOL-WS5000-MIB", "clientDefaultGatewayAddress"),
        ("SYMBOL-WS5000-MIB", "clientDnsAddress"),
        ("SYMBOL-WS5000-MIB", "clientWinsAddress"),
        ("SYMBOL-WS5000-MIB", "clientDomainName"),
        ("SYMBOL-WS5000-MIB", "clientNetBiosNodeType"),
        ("SYMBOL-WS5000-MIB", "clientDhcpLeaseTime"),
        ("SYMBOL-WS5000-MIB", "reuseAddrTime"),
        ("SYMBOL-WS5000-MIB", "ipRangeCount"),
        ("SYMBOL-WS5000-MIB", "clientIpRanges"),
        ("SYMBOL-WS5000-MIB", "wvpnIpPoolsCount"),
        ("SYMBOL-WS5000-MIB", "wvpnIpPoolsNames"),
        ("SYMBOL-WS5000-MIB", "wvpnCertIndex"),
        ("SYMBOL-WS5000-MIB", "userName"),
        ("SYMBOL-WS5000-MIB", "serialNumber"),
        ("SYMBOL-WS5000-MIB", "subject"),
        ("SYMBOL-WS5000-MIB", "version"),
        ("SYMBOL-WS5000-MIB", "issuer"),
        ("SYMBOL-WS5000-MIB", "keyLength"),
        ("SYMBOL-WS5000-MIB", "validFrom"),
        ("SYMBOL-WS5000-MIB", "validTo"),
        ("SYMBOL-WS5000-MIB", "certificate"),
        ("SYMBOL-WS5000-MIB", "binary"),
        ("SYMBOL-WS5000-MIB", "fingerPrint"),
        ("SYMBOL-WS5000-MIB", "authFingerPrint"),
        ("SYMBOL-WS5000-MIB", "serverCertCount"),
        ("SYMBOL-WS5000-MIB", "serverCertUserNames"),
        ("SYMBOL-WS5000-MIB", "wvpnCaCertIndex"),
        ("SYMBOL-WS5000-MIB", "wvpnCaSerialNumber"),
        ("SYMBOL-WS5000-MIB", "wvpnCaSubject"),
        ("SYMBOL-WS5000-MIB", "wvpnCaVersion"),
        ("SYMBOL-WS5000-MIB", "wvpnCaIssuer"),
        ("SYMBOL-WS5000-MIB", "wvpnCaKeyLength"),
        ("SYMBOL-WS5000-MIB", "wvpnCaValidFrom"),
        ("SYMBOL-WS5000-MIB", "wvpnCaValidTo"),
        ("SYMBOL-WS5000-MIB", "wvpnCaBinary"),
        ("SYMBOL-WS5000-MIB", "wvpnCaFingerPrint"),
        ("SYMBOL-WS5000-MIB", "wvpnCaAuthFingerPrint"),
        ("SYMBOL-WS5000-MIB", "caCertCount"),
        ("SYMBOL-WS5000-MIB", "certSerialNumbers"),
        ("SYMBOL-WS5000-MIB", "importServerCert"),
        ("SYMBOL-WS5000-MIB", "removeServerCert"),
        ("SYMBOL-WS5000-MIB", "importCaCert"),
        ("SYMBOL-WS5000-MIB", "removeCaCert"),
        ("SYMBOL-WS5000-MIB", "importTftpServerCert"),
        ("SYMBOL-WS5000-MIB", "importTftpCaCert"),
        ("SYMBOL-WS5000-MIB", "dirCert"),
        ("SYMBOL-WS5000-MIB", "dumpCert"),
        ("SYMBOL-WS5000-MIB", "clearClientDNS"),
        ("SYMBOL-WS5000-MIB", "updateClientDNS"),
        ("SYMBOL-WS5000-MIB", "addDNSAddr"),
        ("SYMBOL-WS5000-MIB", "deleteDNSAddr"),
        ("SYMBOL-WS5000-MIB", "enable"),
        ("SYMBOL-WS5000-MIB", "ttl"),
        ("SYMBOL-WS5000-MIB", "forwardZone"),
        ("SYMBOL-WS5000-MIB", "reverseZone"),
        ("SYMBOL-WS5000-MIB", "clientNameString"),
        ("SYMBOL-WS5000-MIB", "wvpnDDNSAddressIndex"),
        ("SYMBOL-WS5000-MIB", "wvpnDDNSipAddress"),
        ("SYMBOL-WS5000-MIB", "ccRadiusDataSource"),
        ("SYMBOL-WS5000-MIB", "ccRadiusDefaultEapType"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAuthTypePeap"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAuthTypeTtls"),
        ("SYMBOL-WS5000-MIB", "ccRadiusServerCertificate"),
        ("SYMBOL-WS5000-MIB", "ccRadiusCACertificate"),
        ("SYMBOL-WS5000-MIB", "ccRadiusClientAuthIndex"),
        ("SYMBOL-WS5000-MIB", "ccRadiusClientAuthIpAddr"),
        ("SYMBOL-WS5000-MIB", "ccRadiusClientAuthMask"),
        ("SYMBOL-WS5000-MIB", "ccRadiusClientAuthSharedSecret"),
        ("SYMBOL-WS5000-MIB", "ccRadiusClientAuthRowStatus"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyRetryCount"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyTimeout"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyServerIndex"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyServerPrefixOrSuffix"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyServerIp"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyServerPort"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyServerSharedSecret"),
        ("SYMBOL-WS5000-MIB", "ccRadiusProxyServerRowStatus"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1ServerIp"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1ServerPort"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1LoginAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1PasswordAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1BindDistinguishedName"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1BindDistinguishedPassword"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1BaseDistinguishedName"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1GroupAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1GroupFilter"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap1GroupMembershipAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2ServerIp"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2ServerPort"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2LoginAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2PasswordATtribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2BindDistinguishedName"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2BindDistinguishedPassword"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2BaseDistinguishedName"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2GroupAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2GroupFilter"),
        ("SYMBOL-WS5000-MIB", "ccRadiusLdap2GroupMembershipAttribute"),
        ("SYMBOL-WS5000-MIB", "ccRadiusUsersId"),
        ("SYMBOL-WS5000-MIB", "ccRadiusUsersPassword"),
        ("SYMBOL-WS5000-MIB", "ccRadiusUsersRowStatus"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAcctIPAddress"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAcctPort"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAcctTimeout"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAcctMaxRetry"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAcctSharedSecret"),
        ("SYMBOL-WS5000-MIB", "ccRapPollSymbolMusEnable"),
        ("SYMBOL-WS5000-MIB", "ccRapPollSymbolMusInterval"),
        ("SYMBOL-WS5000-MIB", "ccRapOnChannelEnable"),
        ("SYMBOL-WS5000-MIB", "ccRapOnChannelInterval"),
        ("SYMBOL-WS5000-MIB", "ccRapDetectorsEnable"),
        ("SYMBOL-WS5000-MIB", "ccRapDetectorsInterval"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthAllSymbolMac"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthIndex"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthMacFilter"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthEssidFilter"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthRowExists"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthErase"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthCopyAllApproved"),
        ("SYMBOL-WS5000-MIB", "ccRapAuthCopyAllRogue"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedAgeOut"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedIndex"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedApMac"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedEssid"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedCopyToAuthTable"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedFirstHeard"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedLastHeard"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedPortalPtr"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedHowFound"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedHowAuth"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedErase"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueAgeOut"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueIndex"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueApMac"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueEssid"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueCopyToAuthTable"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueFirstHeard"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueLastHeard"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRoguePortalPtr"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueHowFound"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueClosestPortalPtr"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueClosestPortalRssi"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsRogueErase"),
        ("SYMBOL-WS5000-MIB", "ccRestore"),
        ("SYMBOL-WS5000-MIB", "ccFtp"),
        ("SYMBOL-WS5000-MIB", "ccTftp"),
        ("SYMBOL-WS5000-MIB", "ccListFiles"),
        ("SYMBOL-WS5000-MIB", "ccRadiusTimeRestrictionStart"),
        ("SYMBOL-WS5000-MIB", "wvpnSessionIndex"),
        ("SYMBOL-WS5000-MIB", "wvpnSessionId"),
        ("SYMBOL-WS5000-MIB", "wvpnVpnIp"),
        ("SYMBOL-WS5000-MIB", "wvpnRealIp"),
        ("SYMBOL-WS5000-MIB", "wvpnLoginTime"),
        ("SYMBOL-WS5000-MIB", "wvpnRoamTime"),
        ("SYMBOL-WS5000-MIB", "wvpnLastActive"),
        ("SYMBOL-WS5000-MIB", "wvpnPoolName"),
        ("SYMBOL-WS5000-MIB", "wvpnMacAddr"),
        ("SYMBOL-WS5000-MIB", "wvpnSessionCount"),
        ("SYMBOL-WS5000-MIB", "wvpnRefreshSession"),
        ("SYMBOL-WS5000-MIB", "wvpnKillSession"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoWVPNAlert"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoWVPNInfo"),
        ("SYMBOL-WS5000-MIB", "ccEnableWVPNSupport"),
        ("SYMBOL-WS5000-MIB", "cleanupTimeout"),
        ("SYMBOL-WS5000-MIB", "reverseZoneList"),
        ("SYMBOL-WS5000-MIB", "reverseZoneAdd"),
        ("SYMBOL-WS5000-MIB", "reverseZoneDel"),
        ("SYMBOL-WS5000-MIB", "ccRadiusSaveStatus"),
        ("SYMBOL-WS5000-MIB", "ccRapResultsApprovedRowErase"),
        ("SYMBOL-WS5000-MIB", "ccDetectorAp"),
        ("SYMBOL-WS5000-MIB", "ccEnableRap"),
        ("SYMBOL-WS5000-MIB", "ccDeleteFiles"),
        ("SYMBOL-WS5000-MIB", "ccRapNewRogueApControl"),
        ("SYMBOL-WS5000-MIB", "ccRapNewApprovedApControl"),
        ("SYMBOL-WS5000-MIB", "ccRadiusTimeRestrictionEnd"),
        ("SYMBOL-WS5000-MIB", "ccAvgSNR"),
        ("SYMBOL-WS5000-MIB", "ccFWLanRemObj"),
        ("SYMBOL-WS5000-MIB", "ccFWLanAddObj"),
        ("SYMBOL-WS5000-MIB", "remkdcMu"),
        ("SYMBOL-WS5000-MIB", "addkdcMu"),
        ("SYMBOL-WS5000-MIB", "ccAvgRSSI"),
        ("SYMBOL-WS5000-MIB", "ccAvgTxRetry"),
        ("SYMBOL-WS5000-MIB", "ccAPRxPPS"),
        ("SYMBOL-WS5000-MIB", "ccAPTxPPS"),
        ("SYMBOL-WS5000-MIB", "ccEPPrimaryVid"),
        ("SYMBOL-WS5000-MIB", "ccRadioUser802x"),
        ("SYMBOL-WS5000-MIB", "ccSimulateRadar"),
        ("SYMBOL-WS5000-MIB", "ccRadioMaxMUs"),
        ("SYMBOL-WS5000-MIB", "ccRadioMUs"),
        ("SYMBOL-WS5000-MIB", "ccRadiusServerEnable"),
        ("SYMBOL-WS5000-MIB", "ccRadiusEapPasswd"),
        ("SYMBOL-WS5000-MIB", "ccInfoRadiusServerControl"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoRadiusAcct"),
        ("SYMBOL-WS5000-MIB", "ccRouteGenMask"),
        ("SYMBOL-WS5000-MIB", "ccDhcp2RemStaticHost"),
        ("SYMBOL-WS5000-MIB", "ccDhcp1RemStaticHost"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAccessWlanPtrs"),
        ("SYMBOL-WS5000-MIB", "ccRadiusAccessGroupId"),
        ("SYMBOL-WS5000-MIB", "ccRadiusUsersGroups"),
        ("SYMBOL-WS5000-MIB", "ccRadiusGroupRowStatus"),
        ("SYMBOL-WS5000-MIB", "ccRadiusGroup"),
        ("SYMBOL-WS5000-MIB", "ccLANPfDeny"),
        ("SYMBOL-WS5000-MIB", "ccLANPfAllow"),
        ("SYMBOL-WS5000-MIB", "ccRadiusTimeRestrictionDays"),
        ("SYMBOL-WS5000-MIB", "ccLANNATRemoteRealIP"),
        ("SYMBOL-WS5000-MIB", "ccLANNATLocalNatIP"),
        ("SYMBOL-WS5000-MIB", "ccSecVPNEnabled"))
)
if mibBuilder.loadTexts:
    v2dot0Group.setStatus("current")

v2dot0GroupOfDepricated = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 3)
)
v2dot0GroupOfDepricated.setObjects(
    ("SYMBOL-WS5000-MIB", "ccAccessMethodsPermitted")
)
if mibBuilder.loadTexts:
    v2dot0GroupOfDepricated.setStatus("deprecated")

v2dot1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 4)
)
v2dot1Group.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccWMEprofileQosParam"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc4BkAifsn"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc4BkAgTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc4BkTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc4BkEcwmax"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc4BkEcwmin"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc3BeAifsn"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc3BeAgTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc3BeEcwmax"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc3BeEcwmin"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc2ViAifsn"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc2ViAgTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc2ViTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc2ViEcwmax"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc2ViEcwmin"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc1VoAifsn"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc1VoAgTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc1VoTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc1VoEcwmax"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc1VoEcwmin"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileDesc"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofilename"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileIndex"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptSum"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptWorst"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptBest"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptNumBeaconsHeard"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptPortalIndex"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRptLastHeard"),
        ("SYMBOL-WS5000-MIB", "ccMuProbeRptSignalMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccMuProbeRptLastHeard"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyWMEProfile"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyWMEEnable"),
        ("SYMBOL-WS5000-MIB", "ccWlanWMEProfile"),
        ("SYMBOL-WS5000-MIB", "ccWlanWMEEnable"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileRowStatus"),
        ("SYMBOL-WS5000-MIB", "configChangeUpdateControl"),
        ("SYMBOL-WS5000-MIB", "ccNtpPrefTimeServer"),
        ("SYMBOL-WS5000-MIB", "ccNtpFirstAltTimeServer"),
        ("SYMBOL-WS5000-MIB", "ccNtpSecondAltTimeServer"),
        ("SYMBOL-WS5000-MIB", "ccNtpGroupSetTimeServer"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyDTIM4"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyDTIM3"),
        ("SYMBOL-WS5000-MIB", "ccAPPolicyDTIM2"),
        ("SYMBOL-WS5000-MIB", "tunnelUnknownProtocolControl"),
        ("SYMBOL-WS5000-MIB", "tunnelStatusChangedControl"),
        ("SYMBOL-WS5000-MIB", "ccApSensorDhcp"),
        ("SYMBOL-WS5000-MIB", "ccApSensorSecondary"),
        ("SYMBOL-WS5000-MIB", "ccApSensorPrimary"),
        ("SYMBOL-WS5000-MIB", "ccApSensorGateWay"),
        ("SYMBOL-WS5000-MIB", "ccApSensorMask"),
        ("SYMBOL-WS5000-MIB", "ccApSensorIpaddress"),
        ("SYMBOL-WS5000-MIB", "ccSensorRevert"),
        ("SYMBOL-WS5000-MIB", "ccSensorConvert"),
        ("SYMBOL-WS5000-MIB", "ccSensorList"),
        ("SYMBOL-WS5000-MIB", "ccApSensorIndex"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsSwitchControl"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsWlanControl"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsMuControl"),
        ("SYMBOL-WS5000-MIB", "ccApList"),
        ("SYMBOL-WS5000-MIB", "ccMuProbeRptFoundMac"),
        ("SYMBOL-WS5000-MIB", "ccMuProbeRptFinderMac"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRpFoundMac"),
        ("SYMBOL-WS5000-MIB", "ccPortalBeaconRpFinderMac"),
        ("SYMBOL-WS5000-MIB", "ccEPDhcpPriVlan"),
        ("SYMBOL-WS5000-MIB", "sensorOfflineControl"),
        ("SYMBOL-WS5000-MIB", "sensorFailureControl"),
        ("SYMBOL-WS5000-MIB", "sensorRevertControl"),
        ("SYMBOL-WS5000-MIB", "sensorConvertControl"),
        ("SYMBOL-WS5000-MIB", "ccSensorEnable"),
        ("SYMBOL-WS5000-MIB", "ccApSensorMac"),
        ("SYMBOL-WS5000-MIB", "ccEPDDNSUpdateAll"),
        ("SYMBOL-WS5000-MIB", "ccEPDDNSttl"),
        ("SYMBOL-WS5000-MIB", "ccEPDDNSStatus"),
        ("SYMBOL-WS5000-MIB", "ccNtpDelAll"),
        ("SYMBOL-WS5000-MIB", "ccConfigChangeLast"),
        ("SYMBOL-WS5000-MIB", "ccEPDDNSDomainName"),
        ("SYMBOL-WS5000-MIB", "ccEPDDNSMUserStatus"),
        ("SYMBOL-WS5000-MIB", "ccMUInfoRoamCount"),
        ("SYMBOL-WS5000-MIB", "ccWMEprofileAc3BeTxopLimit"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsApControl"))
)
if mibBuilder.loadTexts:
    v2dot1Group.setStatus("current")

v2dot1StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 6)
)
v2dot1StatsGroup.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccApIndex"),
        ("SYMBOL-WS5000-MIB", "ccApNicMac"),
        ("SYMBOL-WS5000-MIB", "ccApModelNumber"),
        ("SYMBOL-WS5000-MIB", "ccApSerialNumber"),
        ("SYMBOL-WS5000-MIB", "ccApPcbRevision"),
        ("SYMBOL-WS5000-MIB", "ccApBootLoaderRev"),
        ("SYMBOL-WS5000-MIB", "ccApWispVersion"),
        ("SYMBOL-WS5000-MIB", "ccApRuntimeFwVersion"),
        ("SYMBOL-WS5000-MIB", "ccApNumPortals"),
        ("SYMBOL-WS5000-MIB", "ccApPointersToPortals"),
        ("SYMBOL-WS5000-MIB", "ccPortalIndex"),
        ("SYMBOL-WS5000-MIB", "ccPortalPointerToAp"),
        ("SYMBOL-WS5000-MIB", "ccPortalPointersToWlans"),
        ("SYMBOL-WS5000-MIB", "ccPortalName"),
        ("SYMBOL-WS5000-MIB", "ccPortalLocation"),
        ("SYMBOL-WS5000-MIB", "ccPortalOptions"),
        ("SYMBOL-WS5000-MIB", "ccPortalMac"),
        ("SYMBOL-WS5000-MIB", "ccPortalNumberofEss"),
        ("SYMBOL-WS5000-MIB", "ccPortalNumberOfBss"),
        ("SYMBOL-WS5000-MIB", "ccPortalAssociatedMus"),
        ("SYMBOL-WS5000-MIB", "ccPortalRadioType"),
        ("SYMBOL-WS5000-MIB", "ccPortalChannel"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPowerLevel"),
        ("SYMBOL-WS5000-MIB", "ccPortalLastAdoption"),
        ("SYMBOL-WS5000-MIB", "ccPortalState"),
        ("SYMBOL-WS5000-MIB", "ccPortalBackgroundNoiseNumSamples"),
        ("SYMBOL-WS5000-MIB", "ccPortalBackgroundNoiseBest"),
        ("SYMBOL-WS5000-MIB", "ccPortalBackgroundNoiseWorst"),
        ("SYMBOL-WS5000-MIB", "ccPortalBackgroundNoiseSum"),
        ("SYMBOL-WS5000-MIB", "ccPortalBackgroundNoiseSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccPortalLastMac"),
        ("SYMBOL-WS5000-MIB", "ccPortalLastReason"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsBeaconTx"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsBeaconsTxOctets"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeReqRx"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeReqRxOctets"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeRespRetriesNone"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeRespRetries1"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeRespRetries2"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeRespRetries3OrMore"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeRespRetriesFailed"),
        ("SYMBOL-WS5000-MIB", "ccPortalSystemStatsProbeRespTxOctets"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsUcast"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsUcast"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsNUcast"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsUcast"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsUcast"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsNUcast"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxUndecryptablePkts"),
        ("SYMBOL-WS5000-MIB", "ccPortalLastActivity"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxPktsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxPktsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalRxOctetsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxOctetsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPktsNone"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts01"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts02"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts03"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts04"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts05"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts06"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts07"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts08"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts09"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts10"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts11"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts12"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts13"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts14"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPktsFailed"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctetsNone"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets01"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets02"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets03"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets04"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets05"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets06"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets07"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets08"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets09"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets10"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets11"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets12"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets13"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets14"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctetsFailed"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSignalBest"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSignalWorst"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSignalSum"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSignalSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSignalMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsNoiseBest"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsNoiseWorst"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsNoiseSum"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsNoiseSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsNoiseMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSnrBest"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSnrWorst"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSnrSum"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSnrSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccPortalSigStatsSnrMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortTimestamp"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPktsPerSec100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortThroughput"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortThroughputTx"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortThroughputRx"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortAvgBitSpeed"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortAvgMuSignal"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortAvgMuNoise"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortAvgMuSnr"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPp10kTxMaxRetries"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortTxAvgRetries100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortTotalMus"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPp10kRfUtil"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsShortPp10kDropped"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongTimestamp"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPktsPerSec100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongThroughput"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongThroughputTx"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongThroughputRx"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongAvgBitSpeed"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongAvgMuSignal"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongAvgMuNoise"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongAvgMuSnr"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPp10kTxMaxRetries"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongTxAvgRetries100"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongTotalMus"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPp10kRfUtil"),
        ("SYMBOL-WS5000-MIB", "ccPortalSumStatsLongPp10kDropped"),
        ("SYMBOL-WS5000-MIB", "ccMuMac"),
        ("SYMBOL-WS5000-MIB", "ccMuWlanIndex"),
        ("SYMBOL-WS5000-MIB", "ccMuWlanName"),
        ("SYMBOL-WS5000-MIB", "ccMuIsDataReady"),
        ("SYMBOL-WS5000-MIB", "ccMuPortalIndex"),
        ("SYMBOL-WS5000-MIB", "ccMuPortalMac"),
        ("SYMBOL-WS5000-MIB", "ccMuSymbolRogueApEna"),
        ("SYMBOL-WS5000-MIB", "ccMuIpAddr"),
        ("SYMBOL-WS5000-MIB", "ccMuType"),
        ("SYMBOL-WS5000-MIB", "ccMuRadioType"),
        ("SYMBOL-WS5000-MIB", "ccMuSupportedRates"),
        ("SYMBOL-WS5000-MIB", "ccMuPowerMode"),
        ("SYMBOL-WS5000-MIB", "ccMuAuthenticationMethod"),
        ("SYMBOL-WS5000-MIB", "ccMuEncryptionMethod"),
        ("SYMBOL-WS5000-MIB", "ccMuVlanId"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsUcast"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsUcast"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsNUcast"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsUcast"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsUcast"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsNUcast"),
        ("SYMBOL-WS5000-MIB", "ccMuRxUndecryptablePkts"),
        ("SYMBOL-WS5000-MIB", "ccMuRxRssiNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccMuRxRssiSum"),
        ("SYMBOL-WS5000-MIB", "ccMuRxRssiSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccMuRxRssiMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccMuLastActivity"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxPktsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxPktsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuRxOctetsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt1Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt2Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt5pt5Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt6Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt9Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt11Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt12Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt18Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt22Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt24Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt36Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt48Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxOctetsAt54Mb"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesNone"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries01"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries02"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries03"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries04"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries05"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries06"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries07"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries08"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries09"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries10"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries11"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries12"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries13"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries14"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesFailed"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesTotal"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccMuLastMac"),
        ("SYMBOL-WS5000-MIB", "ccMuLastReason"),
        ("SYMBOL-WS5000-MIB", "ccMuLastPortal"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctetsNone"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets01"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets02"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets03"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets04"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets05"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets06"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets07"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets08"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets09"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets10"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets11"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets12"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets13"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets14"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctetsFailed"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSignalBest"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSignalWorst"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSignalSum"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSignalSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSignalMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsNoiseBest"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsNoiseWorst"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsNoiseSum"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsNoiseSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsNoiseMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSnrBest"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSnrWorst"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSnrSum"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSnrSumSquares"),
        ("SYMBOL-WS5000-MIB", "ccMuSigStatsSnrMostRecent"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortTimestamp"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPktsPerSec100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortThroughput"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortThroughputTx"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortThroughputRx"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortAvgBitSpeed"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortAvgMuSignal"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortAvgMuNoise"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortAvgMuSnr"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPp10kDropped"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortTxAvgRetries100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongTimestamp"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongNumPkts"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPktsPerSec100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongThroughput"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongThroughputTx"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongThroughputRx"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongAvgBitSpeed"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongAvgMuSignal"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongAvgMuNoise"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongAvgMuSnr"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPp10kDropped"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongTxAvgRetries100"),
        ("SYMBOL-WS5000-MIB", "ccMuSumStatsLongPp10kRxUndecrypt"))
)
if mibBuilder.loadTexts:
    v2dot1StatsGroup.setStatus("current")

v2dot0GroupOfDeprecated = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 7)
)
v2dot0GroupOfDeprecated.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccPortalTxRetriesPkts15"),
        ("SYMBOL-WS5000-MIB", "ccPortalTxRetriesOctets15"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetries15"),
        ("SYMBOL-WS5000-MIB", "ccMuTxRetriesOctets15"))
)
if mibBuilder.loadTexts:
    v2dot0GroupOfDeprecated.setStatus("deprecated")


# Notification objects

ccTrapLowFlashSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 1)
)
ccTrapLowFlashSpace.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapLowFlashSpace.setStatus(
        "current"
    )

ccTrapNicDropping = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 3)
)
ccTrapNicDropping.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapNicDropping.setStatus(
        "current"
    )

ccTrapAPMUMaxExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 6)
)
ccTrapAPMUMaxExceed.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapAPMUMaxExceed.setStatus(
        "current"
    )

ccTrapWLANMUMaxExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 7)
)
ccTrapWLANMUMaxExceed.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapWLANMUMaxExceed.setStatus(
        "current"
    )

ccTrapAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 8)
)
ccTrapAPDetected.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapAPDetected.setStatus(
        "current"
    )

ccTrapAPAdopted = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 9)
)
ccTrapAPAdopted.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapAPAdopted.setStatus(
        "current"
    )

ccTrapAPReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 10)
)
ccTrapAPReset.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapAPReset.setStatus(
        "current"
    )

ccTrapAPUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 11)
)
ccTrapAPUnavailable.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapAPUnavailable.setStatus(
        "current"
    )

ccTrapAPAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 12)
)
ccTrapAPAlert.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapAPAlert.setStatus(
        "current"
    )

ccTrapUserAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 13)
)
ccTrapUserAuthFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapUserAuthFail.setStatus(
        "current"
    )

ccTrapRadiusAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 14)
)
ccTrapRadiusAuthFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapRadiusAuthFail.setStatus(
        "current"
    )

ccTrapACLViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 16)
)
ccTrapACLViolation.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapACLViolation.setStatus(
        "current"
    )

ccTrapDenyAPAdoption = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 18)
)
ccTrapDenyAPAdoption.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapDenyAPAdoption.setStatus(
        "current"
    )

ccTrapHsbPrimaryNoHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 20)
)
ccTrapHsbPrimaryNoHeartbeat.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapHsbPrimaryNoHeartbeat.setStatus(
        "current"
    )

ccTrapHsbStandbyEntersFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 21)
)
ccTrapHsbStandbyEntersFailover.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapHsbStandbyEntersFailover.setStatus(
        "current"
    )

ccTrapHsbPrimaryFailedResetting = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 22)
)
ccTrapHsbPrimaryFailedResetting.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapHsbPrimaryFailedResetting.setStatus(
        "current"
    )

ccTrapHsbStandbyFailedResetting = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 23)
)
ccTrapHsbStandbyFailedResetting.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapHsbStandbyFailedResetting.setStatus(
        "current"
    )

ccTrapKDCUserAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 24)
)
ccTrapKDCUserAuthFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapKDCUserAuthFail.setStatus(
        "current"
    )

ccTrapKDCPropagationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 25)
)
ccTrapKDCPropagationFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapKDCPropagationFail.setStatus(
        "current"
    )

ccTrapHighDecryptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 26)
)
ccTrapHighDecryptFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapHighDecryptFail.setStatus(
        "current"
    )

ccTrapHighReplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 27)
)
ccTrapHighReplyFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapHighReplyFail.setStatus(
        "current"
    )

ccTrapTKIPMICFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 28)
)
ccTrapTKIPMICFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapTKIPMICFail.setStatus(
        "current"
    )

ccTrapWPACounterMeasureStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 29)
)
ccTrapWPACounterMeasureStart.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapWPACounterMeasureStart.setStatus(
        "current"
    )

licenseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 31)
)
licenseChanged.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    licenseChanged.setStatus(
        "current"
    )

clockChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 32)
)
clockChanged.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    clockChanged.setStatus(
        "current"
    )

pktDiscWrongNIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 33)
)
pktDiscWrongNIC.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    pktDiscWrongNIC.setStatus(
        "current"
    )

pktDiscWrongVLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 34)
)
pktDiscWrongVLAN.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    pktDiscWrongVLAN.setStatus(
        "current"
    )

apAdoptFailPol = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 35)
)
apAdoptFailPol.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    apAdoptFailPol.setStatus(
        "current"
    )

apAdoptFailACL = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 36)
)
apAdoptFailACL.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    apAdoptFailACL.setStatus(
        "current"
    )

apAdoptFailLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 37)
)
apAdoptFailLimit.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    apAdoptFailLimit.setStatus(
        "current"
    )

apAdoptFailLic = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 38)
)
apAdoptFailLic.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    apAdoptFailLic.setStatus(
        "current"
    )

apAdoptFailNoImg = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 39)
)
apAdoptFailNoImg.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    apAdoptFailNoImg.setStatus(
        "current"
    )

apCfgFailESS = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 40)
)
apCfgFailESS.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    apCfgFailESS.setStatus(
        "current"
    )

devDropInfoMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 41)
)
devDropInfoMsg.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    devDropInfoMsg.setStatus(
        "current"
    )

devdropLoadmeMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 42)
)
devdropLoadmeMsg.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    devdropLoadmeMsg.setStatus(
        "current"
    )

etherConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 43)
)
etherConnect.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    etherConnect.setStatus(
        "current"
    )

muAssocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 44)
)
muAssocFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muAssocFail.setStatus(
        "current"
    )

muAssocOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 45)
)
muAssocOK.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muAssocOK.setStatus(
        "current"
    )

muRoamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 46)
)
muRoamed.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muRoamed.setStatus(
        "current"
    )

muDisassoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 47)
)
muDisassoc.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muDisassoc.setStatus(
        "current"
    )

muEAPAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 48)
)
muEAPAuthFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muEAPAuthFail.setStatus(
        "current"
    )

muEAPAuthOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 49)
)
muEAPAuthOK.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muEAPAuthOK.setStatus(
        "current"
    )

muKDCAuthOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 50)
)
muKDCAuthOK.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    muKDCAuthOK.setStatus(
        "current"
    )

wlanAuthOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 51)
)
wlanAuthOK.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    wlanAuthOK.setStatus(
        "current"
    )

wlanAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 52)
)
wlanAuthFail.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    wlanAuthFail.setStatus(
        "current"
    )

userAuthOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 53)
)
userAuthOK.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    userAuthOK.setStatus(
        "current"
    )

radiusSrvTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 54)
)
radiusSrvTimeout.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    radiusSrvTimeout.setStatus(
        "current"
    )

kdcPrincAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 55)
)
kdcPrincAdd.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    kdcPrincAdd.setStatus(
        "current"
    )

kdcPrincChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 56)
)
kdcPrincChgd.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    kdcPrincChgd.setStatus(
        "current"
    )

kdcPrincDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 57)
)
kdcPrincDel.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    kdcPrincDel.setStatus(
        "current"
    )

kdcDBReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 58)
)
kdcDBReplaced.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    kdcDBReplaced.setStatus(
        "current"
    )

hsbStdbyAutoRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 59)
)
hsbStdbyAutoRev.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    hsbStdbyAutoRev.setStatus(
        "current"
    )

hsbPrimAutoRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 60)
)
hsbPrimAutoRev.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    hsbPrimAutoRev.setStatus(
        "current"
    )

acsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 61)
)
acsError.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    acsError.setStatus(
        "current"
    )

eopActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 62)
)
eopActive.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    eopActive.setStatus(
        "current"
    )

eopInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 63)
)
eopInactive.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    eopInactive.setStatus(
        "current"
    )

debugEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 64)
)
debugEvent.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    debugEvent.setStatus(
        "current"
    )

hsbStartUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 65)
)
hsbStartUp.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    hsbStartUp.setStatus(
        "current"
    )

hsbPeerConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 66)
)
hsbPeerConnect.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    hsbPeerConnect.setStatus(
        "current"
    )

ccFanAndTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 67)
)
ccFanAndTempNotification.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccFanAndTempNotification.setStatus(
        "current"
    )

ccAccessChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 68)
)
ccAccessChangedNotification.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccAccessChangedNotification.setStatus(
        "current"
    )

tpcPowerReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 69)
)
tpcPowerReduced.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    tpcPowerReduced.setStatus(
        "current"
    )

dfsRadarDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 70)
)
dfsRadarDetect.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    dfsRadarDetect.setStatus(
        "current"
    )

dfsChannelSelect = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 71)
)
dfsChannelSelect.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    dfsChannelSelect.setStatus(
        "current"
    )

dfsChannelSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 72)
)
dfsChannelSwitch.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    dfsChannelSwitch.setStatus(
        "current"
    )

dfsChannelRevert = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 73)
)
dfsChannelRevert.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    dfsChannelRevert.setStatus(
        "current"
    )

radioSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 74)
)
radioSuspend.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    radioSuspend.setStatus(
        "current"
    )

radioResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 75)
)
radioResume.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    radioResume.setStatus(
        "current"
    )

radioRandomChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 76)
)
radioRandomChannel.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    radioRandomChannel.setStatus(
        "current"
    )

ccRapNewRogueAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 77)
)
ccRapNewRogueAp.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccRapNewRogueAp.setStatus(
        "current"
    )

ccRapNewApprovedAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 78)
)
ccRapNewApprovedAp.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccRapNewApprovedAp.setStatus(
        "current"
    )

ccTrapWVPNAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 79)
)
ccTrapWVPNAlert.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapWVPNAlert.setStatus(
        "current"
    )

ccTrapWVPNInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 80)
)
ccTrapWVPNInfo.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapWVPNInfo.setStatus(
        "current"
    )

ccTrapInfoRadiusAcctInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 81)
)
ccTrapInfoRadiusAcctInfo.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccTrapInfoRadiusAcctInfo.setStatus(
        "current"
    )

ccInfoRadiusServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 82)
)
ccInfoRadiusServer.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccInfoRadiusServer.setStatus(
        "current"
    )

configChangeUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 83)
)
configChangeUpdate.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    configChangeUpdate.setStatus(
        "current"
    )

tunnelStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 84)
)
tunnelStatusChanged.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    tunnelStatusChanged.setStatus(
        "current"
    )

tunnelUnknownProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 85)
)
tunnelUnknownProtocol.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    tunnelUnknownProtocol.setStatus(
        "current"
    )

ccSumStatsAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 86)
)
ccSumStatsAp.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccSumStatsAp.setStatus(
        "current"
    )

ccSumStatsMu = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 87)
)
ccSumStatsMu.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccSumStatsMu.setStatus(
        "current"
    )

ccSumStatsWlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 88)
)
ccSumStatsWlan.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccSumStatsWlan.setStatus(
        "current"
    )

ccSumStatsSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 89)
)
ccSumStatsSwitch.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    ccSumStatsSwitch.setStatus(
        "current"
    )

sensorConvert = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 90)
)
sensorConvert.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    sensorConvert.setStatus(
        "current"
    )

sensorRevert = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 91)
)
sensorRevert.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    sensorRevert.setStatus(
        "current"
    )

sensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 92)
)
sensorFailure.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    sensorFailure.setStatus(
        "current"
    )

sensorOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 6, 5, 3, 93)
)
sensorOffline.setObjects(
    ("SYMBOL-WS5000-MIB", "ccTargetTrapString")
)
if mibBuilder.loadTexts:
    sensorOffline.setStatus(
        "current"
    )


# Notifications groups

v1dot2dot5NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 6, 1000, 3)
)
v1dot2dot5NotificationGroup.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccTrapLowFlashSpace"),
        ("SYMBOL-WS5000-MIB", "ccTrapNicDropping"),
        ("SYMBOL-WS5000-MIB", "ccTrapAPMUMaxExceed"),
        ("SYMBOL-WS5000-MIB", "ccTrapWLANMUMaxExceed"),
        ("SYMBOL-WS5000-MIB", "ccTrapAPDetected"),
        ("SYMBOL-WS5000-MIB", "ccTrapAPAdopted"),
        ("SYMBOL-WS5000-MIB", "ccTrapAPReset"),
        ("SYMBOL-WS5000-MIB", "ccTrapAPUnavailable"),
        ("SYMBOL-WS5000-MIB", "ccTrapAPAlert"),
        ("SYMBOL-WS5000-MIB", "ccTrapUserAuthFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapRadiusAuthFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapACLViolation"),
        ("SYMBOL-WS5000-MIB", "ccTrapDenyAPAdoption"),
        ("SYMBOL-WS5000-MIB", "ccTrapHsbPrimaryNoHeartbeat"),
        ("SYMBOL-WS5000-MIB", "ccTrapHsbStandbyEntersFailover"),
        ("SYMBOL-WS5000-MIB", "ccTrapHsbPrimaryFailedResetting"),
        ("SYMBOL-WS5000-MIB", "ccTrapHsbStandbyFailedResetting"),
        ("SYMBOL-WS5000-MIB", "ccTrapKDCUserAuthFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapKDCPropagationFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapHighDecryptFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapHighReplyFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapTKIPMICFail"),
        ("SYMBOL-WS5000-MIB", "ccTrapWPACounterMeasureStart"),
        ("SYMBOL-WS5000-MIB", "hsbStartUp"),
        ("SYMBOL-WS5000-MIB", "ccFanAndTempNotification"),
        ("SYMBOL-WS5000-MIB", "ccAccessChangedNotification"),
        ("SYMBOL-WS5000-MIB", "radioRandomChannel"),
        ("SYMBOL-WS5000-MIB", "radioResume"),
        ("SYMBOL-WS5000-MIB", "radioSuspend"),
        ("SYMBOL-WS5000-MIB", "dfsChannelRevert"),
        ("SYMBOL-WS5000-MIB", "dfsChannelSwitch"),
        ("SYMBOL-WS5000-MIB", "dfsChannelSelect"),
        ("SYMBOL-WS5000-MIB", "dfsRadarDetect"),
        ("SYMBOL-WS5000-MIB", "tpcPowerReduced"),
        ("SYMBOL-WS5000-MIB", "hsbPeerConnect"),
        ("SYMBOL-WS5000-MIB", "licenseChanged"),
        ("SYMBOL-WS5000-MIB", "clockChanged"),
        ("SYMBOL-WS5000-MIB", "pktDiscWrongNIC"),
        ("SYMBOL-WS5000-MIB", "pktDiscWrongVLAN"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailPol"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailACL"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailLimit"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailLic"),
        ("SYMBOL-WS5000-MIB", "apAdoptFailNoImg"),
        ("SYMBOL-WS5000-MIB", "apCfgFailESS"),
        ("SYMBOL-WS5000-MIB", "devDropInfoMsg"),
        ("SYMBOL-WS5000-MIB", "devdropLoadmeMsg"),
        ("SYMBOL-WS5000-MIB", "etherConnect"),
        ("SYMBOL-WS5000-MIB", "muAssocFail"),
        ("SYMBOL-WS5000-MIB", "muAssocOK"),
        ("SYMBOL-WS5000-MIB", "muRoamed"),
        ("SYMBOL-WS5000-MIB", "muDisassoc"),
        ("SYMBOL-WS5000-MIB", "muEAPAuthFail"),
        ("SYMBOL-WS5000-MIB", "muEAPAuthOK"),
        ("SYMBOL-WS5000-MIB", "muKDCAuthOK"),
        ("SYMBOL-WS5000-MIB", "wlanAuthOK"),
        ("SYMBOL-WS5000-MIB", "wlanAuthFail"),
        ("SYMBOL-WS5000-MIB", "userAuthOK"),
        ("SYMBOL-WS5000-MIB", "radiusSrvTimeout"),
        ("SYMBOL-WS5000-MIB", "kdcPrincAdd"),
        ("SYMBOL-WS5000-MIB", "kdcPrincChgd"),
        ("SYMBOL-WS5000-MIB", "kdcPrincDel"),
        ("SYMBOL-WS5000-MIB", "kdcDBReplaced"),
        ("SYMBOL-WS5000-MIB", "hsbStdbyAutoRev"),
        ("SYMBOL-WS5000-MIB", "hsbPrimAutoRev"),
        ("SYMBOL-WS5000-MIB", "acsError"),
        ("SYMBOL-WS5000-MIB", "eopActive"),
        ("SYMBOL-WS5000-MIB", "eopInactive"),
        ("SYMBOL-WS5000-MIB", "debugEvent"))
)
if mibBuilder.loadTexts:
    v1dot2dot5NotificationGroup.setStatus(
        "current"
    )

v2dot0NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 2)
)
v2dot0NotificationGroup.setObjects(
      *(("SYMBOL-WS5000-MIB", "ccRapNewRogueAp"),
        ("SYMBOL-WS5000-MIB", "ccRapNewApprovedAp"),
        ("SYMBOL-WS5000-MIB", "ccTrapWVPNAlert"),
        ("SYMBOL-WS5000-MIB", "ccTrapWVPNInfo"),
        ("SYMBOL-WS5000-MIB", "ccTrapInfoRadiusAcctInfo"),
        ("SYMBOL-WS5000-MIB", "ccInfoRadiusServer"))
)
if mibBuilder.loadTexts:
    v2dot0NotificationGroup.setStatus(
        "current"
    )

v2dot1NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 6, 1000, 5)
)
v2dot1NotificationGroup.setObjects(
      *(("SYMBOL-WS5000-MIB", "tunnelUnknownProtocol"),
        ("SYMBOL-WS5000-MIB", "tunnelStatusChanged"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsSwitch"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsWlan"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsMu"),
        ("SYMBOL-WS5000-MIB", "sensorOffline"),
        ("SYMBOL-WS5000-MIB", "sensorFailure"),
        ("SYMBOL-WS5000-MIB", "sensorRevert"),
        ("SYMBOL-WS5000-MIB", "sensorConvert"),
        ("SYMBOL-WS5000-MIB", "configChangeUpdate"),
        ("SYMBOL-WS5000-MIB", "ccSumStatsAp"))
)
if mibBuilder.loadTexts:
    v2dot1NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

radiusAuthClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 6, 1, 5, 2, 2, 1, 1)
)
radiusAuthClientMIBCompliance.setObjects(
    ("SYMBOL-CC-WS5000-MIB", "radiusAuthClientMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAuthClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBOL-WS5000-MIB",
    **{"DoActionNow": DoActionNow,
       "MultiPointer63": MultiPointer63,
       "AbbrevRowStatus": AbbrevRowStatus,
       "PartsPer10k": PartsPer10k,
       "Password": Password,
       "HexPassword": HexPassword,
       "RadioType": RadioType,
       "StaticRowEnable": StaticRowEnable,
       "MultiPointer255": MultiPointer255,
       "SinglePointer": SinglePointer,
       "TransmitRate": TransmitRate,
       "DoActionShowProgress": DoActionShowProgress,
       "ScaleBy100": ScaleBy100,
       "SnmpOpers": SnmpOpers,
       "TruthValue": TruthValue,
       "FHAlgorithm": FHAlgorithm,
       "SnmpAdminString": SnmpAdminString,
       "APOnlineStatus": APOnlineStatus,
       "EncrType": EncrType,
       "MCValueOffset": MCValueOffset,
       "HsbState": HsbState,
       "MUDeviceType": MUDeviceType,
       "APStatus": APStatus,
       "MUSecurityStatus": MUSecurityStatus,
       "CurrentRate": CurrentRate,
       "SupportedRates": SupportedRates,
       "PSPowerMode": PSPowerMode,
       "AuthState": AuthState,
       "AuthMethod": AuthMethod,
       "StorageType": StorageType,
       "RowStatus": RowStatus,
       "TargetOptions": TargetOptions,
       "symbol": symbol,
       "symbolCC": symbolCC,
       "ws5000": ws5000,
       "ws5100": ws5100,
       "symbolCCSystem": symbolCCSystem,
       "ccSysCfg": ccSysCfg,
       "ccModuleName": ccModuleName,
       "ccModuleDesc": ccModuleDesc,
       "ccManufacture": ccManufacture,
       "ccCopyright": ccCopyright,
       "ccModuleVer": ccModuleVer,
       "ccMaxNumAP": ccMaxNumAP,
       "ccMaxNumMu": ccMaxNumMu,
       "ccActivePolicy": ccActivePolicy,
       "ccTaf": ccTaf,
       "ccSnmpOpers": ccSnmpOpers,
       "ccUptime": ccUptime,
       "ccFTP": ccFTP,
       "ccTelnet": ccTelnet,
       "ccWeb": ccWeb,
       "ccSNMPFlag": ccSNMPFlag,
       "ccTime": ccTime,
       "ccSNMPKdc": ccSNMPKdc,
       "ccCliKdc": ccCliKdc,
       "ccPolicyAddObj": ccPolicyAddObj,
       "ccPolicyRemObj": ccPolicyRemObj,
       "ccLicenseCount": ccLicenseCount,
       "ccEmergencyPolicy": ccEmergencyPolicy,
       "ccEmergencyMode": ccEmergencyMode,
       "ccRunACS": ccRunACS,
       "ccEnableSNMPTrap": ccEnableSNMPTrap,
       "ccEnableWVPNSupport": ccEnableWVPNSupport,
       "ccEnableRap": ccEnableRap,
       "ccAPTxPPS": ccAPTxPPS,
       "ccAPRxPPS": ccAPRxPPS,
       "ccAvgTxRetry": ccAvgTxRetry,
       "ccAvgRSSI": ccAvgRSSI,
       "ccAvgSNR": ccAvgSNR,
       "ccConfigChangeLast": ccConfigChangeLast,
       "ccNTP": ccNTP,
       "ccNtpPrefTimeServer": ccNtpPrefTimeServer,
       "ccNtpFirstAltTimeServer": ccNtpFirstAltTimeServer,
       "ccNtpSecondAltTimeServer": ccNtpSecondAltTimeServer,
       "ccNtpGroupSetTimeServer": ccNtpGroupSetTimeServer,
       "ccNtpDelAll": ccNtpDelAll,
       "ccPolicyTable": ccPolicyTable,
       "ccPolicyEntry": ccPolicyEntry,
       "ccPolicyIndex": ccPolicyIndex,
       "ccPolicyName": ccPolicyName,
       "ccPolicyDesc": ccPolicyDesc,
       "ccPolicyCountry": ccPolicyCountry,
       "ccPolicyDefAdoptAPPolicy": ccPolicyDefAdoptAPPolicy,
       "ccPolicyAPPolicyCount": ccPolicyAPPolicyCount,
       "ccPolicyAPNameOfPolicy": ccPolicyAPNameOfPolicy,
       "ccPolicyAddAPPolicy": ccPolicyAddAPPolicy,
       "ccPolicyRmvAPPolicy": ccPolicyRmvAPPolicy,
       "ccPolicyExcludeInfo": ccPolicyExcludeInfo,
       "ccPolicyExcludeEdit": ccPolicyExcludeEdit,
       "ccPolicyExcludeRmv": ccPolicyExcludeRmv,
       "ccPolicyIncludeInfo": ccPolicyIncludeInfo,
       "ccPolicyIncludeEdit": ccPolicyIncludeEdit,
       "ccPolicyIncludeRmv": ccPolicyIncludeRmv,
       "ccPolicyEtherPolicy": ccPolicyEtherPolicy,
       "ccPolicyTrap": ccPolicyTrap,
       "ccPolicyDefChannel": ccPolicyDefChannel,
       "ccPolicyDefPower": ccPolicyDefPower,
       "ccPolicyChannel11a": ccPolicyChannel11a,
       "ccPolicyPower11a": ccPolicyPower11a,
       "ccPolicyChannel11b": ccPolicyChannel11b,
       "ccPolicyPower11b": ccPolicyPower11b,
       "ccPolicyDSCoExistence": ccPolicyDSCoExistence,
       "ccPolicyDefAdoptAPPolicy11a": ccPolicyDefAdoptAPPolicy11a,
       "ccPolicyDefAdoptAPPolicy11b": ccPolicyDefAdoptAPPolicy11b,
       "ccPolicyDefAdoptAPPolicyFH": ccPolicyDefAdoptAPPolicyFH,
       "ccPolicyDefAdoptAPPolicy11g": ccPolicyDefAdoptAPPolicy11g,
       "ccPolicyChannel11g": ccPolicyChannel11g,
       "ccPolicyPower11g": ccPolicyPower11g,
       "ccCountryInfoTable": ccCountryInfoTable,
       "ccCountryInfoEntry": ccCountryInfoEntry,
       "ccCCIndex": ccCCIndex,
       "ccCCode": ccCCode,
       "ccFullName": ccFullName,
       "cc11aChannels": cc11aChannels,
       "cc11bChannels": cc11bChannels,
       "ccFHTableNum": ccFHTableNum,
       "ccFHChannels": ccFHChannels,
       "ccFHAlgorithm": ccFHAlgorithm,
       "ccFHContiguous": ccFHContiguous,
       "ccFHHopSequence": ccFHHopSequence,
       "cc11gChannels": cc11gChannels,
       "ccOnBoardKerberos": ccOnBoardKerberos,
       "kerbCfgKDC": kerbCfgKDC,
       "kdcType": kdcType,
       "masterHost": masterHost,
       "masterIPAddress": masterIPAddress,
       "createMsKdc": createMsKdc,
       "delMsKdc": delMsKdc,
       "createSlvKdc": createSlvKdc,
       "delSlvKdc": delSlvKdc,
       "kdcRealm": kdcRealm,
       "interfaceNumber": interfaceNumber,
       "addkdcMu": addkdcMu,
       "remkdcMu": remkdcMu,
       "kerbCfgSlave": kerbCfgSlave,
       "addSlave": addSlave,
       "delSlave": delSlave,
       "slaveCount": slaveCount,
       "slaveTable": slaveTable,
       "slaveEntry": slaveEntry,
       "hostName": hostName,
       "realM": realM,
       "ipAddress": ipAddress,
       "domainName": domainName,
       "slaveIndex": slaveIndex,
       "syncDB": syncDB,
       "kerbCfgNTP": kerbCfgNTP,
       "prefTimeServer": prefTimeServer,
       "firstAltTimeServer": firstAltTimeServer,
       "secondAltTimeServer": secondAltTimeServer,
       "groupSetTimeServer": groupSetTimeServer,
       "delAll": delAll,
       "delTimeServer": delTimeServer,
       "kerbKDCUsers": kerbKDCUsers,
       "kdcUserTable": kdcUserTable,
       "kdcUserEntry": kdcUserEntry,
       "kdcUserIndex": kdcUserIndex,
       "kdcUserName": kdcUserName,
       "kdcUserTlife": kdcUserTlife,
       "kdcWLANTable": kdcWLANTable,
       "kdcWLANEntry": kdcWLANEntry,
       "kdcWLANIndex": kdcWLANIndex,
       "kdcWLANName": kdcWLANName,
       "kdcWLANTlife": kdcWLANTlife,
       "radiusAuthentication": radiusAuthentication,
       "radiusAuthClientMIB": radiusAuthClientMIB,
       "radiusAuthClientMIBObjects": radiusAuthClientMIBObjects,
       "radiusAuthClient": radiusAuthClient,
       "radiusAuthClientInvalidServerAddresses": radiusAuthClientInvalidServerAddresses,
       "radiusAuthServerTable": radiusAuthServerTable,
       "radiusAuthServerEntry": radiusAuthServerEntry,
       "radiusAuthServerIndex": radiusAuthServerIndex,
       "radiusAuthServerAddress": radiusAuthServerAddress,
       "radiusAuthClientServerPortNumber": radiusAuthClientServerPortNumber,
       "radiusAuthClientRoundTripTime": radiusAuthClientRoundTripTime,
       "radiusAuthClientAccessRequests": radiusAuthClientAccessRequests,
       "radiusAuthClientAccessRetransmissions": radiusAuthClientAccessRetransmissions,
       "radiusAuthClientAccessAccepts": radiusAuthClientAccessAccepts,
       "radiusAuthClientAccessRejects": radiusAuthClientAccessRejects,
       "radiusAuthClientAccessChallenges": radiusAuthClientAccessChallenges,
       "radiusAuthClientMalformedAccessResponses": radiusAuthClientMalformedAccessResponses,
       "radiusAuthClientBadAuthenticators": radiusAuthClientBadAuthenticators,
       "radiusAuthClientPendingRequests": radiusAuthClientPendingRequests,
       "radiusAuthClientTimeouts": radiusAuthClientTimeouts,
       "radiusAuthClientUnknownTypes": radiusAuthClientUnknownTypes,
       "radiusAuthClientPacketsDropped": radiusAuthClientPacketsDropped,
       "radiusAuthClientIdentifier": radiusAuthClientIdentifier,
       "radiusAuthClientMIBConformance": radiusAuthClientMIBConformance,
       "radiusAuthClientMIBCompliances": radiusAuthClientMIBCompliances,
       "radiusAuthClientMIBCompliance": radiusAuthClientMIBCompliance,
       "radiusAuthClientMIBGroups": radiusAuthClientMIBGroups,
       "radiusAuthClientMIBGroup": radiusAuthClientMIBGroup,
       "ccEventsObjects": ccEventsObjects,
       "ccEventsAllLocalLog": ccEventsAllLocalLog,
       "ccEventsAllSNMPTrap": ccEventsAllSNMPTrap,
       "ccEventsAllSyslog": ccEventsAllSyslog,
       "ccEventsAllDefault": ccEventsAllDefault,
       "ccEventTable": ccEventTable,
       "ccEventEntry": ccEventEntry,
       "ccEventIndex": ccEventIndex,
       "ccEventDescr": ccEventDescr,
       "ccEventDefault": ccEventDefault,
       "ccEventSyslog": ccEventSyslog,
       "ccEventSNMPTrap": ccEventSNMPTrap,
       "ccEventLocalLog": ccEventLocalLog,
       "ccSyslogObjects": ccSyslogObjects,
       "ccSysLogStatus": ccSysLogStatus,
       "ccSyslogHosts": ccSyslogHosts,
       "ccSyslogAddHost": ccSyslogAddHost,
       "ccSyslogRemHost": ccSyslogRemHost,
       "ccSyslogHostsTable": ccSyslogHostsTable,
       "ccSyslogHostsEntry": ccSyslogHostsEntry,
       "ccSyslogHostIndex": ccSyslogHostIndex,
       "ccSyslogHostName": ccSyslogHostName,
       "ccSyslogHostIPAddr": ccSyslogHostIPAddr,
       "ccSyslogHostDomain": ccSyslogHostDomain,
       "ccSyslogHostSetSeverity": ccSyslogHostSetSeverity,
       "ccSyslogHostSeverityList": ccSyslogHostSeverityList,
       "ccSystemHosts": ccSystemHosts,
       "ccSystemAddHost": ccSystemAddHost,
       "ccSystemRemHost": ccSystemRemHost,
       "ccSystemHostsTable": ccSystemHostsTable,
       "ccSystemHostsEntry": ccSystemHostsEntry,
       "ccSystemHostIndex": ccSystemHostIndex,
       "ccSystemHostName": ccSystemHostName,
       "ccSystemHostIPAddr": ccSystemHostIPAddr,
       "ccSystemHostDomain": ccSystemHostDomain,
       "ccPolicyRCObjects": ccPolicyRCObjects,
       "ccPolicyRCAddRemTable": ccPolicyRCAddRemTable,
       "ccPolicyRCAddRemEntry": ccPolicyRCAddRemEntry,
       "ccPolicyRadioType": ccPolicyRadioType,
       "ccPolicyRCAdd": ccPolicyRCAdd,
       "ccPolicyRCRem": ccPolicyRCRem,
       "ccPolicyRCTable": ccPolicyRCTable,
       "ccPolicyRCEntry": ccPolicyRCEntry,
       "ccPolicyRcIndex": ccPolicyRcIndex,
       "ccPolicyRCChannelDescr": ccPolicyRCChannelDescr,
       "ccPolicyObject": ccPolicyObject,
       "ccPolicyAPPolicyTable": ccPolicyAPPolicyTable,
       "ccPolicyAPPolicyEntry": ccPolicyAPPolicyEntry,
       "ccPolicyAPPolicyIndex": ccPolicyAPPolicyIndex,
       "ccPolicyAPPolicyName": ccPolicyAPPolicyName,
       "symbolCCInterfaces": symbolCCInterfaces,
       "ccAPPolicyAddObj": ccAPPolicyAddObj,
       "ccAPPolicyRemObj": ccAPPolicyRemObj,
       "ccEPPAddObj": ccEPPAddObj,
       "ccEPPRemObj": ccEPPRemObj,
       "ccAccessPortAddObj": ccAccessPortAddObj,
       "ccAccessPortRemObj": ccAccessPortRemObj,
       "ccFWLanAddObj": ccFWLanAddObj,
       "ccFWLanRemObj": ccFWLanRemObj,
       "ccAPTable": ccAPTable,
       "ccAPEntry": ccAPEntry,
       "ccRadioIndex": ccRadioIndex,
       "ccRadioName": ccRadioName,
       "ccRadioDesc": ccRadioDesc,
       "ccRadioOnlineStatus": ccRadioOnlineStatus,
       "ccRadioMAC": ccRadioMAC,
       "ccDeviceMAC": ccDeviceMAC,
       "ccDeviceLocation": ccDeviceLocation,
       "ccRadioType": ccRadioType,
       "ccRadioChannel": ccRadioChannel,
       "ccRadioPower": ccRadioPower,
       "ccRadioPolicy": ccRadioPolicy,
       "ccDeviceNic": ccDeviceNic,
       "ccDeviceType": ccDeviceType,
       "ccRadioCCAmode": ccRadioCCAmode,
       "ccRadioCCAthresh": ccRadioCCAthresh,
       "ccRadioDiversity": ccRadioDiversity,
       "ccDeviceVlanid": ccDeviceVlanid,
       "ccDeviceVlanTagsSeen": ccDeviceVlanTagsSeen,
       "ccRadioUptime": ccRadioUptime,
       "ccRadioTxpps": ccRadioTxpps,
       "ccRadioMUs": ccRadioMUs,
       "ccRadioGatherStatistics": ccRadioGatherStatistics,
       "ccRadioReset": ccRadioReset,
       "ccDeviceClearSeenVlanTags": ccDeviceClearSeenVlanTags,
       "ccDeviceReset": ccDeviceReset,
       "ccRadioAuto": ccRadioAuto,
       "ccRadioMUPower": ccRadioMUPower,
       "ccRadioProtection": ccRadioProtection,
       "ccRadioShortSlot": ccRadioShortSlot,
       "ccRadioAntenna": ccRadioAntenna,
       "ccRadioCurrentChannel": ccRadioCurrentChannel,
       "ccRadioAllChannels": ccRadioAllChannels,
       "ccRadioPowerdBm": ccRadioPowerdBm,
       "ccRadioCurrentPower": ccRadioCurrentPower,
       "ccRadioAllPower": ccRadioAllPower,
       "ccRadioMUPowerdBm": ccRadioMUPowerdBm,
       "ccRadioAntCorrection": ccRadioAntCorrection,
       "ccRadioIndoor": ccRadioIndoor,
       "ccRadioDFS": ccRadioDFS,
       "ccRadioTPC": ccRadioTPC,
       "ccRadioRadarChannels": ccRadioRadarChannels,
       "ccDetectorAp": ccDetectorAp,
       "ccRadioMaxMUs": ccRadioMaxMUs,
       "ccSimulateRadar": ccSimulateRadar,
       "ccRadioUser802x": ccRadioUser802x,
       "ccAPPolicyTable": ccAPPolicyTable,
       "ccAPPolicyEntry": ccAPPolicyEntry,
       "ccAPPolicyIndex": ccAPPolicyIndex,
       "ccAPPolicyName": ccAPPolicyName,
       "ccAPPolicyDesc": ccAPPolicyDesc,
       "ccAPPolicyPreAmble": ccAPPolicyPreAmble,
       "ccAPPolicyBeaconInterval": ccAPPolicyBeaconInterval,
       "ccAPPolicyRTSThreshold": ccAPPolicyRTSThreshold,
       "ccAPPolicyDTIM": ccAPPolicyDTIM,
       "ccAPPolicyBasicRates11a": ccAPPolicyBasicRates11a,
       "ccAPPolicySupportedRates11a": ccAPPolicySupportedRates11a,
       "ccAPPolicyBasicRates11b": ccAPPolicyBasicRates11b,
       "ccAPPolicySupportedRates11b": ccAPPolicySupportedRates11b,
       "ccAPPolicyBasicRatesFH": ccAPPolicyBasicRatesFH,
       "ccAPPolicySupportedRatesFH": ccAPPolicySupportedRatesFH,
       "ccAPPolicyBasicRates11g": ccAPPolicyBasicRates11g,
       "ccAPPolicySupportedRates11g": ccAPPolicySupportedRates11g,
       "ccAPPolicyNonSpectrumMgmt": ccAPPolicyNonSpectrumMgmt,
       "ccAPPolicyAddAllWlan": ccAPPolicyAddAllWlan,
       "ccAPPolicyRemAllWlan": ccAPPolicyRemAllWlan,
       "ccAPPolicyWMEEnable": ccAPPolicyWMEEnable,
       "ccAPPolicyWMEProfile": ccAPPolicyWMEProfile,
       "ccAPPolicyDTIM2": ccAPPolicyDTIM2,
       "ccAPPolicyDTIM3": ccAPPolicyDTIM3,
       "ccAPPolicyDTIM4": ccAPPolicyDTIM4,
       "ccEPTable": ccEPTable,
       "ccEPEntry": ccEPEntry,
       "ccEPIndex": ccEPIndex,
       "ccEPNic": ccEPNic,
       "ccEPName": ccEPName,
       "ccEPDesc": ccEPDesc,
       "ccEPMacAddr": ccEPMacAddr,
       "ccEPEnable": ccEPEnable,
       "ccEPSpeed": ccEPSpeed,
       "ccEPEnableDHCP": ccEPEnableDHCP,
       "ccEPIPAddr": ccEPIPAddr,
       "ccEPNetMask": ccEPNetMask,
       "ccEPDnsCount": ccEPDnsCount,
       "ccEPDnsList": ccEPDnsList,
       "ccEPPrimaryVid": ccEPPrimaryVid,
       "ccEPOnline": ccEPOnline,
       "ccEPDisplayName": ccEPDisplayName,
       "ccEPUptime": ccEPUptime,
       "ccEPTx": ccEPTx,
       "ccEPRx": ccEPRx,
       "ccEPDomain": ccEPDomain,
       "ccEPGateway": ccEPGateway,
       "ccEPCFGMode": ccEPCFGMode,
       "ccEPDuplex": ccEPDuplex,
       "ccEPMode": ccEPMode,
       "ccEPDhcpPriVlan": ccEPDhcpPriVlan,
       "ccEPDDNSStatus": ccEPDDNSStatus,
       "ccEPDDNSttl": ccEPDDNSttl,
       "ccEPDDNSUpdateAll": ccEPDDNSUpdateAll,
       "ccEPDDNSMUserStatus": ccEPDDNSMUserStatus,
       "ccEPDDNSDomainName": ccEPDDNSDomainName,
       "ccEPPTable": ccEPPTable,
       "ccEPPEntry": ccEPPEntry,
       "ccEPPIndex": ccEPPIndex,
       "ccEPPName": ccEPPName,
       "ccEPPAlias": ccEPPAlias,
       "ccEPPDesc": ccEPPDesc,
       "ccEPPRonnic": ccEPPRonnic,
       "ccEPPVlanCount": ccEPPVlanCount,
       "ccEPPVlanList": ccEPPVlanList,
       "ccEPPCreateNewVlan": ccEPPCreateNewVlan,
       "ccEPPRemVlan": ccEPPRemVlan,
       "ccEPPDropVlan": ccEPPDropVlan,
       "ccdot11FHPhyTable": ccdot11FHPhyTable,
       "ccdot11FHPhyEntry": ccdot11FHPhyEntry,
       "ccdot11FHIndex": ccdot11FHIndex,
       "ccdot11FHHopTime": ccdot11FHHopTime,
       "ccdot11FHCurrentChannelNumber": ccdot11FHCurrentChannelNumber,
       "ccdot11FHMaxDwellTime": ccdot11FHMaxDwellTime,
       "ccdot11FHCurrentDwellTime": ccdot11FHCurrentDwellTime,
       "ccdot11FHCurrentSet": ccdot11FHCurrentSet,
       "ccdot11FHCurrentPattern": ccdot11FHCurrentPattern,
       "ccdot11FHCurrentIndex": ccdot11FHCurrentIndex,
       "ccAPPolicyObjects": ccAPPolicyObjects,
       "ccAPPolicyAddRemWLANTable": ccAPPolicyAddRemWLANTable,
       "ccAPPolicyAddRemWLANEntry": ccAPPolicyAddRemWLANEntry,
       "ccAPPolicyDeviceType": ccAPPolicyDeviceType,
       "ccAPPolicyAddWLAN": ccAPPolicyAddWLAN,
       "ccAPPolicyRemWLAN": ccAPPolicyRemWLAN,
       "ccAPPolicySelectWLAN": ccAPPolicySelectWLAN,
       "ccAPPolicyUnselectWLAN": ccAPPolicyUnselectWLAN,
       "ccAPPolicyWLANTable": ccAPPolicyWLANTable,
       "ccAPPolicyWLANEntry": ccAPPolicyWLANEntry,
       "ccAPPolicyWLANIndex": ccAPPolicyWLANIndex,
       "ccAPPolicyWLAN": ccAPPolicyWLAN,
       "ccAPPolicyWLANBW": ccAPPolicyWLANBW,
       "ccAPPolicyWLANNP": ccAPPolicyWLANNP,
       "ccAPPolicyWLANBSS": ccAPPolicyWLANBSS,
       "ccAPPolicyBSSTable": ccAPPolicyBSSTable,
       "ccAPPolicyBSSEntry": ccAPPolicyBSSEntry,
       "ccAPPolicyBSS": ccAPPolicyBSS,
       "ccAPPolicyPrimaryWLAN": ccAPPolicyPrimaryWLAN,
       "ccFWLANTable": ccFWLANTable,
       "ccFWLANEntry": ccFWLANEntry,
       "ccLANIndex": ccLANIndex,
       "ccLANName": ccLANName,
       "ccLANDesc": ccLANDesc,
       "ccLANNATCount": ccLANNATCount,
       "ccLANAddNAT": ccLANAddNAT,
       "ccLANRemNAT": ccLANRemNAT,
       "ccLANEp": ccLANEp,
       "ccLANNp": ccLANNp,
       "ccLANPfAllow": ccLANPfAllow,
       "ccLANPfDeny": ccLANPfDeny,
       "ccFWLANNATTable": ccFWLANNATTable,
       "ccFWLANNATEntry": ccFWLANNATEntry,
       "ccLANNATIndex": ccLANNATIndex,
       "ccLANNATRemoteRealIP": ccLANNATRemoteRealIP,
       "ccLANNATLocalNatIP": ccLANNATLocalNatIP,
       "ccRouteTable": ccRouteTable,
       "ccRouteEntry": ccRouteEntry,
       "ccRouteIndex": ccRouteIndex,
       "ccRouteDest": ccRouteDest,
       "ccRouteGateway": ccRouteGateway,
       "ccRouteFlags": ccRouteFlags,
       "ccRouteRefs": ccRouteRefs,
       "ccRouteUse": ccRouteUse,
       "ccRouteInterface": ccRouteInterface,
       "ccRouteGenMask": ccRouteGenMask,
       "ccRouteAddObj": ccRouteAddObj,
       "ccRouteRemObj": ccRouteRemObj,
       "ccRouteFlush": ccRouteFlush,
       "ccDhcpSrvNIC1": ccDhcpSrvNIC1,
       "ccDhcp1Srv": ccDhcp1Srv,
       "ccDhcp1Subnet": ccDhcp1Subnet,
       "ccDhcp1Netmask": ccDhcp1Netmask,
       "ccDhcp1BcastIP": ccDhcp1BcastIP,
       "ccDhcp1RouterIP": ccDhcp1RouterIP,
       "ccDhcp1PriDNSIP": ccDhcp1PriDNSIP,
       "ccDhcp1SecDNSIP": ccDhcp1SecDNSIP,
       "ccDhcp1DomainName": ccDhcp1DomainName,
       "ccDhcp1DefLease": ccDhcp1DefLease,
       "ccDhcp1MaxLease": ccDhcp1MaxLease,
       "ccDhcp1IPRangeTable": ccDhcp1IPRangeTable,
       "ccDhcp1IPRangeEntry": ccDhcp1IPRangeEntry,
       "ccDhcp1RangeIndex": ccDhcp1RangeIndex,
       "ccDhcp1RangeStartIP": ccDhcp1RangeStartIP,
       "ccDhcp1RangeEndIP": ccDhcp1RangeEndIP,
       "ccDhcp1AddIPRangeObj": ccDhcp1AddIPRangeObj,
       "ccDhcp1RemIPRangeObj": ccDhcp1RemIPRangeObj,
       "ccDhcp1StaticIPTable": ccDhcp1StaticIPTable,
       "ccDhcp1StaticIPEntry": ccDhcp1StaticIPEntry,
       "ccDhcp1StaticIPIndex": ccDhcp1StaticIPIndex,
       "ccDhcp1StaticIP": ccDhcp1StaticIP,
       "ccDhcp1StaticMac": ccDhcp1StaticMac,
       "ccDhcp1StaticHost": ccDhcp1StaticHost,
       "ccDhcp1AddStaticIPObj": ccDhcp1AddStaticIPObj,
       "ccDhcp1RemStaticIPObj": ccDhcp1RemStaticIPObj,
       "ccDhcp1OptionTable": ccDhcp1OptionTable,
       "ccDhcp1OptionEntry": ccDhcp1OptionEntry,
       "ccDhcp1OptionIndex": ccDhcp1OptionIndex,
       "ccDhcp1OptionName": ccDhcp1OptionName,
       "ccDhcp1OptionCode": ccDhcp1OptionCode,
       "ccDhcp1OptionType": ccDhcp1OptionType,
       "ccDhcp1OptionValue": ccDhcp1OptionValue,
       "ccDhcp1AddOptionObj": ccDhcp1AddOptionObj,
       "ccDhcp1RemOptionObj": ccDhcp1RemOptionObj,
       "ccDhcp1LeasesTable": ccDhcp1LeasesTable,
       "ccDhcp1LeasesEntry": ccDhcp1LeasesEntry,
       "ccDhcp1LeaseIndex": ccDhcp1LeaseIndex,
       "ccDhcp1LeaseIP": ccDhcp1LeaseIP,
       "ccDhcp1LeaseMac": ccDhcp1LeaseMac,
       "ccDhcp1LeaseStartTime": ccDhcp1LeaseStartTime,
       "ccDhcp1LeaseEndTime": ccDhcp1LeaseEndTime,
       "ccDhcp1RemLeaseObj": ccDhcp1RemLeaseObj,
       "ccDhcp1RemStaticHost": ccDhcp1RemStaticHost,
       "ccDhcpSrvNIC2": ccDhcpSrvNIC2,
       "ccDhcp2Srv": ccDhcp2Srv,
       "ccDhcp2Subnet": ccDhcp2Subnet,
       "ccDhcp2Netmask": ccDhcp2Netmask,
       "ccDhcp2BcastIP": ccDhcp2BcastIP,
       "ccDhcp2RouterIP": ccDhcp2RouterIP,
       "ccDhcp2PriDNSIP": ccDhcp2PriDNSIP,
       "ccDhcp2SecDNSIP": ccDhcp2SecDNSIP,
       "ccDhcp2DomainName": ccDhcp2DomainName,
       "ccDhcp2DefLease": ccDhcp2DefLease,
       "ccDhcp2MaxLease": ccDhcp2MaxLease,
       "ccDhcp2IPRangeTable": ccDhcp2IPRangeTable,
       "ccDhcp2IPRangeEntry": ccDhcp2IPRangeEntry,
       "ccDhcp2RangeIndex": ccDhcp2RangeIndex,
       "ccDhcp2RangeStartIP": ccDhcp2RangeStartIP,
       "ccDhcp2RangeEndIP": ccDhcp2RangeEndIP,
       "ccDhcp2AddIPRangeObj": ccDhcp2AddIPRangeObj,
       "ccDhcp2RemIPRangeObj": ccDhcp2RemIPRangeObj,
       "ccDhcp2StaticIPTable": ccDhcp2StaticIPTable,
       "ccDhcp2StaticIPEntry": ccDhcp2StaticIPEntry,
       "ccDhcp2StaticIPIndex": ccDhcp2StaticIPIndex,
       "ccDhcp2StaticIP": ccDhcp2StaticIP,
       "ccDhcp2StaticMac": ccDhcp2StaticMac,
       "ccDhcp2StaticHost": ccDhcp2StaticHost,
       "ccDhcp2AddStaticIPObj": ccDhcp2AddStaticIPObj,
       "ccDhcp2RemStaticIPObj": ccDhcp2RemStaticIPObj,
       "ccDhcp2OptionTable": ccDhcp2OptionTable,
       "ccDhcp2OptionEntry": ccDhcp2OptionEntry,
       "ccDhcp2OptionIndex": ccDhcp2OptionIndex,
       "ccDhcp2OptionName": ccDhcp2OptionName,
       "ccDhcp2OptionCode": ccDhcp2OptionCode,
       "ccDhcp2OptionType": ccDhcp2OptionType,
       "ccDhcp2OptionValue": ccDhcp2OptionValue,
       "ccDhcp2AddOptionObj": ccDhcp2AddOptionObj,
       "ccDhcp2RemOptionObj": ccDhcp2RemOptionObj,
       "ccDhcp2LeasesTable": ccDhcp2LeasesTable,
       "ccDhcp2LeasesEntry": ccDhcp2LeasesEntry,
       "ccDhcp2LeaseIndex": ccDhcp2LeaseIndex,
       "ccDhcp2LeaseIP": ccDhcp2LeaseIP,
       "ccDhcp2LeaseMac": ccDhcp2LeaseMac,
       "ccDhcp2LeaseStartTime": ccDhcp2LeaseStartTime,
       "ccDhcp2LeaseEndTime": ccDhcp2LeaseEndTime,
       "ccDhcp2RemLeaseObj": ccDhcp2RemLeaseObj,
       "ccDhcp2RemStaticHost": ccDhcp2RemStaticHost,
       "symbolCCMgmt": symbolCCMgmt,
       "ccWLANAddObj": ccWLANAddObj,
       "ccWLANRemObj": ccWLANRemObj,
       "ccUserAddObj": ccUserAddObj,
       "ccUserRemObj": ccUserRemObj,
       "ccGraphAddObj": ccGraphAddObj,
       "ccGraphRemObj": ccGraphRemObj,
       "ccSecAddObj": ccSecAddObj,
       "ccSecRemObj": ccSecRemObj,
       "ccACLAddObj": ccACLAddObj,
       "ccACLRemObj": ccACLRemObj,
       "ccUserTable": ccUserTable,
       "ccUserEntry": ccUserEntry,
       "ccUserID": ccUserID,
       "ccUserFullName": ccUserFullName,
       "ccUserPwd": ccUserPwd,
       "ccUserAdminRight": ccUserAdminRight,
       "ccUserProfileMgmtRight": ccUserProfileMgmtRight,
       "ccUserSysAdminRight": ccUserSysAdminRight,
       "ccUserSNMPAdminRight": ccUserSNMPAdminRight,
       "ccUserSecurityAdminRight": ccUserSecurityAdminRight,
       "ccUserIndex": ccUserIndex,
       "ccWLANTable": ccWLANTable,
       "ccWLANEntry": ccWLANEntry,
       "ccWLANIndex": ccWLANIndex,
       "ccWLANName": ccWLANName,
       "ccESSID": ccESSID,
       "ccSecurity": ccSecurity,
       "ccACLEnabled": ccACLEnabled,
       "ccMaxMus": ccMaxMus,
       "ccKerberosAuthName": ccKerberosAuthName,
       "ccKerberosAuthPass": ccKerberosAuthPass,
       "ccWLANACL": ccWLANACL,
       "ccWLANIsAuthenticated": ccWLANIsAuthenticated,
       "ccWLANMUTraffic": ccWLANMUTraffic,
       "ccWLANSecuredBeacon": ccWLANSecuredBeacon,
       "ccWLANCurrentMU": ccWLANCurrentMU,
       "ccWLANNetMask": ccWLANNetMask,
       "ccWLANDefaultRoute": ccWLANDefaultRoute,
       "ccWLANBCMC11A": ccWLANBCMC11A,
       "ccWLANBCMC11B": ccWLANBCMC11B,
       "ccWLANBCMCFH": ccWLANBCMCFH,
       "ccBroadcastEss": ccBroadcastEss,
       "ccWLANDesc": ccWLANDesc,
       "ccWlanWMEEnable": ccWlanWMEEnable,
       "ccWlanWMEProfile": ccWlanWMEProfile,
       "ccKnownCCTable": ccKnownCCTable,
       "ccKnownCCEntry": ccKnownCCEntry,
       "ccKnownCCIndex": ccKnownCCIndex,
       "ccKnownCCName": ccKnownCCName,
       "ccKnownCCMac": ccKnownCCMac,
       "ccKnownAPTable": ccKnownAPTable,
       "ccKnownAPEntry": ccKnownAPEntry,
       "ccKnownAPIndex": ccKnownAPIndex,
       "ccKnownAPMac": ccKnownAPMac,
       "ccKnownAPVer": ccKnownAPVer,
       "ccKnownAPIP": ccKnownAPIP,
       "ccKnownAPPriority": ccKnownAPPriority,
       "ccKnownAPMus": ccKnownAPMus,
       "ccKnownAPType": ccKnownAPType,
       "ccKnownAPAPVer": ccKnownAPAPVer,
       "ccKnownAPEssid": ccKnownAPEssid,
       "ccGraphTable": ccGraphTable,
       "ccGraphEntry": ccGraphEntry,
       "ccGraphIndex": ccGraphIndex,
       "ccGraphName": ccGraphName,
       "ccGraphWlanId": ccGraphWlanId,
       "ccVLANTable": ccVLANTable,
       "ccVLANEntry": ccVLANEntry,
       "ccVLANIndex": ccVLANIndex,
       "ccVLANName": ccVLANName,
       "ccVLANDesc": ccVLANDesc,
       "ccVLANVid": ccVLANVid,
       "ccVLANPriority": ccVLANPriority,
       "ccVLANPorts": ccVLANPorts,
       "ccVLANEtherPolicy": ccVLANEtherPolicy,
       "ccVLANWlan": ccVLANWlan,
       "ccVLANWlanList": ccVLANWlanList,
       "ccVLANAddWlan": ccVLANAddWlan,
       "ccVLANRemWlan": ccVLANRemWlan,
       "ccSecurityTable": ccSecurityTable,
       "ccSecurityEntry": ccSecurityEntry,
       "ccSecIndex": ccSecIndex,
       "ccSecName": ccSecName,
       "ccSecDesc": ccSecDesc,
       "ccSecBeaconEssid": ccSecBeaconEssid,
       "ccSecPreSharedAuthEnabled": ccSecPreSharedAuthEnabled,
       "ccSecWEPEnabled": ccSecWEPEnabled,
       "ccSecWEPKeyBitSize": ccSecWEPKeyBitSize,
       "ccSecWEPKey": ccSecWEPKey,
       "ccSecWEPKeyUse": ccSecWEPKeyUse,
       "ccSecKerberosEnabled": ccSecKerberosEnabled,
       "ccSecKerberosRealm": ccSecKerberosRealm,
       "ccSecKerberosServer1": ccSecKerberosServer1,
       "ccSecKerberosServer2": ccSecKerberosServer2,
       "ccSecKerberosServer3": ccSecKerberosServer3,
       "ccSecKerberosPort1": ccSecKerberosPort1,
       "ccSecKerberosPort2": ccSecKerberosPort2,
       "ccSecKerberosPort3": ccSecKerberosPort3,
       "ccSecRadiusServer1": ccSecRadiusServer1,
       "ccSecRadiusPort1": ccSecRadiusPort1,
       "ccSecRadiusSecret1": ccSecRadiusSecret1,
       "ccSecRadiusServer2": ccSecRadiusServer2,
       "ccSecRadiusPort2": ccSecRadiusPort2,
       "ccSecRadiusSecret2": ccSecRadiusSecret2,
       "ccSecRadiusHostname": ccSecRadiusHostname,
       "ccSecEapEnabled": ccSecEapEnabled,
       "ccSecEapQuietPeriod": ccSecEapQuietPeriod,
       "ccSecEapTxPeriod": ccSecEapTxPeriod,
       "ccSecEapReauth": ccSecEapReauth,
       "ccSecEapReauthPeriod": ccSecEapReauthPeriod,
       "ccSecEapReauthMaxRetries": ccSecEapReauthMaxRetries,
       "ccSecEapSupplTimeout": ccSecEapSupplTimeout,
       "ccSecEapMaxreqRetries": ccSecEapMaxreqRetries,
       "ccSecGroupRekeyPeriod": ccSecGroupRekeyPeriod,
       "ccSecPreSharedKeyMaterial": ccSecPreSharedKeyMaterial,
       "ccSecOpenEncryptEnabled": ccSecOpenEncryptEnabled,
       "ccSecKeyGuardEnabled": ccSecKeyGuardEnabled,
       "ccSecTKIPEnabled": ccSecTKIPEnabled,
       "ccSecBCMCEncrType": ccSecBCMCEncrType,
       "ccSecCheckValidity": ccSecCheckValidity,
       "ccSecCCMPEnabled": ccSecCCMPEnabled,
       "ccSecPreAuthentication": ccSecPreAuthentication,
       "ccSecPMKCaching": ccSecPMKCaching,
       "ccSecVPNEnabled": ccSecVPNEnabled,
       "ccACLTable": ccACLTable,
       "ccACLEntry": ccACLEntry,
       "ccACLIndex": ccACLIndex,
       "ccACLName": ccACLName,
       "ccACLDefaultAction": ccACLDefaultAction,
       "ccACLAction": ccACLAction,
       "ccACLGetItemCount": ccACLGetItemCount,
       "ccACLGetItem": ccACLGetItem,
       "ccACLAddItem": ccACLAddItem,
       "ccACLRemItem": ccACLRemItem,
       "ccNPolicyMgmt": ccNPolicyMgmt,
       "ccNumNPRec": ccNumNPRec,
       "ccNumPORec": ccNumPORec,
       "ccNumCGRec": ccNumCGRec,
       "ccNumCFRec": ccNumCFRec,
       "ccCFAddObj": ccCFAddObj,
       "ccCFRemObj": ccCFRemObj,
       "ccCGAddObj": ccCGAddObj,
       "ccCGRemObj": ccCGRemObj,
       "ccPOAddObj": ccPOAddObj,
       "ccPORemObj": ccPORemObj,
       "ccNPAddObj": ccNPAddObj,
       "ccNPRemObj": ccNPRemObj,
       "ccNPTable": ccNPTable,
       "ccNPEntry": ccNPEntry,
       "ccNPIndex": ccNPIndex,
       "ccNPName": ccNPName,
       "ccNPDesc": ccNPDesc,
       "ccNPInName": ccNPInName,
       "ccNPOutName": ccNPOutName,
       "ccPOTable": ccPOTable,
       "ccPOEntry": ccPOEntry,
       "ccPOIndex": ccPOIndex,
       "ccPOName": ccPOName,
       "ccPODesc": ccPODesc,
       "ccPOCgCount": ccPOCgCount,
       "ccPOAddCg": ccPOAddCg,
       "ccPORemCg": ccPORemCg,
       "ccPOType": ccPOType,
       "ccPOPacketModifier": ccPOPacketModifier,
       "ccCGTable": ccCGTable,
       "ccCGEntry": ccCGEntry,
       "ccCGIndex": ccCGIndex,
       "ccCGName": ccCGName,
       "ccCGDesc": ccCGDesc,
       "ccCGCfCount": ccCGCfCount,
       "ccCGAddCf": ccCGAddCf,
       "ccCGRemCf": ccCGRemCf,
       "ccCFTable": ccCFTable,
       "ccCFEntry": ccCFEntry,
       "ccCFIndex": ccCFIndex,
       "ccCFName": ccCFName,
       "ccCFDesc": ccCFDesc,
       "ccCFMcCount": ccCFMcCount,
       "ccCFAddMc": ccCFAddMc,
       "ccCFRemMc": ccCFRemMc,
       "ccPOObjects": ccPOObjects,
       "ccPOCGTable": ccPOCGTable,
       "ccPOCGEntry": ccPOCGEntry,
       "ccPOCGIndex": ccPOCGIndex,
       "ccPOCGName": ccPOCGName,
       "ccPOCGNewIP": ccPOCGNewIP,
       "ccPOCGVlanPriority": ccPOCGVlanPriority,
       "ccPOCGTos": ccPOCGTos,
       "ccPOCGBw": ccPOCGBw,
       "ccPOCGTxProfile": ccPOCGTxProfile,
       "ccPOCGPacketModifier": ccPOCGPacketModifier,
       "ccCGObjects": ccCGObjects,
       "ccCGCFTable": ccCGCFTable,
       "ccCGCFEntry": ccCGCFEntry,
       "ccCGCFIndex": ccCGCFIndex,
       "ccCGCFAction": ccCGCFAction,
       "ccCGCFName": ccCGCFName,
       "ccCFObjects": ccCFObjects,
       "ccCFMcTable": ccCFMcTable,
       "ccCFMcEntry": ccCFMcEntry,
       "ccCFMCIndex": ccCFMCIndex,
       "ccCFMCOffset": ccCFMCOffset,
       "ccCFMCValueCount": ccCFMCValueCount,
       "ccCFAddMCValue": ccCFAddMCValue,
       "ccCFRemMCValue": ccCFRemMCValue,
       "ccCFMcValTable": ccCFMcValTable,
       "ccCFMcValEntry": ccCFMcValEntry,
       "ccCFMcValIndex": ccCFMcValIndex,
       "ccCFMCValue": ccCFMCValue,
       "ccHSBConfigure": ccHSBConfigure,
       "ccHsbEnabled": ccHsbEnabled,
       "ccHsbMode": ccHsbMode,
       "ccHsbMacAddress1": ccHsbMacAddress1,
       "ccHsbMacAddress2": ccHsbMacAddress2,
       "ccHsbHeartbeatEnabledOnInterface1": ccHsbHeartbeatEnabledOnInterface1,
       "ccHsbHeartbeatEnabledOnInterface2": ccHsbHeartbeatEnabledOnInterface2,
       "ccHsbConnectivityFlag": ccHsbConnectivityFlag,
       "ccHsbFailoverState": ccHsbFailoverState,
       "ccHsbFailoverReason": ccHsbFailoverReason,
       "ccHsbResetCode": ccHsbResetCode,
       "ccHsbRevert": ccHsbRevert,
       "ccHsbautorevert": ccHsbautorevert,
       "ccHsbautorevertdelay": ccHsbautorevertdelay,
       "ccMUInfoTable": ccMUInfoTable,
       "ccMUInfoEntry": ccMUInfoEntry,
       "ccMUInfoIndex": ccMUInfoIndex,
       "ccMUInfoType": ccMUInfoType,
       "ccMUInfoMac": ccMUInfoMac,
       "ccMUInfoIP": ccMUInfoIP,
       "ccMUInfoWlan": ccMUInfoWlan,
       "ccMUInfoEssid": ccMUInfoEssid,
       "ccMUInfoAP": ccMUInfoAP,
       "ccMUInfoAPState": ccMUInfoAPState,
       "ccMUInfoSecState": ccMUInfoSecState,
       "ccMUInfoCurRate": ccMUInfoCurRate,
       "ccMUInfoSupRates": ccMUInfoSupRates,
       "ccMUInfoRssi": ccMUInfoRssi,
       "ccMUInfoPsp": ccMUInfoPsp,
       "ccMUInfoIntf": ccMUInfoIntf,
       "ccMUInfoAsscUptime": ccMUInfoAsscUptime,
       "ccMUInfoTktExp": ccMUInfoTktExp,
       "ccMUInfoUserName": ccMUInfoUserName,
       "ccMUInfoPktTx": ccMUInfoPktTx,
       "ccMUInfoPktRx": ccMUInfoPktRx,
       "ccMUInfoBytesTx": ccMUInfoBytesTx,
       "ccMUInfoBytesRx": ccMUInfoBytesRx,
       "ccMUInfoLastAct": ccMUInfoLastAct,
       "ccMUInfoVlan": ccMUInfoVlan,
       "ccMUInfoAuthState": ccMUInfoAuthState,
       "ccMUInfoAuthMethod": ccMUInfoAuthMethod,
       "ccMUInfoEncrMethod": ccMUInfoEncrMethod,
       "ccMUInfoBCMCEncrType": ccMUInfoBCMCEncrType,
       "ccMUInfoRoamCount": ccMUInfoRoamCount,
       "ccACLObjects": ccACLObjects,
       "ccACLItemsTable": ccACLItemsTable,
       "ccACLItemsEntry": ccACLItemsEntry,
       "ccACLItemIndex": ccACLItemIndex,
       "ccACLItem": ccACLItem,
       "ccWVPNConfigure": ccWVPNConfigure,
       "wvpnGeneralSettings": wvpnGeneralSettings,
       "wvpnServerEnable": wvpnServerEnable,
       "wvpnServerDisable": wvpnServerDisable,
       "wvpnServerRestart": wvpnServerRestart,
       "wvpnIpAddress": wvpnIpAddress,
       "wvpnPort": wvpnPort,
       "wvpnUnusedTimeout": wvpnUnusedTimeout,
       "wvpnStatus": wvpnStatus,
       "dosEnable": dosEnable,
       "dosPort": dosPort,
       "clientKeepAlive": clientKeepAlive,
       "vpnLicenseMax": vpnLicenseMax,
       "vpnLicenseInUse": vpnLicenseInUse,
       "wvpnWtlsSettings": wvpnWtlsSettings,
       "maxClientRsaKeySize": maxClientRsaKeySize,
       "minClientRsaKeySize": minClientRsaKeySize,
       "maxRsaKeySize": maxRsaKeySize,
       "minRsaKeySize": minRsaKeySize,
       "cipher": cipher,
       "mac": mac,
       "requireClientCertificate": requireClientCertificate,
       "keyRefresh": keyRefresh,
       "wantedFipsMode": wantedFipsMode,
       "securityMode": securityMode,
       "serverNumber": serverNumber,
       "handshakeTimeout": handshakeTimeout,
       "allowSessionResume": allowSessionResume,
       "wvpnAuthServerSettings": wvpnAuthServerSettings,
       "useSimpleAuthentication": useSimpleAuthentication,
       "useRadiusAuthentication": useRadiusAuthentication,
       "useLdapAuthentication": useLdapAuthentication,
       "useLocalDatabaseAuthentication": useLocalDatabaseAuthentication,
       "simpleAuthentication": simpleAuthentication,
       "simpleAuthUserName": simpleAuthUserName,
       "simpleAuthPassword": simpleAuthPassword,
       "simpleAuthDomain": simpleAuthDomain,
       "wvpnRadiusAuthentication": wvpnRadiusAuthentication,
       "radiusAuthPrimaryServer": radiusAuthPrimaryServer,
       "radiusAuthPrimaryHost": radiusAuthPrimaryHost,
       "radiusAuthPrimaryPort": radiusAuthPrimaryPort,
       "radiusAuthPrimaryMaxRetries": radiusAuthPrimaryMaxRetries,
       "radiusAuthPrimaryTimeOut": radiusAuthPrimaryTimeOut,
       "radiusAuthPrimaryUserPassword": radiusAuthPrimaryUserPassword,
       "radiusAuthPrimarySecret": radiusAuthPrimarySecret,
       "radiusAuthSecondaryServer": radiusAuthSecondaryServer,
       "radiusAuthSecondaryHost": radiusAuthSecondaryHost,
       "radiusAuthSecondaryPort": radiusAuthSecondaryPort,
       "radiusAuthSecondaryMaxRetries": radiusAuthSecondaryMaxRetries,
       "radiusAuthSecondaryTimeOut": radiusAuthSecondaryTimeOut,
       "radiusAuthSecondaryUserPassword": radiusAuthSecondaryUserPassword,
       "radiusAuthSecondarySecret": radiusAuthSecondarySecret,
       "wvpnIpPoolsSettings": wvpnIpPoolsSettings,
       "wvpnAddIpPoolObj": wvpnAddIpPoolObj,
       "wvpnRemIpPoolObj": wvpnRemIpPoolObj,
       "wvpnAddIpPoolRange": wvpnAddIpPoolRange,
       "wvpnRemIpPoolRange": wvpnRemIpPoolRange,
       "useDhcpGateway": useDhcpGateway,
       "wvpnIpPoolsTable": wvpnIpPoolsTable,
       "wvpnIpPoolsEntry": wvpnIpPoolsEntry,
       "wvpnIpPoolIndex": wvpnIpPoolIndex,
       "clientIpPoolName": clientIpPoolName,
       "clientNetMask": clientNetMask,
       "clientDhcpServerAddress": clientDhcpServerAddress,
       "clientDefaultGatewayAddress": clientDefaultGatewayAddress,
       "clientDnsAddress": clientDnsAddress,
       "clientWinsAddress": clientWinsAddress,
       "clientDomainName": clientDomainName,
       "clientNetBiosNodeType": clientNetBiosNodeType,
       "clientDhcpLeaseTime": clientDhcpLeaseTime,
       "reuseAddrTime": reuseAddrTime,
       "ipRangeCount": ipRangeCount,
       "clientIpRanges": clientIpRanges,
       "wvpnIpPoolsCount": wvpnIpPoolsCount,
       "wvpnIpPoolsNames": wvpnIpPoolsNames,
       "wvpnCertificateSettings": wvpnCertificateSettings,
       "wvpnServerCertificateTable": wvpnServerCertificateTable,
       "wvpnServerCertificateEntry": wvpnServerCertificateEntry,
       "wvpnCertIndex": wvpnCertIndex,
       "userName": userName,
       "serialNumber": serialNumber,
       "subject": subject,
       "version": version,
       "issuer": issuer,
       "keyLength": keyLength,
       "validFrom": validFrom,
       "validTo": validTo,
       "certificate": certificate,
       "binary": binary,
       "fingerPrint": fingerPrint,
       "authFingerPrint": authFingerPrint,
       "serverCertCount": serverCertCount,
       "serverCertUserNames": serverCertUserNames,
       "wvpnCaCertificateTable": wvpnCaCertificateTable,
       "wvpnCaCertificateEntry": wvpnCaCertificateEntry,
       "wvpnCaCertIndex": wvpnCaCertIndex,
       "wvpnCaSerialNumber": wvpnCaSerialNumber,
       "wvpnCaSubject": wvpnCaSubject,
       "wvpnCaVersion": wvpnCaVersion,
       "wvpnCaIssuer": wvpnCaIssuer,
       "wvpnCaKeyLength": wvpnCaKeyLength,
       "wvpnCaValidFrom": wvpnCaValidFrom,
       "wvpnCaValidTo": wvpnCaValidTo,
       "wvpnCaBinary": wvpnCaBinary,
       "wvpnCaFingerPrint": wvpnCaFingerPrint,
       "wvpnCaAuthFingerPrint": wvpnCaAuthFingerPrint,
       "caCertCount": caCertCount,
       "certSerialNumbers": certSerialNumbers,
       "importServerCert": importServerCert,
       "removeServerCert": removeServerCert,
       "importCaCert": importCaCert,
       "removeCaCert": removeCaCert,
       "importTftpServerCert": importTftpServerCert,
       "importTftpCaCert": importTftpCaCert,
       "dirCert": dirCert,
       "dumpCert": dumpCert,
       "wvpnDDNSSettings": wvpnDDNSSettings,
       "clearClientDNS": clearClientDNS,
       "updateClientDNS": updateClientDNS,
       "addDNSAddr": addDNSAddr,
       "deleteDNSAddr": deleteDNSAddr,
       "enable": enable,
       "ttl": ttl,
       "forwardZone": forwardZone,
       "reverseZone": reverseZone,
       "clientNameString": clientNameString,
       "wvpnDDNSAddressTable": wvpnDDNSAddressTable,
       "wvpnDDNSAddressEntry": wvpnDDNSAddressEntry,
       "wvpnDDNSAddressIndex": wvpnDDNSAddressIndex,
       "wvpnDDNSipAddress": wvpnDDNSipAddress,
       "cleanupTimeout": cleanupTimeout,
       "reverseZoneList": reverseZoneList,
       "reverseZoneAdd": reverseZoneAdd,
       "reverseZoneDel": reverseZoneDel,
       "wvpnRuntimeStats": wvpnRuntimeStats,
       "wvpnSessionTable": wvpnSessionTable,
       "wvpnSessionEntry": wvpnSessionEntry,
       "wvpnSessionIndex": wvpnSessionIndex,
       "wvpnSessionId": wvpnSessionId,
       "wvpnVpnIp": wvpnVpnIp,
       "wvpnRealIp": wvpnRealIp,
       "wvpnLoginTime": wvpnLoginTime,
       "wvpnRoamTime": wvpnRoamTime,
       "wvpnLastActive": wvpnLastActive,
       "wvpnPoolName": wvpnPoolName,
       "wvpnMacAddr": wvpnMacAddr,
       "wvpnSessionCount": wvpnSessionCount,
       "wvpnRefreshSession": wvpnRefreshSession,
       "wvpnKillSession": wvpnKillSession,
       "symbolCCPerformance": symbolCCPerformance,
       "symbolCCFault": symbolCCFault,
       "ccTargetObjects": ccTargetObjects,
       "ccTargetTrapString": ccTargetTrapString,
       "ccTargetAddrTable": ccTargetAddrTable,
       "ccTargetAddrEntry": ccTargetAddrEntry,
       "ccTargetAddrName": ccTargetAddrName,
       "ccTargetAddrSecName": ccTargetAddrSecName,
       "ccTargetAddrHost": ccTargetAddrHost,
       "ccTargetAddrCommunity": ccTargetAddrCommunity,
       "ccTargetAddrPort": ccTargetAddrPort,
       "ccTargetAddrStorageType": ccTargetAddrStorageType,
       "ccTargetAddrRowStatus": ccTargetAddrRowStatus,
       "ccTargetAddrOption": ccTargetAddrOption,
       "ccTrapInfos": ccTrapInfos,
       "ccTrapInfoEnableTrap": ccTrapInfoEnableTrap,
       "ccTrapInfoMaxNumSendOneTrap": ccTrapInfoMaxNumSendOneTrap,
       "ccTrapInfoInterval": ccTrapInfoInterval,
       "ccTrapInfoAclViolation": ccTrapInfoAclViolation,
       "ccTrapInfoDenyAdoption": ccTrapInfoDenyAdoption,
       "ccTrapInfoAPMUMaxExceed": ccTrapInfoAPMUMaxExceed,
       "ccTrapInfoWLANMUMaxExceed": ccTrapInfoWLANMUMaxExceed,
       "ccTrapInfoApDetected": ccTrapInfoApDetected,
       "ccTrapInfoApAdopted": ccTrapInfoApAdopted,
       "ccTrapInfoApReset": ccTrapInfoApReset,
       "ccTrapInfoApUnavailable": ccTrapInfoApUnavailable,
       "ccTrapInfoKDCUserAuthFail": ccTrapInfoKDCUserAuthFail,
       "ccTrapInfoRadiusAuthFail": ccTrapInfoRadiusAuthFail,
       "ccTrapInfoLowFlashSpace": ccTrapInfoLowFlashSpace,
       "ccTrapInfoNicDropping": ccTrapInfoNicDropping,
       "ccTrapInfoApAlert": ccTrapInfoApAlert,
       "ccTrapInfoUserAuthFail": ccTrapInfoUserAuthFail,
       "ccTrapInfoHsbPrimaryNoHeartbeat": ccTrapInfoHsbPrimaryNoHeartbeat,
       "ccTrapInfoHsbStandbyEntersFailover": ccTrapInfoHsbStandbyEntersFailover,
       "ccTrapInfoPrimaryFailedResetting": ccTrapInfoPrimaryFailedResetting,
       "ccTrapInfoKDCPropagationFail": ccTrapInfoKDCPropagationFail,
       "ccTrapInfoHighDecryptFail": ccTrapInfoHighDecryptFail,
       "ccTrapInfoHighReplyFail": ccTrapInfoHighReplyFail,
       "ccTrapInfoTKIPMICFail": ccTrapInfoTKIPMICFail,
       "ccTrapInfoWPACounterMeasureStart": ccTrapInfoWPACounterMeasureStart,
       "licenseChangedControl": licenseChangedControl,
       "clockChangedControl": clockChangedControl,
       "pktDiscWrongNICControl": pktDiscWrongNICControl,
       "pktDiscWrongVLANControl": pktDiscWrongVLANControl,
       "apAdoptFailPolControl": apAdoptFailPolControl,
       "apAdoptFailACLControl": apAdoptFailACLControl,
       "apAdoptFailLimitControl": apAdoptFailLimitControl,
       "apAdoptFailLicControl": apAdoptFailLicControl,
       "apAdoptFailNoImgControl": apAdoptFailNoImgControl,
       "apCfgFailESSControl": apCfgFailESSControl,
       "devDropInfoMsgControl": devDropInfoMsgControl,
       "devdropLoadmeMsgControl": devdropLoadmeMsgControl,
       "etherConnectControl": etherConnectControl,
       "muAssocFailControl": muAssocFailControl,
       "muAssocOKControl": muAssocOKControl,
       "muRoamedControl": muRoamedControl,
       "muDisassocControl": muDisassocControl,
       "muEAPAuthFailControl": muEAPAuthFailControl,
       "muEAPAuthOKControl": muEAPAuthOKControl,
       "muKDCAuthOKControl": muKDCAuthOKControl,
       "wlanAuthOKControl": wlanAuthOKControl,
       "wlanAuthFailControl": wlanAuthFailControl,
       "userAuthOKControl": userAuthOKControl,
       "radiusSrvTimeoutControl": radiusSrvTimeoutControl,
       "kdcPrincAddControl": kdcPrincAddControl,
       "kdcPrincChgdControl": kdcPrincChgdControl,
       "kdcPrincDelControl": kdcPrincDelControl,
       "kdcDBReplacedControl": kdcDBReplacedControl,
       "hsbStdbyAutoRevControl": hsbStdbyAutoRevControl,
       "hsbPrimAutoRevControl": hsbPrimAutoRevControl,
       "acsErrorControl": acsErrorControl,
       "eopActiveControl": eopActiveControl,
       "eopInactiveControl": eopInactiveControl,
       "debugEventControl": debugEventControl,
       "hsbStartUpControl": hsbStartUpControl,
       "hsbPeerConnectControl": hsbPeerConnectControl,
       "ccFanAndTempControl": ccFanAndTempControl,
       "ccAccessChangedControl": ccAccessChangedControl,
       "tpcPowerReducedControl": tpcPowerReducedControl,
       "dfsRadarDetectControl": dfsRadarDetectControl,
       "dfsChannelSelectControl": dfsChannelSelectControl,
       "dfsChannelSwitchControl": dfsChannelSwitchControl,
       "dfsChannelRevertControl": dfsChannelRevertControl,
       "radioSuspendControl": radioSuspendControl,
       "radioResumeControl": radioResumeControl,
       "radioRandomChannelControl": radioRandomChannelControl,
       "ccRapNewRogueApControl": ccRapNewRogueApControl,
       "ccRapNewApprovedApControl": ccRapNewApprovedApControl,
       "ccTrapInfoWVPNAlert": ccTrapInfoWVPNAlert,
       "ccTrapInfoWVPNInfo": ccTrapInfoWVPNInfo,
       "ccTrapInfoRadiusAcct": ccTrapInfoRadiusAcct,
       "ccInfoRadiusServerControl": ccInfoRadiusServerControl,
       "configChangeUpdateControl": configChangeUpdateControl,
       "tunnelStatusChangedControl": tunnelStatusChangedControl,
       "tunnelUnknownProtocolControl": tunnelUnknownProtocolControl,
       "ccSumStatsApControl": ccSumStatsApControl,
       "ccSumStatsMuControl": ccSumStatsMuControl,
       "ccSumStatsWlanControl": ccSumStatsWlanControl,
       "ccSumStatsSwitchControl": ccSumStatsSwitchControl,
       "sensorConvertControl": sensorConvertControl,
       "sensorRevertControl": sensorRevertControl,
       "sensorFailureControl": sensorFailureControl,
       "sensorOfflineControl": sensorOfflineControl,
       "symbolCCTraps": symbolCCTraps,
       "ccTrapLowFlashSpace": ccTrapLowFlashSpace,
       "ccTrapNicDropping": ccTrapNicDropping,
       "ccTrapAPMUMaxExceed": ccTrapAPMUMaxExceed,
       "ccTrapWLANMUMaxExceed": ccTrapWLANMUMaxExceed,
       "ccTrapAPDetected": ccTrapAPDetected,
       "ccTrapAPAdopted": ccTrapAPAdopted,
       "ccTrapAPReset": ccTrapAPReset,
       "ccTrapAPUnavailable": ccTrapAPUnavailable,
       "ccTrapAPAlert": ccTrapAPAlert,
       "ccTrapUserAuthFail": ccTrapUserAuthFail,
       "ccTrapRadiusAuthFail": ccTrapRadiusAuthFail,
       "ccTrapACLViolation": ccTrapACLViolation,
       "ccTrapDenyAPAdoption": ccTrapDenyAPAdoption,
       "ccTrapHsbPrimaryNoHeartbeat": ccTrapHsbPrimaryNoHeartbeat,
       "ccTrapHsbStandbyEntersFailover": ccTrapHsbStandbyEntersFailover,
       "ccTrapHsbPrimaryFailedResetting": ccTrapHsbPrimaryFailedResetting,
       "ccTrapHsbStandbyFailedResetting": ccTrapHsbStandbyFailedResetting,
       "ccTrapKDCUserAuthFail": ccTrapKDCUserAuthFail,
       "ccTrapKDCPropagationFail": ccTrapKDCPropagationFail,
       "ccTrapHighDecryptFail": ccTrapHighDecryptFail,
       "ccTrapHighReplyFail": ccTrapHighReplyFail,
       "ccTrapTKIPMICFail": ccTrapTKIPMICFail,
       "ccTrapWPACounterMeasureStart": ccTrapWPACounterMeasureStart,
       "licenseChanged": licenseChanged,
       "clockChanged": clockChanged,
       "pktDiscWrongNIC": pktDiscWrongNIC,
       "pktDiscWrongVLAN": pktDiscWrongVLAN,
       "apAdoptFailPol": apAdoptFailPol,
       "apAdoptFailACL": apAdoptFailACL,
       "apAdoptFailLimit": apAdoptFailLimit,
       "apAdoptFailLic": apAdoptFailLic,
       "apAdoptFailNoImg": apAdoptFailNoImg,
       "apCfgFailESS": apCfgFailESS,
       "devDropInfoMsg": devDropInfoMsg,
       "devdropLoadmeMsg": devdropLoadmeMsg,
       "etherConnect": etherConnect,
       "muAssocFail": muAssocFail,
       "muAssocOK": muAssocOK,
       "muRoamed": muRoamed,
       "muDisassoc": muDisassoc,
       "muEAPAuthFail": muEAPAuthFail,
       "muEAPAuthOK": muEAPAuthOK,
       "muKDCAuthOK": muKDCAuthOK,
       "wlanAuthOK": wlanAuthOK,
       "wlanAuthFail": wlanAuthFail,
       "userAuthOK": userAuthOK,
       "radiusSrvTimeout": radiusSrvTimeout,
       "kdcPrincAdd": kdcPrincAdd,
       "kdcPrincChgd": kdcPrincChgd,
       "kdcPrincDel": kdcPrincDel,
       "kdcDBReplaced": kdcDBReplaced,
       "hsbStdbyAutoRev": hsbStdbyAutoRev,
       "hsbPrimAutoRev": hsbPrimAutoRev,
       "acsError": acsError,
       "eopActive": eopActive,
       "eopInactive": eopInactive,
       "debugEvent": debugEvent,
       "hsbStartUp": hsbStartUp,
       "hsbPeerConnect": hsbPeerConnect,
       "ccFanAndTempNotification": ccFanAndTempNotification,
       "ccAccessChangedNotification": ccAccessChangedNotification,
       "tpcPowerReduced": tpcPowerReduced,
       "dfsRadarDetect": dfsRadarDetect,
       "dfsChannelSelect": dfsChannelSelect,
       "dfsChannelSwitch": dfsChannelSwitch,
       "dfsChannelRevert": dfsChannelRevert,
       "radioSuspend": radioSuspend,
       "radioResume": radioResume,
       "radioRandomChannel": radioRandomChannel,
       "ccRapNewRogueAp": ccRapNewRogueAp,
       "ccRapNewApprovedAp": ccRapNewApprovedAp,
       "ccTrapWVPNAlert": ccTrapWVPNAlert,
       "ccTrapWVPNInfo": ccTrapWVPNInfo,
       "ccTrapInfoRadiusAcctInfo": ccTrapInfoRadiusAcctInfo,
       "ccInfoRadiusServer": ccInfoRadiusServer,
       "configChangeUpdate": configChangeUpdate,
       "tunnelStatusChanged": tunnelStatusChanged,
       "tunnelUnknownProtocol": tunnelUnknownProtocol,
       "ccSumStatsAp": ccSumStatsAp,
       "ccSumStatsMu": ccSumStatsMu,
       "ccSumStatsWlan": ccSumStatsWlan,
       "ccSumStatsSwitch": ccSumStatsSwitch,
       "sensorConvert": sensorConvert,
       "sensorRevert": sensorRevert,
       "sensorFailure": sensorFailure,
       "sensorOffline": sensorOffline,
       "symbolCCNewInV1dot2dot5": symbolCCNewInV1dot2dot5,
       "ccIdentfication": ccIdentfication,
       "ccIdHwVersion": ccIdHwVersion,
       "ccIdFwVersion": ccIdFwVersion,
       "ccIdSwVersion": ccIdSwVersion,
       "ccIdMibVersion": ccIdMibVersion,
       "ccIdCliVersion": ccIdCliVersion,
       "ccIdXmlVersion": ccIdXmlVersion,
       "ccIdSerialNumber": ccIdSerialNumber,
       "ccIdSwBuildDate": ccIdSwBuildDate,
       "ccIdSwBuildInfo": ccIdSwBuildInfo,
       "ccIdProductFamily": ccIdProductFamily,
       "ccIdProductModel": ccIdProductModel,
       "ccHwSensors": ccHwSensors,
       "ccHwSensorsReset": ccHwSensorsReset,
       "ccHwSensorsTable": ccHwSensorsTable,
       "ccHwSensorsEntry": ccHwSensorsEntry,
       "ccHwSensorsIndex": ccHwSensorsIndex,
       "ccHwSensorsType": ccHwSensorsType,
       "ccHwSensorsDescr": ccHwSensorsDescr,
       "ccHwSensorsCurrentReading": ccHwSensorsCurrentReading,
       "ccHwSensorsMinimum": ccHwSensorsMinimum,
       "ccHwSensorsMaximum": ccHwSensorsMaximum,
       "ccHwSensorsNotifyIfAbove": ccHwSensorsNotifyIfAbove,
       "ccSsh": ccSsh,
       "ccSshEnabled": ccSshEnabled,
       "ccSshProtocolVersion": ccSshProtocolVersion,
       "ccSshPort": ccSshPort,
       "ccSshAuthenticationTimeout": ccSshAuthenticationTimeout,
       "ccSshInactivityTimeout": ccSshInactivityTimeout,
       "ccAccessMethods": ccAccessMethods,
       "ccAccessMethodsPermitted": ccAccessMethodsPermitted,
       "ccV1dot2dot5Groups": ccV1dot2dot5Groups,
       "ccModuleId": ccModuleId,
       "v1dot2dot5Group": v1dot2dot5Group,
       "v1dot2dot5NotificationGroup": v1dot2dot5NotificationGroup,
       "v1dot2dot5GroupOfDepricated": v1dot2dot5GroupOfDepricated,
       "ccRadiusServer": ccRadiusServer,
       "ccRadius": ccRadius,
       "ccRadiusDataSource": ccRadiusDataSource,
       "ccRadiusDefaultEapType": ccRadiusDefaultEapType,
       "ccRadiusAuthTypePeap": ccRadiusAuthTypePeap,
       "ccRadiusAuthTypeTtls": ccRadiusAuthTypeTtls,
       "ccRadiusServerCertificate": ccRadiusServerCertificate,
       "ccRadiusCACertificate": ccRadiusCACertificate,
       "ccRadiusClientAuthTable": ccRadiusClientAuthTable,
       "ccRadiusClientAuthEntry": ccRadiusClientAuthEntry,
       "ccRadiusClientAuthIndex": ccRadiusClientAuthIndex,
       "ccRadiusClientAuthIpAddr": ccRadiusClientAuthIpAddr,
       "ccRadiusClientAuthMask": ccRadiusClientAuthMask,
       "ccRadiusClientAuthSharedSecret": ccRadiusClientAuthSharedSecret,
       "ccRadiusClientAuthRowStatus": ccRadiusClientAuthRowStatus,
       "ccRadiusServerEnable": ccRadiusServerEnable,
       "ccRadiusSaveStatus": ccRadiusSaveStatus,
       "ccRadiusEapPasswd": ccRadiusEapPasswd,
       "ccRadiusProxy": ccRadiusProxy,
       "ccRadiusProxyRetryCount": ccRadiusProxyRetryCount,
       "ccRadiusProxyTimeout": ccRadiusProxyTimeout,
       "ccRadiusProxyServerTable": ccRadiusProxyServerTable,
       "ccRadiusProxyServerEntry": ccRadiusProxyServerEntry,
       "ccRadiusProxyServerIndex": ccRadiusProxyServerIndex,
       "ccRadiusProxyServerPrefixOrSuffix": ccRadiusProxyServerPrefixOrSuffix,
       "ccRadiusProxyServerIp": ccRadiusProxyServerIp,
       "ccRadiusProxyServerPort": ccRadiusProxyServerPort,
       "ccRadiusProxyServerSharedSecret": ccRadiusProxyServerSharedSecret,
       "ccRadiusProxyServerRowStatus": ccRadiusProxyServerRowStatus,
       "ccRadiusLdap": ccRadiusLdap,
       "ccRadiusLdap1Server": ccRadiusLdap1Server,
       "ccRadiusLdap1ServerIp": ccRadiusLdap1ServerIp,
       "ccRadiusLdap1ServerPort": ccRadiusLdap1ServerPort,
       "ccRadiusLdap1LoginAttribute": ccRadiusLdap1LoginAttribute,
       "ccRadiusLdap1PasswordAttribute": ccRadiusLdap1PasswordAttribute,
       "ccRadiusLdap1BindDistinguishedName": ccRadiusLdap1BindDistinguishedName,
       "ccRadiusLdap1BindDistinguishedPassword": ccRadiusLdap1BindDistinguishedPassword,
       "ccRadiusLdap1BaseDistinguishedName": ccRadiusLdap1BaseDistinguishedName,
       "ccRadiusLdap1GroupAttribute": ccRadiusLdap1GroupAttribute,
       "ccRadiusLdap1GroupFilter": ccRadiusLdap1GroupFilter,
       "ccRadiusLdap1GroupMembershipAttribute": ccRadiusLdap1GroupMembershipAttribute,
       "ccRadiusLdap2Server": ccRadiusLdap2Server,
       "ccRadiusLdap2ServerIp": ccRadiusLdap2ServerIp,
       "ccRadiusLdap2ServerPort": ccRadiusLdap2ServerPort,
       "ccRadiusLdap2LoginAttribute": ccRadiusLdap2LoginAttribute,
       "ccRadiusLdap2PasswordATtribute": ccRadiusLdap2PasswordATtribute,
       "ccRadiusLdap2BindDistinguishedName": ccRadiusLdap2BindDistinguishedName,
       "ccRadiusLdap2BindDistinguishedPassword": ccRadiusLdap2BindDistinguishedPassword,
       "ccRadiusLdap2BaseDistinguishedName": ccRadiusLdap2BaseDistinguishedName,
       "ccRadiusLdap2GroupAttribute": ccRadiusLdap2GroupAttribute,
       "ccRadiusLdap2GroupFilter": ccRadiusLdap2GroupFilter,
       "ccRadiusLdap2GroupMembershipAttribute": ccRadiusLdap2GroupMembershipAttribute,
       "ccRadiusUsers": ccRadiusUsers,
       "ccRadiusGroupsTable": ccRadiusGroupsTable,
       "ccRadiusGroupsEntry": ccRadiusGroupsEntry,
       "ccRadiusGroup": ccRadiusGroup,
       "ccRadiusGroupRowStatus": ccRadiusGroupRowStatus,
       "ccRadiusUsersTable": ccRadiusUsersTable,
       "ccRadiusUsersEntry": ccRadiusUsersEntry,
       "ccRadiusUsersId": ccRadiusUsersId,
       "ccRadiusUsersPassword": ccRadiusUsersPassword,
       "ccRadiusUsersGroups": ccRadiusUsersGroups,
       "ccRadiusUsersRowStatus": ccRadiusUsersRowStatus,
       "ccRadiusAccess": ccRadiusAccess,
       "ccRadiusAccessTable": ccRadiusAccessTable,
       "ccRadiusAccessEntry": ccRadiusAccessEntry,
       "ccRadiusAccessGroupId": ccRadiusAccessGroupId,
       "ccRadiusAccessWlanPtrs": ccRadiusAccessWlanPtrs,
       "ccRadiusAcct": ccRadiusAcct,
       "ccRadiusAcctIPAddress": ccRadiusAcctIPAddress,
       "ccRadiusAcctPort": ccRadiusAcctPort,
       "ccRadiusAcctTimeout": ccRadiusAcctTimeout,
       "ccRadiusAcctMaxRetry": ccRadiusAcctMaxRetry,
       "ccRadiusAcctSharedSecret": ccRadiusAcctSharedSecret,
       "ccRadiusTimeRestriction": ccRadiusTimeRestriction,
       "ccRadiusTimeRestrictionTable": ccRadiusTimeRestrictionTable,
       "ccRadiusTimeRestrictionEntry": ccRadiusTimeRestrictionEntry,
       "ccRadiusTimeRestrictionStart": ccRadiusTimeRestrictionStart,
       "ccRadiusTimeRestrictionEnd": ccRadiusTimeRestrictionEnd,
       "ccRadiusTimeRestrictionDays": ccRadiusTimeRestrictionDays,
       "ccRap": ccRap,
       "ccRapControl": ccRapControl,
       "ccRapControlPollSymbolMus": ccRapControlPollSymbolMus,
       "ccRapPollSymbolMusEnable": ccRapPollSymbolMusEnable,
       "ccRapPollSymbolMusInterval": ccRapPollSymbolMusInterval,
       "ccRapControlOnChannel": ccRapControlOnChannel,
       "ccRapOnChannelEnable": ccRapOnChannelEnable,
       "ccRapOnChannelInterval": ccRapOnChannelInterval,
       "ccRapControlDetectors": ccRapControlDetectors,
       "ccRapDetectorsEnable": ccRapDetectorsEnable,
       "ccRapDetectorsInterval": ccRapDetectorsInterval,
       "ccRapAuth": ccRapAuth,
       "ccRapAuthList": ccRapAuthList,
       "ccRapAuthAllSymbolMac": ccRapAuthAllSymbolMac,
       "ccRapAuthTable": ccRapAuthTable,
       "ccRapAuthEntry": ccRapAuthEntry,
       "ccRapAuthIndex": ccRapAuthIndex,
       "ccRapAuthMacFilter": ccRapAuthMacFilter,
       "ccRapAuthEssidFilter": ccRapAuthEssidFilter,
       "ccRapAuthRowExists": ccRapAuthRowExists,
       "ccRapAuthErase": ccRapAuthErase,
       "ccRapAuthCopyAllApproved": ccRapAuthCopyAllApproved,
       "ccRapAuthCopyAllRogue": ccRapAuthCopyAllRogue,
       "ccRapResults": ccRapResults,
       "ccRapResultsApproved": ccRapResultsApproved,
       "ccRapResultsApprovedAgeOut": ccRapResultsApprovedAgeOut,
       "ccRapResultsApprovedTable": ccRapResultsApprovedTable,
       "ccRapResultsApprovedEntry": ccRapResultsApprovedEntry,
       "ccRapResultsApprovedIndex": ccRapResultsApprovedIndex,
       "ccRapResultsApprovedApMac": ccRapResultsApprovedApMac,
       "ccRapResultsApprovedEssid": ccRapResultsApprovedEssid,
       "ccRapResultsApprovedCopyToAuthTable": ccRapResultsApprovedCopyToAuthTable,
       "ccRapResultsApprovedFirstHeard": ccRapResultsApprovedFirstHeard,
       "ccRapResultsApprovedLastHeard": ccRapResultsApprovedLastHeard,
       "ccRapResultsApprovedPortalPtr": ccRapResultsApprovedPortalPtr,
       "ccRapResultsApprovedHowFound": ccRapResultsApprovedHowFound,
       "ccRapResultsApprovedHowAuth": ccRapResultsApprovedHowAuth,
       "ccRapResultsApprovedRowErase": ccRapResultsApprovedRowErase,
       "ccRapResultsApprovedErase": ccRapResultsApprovedErase,
       "ccRapResultsRogue": ccRapResultsRogue,
       "ccRapResultsRogueAgeOut": ccRapResultsRogueAgeOut,
       "ccRapResultsRogueTable": ccRapResultsRogueTable,
       "ccRapResultsRogueEntry": ccRapResultsRogueEntry,
       "ccRapResultsRogueIndex": ccRapResultsRogueIndex,
       "ccRapResultsRogueApMac": ccRapResultsRogueApMac,
       "ccRapResultsRogueEssid": ccRapResultsRogueEssid,
       "ccRapResultsRogueCopyToAuthTable": ccRapResultsRogueCopyToAuthTable,
       "ccRapResultsRogueFirstHeard": ccRapResultsRogueFirstHeard,
       "ccRapResultsRogueLastHeard": ccRapResultsRogueLastHeard,
       "ccRapResultsRoguePortalPtr": ccRapResultsRoguePortalPtr,
       "ccRapResultsRogueHowFound": ccRapResultsRogueHowFound,
       "ccRapResultsRogueClosestPortalPtr": ccRapResultsRogueClosestPortalPtr,
       "ccRapResultsRogueClosestPortalRssi": ccRapResultsRogueClosestPortalRssi,
       "ccRapResultsRogueErase": ccRapResultsRogueErase,
       "ccImageDload": ccImageDload,
       "ccRestore": ccRestore,
       "ccFtp": ccFtp,
       "ccTftp": ccTftp,
       "ccListFiles": ccListFiles,
       "ccDeleteFiles": ccDeleteFiles,
       "ccRFStatistics": ccRFStatistics,
       "ccAp": ccAp,
       "ccApTable": ccApTable,
       "ccApEntry": ccApEntry,
       "ccApIndex": ccApIndex,
       "ccApNicMac": ccApNicMac,
       "ccApModelNumber": ccApModelNumber,
       "ccApSerialNumber": ccApSerialNumber,
       "ccApPcbRevision": ccApPcbRevision,
       "ccApBootLoaderRev": ccApBootLoaderRev,
       "ccApWispVersion": ccApWispVersion,
       "ccApRuntimeFwVersion": ccApRuntimeFwVersion,
       "ccApNumPortals": ccApNumPortals,
       "ccApPointersToPortals": ccApPointersToPortals,
       "ccPortal": ccPortal,
       "ccPortalTable": ccPortalTable,
       "ccPortalEntry": ccPortalEntry,
       "ccPortalIndex": ccPortalIndex,
       "ccPortalPointerToAp": ccPortalPointerToAp,
       "ccPortalPointersToWlans": ccPortalPointersToWlans,
       "ccPortalName": ccPortalName,
       "ccPortalLocation": ccPortalLocation,
       "ccPortalOptions": ccPortalOptions,
       "ccPortalMac": ccPortalMac,
       "ccPortalNumberofEss": ccPortalNumberofEss,
       "ccPortalNumberOfBss": ccPortalNumberOfBss,
       "ccPortalAssociatedMus": ccPortalAssociatedMus,
       "ccPortalRadioType": ccPortalRadioType,
       "ccPortalChannel": ccPortalChannel,
       "ccPortalTxPowerLevel": ccPortalTxPowerLevel,
       "ccPortalLastAdoption": ccPortalLastAdoption,
       "ccPortalState": ccPortalState,
       "ccPortalBackgroundNoiseNumSamples": ccPortalBackgroundNoiseNumSamples,
       "ccPortalBackgroundNoiseBest": ccPortalBackgroundNoiseBest,
       "ccPortalBackgroundNoiseWorst": ccPortalBackgroundNoiseWorst,
       "ccPortalBackgroundNoiseSum": ccPortalBackgroundNoiseSum,
       "ccPortalBackgroundNoiseSumSquares": ccPortalBackgroundNoiseSumSquares,
       "ccPortalLastMac": ccPortalLastMac,
       "ccPortalLastReason": ccPortalLastReason,
       "ccPortalSystemStatsTable": ccPortalSystemStatsTable,
       "ccPortalSystemStatsEntry": ccPortalSystemStatsEntry,
       "ccPortalSystemStatsBeaconTx": ccPortalSystemStatsBeaconTx,
       "ccPortalSystemStatsBeaconsTxOctets": ccPortalSystemStatsBeaconsTxOctets,
       "ccPortalSystemStatsProbeReqRx": ccPortalSystemStatsProbeReqRx,
       "ccPortalSystemStatsProbeReqRxOctets": ccPortalSystemStatsProbeReqRxOctets,
       "ccPortalSystemStatsProbeRespRetriesNone": ccPortalSystemStatsProbeRespRetriesNone,
       "ccPortalSystemStatsProbeRespRetries1": ccPortalSystemStatsProbeRespRetries1,
       "ccPortalSystemStatsProbeRespRetries2": ccPortalSystemStatsProbeRespRetries2,
       "ccPortalSystemStatsProbeRespRetries3OrMore": ccPortalSystemStatsProbeRespRetries3OrMore,
       "ccPortalSystemStatsProbeRespRetriesFailed": ccPortalSystemStatsProbeRespRetriesFailed,
       "ccPortalSystemStatsProbeRespTxOctets": ccPortalSystemStatsProbeRespTxOctets,
       "ccPortalRfSum": ccPortalRfSum,
       "ccPortalStatsTable": ccPortalStatsTable,
       "ccPortalStatsEntry": ccPortalStatsEntry,
       "ccPortalTxPktsUcast": ccPortalTxPktsUcast,
       "ccPortalRxPktsUcast": ccPortalRxPktsUcast,
       "ccPortalRxPktsNUcast": ccPortalRxPktsNUcast,
       "ccPortalTxOctetsUcast": ccPortalTxOctetsUcast,
       "ccPortalRxOctetsUcast": ccPortalRxOctetsUcast,
       "ccPortalRxOctetsNUcast": ccPortalRxOctetsNUcast,
       "ccPortalRxUndecryptablePkts": ccPortalRxUndecryptablePkts,
       "ccPortalLastActivity": ccPortalLastActivity,
       "ccPortalRxPktsTable": ccPortalRxPktsTable,
       "ccPortalRxPktsEntry": ccPortalRxPktsEntry,
       "ccPortalRxPktsAt1Mb": ccPortalRxPktsAt1Mb,
       "ccPortalRxPktsAt2Mb": ccPortalRxPktsAt2Mb,
       "ccPortalRxPktsAt5pt5Mb": ccPortalRxPktsAt5pt5Mb,
       "ccPortalRxPktsAt6Mb": ccPortalRxPktsAt6Mb,
       "ccPortalRxPktsAt9Mb": ccPortalRxPktsAt9Mb,
       "ccPortalRxPktsAt11Mb": ccPortalRxPktsAt11Mb,
       "ccPortalRxPktsAt12Mb": ccPortalRxPktsAt12Mb,
       "ccPortalRxPktsAt18Mb": ccPortalRxPktsAt18Mb,
       "ccPortalRxPktsAt22Mb": ccPortalRxPktsAt22Mb,
       "ccPortalRxPktsAt24Mb": ccPortalRxPktsAt24Mb,
       "ccPortalRxPktsAt36Mb": ccPortalRxPktsAt36Mb,
       "ccPortalRxPktsAt48Mb": ccPortalRxPktsAt48Mb,
       "ccPortalRxPktsAt54Mb": ccPortalRxPktsAt54Mb,
       "ccPortalTxPktsTable": ccPortalTxPktsTable,
       "ccPortalTxPktsEntry": ccPortalTxPktsEntry,
       "ccPortalTxPktsAt1Mb": ccPortalTxPktsAt1Mb,
       "ccPortalTxPktsAt2Mb": ccPortalTxPktsAt2Mb,
       "ccPortalTxPktsAt5pt5Mb": ccPortalTxPktsAt5pt5Mb,
       "ccPortalTxPktsAt6Mb": ccPortalTxPktsAt6Mb,
       "ccPortalTxPktsAt9Mb": ccPortalTxPktsAt9Mb,
       "ccPortalTxPktsAt11Mb": ccPortalTxPktsAt11Mb,
       "ccPortalTxPktsAt12Mb": ccPortalTxPktsAt12Mb,
       "ccPortalTxPktsAt18Mb": ccPortalTxPktsAt18Mb,
       "ccPortalTxPktsAt22Mb": ccPortalTxPktsAt22Mb,
       "ccPortalTxPktsAt24Mb": ccPortalTxPktsAt24Mb,
       "ccPortalTxPktsAt36Mb": ccPortalTxPktsAt36Mb,
       "ccPortalTxPktsAt48Mb": ccPortalTxPktsAt48Mb,
       "ccPortalTxPktsAt54Mb": ccPortalTxPktsAt54Mb,
       "ccPortalRxOctetsTable": ccPortalRxOctetsTable,
       "ccPortalRxOctetsEntry": ccPortalRxOctetsEntry,
       "ccPortalRxOctetsAt1Mb": ccPortalRxOctetsAt1Mb,
       "ccPortalRxOctetsAt2Mb": ccPortalRxOctetsAt2Mb,
       "ccPortalRxOctetsAt5pt5Mb": ccPortalRxOctetsAt5pt5Mb,
       "ccPortalRxOctetsAt6Mb": ccPortalRxOctetsAt6Mb,
       "ccPortalRxOctetsAt9Mb": ccPortalRxOctetsAt9Mb,
       "ccPortalRxOctetsAt11Mb": ccPortalRxOctetsAt11Mb,
       "ccPortalRxOctetsAt12Mb": ccPortalRxOctetsAt12Mb,
       "ccPortalRxOctetsAt18Mb": ccPortalRxOctetsAt18Mb,
       "ccPortalRxOctetsAt22Mb": ccPortalRxOctetsAt22Mb,
       "ccPortalRxOctetsAt24Mb": ccPortalRxOctetsAt24Mb,
       "ccPortalRxOctetsAt36Mb": ccPortalRxOctetsAt36Mb,
       "ccPortalRxOctetsAt48Mb": ccPortalRxOctetsAt48Mb,
       "ccPortalRxOctetsAt54Mb": ccPortalRxOctetsAt54Mb,
       "ccPortalTxOctetsTable": ccPortalTxOctetsTable,
       "ccPortalTxOctetsEntry": ccPortalTxOctetsEntry,
       "ccPortalTxOctetsAt1Mb": ccPortalTxOctetsAt1Mb,
       "ccPortalTxOctetsAt2Mb": ccPortalTxOctetsAt2Mb,
       "ccPortalTxOctetsAt5pt5Mb": ccPortalTxOctetsAt5pt5Mb,
       "ccPortalTxOctetsAt6Mb": ccPortalTxOctetsAt6Mb,
       "ccPortalTxOctetsAt9Mb": ccPortalTxOctetsAt9Mb,
       "ccPortalTxOctetsAt11Mb": ccPortalTxOctetsAt11Mb,
       "ccPortalTxOctetsAt12Mb": ccPortalTxOctetsAt12Mb,
       "ccPortalTxOctetsAt18Mb": ccPortalTxOctetsAt18Mb,
       "ccPortalTxOctetsAt22Mb": ccPortalTxOctetsAt22Mb,
       "ccPortalTxOctetsAt24Mb": ccPortalTxOctetsAt24Mb,
       "ccPortalTxOctetsAt36Mb": ccPortalTxOctetsAt36Mb,
       "ccPortalTxOctetsAt48Mb": ccPortalTxOctetsAt48Mb,
       "ccPortalTxOctetsAt54Mb": ccPortalTxOctetsAt54Mb,
       "ccPortalTxRetriesPktsTable": ccPortalTxRetriesPktsTable,
       "ccPortalTxRetriesPktsEntry": ccPortalTxRetriesPktsEntry,
       "ccPortalTxRetriesPktsNone": ccPortalTxRetriesPktsNone,
       "ccPortalTxRetriesPkts01": ccPortalTxRetriesPkts01,
       "ccPortalTxRetriesPkts02": ccPortalTxRetriesPkts02,
       "ccPortalTxRetriesPkts03": ccPortalTxRetriesPkts03,
       "ccPortalTxRetriesPkts04": ccPortalTxRetriesPkts04,
       "ccPortalTxRetriesPkts05": ccPortalTxRetriesPkts05,
       "ccPortalTxRetriesPkts06": ccPortalTxRetriesPkts06,
       "ccPortalTxRetriesPkts07": ccPortalTxRetriesPkts07,
       "ccPortalTxRetriesPkts08": ccPortalTxRetriesPkts08,
       "ccPortalTxRetriesPkts09": ccPortalTxRetriesPkts09,
       "ccPortalTxRetriesPkts10": ccPortalTxRetriesPkts10,
       "ccPortalTxRetriesPkts11": ccPortalTxRetriesPkts11,
       "ccPortalTxRetriesPkts12": ccPortalTxRetriesPkts12,
       "ccPortalTxRetriesPkts13": ccPortalTxRetriesPkts13,
       "ccPortalTxRetriesPkts14": ccPortalTxRetriesPkts14,
       "ccPortalTxRetriesPkts15": ccPortalTxRetriesPkts15,
       "ccPortalTxRetriesPktsFailed": ccPortalTxRetriesPktsFailed,
       "ccPortalTxRetriesOctetsTable": ccPortalTxRetriesOctetsTable,
       "ccPortalTxRetriesOctetsEntry": ccPortalTxRetriesOctetsEntry,
       "ccPortalTxRetriesOctetsNone": ccPortalTxRetriesOctetsNone,
       "ccPortalTxRetriesOctets01": ccPortalTxRetriesOctets01,
       "ccPortalTxRetriesOctets02": ccPortalTxRetriesOctets02,
       "ccPortalTxRetriesOctets03": ccPortalTxRetriesOctets03,
       "ccPortalTxRetriesOctets04": ccPortalTxRetriesOctets04,
       "ccPortalTxRetriesOctets05": ccPortalTxRetriesOctets05,
       "ccPortalTxRetriesOctets06": ccPortalTxRetriesOctets06,
       "ccPortalTxRetriesOctets07": ccPortalTxRetriesOctets07,
       "ccPortalTxRetriesOctets08": ccPortalTxRetriesOctets08,
       "ccPortalTxRetriesOctets09": ccPortalTxRetriesOctets09,
       "ccPortalTxRetriesOctets10": ccPortalTxRetriesOctets10,
       "ccPortalTxRetriesOctets11": ccPortalTxRetriesOctets11,
       "ccPortalTxRetriesOctets12": ccPortalTxRetriesOctets12,
       "ccPortalTxRetriesOctets13": ccPortalTxRetriesOctets13,
       "ccPortalTxRetriesOctets14": ccPortalTxRetriesOctets14,
       "ccPortalTxRetriesOctets15": ccPortalTxRetriesOctets15,
       "ccPortalTxRetriesOctetsFailed": ccPortalTxRetriesOctetsFailed,
       "ccPortalSigStatsTable": ccPortalSigStatsTable,
       "ccPortalSigStatsEntry": ccPortalSigStatsEntry,
       "ccPortalSigStatsNumPkts": ccPortalSigStatsNumPkts,
       "ccPortalSigStatsSignalBest": ccPortalSigStatsSignalBest,
       "ccPortalSigStatsSignalWorst": ccPortalSigStatsSignalWorst,
       "ccPortalSigStatsSignalSum": ccPortalSigStatsSignalSum,
       "ccPortalSigStatsSignalSumSquares": ccPortalSigStatsSignalSumSquares,
       "ccPortalSigStatsSignalMostRecent": ccPortalSigStatsSignalMostRecent,
       "ccPortalSigStatsNoiseBest": ccPortalSigStatsNoiseBest,
       "ccPortalSigStatsNoiseWorst": ccPortalSigStatsNoiseWorst,
       "ccPortalSigStatsNoiseSum": ccPortalSigStatsNoiseSum,
       "ccPortalSigStatsNoiseSumSquares": ccPortalSigStatsNoiseSumSquares,
       "ccPortalSigStatsNoiseMostRecent": ccPortalSigStatsNoiseMostRecent,
       "ccPortalSigStatsSnrBest": ccPortalSigStatsSnrBest,
       "ccPortalSigStatsSnrWorst": ccPortalSigStatsSnrWorst,
       "ccPortalSigStatsSnrSum": ccPortalSigStatsSnrSum,
       "ccPortalSigStatsSnrSumSquares": ccPortalSigStatsSnrSumSquares,
       "ccPortalSigStatsSnrMostRecent": ccPortalSigStatsSnrMostRecent,
       "ccPortalSumStatsShortTable": ccPortalSumStatsShortTable,
       "ccPortalSumStatsShortEntry": ccPortalSumStatsShortEntry,
       "ccPortalSumStatsShortTimestamp": ccPortalSumStatsShortTimestamp,
       "ccPortalSumStatsShortNumPkts": ccPortalSumStatsShortNumPkts,
       "ccPortalSumStatsShortPktsPerSec100": ccPortalSumStatsShortPktsPerSec100,
       "ccPortalSumStatsShortPktsPerSecTx100": ccPortalSumStatsShortPktsPerSecTx100,
       "ccPortalSumStatsShortPktsPerSecRx100": ccPortalSumStatsShortPktsPerSecRx100,
       "ccPortalSumStatsShortThroughput": ccPortalSumStatsShortThroughput,
       "ccPortalSumStatsShortThroughputTx": ccPortalSumStatsShortThroughputTx,
       "ccPortalSumStatsShortThroughputRx": ccPortalSumStatsShortThroughputRx,
       "ccPortalSumStatsShortAvgBitSpeed": ccPortalSumStatsShortAvgBitSpeed,
       "ccPortalSumStatsShortAvgMuSignal": ccPortalSumStatsShortAvgMuSignal,
       "ccPortalSumStatsShortAvgMuNoise": ccPortalSumStatsShortAvgMuNoise,
       "ccPortalSumStatsShortAvgMuSnr": ccPortalSumStatsShortAvgMuSnr,
       "ccPortalSumStatsShortPp10kNUcastPkts": ccPortalSumStatsShortPp10kNUcastPkts,
       "ccPortalSumStatsShortPp10kTxWithRetries": ccPortalSumStatsShortPp10kTxWithRetries,
       "ccPortalSumStatsShortPp10kTxMaxRetries": ccPortalSumStatsShortPp10kTxMaxRetries,
       "ccPortalSumStatsShortTxAvgRetries100": ccPortalSumStatsShortTxAvgRetries100,
       "ccPortalSumStatsShortPp10kRxUndecrypt": ccPortalSumStatsShortPp10kRxUndecrypt,
       "ccPortalSumStatsShortTotalMus": ccPortalSumStatsShortTotalMus,
       "ccPortalSumStatsShortPp10kRfUtil": ccPortalSumStatsShortPp10kRfUtil,
       "ccPortalSumStatsShortPp10kDropped": ccPortalSumStatsShortPp10kDropped,
       "ccPortalSumStatsLongTable": ccPortalSumStatsLongTable,
       "ccPortalSumStatsLongEntry": ccPortalSumStatsLongEntry,
       "ccPortalSumStatsLongTimestamp": ccPortalSumStatsLongTimestamp,
       "ccPortalSumStatsLongNumPkts": ccPortalSumStatsLongNumPkts,
       "ccPortalSumStatsLongPktsPerSec100": ccPortalSumStatsLongPktsPerSec100,
       "ccPortalSumStatsLongPktsPerSecTx100": ccPortalSumStatsLongPktsPerSecTx100,
       "ccPortalSumStatsLongPktsPerSecRx100": ccPortalSumStatsLongPktsPerSecRx100,
       "ccPortalSumStatsLongThroughput": ccPortalSumStatsLongThroughput,
       "ccPortalSumStatsLongThroughputTx": ccPortalSumStatsLongThroughputTx,
       "ccPortalSumStatsLongThroughputRx": ccPortalSumStatsLongThroughputRx,
       "ccPortalSumStatsLongAvgBitSpeed": ccPortalSumStatsLongAvgBitSpeed,
       "ccPortalSumStatsLongAvgMuSignal": ccPortalSumStatsLongAvgMuSignal,
       "ccPortalSumStatsLongAvgMuNoise": ccPortalSumStatsLongAvgMuNoise,
       "ccPortalSumStatsLongAvgMuSnr": ccPortalSumStatsLongAvgMuSnr,
       "ccPortalSumStatsLongPp10kNUcastPkts": ccPortalSumStatsLongPp10kNUcastPkts,
       "ccPortalSumStatsLongPp10kTxWithRetries": ccPortalSumStatsLongPp10kTxWithRetries,
       "ccPortalSumStatsLongPp10kTxMaxRetries": ccPortalSumStatsLongPp10kTxMaxRetries,
       "ccPortalSumStatsLongTxAvgRetries100": ccPortalSumStatsLongTxAvgRetries100,
       "ccPortalSumStatsLongPp10kRxUndecrypt": ccPortalSumStatsLongPp10kRxUndecrypt,
       "ccPortalSumStatsLongTotalMus": ccPortalSumStatsLongTotalMus,
       "ccPortalSumStatsLongPp10kRfUtil": ccPortalSumStatsLongPp10kRfUtil,
       "ccPortalSumStatsLongPp10kDropped": ccPortalSumStatsLongPp10kDropped,
       "ccMus": ccMus,
       "ccMuInfoTable": ccMuInfoTable,
       "ccMuInfoEntry": ccMuInfoEntry,
       "ccMuMac": ccMuMac,
       "ccMuWlanIndex": ccMuWlanIndex,
       "ccMuWlanName": ccMuWlanName,
       "ccMuIsDataReady": ccMuIsDataReady,
       "ccMuPortalIndex": ccMuPortalIndex,
       "ccMuPortalMac": ccMuPortalMac,
       "ccMuSymbolRogueApEna": ccMuSymbolRogueApEna,
       "ccMuIpAddr": ccMuIpAddr,
       "ccMuType": ccMuType,
       "ccMuRadioType": ccMuRadioType,
       "ccMuSupportedRates": ccMuSupportedRates,
       "ccMuPowerMode": ccMuPowerMode,
       "ccMuAuthenticationMethod": ccMuAuthenticationMethod,
       "ccMuEncryptionMethod": ccMuEncryptionMethod,
       "ccMuVlanId": ccMuVlanId,
       "ccMuStatsTable": ccMuStatsTable,
       "ccMuStatsEntry": ccMuStatsEntry,
       "ccMuTxPktsUcast": ccMuTxPktsUcast,
       "ccMuRxPktsUcast": ccMuRxPktsUcast,
       "ccMuRxPktsNUcast": ccMuRxPktsNUcast,
       "ccMuTxOctetsUcast": ccMuTxOctetsUcast,
       "ccMuRxOctetsUcast": ccMuRxOctetsUcast,
       "ccMuRxOctetsNUcast": ccMuRxOctetsNUcast,
       "ccMuRxUndecryptablePkts": ccMuRxUndecryptablePkts,
       "ccMuRxRssiNumPkts": ccMuRxRssiNumPkts,
       "ccMuRxRssiSum": ccMuRxRssiSum,
       "ccMuRxRssiSumSquares": ccMuRxRssiSumSquares,
       "ccMuRxRssiMostRecent": ccMuRxRssiMostRecent,
       "ccMuLastActivity": ccMuLastActivity,
       "ccMuRxPktsTable": ccMuRxPktsTable,
       "ccMuRxPktsEntry": ccMuRxPktsEntry,
       "ccMuRxPktsAt1Mb": ccMuRxPktsAt1Mb,
       "ccMuRxPktsAt2Mb": ccMuRxPktsAt2Mb,
       "ccMuRxPktsAt5pt5Mb": ccMuRxPktsAt5pt5Mb,
       "ccMuRxPktsAt6Mb": ccMuRxPktsAt6Mb,
       "ccMuRxPktsAt9Mb": ccMuRxPktsAt9Mb,
       "ccMuRxPktsAt11Mb": ccMuRxPktsAt11Mb,
       "ccMuRxPktsAt12Mb": ccMuRxPktsAt12Mb,
       "ccMuRxPktsAt18Mb": ccMuRxPktsAt18Mb,
       "ccMuRxPktsAt22Mb": ccMuRxPktsAt22Mb,
       "ccMuRxPktsAt24Mb": ccMuRxPktsAt24Mb,
       "ccMuRxPktsAt36Mb": ccMuRxPktsAt36Mb,
       "ccMuRxPktsAt48Mb": ccMuRxPktsAt48Mb,
       "ccMuRxPktsAt54Mb": ccMuRxPktsAt54Mb,
       "ccMuTxPktsTable": ccMuTxPktsTable,
       "ccMuTxPktsEntry": ccMuTxPktsEntry,
       "ccMuTxPktsAt1Mb": ccMuTxPktsAt1Mb,
       "ccMuTxPktsAt2Mb": ccMuTxPktsAt2Mb,
       "ccMuTxPktsAt5pt5Mb": ccMuTxPktsAt5pt5Mb,
       "ccMuTxPktsAt6Mb": ccMuTxPktsAt6Mb,
       "ccMuTxPktsAt9Mb": ccMuTxPktsAt9Mb,
       "ccMuTxPktsAt11Mb": ccMuTxPktsAt11Mb,
       "ccMuTxPktsAt12Mb": ccMuTxPktsAt12Mb,
       "ccMuTxPktsAt18Mb": ccMuTxPktsAt18Mb,
       "ccMuTxPktsAt22Mb": ccMuTxPktsAt22Mb,
       "ccMuTxPktsAt24Mb": ccMuTxPktsAt24Mb,
       "ccMuTxPktsAt36Mb": ccMuTxPktsAt36Mb,
       "ccMuTxPktsAt48Mb": ccMuTxPktsAt48Mb,
       "ccMuTxPktsAt54Mb": ccMuTxPktsAt54Mb,
       "ccMuRxOctetsTable": ccMuRxOctetsTable,
       "ccMuRxOctetsEntry": ccMuRxOctetsEntry,
       "ccMuRxOctetsAt1Mb": ccMuRxOctetsAt1Mb,
       "ccMuRxOctetsAt2Mb": ccMuRxOctetsAt2Mb,
       "ccMuRxOctetsAt5pt5Mb": ccMuRxOctetsAt5pt5Mb,
       "ccMuRxOctetsAt6Mb": ccMuRxOctetsAt6Mb,
       "ccMuRxOctetsAt9Mb": ccMuRxOctetsAt9Mb,
       "ccMuRxOctetsAt11Mb": ccMuRxOctetsAt11Mb,
       "ccMuRxOctetsAt12Mb": ccMuRxOctetsAt12Mb,
       "ccMuRxOctetsAt18Mb": ccMuRxOctetsAt18Mb,
       "ccMuRxOctetsAt22Mb": ccMuRxOctetsAt22Mb,
       "ccMuRxOctetsAt24Mb": ccMuRxOctetsAt24Mb,
       "ccMuRxOctetsAt36Mb": ccMuRxOctetsAt36Mb,
       "ccMuRxOctetsAt48Mb": ccMuRxOctetsAt48Mb,
       "ccMuRxOctetsAt54Mb": ccMuRxOctetsAt54Mb,
       "ccMuTxOctetsTable": ccMuTxOctetsTable,
       "ccMuTxOctetsEntry": ccMuTxOctetsEntry,
       "ccMuTxOctetsAt1Mb": ccMuTxOctetsAt1Mb,
       "ccMuTxOctetsAt2Mb": ccMuTxOctetsAt2Mb,
       "ccMuTxOctetsAt5pt5Mb": ccMuTxOctetsAt5pt5Mb,
       "ccMuTxOctetsAt6Mb": ccMuTxOctetsAt6Mb,
       "ccMuTxOctetsAt9Mb": ccMuTxOctetsAt9Mb,
       "ccMuTxOctetsAt11Mb": ccMuTxOctetsAt11Mb,
       "ccMuTxOctetsAt12Mb": ccMuTxOctetsAt12Mb,
       "ccMuTxOctetsAt18Mb": ccMuTxOctetsAt18Mb,
       "ccMuTxOctetsAt22Mb": ccMuTxOctetsAt22Mb,
       "ccMuTxOctetsAt24Mb": ccMuTxOctetsAt24Mb,
       "ccMuTxOctetsAt36Mb": ccMuTxOctetsAt36Mb,
       "ccMuTxOctetsAt48Mb": ccMuTxOctetsAt48Mb,
       "ccMuTxOctetsAt54Mb": ccMuTxOctetsAt54Mb,
       "ccMuTxRetriesTable": ccMuTxRetriesTable,
       "ccMuTxRetriesEntry": ccMuTxRetriesEntry,
       "ccMuTxRetriesNone": ccMuTxRetriesNone,
       "ccMuTxRetries01": ccMuTxRetries01,
       "ccMuTxRetries02": ccMuTxRetries02,
       "ccMuTxRetries03": ccMuTxRetries03,
       "ccMuTxRetries04": ccMuTxRetries04,
       "ccMuTxRetries05": ccMuTxRetries05,
       "ccMuTxRetries06": ccMuTxRetries06,
       "ccMuTxRetries07": ccMuTxRetries07,
       "ccMuTxRetries08": ccMuTxRetries08,
       "ccMuTxRetries09": ccMuTxRetries09,
       "ccMuTxRetries10": ccMuTxRetries10,
       "ccMuTxRetries11": ccMuTxRetries11,
       "ccMuTxRetries12": ccMuTxRetries12,
       "ccMuTxRetries13": ccMuTxRetries13,
       "ccMuTxRetries14": ccMuTxRetries14,
       "ccMuTxRetries15": ccMuTxRetries15,
       "ccMuTxRetriesFailed": ccMuTxRetriesFailed,
       "ccMuTxRetriesTotal": ccMuTxRetriesTotal,
       "ccMuTxRetriesMostRecent": ccMuTxRetriesMostRecent,
       "ccMuLastMac": ccMuLastMac,
       "ccMuLastReason": ccMuLastReason,
       "ccMuLastPortal": ccMuLastPortal,
       "ccMuRfSum": ccMuRfSum,
       "ccMuTxRetriesOctetsTable": ccMuTxRetriesOctetsTable,
       "ccMuTxRetriesOctetsEntry": ccMuTxRetriesOctetsEntry,
       "ccMuTxRetriesOctetsNone": ccMuTxRetriesOctetsNone,
       "ccMuTxRetriesOctets01": ccMuTxRetriesOctets01,
       "ccMuTxRetriesOctets02": ccMuTxRetriesOctets02,
       "ccMuTxRetriesOctets03": ccMuTxRetriesOctets03,
       "ccMuTxRetriesOctets04": ccMuTxRetriesOctets04,
       "ccMuTxRetriesOctets05": ccMuTxRetriesOctets05,
       "ccMuTxRetriesOctets06": ccMuTxRetriesOctets06,
       "ccMuTxRetriesOctets07": ccMuTxRetriesOctets07,
       "ccMuTxRetriesOctets08": ccMuTxRetriesOctets08,
       "ccMuTxRetriesOctets09": ccMuTxRetriesOctets09,
       "ccMuTxRetriesOctets10": ccMuTxRetriesOctets10,
       "ccMuTxRetriesOctets11": ccMuTxRetriesOctets11,
       "ccMuTxRetriesOctets12": ccMuTxRetriesOctets12,
       "ccMuTxRetriesOctets13": ccMuTxRetriesOctets13,
       "ccMuTxRetriesOctets14": ccMuTxRetriesOctets14,
       "ccMuTxRetriesOctets15": ccMuTxRetriesOctets15,
       "ccMuTxRetriesOctetsFailed": ccMuTxRetriesOctetsFailed,
       "ccMuSigStatsTable": ccMuSigStatsTable,
       "ccMuSigStatsEntry": ccMuSigStatsEntry,
       "ccMuSigStatsNumPkts": ccMuSigStatsNumPkts,
       "ccMuSigStatsSignalBest": ccMuSigStatsSignalBest,
       "ccMuSigStatsSignalWorst": ccMuSigStatsSignalWorst,
       "ccMuSigStatsSignalSum": ccMuSigStatsSignalSum,
       "ccMuSigStatsSignalSumSquares": ccMuSigStatsSignalSumSquares,
       "ccMuSigStatsSignalMostRecent": ccMuSigStatsSignalMostRecent,
       "ccMuSigStatsNoiseBest": ccMuSigStatsNoiseBest,
       "ccMuSigStatsNoiseWorst": ccMuSigStatsNoiseWorst,
       "ccMuSigStatsNoiseSum": ccMuSigStatsNoiseSum,
       "ccMuSigStatsNoiseSumSquares": ccMuSigStatsNoiseSumSquares,
       "ccMuSigStatsNoiseMostRecent": ccMuSigStatsNoiseMostRecent,
       "ccMuSigStatsSnrBest": ccMuSigStatsSnrBest,
       "ccMuSigStatsSnrWorst": ccMuSigStatsSnrWorst,
       "ccMuSigStatsSnrSum": ccMuSigStatsSnrSum,
       "ccMuSigStatsSnrSumSquares": ccMuSigStatsSnrSumSquares,
       "ccMuSigStatsSnrMostRecent": ccMuSigStatsSnrMostRecent,
       "ccMuSumStatsShortTable": ccMuSumStatsShortTable,
       "ccMuSumStatsShortEntry": ccMuSumStatsShortEntry,
       "ccMuSumStatsShortTimestamp": ccMuSumStatsShortTimestamp,
       "ccMuSumStatsShortNumPkts": ccMuSumStatsShortNumPkts,
       "ccMuSumStatsShortPktsPerSec100": ccMuSumStatsShortPktsPerSec100,
       "ccMuSumStatsShortPktsPerSecTx100": ccMuSumStatsShortPktsPerSecTx100,
       "ccMuSumStatsShortPktsPerSecRx100": ccMuSumStatsShortPktsPerSecRx100,
       "ccMuSumStatsShortThroughput": ccMuSumStatsShortThroughput,
       "ccMuSumStatsShortThroughputTx": ccMuSumStatsShortThroughputTx,
       "ccMuSumStatsShortThroughputRx": ccMuSumStatsShortThroughputRx,
       "ccMuSumStatsShortAvgBitSpeed": ccMuSumStatsShortAvgBitSpeed,
       "ccMuSumStatsShortAvgMuSignal": ccMuSumStatsShortAvgMuSignal,
       "ccMuSumStatsShortAvgMuNoise": ccMuSumStatsShortAvgMuNoise,
       "ccMuSumStatsShortAvgMuSnr": ccMuSumStatsShortAvgMuSnr,
       "ccMuSumStatsShortPp10kNUcastPkts": ccMuSumStatsShortPp10kNUcastPkts,
       "ccMuSumStatsShortPp10kTxWithRetries": ccMuSumStatsShortPp10kTxWithRetries,
       "ccMuSumStatsShortPp10kDropped": ccMuSumStatsShortPp10kDropped,
       "ccMuSumStatsShortTxAvgRetries100": ccMuSumStatsShortTxAvgRetries100,
       "ccMuSumStatsShortPp10kRxUndecrypt": ccMuSumStatsShortPp10kRxUndecrypt,
       "ccMuSumStatsLongTable": ccMuSumStatsLongTable,
       "ccMuSumStatsLongEntry": ccMuSumStatsLongEntry,
       "ccMuSumStatsLongTimestamp": ccMuSumStatsLongTimestamp,
       "ccMuSumStatsLongNumPkts": ccMuSumStatsLongNumPkts,
       "ccMuSumStatsLongPktsPerSec100": ccMuSumStatsLongPktsPerSec100,
       "ccMuSumStatsLongPktsPerSecTx100": ccMuSumStatsLongPktsPerSecTx100,
       "ccMuSumStatsLongPktsPerSecRx100": ccMuSumStatsLongPktsPerSecRx100,
       "ccMuSumStatsLongThroughput": ccMuSumStatsLongThroughput,
       "ccMuSumStatsLongThroughputTx": ccMuSumStatsLongThroughputTx,
       "ccMuSumStatsLongThroughputRx": ccMuSumStatsLongThroughputRx,
       "ccMuSumStatsLongAvgBitSpeed": ccMuSumStatsLongAvgBitSpeed,
       "ccMuSumStatsLongAvgMuSignal": ccMuSumStatsLongAvgMuSignal,
       "ccMuSumStatsLongAvgMuNoise": ccMuSumStatsLongAvgMuNoise,
       "ccMuSumStatsLongAvgMuSnr": ccMuSumStatsLongAvgMuSnr,
       "ccMuSumStatsLongPp10kNUcastPkts": ccMuSumStatsLongPp10kNUcastPkts,
       "ccMuSumStatsLongPp10kTxWithRetries": ccMuSumStatsLongPp10kTxWithRetries,
       "ccMuSumStatsLongPp10kDropped": ccMuSumStatsLongPp10kDropped,
       "ccMuSumStatsLongTxAvgRetries100": ccMuSumStatsLongTxAvgRetries100,
       "ccMuSumStatsLongPp10kRxUndecrypt": ccMuSumStatsLongPp10kRxUndecrypt,
       "ccWME": ccWME,
       "ccWMEprofileTable": ccWMEprofileTable,
       "ccWMEprofileEntry": ccWMEprofileEntry,
       "ccWMEprofileIndex": ccWMEprofileIndex,
       "ccWMEprofilename": ccWMEprofilename,
       "ccWMEprofileDesc": ccWMEprofileDesc,
       "ccWMEprofileAc1VoEcwmin": ccWMEprofileAc1VoEcwmin,
       "ccWMEprofileAc1VoEcwmax": ccWMEprofileAc1VoEcwmax,
       "ccWMEprofileAc1VoTxopLimit": ccWMEprofileAc1VoTxopLimit,
       "ccWMEprofileAc1VoAgTxopLimit": ccWMEprofileAc1VoAgTxopLimit,
       "ccWMEprofileAc1VoAifsn": ccWMEprofileAc1VoAifsn,
       "ccWMEprofileAc2ViEcwmin": ccWMEprofileAc2ViEcwmin,
       "ccWMEprofileAc2ViEcwmax": ccWMEprofileAc2ViEcwmax,
       "ccWMEprofileAc2ViTxopLimit": ccWMEprofileAc2ViTxopLimit,
       "ccWMEprofileAc2ViAgTxopLimit": ccWMEprofileAc2ViAgTxopLimit,
       "ccWMEprofileAc2ViAifsn": ccWMEprofileAc2ViAifsn,
       "ccWMEprofileAc3BeEcwmin": ccWMEprofileAc3BeEcwmin,
       "ccWMEprofileAc3BeEcwmax": ccWMEprofileAc3BeEcwmax,
       "ccWMEprofileAc3BeTxopLimit": ccWMEprofileAc3BeTxopLimit,
       "ccWMEprofileAc3BeAgTxopLimit": ccWMEprofileAc3BeAgTxopLimit,
       "ccWMEprofileAc3BeAifsn": ccWMEprofileAc3BeAifsn,
       "ccWMEprofileAc4BkEcwmin": ccWMEprofileAc4BkEcwmin,
       "ccWMEprofileAc4BkEcwmax": ccWMEprofileAc4BkEcwmax,
       "ccWMEprofileAc4BkTxopLimit": ccWMEprofileAc4BkTxopLimit,
       "ccWMEprofileAc4BkAgTxopLimit": ccWMEprofileAc4BkAgTxopLimit,
       "ccWMEprofileAc4BkAifsn": ccWMEprofileAc4BkAifsn,
       "ccWMEprofileQosParam": ccWMEprofileQosParam,
       "ccWMEprofileRowStatus": ccWMEprofileRowStatus,
       "ccPortalBeacon": ccPortalBeacon,
       "ccPortalBeaconRptTable": ccPortalBeaconRptTable,
       "ccPortalBeaconRptEntry": ccPortalBeaconRptEntry,
       "ccPortalBeaconRptPortalIndex": ccPortalBeaconRptPortalIndex,
       "ccPortalBeaconRptNumBeaconsHeard": ccPortalBeaconRptNumBeaconsHeard,
       "ccPortalBeaconRptBest": ccPortalBeaconRptBest,
       "ccPortalBeaconRptWorst": ccPortalBeaconRptWorst,
       "ccPortalBeaconRptSum": ccPortalBeaconRptSum,
       "ccPortalBeaconRptSumSquares": ccPortalBeaconRptSumSquares,
       "ccPortalBeaconRptMostRecent": ccPortalBeaconRptMostRecent,
       "ccPortalBeaconRptLastHeard": ccPortalBeaconRptLastHeard,
       "ccPortalBeaconRpFinderMac": ccPortalBeaconRpFinderMac,
       "ccPortalBeaconRpFoundMac": ccPortalBeaconRpFoundMac,
       "ccMuProbeRptTable": ccMuProbeRptTable,
       "ccMuProbeRptEntry": ccMuProbeRptEntry,
       "ccMuProbeRptSignalMostRecent": ccMuProbeRptSignalMostRecent,
       "ccMuProbeRptLastHeard": ccMuProbeRptLastHeard,
       "ccMuProbeRptFinderMac": ccMuProbeRptFinderMac,
       "ccMuProbeRptFoundMac": ccMuProbeRptFoundMac,
       "ccSensor": ccSensor,
       "ccSensorList": ccSensorList,
       "ccApList": ccApList,
       "ccSensorRevert": ccSensorRevert,
       "ccSensorConvert": ccSensorConvert,
       "ccSensorEnable": ccSensorEnable,
       "ccApSensorTable": ccApSensorTable,
       "ccApSensorEntry": ccApSensorEntry,
       "ccApSensorIndex": ccApSensorIndex,
       "ccApSensorMask": ccApSensorMask,
       "ccApSensorGateWay": ccApSensorGateWay,
       "ccApSensorPrimary": ccApSensorPrimary,
       "ccApSensorSecondary": ccApSensorSecondary,
       "ccApSensorDhcp": ccApSensorDhcp,
       "ccApSensorIpaddress": ccApSensorIpaddress,
       "ccApSensorMac": ccApSensorMac,
       "ccV2dot0Groups": ccV2dot0Groups,
       "v2dot0Group": v2dot0Group,
       "v2dot0NotificationGroup": v2dot0NotificationGroup,
       "v2dot0GroupOfDepricated": v2dot0GroupOfDepricated,
       "v2dot1Group": v2dot1Group,
       "v2dot1NotificationGroup": v2dot1NotificationGroup,
       "v2dot1StatsGroup": v2dot1StatsGroup,
       "v2dot0GroupOfDeprecated": v2dot0GroupOfDeprecated}
)
