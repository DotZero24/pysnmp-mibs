# SNMP MIB module (ADTRAN-EFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-EFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:34 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenEfm,
 adGenEfmID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-EFM-MIB",
    "adGenEfm",
    "adGenEfmID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenEfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 66, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEfmMIB.setRevisions(
        ("2020-05-11 00:00",
         "2018-08-29 00:00",
         "2013-01-18 00:00",
         "2011-12-09 00:00",
         "2007-04-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEfmIndex_ObjectIdentity = ObjectIdentity
adGenEfmIndex = _AdGenEfmIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 1)
)
_AdGenEfmIndexTable_Object = MibTable
adGenEfmIndexTable = _AdGenEfmIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEfmIndexTable.setStatus("current")
_AdGenEfmIndexEntry_Object = MibTableRow
adGenEfmIndexEntry = _AdGenEfmIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 1, 1, 1)
)
adGenEfmIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmIndexEntry.setStatus("current")


class _AdGenEfmUnitIndex_Type(Integer32):
    """Custom type adGenEfmUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cot", 1),
          ("rt", 2))
    )


_AdGenEfmUnitIndex_Type.__name__ = "Integer32"
_AdGenEfmUnitIndex_Object = MibTableColumn
adGenEfmUnitIndex = _AdGenEfmUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 1, 1, 1, 1),
    _AdGenEfmUnitIndex_Type()
)
adGenEfmUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmUnitIndex.setStatus("current")
_AdGenEfmConfiguration_ObjectIdentity = ObjectIdentity
adGenEfmConfiguration = _AdGenEfmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 2)
)
_AdGenEfmConfTable_Object = MibTable
adGenEfmConfTable = _AdGenEfmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEfmConfTable.setStatus("current")
_AdGenEfmConfEntry_Object = MibTableRow
adGenEfmConfEntry = _AdGenEfmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 2, 1, 1)
)
adGenEfmConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmConfEntry.setStatus("current")
_AdGenEfmConfMaxGroups_Type = Integer32
_AdGenEfmConfMaxGroups_Object = MibTableColumn
adGenEfmConfMaxGroups = _AdGenEfmConfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 2, 1, 1, 1),
    _AdGenEfmConfMaxGroups_Type()
)
adGenEfmConfMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmConfMaxGroups.setStatus("current")
_AdGenEfmConfMaxGroupSize_Type = Integer32
_AdGenEfmConfMaxGroupSize_Object = MibTableColumn
adGenEfmConfMaxGroupSize = _AdGenEfmConfMaxGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 2, 1, 1, 2),
    _AdGenEfmConfMaxGroupSize_Type()
)
adGenEfmConfMaxGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmConfMaxGroupSize.setStatus("current")
_AdGenEfmProvisioning_ObjectIdentity = ObjectIdentity
adGenEfmProvisioning = _AdGenEfmProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3)
)
_AdGenEfmProvTable_Object = MibTable
adGenEfmProvTable = _AdGenEfmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenEfmProvTable.setStatus("current")
_AdGenEfmProvEntry_Object = MibTableRow
adGenEfmProvEntry = _AdGenEfmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 1, 1)
)
adGenEfmProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmProvEntry.setStatus("current")
_AdGenEfmProvErrorString_Type = OctetString
_AdGenEfmProvErrorString_Object = MibTableColumn
adGenEfmProvErrorString = _AdGenEfmProvErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 1, 1, 1),
    _AdGenEfmProvErrorString_Type()
)
adGenEfmProvErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmProvErrorString.setStatus("current")
_AdGenEfmProvGroupTable_Object = MibTable
adGenEfmProvGroupTable = _AdGenEfmProvGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adGenEfmProvGroupTable.setStatus("current")
_AdGenEfmProvGroupEntry_Object = MibTableRow
adGenEfmProvGroupEntry = _AdGenEfmProvGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1)
)
adGenEfmProvGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmProvGroupEntry.setStatus("current")


class _AdGenEfmProvGroupServiceState_Type(Integer32):
    """Custom type adGenEfmProvGroupServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("oosUnassigned", 2),
          ("oosMaintenance", 3))
    )


_AdGenEfmProvGroupServiceState_Type.__name__ = "Integer32"
_AdGenEfmProvGroupServiceState_Object = MibTableColumn
adGenEfmProvGroupServiceState = _AdGenEfmProvGroupServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 1),
    _AdGenEfmProvGroupServiceState_Type()
)
adGenEfmProvGroupServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupServiceState.setStatus("current")
_AdGenEfmProvGroupFragmentSize_Type = Integer32
_AdGenEfmProvGroupFragmentSize_Object = MibTableColumn
adGenEfmProvGroupFragmentSize = _AdGenEfmProvGroupFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 2),
    _AdGenEfmProvGroupFragmentSize_Type()
)
adGenEfmProvGroupFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupFragmentSize.setStatus("current")
_AdGenEfmProvGroupSkewThreshold_Type = Integer32
_AdGenEfmProvGroupSkewThreshold_Object = MibTableColumn
adGenEfmProvGroupSkewThreshold = _AdGenEfmProvGroupSkewThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 3),
    _AdGenEfmProvGroupSkewThreshold_Type()
)
adGenEfmProvGroupSkewThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupSkewThreshold.setStatus("current")


class _AdGenEfmProvGroupXCVThreshold_Type(Integer32):
    """Custom type adGenEfmProvGroupXCVThreshold based on Integer32"""
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
        *(("disabled", 1),
          ("rate1Eto8", 2),
          ("rate1Eto7", 3),
          ("rate1Eto6", 4),
          ("rate1Eto5", 5),
          ("rate1Eto4", 6),
          ("rate1Eto3", 7))
    )


_AdGenEfmProvGroupXCVThreshold_Type.__name__ = "Integer32"
_AdGenEfmProvGroupXCVThreshold_Object = MibTableColumn
adGenEfmProvGroupXCVThreshold = _AdGenEfmProvGroupXCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 4),
    _AdGenEfmProvGroupXCVThreshold_Type()
)
adGenEfmProvGroupXCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupXCVThreshold.setStatus("current")
_AdGenEfmProvGroupName_Type = DisplayString
_AdGenEfmProvGroupName_Object = MibTableColumn
adGenEfmProvGroupName = _AdGenEfmProvGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 5),
    _AdGenEfmProvGroupName_Type()
)
adGenEfmProvGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupName.setStatus("current")


class _AdGenEfmProvGroupCRCMode_Type(Integer32):
    """Custom type adGenEfmProvGroupCRCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_AdGenEfmProvGroupCRCMode_Type.__name__ = "Integer32"
_AdGenEfmProvGroupCRCMode_Object = MibTableColumn
adGenEfmProvGroupCRCMode = _AdGenEfmProvGroupCRCMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 6),
    _AdGenEfmProvGroupCRCMode_Type()
)
adGenEfmProvGroupCRCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupCRCMode.setStatus("current")


class _AdGenEfmProvGroupXCVLinkRemoval_Type(Integer32):
    """Custom type adGenEfmProvGroupXCVLinkRemoval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenEfmProvGroupXCVLinkRemoval_Type.__name__ = "Integer32"
_AdGenEfmProvGroupXCVLinkRemoval_Object = MibTableColumn
adGenEfmProvGroupXCVLinkRemoval = _AdGenEfmProvGroupXCVLinkRemoval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 7),
    _AdGenEfmProvGroupXCVLinkRemoval_Type()
)
adGenEfmProvGroupXCVLinkRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupXCVLinkRemoval.setStatus("current")


class _AdGenEfmProvGroupLoopbackDetection_Type(Integer32):
    """Custom type adGenEfmProvGroupLoopbackDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenEfmProvGroupLoopbackDetection_Type.__name__ = "Integer32"
_AdGenEfmProvGroupLoopbackDetection_Object = MibTableColumn
adGenEfmProvGroupLoopbackDetection = _AdGenEfmProvGroupLoopbackDetection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 8),
    _AdGenEfmProvGroupLoopbackDetection_Type()
)
adGenEfmProvGroupLoopbackDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupLoopbackDetection.setStatus("current")


class _AdGenEfmProvGroupTrapReportingGroupDown_Type(Integer32):
    """Custom type adGenEfmProvGroupTrapReportingGroupDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenEfmProvGroupTrapReportingGroupDown_Type.__name__ = "Integer32"
_AdGenEfmProvGroupTrapReportingGroupDown_Object = MibTableColumn
adGenEfmProvGroupTrapReportingGroupDown = _AdGenEfmProvGroupTrapReportingGroupDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 9),
    _AdGenEfmProvGroupTrapReportingGroupDown_Type()
)
adGenEfmProvGroupTrapReportingGroupDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupTrapReportingGroupDown.setStatus("current")


class _AdGenEfmProvGroupTrapReportingGroupPartial_Type(Integer32):
    """Custom type adGenEfmProvGroupTrapReportingGroupPartial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenEfmProvGroupTrapReportingGroupPartial_Type.__name__ = "Integer32"
_AdGenEfmProvGroupTrapReportingGroupPartial_Object = MibTableColumn
adGenEfmProvGroupTrapReportingGroupPartial = _AdGenEfmProvGroupTrapReportingGroupPartial_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 10),
    _AdGenEfmProvGroupTrapReportingGroupPartial_Type()
)
adGenEfmProvGroupTrapReportingGroupPartial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupTrapReportingGroupPartial.setStatus("current")


class _AdGenEfmProvGroupDownlinkEnable_Type(TruthValue):
    """Custom type adGenEfmProvGroupDownlinkEnable based on TruthValue"""
    defaultValue = 2


_AdGenEfmProvGroupDownlinkEnable_Type.__name__ = "TruthValue"
_AdGenEfmProvGroupDownlinkEnable_Object = MibTableColumn
adGenEfmProvGroupDownlinkEnable = _AdGenEfmProvGroupDownlinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 2, 1, 11),
    _AdGenEfmProvGroupDownlinkEnable_Type()
)
adGenEfmProvGroupDownlinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupDownlinkEnable.setStatus("current")
_AdGenEfmProvLinkTable_Object = MibTable
adGenEfmProvLinkTable = _AdGenEfmProvLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 3)
)
if mibBuilder.loadTexts:
    adGenEfmProvLinkTable.setStatus("current")
_AdGenEfmProvLinkEntry_Object = MibTableRow
adGenEfmProvLinkEntry = _AdGenEfmProvLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 3, 1)
)
adGenEfmProvLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmProvLinkEntry.setStatus("current")
_AdGenEfmProvLinkAssignment_Type = Integer32
_AdGenEfmProvLinkAssignment_Object = MibTableColumn
adGenEfmProvLinkAssignment = _AdGenEfmProvLinkAssignment_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 3, 1, 1),
    _AdGenEfmProvLinkAssignment_Type()
)
adGenEfmProvLinkAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvLinkAssignment.setStatus("current")
_AdGenEfmProvLinkIfAssignment_Type = InterfaceIndex
_AdGenEfmProvLinkIfAssignment_Object = MibTableColumn
adGenEfmProvLinkIfAssignment = _AdGenEfmProvLinkIfAssignment_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 3, 1, 2),
    _AdGenEfmProvLinkIfAssignment_Type()
)
adGenEfmProvLinkIfAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvLinkIfAssignment.setStatus("current")


class _AdGenEfmProvLinkTrapReportingLinkDown_Type(Integer32):
    """Custom type adGenEfmProvLinkTrapReportingLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenEfmProvLinkTrapReportingLinkDown_Type.__name__ = "Integer32"
_AdGenEfmProvLinkTrapReportingLinkDown_Object = MibTableColumn
adGenEfmProvLinkTrapReportingLinkDown = _AdGenEfmProvLinkTrapReportingLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 3, 1, 3),
    _AdGenEfmProvLinkTrapReportingLinkDown_Type()
)
adGenEfmProvLinkTrapReportingLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvLinkTrapReportingLinkDown.setStatus("current")
_AdGenEfmProvGroupAlarmSlotTable_Object = MibTable
adGenEfmProvGroupAlarmSlotTable = _AdGenEfmProvGroupAlarmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 4)
)
if mibBuilder.loadTexts:
    adGenEfmProvGroupAlarmSlotTable.setStatus("current")
_AdGenEfmProvGroupAlarmSlotEntry_Object = MibTableRow
adGenEfmProvGroupAlarmSlotEntry = _AdGenEfmProvGroupAlarmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 4, 1)
)
adGenEfmProvGroupAlarmSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmProvGroupAlarmSlotEntry.setStatus("current")


class _AdGenEfmProvGroupAlarmSlotGroupDownSeverity_Type(Integer32):
    """Custom type adGenEfmProvGroupAlarmSlotGroupDownSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenEfmProvGroupAlarmSlotGroupDownSeverity_Type.__name__ = "Integer32"
_AdGenEfmProvGroupAlarmSlotGroupDownSeverity_Object = MibTableColumn
adGenEfmProvGroupAlarmSlotGroupDownSeverity = _AdGenEfmProvGroupAlarmSlotGroupDownSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 4, 1, 1),
    _AdGenEfmProvGroupAlarmSlotGroupDownSeverity_Type()
)
adGenEfmProvGroupAlarmSlotGroupDownSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupAlarmSlotGroupDownSeverity.setStatus("current")


class _AdGenEfmProvGroupAlarmSlotGroupPartialSeverity_Type(Integer32):
    """Custom type adGenEfmProvGroupAlarmSlotGroupPartialSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenEfmProvGroupAlarmSlotGroupPartialSeverity_Type.__name__ = "Integer32"
_AdGenEfmProvGroupAlarmSlotGroupPartialSeverity_Object = MibTableColumn
adGenEfmProvGroupAlarmSlotGroupPartialSeverity = _AdGenEfmProvGroupAlarmSlotGroupPartialSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 3, 4, 1, 2),
    _AdGenEfmProvGroupAlarmSlotGroupPartialSeverity_Type()
)
adGenEfmProvGroupAlarmSlotGroupPartialSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmProvGroupAlarmSlotGroupPartialSeverity.setStatus("current")
_AdGenEfmStatus_ObjectIdentity = ObjectIdentity
adGenEfmStatus = _AdGenEfmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4)
)
_AdGenEfmStatTable_Object = MibTable
adGenEfmStatTable = _AdGenEfmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adGenEfmStatTable.setStatus("current")
_AdGenEfmStatEntry_Object = MibTableRow
adGenEfmStatEntry = _AdGenEfmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1)
)
adGenEfmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmStatEntry.setStatus("current")


class _AdGenEfmStatGroupStatus_Type(Integer32):
    """Custom type adGenEfmStatGroupStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("noLinksInGroup", 4),
          ("upPartial", 5))
    )


_AdGenEfmStatGroupStatus_Type.__name__ = "Integer32"
_AdGenEfmStatGroupStatus_Object = MibTableColumn
adGenEfmStatGroupStatus = _AdGenEfmStatGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1, 1),
    _AdGenEfmStatGroupStatus_Type()
)
adGenEfmStatGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmStatGroupStatus.setStatus("current")
_AdGenEfmStatGroupSize_Type = Integer32
_AdGenEfmStatGroupSize_Object = MibTableColumn
adGenEfmStatGroupSize = _AdGenEfmStatGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1, 2),
    _AdGenEfmStatGroupSize_Type()
)
adGenEfmStatGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmStatGroupSize.setStatus("current")
_AdGenEfmStatNumActiveLinks_Type = Integer32
_AdGenEfmStatNumActiveLinks_Object = MibTableColumn
adGenEfmStatNumActiveLinks = _AdGenEfmStatNumActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1, 3),
    _AdGenEfmStatNumActiveLinks_Type()
)
adGenEfmStatNumActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmStatNumActiveLinks.setStatus("current")


class _AdGenEfmStatLinkNeTcSync_Type(Integer32):
    """Custom type adGenEfmStatLinkNeTcSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdGenEfmStatLinkNeTcSync_Type.__name__ = "Integer32"
_AdGenEfmStatLinkNeTcSync_Object = MibTableColumn
adGenEfmStatLinkNeTcSync = _AdGenEfmStatLinkNeTcSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1, 4),
    _AdGenEfmStatLinkNeTcSync_Type()
)
adGenEfmStatLinkNeTcSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmStatLinkNeTcSync.setStatus("current")


class _AdGenEfmStatLinkFeTcSync_Type(Integer32):
    """Custom type adGenEfmStatLinkFeTcSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdGenEfmStatLinkFeTcSync_Type.__name__ = "Integer32"
_AdGenEfmStatLinkFeTcSync_Object = MibTableColumn
adGenEfmStatLinkFeTcSync = _AdGenEfmStatLinkFeTcSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1, 5),
    _AdGenEfmStatLinkFeTcSync_Type()
)
adGenEfmStatLinkFeTcSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmStatLinkFeTcSync.setStatus("current")
_AdGenEfmStatLinkSkew_Type = Integer32
_AdGenEfmStatLinkSkew_Object = MibTableColumn
adGenEfmStatLinkSkew = _AdGenEfmStatLinkSkew_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 4, 1, 1, 6),
    _AdGenEfmStatLinkSkew_Type()
)
adGenEfmStatLinkSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmStatLinkSkew.setStatus("current")
_AdGenEfmTest_ObjectIdentity = ObjectIdentity
adGenEfmTest = _AdGenEfmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 5)
)
_AdGenEfmTestTable_Object = MibTable
adGenEfmTestTable = _AdGenEfmTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 5, 1)
)
if mibBuilder.loadTexts:
    adGenEfmTestTable.setStatus("current")
_AdGenEfmTestEntry_Object = MibTableRow
adGenEfmTestEntry = _AdGenEfmTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 5, 1, 1)
)
adGenEfmTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmTestEntry.setStatus("current")


class _AdGenEfmTestOamRemoteLoopback_Type(Integer32):
    """Custom type adGenEfmTestOamRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenEfmTestOamRemoteLoopback_Type.__name__ = "Integer32"
_AdGenEfmTestOamRemoteLoopback_Object = MibTableColumn
adGenEfmTestOamRemoteLoopback = _AdGenEfmTestOamRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 5, 1, 1, 1),
    _AdGenEfmTestOamRemoteLoopback_Type()
)
adGenEfmTestOamRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmTestOamRemoteLoopback.setStatus("current")
_AdGenEfmTestOamRemoteLoopbackTimeout_Type = Integer32
_AdGenEfmTestOamRemoteLoopbackTimeout_Object = MibTableColumn
adGenEfmTestOamRemoteLoopbackTimeout = _AdGenEfmTestOamRemoteLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 5, 1, 1, 2),
    _AdGenEfmTestOamRemoteLoopbackTimeout_Type()
)
adGenEfmTestOamRemoteLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmTestOamRemoteLoopbackTimeout.setStatus("current")
_AdGenEfmPerformance_ObjectIdentity = ObjectIdentity
adGenEfmPerformance = _AdGenEfmPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6)
)
_AdGenEfmPerfGroupCurr15MinTable_Object = MibTable
adGenEfmPerfGroupCurr15MinTable = _AdGenEfmPerfGroupCurr15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinTable.setStatus("current")
_AdGenEfmPerfGroupCurr15MinEntry_Object = MibTableRow
adGenEfmPerfGroupCurr15MinEntry = _AdGenEfmPerfGroupCurr15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1)
)
adGenEfmPerfGroupCurr15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinEntry.setStatus("current")
_AdGenEfmPerfGroupCurr15MinTxOctets_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinTxOctets_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinTxOctets = _AdGenEfmPerfGroupCurr15MinTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 1),
    _AdGenEfmPerfGroupCurr15MinTxOctets_Type()
)
adGenEfmPerfGroupCurr15MinTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinTxOctets.setStatus("current")
_AdGenEfmPerfGroupCurr15MinTxFrames_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinTxFrames_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinTxFrames = _AdGenEfmPerfGroupCurr15MinTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 2),
    _AdGenEfmPerfGroupCurr15MinTxFrames_Type()
)
adGenEfmPerfGroupCurr15MinTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinTxFrames.setStatus("current")
_AdGenEfmPerfGroupCurr15MinRxOctets_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxOctets_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxOctets = _AdGenEfmPerfGroupCurr15MinRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 3),
    _AdGenEfmPerfGroupCurr15MinRxOctets_Type()
)
adGenEfmPerfGroupCurr15MinRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxOctets.setStatus("current")
_AdGenEfmPerfGroupCurr15MinRxFrames_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxFrames_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxFrames = _AdGenEfmPerfGroupCurr15MinRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 4),
    _AdGenEfmPerfGroupCurr15MinRxFrames_Type()
)
adGenEfmPerfGroupCurr15MinRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxFrames.setStatus("current")
_AdGenEfmPerfGroupCurr15MinRxBadFragments_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxBadFragments = _AdGenEfmPerfGroupCurr15MinRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 5),
    _AdGenEfmPerfGroupCurr15MinRxBadFragments_Type()
)
adGenEfmPerfGroupCurr15MinRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxBadFragments.setStatus("current")
_AdGenEfmPerfGroupCurr15MinRxLostFragments_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxLostFragments = _AdGenEfmPerfGroupCurr15MinRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 6),
    _AdGenEfmPerfGroupCurr15MinRxLostFragments_Type()
)
adGenEfmPerfGroupCurr15MinRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxLostFragments.setStatus("current")
_AdGenEfmPerfGroupCurr15MinRxLostStarts_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxLostStarts = _AdGenEfmPerfGroupCurr15MinRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 7),
    _AdGenEfmPerfGroupCurr15MinRxLostStarts_Type()
)
adGenEfmPerfGroupCurr15MinRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxLostStarts.setStatus("current")
_AdGenEfmPerfGroupCurr15MinRxLostEnds_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxLostEnds = _AdGenEfmPerfGroupCurr15MinRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 8),
    _AdGenEfmPerfGroupCurr15MinRxLostEnds_Type()
)
adGenEfmPerfGroupCurr15MinRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxLostEnds.setStatus("current")
_AdGenEfmPerfGroup15MinValidIntervals_Type = Integer32
_AdGenEfmPerfGroup15MinValidIntervals_Object = MibTableColumn
adGenEfmPerfGroup15MinValidIntervals = _AdGenEfmPerfGroup15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 9),
    _AdGenEfmPerfGroup15MinValidIntervals_Type()
)
adGenEfmPerfGroup15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinValidIntervals.setStatus("current")
_AdGenEfmPerfGroupCurr15MinTxPercUtil_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinTxPercUtil_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinTxPercUtil = _AdGenEfmPerfGroupCurr15MinTxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 10),
    _AdGenEfmPerfGroupCurr15MinTxPercUtil_Type()
)
adGenEfmPerfGroupCurr15MinTxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinTxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinTxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroupCurr15MinRxPercUtil_Type = Gauge32
_AdGenEfmPerfGroupCurr15MinRxPercUtil_Object = MibTableColumn
adGenEfmPerfGroupCurr15MinRxPercUtil = _AdGenEfmPerfGroupCurr15MinRxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 1, 1, 11),
    _AdGenEfmPerfGroupCurr15MinRxPercUtil_Type()
)
adGenEfmPerfGroupCurr15MinRxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr15MinRxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroupCurr24HrTable_Object = MibTable
adGenEfmPerfGroupCurr24HrTable = _AdGenEfmPerfGroupCurr24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrTable.setStatus("current")
_AdGenEfmPerfGroupCurr24HrEntry_Object = MibTableRow
adGenEfmPerfGroupCurr24HrEntry = _AdGenEfmPerfGroupCurr24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1)
)
adGenEfmPerfGroupCurr24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrEntry.setStatus("current")
_AdGenEfmPerfGroupCurr24HrTxOctets_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrTxOctets_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrTxOctets = _AdGenEfmPerfGroupCurr24HrTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 1),
    _AdGenEfmPerfGroupCurr24HrTxOctets_Type()
)
adGenEfmPerfGroupCurr24HrTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrTxOctets.setStatus("current")
_AdGenEfmPerfGroupCurr24HrTxFrames_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrTxFrames_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrTxFrames = _AdGenEfmPerfGroupCurr24HrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 2),
    _AdGenEfmPerfGroupCurr24HrTxFrames_Type()
)
adGenEfmPerfGroupCurr24HrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrTxFrames.setStatus("current")
_AdGenEfmPerfGroupCurr24HrRxOctets_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxOctets_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxOctets = _AdGenEfmPerfGroupCurr24HrRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 3),
    _AdGenEfmPerfGroupCurr24HrRxOctets_Type()
)
adGenEfmPerfGroupCurr24HrRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxOctets.setStatus("current")
_AdGenEfmPerfGroupCurr24HrRxFrames_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxFrames_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxFrames = _AdGenEfmPerfGroupCurr24HrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 4),
    _AdGenEfmPerfGroupCurr24HrRxFrames_Type()
)
adGenEfmPerfGroupCurr24HrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxFrames.setStatus("current")
_AdGenEfmPerfGroupCurr24HrRxBadFragments_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxBadFragments = _AdGenEfmPerfGroupCurr24HrRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 5),
    _AdGenEfmPerfGroupCurr24HrRxBadFragments_Type()
)
adGenEfmPerfGroupCurr24HrRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxBadFragments.setStatus("current")
_AdGenEfmPerfGroupCurr24HrRxLostFragments_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxLostFragments = _AdGenEfmPerfGroupCurr24HrRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 6),
    _AdGenEfmPerfGroupCurr24HrRxLostFragments_Type()
)
adGenEfmPerfGroupCurr24HrRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxLostFragments.setStatus("current")
_AdGenEfmPerfGroupCurr24HrRxLostStarts_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxLostStarts = _AdGenEfmPerfGroupCurr24HrRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 7),
    _AdGenEfmPerfGroupCurr24HrRxLostStarts_Type()
)
adGenEfmPerfGroupCurr24HrRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxLostStarts.setStatus("current")
_AdGenEfmPerfGroupCurr24HrRxLostEnds_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxLostEnds = _AdGenEfmPerfGroupCurr24HrRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 8),
    _AdGenEfmPerfGroupCurr24HrRxLostEnds_Type()
)
adGenEfmPerfGroupCurr24HrRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxLostEnds.setStatus("current")
_AdGenEfmPerfGroup24HrValidIntervals_Type = Integer32
_AdGenEfmPerfGroup24HrValidIntervals_Object = MibTableColumn
adGenEfmPerfGroup24HrValidIntervals = _AdGenEfmPerfGroup24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 9),
    _AdGenEfmPerfGroup24HrValidIntervals_Type()
)
adGenEfmPerfGroup24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrValidIntervals.setStatus("current")
_AdGenEfmPerfGroupCurr24HrTxPercUtil_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrTxPercUtil_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrTxPercUtil = _AdGenEfmPerfGroupCurr24HrTxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 10),
    _AdGenEfmPerfGroupCurr24HrTxPercUtil_Type()
)
adGenEfmPerfGroupCurr24HrTxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrTxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrTxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroupCurr24HrRxPercUtil_Type = Gauge32
_AdGenEfmPerfGroupCurr24HrRxPercUtil_Object = MibTableColumn
adGenEfmPerfGroupCurr24HrRxPercUtil = _AdGenEfmPerfGroupCurr24HrRxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 2, 1, 11),
    _AdGenEfmPerfGroupCurr24HrRxPercUtil_Type()
)
adGenEfmPerfGroupCurr24HrRxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupCurr24HrRxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroup15MinIntTable_Object = MibTable
adGenEfmPerfGroup15MinIntTable = _AdGenEfmPerfGroup15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntTable.setStatus("current")
_AdGenEfmPerfGroup15MinIntEntry_Object = MibTableRow
adGenEfmPerfGroup15MinIntEntry = _AdGenEfmPerfGroup15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1)
)
adGenEfmPerfGroup15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntNumber"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntEntry.setStatus("current")
_AdGenEfmPerfGroup15MinIntNumber_Type = Gauge32
_AdGenEfmPerfGroup15MinIntNumber_Object = MibTableColumn
adGenEfmPerfGroup15MinIntNumber = _AdGenEfmPerfGroup15MinIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 1),
    _AdGenEfmPerfGroup15MinIntNumber_Type()
)
adGenEfmPerfGroup15MinIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntNumber.setStatus("current")
_AdGenEfmPerfGroup15MinIntTxOctets_Type = Gauge32
_AdGenEfmPerfGroup15MinIntTxOctets_Object = MibTableColumn
adGenEfmPerfGroup15MinIntTxOctets = _AdGenEfmPerfGroup15MinIntTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 2),
    _AdGenEfmPerfGroup15MinIntTxOctets_Type()
)
adGenEfmPerfGroup15MinIntTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntTxOctets.setStatus("current")
_AdGenEfmPerfGroup15MinIntTxFrames_Type = Gauge32
_AdGenEfmPerfGroup15MinIntTxFrames_Object = MibTableColumn
adGenEfmPerfGroup15MinIntTxFrames = _AdGenEfmPerfGroup15MinIntTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 3),
    _AdGenEfmPerfGroup15MinIntTxFrames_Type()
)
adGenEfmPerfGroup15MinIntTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntTxFrames.setStatus("current")
_AdGenEfmPerfGroup15MinIntRxOctets_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxOctets_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxOctets = _AdGenEfmPerfGroup15MinIntRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 4),
    _AdGenEfmPerfGroup15MinIntRxOctets_Type()
)
adGenEfmPerfGroup15MinIntRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxOctets.setStatus("current")
_AdGenEfmPerfGroup15MinIntRxFrames_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxFrames_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxFrames = _AdGenEfmPerfGroup15MinIntRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 5),
    _AdGenEfmPerfGroup15MinIntRxFrames_Type()
)
adGenEfmPerfGroup15MinIntRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxFrames.setStatus("current")
_AdGenEfmPerfGroup15MinIntRxBadFragments_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxBadFragments = _AdGenEfmPerfGroup15MinIntRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 6),
    _AdGenEfmPerfGroup15MinIntRxBadFragments_Type()
)
adGenEfmPerfGroup15MinIntRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxBadFragments.setStatus("current")
_AdGenEfmPerfGroup15MinIntRxLostFragments_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxLostFragments = _AdGenEfmPerfGroup15MinIntRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 7),
    _AdGenEfmPerfGroup15MinIntRxLostFragments_Type()
)
adGenEfmPerfGroup15MinIntRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxLostFragments.setStatus("current")
_AdGenEfmPerfGroup15MinIntRxLostStarts_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxLostStarts = _AdGenEfmPerfGroup15MinIntRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 8),
    _AdGenEfmPerfGroup15MinIntRxLostStarts_Type()
)
adGenEfmPerfGroup15MinIntRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxLostStarts.setStatus("current")
_AdGenEfmPerfGroup15MinIntRxLostEnds_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxLostEnds = _AdGenEfmPerfGroup15MinIntRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 9),
    _AdGenEfmPerfGroup15MinIntRxLostEnds_Type()
)
adGenEfmPerfGroup15MinIntRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxLostEnds.setStatus("current")
_AdGenEfmPerfGroup15MinIntTxPercUtil_Type = Gauge32
_AdGenEfmPerfGroup15MinIntTxPercUtil_Object = MibTableColumn
adGenEfmPerfGroup15MinIntTxPercUtil = _AdGenEfmPerfGroup15MinIntTxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 10),
    _AdGenEfmPerfGroup15MinIntTxPercUtil_Type()
)
adGenEfmPerfGroup15MinIntTxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntTxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntTxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroup15MinIntRxPercUtil_Type = Gauge32
_AdGenEfmPerfGroup15MinIntRxPercUtil_Object = MibTableColumn
adGenEfmPerfGroup15MinIntRxPercUtil = _AdGenEfmPerfGroup15MinIntRxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 3, 1, 11),
    _AdGenEfmPerfGroup15MinIntRxPercUtil_Type()
)
adGenEfmPerfGroup15MinIntRxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinIntRxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroup24HrIntTable_Object = MibTable
adGenEfmPerfGroup24HrIntTable = _AdGenEfmPerfGroup24HrIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntTable.setStatus("current")
_AdGenEfmPerfGroup24HrIntEntry_Object = MibTableRow
adGenEfmPerfGroup24HrIntEntry = _AdGenEfmPerfGroup24HrIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1)
)
adGenEfmPerfGroup24HrIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntNumber"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntEntry.setStatus("current")
_AdGenEfmPerfGroup24HrIntNumber_Type = Gauge32
_AdGenEfmPerfGroup24HrIntNumber_Object = MibTableColumn
adGenEfmPerfGroup24HrIntNumber = _AdGenEfmPerfGroup24HrIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 1),
    _AdGenEfmPerfGroup24HrIntNumber_Type()
)
adGenEfmPerfGroup24HrIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntNumber.setStatus("current")
_AdGenEfmPerfGroup24HrIntTxOctets_Type = Gauge32
_AdGenEfmPerfGroup24HrIntTxOctets_Object = MibTableColumn
adGenEfmPerfGroup24HrIntTxOctets = _AdGenEfmPerfGroup24HrIntTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 2),
    _AdGenEfmPerfGroup24HrIntTxOctets_Type()
)
adGenEfmPerfGroup24HrIntTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntTxOctets.setStatus("current")
_AdGenEfmPerfGroup24HrIntTxFrames_Type = Gauge32
_AdGenEfmPerfGroup24HrIntTxFrames_Object = MibTableColumn
adGenEfmPerfGroup24HrIntTxFrames = _AdGenEfmPerfGroup24HrIntTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 3),
    _AdGenEfmPerfGroup24HrIntTxFrames_Type()
)
adGenEfmPerfGroup24HrIntTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntTxFrames.setStatus("current")
_AdGenEfmPerfGroup24HrIntRxOctets_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxOctets_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxOctets = _AdGenEfmPerfGroup24HrIntRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 4),
    _AdGenEfmPerfGroup24HrIntRxOctets_Type()
)
adGenEfmPerfGroup24HrIntRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxOctets.setStatus("current")
_AdGenEfmPerfGroup24HrIntRxFrames_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxFrames_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxFrames = _AdGenEfmPerfGroup24HrIntRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 5),
    _AdGenEfmPerfGroup24HrIntRxFrames_Type()
)
adGenEfmPerfGroup24HrIntRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxFrames.setStatus("current")
_AdGenEfmPerfGroup24HrIntRxBadFragments_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxBadFragments = _AdGenEfmPerfGroup24HrIntRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 6),
    _AdGenEfmPerfGroup24HrIntRxBadFragments_Type()
)
adGenEfmPerfGroup24HrIntRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxBadFragments.setStatus("current")
_AdGenEfmPerfGroup24HrIntRxLostFragments_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxLostFragments = _AdGenEfmPerfGroup24HrIntRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 7),
    _AdGenEfmPerfGroup24HrIntRxLostFragments_Type()
)
adGenEfmPerfGroup24HrIntRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxLostFragments.setStatus("current")
_AdGenEfmPerfGroup24HrIntRxLostStarts_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxLostStarts = _AdGenEfmPerfGroup24HrIntRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 8),
    _AdGenEfmPerfGroup24HrIntRxLostStarts_Type()
)
adGenEfmPerfGroup24HrIntRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxLostStarts.setStatus("current")
_AdGenEfmPerfGroup24HrIntRxLostEnds_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxLostEnds = _AdGenEfmPerfGroup24HrIntRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 9),
    _AdGenEfmPerfGroup24HrIntRxLostEnds_Type()
)
adGenEfmPerfGroup24HrIntRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxLostEnds.setStatus("current")
_AdGenEfmPerfGroup24HrIntTxPercUtil_Type = Gauge32
_AdGenEfmPerfGroup24HrIntTxPercUtil_Object = MibTableColumn
adGenEfmPerfGroup24HrIntTxPercUtil = _AdGenEfmPerfGroup24HrIntTxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 10),
    _AdGenEfmPerfGroup24HrIntTxPercUtil_Type()
)
adGenEfmPerfGroup24HrIntTxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntTxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntTxPercUtil.setUnits("0.01%")
_AdGenEfmPerfGroup24HrIntRxPercUtil_Type = Gauge32
_AdGenEfmPerfGroup24HrIntRxPercUtil_Object = MibTableColumn
adGenEfmPerfGroup24HrIntRxPercUtil = _AdGenEfmPerfGroup24HrIntRxPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 4, 1, 11),
    _AdGenEfmPerfGroup24HrIntRxPercUtil_Type()
)
adGenEfmPerfGroup24HrIntRxPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxPercUtil.setStatus("current")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrIntRxPercUtil.setUnits("0.01%")
_AdGenEfmPerfLinkCurr15MinTable_Object = MibTable
adGenEfmPerfLinkCurr15MinTable = _AdGenEfmPerfLinkCurr15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinTable.setStatus("current")
_AdGenEfmPerfLinkCurr15MinEntry_Object = MibTableRow
adGenEfmPerfLinkCurr15MinEntry = _AdGenEfmPerfLinkCurr15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1)
)
adGenEfmPerfLinkCurr15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinEntry.setStatus("current")
_AdGenEfmPerfLinkCurr15MinTxFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinTxFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinTxFragments = _AdGenEfmPerfLinkCurr15MinTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 1),
    _AdGenEfmPerfLinkCurr15MinTxFragments_Type()
)
adGenEfmPerfLinkCurr15MinTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinTxFragments.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxFragments = _AdGenEfmPerfLinkCurr15MinRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 2),
    _AdGenEfmPerfLinkCurr15MinRxFragments_Type()
)
adGenEfmPerfLinkCurr15MinRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxFragments.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxErroredFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxErroredFragments = _AdGenEfmPerfLinkCurr15MinRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 3),
    _AdGenEfmPerfLinkCurr15MinRxErroredFragments_Type()
)
adGenEfmPerfLinkCurr15MinRxErroredFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxErroredFragments.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxSmallFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxSmallFragments = _AdGenEfmPerfLinkCurr15MinRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 4),
    _AdGenEfmPerfLinkCurr15MinRxSmallFragments_Type()
)
adGenEfmPerfLinkCurr15MinRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxSmallFragments.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxLargeFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxLargeFragments = _AdGenEfmPerfLinkCurr15MinRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 5),
    _AdGenEfmPerfLinkCurr15MinRxLargeFragments_Type()
)
adGenEfmPerfLinkCurr15MinRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxLargeFragments.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxDiscardedFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxDiscardedFragments = _AdGenEfmPerfLinkCurr15MinRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 6),
    _AdGenEfmPerfLinkCurr15MinRxDiscardedFragments_Type()
)
adGenEfmPerfLinkCurr15MinRxDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxFcsErrors_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxFcsErrors = _AdGenEfmPerfLinkCurr15MinRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 7),
    _AdGenEfmPerfLinkCurr15MinRxFcsErrors_Type()
)
adGenEfmPerfLinkCurr15MinRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxFcsErrors.setStatus("current")
_AdGenEfmPerfLinkCurr15MinRxCodingErrors_Type = Gauge32
_AdGenEfmPerfLinkCurr15MinRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLinkCurr15MinRxCodingErrors = _AdGenEfmPerfLinkCurr15MinRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 8),
    _AdGenEfmPerfLinkCurr15MinRxCodingErrors_Type()
)
adGenEfmPerfLinkCurr15MinRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr15MinRxCodingErrors.setStatus("current")
_AdGenEfmPerfLink15MinValidIntervals_Type = Integer32
_AdGenEfmPerfLink15MinValidIntervals_Object = MibTableColumn
adGenEfmPerfLink15MinValidIntervals = _AdGenEfmPerfLink15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 5, 1, 9),
    _AdGenEfmPerfLink15MinValidIntervals_Type()
)
adGenEfmPerfLink15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinValidIntervals.setStatus("current")
_AdGenEfmPerfLinkCurr24HrTable_Object = MibTable
adGenEfmPerfLinkCurr24HrTable = _AdGenEfmPerfLinkCurr24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrTable.setStatus("current")
_AdGenEfmPerfLinkCurr24HrEntry_Object = MibTableRow
adGenEfmPerfLinkCurr24HrEntry = _AdGenEfmPerfLinkCurr24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1)
)
adGenEfmPerfLinkCurr24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrEntry.setStatus("current")
_AdGenEfmPerfLinkCurr24HrTxFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrTxFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrTxFragments = _AdGenEfmPerfLinkCurr24HrTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 1),
    _AdGenEfmPerfLinkCurr24HrTxFragments_Type()
)
adGenEfmPerfLinkCurr24HrTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrTxFragments.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxFragments = _AdGenEfmPerfLinkCurr24HrRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 2),
    _AdGenEfmPerfLinkCurr24HrRxFragments_Type()
)
adGenEfmPerfLinkCurr24HrRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxFragments.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxErroredFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxErroredFragments = _AdGenEfmPerfLinkCurr24HrRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 3),
    _AdGenEfmPerfLinkCurr24HrRxErroredFragments_Type()
)
adGenEfmPerfLinkCurr24HrRxErroredFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxErroredFragments.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxSmallFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxSmallFragments = _AdGenEfmPerfLinkCurr24HrRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 4),
    _AdGenEfmPerfLinkCurr24HrRxSmallFragments_Type()
)
adGenEfmPerfLinkCurr24HrRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxSmallFragments.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxLargeFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxLargeFragments = _AdGenEfmPerfLinkCurr24HrRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 5),
    _AdGenEfmPerfLinkCurr24HrRxLargeFragments_Type()
)
adGenEfmPerfLinkCurr24HrRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxLargeFragments.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxDiscardedFragments_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxDiscardedFragments = _AdGenEfmPerfLinkCurr24HrRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 6),
    _AdGenEfmPerfLinkCurr24HrRxDiscardedFragments_Type()
)
adGenEfmPerfLinkCurr24HrRxDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxFcsErrors_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxFcsErrors = _AdGenEfmPerfLinkCurr24HrRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 7),
    _AdGenEfmPerfLinkCurr24HrRxFcsErrors_Type()
)
adGenEfmPerfLinkCurr24HrRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxFcsErrors.setStatus("current")
_AdGenEfmPerfLinkCurr24HrRxCodingErrors_Type = Gauge32
_AdGenEfmPerfLinkCurr24HrRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLinkCurr24HrRxCodingErrors = _AdGenEfmPerfLinkCurr24HrRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 8),
    _AdGenEfmPerfLinkCurr24HrRxCodingErrors_Type()
)
adGenEfmPerfLinkCurr24HrRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkCurr24HrRxCodingErrors.setStatus("current")
_AdGenEfmPerfLink24HrValidIntervals_Type = Integer32
_AdGenEfmPerfLink24HrValidIntervals_Object = MibTableColumn
adGenEfmPerfLink24HrValidIntervals = _AdGenEfmPerfLink24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 6, 1, 9),
    _AdGenEfmPerfLink24HrValidIntervals_Type()
)
adGenEfmPerfLink24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrValidIntervals.setStatus("current")
_AdGenEfmPerfLink15MinIntTable_Object = MibTable
adGenEfmPerfLink15MinIntTable = _AdGenEfmPerfLink15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntTable.setStatus("current")
_AdGenEfmPerfLink15MinIntEntry_Object = MibTableRow
adGenEfmPerfLink15MinIntEntry = _AdGenEfmPerfLink15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1)
)
adGenEfmPerfLink15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntNumber"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntEntry.setStatus("current")
_AdGenEfmPerfLink15MinIntNumber_Type = Gauge32
_AdGenEfmPerfLink15MinIntNumber_Object = MibTableColumn
adGenEfmPerfLink15MinIntNumber = _AdGenEfmPerfLink15MinIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 1),
    _AdGenEfmPerfLink15MinIntNumber_Type()
)
adGenEfmPerfLink15MinIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntNumber.setStatus("current")
_AdGenEfmPerfLink15MinIntTxFragments_Type = Gauge32
_AdGenEfmPerfLink15MinIntTxFragments_Object = MibTableColumn
adGenEfmPerfLink15MinIntTxFragments = _AdGenEfmPerfLink15MinIntTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 2),
    _AdGenEfmPerfLink15MinIntTxFragments_Type()
)
adGenEfmPerfLink15MinIntTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntTxFragments.setStatus("current")
_AdGenEfmPerfLink15MinIntRxFragments_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxFragments_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxFragments = _AdGenEfmPerfLink15MinIntRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 3),
    _AdGenEfmPerfLink15MinIntRxFragments_Type()
)
adGenEfmPerfLink15MinIntRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxFragments.setStatus("current")
_AdGenEfmPerfLink15MinIntRxErroredFragments_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxErroredFragments = _AdGenEfmPerfLink15MinIntRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 4),
    _AdGenEfmPerfLink15MinIntRxErroredFragments_Type()
)
adGenEfmPerfLink15MinIntRxErroredFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxErroredFragments.setStatus("current")
_AdGenEfmPerfLink15MinIntRxSmallFragments_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxSmallFragments = _AdGenEfmPerfLink15MinIntRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 5),
    _AdGenEfmPerfLink15MinIntRxSmallFragments_Type()
)
adGenEfmPerfLink15MinIntRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxSmallFragments.setStatus("current")
_AdGenEfmPerfLink15MinIntRxLargeFragments_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxLargeFragments = _AdGenEfmPerfLink15MinIntRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 6),
    _AdGenEfmPerfLink15MinIntRxLargeFragments_Type()
)
adGenEfmPerfLink15MinIntRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxLargeFragments.setStatus("current")
_AdGenEfmPerfLink15MinIntRxDiscardedFragments_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxDiscardedFragments = _AdGenEfmPerfLink15MinIntRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 7),
    _AdGenEfmPerfLink15MinIntRxDiscardedFragments_Type()
)
adGenEfmPerfLink15MinIntRxDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLink15MinIntRxFcsErrors_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxFcsErrors = _AdGenEfmPerfLink15MinIntRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 8),
    _AdGenEfmPerfLink15MinIntRxFcsErrors_Type()
)
adGenEfmPerfLink15MinIntRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxFcsErrors.setStatus("current")
_AdGenEfmPerfLink15MinIntRxCodingErrors_Type = Gauge32
_AdGenEfmPerfLink15MinIntRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLink15MinIntRxCodingErrors = _AdGenEfmPerfLink15MinIntRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 7, 1, 9),
    _AdGenEfmPerfLink15MinIntRxCodingErrors_Type()
)
adGenEfmPerfLink15MinIntRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinIntRxCodingErrors.setStatus("current")
_AdGenEfmPerfLink24HrIntTable_Object = MibTable
adGenEfmPerfLink24HrIntTable = _AdGenEfmPerfLink24HrIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntTable.setStatus("current")
_AdGenEfmPerfLink24HrIntEntry_Object = MibTableRow
adGenEfmPerfLink24HrIntEntry = _AdGenEfmPerfLink24HrIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1)
)
adGenEfmPerfLink24HrIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntNumber"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntEntry.setStatus("current")
_AdGenEfmPerfLink24HrIntNumber_Type = Gauge32
_AdGenEfmPerfLink24HrIntNumber_Object = MibTableColumn
adGenEfmPerfLink24HrIntNumber = _AdGenEfmPerfLink24HrIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 1),
    _AdGenEfmPerfLink24HrIntNumber_Type()
)
adGenEfmPerfLink24HrIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntNumber.setStatus("current")
_AdGenEfmPerfLink24HrIntTxFragments_Type = Gauge32
_AdGenEfmPerfLink24HrIntTxFragments_Object = MibTableColumn
adGenEfmPerfLink24HrIntTxFragments = _AdGenEfmPerfLink24HrIntTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 2),
    _AdGenEfmPerfLink24HrIntTxFragments_Type()
)
adGenEfmPerfLink24HrIntTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntTxFragments.setStatus("current")
_AdGenEfmPerfLink24HrIntRxFragments_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxFragments_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxFragments = _AdGenEfmPerfLink24HrIntRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 3),
    _AdGenEfmPerfLink24HrIntRxFragments_Type()
)
adGenEfmPerfLink24HrIntRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxFragments.setStatus("current")
_AdGenEfmPerfLink24HrIntRxErroredFragments_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxErroredFragments = _AdGenEfmPerfLink24HrIntRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 4),
    _AdGenEfmPerfLink24HrIntRxErroredFragments_Type()
)
adGenEfmPerfLink24HrIntRxErroredFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxErroredFragments.setStatus("current")
_AdGenEfmPerfLink24HrIntRxSmallFragments_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxSmallFragments = _AdGenEfmPerfLink24HrIntRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 5),
    _AdGenEfmPerfLink24HrIntRxSmallFragments_Type()
)
adGenEfmPerfLink24HrIntRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxSmallFragments.setStatus("current")
_AdGenEfmPerfLink24HrIntRxLargeFragments_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxLargeFragments = _AdGenEfmPerfLink24HrIntRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 6),
    _AdGenEfmPerfLink24HrIntRxLargeFragments_Type()
)
adGenEfmPerfLink24HrIntRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxLargeFragments.setStatus("current")
_AdGenEfmPerfLink24HrIntRxDiscardedFragments_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxDiscardedFragments = _AdGenEfmPerfLink24HrIntRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 7),
    _AdGenEfmPerfLink24HrIntRxDiscardedFragments_Type()
)
adGenEfmPerfLink24HrIntRxDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLink24HrIntRxFcsErrors_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxFcsErrors = _AdGenEfmPerfLink24HrIntRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 8),
    _AdGenEfmPerfLink24HrIntRxFcsErrors_Type()
)
adGenEfmPerfLink24HrIntRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxFcsErrors.setStatus("current")
_AdGenEfmPerfLink24HrIntRxCodingErrors_Type = Gauge32
_AdGenEfmPerfLink24HrIntRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLink24HrIntRxCodingErrors = _AdGenEfmPerfLink24HrIntRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 8, 1, 9),
    _AdGenEfmPerfLink24HrIntRxCodingErrors_Type()
)
adGenEfmPerfLink24HrIntRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrIntRxCodingErrors.setStatus("current")
_AdGenEfmPerfResetTable_Object = MibTable
adGenEfmPerfResetTable = _AdGenEfmPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 9)
)
if mibBuilder.loadTexts:
    adGenEfmPerfResetTable.setStatus("current")
_AdGenEfmPerfResetEntry_Object = MibTableRow
adGenEfmPerfResetEntry = _AdGenEfmPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 9, 1)
)
adGenEfmPerfResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfResetEntry.setStatus("current")


class _AdGenEfmPerfResetGroupData_Type(Integer32):
    """Custom type adGenEfmPerfResetGroupData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenEfmPerfResetGroupData_Type.__name__ = "Integer32"
_AdGenEfmPerfResetGroupData_Object = MibTableColumn
adGenEfmPerfResetGroupData = _AdGenEfmPerfResetGroupData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 9, 1, 1),
    _AdGenEfmPerfResetGroupData_Type()
)
adGenEfmPerfResetGroupData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfResetGroupData.setStatus("current")


class _AdGenEfmPerfResetLinkData_Type(Integer32):
    """Custom type adGenEfmPerfResetLinkData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenEfmPerfResetLinkData_Type.__name__ = "Integer32"
_AdGenEfmPerfResetLinkData_Object = MibTableColumn
adGenEfmPerfResetLinkData = _AdGenEfmPerfResetLinkData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 9, 1, 2),
    _AdGenEfmPerfResetLinkData_Type()
)
adGenEfmPerfResetLinkData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfResetLinkData.setStatus("current")
_AdGenEfmPerfGroup15MinThreshTable_Object = MibTable
adGenEfmPerfGroup15MinThreshTable = _AdGenEfmPerfGroup15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 10)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinThreshTable.setStatus("current")
_AdGenEfmPerfGroup15MinThreshEntry_Object = MibTableRow
adGenEfmPerfGroup15MinThreshEntry = _AdGenEfmPerfGroup15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 10, 1)
)
adGenEfmPerfGroup15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinThreshEntry.setStatus("current")
_AdGenEfmPerfGroup15MinThreshRxBadFragments_Type = Unsigned32
_AdGenEfmPerfGroup15MinThreshRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroup15MinThreshRxBadFragments = _AdGenEfmPerfGroup15MinThreshRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 10, 1, 1),
    _AdGenEfmPerfGroup15MinThreshRxBadFragments_Type()
)
adGenEfmPerfGroup15MinThreshRxBadFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinThreshRxBadFragments.setStatus("current")
_AdGenEfmPerfGroup15MinThreshRxLostFragments_Type = Unsigned32
_AdGenEfmPerfGroup15MinThreshRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroup15MinThreshRxLostFragments = _AdGenEfmPerfGroup15MinThreshRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 10, 1, 2),
    _AdGenEfmPerfGroup15MinThreshRxLostFragments_Type()
)
adGenEfmPerfGroup15MinThreshRxLostFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinThreshRxLostFragments.setStatus("current")
_AdGenEfmPerfGroup15MinThreshRxLostStarts_Type = Unsigned32
_AdGenEfmPerfGroup15MinThreshRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroup15MinThreshRxLostStarts = _AdGenEfmPerfGroup15MinThreshRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 10, 1, 3),
    _AdGenEfmPerfGroup15MinThreshRxLostStarts_Type()
)
adGenEfmPerfGroup15MinThreshRxLostStarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinThreshRxLostStarts.setStatus("current")
_AdGenEfmPerfGroup15MinThreshRxLostEnds_Type = Unsigned32
_AdGenEfmPerfGroup15MinThreshRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroup15MinThreshRxLostEnds = _AdGenEfmPerfGroup15MinThreshRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 10, 1, 4),
    _AdGenEfmPerfGroup15MinThreshRxLostEnds_Type()
)
adGenEfmPerfGroup15MinThreshRxLostEnds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup15MinThreshRxLostEnds.setStatus("current")
_AdGenEfmPerfGroup24HrThreshTable_Object = MibTable
adGenEfmPerfGroup24HrThreshTable = _AdGenEfmPerfGroup24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 11)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrThreshTable.setStatus("current")
_AdGenEfmPerfGroup24HrThreshEntry_Object = MibTableRow
adGenEfmPerfGroup24HrThreshEntry = _AdGenEfmPerfGroup24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 11, 1)
)
adGenEfmPerfGroup24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrThreshEntry.setStatus("current")
_AdGenEfmPerfGroup24HrThreshRxBadFragments_Type = Unsigned32
_AdGenEfmPerfGroup24HrThreshRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroup24HrThreshRxBadFragments = _AdGenEfmPerfGroup24HrThreshRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 11, 1, 1),
    _AdGenEfmPerfGroup24HrThreshRxBadFragments_Type()
)
adGenEfmPerfGroup24HrThreshRxBadFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrThreshRxBadFragments.setStatus("current")
_AdGenEfmPerfGroup24HrThreshRxLostFragments_Type = Unsigned32
_AdGenEfmPerfGroup24HrThreshRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroup24HrThreshRxLostFragments = _AdGenEfmPerfGroup24HrThreshRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 11, 1, 2),
    _AdGenEfmPerfGroup24HrThreshRxLostFragments_Type()
)
adGenEfmPerfGroup24HrThreshRxLostFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrThreshRxLostFragments.setStatus("current")
_AdGenEfmPerfGroup24HrThreshRxLostStarts_Type = Unsigned32
_AdGenEfmPerfGroup24HrThreshRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroup24HrThreshRxLostStarts = _AdGenEfmPerfGroup24HrThreshRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 11, 1, 3),
    _AdGenEfmPerfGroup24HrThreshRxLostStarts_Type()
)
adGenEfmPerfGroup24HrThreshRxLostStarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrThreshRxLostStarts.setStatus("current")
_AdGenEfmPerfGroup24HrThreshRxLostEnds_Type = Unsigned32
_AdGenEfmPerfGroup24HrThreshRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroup24HrThreshRxLostEnds = _AdGenEfmPerfGroup24HrThreshRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 11, 1, 4),
    _AdGenEfmPerfGroup24HrThreshRxLostEnds_Type()
)
adGenEfmPerfGroup24HrThreshRxLostEnds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroup24HrThreshRxLostEnds.setStatus("current")
_AdGenEfmPerfLink15MinThreshTable_Object = MibTable
adGenEfmPerfLink15MinThreshTable = _AdGenEfmPerfLink15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshTable.setStatus("current")
_AdGenEfmPerfLink15MinThreshEntry_Object = MibTableRow
adGenEfmPerfLink15MinThreshEntry = _AdGenEfmPerfLink15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1)
)
adGenEfmPerfLink15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshEntry.setStatus("current")
_AdGenEfmPerfLink15MinThreshRxErroredFragments_Type = Unsigned32
_AdGenEfmPerfLink15MinThreshRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLink15MinThreshRxErroredFragments = _AdGenEfmPerfLink15MinThreshRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1, 1),
    _AdGenEfmPerfLink15MinThreshRxErroredFragments_Type()
)
adGenEfmPerfLink15MinThreshRxErroredFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshRxErroredFragments.setStatus("current")
_AdGenEfmPerfLink15MinThreshRxSmallFragments_Type = Unsigned32
_AdGenEfmPerfLink15MinThreshRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLink15MinThreshRxSmallFragments = _AdGenEfmPerfLink15MinThreshRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1, 2),
    _AdGenEfmPerfLink15MinThreshRxSmallFragments_Type()
)
adGenEfmPerfLink15MinThreshRxSmallFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshRxSmallFragments.setStatus("current")
_AdGenEfmPerfLink15MinThreshRxLargeFragments_Type = Unsigned32
_AdGenEfmPerfLink15MinThreshRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLink15MinThreshRxLargeFragments = _AdGenEfmPerfLink15MinThreshRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1, 3),
    _AdGenEfmPerfLink15MinThreshRxLargeFragments_Type()
)
adGenEfmPerfLink15MinThreshRxLargeFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshRxLargeFragments.setStatus("current")
_AdGenEfmPerfLink15MinThreshRxDiscardedFragments_Type = Unsigned32
_AdGenEfmPerfLink15MinThreshRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLink15MinThreshRxDiscardedFragments = _AdGenEfmPerfLink15MinThreshRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1, 4),
    _AdGenEfmPerfLink15MinThreshRxDiscardedFragments_Type()
)
adGenEfmPerfLink15MinThreshRxDiscardedFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLink15MinThreshRxFcsErrors_Type = Unsigned32
_AdGenEfmPerfLink15MinThreshRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLink15MinThreshRxFcsErrors = _AdGenEfmPerfLink15MinThreshRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1, 5),
    _AdGenEfmPerfLink15MinThreshRxFcsErrors_Type()
)
adGenEfmPerfLink15MinThreshRxFcsErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshRxFcsErrors.setStatus("current")
_AdGenEfmPerfLink15MinThreshRxCodingErrors_Type = Unsigned32
_AdGenEfmPerfLink15MinThreshRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLink15MinThreshRxCodingErrors = _AdGenEfmPerfLink15MinThreshRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 12, 1, 6),
    _AdGenEfmPerfLink15MinThreshRxCodingErrors_Type()
)
adGenEfmPerfLink15MinThreshRxCodingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink15MinThreshRxCodingErrors.setStatus("current")
_AdGenEfmPerfLink24HrThreshTable_Object = MibTable
adGenEfmPerfLink24HrThreshTable = _AdGenEfmPerfLink24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshTable.setStatus("current")
_AdGenEfmPerfLink24HrThreshEntry_Object = MibTableRow
adGenEfmPerfLink24HrThreshEntry = _AdGenEfmPerfLink24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1)
)
adGenEfmPerfLink24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-MIB", "adGenEfmUnitIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshEntry.setStatus("current")
_AdGenEfmPerfLink24HrThreshRxErroredFragments_Type = Unsigned32
_AdGenEfmPerfLink24HrThreshRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLink24HrThreshRxErroredFragments = _AdGenEfmPerfLink24HrThreshRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1, 1),
    _AdGenEfmPerfLink24HrThreshRxErroredFragments_Type()
)
adGenEfmPerfLink24HrThreshRxErroredFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshRxErroredFragments.setStatus("current")
_AdGenEfmPerfLink24HrThreshRxSmallFragments_Type = Unsigned32
_AdGenEfmPerfLink24HrThreshRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLink24HrThreshRxSmallFragments = _AdGenEfmPerfLink24HrThreshRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1, 2),
    _AdGenEfmPerfLink24HrThreshRxSmallFragments_Type()
)
adGenEfmPerfLink24HrThreshRxSmallFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshRxSmallFragments.setStatus("current")
_AdGenEfmPerfLink24HrThreshRxLargeFragments_Type = Unsigned32
_AdGenEfmPerfLink24HrThreshRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLink24HrThreshRxLargeFragments = _AdGenEfmPerfLink24HrThreshRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1, 3),
    _AdGenEfmPerfLink24HrThreshRxLargeFragments_Type()
)
adGenEfmPerfLink24HrThreshRxLargeFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshRxLargeFragments.setStatus("current")
_AdGenEfmPerfLink24HrThreshRxDiscardedFragments_Type = Unsigned32
_AdGenEfmPerfLink24HrThreshRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLink24HrThreshRxDiscardedFragments = _AdGenEfmPerfLink24HrThreshRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1, 4),
    _AdGenEfmPerfLink24HrThreshRxDiscardedFragments_Type()
)
adGenEfmPerfLink24HrThreshRxDiscardedFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLink24HrThreshRxFcsErrors_Type = Unsigned32
_AdGenEfmPerfLink24HrThreshRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLink24HrThreshRxFcsErrors = _AdGenEfmPerfLink24HrThreshRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1, 5),
    _AdGenEfmPerfLink24HrThreshRxFcsErrors_Type()
)
adGenEfmPerfLink24HrThreshRxFcsErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshRxFcsErrors.setStatus("current")
_AdGenEfmPerfLink24HrThreshRxCodingErrors_Type = Unsigned32
_AdGenEfmPerfLink24HrThreshRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLink24HrThreshRxCodingErrors = _AdGenEfmPerfLink24HrThreshRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 13, 1, 6),
    _AdGenEfmPerfLink24HrThreshRxCodingErrors_Type()
)
adGenEfmPerfLink24HrThreshRxCodingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLink24HrThreshRxCodingErrors.setStatus("current")
_AdGenEfmPerfGroupResetTable_Object = MibTable
adGenEfmPerfGroupResetTable = _AdGenEfmPerfGroupResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 14)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupResetTable.setStatus("current")
_AdGenEfmPerfGroupResetEntry_Object = MibTableRow
adGenEfmPerfGroupResetEntry = _AdGenEfmPerfGroupResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 14, 1)
)
adGenEfmPerfGroupResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupResetEntry.setStatus("current")


class _AdGenEfmPerfGroupReset_Type(Integer32):
    """Custom type adGenEfmPerfGroupReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenEfmPerfGroupReset_Type.__name__ = "Integer32"
_AdGenEfmPerfGroupReset_Object = MibTableColumn
adGenEfmPerfGroupReset = _AdGenEfmPerfGroupReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 14, 1, 1),
    _AdGenEfmPerfGroupReset_Type()
)
adGenEfmPerfGroupReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupReset.setStatus("current")
_AdGenEfmPerfLinkResetTable_Object = MibTable
adGenEfmPerfLinkResetTable = _AdGenEfmPerfLinkResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 15)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkResetTable.setStatus("current")
_AdGenEfmPerfLinkResetEntry_Object = MibTableRow
adGenEfmPerfLinkResetEntry = _AdGenEfmPerfLinkResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 15, 1)
)
adGenEfmPerfLinkResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkResetEntry.setStatus("current")


class _AdGenEfmPerfLinkReset_Type(Integer32):
    """Custom type adGenEfmPerfLinkReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenEfmPerfLinkReset_Type.__name__ = "Integer32"
_AdGenEfmPerfLinkReset_Object = MibTableColumn
adGenEfmPerfLinkReset = _AdGenEfmPerfLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 15, 1, 1),
    _AdGenEfmPerfLinkReset_Type()
)
adGenEfmPerfLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkReset.setStatus("current")
_AdGenEfmPerfGroupFreeRollingCountTable_Object = MibTable
adGenEfmPerfGroupFreeRollingCountTable = _AdGenEfmPerfGroupFreeRollingCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 16)
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupFreeRollingCountTable.setStatus("current")
_AdGenEfmPerfGroupFreeRollingCountEntry_Object = MibTableRow
adGenEfmPerfGroupFreeRollingCountEntry = _AdGenEfmPerfGroupFreeRollingCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 16, 1)
)
adGenEfmPerfGroupFreeRollingCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfGroupFreeRollingCountEntry.setStatus("current")
_AdGenEfmPerfGroupFreeRollingCountRxBadFragments_Type = Counter32
_AdGenEfmPerfGroupFreeRollingCountRxBadFragments_Object = MibTableColumn
adGenEfmPerfGroupFreeRollingCountRxBadFragments = _AdGenEfmPerfGroupFreeRollingCountRxBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 16, 1, 1),
    _AdGenEfmPerfGroupFreeRollingCountRxBadFragments_Type()
)
adGenEfmPerfGroupFreeRollingCountRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupFreeRollingCountRxBadFragments.setStatus("current")
_AdGenEfmPerfGroupFreeRollingCountRxLostFragments_Type = Counter32
_AdGenEfmPerfGroupFreeRollingCountRxLostFragments_Object = MibTableColumn
adGenEfmPerfGroupFreeRollingCountRxLostFragments = _AdGenEfmPerfGroupFreeRollingCountRxLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 16, 1, 2),
    _AdGenEfmPerfGroupFreeRollingCountRxLostFragments_Type()
)
adGenEfmPerfGroupFreeRollingCountRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupFreeRollingCountRxLostFragments.setStatus("current")
_AdGenEfmPerfGroupFreeRollingCountRxLostStarts_Type = Counter32
_AdGenEfmPerfGroupFreeRollingCountRxLostStarts_Object = MibTableColumn
adGenEfmPerfGroupFreeRollingCountRxLostStarts = _AdGenEfmPerfGroupFreeRollingCountRxLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 16, 1, 3),
    _AdGenEfmPerfGroupFreeRollingCountRxLostStarts_Type()
)
adGenEfmPerfGroupFreeRollingCountRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupFreeRollingCountRxLostStarts.setStatus("current")
_AdGenEfmPerfGroupFreeRollingCountRxLostEnds_Type = Counter32
_AdGenEfmPerfGroupFreeRollingCountRxLostEnds_Object = MibTableColumn
adGenEfmPerfGroupFreeRollingCountRxLostEnds = _AdGenEfmPerfGroupFreeRollingCountRxLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 16, 1, 4),
    _AdGenEfmPerfGroupFreeRollingCountRxLostEnds_Type()
)
adGenEfmPerfGroupFreeRollingCountRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfGroupFreeRollingCountRxLostEnds.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountTable_Object = MibTable
adGenEfmPerfLinkFreeRollingCountTable = _AdGenEfmPerfLinkFreeRollingCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17)
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountTable.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountEntry_Object = MibTableRow
adGenEfmPerfLinkFreeRollingCountEntry = _AdGenEfmPerfLinkFreeRollingCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1)
)
adGenEfmPerfLinkFreeRollingCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountEntry.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountTxFragments_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountTxFragments_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountTxFragments = _AdGenEfmPerfLinkFreeRollingCountTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 1),
    _AdGenEfmPerfLinkFreeRollingCountTxFragments_Type()
)
adGenEfmPerfLinkFreeRollingCountTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountTxFragments.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxFragments_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxFragments_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxFragments = _AdGenEfmPerfLinkFreeRollingCountRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 2),
    _AdGenEfmPerfLinkFreeRollingCountRxFragments_Type()
)
adGenEfmPerfLinkFreeRollingCountRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxFragments.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxErroredFragments_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxErroredFragments_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxErroredFragments = _AdGenEfmPerfLinkFreeRollingCountRxErroredFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 3),
    _AdGenEfmPerfLinkFreeRollingCountRxErroredFragments_Type()
)
adGenEfmPerfLinkFreeRollingCountRxErroredFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxErroredFragments.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxSmallFragments_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxSmallFragments_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxSmallFragments = _AdGenEfmPerfLinkFreeRollingCountRxSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 4),
    _AdGenEfmPerfLinkFreeRollingCountRxSmallFragments_Type()
)
adGenEfmPerfLinkFreeRollingCountRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxSmallFragments.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxLargeFragments_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxLargeFragments_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxLargeFragments = _AdGenEfmPerfLinkFreeRollingCountRxLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 5),
    _AdGenEfmPerfLinkFreeRollingCountRxLargeFragments_Type()
)
adGenEfmPerfLinkFreeRollingCountRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxLargeFragments.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxDiscardedFragments_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxDiscardedFragments_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxDiscardedFragments = _AdGenEfmPerfLinkFreeRollingCountRxDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 6),
    _AdGenEfmPerfLinkFreeRollingCountRxDiscardedFragments_Type()
)
adGenEfmPerfLinkFreeRollingCountRxDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxDiscardedFragments.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxFcsErrors_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxFcsErrors_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxFcsErrors = _AdGenEfmPerfLinkFreeRollingCountRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 7),
    _AdGenEfmPerfLinkFreeRollingCountRxFcsErrors_Type()
)
adGenEfmPerfLinkFreeRollingCountRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxFcsErrors.setStatus("current")
_AdGenEfmPerfLinkFreeRollingCountRxCodingErrors_Type = Counter32
_AdGenEfmPerfLinkFreeRollingCountRxCodingErrors_Object = MibTableColumn
adGenEfmPerfLinkFreeRollingCountRxCodingErrors = _AdGenEfmPerfLinkFreeRollingCountRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 6, 17, 1, 8),
    _AdGenEfmPerfLinkFreeRollingCountRxCodingErrors_Type()
)
adGenEfmPerfLinkFreeRollingCountRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmPerfLinkFreeRollingCountRxCodingErrors.setStatus("current")
_AdGenEfmMibConformance_ObjectIdentity = ObjectIdentity
adGenEfmMibConformance = _AdGenEfmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7)
)
_AdGenEfmMibGroups_ObjectIdentity = ObjectIdentity
adGenEfmMibGroups = _AdGenEfmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1)
)
_AdGenEfmAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenEfmAlarmsPrefix = _AdGenEfmAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10)
)
_AdGenEfmAlarms_ObjectIdentity = ObjectIdentity
adGenEfmAlarms = _AdGenEfmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0)
)

# Managed Objects groups

adGenEfmIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 1)
)
adGenEfmIndexGroup.setObjects(
    ("ADTRAN-EFM-MIB", "adGenEfmUnitIndex")
)
if mibBuilder.loadTexts:
    adGenEfmIndexGroup.setStatus("current")

adGenEfmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 2)
)
adGenEfmCfgGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmConfMaxGroups"),
        ("ADTRAN-EFM-MIB", "adGenEfmConfMaxGroupSize"))
)
if mibBuilder.loadTexts:
    adGenEfmCfgGroup.setStatus("current")

adGenEfmProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 3)
)
adGenEfmProvGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmProvErrorString"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupServiceState"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupFragmentSize"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupSkewThreshold"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupXCVThreshold"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvLinkAssignment"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupName"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupXCVLinkRemoval"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvGroupLoopbackDetection"),
        ("ADTRAN-EFM-MIB", "adGenEfmProvLinkIfAssignment"))
)
if mibBuilder.loadTexts:
    adGenEfmProvGroup.setStatus("current")

adGenEfmStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 4)
)
adGenEfmStatGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmStatGroupStatus"),
        ("ADTRAN-EFM-MIB", "adGenEfmStatGroupSize"),
        ("ADTRAN-EFM-MIB", "adGenEfmStatNumActiveLinks"),
        ("ADTRAN-EFM-MIB", "adGenEfmStatLinkNeTcSync"),
        ("ADTRAN-EFM-MIB", "adGenEfmStatLinkFeTcSync"))
)
if mibBuilder.loadTexts:
    adGenEfmStatGroup.setStatus("current")

adGenEfmTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 5)
)
adGenEfmTestGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmTestOamRemoteLoopback"),
        ("ADTRAN-EFM-MIB", "adGenEfmTestOamRemoteLoopbackTimeout"))
)
if mibBuilder.loadTexts:
    adGenEfmTestGroup.setStatus("current")

adGenEfmCurr15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 6)
)
adGenEfmCurr15MinPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinTxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinTxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxBadFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxLostFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxLostStarts"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxLostEnds"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinValidIntervals"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinTxPercUtil"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr15MinRxPercUtil"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinTxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxErroredFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxSmallFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxLargeFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxDiscardedFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxFcsErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr15MinRxCodingErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinValidIntervals"))
)
if mibBuilder.loadTexts:
    adGenEfmCurr15MinPerfGroup.setStatus("current")

adGenEfmCurr24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 7)
)
adGenEfmCurr24HrPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrTxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrTxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxBadFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxLostFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxLostStarts"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxLostEnds"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrValidIntervals"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrTxPercUtil"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupCurr24HrRxPercUtil"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrTxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxErroredFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxSmallFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxLargeFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxDiscardedFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxFcsErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkCurr24HrRxCodingErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrValidIntervals"))
)
if mibBuilder.loadTexts:
    adGenEfmCurr24HrPerfGroup.setStatus("current")

adGenEfmInt15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 8)
)
adGenEfmInt15MinPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntTxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntTxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxBadFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxLostFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxLostStarts"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxLostEnds"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntTxPercUtil"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinIntRxPercUtil"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntTxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxErroredFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxSmallFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxLargeFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxDiscardedFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxFcsErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinIntRxCodingErrors"))
)
if mibBuilder.loadTexts:
    adGenEfmInt15MinPerfGroup.setStatus("current")

adGenEfmInt24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 9)
)
adGenEfmInt24HrPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntTxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntTxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntRxOctets"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntRxFrames"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntRxBadFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntRxLostFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntRxLostStarts"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrIntRxLostEnds"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntTxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxErroredFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxSmallFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxLargeFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxDiscardedFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxFcsErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrIntRxCodingErrors"))
)
if mibBuilder.loadTexts:
    adGenEfmInt24HrPerfGroup.setStatus("current")

adGenEfmResetPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 10)
)
adGenEfmResetPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfResetGroupData"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfResetLinkData"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroupReset"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLinkReset"))
)
if mibBuilder.loadTexts:
    adGenEfmResetPerfGroup.setStatus("current")

adGenEfm15MinThreshPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 12)
)
adGenEfm15MinThreshPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinThreshRxBadFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinThreshRxLostFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinThreshRxLostStarts"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup15MinThreshRxLostEnds"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinThreshRxErroredFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinThreshRxSmallFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinThreshRxLargeFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinThreshRxDiscardedFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinThreshRxFcsErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink15MinThreshRxCodingErrors"))
)
if mibBuilder.loadTexts:
    adGenEfm15MinThreshPerfGroup.setStatus("current")

adGenEfm24HrThreshPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 13)
)
adGenEfm24HrThreshPerfGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrThreshRxBadFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrThreshRxLostFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrThreshRxLostStarts"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfGroup24HrThreshRxLostEnds"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrThreshRxErroredFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrThreshRxSmallFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrThreshRxLargeFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrThreshRxDiscardedFragments"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrThreshRxFcsErrors"),
        ("ADTRAN-EFM-MIB", "adGenEfmPerfLink24HrThreshRxCodingErrors"))
)
if mibBuilder.loadTexts:
    adGenEfm24HrThreshPerfGroup.setStatus("current")


# Notification objects

adGenEfmGroupDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 2)
)
adGenEfmGroupDownClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownClr.setStatus(
        "current"
    )

adGenEfmGroupDownAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 3)
)
adGenEfmGroupDownAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownAct.setStatus(
        "current"
    )

adGenEfmLinkDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 4)
)
adGenEfmLinkDownClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLinkDownClr.setStatus(
        "current"
    )

adGenEfmLinkDownAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 5)
)
adGenEfmLinkDownAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLinkDownAct.setStatus(
        "current"
    )

adGenEfmGroupDownPartialClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 6)
)
adGenEfmGroupDownPartialClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownPartialClr.setStatus(
        "current"
    )

adGenEfmGroupDownPartialAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 7)
)
adGenEfmGroupDownPartialAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownPartialAct.setStatus(
        "current"
    )

adGenEfmGroupDownstreamBandwidthClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 8)
)
adGenEfmGroupDownstreamBandwidthClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownstreamBandwidthClr.setStatus(
        "current"
    )

adGenEfmGroupDownstreamBandwidthAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 9)
)
adGenEfmGroupDownstreamBandwidthAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownstreamBandwidthAct.setStatus(
        "current"
    )

adGenEfmGroupUpstreamBandwidthClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 10)
)
adGenEfmGroupUpstreamBandwidthClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupUpstreamBandwidthClr.setStatus(
        "current"
    )

adGenEfmGroupUpstreamBandwidthAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 11)
)
adGenEfmGroupUpstreamBandwidthAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupUpstreamBandwidthAct.setStatus(
        "current"
    )

adGenEfmGroupDownstream4xRateViolationClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 12)
)
adGenEfmGroupDownstream4xRateViolationClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownstream4xRateViolationClr.setStatus(
        "current"
    )

adGenEfmGroupDownstream4xRateViolationAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 13)
)
adGenEfmGroupDownstream4xRateViolationAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupDownstream4xRateViolationAct.setStatus(
        "current"
    )

adGenEfmGroupUpstream4xRateViolationClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 14)
)
adGenEfmGroupUpstream4xRateViolationClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupUpstream4xRateViolationClr.setStatus(
        "current"
    )

adGenEfmGroupUpstream4xRateViolationAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 15)
)
adGenEfmGroupUpstream4xRateViolationAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroupUpstream4xRateViolationAct.setStatus(
        "current"
    )

adGenEfmGroup15MinRxBadFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 20)
)
adGenEfmGroup15MinRxBadFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup15MinRxBadFragmentsAct.setStatus(
        "current"
    )

adGenEfmGroup15MinRxLostFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 21)
)
adGenEfmGroup15MinRxLostFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup15MinRxLostFragmentsAct.setStatus(
        "current"
    )

adGenEfmGroup15MinRxLostStartsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 22)
)
adGenEfmGroup15MinRxLostStartsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup15MinRxLostStartsAct.setStatus(
        "current"
    )

adGenEfmGroup15MinRxLostEndsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 23)
)
adGenEfmGroup15MinRxLostEndsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup15MinRxLostEndsAct.setStatus(
        "current"
    )

adGenEfmGroup24HrRxBadFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 24)
)
adGenEfmGroup24HrRxBadFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup24HrRxBadFragmentsAct.setStatus(
        "current"
    )

adGenEfmGroup24HrRxLostFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 25)
)
adGenEfmGroup24HrRxLostFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup24HrRxLostFragmentsAct.setStatus(
        "current"
    )

adGenEfmGroup24HrRxLostStartsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 26)
)
adGenEfmGroup24HrRxLostStartsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup24HrRxLostStartsAct.setStatus(
        "current"
    )

adGenEfmGroup24HrRxLostEndsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 27)
)
adGenEfmGroup24HrRxLostEndsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmGroup24HrRxLostEndsAct.setStatus(
        "current"
    )

adGenEfmLink15MinRxErroredFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 28)
)
adGenEfmLink15MinRxErroredFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink15MinRxErroredFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink15MinRxSmallFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 29)
)
adGenEfmLink15MinRxSmallFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink15MinRxSmallFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink15MinRxLargeFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 30)
)
adGenEfmLink15MinRxLargeFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink15MinRxLargeFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink15MinRxDiscardedFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 31)
)
adGenEfmLink15MinRxDiscardedFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink15MinRxDiscardedFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink15MinRxFcsErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 32)
)
adGenEfmLink15MinRxFcsErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink15MinRxFcsErrorsAct.setStatus(
        "current"
    )

adGenEfmLink15MinRxCodingErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 33)
)
adGenEfmLink15MinRxCodingErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink15MinRxCodingErrorsAct.setStatus(
        "current"
    )

adGenEfmLink24HrRxErroredFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 34)
)
adGenEfmLink24HrRxErroredFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink24HrRxErroredFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink24HrRxSmallFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 35)
)
adGenEfmLink24HrRxSmallFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink24HrRxSmallFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink24HrRxLargeFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 36)
)
adGenEfmLink24HrRxLargeFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink24HrRxLargeFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink24HrRxDiscardedFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 37)
)
adGenEfmLink24HrRxDiscardedFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink24HrRxDiscardedFragmentsAct.setStatus(
        "current"
    )

adGenEfmLink24HrRxFcsErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 38)
)
adGenEfmLink24HrRxFcsErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink24HrRxFcsErrorsAct.setStatus(
        "current"
    )

adGenEfmLink24HrRxCodingErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 10, 0, 39)
)
adGenEfmLink24HrRxCodingErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmLink24HrRxCodingErrorsAct.setStatus(
        "current"
    )


# Notifications groups

adGenEfmEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 1, 7, 1, 11)
)
adGenEfmEventGroup.setObjects(
      *(("ADTRAN-EFM-MIB", "adGenEfmGroupDownClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLinkDownClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmLinkDownAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownPartialClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownPartialAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownstreamBandwidthClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownstreamBandwidthAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupUpstreamBandwidthClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupUpstreamBandwidthAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownstream4xRateViolationClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupDownstream4xRateViolationAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupUpstream4xRateViolationClr"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroupUpstream4xRateViolationAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup15MinRxBadFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup15MinRxLostFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup15MinRxLostStartsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup15MinRxLostEndsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup24HrRxBadFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup24HrRxLostFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup24HrRxLostStartsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmGroup24HrRxLostEndsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink15MinRxErroredFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink15MinRxSmallFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink15MinRxLargeFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink15MinRxDiscardedFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink15MinRxFcsErrorsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink15MinRxCodingErrorsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink24HrRxErroredFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink24HrRxSmallFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink24HrRxLargeFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink24HrRxDiscardedFragmentsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink24HrRxFcsErrorsAct"),
        ("ADTRAN-EFM-MIB", "adGenEfmLink24HrRxCodingErrorsAct"))
)
if mibBuilder.loadTexts:
    adGenEfmEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-EFM-MIB",
    **{"adGenEfmIndex": adGenEfmIndex,
       "adGenEfmIndexTable": adGenEfmIndexTable,
       "adGenEfmIndexEntry": adGenEfmIndexEntry,
       "adGenEfmUnitIndex": adGenEfmUnitIndex,
       "adGenEfmConfiguration": adGenEfmConfiguration,
       "adGenEfmConfTable": adGenEfmConfTable,
       "adGenEfmConfEntry": adGenEfmConfEntry,
       "adGenEfmConfMaxGroups": adGenEfmConfMaxGroups,
       "adGenEfmConfMaxGroupSize": adGenEfmConfMaxGroupSize,
       "adGenEfmProvisioning": adGenEfmProvisioning,
       "adGenEfmProvTable": adGenEfmProvTable,
       "adGenEfmProvEntry": adGenEfmProvEntry,
       "adGenEfmProvErrorString": adGenEfmProvErrorString,
       "adGenEfmProvGroupTable": adGenEfmProvGroupTable,
       "adGenEfmProvGroupEntry": adGenEfmProvGroupEntry,
       "adGenEfmProvGroupServiceState": adGenEfmProvGroupServiceState,
       "adGenEfmProvGroupFragmentSize": adGenEfmProvGroupFragmentSize,
       "adGenEfmProvGroupSkewThreshold": adGenEfmProvGroupSkewThreshold,
       "adGenEfmProvGroupXCVThreshold": adGenEfmProvGroupXCVThreshold,
       "adGenEfmProvGroupName": adGenEfmProvGroupName,
       "adGenEfmProvGroupCRCMode": adGenEfmProvGroupCRCMode,
       "adGenEfmProvGroupXCVLinkRemoval": adGenEfmProvGroupXCVLinkRemoval,
       "adGenEfmProvGroupLoopbackDetection": adGenEfmProvGroupLoopbackDetection,
       "adGenEfmProvGroupTrapReportingGroupDown": adGenEfmProvGroupTrapReportingGroupDown,
       "adGenEfmProvGroupTrapReportingGroupPartial": adGenEfmProvGroupTrapReportingGroupPartial,
       "adGenEfmProvGroupDownlinkEnable": adGenEfmProvGroupDownlinkEnable,
       "adGenEfmProvLinkTable": adGenEfmProvLinkTable,
       "adGenEfmProvLinkEntry": adGenEfmProvLinkEntry,
       "adGenEfmProvLinkAssignment": adGenEfmProvLinkAssignment,
       "adGenEfmProvLinkIfAssignment": adGenEfmProvLinkIfAssignment,
       "adGenEfmProvLinkTrapReportingLinkDown": adGenEfmProvLinkTrapReportingLinkDown,
       "adGenEfmProvGroupAlarmSlotTable": adGenEfmProvGroupAlarmSlotTable,
       "adGenEfmProvGroupAlarmSlotEntry": adGenEfmProvGroupAlarmSlotEntry,
       "adGenEfmProvGroupAlarmSlotGroupDownSeverity": adGenEfmProvGroupAlarmSlotGroupDownSeverity,
       "adGenEfmProvGroupAlarmSlotGroupPartialSeverity": adGenEfmProvGroupAlarmSlotGroupPartialSeverity,
       "adGenEfmStatus": adGenEfmStatus,
       "adGenEfmStatTable": adGenEfmStatTable,
       "adGenEfmStatEntry": adGenEfmStatEntry,
       "adGenEfmStatGroupStatus": adGenEfmStatGroupStatus,
       "adGenEfmStatGroupSize": adGenEfmStatGroupSize,
       "adGenEfmStatNumActiveLinks": adGenEfmStatNumActiveLinks,
       "adGenEfmStatLinkNeTcSync": adGenEfmStatLinkNeTcSync,
       "adGenEfmStatLinkFeTcSync": adGenEfmStatLinkFeTcSync,
       "adGenEfmStatLinkSkew": adGenEfmStatLinkSkew,
       "adGenEfmTest": adGenEfmTest,
       "adGenEfmTestTable": adGenEfmTestTable,
       "adGenEfmTestEntry": adGenEfmTestEntry,
       "adGenEfmTestOamRemoteLoopback": adGenEfmTestOamRemoteLoopback,
       "adGenEfmTestOamRemoteLoopbackTimeout": adGenEfmTestOamRemoteLoopbackTimeout,
       "adGenEfmPerformance": adGenEfmPerformance,
       "adGenEfmPerfGroupCurr15MinTable": adGenEfmPerfGroupCurr15MinTable,
       "adGenEfmPerfGroupCurr15MinEntry": adGenEfmPerfGroupCurr15MinEntry,
       "adGenEfmPerfGroupCurr15MinTxOctets": adGenEfmPerfGroupCurr15MinTxOctets,
       "adGenEfmPerfGroupCurr15MinTxFrames": adGenEfmPerfGroupCurr15MinTxFrames,
       "adGenEfmPerfGroupCurr15MinRxOctets": adGenEfmPerfGroupCurr15MinRxOctets,
       "adGenEfmPerfGroupCurr15MinRxFrames": adGenEfmPerfGroupCurr15MinRxFrames,
       "adGenEfmPerfGroupCurr15MinRxBadFragments": adGenEfmPerfGroupCurr15MinRxBadFragments,
       "adGenEfmPerfGroupCurr15MinRxLostFragments": adGenEfmPerfGroupCurr15MinRxLostFragments,
       "adGenEfmPerfGroupCurr15MinRxLostStarts": adGenEfmPerfGroupCurr15MinRxLostStarts,
       "adGenEfmPerfGroupCurr15MinRxLostEnds": adGenEfmPerfGroupCurr15MinRxLostEnds,
       "adGenEfmPerfGroup15MinValidIntervals": adGenEfmPerfGroup15MinValidIntervals,
       "adGenEfmPerfGroupCurr15MinTxPercUtil": adGenEfmPerfGroupCurr15MinTxPercUtil,
       "adGenEfmPerfGroupCurr15MinRxPercUtil": adGenEfmPerfGroupCurr15MinRxPercUtil,
       "adGenEfmPerfGroupCurr24HrTable": adGenEfmPerfGroupCurr24HrTable,
       "adGenEfmPerfGroupCurr24HrEntry": adGenEfmPerfGroupCurr24HrEntry,
       "adGenEfmPerfGroupCurr24HrTxOctets": adGenEfmPerfGroupCurr24HrTxOctets,
       "adGenEfmPerfGroupCurr24HrTxFrames": adGenEfmPerfGroupCurr24HrTxFrames,
       "adGenEfmPerfGroupCurr24HrRxOctets": adGenEfmPerfGroupCurr24HrRxOctets,
       "adGenEfmPerfGroupCurr24HrRxFrames": adGenEfmPerfGroupCurr24HrRxFrames,
       "adGenEfmPerfGroupCurr24HrRxBadFragments": adGenEfmPerfGroupCurr24HrRxBadFragments,
       "adGenEfmPerfGroupCurr24HrRxLostFragments": adGenEfmPerfGroupCurr24HrRxLostFragments,
       "adGenEfmPerfGroupCurr24HrRxLostStarts": adGenEfmPerfGroupCurr24HrRxLostStarts,
       "adGenEfmPerfGroupCurr24HrRxLostEnds": adGenEfmPerfGroupCurr24HrRxLostEnds,
       "adGenEfmPerfGroup24HrValidIntervals": adGenEfmPerfGroup24HrValidIntervals,
       "adGenEfmPerfGroupCurr24HrTxPercUtil": adGenEfmPerfGroupCurr24HrTxPercUtil,
       "adGenEfmPerfGroupCurr24HrRxPercUtil": adGenEfmPerfGroupCurr24HrRxPercUtil,
       "adGenEfmPerfGroup15MinIntTable": adGenEfmPerfGroup15MinIntTable,
       "adGenEfmPerfGroup15MinIntEntry": adGenEfmPerfGroup15MinIntEntry,
       "adGenEfmPerfGroup15MinIntNumber": adGenEfmPerfGroup15MinIntNumber,
       "adGenEfmPerfGroup15MinIntTxOctets": adGenEfmPerfGroup15MinIntTxOctets,
       "adGenEfmPerfGroup15MinIntTxFrames": adGenEfmPerfGroup15MinIntTxFrames,
       "adGenEfmPerfGroup15MinIntRxOctets": adGenEfmPerfGroup15MinIntRxOctets,
       "adGenEfmPerfGroup15MinIntRxFrames": adGenEfmPerfGroup15MinIntRxFrames,
       "adGenEfmPerfGroup15MinIntRxBadFragments": adGenEfmPerfGroup15MinIntRxBadFragments,
       "adGenEfmPerfGroup15MinIntRxLostFragments": adGenEfmPerfGroup15MinIntRxLostFragments,
       "adGenEfmPerfGroup15MinIntRxLostStarts": adGenEfmPerfGroup15MinIntRxLostStarts,
       "adGenEfmPerfGroup15MinIntRxLostEnds": adGenEfmPerfGroup15MinIntRxLostEnds,
       "adGenEfmPerfGroup15MinIntTxPercUtil": adGenEfmPerfGroup15MinIntTxPercUtil,
       "adGenEfmPerfGroup15MinIntRxPercUtil": adGenEfmPerfGroup15MinIntRxPercUtil,
       "adGenEfmPerfGroup24HrIntTable": adGenEfmPerfGroup24HrIntTable,
       "adGenEfmPerfGroup24HrIntEntry": adGenEfmPerfGroup24HrIntEntry,
       "adGenEfmPerfGroup24HrIntNumber": adGenEfmPerfGroup24HrIntNumber,
       "adGenEfmPerfGroup24HrIntTxOctets": adGenEfmPerfGroup24HrIntTxOctets,
       "adGenEfmPerfGroup24HrIntTxFrames": adGenEfmPerfGroup24HrIntTxFrames,
       "adGenEfmPerfGroup24HrIntRxOctets": adGenEfmPerfGroup24HrIntRxOctets,
       "adGenEfmPerfGroup24HrIntRxFrames": adGenEfmPerfGroup24HrIntRxFrames,
       "adGenEfmPerfGroup24HrIntRxBadFragments": adGenEfmPerfGroup24HrIntRxBadFragments,
       "adGenEfmPerfGroup24HrIntRxLostFragments": adGenEfmPerfGroup24HrIntRxLostFragments,
       "adGenEfmPerfGroup24HrIntRxLostStarts": adGenEfmPerfGroup24HrIntRxLostStarts,
       "adGenEfmPerfGroup24HrIntRxLostEnds": adGenEfmPerfGroup24HrIntRxLostEnds,
       "adGenEfmPerfGroup24HrIntTxPercUtil": adGenEfmPerfGroup24HrIntTxPercUtil,
       "adGenEfmPerfGroup24HrIntRxPercUtil": adGenEfmPerfGroup24HrIntRxPercUtil,
       "adGenEfmPerfLinkCurr15MinTable": adGenEfmPerfLinkCurr15MinTable,
       "adGenEfmPerfLinkCurr15MinEntry": adGenEfmPerfLinkCurr15MinEntry,
       "adGenEfmPerfLinkCurr15MinTxFragments": adGenEfmPerfLinkCurr15MinTxFragments,
       "adGenEfmPerfLinkCurr15MinRxFragments": adGenEfmPerfLinkCurr15MinRxFragments,
       "adGenEfmPerfLinkCurr15MinRxErroredFragments": adGenEfmPerfLinkCurr15MinRxErroredFragments,
       "adGenEfmPerfLinkCurr15MinRxSmallFragments": adGenEfmPerfLinkCurr15MinRxSmallFragments,
       "adGenEfmPerfLinkCurr15MinRxLargeFragments": adGenEfmPerfLinkCurr15MinRxLargeFragments,
       "adGenEfmPerfLinkCurr15MinRxDiscardedFragments": adGenEfmPerfLinkCurr15MinRxDiscardedFragments,
       "adGenEfmPerfLinkCurr15MinRxFcsErrors": adGenEfmPerfLinkCurr15MinRxFcsErrors,
       "adGenEfmPerfLinkCurr15MinRxCodingErrors": adGenEfmPerfLinkCurr15MinRxCodingErrors,
       "adGenEfmPerfLink15MinValidIntervals": adGenEfmPerfLink15MinValidIntervals,
       "adGenEfmPerfLinkCurr24HrTable": adGenEfmPerfLinkCurr24HrTable,
       "adGenEfmPerfLinkCurr24HrEntry": adGenEfmPerfLinkCurr24HrEntry,
       "adGenEfmPerfLinkCurr24HrTxFragments": adGenEfmPerfLinkCurr24HrTxFragments,
       "adGenEfmPerfLinkCurr24HrRxFragments": adGenEfmPerfLinkCurr24HrRxFragments,
       "adGenEfmPerfLinkCurr24HrRxErroredFragments": adGenEfmPerfLinkCurr24HrRxErroredFragments,
       "adGenEfmPerfLinkCurr24HrRxSmallFragments": adGenEfmPerfLinkCurr24HrRxSmallFragments,
       "adGenEfmPerfLinkCurr24HrRxLargeFragments": adGenEfmPerfLinkCurr24HrRxLargeFragments,
       "adGenEfmPerfLinkCurr24HrRxDiscardedFragments": adGenEfmPerfLinkCurr24HrRxDiscardedFragments,
       "adGenEfmPerfLinkCurr24HrRxFcsErrors": adGenEfmPerfLinkCurr24HrRxFcsErrors,
       "adGenEfmPerfLinkCurr24HrRxCodingErrors": adGenEfmPerfLinkCurr24HrRxCodingErrors,
       "adGenEfmPerfLink24HrValidIntervals": adGenEfmPerfLink24HrValidIntervals,
       "adGenEfmPerfLink15MinIntTable": adGenEfmPerfLink15MinIntTable,
       "adGenEfmPerfLink15MinIntEntry": adGenEfmPerfLink15MinIntEntry,
       "adGenEfmPerfLink15MinIntNumber": adGenEfmPerfLink15MinIntNumber,
       "adGenEfmPerfLink15MinIntTxFragments": adGenEfmPerfLink15MinIntTxFragments,
       "adGenEfmPerfLink15MinIntRxFragments": adGenEfmPerfLink15MinIntRxFragments,
       "adGenEfmPerfLink15MinIntRxErroredFragments": adGenEfmPerfLink15MinIntRxErroredFragments,
       "adGenEfmPerfLink15MinIntRxSmallFragments": adGenEfmPerfLink15MinIntRxSmallFragments,
       "adGenEfmPerfLink15MinIntRxLargeFragments": adGenEfmPerfLink15MinIntRxLargeFragments,
       "adGenEfmPerfLink15MinIntRxDiscardedFragments": adGenEfmPerfLink15MinIntRxDiscardedFragments,
       "adGenEfmPerfLink15MinIntRxFcsErrors": adGenEfmPerfLink15MinIntRxFcsErrors,
       "adGenEfmPerfLink15MinIntRxCodingErrors": adGenEfmPerfLink15MinIntRxCodingErrors,
       "adGenEfmPerfLink24HrIntTable": adGenEfmPerfLink24HrIntTable,
       "adGenEfmPerfLink24HrIntEntry": adGenEfmPerfLink24HrIntEntry,
       "adGenEfmPerfLink24HrIntNumber": adGenEfmPerfLink24HrIntNumber,
       "adGenEfmPerfLink24HrIntTxFragments": adGenEfmPerfLink24HrIntTxFragments,
       "adGenEfmPerfLink24HrIntRxFragments": adGenEfmPerfLink24HrIntRxFragments,
       "adGenEfmPerfLink24HrIntRxErroredFragments": adGenEfmPerfLink24HrIntRxErroredFragments,
       "adGenEfmPerfLink24HrIntRxSmallFragments": adGenEfmPerfLink24HrIntRxSmallFragments,
       "adGenEfmPerfLink24HrIntRxLargeFragments": adGenEfmPerfLink24HrIntRxLargeFragments,
       "adGenEfmPerfLink24HrIntRxDiscardedFragments": adGenEfmPerfLink24HrIntRxDiscardedFragments,
       "adGenEfmPerfLink24HrIntRxFcsErrors": adGenEfmPerfLink24HrIntRxFcsErrors,
       "adGenEfmPerfLink24HrIntRxCodingErrors": adGenEfmPerfLink24HrIntRxCodingErrors,
       "adGenEfmPerfResetTable": adGenEfmPerfResetTable,
       "adGenEfmPerfResetEntry": adGenEfmPerfResetEntry,
       "adGenEfmPerfResetGroupData": adGenEfmPerfResetGroupData,
       "adGenEfmPerfResetLinkData": adGenEfmPerfResetLinkData,
       "adGenEfmPerfGroup15MinThreshTable": adGenEfmPerfGroup15MinThreshTable,
       "adGenEfmPerfGroup15MinThreshEntry": adGenEfmPerfGroup15MinThreshEntry,
       "adGenEfmPerfGroup15MinThreshRxBadFragments": adGenEfmPerfGroup15MinThreshRxBadFragments,
       "adGenEfmPerfGroup15MinThreshRxLostFragments": adGenEfmPerfGroup15MinThreshRxLostFragments,
       "adGenEfmPerfGroup15MinThreshRxLostStarts": adGenEfmPerfGroup15MinThreshRxLostStarts,
       "adGenEfmPerfGroup15MinThreshRxLostEnds": adGenEfmPerfGroup15MinThreshRxLostEnds,
       "adGenEfmPerfGroup24HrThreshTable": adGenEfmPerfGroup24HrThreshTable,
       "adGenEfmPerfGroup24HrThreshEntry": adGenEfmPerfGroup24HrThreshEntry,
       "adGenEfmPerfGroup24HrThreshRxBadFragments": adGenEfmPerfGroup24HrThreshRxBadFragments,
       "adGenEfmPerfGroup24HrThreshRxLostFragments": adGenEfmPerfGroup24HrThreshRxLostFragments,
       "adGenEfmPerfGroup24HrThreshRxLostStarts": adGenEfmPerfGroup24HrThreshRxLostStarts,
       "adGenEfmPerfGroup24HrThreshRxLostEnds": adGenEfmPerfGroup24HrThreshRxLostEnds,
       "adGenEfmPerfLink15MinThreshTable": adGenEfmPerfLink15MinThreshTable,
       "adGenEfmPerfLink15MinThreshEntry": adGenEfmPerfLink15MinThreshEntry,
       "adGenEfmPerfLink15MinThreshRxErroredFragments": adGenEfmPerfLink15MinThreshRxErroredFragments,
       "adGenEfmPerfLink15MinThreshRxSmallFragments": adGenEfmPerfLink15MinThreshRxSmallFragments,
       "adGenEfmPerfLink15MinThreshRxLargeFragments": adGenEfmPerfLink15MinThreshRxLargeFragments,
       "adGenEfmPerfLink15MinThreshRxDiscardedFragments": adGenEfmPerfLink15MinThreshRxDiscardedFragments,
       "adGenEfmPerfLink15MinThreshRxFcsErrors": adGenEfmPerfLink15MinThreshRxFcsErrors,
       "adGenEfmPerfLink15MinThreshRxCodingErrors": adGenEfmPerfLink15MinThreshRxCodingErrors,
       "adGenEfmPerfLink24HrThreshTable": adGenEfmPerfLink24HrThreshTable,
       "adGenEfmPerfLink24HrThreshEntry": adGenEfmPerfLink24HrThreshEntry,
       "adGenEfmPerfLink24HrThreshRxErroredFragments": adGenEfmPerfLink24HrThreshRxErroredFragments,
       "adGenEfmPerfLink24HrThreshRxSmallFragments": adGenEfmPerfLink24HrThreshRxSmallFragments,
       "adGenEfmPerfLink24HrThreshRxLargeFragments": adGenEfmPerfLink24HrThreshRxLargeFragments,
       "adGenEfmPerfLink24HrThreshRxDiscardedFragments": adGenEfmPerfLink24HrThreshRxDiscardedFragments,
       "adGenEfmPerfLink24HrThreshRxFcsErrors": adGenEfmPerfLink24HrThreshRxFcsErrors,
       "adGenEfmPerfLink24HrThreshRxCodingErrors": adGenEfmPerfLink24HrThreshRxCodingErrors,
       "adGenEfmPerfGroupResetTable": adGenEfmPerfGroupResetTable,
       "adGenEfmPerfGroupResetEntry": adGenEfmPerfGroupResetEntry,
       "adGenEfmPerfGroupReset": adGenEfmPerfGroupReset,
       "adGenEfmPerfLinkResetTable": adGenEfmPerfLinkResetTable,
       "adGenEfmPerfLinkResetEntry": adGenEfmPerfLinkResetEntry,
       "adGenEfmPerfLinkReset": adGenEfmPerfLinkReset,
       "adGenEfmPerfGroupFreeRollingCountTable": adGenEfmPerfGroupFreeRollingCountTable,
       "adGenEfmPerfGroupFreeRollingCountEntry": adGenEfmPerfGroupFreeRollingCountEntry,
       "adGenEfmPerfGroupFreeRollingCountRxBadFragments": adGenEfmPerfGroupFreeRollingCountRxBadFragments,
       "adGenEfmPerfGroupFreeRollingCountRxLostFragments": adGenEfmPerfGroupFreeRollingCountRxLostFragments,
       "adGenEfmPerfGroupFreeRollingCountRxLostStarts": adGenEfmPerfGroupFreeRollingCountRxLostStarts,
       "adGenEfmPerfGroupFreeRollingCountRxLostEnds": adGenEfmPerfGroupFreeRollingCountRxLostEnds,
       "adGenEfmPerfLinkFreeRollingCountTable": adGenEfmPerfLinkFreeRollingCountTable,
       "adGenEfmPerfLinkFreeRollingCountEntry": adGenEfmPerfLinkFreeRollingCountEntry,
       "adGenEfmPerfLinkFreeRollingCountTxFragments": adGenEfmPerfLinkFreeRollingCountTxFragments,
       "adGenEfmPerfLinkFreeRollingCountRxFragments": adGenEfmPerfLinkFreeRollingCountRxFragments,
       "adGenEfmPerfLinkFreeRollingCountRxErroredFragments": adGenEfmPerfLinkFreeRollingCountRxErroredFragments,
       "adGenEfmPerfLinkFreeRollingCountRxSmallFragments": adGenEfmPerfLinkFreeRollingCountRxSmallFragments,
       "adGenEfmPerfLinkFreeRollingCountRxLargeFragments": adGenEfmPerfLinkFreeRollingCountRxLargeFragments,
       "adGenEfmPerfLinkFreeRollingCountRxDiscardedFragments": adGenEfmPerfLinkFreeRollingCountRxDiscardedFragments,
       "adGenEfmPerfLinkFreeRollingCountRxFcsErrors": adGenEfmPerfLinkFreeRollingCountRxFcsErrors,
       "adGenEfmPerfLinkFreeRollingCountRxCodingErrors": adGenEfmPerfLinkFreeRollingCountRxCodingErrors,
       "adGenEfmMibConformance": adGenEfmMibConformance,
       "adGenEfmMibGroups": adGenEfmMibGroups,
       "adGenEfmIndexGroup": adGenEfmIndexGroup,
       "adGenEfmCfgGroup": adGenEfmCfgGroup,
       "adGenEfmProvGroup": adGenEfmProvGroup,
       "adGenEfmStatGroup": adGenEfmStatGroup,
       "adGenEfmTestGroup": adGenEfmTestGroup,
       "adGenEfmCurr15MinPerfGroup": adGenEfmCurr15MinPerfGroup,
       "adGenEfmCurr24HrPerfGroup": adGenEfmCurr24HrPerfGroup,
       "adGenEfmInt15MinPerfGroup": adGenEfmInt15MinPerfGroup,
       "adGenEfmInt24HrPerfGroup": adGenEfmInt24HrPerfGroup,
       "adGenEfmResetPerfGroup": adGenEfmResetPerfGroup,
       "adGenEfmEventGroup": adGenEfmEventGroup,
       "adGenEfm15MinThreshPerfGroup": adGenEfm15MinThreshPerfGroup,
       "adGenEfm24HrThreshPerfGroup": adGenEfm24HrThreshPerfGroup,
       "adGenEfmAlarmsPrefix": adGenEfmAlarmsPrefix,
       "adGenEfmAlarms": adGenEfmAlarms,
       "adGenEfmGroupDownClr": adGenEfmGroupDownClr,
       "adGenEfmGroupDownAct": adGenEfmGroupDownAct,
       "adGenEfmLinkDownClr": adGenEfmLinkDownClr,
       "adGenEfmLinkDownAct": adGenEfmLinkDownAct,
       "adGenEfmGroupDownPartialClr": adGenEfmGroupDownPartialClr,
       "adGenEfmGroupDownPartialAct": adGenEfmGroupDownPartialAct,
       "adGenEfmGroupDownstreamBandwidthClr": adGenEfmGroupDownstreamBandwidthClr,
       "adGenEfmGroupDownstreamBandwidthAct": adGenEfmGroupDownstreamBandwidthAct,
       "adGenEfmGroupUpstreamBandwidthClr": adGenEfmGroupUpstreamBandwidthClr,
       "adGenEfmGroupUpstreamBandwidthAct": adGenEfmGroupUpstreamBandwidthAct,
       "adGenEfmGroupDownstream4xRateViolationClr": adGenEfmGroupDownstream4xRateViolationClr,
       "adGenEfmGroupDownstream4xRateViolationAct": adGenEfmGroupDownstream4xRateViolationAct,
       "adGenEfmGroupUpstream4xRateViolationClr": adGenEfmGroupUpstream4xRateViolationClr,
       "adGenEfmGroupUpstream4xRateViolationAct": adGenEfmGroupUpstream4xRateViolationAct,
       "adGenEfmGroup15MinRxBadFragmentsAct": adGenEfmGroup15MinRxBadFragmentsAct,
       "adGenEfmGroup15MinRxLostFragmentsAct": adGenEfmGroup15MinRxLostFragmentsAct,
       "adGenEfmGroup15MinRxLostStartsAct": adGenEfmGroup15MinRxLostStartsAct,
       "adGenEfmGroup15MinRxLostEndsAct": adGenEfmGroup15MinRxLostEndsAct,
       "adGenEfmGroup24HrRxBadFragmentsAct": adGenEfmGroup24HrRxBadFragmentsAct,
       "adGenEfmGroup24HrRxLostFragmentsAct": adGenEfmGroup24HrRxLostFragmentsAct,
       "adGenEfmGroup24HrRxLostStartsAct": adGenEfmGroup24HrRxLostStartsAct,
       "adGenEfmGroup24HrRxLostEndsAct": adGenEfmGroup24HrRxLostEndsAct,
       "adGenEfmLink15MinRxErroredFragmentsAct": adGenEfmLink15MinRxErroredFragmentsAct,
       "adGenEfmLink15MinRxSmallFragmentsAct": adGenEfmLink15MinRxSmallFragmentsAct,
       "adGenEfmLink15MinRxLargeFragmentsAct": adGenEfmLink15MinRxLargeFragmentsAct,
       "adGenEfmLink15MinRxDiscardedFragmentsAct": adGenEfmLink15MinRxDiscardedFragmentsAct,
       "adGenEfmLink15MinRxFcsErrorsAct": adGenEfmLink15MinRxFcsErrorsAct,
       "adGenEfmLink15MinRxCodingErrorsAct": adGenEfmLink15MinRxCodingErrorsAct,
       "adGenEfmLink24HrRxErroredFragmentsAct": adGenEfmLink24HrRxErroredFragmentsAct,
       "adGenEfmLink24HrRxSmallFragmentsAct": adGenEfmLink24HrRxSmallFragmentsAct,
       "adGenEfmLink24HrRxLargeFragmentsAct": adGenEfmLink24HrRxLargeFragmentsAct,
       "adGenEfmLink24HrRxDiscardedFragmentsAct": adGenEfmLink24HrRxDiscardedFragmentsAct,
       "adGenEfmLink24HrRxFcsErrorsAct": adGenEfmLink24HrRxFcsErrorsAct,
       "adGenEfmLink24HrRxCodingErrorsAct": adGenEfmLink24HrRxCodingErrorsAct,
       "adGenEfmMIB": adGenEfmMIB}
)
