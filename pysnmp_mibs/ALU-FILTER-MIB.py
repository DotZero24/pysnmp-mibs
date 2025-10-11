# SNMP MIB module (ALU-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-FILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:54:56 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tIPFilterParamsEntry,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "tIPFilterParamsEntry")

(TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TOperator) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TOperator")


# MODULE-IDENTITY

aluFilterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 14)
)
if mibBuilder.loadTexts:
    aluFilterMIBModule.setRevisions(
        ("2012-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluFilterID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AluEntryId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class AluFilterAction(TextualConvention, Integer32):
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
          ("forward", 2))
    )



class AluFilterScope(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("template", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AluFilterMIBConformance_ObjectIdentity = ObjectIdentity
aluFilterMIBConformance = _AluFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26)
)
_AluFilterMIBCompliances_ObjectIdentity = ObjectIdentity
aluFilterMIBCompliances = _AluFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 1)
)
_AluFilterMIBGroups_ObjectIdentity = ObjectIdentity
aluFilterMIBGroups = _AluFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 2)
)
_AluFilterObjects_ObjectIdentity = ObjectIdentity
aluFilterObjects = _AluFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16)
)
_AluVlanFilterTable_Object = MibTable
aluVlanFilterTable = _AluVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1)
)
if mibBuilder.loadTexts:
    aluVlanFilterTable.setStatus("current")
_AluVlanFilterEntry_Object = MibTableRow
aluVlanFilterEntry = _AluVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1)
)
aluVlanFilterEntry.setIndexNames(
    (0, "ALU-FILTER-MIB", "aluVlanFilterId"),
)
if mibBuilder.loadTexts:
    aluVlanFilterEntry.setStatus("current")


class _AluVlanFilterId_Type(AluFilterID):
    """Custom type aluVlanFilterId based on AluFilterID"""
    subtypeSpec = AluFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluVlanFilterId_Type.__name__ = "AluFilterID"
_AluVlanFilterId_Object = MibTableColumn
aluVlanFilterId = _AluVlanFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 1),
    _AluVlanFilterId_Type()
)
aluVlanFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluVlanFilterId.setStatus("current")
_AluVlanFilterRowStatus_Type = RowStatus
_AluVlanFilterRowStatus_Object = MibTableColumn
aluVlanFilterRowStatus = _AluVlanFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 2),
    _AluVlanFilterRowStatus_Type()
)
aluVlanFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterRowStatus.setStatus("current")


class _AluVlanFilterDescription_Type(TItemDescription):
    """Custom type aluVlanFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_AluVlanFilterDescription_Type.__name__ = "TItemDescription"
_AluVlanFilterDescription_Object = MibTableColumn
aluVlanFilterDescription = _AluVlanFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 3),
    _AluVlanFilterDescription_Type()
)
aluVlanFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterDescription.setStatus("current")


class _AluVlanFilterDefaultAction_Type(AluFilterAction):
    """Custom type aluVlanFilterDefaultAction based on AluFilterAction"""
    defaultValue = 1


_AluVlanFilterDefaultAction_Type.__name__ = "AluFilterAction"
_AluVlanFilterDefaultAction_Object = MibTableColumn
aluVlanFilterDefaultAction = _AluVlanFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 4),
    _AluVlanFilterDefaultAction_Type()
)
aluVlanFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterDefaultAction.setStatus("current")


class _AluVlanFilterName_Type(TLNamedItemOrEmpty):
    """Custom type aluVlanFilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_AluVlanFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_AluVlanFilterName_Object = MibTableColumn
aluVlanFilterName = _AluVlanFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 5),
    _AluVlanFilterName_Type()
)
aluVlanFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterName.setStatus("current")
_AluVlanFilterParamsTable_Object = MibTable
aluVlanFilterParamsTable = _AluVlanFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2)
)
if mibBuilder.loadTexts:
    aluVlanFilterParamsTable.setStatus("current")
_AluVlanFilterParamsEntry_Object = MibTableRow
aluVlanFilterParamsEntry = _AluVlanFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1)
)
aluVlanFilterParamsEntry.setIndexNames(
    (0, "ALU-FILTER-MIB", "aluVlanFilterId"),
    (0, "ALU-FILTER-MIB", "aluVlanFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    aluVlanFilterParamsEntry.setStatus("current")
_AluVlanFilterParamsIndex_Type = AluEntryId
_AluVlanFilterParamsIndex_Object = MibTableColumn
aluVlanFilterParamsIndex = _AluVlanFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 1),
    _AluVlanFilterParamsIndex_Type()
)
aluVlanFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluVlanFilterParamsIndex.setStatus("current")
_AluVlanFilterParamsRowStatus_Type = RowStatus
_AluVlanFilterParamsRowStatus_Object = MibTableColumn
aluVlanFilterParamsRowStatus = _AluVlanFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 2),
    _AluVlanFilterParamsRowStatus_Type()
)
aluVlanFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsRowStatus.setStatus("current")


class _AluVlanFilterParamsDescription_Type(TItemDescription):
    """Custom type aluVlanFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_AluVlanFilterParamsDescription_Type.__name__ = "TItemDescription"
_AluVlanFilterParamsDescription_Object = MibTableColumn
aluVlanFilterParamsDescription = _AluVlanFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 3),
    _AluVlanFilterParamsDescription_Type()
)
aluVlanFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsDescription.setStatus("current")


class _AluVlanFilterParamsAction_Type(AluFilterAction):
    """Custom type aluVlanFilterParamsAction based on AluFilterAction"""
    defaultValue = 1


_AluVlanFilterParamsAction_Type.__name__ = "AluFilterAction"
_AluVlanFilterParamsAction_Object = MibTableColumn
aluVlanFilterParamsAction = _AluVlanFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 4),
    _AluVlanFilterParamsAction_Type()
)
aluVlanFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsAction.setStatus("current")


class _AluVlanFilterParamsVlanValue1_Type(Integer32):
    """Custom type aluVlanFilterParamsVlanValue1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AluVlanFilterParamsVlanValue1_Type.__name__ = "Integer32"
_AluVlanFilterParamsVlanValue1_Object = MibTableColumn
aluVlanFilterParamsVlanValue1 = _AluVlanFilterParamsVlanValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 5),
    _AluVlanFilterParamsVlanValue1_Type()
)
aluVlanFilterParamsVlanValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsVlanValue1.setStatus("current")


class _AluVlanFilterParamsVlanValue2_Type(Integer32):
    """Custom type aluVlanFilterParamsVlanValue2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AluVlanFilterParamsVlanValue2_Type.__name__ = "Integer32"
_AluVlanFilterParamsVlanValue2_Object = MibTableColumn
aluVlanFilterParamsVlanValue2 = _AluVlanFilterParamsVlanValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 6),
    _AluVlanFilterParamsVlanValue2_Type()
)
aluVlanFilterParamsVlanValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsVlanValue2.setStatus("current")


class _AluVlanFilterParamsVlanOperator_Type(TOperator):
    """Custom type aluVlanFilterParamsVlanOperator based on TOperator"""
    defaultValue = 0


_AluVlanFilterParamsVlanOperator_Type.__name__ = "TOperator"
_AluVlanFilterParamsVlanOperator_Object = MibTableColumn
aluVlanFilterParamsVlanOperator = _AluVlanFilterParamsVlanOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 7),
    _AluVlanFilterParamsVlanOperator_Type()
)
aluVlanFilterParamsVlanOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsVlanOperator.setStatus("current")


class _AluVlanFilterParamsUntagged_Type(TruthValue):
    """Custom type aluVlanFilterParamsUntagged based on TruthValue"""
    defaultValue = 2


_AluVlanFilterParamsUntagged_Type.__name__ = "TruthValue"
_AluVlanFilterParamsUntagged_Object = MibTableColumn
aluVlanFilterParamsUntagged = _AluVlanFilterParamsUntagged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 8),
    _AluVlanFilterParamsUntagged_Type()
)
aluVlanFilterParamsUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVlanFilterParamsUntagged.setStatus("current")
_AluExtIPFilterParamsTable_Object = MibTable
aluExtIPFilterParamsTable = _AluExtIPFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3)
)
if mibBuilder.loadTexts:
    aluExtIPFilterParamsTable.setStatus("current")
_AluExtIPFilterParamsEntry_Object = MibTableRow
aluExtIPFilterParamsEntry = _AluExtIPFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    aluExtIPFilterParamsEntry.setStatus("current")


class _AluExtIPFilterParamsForwardFC_Type(TruthValue):
    """Custom type aluExtIPFilterParamsForwardFC based on TruthValue"""
    defaultValue = 2


_AluExtIPFilterParamsForwardFC_Type.__name__ = "TruthValue"
_AluExtIPFilterParamsForwardFC_Object = MibTableColumn
aluExtIPFilterParamsForwardFC = _AluExtIPFilterParamsForwardFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1, 1),
    _AluExtIPFilterParamsForwardFC_Type()
)
aluExtIPFilterParamsForwardFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtIPFilterParamsForwardFC.setStatus("current")


class _AluExtIPFilterParamsForwardFcType_Type(Integer32):
    """Custom type aluExtIPFilterParamsForwardFcType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7))
    )


_AluExtIPFilterParamsForwardFcType_Type.__name__ = "Integer32"
_AluExtIPFilterParamsForwardFcType_Object = MibTableColumn
aluExtIPFilterParamsForwardFcType = _AluExtIPFilterParamsForwardFcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1, 2),
    _AluExtIPFilterParamsForwardFcType_Type()
)
aluExtIPFilterParamsForwardFcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtIPFilterParamsForwardFcType.setStatus("current")


class _AluExtIPFilterParamsForwardFcPri_Type(Integer32):
    """Custom type aluExtIPFilterParamsForwardFcPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_AluExtIPFilterParamsForwardFcPri_Type.__name__ = "Integer32"
_AluExtIPFilterParamsForwardFcPri_Object = MibTableColumn
aluExtIPFilterParamsForwardFcPri = _AluExtIPFilterParamsForwardFcPri_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1, 3),
    _AluExtIPFilterParamsForwardFcPri_Type()
)
aluExtIPFilterParamsForwardFcPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtIPFilterParamsForwardFcPri.setStatus("current")
_AluVlanFilterNameTable_Object = MibTable
aluVlanFilterNameTable = _AluVlanFilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4)
)
if mibBuilder.loadTexts:
    aluVlanFilterNameTable.setStatus("current")
_AluVlanFilterNameEntry_Object = MibTableRow
aluVlanFilterNameEntry = _AluVlanFilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4, 1)
)
aluVlanFilterNameEntry.setIndexNames(
    (0, "ALU-FILTER-MIB", "aluVlanFilterName"),
)
if mibBuilder.loadTexts:
    aluVlanFilterNameEntry.setStatus("current")
_AluVlanFilterNameId_Type = AluFilterID
_AluVlanFilterNameId_Object = MibTableColumn
aluVlanFilterNameId = _AluVlanFilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4, 1, 1),
    _AluVlanFilterNameId_Type()
)
aluVlanFilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVlanFilterNameId.setStatus("current")
_AluVlanFilterNameRowStatus_Type = RowStatus
_AluVlanFilterNameRowStatus_Object = MibTableColumn
aluVlanFilterNameRowStatus = _AluVlanFilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4, 1, 2),
    _AluVlanFilterNameRowStatus_Type()
)
aluVlanFilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVlanFilterNameRowStatus.setStatus("current")
_AluFilterNotificationsPrefix_ObjectIdentity = ObjectIdentity
aluFilterNotificationsPrefix = _AluFilterNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 13)
)
_AlyFilterNotifications_ObjectIdentity = ObjectIdentity
alyFilterNotifications = _AlyFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 13, 0)
)
tIPFilterParamsEntry.registerAugmentions(
    ("ALU-FILTER-MIB",
     "aluExtIPFilterParamsEntry")
)
aluExtIPFilterParamsEntry.setIndexNames(*tIPFilterParamsEntry.getIndexNames())

# Managed Objects groups

aluFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 2, 1)
)
aluFilterGroup.setObjects(
      *(("ALU-FILTER-MIB", "aluVlanFilterRowStatus"),
        ("ALU-FILTER-MIB", "aluVlanFilterDescription"),
        ("ALU-FILTER-MIB", "aluVlanFilterDefaultAction"),
        ("ALU-FILTER-MIB", "aluVlanFilterName"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsRowStatus"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsDescription"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsAction"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsVlanValue1"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsVlanValue2"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsVlanOperator"),
        ("ALU-FILTER-MIB", "aluVlanFilterParamsUntagged"),
        ("ALU-FILTER-MIB", "aluExtIPFilterParamsForwardFC"),
        ("ALU-FILTER-MIB", "aluExtIPFilterParamsForwardFcType"),
        ("ALU-FILTER-MIB", "aluExtIPFilterParamsForwardFcPri"),
        ("ALU-FILTER-MIB", "aluVlanFilterNameId"),
        ("ALU-FILTER-MIB", "aluVlanFilterNameRowStatus"))
)
if mibBuilder.loadTexts:
    aluFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluFilter7705V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 1, 1)
)
aluFilter7705V6v0Compliance.setObjects(
    ("ALU-FILTER-MIB", "aluFilterGroup")
)
if mibBuilder.loadTexts:
    aluFilter7705V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-FILTER-MIB",
    **{"AluFilterID": AluFilterID,
       "AluEntryId": AluEntryId,
       "AluFilterAction": AluFilterAction,
       "AluFilterScope": AluFilterScope,
       "aluFilterMIBModule": aluFilterMIBModule,
       "aluFilterMIBConformance": aluFilterMIBConformance,
       "aluFilterMIBCompliances": aluFilterMIBCompliances,
       "aluFilter7705V6v0Compliance": aluFilter7705V6v0Compliance,
       "aluFilterMIBGroups": aluFilterMIBGroups,
       "aluFilterGroup": aluFilterGroup,
       "aluFilterObjects": aluFilterObjects,
       "aluVlanFilterTable": aluVlanFilterTable,
       "aluVlanFilterEntry": aluVlanFilterEntry,
       "aluVlanFilterId": aluVlanFilterId,
       "aluVlanFilterRowStatus": aluVlanFilterRowStatus,
       "aluVlanFilterDescription": aluVlanFilterDescription,
       "aluVlanFilterDefaultAction": aluVlanFilterDefaultAction,
       "aluVlanFilterName": aluVlanFilterName,
       "aluVlanFilterParamsTable": aluVlanFilterParamsTable,
       "aluVlanFilterParamsEntry": aluVlanFilterParamsEntry,
       "aluVlanFilterParamsIndex": aluVlanFilterParamsIndex,
       "aluVlanFilterParamsRowStatus": aluVlanFilterParamsRowStatus,
       "aluVlanFilterParamsDescription": aluVlanFilterParamsDescription,
       "aluVlanFilterParamsAction": aluVlanFilterParamsAction,
       "aluVlanFilterParamsVlanValue1": aluVlanFilterParamsVlanValue1,
       "aluVlanFilterParamsVlanValue2": aluVlanFilterParamsVlanValue2,
       "aluVlanFilterParamsVlanOperator": aluVlanFilterParamsVlanOperator,
       "aluVlanFilterParamsUntagged": aluVlanFilterParamsUntagged,
       "aluExtIPFilterParamsTable": aluExtIPFilterParamsTable,
       "aluExtIPFilterParamsEntry": aluExtIPFilterParamsEntry,
       "aluExtIPFilterParamsForwardFC": aluExtIPFilterParamsForwardFC,
       "aluExtIPFilterParamsForwardFcType": aluExtIPFilterParamsForwardFcType,
       "aluExtIPFilterParamsForwardFcPri": aluExtIPFilterParamsForwardFcPri,
       "aluVlanFilterNameTable": aluVlanFilterNameTable,
       "aluVlanFilterNameEntry": aluVlanFilterNameEntry,
       "aluVlanFilterNameId": aluVlanFilterNameId,
       "aluVlanFilterNameRowStatus": aluVlanFilterNameRowStatus,
       "aluFilterNotificationsPrefix": aluFilterNotificationsPrefix,
       "alyFilterNotifications": alyFilterNotifications}
)
