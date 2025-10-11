# SNMP MIB module (OA-ETH-OAM-LM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-ETH-OAM-LM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:25 2025
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

(MepList,
 oaOptiSwitch) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "MepList",
    "oaOptiSwitch")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osEthOamLs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18)
)
if mibBuilder.loadTexts:
    osEthOamLs.setRevisions(
        ("2011-09-22 00:00",
         "2010-08-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OsEthOamMepId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )



class OsEthOamMepIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )



# MIB Managed Objects in the order of their OIDs

_OsEthOamLsCapabilities_ObjectIdentity = ObjectIdentity
osEthOamLsCapabilities = _OsEthOamLsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 1)
)
_OsEthOamLsConfTable_Object = MibTable
osEthOamLsConfTable = _OsEthOamLsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2)
)
if mibBuilder.loadTexts:
    osEthOamLsConfTable.setStatus("current")
_OsEthOamLsConfEntry_Object = MibTableRow
osEthOamLsConfEntry = _OsEthOamLsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1)
)
osEthOamLsConfEntry.setIndexNames(
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMdIndex"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMaIndex"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    osEthOamLsConfEntry.setStatus("current")


class _OsEthOamMdIndex_Type(Unsigned32):
    """Custom type osEthOamMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OsEthOamMdIndex_Type.__name__ = "Unsigned32"
_OsEthOamMdIndex_Object = MibTableColumn
osEthOamMdIndex = _OsEthOamMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 1),
    _OsEthOamMdIndex_Type()
)
osEthOamMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osEthOamMdIndex.setStatus("current")


class _OsEthOamMaIndex_Type(Unsigned32):
    """Custom type osEthOamMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OsEthOamMaIndex_Type.__name__ = "Unsigned32"
_OsEthOamMaIndex_Object = MibTableColumn
osEthOamMaIndex = _OsEthOamMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 2),
    _OsEthOamMaIndex_Type()
)
osEthOamMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osEthOamMaIndex.setStatus("current")
_OsEthOamMepIdentifier_Type = OsEthOamMepId
_OsEthOamMepIdentifier_Object = MibTableColumn
osEthOamMepIdentifier = _OsEthOamMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 3),
    _OsEthOamMepIdentifier_Type()
)
osEthOamMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osEthOamMepIdentifier.setStatus("current")


class _OsEthOamLsEnabled_Type(TruthValue):
    """Custom type osEthOamLsEnabled based on TruthValue"""
    defaultValue = 1


_OsEthOamLsEnabled_Type.__name__ = "TruthValue"
_OsEthOamLsEnabled_Object = MibTableColumn
osEthOamLsEnabled = _OsEthOamLsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 4),
    _OsEthOamLsEnabled_Type()
)
osEthOamLsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osEthOamLsEnabled.setStatus("current")


class _OsEthOamLsCounterEnable_Type(Bits):
    """Custom type osEthOamLsCounterEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bTimeOfDayTimestamp", 0),
          ("bMeasurementIntervalElapsedTime", 1),
          ("bInitiatedMeasurementCounter", 2),
          ("bCompleteMeasurementCounter", 3),
          ("bTransmitFrameCountForward", 4),
          ("bReceiveFrameCountForward", 6),
          ("bTransmitFrameCountBackward", 7),
          ("bReceiveFrameCountBackward", 8),
          ("bAvailabilityIndicatorForward", 9),
          ("bAvailabilityIndicatorBackward", 10),
          ("bUnavailabilityIndicatorForward", 11),
          ("bUnavailabilityIndicatorBackward", 12),
          ("bFrameLossRatioForwardMin", 13),
          ("bFrameLossRatioForwardMax", 14),
          ("bFrameLossRatioForwardAve", 15),
          ("bFrameLossRatioBackwardMin", 16),
          ("bFrameLossRatioBackwardMax", 17),
          ("bFrameLossRatioBackwardAve", 18))
    )

_OsEthOamLsCounterEnable_Type.__name__ = "Bits"
_OsEthOamLsCounterEnable_Object = MibTableColumn
osEthOamLsCounterEnable = _OsEthOamLsCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 5),
    _OsEthOamLsCounterEnable_Type()
)
osEthOamLsCounterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osEthOamLsCounterEnable.setStatus("current")


class _OsEthOamLsInterval_Type(Unsigned32):
    """Custom type osEthOamLsInterval based on Unsigned32"""
    defaultValue = 1000


_OsEthOamLsInterval_Type.__name__ = "Unsigned32"
_OsEthOamLsInterval_Object = MibTableColumn
osEthOamLsInterval = _OsEthOamLsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 6),
    _OsEthOamLsInterval_Type()
)
osEthOamLsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsInterval.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsInterval.setUnits("ms")


class _OsEthOamLsPriority_Type(Unsigned32):
    """Custom type osEthOamLsPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(8, 8),
    )


_OsEthOamLsPriority_Type.__name__ = "Unsigned32"
_OsEthOamLsPriority_Object = MibTableColumn
osEthOamLsPriority = _OsEthOamLsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 7),
    _OsEthOamLsPriority_Type()
)
osEthOamLsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsPriority.setStatus("current")


class _OsEthOamLsFrameSize_Type(Unsigned32):
    """Custom type osEthOamLsFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_OsEthOamLsFrameSize_Type.__name__ = "Unsigned32"
_OsEthOamLsFrameSize_Object = MibTableColumn
osEthOamLsFrameSize = _OsEthOamLsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 8),
    _OsEthOamLsFrameSize_Type()
)
osEthOamLsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsFrameSize.setUnits("bytes")


class _OsEthOamLsFramePattern_Type(OctetString):
    """Custom type osEthOamLsFramePattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1436),
    )


_OsEthOamLsFramePattern_Type.__name__ = "OctetString"
_OsEthOamLsFramePattern_Object = MibTableColumn
osEthOamLsFramePattern = _OsEthOamLsFramePattern_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 9),
    _OsEthOamLsFramePattern_Type()
)
osEthOamLsFramePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsFramePattern.setStatus("current")


class _OsEthOamLsMeasurementInterval_Type(Integer32):
    """Custom type osEthOamLsMeasurementInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_OsEthOamLsMeasurementInterval_Type.__name__ = "Integer32"
_OsEthOamLsMeasurementInterval_Object = MibTableColumn
osEthOamLsMeasurementInterval = _OsEthOamLsMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 10),
    _OsEthOamLsMeasurementInterval_Type()
)
osEthOamLsMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsMeasurementInterval.setUnits("seconds")


class _OsEthOamLsConfDestType_Type(Integer32):
    """Custom type osEthOamLsConfDestType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singleRMepId", 1),
          ("macAddress", 2),
          ("listOfRMeps", 3))
    )


_OsEthOamLsConfDestType_Type.__name__ = "Integer32"
_OsEthOamLsConfDestType_Object = MibTableColumn
osEthOamLsConfDestType = _OsEthOamLsConfDestType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 11),
    _OsEthOamLsConfDestType_Type()
)
osEthOamLsConfDestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osEthOamLsConfDestType.setStatus("current")
_OsEthOamLsConfDestMepId_Type = OsEthOamMepIdOrZero
_OsEthOamLsConfDestMepId_Object = MibTableColumn
osEthOamLsConfDestMepId = _OsEthOamLsConfDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 12),
    _OsEthOamLsConfDestMepId_Type()
)
osEthOamLsConfDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osEthOamLsConfDestMepId.setStatus("current")
_OsEthOamLsConfDestMepMac_Type = MacAddress
_OsEthOamLsConfDestMepMac_Object = MibTableColumn
osEthOamLsConfDestMepMac = _OsEthOamLsConfDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 13),
    _OsEthOamLsConfDestMepMac_Type()
)
osEthOamLsConfDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsConfDestMepMac.setStatus("current")
_OsEthOamLsConfDestMepList_Type = MepList
_OsEthOamLsConfDestMepList_Object = MibTableColumn
osEthOamLsConfDestMepList = _OsEthOamLsConfDestMepList_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 14),
    _OsEthOamLsConfDestMepList_Type()
)
osEthOamLsConfDestMepList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osEthOamLsConfDestMepList.setStatus("current")


class _OsEthOamLsConfHistorySize_Type(Unsigned32):
    """Custom type osEthOamLsConfHistorySize based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_OsEthOamLsConfHistorySize_Type.__name__ = "Unsigned32"
_OsEthOamLsConfHistorySize_Object = MibTableColumn
osEthOamLsConfHistorySize = _OsEthOamLsConfHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 15),
    _OsEthOamLsConfHistorySize_Type()
)
osEthOamLsConfHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osEthOamLsConfHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsConfHistorySize.setUnits("lines")


class _OsEthOamLsConfTimeout_Type(Unsigned32):
    """Custom type osEthOamLsConfTimeout based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_OsEthOamLsConfTimeout_Type.__name__ = "Unsigned32"
_OsEthOamLsConfTimeout_Object = MibTableColumn
osEthOamLsConfTimeout = _OsEthOamLsConfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 2, 1, 16),
    _OsEthOamLsConfTimeout_Type()
)
osEthOamLsConfTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osEthOamLsConfTimeout.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsConfTimeout.setUnits("milliseconds")
_OsEthOamLsHistTable_Object = MibTable
osEthOamLsHistTable = _OsEthOamLsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3)
)
if mibBuilder.loadTexts:
    osEthOamLsHistTable.setStatus("current")
_OsEthOamLsHistEntry_Object = MibTableRow
osEthOamLsHistEntry = _OsEthOamLsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1)
)
osEthOamLsHistEntry.setIndexNames(
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMdIndex"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMaIndex"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMepIdentifier"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamLsHistSampleIndex"),
)
if mibBuilder.loadTexts:
    osEthOamLsHistEntry.setStatus("current")


class _OsEthOamLsHistSampleIndex_Type(Unsigned32):
    """Custom type osEthOamLsHistSampleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OsEthOamLsHistSampleIndex_Type.__name__ = "Unsigned32"
_OsEthOamLsHistSampleIndex_Object = MibTableColumn
osEthOamLsHistSampleIndex = _OsEthOamLsHistSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 1),
    _OsEthOamLsHistSampleIndex_Type()
)
osEthOamLsHistSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osEthOamLsHistSampleIndex.setStatus("current")


class _OsEthOamLsHistNeTotTxFrames_Type(Counter32):
    """Custom type osEthOamLsHistNeTotTxFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNeTotTxFrames_Type.__name__ = "Counter32"
_OsEthOamLsHistNeTotTxFrames_Object = MibTableColumn
osEthOamLsHistNeTotTxFrames = _OsEthOamLsHistNeTotTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 2),
    _OsEthOamLsHistNeTotTxFrames_Type()
)
osEthOamLsHistNeTotTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNeTotTxFrames.setStatus("current")


class _OsEthOamLsHistNeTotLostFrames_Type(Counter32):
    """Custom type osEthOamLsHistNeTotLostFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNeTotLostFrames_Type.__name__ = "Counter32"
_OsEthOamLsHistNeTotLostFrames_Object = MibTableColumn
osEthOamLsHistNeTotLostFrames = _OsEthOamLsHistNeTotLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 3),
    _OsEthOamLsHistNeTotLostFrames_Type()
)
osEthOamLsHistNeTotLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNeTotLostFrames.setStatus("current")


class _OsEthOamLsHistNeTotFlr_Type(Counter32):
    """Custom type osEthOamLsHistNeTotFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNeTotFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistNeTotFlr_Object = MibTableColumn
osEthOamLsHistNeTotFlr = _OsEthOamLsHistNeTotFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 4),
    _OsEthOamLsHistNeTotFlr_Type()
)
osEthOamLsHistNeTotFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNeTotFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNeTotFlr.setUnits("0.01%")


class _OsEthOamLsHistNeMinFlr_Type(Counter32):
    """Custom type osEthOamLsHistNeMinFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNeMinFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistNeMinFlr_Object = MibTableColumn
osEthOamLsHistNeMinFlr = _OsEthOamLsHistNeMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 5),
    _OsEthOamLsHistNeMinFlr_Type()
)
osEthOamLsHistNeMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNeMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNeMinFlr.setUnits("0.01%")


class _OsEthOamLsHistNeMaxFlr_Type(Counter32):
    """Custom type osEthOamLsHistNeMaxFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNeMaxFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistNeMaxFlr_Object = MibTableColumn
osEthOamLsHistNeMaxFlr = _OsEthOamLsHistNeMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 6),
    _OsEthOamLsHistNeMaxFlr_Type()
)
osEthOamLsHistNeMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNeMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNeMaxFlr.setUnits("0.01%")


class _OsEthOamLsHistNeAvgFlr_Type(Counter32):
    """Custom type osEthOamLsHistNeAvgFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNeAvgFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistNeAvgFlr_Object = MibTableColumn
osEthOamLsHistNeAvgFlr = _OsEthOamLsHistNeAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 7),
    _OsEthOamLsHistNeAvgFlr_Type()
)
osEthOamLsHistNeAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNeAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNeAvgFlr.setUnits("0.01%")


class _OsEthOamLsHistFeTotTxFrames_Type(Counter32):
    """Custom type osEthOamLsHistFeTotTxFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistFeTotTxFrames_Type.__name__ = "Counter32"
_OsEthOamLsHistFeTotTxFrames_Object = MibTableColumn
osEthOamLsHistFeTotTxFrames = _OsEthOamLsHistFeTotTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 8),
    _OsEthOamLsHistFeTotTxFrames_Type()
)
osEthOamLsHistFeTotTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFeTotTxFrames.setStatus("current")


class _OsEthOamLsHistFeTotLostFrames_Type(Counter32):
    """Custom type osEthOamLsHistFeTotLostFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistFeTotLostFrames_Type.__name__ = "Counter32"
_OsEthOamLsHistFeTotLostFrames_Object = MibTableColumn
osEthOamLsHistFeTotLostFrames = _OsEthOamLsHistFeTotLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 9),
    _OsEthOamLsHistFeTotLostFrames_Type()
)
osEthOamLsHistFeTotLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFeTotLostFrames.setStatus("current")


class _OsEthOamLsHistFeTotFlr_Type(Counter32):
    """Custom type osEthOamLsHistFeTotFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistFeTotFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistFeTotFlr_Object = MibTableColumn
osEthOamLsHistFeTotFlr = _OsEthOamLsHistFeTotFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 10),
    _OsEthOamLsHistFeTotFlr_Type()
)
osEthOamLsHistFeTotFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFeTotFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFeTotFlr.setUnits("0.01%")


class _OsEthOamLsHistFeMinFlr_Type(Counter32):
    """Custom type osEthOamLsHistFeMinFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistFeMinFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistFeMinFlr_Object = MibTableColumn
osEthOamLsHistFeMinFlr = _OsEthOamLsHistFeMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 11),
    _OsEthOamLsHistFeMinFlr_Type()
)
osEthOamLsHistFeMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFeMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFeMinFlr.setUnits("0.01%")


class _OsEthOamLsHistFeMaxFlr_Type(Counter32):
    """Custom type osEthOamLsHistFeMaxFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistFeMaxFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistFeMaxFlr_Object = MibTableColumn
osEthOamLsHistFeMaxFlr = _OsEthOamLsHistFeMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 12),
    _OsEthOamLsHistFeMaxFlr_Type()
)
osEthOamLsHistFeMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFeMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFeMaxFlr.setUnits("0.01%")


class _OsEthOamLsHistFeAvgFlr_Type(Counter32):
    """Custom type osEthOamLsHistFeAvgFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistFeAvgFlr_Type.__name__ = "Counter32"
_OsEthOamLsHistFeAvgFlr_Object = MibTableColumn
osEthOamLsHistFeAvgFlr = _OsEthOamLsHistFeAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 13),
    _OsEthOamLsHistFeAvgFlr_Type()
)
osEthOamLsHistFeAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFeAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFeAvgFlr.setUnits("0.01%")


class _OsEthOamLsHistNumLmmOut_Type(Counter32):
    """Custom type osEthOamLsHistNumLmmOut based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNumLmmOut_Type.__name__ = "Counter32"
_OsEthOamLsHistNumLmmOut_Object = MibTableColumn
osEthOamLsHistNumLmmOut = _OsEthOamLsHistNumLmmOut_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 14),
    _OsEthOamLsHistNumLmmOut_Type()
)
osEthOamLsHistNumLmmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNumLmmOut.setStatus("current")


class _OsEthOamLsHistNumLmmIn_Type(Counter32):
    """Custom type osEthOamLsHistNumLmmIn based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNumLmmIn_Type.__name__ = "Counter32"
_OsEthOamLsHistNumLmmIn_Object = MibTableColumn
osEthOamLsHistNumLmmIn = _OsEthOamLsHistNumLmmIn_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 15),
    _OsEthOamLsHistNumLmmIn_Type()
)
osEthOamLsHistNumLmmIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNumLmmIn.setStatus("current")


class _OsEthOamLsHistNumLmrIn_Type(Counter32):
    """Custom type osEthOamLsHistNumLmrIn based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNumLmrIn_Type.__name__ = "Counter32"
_OsEthOamLsHistNumLmrIn_Object = MibTableColumn
osEthOamLsHistNumLmrIn = _OsEthOamLsHistNumLmrIn_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 16),
    _OsEthOamLsHistNumLmrIn_Type()
)
osEthOamLsHistNumLmrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNumLmrIn.setStatus("current")


class _OsEthOamLsHistNumLmrOut_Type(Counter32):
    """Custom type osEthOamLsHistNumLmrOut based on Counter32"""
    defaultValue = 0


_OsEthOamLsHistNumLmrOut_Type.__name__ = "Counter32"
_OsEthOamLsHistNumLmrOut_Object = MibTableColumn
osEthOamLsHistNumLmrOut = _OsEthOamLsHistNumLmrOut_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 17),
    _OsEthOamLsHistNumLmrOut_Type()
)
osEthOamLsHistNumLmrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNumLmrOut.setStatus("current")
_OsEthOamLsHistTestStarted_Type = DateAndTime
_OsEthOamLsHistTestStarted_Object = MibTableColumn
osEthOamLsHistTestStarted = _OsEthOamLsHistTestStarted_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 18),
    _OsEthOamLsHistTestStarted_Type()
)
osEthOamLsHistTestStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistTestStarted.setStatus("current")
_OsEthOamLsHistBurstStarted_Type = DateAndTime
_OsEthOamLsHistBurstStarted_Object = MibTableColumn
osEthOamLsHistBurstStarted = _OsEthOamLsHistBurstStarted_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 19),
    _OsEthOamLsHistBurstStarted_Type()
)
osEthOamLsHistBurstStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistBurstStarted.setStatus("current")
_OsEthOamLsHistDestMepId_Type = OsEthOamMepIdOrZero
_OsEthOamLsHistDestMepId_Object = MibTableColumn
osEthOamLsHistDestMepId = _OsEthOamLsHistDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 20),
    _OsEthOamLsHistDestMepId_Type()
)
osEthOamLsHistDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistDestMepId.setStatus("current")
_OsEthOamLsHistDestMepMac_Type = MacAddress
_OsEthOamLsHistDestMepMac_Object = MibTableColumn
osEthOamLsHistDestMepMac = _OsEthOamLsHistDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 21),
    _OsEthOamLsHistDestMepMac_Type()
)
osEthOamLsHistDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistDestMepMac.setStatus("current")
_OsEthOamLsHistNearEndMsgTx_Type = Unsigned32
_OsEthOamLsHistNearEndMsgTx_Object = MibTableColumn
osEthOamLsHistNearEndMsgTx = _OsEthOamLsHistNearEndMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 22),
    _OsEthOamLsHistNearEndMsgTx_Type()
)
osEthOamLsHistNearEndMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndMsgTx.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndMsgTx.setUnits("packets")
_OsEthOamLsHistNearEndMsgReceived_Type = Unsigned32
_OsEthOamLsHistNearEndMsgReceived_Object = MibTableColumn
osEthOamLsHistNearEndMsgReceived = _OsEthOamLsHistNearEndMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 23),
    _OsEthOamLsHistNearEndMsgReceived_Type()
)
osEthOamLsHistNearEndMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndMsgReceived.setUnits("packets")
_OsEthOamLsHistFarEndMsgTx_Type = Unsigned32
_OsEthOamLsHistFarEndMsgTx_Object = MibTableColumn
osEthOamLsHistFarEndMsgTx = _OsEthOamLsHistFarEndMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 24),
    _OsEthOamLsHistFarEndMsgTx_Type()
)
osEthOamLsHistFarEndMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndMsgTx.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndMsgTx.setUnits("packets")
_OsEthOamLsHistFarEndMsgReceived_Type = Unsigned32
_OsEthOamLsHistFarEndMsgReceived_Object = MibTableColumn
osEthOamLsHistFarEndMsgReceived = _OsEthOamLsHistFarEndMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 25),
    _OsEthOamLsHistFarEndMsgReceived_Type()
)
osEthOamLsHistFarEndMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndMsgReceived.setUnits("packets")
_OsEthOamLsHistNearEndMsgLoss_Type = Unsigned32
_OsEthOamLsHistNearEndMsgLoss_Object = MibTableColumn
osEthOamLsHistNearEndMsgLoss = _OsEthOamLsHistNearEndMsgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 26),
    _OsEthOamLsHistNearEndMsgLoss_Type()
)
osEthOamLsHistNearEndMsgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndMsgLoss.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndMsgLoss.setUnits("packets")
_OsEthOamLsHistFarEndMsgLoss_Type = Unsigned32
_OsEthOamLsHistFarEndMsgLoss_Object = MibTableColumn
osEthOamLsHistFarEndMsgLoss = _OsEthOamLsHistFarEndMsgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 27),
    _OsEthOamLsHistFarEndMsgLoss_Type()
)
osEthOamLsHistFarEndMsgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndMsgLoss.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndMsgLoss.setUnits("packets")
_OsEthOamLsHistNearEndFlr_Type = Counter32
_OsEthOamLsHistNearEndFlr_Object = MibTableColumn
osEthOamLsHistNearEndFlr = _OsEthOamLsHistNearEndFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 28),
    _OsEthOamLsHistNearEndFlr_Type()
)
osEthOamLsHistNearEndFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistNearEndFlr.setUnits("0.01%")
_OsEthOamLsHistFarEndFlr_Type = Counter32
_OsEthOamLsHistFarEndFlr_Object = MibTableColumn
osEthOamLsHistFarEndFlr = _OsEthOamLsHistFarEndFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 29),
    _OsEthOamLsHistFarEndFlr_Type()
)
osEthOamLsHistFarEndFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsHistFarEndFlr.setUnits("0.01%")


class _OsEthOamLsHistPriority_Type(Unsigned32):
    """Custom type osEthOamLsHistPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OsEthOamLsHistPriority_Type.__name__ = "Unsigned32"
_OsEthOamLsHistPriority_Object = MibTableColumn
osEthOamLsHistPriority = _OsEthOamLsHistPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 3, 1, 30),
    _OsEthOamLsHistPriority_Type()
)
osEthOamLsHistPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsHistPriority.setStatus("current")
_OsEthOamLsLastTable_Object = MibTable
osEthOamLsLastTable = _OsEthOamLsLastTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4)
)
if mibBuilder.loadTexts:
    osEthOamLsLastTable.setStatus("current")
_OsEthOamLsLastEntry_Object = MibTableRow
osEthOamLsLastEntry = _OsEthOamLsLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1)
)
osEthOamLsLastEntry.setIndexNames(
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMdIndex"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMaIndex"),
    (0, "OA-ETH-OAM-LM-MIB", "osEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    osEthOamLsLastEntry.setStatus("current")


class _OsEthOamLsLastNeTotTxFrames_Type(Counter32):
    """Custom type osEthOamLsLastNeTotTxFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNeTotTxFrames_Type.__name__ = "Counter32"
_OsEthOamLsLastNeTotTxFrames_Object = MibTableColumn
osEthOamLsLastNeTotTxFrames = _OsEthOamLsLastNeTotTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 1),
    _OsEthOamLsLastNeTotTxFrames_Type()
)
osEthOamLsLastNeTotTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNeTotTxFrames.setStatus("current")


class _OsEthOamLsLastNeTotLostFrames_Type(Counter32):
    """Custom type osEthOamLsLastNeTotLostFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNeTotLostFrames_Type.__name__ = "Counter32"
_OsEthOamLsLastNeTotLostFrames_Object = MibTableColumn
osEthOamLsLastNeTotLostFrames = _OsEthOamLsLastNeTotLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 2),
    _OsEthOamLsLastNeTotLostFrames_Type()
)
osEthOamLsLastNeTotLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNeTotLostFrames.setStatus("current")


class _OsEthOamLsLastNeTotFlr_Type(Counter32):
    """Custom type osEthOamLsLastNeTotFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNeTotFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastNeTotFlr_Object = MibTableColumn
osEthOamLsLastNeTotFlr = _OsEthOamLsLastNeTotFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 3),
    _OsEthOamLsLastNeTotFlr_Type()
)
osEthOamLsLastNeTotFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNeTotFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastNeTotFlr.setUnits("0.01%")


class _OsEthOamLsLastNeMinFlr_Type(Counter32):
    """Custom type osEthOamLsLastNeMinFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNeMinFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastNeMinFlr_Object = MibTableColumn
osEthOamLsLastNeMinFlr = _OsEthOamLsLastNeMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 4),
    _OsEthOamLsLastNeMinFlr_Type()
)
osEthOamLsLastNeMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNeMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastNeMinFlr.setUnits("0.01%")


class _OsEthOamLsLastNeMaxFlr_Type(Counter32):
    """Custom type osEthOamLsLastNeMaxFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNeMaxFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastNeMaxFlr_Object = MibTableColumn
osEthOamLsLastNeMaxFlr = _OsEthOamLsLastNeMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 5),
    _OsEthOamLsLastNeMaxFlr_Type()
)
osEthOamLsLastNeMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNeMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastNeMaxFlr.setUnits("0.01%")


class _OsEthOamLsLastNeAvgFlr_Type(Counter32):
    """Custom type osEthOamLsLastNeAvgFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNeAvgFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastNeAvgFlr_Object = MibTableColumn
osEthOamLsLastNeAvgFlr = _OsEthOamLsLastNeAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 6),
    _OsEthOamLsLastNeAvgFlr_Type()
)
osEthOamLsLastNeAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNeAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastNeAvgFlr.setUnits("0.01%")


class _OsEthOamLsLastFeTotTxFrames_Type(Counter32):
    """Custom type osEthOamLsLastFeTotTxFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastFeTotTxFrames_Type.__name__ = "Counter32"
_OsEthOamLsLastFeTotTxFrames_Object = MibTableColumn
osEthOamLsLastFeTotTxFrames = _OsEthOamLsLastFeTotTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 7),
    _OsEthOamLsLastFeTotTxFrames_Type()
)
osEthOamLsLastFeTotTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFeTotTxFrames.setStatus("current")


class _OsEthOamLsLastFeTotLostFrames_Type(Counter32):
    """Custom type osEthOamLsLastFeTotLostFrames based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastFeTotLostFrames_Type.__name__ = "Counter32"
_OsEthOamLsLastFeTotLostFrames_Object = MibTableColumn
osEthOamLsLastFeTotLostFrames = _OsEthOamLsLastFeTotLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 8),
    _OsEthOamLsLastFeTotLostFrames_Type()
)
osEthOamLsLastFeTotLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFeTotLostFrames.setStatus("current")


class _OsEthOamLsLastFeTotFlr_Type(Counter32):
    """Custom type osEthOamLsLastFeTotFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastFeTotFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastFeTotFlr_Object = MibTableColumn
osEthOamLsLastFeTotFlr = _OsEthOamLsLastFeTotFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 9),
    _OsEthOamLsLastFeTotFlr_Type()
)
osEthOamLsLastFeTotFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFeTotFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastFeTotFlr.setUnits("0.01%")


class _OsEthOamLsLastFeMinFlr_Type(Counter32):
    """Custom type osEthOamLsLastFeMinFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastFeMinFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastFeMinFlr_Object = MibTableColumn
osEthOamLsLastFeMinFlr = _OsEthOamLsLastFeMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 10),
    _OsEthOamLsLastFeMinFlr_Type()
)
osEthOamLsLastFeMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFeMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastFeMinFlr.setUnits("0.01%")


class _OsEthOamLsLastFeMaxFlr_Type(Counter32):
    """Custom type osEthOamLsLastFeMaxFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastFeMaxFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastFeMaxFlr_Object = MibTableColumn
osEthOamLsLastFeMaxFlr = _OsEthOamLsLastFeMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 11),
    _OsEthOamLsLastFeMaxFlr_Type()
)
osEthOamLsLastFeMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFeMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastFeMaxFlr.setUnits("0.01%")


class _OsEthOamLsLastFeAvgFlr_Type(Counter32):
    """Custom type osEthOamLsLastFeAvgFlr based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastFeAvgFlr_Type.__name__ = "Counter32"
_OsEthOamLsLastFeAvgFlr_Object = MibTableColumn
osEthOamLsLastFeAvgFlr = _OsEthOamLsLastFeAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 12),
    _OsEthOamLsLastFeAvgFlr_Type()
)
osEthOamLsLastFeAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFeAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastFeAvgFlr.setUnits("0.01%")


class _OsEthOamLsLastNumLmmOut_Type(Counter32):
    """Custom type osEthOamLsLastNumLmmOut based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNumLmmOut_Type.__name__ = "Counter32"
_OsEthOamLsLastNumLmmOut_Object = MibTableColumn
osEthOamLsLastNumLmmOut = _OsEthOamLsLastNumLmmOut_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 13),
    _OsEthOamLsLastNumLmmOut_Type()
)
osEthOamLsLastNumLmmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNumLmmOut.setStatus("current")


class _OsEthOamLsLastNumLmmIn_Type(Counter32):
    """Custom type osEthOamLsLastNumLmmIn based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNumLmmIn_Type.__name__ = "Counter32"
_OsEthOamLsLastNumLmmIn_Object = MibTableColumn
osEthOamLsLastNumLmmIn = _OsEthOamLsLastNumLmmIn_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 14),
    _OsEthOamLsLastNumLmmIn_Type()
)
osEthOamLsLastNumLmmIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNumLmmIn.setStatus("current")


class _OsEthOamLsLastNumLmrIn_Type(Counter32):
    """Custom type osEthOamLsLastNumLmrIn based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNumLmrIn_Type.__name__ = "Counter32"
_OsEthOamLsLastNumLmrIn_Object = MibTableColumn
osEthOamLsLastNumLmrIn = _OsEthOamLsLastNumLmrIn_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 15),
    _OsEthOamLsLastNumLmrIn_Type()
)
osEthOamLsLastNumLmrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNumLmrIn.setStatus("current")


class _OsEthOamLsLastNumLmrOut_Type(Counter32):
    """Custom type osEthOamLsLastNumLmrOut based on Counter32"""
    defaultValue = 0


_OsEthOamLsLastNumLmrOut_Type.__name__ = "Counter32"
_OsEthOamLsLastNumLmrOut_Object = MibTableColumn
osEthOamLsLastNumLmrOut = _OsEthOamLsLastNumLmrOut_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 16),
    _OsEthOamLsLastNumLmrOut_Type()
)
osEthOamLsLastNumLmrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNumLmrOut.setStatus("current")
_OsEthOamLsLastTestStarted_Type = DateAndTime
_OsEthOamLsLastTestStarted_Object = MibTableColumn
osEthOamLsLastTestStarted = _OsEthOamLsLastTestStarted_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 17),
    _OsEthOamLsLastTestStarted_Type()
)
osEthOamLsLastTestStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastTestStarted.setStatus("current")
_OsEthOamLsLastBurstStarted_Type = DateAndTime
_OsEthOamLsLastBurstStarted_Object = MibTableColumn
osEthOamLsLastBurstStarted = _OsEthOamLsLastBurstStarted_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 18),
    _OsEthOamLsLastBurstStarted_Type()
)
osEthOamLsLastBurstStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastBurstStarted.setStatus("current")
_OsEthOamLsLastDestMepId_Type = OsEthOamMepIdOrZero
_OsEthOamLsLastDestMepId_Object = MibTableColumn
osEthOamLsLastDestMepId = _OsEthOamLsLastDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 19),
    _OsEthOamLsLastDestMepId_Type()
)
osEthOamLsLastDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastDestMepId.setStatus("current")
_OsEthOamLsLastDestMepMac_Type = MacAddress
_OsEthOamLsLastDestMepMac_Object = MibTableColumn
osEthOamLsLastDestMepMac = _OsEthOamLsLastDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 20),
    _OsEthOamLsLastDestMepMac_Type()
)
osEthOamLsLastDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastDestMepMac.setStatus("current")
_OsEthOamLsLastNearEndMsgLoss_Type = Unsigned32
_OsEthOamLsLastNearEndMsgLoss_Object = MibTableColumn
osEthOamLsLastNearEndMsgLoss = _OsEthOamLsLastNearEndMsgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 21),
    _OsEthOamLsLastNearEndMsgLoss_Type()
)
osEthOamLsLastNearEndMsgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNearEndMsgLoss.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastNearEndMsgLoss.setUnits("packets")
_OsEthOamLsLastFarEndMsgLoss_Type = Unsigned32
_OsEthOamLsLastFarEndMsgLoss_Object = MibTableColumn
osEthOamLsLastFarEndMsgLoss = _OsEthOamLsLastFarEndMsgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 22),
    _OsEthOamLsLastFarEndMsgLoss_Type()
)
osEthOamLsLastFarEndMsgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFarEndMsgLoss.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastFarEndMsgLoss.setUnits("packets")
_OsEthOamLsLastNearEndFlr_Type = Counter32
_OsEthOamLsLastNearEndFlr_Object = MibTableColumn
osEthOamLsLastNearEndFlr = _OsEthOamLsLastNearEndFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 23),
    _OsEthOamLsLastNearEndFlr_Type()
)
osEthOamLsLastNearEndFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastNearEndFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastNearEndFlr.setUnits("0.01%")
_OsEthOamLsLastFarEndFlr_Type = Counter32
_OsEthOamLsLastFarEndFlr_Object = MibTableColumn
osEthOamLsLastFarEndFlr = _OsEthOamLsLastFarEndFlr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 24),
    _OsEthOamLsLastFarEndFlr_Type()
)
osEthOamLsLastFarEndFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastFarEndFlr.setStatus("current")
if mibBuilder.loadTexts:
    osEthOamLsLastFarEndFlr.setUnits("0.01%")


class _OsEthOamLsLastPriority_Type(Unsigned32):
    """Custom type osEthOamLsLastPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OsEthOamLsLastPriority_Type.__name__ = "Unsigned32"
_OsEthOamLsLastPriority_Object = MibTableColumn
osEthOamLsLastPriority = _OsEthOamLsLastPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 4, 1, 25),
    _OsEthOamLsLastPriority_Type()
)
osEthOamLsLastPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osEthOamLsLastPriority.setStatus("current")
_OsEthOamLsConformance_ObjectIdentity = ObjectIdentity
osEthOamLsConformance = _OsEthOamLsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 100)
)
_OsEthOamLsCompliances_ObjectIdentity = ObjectIdentity
osEthOamLsCompliances = _OsEthOamLsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 100, 1)
)
_OsEthOamLsGroups_ObjectIdentity = ObjectIdentity
osEthOamLsGroups = _OsEthOamLsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 100, 2)
)

# Managed Objects groups

osEthOamLsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 100, 2, 1)
)
osEthOamLsMandatoryGroup.setObjects(
      *(("OA-ETH-OAM-LM-MIB", "osEthOamLsEnabled"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsCounterEnable"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsInterval"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsPriority"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsFrameSize"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsFramePattern"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsMeasurementInterval"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsConfDestType"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsConfDestMepId"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsConfDestMepMac"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsConfDestMepList"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsConfHistorySize"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsConfTimeout"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNeTotTxFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNeTotLostFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNeTotFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNeMinFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNeMaxFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNeAvgFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFeTotTxFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFeTotLostFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFeTotFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFeMinFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFeMaxFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFeAvgFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNumLmmOut"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNumLmmIn"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNumLmrIn"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNumLmrOut"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistTestStarted"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistBurstStarted"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistDestMepId"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistDestMepMac"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNearEndMsgTx"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNearEndMsgReceived"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFarEndMsgTx"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFarEndMsgReceived"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNearEndMsgLoss"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFarEndMsgLoss"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistNearEndFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistFarEndFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsHistPriority"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNeTotTxFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNeTotLostFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNeTotFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNeMinFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNeMaxFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNeAvgFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFeTotTxFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFeTotLostFrames"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFeTotFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFeMinFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFeMaxFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFeAvgFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNumLmmOut"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNumLmmIn"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNumLmrIn"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNumLmrOut"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastTestStarted"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastBurstStarted"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastDestMepId"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastDestMepMac"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNearEndMsgLoss"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFarEndMsgLoss"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastNearEndFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastFarEndFlr"),
        ("OA-ETH-OAM-LM-MIB", "osEthOamLsLastPriority"))
)
if mibBuilder.loadTexts:
    osEthOamLsMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nbEthOamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 18, 100, 1, 1)
)
nbEthOamMIBCompliance.setObjects(
    ("OA-ETH-OAM-LM-MIB", "osEthOamLsMandatoryGroup")
)
if mibBuilder.loadTexts:
    nbEthOamMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-ETH-OAM-LM-MIB",
    **{"OsEthOamMepId": OsEthOamMepId,
       "OsEthOamMepIdOrZero": OsEthOamMepIdOrZero,
       "osEthOamLs": osEthOamLs,
       "osEthOamLsCapabilities": osEthOamLsCapabilities,
       "osEthOamLsConfTable": osEthOamLsConfTable,
       "osEthOamLsConfEntry": osEthOamLsConfEntry,
       "osEthOamMdIndex": osEthOamMdIndex,
       "osEthOamMaIndex": osEthOamMaIndex,
       "osEthOamMepIdentifier": osEthOamMepIdentifier,
       "osEthOamLsEnabled": osEthOamLsEnabled,
       "osEthOamLsCounterEnable": osEthOamLsCounterEnable,
       "osEthOamLsInterval": osEthOamLsInterval,
       "osEthOamLsPriority": osEthOamLsPriority,
       "osEthOamLsFrameSize": osEthOamLsFrameSize,
       "osEthOamLsFramePattern": osEthOamLsFramePattern,
       "osEthOamLsMeasurementInterval": osEthOamLsMeasurementInterval,
       "osEthOamLsConfDestType": osEthOamLsConfDestType,
       "osEthOamLsConfDestMepId": osEthOamLsConfDestMepId,
       "osEthOamLsConfDestMepMac": osEthOamLsConfDestMepMac,
       "osEthOamLsConfDestMepList": osEthOamLsConfDestMepList,
       "osEthOamLsConfHistorySize": osEthOamLsConfHistorySize,
       "osEthOamLsConfTimeout": osEthOamLsConfTimeout,
       "osEthOamLsHistTable": osEthOamLsHistTable,
       "osEthOamLsHistEntry": osEthOamLsHistEntry,
       "osEthOamLsHistSampleIndex": osEthOamLsHistSampleIndex,
       "osEthOamLsHistNeTotTxFrames": osEthOamLsHistNeTotTxFrames,
       "osEthOamLsHistNeTotLostFrames": osEthOamLsHistNeTotLostFrames,
       "osEthOamLsHistNeTotFlr": osEthOamLsHistNeTotFlr,
       "osEthOamLsHistNeMinFlr": osEthOamLsHistNeMinFlr,
       "osEthOamLsHistNeMaxFlr": osEthOamLsHistNeMaxFlr,
       "osEthOamLsHistNeAvgFlr": osEthOamLsHistNeAvgFlr,
       "osEthOamLsHistFeTotTxFrames": osEthOamLsHistFeTotTxFrames,
       "osEthOamLsHistFeTotLostFrames": osEthOamLsHistFeTotLostFrames,
       "osEthOamLsHistFeTotFlr": osEthOamLsHistFeTotFlr,
       "osEthOamLsHistFeMinFlr": osEthOamLsHistFeMinFlr,
       "osEthOamLsHistFeMaxFlr": osEthOamLsHistFeMaxFlr,
       "osEthOamLsHistFeAvgFlr": osEthOamLsHistFeAvgFlr,
       "osEthOamLsHistNumLmmOut": osEthOamLsHistNumLmmOut,
       "osEthOamLsHistNumLmmIn": osEthOamLsHistNumLmmIn,
       "osEthOamLsHistNumLmrIn": osEthOamLsHistNumLmrIn,
       "osEthOamLsHistNumLmrOut": osEthOamLsHistNumLmrOut,
       "osEthOamLsHistTestStarted": osEthOamLsHistTestStarted,
       "osEthOamLsHistBurstStarted": osEthOamLsHistBurstStarted,
       "osEthOamLsHistDestMepId": osEthOamLsHistDestMepId,
       "osEthOamLsHistDestMepMac": osEthOamLsHistDestMepMac,
       "osEthOamLsHistNearEndMsgTx": osEthOamLsHistNearEndMsgTx,
       "osEthOamLsHistNearEndMsgReceived": osEthOamLsHistNearEndMsgReceived,
       "osEthOamLsHistFarEndMsgTx": osEthOamLsHistFarEndMsgTx,
       "osEthOamLsHistFarEndMsgReceived": osEthOamLsHistFarEndMsgReceived,
       "osEthOamLsHistNearEndMsgLoss": osEthOamLsHistNearEndMsgLoss,
       "osEthOamLsHistFarEndMsgLoss": osEthOamLsHistFarEndMsgLoss,
       "osEthOamLsHistNearEndFlr": osEthOamLsHistNearEndFlr,
       "osEthOamLsHistFarEndFlr": osEthOamLsHistFarEndFlr,
       "osEthOamLsHistPriority": osEthOamLsHistPriority,
       "osEthOamLsLastTable": osEthOamLsLastTable,
       "osEthOamLsLastEntry": osEthOamLsLastEntry,
       "osEthOamLsLastNeTotTxFrames": osEthOamLsLastNeTotTxFrames,
       "osEthOamLsLastNeTotLostFrames": osEthOamLsLastNeTotLostFrames,
       "osEthOamLsLastNeTotFlr": osEthOamLsLastNeTotFlr,
       "osEthOamLsLastNeMinFlr": osEthOamLsLastNeMinFlr,
       "osEthOamLsLastNeMaxFlr": osEthOamLsLastNeMaxFlr,
       "osEthOamLsLastNeAvgFlr": osEthOamLsLastNeAvgFlr,
       "osEthOamLsLastFeTotTxFrames": osEthOamLsLastFeTotTxFrames,
       "osEthOamLsLastFeTotLostFrames": osEthOamLsLastFeTotLostFrames,
       "osEthOamLsLastFeTotFlr": osEthOamLsLastFeTotFlr,
       "osEthOamLsLastFeMinFlr": osEthOamLsLastFeMinFlr,
       "osEthOamLsLastFeMaxFlr": osEthOamLsLastFeMaxFlr,
       "osEthOamLsLastFeAvgFlr": osEthOamLsLastFeAvgFlr,
       "osEthOamLsLastNumLmmOut": osEthOamLsLastNumLmmOut,
       "osEthOamLsLastNumLmmIn": osEthOamLsLastNumLmmIn,
       "osEthOamLsLastNumLmrIn": osEthOamLsLastNumLmrIn,
       "osEthOamLsLastNumLmrOut": osEthOamLsLastNumLmrOut,
       "osEthOamLsLastTestStarted": osEthOamLsLastTestStarted,
       "osEthOamLsLastBurstStarted": osEthOamLsLastBurstStarted,
       "osEthOamLsLastDestMepId": osEthOamLsLastDestMepId,
       "osEthOamLsLastDestMepMac": osEthOamLsLastDestMepMac,
       "osEthOamLsLastNearEndMsgLoss": osEthOamLsLastNearEndMsgLoss,
       "osEthOamLsLastFarEndMsgLoss": osEthOamLsLastFarEndMsgLoss,
       "osEthOamLsLastNearEndFlr": osEthOamLsLastNearEndFlr,
       "osEthOamLsLastFarEndFlr": osEthOamLsLastFarEndFlr,
       "osEthOamLsLastPriority": osEthOamLsLastPriority,
       "osEthOamLsConformance": osEthOamLsConformance,
       "osEthOamLsCompliances": osEthOamLsCompliances,
       "nbEthOamMIBCompliance": nbEthOamMIBCompliance,
       "osEthOamLsGroups": osEthOamLsGroups,
       "osEthOamLsMandatoryGroup": osEthOamLsMandatoryGroup}
)
