# SNMP MIB module (QTECH-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-QINQ-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:23 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechQinQMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53)
)
if mibBuilder.loadTexts:
    qtechQinQMIB.setRevisions(
        ("2009-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_QtechQINQMIBObjects_ObjectIdentity = ObjectIdentity
qtechQINQMIBObjects = _QtechQINQMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1)
)
_QtechQinQPortConfigTable_Object = MibTable
qtechQinQPortConfigTable = _QtechQinQPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1)
)
if mibBuilder.loadTexts:
    qtechQinQPortConfigTable.setStatus("current")
_QtechQinQPortConfigEntry_Object = MibTableRow
qtechQinQPortConfigEntry = _QtechQinQPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1, 1)
)
qtechQinQPortConfigEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechQinQPortConfigIndex"),
)
if mibBuilder.loadTexts:
    qtechQinQPortConfigEntry.setStatus("current")
_QtechQinQPortConfigIndex_Type = IfIndex
_QtechQinQPortConfigIndex_Object = MibTableColumn
qtechQinQPortConfigIndex = _QtechQinQPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1, 1, 1),
    _QtechQinQPortConfigIndex_Type()
)
qtechQinQPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechQinQPortConfigIndex.setStatus("current")


class _QtechQinQPortConfigMode_Type(Integer32):
    """Custom type qtechQinQPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dot1q-tunnel", 2))
    )


_QtechQinQPortConfigMode_Type.__name__ = "Integer32"
_QtechQinQPortConfigMode_Object = MibTableColumn
qtechQinQPortConfigMode = _QtechQinQPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1, 1, 2),
    _QtechQinQPortConfigMode_Type()
)
qtechQinQPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQPortConfigMode.setStatus("current")
_QtechQinQPortNativeVlan_Type = VlanId
_QtechQinQPortNativeVlan_Object = MibTableColumn
qtechQinQPortNativeVlan = _QtechQinQPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1, 1, 3),
    _QtechQinQPortNativeVlan_Type()
)
qtechQinQPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQPortNativeVlan.setStatus("current")
_QtechQinQPortAllowedUntagVlanList_Type = VlanList
_QtechQinQPortAllowedUntagVlanList_Object = MibTableColumn
qtechQinQPortAllowedUntagVlanList = _QtechQinQPortAllowedUntagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1, 1, 4),
    _QtechQinQPortAllowedUntagVlanList_Type()
)
qtechQinQPortAllowedUntagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQPortAllowedUntagVlanList.setStatus("current")
_QtechQinQPortAllowedTagVlanList_Type = VlanList
_QtechQinQPortAllowedTagVlanList_Object = MibTableColumn
qtechQinQPortAllowedTagVlanList = _QtechQinQPortAllowedTagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 1, 1, 5),
    _QtechQinQPortAllowedTagVlanList_Type()
)
qtechQinQPortAllowedTagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQPortAllowedTagVlanList.setStatus("current")


class _QtechQinQServiceTPIDValue_Type(Integer32):
    """Custom type qtechQinQServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechQinQServiceTPIDValue_Type.__name__ = "Integer32"
_QtechQinQServiceTPIDValue_Object = MibScalar
qtechQinQServiceTPIDValue = _QtechQinQServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 2),
    _QtechQinQServiceTPIDValue_Type()
)
qtechQinQServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQServiceTPIDValue.setStatus("current")
_QtechQinQIfServiceTPIDConfigTable_Object = MibTable
qtechQinQIfServiceTPIDConfigTable = _QtechQinQIfServiceTPIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 3)
)
if mibBuilder.loadTexts:
    qtechQinQIfServiceTPIDConfigTable.setStatus("current")
_QtechQinQIfServiceTPIDConfigEntry_Object = MibTableRow
qtechQinQIfServiceTPIDConfigEntry = _QtechQinQIfServiceTPIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 3, 1)
)
qtechQinQIfServiceTPIDConfigEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechQinQIfServiceTPIDConfigIfIndex"),
)
if mibBuilder.loadTexts:
    qtechQinQIfServiceTPIDConfigEntry.setStatus("current")
_QtechQinQIfServiceTPIDConfigIfIndex_Type = IfIndex
_QtechQinQIfServiceTPIDConfigIfIndex_Object = MibTableColumn
qtechQinQIfServiceTPIDConfigIfIndex = _QtechQinQIfServiceTPIDConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 3, 1, 1),
    _QtechQinQIfServiceTPIDConfigIfIndex_Type()
)
qtechQinQIfServiceTPIDConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechQinQIfServiceTPIDConfigIfIndex.setStatus("current")


class _QtechQinQIfServiceTPIDValue_Type(Integer32):
    """Custom type qtechQinQIfServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechQinQIfServiceTPIDValue_Type.__name__ = "Integer32"
_QtechQinQIfServiceTPIDValue_Object = MibTableColumn
qtechQinQIfServiceTPIDValue = _QtechQinQIfServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 3, 1, 2),
    _QtechQinQIfServiceTPIDValue_Type()
)
qtechQinQIfServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQIfServiceTPIDValue.setStatus("current")
_QtechQinQPriorityCopyTable_Object = MibTable
qtechQinQPriorityCopyTable = _QtechQinQPriorityCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 4)
)
if mibBuilder.loadTexts:
    qtechQinQPriorityCopyTable.setStatus("current")
_QtechQinQPriorityCopyEntry_Object = MibTableRow
qtechQinQPriorityCopyEntry = _QtechQinQPriorityCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 4, 1)
)
qtechQinQPriorityCopyEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechQinQPriorityCopyIfIndex"),
)
if mibBuilder.loadTexts:
    qtechQinQPriorityCopyEntry.setStatus("current")
_QtechQinQPriorityCopyIfIndex_Type = IfIndex
_QtechQinQPriorityCopyIfIndex_Object = MibTableColumn
qtechQinQPriorityCopyIfIndex = _QtechQinQPriorityCopyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 4, 1, 1),
    _QtechQinQPriorityCopyIfIndex_Type()
)
qtechQinQPriorityCopyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechQinQPriorityCopyIfIndex.setStatus("current")
_QtechQinQPriorityCopyPortStatus_Type = EnabledStatus
_QtechQinQPriorityCopyPortStatus_Object = MibTableColumn
qtechQinQPriorityCopyPortStatus = _QtechQinQPriorityCopyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 4, 1, 2),
    _QtechQinQPriorityCopyPortStatus_Type()
)
qtechQinQPriorityCopyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQinQPriorityCopyPortStatus.setStatus("current")
_QtechQinQPriorityRemarkTable_Object = MibTable
qtechQinQPriorityRemarkTable = _QtechQinQPriorityRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 5)
)
if mibBuilder.loadTexts:
    qtechQinQPriorityRemarkTable.setStatus("current")
_QtechQinQPriorityRemarkEntry_Object = MibTableRow
qtechQinQPriorityRemarkEntry = _QtechQinQPriorityRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 5, 1)
)
qtechQinQPriorityRemarkEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechQinQPriorityRemarkIfIndex"),
    (0, "QTECH-QINQ-MIB", "qtechQinQPriorityValue"),
)
if mibBuilder.loadTexts:
    qtechQinQPriorityRemarkEntry.setStatus("current")
_QtechQinQPriorityRemarkIfIndex_Type = IfIndex
_QtechQinQPriorityRemarkIfIndex_Object = MibTableColumn
qtechQinQPriorityRemarkIfIndex = _QtechQinQPriorityRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 5, 1, 1),
    _QtechQinQPriorityRemarkIfIndex_Type()
)
qtechQinQPriorityRemarkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechQinQPriorityRemarkIfIndex.setStatus("current")


class _QtechQinQPriorityValue_Type(Integer32):
    """Custom type qtechQinQPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechQinQPriorityValue_Type.__name__ = "Integer32"
_QtechQinQPriorityValue_Object = MibTableColumn
qtechQinQPriorityValue = _QtechQinQPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 5, 1, 2),
    _QtechQinQPriorityValue_Type()
)
qtechQinQPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQinQPriorityValue.setStatus("current")


class _QtechQinQPriorityRemarkValue_Type(Integer32):
    """Custom type qtechQinQPriorityRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechQinQPriorityRemarkValue_Type.__name__ = "Integer32"
_QtechQinQPriorityRemarkValue_Object = MibTableColumn
qtechQinQPriorityRemarkValue = _QtechQinQPriorityRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 5, 1, 3),
    _QtechQinQPriorityRemarkValue_Type()
)
qtechQinQPriorityRemarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQinQPriorityRemarkValue.setStatus("current")
_QtechselectiveQinQBasedOnVlanTable_Object = MibTable
qtechselectiveQinQBasedOnVlanTable = _QtechselectiveQinQBasedOnVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6)
)
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanTable.setStatus("current")
_QtechselectiveQinQBasedOnVlanEntry_Object = MibTableRow
qtechselectiveQinQBasedOnVlanEntry = _QtechselectiveQinQBasedOnVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6, 1)
)
qtechselectiveQinQBasedOnVlanEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanIfIndex"),
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanType"),
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanOuterVlanID"),
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanOldOuterVlanID"),
)
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanEntry.setStatus("current")
_QtechselectiveQinQBasedOnVlanIfIndex_Type = IfIndex
_QtechselectiveQinQBasedOnVlanIfIndex_Object = MibTableColumn
qtechselectiveQinQBasedOnVlanIfIndex = _QtechselectiveQinQBasedOnVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6, 1, 1),
    _QtechselectiveQinQBasedOnVlanIfIndex_Type()
)
qtechselectiveQinQBasedOnVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanIfIndex.setStatus("current")


class _QtechselectiveQinQBasedOnVlanType_Type(Integer32):
    """Custom type qtechselectiveQinQBasedOnVlanType based on Integer32"""
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
        *(("addOuterTag", 1),
          ("modifyOuterTagBaseInnerTag", 2),
          ("modifyOuterTagBaseOuterTag", 3),
          ("modifyOuterTagBaseInnerAndOuterTag", 4))
    )


_QtechselectiveQinQBasedOnVlanType_Type.__name__ = "Integer32"
_QtechselectiveQinQBasedOnVlanType_Object = MibTableColumn
qtechselectiveQinQBasedOnVlanType = _QtechselectiveQinQBasedOnVlanType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6, 1, 2),
    _QtechselectiveQinQBasedOnVlanType_Type()
)
qtechselectiveQinQBasedOnVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanType.setStatus("current")


class _QtechselectiveQinQBasedOnVlanOuterVlanID_Type(Integer32):
    """Custom type qtechselectiveQinQBasedOnVlanOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechselectiveQinQBasedOnVlanOuterVlanID_Type.__name__ = "Integer32"
_QtechselectiveQinQBasedOnVlanOuterVlanID_Object = MibTableColumn
qtechselectiveQinQBasedOnVlanOuterVlanID = _QtechselectiveQinQBasedOnVlanOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6, 1, 3),
    _QtechselectiveQinQBasedOnVlanOuterVlanID_Type()
)
qtechselectiveQinQBasedOnVlanOuterVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanOuterVlanID.setStatus("current")


class _QtechselectiveQinQBasedOnVlanOldOuterVlanID_Type(Integer32):
    """Custom type qtechselectiveQinQBasedOnVlanOldOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechselectiveQinQBasedOnVlanOldOuterVlanID_Type.__name__ = "Integer32"
_QtechselectiveQinQBasedOnVlanOldOuterVlanID_Object = MibTableColumn
qtechselectiveQinQBasedOnVlanOldOuterVlanID = _QtechselectiveQinQBasedOnVlanOldOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6, 1, 4),
    _QtechselectiveQinQBasedOnVlanOldOuterVlanID_Type()
)
qtechselectiveQinQBasedOnVlanOldOuterVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanOldOuterVlanID.setStatus("current")
_QtechselectiveQinQBasedOnVlanVlanList_Type = VlanList
_QtechselectiveQinQBasedOnVlanVlanList_Object = MibTableColumn
qtechselectiveQinQBasedOnVlanVlanList = _QtechselectiveQinQBasedOnVlanVlanList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 6, 1, 5),
    _QtechselectiveQinQBasedOnVlanVlanList_Type()
)
qtechselectiveQinQBasedOnVlanVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnVlanVlanList.setStatus("current")
_QtechselectiveQinQBasedOnAclTable_Object = MibTable
qtechselectiveQinQBasedOnAclTable = _QtechselectiveQinQBasedOnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 7)
)
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnAclTable.setStatus("current")
_QtechselectiveQinQBasedOnAclEntry_Object = MibTableRow
qtechselectiveQinQBasedOnAclEntry = _QtechselectiveQinQBasedOnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 7, 1)
)
qtechselectiveQinQBasedOnAclEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnAclIfIndex"),
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnAclType"),
    (0, "QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnAclAclID"),
)
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnAclEntry.setStatus("current")
_QtechselectiveQinQBasedOnAclIfIndex_Type = IfIndex
_QtechselectiveQinQBasedOnAclIfIndex_Object = MibTableColumn
qtechselectiveQinQBasedOnAclIfIndex = _QtechselectiveQinQBasedOnAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 7, 1, 1),
    _QtechselectiveQinQBasedOnAclIfIndex_Type()
)
qtechselectiveQinQBasedOnAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnAclIfIndex.setStatus("current")


class _QtechselectiveQinQBasedOnAclType_Type(Integer32):
    """Custom type qtechselectiveQinQBasedOnAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addOuterTag", 1),
          ("modifyOuterTag", 2),
          ("modifyInnerTag", 3))
    )


_QtechselectiveQinQBasedOnAclType_Type.__name__ = "Integer32"
_QtechselectiveQinQBasedOnAclType_Object = MibTableColumn
qtechselectiveQinQBasedOnAclType = _QtechselectiveQinQBasedOnAclType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 7, 1, 2),
    _QtechselectiveQinQBasedOnAclType_Type()
)
qtechselectiveQinQBasedOnAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnAclType.setStatus("current")
_QtechselectiveQinQBasedOnAclAclID_Type = Integer32
_QtechselectiveQinQBasedOnAclAclID_Object = MibTableColumn
qtechselectiveQinQBasedOnAclAclID = _QtechselectiveQinQBasedOnAclAclID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 7, 1, 3),
    _QtechselectiveQinQBasedOnAclAclID_Type()
)
qtechselectiveQinQBasedOnAclAclID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnAclAclID.setStatus("current")


class _QtechselectiveQinQBasedOnAclVlanID_Type(Integer32):
    """Custom type qtechselectiveQinQBasedOnAclVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechselectiveQinQBasedOnAclVlanID_Type.__name__ = "Integer32"
_QtechselectiveQinQBasedOnAclVlanID_Object = MibTableColumn
qtechselectiveQinQBasedOnAclVlanID = _QtechselectiveQinQBasedOnAclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 7, 1, 4),
    _QtechselectiveQinQBasedOnAclVlanID_Type()
)
qtechselectiveQinQBasedOnAclVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechselectiveQinQBasedOnAclVlanID.setStatus("current")
_QtechQinQVlanMappingTable_Object = MibTable
qtechQinQVlanMappingTable = _QtechQinQVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8)
)
if mibBuilder.loadTexts:
    qtechQinQVlanMappingTable.setStatus("current")
_QtechQinQVlanMappingEntry_Object = MibTableRow
qtechQinQVlanMappingEntry = _QtechQinQVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8, 1)
)
qtechQinQVlanMappingEntry.setIndexNames(
    (0, "QTECH-QINQ-MIB", "qtechQinQVlanMappingIfIndex"),
    (0, "QTECH-QINQ-MIB", "qtechQinQVlanMappingType"),
    (0, "QTECH-QINQ-MIB", "qtechQinQVlanMappingNewVlanID"),
)
if mibBuilder.loadTexts:
    qtechQinQVlanMappingEntry.setStatus("current")
_QtechQinQVlanMappingIfIndex_Type = IfIndex
_QtechQinQVlanMappingIfIndex_Object = MibTableColumn
qtechQinQVlanMappingIfIndex = _QtechQinQVlanMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8, 1, 1),
    _QtechQinQVlanMappingIfIndex_Type()
)
qtechQinQVlanMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechQinQVlanMappingIfIndex.setStatus("current")


class _QtechQinQVlanMappingType_Type(Integer32):
    """Custom type qtechQinQVlanMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanMappingIn", 1),
          ("vlanMappingOut", 2))
    )


_QtechQinQVlanMappingType_Type.__name__ = "Integer32"
_QtechQinQVlanMappingType_Object = MibTableColumn
qtechQinQVlanMappingType = _QtechQinQVlanMappingType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8, 1, 2),
    _QtechQinQVlanMappingType_Type()
)
qtechQinQVlanMappingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQinQVlanMappingType.setStatus("current")


class _QtechQinQVlanMappingNewVlanID_Type(Integer32):
    """Custom type qtechQinQVlanMappingNewVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechQinQVlanMappingNewVlanID_Type.__name__ = "Integer32"
_QtechQinQVlanMappingNewVlanID_Object = MibTableColumn
qtechQinQVlanMappingNewVlanID = _QtechQinQVlanMappingNewVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8, 1, 3),
    _QtechQinQVlanMappingNewVlanID_Type()
)
qtechQinQVlanMappingNewVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQinQVlanMappingNewVlanID.setStatus("current")
_QtechQinQVlanMappingOldVlanList_Type = VlanList
_QtechQinQVlanMappingOldVlanList_Object = MibTableColumn
qtechQinQVlanMappingOldVlanList = _QtechQinQVlanMappingOldVlanList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8, 1, 4),
    _QtechQinQVlanMappingOldVlanList_Type()
)
qtechQinQVlanMappingOldVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQinQVlanMappingOldVlanList.setStatus("current")


class _QtechQinQVlanMappingOldVlanID_Type(Integer32):
    """Custom type qtechQinQVlanMappingOldVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechQinQVlanMappingOldVlanID_Type.__name__ = "Integer32"
_QtechQinQVlanMappingOldVlanID_Object = MibTableColumn
qtechQinQVlanMappingOldVlanID = _QtechQinQVlanMappingOldVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 1, 8, 1, 5),
    _QtechQinQVlanMappingOldVlanID_Type()
)
qtechQinQVlanMappingOldVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQinQVlanMappingOldVlanID.setStatus("current")
_QtechQinQMIBConformance_ObjectIdentity = ObjectIdentity
qtechQinQMIBConformance = _QtechQinQMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 2)
)
_QtechQinQMIBCompliances_ObjectIdentity = ObjectIdentity
qtechQinQMIBCompliances = _QtechQinQMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 2, 1)
)
_QtechQinQMIBGroups_ObjectIdentity = ObjectIdentity
qtechQinQMIBGroups = _QtechQinQMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 2, 2)
)

# Managed Objects groups

qtechQinQMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 2, 2, 1)
)
qtechQinQMIBGroup.setObjects(
      *(("QTECH-QINQ-MIB", "qtechQinQPortConfigMode"),
        ("QTECH-QINQ-MIB", "qtechQinQPortNativeVlan"),
        ("QTECH-QINQ-MIB", "qtechQinQPortAllowedUntagVlanList"),
        ("QTECH-QINQ-MIB", "qtechQinQPortAllowedTagVlanList"),
        ("QTECH-QINQ-MIB", "qtechQinQServiceTPIDValue"),
        ("QTECH-QINQ-MIB", "qtechQinQIfServiceTPIDValue"),
        ("QTECH-QINQ-MIB", "qtechQinQPriorityCopyPortStatus"),
        ("QTECH-QINQ-MIB", "qtechQinQPriorityValue"),
        ("QTECH-QINQ-MIB", "qtechQinQPriorityRemarkValue"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanType"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanOuterVlanID"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanOldOuterVlanID"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnVlanVlanList"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnAclType"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnAclAclID"),
        ("QTECH-QINQ-MIB", "qtechselectiveQinQBasedOnAclVlanID"),
        ("QTECH-QINQ-MIB", "qtechQinQVlanMappingNewVlanID"))
)
if mibBuilder.loadTexts:
    qtechQinQMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechQinQMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 53, 2, 1, 1)
)
qtechQinQMIBCompliance.setObjects(
    ("QTECH-QINQ-MIB", "qtechQinQMIBGroup")
)
if mibBuilder.loadTexts:
    qtechQinQMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-QINQ-MIB",
    **{"VlanList": VlanList,
       "qtechQinQMIB": qtechQinQMIB,
       "qtechQINQMIBObjects": qtechQINQMIBObjects,
       "qtechQinQPortConfigTable": qtechQinQPortConfigTable,
       "qtechQinQPortConfigEntry": qtechQinQPortConfigEntry,
       "qtechQinQPortConfigIndex": qtechQinQPortConfigIndex,
       "qtechQinQPortConfigMode": qtechQinQPortConfigMode,
       "qtechQinQPortNativeVlan": qtechQinQPortNativeVlan,
       "qtechQinQPortAllowedUntagVlanList": qtechQinQPortAllowedUntagVlanList,
       "qtechQinQPortAllowedTagVlanList": qtechQinQPortAllowedTagVlanList,
       "qtechQinQServiceTPIDValue": qtechQinQServiceTPIDValue,
       "qtechQinQIfServiceTPIDConfigTable": qtechQinQIfServiceTPIDConfigTable,
       "qtechQinQIfServiceTPIDConfigEntry": qtechQinQIfServiceTPIDConfigEntry,
       "qtechQinQIfServiceTPIDConfigIfIndex": qtechQinQIfServiceTPIDConfigIfIndex,
       "qtechQinQIfServiceTPIDValue": qtechQinQIfServiceTPIDValue,
       "qtechQinQPriorityCopyTable": qtechQinQPriorityCopyTable,
       "qtechQinQPriorityCopyEntry": qtechQinQPriorityCopyEntry,
       "qtechQinQPriorityCopyIfIndex": qtechQinQPriorityCopyIfIndex,
       "qtechQinQPriorityCopyPortStatus": qtechQinQPriorityCopyPortStatus,
       "qtechQinQPriorityRemarkTable": qtechQinQPriorityRemarkTable,
       "qtechQinQPriorityRemarkEntry": qtechQinQPriorityRemarkEntry,
       "qtechQinQPriorityRemarkIfIndex": qtechQinQPriorityRemarkIfIndex,
       "qtechQinQPriorityValue": qtechQinQPriorityValue,
       "qtechQinQPriorityRemarkValue": qtechQinQPriorityRemarkValue,
       "qtechselectiveQinQBasedOnVlanTable": qtechselectiveQinQBasedOnVlanTable,
       "qtechselectiveQinQBasedOnVlanEntry": qtechselectiveQinQBasedOnVlanEntry,
       "qtechselectiveQinQBasedOnVlanIfIndex": qtechselectiveQinQBasedOnVlanIfIndex,
       "qtechselectiveQinQBasedOnVlanType": qtechselectiveQinQBasedOnVlanType,
       "qtechselectiveQinQBasedOnVlanOuterVlanID": qtechselectiveQinQBasedOnVlanOuterVlanID,
       "qtechselectiveQinQBasedOnVlanOldOuterVlanID": qtechselectiveQinQBasedOnVlanOldOuterVlanID,
       "qtechselectiveQinQBasedOnVlanVlanList": qtechselectiveQinQBasedOnVlanVlanList,
       "qtechselectiveQinQBasedOnAclTable": qtechselectiveQinQBasedOnAclTable,
       "qtechselectiveQinQBasedOnAclEntry": qtechselectiveQinQBasedOnAclEntry,
       "qtechselectiveQinQBasedOnAclIfIndex": qtechselectiveQinQBasedOnAclIfIndex,
       "qtechselectiveQinQBasedOnAclType": qtechselectiveQinQBasedOnAclType,
       "qtechselectiveQinQBasedOnAclAclID": qtechselectiveQinQBasedOnAclAclID,
       "qtechselectiveQinQBasedOnAclVlanID": qtechselectiveQinQBasedOnAclVlanID,
       "qtechQinQVlanMappingTable": qtechQinQVlanMappingTable,
       "qtechQinQVlanMappingEntry": qtechQinQVlanMappingEntry,
       "qtechQinQVlanMappingIfIndex": qtechQinQVlanMappingIfIndex,
       "qtechQinQVlanMappingType": qtechQinQVlanMappingType,
       "qtechQinQVlanMappingNewVlanID": qtechQinQVlanMappingNewVlanID,
       "qtechQinQVlanMappingOldVlanList": qtechQinQVlanMappingOldVlanList,
       "qtechQinQVlanMappingOldVlanID": qtechQinQVlanMappingOldVlanID,
       "qtechQinQMIBConformance": qtechQinQMIBConformance,
       "qtechQinQMIBCompliances": qtechQinQMIBCompliances,
       "qtechQinQMIBCompliance": qtechQinQMIBCompliance,
       "qtechQinQMIBGroups": qtechQinQMIBGroups,
       "qtechQinQMIBGroup": qtechQinQMIBGroup}
)
