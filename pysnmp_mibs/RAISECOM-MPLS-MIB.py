# SNMP MIB module (RAISECOM-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-MPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:15 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(mplsXCEntry,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsXCEntry")

(pwEntry,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwEntry")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

raisecomMpls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RefreshInterval(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomMplsLsrObjects_ObjectIdentity = ObjectIdentity
raisecomMplsLsrObjects = _RaisecomMplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1)
)
_RaisecomMplsLsrId_Type = InetAddressIPv4
_RaisecomMplsLsrId_Object = MibScalar
raisecomMplsLsrId = _RaisecomMplsLsrId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 1),
    _RaisecomMplsLsrId_Type()
)
raisecomMplsLsrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLsrId.setStatus("current")


class _RaisecomMplsEnable_Type(TruthValue):
    """Custom type raisecomMplsEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsEnable_Type.__name__ = "TruthValue"
_RaisecomMplsEnable_Object = MibScalar
raisecomMplsEnable = _RaisecomMplsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 2),
    _RaisecomMplsEnable_Type()
)
raisecomMplsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsEnable.setStatus("current")


class _RaisecomMplsLspStatisticsClear_Type(TruthValue):
    """Custom type raisecomMplsLspStatisticsClear based on TruthValue"""
    defaultValue = 2


_RaisecomMplsLspStatisticsClear_Type.__name__ = "TruthValue"
_RaisecomMplsLspStatisticsClear_Object = MibScalar
raisecomMplsLspStatisticsClear = _RaisecomMplsLspStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 3),
    _RaisecomMplsLspStatisticsClear_Type()
)
raisecomMplsLspStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLspStatisticsClear.setStatus("current")
_RaisecomMplsInterfaceTable_Object = MibTable
raisecomMplsInterfaceTable = _RaisecomMplsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomMplsInterfaceTable.setStatus("current")
_RaisecomMplsInterfaceEntry_Object = MibTableRow
raisecomMplsInterfaceEntry = _RaisecomMplsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 4, 1)
)
raisecomMplsInterfaceEntry.setIndexNames(
    (0, "RAISECOM-MPLS-MIB", "raisecomMplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    raisecomMplsInterfaceEntry.setStatus("current")
_RaisecomMplsInterfaceIndex_Type = InterfaceIndexOrZero
_RaisecomMplsInterfaceIndex_Object = MibTableColumn
raisecomMplsInterfaceIndex = _RaisecomMplsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 4, 1, 1),
    _RaisecomMplsInterfaceIndex_Type()
)
raisecomMplsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomMplsInterfaceIndex.setStatus("current")


class _RaisecomMplsInterfaceEnable_Type(TruthValue):
    """Custom type raisecomMplsInterfaceEnable based on TruthValue"""
    defaultValue = 1


_RaisecomMplsInterfaceEnable_Type.__name__ = "TruthValue"
_RaisecomMplsInterfaceEnable_Object = MibTableColumn
raisecomMplsInterfaceEnable = _RaisecomMplsInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 4, 1, 2),
    _RaisecomMplsInterfaceEnable_Type()
)
raisecomMplsInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsInterfaceEnable.setStatus("current")
_RaisecomMplsLspTable_Object = MibTable
raisecomMplsLspTable = _RaisecomMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 5)
)
if mibBuilder.loadTexts:
    raisecomMplsLspTable.setStatus("current")
_RaisecomMplsLspEntry_Object = MibTableRow
raisecomMplsLspEntry = _RaisecomMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 5, 1)
)
if mibBuilder.loadTexts:
    raisecomMplsLspEntry.setStatus("current")


class _RaisecomMplsLspName_Type(OctetString):
    """Custom type raisecomMplsLspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RaisecomMplsLspName_Type.__name__ = "OctetString"
_RaisecomMplsLspName_Object = MibTableColumn
raisecomMplsLspName = _RaisecomMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 5, 1, 1),
    _RaisecomMplsLspName_Type()
)
raisecomMplsLspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLspName.setStatus("current")
_RaisecomMplsLspStatisticsObjects_ObjectIdentity = ObjectIdentity
raisecomMplsLspStatisticsObjects = _RaisecomMplsLspStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6)
)
_RaisecomMplsLspConfigured_Type = Unsigned32
_RaisecomMplsLspConfigured_Object = MibScalar
raisecomMplsLspConfigured = _RaisecomMplsLspConfigured_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 1),
    _RaisecomMplsLspConfigured_Type()
)
raisecomMplsLspConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspConfigured.setStatus("current")
_RaisecomMplsLspActicve_Type = Unsigned32
_RaisecomMplsLspActicve_Object = MibScalar
raisecomMplsLspActicve = _RaisecomMplsLspActicve_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 2),
    _RaisecomMplsLspActicve_Type()
)
raisecomMplsLspActicve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspActicve.setStatus("current")
_RaisecomMplsLspInActicve_Type = Unsigned32
_RaisecomMplsLspInActicve_Object = MibScalar
raisecomMplsLspInActicve = _RaisecomMplsLspInActicve_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 3),
    _RaisecomMplsLspInActicve_Type()
)
raisecomMplsLspInActicve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspInActicve.setStatus("current")
_RaisecomMplsLspIngress_Type = Unsigned32
_RaisecomMplsLspIngress_Object = MibScalar
raisecomMplsLspIngress = _RaisecomMplsLspIngress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 4),
    _RaisecomMplsLspIngress_Type()
)
raisecomMplsLspIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspIngress.setStatus("current")
_RaisecomMplsLspTransit_Type = Unsigned32
_RaisecomMplsLspTransit_Object = MibScalar
raisecomMplsLspTransit = _RaisecomMplsLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 5),
    _RaisecomMplsLspTransit_Type()
)
raisecomMplsLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspTransit.setStatus("current")
_RaisecomMplsLspEgress_Type = Unsigned32
_RaisecomMplsLspEgress_Object = MibScalar
raisecomMplsLspEgress = _RaisecomMplsLspEgress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 6),
    _RaisecomMplsLspEgress_Type()
)
raisecomMplsLspEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspEgress.setStatus("current")
_RaisecomMplsLspStatic_Type = Unsigned32
_RaisecomMplsLspStatic_Object = MibScalar
raisecomMplsLspStatic = _RaisecomMplsLspStatic_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 7),
    _RaisecomMplsLspStatic_Type()
)
raisecomMplsLspStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspStatic.setStatus("current")
_RaisecomMplsLspLdp_Type = Unsigned32
_RaisecomMplsLspLdp_Object = MibScalar
raisecomMplsLspLdp = _RaisecomMplsLspLdp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 8),
    _RaisecomMplsLspLdp_Type()
)
raisecomMplsLspLdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspLdp.setStatus("current")
_RaisecomMplsLspRsvpTe_Type = Unsigned32
_RaisecomMplsLspRsvpTe_Object = MibScalar
raisecomMplsLspRsvpTe = _RaisecomMplsLspRsvpTe_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 6, 9),
    _RaisecomMplsLspRsvpTe_Type()
)
raisecomMplsLspRsvpTe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLspRsvpTe.setStatus("current")


class _RaisecomMplsTunnelReroutedNotifEnable_Type(TruthValue):
    """Custom type raisecomMplsTunnelReroutedNotifEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsTunnelReroutedNotifEnable_Type.__name__ = "TruthValue"
_RaisecomMplsTunnelReroutedNotifEnable_Object = MibScalar
raisecomMplsTunnelReroutedNotifEnable = _RaisecomMplsTunnelReroutedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 7),
    _RaisecomMplsTunnelReroutedNotifEnable_Type()
)
raisecomMplsTunnelReroutedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsTunnelReroutedNotifEnable.setStatus("current")


class _RaisecomMplsTunnelReoptimizedNotifEnable_Type(TruthValue):
    """Custom type raisecomMplsTunnelReoptimizedNotifEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsTunnelReoptimizedNotifEnable_Type.__name__ = "TruthValue"
_RaisecomMplsTunnelReoptimizedNotifEnable_Object = MibScalar
raisecomMplsTunnelReoptimizedNotifEnable = _RaisecomMplsTunnelReoptimizedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 8),
    _RaisecomMplsTunnelReoptimizedNotifEnable_Type()
)
raisecomMplsTunnelReoptimizedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsTunnelReoptimizedNotifEnable.setStatus("current")


class _RaisecomMplsTtlPublicPropagate_Type(TruthValue):
    """Custom type raisecomMplsTtlPublicPropagate based on TruthValue"""
    defaultValue = 1


_RaisecomMplsTtlPublicPropagate_Type.__name__ = "TruthValue"
_RaisecomMplsTtlPublicPropagate_Object = MibScalar
raisecomMplsTtlPublicPropagate = _RaisecomMplsTtlPublicPropagate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 9),
    _RaisecomMplsTtlPublicPropagate_Type()
)
raisecomMplsTtlPublicPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsTtlPublicPropagate.setStatus("current")


class _RaisecomMplsTtlVpnPropagate_Type(TruthValue):
    """Custom type raisecomMplsTtlVpnPropagate based on TruthValue"""
    defaultValue = 2


_RaisecomMplsTtlVpnPropagate_Type.__name__ = "TruthValue"
_RaisecomMplsTtlVpnPropagate_Object = MibScalar
raisecomMplsTtlVpnPropagate = _RaisecomMplsTtlVpnPropagate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 1, 10),
    _RaisecomMplsTtlVpnPropagate_Type()
)
raisecomMplsTtlVpnPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsTtlVpnPropagate.setStatus("current")
_RaisecomMplsVpnObjects_ObjectIdentity = ObjectIdentity
raisecomMplsVpnObjects = _RaisecomMplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2)
)
_RaisecomMplsL2VpnObjects_ObjectIdentity = ObjectIdentity
raisecomMplsL2VpnObjects = _RaisecomMplsL2VpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1)
)


class _RaisecomMplsL2vpnEnable_Type(TruthValue):
    """Custom type raisecomMplsL2vpnEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsL2vpnEnable_Type.__name__ = "TruthValue"
_RaisecomMplsL2vpnEnable_Object = MibScalar
raisecomMplsL2vpnEnable = _RaisecomMplsL2vpnEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 1),
    _RaisecomMplsL2vpnEnable_Type()
)
raisecomMplsL2vpnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsL2vpnEnable.setStatus("current")


class _RaisecomMplsL2vpnMartiniEnable_Type(TruthValue):
    """Custom type raisecomMplsL2vpnMartiniEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsL2vpnMartiniEnable_Type.__name__ = "TruthValue"
_RaisecomMplsL2vpnMartiniEnable_Object = MibScalar
raisecomMplsL2vpnMartiniEnable = _RaisecomMplsL2vpnMartiniEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 2),
    _RaisecomMplsL2vpnMartiniEnable_Type()
)
raisecomMplsL2vpnMartiniEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsL2vpnMartiniEnable.setStatus("current")
_RaisecomMplsL2vpnInterfaceTable_Object = MibTable
raisecomMplsL2vpnInterfaceTable = _RaisecomMplsL2vpnInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomMplsL2vpnInterfaceTable.setStatus("current")
_RaisecomMplsL2vpnInterfaceEntry_Object = MibTableRow
raisecomMplsL2vpnInterfaceEntry = _RaisecomMplsL2vpnInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 3, 1)
)
raisecomMplsL2vpnInterfaceEntry.setIndexNames(
    (0, "RAISECOM-MPLS-MIB", "raisecomMplsL2vpnInterfaceIndex"),
)
if mibBuilder.loadTexts:
    raisecomMplsL2vpnInterfaceEntry.setStatus("current")
_RaisecomMplsL2vpnInterfaceIndex_Type = InterfaceIndexOrZero
_RaisecomMplsL2vpnInterfaceIndex_Object = MibTableColumn
raisecomMplsL2vpnInterfaceIndex = _RaisecomMplsL2vpnInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 3, 1, 1),
    _RaisecomMplsL2vpnInterfaceIndex_Type()
)
raisecomMplsL2vpnInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomMplsL2vpnInterfaceIndex.setStatus("current")


class _RaisecomMplsL2vpnInterfaceEnable_Type(TruthValue):
    """Custom type raisecomMplsL2vpnInterfaceEnable based on TruthValue"""
    defaultValue = 1


_RaisecomMplsL2vpnInterfaceEnable_Type.__name__ = "TruthValue"
_RaisecomMplsL2vpnInterfaceEnable_Object = MibTableColumn
raisecomMplsL2vpnInterfaceEnable = _RaisecomMplsL2vpnInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 3, 1, 2),
    _RaisecomMplsL2vpnInterfaceEnable_Type()
)
raisecomMplsL2vpnInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsL2vpnInterfaceEnable.setStatus("current")
_RaisecomMplsCccPwTable_Object = MibTable
raisecomMplsCccPwTable = _RaisecomMplsCccPwTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomMplsCccPwTable.setStatus("current")
_RaisecomMplsCccPwEntry_Object = MibTableRow
raisecomMplsCccPwEntry = _RaisecomMplsCccPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    raisecomMplsCccPwEntry.setStatus("current")
_RaisecomMplsCccNexthopType_Type = InetAddressType
_RaisecomMplsCccNexthopType_Object = MibTableColumn
raisecomMplsCccNexthopType = _RaisecomMplsCccNexthopType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 4, 1, 1),
    _RaisecomMplsCccNexthopType_Type()
)
raisecomMplsCccNexthopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMplsCccNexthopType.setStatus("current")
_RaisecomMplsCccNexthop_Type = InetAddress
_RaisecomMplsCccNexthop_Object = MibTableColumn
raisecomMplsCccNexthop = _RaisecomMplsCccNexthop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 2, 1, 4, 1, 2),
    _RaisecomMplsCccNexthop_Type()
)
raisecomMplsCccNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMplsCccNexthop.setStatus("current")
_RaisecomMplsLdpObjects_ObjectIdentity = ObjectIdentity
raisecomMplsLdpObjects = _RaisecomMplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3)
)


class _RaisecomMplsLdpEnable_Type(TruthValue):
    """Custom type raisecomMplsLdpEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsLdpEnable_Type.__name__ = "TruthValue"
_RaisecomMplsLdpEnable_Object = MibScalar
raisecomMplsLdpEnable = _RaisecomMplsLdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 1),
    _RaisecomMplsLdpEnable_Type()
)
raisecomMplsLdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpEnable.setStatus("current")
_RaisecomMplsLdpInterfaceTable_Object = MibTable
raisecomMplsLdpInterfaceTable = _RaisecomMplsLdpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2)
)
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceTable.setStatus("current")
_RaisecomMplsLdpInterfaceEntry_Object = MibTableRow
raisecomMplsLdpInterfaceEntry = _RaisecomMplsLdpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1)
)
raisecomMplsLdpInterfaceEntry.setIndexNames(
    (0, "RAISECOM-MPLS-MIB", "raisecomMplsLdpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceEntry.setStatus("current")
_RaisecomMplsLdpInterfaceIndex_Type = InterfaceIndexOrZero
_RaisecomMplsLdpInterfaceIndex_Object = MibTableColumn
raisecomMplsLdpInterfaceIndex = _RaisecomMplsLdpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 1),
    _RaisecomMplsLdpInterfaceIndex_Type()
)
raisecomMplsLdpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceIndex.setStatus("current")


class _RaisecomMplsLdpInterfaceEnable_Type(TruthValue):
    """Custom type raisecomMplsLdpInterfaceEnable based on TruthValue"""
    defaultValue = 1


_RaisecomMplsLdpInterfaceEnable_Type.__name__ = "TruthValue"
_RaisecomMplsLdpInterfaceEnable_Object = MibTableColumn
raisecomMplsLdpInterfaceEnable = _RaisecomMplsLdpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 2),
    _RaisecomMplsLdpInterfaceEnable_Type()
)
raisecomMplsLdpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceEnable.setStatus("current")
_RaisecomMplsLdpInterfaceLAM_Type = Integer32
_RaisecomMplsLdpInterfaceLAM_Object = MibTableColumn
raisecomMplsLdpInterfaceLAM = _RaisecomMplsLdpInterfaceLAM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 3),
    _RaisecomMplsLdpInterfaceLAM_Type()
)
raisecomMplsLdpInterfaceLAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceLAM.setStatus("current")
_RaisecomMplsLdpInterfaceTransportAddress_Type = InetAddress
_RaisecomMplsLdpInterfaceTransportAddress_Object = MibTableColumn
raisecomMplsLdpInterfaceTransportAddress = _RaisecomMplsLdpInterfaceTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 4),
    _RaisecomMplsLdpInterfaceTransportAddress_Type()
)
raisecomMplsLdpInterfaceTransportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceTransportAddress.setStatus("current")
_RaisecomMplsLdpInterfaceLdpID_Type = OctetString
_RaisecomMplsLdpInterfaceLdpID_Object = MibTableColumn
raisecomMplsLdpInterfaceLdpID = _RaisecomMplsLdpInterfaceLdpID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 5),
    _RaisecomMplsLdpInterfaceLdpID_Type()
)
raisecomMplsLdpInterfaceLdpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceLdpID.setStatus("current")


class _RaisecomMplsLdpInterfaceMTU_Type(Integer32):
    """Custom type raisecomMplsLdpInterfaceMTU based on Integer32"""
    defaultValue = 1500


_RaisecomMplsLdpInterfaceMTU_Type.__name__ = "Integer32"
_RaisecomMplsLdpInterfaceMTU_Object = MibTableColumn
raisecomMplsLdpInterfaceMTU = _RaisecomMplsLdpInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 6),
    _RaisecomMplsLdpInterfaceMTU_Type()
)
raisecomMplsLdpInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceMTU.setStatus("current")


class _RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Type(Integer32):
    """Custom type raisecomMplsLdpInterfaceKeepAliveHoldTimer based on Integer32"""
    defaultValue = 40


_RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Type.__name__ = "Integer32"
_RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Object = MibTableColumn
raisecomMplsLdpInterfaceKeepAliveHoldTimer = _RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 7),
    _RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Type()
)
raisecomMplsLdpInterfaceKeepAliveHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceKeepAliveHoldTimer.setStatus("current")


class _RaisecomMplsLdpInterfaceHelloHoldTimer_Type(Integer32):
    """Custom type raisecomMplsLdpInterfaceHelloHoldTimer based on Integer32"""
    defaultValue = 0


_RaisecomMplsLdpInterfaceHelloHoldTimer_Type.__name__ = "Integer32"
_RaisecomMplsLdpInterfaceHelloHoldTimer_Object = MibTableColumn
raisecomMplsLdpInterfaceHelloHoldTimer = _RaisecomMplsLdpInterfaceHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 2, 1, 8),
    _RaisecomMplsLdpInterfaceHelloHoldTimer_Type()
)
raisecomMplsLdpInterfaceHelloHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpInterfaceHelloHoldTimer.setStatus("current")


class _RaisecomMplsLdpSessionStatusTrapEnable_Type(TruthValue):
    """Custom type raisecomMplsLdpSessionStatusTrapEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsLdpSessionStatusTrapEnable_Type.__name__ = "TruthValue"
_RaisecomMplsLdpSessionStatusTrapEnable_Object = MibScalar
raisecomMplsLdpSessionStatusTrapEnable = _RaisecomMplsLdpSessionStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 3),
    _RaisecomMplsLdpSessionStatusTrapEnable_Type()
)
raisecomMplsLdpSessionStatusTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpSessionStatusTrapEnable.setStatus("current")


class _RaisecomMplsLdpPathVecLimitTrapEnable_Type(TruthValue):
    """Custom type raisecomMplsLdpPathVecLimitTrapEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsLdpPathVecLimitTrapEnable_Type.__name__ = "TruthValue"
_RaisecomMplsLdpPathVecLimitTrapEnable_Object = MibScalar
raisecomMplsLdpPathVecLimitTrapEnable = _RaisecomMplsLdpPathVecLimitTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 4),
    _RaisecomMplsLdpPathVecLimitTrapEnable_Type()
)
raisecomMplsLdpPathVecLimitTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpPathVecLimitTrapEnable.setStatus("current")


class _RaisecomMplsLdpSessionThreshTrapEnable_Type(TruthValue):
    """Custom type raisecomMplsLdpSessionThreshTrapEnable based on TruthValue"""
    defaultValue = 2


_RaisecomMplsLdpSessionThreshTrapEnable_Type.__name__ = "TruthValue"
_RaisecomMplsLdpSessionThreshTrapEnable_Object = MibScalar
raisecomMplsLdpSessionThreshTrapEnable = _RaisecomMplsLdpSessionThreshTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 3, 5),
    _RaisecomMplsLdpSessionThreshTrapEnable_Type()
)
raisecomMplsLdpSessionThreshTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsLdpSessionThreshTrapEnable.setStatus("current")
_RaisecomMplsRsvpTEObjects_ObjectIdentity = ObjectIdentity
raisecomMplsRsvpTEObjects = _RaisecomMplsRsvpTEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4)
)


class _RaisecomMplsRsvpTEEnabled_Type(TruthValue):
    """Custom type raisecomMplsRsvpTEEnabled based on TruthValue"""
    defaultValue = 2


_RaisecomMplsRsvpTEEnabled_Type.__name__ = "TruthValue"
_RaisecomMplsRsvpTEEnabled_Object = MibScalar
raisecomMplsRsvpTEEnabled = _RaisecomMplsRsvpTEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 1),
    _RaisecomMplsRsvpTEEnabled_Type()
)
raisecomMplsRsvpTEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEEnabled.setStatus("current")


class _RaisecomMplsRsvpTERefreshInterval_Type(RefreshInterval):
    """Custom type raisecomMplsRsvpTERefreshInterval based on RefreshInterval"""
    defaultValue = 3000


_RaisecomMplsRsvpTERefreshInterval_Type.__name__ = "RefreshInterval"
_RaisecomMplsRsvpTERefreshInterval_Object = MibScalar
raisecomMplsRsvpTERefreshInterval = _RaisecomMplsRsvpTERefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 2),
    _RaisecomMplsRsvpTERefreshInterval_Type()
)
raisecomMplsRsvpTERefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTERefreshInterval.setStatus("current")


class _RaisecomMplsRsvpTERefreshMultiple_Type(Integer32):
    """Custom type raisecomMplsRsvpTERefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_RaisecomMplsRsvpTERefreshMultiple_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTERefreshMultiple_Object = MibScalar
raisecomMplsRsvpTERefreshMultiple = _RaisecomMplsRsvpTERefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 3),
    _RaisecomMplsRsvpTERefreshMultiple_Type()
)
raisecomMplsRsvpTERefreshMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTERefreshMultiple.setStatus("current")


class _RaisecomMplsRsvpTERefreshBlockadeMultiple_Type(Integer32):
    """Custom type raisecomMplsRsvpTERefreshBlockadeMultiple based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RaisecomMplsRsvpTERefreshBlockadeMultiple_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTERefreshBlockadeMultiple_Object = MibScalar
raisecomMplsRsvpTERefreshBlockadeMultiple = _RaisecomMplsRsvpTERefreshBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 4),
    _RaisecomMplsRsvpTERefreshBlockadeMultiple_Type()
)
raisecomMplsRsvpTERefreshBlockadeMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTERefreshBlockadeMultiple.setStatus("current")


class _RaisecomMplsRsvpTELSPSetupPriority_Type(Integer32):
    """Custom type raisecomMplsRsvpTELSPSetupPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomMplsRsvpTELSPSetupPriority_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTELSPSetupPriority_Object = MibScalar
raisecomMplsRsvpTELSPSetupPriority = _RaisecomMplsRsvpTELSPSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 5),
    _RaisecomMplsRsvpTELSPSetupPriority_Type()
)
raisecomMplsRsvpTELSPSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTELSPSetupPriority.setStatus("deprecated")


class _RaisecomMplsRsvpTELSPHoldingPriority_Type(Integer32):
    """Custom type raisecomMplsRsvpTELSPHoldingPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomMplsRsvpTELSPHoldingPriority_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTELSPHoldingPriority_Object = MibScalar
raisecomMplsRsvpTELSPHoldingPriority = _RaisecomMplsRsvpTELSPHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 6),
    _RaisecomMplsRsvpTELSPHoldingPriority_Type()
)
raisecomMplsRsvpTELSPHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTELSPHoldingPriority.setStatus("deprecated")


class _RaisecomMplsRsvpTEInitPathRRInterval_Type(Integer32):
    """Custom type raisecomMplsRsvpTEInitPathRRInterval based on Integer32"""
    defaultValue = 2000


_RaisecomMplsRsvpTEInitPathRRInterval_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTEInitPathRRInterval_Object = MibScalar
raisecomMplsRsvpTEInitPathRRInterval = _RaisecomMplsRsvpTEInitPathRRInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 7),
    _RaisecomMplsRsvpTEInitPathRRInterval_Type()
)
raisecomMplsRsvpTEInitPathRRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEInitPathRRInterval.setStatus("current")


class _RaisecomMplsRsvpTEInitPathRRDecay_Type(Integer32):
    """Custom type raisecomMplsRsvpTEInitPathRRDecay based on Integer32"""
    defaultValue = 100


_RaisecomMplsRsvpTEInitPathRRDecay_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTEInitPathRRDecay_Object = MibScalar
raisecomMplsRsvpTEInitPathRRDecay = _RaisecomMplsRsvpTEInitPathRRDecay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 8),
    _RaisecomMplsRsvpTEInitPathRRDecay_Type()
)
raisecomMplsRsvpTEInitPathRRDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEInitPathRRDecay.setStatus("current")


class _RaisecomMplsRsvpTEInitPathRRLimit_Type(Integer32):
    """Custom type raisecomMplsRsvpTEInitPathRRLimit based on Integer32"""
    defaultValue = 2


_RaisecomMplsRsvpTEInitPathRRLimit_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTEInitPathRRLimit_Object = MibScalar
raisecomMplsRsvpTEInitPathRRLimit = _RaisecomMplsRsvpTEInitPathRRLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 9),
    _RaisecomMplsRsvpTEInitPathRRLimit_Type()
)
raisecomMplsRsvpTEInitPathRRLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEInitPathRRLimit.setStatus("current")
_RaisecomMplsRsvpTEInterfaceTable_Object = MibTable
raisecomMplsRsvpTEInterfaceTable = _RaisecomMplsRsvpTEInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10)
)
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEInterfaceTable.setStatus("current")
_RaisecomMplsRsvpTEInterfaceEntry_Object = MibTableRow
raisecomMplsRsvpTEInterfaceEntry = _RaisecomMplsRsvpTEInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1)
)
raisecomMplsRsvpTEInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEInterfaceEntry.setStatus("current")


class _RaisecomMplsRsvpTEIfRefreshInterval_Type(RefreshInterval):
    """Custom type raisecomMplsRsvpTEIfRefreshInterval based on RefreshInterval"""
    defaultValue = 0


_RaisecomMplsRsvpTEIfRefreshInterval_Type.__name__ = "RefreshInterval"
_RaisecomMplsRsvpTEIfRefreshInterval_Object = MibTableColumn
raisecomMplsRsvpTEIfRefreshInterval = _RaisecomMplsRsvpTEIfRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 1),
    _RaisecomMplsRsvpTEIfRefreshInterval_Type()
)
raisecomMplsRsvpTEIfRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfRefreshInterval.setUnits("milliseconds")


class _RaisecomMplsRsvpTEIfRefreshMultiple_Type(Integer32):
    """Custom type raisecomMplsRsvpTEIfRefreshMultiple based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RaisecomMplsRsvpTEIfRefreshMultiple_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTEIfRefreshMultiple_Object = MibTableColumn
raisecomMplsRsvpTEIfRefreshMultiple = _RaisecomMplsRsvpTEIfRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 2),
    _RaisecomMplsRsvpTEIfRefreshMultiple_Type()
)
raisecomMplsRsvpTEIfRefreshMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfRefreshMultiple.setStatus("current")


class _RaisecomMplsRsvpTEIfBlockadeMultiple_Type(Integer32):
    """Custom type raisecomMplsRsvpTEIfBlockadeMultiple based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RaisecomMplsRsvpTEIfBlockadeMultiple_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTEIfBlockadeMultiple_Object = MibTableColumn
raisecomMplsRsvpTEIfBlockadeMultiple = _RaisecomMplsRsvpTEIfBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 3),
    _RaisecomMplsRsvpTEIfBlockadeMultiple_Type()
)
raisecomMplsRsvpTEIfBlockadeMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfBlockadeMultiple.setStatus("current")


class _RaisecomMplsRsvpTEIfRRInterval_Type(Unsigned32):
    """Custom type raisecomMplsRsvpTEIfRRInterval based on Unsigned32"""
    defaultValue = 500


_RaisecomMplsRsvpTEIfRRInterval_Type.__name__ = "Unsigned32"
_RaisecomMplsRsvpTEIfRRInterval_Object = MibTableColumn
raisecomMplsRsvpTEIfRRInterval = _RaisecomMplsRsvpTEIfRRInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 4),
    _RaisecomMplsRsvpTEIfRRInterval_Type()
)
raisecomMplsRsvpTEIfRRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfRRInterval.setStatus("current")


class _RaisecomMplsRsvpTEIfRRDecay_Type(Integer32):
    """Custom type raisecomMplsRsvpTEIfRRDecay based on Integer32"""
    defaultValue = 100


_RaisecomMplsRsvpTEIfRRDecay_Type.__name__ = "Integer32"
_RaisecomMplsRsvpTEIfRRDecay_Object = MibTableColumn
raisecomMplsRsvpTEIfRRDecay = _RaisecomMplsRsvpTEIfRRDecay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 5),
    _RaisecomMplsRsvpTEIfRRDecay_Type()
)
raisecomMplsRsvpTEIfRRDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfRRDecay.setStatus("current")


class _RaisecomMplsRsvpTEIfRRLimit_Type(Unsigned32):
    """Custom type raisecomMplsRsvpTEIfRRLimit based on Unsigned32"""
    defaultValue = 2


_RaisecomMplsRsvpTEIfRRLimit_Type.__name__ = "Unsigned32"
_RaisecomMplsRsvpTEIfRRLimit_Object = MibTableColumn
raisecomMplsRsvpTEIfRRLimit = _RaisecomMplsRsvpTEIfRRLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 6),
    _RaisecomMplsRsvpTEIfRRLimit_Type()
)
raisecomMplsRsvpTEIfRRLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfRRLimit.setStatus("current")


class _RaisecomMplsRsvpTEIfHelloPeriod_Type(Unsigned32):
    """Custom type raisecomMplsRsvpTEIfHelloPeriod based on Unsigned32"""
    defaultValue = 0


_RaisecomMplsRsvpTEIfHelloPeriod_Type.__name__ = "Unsigned32"
_RaisecomMplsRsvpTEIfHelloPeriod_Object = MibTableColumn
raisecomMplsRsvpTEIfHelloPeriod = _RaisecomMplsRsvpTEIfHelloPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 7),
    _RaisecomMplsRsvpTEIfHelloPeriod_Type()
)
raisecomMplsRsvpTEIfHelloPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfHelloPeriod.setStatus("current")


class _RaisecomMplsRsvpTEIfHelloHoldPeriod_Type(Unsigned32):
    """Custom type raisecomMplsRsvpTEIfHelloHoldPeriod based on Unsigned32"""
    defaultValue = 3


_RaisecomMplsRsvpTEIfHelloHoldPeriod_Type.__name__ = "Unsigned32"
_RaisecomMplsRsvpTEIfHelloHoldPeriod_Object = MibTableColumn
raisecomMplsRsvpTEIfHelloHoldPeriod = _RaisecomMplsRsvpTEIfHelloHoldPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 8),
    _RaisecomMplsRsvpTEIfHelloHoldPeriod_Type()
)
raisecomMplsRsvpTEIfHelloHoldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfHelloHoldPeriod.setStatus("current")


class _RaisecomMplsRsvpTEIfHelloDecay_Type(Unsigned32):
    """Custom type raisecomMplsRsvpTEIfHelloDecay based on Unsigned32"""
    defaultValue = 0


_RaisecomMplsRsvpTEIfHelloDecay_Type.__name__ = "Unsigned32"
_RaisecomMplsRsvpTEIfHelloDecay_Object = MibTableColumn
raisecomMplsRsvpTEIfHelloDecay = _RaisecomMplsRsvpTEIfHelloDecay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 9),
    _RaisecomMplsRsvpTEIfHelloDecay_Type()
)
raisecomMplsRsvpTEIfHelloDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfHelloDecay.setStatus("current")
_RaisecomMplsRsvpTEIfHelloPersist_Type = Unsigned32
_RaisecomMplsRsvpTEIfHelloPersist_Object = MibTableColumn
raisecomMplsRsvpTEIfHelloPersist = _RaisecomMplsRsvpTEIfHelloPersist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 10),
    _RaisecomMplsRsvpTEIfHelloPersist_Type()
)
raisecomMplsRsvpTEIfHelloPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfHelloPersist.setStatus("current")
_RaisecomMplsRsvpTEIfEnabled_Type = TruthValue
_RaisecomMplsRsvpTEIfEnabled_Object = MibTableColumn
raisecomMplsRsvpTEIfEnabled = _RaisecomMplsRsvpTEIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 11),
    _RaisecomMplsRsvpTEIfEnabled_Type()
)
raisecomMplsRsvpTEIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfEnabled.setStatus("current")
_RaisecomMplsRsvpTEIfStatus_Type = RowStatus
_RaisecomMplsRsvpTEIfStatus_Object = MibTableColumn
raisecomMplsRsvpTEIfStatus = _RaisecomMplsRsvpTEIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 25, 4, 10, 1, 12),
    _RaisecomMplsRsvpTEIfStatus_Type()
)
raisecomMplsRsvpTEIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMplsRsvpTEIfStatus.setStatus("current")
mplsXCEntry.registerAugmentions(
    ("RAISECOM-MPLS-MIB",
     "raisecomMplsLspEntry")
)
raisecomMplsLspEntry.setIndexNames(*mplsXCEntry.getIndexNames())
pwEntry.registerAugmentions(
    ("RAISECOM-MPLS-MIB",
     "raisecomMplsCccPwEntry")
)
raisecomMplsCccPwEntry.setIndexNames(*pwEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-MPLS-MIB",
    **{"RefreshInterval": RefreshInterval,
       "raisecomMpls": raisecomMpls,
       "raisecomMplsLsrObjects": raisecomMplsLsrObjects,
       "raisecomMplsLsrId": raisecomMplsLsrId,
       "raisecomMplsEnable": raisecomMplsEnable,
       "raisecomMplsLspStatisticsClear": raisecomMplsLspStatisticsClear,
       "raisecomMplsInterfaceTable": raisecomMplsInterfaceTable,
       "raisecomMplsInterfaceEntry": raisecomMplsInterfaceEntry,
       "raisecomMplsInterfaceIndex": raisecomMplsInterfaceIndex,
       "raisecomMplsInterfaceEnable": raisecomMplsInterfaceEnable,
       "raisecomMplsLspTable": raisecomMplsLspTable,
       "raisecomMplsLspEntry": raisecomMplsLspEntry,
       "raisecomMplsLspName": raisecomMplsLspName,
       "raisecomMplsLspStatisticsObjects": raisecomMplsLspStatisticsObjects,
       "raisecomMplsLspConfigured": raisecomMplsLspConfigured,
       "raisecomMplsLspActicve": raisecomMplsLspActicve,
       "raisecomMplsLspInActicve": raisecomMplsLspInActicve,
       "raisecomMplsLspIngress": raisecomMplsLspIngress,
       "raisecomMplsLspTransit": raisecomMplsLspTransit,
       "raisecomMplsLspEgress": raisecomMplsLspEgress,
       "raisecomMplsLspStatic": raisecomMplsLspStatic,
       "raisecomMplsLspLdp": raisecomMplsLspLdp,
       "raisecomMplsLspRsvpTe": raisecomMplsLspRsvpTe,
       "raisecomMplsTunnelReroutedNotifEnable": raisecomMplsTunnelReroutedNotifEnable,
       "raisecomMplsTunnelReoptimizedNotifEnable": raisecomMplsTunnelReoptimizedNotifEnable,
       "raisecomMplsTtlPublicPropagate": raisecomMplsTtlPublicPropagate,
       "raisecomMplsTtlVpnPropagate": raisecomMplsTtlVpnPropagate,
       "raisecomMplsVpnObjects": raisecomMplsVpnObjects,
       "raisecomMplsL2VpnObjects": raisecomMplsL2VpnObjects,
       "raisecomMplsL2vpnEnable": raisecomMplsL2vpnEnable,
       "raisecomMplsL2vpnMartiniEnable": raisecomMplsL2vpnMartiniEnable,
       "raisecomMplsL2vpnInterfaceTable": raisecomMplsL2vpnInterfaceTable,
       "raisecomMplsL2vpnInterfaceEntry": raisecomMplsL2vpnInterfaceEntry,
       "raisecomMplsL2vpnInterfaceIndex": raisecomMplsL2vpnInterfaceIndex,
       "raisecomMplsL2vpnInterfaceEnable": raisecomMplsL2vpnInterfaceEnable,
       "raisecomMplsCccPwTable": raisecomMplsCccPwTable,
       "raisecomMplsCccPwEntry": raisecomMplsCccPwEntry,
       "raisecomMplsCccNexthopType": raisecomMplsCccNexthopType,
       "raisecomMplsCccNexthop": raisecomMplsCccNexthop,
       "raisecomMplsLdpObjects": raisecomMplsLdpObjects,
       "raisecomMplsLdpEnable": raisecomMplsLdpEnable,
       "raisecomMplsLdpInterfaceTable": raisecomMplsLdpInterfaceTable,
       "raisecomMplsLdpInterfaceEntry": raisecomMplsLdpInterfaceEntry,
       "raisecomMplsLdpInterfaceIndex": raisecomMplsLdpInterfaceIndex,
       "raisecomMplsLdpInterfaceEnable": raisecomMplsLdpInterfaceEnable,
       "raisecomMplsLdpInterfaceLAM": raisecomMplsLdpInterfaceLAM,
       "raisecomMplsLdpInterfaceTransportAddress": raisecomMplsLdpInterfaceTransportAddress,
       "raisecomMplsLdpInterfaceLdpID": raisecomMplsLdpInterfaceLdpID,
       "raisecomMplsLdpInterfaceMTU": raisecomMplsLdpInterfaceMTU,
       "raisecomMplsLdpInterfaceKeepAliveHoldTimer": raisecomMplsLdpInterfaceKeepAliveHoldTimer,
       "raisecomMplsLdpInterfaceHelloHoldTimer": raisecomMplsLdpInterfaceHelloHoldTimer,
       "raisecomMplsLdpSessionStatusTrapEnable": raisecomMplsLdpSessionStatusTrapEnable,
       "raisecomMplsLdpPathVecLimitTrapEnable": raisecomMplsLdpPathVecLimitTrapEnable,
       "raisecomMplsLdpSessionThreshTrapEnable": raisecomMplsLdpSessionThreshTrapEnable,
       "raisecomMplsRsvpTEObjects": raisecomMplsRsvpTEObjects,
       "raisecomMplsRsvpTEEnabled": raisecomMplsRsvpTEEnabled,
       "raisecomMplsRsvpTERefreshInterval": raisecomMplsRsvpTERefreshInterval,
       "raisecomMplsRsvpTERefreshMultiple": raisecomMplsRsvpTERefreshMultiple,
       "raisecomMplsRsvpTERefreshBlockadeMultiple": raisecomMplsRsvpTERefreshBlockadeMultiple,
       "raisecomMplsRsvpTELSPSetupPriority": raisecomMplsRsvpTELSPSetupPriority,
       "raisecomMplsRsvpTELSPHoldingPriority": raisecomMplsRsvpTELSPHoldingPriority,
       "raisecomMplsRsvpTEInitPathRRInterval": raisecomMplsRsvpTEInitPathRRInterval,
       "raisecomMplsRsvpTEInitPathRRDecay": raisecomMplsRsvpTEInitPathRRDecay,
       "raisecomMplsRsvpTEInitPathRRLimit": raisecomMplsRsvpTEInitPathRRLimit,
       "raisecomMplsRsvpTEInterfaceTable": raisecomMplsRsvpTEInterfaceTable,
       "raisecomMplsRsvpTEInterfaceEntry": raisecomMplsRsvpTEInterfaceEntry,
       "raisecomMplsRsvpTEIfRefreshInterval": raisecomMplsRsvpTEIfRefreshInterval,
       "raisecomMplsRsvpTEIfRefreshMultiple": raisecomMplsRsvpTEIfRefreshMultiple,
       "raisecomMplsRsvpTEIfBlockadeMultiple": raisecomMplsRsvpTEIfBlockadeMultiple,
       "raisecomMplsRsvpTEIfRRInterval": raisecomMplsRsvpTEIfRRInterval,
       "raisecomMplsRsvpTEIfRRDecay": raisecomMplsRsvpTEIfRRDecay,
       "raisecomMplsRsvpTEIfRRLimit": raisecomMplsRsvpTEIfRRLimit,
       "raisecomMplsRsvpTEIfHelloPeriod": raisecomMplsRsvpTEIfHelloPeriod,
       "raisecomMplsRsvpTEIfHelloHoldPeriod": raisecomMplsRsvpTEIfHelloHoldPeriod,
       "raisecomMplsRsvpTEIfHelloDecay": raisecomMplsRsvpTEIfHelloDecay,
       "raisecomMplsRsvpTEIfHelloPersist": raisecomMplsRsvpTEIfHelloPersist,
       "raisecomMplsRsvpTEIfEnabled": raisecomMplsRsvpTEIfEnabled,
       "raisecomMplsRsvpTEIfStatus": raisecomMplsRsvpTEIfStatus}
)
