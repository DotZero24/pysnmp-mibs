# SNMP MIB module (FS-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-QINQ-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:41 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

fsQinQMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53)
)
if mibBuilder.loadTexts:
    fsQinQMIB.setRevisions(
        ("2009-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_FsQINQMIBObjects_ObjectIdentity = ObjectIdentity
fsQINQMIBObjects = _FsQINQMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1)
)
_FsQinQPortConfigTable_Object = MibTable
fsQinQPortConfigTable = _FsQinQPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1)
)
if mibBuilder.loadTexts:
    fsQinQPortConfigTable.setStatus("current")
_FsQinQPortConfigEntry_Object = MibTableRow
fsQinQPortConfigEntry = _FsQinQPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1, 1)
)
fsQinQPortConfigEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsQinQPortConfigIndex"),
)
if mibBuilder.loadTexts:
    fsQinQPortConfigEntry.setStatus("current")
_FsQinQPortConfigIndex_Type = IfIndex
_FsQinQPortConfigIndex_Object = MibTableColumn
fsQinQPortConfigIndex = _FsQinQPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1, 1, 1),
    _FsQinQPortConfigIndex_Type()
)
fsQinQPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQinQPortConfigIndex.setStatus("current")


class _FsQinQPortConfigMode_Type(Integer32):
    """Custom type fsQinQPortConfigMode based on Integer32"""
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


_FsQinQPortConfigMode_Type.__name__ = "Integer32"
_FsQinQPortConfigMode_Object = MibTableColumn
fsQinQPortConfigMode = _FsQinQPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1, 1, 2),
    _FsQinQPortConfigMode_Type()
)
fsQinQPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQPortConfigMode.setStatus("current")
_FsQinQPortNativeVlan_Type = VlanId
_FsQinQPortNativeVlan_Object = MibTableColumn
fsQinQPortNativeVlan = _FsQinQPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1, 1, 3),
    _FsQinQPortNativeVlan_Type()
)
fsQinQPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQPortNativeVlan.setStatus("current")
_FsQinQPortAllowedUntagVlanList_Type = VlanList
_FsQinQPortAllowedUntagVlanList_Object = MibTableColumn
fsQinQPortAllowedUntagVlanList = _FsQinQPortAllowedUntagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1, 1, 4),
    _FsQinQPortAllowedUntagVlanList_Type()
)
fsQinQPortAllowedUntagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQPortAllowedUntagVlanList.setStatus("current")
_FsQinQPortAllowedTagVlanList_Type = VlanList
_FsQinQPortAllowedTagVlanList_Object = MibTableColumn
fsQinQPortAllowedTagVlanList = _FsQinQPortAllowedTagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 1, 1, 5),
    _FsQinQPortAllowedTagVlanList_Type()
)
fsQinQPortAllowedTagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQPortAllowedTagVlanList.setStatus("current")


class _FsQinQServiceTPIDValue_Type(Integer32):
    """Custom type fsQinQServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQinQServiceTPIDValue_Type.__name__ = "Integer32"
_FsQinQServiceTPIDValue_Object = MibScalar
fsQinQServiceTPIDValue = _FsQinQServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 2),
    _FsQinQServiceTPIDValue_Type()
)
fsQinQServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQServiceTPIDValue.setStatus("current")
_FsQinQIfServiceTPIDConfigTable_Object = MibTable
fsQinQIfServiceTPIDConfigTable = _FsQinQIfServiceTPIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 3)
)
if mibBuilder.loadTexts:
    fsQinQIfServiceTPIDConfigTable.setStatus("current")
_FsQinQIfServiceTPIDConfigEntry_Object = MibTableRow
fsQinQIfServiceTPIDConfigEntry = _FsQinQIfServiceTPIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 3, 1)
)
fsQinQIfServiceTPIDConfigEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsQinQIfServiceTPIDConfigIfIndex"),
)
if mibBuilder.loadTexts:
    fsQinQIfServiceTPIDConfigEntry.setStatus("current")
_FsQinQIfServiceTPIDConfigIfIndex_Type = IfIndex
_FsQinQIfServiceTPIDConfigIfIndex_Object = MibTableColumn
fsQinQIfServiceTPIDConfigIfIndex = _FsQinQIfServiceTPIDConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 3, 1, 1),
    _FsQinQIfServiceTPIDConfigIfIndex_Type()
)
fsQinQIfServiceTPIDConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQinQIfServiceTPIDConfigIfIndex.setStatus("current")


class _FsQinQIfServiceTPIDValue_Type(Integer32):
    """Custom type fsQinQIfServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsQinQIfServiceTPIDValue_Type.__name__ = "Integer32"
_FsQinQIfServiceTPIDValue_Object = MibTableColumn
fsQinQIfServiceTPIDValue = _FsQinQIfServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 3, 1, 2),
    _FsQinQIfServiceTPIDValue_Type()
)
fsQinQIfServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQIfServiceTPIDValue.setStatus("current")
_FsQinQPriorityCopyTable_Object = MibTable
fsQinQPriorityCopyTable = _FsQinQPriorityCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 4)
)
if mibBuilder.loadTexts:
    fsQinQPriorityCopyTable.setStatus("current")
_FsQinQPriorityCopyEntry_Object = MibTableRow
fsQinQPriorityCopyEntry = _FsQinQPriorityCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 4, 1)
)
fsQinQPriorityCopyEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsQinQPriorityCopyIfIndex"),
)
if mibBuilder.loadTexts:
    fsQinQPriorityCopyEntry.setStatus("current")
_FsQinQPriorityCopyIfIndex_Type = IfIndex
_FsQinQPriorityCopyIfIndex_Object = MibTableColumn
fsQinQPriorityCopyIfIndex = _FsQinQPriorityCopyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 4, 1, 1),
    _FsQinQPriorityCopyIfIndex_Type()
)
fsQinQPriorityCopyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQinQPriorityCopyIfIndex.setStatus("current")
_FsQinQPriorityCopyPortStatus_Type = EnabledStatus
_FsQinQPriorityCopyPortStatus_Object = MibTableColumn
fsQinQPriorityCopyPortStatus = _FsQinQPriorityCopyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 4, 1, 2),
    _FsQinQPriorityCopyPortStatus_Type()
)
fsQinQPriorityCopyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQinQPriorityCopyPortStatus.setStatus("current")
_FsQinQPriorityRemarkTable_Object = MibTable
fsQinQPriorityRemarkTable = _FsQinQPriorityRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 5)
)
if mibBuilder.loadTexts:
    fsQinQPriorityRemarkTable.setStatus("current")
_FsQinQPriorityRemarkEntry_Object = MibTableRow
fsQinQPriorityRemarkEntry = _FsQinQPriorityRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 5, 1)
)
fsQinQPriorityRemarkEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsQinQPriorityRemarkIfIndex"),
    (0, "FS-QINQ-MIB", "fsQinQPriorityValue"),
)
if mibBuilder.loadTexts:
    fsQinQPriorityRemarkEntry.setStatus("current")
_FsQinQPriorityRemarkIfIndex_Type = IfIndex
_FsQinQPriorityRemarkIfIndex_Object = MibTableColumn
fsQinQPriorityRemarkIfIndex = _FsQinQPriorityRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 5, 1, 1),
    _FsQinQPriorityRemarkIfIndex_Type()
)
fsQinQPriorityRemarkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQinQPriorityRemarkIfIndex.setStatus("current")


class _FsQinQPriorityValue_Type(Integer32):
    """Custom type fsQinQPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQinQPriorityValue_Type.__name__ = "Integer32"
_FsQinQPriorityValue_Object = MibTableColumn
fsQinQPriorityValue = _FsQinQPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 5, 1, 2),
    _FsQinQPriorityValue_Type()
)
fsQinQPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQinQPriorityValue.setStatus("current")


class _FsQinQPriorityRemarkValue_Type(Integer32):
    """Custom type fsQinQPriorityRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsQinQPriorityRemarkValue_Type.__name__ = "Integer32"
_FsQinQPriorityRemarkValue_Object = MibTableColumn
fsQinQPriorityRemarkValue = _FsQinQPriorityRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 5, 1, 3),
    _FsQinQPriorityRemarkValue_Type()
)
fsQinQPriorityRemarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQinQPriorityRemarkValue.setStatus("current")
_FsselectiveQinQBasedOnVlanTable_Object = MibTable
fsselectiveQinQBasedOnVlanTable = _FsselectiveQinQBasedOnVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6)
)
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanTable.setStatus("current")
_FsselectiveQinQBasedOnVlanEntry_Object = MibTableRow
fsselectiveQinQBasedOnVlanEntry = _FsselectiveQinQBasedOnVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6, 1)
)
fsselectiveQinQBasedOnVlanEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanIfIndex"),
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanType"),
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanOuterVlanID"),
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanOldOuterVlanID"),
)
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanEntry.setStatus("current")
_FsselectiveQinQBasedOnVlanIfIndex_Type = IfIndex
_FsselectiveQinQBasedOnVlanIfIndex_Object = MibTableColumn
fsselectiveQinQBasedOnVlanIfIndex = _FsselectiveQinQBasedOnVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6, 1, 1),
    _FsselectiveQinQBasedOnVlanIfIndex_Type()
)
fsselectiveQinQBasedOnVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanIfIndex.setStatus("current")


class _FsselectiveQinQBasedOnVlanType_Type(Integer32):
    """Custom type fsselectiveQinQBasedOnVlanType based on Integer32"""
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


_FsselectiveQinQBasedOnVlanType_Type.__name__ = "Integer32"
_FsselectiveQinQBasedOnVlanType_Object = MibTableColumn
fsselectiveQinQBasedOnVlanType = _FsselectiveQinQBasedOnVlanType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6, 1, 2),
    _FsselectiveQinQBasedOnVlanType_Type()
)
fsselectiveQinQBasedOnVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanType.setStatus("current")


class _FsselectiveQinQBasedOnVlanOuterVlanID_Type(Integer32):
    """Custom type fsselectiveQinQBasedOnVlanOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsselectiveQinQBasedOnVlanOuterVlanID_Type.__name__ = "Integer32"
_FsselectiveQinQBasedOnVlanOuterVlanID_Object = MibTableColumn
fsselectiveQinQBasedOnVlanOuterVlanID = _FsselectiveQinQBasedOnVlanOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6, 1, 3),
    _FsselectiveQinQBasedOnVlanOuterVlanID_Type()
)
fsselectiveQinQBasedOnVlanOuterVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanOuterVlanID.setStatus("current")


class _FsselectiveQinQBasedOnVlanOldOuterVlanID_Type(Integer32):
    """Custom type fsselectiveQinQBasedOnVlanOldOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsselectiveQinQBasedOnVlanOldOuterVlanID_Type.__name__ = "Integer32"
_FsselectiveQinQBasedOnVlanOldOuterVlanID_Object = MibTableColumn
fsselectiveQinQBasedOnVlanOldOuterVlanID = _FsselectiveQinQBasedOnVlanOldOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6, 1, 4),
    _FsselectiveQinQBasedOnVlanOldOuterVlanID_Type()
)
fsselectiveQinQBasedOnVlanOldOuterVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanOldOuterVlanID.setStatus("current")
_FsselectiveQinQBasedOnVlanVlanList_Type = VlanList
_FsselectiveQinQBasedOnVlanVlanList_Object = MibTableColumn
fsselectiveQinQBasedOnVlanVlanList = _FsselectiveQinQBasedOnVlanVlanList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 6, 1, 5),
    _FsselectiveQinQBasedOnVlanVlanList_Type()
)
fsselectiveQinQBasedOnVlanVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnVlanVlanList.setStatus("current")
_FsselectiveQinQBasedOnAclTable_Object = MibTable
fsselectiveQinQBasedOnAclTable = _FsselectiveQinQBasedOnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 7)
)
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnAclTable.setStatus("current")
_FsselectiveQinQBasedOnAclEntry_Object = MibTableRow
fsselectiveQinQBasedOnAclEntry = _FsselectiveQinQBasedOnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 7, 1)
)
fsselectiveQinQBasedOnAclEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnAclIfIndex"),
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnAclType"),
    (0, "FS-QINQ-MIB", "fsselectiveQinQBasedOnAclAclID"),
)
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnAclEntry.setStatus("current")
_FsselectiveQinQBasedOnAclIfIndex_Type = IfIndex
_FsselectiveQinQBasedOnAclIfIndex_Object = MibTableColumn
fsselectiveQinQBasedOnAclIfIndex = _FsselectiveQinQBasedOnAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 7, 1, 1),
    _FsselectiveQinQBasedOnAclIfIndex_Type()
)
fsselectiveQinQBasedOnAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnAclIfIndex.setStatus("current")


class _FsselectiveQinQBasedOnAclType_Type(Integer32):
    """Custom type fsselectiveQinQBasedOnAclType based on Integer32"""
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


_FsselectiveQinQBasedOnAclType_Type.__name__ = "Integer32"
_FsselectiveQinQBasedOnAclType_Object = MibTableColumn
fsselectiveQinQBasedOnAclType = _FsselectiveQinQBasedOnAclType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 7, 1, 2),
    _FsselectiveQinQBasedOnAclType_Type()
)
fsselectiveQinQBasedOnAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnAclType.setStatus("current")
_FsselectiveQinQBasedOnAclAclID_Type = Integer32
_FsselectiveQinQBasedOnAclAclID_Object = MibTableColumn
fsselectiveQinQBasedOnAclAclID = _FsselectiveQinQBasedOnAclAclID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 7, 1, 3),
    _FsselectiveQinQBasedOnAclAclID_Type()
)
fsselectiveQinQBasedOnAclAclID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnAclAclID.setStatus("current")


class _FsselectiveQinQBasedOnAclVlanID_Type(Integer32):
    """Custom type fsselectiveQinQBasedOnAclVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsselectiveQinQBasedOnAclVlanID_Type.__name__ = "Integer32"
_FsselectiveQinQBasedOnAclVlanID_Object = MibTableColumn
fsselectiveQinQBasedOnAclVlanID = _FsselectiveQinQBasedOnAclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 7, 1, 4),
    _FsselectiveQinQBasedOnAclVlanID_Type()
)
fsselectiveQinQBasedOnAclVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsselectiveQinQBasedOnAclVlanID.setStatus("current")
_FsQinQVlanMappingTable_Object = MibTable
fsQinQVlanMappingTable = _FsQinQVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8)
)
if mibBuilder.loadTexts:
    fsQinQVlanMappingTable.setStatus("current")
_FsQinQVlanMappingEntry_Object = MibTableRow
fsQinQVlanMappingEntry = _FsQinQVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8, 1)
)
fsQinQVlanMappingEntry.setIndexNames(
    (0, "FS-QINQ-MIB", "fsQinQVlanMappingIfIndex"),
    (0, "FS-QINQ-MIB", "fsQinQVlanMappingType"),
    (0, "FS-QINQ-MIB", "fsQinQVlanMappingNewVlanID"),
)
if mibBuilder.loadTexts:
    fsQinQVlanMappingEntry.setStatus("current")
_FsQinQVlanMappingIfIndex_Type = IfIndex
_FsQinQVlanMappingIfIndex_Object = MibTableColumn
fsQinQVlanMappingIfIndex = _FsQinQVlanMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8, 1, 1),
    _FsQinQVlanMappingIfIndex_Type()
)
fsQinQVlanMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsQinQVlanMappingIfIndex.setStatus("current")


class _FsQinQVlanMappingType_Type(Integer32):
    """Custom type fsQinQVlanMappingType based on Integer32"""
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


_FsQinQVlanMappingType_Type.__name__ = "Integer32"
_FsQinQVlanMappingType_Object = MibTableColumn
fsQinQVlanMappingType = _FsQinQVlanMappingType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8, 1, 2),
    _FsQinQVlanMappingType_Type()
)
fsQinQVlanMappingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQinQVlanMappingType.setStatus("current")


class _FsQinQVlanMappingNewVlanID_Type(Integer32):
    """Custom type fsQinQVlanMappingNewVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsQinQVlanMappingNewVlanID_Type.__name__ = "Integer32"
_FsQinQVlanMappingNewVlanID_Object = MibTableColumn
fsQinQVlanMappingNewVlanID = _FsQinQVlanMappingNewVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8, 1, 3),
    _FsQinQVlanMappingNewVlanID_Type()
)
fsQinQVlanMappingNewVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQinQVlanMappingNewVlanID.setStatus("current")
_FsQinQVlanMappingOldVlanList_Type = VlanList
_FsQinQVlanMappingOldVlanList_Object = MibTableColumn
fsQinQVlanMappingOldVlanList = _FsQinQVlanMappingOldVlanList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8, 1, 4),
    _FsQinQVlanMappingOldVlanList_Type()
)
fsQinQVlanMappingOldVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQinQVlanMappingOldVlanList.setStatus("current")


class _FsQinQVlanMappingOldVlanID_Type(Integer32):
    """Custom type fsQinQVlanMappingOldVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsQinQVlanMappingOldVlanID_Type.__name__ = "Integer32"
_FsQinQVlanMappingOldVlanID_Object = MibTableColumn
fsQinQVlanMappingOldVlanID = _FsQinQVlanMappingOldVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 1, 8, 1, 5),
    _FsQinQVlanMappingOldVlanID_Type()
)
fsQinQVlanMappingOldVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQinQVlanMappingOldVlanID.setStatus("current")
_FsQinQMIBConformance_ObjectIdentity = ObjectIdentity
fsQinQMIBConformance = _FsQinQMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 2)
)
_FsQinQMIBCompliances_ObjectIdentity = ObjectIdentity
fsQinQMIBCompliances = _FsQinQMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 2, 1)
)
_FsQinQMIBGroups_ObjectIdentity = ObjectIdentity
fsQinQMIBGroups = _FsQinQMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 2, 2)
)

# Managed Objects groups

fsQinQMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 2, 2, 1)
)
fsQinQMIBGroup.setObjects(
      *(("FS-QINQ-MIB", "fsQinQPortConfigMode"),
        ("FS-QINQ-MIB", "fsQinQPortNativeVlan"),
        ("FS-QINQ-MIB", "fsQinQPortAllowedUntagVlanList"),
        ("FS-QINQ-MIB", "fsQinQPortAllowedTagVlanList"),
        ("FS-QINQ-MIB", "fsQinQServiceTPIDValue"),
        ("FS-QINQ-MIB", "fsQinQIfServiceTPIDValue"),
        ("FS-QINQ-MIB", "fsQinQPriorityCopyPortStatus"),
        ("FS-QINQ-MIB", "fsQinQPriorityValue"),
        ("FS-QINQ-MIB", "fsQinQPriorityRemarkValue"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanType"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanOuterVlanID"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanOldOuterVlanID"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnVlanVlanList"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnAclType"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnAclAclID"),
        ("FS-QINQ-MIB", "fsselectiveQinQBasedOnAclVlanID"),
        ("FS-QINQ-MIB", "fsQinQVlanMappingNewVlanID"))
)
if mibBuilder.loadTexts:
    fsQinQMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsQinQMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 53, 2, 1, 1)
)
fsQinQMIBCompliance.setObjects(
    ("FS-QINQ-MIB", "fsQinQMIBGroup")
)
if mibBuilder.loadTexts:
    fsQinQMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-QINQ-MIB",
    **{"VlanList": VlanList,
       "fsQinQMIB": fsQinQMIB,
       "fsQINQMIBObjects": fsQINQMIBObjects,
       "fsQinQPortConfigTable": fsQinQPortConfigTable,
       "fsQinQPortConfigEntry": fsQinQPortConfigEntry,
       "fsQinQPortConfigIndex": fsQinQPortConfigIndex,
       "fsQinQPortConfigMode": fsQinQPortConfigMode,
       "fsQinQPortNativeVlan": fsQinQPortNativeVlan,
       "fsQinQPortAllowedUntagVlanList": fsQinQPortAllowedUntagVlanList,
       "fsQinQPortAllowedTagVlanList": fsQinQPortAllowedTagVlanList,
       "fsQinQServiceTPIDValue": fsQinQServiceTPIDValue,
       "fsQinQIfServiceTPIDConfigTable": fsQinQIfServiceTPIDConfigTable,
       "fsQinQIfServiceTPIDConfigEntry": fsQinQIfServiceTPIDConfigEntry,
       "fsQinQIfServiceTPIDConfigIfIndex": fsQinQIfServiceTPIDConfigIfIndex,
       "fsQinQIfServiceTPIDValue": fsQinQIfServiceTPIDValue,
       "fsQinQPriorityCopyTable": fsQinQPriorityCopyTable,
       "fsQinQPriorityCopyEntry": fsQinQPriorityCopyEntry,
       "fsQinQPriorityCopyIfIndex": fsQinQPriorityCopyIfIndex,
       "fsQinQPriorityCopyPortStatus": fsQinQPriorityCopyPortStatus,
       "fsQinQPriorityRemarkTable": fsQinQPriorityRemarkTable,
       "fsQinQPriorityRemarkEntry": fsQinQPriorityRemarkEntry,
       "fsQinQPriorityRemarkIfIndex": fsQinQPriorityRemarkIfIndex,
       "fsQinQPriorityValue": fsQinQPriorityValue,
       "fsQinQPriorityRemarkValue": fsQinQPriorityRemarkValue,
       "fsselectiveQinQBasedOnVlanTable": fsselectiveQinQBasedOnVlanTable,
       "fsselectiveQinQBasedOnVlanEntry": fsselectiveQinQBasedOnVlanEntry,
       "fsselectiveQinQBasedOnVlanIfIndex": fsselectiveQinQBasedOnVlanIfIndex,
       "fsselectiveQinQBasedOnVlanType": fsselectiveQinQBasedOnVlanType,
       "fsselectiveQinQBasedOnVlanOuterVlanID": fsselectiveQinQBasedOnVlanOuterVlanID,
       "fsselectiveQinQBasedOnVlanOldOuterVlanID": fsselectiveQinQBasedOnVlanOldOuterVlanID,
       "fsselectiveQinQBasedOnVlanVlanList": fsselectiveQinQBasedOnVlanVlanList,
       "fsselectiveQinQBasedOnAclTable": fsselectiveQinQBasedOnAclTable,
       "fsselectiveQinQBasedOnAclEntry": fsselectiveQinQBasedOnAclEntry,
       "fsselectiveQinQBasedOnAclIfIndex": fsselectiveQinQBasedOnAclIfIndex,
       "fsselectiveQinQBasedOnAclType": fsselectiveQinQBasedOnAclType,
       "fsselectiveQinQBasedOnAclAclID": fsselectiveQinQBasedOnAclAclID,
       "fsselectiveQinQBasedOnAclVlanID": fsselectiveQinQBasedOnAclVlanID,
       "fsQinQVlanMappingTable": fsQinQVlanMappingTable,
       "fsQinQVlanMappingEntry": fsQinQVlanMappingEntry,
       "fsQinQVlanMappingIfIndex": fsQinQVlanMappingIfIndex,
       "fsQinQVlanMappingType": fsQinQVlanMappingType,
       "fsQinQVlanMappingNewVlanID": fsQinQVlanMappingNewVlanID,
       "fsQinQVlanMappingOldVlanList": fsQinQVlanMappingOldVlanList,
       "fsQinQVlanMappingOldVlanID": fsQinQVlanMappingOldVlanID,
       "fsQinQMIBConformance": fsQinQMIBConformance,
       "fsQinQMIBCompliances": fsQinQMIBCompliances,
       "fsQinQMIBCompliance": fsQinQMIBCompliance,
       "fsQinQMIBGroups": fsQinQMIBGroups,
       "fsQinQMIBGroup": fsQinQMIBGroup}
)
