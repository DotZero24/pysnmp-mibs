# SNMP MIB module (SWITCH-VLANCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-VLANCFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:35 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "Vlanset")


# MODULE-IDENTITY

rcVlanCfg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcVlanCfgMibObjects_ObjectIdentity = ObjectIdentity
rcVlanCfgMibObjects = _RcVlanCfgMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1)
)
_RcVlanCfgConfig_ObjectIdentity = ObjectIdentity
rcVlanCfgConfig = _RcVlanCfgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 1)
)


class _RcVlanCfgSwitchMode_Type(Integer32):
    """Custom type rcVlanCfgSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("dot1q-vlan", 2))
    )


_RcVlanCfgSwitchMode_Type.__name__ = "Integer32"
_RcVlanCfgSwitchMode_Object = MibScalar
rcVlanCfgSwitchMode = _RcVlanCfgSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 1, 1),
    _RcVlanCfgSwitchMode_Type()
)
rcVlanCfgSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanCfgSwitchMode.setStatus("current")
_RcVlanCfgPort_ObjectIdentity = ObjectIdentity
rcVlanCfgPort = _RcVlanCfgPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2)
)
_RcVlanCfgPortTable_Object = MibTable
rcVlanCfgPortTable = _RcVlanCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcVlanCfgPortTable.setStatus("current")
_RcVlanCfgPortEntry_Object = MibTableRow
rcVlanCfgPortEntry = _RcVlanCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1)
)
rcVlanCfgPortEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    rcVlanCfgPortEntry.setStatus("current")


class _RcPortMode_Type(Integer32):
    """Custom type rcPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2))
    )


_RcPortMode_Type.__name__ = "Integer32"
_RcPortMode_Object = MibTableColumn
rcPortMode = _RcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 1),
    _RcPortMode_Type()
)
rcPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortMode.setStatus("current")


class _RcPortAccessVlanId_Type(Integer32):
    """Custom type rcPortAccessVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcPortAccessVlanId_Type.__name__ = "Integer32"
_RcPortAccessVlanId_Object = MibTableColumn
rcPortAccessVlanId = _RcPortAccessVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 2),
    _RcPortAccessVlanId_Type()
)
rcPortAccessVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortAccessVlanId.setStatus("current")
_RcPortAccessPvidOverride_Type = EnableVar
_RcPortAccessPvidOverride_Object = MibTableColumn
rcPortAccessPvidOverride = _RcPortAccessPvidOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 3),
    _RcPortAccessPvidOverride_Type()
)
rcPortAccessPvidOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortAccessPvidOverride.setStatus("current")
_RcPortAccessEgressVlanList_Type = Vlanset
_RcPortAccessEgressVlanList_Object = MibTableColumn
rcPortAccessEgressVlanList = _RcPortAccessEgressVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 4),
    _RcPortAccessEgressVlanList_Type()
)
rcPortAccessEgressVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortAccessEgressVlanList.setStatus("current")


class _RcPortTrunkVlanNative_Type(Integer32):
    """Custom type rcPortTrunkVlanNative based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcPortTrunkVlanNative_Type.__name__ = "Integer32"
_RcPortTrunkVlanNative_Object = MibTableColumn
rcPortTrunkVlanNative = _RcPortTrunkVlanNative_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 5),
    _RcPortTrunkVlanNative_Type()
)
rcPortTrunkVlanNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortTrunkVlanNative.setStatus("current")
_RcPortTrunkAllowVlanList_Type = Vlanset
_RcPortTrunkAllowVlanList_Object = MibTableColumn
rcPortTrunkAllowVlanList = _RcPortTrunkAllowVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 6),
    _RcPortTrunkAllowVlanList_Type()
)
rcPortTrunkAllowVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortTrunkAllowVlanList.setStatus("current")
_RcPortTrunkUntagVlanList_Type = Vlanset
_RcPortTrunkUntagVlanList_Object = MibTableColumn
rcPortTrunkUntagVlanList = _RcPortTrunkUntagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 7),
    _RcPortTrunkUntagVlanList_Type()
)
rcPortTrunkUntagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortTrunkUntagVlanList.setStatus("current")


class _RcPortRejectFrameType_Type(Integer32):
    """Custom type rcPortRejectFrameType based on Integer32"""
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
          ("tagged", 2),
          ("untagged", 3),
          ("taggedAndUntagged", 4))
    )


_RcPortRejectFrameType_Type.__name__ = "Integer32"
_RcPortRejectFrameType_Object = MibTableColumn
rcPortRejectFrameType = _RcPortRejectFrameType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 8),
    _RcPortRejectFrameType_Type()
)
rcPortRejectFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortRejectFrameType.setStatus("current")


class _RcPortVlanMappingMissMode_Type(Integer32):
    """Custom type rcPortVlanMappingMissMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forwarding", 2))
    )


_RcPortVlanMappingMissMode_Type.__name__ = "Integer32"
_RcPortVlanMappingMissMode_Object = MibTableColumn
rcPortVlanMappingMissMode = _RcPortVlanMappingMissMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 2, 1, 1, 9),
    _RcPortVlanMappingMissMode_Type()
)
rcPortVlanMappingMissMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortVlanMappingMissMode.setStatus("current")
_RcVlanCfgPriority_ObjectIdentity = ObjectIdentity
rcVlanCfgPriority = _RcVlanCfgPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3)
)
_RcVlanCfgPriorityTable_Object = MibTable
rcVlanCfgPriorityTable = _RcVlanCfgPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rcVlanCfgPriorityTable.setStatus("current")
_RcVlanCfgPriorityEntry_Object = MibTableRow
rcVlanCfgPriorityEntry = _RcVlanCfgPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3, 2, 1)
)
rcVlanCfgPriorityEntry.setIndexNames(
    (0, "SWITCH-VLANCFG-MIB", "rcVlanPriorityIndex"),
)
if mibBuilder.loadTexts:
    rcVlanCfgPriorityEntry.setStatus("current")


class _RcVlanPriorityIndex_Type(Integer32):
    """Custom type rcVlanPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcVlanPriorityIndex_Type.__name__ = "Integer32"
_RcVlanPriorityIndex_Object = MibTableColumn
rcVlanPriorityIndex = _RcVlanPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3, 2, 1, 1),
    _RcVlanPriorityIndex_Type()
)
rcVlanPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanPriorityIndex.setStatus("current")


class _RcVlanPriority_Type(Integer32):
    """Custom type rcVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_RcVlanPriority_Type.__name__ = "Integer32"
_RcVlanPriority_Object = MibTableColumn
rcVlanPriority = _RcVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3, 2, 1, 2),
    _RcVlanPriority_Type()
)
rcVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanPriority.setStatus("current")
_RcVlanPriorityRowStatus_Type = RowStatus
_RcVlanPriorityRowStatus_Object = MibTableColumn
rcVlanPriorityRowStatus = _RcVlanPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3, 2, 1, 3),
    _RcVlanPriorityRowStatus_Type()
)
rcVlanPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanPriorityRowStatus.setStatus("current")


class _RcVlanFidVlan_Type(Integer32):
    """Custom type rcVlanFidVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcVlanFidVlan_Type.__name__ = "Integer32"
_RcVlanFidVlan_Object = MibTableColumn
rcVlanFidVlan = _RcVlanFidVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 3, 2, 1, 4),
    _RcVlanFidVlan_Type()
)
rcVlanFidVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanFidVlan.setStatus("current")
_RcVlanCfgMgmt_ObjectIdentity = ObjectIdentity
rcVlanCfgMgmt = _RcVlanCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 4)
)
_RcMgmtVlanTable_Object = MibTable
rcMgmtVlanTable = _RcMgmtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rcMgmtVlanTable.setStatus("current")
_RcMgmtVlanEntry_Object = MibTableRow
rcMgmtVlanEntry = _RcMgmtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 4, 1, 1)
)
rcMgmtVlanEntry.setIndexNames(
    (0, "SWITCH-VLANCFG-MIB", "rcMgmtVlanIndex"),
)
if mibBuilder.loadTexts:
    rcMgmtVlanEntry.setStatus("current")


class _RcMgmtVlanIndex_Type(Integer32):
    """Custom type rcMgmtVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcMgmtVlanIndex_Type.__name__ = "Integer32"
_RcMgmtVlanIndex_Object = MibTableColumn
rcMgmtVlanIndex = _RcMgmtVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 4, 1, 1, 1),
    _RcMgmtVlanIndex_Type()
)
rcMgmtVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMgmtVlanIndex.setStatus("current")


class _RcMgmtVlanMode_Type(Integer32):
    """Custom type rcMgmtVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("termination", 2))
    )


_RcMgmtVlanMode_Type.__name__ = "Integer32"
_RcMgmtVlanMode_Object = MibTableColumn
rcMgmtVlanMode = _RcMgmtVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 4, 1, 1, 2),
    _RcMgmtVlanMode_Type()
)
rcMgmtVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMgmtVlanMode.setStatus("current")
_RcMgmtVlanRowStatus_Type = RowStatus
_RcMgmtVlanRowStatus_Object = MibTableColumn
rcMgmtVlanRowStatus = _RcMgmtVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 4, 1, 1, 3),
    _RcMgmtVlanRowStatus_Type()
)
rcMgmtVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMgmtVlanRowStatus.setStatus("current")
_RcVlanCfgAttribute_ObjectIdentity = ObjectIdentity
rcVlanCfgAttribute = _RcVlanCfgAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 5)
)
_RcVlanCfgStaticTable_Object = MibTable
rcVlanCfgStaticTable = _RcVlanCfgStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rcVlanCfgStaticTable.setStatus("current")
_RcVlanCfgStaticEntry_Object = MibTableRow
rcVlanCfgStaticEntry = _RcVlanCfgStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 5, 1, 1)
)
rcVlanCfgStaticEntry.setIndexNames(
    (0, "SWITCH-VLANCFG-MIB", "rcVlanCfgStaticIndex"),
)
if mibBuilder.loadTexts:
    rcVlanCfgStaticEntry.setStatus("current")


class _RcVlanCfgStaticIndex_Type(Integer32):
    """Custom type rcVlanCfgStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcVlanCfgStaticIndex_Type.__name__ = "Integer32"
_RcVlanCfgStaticIndex_Object = MibTableColumn
rcVlanCfgStaticIndex = _RcVlanCfgStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 5, 1, 1, 1),
    _RcVlanCfgStaticIndex_Type()
)
rcVlanCfgStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanCfgStaticIndex.setStatus("current")


class _RcVlanCfgStaticBeCustomerVlan_Type(Integer32):
    """Custom type rcVlanCfgStaticBeCustomerVlan based on Integer32"""
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


_RcVlanCfgStaticBeCustomerVlan_Type.__name__ = "Integer32"
_RcVlanCfgStaticBeCustomerVlan_Object = MibTableColumn
rcVlanCfgStaticBeCustomerVlan = _RcVlanCfgStaticBeCustomerVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 43, 1, 5, 1, 1, 2),
    _RcVlanCfgStaticBeCustomerVlan_Type()
)
rcVlanCfgStaticBeCustomerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanCfgStaticBeCustomerVlan.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-VLANCFG-MIB",
    **{"rcVlanCfg": rcVlanCfg,
       "rcVlanCfgMibObjects": rcVlanCfgMibObjects,
       "rcVlanCfgConfig": rcVlanCfgConfig,
       "rcVlanCfgSwitchMode": rcVlanCfgSwitchMode,
       "rcVlanCfgPort": rcVlanCfgPort,
       "rcVlanCfgPortTable": rcVlanCfgPortTable,
       "rcVlanCfgPortEntry": rcVlanCfgPortEntry,
       "rcPortMode": rcPortMode,
       "rcPortAccessVlanId": rcPortAccessVlanId,
       "rcPortAccessPvidOverride": rcPortAccessPvidOverride,
       "rcPortAccessEgressVlanList": rcPortAccessEgressVlanList,
       "rcPortTrunkVlanNative": rcPortTrunkVlanNative,
       "rcPortTrunkAllowVlanList": rcPortTrunkAllowVlanList,
       "rcPortTrunkUntagVlanList": rcPortTrunkUntagVlanList,
       "rcPortRejectFrameType": rcPortRejectFrameType,
       "rcPortVlanMappingMissMode": rcPortVlanMappingMissMode,
       "rcVlanCfgPriority": rcVlanCfgPriority,
       "rcVlanCfgPriorityTable": rcVlanCfgPriorityTable,
       "rcVlanCfgPriorityEntry": rcVlanCfgPriorityEntry,
       "rcVlanPriorityIndex": rcVlanPriorityIndex,
       "rcVlanPriority": rcVlanPriority,
       "rcVlanPriorityRowStatus": rcVlanPriorityRowStatus,
       "rcVlanFidVlan": rcVlanFidVlan,
       "rcVlanCfgMgmt": rcVlanCfgMgmt,
       "rcMgmtVlanTable": rcMgmtVlanTable,
       "rcMgmtVlanEntry": rcMgmtVlanEntry,
       "rcMgmtVlanIndex": rcMgmtVlanIndex,
       "rcMgmtVlanMode": rcMgmtVlanMode,
       "rcMgmtVlanRowStatus": rcMgmtVlanRowStatus,
       "rcVlanCfgAttribute": rcVlanCfgAttribute,
       "rcVlanCfgStaticTable": rcVlanCfgStaticTable,
       "rcVlanCfgStaticEntry": rcVlanCfgStaticEntry,
       "rcVlanCfgStaticIndex": rcVlanCfgStaticIndex,
       "rcVlanCfgStaticBeCustomerVlan": rcVlanCfgStaticBeCustomerVlan}
)
