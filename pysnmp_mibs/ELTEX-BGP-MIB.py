# SNMP MIB module (ELTEX-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:51 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexBgpIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class EltexBgpAfi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              25)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("l2vpn", 25))
    )



class EltexBgpSafi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              65,
              70,
              128,
              241)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("both", 3),
          ("labeled", 4),
          ("vpls", 65),
          ("evpn", 70),
          ("mplsBgpVpn", 128),
          ("private", 241))
    )



class EltexBgpAutonomousSystemNumber(TextualConvention, Unsigned32):
    status = "current"


class EltexBgpAsSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoOctet", 1),
          ("fourOctet", 2))
    )



class EltexBgpAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusUp", 1),
          ("adminStatusDown", 2))
    )



class EltexBgpOperStatus(TextualConvention, Integer32):
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
        *(("operStatusUp", 1),
          ("operStatusDown", 2),
          ("operStatusGoingUp", 3),
          ("operStatusGoingDown", 4),
          ("operStatusActFailed", 5))
    )



class EltexBgpOriginCode(TextualConvention, Integer32):
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
        *(("originIgp", 0),
          ("originEgp", 1),
          ("originIncomplete", 2))
    )



class EltexBgpConfigDropOrWarn(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("warn", 2))
    )



class EltexBgpPeerOrRib(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("peerIndex", 1),
          ("ribIndex", 2))
    )



class EltexBgpPeerStates(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )



class EltexBgpPeerEvents(TextualConvention, Integer32):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("noEvent", 0),
          ("start", 1),
          ("stop", 2),
          ("transportOpen", 3),
          ("transportClosed", 4),
          ("transportOpenFailed", 5),
          ("transportFatalError", 6),
          ("connectRetryTimer", 7),
          ("holdTimer", 8),
          ("keepaliverTimer", 9),
          ("recvOpen", 10),
          ("recvKeepAlive", 11),
          ("recvUpdate", 12),
          ("recvNotification", 13),
          ("connParmsUpdate", 14))
    )



class EltexBgpCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("mpIpv4Unicast", 0),
          ("mpIpv4Multicast", 1),
          ("mpIpv4Vpn", 2),
          ("mpIpv4Label", 3),
          ("mpIpv6Unicast", 4),
          ("mpIpv6Multicast", 5),
          ("mpIpv6Vpn", 6),
          ("mpIpv6Label", 7),
          ("routeRefresh", 8),
          ("gracefulRestart", 9),
          ("routeRefreshCisco", 10),
          ("outboundRouteFilter", 11),
          ("outboundRouteFilterCisco", 12),
          ("fourOctetAs", 13),
          ("mpL2vpnVpls", 14),
          ("addPath", 15),
          ("mpL2vpnEvpn", 16),
          ("mpIpv4Private", 17),
          ("enhancedRouteRefresh", 18))
    )


class EltexBgpCeaseErrorSubcode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("adminShutdown", 2),
          ("peerUnconfig", 3),
          ("adminReset", 4),
          ("configChange", 6),
          ("noResource", 8))
    )



class EltexBgpNlriIsActiveFlag(TextualConvention, Integer32):
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
        *(("notTracked", 1),
          ("inactive", 2),
          ("active", 3))
    )



class EltexBgpPeerConfigStates(TextualConvention, Integer32):
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
        *(("stateUpToDate", 1),
          ("stateOutOfDateAdminDown", 2),
          ("stateOutOfDateRowInactive", 3))
    )



class EltexBgpReasonNotBest(TextualConvention, Integer32):
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("notConsidered", 0),
          ("routeIsBest", 1),
          ("weight", 2),
          ("localPref", 3),
          ("localOrigPreferred", 4),
          ("asPathLen", 5),
          ("origin", 6),
          ("med", 7),
          ("localOrigTieBreaker", 8),
          ("ebgpVsibgp", 9),
          ("adminDistance", 10),
          ("pathCostToNextHop", 11),
          ("prefExisting", 12),
          ("identifier", 13),
          ("clusterLen", 14),
          ("peerType", 15),
          ("peerAddress", 16),
          ("peerPort", 17),
          ("pathId", 18))
    )



class EltexBgpNlriPeerTypes(TextualConvention, Integer32):
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
        *(("none", 1),
          ("iBGP", 2),
          ("eBGP", 3))
    )



class EltexBgpASNotation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asplainASNumber", 1),
          ("asdotASnumber", 2))
    )



class EltexBgpPeerReflectorClientType(TextualConvention, Integer32):
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
        *(("nonClient", 0),
          ("client", 1),
          ("meshedClient", 2))
    )



class EltexBgpRouteMapAsPathAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("set", 1))
    )



class EltexBgpAddPathSrCap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("receive", 1),
          ("send", 2),
          ("both", 3),
          ("inherit", 4),
          ("unknown", 5))
    )



class EltexBfdSessionStatus(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("bfdSessNotRequired", 0),
          ("bfdSessInitial", 1),
          ("bfdSessActivating", 2),
          ("bfdSessActive", 3),
          ("bfdSessInactive", 4),
          ("bfdSessAdminDown", 5),
          ("bfdSessNoContact", 6))
    )



# MIB Managed Objects in the order of their OIDs

_EltexBgpObjects_ObjectIdentity = ObjectIdentity
eltexBgpObjects = _EltexBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1)
)
_EltexBgpProcess_ObjectIdentity = ObjectIdentity
eltexBgpProcess = _EltexBgpProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1)
)
_EltexBgpProcessTable_Object = MibTable
eltexBgpProcessTable = _EltexBgpProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltexBgpProcessTable.setStatus("current")
_EltexBgpProcessEntry_Object = MibTableRow
eltexBgpProcessEntry = _EltexBgpProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1)
)
eltexBgpProcessEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
)
if mibBuilder.loadTexts:
    eltexBgpProcessEntry.setStatus("current")
_EltexBgpProcessId_Type = Unsigned32
_EltexBgpProcessId_Object = MibTableColumn
eltexBgpProcessId = _EltexBgpProcessId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 1),
    _EltexBgpProcessId_Type()
)
eltexBgpProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpProcessId.setStatus("current")
_EltexBgpProcessRowStatus_Type = RowStatus
_EltexBgpProcessRowStatus_Object = MibTableColumn
eltexBgpProcessRowStatus = _EltexBgpProcessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 2),
    _EltexBgpProcessRowStatus_Type()
)
eltexBgpProcessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexBgpProcessRowStatus.setStatus("current")


class _EltexBgpProcessAdminStatus_Type(EltexBgpAdminStatus):
    """Custom type eltexBgpProcessAdminStatus based on EltexBgpAdminStatus"""
    defaultValue = 2


_EltexBgpProcessAdminStatus_Type.__name__ = "EltexBgpAdminStatus"
_EltexBgpProcessAdminStatus_Object = MibTableColumn
eltexBgpProcessAdminStatus = _EltexBgpProcessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 3),
    _EltexBgpProcessAdminStatus_Type()
)
eltexBgpProcessAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessAdminStatus.setStatus("current")
_EltexBgpProcessOperStatus_Type = EltexBgpOperStatus
_EltexBgpProcessOperStatus_Object = MibTableColumn
eltexBgpProcessOperStatus = _EltexBgpProcessOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 4),
    _EltexBgpProcessOperStatus_Type()
)
eltexBgpProcessOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpProcessOperStatus.setStatus("current")
_EltexBgpProcessLocalAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpProcessLocalAs_Object = MibTableColumn
eltexBgpProcessLocalAs = _EltexBgpProcessLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 5),
    _EltexBgpProcessLocalAs_Type()
)
eltexBgpProcessLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessLocalAs.setStatus("current")


class _EltexBgpProcessLocalIdentifier_Type(EltexBgpIdentifier):
    """Custom type eltexBgpProcessLocalIdentifier based on EltexBgpIdentifier"""
    defaultHexValue = "00000000"


_EltexBgpProcessLocalIdentifier_Type.__name__ = "EltexBgpIdentifier"
_EltexBgpProcessLocalIdentifier_Object = MibTableColumn
eltexBgpProcessLocalIdentifier = _EltexBgpProcessLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 6),
    _EltexBgpProcessLocalIdentifier_Type()
)
eltexBgpProcessLocalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessLocalIdentifier.setStatus("current")
_EltexBgpProcessOperLocalIdentifier_Type = EltexBgpIdentifier
_EltexBgpProcessOperLocalIdentifier_Object = MibTableColumn
eltexBgpProcessOperLocalIdentifier = _EltexBgpProcessOperLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 7),
    _EltexBgpProcessOperLocalIdentifier_Type()
)
eltexBgpProcessOperLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpProcessOperLocalIdentifier.setStatus("current")


class _EltexBgpProcessTableVersion_Type(Unsigned32):
    """Custom type eltexBgpProcessTableVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EltexBgpProcessTableVersion_Type.__name__ = "Unsigned32"
_EltexBgpProcessTableVersion_Object = MibTableColumn
eltexBgpProcessTableVersion = _EltexBgpProcessTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 8),
    _EltexBgpProcessTableVersion_Type()
)
eltexBgpProcessTableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpProcessTableVersion.setStatus("current")


class _EltexBgpProcessASNotation_Type(EltexBgpASNotation):
    """Custom type eltexBgpProcessASNotation based on EltexBgpASNotation"""
    defaultValue = 1


_EltexBgpProcessASNotation_Type.__name__ = "EltexBgpASNotation"
_EltexBgpProcessASNotation_Object = MibTableColumn
eltexBgpProcessASNotation = _EltexBgpProcessASNotation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 9),
    _EltexBgpProcessASNotation_Type()
)
eltexBgpProcessASNotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessASNotation.setStatus("current")


class _EltexBgpProcessClusterIdentifier_Type(EltexBgpIdentifier):
    """Custom type eltexBgpProcessClusterIdentifier based on EltexBgpIdentifier"""
    defaultHexValue = "00000000"


_EltexBgpProcessClusterIdentifier_Type.__name__ = "EltexBgpIdentifier"
_EltexBgpProcessClusterIdentifier_Object = MibTableColumn
eltexBgpProcessClusterIdentifier = _EltexBgpProcessClusterIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 10),
    _EltexBgpProcessClusterIdentifier_Type()
)
eltexBgpProcessClusterIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessClusterIdentifier.setStatus("current")


class _EltexBgpProcessOperClusterIdentifier_Type(EltexBgpIdentifier):
    """Custom type eltexBgpProcessOperClusterIdentifier based on EltexBgpIdentifier"""
    defaultHexValue = "00000000"


_EltexBgpProcessOperClusterIdentifier_Type.__name__ = "EltexBgpIdentifier"
_EltexBgpProcessOperClusterIdentifier_Object = MibTableColumn
eltexBgpProcessOperClusterIdentifier = _EltexBgpProcessOperClusterIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 11),
    _EltexBgpProcessOperClusterIdentifier_Type()
)
eltexBgpProcessOperClusterIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpProcessOperClusterIdentifier.setStatus("current")


class _EltexBgpProcessInterClientReflEnabled_Type(TruthValue):
    """Custom type eltexBgpProcessInterClientReflEnabled based on TruthValue"""
    defaultValue = 1


_EltexBgpProcessInterClientReflEnabled_Type.__name__ = "TruthValue"
_EltexBgpProcessInterClientReflEnabled_Object = MibTableColumn
eltexBgpProcessInterClientReflEnabled = _EltexBgpProcessInterClientReflEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 12),
    _EltexBgpProcessInterClientReflEnabled_Type()
)
eltexBgpProcessInterClientReflEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessInterClientReflEnabled.setStatus("current")


class _EltexBgpProcessPathMtuDiscovery_Type(TruthValue):
    """Custom type eltexBgpProcessPathMtuDiscovery based on TruthValue"""
    defaultValue = 2


_EltexBgpProcessPathMtuDiscovery_Type.__name__ = "TruthValue"
_EltexBgpProcessPathMtuDiscovery_Object = MibTableColumn
eltexBgpProcessPathMtuDiscovery = _EltexBgpProcessPathMtuDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 1, 1, 13),
    _EltexBgpProcessPathMtuDiscovery_Type()
)
eltexBgpProcessPathMtuDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessPathMtuDiscovery.setStatus("current")
_EltexBgpProcessAddrFamilyTable_Object = MibTable
eltexBgpProcessAddrFamilyTable = _EltexBgpProcessAddrFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltexBgpProcessAddrFamilyTable.setStatus("current")
_EltexBgpProcessAddrFamilyEntry_Object = MibTableRow
eltexBgpProcessAddrFamilyEntry = _EltexBgpProcessAddrFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 2, 1)
)
eltexBgpProcessAddrFamilyEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessAddrFamilyAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessAddrFamilySafi"),
)
if mibBuilder.loadTexts:
    eltexBgpProcessAddrFamilyEntry.setStatus("current")
_EltexBgpProcessAddrFamilyAfi_Type = EltexBgpAfi
_EltexBgpProcessAddrFamilyAfi_Object = MibTableColumn
eltexBgpProcessAddrFamilyAfi = _EltexBgpProcessAddrFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 2, 1, 2),
    _EltexBgpProcessAddrFamilyAfi_Type()
)
eltexBgpProcessAddrFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpProcessAddrFamilyAfi.setStatus("current")
_EltexBgpProcessAddrFamilySafi_Type = EltexBgpSafi
_EltexBgpProcessAddrFamilySafi_Object = MibTableColumn
eltexBgpProcessAddrFamilySafi = _EltexBgpProcessAddrFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 2, 1, 3),
    _EltexBgpProcessAddrFamilySafi_Type()
)
eltexBgpProcessAddrFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpProcessAddrFamilySafi.setStatus("current")
_EltexBgpProcessAddrFamilyRowStatus_Type = RowStatus
_EltexBgpProcessAddrFamilyRowStatus_Object = MibTableColumn
eltexBgpProcessAddrFamilyRowStatus = _EltexBgpProcessAddrFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 1, 2, 1, 4),
    _EltexBgpProcessAddrFamilyRowStatus_Type()
)
eltexBgpProcessAddrFamilyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpProcessAddrFamilyRowStatus.setStatus("current")
_EltexBgpPeer_ObjectIdentity = ObjectIdentity
eltexBgpPeer = _EltexBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2)
)
_EltexBgpPeerData_ObjectIdentity = ObjectIdentity
eltexBgpPeerData = _EltexBgpPeerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1)
)
_EltexBgpPeerTable_Object = MibTable
eltexBgpPeerTable = _EltexBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltexBgpPeerTable.setStatus("current")
_EltexBgpPeerEntry_Object = MibTableRow
eltexBgpPeerEntry = _EltexBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1)
)
eltexBgpPeerEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddrType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    eltexBgpPeerEntry.setStatus("current")
_EltexBgpPeerRemoteAddrType_Type = InetAddressType
_EltexBgpPeerRemoteAddrType_Object = MibTableColumn
eltexBgpPeerRemoteAddrType = _EltexBgpPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 1),
    _EltexBgpPeerRemoteAddrType_Type()
)
eltexBgpPeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpPeerRemoteAddrType.setStatus("current")
_EltexBgpPeerRemoteAddr_Type = InetAddress
_EltexBgpPeerRemoteAddr_Object = MibTableColumn
eltexBgpPeerRemoteAddr = _EltexBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 2),
    _EltexBgpPeerRemoteAddr_Type()
)
eltexBgpPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpPeerRemoteAddr.setStatus("current")
_EltexBgpPeerRowStatus_Type = RowStatus
_EltexBgpPeerRowStatus_Object = MibTableColumn
eltexBgpPeerRowStatus = _EltexBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 3),
    _EltexBgpPeerRowStatus_Type()
)
eltexBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexBgpPeerRowStatus.setStatus("current")


class _EltexBgpPeerAdminStatus_Type(EltexBgpAdminStatus):
    """Custom type eltexBgpPeerAdminStatus based on EltexBgpAdminStatus"""
    defaultValue = 2


_EltexBgpPeerAdminStatus_Type.__name__ = "EltexBgpAdminStatus"
_EltexBgpPeerAdminStatus_Object = MibTableColumn
eltexBgpPeerAdminStatus = _EltexBgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 4),
    _EltexBgpPeerAdminStatus_Type()
)
eltexBgpPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAdminStatus.setStatus("current")
_EltexBgpPeerOperStatus_Type = EltexBgpOperStatus
_EltexBgpPeerOperStatus_Object = MibTableColumn
eltexBgpPeerOperStatus = _EltexBgpPeerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 5),
    _EltexBgpPeerOperStatus_Type()
)
eltexBgpPeerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerOperStatus.setStatus("current")
_EltexBgpPeerRemoteAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpPeerRemoteAs_Object = MibTableColumn
eltexBgpPeerRemoteAs = _EltexBgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 6),
    _EltexBgpPeerRemoteAs_Type()
)
eltexBgpPeerRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerRemoteAs.setStatus("current")


class _EltexBgpPeerSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type eltexBgpPeerSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_EltexBgpPeerSourceInterface_Type.__name__ = "InterfaceIndexOrZero"
_EltexBgpPeerSourceInterface_Object = MibTableColumn
eltexBgpPeerSourceInterface = _EltexBgpPeerSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 7),
    _EltexBgpPeerSourceInterface_Type()
)
eltexBgpPeerSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerSourceInterface.setStatus("current")


class _EltexBgpPeerNxtHopSlf_Type(TruthValue):
    """Custom type eltexBgpPeerNxtHopSlf based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerNxtHopSlf_Type.__name__ = "TruthValue"
_EltexBgpPeerNxtHopSlf_Object = MibTableColumn
eltexBgpPeerNxtHopSlf = _EltexBgpPeerNxtHopSlf_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 8),
    _EltexBgpPeerNxtHopSlf_Type()
)
eltexBgpPeerNxtHopSlf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerNxtHopSlf.setStatus("current")


class _EltexBgpPeerConfigMaxPrfx_Type(Unsigned32):
    """Custom type eltexBgpPeerConfigMaxPrfx based on Unsigned32"""
    defaultValue = 0


_EltexBgpPeerConfigMaxPrfx_Type.__name__ = "Unsigned32"
_EltexBgpPeerConfigMaxPrfx_Object = MibTableColumn
eltexBgpPeerConfigMaxPrfx = _EltexBgpPeerConfigMaxPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 9),
    _EltexBgpPeerConfigMaxPrfx_Type()
)
eltexBgpPeerConfigMaxPrfx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConfigMaxPrfx.setStatus("current")


class _EltexBgpPeerConfigDropWarn_Type(EltexBgpConfigDropOrWarn):
    """Custom type eltexBgpPeerConfigDropWarn based on EltexBgpConfigDropOrWarn"""
    defaultValue = 2


_EltexBgpPeerConfigDropWarn_Type.__name__ = "EltexBgpConfigDropOrWarn"
_EltexBgpPeerConfigDropWarn_Object = MibTableColumn
eltexBgpPeerConfigDropWarn = _EltexBgpPeerConfigDropWarn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 10),
    _EltexBgpPeerConfigDropWarn_Type()
)
eltexBgpPeerConfigDropWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConfigDropWarn.setStatus("current")


class _EltexBgpPeerMaxPrfxHold_Type(Unsigned32):
    """Custom type eltexBgpPeerMaxPrfxHold based on Unsigned32"""
    defaultValue = 90


_EltexBgpPeerMaxPrfxHold_Type.__name__ = "Unsigned32"
_EltexBgpPeerMaxPrfxHold_Object = MibTableColumn
eltexBgpPeerMaxPrfxHold = _EltexBgpPeerMaxPrfxHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 11),
    _EltexBgpPeerMaxPrfxHold_Type()
)
eltexBgpPeerMaxPrfxHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerMaxPrfxHold.setStatus("current")


class _EltexBgpPeerConfigThreshold_Type(Unsigned32):
    """Custom type eltexBgpPeerConfigThreshold based on Unsigned32"""
    defaultValue = 75


_EltexBgpPeerConfigThreshold_Type.__name__ = "Unsigned32"
_EltexBgpPeerConfigThreshold_Object = MibTableColumn
eltexBgpPeerConfigThreshold = _EltexBgpPeerConfigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 12),
    _EltexBgpPeerConfigThreshold_Type()
)
eltexBgpPeerConfigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConfigThreshold.setStatus("current")


class _EltexBgpPeerConnectRetryInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexBgpPeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerConnectRetryInterval_Object = MibTableColumn
eltexBgpPeerConnectRetryInterval = _EltexBgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 13),
    _EltexBgpPeerConnectRetryInterval_Type()
)
eltexBgpPeerConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConnectRetryInterval.setStatus("current")


class _EltexBgpPeerHoldTimeConfigd_Type(Unsigned32):
    """Custom type eltexBgpPeerHoldTimeConfigd based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerHoldTimeConfigd_Type.__name__ = "Unsigned32"
_EltexBgpPeerHoldTimeConfigd_Object = MibTableColumn
eltexBgpPeerHoldTimeConfigd = _EltexBgpPeerHoldTimeConfigd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 14),
    _EltexBgpPeerHoldTimeConfigd_Type()
)
eltexBgpPeerHoldTimeConfigd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerHoldTimeConfigd.setStatus("current")


class _EltexBgpPeerKeepAliveConfigd_Type(Unsigned32):
    """Custom type eltexBgpPeerKeepAliveConfigd based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_EltexBgpPeerKeepAliveConfigd_Type.__name__ = "Unsigned32"
_EltexBgpPeerKeepAliveConfigd_Object = MibTableColumn
eltexBgpPeerKeepAliveConfigd = _EltexBgpPeerKeepAliveConfigd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 15),
    _EltexBgpPeerKeepAliveConfigd_Type()
)
eltexBgpPeerKeepAliveConfigd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerKeepAliveConfigd.setStatus("current")


class _EltexBgpPeerMinRouteAdvertiseInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerMinRouteAdvertiseInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerMinRouteAdvertiseInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerMinRouteAdvertiseInterval_Object = MibTableColumn
eltexBgpPeerMinRouteAdvertiseInterval = _EltexBgpPeerMinRouteAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 16),
    _EltexBgpPeerMinRouteAdvertiseInterval_Type()
)
eltexBgpPeerMinRouteAdvertiseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerMinRouteAdvertiseInterval.setStatus("current")


class _EltexBgpPeerMinASOriginationInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerMinASOriginationInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerMinASOriginationInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerMinASOriginationInterval_Object = MibTableColumn
eltexBgpPeerMinASOriginationInterval = _EltexBgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 17),
    _EltexBgpPeerMinASOriginationInterval_Type()
)
eltexBgpPeerMinASOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerMinASOriginationInterval.setStatus("current")


class _EltexBgpPeerMinRouteWithdrawInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerMinRouteWithdrawInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerMinRouteWithdrawInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerMinRouteWithdrawInterval_Object = MibTableColumn
eltexBgpPeerMinRouteWithdrawInterval = _EltexBgpPeerMinRouteWithdrawInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 18),
    _EltexBgpPeerMinRouteWithdrawInterval_Type()
)
eltexBgpPeerMinRouteWithdrawInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerMinRouteWithdrawInterval.setStatus("current")


class _EltexBgpPeerConfigOpenDelay_Type(Unsigned32):
    """Custom type eltexBgpPeerConfigOpenDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_EltexBgpPeerConfigOpenDelay_Type.__name__ = "Unsigned32"
_EltexBgpPeerConfigOpenDelay_Object = MibTableColumn
eltexBgpPeerConfigOpenDelay = _EltexBgpPeerConfigOpenDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 19),
    _EltexBgpPeerConfigOpenDelay_Type()
)
eltexBgpPeerConfigOpenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConfigOpenDelay.setStatus("current")


class _EltexBgpPeerConfigIdleHold_Type(Unsigned32):
    """Custom type eltexBgpPeerConfigIdleHold based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_EltexBgpPeerConfigIdleHold_Type.__name__ = "Unsigned32"
_EltexBgpPeerConfigIdleHold_Object = MibTableColumn
eltexBgpPeerConfigIdleHold = _EltexBgpPeerConfigIdleHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 20),
    _EltexBgpPeerConfigIdleHold_Type()
)
eltexBgpPeerConfigIdleHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConfigIdleHold.setStatus("current")
_EltexBgpPeerDistListPlIn_Type = DisplayString
_EltexBgpPeerDistListPlIn_Object = MibTableColumn
eltexBgpPeerDistListPlIn = _EltexBgpPeerDistListPlIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 21),
    _EltexBgpPeerDistListPlIn_Type()
)
eltexBgpPeerDistListPlIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerDistListPlIn.setStatus("current")
_EltexBgpPeerDistListPlOut_Type = DisplayString
_EltexBgpPeerDistListPlOut_Object = MibTableColumn
eltexBgpPeerDistListPlOut = _EltexBgpPeerDistListPlOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 22),
    _EltexBgpPeerDistListPlOut_Type()
)
eltexBgpPeerDistListPlOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerDistListPlOut.setStatus("current")


class _EltexBgpPeerReflectorClient_Type(EltexBgpPeerReflectorClientType):
    """Custom type eltexBgpPeerReflectorClient based on EltexBgpPeerReflectorClientType"""
    defaultValue = 0


_EltexBgpPeerReflectorClient_Type.__name__ = "EltexBgpPeerReflectorClientType"
_EltexBgpPeerReflectorClient_Object = MibTableColumn
eltexBgpPeerReflectorClient = _EltexBgpPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 23),
    _EltexBgpPeerReflectorClient_Type()
)
eltexBgpPeerReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerReflectorClient.setStatus("current")


class _EltexBgpPeerSoftResetWithStoredInfo_Type(TruthValue):
    """Custom type eltexBgpPeerSoftResetWithStoredInfo based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerSoftResetWithStoredInfo_Type.__name__ = "TruthValue"
_EltexBgpPeerSoftResetWithStoredInfo_Object = MibTableColumn
eltexBgpPeerSoftResetWithStoredInfo = _EltexBgpPeerSoftResetWithStoredInfo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 24),
    _EltexBgpPeerSoftResetWithStoredInfo_Type()
)
eltexBgpPeerSoftResetWithStoredInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerSoftResetWithStoredInfo.setStatus("current")
_EltexBgpPeerConfigPeerGroup_Type = DisplayString
_EltexBgpPeerConfigPeerGroup_Object = MibTableColumn
eltexBgpPeerConfigPeerGroup = _EltexBgpPeerConfigPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 25),
    _EltexBgpPeerConfigPeerGroup_Type()
)
eltexBgpPeerConfigPeerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerConfigPeerGroup.setStatus("current")


class _EltexBgpPeerPathMtuDiscovery_Type(TruthValue):
    """Custom type eltexBgpPeerPathMtuDiscovery based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerPathMtuDiscovery_Type.__name__ = "TruthValue"
_EltexBgpPeerPathMtuDiscovery_Object = MibTableColumn
eltexBgpPeerPathMtuDiscovery = _EltexBgpPeerPathMtuDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 26),
    _EltexBgpPeerPathMtuDiscovery_Type()
)
eltexBgpPeerPathMtuDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerPathMtuDiscovery.setStatus("current")


class _EltexBgpPeerBfdDesired_Type(TruthValue):
    """Custom type eltexBgpPeerBfdDesired based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerBfdDesired_Type.__name__ = "TruthValue"
_EltexBgpPeerBfdDesired_Object = MibTableColumn
eltexBgpPeerBfdDesired = _EltexBgpPeerBfdDesired_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 1, 1, 27),
    _EltexBgpPeerBfdDesired_Type()
)
eltexBgpPeerBfdDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerBfdDesired.setStatus("current")
_EltexBgpPeerAddrFamilyTable_Object = MibTable
eltexBgpPeerAddrFamilyTable = _EltexBgpPeerAddrFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyTable.setStatus("current")
_EltexBgpPeerAddrFamilyEntry_Object = MibTableRow
eltexBgpPeerAddrFamilyEntry = _EltexBgpPeerAddrFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1)
)
eltexBgpPeerAddrFamilyEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddrType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddr"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerAddrFamilyAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerAddrFamilySafi"),
)
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyEntry.setStatus("current")
_EltexBgpPeerAddrFamilyAfi_Type = EltexBgpAfi
_EltexBgpPeerAddrFamilyAfi_Object = MibTableColumn
eltexBgpPeerAddrFamilyAfi = _EltexBgpPeerAddrFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 1),
    _EltexBgpPeerAddrFamilyAfi_Type()
)
eltexBgpPeerAddrFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyAfi.setStatus("current")
_EltexBgpPeerAddrFamilySafi_Type = EltexBgpSafi
_EltexBgpPeerAddrFamilySafi_Object = MibTableColumn
eltexBgpPeerAddrFamilySafi = _EltexBgpPeerAddrFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 2),
    _EltexBgpPeerAddrFamilySafi_Type()
)
eltexBgpPeerAddrFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilySafi.setStatus("current")


class _EltexBgpPeerAddrFamilyDisable_Type(TruthValue):
    """Custom type eltexBgpPeerAddrFamilyDisable based on TruthValue"""
    defaultValue = 1


_EltexBgpPeerAddrFamilyDisable_Type.__name__ = "TruthValue"
_EltexBgpPeerAddrFamilyDisable_Object = MibTableColumn
eltexBgpPeerAddrFamilyDisable = _EltexBgpPeerAddrFamilyDisable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 3),
    _EltexBgpPeerAddrFamilyDisable_Type()
)
eltexBgpPeerAddrFamilyDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyDisable.setStatus("current")


class _EltexBgpPeerAddrFamilyNxtHopSlf_Type(TruthValue):
    """Custom type eltexBgpPeerAddrFamilyNxtHopSlf based on TruthValue"""
    defaultValue = 1


_EltexBgpPeerAddrFamilyNxtHopSlf_Type.__name__ = "TruthValue"
_EltexBgpPeerAddrFamilyNxtHopSlf_Object = MibTableColumn
eltexBgpPeerAddrFamilyNxtHopSlf = _EltexBgpPeerAddrFamilyNxtHopSlf_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 4),
    _EltexBgpPeerAddrFamilyNxtHopSlf_Type()
)
eltexBgpPeerAddrFamilyNxtHopSlf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyNxtHopSlf.setStatus("current")


class _EltexBgpPeerAddrFamilyConfigMaxPrfx_Type(Unsigned32):
    """Custom type eltexBgpPeerAddrFamilyConfigMaxPrfx based on Unsigned32"""
    defaultValue = 0


_EltexBgpPeerAddrFamilyConfigMaxPrfx_Type.__name__ = "Unsigned32"
_EltexBgpPeerAddrFamilyConfigMaxPrfx_Object = MibTableColumn
eltexBgpPeerAddrFamilyConfigMaxPrfx = _EltexBgpPeerAddrFamilyConfigMaxPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 5),
    _EltexBgpPeerAddrFamilyConfigMaxPrfx_Type()
)
eltexBgpPeerAddrFamilyConfigMaxPrfx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyConfigMaxPrfx.setStatus("current")


class _EltexBgpPeerAddrFamilyConfigDropWarn_Type(EltexBgpConfigDropOrWarn):
    """Custom type eltexBgpPeerAddrFamilyConfigDropWarn based on EltexBgpConfigDropOrWarn"""
    defaultValue = 2


_EltexBgpPeerAddrFamilyConfigDropWarn_Type.__name__ = "EltexBgpConfigDropOrWarn"
_EltexBgpPeerAddrFamilyConfigDropWarn_Object = MibTableColumn
eltexBgpPeerAddrFamilyConfigDropWarn = _EltexBgpPeerAddrFamilyConfigDropWarn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 6),
    _EltexBgpPeerAddrFamilyConfigDropWarn_Type()
)
eltexBgpPeerAddrFamilyConfigDropWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyConfigDropWarn.setStatus("current")


class _EltexBgpPeerAddrFamilyMaxPrfxHold_Type(Unsigned32):
    """Custom type eltexBgpPeerAddrFamilyMaxPrfxHold based on Unsigned32"""
    defaultValue = 90


_EltexBgpPeerAddrFamilyMaxPrfxHold_Type.__name__ = "Unsigned32"
_EltexBgpPeerAddrFamilyMaxPrfxHold_Object = MibTableColumn
eltexBgpPeerAddrFamilyMaxPrfxHold = _EltexBgpPeerAddrFamilyMaxPrfxHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 7),
    _EltexBgpPeerAddrFamilyMaxPrfxHold_Type()
)
eltexBgpPeerAddrFamilyMaxPrfxHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyMaxPrfxHold.setStatus("current")


class _EltexBgpPeerAddrFamilyConfigThreshold_Type(Unsigned32):
    """Custom type eltexBgpPeerAddrFamilyConfigThreshold based on Unsigned32"""
    defaultValue = 75


_EltexBgpPeerAddrFamilyConfigThreshold_Type.__name__ = "Unsigned32"
_EltexBgpPeerAddrFamilyConfigThreshold_Object = MibTableColumn
eltexBgpPeerAddrFamilyConfigThreshold = _EltexBgpPeerAddrFamilyConfigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 8),
    _EltexBgpPeerAddrFamilyConfigThreshold_Type()
)
eltexBgpPeerAddrFamilyConfigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyConfigThreshold.setStatus("current")


class _EltexBgpPeerAddrFamilyMinRteAdvertInt_Type(Unsigned32):
    """Custom type eltexBgpPeerAddrFamilyMinRteAdvertInt based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerAddrFamilyMinRteAdvertInt_Type.__name__ = "Unsigned32"
_EltexBgpPeerAddrFamilyMinRteAdvertInt_Object = MibTableColumn
eltexBgpPeerAddrFamilyMinRteAdvertInt = _EltexBgpPeerAddrFamilyMinRteAdvertInt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 9),
    _EltexBgpPeerAddrFamilyMinRteAdvertInt_Type()
)
eltexBgpPeerAddrFamilyMinRteAdvertInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyMinRteAdvertInt.setStatus("current")


class _EltexBgpPeerAddrFamilyMinASOrigInt_Type(Unsigned32):
    """Custom type eltexBgpPeerAddrFamilyMinASOrigInt based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexBgpPeerAddrFamilyMinASOrigInt_Type.__name__ = "Unsigned32"
_EltexBgpPeerAddrFamilyMinASOrigInt_Object = MibTableColumn
eltexBgpPeerAddrFamilyMinASOrigInt = _EltexBgpPeerAddrFamilyMinASOrigInt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 10),
    _EltexBgpPeerAddrFamilyMinASOrigInt_Type()
)
eltexBgpPeerAddrFamilyMinASOrigInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyMinASOrigInt.setStatus("current")


class _EltexBgpPeerAddrFamilyMinRteWithdrawInt_Type(Unsigned32):
    """Custom type eltexBgpPeerAddrFamilyMinRteWithdrawInt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerAddrFamilyMinRteWithdrawInt_Type.__name__ = "Unsigned32"
_EltexBgpPeerAddrFamilyMinRteWithdrawInt_Object = MibTableColumn
eltexBgpPeerAddrFamilyMinRteWithdrawInt = _EltexBgpPeerAddrFamilyMinRteWithdrawInt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 11),
    _EltexBgpPeerAddrFamilyMinRteWithdrawInt_Type()
)
eltexBgpPeerAddrFamilyMinRteWithdrawInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyMinRteWithdrawInt.setStatus("current")


class _EltexBgpPeerAddrFamilyReflectorClient_Type(EltexBgpPeerReflectorClientType):
    """Custom type eltexBgpPeerAddrFamilyReflectorClient based on EltexBgpPeerReflectorClientType"""
    defaultValue = 0


_EltexBgpPeerAddrFamilyReflectorClient_Type.__name__ = "EltexBgpPeerReflectorClientType"
_EltexBgpPeerAddrFamilyReflectorClient_Object = MibTableColumn
eltexBgpPeerAddrFamilyReflectorClient = _EltexBgpPeerAddrFamilyReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 12),
    _EltexBgpPeerAddrFamilyReflectorClient_Type()
)
eltexBgpPeerAddrFamilyReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyReflectorClient.setStatus("current")
_EltexBgpPeerAddrFamilyRouteMapIn_Type = DisplayString
_EltexBgpPeerAddrFamilyRouteMapIn_Object = MibTableColumn
eltexBgpPeerAddrFamilyRouteMapIn = _EltexBgpPeerAddrFamilyRouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 13),
    _EltexBgpPeerAddrFamilyRouteMapIn_Type()
)
eltexBgpPeerAddrFamilyRouteMapIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyRouteMapIn.setStatus("current")
_EltexBgpPeerAddrFamilyRouteMapOut_Type = DisplayString
_EltexBgpPeerAddrFamilyRouteMapOut_Object = MibTableColumn
eltexBgpPeerAddrFamilyRouteMapOut = _EltexBgpPeerAddrFamilyRouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 2, 1, 14),
    _EltexBgpPeerAddrFamilyRouteMapOut_Type()
)
eltexBgpPeerAddrFamilyRouteMapOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyRouteMapOut.setStatus("current")
_EltexBgpPeerStatusTable_Object = MibTable
eltexBgpPeerStatusTable = _EltexBgpPeerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    eltexBgpPeerStatusTable.setStatus("current")
_EltexBgpPeerStatusEntry_Object = MibTableRow
eltexBgpPeerStatusEntry = _EltexBgpPeerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1)
)
eltexBgpPeerStatusEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddrType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    eltexBgpPeerStatusEntry.setStatus("current")
_EltexBgpPeerStatusIdentifier_Type = EltexBgpIdentifier
_EltexBgpPeerStatusIdentifier_Object = MibTableColumn
eltexBgpPeerStatusIdentifier = _EltexBgpPeerStatusIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 1),
    _EltexBgpPeerStatusIdentifier_Type()
)
eltexBgpPeerStatusIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusIdentifier.setStatus("current")
_EltexBgpPeerStatusState_Type = EltexBgpPeerStates
_EltexBgpPeerStatusState_Object = MibTableColumn
eltexBgpPeerStatusState = _EltexBgpPeerStatusState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 2),
    _EltexBgpPeerStatusState_Type()
)
eltexBgpPeerStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusState.setStatus("current")
_EltexBgpPeerStatusDynamicPeer_Type = TruthValue
_EltexBgpPeerStatusDynamicPeer_Object = MibTableColumn
eltexBgpPeerStatusDynamicPeer = _EltexBgpPeerStatusDynamicPeer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 3),
    _EltexBgpPeerStatusDynamicPeer_Type()
)
eltexBgpPeerStatusDynamicPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusDynamicPeer.setStatus("current")
_EltexBgpPeerStatusRemoteAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpPeerStatusRemoteAs_Object = MibTableColumn
eltexBgpPeerStatusRemoteAs = _EltexBgpPeerStatusRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 4),
    _EltexBgpPeerStatusRemoteAs_Type()
)
eltexBgpPeerStatusRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusRemoteAs.setStatus("current")
_EltexBgpPeerStatusPeerIndex_Type = Unsigned32
_EltexBgpPeerStatusPeerIndex_Object = MibTableColumn
eltexBgpPeerStatusPeerIndex = _EltexBgpPeerStatusPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 5),
    _EltexBgpPeerStatusPeerIndex_Type()
)
eltexBgpPeerStatusPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusPeerIndex.setStatus("current")
_EltexBgpPeerStatusCapsSupport_Type = TruthValue
_EltexBgpPeerStatusCapsSupport_Object = MibTableColumn
eltexBgpPeerStatusCapsSupport = _EltexBgpPeerStatusCapsSupport_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 6),
    _EltexBgpPeerStatusCapsSupport_Type()
)
eltexBgpPeerStatusCapsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusCapsSupport.setStatus("current")


class _EltexBgpPeerStatusLastError_Type(OctetString):
    """Custom type eltexBgpPeerStatusLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_EltexBgpPeerStatusLastError_Type.__name__ = "OctetString"
_EltexBgpPeerStatusLastError_Object = MibTableColumn
eltexBgpPeerStatusLastError = _EltexBgpPeerStatusLastError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 7),
    _EltexBgpPeerStatusLastError_Type()
)
eltexBgpPeerStatusLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastError.setStatus("current")
_EltexBgpPeerStatusLastErrorDataLen_Type = Unsigned32
_EltexBgpPeerStatusLastErrorDataLen_Object = MibTableColumn
eltexBgpPeerStatusLastErrorDataLen = _EltexBgpPeerStatusLastErrorDataLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 8),
    _EltexBgpPeerStatusLastErrorDataLen_Type()
)
eltexBgpPeerStatusLastErrorDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastErrorDataLen.setStatus("current")


class _EltexBgpPeerStatusLastErrorData_Type(OctetString):
    """Custom type eltexBgpPeerStatusLastErrorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_EltexBgpPeerStatusLastErrorData_Type.__name__ = "OctetString"
_EltexBgpPeerStatusLastErrorData_Object = MibTableColumn
eltexBgpPeerStatusLastErrorData = _EltexBgpPeerStatusLastErrorData_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 9),
    _EltexBgpPeerStatusLastErrorData_Type()
)
eltexBgpPeerStatusLastErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastErrorData.setStatus("current")
_EltexBgpPeerStatusFsmEstablishedTime_Type = Gauge32
_EltexBgpPeerStatusFsmEstablishedTime_Object = MibTableColumn
eltexBgpPeerStatusFsmEstablishedTime = _EltexBgpPeerStatusFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 10),
    _EltexBgpPeerStatusFsmEstablishedTime_Type()
)
eltexBgpPeerStatusFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusFsmEstablishedTime.setStatus("current")
_EltexBgpPeerStatusInUpdatesElpsTime_Type = Gauge32
_EltexBgpPeerStatusInUpdatesElpsTime_Object = MibTableColumn
eltexBgpPeerStatusInUpdatesElpsTime = _EltexBgpPeerStatusInUpdatesElpsTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 11),
    _EltexBgpPeerStatusInUpdatesElpsTime_Type()
)
eltexBgpPeerStatusInUpdatesElpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInUpdatesElpsTime.setStatus("current")
_EltexBgpPeerStatusHoldTime_Type = Integer32
_EltexBgpPeerStatusHoldTime_Object = MibTableColumn
eltexBgpPeerStatusHoldTime = _EltexBgpPeerStatusHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 12),
    _EltexBgpPeerStatusHoldTime_Type()
)
eltexBgpPeerStatusHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusHoldTime.setStatus("current")
_EltexBgpPeerStatusKeepAlive_Type = Integer32
_EltexBgpPeerStatusKeepAlive_Object = MibTableColumn
eltexBgpPeerStatusKeepAlive = _EltexBgpPeerStatusKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 13),
    _EltexBgpPeerStatusKeepAlive_Type()
)
eltexBgpPeerStatusKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusKeepAlive.setStatus("current")
_EltexBgpPeerStatusInOpens_Type = Counter32
_EltexBgpPeerStatusInOpens_Object = MibTableColumn
eltexBgpPeerStatusInOpens = _EltexBgpPeerStatusInOpens_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 14),
    _EltexBgpPeerStatusInOpens_Type()
)
eltexBgpPeerStatusInOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInOpens.setStatus("current")
_EltexBgpPeerStatusOutOpens_Type = Counter32
_EltexBgpPeerStatusOutOpens_Object = MibTableColumn
eltexBgpPeerStatusOutOpens = _EltexBgpPeerStatusOutOpens_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 15),
    _EltexBgpPeerStatusOutOpens_Type()
)
eltexBgpPeerStatusOutOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutOpens.setStatus("current")
_EltexBgpPeerStatusInNotifications_Type = Counter32
_EltexBgpPeerStatusInNotifications_Object = MibTableColumn
eltexBgpPeerStatusInNotifications = _EltexBgpPeerStatusInNotifications_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 16),
    _EltexBgpPeerStatusInNotifications_Type()
)
eltexBgpPeerStatusInNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInNotifications.setStatus("current")
_EltexBgpPeerStatusOutNotifications_Type = Counter32
_EltexBgpPeerStatusOutNotifications_Object = MibTableColumn
eltexBgpPeerStatusOutNotifications = _EltexBgpPeerStatusOutNotifications_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 17),
    _EltexBgpPeerStatusOutNotifications_Type()
)
eltexBgpPeerStatusOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutNotifications.setStatus("current")
_EltexBgpPeerStatusInUpdates_Type = Counter32
_EltexBgpPeerStatusInUpdates_Object = MibTableColumn
eltexBgpPeerStatusInUpdates = _EltexBgpPeerStatusInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 18),
    _EltexBgpPeerStatusInUpdates_Type()
)
eltexBgpPeerStatusInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInUpdates.setStatus("current")
_EltexBgpPeerStatusOutUpdates_Type = Counter32
_EltexBgpPeerStatusOutUpdates_Object = MibTableColumn
eltexBgpPeerStatusOutUpdates = _EltexBgpPeerStatusOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 19),
    _EltexBgpPeerStatusOutUpdates_Type()
)
eltexBgpPeerStatusOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutUpdates.setStatus("current")
_EltexBgpPeerStatusInKeepalives_Type = Counter32
_EltexBgpPeerStatusInKeepalives_Object = MibTableColumn
eltexBgpPeerStatusInKeepalives = _EltexBgpPeerStatusInKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 20),
    _EltexBgpPeerStatusInKeepalives_Type()
)
eltexBgpPeerStatusInKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInKeepalives.setStatus("current")
_EltexBgpPeerStatusOutKeepalives_Type = Counter32
_EltexBgpPeerStatusOutKeepalives_Object = MibTableColumn
eltexBgpPeerStatusOutKeepalives = _EltexBgpPeerStatusOutKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 21),
    _EltexBgpPeerStatusOutKeepalives_Type()
)
eltexBgpPeerStatusOutKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutKeepalives.setStatus("current")
_EltexBgpPeerStatusInRefreshes_Type = Counter32
_EltexBgpPeerStatusInRefreshes_Object = MibTableColumn
eltexBgpPeerStatusInRefreshes = _EltexBgpPeerStatusInRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 22),
    _EltexBgpPeerStatusInRefreshes_Type()
)
eltexBgpPeerStatusInRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInRefreshes.setStatus("current")
_EltexBgpPeerStatusOutRefreshes_Type = Counter32
_EltexBgpPeerStatusOutRefreshes_Object = MibTableColumn
eltexBgpPeerStatusOutRefreshes = _EltexBgpPeerStatusOutRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 23),
    _EltexBgpPeerStatusOutRefreshes_Type()
)
eltexBgpPeerStatusOutRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutRefreshes.setStatus("current")
_EltexBgpPeerStatusInTotalMessages_Type = Counter32
_EltexBgpPeerStatusInTotalMessages_Object = MibTableColumn
eltexBgpPeerStatusInTotalMessages = _EltexBgpPeerStatusInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 24),
    _EltexBgpPeerStatusInTotalMessages_Type()
)
eltexBgpPeerStatusInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInTotalMessages.setStatus("current")
_EltexBgpPeerStatusOutTotalMessages_Type = Counter32
_EltexBgpPeerStatusOutTotalMessages_Object = MibTableColumn
eltexBgpPeerStatusOutTotalMessages = _EltexBgpPeerStatusOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 25),
    _EltexBgpPeerStatusOutTotalMessages_Type()
)
eltexBgpPeerStatusOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutTotalMessages.setStatus("current")
_EltexBgpPeerStatusFsmEstTransitions_Type = Counter32
_EltexBgpPeerStatusFsmEstTransitions_Object = MibTableColumn
eltexBgpPeerStatusFsmEstTransitions = _EltexBgpPeerStatusFsmEstTransitions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 26),
    _EltexBgpPeerStatusFsmEstTransitions_Type()
)
eltexBgpPeerStatusFsmEstTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusFsmEstTransitions.setStatus("current")
_EltexBgpPeerStatusConnectRetryCount_Type = Counter32
_EltexBgpPeerStatusConnectRetryCount_Object = MibTableColumn
eltexBgpPeerStatusConnectRetryCount = _EltexBgpPeerStatusConnectRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 27),
    _EltexBgpPeerStatusConnectRetryCount_Type()
)
eltexBgpPeerStatusConnectRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusConnectRetryCount.setStatus("current")
_EltexBgpPeerStatusClearCnts_Type = TruthValue
_EltexBgpPeerStatusClearCnts_Object = MibTableColumn
eltexBgpPeerStatusClearCnts = _EltexBgpPeerStatusClearCnts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 28),
    _EltexBgpPeerStatusClearCnts_Type()
)
eltexBgpPeerStatusClearCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusClearCnts.setStatus("current")
_EltexBgpPeerStatusRtRefresh_Type = TruthValue
_EltexBgpPeerStatusRtRefresh_Object = MibTableColumn
eltexBgpPeerStatusRtRefresh = _EltexBgpPeerStatusRtRefresh_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 29),
    _EltexBgpPeerStatusRtRefresh_Type()
)
eltexBgpPeerStatusRtRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusRtRefresh.setStatus("current")


class _EltexBgpPeerStatusLastErrorRcvd_Type(OctetString):
    """Custom type eltexBgpPeerStatusLastErrorRcvd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_EltexBgpPeerStatusLastErrorRcvd_Type.__name__ = "OctetString"
_EltexBgpPeerStatusLastErrorRcvd_Object = MibTableColumn
eltexBgpPeerStatusLastErrorRcvd = _EltexBgpPeerStatusLastErrorRcvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 30),
    _EltexBgpPeerStatusLastErrorRcvd_Type()
)
eltexBgpPeerStatusLastErrorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastErrorRcvd.setStatus("current")
_EltexBgpPeerStatusLastErrorRcvdTime_Type = TimeStamp
_EltexBgpPeerStatusLastErrorRcvdTime_Object = MibTableColumn
eltexBgpPeerStatusLastErrorRcvdTime = _EltexBgpPeerStatusLastErrorRcvdTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 31),
    _EltexBgpPeerStatusLastErrorRcvdTime_Type()
)
eltexBgpPeerStatusLastErrorRcvdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastErrorRcvdTime.setStatus("current")


class _EltexBgpPeerStatusLastErrorSent_Type(OctetString):
    """Custom type eltexBgpPeerStatusLastErrorSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_EltexBgpPeerStatusLastErrorSent_Type.__name__ = "OctetString"
_EltexBgpPeerStatusLastErrorSent_Object = MibTableColumn
eltexBgpPeerStatusLastErrorSent = _EltexBgpPeerStatusLastErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 32),
    _EltexBgpPeerStatusLastErrorSent_Type()
)
eltexBgpPeerStatusLastErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastErrorSent.setStatus("current")
_EltexBgpPeerStatusLastErrorSentTime_Type = TimeStamp
_EltexBgpPeerStatusLastErrorSentTime_Object = MibTableColumn
eltexBgpPeerStatusLastErrorSentTime = _EltexBgpPeerStatusLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 33),
    _EltexBgpPeerStatusLastErrorSentTime_Type()
)
eltexBgpPeerStatusLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastErrorSentTime.setStatus("current")
_EltexBgpPeerStatusLastState_Type = EltexBgpPeerStates
_EltexBgpPeerStatusLastState_Object = MibTableColumn
eltexBgpPeerStatusLastState = _EltexBgpPeerStatusLastState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 34),
    _EltexBgpPeerStatusLastState_Type()
)
eltexBgpPeerStatusLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastState.setStatus("current")
_EltexBgpPeerStatusLastEvent_Type = EltexBgpPeerEvents
_EltexBgpPeerStatusLastEvent_Object = MibTableColumn
eltexBgpPeerStatusLastEvent = _EltexBgpPeerStatusLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 35),
    _EltexBgpPeerStatusLastEvent_Type()
)
eltexBgpPeerStatusLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusLastEvent.setStatus("current")
_EltexBgpPeerStatusCapsSent_Type = EltexBgpCapabilities
_EltexBgpPeerStatusCapsSent_Object = MibTableColumn
eltexBgpPeerStatusCapsSent = _EltexBgpPeerStatusCapsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 36),
    _EltexBgpPeerStatusCapsSent_Type()
)
eltexBgpPeerStatusCapsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusCapsSent.setStatus("current")
_EltexBgpPeerStatusCapsRcvd_Type = EltexBgpCapabilities
_EltexBgpPeerStatusCapsRcvd_Object = MibTableColumn
eltexBgpPeerStatusCapsRcvd = _EltexBgpPeerStatusCapsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 37),
    _EltexBgpPeerStatusCapsRcvd_Type()
)
eltexBgpPeerStatusCapsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusCapsRcvd.setStatus("current")
_EltexBgpPeerStatusCapsNegotiated_Type = EltexBgpCapabilities
_EltexBgpPeerStatusCapsNegotiated_Object = MibTableColumn
eltexBgpPeerStatusCapsNegotiated = _EltexBgpPeerStatusCapsNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 38),
    _EltexBgpPeerStatusCapsNegotiated_Type()
)
eltexBgpPeerStatusCapsNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusCapsNegotiated.setStatus("current")
_EltexBgpPeerStatusRcvdMsgElpsTime_Type = TimeInterval
_EltexBgpPeerStatusRcvdMsgElpsTime_Object = MibTableColumn
eltexBgpPeerStatusRcvdMsgElpsTime = _EltexBgpPeerStatusRcvdMsgElpsTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 39),
    _EltexBgpPeerStatusRcvdMsgElpsTime_Type()
)
eltexBgpPeerStatusRcvdMsgElpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusRcvdMsgElpsTime.setStatus("current")
_EltexBgpPeerStatusIdleHoldRemTime_Type = TimeInterval
_EltexBgpPeerStatusIdleHoldRemTime_Object = MibTableColumn
eltexBgpPeerStatusIdleHoldRemTime = _EltexBgpPeerStatusIdleHoldRemTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 40),
    _EltexBgpPeerStatusIdleHoldRemTime_Type()
)
eltexBgpPeerStatusIdleHoldRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusIdleHoldRemTime.setStatus("current")
_EltexBgpPeerStatusRouteRefrSent_Type = Counter32
_EltexBgpPeerStatusRouteRefrSent_Object = MibTableColumn
eltexBgpPeerStatusRouteRefrSent = _EltexBgpPeerStatusRouteRefrSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 41),
    _EltexBgpPeerStatusRouteRefrSent_Type()
)
eltexBgpPeerStatusRouteRefrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusRouteRefrSent.setStatus("current")
_EltexBgpPeerStatusRouteRefrRcvd_Type = Counter32
_EltexBgpPeerStatusRouteRefrRcvd_Object = MibTableColumn
eltexBgpPeerStatusRouteRefrRcvd = _EltexBgpPeerStatusRouteRefrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 42),
    _EltexBgpPeerStatusRouteRefrRcvd_Type()
)
eltexBgpPeerStatusRouteRefrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusRouteRefrRcvd.setStatus("current")
_EltexBgpPeerStatusSelLocalAddrType_Type = InetAddressType
_EltexBgpPeerStatusSelLocalAddrType_Object = MibTableColumn
eltexBgpPeerStatusSelLocalAddrType = _EltexBgpPeerStatusSelLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 43),
    _EltexBgpPeerStatusSelLocalAddrType_Type()
)
eltexBgpPeerStatusSelLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusSelLocalAddrType.setStatus("current")
_EltexBgpPeerStatusSelLocalAddr_Type = InetAddress
_EltexBgpPeerStatusSelLocalAddr_Object = MibTableColumn
eltexBgpPeerStatusSelLocalAddr = _EltexBgpPeerStatusSelLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 44),
    _EltexBgpPeerStatusSelLocalAddr_Type()
)
eltexBgpPeerStatusSelLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusSelLocalAddr.setStatus("current")
_EltexBgpPeerStatusSelLocalPort_Type = InetPortNumber
_EltexBgpPeerStatusSelLocalPort_Object = MibTableColumn
eltexBgpPeerStatusSelLocalPort = _EltexBgpPeerStatusSelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 45),
    _EltexBgpPeerStatusSelLocalPort_Type()
)
eltexBgpPeerStatusSelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusSelLocalPort.setStatus("current")
_EltexBgpPeerStatusSelRemotePort_Type = InetPortNumber
_EltexBgpPeerStatusSelRemotePort_Object = MibTableColumn
eltexBgpPeerStatusSelRemotePort = _EltexBgpPeerStatusSelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 46),
    _EltexBgpPeerStatusSelRemotePort_Type()
)
eltexBgpPeerStatusSelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusSelRemotePort.setStatus("current")
_EltexBgpPeerStatusSelLocalAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpPeerStatusSelLocalAs_Object = MibTableColumn
eltexBgpPeerStatusSelLocalAs = _EltexBgpPeerStatusSelLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 47),
    _EltexBgpPeerStatusSelLocalAs_Type()
)
eltexBgpPeerStatusSelLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusSelLocalAs.setStatus("current")
_EltexBgpPeerStatusSelRemoteAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpPeerStatusSelRemoteAs_Object = MibTableColumn
eltexBgpPeerStatusSelRemoteAs = _EltexBgpPeerStatusSelRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 48),
    _EltexBgpPeerStatusSelRemoteAs_Type()
)
eltexBgpPeerStatusSelRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusSelRemoteAs.setStatus("current")
_EltexBgpPeerStatusInPrfxes_Type = Gauge32
_EltexBgpPeerStatusInPrfxes_Object = MibTableColumn
eltexBgpPeerStatusInPrfxes = _EltexBgpPeerStatusInPrfxes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 49),
    _EltexBgpPeerStatusInPrfxes_Type()
)
eltexBgpPeerStatusInPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInPrfxes.setStatus("current")
_EltexBgpPeerStatusOutPrfxes_Type = Gauge32
_EltexBgpPeerStatusOutPrfxes_Object = MibTableColumn
eltexBgpPeerStatusOutPrfxes = _EltexBgpPeerStatusOutPrfxes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 50),
    _EltexBgpPeerStatusOutPrfxes_Type()
)
eltexBgpPeerStatusOutPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutPrfxes.setStatus("current")
_EltexBgpPeerStatusOutPrfxesAdvertised_Type = Gauge32
_EltexBgpPeerStatusOutPrfxesAdvertised_Object = MibTableColumn
eltexBgpPeerStatusOutPrfxesAdvertised = _EltexBgpPeerStatusOutPrfxesAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 51),
    _EltexBgpPeerStatusOutPrfxesAdvertised_Type()
)
eltexBgpPeerStatusOutPrfxesAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutPrfxesAdvertised.setStatus("current")
_EltexBgpPeerStatusConfigState_Type = EltexBgpPeerConfigStates
_EltexBgpPeerStatusConfigState_Object = MibTableColumn
eltexBgpPeerStatusConfigState = _EltexBgpPeerStatusConfigState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 52),
    _EltexBgpPeerStatusConfigState_Type()
)
eltexBgpPeerStatusConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusConfigState.setStatus("current")
_EltexBgpPeerStatusConnectRetryInt_Type = Unsigned32
_EltexBgpPeerStatusConnectRetryInt_Object = MibTableColumn
eltexBgpPeerStatusConnectRetryInt = _EltexBgpPeerStatusConnectRetryInt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 53),
    _EltexBgpPeerStatusConnectRetryInt_Type()
)
eltexBgpPeerStatusConnectRetryInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusConnectRetryInt.setStatus("current")
_EltexBgpPeerStatusConfigPassive_Type = TruthValue
_EltexBgpPeerStatusConfigPassive_Object = MibTableColumn
eltexBgpPeerStatusConfigPassive = _EltexBgpPeerStatusConfigPassive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 54),
    _EltexBgpPeerStatusConfigPassive_Type()
)
eltexBgpPeerStatusConfigPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusConfigPassive.setStatus("current")
_EltexBgpPeerStatusConfigOpenDelay_Type = Unsigned32
_EltexBgpPeerStatusConfigOpenDelay_Object = MibTableColumn
eltexBgpPeerStatusConfigOpenDelay = _EltexBgpPeerStatusConfigOpenDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 55),
    _EltexBgpPeerStatusConfigOpenDelay_Type()
)
eltexBgpPeerStatusConfigOpenDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusConfigOpenDelay.setStatus("current")
_EltexBgpPeerStatusConfigIdleHold_Type = Unsigned32
_EltexBgpPeerStatusConfigIdleHold_Object = MibTableColumn
eltexBgpPeerStatusConfigIdleHold = _EltexBgpPeerStatusConfigIdleHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 56),
    _EltexBgpPeerStatusConfigIdleHold_Type()
)
eltexBgpPeerStatusConfigIdleHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusConfigIdleHold.setStatus("current")
_EltexBgpPeerStatusTtl_Type = Integer32
_EltexBgpPeerStatusTtl_Object = MibTableColumn
eltexBgpPeerStatusTtl = _EltexBgpPeerStatusTtl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 57),
    _EltexBgpPeerStatusTtl_Type()
)
eltexBgpPeerStatusTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusTtl.setStatus("current")
_EltexBgpPeerStatusHoldTimeConfigd_Type = Unsigned32
_EltexBgpPeerStatusHoldTimeConfigd_Object = MibTableColumn
eltexBgpPeerStatusHoldTimeConfigd = _EltexBgpPeerStatusHoldTimeConfigd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 58),
    _EltexBgpPeerStatusHoldTimeConfigd_Type()
)
eltexBgpPeerStatusHoldTimeConfigd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusHoldTimeConfigd.setStatus("current")
_EltexBgpPeerStatusKeepAliveConfigd_Type = Unsigned32
_EltexBgpPeerStatusKeepAliveConfigd_Object = MibTableColumn
eltexBgpPeerStatusKeepAliveConfigd = _EltexBgpPeerStatusKeepAliveConfigd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 59),
    _EltexBgpPeerStatusKeepAliveConfigd_Type()
)
eltexBgpPeerStatusKeepAliveConfigd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusKeepAliveConfigd.setStatus("current")


class _EltexBgpPeerStatusResendAllRoutes_Type(TruthValue):
    """Custom type eltexBgpPeerStatusResendAllRoutes based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerStatusResendAllRoutes_Type.__name__ = "TruthValue"
_EltexBgpPeerStatusResendAllRoutes_Object = MibTableColumn
eltexBgpPeerStatusResendAllRoutes = _EltexBgpPeerStatusResendAllRoutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 60),
    _EltexBgpPeerStatusResendAllRoutes_Type()
)
eltexBgpPeerStatusResendAllRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusResendAllRoutes.setStatus("current")
_EltexBgpPeerStatusOutUpdateElpsTime_Type = Gauge32
_EltexBgpPeerStatusOutUpdateElpsTime_Object = MibTableColumn
eltexBgpPeerStatusOutUpdateElpsTime = _EltexBgpPeerStatusOutUpdateElpsTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 61),
    _EltexBgpPeerStatusOutUpdateElpsTime_Type()
)
eltexBgpPeerStatusOutUpdateElpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutUpdateElpsTime.setStatus("current")
_EltexBgpPeerStatusOutPrfxesDenied_Type = Counter32
_EltexBgpPeerStatusOutPrfxesDenied_Object = MibTableColumn
eltexBgpPeerStatusOutPrfxesDenied = _EltexBgpPeerStatusOutPrfxesDenied_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 62),
    _EltexBgpPeerStatusOutPrfxesDenied_Type()
)
eltexBgpPeerStatusOutPrfxesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutPrfxesDenied.setStatus("current")
_EltexBgpPeerStatusOutPrfxesImpWdr_Type = Counter32
_EltexBgpPeerStatusOutPrfxesImpWdr_Object = MibTableColumn
eltexBgpPeerStatusOutPrfxesImpWdr = _EltexBgpPeerStatusOutPrfxesImpWdr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 63),
    _EltexBgpPeerStatusOutPrfxesImpWdr_Type()
)
eltexBgpPeerStatusOutPrfxesImpWdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutPrfxesImpWdr.setStatus("current")
_EltexBgpPeerStatusOutPrfxesExpWdr_Type = Counter32
_EltexBgpPeerStatusOutPrfxesExpWdr_Object = MibTableColumn
eltexBgpPeerStatusOutPrfxesExpWdr = _EltexBgpPeerStatusOutPrfxesExpWdr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 64),
    _EltexBgpPeerStatusOutPrfxesExpWdr_Type()
)
eltexBgpPeerStatusOutPrfxesExpWdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusOutPrfxesExpWdr.setStatus("current")
_EltexBgpPeerStatusInPrfxesImpWdr_Type = Counter32
_EltexBgpPeerStatusInPrfxesImpWdr_Object = MibTableColumn
eltexBgpPeerStatusInPrfxesImpWdr = _EltexBgpPeerStatusInPrfxesImpWdr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 65),
    _EltexBgpPeerStatusInPrfxesImpWdr_Type()
)
eltexBgpPeerStatusInPrfxesImpWdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInPrfxesImpWdr.setStatus("current")
_EltexBgpPeerStatusInPrfxesExpWdr_Type = Counter32
_EltexBgpPeerStatusInPrfxesExpWdr_Object = MibTableColumn
eltexBgpPeerStatusInPrfxesExpWdr = _EltexBgpPeerStatusInPrfxesExpWdr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 66),
    _EltexBgpPeerStatusInPrfxesExpWdr_Type()
)
eltexBgpPeerStatusInPrfxesExpWdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusInPrfxesExpWdr.setStatus("current")
_EltexBgpPeerStatusReceivedHoldTime_Type = Integer32
_EltexBgpPeerStatusReceivedHoldTime_Object = MibTableColumn
eltexBgpPeerStatusReceivedHoldTime = _EltexBgpPeerStatusReceivedHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 67),
    _EltexBgpPeerStatusReceivedHoldTime_Type()
)
eltexBgpPeerStatusReceivedHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusReceivedHoldTime.setStatus("current")
_EltexBgpPeerStatusDropSession_Type = TruthValue
_EltexBgpPeerStatusDropSession_Object = MibTableColumn
eltexBgpPeerStatusDropSession = _EltexBgpPeerStatusDropSession_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 68),
    _EltexBgpPeerStatusDropSession_Type()
)
eltexBgpPeerStatusDropSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusDropSession.setStatus("current")


class _EltexBgpPeerStatusCeaseErrorSubcode_Type(EltexBgpCeaseErrorSubcode):
    """Custom type eltexBgpPeerStatusCeaseErrorSubcode based on EltexBgpCeaseErrorSubcode"""
    defaultValue = 0


_EltexBgpPeerStatusCeaseErrorSubcode_Type.__name__ = "EltexBgpCeaseErrorSubcode"
_EltexBgpPeerStatusCeaseErrorSubcode_Object = MibTableColumn
eltexBgpPeerStatusCeaseErrorSubcode = _EltexBgpPeerStatusCeaseErrorSubcode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 69),
    _EltexBgpPeerStatusCeaseErrorSubcode_Type()
)
eltexBgpPeerStatusCeaseErrorSubcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusCeaseErrorSubcode.setStatus("current")
_EltexBgpPeerStatusBfdStatus_Type = EltexBfdSessionStatus
_EltexBgpPeerStatusBfdStatus_Object = MibTableColumn
eltexBgpPeerStatusBfdStatus = _EltexBgpPeerStatusBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 3, 1, 70),
    _EltexBgpPeerStatusBfdStatus_Type()
)
eltexBgpPeerStatusBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerStatusBfdStatus.setStatus("current")
_EltexBgpPeerAddrFamilyStatusTable_Object = MibTable
eltexBgpPeerAddrFamilyStatusTable = _EltexBgpPeerAddrFamilyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusTable.setStatus("current")
_EltexBgpPeerAddrFamilyStatusEntry_Object = MibTableRow
eltexBgpPeerAddrFamilyStatusEntry = _EltexBgpPeerAddrFamilyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4, 1)
)
eltexBgpPeerAddrFamilyStatusEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddrType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerRemoteAddr"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerAddrFamilyAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerAddrFamilySafi"),
)
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusEntry.setStatus("current")


class _EltexBgpPeerAddrFamilyStatusRtRefresh_Type(TruthValue):
    """Custom type eltexBgpPeerAddrFamilyStatusRtRefresh based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerAddrFamilyStatusRtRefresh_Type.__name__ = "TruthValue"
_EltexBgpPeerAddrFamilyStatusRtRefresh_Object = MibTableColumn
eltexBgpPeerAddrFamilyStatusRtRefresh = _EltexBgpPeerAddrFamilyStatusRtRefresh_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4, 1, 1),
    _EltexBgpPeerAddrFamilyStatusRtRefresh_Type()
)
eltexBgpPeerAddrFamilyStatusRtRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusRtRefresh.setStatus("current")
_EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Type = EltexBgpAddPathSrCap
_EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Object = MibTableColumn
eltexBgpPeerAddrFamilyStatusAddPathCapNeg = _EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4, 1, 2),
    _EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Type()
)
eltexBgpPeerAddrFamilyStatusAddPathCapNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusAddPathCapNeg.setStatus("current")
_EltexBgpPeerAddrFamilyStatusReflectorClient_Type = EltexBgpPeerReflectorClientType
_EltexBgpPeerAddrFamilyStatusReflectorClient_Object = MibTableColumn
eltexBgpPeerAddrFamilyStatusReflectorClient = _EltexBgpPeerAddrFamilyStatusReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4, 1, 3),
    _EltexBgpPeerAddrFamilyStatusReflectorClient_Type()
)
eltexBgpPeerAddrFamilyStatusReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusReflectorClient.setStatus("current")
_EltexBgpPeerAddrFamilyStatusUpdateGroup_Type = Unsigned32
_EltexBgpPeerAddrFamilyStatusUpdateGroup_Object = MibTableColumn
eltexBgpPeerAddrFamilyStatusUpdateGroup = _EltexBgpPeerAddrFamilyStatusUpdateGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4, 1, 4),
    _EltexBgpPeerAddrFamilyStatusUpdateGroup_Type()
)
eltexBgpPeerAddrFamilyStatusUpdateGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusUpdateGroup.setStatus("current")


class _EltexBgpPeerAddrFamilyStatusResendAllRoutes_Type(TruthValue):
    """Custom type eltexBgpPeerAddrFamilyStatusResendAllRoutes based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerAddrFamilyStatusResendAllRoutes_Type.__name__ = "TruthValue"
_EltexBgpPeerAddrFamilyStatusResendAllRoutes_Object = MibTableColumn
eltexBgpPeerAddrFamilyStatusResendAllRoutes = _EltexBgpPeerAddrFamilyStatusResendAllRoutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 1, 4, 1, 5),
    _EltexBgpPeerAddrFamilyStatusResendAllRoutes_Type()
)
eltexBgpPeerAddrFamilyStatusResendAllRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerAddrFamilyStatusResendAllRoutes.setStatus("current")
_EltexBgpPeerGroup_ObjectIdentity = ObjectIdentity
eltexBgpPeerGroup = _EltexBgpPeerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2)
)
_EltexBgpPeerGroupTable_Object = MibTable
eltexBgpPeerGroupTable = _EltexBgpPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltexBgpPeerGroupTable.setStatus("current")
_EltexBgpPeerGroupEntry_Object = MibTableRow
eltexBgpPeerGroupEntry = _EltexBgpPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1)
)
eltexBgpPeerGroupEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerGroupName"),
)
if mibBuilder.loadTexts:
    eltexBgpPeerGroupEntry.setStatus("current")
_EltexBgpPeerGroupName_Type = DisplayString
_EltexBgpPeerGroupName_Object = MibTableColumn
eltexBgpPeerGroupName = _EltexBgpPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 1),
    _EltexBgpPeerGroupName_Type()
)
eltexBgpPeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupName.setStatus("current")
_EltexBgpPeerGroupRowStatus_Type = RowStatus
_EltexBgpPeerGroupRowStatus_Object = MibTableColumn
eltexBgpPeerGroupRowStatus = _EltexBgpPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 2),
    _EltexBgpPeerGroupRowStatus_Type()
)
eltexBgpPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupRowStatus.setStatus("current")
_EltexBgpPeerGroupRemoteAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpPeerGroupRemoteAs_Object = MibTableColumn
eltexBgpPeerGroupRemoteAs = _EltexBgpPeerGroupRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 3),
    _EltexBgpPeerGroupRemoteAs_Type()
)
eltexBgpPeerGroupRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupRemoteAs.setStatus("current")


class _EltexBgpPeerGroupSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type eltexBgpPeerGroupSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_EltexBgpPeerGroupSourceInterface_Type.__name__ = "InterfaceIndexOrZero"
_EltexBgpPeerGroupSourceInterface_Object = MibTableColumn
eltexBgpPeerGroupSourceInterface = _EltexBgpPeerGroupSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 4),
    _EltexBgpPeerGroupSourceInterface_Type()
)
eltexBgpPeerGroupSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupSourceInterface.setStatus("current")


class _EltexBgpPeerGroupNxtHopSlf_Type(TruthValue):
    """Custom type eltexBgpPeerGroupNxtHopSlf based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerGroupNxtHopSlf_Type.__name__ = "TruthValue"
_EltexBgpPeerGroupNxtHopSlf_Object = MibTableColumn
eltexBgpPeerGroupNxtHopSlf = _EltexBgpPeerGroupNxtHopSlf_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 5),
    _EltexBgpPeerGroupNxtHopSlf_Type()
)
eltexBgpPeerGroupNxtHopSlf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupNxtHopSlf.setStatus("current")


class _EltexBgpPeerGroupConfigMaxPrfx_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupConfigMaxPrfx based on Unsigned32"""
    defaultValue = 0


_EltexBgpPeerGroupConfigMaxPrfx_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupConfigMaxPrfx_Object = MibTableColumn
eltexBgpPeerGroupConfigMaxPrfx = _EltexBgpPeerGroupConfigMaxPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 6),
    _EltexBgpPeerGroupConfigMaxPrfx_Type()
)
eltexBgpPeerGroupConfigMaxPrfx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupConfigMaxPrfx.setStatus("current")


class _EltexBgpPeerGroupConfigDropWarn_Type(EltexBgpConfigDropOrWarn):
    """Custom type eltexBgpPeerGroupConfigDropWarn based on EltexBgpConfigDropOrWarn"""
    defaultValue = 2


_EltexBgpPeerGroupConfigDropWarn_Type.__name__ = "EltexBgpConfigDropOrWarn"
_EltexBgpPeerGroupConfigDropWarn_Object = MibTableColumn
eltexBgpPeerGroupConfigDropWarn = _EltexBgpPeerGroupConfigDropWarn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 7),
    _EltexBgpPeerGroupConfigDropWarn_Type()
)
eltexBgpPeerGroupConfigDropWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupConfigDropWarn.setStatus("current")


class _EltexBgpPeerGroupMaxPrfxHold_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupMaxPrfxHold based on Unsigned32"""
    defaultValue = 90


_EltexBgpPeerGroupMaxPrfxHold_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupMaxPrfxHold_Object = MibTableColumn
eltexBgpPeerGroupMaxPrfxHold = _EltexBgpPeerGroupMaxPrfxHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 8),
    _EltexBgpPeerGroupMaxPrfxHold_Type()
)
eltexBgpPeerGroupMaxPrfxHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupMaxPrfxHold.setStatus("current")


class _EltexBgpPeerGroupConfigThreshold_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupConfigThreshold based on Unsigned32"""
    defaultValue = 75


_EltexBgpPeerGroupConfigThreshold_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupConfigThreshold_Object = MibTableColumn
eltexBgpPeerGroupConfigThreshold = _EltexBgpPeerGroupConfigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 9),
    _EltexBgpPeerGroupConfigThreshold_Type()
)
eltexBgpPeerGroupConfigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupConfigThreshold.setStatus("current")


class _EltexBgpPeerGroupConnectRetryInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexBgpPeerGroupConnectRetryInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupConnectRetryInterval_Object = MibTableColumn
eltexBgpPeerGroupConnectRetryInterval = _EltexBgpPeerGroupConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 10),
    _EltexBgpPeerGroupConnectRetryInterval_Type()
)
eltexBgpPeerGroupConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupConnectRetryInterval.setStatus("current")


class _EltexBgpPeerGroupHoldTimeConfigd_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupHoldTimeConfigd based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerGroupHoldTimeConfigd_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupHoldTimeConfigd_Object = MibTableColumn
eltexBgpPeerGroupHoldTimeConfigd = _EltexBgpPeerGroupHoldTimeConfigd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 11),
    _EltexBgpPeerGroupHoldTimeConfigd_Type()
)
eltexBgpPeerGroupHoldTimeConfigd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupHoldTimeConfigd.setStatus("current")


class _EltexBgpPeerGroupKeepAliveConfigd_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupKeepAliveConfigd based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_EltexBgpPeerGroupKeepAliveConfigd_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupKeepAliveConfigd_Object = MibTableColumn
eltexBgpPeerGroupKeepAliveConfigd = _EltexBgpPeerGroupKeepAliveConfigd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 12),
    _EltexBgpPeerGroupKeepAliveConfigd_Type()
)
eltexBgpPeerGroupKeepAliveConfigd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupKeepAliveConfigd.setStatus("current")


class _EltexBgpPeerGroupMinRouteAdvertiseInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupMinRouteAdvertiseInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerGroupMinRouteAdvertiseInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupMinRouteAdvertiseInterval_Object = MibTableColumn
eltexBgpPeerGroupMinRouteAdvertiseInterval = _EltexBgpPeerGroupMinRouteAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 13),
    _EltexBgpPeerGroupMinRouteAdvertiseInterval_Type()
)
eltexBgpPeerGroupMinRouteAdvertiseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupMinRouteAdvertiseInterval.setStatus("current")


class _EltexBgpPeerGroupMinASOriginationInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupMinASOriginationInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerGroupMinASOriginationInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupMinASOriginationInterval_Object = MibTableColumn
eltexBgpPeerGroupMinASOriginationInterval = _EltexBgpPeerGroupMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 14),
    _EltexBgpPeerGroupMinASOriginationInterval_Type()
)
eltexBgpPeerGroupMinASOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupMinASOriginationInterval.setStatus("current")


class _EltexBgpPeerGroupMinRouteWithdrawInterval_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupMinRouteWithdrawInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexBgpPeerGroupMinRouteWithdrawInterval_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupMinRouteWithdrawInterval_Object = MibTableColumn
eltexBgpPeerGroupMinRouteWithdrawInterval = _EltexBgpPeerGroupMinRouteWithdrawInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 15),
    _EltexBgpPeerGroupMinRouteWithdrawInterval_Type()
)
eltexBgpPeerGroupMinRouteWithdrawInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupMinRouteWithdrawInterval.setStatus("current")


class _EltexBgpPeerGroupConfigOpenDelay_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupConfigOpenDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_EltexBgpPeerGroupConfigOpenDelay_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupConfigOpenDelay_Object = MibTableColumn
eltexBgpPeerGroupConfigOpenDelay = _EltexBgpPeerGroupConfigOpenDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 16),
    _EltexBgpPeerGroupConfigOpenDelay_Type()
)
eltexBgpPeerGroupConfigOpenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupConfigOpenDelay.setStatus("current")


class _EltexBgpPeerGroupConfigIdleHold_Type(Unsigned32):
    """Custom type eltexBgpPeerGroupConfigIdleHold based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_EltexBgpPeerGroupConfigIdleHold_Type.__name__ = "Unsigned32"
_EltexBgpPeerGroupConfigIdleHold_Object = MibTableColumn
eltexBgpPeerGroupConfigIdleHold = _EltexBgpPeerGroupConfigIdleHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 17),
    _EltexBgpPeerGroupConfigIdleHold_Type()
)
eltexBgpPeerGroupConfigIdleHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupConfigIdleHold.setStatus("current")
_EltexBgpPeerGroupDistListPlIn_Type = DisplayString
_EltexBgpPeerGroupDistListPlIn_Object = MibTableColumn
eltexBgpPeerGroupDistListPlIn = _EltexBgpPeerGroupDistListPlIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 18),
    _EltexBgpPeerGroupDistListPlIn_Type()
)
eltexBgpPeerGroupDistListPlIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupDistListPlIn.setStatus("current")
_EltexBgpPeerGroupDistListPlOut_Type = DisplayString
_EltexBgpPeerGroupDistListPlOut_Object = MibTableColumn
eltexBgpPeerGroupDistListPlOut = _EltexBgpPeerGroupDistListPlOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 19),
    _EltexBgpPeerGroupDistListPlOut_Type()
)
eltexBgpPeerGroupDistListPlOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupDistListPlOut.setStatus("current")


class _EltexBgpPeerGroupReflectorClient_Type(EltexBgpPeerReflectorClientType):
    """Custom type eltexBgpPeerGroupReflectorClient based on EltexBgpPeerReflectorClientType"""
    defaultValue = 0


_EltexBgpPeerGroupReflectorClient_Type.__name__ = "EltexBgpPeerReflectorClientType"
_EltexBgpPeerGroupReflectorClient_Object = MibTableColumn
eltexBgpPeerGroupReflectorClient = _EltexBgpPeerGroupReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 20),
    _EltexBgpPeerGroupReflectorClient_Type()
)
eltexBgpPeerGroupReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupReflectorClient.setStatus("current")


class _EltexBgpPeerGroupSoftResetWithStoredInfo_Type(TruthValue):
    """Custom type eltexBgpPeerGroupSoftResetWithStoredInfo based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerGroupSoftResetWithStoredInfo_Type.__name__ = "TruthValue"
_EltexBgpPeerGroupSoftResetWithStoredInfo_Object = MibTableColumn
eltexBgpPeerGroupSoftResetWithStoredInfo = _EltexBgpPeerGroupSoftResetWithStoredInfo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 21),
    _EltexBgpPeerGroupSoftResetWithStoredInfo_Type()
)
eltexBgpPeerGroupSoftResetWithStoredInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupSoftResetWithStoredInfo.setStatus("current")


class _EltexBgpPeerGroupBfdDesired_Type(TruthValue):
    """Custom type eltexBgpPeerGroupBfdDesired based on TruthValue"""
    defaultValue = 2


_EltexBgpPeerGroupBfdDesired_Type.__name__ = "TruthValue"
_EltexBgpPeerGroupBfdDesired_Object = MibTableColumn
eltexBgpPeerGroupBfdDesired = _EltexBgpPeerGroupBfdDesired_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 2, 2, 1, 1, 22),
    _EltexBgpPeerGroupBfdDesired_Type()
)
eltexBgpPeerGroupBfdDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpPeerGroupBfdDesired.setStatus("current")
_EltexBgpRib_ObjectIdentity = ObjectIdentity
eltexBgpRib = _EltexBgpRib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3)
)
_EltexBgpLocRibTable_Object = MibTable
eltexBgpLocRibTable = _EltexBgpLocRibTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexBgpLocRibTable.setStatus("current")
_EltexBgpLocRibEntry_Object = MibTableRow
eltexBgpLocRibEntry = _EltexBgpLocRibEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1)
)
eltexBgpLocRibEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibSafi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPrfxType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPrfx"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPrfxLen"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPeerOrRib"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPeerRibIndex"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPathId"),
)
if mibBuilder.loadTexts:
    eltexBgpLocRibEntry.setStatus("current")
_EltexBgpLocRibAfi_Type = EltexBgpAfi
_EltexBgpLocRibAfi_Object = MibTableColumn
eltexBgpLocRibAfi = _EltexBgpLocRibAfi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 1),
    _EltexBgpLocRibAfi_Type()
)
eltexBgpLocRibAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibAfi.setStatus("current")
_EltexBgpLocRibSafi_Type = EltexBgpSafi
_EltexBgpLocRibSafi_Object = MibTableColumn
eltexBgpLocRibSafi = _EltexBgpLocRibSafi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 2),
    _EltexBgpLocRibSafi_Type()
)
eltexBgpLocRibSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibSafi.setStatus("current")
_EltexBgpLocRibPrfxType_Type = InetAddressType
_EltexBgpLocRibPrfxType_Object = MibTableColumn
eltexBgpLocRibPrfxType = _EltexBgpLocRibPrfxType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 3),
    _EltexBgpLocRibPrfxType_Type()
)
eltexBgpLocRibPrfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibPrfxType.setStatus("current")
_EltexBgpLocRibPrfx_Type = InetAddress
_EltexBgpLocRibPrfx_Object = MibTableColumn
eltexBgpLocRibPrfx = _EltexBgpLocRibPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 4),
    _EltexBgpLocRibPrfx_Type()
)
eltexBgpLocRibPrfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibPrfx.setStatus("current")
_EltexBgpLocRibPrfxLen_Type = InetAddressPrefixLength
_EltexBgpLocRibPrfxLen_Object = MibTableColumn
eltexBgpLocRibPrfxLen = _EltexBgpLocRibPrfxLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 5),
    _EltexBgpLocRibPrfxLen_Type()
)
eltexBgpLocRibPrfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibPrfxLen.setStatus("current")
_EltexBgpLocRibPeerOrRib_Type = EltexBgpPeerOrRib
_EltexBgpLocRibPeerOrRib_Object = MibTableColumn
eltexBgpLocRibPeerOrRib = _EltexBgpLocRibPeerOrRib_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 6),
    _EltexBgpLocRibPeerOrRib_Type()
)
eltexBgpLocRibPeerOrRib.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibPeerOrRib.setStatus("current")
_EltexBgpLocRibPeerRibIndex_Type = Unsigned32
_EltexBgpLocRibPeerRibIndex_Object = MibTableColumn
eltexBgpLocRibPeerRibIndex = _EltexBgpLocRibPeerRibIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 7),
    _EltexBgpLocRibPeerRibIndex_Type()
)
eltexBgpLocRibPeerRibIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibPeerRibIndex.setStatus("current")
_EltexBgpLocRibPathId_Type = Unsigned32
_EltexBgpLocRibPathId_Object = MibTableColumn
eltexBgpLocRibPathId = _EltexBgpLocRibPathId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 8),
    _EltexBgpLocRibPathId_Type()
)
eltexBgpLocRibPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathId.setStatus("current")
_EltexBgpLocRibBest_Type = TruthValue
_EltexBgpLocRibBest_Object = MibTableColumn
eltexBgpLocRibBest = _EltexBgpLocRibBest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 9),
    _EltexBgpLocRibBest_Type()
)
eltexBgpLocRibBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibBest.setStatus("current")
_EltexBgpLocRibAsSize_Type = EltexBgpAsSize
_EltexBgpLocRibAsSize_Object = MibTableColumn
eltexBgpLocRibAsSize = _EltexBgpLocRibAsSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 10),
    _EltexBgpLocRibAsSize_Type()
)
eltexBgpLocRibAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibAsSize.setStatus("current")


class _EltexBgpLocRibASPathStr_Type(OctetString):
    """Custom type eltexBgpLocRibASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexBgpLocRibASPathStr_Type.__name__ = "OctetString"
_EltexBgpLocRibASPathStr_Object = MibTableColumn
eltexBgpLocRibASPathStr = _EltexBgpLocRibASPathStr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 11),
    _EltexBgpLocRibASPathStr_Type()
)
eltexBgpLocRibASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibASPathStr.setStatus("current")
_EltexBgpLocRibPathAttrOrigin_Type = EltexBgpOriginCode
_EltexBgpLocRibPathAttrOrigin_Object = MibTableColumn
eltexBgpLocRibPathAttrOrigin = _EltexBgpLocRibPathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 12),
    _EltexBgpLocRibPathAttrOrigin_Type()
)
eltexBgpLocRibPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrOrigin.setStatus("current")
_EltexBgpLocRibPathAttrNextHopType_Type = InetAddressType
_EltexBgpLocRibPathAttrNextHopType_Object = MibTableColumn
eltexBgpLocRibPathAttrNextHopType = _EltexBgpLocRibPathAttrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 13),
    _EltexBgpLocRibPathAttrNextHopType_Type()
)
eltexBgpLocRibPathAttrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrNextHopType.setStatus("current")
_EltexBgpLocRibPathAttrNextHop_Type = InetAddress
_EltexBgpLocRibPathAttrNextHop_Object = MibTableColumn
eltexBgpLocRibPathAttrNextHop = _EltexBgpLocRibPathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 14),
    _EltexBgpLocRibPathAttrNextHop_Type()
)
eltexBgpLocRibPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrNextHop.setStatus("current")
_EltexBgpLocRibPathAttrMultExtDisc_Type = Unsigned32
_EltexBgpLocRibPathAttrMultExtDisc_Object = MibTableColumn
eltexBgpLocRibPathAttrMultExtDisc = _EltexBgpLocRibPathAttrMultExtDisc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 15),
    _EltexBgpLocRibPathAttrMultExtDisc_Type()
)
eltexBgpLocRibPathAttrMultExtDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrMultExtDisc.setStatus("current")
_EltexBgpLocRibPathAttrLocalPref_Type = Unsigned32
_EltexBgpLocRibPathAttrLocalPref_Object = MibTableColumn
eltexBgpLocRibPathAttrLocalPref = _EltexBgpLocRibPathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 16),
    _EltexBgpLocRibPathAttrLocalPref_Type()
)
eltexBgpLocRibPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrLocalPref.setStatus("current")
_EltexBgpLocRibPathAttrAtomicAgg_Type = TruthValue
_EltexBgpLocRibPathAttrAtomicAgg_Object = MibTableColumn
eltexBgpLocRibPathAttrAtomicAgg = _EltexBgpLocRibPathAttrAtomicAgg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 17),
    _EltexBgpLocRibPathAttrAtomicAgg_Type()
)
eltexBgpLocRibPathAttrAtomicAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrAtomicAgg.setStatus("current")
_EltexBgpLocRibPathAttrAggAS_Type = EltexBgpAutonomousSystemNumber
_EltexBgpLocRibPathAttrAggAS_Object = MibTableColumn
eltexBgpLocRibPathAttrAggAS = _EltexBgpLocRibPathAttrAggAS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 18),
    _EltexBgpLocRibPathAttrAggAS_Type()
)
eltexBgpLocRibPathAttrAggAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrAggAS.setStatus("current")
_EltexBgpLocRibPathAttrAggAddr_Type = EltexBgpIdentifier
_EltexBgpLocRibPathAttrAggAddr_Object = MibTableColumn
eltexBgpLocRibPathAttrAggAddr = _EltexBgpLocRibPathAttrAggAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 19),
    _EltexBgpLocRibPathAttrAggAddr_Type()
)
eltexBgpLocRibPathAttrAggAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrAggAddr.setStatus("current")
_EltexBgpLocRibPathAttrCalcLclPref_Type = Unsigned32
_EltexBgpLocRibPathAttrCalcLclPref_Object = MibTableColumn
eltexBgpLocRibPathAttrCalcLclPref = _EltexBgpLocRibPathAttrCalcLclPref_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 20),
    _EltexBgpLocRibPathAttrCalcLclPref_Type()
)
eltexBgpLocRibPathAttrCalcLclPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrCalcLclPref.setStatus("current")
_EltexBgpLocRibPathAttrOrigId_Type = EltexBgpIdentifier
_EltexBgpLocRibPathAttrOrigId_Object = MibTableColumn
eltexBgpLocRibPathAttrOrigId = _EltexBgpLocRibPathAttrOrigId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 21),
    _EltexBgpLocRibPathAttrOrigId_Type()
)
eltexBgpLocRibPathAttrOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrOrigId.setStatus("current")
_EltexBgpLocRibPathAttrWeight_Type = Unsigned32
_EltexBgpLocRibPathAttrWeight_Object = MibTableColumn
eltexBgpLocRibPathAttrWeight = _EltexBgpLocRibPathAttrWeight_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 22),
    _EltexBgpLocRibPathAttrWeight_Type()
)
eltexBgpLocRibPathAttrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrWeight.setStatus("current")
_EltexBgpLocRibEcmp_Type = TruthValue
_EltexBgpLocRibEcmp_Object = MibTableColumn
eltexBgpLocRibEcmp = _EltexBgpLocRibEcmp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 23),
    _EltexBgpLocRibEcmp_Type()
)
eltexBgpLocRibEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibEcmp.setStatus("current")
_EltexBgpLocRibPathAttrAsPathLimAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpLocRibPathAttrAsPathLimAs_Object = MibTableColumn
eltexBgpLocRibPathAttrAsPathLimAs = _EltexBgpLocRibPathAttrAsPathLimAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 24),
    _EltexBgpLocRibPathAttrAsPathLimAs_Type()
)
eltexBgpLocRibPathAttrAsPathLimAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrAsPathLimAs.setStatus("current")


class _EltexBgpLocRibPthAttAsPthLimUpper_Type(Unsigned32):
    """Custom type eltexBgpLocRibPthAttAsPthLimUpper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexBgpLocRibPthAttAsPthLimUpper_Type.__name__ = "Unsigned32"
_EltexBgpLocRibPthAttAsPthLimUpper_Object = MibTableColumn
eltexBgpLocRibPthAttAsPthLimUpper = _EltexBgpLocRibPthAttAsPthLimUpper_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 25),
    _EltexBgpLocRibPthAttAsPthLimUpper_Type()
)
eltexBgpLocRibPthAttAsPthLimUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPthAttAsPthLimUpper.setStatus("current")
_EltexBgpLocRibIsActive_Type = EltexBgpNlriIsActiveFlag
_EltexBgpLocRibIsActive_Object = MibTableColumn
eltexBgpLocRibIsActive = _EltexBgpLocRibIsActive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 26),
    _EltexBgpLocRibIsActive_Type()
)
eltexBgpLocRibIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibIsActive.setStatus("current")
_EltexBgpLocRibPathAttrMEDPrsnt_Type = TruthValue
_EltexBgpLocRibPathAttrMEDPrsnt_Object = MibTableColumn
eltexBgpLocRibPathAttrMEDPrsnt = _EltexBgpLocRibPathAttrMEDPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 27),
    _EltexBgpLocRibPathAttrMEDPrsnt_Type()
)
eltexBgpLocRibPathAttrMEDPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPathAttrMEDPrsnt.setStatus("current")
_EltexBgpLocRibReasonNotBest_Type = EltexBgpReasonNotBest
_EltexBgpLocRibReasonNotBest_Object = MibTableColumn
eltexBgpLocRibReasonNotBest = _EltexBgpLocRibReasonNotBest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 28),
    _EltexBgpLocRibReasonNotBest_Type()
)
eltexBgpLocRibReasonNotBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibReasonNotBest.setStatus("current")
_EltexBgpLocRibPeerType_Type = EltexBgpNlriPeerTypes
_EltexBgpLocRibPeerType_Object = MibTableColumn
eltexBgpLocRibPeerType = _EltexBgpLocRibPeerType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 1, 1, 29),
    _EltexBgpLocRibPeerType_Type()
)
eltexBgpLocRibPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpLocRibPeerType.setStatus("current")
_EltexBgpAdjRibInTable_Object = MibTable
eltexBgpAdjRibInTable = _EltexBgpAdjRibInTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexBgpAdjRibInTable.setStatus("current")
_EltexBgpAdjRibInEntry_Object = MibTableRow
eltexBgpAdjRibInEntry = _EltexBgpAdjRibInEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1)
)
eltexBgpAdjRibInEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInPeerIndex"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInSafi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInPrfxType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInPrfx"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInPrfxLen"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibInPathId"),
)
if mibBuilder.loadTexts:
    eltexBgpAdjRibInEntry.setStatus("current")
_EltexBgpAdjRibInPeerIndex_Type = Unsigned32
_EltexBgpAdjRibInPeerIndex_Object = MibTableColumn
eltexBgpAdjRibInPeerIndex = _EltexBgpAdjRibInPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 1),
    _EltexBgpAdjRibInPeerIndex_Type()
)
eltexBgpAdjRibInPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPeerIndex.setStatus("current")
_EltexBgpAdjRibInAfi_Type = EltexBgpAfi
_EltexBgpAdjRibInAfi_Object = MibTableColumn
eltexBgpAdjRibInAfi = _EltexBgpAdjRibInAfi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 2),
    _EltexBgpAdjRibInAfi_Type()
)
eltexBgpAdjRibInAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInAfi.setStatus("current")
_EltexBgpAdjRibInSafi_Type = EltexBgpSafi
_EltexBgpAdjRibInSafi_Object = MibTableColumn
eltexBgpAdjRibInSafi = _EltexBgpAdjRibInSafi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 3),
    _EltexBgpAdjRibInSafi_Type()
)
eltexBgpAdjRibInSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInSafi.setStatus("current")
_EltexBgpAdjRibInPrfxType_Type = InetAddressType
_EltexBgpAdjRibInPrfxType_Object = MibTableColumn
eltexBgpAdjRibInPrfxType = _EltexBgpAdjRibInPrfxType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 4),
    _EltexBgpAdjRibInPrfxType_Type()
)
eltexBgpAdjRibInPrfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPrfxType.setStatus("current")
_EltexBgpAdjRibInPrfx_Type = InetAddress
_EltexBgpAdjRibInPrfx_Object = MibTableColumn
eltexBgpAdjRibInPrfx = _EltexBgpAdjRibInPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 5),
    _EltexBgpAdjRibInPrfx_Type()
)
eltexBgpAdjRibInPrfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPrfx.setStatus("current")
_EltexBgpAdjRibInPrfxLen_Type = InetAddressPrefixLength
_EltexBgpAdjRibInPrfxLen_Object = MibTableColumn
eltexBgpAdjRibInPrfxLen = _EltexBgpAdjRibInPrfxLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 6),
    _EltexBgpAdjRibInPrfxLen_Type()
)
eltexBgpAdjRibInPrfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPrfxLen.setStatus("current")
_EltexBgpAdjRibInPathId_Type = Unsigned32
_EltexBgpAdjRibInPathId_Object = MibTableColumn
eltexBgpAdjRibInPathId = _EltexBgpAdjRibInPathId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 7),
    _EltexBgpAdjRibInPathId_Type()
)
eltexBgpAdjRibInPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathId.setStatus("current")
_EltexBgpAdjRibInAsSize_Type = EltexBgpAsSize
_EltexBgpAdjRibInAsSize_Object = MibTableColumn
eltexBgpAdjRibInAsSize = _EltexBgpAdjRibInAsSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 8),
    _EltexBgpAdjRibInAsSize_Type()
)
eltexBgpAdjRibInAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInAsSize.setStatus("current")


class _EltexBgpAdjRibInASPathStr_Type(OctetString):
    """Custom type eltexBgpAdjRibInASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexBgpAdjRibInASPathStr_Type.__name__ = "OctetString"
_EltexBgpAdjRibInASPathStr_Object = MibTableColumn
eltexBgpAdjRibInASPathStr = _EltexBgpAdjRibInASPathStr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 9),
    _EltexBgpAdjRibInASPathStr_Type()
)
eltexBgpAdjRibInASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInASPathStr.setStatus("current")
_EltexBgpAdjRibInPathAttrOrigin_Type = EltexBgpOriginCode
_EltexBgpAdjRibInPathAttrOrigin_Object = MibTableColumn
eltexBgpAdjRibInPathAttrOrigin = _EltexBgpAdjRibInPathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 10),
    _EltexBgpAdjRibInPathAttrOrigin_Type()
)
eltexBgpAdjRibInPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrOrigin.setStatus("current")
_EltexBgpAdjRibInPathAttrNextHopType_Type = InetAddressType
_EltexBgpAdjRibInPathAttrNextHopType_Object = MibTableColumn
eltexBgpAdjRibInPathAttrNextHopType = _EltexBgpAdjRibInPathAttrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 11),
    _EltexBgpAdjRibInPathAttrNextHopType_Type()
)
eltexBgpAdjRibInPathAttrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrNextHopType.setStatus("current")
_EltexBgpAdjRibInPathAttrNextHop_Type = InetAddress
_EltexBgpAdjRibInPathAttrNextHop_Object = MibTableColumn
eltexBgpAdjRibInPathAttrNextHop = _EltexBgpAdjRibInPathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 12),
    _EltexBgpAdjRibInPathAttrNextHop_Type()
)
eltexBgpAdjRibInPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrNextHop.setStatus("current")
_EltexBgpAdjRibInPathAttrMultiExitDisc_Type = Unsigned32
_EltexBgpAdjRibInPathAttrMultiExitDisc_Object = MibTableColumn
eltexBgpAdjRibInPathAttrMultiExitDisc = _EltexBgpAdjRibInPathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 13),
    _EltexBgpAdjRibInPathAttrMultiExitDisc_Type()
)
eltexBgpAdjRibInPathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrMultiExitDisc.setStatus("current")
_EltexBgpAdjRibInPathAttrLocalPref_Type = Unsigned32
_EltexBgpAdjRibInPathAttrLocalPref_Object = MibTableColumn
eltexBgpAdjRibInPathAttrLocalPref = _EltexBgpAdjRibInPathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 14),
    _EltexBgpAdjRibInPathAttrLocalPref_Type()
)
eltexBgpAdjRibInPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrLocalPref.setStatus("current")
_EltexBgpAdjRibInPathAttrAtomicAggregate_Type = TruthValue
_EltexBgpAdjRibInPathAttrAtomicAggregate_Object = MibTableColumn
eltexBgpAdjRibInPathAttrAtomicAggregate = _EltexBgpAdjRibInPathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 15),
    _EltexBgpAdjRibInPathAttrAtomicAggregate_Type()
)
eltexBgpAdjRibInPathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrAtomicAggregate.setStatus("current")
_EltexBgpAdjRibInPathAttrAggregatorAS_Type = EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibInPathAttrAggregatorAS_Object = MibTableColumn
eltexBgpAdjRibInPathAttrAggregatorAS = _EltexBgpAdjRibInPathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 16),
    _EltexBgpAdjRibInPathAttrAggregatorAS_Type()
)
eltexBgpAdjRibInPathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrAggregatorAS.setStatus("current")
_EltexBgpAdjRibInPathAttrAggregatorAddr_Type = EltexBgpIdentifier
_EltexBgpAdjRibInPathAttrAggregatorAddr_Object = MibTableColumn
eltexBgpAdjRibInPathAttrAggregatorAddr = _EltexBgpAdjRibInPathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 17),
    _EltexBgpAdjRibInPathAttrAggregatorAddr_Type()
)
eltexBgpAdjRibInPathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrAggregatorAddr.setStatus("current")
_EltexBgpAdjRibInPathAttrOrigId_Type = EltexBgpIdentifier
_EltexBgpAdjRibInPathAttrOrigId_Object = MibTableColumn
eltexBgpAdjRibInPathAttrOrigId = _EltexBgpAdjRibInPathAttrOrigId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 18),
    _EltexBgpAdjRibInPathAttrOrigId_Type()
)
eltexBgpAdjRibInPathAttrOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrOrigId.setStatus("current")
_EltexBgpAdjRibInPathAttrAsPathLimAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibInPathAttrAsPathLimAs_Object = MibTableColumn
eltexBgpAdjRibInPathAttrAsPathLimAs = _EltexBgpAdjRibInPathAttrAsPathLimAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 19),
    _EltexBgpAdjRibInPathAttrAsPathLimAs_Type()
)
eltexBgpAdjRibInPathAttrAsPathLimAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrAsPathLimAs.setStatus("current")


class _EltexBgpAdjRibInPathAttrAsPathLimUpper_Type(Unsigned32):
    """Custom type eltexBgpAdjRibInPathAttrAsPathLimUpper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexBgpAdjRibInPathAttrAsPathLimUpper_Type.__name__ = "Unsigned32"
_EltexBgpAdjRibInPathAttrAsPathLimUpper_Object = MibTableColumn
eltexBgpAdjRibInPathAttrAsPathLimUpper = _EltexBgpAdjRibInPathAttrAsPathLimUpper_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 20),
    _EltexBgpAdjRibInPathAttrAsPathLimUpper_Type()
)
eltexBgpAdjRibInPathAttrAsPathLimUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrAsPathLimUpper.setStatus("current")
_EltexBgpAdjRibInPathAttrMEDPrsnt_Type = TruthValue
_EltexBgpAdjRibInPathAttrMEDPrsnt_Object = MibTableColumn
eltexBgpAdjRibInPathAttrMEDPrsnt = _EltexBgpAdjRibInPathAttrMEDPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 21),
    _EltexBgpAdjRibInPathAttrMEDPrsnt_Type()
)
eltexBgpAdjRibInPathAttrMEDPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAttrMEDPrsnt.setStatus("current")
_EltexBgpAdjRibInPathAccepted_Type = TruthValue
_EltexBgpAdjRibInPathAccepted_Object = MibTableColumn
eltexBgpAdjRibInPathAccepted = _EltexBgpAdjRibInPathAccepted_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 2, 1, 22),
    _EltexBgpAdjRibInPathAccepted_Type()
)
eltexBgpAdjRibInPathAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibInPathAccepted.setStatus("current")
_EltexBgpAdjRibOutTable_Object = MibTable
eltexBgpAdjRibOutTable = _EltexBgpAdjRibOutTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutTable.setStatus("current")
_EltexBgpAdjRibOutEntry_Object = MibTableRow
eltexBgpAdjRibOutEntry = _EltexBgpAdjRibOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1)
)
eltexBgpAdjRibOutEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPeerStatusPeerIndex"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibOutAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibOutSafi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibOutPrfxType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibOutPrfx"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibOutPrfxLen"),
    (0, "ELTEX-BGP-MIB", "eltexBgpAdjRibOutPathId"),
)
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutEntry.setStatus("current")
_EltexBgpAdjRibOutAfi_Type = EltexBgpAfi
_EltexBgpAdjRibOutAfi_Object = MibTableColumn
eltexBgpAdjRibOutAfi = _EltexBgpAdjRibOutAfi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 1),
    _EltexBgpAdjRibOutAfi_Type()
)
eltexBgpAdjRibOutAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAfi.setStatus("current")
_EltexBgpAdjRibOutSafi_Type = EltexBgpSafi
_EltexBgpAdjRibOutSafi_Object = MibTableColumn
eltexBgpAdjRibOutSafi = _EltexBgpAdjRibOutSafi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 2),
    _EltexBgpAdjRibOutSafi_Type()
)
eltexBgpAdjRibOutSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutSafi.setStatus("current")
_EltexBgpAdjRibOutPrfxType_Type = InetAddressType
_EltexBgpAdjRibOutPrfxType_Object = MibTableColumn
eltexBgpAdjRibOutPrfxType = _EltexBgpAdjRibOutPrfxType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 3),
    _EltexBgpAdjRibOutPrfxType_Type()
)
eltexBgpAdjRibOutPrfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutPrfxType.setStatus("current")
_EltexBgpAdjRibOutPrfx_Type = InetAddress
_EltexBgpAdjRibOutPrfx_Object = MibTableColumn
eltexBgpAdjRibOutPrfx = _EltexBgpAdjRibOutPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 4),
    _EltexBgpAdjRibOutPrfx_Type()
)
eltexBgpAdjRibOutPrfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutPrfx.setStatus("current")
_EltexBgpAdjRibOutPrfxLen_Type = InetAddressPrefixLength
_EltexBgpAdjRibOutPrfxLen_Object = MibTableColumn
eltexBgpAdjRibOutPrfxLen = _EltexBgpAdjRibOutPrfxLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 5),
    _EltexBgpAdjRibOutPrfxLen_Type()
)
eltexBgpAdjRibOutPrfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutPrfxLen.setStatus("current")
_EltexBgpAdjRibOutPathId_Type = Unsigned32
_EltexBgpAdjRibOutPathId_Object = MibTableColumn
eltexBgpAdjRibOutPathId = _EltexBgpAdjRibOutPathId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 6),
    _EltexBgpAdjRibOutPathId_Type()
)
eltexBgpAdjRibOutPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutPathId.setStatus("current")
_EltexBgpAdjRibOutBest_Type = TruthValue
_EltexBgpAdjRibOutBest_Object = MibTableColumn
eltexBgpAdjRibOutBest = _EltexBgpAdjRibOutBest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 7),
    _EltexBgpAdjRibOutBest_Type()
)
eltexBgpAdjRibOutBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutBest.setStatus("current")


class _EltexBgpAdjRibOutAdvertStatus_Type(Integer32):
    """Custom type eltexBgpAdjRibOutAdvertStatus based on Integer32"""
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
        *(("advertised", 1),
          ("suppressed", 2),
          ("pendingWithdrawal", 3),
          ("withdrawn", 4))
    )


_EltexBgpAdjRibOutAdvertStatus_Type.__name__ = "Integer32"
_EltexBgpAdjRibOutAdvertStatus_Object = MibTableColumn
eltexBgpAdjRibOutAdvertStatus = _EltexBgpAdjRibOutAdvertStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 8),
    _EltexBgpAdjRibOutAdvertStatus_Type()
)
eltexBgpAdjRibOutAdvertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAdvertStatus.setStatus("current")


class _EltexBgpAdjRibOutLocalAggrType_Type(Integer32):
    """Custom type eltexBgpAdjRibOutLocalAggrType based on Integer32"""
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
        *(("noAggregation", 1),
          ("aggregateRoute", 2),
          ("unsuppAggregatedRoute", 3),
          ("suppressedAggregatedRoute", 4))
    )


_EltexBgpAdjRibOutLocalAggrType_Type.__name__ = "Integer32"
_EltexBgpAdjRibOutLocalAggrType_Object = MibTableColumn
eltexBgpAdjRibOutLocalAggrType = _EltexBgpAdjRibOutLocalAggrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 9),
    _EltexBgpAdjRibOutLocalAggrType_Type()
)
eltexBgpAdjRibOutLocalAggrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutLocalAggrType.setStatus("current")
_EltexBgpAdjRibOutAsSize_Type = EltexBgpAsSize
_EltexBgpAdjRibOutAsSize_Object = MibTableColumn
eltexBgpAdjRibOutAsSize = _EltexBgpAdjRibOutAsSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 10),
    _EltexBgpAdjRibOutAsSize_Type()
)
eltexBgpAdjRibOutAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAsSize.setStatus("current")


class _EltexBgpAdjRibOutASPathStr_Type(OctetString):
    """Custom type eltexBgpAdjRibOutASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexBgpAdjRibOutASPathStr_Type.__name__ = "OctetString"
_EltexBgpAdjRibOutASPathStr_Object = MibTableColumn
eltexBgpAdjRibOutASPathStr = _EltexBgpAdjRibOutASPathStr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 11),
    _EltexBgpAdjRibOutASPathStr_Type()
)
eltexBgpAdjRibOutASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutASPathStr.setStatus("current")
_EltexBgpAdjRibOutOrigin_Type = EltexBgpOriginCode
_EltexBgpAdjRibOutOrigin_Object = MibTableColumn
eltexBgpAdjRibOutOrigin = _EltexBgpAdjRibOutOrigin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 12),
    _EltexBgpAdjRibOutOrigin_Type()
)
eltexBgpAdjRibOutOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutOrigin.setStatus("current")
_EltexBgpAdjRibOutNextHopType_Type = InetAddressType
_EltexBgpAdjRibOutNextHopType_Object = MibTableColumn
eltexBgpAdjRibOutNextHopType = _EltexBgpAdjRibOutNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 13),
    _EltexBgpAdjRibOutNextHopType_Type()
)
eltexBgpAdjRibOutNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutNextHopType.setStatus("current")
_EltexBgpAdjRibOutNextHop_Type = InetAddress
_EltexBgpAdjRibOutNextHop_Object = MibTableColumn
eltexBgpAdjRibOutNextHop = _EltexBgpAdjRibOutNextHop_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 14),
    _EltexBgpAdjRibOutNextHop_Type()
)
eltexBgpAdjRibOutNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutNextHop.setStatus("current")
_EltexBgpAdjRibOutMultiExitDisc_Type = Unsigned32
_EltexBgpAdjRibOutMultiExitDisc_Object = MibTableColumn
eltexBgpAdjRibOutMultiExitDisc = _EltexBgpAdjRibOutMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 15),
    _EltexBgpAdjRibOutMultiExitDisc_Type()
)
eltexBgpAdjRibOutMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutMultiExitDisc.setStatus("current")
_EltexBgpAdjRibOutLocalPref_Type = Unsigned32
_EltexBgpAdjRibOutLocalPref_Object = MibTableColumn
eltexBgpAdjRibOutLocalPref = _EltexBgpAdjRibOutLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 16),
    _EltexBgpAdjRibOutLocalPref_Type()
)
eltexBgpAdjRibOutLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutLocalPref.setStatus("current")
_EltexBgpAdjRibOutAtomicAggregate_Type = TruthValue
_EltexBgpAdjRibOutAtomicAggregate_Object = MibTableColumn
eltexBgpAdjRibOutAtomicAggregate = _EltexBgpAdjRibOutAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 17),
    _EltexBgpAdjRibOutAtomicAggregate_Type()
)
eltexBgpAdjRibOutAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAtomicAggregate.setStatus("current")
_EltexBgpAdjRibOutAggregatorAS_Type = EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibOutAggregatorAS_Object = MibTableColumn
eltexBgpAdjRibOutAggregatorAS = _EltexBgpAdjRibOutAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 18),
    _EltexBgpAdjRibOutAggregatorAS_Type()
)
eltexBgpAdjRibOutAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAggregatorAS.setStatus("current")
_EltexBgpAdjRibOutAggregatorAddr_Type = EltexBgpIdentifier
_EltexBgpAdjRibOutAggregatorAddr_Object = MibTableColumn
eltexBgpAdjRibOutAggregatorAddr = _EltexBgpAdjRibOutAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 19),
    _EltexBgpAdjRibOutAggregatorAddr_Type()
)
eltexBgpAdjRibOutAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAggregatorAddr.setStatus("current")
_EltexBgpAdjRibOutOrigId_Type = EltexBgpIdentifier
_EltexBgpAdjRibOutOrigId_Object = MibTableColumn
eltexBgpAdjRibOutOrigId = _EltexBgpAdjRibOutOrigId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 20),
    _EltexBgpAdjRibOutOrigId_Type()
)
eltexBgpAdjRibOutOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutOrigId.setStatus("current")
_EltexBgpAdjRibOutEcmp_Type = TruthValue
_EltexBgpAdjRibOutEcmp_Object = MibTableColumn
eltexBgpAdjRibOutEcmp = _EltexBgpAdjRibOutEcmp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 21),
    _EltexBgpAdjRibOutEcmp_Type()
)
eltexBgpAdjRibOutEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutEcmp.setStatus("current")
_EltexBgpAdjRibOutAsLimAs_Type = EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibOutAsLimAs_Object = MibTableColumn
eltexBgpAdjRibOutAsLimAs = _EltexBgpAdjRibOutAsLimAs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 22),
    _EltexBgpAdjRibOutAsLimAs_Type()
)
eltexBgpAdjRibOutAsLimAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAsLimAs.setStatus("current")


class _EltexBgpAdjRibOutAsLimUpper_Type(Unsigned32):
    """Custom type eltexBgpAdjRibOutAsLimUpper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexBgpAdjRibOutAsLimUpper_Type.__name__ = "Unsigned32"
_EltexBgpAdjRibOutAsLimUpper_Object = MibTableColumn
eltexBgpAdjRibOutAsLimUpper = _EltexBgpAdjRibOutAsLimUpper_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 23),
    _EltexBgpAdjRibOutAsLimUpper_Type()
)
eltexBgpAdjRibOutAsLimUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutAsLimUpper.setStatus("current")
_EltexBgpAdjRibOutIsActive_Type = EltexBgpNlriIsActiveFlag
_EltexBgpAdjRibOutIsActive_Object = MibTableColumn
eltexBgpAdjRibOutIsActive = _EltexBgpAdjRibOutIsActive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 24),
    _EltexBgpAdjRibOutIsActive_Type()
)
eltexBgpAdjRibOutIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutIsActive.setStatus("current")
_EltexBgpAdjRibOutMEDPrsnt_Type = TruthValue
_EltexBgpAdjRibOutMEDPrsnt_Object = MibTableColumn
eltexBgpAdjRibOutMEDPrsnt = _EltexBgpAdjRibOutMEDPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 25),
    _EltexBgpAdjRibOutMEDPrsnt_Type()
)
eltexBgpAdjRibOutMEDPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutMEDPrsnt.setStatus("current")
_EltexBgpAdjRibOutPeerType_Type = EltexBgpNlriPeerTypes
_EltexBgpAdjRibOutPeerType_Object = MibTableColumn
eltexBgpAdjRibOutPeerType = _EltexBgpAdjRibOutPeerType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 3, 1, 26),
    _EltexBgpAdjRibOutPeerType_Type()
)
eltexBgpAdjRibOutPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpAdjRibOutPeerType.setStatus("current")
_EltexBgpNetworkTable_Object = MibTable
eltexBgpNetworkTable = _EltexBgpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4)
)
if mibBuilder.loadTexts:
    eltexBgpNetworkTable.setStatus("current")
_EltexBgpNetworkEntry_Object = MibTableRow
eltexBgpNetworkEntry = _EltexBgpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1)
)
eltexBgpNetworkEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpNetworkAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpNetworkSafi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpNetworkPrfxType"),
    (0, "ELTEX-BGP-MIB", "eltexBgpNetworkPrfx"),
    (0, "ELTEX-BGP-MIB", "eltexBgpNetworkPrfxLen"),
)
if mibBuilder.loadTexts:
    eltexBgpNetworkEntry.setStatus("current")


class _EltexBgpNetworkAfi_Type(EltexBgpAfi):
    """Custom type eltexBgpNetworkAfi based on EltexBgpAfi"""
    defaultValue = 1


_EltexBgpNetworkAfi_Type.__name__ = "EltexBgpAfi"
_EltexBgpNetworkAfi_Object = MibTableColumn
eltexBgpNetworkAfi = _EltexBgpNetworkAfi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1, 1),
    _EltexBgpNetworkAfi_Type()
)
eltexBgpNetworkAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpNetworkAfi.setStatus("current")


class _EltexBgpNetworkSafi_Type(EltexBgpSafi):
    """Custom type eltexBgpNetworkSafi based on EltexBgpSafi"""
    defaultValue = 1


_EltexBgpNetworkSafi_Type.__name__ = "EltexBgpSafi"
_EltexBgpNetworkSafi_Object = MibTableColumn
eltexBgpNetworkSafi = _EltexBgpNetworkSafi_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1, 2),
    _EltexBgpNetworkSafi_Type()
)
eltexBgpNetworkSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpNetworkSafi.setStatus("current")
_EltexBgpNetworkPrfxType_Type = InetAddressType
_EltexBgpNetworkPrfxType_Object = MibTableColumn
eltexBgpNetworkPrfxType = _EltexBgpNetworkPrfxType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1, 3),
    _EltexBgpNetworkPrfxType_Type()
)
eltexBgpNetworkPrfxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpNetworkPrfxType.setStatus("current")
_EltexBgpNetworkPrfx_Type = InetAddress
_EltexBgpNetworkPrfx_Object = MibTableColumn
eltexBgpNetworkPrfx = _EltexBgpNetworkPrfx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1, 4),
    _EltexBgpNetworkPrfx_Type()
)
eltexBgpNetworkPrfx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpNetworkPrfx.setStatus("current")
_EltexBgpNetworkPrfxLen_Type = InetAddressPrefixLength
_EltexBgpNetworkPrfxLen_Object = MibTableColumn
eltexBgpNetworkPrfxLen = _EltexBgpNetworkPrfxLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1, 5),
    _EltexBgpNetworkPrfxLen_Type()
)
eltexBgpNetworkPrfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexBgpNetworkPrfxLen.setStatus("current")
_EltexBgpNetworkRowStatus_Type = RowStatus
_EltexBgpNetworkRowStatus_Object = MibTableColumn
eltexBgpNetworkRowStatus = _EltexBgpNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 4, 1, 6),
    _EltexBgpNetworkRowStatus_Type()
)
eltexBgpNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexBgpNetworkRowStatus.setStatus("current")
_EltexBgpPathAttrExtensions_ObjectIdentity = ObjectIdentity
eltexBgpPathAttrExtensions = _EltexBgpPathAttrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 5)
)
_EltexBgpPathAttrRouteReflectionExts_ObjectIdentity = ObjectIdentity
eltexBgpPathAttrRouteReflectionExts = _EltexBgpPathAttrRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 5, 1)
)
_EltexBgpPathAttrClusterLocTable_Object = MibTable
eltexBgpPathAttrClusterLocTable = _EltexBgpPathAttrClusterLocTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    eltexBgpPathAttrClusterLocTable.setStatus("current")
_EltexBgpPathAttrClusterLocEntry_Object = MibTableRow
eltexBgpPathAttrClusterLocEntry = _EltexBgpPathAttrClusterLocEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 5, 1, 1, 1)
)
eltexBgpPathAttrClusterLocEntry.setIndexNames(
    (0, "ELTEX-BGP-MIB", "eltexBgpProcessId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPeerOrRib"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPeerRibIndex"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibAfi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibSafi"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPrfx"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPrfxLen"),
    (0, "ELTEX-BGP-MIB", "eltexBgpLocRibPathId"),
    (0, "ELTEX-BGP-MIB", "eltexBgpPathAttrClusterLocIndex"),
)
if mibBuilder.loadTexts:
    eltexBgpPathAttrClusterLocEntry.setStatus("current")
_EltexBgpPathAttrClusterLocIndex_Type = Unsigned32
_EltexBgpPathAttrClusterLocIndex_Object = MibTableColumn
eltexBgpPathAttrClusterLocIndex = _EltexBgpPathAttrClusterLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 5, 1, 1, 1, 1),
    _EltexBgpPathAttrClusterLocIndex_Type()
)
eltexBgpPathAttrClusterLocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexBgpPathAttrClusterLocIndex.setStatus("current")
_EltexBgpPathAttrClusterLocValue_Type = Unsigned32
_EltexBgpPathAttrClusterLocValue_Object = MibTableColumn
eltexBgpPathAttrClusterLocValue = _EltexBgpPathAttrClusterLocValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 45, 1, 3, 5, 1, 1, 1, 2),
    _EltexBgpPathAttrClusterLocValue_Type()
)
eltexBgpPathAttrClusterLocValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexBgpPathAttrClusterLocValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-BGP-MIB",
    **{"EltexBgpIdentifier": EltexBgpIdentifier,
       "EltexBgpAfi": EltexBgpAfi,
       "EltexBgpSafi": EltexBgpSafi,
       "EltexBgpAutonomousSystemNumber": EltexBgpAutonomousSystemNumber,
       "EltexBgpAsSize": EltexBgpAsSize,
       "EltexBgpAdminStatus": EltexBgpAdminStatus,
       "EltexBgpOperStatus": EltexBgpOperStatus,
       "EltexBgpOriginCode": EltexBgpOriginCode,
       "EltexBgpConfigDropOrWarn": EltexBgpConfigDropOrWarn,
       "EltexBgpPeerOrRib": EltexBgpPeerOrRib,
       "EltexBgpPeerStates": EltexBgpPeerStates,
       "EltexBgpPeerEvents": EltexBgpPeerEvents,
       "EltexBgpCapabilities": EltexBgpCapabilities,
       "EltexBgpCeaseErrorSubcode": EltexBgpCeaseErrorSubcode,
       "EltexBgpNlriIsActiveFlag": EltexBgpNlriIsActiveFlag,
       "EltexBgpPeerConfigStates": EltexBgpPeerConfigStates,
       "EltexBgpReasonNotBest": EltexBgpReasonNotBest,
       "EltexBgpNlriPeerTypes": EltexBgpNlriPeerTypes,
       "EltexBgpASNotation": EltexBgpASNotation,
       "EltexBgpPeerReflectorClientType": EltexBgpPeerReflectorClientType,
       "EltexBgpRouteMapAsPathAction": EltexBgpRouteMapAsPathAction,
       "EltexBgpAddPathSrCap": EltexBgpAddPathSrCap,
       "EltexBfdSessionStatus": EltexBfdSessionStatus,
       "eltexBgpMIB": eltexBgpMIB,
       "eltexBgpObjects": eltexBgpObjects,
       "eltexBgpProcess": eltexBgpProcess,
       "eltexBgpProcessTable": eltexBgpProcessTable,
       "eltexBgpProcessEntry": eltexBgpProcessEntry,
       "eltexBgpProcessId": eltexBgpProcessId,
       "eltexBgpProcessRowStatus": eltexBgpProcessRowStatus,
       "eltexBgpProcessAdminStatus": eltexBgpProcessAdminStatus,
       "eltexBgpProcessOperStatus": eltexBgpProcessOperStatus,
       "eltexBgpProcessLocalAs": eltexBgpProcessLocalAs,
       "eltexBgpProcessLocalIdentifier": eltexBgpProcessLocalIdentifier,
       "eltexBgpProcessOperLocalIdentifier": eltexBgpProcessOperLocalIdentifier,
       "eltexBgpProcessTableVersion": eltexBgpProcessTableVersion,
       "eltexBgpProcessASNotation": eltexBgpProcessASNotation,
       "eltexBgpProcessClusterIdentifier": eltexBgpProcessClusterIdentifier,
       "eltexBgpProcessOperClusterIdentifier": eltexBgpProcessOperClusterIdentifier,
       "eltexBgpProcessInterClientReflEnabled": eltexBgpProcessInterClientReflEnabled,
       "eltexBgpProcessPathMtuDiscovery": eltexBgpProcessPathMtuDiscovery,
       "eltexBgpProcessAddrFamilyTable": eltexBgpProcessAddrFamilyTable,
       "eltexBgpProcessAddrFamilyEntry": eltexBgpProcessAddrFamilyEntry,
       "eltexBgpProcessAddrFamilyAfi": eltexBgpProcessAddrFamilyAfi,
       "eltexBgpProcessAddrFamilySafi": eltexBgpProcessAddrFamilySafi,
       "eltexBgpProcessAddrFamilyRowStatus": eltexBgpProcessAddrFamilyRowStatus,
       "eltexBgpPeer": eltexBgpPeer,
       "eltexBgpPeerData": eltexBgpPeerData,
       "eltexBgpPeerTable": eltexBgpPeerTable,
       "eltexBgpPeerEntry": eltexBgpPeerEntry,
       "eltexBgpPeerRemoteAddrType": eltexBgpPeerRemoteAddrType,
       "eltexBgpPeerRemoteAddr": eltexBgpPeerRemoteAddr,
       "eltexBgpPeerRowStatus": eltexBgpPeerRowStatus,
       "eltexBgpPeerAdminStatus": eltexBgpPeerAdminStatus,
       "eltexBgpPeerOperStatus": eltexBgpPeerOperStatus,
       "eltexBgpPeerRemoteAs": eltexBgpPeerRemoteAs,
       "eltexBgpPeerSourceInterface": eltexBgpPeerSourceInterface,
       "eltexBgpPeerNxtHopSlf": eltexBgpPeerNxtHopSlf,
       "eltexBgpPeerConfigMaxPrfx": eltexBgpPeerConfigMaxPrfx,
       "eltexBgpPeerConfigDropWarn": eltexBgpPeerConfigDropWarn,
       "eltexBgpPeerMaxPrfxHold": eltexBgpPeerMaxPrfxHold,
       "eltexBgpPeerConfigThreshold": eltexBgpPeerConfigThreshold,
       "eltexBgpPeerConnectRetryInterval": eltexBgpPeerConnectRetryInterval,
       "eltexBgpPeerHoldTimeConfigd": eltexBgpPeerHoldTimeConfigd,
       "eltexBgpPeerKeepAliveConfigd": eltexBgpPeerKeepAliveConfigd,
       "eltexBgpPeerMinRouteAdvertiseInterval": eltexBgpPeerMinRouteAdvertiseInterval,
       "eltexBgpPeerMinASOriginationInterval": eltexBgpPeerMinASOriginationInterval,
       "eltexBgpPeerMinRouteWithdrawInterval": eltexBgpPeerMinRouteWithdrawInterval,
       "eltexBgpPeerConfigOpenDelay": eltexBgpPeerConfigOpenDelay,
       "eltexBgpPeerConfigIdleHold": eltexBgpPeerConfigIdleHold,
       "eltexBgpPeerDistListPlIn": eltexBgpPeerDistListPlIn,
       "eltexBgpPeerDistListPlOut": eltexBgpPeerDistListPlOut,
       "eltexBgpPeerReflectorClient": eltexBgpPeerReflectorClient,
       "eltexBgpPeerSoftResetWithStoredInfo": eltexBgpPeerSoftResetWithStoredInfo,
       "eltexBgpPeerConfigPeerGroup": eltexBgpPeerConfigPeerGroup,
       "eltexBgpPeerPathMtuDiscovery": eltexBgpPeerPathMtuDiscovery,
       "eltexBgpPeerBfdDesired": eltexBgpPeerBfdDesired,
       "eltexBgpPeerAddrFamilyTable": eltexBgpPeerAddrFamilyTable,
       "eltexBgpPeerAddrFamilyEntry": eltexBgpPeerAddrFamilyEntry,
       "eltexBgpPeerAddrFamilyAfi": eltexBgpPeerAddrFamilyAfi,
       "eltexBgpPeerAddrFamilySafi": eltexBgpPeerAddrFamilySafi,
       "eltexBgpPeerAddrFamilyDisable": eltexBgpPeerAddrFamilyDisable,
       "eltexBgpPeerAddrFamilyNxtHopSlf": eltexBgpPeerAddrFamilyNxtHopSlf,
       "eltexBgpPeerAddrFamilyConfigMaxPrfx": eltexBgpPeerAddrFamilyConfigMaxPrfx,
       "eltexBgpPeerAddrFamilyConfigDropWarn": eltexBgpPeerAddrFamilyConfigDropWarn,
       "eltexBgpPeerAddrFamilyMaxPrfxHold": eltexBgpPeerAddrFamilyMaxPrfxHold,
       "eltexBgpPeerAddrFamilyConfigThreshold": eltexBgpPeerAddrFamilyConfigThreshold,
       "eltexBgpPeerAddrFamilyMinRteAdvertInt": eltexBgpPeerAddrFamilyMinRteAdvertInt,
       "eltexBgpPeerAddrFamilyMinASOrigInt": eltexBgpPeerAddrFamilyMinASOrigInt,
       "eltexBgpPeerAddrFamilyMinRteWithdrawInt": eltexBgpPeerAddrFamilyMinRteWithdrawInt,
       "eltexBgpPeerAddrFamilyReflectorClient": eltexBgpPeerAddrFamilyReflectorClient,
       "eltexBgpPeerAddrFamilyRouteMapIn": eltexBgpPeerAddrFamilyRouteMapIn,
       "eltexBgpPeerAddrFamilyRouteMapOut": eltexBgpPeerAddrFamilyRouteMapOut,
       "eltexBgpPeerStatusTable": eltexBgpPeerStatusTable,
       "eltexBgpPeerStatusEntry": eltexBgpPeerStatusEntry,
       "eltexBgpPeerStatusIdentifier": eltexBgpPeerStatusIdentifier,
       "eltexBgpPeerStatusState": eltexBgpPeerStatusState,
       "eltexBgpPeerStatusDynamicPeer": eltexBgpPeerStatusDynamicPeer,
       "eltexBgpPeerStatusRemoteAs": eltexBgpPeerStatusRemoteAs,
       "eltexBgpPeerStatusPeerIndex": eltexBgpPeerStatusPeerIndex,
       "eltexBgpPeerStatusCapsSupport": eltexBgpPeerStatusCapsSupport,
       "eltexBgpPeerStatusLastError": eltexBgpPeerStatusLastError,
       "eltexBgpPeerStatusLastErrorDataLen": eltexBgpPeerStatusLastErrorDataLen,
       "eltexBgpPeerStatusLastErrorData": eltexBgpPeerStatusLastErrorData,
       "eltexBgpPeerStatusFsmEstablishedTime": eltexBgpPeerStatusFsmEstablishedTime,
       "eltexBgpPeerStatusInUpdatesElpsTime": eltexBgpPeerStatusInUpdatesElpsTime,
       "eltexBgpPeerStatusHoldTime": eltexBgpPeerStatusHoldTime,
       "eltexBgpPeerStatusKeepAlive": eltexBgpPeerStatusKeepAlive,
       "eltexBgpPeerStatusInOpens": eltexBgpPeerStatusInOpens,
       "eltexBgpPeerStatusOutOpens": eltexBgpPeerStatusOutOpens,
       "eltexBgpPeerStatusInNotifications": eltexBgpPeerStatusInNotifications,
       "eltexBgpPeerStatusOutNotifications": eltexBgpPeerStatusOutNotifications,
       "eltexBgpPeerStatusInUpdates": eltexBgpPeerStatusInUpdates,
       "eltexBgpPeerStatusOutUpdates": eltexBgpPeerStatusOutUpdates,
       "eltexBgpPeerStatusInKeepalives": eltexBgpPeerStatusInKeepalives,
       "eltexBgpPeerStatusOutKeepalives": eltexBgpPeerStatusOutKeepalives,
       "eltexBgpPeerStatusInRefreshes": eltexBgpPeerStatusInRefreshes,
       "eltexBgpPeerStatusOutRefreshes": eltexBgpPeerStatusOutRefreshes,
       "eltexBgpPeerStatusInTotalMessages": eltexBgpPeerStatusInTotalMessages,
       "eltexBgpPeerStatusOutTotalMessages": eltexBgpPeerStatusOutTotalMessages,
       "eltexBgpPeerStatusFsmEstTransitions": eltexBgpPeerStatusFsmEstTransitions,
       "eltexBgpPeerStatusConnectRetryCount": eltexBgpPeerStatusConnectRetryCount,
       "eltexBgpPeerStatusClearCnts": eltexBgpPeerStatusClearCnts,
       "eltexBgpPeerStatusRtRefresh": eltexBgpPeerStatusRtRefresh,
       "eltexBgpPeerStatusLastErrorRcvd": eltexBgpPeerStatusLastErrorRcvd,
       "eltexBgpPeerStatusLastErrorRcvdTime": eltexBgpPeerStatusLastErrorRcvdTime,
       "eltexBgpPeerStatusLastErrorSent": eltexBgpPeerStatusLastErrorSent,
       "eltexBgpPeerStatusLastErrorSentTime": eltexBgpPeerStatusLastErrorSentTime,
       "eltexBgpPeerStatusLastState": eltexBgpPeerStatusLastState,
       "eltexBgpPeerStatusLastEvent": eltexBgpPeerStatusLastEvent,
       "eltexBgpPeerStatusCapsSent": eltexBgpPeerStatusCapsSent,
       "eltexBgpPeerStatusCapsRcvd": eltexBgpPeerStatusCapsRcvd,
       "eltexBgpPeerStatusCapsNegotiated": eltexBgpPeerStatusCapsNegotiated,
       "eltexBgpPeerStatusRcvdMsgElpsTime": eltexBgpPeerStatusRcvdMsgElpsTime,
       "eltexBgpPeerStatusIdleHoldRemTime": eltexBgpPeerStatusIdleHoldRemTime,
       "eltexBgpPeerStatusRouteRefrSent": eltexBgpPeerStatusRouteRefrSent,
       "eltexBgpPeerStatusRouteRefrRcvd": eltexBgpPeerStatusRouteRefrRcvd,
       "eltexBgpPeerStatusSelLocalAddrType": eltexBgpPeerStatusSelLocalAddrType,
       "eltexBgpPeerStatusSelLocalAddr": eltexBgpPeerStatusSelLocalAddr,
       "eltexBgpPeerStatusSelLocalPort": eltexBgpPeerStatusSelLocalPort,
       "eltexBgpPeerStatusSelRemotePort": eltexBgpPeerStatusSelRemotePort,
       "eltexBgpPeerStatusSelLocalAs": eltexBgpPeerStatusSelLocalAs,
       "eltexBgpPeerStatusSelRemoteAs": eltexBgpPeerStatusSelRemoteAs,
       "eltexBgpPeerStatusInPrfxes": eltexBgpPeerStatusInPrfxes,
       "eltexBgpPeerStatusOutPrfxes": eltexBgpPeerStatusOutPrfxes,
       "eltexBgpPeerStatusOutPrfxesAdvertised": eltexBgpPeerStatusOutPrfxesAdvertised,
       "eltexBgpPeerStatusConfigState": eltexBgpPeerStatusConfigState,
       "eltexBgpPeerStatusConnectRetryInt": eltexBgpPeerStatusConnectRetryInt,
       "eltexBgpPeerStatusConfigPassive": eltexBgpPeerStatusConfigPassive,
       "eltexBgpPeerStatusConfigOpenDelay": eltexBgpPeerStatusConfigOpenDelay,
       "eltexBgpPeerStatusConfigIdleHold": eltexBgpPeerStatusConfigIdleHold,
       "eltexBgpPeerStatusTtl": eltexBgpPeerStatusTtl,
       "eltexBgpPeerStatusHoldTimeConfigd": eltexBgpPeerStatusHoldTimeConfigd,
       "eltexBgpPeerStatusKeepAliveConfigd": eltexBgpPeerStatusKeepAliveConfigd,
       "eltexBgpPeerStatusResendAllRoutes": eltexBgpPeerStatusResendAllRoutes,
       "eltexBgpPeerStatusOutUpdateElpsTime": eltexBgpPeerStatusOutUpdateElpsTime,
       "eltexBgpPeerStatusOutPrfxesDenied": eltexBgpPeerStatusOutPrfxesDenied,
       "eltexBgpPeerStatusOutPrfxesImpWdr": eltexBgpPeerStatusOutPrfxesImpWdr,
       "eltexBgpPeerStatusOutPrfxesExpWdr": eltexBgpPeerStatusOutPrfxesExpWdr,
       "eltexBgpPeerStatusInPrfxesImpWdr": eltexBgpPeerStatusInPrfxesImpWdr,
       "eltexBgpPeerStatusInPrfxesExpWdr": eltexBgpPeerStatusInPrfxesExpWdr,
       "eltexBgpPeerStatusReceivedHoldTime": eltexBgpPeerStatusReceivedHoldTime,
       "eltexBgpPeerStatusDropSession": eltexBgpPeerStatusDropSession,
       "eltexBgpPeerStatusCeaseErrorSubcode": eltexBgpPeerStatusCeaseErrorSubcode,
       "eltexBgpPeerStatusBfdStatus": eltexBgpPeerStatusBfdStatus,
       "eltexBgpPeerAddrFamilyStatusTable": eltexBgpPeerAddrFamilyStatusTable,
       "eltexBgpPeerAddrFamilyStatusEntry": eltexBgpPeerAddrFamilyStatusEntry,
       "eltexBgpPeerAddrFamilyStatusRtRefresh": eltexBgpPeerAddrFamilyStatusRtRefresh,
       "eltexBgpPeerAddrFamilyStatusAddPathCapNeg": eltexBgpPeerAddrFamilyStatusAddPathCapNeg,
       "eltexBgpPeerAddrFamilyStatusReflectorClient": eltexBgpPeerAddrFamilyStatusReflectorClient,
       "eltexBgpPeerAddrFamilyStatusUpdateGroup": eltexBgpPeerAddrFamilyStatusUpdateGroup,
       "eltexBgpPeerAddrFamilyStatusResendAllRoutes": eltexBgpPeerAddrFamilyStatusResendAllRoutes,
       "eltexBgpPeerGroup": eltexBgpPeerGroup,
       "eltexBgpPeerGroupTable": eltexBgpPeerGroupTable,
       "eltexBgpPeerGroupEntry": eltexBgpPeerGroupEntry,
       "eltexBgpPeerGroupName": eltexBgpPeerGroupName,
       "eltexBgpPeerGroupRowStatus": eltexBgpPeerGroupRowStatus,
       "eltexBgpPeerGroupRemoteAs": eltexBgpPeerGroupRemoteAs,
       "eltexBgpPeerGroupSourceInterface": eltexBgpPeerGroupSourceInterface,
       "eltexBgpPeerGroupNxtHopSlf": eltexBgpPeerGroupNxtHopSlf,
       "eltexBgpPeerGroupConfigMaxPrfx": eltexBgpPeerGroupConfigMaxPrfx,
       "eltexBgpPeerGroupConfigDropWarn": eltexBgpPeerGroupConfigDropWarn,
       "eltexBgpPeerGroupMaxPrfxHold": eltexBgpPeerGroupMaxPrfxHold,
       "eltexBgpPeerGroupConfigThreshold": eltexBgpPeerGroupConfigThreshold,
       "eltexBgpPeerGroupConnectRetryInterval": eltexBgpPeerGroupConnectRetryInterval,
       "eltexBgpPeerGroupHoldTimeConfigd": eltexBgpPeerGroupHoldTimeConfigd,
       "eltexBgpPeerGroupKeepAliveConfigd": eltexBgpPeerGroupKeepAliveConfigd,
       "eltexBgpPeerGroupMinRouteAdvertiseInterval": eltexBgpPeerGroupMinRouteAdvertiseInterval,
       "eltexBgpPeerGroupMinASOriginationInterval": eltexBgpPeerGroupMinASOriginationInterval,
       "eltexBgpPeerGroupMinRouteWithdrawInterval": eltexBgpPeerGroupMinRouteWithdrawInterval,
       "eltexBgpPeerGroupConfigOpenDelay": eltexBgpPeerGroupConfigOpenDelay,
       "eltexBgpPeerGroupConfigIdleHold": eltexBgpPeerGroupConfigIdleHold,
       "eltexBgpPeerGroupDistListPlIn": eltexBgpPeerGroupDistListPlIn,
       "eltexBgpPeerGroupDistListPlOut": eltexBgpPeerGroupDistListPlOut,
       "eltexBgpPeerGroupReflectorClient": eltexBgpPeerGroupReflectorClient,
       "eltexBgpPeerGroupSoftResetWithStoredInfo": eltexBgpPeerGroupSoftResetWithStoredInfo,
       "eltexBgpPeerGroupBfdDesired": eltexBgpPeerGroupBfdDesired,
       "eltexBgpRib": eltexBgpRib,
       "eltexBgpLocRibTable": eltexBgpLocRibTable,
       "eltexBgpLocRibEntry": eltexBgpLocRibEntry,
       "eltexBgpLocRibAfi": eltexBgpLocRibAfi,
       "eltexBgpLocRibSafi": eltexBgpLocRibSafi,
       "eltexBgpLocRibPrfxType": eltexBgpLocRibPrfxType,
       "eltexBgpLocRibPrfx": eltexBgpLocRibPrfx,
       "eltexBgpLocRibPrfxLen": eltexBgpLocRibPrfxLen,
       "eltexBgpLocRibPeerOrRib": eltexBgpLocRibPeerOrRib,
       "eltexBgpLocRibPeerRibIndex": eltexBgpLocRibPeerRibIndex,
       "eltexBgpLocRibPathId": eltexBgpLocRibPathId,
       "eltexBgpLocRibBest": eltexBgpLocRibBest,
       "eltexBgpLocRibAsSize": eltexBgpLocRibAsSize,
       "eltexBgpLocRibASPathStr": eltexBgpLocRibASPathStr,
       "eltexBgpLocRibPathAttrOrigin": eltexBgpLocRibPathAttrOrigin,
       "eltexBgpLocRibPathAttrNextHopType": eltexBgpLocRibPathAttrNextHopType,
       "eltexBgpLocRibPathAttrNextHop": eltexBgpLocRibPathAttrNextHop,
       "eltexBgpLocRibPathAttrMultExtDisc": eltexBgpLocRibPathAttrMultExtDisc,
       "eltexBgpLocRibPathAttrLocalPref": eltexBgpLocRibPathAttrLocalPref,
       "eltexBgpLocRibPathAttrAtomicAgg": eltexBgpLocRibPathAttrAtomicAgg,
       "eltexBgpLocRibPathAttrAggAS": eltexBgpLocRibPathAttrAggAS,
       "eltexBgpLocRibPathAttrAggAddr": eltexBgpLocRibPathAttrAggAddr,
       "eltexBgpLocRibPathAttrCalcLclPref": eltexBgpLocRibPathAttrCalcLclPref,
       "eltexBgpLocRibPathAttrOrigId": eltexBgpLocRibPathAttrOrigId,
       "eltexBgpLocRibPathAttrWeight": eltexBgpLocRibPathAttrWeight,
       "eltexBgpLocRibEcmp": eltexBgpLocRibEcmp,
       "eltexBgpLocRibPathAttrAsPathLimAs": eltexBgpLocRibPathAttrAsPathLimAs,
       "eltexBgpLocRibPthAttAsPthLimUpper": eltexBgpLocRibPthAttAsPthLimUpper,
       "eltexBgpLocRibIsActive": eltexBgpLocRibIsActive,
       "eltexBgpLocRibPathAttrMEDPrsnt": eltexBgpLocRibPathAttrMEDPrsnt,
       "eltexBgpLocRibReasonNotBest": eltexBgpLocRibReasonNotBest,
       "eltexBgpLocRibPeerType": eltexBgpLocRibPeerType,
       "eltexBgpAdjRibInTable": eltexBgpAdjRibInTable,
       "eltexBgpAdjRibInEntry": eltexBgpAdjRibInEntry,
       "eltexBgpAdjRibInPeerIndex": eltexBgpAdjRibInPeerIndex,
       "eltexBgpAdjRibInAfi": eltexBgpAdjRibInAfi,
       "eltexBgpAdjRibInSafi": eltexBgpAdjRibInSafi,
       "eltexBgpAdjRibInPrfxType": eltexBgpAdjRibInPrfxType,
       "eltexBgpAdjRibInPrfx": eltexBgpAdjRibInPrfx,
       "eltexBgpAdjRibInPrfxLen": eltexBgpAdjRibInPrfxLen,
       "eltexBgpAdjRibInPathId": eltexBgpAdjRibInPathId,
       "eltexBgpAdjRibInAsSize": eltexBgpAdjRibInAsSize,
       "eltexBgpAdjRibInASPathStr": eltexBgpAdjRibInASPathStr,
       "eltexBgpAdjRibInPathAttrOrigin": eltexBgpAdjRibInPathAttrOrigin,
       "eltexBgpAdjRibInPathAttrNextHopType": eltexBgpAdjRibInPathAttrNextHopType,
       "eltexBgpAdjRibInPathAttrNextHop": eltexBgpAdjRibInPathAttrNextHop,
       "eltexBgpAdjRibInPathAttrMultiExitDisc": eltexBgpAdjRibInPathAttrMultiExitDisc,
       "eltexBgpAdjRibInPathAttrLocalPref": eltexBgpAdjRibInPathAttrLocalPref,
       "eltexBgpAdjRibInPathAttrAtomicAggregate": eltexBgpAdjRibInPathAttrAtomicAggregate,
       "eltexBgpAdjRibInPathAttrAggregatorAS": eltexBgpAdjRibInPathAttrAggregatorAS,
       "eltexBgpAdjRibInPathAttrAggregatorAddr": eltexBgpAdjRibInPathAttrAggregatorAddr,
       "eltexBgpAdjRibInPathAttrOrigId": eltexBgpAdjRibInPathAttrOrigId,
       "eltexBgpAdjRibInPathAttrAsPathLimAs": eltexBgpAdjRibInPathAttrAsPathLimAs,
       "eltexBgpAdjRibInPathAttrAsPathLimUpper": eltexBgpAdjRibInPathAttrAsPathLimUpper,
       "eltexBgpAdjRibInPathAttrMEDPrsnt": eltexBgpAdjRibInPathAttrMEDPrsnt,
       "eltexBgpAdjRibInPathAccepted": eltexBgpAdjRibInPathAccepted,
       "eltexBgpAdjRibOutTable": eltexBgpAdjRibOutTable,
       "eltexBgpAdjRibOutEntry": eltexBgpAdjRibOutEntry,
       "eltexBgpAdjRibOutAfi": eltexBgpAdjRibOutAfi,
       "eltexBgpAdjRibOutSafi": eltexBgpAdjRibOutSafi,
       "eltexBgpAdjRibOutPrfxType": eltexBgpAdjRibOutPrfxType,
       "eltexBgpAdjRibOutPrfx": eltexBgpAdjRibOutPrfx,
       "eltexBgpAdjRibOutPrfxLen": eltexBgpAdjRibOutPrfxLen,
       "eltexBgpAdjRibOutPathId": eltexBgpAdjRibOutPathId,
       "eltexBgpAdjRibOutBest": eltexBgpAdjRibOutBest,
       "eltexBgpAdjRibOutAdvertStatus": eltexBgpAdjRibOutAdvertStatus,
       "eltexBgpAdjRibOutLocalAggrType": eltexBgpAdjRibOutLocalAggrType,
       "eltexBgpAdjRibOutAsSize": eltexBgpAdjRibOutAsSize,
       "eltexBgpAdjRibOutASPathStr": eltexBgpAdjRibOutASPathStr,
       "eltexBgpAdjRibOutOrigin": eltexBgpAdjRibOutOrigin,
       "eltexBgpAdjRibOutNextHopType": eltexBgpAdjRibOutNextHopType,
       "eltexBgpAdjRibOutNextHop": eltexBgpAdjRibOutNextHop,
       "eltexBgpAdjRibOutMultiExitDisc": eltexBgpAdjRibOutMultiExitDisc,
       "eltexBgpAdjRibOutLocalPref": eltexBgpAdjRibOutLocalPref,
       "eltexBgpAdjRibOutAtomicAggregate": eltexBgpAdjRibOutAtomicAggregate,
       "eltexBgpAdjRibOutAggregatorAS": eltexBgpAdjRibOutAggregatorAS,
       "eltexBgpAdjRibOutAggregatorAddr": eltexBgpAdjRibOutAggregatorAddr,
       "eltexBgpAdjRibOutOrigId": eltexBgpAdjRibOutOrigId,
       "eltexBgpAdjRibOutEcmp": eltexBgpAdjRibOutEcmp,
       "eltexBgpAdjRibOutAsLimAs": eltexBgpAdjRibOutAsLimAs,
       "eltexBgpAdjRibOutAsLimUpper": eltexBgpAdjRibOutAsLimUpper,
       "eltexBgpAdjRibOutIsActive": eltexBgpAdjRibOutIsActive,
       "eltexBgpAdjRibOutMEDPrsnt": eltexBgpAdjRibOutMEDPrsnt,
       "eltexBgpAdjRibOutPeerType": eltexBgpAdjRibOutPeerType,
       "eltexBgpNetworkTable": eltexBgpNetworkTable,
       "eltexBgpNetworkEntry": eltexBgpNetworkEntry,
       "eltexBgpNetworkAfi": eltexBgpNetworkAfi,
       "eltexBgpNetworkSafi": eltexBgpNetworkSafi,
       "eltexBgpNetworkPrfxType": eltexBgpNetworkPrfxType,
       "eltexBgpNetworkPrfx": eltexBgpNetworkPrfx,
       "eltexBgpNetworkPrfxLen": eltexBgpNetworkPrfxLen,
       "eltexBgpNetworkRowStatus": eltexBgpNetworkRowStatus,
       "eltexBgpPathAttrExtensions": eltexBgpPathAttrExtensions,
       "eltexBgpPathAttrRouteReflectionExts": eltexBgpPathAttrRouteReflectionExts,
       "eltexBgpPathAttrClusterLocTable": eltexBgpPathAttrClusterLocTable,
       "eltexBgpPathAttrClusterLocEntry": eltexBgpPathAttrClusterLocEntry,
       "eltexBgpPathAttrClusterLocIndex": eltexBgpPathAttrClusterLocIndex,
       "eltexBgpPathAttrClusterLocValue": eltexBgpPathAttrClusterLocValue}
)
