# SNMP MIB module (ENTERASYS-MGMD-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-MGMD-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:37 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysMgmdExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71)
)
if mibBuilder.loadTexts:
    etsysMgmdExtMIB.setRevisions(
        ("2013-08-08 17:28",
         "2013-04-24 12:50",
         "2012-04-25 13:32",
         "2010-02-08 14:08")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MGMDNumGroupsTc(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("minimum", 2),
          ("default", 3),
          ("maximum", 4))
    )



class MGMDPortModeTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reporter", 1),
          ("source", 2))
    )



class MGMDDiscoveredRouterModeTc(TextualConvention, Integer32):
    status = "current"
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
        *(("querier", 1),
          ("routingProtocol", 2),
          ("multicastRouterDiscovery", 3),
          ("staticallyConfigured", 4))
    )



class MGMDProtocolClassTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicastData", 1),
          ("routingProtocol", 2),
          ("ignore", 3))
    )



class MGMDProtocolIdTc(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("hopopt", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ggp", 3),
          ("ip", 4),
          ("st", 5),
          ("tcp", 6),
          ("cbt", 7),
          ("egp", 8),
          ("igp", 9),
          ("bbnRccMon", 10),
          ("nvpII", 11),
          ("pup", 12),
          ("argus", 13),
          ("emcon", 14),
          ("xnet", 15),
          ("chaos", 16),
          ("udp", 17),
          ("mux", 18),
          ("dcnMeas", 19),
          ("hmp", 20),
          ("prm", 21),
          ("xnsIdp", 22),
          ("trunk1", 23),
          ("trunk2", 24),
          ("leaf1", 25),
          ("leaf2", 26),
          ("rdp", 27),
          ("irtp", 28),
          ("isoTp4", 29),
          ("netblt", 30),
          ("mfeNsp", 31),
          ("meritInp", 32),
          ("sep", 33),
          ("x3pc", 34),
          ("idpr", 35),
          ("xtp", 36),
          ("ddp", 37),
          ("idprCmtp", 38),
          ("tpPlusPlus", 39),
          ("il", 40),
          ("ipv6", 41),
          ("sdrp", 42),
          ("ipv6Route", 43),
          ("ipv6Frag", 44),
          ("idrp", 45),
          ("rsvp", 46),
          ("gre", 47),
          ("mhrp", 48),
          ("bna", 49),
          ("esp", 50),
          ("ah", 51),
          ("inlsp", 52),
          ("swipe", 53),
          ("narp", 54),
          ("mobile", 55),
          ("tlsp", 56),
          ("skip", 57),
          ("ipv6Icmp", 58),
          ("ipv6NoNxt", 59),
          ("ipv6Opts", 60),
          ("ipProt61", 61),
          ("cftp", 62),
          ("ipProt63", 63),
          ("satExpak", 64),
          ("kryptolan", 65),
          ("rvd", 66),
          ("ippc", 67),
          ("ipProt64", 68),
          ("satMon", 69),
          ("visa", 70),
          ("ipcv", 71),
          ("cpnx", 72),
          ("cphb", 73),
          ("wsn", 74),
          ("pvp", 75),
          ("brSatMon", 76),
          ("sunNd", 77),
          ("wbMon", 78),
          ("wbExpak", 79),
          ("isoIp", 80),
          ("vmtp", 81),
          ("secureVmtp", 82),
          ("vines", 83),
          ("ttp", 84),
          ("nsfnetIgp", 85),
          ("dgp", 86),
          ("tcf", 87),
          ("eigrp", 88),
          ("ospfIgp", 89),
          ("spriteRpc", 90),
          ("larp", 91),
          ("mtp", 92),
          ("ax25", 93),
          ("ipip", 94),
          ("micp", 95),
          ("sccSp", 96),
          ("etherIp", 97),
          ("encap", 98),
          ("ipProt99", 99),
          ("gmtp", 100),
          ("ifmp", 101),
          ("pnni", 102),
          ("pim", 103),
          ("aris", 104),
          ("scps", 105),
          ("qnx", 106),
          ("an", 107),
          ("ipComp", 108),
          ("snp", 109),
          ("compaqPeer", 110),
          ("ipxInIp", 111),
          ("vrrp", 112),
          ("pgm", 113),
          ("ipProt114", 114),
          ("l2tp", 115),
          ("ddx", 116),
          ("iatp", 117),
          ("stp", 118),
          ("srp", 119),
          ("uti", 120),
          ("smp", 121),
          ("sm", 122),
          ("ptp", 123),
          ("isisIpv4", 124),
          ("fire", 125),
          ("crtp", 126),
          ("crudp", 127),
          ("sscopmce", 128),
          ("iplt", 129),
          ("sps", 130),
          ("pipe", 131),
          ("sctp", 132),
          ("fc", 133),
          ("rsvpE2eIgn", 134),
          ("mobHeader", 135),
          ("udpLite", 136),
          ("mpls", 137),
          ("ipProto138", 138),
          ("ipProto139", 139),
          ("ipProto140", 140),
          ("ipProto141", 141),
          ("ipProto142", 142),
          ("ipProto143", 143),
          ("ipProto144", 144),
          ("ipProto145", 145),
          ("ipProto146", 146),
          ("ipProto147", 147),
          ("ipProto148", 148),
          ("ipProto149", 149),
          ("ipProto150", 150),
          ("ipProto151", 151),
          ("ipProto152", 152),
          ("ipProto153", 153),
          ("ipProto154", 154),
          ("ipProto155", 155),
          ("ipProto156", 156),
          ("ipProto157", 157),
          ("ipProto158", 158),
          ("ipProto159", 159),
          ("ipProto160", 160),
          ("ipProto161", 161),
          ("ipProto162", 162),
          ("ipProto163", 163),
          ("ipProto164", 164),
          ("ipProto165", 165),
          ("ipProto166", 166),
          ("ipProto167", 167),
          ("ipProto168", 168),
          ("ipProto169", 169),
          ("ipProto170", 170),
          ("ipProto171", 171),
          ("ipProto172", 172),
          ("ipProto173", 173),
          ("ipProto174", 174),
          ("ipProto175", 175),
          ("ipProto176", 176),
          ("ipProto177", 177),
          ("ipProto178", 178),
          ("ipProto179", 179),
          ("ipProto180", 180),
          ("ipProto181", 181),
          ("ipProto182", 182),
          ("ipProto183", 183),
          ("ipProto184", 184),
          ("ipProto185", 185),
          ("ipProto186", 186),
          ("ipProto187", 187),
          ("ipProto188", 188),
          ("ipProto189", 189),
          ("ipProto190", 190),
          ("ipProto191", 191),
          ("ipProto192", 192),
          ("ipProto193", 193),
          ("ipProto194", 194),
          ("ipProto195", 195),
          ("ipProto196", 196),
          ("ipProto197", 197),
          ("ipProto198", 198),
          ("ipProto199", 199),
          ("ipProto200", 200),
          ("ipProto201", 201),
          ("ipProto202", 202),
          ("ipProto203", 203),
          ("ipProto204", 204),
          ("ipProto205", 205),
          ("ipProto206", 206),
          ("ipProto207", 207),
          ("ipProto208", 208),
          ("ipProto209", 209),
          ("ipProto210", 210),
          ("ipProto211", 211),
          ("ipProto212", 212),
          ("ipProto213", 213),
          ("ipProto214", 214),
          ("ipProto215", 215),
          ("ipProto216", 216),
          ("ipProto217", 217),
          ("ipProto218", 218),
          ("ipProto219", 219),
          ("ipProto220", 220),
          ("ipProto221", 221),
          ("ipProto222", 222),
          ("ipProto223", 223),
          ("ipProto224", 224),
          ("ipProto225", 225),
          ("ipProto226", 226),
          ("ipProto227", 227),
          ("ipProto228", 228),
          ("ipProto229", 229),
          ("ipProto230", 230),
          ("ipProto231", 231),
          ("ipProto232", 232),
          ("ipProto233", 233),
          ("ipProto234", 234),
          ("ipProto235", 235),
          ("ipProto236", 236),
          ("ipProto237", 237),
          ("ipProto238", 238),
          ("ipProto239", 239),
          ("ipProto240", 240),
          ("ipProto241", 241),
          ("ipProto242", 242),
          ("ipProto243", 243),
          ("ipProto244", 244),
          ("ipProto245", 245),
          ("ipProto246", 246),
          ("ipProto247", 247),
          ("ipProto248", 248),
          ("ipProto249", 249),
          ("ipProto250", 250),
          ("ipProto251", 251),
          ("ipProto252", 252),
          ("ipProto253", 253),
          ("ipProto254", 254),
          ("ipProto255", 255))
    )


class MGMDInputFilterFlowActionsTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("flood", 2),
          ("allow", 3))
    )



class MGMDInputFilterProtocolActionsTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysMgmdExtObjects_ObjectIdentity = ObjectIdentity
etsysMgmdExtObjects = _EtsysMgmdExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1)
)
_EtsysMgmdExtConfigGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtConfigGroup = _EtsysMgmdExtConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1)
)
_EtsysMgmdExtConfigRevString_Type = SnmpAdminString
_EtsysMgmdExtConfigRevString_Object = MibScalar
etsysMgmdExtConfigRevString = _EtsysMgmdExtConfigRevString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 1),
    _EtsysMgmdExtConfigRevString_Type()
)
etsysMgmdExtConfigRevString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigRevString.setStatus("current")


class _EtsysMgmdExtConfigFullAction_Type(Integer32):
    """Custom type etsysMgmdExtConfigFullAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routers", 1),
          ("flood", 2))
    )


_EtsysMgmdExtConfigFullAction_Type.__name__ = "Integer32"
_EtsysMgmdExtConfigFullAction_Object = MibScalar
etsysMgmdExtConfigFullAction = _EtsysMgmdExtConfigFullAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 2),
    _EtsysMgmdExtConfigFullAction_Type()
)
etsysMgmdExtConfigFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigFullAction.setStatus("current")
_EtsysMgmdExtConfigMinNumberOfGroups_Type = Integer32
_EtsysMgmdExtConfigMinNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigMinNumberOfGroups = _EtsysMgmdExtConfigMinNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 3),
    _EtsysMgmdExtConfigMinNumberOfGroups_Type()
)
etsysMgmdExtConfigMinNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigMinNumberOfGroups.setStatus("current")
_EtsysMgmdExtConfigDefaultNumberOfGroups_Type = Integer32
_EtsysMgmdExtConfigDefaultNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigDefaultNumberOfGroups = _EtsysMgmdExtConfigDefaultNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 4),
    _EtsysMgmdExtConfigDefaultNumberOfGroups_Type()
)
etsysMgmdExtConfigDefaultNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigDefaultNumberOfGroups.setStatus("current")
_EtsysMgmdExtConfigMaxNumberOfGroups_Type = Integer32
_EtsysMgmdExtConfigMaxNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigMaxNumberOfGroups = _EtsysMgmdExtConfigMaxNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 5),
    _EtsysMgmdExtConfigMaxNumberOfGroups_Type()
)
etsysMgmdExtConfigMaxNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigMaxNumberOfGroups.setStatus("current")


class _EtsysMgmdExtConfigNumberOfGroups_Type(MGMDNumGroupsTc):
    """Custom type etsysMgmdExtConfigNumberOfGroups based on MGMDNumGroupsTc"""
    defaultValue = 3


_EtsysMgmdExtConfigNumberOfGroups_Type.__name__ = "MGMDNumGroupsTc"
_EtsysMgmdExtConfigNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigNumberOfGroups = _EtsysMgmdExtConfigNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 6),
    _EtsysMgmdExtConfigNumberOfGroups_Type()
)
etsysMgmdExtConfigNumberOfGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigNumberOfGroups.setStatus("current")


class _EtsysMgmdExtConfigUnknownInputAction_Type(Integer32):
    """Custom type etsysMgmdExtConfigUnknownInputAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("routers", 1),
          ("flood", 2),
          ("discard", 3))
    )


_EtsysMgmdExtConfigUnknownInputAction_Type.__name__ = "Integer32"
_EtsysMgmdExtConfigUnknownInputAction_Object = MibScalar
etsysMgmdExtConfigUnknownInputAction = _EtsysMgmdExtConfigUnknownInputAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 7),
    _EtsysMgmdExtConfigUnknownInputAction_Type()
)
etsysMgmdExtConfigUnknownInputAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigUnknownInputAction.setStatus("current")


class _EtsysMgmdExtConfigFlowWaitEnable_Type(EnabledStatus):
    """Custom type etsysMgmdExtConfigFlowWaitEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysMgmdExtConfigFlowWaitEnable_Type.__name__ = "EnabledStatus"
_EtsysMgmdExtConfigFlowWaitEnable_Object = MibScalar
etsysMgmdExtConfigFlowWaitEnable = _EtsysMgmdExtConfigFlowWaitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 8),
    _EtsysMgmdExtConfigFlowWaitEnable_Type()
)
etsysMgmdExtConfigFlowWaitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigFlowWaitEnable.setStatus("current")


class _EtsysMgmdExtConfigFlowWaitTime_Type(Integer32):
    """Custom type etsysMgmdExtConfigFlowWaitTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_EtsysMgmdExtConfigFlowWaitTime_Type.__name__ = "Integer32"
_EtsysMgmdExtConfigFlowWaitTime_Object = MibScalar
etsysMgmdExtConfigFlowWaitTime = _EtsysMgmdExtConfigFlowWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 9),
    _EtsysMgmdExtConfigFlowWaitTime_Type()
)
etsysMgmdExtConfigFlowWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigFlowWaitTime.setStatus("current")
_EtsysMgmdExtInterfaceGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtInterfaceGroup = _EtsysMgmdExtInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2)
)
_EtsysMgmdExtInterfaceTable_Object = MibTable
etsysMgmdExtInterfaceTable = _EtsysMgmdExtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceTable.setStatus("current")
_EtsysMgmdExtInterfaceEntry_Object = MibTableRow
etsysMgmdExtInterfaceEntry = _EtsysMgmdExtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1)
)
etsysMgmdExtInterfaceEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceApplication"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceEntry.setStatus("current")
_EtsysMgmdExtInterfaceApplication_Type = InetAddressType
_EtsysMgmdExtInterfaceApplication_Object = MibTableColumn
etsysMgmdExtInterfaceApplication = _EtsysMgmdExtInterfaceApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 1),
    _EtsysMgmdExtInterfaceApplication_Type()
)
etsysMgmdExtInterfaceApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceApplication.setStatus("current")


class _EtsysMgmdExtInterfaceQueryEnableState_Type(EnabledStatus):
    """Custom type etsysMgmdExtInterfaceQueryEnableState based on EnabledStatus"""
    defaultValue = 2


_EtsysMgmdExtInterfaceQueryEnableState_Type.__name__ = "EnabledStatus"
_EtsysMgmdExtInterfaceQueryEnableState_Object = MibTableColumn
etsysMgmdExtInterfaceQueryEnableState = _EtsysMgmdExtInterfaceQueryEnableState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 2),
    _EtsysMgmdExtInterfaceQueryEnableState_Type()
)
etsysMgmdExtInterfaceQueryEnableState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceQueryEnableState.setStatus("current")


class _EtsysMgmdExtInterfaceFastLeaveState_Type(EnabledStatus):
    """Custom type etsysMgmdExtInterfaceFastLeaveState based on EnabledStatus"""
    defaultValue = 2


_EtsysMgmdExtInterfaceFastLeaveState_Type.__name__ = "EnabledStatus"
_EtsysMgmdExtInterfaceFastLeaveState_Object = MibTableColumn
etsysMgmdExtInterfaceFastLeaveState = _EtsysMgmdExtInterfaceFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 3),
    _EtsysMgmdExtInterfaceFastLeaveState_Type()
)
etsysMgmdExtInterfaceFastLeaveState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceFastLeaveState.setStatus("current")
_EtsysMgmdExtInterfaceClearGroups_Type = TruthValue
_EtsysMgmdExtInterfaceClearGroups_Object = MibTableColumn
etsysMgmdExtInterfaceClearGroups = _EtsysMgmdExtInterfaceClearGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 4),
    _EtsysMgmdExtInterfaceClearGroups_Type()
)
etsysMgmdExtInterfaceClearGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceClearGroups.setStatus("current")


class _EtsysMgmdExtRtrAlertRequired_Type(TruthValue):
    """Custom type etsysMgmdExtRtrAlertRequired based on TruthValue"""
    defaultValue = 1


_EtsysMgmdExtRtrAlertRequired_Type.__name__ = "TruthValue"
_EtsysMgmdExtRtrAlertRequired_Object = MibTableColumn
etsysMgmdExtRtrAlertRequired = _EtsysMgmdExtRtrAlertRequired_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 5),
    _EtsysMgmdExtRtrAlertRequired_Type()
)
etsysMgmdExtRtrAlertRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtRtrAlertRequired.setStatus("current")
_EtsysMgmdExtInterfaceFilterId_Type = Integer32
_EtsysMgmdExtInterfaceFilterId_Object = MibTableColumn
etsysMgmdExtInterfaceFilterId = _EtsysMgmdExtInterfaceFilterId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 6),
    _EtsysMgmdExtInterfaceFilterId_Type()
)
etsysMgmdExtInterfaceFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceFilterId.setStatus("current")


class _EtsysMgmdExtInterfaceFilterIdEnable_Type(EnabledStatus):
    """Custom type etsysMgmdExtInterfaceFilterIdEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysMgmdExtInterfaceFilterIdEnable_Type.__name__ = "EnabledStatus"
_EtsysMgmdExtInterfaceFilterIdEnable_Object = MibTableColumn
etsysMgmdExtInterfaceFilterIdEnable = _EtsysMgmdExtInterfaceFilterIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 7),
    _EtsysMgmdExtInterfaceFilterIdEnable_Type()
)
etsysMgmdExtInterfaceFilterIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceFilterIdEnable.setStatus("current")
_EtsysMgmdExtStaticCacheGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtStaticCacheGroup = _EtsysMgmdExtStaticCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3)
)
_EtsysMgmdExtStaticCacheTable_Object = MibTable
etsysMgmdExtStaticCacheTable = _EtsysMgmdExtStaticCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheTable.setStatus("current")
_EtsysMgmdExtStaticCacheEntry_Object = MibTableRow
etsysMgmdExtStaticCacheEntry = _EtsysMgmdExtStaticCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1)
)
etsysMgmdExtStaticCacheEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIPAddrType"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheGroupIPAddress"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheSourceIPAddress"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheEntry.setStatus("current")
_EtsysMgmdExtStaticCacheIPAddrType_Type = InetAddressType
_EtsysMgmdExtStaticCacheIPAddrType_Object = MibTableColumn
etsysMgmdExtStaticCacheIPAddrType = _EtsysMgmdExtStaticCacheIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 1),
    _EtsysMgmdExtStaticCacheIPAddrType_Type()
)
etsysMgmdExtStaticCacheIPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheIPAddrType.setStatus("current")


class _EtsysMgmdExtStaticCacheGroupIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtStaticCacheGroupIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtStaticCacheGroupIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtStaticCacheGroupIPAddress_Object = MibTableColumn
etsysMgmdExtStaticCacheGroupIPAddress = _EtsysMgmdExtStaticCacheGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 2),
    _EtsysMgmdExtStaticCacheGroupIPAddress_Type()
)
etsysMgmdExtStaticCacheGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheGroupIPAddress.setStatus("current")


class _EtsysMgmdExtStaticCacheSourceIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtStaticCacheSourceIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtStaticCacheSourceIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtStaticCacheSourceIPAddress_Object = MibTableColumn
etsysMgmdExtStaticCacheSourceIPAddress = _EtsysMgmdExtStaticCacheSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 3),
    _EtsysMgmdExtStaticCacheSourceIPAddress_Type()
)
etsysMgmdExtStaticCacheSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheSourceIPAddress.setStatus("current")
_EtsysMgmdExtStaticCacheIncludeList_Type = PortList
_EtsysMgmdExtStaticCacheIncludeList_Object = MibTableColumn
etsysMgmdExtStaticCacheIncludeList = _EtsysMgmdExtStaticCacheIncludeList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 4),
    _EtsysMgmdExtStaticCacheIncludeList_Type()
)
etsysMgmdExtStaticCacheIncludeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheIncludeList.setStatus("current")
_EtsysMgmdExtStaticCacheExcludeList_Type = PortList
_EtsysMgmdExtStaticCacheExcludeList_Object = MibTableColumn
etsysMgmdExtStaticCacheExcludeList = _EtsysMgmdExtStaticCacheExcludeList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 5),
    _EtsysMgmdExtStaticCacheExcludeList_Type()
)
etsysMgmdExtStaticCacheExcludeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheExcludeList.setStatus("current")
_EtsysMgmdExtStaticCacheRowStatus_Type = RowStatus
_EtsysMgmdExtStaticCacheRowStatus_Object = MibTableColumn
etsysMgmdExtStaticCacheRowStatus = _EtsysMgmdExtStaticCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 6),
    _EtsysMgmdExtStaticCacheRowStatus_Type()
)
etsysMgmdExtStaticCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheRowStatus.setStatus("current")
_EtsysMgmdExtCacheGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtCacheGroup = _EtsysMgmdExtCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4)
)
_EtsysMgmdExtCacheTable_Object = MibTable
etsysMgmdExtCacheTable = _EtsysMgmdExtCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtCacheTable.setStatus("current")
_EtsysMgmdExtCacheEntry_Object = MibTableRow
etsysMgmdExtCacheEntry = _EtsysMgmdExtCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1)
)
etsysMgmdExtCacheEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIPAddrType"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheGroupIPAddress"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSourceIPAddress"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtCacheEntry.setStatus("current")
_EtsysMgmdExtCacheIPAddrType_Type = InetAddressType
_EtsysMgmdExtCacheIPAddrType_Object = MibTableColumn
etsysMgmdExtCacheIPAddrType = _EtsysMgmdExtCacheIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 1),
    _EtsysMgmdExtCacheIPAddrType_Type()
)
etsysMgmdExtCacheIPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheIPAddrType.setStatus("current")


class _EtsysMgmdExtCacheGroupIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtCacheGroupIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtCacheGroupIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtCacheGroupIPAddress_Object = MibTableColumn
etsysMgmdExtCacheGroupIPAddress = _EtsysMgmdExtCacheGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 2),
    _EtsysMgmdExtCacheGroupIPAddress_Type()
)
etsysMgmdExtCacheGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheGroupIPAddress.setStatus("current")


class _EtsysMgmdExtCacheSourceIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtCacheSourceIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtCacheSourceIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtCacheSourceIPAddress_Object = MibTableColumn
etsysMgmdExtCacheSourceIPAddress = _EtsysMgmdExtCacheSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 3),
    _EtsysMgmdExtCacheSourceIPAddress_Type()
)
etsysMgmdExtCacheSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheSourceIPAddress.setStatus("current")
_EtsysMgmdExtCacheExpiryTime_Type = Integer32
_EtsysMgmdExtCacheExpiryTime_Object = MibTableColumn
etsysMgmdExtCacheExpiryTime = _EtsysMgmdExtCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 4),
    _EtsysMgmdExtCacheExpiryTime_Type()
)
etsysMgmdExtCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheExpiryTime.setUnits("seconds")
_EtsysMgmdExtCacheIncludePortList_Type = PortList
_EtsysMgmdExtCacheIncludePortList_Object = MibTableColumn
etsysMgmdExtCacheIncludePortList = _EtsysMgmdExtCacheIncludePortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 5),
    _EtsysMgmdExtCacheIncludePortList_Type()
)
etsysMgmdExtCacheIncludePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheIncludePortList.setStatus("current")
_EtsysMgmdExtCacheExcludePortList_Type = PortList
_EtsysMgmdExtCacheExcludePortList_Object = MibTableColumn
etsysMgmdExtCacheExcludePortList = _EtsysMgmdExtCacheExcludePortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 6),
    _EtsysMgmdExtCacheExcludePortList_Type()
)
etsysMgmdExtCacheExcludePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheExcludePortList.setStatus("current")


class _EtsysMgmdExtCacheSrcPort_Type(Integer32):
    """Custom type etsysMgmdExtCacheSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysMgmdExtCacheSrcPort_Type.__name__ = "Integer32"
_EtsysMgmdExtCacheSrcPort_Object = MibTableColumn
etsysMgmdExtCacheSrcPort = _EtsysMgmdExtCacheSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 7),
    _EtsysMgmdExtCacheSrcPort_Type()
)
etsysMgmdExtCacheSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheSrcPort.setStatus("current")
_EtsysMgmdExtDiscoveredRouterGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtDiscoveredRouterGroup = _EtsysMgmdExtDiscoveredRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5)
)
_EtsysMgmdExtDiscoveredRouterTable_Object = MibTable
etsysMgmdExtDiscoveredRouterTable = _EtsysMgmdExtDiscoveredRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterTable.setStatus("current")
_EtsysMgmdExtDiscoveredRouterEntry_Object = MibTableRow
etsysMgmdExtDiscoveredRouterEntry = _EtsysMgmdExtDiscoveredRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1)
)
etsysMgmdExtDiscoveredRouterEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterApplication"),
    (0, "IF-MIB", "ifIndex"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterEntry.setStatus("current")
_EtsysMgmdExtDiscoveredRouterApplication_Type = InetAddressType
_EtsysMgmdExtDiscoveredRouterApplication_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterApplication = _EtsysMgmdExtDiscoveredRouterApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 1),
    _EtsysMgmdExtDiscoveredRouterApplication_Type()
)
etsysMgmdExtDiscoveredRouterApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterApplication.setStatus("current")
_EtsysMgmdExtDiscoveredRouterLearnedMethod_Type = MGMDDiscoveredRouterModeTc
_EtsysMgmdExtDiscoveredRouterLearnedMethod_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterLearnedMethod = _EtsysMgmdExtDiscoveredRouterLearnedMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 2),
    _EtsysMgmdExtDiscoveredRouterLearnedMethod_Type()
)
etsysMgmdExtDiscoveredRouterLearnedMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterLearnedMethod.setStatus("current")
_EtsysMgmdExtDiscoveredRouterEgressing_Type = TruthValue
_EtsysMgmdExtDiscoveredRouterEgressing_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterEgressing = _EtsysMgmdExtDiscoveredRouterEgressing_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 3),
    _EtsysMgmdExtDiscoveredRouterEgressing_Type()
)
etsysMgmdExtDiscoveredRouterEgressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterEgressing.setStatus("current")


class _EtsysMgmdExtDiscoveredRouterStaticPortList_Type(EnabledStatus):
    """Custom type etsysMgmdExtDiscoveredRouterStaticPortList based on EnabledStatus"""
    defaultValue = 2


_EtsysMgmdExtDiscoveredRouterStaticPortList_Type.__name__ = "EnabledStatus"
_EtsysMgmdExtDiscoveredRouterStaticPortList_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterStaticPortList = _EtsysMgmdExtDiscoveredRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 4),
    _EtsysMgmdExtDiscoveredRouterStaticPortList_Type()
)
etsysMgmdExtDiscoveredRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterStaticPortList.setStatus("current")
_EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Type = TimeTicks
_EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterBridgePortAgeTime = _EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 5),
    _EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Type()
)
etsysMgmdExtDiscoveredRouterBridgePortAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterBridgePortAgeTime.setStatus("current")
_EtsysMgmdExtPortGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtPortGroup = _EtsysMgmdExtPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6)
)
_EtsysMgmdExtPortTable_Object = MibTable
etsysMgmdExtPortTable = _EtsysMgmdExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortTable.setStatus("current")
_EtsysMgmdExtPortTableEntry_Object = MibTableRow
etsysMgmdExtPortTableEntry = _EtsysMgmdExtPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1)
)
etsysMgmdExtPortTableEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortMode"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortIPAddressType"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableGroupIPAddress"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableSourceIPAddress"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableEntry.setStatus("current")
_EtsysMgmdExtPortMode_Type = MGMDPortModeTc
_EtsysMgmdExtPortMode_Object = MibTableColumn
etsysMgmdExtPortMode = _EtsysMgmdExtPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 1),
    _EtsysMgmdExtPortMode_Type()
)
etsysMgmdExtPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortMode.setStatus("current")
_EtsysMgmdExtPortIPAddressType_Type = InetAddressType
_EtsysMgmdExtPortIPAddressType_Object = MibTableColumn
etsysMgmdExtPortIPAddressType = _EtsysMgmdExtPortIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 2),
    _EtsysMgmdExtPortIPAddressType_Type()
)
etsysMgmdExtPortIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortIPAddressType.setStatus("current")


class _EtsysMgmdExtPortTableGroupIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtPortTableGroupIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtPortTableGroupIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtPortTableGroupIPAddress_Object = MibTableColumn
etsysMgmdExtPortTableGroupIPAddress = _EtsysMgmdExtPortTableGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 3),
    _EtsysMgmdExtPortTableGroupIPAddress_Type()
)
etsysMgmdExtPortTableGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableGroupIPAddress.setStatus("current")


class _EtsysMgmdExtPortTableSourceIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtPortTableSourceIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtPortTableSourceIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtPortTableSourceIPAddress_Object = MibTableColumn
etsysMgmdExtPortTableSourceIPAddress = _EtsysMgmdExtPortTableSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 4),
    _EtsysMgmdExtPortTableSourceIPAddress_Type()
)
etsysMgmdExtPortTableSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableSourceIPAddress.setStatus("current")
_EtsysMgmdExtPortTableExpireTime_Type = Integer32
_EtsysMgmdExtPortTableExpireTime_Object = MibTableColumn
etsysMgmdExtPortTableExpireTime = _EtsysMgmdExtPortTableExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 5),
    _EtsysMgmdExtPortTableExpireTime_Type()
)
etsysMgmdExtPortTableExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableExpireTime.setUnits("seconds")
_EtsysMgmdExtPortFastLeaveGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtPortFastLeaveGroup = _EtsysMgmdExtPortFastLeaveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7)
)
_EtsysMgmdExtPortFastLeaveTable_Object = MibTable
etsysMgmdExtPortFastLeaveTable = _EtsysMgmdExtPortFastLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveTable.setStatus("current")
_EtsysMgmdExtPortFastLeaveTableEntry_Object = MibTableRow
etsysMgmdExtPortFastLeaveTableEntry = _EtsysMgmdExtPortFastLeaveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7, 1, 1)
)
etsysMgmdExtPortFastLeaveTableEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveTableEntry.setStatus("current")


class _EtsysMgmdExtPortFastLeaveState_Type(EnabledStatus):
    """Custom type etsysMgmdExtPortFastLeaveState based on EnabledStatus"""
    defaultValue = 2


_EtsysMgmdExtPortFastLeaveState_Type.__name__ = "EnabledStatus"
_EtsysMgmdExtPortFastLeaveState_Object = MibTableColumn
etsysMgmdExtPortFastLeaveState = _EtsysMgmdExtPortFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7, 1, 1, 1),
    _EtsysMgmdExtPortFastLeaveState_Type()
)
etsysMgmdExtPortFastLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveState.setStatus("current")
_EtsysMgmdExtStatsCntrsGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtStatsCntrsGroup = _EtsysMgmdExtStatsCntrsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8)
)
_EtsysMgmdExtStatsCntrsTable_Object = MibTable
etsysMgmdExtStatsCntrsTable = _EtsysMgmdExtStatsCntrsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsTable.setStatus("current")
_EtsysMgmdExtStatsCntrsEntry_Object = MibTableRow
etsysMgmdExtStatsCntrsEntry = _EtsysMgmdExtStatsCntrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1)
)
etsysMgmdExtStatsCntrsEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsApplication"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsEntry.setStatus("current")
_EtsysMgmdExtStatsCntrsApplication_Type = InetAddressType
_EtsysMgmdExtStatsCntrsApplication_Object = MibTableColumn
etsysMgmdExtStatsCntrsApplication = _EtsysMgmdExtStatsCntrsApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 1),
    _EtsysMgmdExtStatsCntrsApplication_Type()
)
etsysMgmdExtStatsCntrsApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsApplication.setStatus("current")
_EtsysMgmdExtStatsCntrsGroupFull_Type = TruthValue
_EtsysMgmdExtStatsCntrsGroupFull_Object = MibTableColumn
etsysMgmdExtStatsCntrsGroupFull = _EtsysMgmdExtStatsCntrsGroupFull_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 2),
    _EtsysMgmdExtStatsCntrsGroupFull_Type()
)
etsysMgmdExtStatsCntrsGroupFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsGroupFull.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV1QueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV1QueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV1QueriesSent = _EtsysMgmdExtStatsCntrsNumV1QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 3),
    _EtsysMgmdExtStatsCntrsNumV1QueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumV1QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV1QueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV2QueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV2QueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV2QueriesSent = _EtsysMgmdExtStatsCntrsNumV2QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 4),
    _EtsysMgmdExtStatsCntrsNumV2QueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumV2QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV2QueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV3QueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV3QueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV3QueriesSent = _EtsysMgmdExtStatsCntrsNumV3QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 5),
    _EtsysMgmdExtStatsCntrsNumV3QueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumV3QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV3QueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGSQueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGSQueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGSQueriesSent = _EtsysMgmdExtStatsCntrsNumGSQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 6),
    _EtsysMgmdExtStatsCntrsNumGSQueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumGSQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGSQueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGAndSQueriesSent = _EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 7),
    _EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumGAndSQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGAndSQueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV1QueriesRcvd = _EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 8),
    _EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV1QueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV1QueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV2QueriesRcvd = _EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 9),
    _EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV2QueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV2QueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV3QueriesRcvd = _EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 10),
    _EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV3QueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV3QueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGSQueriesRcvd = _EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 11),
    _EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumGSQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGSQueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd = _EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 12),
    _EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd = _EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 13),
    _EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV1ReportsRcvd = _EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 14),
    _EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV1ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV1ReportsRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV2ReportsRcvd = _EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 15),
    _EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV2ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV2ReportsRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV3ReportsRcvd = _EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 16),
    _EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV3ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV3ReportsRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumLeavesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumLeavesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumLeavesRcvd = _EtsysMgmdExtStatsCntrsNumLeavesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 17),
    _EtsysMgmdExtStatsCntrsNumLeavesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumLeavesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumLeavesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumBadFramesRcvd = _EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 18),
    _EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumBadFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumBadFramesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsClear_Type = TruthValue
_EtsysMgmdExtStatsCntrsClear_Object = MibTableColumn
etsysMgmdExtStatsCntrsClear = _EtsysMgmdExtStatsCntrsClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 19),
    _EtsysMgmdExtStatsCntrsClear_Type()
)
etsysMgmdExtStatsCntrsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsClear.setStatus("current")
_EtsysMgmdExtStatsCntrsNumCurrentStateRecRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumCurrentStateRecRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumCurrentStateRecRcvd = _EtsysMgmdExtStatsCntrsNumCurrentStateRecRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 20),
    _EtsysMgmdExtStatsCntrsNumCurrentStateRecRcvd_Type()
)
etsysMgmdExtStatsCntrsNumCurrentStateRecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumCurrentStateRecRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd = _EtsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 21),
    _EtsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd_Type()
)
etsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumSrcListChgRecRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumSrcListChgRecRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumSrcListChgRecRcvd = _EtsysMgmdExtStatsCntrsNumSrcListChgRecRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 22),
    _EtsysMgmdExtStatsCntrsNumSrcListChgRecRcvd_Type()
)
etsysMgmdExtStatsCntrsNumSrcListChgRecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumSrcListChgRecRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP = _EtsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 23),
    _EtsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP_Type()
)
etsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToBeingDisabled_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToBeingDisabled_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToBeingDisabled = _EtsysMgmdExtStatsCntrsDropsDueToBeingDisabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 24),
    _EtsysMgmdExtStatsCntrsDropsDueToBeingDisabled_Type()
)
etsysMgmdExtStatsCntrsDropsDueToBeingDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToBeingDisabled.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToBadHdrLength_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToBadHdrLength_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToBadHdrLength = _EtsysMgmdExtStatsCntrsDropsDueToBadHdrLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 25),
    _EtsysMgmdExtStatsCntrsDropsDueToBadHdrLength_Type()
)
etsysMgmdExtStatsCntrsDropsDueToBadHdrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToBadHdrLength.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm = _EtsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 26),
    _EtsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm_Type()
)
etsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm = _EtsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 27),
    _EtsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm_Type()
)
etsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert = _EtsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 28),
    _EtsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert_Type()
)
etsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP = _EtsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 29),
    _EtsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP_Type()
)
etsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery = _EtsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 30),
    _EtsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery_Type()
)
etsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery = _EtsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 31),
    _EtsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery_Type()
)
etsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery.setStatus("current")
_EtsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave_Type = Counter32
_EtsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave = _EtsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 32),
    _EtsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave_Type()
)
etsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave.setStatus("current")
_EtsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery_Type = Counter32
_EtsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery = _EtsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 33),
    _EtsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery_Type()
)
etsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery.setStatus("current")
_EtsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal_Type = Counter32
_EtsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal = _EtsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 34),
    _EtsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal_Type()
)
etsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal.setStatus("current")
_EtsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode_Type = Counter32
_EtsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode_Object = MibTableColumn
etsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode = _EtsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 35),
    _EtsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode_Type()
)
etsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange = _EtsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 36),
    _EtsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange_Type()
)
etsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange.setStatus("current")
_EtsysMgmdExtStatsCntrsDropsProtocolTTLNot1_Type = Counter32
_EtsysMgmdExtStatsCntrsDropsProtocolTTLNot1_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropsProtocolTTLNot1 = _EtsysMgmdExtStatsCntrsDropsProtocolTTLNot1_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 37),
    _EtsysMgmdExtStatsCntrsDropsProtocolTTLNot1_Type()
)
etsysMgmdExtStatsCntrsDropsProtocolTTLNot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropsProtocolTTLNot1.setStatus("current")
_EtsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs_Type = Counter32
_EtsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs_Object = MibTableColumn
etsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs = _EtsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 38),
    _EtsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs_Type()
)
etsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs.setStatus("current")
_EtsysMgmdExtProtocolClassificationGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtProtocolClassificationGroup = _EtsysMgmdExtProtocolClassificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9)
)
_EtsysMgmdExtProtocolClassificationTable_Object = MibTable
etsysMgmdExtProtocolClassificationTable = _EtsysMgmdExtProtocolClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassificationTable.setStatus("current")
_EtsysMgmdExtProtocolClassificationEntry_Object = MibTableRow
etsysMgmdExtProtocolClassificationEntry = _EtsysMgmdExtProtocolClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1, 1)
)
etsysMgmdExtProtocolClassificationEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolClassification"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassificationEntry.setStatus("current")
_EtsysMgmdExtProtocolClassification_Type = MGMDProtocolClassTc
_EtsysMgmdExtProtocolClassification_Object = MibTableColumn
etsysMgmdExtProtocolClassification = _EtsysMgmdExtProtocolClassification_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1, 1, 1),
    _EtsysMgmdExtProtocolClassification_Type()
)
etsysMgmdExtProtocolClassification.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassification.setStatus("current")
_EtsysMgmdExtProtocolIdentifier_Type = MGMDProtocolIdTc
_EtsysMgmdExtProtocolIdentifier_Object = MibTableColumn
etsysMgmdExtProtocolIdentifier = _EtsysMgmdExtProtocolIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1, 1, 2),
    _EtsysMgmdExtProtocolIdentifier_Type()
)
etsysMgmdExtProtocolIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolIdentifier.setStatus("current")
_EtsysMgmdExtInputFilterGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtInputFilterGroup = _EtsysMgmdExtInputFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10)
)
_EtsysMgmdExtInputFilterTable_Object = MibTable
etsysMgmdExtInputFilterTable = _EtsysMgmdExtInputFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterTable.setStatus("current")
_EtsysMgmdExtInputFilterEntry_Object = MibTableRow
etsysMgmdExtInputFilterEntry = _EtsysMgmdExtInputFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1)
)
etsysMgmdExtInputFilterEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterApplication"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterId"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterRuleId"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterEntry.setStatus("current")
_EtsysMgmdExtInputFilterApplication_Type = InetAddressType
_EtsysMgmdExtInputFilterApplication_Object = MibTableColumn
etsysMgmdExtInputFilterApplication = _EtsysMgmdExtInputFilterApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 1),
    _EtsysMgmdExtInputFilterApplication_Type()
)
etsysMgmdExtInputFilterApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterApplication.setStatus("current")


class _EtsysMgmdExtInputFilterId_Type(Integer32):
    """Custom type etsysMgmdExtInputFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EtsysMgmdExtInputFilterId_Type.__name__ = "Integer32"
_EtsysMgmdExtInputFilterId_Object = MibTableColumn
etsysMgmdExtInputFilterId = _EtsysMgmdExtInputFilterId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 2),
    _EtsysMgmdExtInputFilterId_Type()
)
etsysMgmdExtInputFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterId.setStatus("current")


class _EtsysMgmdExtInputFilterRuleId_Type(Integer32):
    """Custom type etsysMgmdExtInputFilterRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EtsysMgmdExtInputFilterRuleId_Type.__name__ = "Integer32"
_EtsysMgmdExtInputFilterRuleId_Object = MibTableColumn
etsysMgmdExtInputFilterRuleId = _EtsysMgmdExtInputFilterRuleId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 3),
    _EtsysMgmdExtInputFilterRuleId_Type()
)
etsysMgmdExtInputFilterRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterRuleId.setStatus("current")
_EtsysMgmdExtInputFilterStartIPAddress_Type = InetAddress
_EtsysMgmdExtInputFilterStartIPAddress_Object = MibTableColumn
etsysMgmdExtInputFilterStartIPAddress = _EtsysMgmdExtInputFilterStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 4),
    _EtsysMgmdExtInputFilterStartIPAddress_Type()
)
etsysMgmdExtInputFilterStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterStartIPAddress.setStatus("current")
_EtsysMgmdExtInputFilterEndIPAddress_Type = InetAddress
_EtsysMgmdExtInputFilterEndIPAddress_Object = MibTableColumn
etsysMgmdExtInputFilterEndIPAddress = _EtsysMgmdExtInputFilterEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 5),
    _EtsysMgmdExtInputFilterEndIPAddress_Type()
)
etsysMgmdExtInputFilterEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterEndIPAddress.setStatus("current")
_EtsysMgmdExtInputFilterProtocolAction_Type = MGMDInputFilterProtocolActionsTc
_EtsysMgmdExtInputFilterProtocolAction_Object = MibTableColumn
etsysMgmdExtInputFilterProtocolAction = _EtsysMgmdExtInputFilterProtocolAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 6),
    _EtsysMgmdExtInputFilterProtocolAction_Type()
)
etsysMgmdExtInputFilterProtocolAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterProtocolAction.setStatus("current")
_EtsysMgmdExtInputFilterFlowAction_Type = MGMDInputFilterFlowActionsTc
_EtsysMgmdExtInputFilterFlowAction_Object = MibTableColumn
etsysMgmdExtInputFilterFlowAction = _EtsysMgmdExtInputFilterFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 7),
    _EtsysMgmdExtInputFilterFlowAction_Type()
)
etsysMgmdExtInputFilterFlowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterFlowAction.setStatus("current")
_EtsysMgmdExtInputFilterRuleHitCounter_Type = Integer32
_EtsysMgmdExtInputFilterRuleHitCounter_Object = MibTableColumn
etsysMgmdExtInputFilterRuleHitCounter = _EtsysMgmdExtInputFilterRuleHitCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 8),
    _EtsysMgmdExtInputFilterRuleHitCounter_Type()
)
etsysMgmdExtInputFilterRuleHitCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterRuleHitCounter.setStatus("current")
_EtsysMgmdExtInputFilterRowStatus_Type = RowStatus
_EtsysMgmdExtInputFilterRowStatus_Object = MibTableColumn
etsysMgmdExtInputFilterRowStatus = _EtsysMgmdExtInputFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 10, 1, 1, 9),
    _EtsysMgmdExtInputFilterRowStatus_Type()
)
etsysMgmdExtInputFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterRowStatus.setStatus("current")
_EtsysMgmdExtConformance_ObjectIdentity = ObjectIdentity
etsysMgmdExtConformance = _EtsysMgmdExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2)
)
_EtsysMgmdExtGroups_ObjectIdentity = ObjectIdentity
etsysMgmdExtGroups = _EtsysMgmdExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1)
)
_EtsysMgmdExtCompliances_ObjectIdentity = ObjectIdentity
etsysMgmdExtCompliances = _EtsysMgmdExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2)
)

# Managed Objects groups

etsysMgmdExtConfigGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 1)
)
etsysMgmdExtConfigGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigRevString"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMinNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigDefaultNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMaxNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtConfigGroups.setStatus("deprecated")

etsysMgmdExtInterfaceGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 2)
)
etsysMgmdExtInterfaceGroups.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState")
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceGroups.setStatus("deprecated")

etsysMgmdExtStaticCacheGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 3)
)
etsysMgmdExtStaticCacheGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheGroups.setStatus("current")

etsysMgmdExtCacheGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 4)
)
etsysMgmdExtCacheGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExpiryTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIncludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExcludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSrcPort"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtCacheGroups.setStatus("current")

etsysMgmdExtDiscoveredRouterGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 5)
)
etsysMgmdExtDiscoveredRouterGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterLearnedMethod"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterEgressing"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterBridgePortAgeTime"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterGroups.setStatus("current")

etsysMgmdExtPortGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 6)
)
etsysMgmdExtPortGroups.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableExpireTime")
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortGroups.setStatus("current")

etsysMgmdExtPortFastLeaveGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 7)
)
etsysMgmdExtPortFastLeaveGroups.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState")
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveGroups.setStatus("current")

etsysMgmdExtStatsCntsGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 8)
)
etsysMgmdExtStatsCntsGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsGroupFull"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumLeavesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumBadFramesRcvd"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntsGroups.setStatus("deprecated")

etsysMgmdExtProtocolClassificationGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 9)
)
etsysMgmdExtProtocolClassificationGroups.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolIdentifier")
)
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassificationGroups.setStatus("current")

etsysMgmdExtReadBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 10)
)
etsysMgmdExtReadBaseGroup.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigRevString"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMinNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigDefaultNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMaxNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExpiryTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIncludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExcludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSrcPort"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterLearnedMethod"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterEgressing"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterBridgePortAgeTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsGroupFull"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumLeavesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumBadFramesRcvd"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtReadBaseGroup.setStatus("deprecated")

etsysMgmdExtWriteBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 11)
)
etsysMgmdExtWriteBaseGroup.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolIdentifier"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtWriteBaseGroup.setStatus("deprecated")

etsysMgmdExtConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 12)
)
etsysMgmdExtConfigGroup2.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigRevString"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMinNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigDefaultNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMaxNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigUnknownInputAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFlowWaitEnable"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFlowWaitTime"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtConfigGroup2.setStatus("current")

etsysMgmdExtInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 13)
)
etsysMgmdExtInterfaceGroup2.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceQueryEnableState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceClearGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtRtrAlertRequired"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceGroup2.setStatus("current")

etsysMgmdExtStatsCntsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 14)
)
etsysMgmdExtStatsCntsGroup2.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsGroupFull"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumLeavesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumCurrentStateRecRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumSrcListChgRecRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToBeingDisabled"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToBadHdrLength"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropsProtocolTTLNot1"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumBadFramesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsClear"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntsGroup2.setStatus("current")

etsysMgmdExtInputFilterGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 15)
)
etsysMgmdExtInputFilterGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterStartIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterEndIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterProtocolAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterFlowAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterRuleHitCounter"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtInputFilterGroups.setStatus("current")

etsysMgmdExtReadBaseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 16)
)
etsysMgmdExtReadBaseGroup2.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigRevString"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMinNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigDefaultNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMaxNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigUnknownInputAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceClearGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFilterId"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFilterIdEnable"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExpiryTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIncludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExcludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSrcPort"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterLearnedMethod"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterEgressing"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterBridgePortAgeTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsGroupFull"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumLeavesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumBadFramesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterStartIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterEndIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterProtocolAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterFlowAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterRuleHitCounter"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtReadBaseGroup2.setStatus("current")

etsysMgmdExtWriteBaseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 17)
)
etsysMgmdExtWriteBaseGroup2.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceClearGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFilterId"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFilterIdEnable"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolIdentifier"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterStartIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterEndIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterProtocolAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterFlowAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtWriteBaseGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysMgmdExtReadCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 1)
)
etsysMgmdExtReadCompliance.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtReadBaseGroup")
)
if mibBuilder.loadTexts:
    etsysMgmdExtReadCompliance.setStatus(
        "deprecated"
    )

etsysMgmdExtWriteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 2)
)
etsysMgmdExtWriteCompliance.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtWriteBaseGroup")
)
if mibBuilder.loadTexts:
    etsysMgmdExtWriteCompliance.setStatus(
        "deprecated"
    )

etsysMgmdExtReadCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 3)
)
etsysMgmdExtReadCompliance2.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtReadBaseGroup2")
)
if mibBuilder.loadTexts:
    etsysMgmdExtReadCompliance2.setStatus(
        "current"
    )

etsysMgmdExtWriteCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 4)
)
etsysMgmdExtWriteCompliance2.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtWriteBaseGroup2")
)
if mibBuilder.loadTexts:
    etsysMgmdExtWriteCompliance2.setStatus(
        "current"
    )

etsysMgmdExtiBaseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 5)
)
etsysMgmdExtiBaseCompliance.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolClassificationGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigGroup2"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceGroup2"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntsGroup2"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInputFilterGroups"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtiBaseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MGMD-EXT-MIB",
    **{"MGMDNumGroupsTc": MGMDNumGroupsTc,
       "MGMDPortModeTc": MGMDPortModeTc,
       "MGMDDiscoveredRouterModeTc": MGMDDiscoveredRouterModeTc,
       "MGMDProtocolClassTc": MGMDProtocolClassTc,
       "MGMDProtocolIdTc": MGMDProtocolIdTc,
       "MGMDInputFilterFlowActionsTc": MGMDInputFilterFlowActionsTc,
       "MGMDInputFilterProtocolActionsTc": MGMDInputFilterProtocolActionsTc,
       "etsysMgmdExtMIB": etsysMgmdExtMIB,
       "etsysMgmdExtObjects": etsysMgmdExtObjects,
       "etsysMgmdExtConfigGroup": etsysMgmdExtConfigGroup,
       "etsysMgmdExtConfigRevString": etsysMgmdExtConfigRevString,
       "etsysMgmdExtConfigFullAction": etsysMgmdExtConfigFullAction,
       "etsysMgmdExtConfigMinNumberOfGroups": etsysMgmdExtConfigMinNumberOfGroups,
       "etsysMgmdExtConfigDefaultNumberOfGroups": etsysMgmdExtConfigDefaultNumberOfGroups,
       "etsysMgmdExtConfigMaxNumberOfGroups": etsysMgmdExtConfigMaxNumberOfGroups,
       "etsysMgmdExtConfigNumberOfGroups": etsysMgmdExtConfigNumberOfGroups,
       "etsysMgmdExtConfigUnknownInputAction": etsysMgmdExtConfigUnknownInputAction,
       "etsysMgmdExtConfigFlowWaitEnable": etsysMgmdExtConfigFlowWaitEnable,
       "etsysMgmdExtConfigFlowWaitTime": etsysMgmdExtConfigFlowWaitTime,
       "etsysMgmdExtInterfaceGroup": etsysMgmdExtInterfaceGroup,
       "etsysMgmdExtInterfaceTable": etsysMgmdExtInterfaceTable,
       "etsysMgmdExtInterfaceEntry": etsysMgmdExtInterfaceEntry,
       "etsysMgmdExtInterfaceApplication": etsysMgmdExtInterfaceApplication,
       "etsysMgmdExtInterfaceQueryEnableState": etsysMgmdExtInterfaceQueryEnableState,
       "etsysMgmdExtInterfaceFastLeaveState": etsysMgmdExtInterfaceFastLeaveState,
       "etsysMgmdExtInterfaceClearGroups": etsysMgmdExtInterfaceClearGroups,
       "etsysMgmdExtRtrAlertRequired": etsysMgmdExtRtrAlertRequired,
       "etsysMgmdExtInterfaceFilterId": etsysMgmdExtInterfaceFilterId,
       "etsysMgmdExtInterfaceFilterIdEnable": etsysMgmdExtInterfaceFilterIdEnable,
       "etsysMgmdExtStaticCacheGroup": etsysMgmdExtStaticCacheGroup,
       "etsysMgmdExtStaticCacheTable": etsysMgmdExtStaticCacheTable,
       "etsysMgmdExtStaticCacheEntry": etsysMgmdExtStaticCacheEntry,
       "etsysMgmdExtStaticCacheIPAddrType": etsysMgmdExtStaticCacheIPAddrType,
       "etsysMgmdExtStaticCacheGroupIPAddress": etsysMgmdExtStaticCacheGroupIPAddress,
       "etsysMgmdExtStaticCacheSourceIPAddress": etsysMgmdExtStaticCacheSourceIPAddress,
       "etsysMgmdExtStaticCacheIncludeList": etsysMgmdExtStaticCacheIncludeList,
       "etsysMgmdExtStaticCacheExcludeList": etsysMgmdExtStaticCacheExcludeList,
       "etsysMgmdExtStaticCacheRowStatus": etsysMgmdExtStaticCacheRowStatus,
       "etsysMgmdExtCacheGroup": etsysMgmdExtCacheGroup,
       "etsysMgmdExtCacheTable": etsysMgmdExtCacheTable,
       "etsysMgmdExtCacheEntry": etsysMgmdExtCacheEntry,
       "etsysMgmdExtCacheIPAddrType": etsysMgmdExtCacheIPAddrType,
       "etsysMgmdExtCacheGroupIPAddress": etsysMgmdExtCacheGroupIPAddress,
       "etsysMgmdExtCacheSourceIPAddress": etsysMgmdExtCacheSourceIPAddress,
       "etsysMgmdExtCacheExpiryTime": etsysMgmdExtCacheExpiryTime,
       "etsysMgmdExtCacheIncludePortList": etsysMgmdExtCacheIncludePortList,
       "etsysMgmdExtCacheExcludePortList": etsysMgmdExtCacheExcludePortList,
       "etsysMgmdExtCacheSrcPort": etsysMgmdExtCacheSrcPort,
       "etsysMgmdExtDiscoveredRouterGroup": etsysMgmdExtDiscoveredRouterGroup,
       "etsysMgmdExtDiscoveredRouterTable": etsysMgmdExtDiscoveredRouterTable,
       "etsysMgmdExtDiscoveredRouterEntry": etsysMgmdExtDiscoveredRouterEntry,
       "etsysMgmdExtDiscoveredRouterApplication": etsysMgmdExtDiscoveredRouterApplication,
       "etsysMgmdExtDiscoveredRouterLearnedMethod": etsysMgmdExtDiscoveredRouterLearnedMethod,
       "etsysMgmdExtDiscoveredRouterEgressing": etsysMgmdExtDiscoveredRouterEgressing,
       "etsysMgmdExtDiscoveredRouterStaticPortList": etsysMgmdExtDiscoveredRouterStaticPortList,
       "etsysMgmdExtDiscoveredRouterBridgePortAgeTime": etsysMgmdExtDiscoveredRouterBridgePortAgeTime,
       "etsysMgmdExtPortGroup": etsysMgmdExtPortGroup,
       "etsysMgmdExtPortTable": etsysMgmdExtPortTable,
       "etsysMgmdExtPortTableEntry": etsysMgmdExtPortTableEntry,
       "etsysMgmdExtPortMode": etsysMgmdExtPortMode,
       "etsysMgmdExtPortIPAddressType": etsysMgmdExtPortIPAddressType,
       "etsysMgmdExtPortTableGroupIPAddress": etsysMgmdExtPortTableGroupIPAddress,
       "etsysMgmdExtPortTableSourceIPAddress": etsysMgmdExtPortTableSourceIPAddress,
       "etsysMgmdExtPortTableExpireTime": etsysMgmdExtPortTableExpireTime,
       "etsysMgmdExtPortFastLeaveGroup": etsysMgmdExtPortFastLeaveGroup,
       "etsysMgmdExtPortFastLeaveTable": etsysMgmdExtPortFastLeaveTable,
       "etsysMgmdExtPortFastLeaveTableEntry": etsysMgmdExtPortFastLeaveTableEntry,
       "etsysMgmdExtPortFastLeaveState": etsysMgmdExtPortFastLeaveState,
       "etsysMgmdExtStatsCntrsGroup": etsysMgmdExtStatsCntrsGroup,
       "etsysMgmdExtStatsCntrsTable": etsysMgmdExtStatsCntrsTable,
       "etsysMgmdExtStatsCntrsEntry": etsysMgmdExtStatsCntrsEntry,
       "etsysMgmdExtStatsCntrsApplication": etsysMgmdExtStatsCntrsApplication,
       "etsysMgmdExtStatsCntrsGroupFull": etsysMgmdExtStatsCntrsGroupFull,
       "etsysMgmdExtStatsCntrsNumV1QueriesSent": etsysMgmdExtStatsCntrsNumV1QueriesSent,
       "etsysMgmdExtStatsCntrsNumV2QueriesSent": etsysMgmdExtStatsCntrsNumV2QueriesSent,
       "etsysMgmdExtStatsCntrsNumV3QueriesSent": etsysMgmdExtStatsCntrsNumV3QueriesSent,
       "etsysMgmdExtStatsCntrsNumGSQueriesSent": etsysMgmdExtStatsCntrsNumGSQueriesSent,
       "etsysMgmdExtStatsCntrsNumGAndSQueriesSent": etsysMgmdExtStatsCntrsNumGAndSQueriesSent,
       "etsysMgmdExtStatsCntrsNumV1QueriesRcvd": etsysMgmdExtStatsCntrsNumV1QueriesRcvd,
       "etsysMgmdExtStatsCntrsNumV2QueriesRcvd": etsysMgmdExtStatsCntrsNumV2QueriesRcvd,
       "etsysMgmdExtStatsCntrsNumV3QueriesRcvd": etsysMgmdExtStatsCntrsNumV3QueriesRcvd,
       "etsysMgmdExtStatsCntrsNumGSQueriesRcvd": etsysMgmdExtStatsCntrsNumGSQueriesRcvd,
       "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd": etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd,
       "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd": etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd,
       "etsysMgmdExtStatsCntrsNumV1ReportsRcvd": etsysMgmdExtStatsCntrsNumV1ReportsRcvd,
       "etsysMgmdExtStatsCntrsNumV2ReportsRcvd": etsysMgmdExtStatsCntrsNumV2ReportsRcvd,
       "etsysMgmdExtStatsCntrsNumV3ReportsRcvd": etsysMgmdExtStatsCntrsNumV3ReportsRcvd,
       "etsysMgmdExtStatsCntrsNumLeavesRcvd": etsysMgmdExtStatsCntrsNumLeavesRcvd,
       "etsysMgmdExtStatsCntrsNumBadFramesRcvd": etsysMgmdExtStatsCntrsNumBadFramesRcvd,
       "etsysMgmdExtStatsCntrsClear": etsysMgmdExtStatsCntrsClear,
       "etsysMgmdExtStatsCntrsNumCurrentStateRecRcvd": etsysMgmdExtStatsCntrsNumCurrentStateRecRcvd,
       "etsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd": etsysMgmdExtStatsCntrsNumFilterModeChangeRecRcvd,
       "etsysMgmdExtStatsCntrsNumSrcListChgRecRcvd": etsysMgmdExtStatsCntrsNumSrcListChgRecRcvd,
       "etsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP": etsysMgmdExtStatsCntrsDropsDueToInvalidSrcIP,
       "etsysMgmdExtStatsCntrsDropsDueToBeingDisabled": etsysMgmdExtStatsCntrsDropsDueToBeingDisabled,
       "etsysMgmdExtStatsCntrsDropsDueToBadHdrLength": etsysMgmdExtStatsCntrsDropsDueToBadHdrLength,
       "etsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm": etsysMgmdExtStatsCntrsDropsDueToBadIPHdrChksm,
       "etsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm": etsysMgmdExtStatsCntrsDropsDueToBadIGMPHdrChksm,
       "etsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert": etsysMgmdExtStatsCntrsDropsDueToMissingRtrAlert,
       "etsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP": etsysMgmdExtStatsCntrsDropsDueToOffNetworkSrcIP,
       "etsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery": etsysMgmdExtStatsCntrsDropsDueToZeroSipIPQuery,
       "etsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery": etsysMgmdExtStatsCntrsDropsDueToBadGrpAddressInQuery,
       "etsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave": etsysMgmdExtStatsCntrsDropDueToBadGrpAddressInLeave,
       "etsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery": etsysMgmdExtStatsCntrsDropDueToTooManySrcsInQuery,
       "etsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal": etsysMgmdExtStatsCntrsDropDueToMLDQueryFromNonLinkLocal,
       "etsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode": etsysMgmdExtStatsCntrsDroppedLeaveWeAreInV1Mode,
       "etsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange": etsysMgmdExtStatsCntrsDropsDueToBeingInSSMRange,
       "etsysMgmdExtStatsCntrsDropsProtocolTTLNot1": etsysMgmdExtStatsCntrsDropsProtocolTTLNot1,
       "etsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs": etsysMgmdExtStatsCntrsDropReportsDueToTooManySrcs,
       "etsysMgmdExtProtocolClassificationGroup": etsysMgmdExtProtocolClassificationGroup,
       "etsysMgmdExtProtocolClassificationTable": etsysMgmdExtProtocolClassificationTable,
       "etsysMgmdExtProtocolClassificationEntry": etsysMgmdExtProtocolClassificationEntry,
       "etsysMgmdExtProtocolClassification": etsysMgmdExtProtocolClassification,
       "etsysMgmdExtProtocolIdentifier": etsysMgmdExtProtocolIdentifier,
       "etsysMgmdExtInputFilterGroup": etsysMgmdExtInputFilterGroup,
       "etsysMgmdExtInputFilterTable": etsysMgmdExtInputFilterTable,
       "etsysMgmdExtInputFilterEntry": etsysMgmdExtInputFilterEntry,
       "etsysMgmdExtInputFilterApplication": etsysMgmdExtInputFilterApplication,
       "etsysMgmdExtInputFilterId": etsysMgmdExtInputFilterId,
       "etsysMgmdExtInputFilterRuleId": etsysMgmdExtInputFilterRuleId,
       "etsysMgmdExtInputFilterStartIPAddress": etsysMgmdExtInputFilterStartIPAddress,
       "etsysMgmdExtInputFilterEndIPAddress": etsysMgmdExtInputFilterEndIPAddress,
       "etsysMgmdExtInputFilterProtocolAction": etsysMgmdExtInputFilterProtocolAction,
       "etsysMgmdExtInputFilterFlowAction": etsysMgmdExtInputFilterFlowAction,
       "etsysMgmdExtInputFilterRuleHitCounter": etsysMgmdExtInputFilterRuleHitCounter,
       "etsysMgmdExtInputFilterRowStatus": etsysMgmdExtInputFilterRowStatus,
       "etsysMgmdExtConformance": etsysMgmdExtConformance,
       "etsysMgmdExtGroups": etsysMgmdExtGroups,
       "etsysMgmdExtConfigGroups": etsysMgmdExtConfigGroups,
       "etsysMgmdExtInterfaceGroups": etsysMgmdExtInterfaceGroups,
       "etsysMgmdExtStaticCacheGroups": etsysMgmdExtStaticCacheGroups,
       "etsysMgmdExtCacheGroups": etsysMgmdExtCacheGroups,
       "etsysMgmdExtDiscoveredRouterGroups": etsysMgmdExtDiscoveredRouterGroups,
       "etsysMgmdExtPortGroups": etsysMgmdExtPortGroups,
       "etsysMgmdExtPortFastLeaveGroups": etsysMgmdExtPortFastLeaveGroups,
       "etsysMgmdExtStatsCntsGroups": etsysMgmdExtStatsCntsGroups,
       "etsysMgmdExtProtocolClassificationGroups": etsysMgmdExtProtocolClassificationGroups,
       "etsysMgmdExtReadBaseGroup": etsysMgmdExtReadBaseGroup,
       "etsysMgmdExtWriteBaseGroup": etsysMgmdExtWriteBaseGroup,
       "etsysMgmdExtConfigGroup2": etsysMgmdExtConfigGroup2,
       "etsysMgmdExtInterfaceGroup2": etsysMgmdExtInterfaceGroup2,
       "etsysMgmdExtStatsCntsGroup2": etsysMgmdExtStatsCntsGroup2,
       "etsysMgmdExtInputFilterGroups": etsysMgmdExtInputFilterGroups,
       "etsysMgmdExtReadBaseGroup2": etsysMgmdExtReadBaseGroup2,
       "etsysMgmdExtWriteBaseGroup2": etsysMgmdExtWriteBaseGroup2,
       "etsysMgmdExtCompliances": etsysMgmdExtCompliances,
       "etsysMgmdExtReadCompliance": etsysMgmdExtReadCompliance,
       "etsysMgmdExtWriteCompliance": etsysMgmdExtWriteCompliance,
       "etsysMgmdExtReadCompliance2": etsysMgmdExtReadCompliance2,
       "etsysMgmdExtWriteCompliance2": etsysMgmdExtWriteCompliance2,
       "etsysMgmdExtiBaseCompliance": etsysMgmdExtiBaseCompliance}
)
