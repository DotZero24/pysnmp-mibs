# SNMP MIB module (SWITCH-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-FILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:59 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

rcFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcAclFilter_ObjectIdentity = ObjectIdentity
rcAclFilter = _RcAclFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1)
)
_RcAclFilterAction_Type = EnableVar
_RcAclFilterAction_Object = MibScalar
rcAclFilterAction = _RcAclFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 1),
    _RcAclFilterAction_Type()
)
rcAclFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAclFilterAction.setStatus("current")
_RcAclFilterNextIndex_Type = Integer32
_RcAclFilterNextIndex_Object = MibScalar
rcAclFilterNextIndex = _RcAclFilterNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 2),
    _RcAclFilterNextIndex_Type()
)
rcAclFilterNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAclFilterNextIndex.setStatus("current")
_RcAclFilterTable_Object = MibTable
rcAclFilterTable = _RcAclFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    rcAclFilterTable.setStatus("current")
_RcAclFilterEntry_Object = MibTableRow
rcAclFilterEntry = _RcAclFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1)
)
rcAclFilterEntry.setIndexNames(
    (0, "SWITCH-FILTER-MIB", "rcAclFilterIndex"),
)
if mibBuilder.loadTexts:
    rcAclFilterEntry.setStatus("current")
_RcAclFilterIndex_Type = Integer32
_RcAclFilterIndex_Object = MibTableColumn
rcAclFilterIndex = _RcAclFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 1),
    _RcAclFilterIndex_Type()
)
rcAclFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcAclFilterIndex.setStatus("current")


class _RcAclFilterAclType_Type(Integer32):
    """Custom type rcAclFilterAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-acl", 1),
          ("mac-acl", 2),
          ("user-acl", 3))
    )


_RcAclFilterAclType_Type.__name__ = "Integer32"
_RcAclFilterAclType_Object = MibTableColumn
rcAclFilterAclType = _RcAclFilterAclType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 2),
    _RcAclFilterAclType_Type()
)
rcAclFilterAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterAclType.setStatus("current")
_RcAclFilterAclNumber_Type = Integer32
_RcAclFilterAclNumber_Object = MibTableColumn
rcAclFilterAclNumber = _RcAclFilterAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 3),
    _RcAclFilterAclNumber_Type()
)
rcAclFilterAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterAclNumber.setStatus("current")
_RcAclFilterIngressPort_Type = Integer32
_RcAclFilterIngressPort_Object = MibTableColumn
rcAclFilterIngressPort = _RcAclFilterIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 4),
    _RcAclFilterIngressPort_Type()
)
rcAclFilterIngressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterIngressPort.setStatus("current")
_RcAclFilterEgressPort_Type = Integer32
_RcAclFilterEgressPort_Object = MibTableColumn
rcAclFilterEgressPort = _RcAclFilterEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 5),
    _RcAclFilterEgressPort_Type()
)
rcAclFilterEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterEgressPort.setStatus("current")


class _RcAclFilterVlan_Type(Integer32):
    """Custom type rcAclFilterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcAclFilterVlan_Type.__name__ = "Integer32"
_RcAclFilterVlan_Object = MibTableColumn
rcAclFilterVlan = _RcAclFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 6),
    _RcAclFilterVlan_Type()
)
rcAclFilterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterVlan.setStatus("current")
_RcAclFilterStatus_Type = RowStatus
_RcAclFilterStatus_Object = MibTableColumn
rcAclFilterStatus = _RcAclFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 7),
    _RcAclFilterStatus_Type()
)
rcAclFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterStatus.setStatus("current")
_RcAclFilterHwStatus_Type = EnableVar
_RcAclFilterHwStatus_Object = MibTableColumn
rcAclFilterHwStatus = _RcAclFilterHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 8),
    _RcAclFilterHwStatus_Type()
)
rcAclFilterHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAclFilterHwStatus.setStatus("current")
_RcAclFilterDoubleTagging_Type = TruthValue
_RcAclFilterDoubleTagging_Object = MibTableColumn
rcAclFilterDoubleTagging = _RcAclFilterDoubleTagging_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 9),
    _RcAclFilterDoubleTagging_Type()
)
rcAclFilterDoubleTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterDoubleTagging.setStatus("current")


class _RcAclFilterVlanType_Type(Integer32):
    """Custom type rcAclFilterVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inner", 1),
          ("outer", 2))
    )


_RcAclFilterVlanType_Type.__name__ = "Integer32"
_RcAclFilterVlanType_Object = MibTableColumn
rcAclFilterVlanType = _RcAclFilterVlanType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 10),
    _RcAclFilterVlanType_Type()
)
rcAclFilterVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterVlanType.setStatus("current")
_RcAclFilterStatEnable_Type = EnableVar
_RcAclFilterStatEnable_Object = MibTableColumn
rcAclFilterStatEnable = _RcAclFilterStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 11),
    _RcAclFilterStatEnable_Type()
)
rcAclFilterStatEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcAclFilterStatEnable.setStatus("current")
_RcAclFilterStatHwStatus_Type = EnableVar
_RcAclFilterStatHwStatus_Object = MibTableColumn
rcAclFilterStatHwStatus = _RcAclFilterStatHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 12),
    _RcAclFilterStatHwStatus_Type()
)
rcAclFilterStatHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAclFilterStatHwStatus.setStatus("current")
_RcAclFilterIngressPortList_Type = PortList
_RcAclFilterIngressPortList_Object = MibTableColumn
rcAclFilterIngressPortList = _RcAclFilterIngressPortList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 3, 1, 14),
    _RcAclFilterIngressPortList_Type()
)
rcAclFilterIngressPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAclFilterIngressPortList.setStatus("current")
_RcAclFilterStatisticsTable_Object = MibTable
rcAclFilterStatisticsTable = _RcAclFilterStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    rcAclFilterStatisticsTable.setStatus("current")
_RcAclFilterStatisticsEntry_Object = MibTableRow
rcAclFilterStatisticsEntry = _RcAclFilterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rcAclFilterStatisticsEntry.setStatus("current")
_RcAclFilterCounterReset_Type = EnableVar
_RcAclFilterCounterReset_Object = MibTableColumn
rcAclFilterCounterReset = _RcAclFilterCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 4, 1, 1),
    _RcAclFilterCounterReset_Type()
)
rcAclFilterCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAclFilterCounterReset.setStatus("current")
_RcAclFilterCounterPkt64_Type = Counter64
_RcAclFilterCounterPkt64_Object = MibTableColumn
rcAclFilterCounterPkt64 = _RcAclFilterCounterPkt64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 4, 1, 2),
    _RcAclFilterCounterPkt64_Type()
)
rcAclFilterCounterPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAclFilterCounterPkt64.setStatus("current")
_RcAclFilterCounterByte64_Type = Counter64
_RcAclFilterCounterByte64_Object = MibTableColumn
rcAclFilterCounterByte64 = _RcAclFilterCounterByte64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 4, 1, 3),
    _RcAclFilterCounterByte64_Type()
)
rcAclFilterCounterByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAclFilterCounterByte64.setStatus("current")
_RcAclFilterCounterStatisticUnit_Type = Integer32
_RcAclFilterCounterStatisticUnit_Object = MibTableColumn
rcAclFilterCounterStatisticUnit = _RcAclFilterCounterStatisticUnit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 14, 1, 4, 1, 4),
    _RcAclFilterCounterStatisticUnit_Type()
)
rcAclFilterCounterStatisticUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAclFilterCounterStatisticUnit.setStatus("current")
rcAclFilterEntry.registerAugmentions(
    ("SWITCH-FILTER-MIB",
     "rcAclFilterStatisticsEntry")
)
rcAclFilterStatisticsEntry.setIndexNames(*rcAclFilterEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-FILTER-MIB",
    **{"rcFilter": rcFilter,
       "rcAclFilter": rcAclFilter,
       "rcAclFilterAction": rcAclFilterAction,
       "rcAclFilterNextIndex": rcAclFilterNextIndex,
       "rcAclFilterTable": rcAclFilterTable,
       "rcAclFilterEntry": rcAclFilterEntry,
       "rcAclFilterIndex": rcAclFilterIndex,
       "rcAclFilterAclType": rcAclFilterAclType,
       "rcAclFilterAclNumber": rcAclFilterAclNumber,
       "rcAclFilterIngressPort": rcAclFilterIngressPort,
       "rcAclFilterEgressPort": rcAclFilterEgressPort,
       "rcAclFilterVlan": rcAclFilterVlan,
       "rcAclFilterStatus": rcAclFilterStatus,
       "rcAclFilterHwStatus": rcAclFilterHwStatus,
       "rcAclFilterDoubleTagging": rcAclFilterDoubleTagging,
       "rcAclFilterVlanType": rcAclFilterVlanType,
       "rcAclFilterStatEnable": rcAclFilterStatEnable,
       "rcAclFilterStatHwStatus": rcAclFilterStatHwStatus,
       "rcAclFilterIngressPortList": rcAclFilterIngressPortList,
       "rcAclFilterStatisticsTable": rcAclFilterStatisticsTable,
       "rcAclFilterStatisticsEntry": rcAclFilterStatisticsEntry,
       "rcAclFilterCounterReset": rcAclFilterCounterReset,
       "rcAclFilterCounterPkt64": rcAclFilterCounterPkt64,
       "rcAclFilterCounterByte64": rcAclFilterCounterByte64,
       "rcAclFilterCounterStatisticUnit": rcAclFilterCounterStatisticUnit}
)
