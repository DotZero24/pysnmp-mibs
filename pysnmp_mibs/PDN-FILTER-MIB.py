# SNMP MIB module (PDN-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-FILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:59:52 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_filter,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-filter")

(VnidRange,) = mibBuilder.importSymbols(
    "PDN-TC",
    "VnidRange")

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
 NotificationType,
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
    "NotificationType",
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysDevFilterMIBObjects_ObjectIdentity = ObjectIdentity
sysDevFilterMIBObjects = _SysDevFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1)
)
_SysDevFilter_ObjectIdentity = ObjectIdentity
sysDevFilter = _SysDevFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1)
)


class _SysDevSNInjectionType_Type(Integer32):
    """Custom type sysDevSNInjectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipFilter", 1)
    )


_SysDevSNInjectionType_Type.__name__ = "Integer32"
_SysDevSNInjectionType_Object = MibScalar
sysDevSNInjectionType = _SysDevSNInjectionType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 1),
    _SysDevSNInjectionType_Type()
)
sysDevSNInjectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDevSNInjectionType.setStatus("mandatory")
_SysDevSNInjectionVnid_Type = VnidRange
_SysDevSNInjectionVnid_Object = MibScalar
sysDevSNInjectionVnid = _SysDevSNInjectionVnid_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 2),
    _SysDevSNInjectionVnid_Type()
)
sysDevSNInjectionVnid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDevSNInjectionVnid.setStatus("mandatory")
_SysDevFilterConfigTable_Object = MibTable
sysDevFilterConfigTable = _SysDevFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sysDevFilterConfigTable.setStatus("mandatory")
_SysDevFilterConfigTableEntry_Object = MibTableRow
sysDevFilterConfigTableEntry = _SysDevFilterConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1)
)
sysDevFilterConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevFilterIndex"),
)
if mibBuilder.loadTexts:
    sysDevFilterConfigTableEntry.setStatus("mandatory")
_SysDevFilterIndex_Type = Integer32
_SysDevFilterIndex_Object = MibTableColumn
sysDevFilterIndex = _SysDevFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 1),
    _SysDevFilterIndex_Type()
)
sysDevFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterIndex.setStatus("mandatory")


class _SysDevFilterName_Type(DisplayString):
    """Custom type sysDevFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevFilterName_Type.__name__ = "DisplayString"
_SysDevFilterName_Object = MibTableColumn
sysDevFilterName = _SysDevFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 2),
    _SysDevFilterName_Type()
)
sysDevFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterName.setStatus("mandatory")


class _SysDevFilterType_Type(Integer32):
    """Custom type sysDevFilterType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("layer1", 1),
          ("layer2", 2),
          ("layer3", 3),
          ("layer4", 4),
          ("layer5", 5),
          ("layer6", 6),
          ("layer7", 7),
          ("unknown", 8))
    )


_SysDevFilterType_Type.__name__ = "Integer32"
_SysDevFilterType_Object = MibTableColumn
sysDevFilterType = _SysDevFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 3),
    _SysDevFilterType_Type()
)
sysDevFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterType.setStatus("mandatory")


class _SysDevDefFilterAction_Type(Integer32):
    """Custom type sysDevDefFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_SysDevDefFilterAction_Type.__name__ = "Integer32"
_SysDevDefFilterAction_Object = MibTableColumn
sysDevDefFilterAction = _SysDevDefFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 4),
    _SysDevDefFilterAction_Type()
)
sysDevDefFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevDefFilterAction.setStatus("mandatory")
_SysDevFilterNumOfDynamicRules_Type = Integer32
_SysDevFilterNumOfDynamicRules_Object = MibTableColumn
sysDevFilterNumOfDynamicRules = _SysDevFilterNumOfDynamicRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 5),
    _SysDevFilterNumOfDynamicRules_Type()
)
sysDevFilterNumOfDynamicRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterNumOfDynamicRules.setStatus("mandatory")
_SysDevFilterNumOfStaticRules_Type = Integer32
_SysDevFilterNumOfStaticRules_Object = MibTableColumn
sysDevFilterNumOfStaticRules = _SysDevFilterNumOfStaticRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 6),
    _SysDevFilterNumOfStaticRules_Type()
)
sysDevFilterNumOfStaticRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterNumOfStaticRules.setStatus("mandatory")
_SysDevFilterRefCount_Type = Integer32
_SysDevFilterRefCount_Object = MibTableColumn
sysDevFilterRefCount = _SysDevFilterRefCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 7),
    _SysDevFilterRefCount_Type()
)
sysDevFilterRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterRefCount.setStatus("mandatory")
_SysDevFilterRowStatus_Type = RowStatus
_SysDevFilterRowStatus_Object = MibTableColumn
sysDevFilterRowStatus = _SysDevFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 3, 1, 8),
    _SysDevFilterRowStatus_Type()
)
sysDevFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterRowStatus.setStatus("mandatory")
_SysDevL2FilterRuleConfigTable_Object = MibTable
sysDevL2FilterRuleConfigTable = _SysDevL2FilterRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sysDevL2FilterRuleConfigTable.setStatus("mandatory")
_SysDevL2FilterRuleConfigTableEntry_Object = MibTableRow
sysDevL2FilterRuleConfigTableEntry = _SysDevL2FilterRuleConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1)
)
sysDevL2FilterRuleConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevL2FilterRuleIndex"),
)
if mibBuilder.loadTexts:
    sysDevL2FilterRuleConfigTableEntry.setStatus("mandatory")
_SysDevL2FilterRuleIndex_Type = Integer32
_SysDevL2FilterRuleIndex_Object = MibTableColumn
sysDevL2FilterRuleIndex = _SysDevL2FilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 1),
    _SysDevL2FilterRuleIndex_Type()
)
sysDevL2FilterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleIndex.setStatus("mandatory")


class _SysDevL2FilterRuleName_Type(DisplayString):
    """Custom type sysDevL2FilterRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevL2FilterRuleName_Type.__name__ = "DisplayString"
_SysDevL2FilterRuleName_Object = MibTableColumn
sysDevL2FilterRuleName = _SysDevL2FilterRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 2),
    _SysDevL2FilterRuleName_Type()
)
sysDevL2FilterRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleName.setStatus("mandatory")


class _SysDevL2FilterRuleEtherFrameType_Type(Integer32):
    """Custom type sysDevL2FilterRuleEtherFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dix", 1),
          ("snap", 2))
    )


_SysDevL2FilterRuleEtherFrameType_Type.__name__ = "Integer32"
_SysDevL2FilterRuleEtherFrameType_Object = MibTableColumn
sysDevL2FilterRuleEtherFrameType = _SysDevL2FilterRuleEtherFrameType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 3),
    _SysDevL2FilterRuleEtherFrameType_Type()
)
sysDevL2FilterRuleEtherFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleEtherFrameType.setStatus("mandatory")


class _SysDevL2FilterRuleEtherType_Type(Integer32):
    """Custom type sysDevL2FilterRuleEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("range", 1),
          ("singleType", 2))
    )


_SysDevL2FilterRuleEtherType_Type.__name__ = "Integer32"
_SysDevL2FilterRuleEtherType_Object = MibTableColumn
sysDevL2FilterRuleEtherType = _SysDevL2FilterRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 4),
    _SysDevL2FilterRuleEtherType_Type()
)
sysDevL2FilterRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleEtherType.setStatus("mandatory")
_SysDevL2FilterRuleEtherTypeRangeStarts_Type = Integer32
_SysDevL2FilterRuleEtherTypeRangeStarts_Object = MibTableColumn
sysDevL2FilterRuleEtherTypeRangeStarts = _SysDevL2FilterRuleEtherTypeRangeStarts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 5),
    _SysDevL2FilterRuleEtherTypeRangeStarts_Type()
)
sysDevL2FilterRuleEtherTypeRangeStarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleEtherTypeRangeStarts.setStatus("mandatory")
_SysDevL2FilterRuleEtherTypeRangeEnds_Type = Integer32
_SysDevL2FilterRuleEtherTypeRangeEnds_Object = MibTableColumn
sysDevL2FilterRuleEtherTypeRangeEnds = _SysDevL2FilterRuleEtherTypeRangeEnds_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 6),
    _SysDevL2FilterRuleEtherTypeRangeEnds_Type()
)
sysDevL2FilterRuleEtherTypeRangeEnds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleEtherTypeRangeEnds.setStatus("mandatory")


class _SysDevL2FilterRuleAction_Type(Integer32):
    """Custom type sysDevL2FilterRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_SysDevL2FilterRuleAction_Type.__name__ = "Integer32"
_SysDevL2FilterRuleAction_Object = MibTableColumn
sysDevL2FilterRuleAction = _SysDevL2FilterRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 7),
    _SysDevL2FilterRuleAction_Type()
)
sysDevL2FilterRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleAction.setStatus("mandatory")
_SysDevL2FilterRuleRowStatus_Type = RowStatus
_SysDevL2FilterRuleRowStatus_Object = MibTableColumn
sysDevL2FilterRuleRowStatus = _SysDevL2FilterRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 4, 1, 8),
    _SysDevL2FilterRuleRowStatus_Type()
)
sysDevL2FilterRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleRowStatus.setStatus("mandatory")
_SysDevFilterBindingTable_Object = MibTable
sysDevFilterBindingTable = _SysDevFilterBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sysDevFilterBindingTable.setStatus("mandatory")
_SysDevFilterBindingTableEntry_Object = MibTableRow
sysDevFilterBindingTableEntry = _SysDevFilterBindingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5, 1)
)
sysDevFilterBindingTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-FILTER-MIB", "sysDevFilterBindingIndex"),
    (0, "PDN-FILTER-MIB", "sysDevFilterBindingDirection"),
)
if mibBuilder.loadTexts:
    sysDevFilterBindingTableEntry.setStatus("mandatory")
_SysDevFilterBindingIndex_Type = Integer32
_SysDevFilterBindingIndex_Object = MibTableColumn
sysDevFilterBindingIndex = _SysDevFilterBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5, 1, 1),
    _SysDevFilterBindingIndex_Type()
)
sysDevFilterBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterBindingIndex.setStatus("mandatory")


class _SysDevFilterBindingDirection_Type(Integer32):
    """Custom type sysDevFilterBindingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inboundFilter", 1),
          ("outboundFilter", 2),
          ("inboundOutboundFilter", 3))
    )


_SysDevFilterBindingDirection_Type.__name__ = "Integer32"
_SysDevFilterBindingDirection_Object = MibTableColumn
sysDevFilterBindingDirection = _SysDevFilterBindingDirection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5, 1, 2),
    _SysDevFilterBindingDirection_Type()
)
sysDevFilterBindingDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterBindingDirection.setStatus("mandatory")


class _SysDevFilterBindingAdminStatus_Type(Integer32):
    """Custom type sysDevFilterBindingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SysDevFilterBindingAdminStatus_Type.__name__ = "Integer32"
_SysDevFilterBindingAdminStatus_Object = MibTableColumn
sysDevFilterBindingAdminStatus = _SysDevFilterBindingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5, 1, 3),
    _SysDevFilterBindingAdminStatus_Type()
)
sysDevFilterBindingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterBindingAdminStatus.setStatus("mandatory")


class _SysDevFilterBindingOperStatus_Type(Integer32):
    """Custom type sysDevFilterBindingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SysDevFilterBindingOperStatus_Type.__name__ = "Integer32"
_SysDevFilterBindingOperStatus_Object = MibTableColumn
sysDevFilterBindingOperStatus = _SysDevFilterBindingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5, 1, 4),
    _SysDevFilterBindingOperStatus_Type()
)
sysDevFilterBindingOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterBindingOperStatus.setStatus("mandatory")
_SysDevFilterBindingRowStatus_Type = RowStatus
_SysDevFilterBindingRowStatus_Object = MibTableColumn
sysDevFilterBindingRowStatus = _SysDevFilterBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 5, 1, 5),
    _SysDevFilterBindingRowStatus_Type()
)
sysDevFilterBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterBindingRowStatus.setStatus("mandatory")
_SysDevFilterIndexNext_Type = Integer32
_SysDevFilterIndexNext_Object = MibScalar
sysDevFilterIndexNext = _SysDevFilterIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 6),
    _SysDevFilterIndexNext_Type()
)
sysDevFilterIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterIndexNext.setStatus("mandatory")
_SysDevL2FilterRuleIndexNext_Type = Integer32
_SysDevL2FilterRuleIndexNext_Object = MibScalar
sysDevL2FilterRuleIndexNext = _SysDevL2FilterRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 7),
    _SysDevL2FilterRuleIndexNext_Type()
)
sysDevL2FilterRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevL2FilterRuleIndexNext.setStatus("mandatory")
_SysDevFilterToRuleBindingTable_Object = MibTable
sysDevFilterToRuleBindingTable = _SysDevFilterToRuleBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 8)
)
if mibBuilder.loadTexts:
    sysDevFilterToRuleBindingTable.setStatus("mandatory")
_SysDevFilterToRuleBindingTableEntry_Object = MibTableRow
sysDevFilterToRuleBindingTableEntry = _SysDevFilterToRuleBindingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 8, 1)
)
sysDevFilterToRuleBindingTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevFilterIndex"),
    (0, "PDN-FILTER-MIB", "sysDevFilterToRuleBindingIndex"),
)
if mibBuilder.loadTexts:
    sysDevFilterToRuleBindingTableEntry.setStatus("mandatory")
_SysDevFilterToRuleBindingIndex_Type = Integer32
_SysDevFilterToRuleBindingIndex_Object = MibTableColumn
sysDevFilterToRuleBindingIndex = _SysDevFilterToRuleBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 8, 1, 1),
    _SysDevFilterToRuleBindingIndex_Type()
)
sysDevFilterToRuleBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevFilterToRuleBindingIndex.setStatus("mandatory")
_SysDevFilterToRulePriority_Type = Integer32
_SysDevFilterToRulePriority_Object = MibTableColumn
sysDevFilterToRulePriority = _SysDevFilterToRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 8, 1, 2),
    _SysDevFilterToRulePriority_Type()
)
sysDevFilterToRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterToRulePriority.setStatus("mandatory")
_SysDevFilterToRuleBindingRowStatus_Type = RowStatus
_SysDevFilterToRuleBindingRowStatus_Object = MibTableColumn
sysDevFilterToRuleBindingRowStatus = _SysDevFilterToRuleBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 8, 1, 3),
    _SysDevFilterToRuleBindingRowStatus_Type()
)
sysDevFilterToRuleBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevFilterToRuleBindingRowStatus.setStatus("mandatory")
_SysDevL3FilterRuleConfigTable_Object = MibTable
sysDevL3FilterRuleConfigTable = _SysDevL3FilterRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9)
)
if mibBuilder.loadTexts:
    sysDevL3FilterRuleConfigTable.setStatus("mandatory")
_SysDevL3FilterRuleConfigTableEntry_Object = MibTableRow
sysDevL3FilterRuleConfigTableEntry = _SysDevL3FilterRuleConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1)
)
sysDevL3FilterRuleConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevL3FilterRuleIndex"),
)
if mibBuilder.loadTexts:
    sysDevL3FilterRuleConfigTableEntry.setStatus("mandatory")
_SysDevL3FilterRuleIndex_Type = Integer32
_SysDevL3FilterRuleIndex_Object = MibTableColumn
sysDevL3FilterRuleIndex = _SysDevL3FilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 1),
    _SysDevL3FilterRuleIndex_Type()
)
sysDevL3FilterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleIndex.setStatus("mandatory")
_SysDevL3FilterRuleName_Type = DisplayString
_SysDevL3FilterRuleName_Object = MibTableColumn
sysDevL3FilterRuleName = _SysDevL3FilterRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 2),
    _SysDevL3FilterRuleName_Type()
)
sysDevL3FilterRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleName.setStatus("mandatory")
_SysDevL3FilterRuleSrcAddress_Type = IpAddress
_SysDevL3FilterRuleSrcAddress_Object = MibTableColumn
sysDevL3FilterRuleSrcAddress = _SysDevL3FilterRuleSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 3),
    _SysDevL3FilterRuleSrcAddress_Type()
)
sysDevL3FilterRuleSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleSrcAddress.setStatus("mandatory")
_SysDevL3FilterRuleSrcAddrMask_Type = IpAddress
_SysDevL3FilterRuleSrcAddrMask_Object = MibTableColumn
sysDevL3FilterRuleSrcAddrMask = _SysDevL3FilterRuleSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 4),
    _SysDevL3FilterRuleSrcAddrMask_Type()
)
sysDevL3FilterRuleSrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleSrcAddrMask.setStatus("mandatory")


class _SysDevL3FilterRuleSrcAddrAction_Type(Integer32):
    """Custom type sysDevL3FilterRuleSrcAddrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("none", 3))
    )


_SysDevL3FilterRuleSrcAddrAction_Type.__name__ = "Integer32"
_SysDevL3FilterRuleSrcAddrAction_Object = MibTableColumn
sysDevL3FilterRuleSrcAddrAction = _SysDevL3FilterRuleSrcAddrAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 5),
    _SysDevL3FilterRuleSrcAddrAction_Type()
)
sysDevL3FilterRuleSrcAddrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleSrcAddrAction.setStatus("mandatory")
_SysDevL3FilterRuleSrcPortNum_Type = Integer32
_SysDevL3FilterRuleSrcPortNum_Object = MibTableColumn
sysDevL3FilterRuleSrcPortNum = _SysDevL3FilterRuleSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 6),
    _SysDevL3FilterRuleSrcPortNum_Type()
)
sysDevL3FilterRuleSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleSrcPortNum.setStatus("mandatory")
_SysDevL3FilterRuleMaxSrcPortNum_Type = Integer32
_SysDevL3FilterRuleMaxSrcPortNum_Object = MibTableColumn
sysDevL3FilterRuleMaxSrcPortNum = _SysDevL3FilterRuleMaxSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 7),
    _SysDevL3FilterRuleMaxSrcPortNum_Type()
)
sysDevL3FilterRuleMaxSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleMaxSrcPortNum.setStatus("mandatory")


class _SysDevL3FilterRuleSrcCompType_Type(Integer32):
    """Custom type sysDevL3FilterRuleSrcCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eq", 2),
          ("neq", 3),
          ("gt", 4),
          ("lt", 5),
          ("inRange", 6),
          ("outRange", 7))
    )


_SysDevL3FilterRuleSrcCompType_Type.__name__ = "Integer32"
_SysDevL3FilterRuleSrcCompType_Object = MibTableColumn
sysDevL3FilterRuleSrcCompType = _SysDevL3FilterRuleSrcCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 8),
    _SysDevL3FilterRuleSrcCompType_Type()
)
sysDevL3FilterRuleSrcCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleSrcCompType.setStatus("mandatory")
_SysDevL3FilterRuleDestAddress_Type = IpAddress
_SysDevL3FilterRuleDestAddress_Object = MibTableColumn
sysDevL3FilterRuleDestAddress = _SysDevL3FilterRuleDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 9),
    _SysDevL3FilterRuleDestAddress_Type()
)
sysDevL3FilterRuleDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleDestAddress.setStatus("mandatory")
_SysDevL3FilterRuleDestAddrMask_Type = IpAddress
_SysDevL3FilterRuleDestAddrMask_Object = MibTableColumn
sysDevL3FilterRuleDestAddrMask = _SysDevL3FilterRuleDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 10),
    _SysDevL3FilterRuleDestAddrMask_Type()
)
sysDevL3FilterRuleDestAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleDestAddrMask.setStatus("mandatory")


class _SysDevL3FilterRuleDestAddrAction_Type(Integer32):
    """Custom type sysDevL3FilterRuleDestAddrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("none", 3))
    )


_SysDevL3FilterRuleDestAddrAction_Type.__name__ = "Integer32"
_SysDevL3FilterRuleDestAddrAction_Object = MibTableColumn
sysDevL3FilterRuleDestAddrAction = _SysDevL3FilterRuleDestAddrAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 11),
    _SysDevL3FilterRuleDestAddrAction_Type()
)
sysDevL3FilterRuleDestAddrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleDestAddrAction.setStatus("mandatory")
_SysDevL3FilterRuleDestPortNum_Type = Integer32
_SysDevL3FilterRuleDestPortNum_Object = MibTableColumn
sysDevL3FilterRuleDestPortNum = _SysDevL3FilterRuleDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 12),
    _SysDevL3FilterRuleDestPortNum_Type()
)
sysDevL3FilterRuleDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleDestPortNum.setStatus("mandatory")
_SysDevL3FilterRuleMaxDestPortNum_Type = Integer32
_SysDevL3FilterRuleMaxDestPortNum_Object = MibTableColumn
sysDevL3FilterRuleMaxDestPortNum = _SysDevL3FilterRuleMaxDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 13),
    _SysDevL3FilterRuleMaxDestPortNum_Type()
)
sysDevL3FilterRuleMaxDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleMaxDestPortNum.setStatus("mandatory")


class _SysDevL3FilterRuleDestCompType_Type(Integer32):
    """Custom type sysDevL3FilterRuleDestCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eq", 2),
          ("neq", 3),
          ("gt", 4),
          ("lt", 5),
          ("inRange", 6),
          ("outRange", 7))
    )


_SysDevL3FilterRuleDestCompType_Type.__name__ = "Integer32"
_SysDevL3FilterRuleDestCompType_Object = MibTableColumn
sysDevL3FilterRuleDestCompType = _SysDevL3FilterRuleDestCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 14),
    _SysDevL3FilterRuleDestCompType_Type()
)
sysDevL3FilterRuleDestCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleDestCompType.setStatus("mandatory")


class _SysDevL3FilterRuleProtocolTypeUdp_Type(Integer32):
    """Custom type sysDevL3FilterRuleProtocolTypeUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("none", 3))
    )


_SysDevL3FilterRuleProtocolTypeUdp_Type.__name__ = "Integer32"
_SysDevL3FilterRuleProtocolTypeUdp_Object = MibTableColumn
sysDevL3FilterRuleProtocolTypeUdp = _SysDevL3FilterRuleProtocolTypeUdp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 15),
    _SysDevL3FilterRuleProtocolTypeUdp_Type()
)
sysDevL3FilterRuleProtocolTypeUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleProtocolTypeUdp.setStatus("mandatory")


class _SysDevL3FilterRuleProtocolTypeTcp_Type(Integer32):
    """Custom type sysDevL3FilterRuleProtocolTypeTcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("none", 3))
    )


_SysDevL3FilterRuleProtocolTypeTcp_Type.__name__ = "Integer32"
_SysDevL3FilterRuleProtocolTypeTcp_Object = MibTableColumn
sysDevL3FilterRuleProtocolTypeTcp = _SysDevL3FilterRuleProtocolTypeTcp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 16),
    _SysDevL3FilterRuleProtocolTypeTcp_Type()
)
sysDevL3FilterRuleProtocolTypeTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleProtocolTypeTcp.setStatus("mandatory")


class _SysDevL3FilterRuleProtocolTypeIcmp_Type(Integer32):
    """Custom type sysDevL3FilterRuleProtocolTypeIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("none", 3))
    )


_SysDevL3FilterRuleProtocolTypeIcmp_Type.__name__ = "Integer32"
_SysDevL3FilterRuleProtocolTypeIcmp_Object = MibTableColumn
sysDevL3FilterRuleProtocolTypeIcmp = _SysDevL3FilterRuleProtocolTypeIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 17),
    _SysDevL3FilterRuleProtocolTypeIcmp_Type()
)
sysDevL3FilterRuleProtocolTypeIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleProtocolTypeIcmp.setStatus("mandatory")
_SysDevL3FilterRuleRowStatus_Type = RowStatus
_SysDevL3FilterRuleRowStatus_Object = MibTableColumn
sysDevL3FilterRuleRowStatus = _SysDevL3FilterRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 9, 1, 18),
    _SysDevL3FilterRuleRowStatus_Type()
)
sysDevL3FilterRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleRowStatus.setStatus("mandatory")
_SysDevL3FilterRuleIndexNext_Type = Integer32
_SysDevL3FilterRuleIndexNext_Object = MibScalar
sysDevL3FilterRuleIndexNext = _SysDevL3FilterRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 10),
    _SysDevL3FilterRuleIndexNext_Type()
)
sysDevL3FilterRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevL3FilterRuleIndexNext.setStatus("mandatory")
_SysDevIpFilter_ObjectIdentity = ObjectIdentity
sysDevIpFilter = _SysDevIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2)
)
_SysDevIpFilterConfigTable_Object = MibTable
sysDevIpFilterConfigTable = _SysDevIpFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysDevIpFilterConfigTable.setStatus("mandatory")
_SysDevIpFilterConfigTableEntry_Object = MibTableRow
sysDevIpFilterConfigTableEntry = _SysDevIpFilterConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1)
)
sysDevIpFilterConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevIpFilterName"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterConfigTableEntry.setStatus("mandatory")


class _SysDevIpFilterName_Type(DisplayString):
    """Custom type sysDevIpFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpFilterName_Type.__name__ = "DisplayString"
_SysDevIpFilterName_Object = MibTableColumn
sysDevIpFilterName = _SysDevIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 1),
    _SysDevIpFilterName_Type()
)
sysDevIpFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterName.setStatus("mandatory")


class _SysDevIpDefFilterAction_Type(Integer32):
    """Custom type sysDevIpDefFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("delete", 3))
    )


_SysDevIpDefFilterAction_Type.__name__ = "Integer32"
_SysDevIpDefFilterAction_Object = MibTableColumn
sysDevIpDefFilterAction = _SysDevIpDefFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 2),
    _SysDevIpDefFilterAction_Type()
)
sysDevIpDefFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpDefFilterAction.setStatus("mandatory")
_SysDevIpFilterNumOfDynamicRules_Type = Integer32
_SysDevIpFilterNumOfDynamicRules_Object = MibTableColumn
sysDevIpFilterNumOfDynamicRules = _SysDevIpFilterNumOfDynamicRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 3),
    _SysDevIpFilterNumOfDynamicRules_Type()
)
sysDevIpFilterNumOfDynamicRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterNumOfDynamicRules.setStatus("mandatory")
_SysDevIpFilterNumOfStaticRules_Type = Integer32
_SysDevIpFilterNumOfStaticRules_Object = MibTableColumn
sysDevIpFilterNumOfStaticRules = _SysDevIpFilterNumOfStaticRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 4),
    _SysDevIpFilterNumOfStaticRules_Type()
)
sysDevIpFilterNumOfStaticRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterNumOfStaticRules.setStatus("mandatory")
_SysDevIpFilterRefCount_Type = Integer32
_SysDevIpFilterRefCount_Object = MibTableColumn
sysDevIpFilterRefCount = _SysDevIpFilterRefCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 5),
    _SysDevIpFilterRefCount_Type()
)
sysDevIpFilterRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterRefCount.setStatus("mandatory")


class _SysDevIpFilterTcpAckFilterAction_Type(Integer32):
    """Custom type sysDevIpFilterTcpAckFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("noOp", 3))
    )


_SysDevIpFilterTcpAckFilterAction_Type.__name__ = "Integer32"
_SysDevIpFilterTcpAckFilterAction_Object = MibTableColumn
sysDevIpFilterTcpAckFilterAction = _SysDevIpFilterTcpAckFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 6),
    _SysDevIpFilterTcpAckFilterAction_Type()
)
sysDevIpFilterTcpAckFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterTcpAckFilterAction.setStatus("mandatory")


class _SysDevIpFilterDhcpFilterAction_Type(Integer32):
    """Custom type sysDevIpFilterDhcpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2),
          ("noOp", 3))
    )


_SysDevIpFilterDhcpFilterAction_Type.__name__ = "Integer32"
_SysDevIpFilterDhcpFilterAction_Object = MibTableColumn
sysDevIpFilterDhcpFilterAction = _SysDevIpFilterDhcpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 7),
    _SysDevIpFilterDhcpFilterAction_Type()
)
sysDevIpFilterDhcpFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterDhcpFilterAction.setStatus("mandatory")
_SysDevIpFilterRowStatus_Type = RowStatus
_SysDevIpFilterRowStatus_Object = MibTableColumn
sysDevIpFilterRowStatus = _SysDevIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 8),
    _SysDevIpFilterRowStatus_Type()
)
sysDevIpFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRowStatus.setStatus("mandatory")
_SysDevIpFilterRuleConfigTable_Object = MibTable
sysDevIpFilterRuleConfigTable = _SysDevIpFilterRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sysDevIpFilterRuleConfigTable.setStatus("deprecated")
_SysDevIpFilterRuleConfigTableEntry_Object = MibTableRow
sysDevIpFilterRuleConfigTableEntry = _SysDevIpFilterRuleConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1)
)
sysDevIpFilterRuleConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevIpRuleFilterName"),
    (0, "PDN-FILTER-MIB", "sysDevIpFilterRuleNumber"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterRuleConfigTableEntry.setStatus("deprecated")


class _SysDevIpRuleFilterName_Type(DisplayString):
    """Custom type sysDevIpRuleFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpRuleFilterName_Type.__name__ = "DisplayString"
_SysDevIpRuleFilterName_Object = MibTableColumn
sysDevIpRuleFilterName = _SysDevIpRuleFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 1),
    _SysDevIpRuleFilterName_Type()
)
sysDevIpRuleFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpRuleFilterName.setStatus("deprecated")


class _SysDevIpFilterRuleNumber_Type(Integer32):
    """Custom type sysDevIpFilterRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_SysDevIpFilterRuleNumber_Type.__name__ = "Integer32"
_SysDevIpFilterRuleNumber_Object = MibTableColumn
sysDevIpFilterRuleNumber = _SysDevIpFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 2),
    _SysDevIpFilterRuleNumber_Type()
)
sysDevIpFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleNumber.setStatus("deprecated")
_SysDevIpFilterRuleSrcAddress_Type = IpAddress
_SysDevIpFilterRuleSrcAddress_Object = MibTableColumn
sysDevIpFilterRuleSrcAddress = _SysDevIpFilterRuleSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 3),
    _SysDevIpFilterRuleSrcAddress_Type()
)
sysDevIpFilterRuleSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcAddress.setStatus("deprecated")
_SysDevIpFilterRuleSrcAddrMask_Type = IpAddress
_SysDevIpFilterRuleSrcAddrMask_Object = MibTableColumn
sysDevIpFilterRuleSrcAddrMask = _SysDevIpFilterRuleSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 4),
    _SysDevIpFilterRuleSrcAddrMask_Type()
)
sysDevIpFilterRuleSrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcAddrMask.setStatus("deprecated")


class _SysDevIpFilterRuleSrcAddrCompEnable_Type(Integer32):
    """Custom type sysDevIpFilterRuleSrcAddrCompEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("noOp", 3))
    )


_SysDevIpFilterRuleSrcAddrCompEnable_Type.__name__ = "Integer32"
_SysDevIpFilterRuleSrcAddrCompEnable_Object = MibTableColumn
sysDevIpFilterRuleSrcAddrCompEnable = _SysDevIpFilterRuleSrcAddrCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 5),
    _SysDevIpFilterRuleSrcAddrCompEnable_Type()
)
sysDevIpFilterRuleSrcAddrCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcAddrCompEnable.setStatus("deprecated")


class _SysDevIpFilterRuleSrcPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleSrcPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleSrcPortNum_Object = MibTableColumn
sysDevIpFilterRuleSrcPortNum = _SysDevIpFilterRuleSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 6),
    _SysDevIpFilterRuleSrcPortNum_Type()
)
sysDevIpFilterRuleSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcPortNum.setStatus("deprecated")


class _SysDevIpFilterRuleMaxSrcPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleMaxSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleMaxSrcPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleMaxSrcPortNum_Object = MibTableColumn
sysDevIpFilterRuleMaxSrcPortNum = _SysDevIpFilterRuleMaxSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 7),
    _SysDevIpFilterRuleMaxSrcPortNum_Type()
)
sysDevIpFilterRuleMaxSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleMaxSrcPortNum.setStatus("deprecated")


class _SysDevIpFilterRuleSrcCompType_Type(Integer32):
    """Custom type sysDevIpFilterRuleSrcCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eq", 2),
          ("neq", 3),
          ("gt", 4),
          ("lt", 5),
          ("inRange", 6),
          ("outRange", 7))
    )


_SysDevIpFilterRuleSrcCompType_Type.__name__ = "Integer32"
_SysDevIpFilterRuleSrcCompType_Object = MibTableColumn
sysDevIpFilterRuleSrcCompType = _SysDevIpFilterRuleSrcCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 8),
    _SysDevIpFilterRuleSrcCompType_Type()
)
sysDevIpFilterRuleSrcCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcCompType.setStatus("deprecated")
_SysDevIpFilterRuleDestAddress_Type = IpAddress
_SysDevIpFilterRuleDestAddress_Object = MibTableColumn
sysDevIpFilterRuleDestAddress = _SysDevIpFilterRuleDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 9),
    _SysDevIpFilterRuleDestAddress_Type()
)
sysDevIpFilterRuleDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestAddress.setStatus("deprecated")
_SysDevIpFilterRuleDestAddrMask_Type = IpAddress
_SysDevIpFilterRuleDestAddrMask_Object = MibTableColumn
sysDevIpFilterRuleDestAddrMask = _SysDevIpFilterRuleDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 10),
    _SysDevIpFilterRuleDestAddrMask_Type()
)
sysDevIpFilterRuleDestAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestAddrMask.setStatus("deprecated")


class _SysDevIpFilterRuleDestAddrCompEnable_Type(Integer32):
    """Custom type sysDevIpFilterRuleDestAddrCompEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("noOp", 3))
    )


_SysDevIpFilterRuleDestAddrCompEnable_Type.__name__ = "Integer32"
_SysDevIpFilterRuleDestAddrCompEnable_Object = MibTableColumn
sysDevIpFilterRuleDestAddrCompEnable = _SysDevIpFilterRuleDestAddrCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 11),
    _SysDevIpFilterRuleDestAddrCompEnable_Type()
)
sysDevIpFilterRuleDestAddrCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestAddrCompEnable.setStatus("deprecated")


class _SysDevIpFilterRuleDestPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleDestPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleDestPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleDestPortNum_Object = MibTableColumn
sysDevIpFilterRuleDestPortNum = _SysDevIpFilterRuleDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 12),
    _SysDevIpFilterRuleDestPortNum_Type()
)
sysDevIpFilterRuleDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestPortNum.setStatus("deprecated")


class _SysDevIpFilterRuleMaxDestPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleMaxDestPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleMaxDestPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleMaxDestPortNum_Object = MibTableColumn
sysDevIpFilterRuleMaxDestPortNum = _SysDevIpFilterRuleMaxDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 13),
    _SysDevIpFilterRuleMaxDestPortNum_Type()
)
sysDevIpFilterRuleMaxDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleMaxDestPortNum.setStatus("deprecated")


class _SysDevIpFilterRuleDestCompType_Type(Integer32):
    """Custom type sysDevIpFilterRuleDestCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eq", 2),
          ("neq", 3),
          ("gt", 4),
          ("lt", 5),
          ("inRange", 6),
          ("outRange", 7))
    )


_SysDevIpFilterRuleDestCompType_Type.__name__ = "Integer32"
_SysDevIpFilterRuleDestCompType_Object = MibTableColumn
sysDevIpFilterRuleDestCompType = _SysDevIpFilterRuleDestCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 14),
    _SysDevIpFilterRuleDestCompType_Type()
)
sysDevIpFilterRuleDestCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestCompType.setStatus("deprecated")


class _SysDevIpFilterRuleType_Type(Integer32):
    """Custom type sysDevIpFilterRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_SysDevIpFilterRuleType_Type.__name__ = "Integer32"
_SysDevIpFilterRuleType_Object = MibTableColumn
sysDevIpFilterRuleType = _SysDevIpFilterRuleType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 15),
    _SysDevIpFilterRuleType_Type()
)
sysDevIpFilterRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleType.setStatus("deprecated")


class _SysDevIpFilterRuleProtocolTypeUdp_Type(Integer32):
    """Custom type sysDevIpFilterRuleProtocolTypeUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_SysDevIpFilterRuleProtocolTypeUdp_Type.__name__ = "Integer32"
_SysDevIpFilterRuleProtocolTypeUdp_Object = MibTableColumn
sysDevIpFilterRuleProtocolTypeUdp = _SysDevIpFilterRuleProtocolTypeUdp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 16),
    _SysDevIpFilterRuleProtocolTypeUdp_Type()
)
sysDevIpFilterRuleProtocolTypeUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleProtocolTypeUdp.setStatus("deprecated")


class _SysDevIpFilterRuleProtocolTypeTcp_Type(Integer32):
    """Custom type sysDevIpFilterRuleProtocolTypeTcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_SysDevIpFilterRuleProtocolTypeTcp_Type.__name__ = "Integer32"
_SysDevIpFilterRuleProtocolTypeTcp_Object = MibTableColumn
sysDevIpFilterRuleProtocolTypeTcp = _SysDevIpFilterRuleProtocolTypeTcp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 17),
    _SysDevIpFilterRuleProtocolTypeTcp_Type()
)
sysDevIpFilterRuleProtocolTypeTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleProtocolTypeTcp.setStatus("deprecated")


class _SysDevIpFilterRuleProtocolTypeIcmp_Type(Integer32):
    """Custom type sysDevIpFilterRuleProtocolTypeIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_SysDevIpFilterRuleProtocolTypeIcmp_Type.__name__ = "Integer32"
_SysDevIpFilterRuleProtocolTypeIcmp_Object = MibTableColumn
sysDevIpFilterRuleProtocolTypeIcmp = _SysDevIpFilterRuleProtocolTypeIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 18),
    _SysDevIpFilterRuleProtocolTypeIcmp_Type()
)
sysDevIpFilterRuleProtocolTypeIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleProtocolTypeIcmp.setStatus("deprecated")
_SysDevIpFilterRuleRowStatus_Type = RowStatus
_SysDevIpFilterRuleRowStatus_Object = MibTableColumn
sysDevIpFilterRuleRowStatus = _SysDevIpFilterRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 19),
    _SysDevIpFilterRuleRowStatus_Type()
)
sysDevIpFilterRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleRowStatus.setStatus("deprecated")
_SysDevMaxNumOfInputIpFilters_Type = Integer32
_SysDevMaxNumOfInputIpFilters_Object = MibScalar
sysDevMaxNumOfInputIpFilters = _SysDevMaxNumOfInputIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 3),
    _SysDevMaxNumOfInputIpFilters_Type()
)
sysDevMaxNumOfInputIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevMaxNumOfInputIpFilters.setStatus("mandatory")
_SysDevMaxNumOfOutputIpFilters_Type = Integer32
_SysDevMaxNumOfOutputIpFilters_Object = MibScalar
sysDevMaxNumOfOutputIpFilters = _SysDevMaxNumOfOutputIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 4),
    _SysDevMaxNumOfOutputIpFilters_Type()
)
sysDevMaxNumOfOutputIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevMaxNumOfOutputIpFilters.setStatus("mandatory")
_SysDevIpFilterBindingTable_Object = MibTable
sysDevIpFilterBindingTable = _SysDevIpFilterBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5)
)
if mibBuilder.loadTexts:
    sysDevIpFilterBindingTable.setStatus("mandatory")
_SysDevIpFilterBindingTableEntry_Object = MibTableRow
sysDevIpFilterBindingTableEntry = _SysDevIpFilterBindingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1)
)
sysDevIpFilterBindingTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-FILTER-MIB", "sysDevIpBindingFilterName"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterBindingTableEntry.setStatus("mandatory")


class _SysDevIpBindingFilterName_Type(DisplayString):
    """Custom type sysDevIpBindingFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpBindingFilterName_Type.__name__ = "DisplayString"
_SysDevIpBindingFilterName_Object = MibTableColumn
sysDevIpBindingFilterName = _SysDevIpBindingFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1, 1),
    _SysDevIpBindingFilterName_Type()
)
sysDevIpBindingFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpBindingFilterName.setStatus("mandatory")


class _SysDevIpBindingFilterType_Type(Integer32):
    """Custom type sysDevIpBindingFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputFilter", 1),
          ("outputFilter", 2),
          ("inputOutputFilter", 3))
    )


_SysDevIpBindingFilterType_Type.__name__ = "Integer32"
_SysDevIpBindingFilterType_Object = MibTableColumn
sysDevIpBindingFilterType = _SysDevIpBindingFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1, 2),
    _SysDevIpBindingFilterType_Type()
)
sysDevIpBindingFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpBindingFilterType.setStatus("mandatory")
_SysDevIpBindingFilterRowStatus_Type = RowStatus
_SysDevIpBindingFilterRowStatus_Object = MibTableColumn
sysDevIpBindingFilterRowStatus = _SysDevIpBindingFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1, 3),
    _SysDevIpBindingFilterRowStatus_Type()
)
sysDevIpBindingFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpBindingFilterRowStatus.setStatus("mandatory")
_SysDevIpFilterSNBindingTable_Object = MibTable
sysDevIpFilterSNBindingTable = _SysDevIpFilterSNBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sysDevIpFilterSNBindingTable.setStatus("mandatory")
_SysDevIpFilterSNBindingTableEntry_Object = MibTableRow
sysDevIpFilterSNBindingTableEntry = _SysDevIpFilterSNBindingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1)
)
sysDevIpFilterSNBindingTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-FILTER-MIB", "sysDevIpSNBindingVnidId"),
    (0, "PDN-FILTER-MIB", "sysDevIpSNBindingFilterName"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterSNBindingTableEntry.setStatus("mandatory")
_SysDevIpSNBindingVnidId_Type = VnidRange
_SysDevIpSNBindingVnidId_Object = MibTableColumn
sysDevIpSNBindingVnidId = _SysDevIpSNBindingVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 1),
    _SysDevIpSNBindingVnidId_Type()
)
sysDevIpSNBindingVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpSNBindingVnidId.setStatus("mandatory")


class _SysDevIpSNBindingFilterName_Type(DisplayString):
    """Custom type sysDevIpSNBindingFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpSNBindingFilterName_Type.__name__ = "DisplayString"
_SysDevIpSNBindingFilterName_Object = MibTableColumn
sysDevIpSNBindingFilterName = _SysDevIpSNBindingFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 2),
    _SysDevIpSNBindingFilterName_Type()
)
sysDevIpSNBindingFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpSNBindingFilterName.setStatus("mandatory")


class _SysDevIpSNBindingFilterType_Type(Integer32):
    """Custom type sysDevIpSNBindingFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputFilter", 1),
          ("outputFilter", 2),
          ("inputOutputFilter", 3))
    )


_SysDevIpSNBindingFilterType_Type.__name__ = "Integer32"
_SysDevIpSNBindingFilterType_Object = MibTableColumn
sysDevIpSNBindingFilterType = _SysDevIpSNBindingFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 3),
    _SysDevIpSNBindingFilterType_Type()
)
sysDevIpSNBindingFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpSNBindingFilterType.setStatus("mandatory")
_SysDevIpSNBindingFilterRowStatus_Type = RowStatus
_SysDevIpSNBindingFilterRowStatus_Object = MibTableColumn
sysDevIpSNBindingFilterRowStatus = _SysDevIpSNBindingFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 4),
    _SysDevIpSNBindingFilterRowStatus_Type()
)
sysDevIpSNBindingFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpSNBindingFilterRowStatus.setStatus("mandatory")
_SysDevIpInputPacketsFiltered_Type = Counter32
_SysDevIpInputPacketsFiltered_Object = MibScalar
sysDevIpInputPacketsFiltered = _SysDevIpInputPacketsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 7),
    _SysDevIpInputPacketsFiltered_Type()
)
sysDevIpInputPacketsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpInputPacketsFiltered.setStatus("mandatory")
_SysDevIpOutputPacketsFiltered_Type = Counter32
_SysDevIpOutputPacketsFiltered_Object = MibScalar
sysDevIpOutputPacketsFiltered = _SysDevIpOutputPacketsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 8),
    _SysDevIpOutputPacketsFiltered_Type()
)
sysDevIpOutputPacketsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpOutputPacketsFiltered.setStatus("mandatory")
_SysDevFilterMIBTraps_ObjectIdentity = ObjectIdentity
sysDevFilterMIBTraps = _SysDevFilterMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 2)
)

# Managed Objects groups


# Notification objects

sysDevSNInjectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 2, 0, 22)
)
sysDevSNInjectionFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionVnid"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionType"))
)
if mibBuilder.loadTexts:
    sysDevSNInjectionFailureTrap.setStatus(
        ""
    )

sysDevSNInjectionIncompatibleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 2, 0, 23)
)
sysDevSNInjectionIncompatibleTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionVnid"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionType"))
)
if mibBuilder.loadTexts:
    sysDevSNInjectionIncompatibleTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-FILTER-MIB",
    **{"sysDevFilterMIBObjects": sysDevFilterMIBObjects,
       "sysDevFilter": sysDevFilter,
       "sysDevSNInjectionType": sysDevSNInjectionType,
       "sysDevSNInjectionVnid": sysDevSNInjectionVnid,
       "sysDevFilterConfigTable": sysDevFilterConfigTable,
       "sysDevFilterConfigTableEntry": sysDevFilterConfigTableEntry,
       "sysDevFilterIndex": sysDevFilterIndex,
       "sysDevFilterName": sysDevFilterName,
       "sysDevFilterType": sysDevFilterType,
       "sysDevDefFilterAction": sysDevDefFilterAction,
       "sysDevFilterNumOfDynamicRules": sysDevFilterNumOfDynamicRules,
       "sysDevFilterNumOfStaticRules": sysDevFilterNumOfStaticRules,
       "sysDevFilterRefCount": sysDevFilterRefCount,
       "sysDevFilterRowStatus": sysDevFilterRowStatus,
       "sysDevL2FilterRuleConfigTable": sysDevL2FilterRuleConfigTable,
       "sysDevL2FilterRuleConfigTableEntry": sysDevL2FilterRuleConfigTableEntry,
       "sysDevL2FilterRuleIndex": sysDevL2FilterRuleIndex,
       "sysDevL2FilterRuleName": sysDevL2FilterRuleName,
       "sysDevL2FilterRuleEtherFrameType": sysDevL2FilterRuleEtherFrameType,
       "sysDevL2FilterRuleEtherType": sysDevL2FilterRuleEtherType,
       "sysDevL2FilterRuleEtherTypeRangeStarts": sysDevL2FilterRuleEtherTypeRangeStarts,
       "sysDevL2FilterRuleEtherTypeRangeEnds": sysDevL2FilterRuleEtherTypeRangeEnds,
       "sysDevL2FilterRuleAction": sysDevL2FilterRuleAction,
       "sysDevL2FilterRuleRowStatus": sysDevL2FilterRuleRowStatus,
       "sysDevFilterBindingTable": sysDevFilterBindingTable,
       "sysDevFilterBindingTableEntry": sysDevFilterBindingTableEntry,
       "sysDevFilterBindingIndex": sysDevFilterBindingIndex,
       "sysDevFilterBindingDirection": sysDevFilterBindingDirection,
       "sysDevFilterBindingAdminStatus": sysDevFilterBindingAdminStatus,
       "sysDevFilterBindingOperStatus": sysDevFilterBindingOperStatus,
       "sysDevFilterBindingRowStatus": sysDevFilterBindingRowStatus,
       "sysDevFilterIndexNext": sysDevFilterIndexNext,
       "sysDevL2FilterRuleIndexNext": sysDevL2FilterRuleIndexNext,
       "sysDevFilterToRuleBindingTable": sysDevFilterToRuleBindingTable,
       "sysDevFilterToRuleBindingTableEntry": sysDevFilterToRuleBindingTableEntry,
       "sysDevFilterToRuleBindingIndex": sysDevFilterToRuleBindingIndex,
       "sysDevFilterToRulePriority": sysDevFilterToRulePriority,
       "sysDevFilterToRuleBindingRowStatus": sysDevFilterToRuleBindingRowStatus,
       "sysDevL3FilterRuleConfigTable": sysDevL3FilterRuleConfigTable,
       "sysDevL3FilterRuleConfigTableEntry": sysDevL3FilterRuleConfigTableEntry,
       "sysDevL3FilterRuleIndex": sysDevL3FilterRuleIndex,
       "sysDevL3FilterRuleName": sysDevL3FilterRuleName,
       "sysDevL3FilterRuleSrcAddress": sysDevL3FilterRuleSrcAddress,
       "sysDevL3FilterRuleSrcAddrMask": sysDevL3FilterRuleSrcAddrMask,
       "sysDevL3FilterRuleSrcAddrAction": sysDevL3FilterRuleSrcAddrAction,
       "sysDevL3FilterRuleSrcPortNum": sysDevL3FilterRuleSrcPortNum,
       "sysDevL3FilterRuleMaxSrcPortNum": sysDevL3FilterRuleMaxSrcPortNum,
       "sysDevL3FilterRuleSrcCompType": sysDevL3FilterRuleSrcCompType,
       "sysDevL3FilterRuleDestAddress": sysDevL3FilterRuleDestAddress,
       "sysDevL3FilterRuleDestAddrMask": sysDevL3FilterRuleDestAddrMask,
       "sysDevL3FilterRuleDestAddrAction": sysDevL3FilterRuleDestAddrAction,
       "sysDevL3FilterRuleDestPortNum": sysDevL3FilterRuleDestPortNum,
       "sysDevL3FilterRuleMaxDestPortNum": sysDevL3FilterRuleMaxDestPortNum,
       "sysDevL3FilterRuleDestCompType": sysDevL3FilterRuleDestCompType,
       "sysDevL3FilterRuleProtocolTypeUdp": sysDevL3FilterRuleProtocolTypeUdp,
       "sysDevL3FilterRuleProtocolTypeTcp": sysDevL3FilterRuleProtocolTypeTcp,
       "sysDevL3FilterRuleProtocolTypeIcmp": sysDevL3FilterRuleProtocolTypeIcmp,
       "sysDevL3FilterRuleRowStatus": sysDevL3FilterRuleRowStatus,
       "sysDevL3FilterRuleIndexNext": sysDevL3FilterRuleIndexNext,
       "sysDevIpFilter": sysDevIpFilter,
       "sysDevIpFilterConfigTable": sysDevIpFilterConfigTable,
       "sysDevIpFilterConfigTableEntry": sysDevIpFilterConfigTableEntry,
       "sysDevIpFilterName": sysDevIpFilterName,
       "sysDevIpDefFilterAction": sysDevIpDefFilterAction,
       "sysDevIpFilterNumOfDynamicRules": sysDevIpFilterNumOfDynamicRules,
       "sysDevIpFilterNumOfStaticRules": sysDevIpFilterNumOfStaticRules,
       "sysDevIpFilterRefCount": sysDevIpFilterRefCount,
       "sysDevIpFilterTcpAckFilterAction": sysDevIpFilterTcpAckFilterAction,
       "sysDevIpFilterDhcpFilterAction": sysDevIpFilterDhcpFilterAction,
       "sysDevIpFilterRowStatus": sysDevIpFilterRowStatus,
       "sysDevIpFilterRuleConfigTable": sysDevIpFilterRuleConfigTable,
       "sysDevIpFilterRuleConfigTableEntry": sysDevIpFilterRuleConfigTableEntry,
       "sysDevIpRuleFilterName": sysDevIpRuleFilterName,
       "sysDevIpFilterRuleNumber": sysDevIpFilterRuleNumber,
       "sysDevIpFilterRuleSrcAddress": sysDevIpFilterRuleSrcAddress,
       "sysDevIpFilterRuleSrcAddrMask": sysDevIpFilterRuleSrcAddrMask,
       "sysDevIpFilterRuleSrcAddrCompEnable": sysDevIpFilterRuleSrcAddrCompEnable,
       "sysDevIpFilterRuleSrcPortNum": sysDevIpFilterRuleSrcPortNum,
       "sysDevIpFilterRuleMaxSrcPortNum": sysDevIpFilterRuleMaxSrcPortNum,
       "sysDevIpFilterRuleSrcCompType": sysDevIpFilterRuleSrcCompType,
       "sysDevIpFilterRuleDestAddress": sysDevIpFilterRuleDestAddress,
       "sysDevIpFilterRuleDestAddrMask": sysDevIpFilterRuleDestAddrMask,
       "sysDevIpFilterRuleDestAddrCompEnable": sysDevIpFilterRuleDestAddrCompEnable,
       "sysDevIpFilterRuleDestPortNum": sysDevIpFilterRuleDestPortNum,
       "sysDevIpFilterRuleMaxDestPortNum": sysDevIpFilterRuleMaxDestPortNum,
       "sysDevIpFilterRuleDestCompType": sysDevIpFilterRuleDestCompType,
       "sysDevIpFilterRuleType": sysDevIpFilterRuleType,
       "sysDevIpFilterRuleProtocolTypeUdp": sysDevIpFilterRuleProtocolTypeUdp,
       "sysDevIpFilterRuleProtocolTypeTcp": sysDevIpFilterRuleProtocolTypeTcp,
       "sysDevIpFilterRuleProtocolTypeIcmp": sysDevIpFilterRuleProtocolTypeIcmp,
       "sysDevIpFilterRuleRowStatus": sysDevIpFilterRuleRowStatus,
       "sysDevMaxNumOfInputIpFilters": sysDevMaxNumOfInputIpFilters,
       "sysDevMaxNumOfOutputIpFilters": sysDevMaxNumOfOutputIpFilters,
       "sysDevIpFilterBindingTable": sysDevIpFilterBindingTable,
       "sysDevIpFilterBindingTableEntry": sysDevIpFilterBindingTableEntry,
       "sysDevIpBindingFilterName": sysDevIpBindingFilterName,
       "sysDevIpBindingFilterType": sysDevIpBindingFilterType,
       "sysDevIpBindingFilterRowStatus": sysDevIpBindingFilterRowStatus,
       "sysDevIpFilterSNBindingTable": sysDevIpFilterSNBindingTable,
       "sysDevIpFilterSNBindingTableEntry": sysDevIpFilterSNBindingTableEntry,
       "sysDevIpSNBindingVnidId": sysDevIpSNBindingVnidId,
       "sysDevIpSNBindingFilterName": sysDevIpSNBindingFilterName,
       "sysDevIpSNBindingFilterType": sysDevIpSNBindingFilterType,
       "sysDevIpSNBindingFilterRowStatus": sysDevIpSNBindingFilterRowStatus,
       "sysDevIpInputPacketsFiltered": sysDevIpInputPacketsFiltered,
       "sysDevIpOutputPacketsFiltered": sysDevIpOutputPacketsFiltered,
       "sysDevFilterMIBTraps": sysDevFilterMIBTraps,
       "sysDevSNInjectionFailureTrap": sysDevSNInjectionFailureTrap,
       "sysDevSNInjectionIncompatibleTrap": sysDevSNInjectionIncompatibleTrap}
)
