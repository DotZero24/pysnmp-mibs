# SNMP MIB module (ELTEX-MES-SECURITY-SUITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-SECURITY-SUITE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:50 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(RlSecuritySuiteSynProtectionPortMode,) = mibBuilder.importSymbols(
    "RADLAN-SECURITY-SUITE",
    "RlSecuritySuiteSynProtectionPortMode")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesSecuritySuiteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19)
)
if mibBuilder.loadTexts:
    eltMesSecuritySuiteMIB.setRevisions(
        ("2020-05-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesSecuritySuiteMIBObjects_ObjectIdentity = ObjectIdentity
eltMesSecuritySuiteMIBObjects = _EltMesSecuritySuiteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1)
)
_EltMesSecuritySuiteGlobals_ObjectIdentity = ObjectIdentity
eltMesSecuritySuiteGlobals = _EltMesSecuritySuiteGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 1)
)
_EltMesSecuritySuiteSynProtection_ObjectIdentity = ObjectIdentity
eltMesSecuritySuiteSynProtection = _EltMesSecuritySuiteSynProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2)
)
_EltMesSecuritySuiteSynProtectionGlobals_ObjectIdentity = ObjectIdentity
eltMesSecuritySuiteSynProtectionGlobals = _EltMesSecuritySuiteSynProtectionGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 1)
)
_EltMesSecuritySuiteSynProtectionStatistics_ObjectIdentity = ObjectIdentity
eltMesSecuritySuiteSynProtectionStatistics = _EltMesSecuritySuiteSynProtectionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2)
)
_EltSecuritySuiteSynProtectionStatsEnable_Type = TruthValue
_EltSecuritySuiteSynProtectionStatsEnable_Object = MibScalar
eltSecuritySuiteSynProtectionStatsEnable = _EltSecuritySuiteSynProtectionStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 1),
    _EltSecuritySuiteSynProtectionStatsEnable_Type()
)
eltSecuritySuiteSynProtectionStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionStatsEnable.setStatus("current")


class _EltSecuritySuiteSynProtectionStatsClearAction_Type(Integer32):
    """Custom type eltSecuritySuiteSynProtectionStatsClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearNow", 2))
    )


_EltSecuritySuiteSynProtectionStatsClearAction_Type.__name__ = "Integer32"
_EltSecuritySuiteSynProtectionStatsClearAction_Object = MibScalar
eltSecuritySuiteSynProtectionStatsClearAction = _EltSecuritySuiteSynProtectionStatsClearAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 2),
    _EltSecuritySuiteSynProtectionStatsClearAction_Type()
)
eltSecuritySuiteSynProtectionStatsClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionStatsClearAction.setStatus("current")
_EltSecuritySuiteSynProtectionFlowTable_Object = MibTable
eltSecuritySuiteSynProtectionFlowTable = _EltSecuritySuiteSynProtectionFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowTable.setStatus("current")
_EltSecuritySuiteSynProtectionFlowEntry_Object = MibTableRow
eltSecuritySuiteSynProtectionFlowEntry = _EltSecuritySuiteSynProtectionFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1)
)
eltSecuritySuiteSynProtectionFlowEntry.setIndexNames(
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowIfIndex"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowVlanId"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowSrcAddrType"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowSrcAddr"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowSrcPort"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowDstAddrType"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowDstAddr"),
    (0, "ELTEX-MES-SECURITY-SUITE-MIB", "eltSecuritySuiteSynProtectionFlowDstPort"),
)
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowEntry.setStatus("current")
_EltSecuritySuiteSynProtectionFlowIfIndex_Type = InterfaceIndex
_EltSecuritySuiteSynProtectionFlowIfIndex_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowIfIndex = _EltSecuritySuiteSynProtectionFlowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 1),
    _EltSecuritySuiteSynProtectionFlowIfIndex_Type()
)
eltSecuritySuiteSynProtectionFlowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowIfIndex.setStatus("current")
_EltSecuritySuiteSynProtectionFlowVlanId_Type = VlanId
_EltSecuritySuiteSynProtectionFlowVlanId_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowVlanId = _EltSecuritySuiteSynProtectionFlowVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 2),
    _EltSecuritySuiteSynProtectionFlowVlanId_Type()
)
eltSecuritySuiteSynProtectionFlowVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowVlanId.setStatus("current")
_EltSecuritySuiteSynProtectionFlowSrcAddrType_Type = InetAddressType
_EltSecuritySuiteSynProtectionFlowSrcAddrType_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowSrcAddrType = _EltSecuritySuiteSynProtectionFlowSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 3),
    _EltSecuritySuiteSynProtectionFlowSrcAddrType_Type()
)
eltSecuritySuiteSynProtectionFlowSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowSrcAddrType.setStatus("current")
_EltSecuritySuiteSynProtectionFlowSrcAddr_Type = InetAddress
_EltSecuritySuiteSynProtectionFlowSrcAddr_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowSrcAddr = _EltSecuritySuiteSynProtectionFlowSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 4),
    _EltSecuritySuiteSynProtectionFlowSrcAddr_Type()
)
eltSecuritySuiteSynProtectionFlowSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowSrcAddr.setStatus("current")


class _EltSecuritySuiteSynProtectionFlowSrcPort_Type(Unsigned32):
    """Custom type eltSecuritySuiteSynProtectionFlowSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltSecuritySuiteSynProtectionFlowSrcPort_Type.__name__ = "Unsigned32"
_EltSecuritySuiteSynProtectionFlowSrcPort_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowSrcPort = _EltSecuritySuiteSynProtectionFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 5),
    _EltSecuritySuiteSynProtectionFlowSrcPort_Type()
)
eltSecuritySuiteSynProtectionFlowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowSrcPort.setStatus("current")
_EltSecuritySuiteSynProtectionFlowDstAddrType_Type = InetAddressType
_EltSecuritySuiteSynProtectionFlowDstAddrType_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowDstAddrType = _EltSecuritySuiteSynProtectionFlowDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 6),
    _EltSecuritySuiteSynProtectionFlowDstAddrType_Type()
)
eltSecuritySuiteSynProtectionFlowDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowDstAddrType.setStatus("current")
_EltSecuritySuiteSynProtectionFlowDstAddr_Type = InetAddress
_EltSecuritySuiteSynProtectionFlowDstAddr_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowDstAddr = _EltSecuritySuiteSynProtectionFlowDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 7),
    _EltSecuritySuiteSynProtectionFlowDstAddr_Type()
)
eltSecuritySuiteSynProtectionFlowDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowDstAddr.setStatus("current")


class _EltSecuritySuiteSynProtectionFlowDstPort_Type(Unsigned32):
    """Custom type eltSecuritySuiteSynProtectionFlowDstPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltSecuritySuiteSynProtectionFlowDstPort_Type.__name__ = "Unsigned32"
_EltSecuritySuiteSynProtectionFlowDstPort_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowDstPort = _EltSecuritySuiteSynProtectionFlowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 8),
    _EltSecuritySuiteSynProtectionFlowDstPort_Type()
)
eltSecuritySuiteSynProtectionFlowDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowDstPort.setStatus("current")
_EltSecuritySuiteSynProtectionFlowCurrentRate_Type = Unsigned32
_EltSecuritySuiteSynProtectionFlowCurrentRate_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowCurrentRate = _EltSecuritySuiteSynProtectionFlowCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 9),
    _EltSecuritySuiteSynProtectionFlowCurrentRate_Type()
)
eltSecuritySuiteSynProtectionFlowCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowCurrentRate.setStatus("current")
_EltSecuritySuiteSynProtectionFlowMaxRate_Type = Unsigned32
_EltSecuritySuiteSynProtectionFlowMaxRate_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowMaxRate = _EltSecuritySuiteSynProtectionFlowMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 10),
    _EltSecuritySuiteSynProtectionFlowMaxRate_Type()
)
eltSecuritySuiteSynProtectionFlowMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowMaxRate.setStatus("current")
_EltSecuritySuiteSynProtectionFlowTotalCount_Type = Counter32
_EltSecuritySuiteSynProtectionFlowTotalCount_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowTotalCount = _EltSecuritySuiteSynProtectionFlowTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 11),
    _EltSecuritySuiteSynProtectionFlowTotalCount_Type()
)
eltSecuritySuiteSynProtectionFlowTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowTotalCount.setStatus("current")
_EltSecuritySuiteSynProtectionFlowLastTimeAttack_Type = DisplayString
_EltSecuritySuiteSynProtectionFlowLastTimeAttack_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowLastTimeAttack = _EltSecuritySuiteSynProtectionFlowLastTimeAttack_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 12),
    _EltSecuritySuiteSynProtectionFlowLastTimeAttack_Type()
)
eltSecuritySuiteSynProtectionFlowLastTimeAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowLastTimeAttack.setStatus("current")
_EltSecuritySuiteSynProtectionFlowStatus_Type = RlSecuritySuiteSynProtectionPortMode
_EltSecuritySuiteSynProtectionFlowStatus_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowStatus = _EltSecuritySuiteSynProtectionFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 13),
    _EltSecuritySuiteSynProtectionFlowStatus_Type()
)
eltSecuritySuiteSynProtectionFlowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowStatus.setStatus("current")
_EltSecuritySuiteSynProtectionFlowId_Type = Counter32
_EltSecuritySuiteSynProtectionFlowId_Object = MibTableColumn
eltSecuritySuiteSynProtectionFlowId = _EltSecuritySuiteSynProtectionFlowId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 19, 1, 2, 2, 3, 1, 14),
    _EltSecuritySuiteSynProtectionFlowId_Type()
)
eltSecuritySuiteSynProtectionFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSecuritySuiteSynProtectionFlowId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SECURITY-SUITE-MIB",
    **{"eltMesSecuritySuiteMIB": eltMesSecuritySuiteMIB,
       "eltMesSecuritySuiteMIBObjects": eltMesSecuritySuiteMIBObjects,
       "eltMesSecuritySuiteGlobals": eltMesSecuritySuiteGlobals,
       "eltMesSecuritySuiteSynProtection": eltMesSecuritySuiteSynProtection,
       "eltMesSecuritySuiteSynProtectionGlobals": eltMesSecuritySuiteSynProtectionGlobals,
       "eltMesSecuritySuiteSynProtectionStatistics": eltMesSecuritySuiteSynProtectionStatistics,
       "eltSecuritySuiteSynProtectionStatsEnable": eltSecuritySuiteSynProtectionStatsEnable,
       "eltSecuritySuiteSynProtectionStatsClearAction": eltSecuritySuiteSynProtectionStatsClearAction,
       "eltSecuritySuiteSynProtectionFlowTable": eltSecuritySuiteSynProtectionFlowTable,
       "eltSecuritySuiteSynProtectionFlowEntry": eltSecuritySuiteSynProtectionFlowEntry,
       "eltSecuritySuiteSynProtectionFlowIfIndex": eltSecuritySuiteSynProtectionFlowIfIndex,
       "eltSecuritySuiteSynProtectionFlowVlanId": eltSecuritySuiteSynProtectionFlowVlanId,
       "eltSecuritySuiteSynProtectionFlowSrcAddrType": eltSecuritySuiteSynProtectionFlowSrcAddrType,
       "eltSecuritySuiteSynProtectionFlowSrcAddr": eltSecuritySuiteSynProtectionFlowSrcAddr,
       "eltSecuritySuiteSynProtectionFlowSrcPort": eltSecuritySuiteSynProtectionFlowSrcPort,
       "eltSecuritySuiteSynProtectionFlowDstAddrType": eltSecuritySuiteSynProtectionFlowDstAddrType,
       "eltSecuritySuiteSynProtectionFlowDstAddr": eltSecuritySuiteSynProtectionFlowDstAddr,
       "eltSecuritySuiteSynProtectionFlowDstPort": eltSecuritySuiteSynProtectionFlowDstPort,
       "eltSecuritySuiteSynProtectionFlowCurrentRate": eltSecuritySuiteSynProtectionFlowCurrentRate,
       "eltSecuritySuiteSynProtectionFlowMaxRate": eltSecuritySuiteSynProtectionFlowMaxRate,
       "eltSecuritySuiteSynProtectionFlowTotalCount": eltSecuritySuiteSynProtectionFlowTotalCount,
       "eltSecuritySuiteSynProtectionFlowLastTimeAttack": eltSecuritySuiteSynProtectionFlowLastTimeAttack,
       "eltSecuritySuiteSynProtectionFlowStatus": eltSecuritySuiteSynProtectionFlowStatus,
       "eltSecuritySuiteSynProtectionFlowId": eltSecuritySuiteSynProtectionFlowId}
)
