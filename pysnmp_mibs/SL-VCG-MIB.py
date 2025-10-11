# SNMP MIB module (SL-VCG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-VCG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:11 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

vcgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VcgLinkType(TextualConvention, Integer32):
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
        *(("framed", 1),
          ("transparent", 2),
          ("pos", 3))
    )



# MIB Managed Objects in the order of their OIDs

_VcgMIBObjects_ObjectIdentity = ObjectIdentity
vcgMIBObjects = _VcgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1)
)
_VcgConfig_ObjectIdentity = ObjectIdentity
vcgConfig = _VcgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1)
)
_VcgStackStatusTable_Object = MibTable
vcgStackStatusTable = _VcgStackStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vcgStackStatusTable.setStatus("current")
_VcgStackStatusEntry_Object = MibTableRow
vcgStackStatusEntry = _VcgStackStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1)
)
vcgStackStatusEntry.setIndexNames(
    (0, "SL-VCG-MIB", "vcgStackLinkIndex"),
    (0, "SL-VCG-MIB", "vcgStackStsIndex"),
)
if mibBuilder.loadTexts:
    vcgStackStatusEntry.setStatus("current")
_VcgStackLinkIndex_Type = InterfaceIndex
_VcgStackLinkIndex_Object = MibTableColumn
vcgStackLinkIndex = _VcgStackLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 1),
    _VcgStackLinkIndex_Type()
)
vcgStackLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgStackLinkIndex.setStatus("current")
_VcgStackStsIndex_Type = InterfaceIndex
_VcgStackStsIndex_Object = MibTableColumn
vcgStackStsIndex = _VcgStackStsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 2),
    _VcgStackStsIndex_Type()
)
vcgStackStsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgStackStsIndex.setStatus("current")


class _VcgStackPathWidth_Type(Integer32):
    """Custom type vcgStackPathWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vtWidth45STS1", 1),
          ("vtWidth155STS3", 3),
          ("vtWidth15VC11", 11),
          ("vtWidth2VC12", 12))
    )


_VcgStackPathWidth_Type.__name__ = "Integer32"
_VcgStackPathWidth_Object = MibTableColumn
vcgStackPathWidth = _VcgStackPathWidth_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 3),
    _VcgStackPathWidth_Type()
)
vcgStackPathWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackPathWidth.setStatus("current")


class _VcgStackSts1Mapping_Type(Integer32):
    """Custom type vcgStackSts1Mapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tu3", 1),
          ("au3", 2),
          ("na", 3))
    )


_VcgStackSts1Mapping_Type.__name__ = "Integer32"
_VcgStackSts1Mapping_Object = MibTableColumn
vcgStackSts1Mapping = _VcgStackSts1Mapping_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 4),
    _VcgStackSts1Mapping_Type()
)
vcgStackSts1Mapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackSts1Mapping.setStatus("current")
_VcgStackTxSequenceNumber_Type = Integer32
_VcgStackTxSequenceNumber_Object = MibTableColumn
vcgStackTxSequenceNumber = _VcgStackTxSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 5),
    _VcgStackTxSequenceNumber_Type()
)
vcgStackTxSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackTxSequenceNumber.setStatus("current")


class _VcgStackLcasStatusOper_Type(Integer32):
    """Custom type vcgStackLcasStatusOper based on Integer32"""
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


_VcgStackLcasStatusOper_Type.__name__ = "Integer32"
_VcgStackLcasStatusOper_Object = MibTableColumn
vcgStackLcasStatusOper = _VcgStackLcasStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 6),
    _VcgStackLcasStatusOper_Type()
)
vcgStackLcasStatusOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackLcasStatusOper.setStatus("current")


class _VcgStackLcasStatusAdmin_Type(Integer32):
    """Custom type vcgStackLcasStatusAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonActive", 2))
    )


_VcgStackLcasStatusAdmin_Type.__name__ = "Integer32"
_VcgStackLcasStatusAdmin_Object = MibTableColumn
vcgStackLcasStatusAdmin = _VcgStackLcasStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 7),
    _VcgStackLcasStatusAdmin_Type()
)
vcgStackLcasStatusAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackLcasStatusAdmin.setStatus("current")


class _VcgStackLcasSourceState_Type(Integer32):
    """Custom type vcgStackLcasSourceState based on Integer32"""
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
        *(("norm", 1),
          ("dnu", 2),
          ("add", 3),
          ("idle", 4))
    )


_VcgStackLcasSourceState_Type.__name__ = "Integer32"
_VcgStackLcasSourceState_Object = MibTableColumn
vcgStackLcasSourceState = _VcgStackLcasSourceState_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 8),
    _VcgStackLcasSourceState_Type()
)
vcgStackLcasSourceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackLcasSourceState.setStatus("current")


class _VcgStackLcasSinkState_Type(Integer32):
    """Custom type vcgStackLcasSinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2),
          ("idle", 3))
    )


_VcgStackLcasSinkState_Type.__name__ = "Integer32"
_VcgStackLcasSinkState_Object = MibTableColumn
vcgStackLcasSinkState = _VcgStackLcasSinkState_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 9),
    _VcgStackLcasSinkState_Type()
)
vcgStackLcasSinkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackLcasSinkState.setStatus("current")
_VcgStackStatusRow_Type = RowStatus
_VcgStackStatusRow_Object = MibTableColumn
vcgStackStatusRow = _VcgStackStatusRow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 1, 1, 10),
    _VcgStackStatusRow_Type()
)
vcgStackStatusRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgStackStatusRow.setStatus("current")
_VcgLinkConfigTable_Object = MibTable
vcgLinkConfigTable = _VcgLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vcgLinkConfigTable.setStatus("current")
_VcgLinkConfigEntry_Object = MibTableRow
vcgLinkConfigEntry = _VcgLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1)
)
vcgLinkConfigEntry.setIndexNames(
    (0, "SL-VCG-MIB", "vcgLinkConfigIndex"),
)
if mibBuilder.loadTexts:
    vcgLinkConfigEntry.setStatus("current")
_VcgLinkConfigIndex_Type = InterfaceIndex
_VcgLinkConfigIndex_Object = MibTableColumn
vcgLinkConfigIndex = _VcgLinkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 1),
    _VcgLinkConfigIndex_Type()
)
vcgLinkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkConfigIndex.setStatus("current")
_VcgLinkConfigType_Type = VcgLinkType
_VcgLinkConfigType_Object = MibTableColumn
vcgLinkConfigType = _VcgLinkConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 2),
    _VcgLinkConfigType_Type()
)
vcgLinkConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigType.setStatus("current")
_VcgLinkConfigLcasSupport_Type = TruthValue
_VcgLinkConfigLcasSupport_Object = MibTableColumn
vcgLinkConfigLcasSupport = _VcgLinkConfigLcasSupport_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 3),
    _VcgLinkConfigLcasSupport_Type()
)
vcgLinkConfigLcasSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigLcasSupport.setStatus("current")
_VcgLinkConfigExtensionSupport_Type = TruthValue
_VcgLinkConfigExtensionSupport_Object = MibTableColumn
vcgLinkConfigExtensionSupport = _VcgLinkConfigExtensionSupport_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 4),
    _VcgLinkConfigExtensionSupport_Type()
)
vcgLinkConfigExtensionSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigExtensionSupport.setStatus("current")
_VcgLinkConfigResetPmCounters_Type = Integer32
_VcgLinkConfigResetPmCounters_Object = MibTableColumn
vcgLinkConfigResetPmCounters = _VcgLinkConfigResetPmCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 5),
    _VcgLinkConfigResetPmCounters_Type()
)
vcgLinkConfigResetPmCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigResetPmCounters.setStatus("current")


class _VcgLinkConfigValidIntervals_Type(Integer32):
    """Custom type vcgLinkConfigValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_VcgLinkConfigValidIntervals_Type.__name__ = "Integer32"
_VcgLinkConfigValidIntervals_Object = MibTableColumn
vcgLinkConfigValidIntervals = _VcgLinkConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 6),
    _VcgLinkConfigValidIntervals_Type()
)
vcgLinkConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkConfigValidIntervals.setStatus("current")
_VcgLinkConfigLcasHoldOfTime_Type = Integer32
_VcgLinkConfigLcasHoldOfTime_Object = MibTableColumn
vcgLinkConfigLcasHoldOfTime = _VcgLinkConfigLcasHoldOfTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 7),
    _VcgLinkConfigLcasHoldOfTime_Type()
)
vcgLinkConfigLcasHoldOfTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigLcasHoldOfTime.setStatus("current")
_VcgLinkConfigLcasWaitToRestoreTime_Type = Integer32
_VcgLinkConfigLcasWaitToRestoreTime_Object = MibTableColumn
vcgLinkConfigLcasWaitToRestoreTime = _VcgLinkConfigLcasWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 8),
    _VcgLinkConfigLcasWaitToRestoreTime_Type()
)
vcgLinkConfigLcasWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigLcasWaitToRestoreTime.setStatus("current")
_VcgLinkConfigStackApplyChanges_Type = Integer32
_VcgLinkConfigStackApplyChanges_Object = MibTableColumn
vcgLinkConfigStackApplyChanges = _VcgLinkConfigStackApplyChanges_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 1, 2, 1, 9),
    _VcgLinkConfigStackApplyChanges_Type()
)
vcgLinkConfigStackApplyChanges.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgLinkConfigStackApplyChanges.setStatus("current")
_VcgPm_ObjectIdentity = ObjectIdentity
vcgPm = _VcgPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2)
)
_VcgLinkCurrentTable_Object = MibTable
vcgLinkCurrentTable = _VcgLinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vcgLinkCurrentTable.setStatus("current")
_VcgLinkCurrentEntry_Object = MibTableRow
vcgLinkCurrentEntry = _VcgLinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 1, 1)
)
vcgLinkCurrentEntry.setIndexNames(
    (0, "SL-VCG-MIB", "vcgLinkCurrentIndex"),
)
if mibBuilder.loadTexts:
    vcgLinkCurrentEntry.setStatus("current")
_VcgLinkCurrentIndex_Type = InterfaceIndex
_VcgLinkCurrentIndex_Object = MibTableColumn
vcgLinkCurrentIndex = _VcgLinkCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 1, 1, 1),
    _VcgLinkCurrentIndex_Type()
)
vcgLinkCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkCurrentIndex.setStatus("current")
_VcgLinkCurrentRxVcatSyncLossSeconds_Type = Counter64
_VcgLinkCurrentRxVcatSyncLossSeconds_Object = MibTableColumn
vcgLinkCurrentRxVcatSyncLossSeconds = _VcgLinkCurrentRxVcatSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 1, 1, 2),
    _VcgLinkCurrentRxVcatSyncLossSeconds_Type()
)
vcgLinkCurrentRxVcatSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkCurrentRxVcatSyncLossSeconds.setStatus("current")
_VcgLinkCurrentRxLcasCrcErrors_Type = Counter64
_VcgLinkCurrentRxLcasCrcErrors_Object = MibTableColumn
vcgLinkCurrentRxLcasCrcErrors = _VcgLinkCurrentRxLcasCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 1, 1, 3),
    _VcgLinkCurrentRxLcasCrcErrors_Type()
)
vcgLinkCurrentRxLcasCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkCurrentRxLcasCrcErrors.setStatus("current")
_VcgLinkIntervalTable_Object = MibTable
vcgLinkIntervalTable = _VcgLinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vcgLinkIntervalTable.setStatus("current")
_VcgLinkIntervalEntry_Object = MibTableRow
vcgLinkIntervalEntry = _VcgLinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 2, 1)
)
vcgLinkIntervalEntry.setIndexNames(
    (0, "SL-VCG-MIB", "vcgLinkIntervalIndex"),
    (0, "SL-VCG-MIB", "vcgLinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    vcgLinkIntervalEntry.setStatus("current")
_VcgLinkIntervalIndex_Type = InterfaceIndex
_VcgLinkIntervalIndex_Object = MibTableColumn
vcgLinkIntervalIndex = _VcgLinkIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 2, 1, 1),
    _VcgLinkIntervalIndex_Type()
)
vcgLinkIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkIntervalIndex.setStatus("current")


class _VcgLinkIntervalNumber_Type(Integer32):
    """Custom type vcgLinkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_VcgLinkIntervalNumber_Type.__name__ = "Integer32"
_VcgLinkIntervalNumber_Object = MibTableColumn
vcgLinkIntervalNumber = _VcgLinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 2, 1, 2),
    _VcgLinkIntervalNumber_Type()
)
vcgLinkIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkIntervalNumber.setStatus("current")
_VcgLinkIntervalRxVcatSyncLossSeconds_Type = Counter64
_VcgLinkIntervalRxVcatSyncLossSeconds_Object = MibTableColumn
vcgLinkIntervalRxVcatSyncLossSeconds = _VcgLinkIntervalRxVcatSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 2, 1, 3),
    _VcgLinkIntervalRxVcatSyncLossSeconds_Type()
)
vcgLinkIntervalRxVcatSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkIntervalRxVcatSyncLossSeconds.setStatus("current")
_VcgLinkIntervalRxLcasCrcErrors_Type = Counter64
_VcgLinkIntervalRxLcasCrcErrors_Object = MibTableColumn
vcgLinkIntervalRxLcasCrcErrors = _VcgLinkIntervalRxLcasCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 2, 1, 4),
    _VcgLinkIntervalRxLcasCrcErrors_Type()
)
vcgLinkIntervalRxLcasCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkIntervalRxLcasCrcErrors.setStatus("current")
_VcgLinkDayTable_Object = MibTable
vcgLinkDayTable = _VcgLinkDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vcgLinkDayTable.setStatus("current")
_VcgLinkDayEntry_Object = MibTableRow
vcgLinkDayEntry = _VcgLinkDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 3, 1)
)
vcgLinkDayEntry.setIndexNames(
    (0, "SL-VCG-MIB", "vcgLinkDayIndex"),
    (0, "SL-VCG-MIB", "vcgLinkDayNumber"),
)
if mibBuilder.loadTexts:
    vcgLinkDayEntry.setStatus("current")
_VcgLinkDayIndex_Type = InterfaceIndex
_VcgLinkDayIndex_Object = MibTableColumn
vcgLinkDayIndex = _VcgLinkDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 3, 1, 1),
    _VcgLinkDayIndex_Type()
)
vcgLinkDayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkDayIndex.setStatus("current")


class _VcgLinkDayNumber_Type(Integer32):
    """Custom type vcgLinkDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_VcgLinkDayNumber_Type.__name__ = "Integer32"
_VcgLinkDayNumber_Object = MibTableColumn
vcgLinkDayNumber = _VcgLinkDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 3, 1, 2),
    _VcgLinkDayNumber_Type()
)
vcgLinkDayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcgLinkDayNumber.setStatus("current")
_VcgLinkDayRxVcatSyncLossSeconds_Type = Counter64
_VcgLinkDayRxVcatSyncLossSeconds_Object = MibTableColumn
vcgLinkDayRxVcatSyncLossSeconds = _VcgLinkDayRxVcatSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 3, 1, 3),
    _VcgLinkDayRxVcatSyncLossSeconds_Type()
)
vcgLinkDayRxVcatSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkDayRxVcatSyncLossSeconds.setStatus("current")
_VcgLinkDayRxLcasCrcErrors_Type = Counter64
_VcgLinkDayRxLcasCrcErrors_Object = MibTableColumn
vcgLinkDayRxLcasCrcErrors = _VcgLinkDayRxLcasCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 2, 3, 1, 4),
    _VcgLinkDayRxLcasCrcErrors_Type()
)
vcgLinkDayRxLcasCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLinkDayRxLcasCrcErrors.setStatus("current")
_VcgTraps_ObjectIdentity = ObjectIdentity
vcgTraps = _VcgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 3)
)

# Managed Objects groups


# Notification objects

vcgStackValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 3, 1)
)
vcgStackValueChange.setObjects(
      *(("SL-VCG-MIB", "vcgStackLinkIndex"),
        ("SL-VCG-MIB", "vcgStackStsIndex"),
        ("SL-VCG-MIB", "vcgStackLcasStatusOper"))
)
if mibBuilder.loadTexts:
    vcgStackValueChange.setStatus(
        "current"
    )

vcgStackConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 10, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vcgStackConfigurationChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-VCG-MIB",
    **{"VcgLinkType": VcgLinkType,
       "vcgMIB": vcgMIB,
       "vcgMIBObjects": vcgMIBObjects,
       "vcgConfig": vcgConfig,
       "vcgStackStatusTable": vcgStackStatusTable,
       "vcgStackStatusEntry": vcgStackStatusEntry,
       "vcgStackLinkIndex": vcgStackLinkIndex,
       "vcgStackStsIndex": vcgStackStsIndex,
       "vcgStackPathWidth": vcgStackPathWidth,
       "vcgStackSts1Mapping": vcgStackSts1Mapping,
       "vcgStackTxSequenceNumber": vcgStackTxSequenceNumber,
       "vcgStackLcasStatusOper": vcgStackLcasStatusOper,
       "vcgStackLcasStatusAdmin": vcgStackLcasStatusAdmin,
       "vcgStackLcasSourceState": vcgStackLcasSourceState,
       "vcgStackLcasSinkState": vcgStackLcasSinkState,
       "vcgStackStatusRow": vcgStackStatusRow,
       "vcgLinkConfigTable": vcgLinkConfigTable,
       "vcgLinkConfigEntry": vcgLinkConfigEntry,
       "vcgLinkConfigIndex": vcgLinkConfigIndex,
       "vcgLinkConfigType": vcgLinkConfigType,
       "vcgLinkConfigLcasSupport": vcgLinkConfigLcasSupport,
       "vcgLinkConfigExtensionSupport": vcgLinkConfigExtensionSupport,
       "vcgLinkConfigResetPmCounters": vcgLinkConfigResetPmCounters,
       "vcgLinkConfigValidIntervals": vcgLinkConfigValidIntervals,
       "vcgLinkConfigLcasHoldOfTime": vcgLinkConfigLcasHoldOfTime,
       "vcgLinkConfigLcasWaitToRestoreTime": vcgLinkConfigLcasWaitToRestoreTime,
       "vcgLinkConfigStackApplyChanges": vcgLinkConfigStackApplyChanges,
       "vcgPm": vcgPm,
       "vcgLinkCurrentTable": vcgLinkCurrentTable,
       "vcgLinkCurrentEntry": vcgLinkCurrentEntry,
       "vcgLinkCurrentIndex": vcgLinkCurrentIndex,
       "vcgLinkCurrentRxVcatSyncLossSeconds": vcgLinkCurrentRxVcatSyncLossSeconds,
       "vcgLinkCurrentRxLcasCrcErrors": vcgLinkCurrentRxLcasCrcErrors,
       "vcgLinkIntervalTable": vcgLinkIntervalTable,
       "vcgLinkIntervalEntry": vcgLinkIntervalEntry,
       "vcgLinkIntervalIndex": vcgLinkIntervalIndex,
       "vcgLinkIntervalNumber": vcgLinkIntervalNumber,
       "vcgLinkIntervalRxVcatSyncLossSeconds": vcgLinkIntervalRxVcatSyncLossSeconds,
       "vcgLinkIntervalRxLcasCrcErrors": vcgLinkIntervalRxLcasCrcErrors,
       "vcgLinkDayTable": vcgLinkDayTable,
       "vcgLinkDayEntry": vcgLinkDayEntry,
       "vcgLinkDayIndex": vcgLinkDayIndex,
       "vcgLinkDayNumber": vcgLinkDayNumber,
       "vcgLinkDayRxVcatSyncLossSeconds": vcgLinkDayRxVcatSyncLossSeconds,
       "vcgLinkDayRxLcasCrcErrors": vcgLinkDayRxLcasCrcErrors,
       "vcgTraps": vcgTraps,
       "vcgStackValueChange": vcgStackValueChange,
       "vcgStackConfigurationChange": vcgStackConfigurationChange}
)
