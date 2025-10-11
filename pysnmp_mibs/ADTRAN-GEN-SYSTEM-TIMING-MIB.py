# SNMP MIB module (ADTRAN-GEN-SYSTEM-TIMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-SYSTEM-TIMING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:24 2025
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

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenSystemTiming,
 adGenSystemTimingID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenSystemTiming",
    "adGenSystemTimingID")

(GenSystemInterfaceType,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "GenSystemInterfaceType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

adGenSystemTimingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 13, 1)
)
if mibBuilder.loadTexts:
    adGenSystemTimingMIB.setRevisions(
        ("2018-01-09 00:00",
         "2017-09-29 00:00",
         "2017-07-25 00:00",
         "2017-06-12 00:00",
         "2013-09-09 00:00",
         "2011-10-26 11:00",
         "2011-09-02 00:00",
         "2009-03-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenTimingSource(TextualConvention, Integer32):
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
        *(("primaryTimingSource", 1),
          ("secondaryTimingSource", 2),
          ("fallbackTimingSource", 3))
    )



class AdGenTimingSourceSelection(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("externalPrimary", 2),
          ("externalSecondary", 3),
          ("loopA", 4),
          ("loopB", 5),
          ("localPort", 6),
          ("fixedPort", 7),
          ("localPortSyncE", 8),
          ("fixedPortSyncE", 9),
          ("localPortPhy", 10),
          ("fixedPortPhy", 11),
          ("vdslUplinkNTR", 12))
    )



class AdGenExternalSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalPrimary", 1),
          ("externalSecondary", 2))
    )



class AdGenTimingConfigurationStatus(TextualConvention, Integer32):
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
        *(("invalidConfiguration", 1),
          ("incompleteConfiguration", 2),
          ("okConfiguration", 3))
    )



class AdGenExternalSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bitsD4", 1),
          ("bitsOD", 2),
          ("composite", 3),
          ("composite8kHz", 4),
          ("bitsG704", 5),
          ("bitsD5", 6))
    )



class AdGenTimingSourceQuality(TextualConvention, Integer32):
    status = "current"
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
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("stratum1", 1),
          ("synchronized", 2),
          ("stratum2", 3),
          ("transmitModeClock", 4),
          ("stratum3e", 5),
          ("stratum3", 6),
          ("sonetClock", 7),
          ("stratum4or4e", 8),
          ("doNotUseForSync", 15))
    )



class AdGenSystemTimingSourceHealth(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_AdGenSystemTimingProv_ObjectIdentity = ObjectIdentity
adGenSystemTimingProv = _AdGenSystemTimingProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1)
)
_AdGenSystemTimingProvTable_Object = MibTable
adGenSystemTimingProvTable = _AdGenSystemTimingProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSystemTimingProvTable.setStatus("current")
_AdGenSystemTimingProvEntry_Object = MibTableRow
adGenSystemTimingProvEntry = _AdGenSystemTimingProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1)
)
adGenSystemTimingProvEntry.setIndexNames(
    (0, "ADTRAN-GEN-SYSTEM-TIMING-MIB", "adGenSystemTimingSource"),
)
if mibBuilder.loadTexts:
    adGenSystemTimingProvEntry.setStatus("current")
_AdGenSystemTimingSource_Type = AdGenTimingSource
_AdGenSystemTimingSource_Object = MibTableColumn
adGenSystemTimingSource = _AdGenSystemTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 1),
    _AdGenSystemTimingSource_Type()
)
adGenSystemTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingSource.setStatus("current")
_AdGenSystemTimingSelection_Type = AdGenTimingSourceSelection
_AdGenSystemTimingSelection_Object = MibTableColumn
adGenSystemTimingSelection = _AdGenSystemTimingSelection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 2),
    _AdGenSystemTimingSelection_Type()
)
adGenSystemTimingSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingSelection.setStatus("current")
_AdGenSystemTimingInterfaceType_Type = GenSystemInterfaceType
_AdGenSystemTimingInterfaceType_Object = MibTableColumn
adGenSystemTimingInterfaceType = _AdGenSystemTimingInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 3),
    _AdGenSystemTimingInterfaceType_Type()
)
adGenSystemTimingInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingInterfaceType.setStatus("current")
_AdGenSystemTimingShelf_Type = Integer32
_AdGenSystemTimingShelf_Object = MibTableColumn
adGenSystemTimingShelf = _AdGenSystemTimingShelf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 4),
    _AdGenSystemTimingShelf_Type()
)
adGenSystemTimingShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingShelf.setStatus("current")
_AdGenSystemTimingSlot_Type = Integer32
_AdGenSystemTimingSlot_Object = MibTableColumn
adGenSystemTimingSlot = _AdGenSystemTimingSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 5),
    _AdGenSystemTimingSlot_Type()
)
adGenSystemTimingSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingSlot.setStatus("current")
_AdGenSystemTimingPort_Type = Integer32
_AdGenSystemTimingPort_Object = MibTableColumn
adGenSystemTimingPort = _AdGenSystemTimingPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 6),
    _AdGenSystemTimingPort_Type()
)
adGenSystemTimingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingPort.setStatus("current")
_AdGenSystemTimingConfigurationStatus_Type = AdGenTimingConfigurationStatus
_AdGenSystemTimingConfigurationStatus_Object = MibTableColumn
adGenSystemTimingConfigurationStatus = _AdGenSystemTimingConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 1, 1, 7),
    _AdGenSystemTimingConfigurationStatus_Type()
)
adGenSystemTimingConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingConfigurationStatus.setStatus("current")
_AdGenSystemTimingExternalSourceProvTable_Object = MibTable
adGenSystemTimingExternalSourceProvTable = _AdGenSystemTimingExternalSourceProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2)
)
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourceProvTable.setStatus("current")
_AdGenSystemTimingExternalSourceProvEntry_Object = MibTableRow
adGenSystemTimingExternalSourceProvEntry = _AdGenSystemTimingExternalSourceProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2, 1)
)
adGenSystemTimingExternalSourceProvEntry.setIndexNames(
    (0, "ADTRAN-GEN-SYSTEM-TIMING-MIB", "adGenSystemTimingExternalSourceId"),
)
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourceProvEntry.setStatus("current")
_AdGenSystemTimingExternalSourceId_Type = AdGenExternalSource
_AdGenSystemTimingExternalSourceId_Object = MibTableColumn
adGenSystemTimingExternalSourceId = _AdGenSystemTimingExternalSourceId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2, 1, 1),
    _AdGenSystemTimingExternalSourceId_Type()
)
adGenSystemTimingExternalSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourceId.setStatus("current")
_AdGenSystemTimingExternalSourceType_Type = AdGenExternalSourceType
_AdGenSystemTimingExternalSourceType_Object = MibTableColumn
adGenSystemTimingExternalSourceType = _AdGenSystemTimingExternalSourceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2, 1, 2),
    _AdGenSystemTimingExternalSourceType_Type()
)
adGenSystemTimingExternalSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourceType.setStatus("current")
_AdGenSystemTimingExternalSourceQuality_Type = AdGenTimingSourceQuality
_AdGenSystemTimingExternalSourceQuality_Object = MibTableColumn
adGenSystemTimingExternalSourceQuality = _AdGenSystemTimingExternalSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2, 1, 3),
    _AdGenSystemTimingExternalSourceQuality_Type()
)
adGenSystemTimingExternalSourceQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourceQuality.setStatus("current")


class _AdGenSystemTimingExternalSourcePriority_Type(Integer32):
    """Custom type adGenSystemTimingExternalSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenSystemTimingExternalSourcePriority_Type.__name__ = "Integer32"
_AdGenSystemTimingExternalSourcePriority_Object = MibTableColumn
adGenSystemTimingExternalSourcePriority = _AdGenSystemTimingExternalSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2, 1, 4),
    _AdGenSystemTimingExternalSourcePriority_Type()
)
adGenSystemTimingExternalSourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourcePriority.setStatus("current")


class _AdGenSystemTimingExternalSourceHopCount_Type(Integer32):
    """Custom type adGenSystemTimingExternalSourceHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenSystemTimingExternalSourceHopCount_Type.__name__ = "Integer32"
_AdGenSystemTimingExternalSourceHopCount_Object = MibTableColumn
adGenSystemTimingExternalSourceHopCount = _AdGenSystemTimingExternalSourceHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 2, 1, 5),
    _AdGenSystemTimingExternalSourceHopCount_Type()
)
adGenSystemTimingExternalSourceHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingExternalSourceHopCount.setStatus("current")


class _AdGenSystemTimingModeRevertive_Type(Integer32):
    """Custom type adGenSystemTimingModeRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenSystemTimingModeRevertive_Type.__name__ = "Integer32"
_AdGenSystemTimingModeRevertive_Object = MibScalar
adGenSystemTimingModeRevertive = _AdGenSystemTimingModeRevertive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 3),
    _AdGenSystemTimingModeRevertive_Type()
)
adGenSystemTimingModeRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingModeRevertive.setStatus("deprecated")


class _AdGenSystemTimingForceClockFailover_Type(Integer32):
    """Custom type adGenSystemTimingForceClockFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failover", 1),
          ("notavailable", 2))
    )


_AdGenSystemTimingForceClockFailover_Type.__name__ = "Integer32"
_AdGenSystemTimingForceClockFailover_Object = MibScalar
adGenSystemTimingForceClockFailover = _AdGenSystemTimingForceClockFailover_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 4),
    _AdGenSystemTimingForceClockFailover_Type()
)
adGenSystemTimingForceClockFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingForceClockFailover.setStatus("current")


class _AdGenSystemTimingUseHopCount_Type(Integer32):
    """Custom type adGenSystemTimingUseHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenSystemTimingUseHopCount_Type.__name__ = "Integer32"
_AdGenSystemTimingUseHopCount_Object = MibScalar
adGenSystemTimingUseHopCount = _AdGenSystemTimingUseHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 5),
    _AdGenSystemTimingUseHopCount_Type()
)
adGenSystemTimingUseHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingUseHopCount.setStatus("deprecated")


class _AdGenSystemTimingSrcSwitchAlarmEnable_Type(TruthValue):
    """Custom type adGenSystemTimingSrcSwitchAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenSystemTimingSrcSwitchAlarmEnable_Type.__name__ = "TruthValue"
_AdGenSystemTimingSrcSwitchAlarmEnable_Object = MibScalar
adGenSystemTimingSrcSwitchAlarmEnable = _AdGenSystemTimingSrcSwitchAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 6),
    _AdGenSystemTimingSrcSwitchAlarmEnable_Type()
)
adGenSystemTimingSrcSwitchAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingSrcSwitchAlarmEnable.setStatus("current")


class _AdGenSystemTimingPriSrcFailAlarmEnable_Type(TruthValue):
    """Custom type adGenSystemTimingPriSrcFailAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenSystemTimingPriSrcFailAlarmEnable_Type.__name__ = "TruthValue"
_AdGenSystemTimingPriSrcFailAlarmEnable_Object = MibScalar
adGenSystemTimingPriSrcFailAlarmEnable = _AdGenSystemTimingPriSrcFailAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 7),
    _AdGenSystemTimingPriSrcFailAlarmEnable_Type()
)
adGenSystemTimingPriSrcFailAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingPriSrcFailAlarmEnable.setStatus("current")


class _AdGenSystemTimingSecSrcFailAlarmEnable_Type(TruthValue):
    """Custom type adGenSystemTimingSecSrcFailAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenSystemTimingSecSrcFailAlarmEnable_Type.__name__ = "TruthValue"
_AdGenSystemTimingSecSrcFailAlarmEnable_Object = MibScalar
adGenSystemTimingSecSrcFailAlarmEnable = _AdGenSystemTimingSecSrcFailAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 8),
    _AdGenSystemTimingSecSrcFailAlarmEnable_Type()
)
adGenSystemTimingSecSrcFailAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingSecSrcFailAlarmEnable.setStatus("current")


class _AdGenSystemTimingSelectionMode_Type(Integer32):
    """Custom type adGenSystemTimingSelectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("nonRevertive", 2),
          ("useHopCount", 3))
    )


_AdGenSystemTimingSelectionMode_Type.__name__ = "Integer32"
_AdGenSystemTimingSelectionMode_Object = MibScalar
adGenSystemTimingSelectionMode = _AdGenSystemTimingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 9),
    _AdGenSystemTimingSelectionMode_Type()
)
adGenSystemTimingSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingSelectionMode.setStatus("current")
_AdGenSystemTimingProvPortTable_Object = MibTable
adGenSystemTimingProvPortTable = _AdGenSystemTimingProvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 10)
)
if mibBuilder.loadTexts:
    adGenSystemTimingProvPortTable.setStatus("current")
_AdGenSystemTimingProvPortEntry_Object = MibTableRow
adGenSystemTimingProvPortEntry = _AdGenSystemTimingProvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 10, 1)
)
adGenSystemTimingProvPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenSystemTimingProvPortEntry.setStatus("current")


class _AdGenSystemTimingTransmitSSMEnable_Type(Integer32):
    """Custom type adGenSystemTimingTransmitSSMEnable based on Integer32"""
    defaultValue = 2

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


_AdGenSystemTimingTransmitSSMEnable_Type.__name__ = "Integer32"
_AdGenSystemTimingTransmitSSMEnable_Object = MibTableColumn
adGenSystemTimingTransmitSSMEnable = _AdGenSystemTimingTransmitSSMEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 1, 10, 1, 1),
    _AdGenSystemTimingTransmitSSMEnable_Type()
)
adGenSystemTimingTransmitSSMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSystemTimingTransmitSSMEnable.setStatus("current")
_AdGenSystemTimingStatus_ObjectIdentity = ObjectIdentity
adGenSystemTimingStatus = _AdGenSystemTimingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2)
)


class _AdGenSystemTimingCurrentSource_Type(Integer32):
    """Custom type adGenSystemTimingCurrentSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("fallback", 3),
          ("standby", 4),
          ("internal", 5),
          ("holdover", 6))
    )


_AdGenSystemTimingCurrentSource_Type.__name__ = "Integer32"
_AdGenSystemTimingCurrentSource_Object = MibScalar
adGenSystemTimingCurrentSource = _AdGenSystemTimingCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 1),
    _AdGenSystemTimingCurrentSource_Type()
)
adGenSystemTimingCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingCurrentSource.setStatus("current")
_AdGenSystemTimingLoopAClockHealth_Type = AdGenSystemTimingSourceHealth
_AdGenSystemTimingLoopAClockHealth_Object = MibScalar
adGenSystemTimingLoopAClockHealth = _AdGenSystemTimingLoopAClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 2),
    _AdGenSystemTimingLoopAClockHealth_Type()
)
adGenSystemTimingLoopAClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingLoopAClockHealth.setStatus("current")
_AdGenSystemTimingLoopBClockHealth_Type = AdGenSystemTimingSourceHealth
_AdGenSystemTimingLoopBClockHealth_Object = MibScalar
adGenSystemTimingLoopBClockHealth = _AdGenSystemTimingLoopBClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 3),
    _AdGenSystemTimingLoopBClockHealth_Type()
)
adGenSystemTimingLoopBClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingLoopBClockHealth.setStatus("current")
_AdGenSystemTimingBitsAClockHealth_Type = AdGenSystemTimingSourceHealth
_AdGenSystemTimingBitsAClockHealth_Object = MibScalar
adGenSystemTimingBitsAClockHealth = _AdGenSystemTimingBitsAClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 4),
    _AdGenSystemTimingBitsAClockHealth_Type()
)
adGenSystemTimingBitsAClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingBitsAClockHealth.setStatus("current")
_AdGenSystemTimingBitsBClockHealth_Type = AdGenSystemTimingSourceHealth
_AdGenSystemTimingBitsBClockHealth_Object = MibScalar
adGenSystemTimingBitsBClockHealth = _AdGenSystemTimingBitsBClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 5),
    _AdGenSystemTimingBitsBClockHealth_Type()
)
adGenSystemTimingBitsBClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingBitsBClockHealth.setStatus("current")
_AdGenSystemTimingPrimaryClockHealth_Type = AdGenSystemTimingSourceHealth
_AdGenSystemTimingPrimaryClockHealth_Object = MibScalar
adGenSystemTimingPrimaryClockHealth = _AdGenSystemTimingPrimaryClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 6),
    _AdGenSystemTimingPrimaryClockHealth_Type()
)
adGenSystemTimingPrimaryClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingPrimaryClockHealth.setStatus("current")
_AdGenSystemTimingSecondaryClockHealth_Type = AdGenSystemTimingSourceHealth
_AdGenSystemTimingSecondaryClockHealth_Object = MibScalar
adGenSystemTimingSecondaryClockHealth = _AdGenSystemTimingSecondaryClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 7),
    _AdGenSystemTimingSecondaryClockHealth_Type()
)
adGenSystemTimingSecondaryClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingSecondaryClockHealth.setStatus("current")


class _AdGenSystemTimingCurrentHopCount_Type(Integer32):
    """Custom type adGenSystemTimingCurrentHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenSystemTimingCurrentHopCount_Type.__name__ = "Integer32"
_AdGenSystemTimingCurrentHopCount_Object = MibScalar
adGenSystemTimingCurrentHopCount = _AdGenSystemTimingCurrentHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 8),
    _AdGenSystemTimingCurrentHopCount_Type()
)
adGenSystemTimingCurrentHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingCurrentHopCount.setStatus("current")


class _AdGenSystemTimingCurrentTimingSourcePriority_Type(Integer32):
    """Custom type adGenSystemTimingCurrentTimingSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenSystemTimingCurrentTimingSourcePriority_Type.__name__ = "Integer32"
_AdGenSystemTimingCurrentTimingSourcePriority_Object = MibScalar
adGenSystemTimingCurrentTimingSourcePriority = _AdGenSystemTimingCurrentTimingSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 9),
    _AdGenSystemTimingCurrentTimingSourcePriority_Type()
)
adGenSystemTimingCurrentTimingSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingCurrentTimingSourcePriority.setStatus("current")
_AdGenSystemTimingCurrentTimingSourceQuality_Type = AdGenTimingSourceQuality
_AdGenSystemTimingCurrentTimingSourceQuality_Object = MibScalar
adGenSystemTimingCurrentTimingSourceQuality = _AdGenSystemTimingCurrentTimingSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 10),
    _AdGenSystemTimingCurrentTimingSourceQuality_Type()
)
adGenSystemTimingCurrentTimingSourceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingCurrentTimingSourceQuality.setStatus("current")


class _AdGenSystemTimingPrimaryHopCount_Type(Integer32):
    """Custom type adGenSystemTimingPrimaryHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenSystemTimingPrimaryHopCount_Type.__name__ = "Integer32"
_AdGenSystemTimingPrimaryHopCount_Object = MibScalar
adGenSystemTimingPrimaryHopCount = _AdGenSystemTimingPrimaryHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 11),
    _AdGenSystemTimingPrimaryHopCount_Type()
)
adGenSystemTimingPrimaryHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingPrimaryHopCount.setStatus("current")


class _AdGenSystemTimingPrimaryTimingSourcePriority_Type(Integer32):
    """Custom type adGenSystemTimingPrimaryTimingSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenSystemTimingPrimaryTimingSourcePriority_Type.__name__ = "Integer32"
_AdGenSystemTimingPrimaryTimingSourcePriority_Object = MibScalar
adGenSystemTimingPrimaryTimingSourcePriority = _AdGenSystemTimingPrimaryTimingSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 12),
    _AdGenSystemTimingPrimaryTimingSourcePriority_Type()
)
adGenSystemTimingPrimaryTimingSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingPrimaryTimingSourcePriority.setStatus("current")
_AdGenSystemTimingPrimaryTimingSourceQuality_Type = AdGenTimingSourceQuality
_AdGenSystemTimingPrimaryTimingSourceQuality_Object = MibScalar
adGenSystemTimingPrimaryTimingSourceQuality = _AdGenSystemTimingPrimaryTimingSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 13),
    _AdGenSystemTimingPrimaryTimingSourceQuality_Type()
)
adGenSystemTimingPrimaryTimingSourceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingPrimaryTimingSourceQuality.setStatus("current")


class _AdGenSystemTimingSecondaryHopCount_Type(Integer32):
    """Custom type adGenSystemTimingSecondaryHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenSystemTimingSecondaryHopCount_Type.__name__ = "Integer32"
_AdGenSystemTimingSecondaryHopCount_Object = MibScalar
adGenSystemTimingSecondaryHopCount = _AdGenSystemTimingSecondaryHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 14),
    _AdGenSystemTimingSecondaryHopCount_Type()
)
adGenSystemTimingSecondaryHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingSecondaryHopCount.setStatus("current")


class _AdGenSystemTimingSecondaryTimingSourcePriority_Type(Integer32):
    """Custom type adGenSystemTimingSecondaryTimingSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenSystemTimingSecondaryTimingSourcePriority_Type.__name__ = "Integer32"
_AdGenSystemTimingSecondaryTimingSourcePriority_Object = MibScalar
adGenSystemTimingSecondaryTimingSourcePriority = _AdGenSystemTimingSecondaryTimingSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 15),
    _AdGenSystemTimingSecondaryTimingSourcePriority_Type()
)
adGenSystemTimingSecondaryTimingSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingSecondaryTimingSourcePriority.setStatus("current")
_AdGenSystemTimingSecondaryTimingSourceQuality_Type = AdGenTimingSourceQuality
_AdGenSystemTimingSecondaryTimingSourceQuality_Object = MibScalar
adGenSystemTimingSecondaryTimingSourceQuality = _AdGenSystemTimingSecondaryTimingSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 16),
    _AdGenSystemTimingSecondaryTimingSourceQuality_Type()
)
adGenSystemTimingSecondaryTimingSourceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingSecondaryTimingSourceQuality.setStatus("current")


class _AdGenSystemTimingFallbackHopCount_Type(Integer32):
    """Custom type adGenSystemTimingFallbackHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenSystemTimingFallbackHopCount_Type.__name__ = "Integer32"
_AdGenSystemTimingFallbackHopCount_Object = MibScalar
adGenSystemTimingFallbackHopCount = _AdGenSystemTimingFallbackHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 17),
    _AdGenSystemTimingFallbackHopCount_Type()
)
adGenSystemTimingFallbackHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingFallbackHopCount.setStatus("current")


class _AdGenSystemTimingFallbackTimingSourcePriority_Type(Integer32):
    """Custom type adGenSystemTimingFallbackTimingSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenSystemTimingFallbackTimingSourcePriority_Type.__name__ = "Integer32"
_AdGenSystemTimingFallbackTimingSourcePriority_Object = MibScalar
adGenSystemTimingFallbackTimingSourcePriority = _AdGenSystemTimingFallbackTimingSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 18),
    _AdGenSystemTimingFallbackTimingSourcePriority_Type()
)
adGenSystemTimingFallbackTimingSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingFallbackTimingSourcePriority.setStatus("current")
_AdGenSystemTimingFallbackTimingSourceQuality_Type = AdGenTimingSourceQuality
_AdGenSystemTimingFallbackTimingSourceQuality_Object = MibScalar
adGenSystemTimingFallbackTimingSourceQuality = _AdGenSystemTimingFallbackTimingSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 2, 19),
    _AdGenSystemTimingFallbackTimingSourceQuality_Type()
)
adGenSystemTimingFallbackTimingSourceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemTimingFallbackTimingSourceQuality.setStatus("current")
_AdGenSystemTimingAlarmPrefix_ObjectIdentity = ObjectIdentity
adGenSystemTimingAlarmPrefix = _AdGenSystemTimingAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3)
)
_AdGenSystemTimingAlarms_ObjectIdentity = ObjectIdentity
adGenSystemTimingAlarms = _AdGenSystemTimingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3, 0)
)

# Managed Objects groups


# Notification objects

adGenSystemTimingSrcSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3, 0, 1)
)
adGenSystemTimingSrcSwitch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GEN-SYSTEM-TIMING-MIB", "adGenSystemTimingCurrentSource"))
)
if mibBuilder.loadTexts:
    adGenSystemTimingSrcSwitch.setStatus(
        "current"
    )

adGenSystemTimingPriSrcClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3, 0, 2)
)
adGenSystemTimingPriSrcClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adGenSystemTimingPriSrcClear.setStatus(
        "current"
    )

adGenSystemTimingPriSrcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3, 0, 3)
)
adGenSystemTimingPriSrcFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adGenSystemTimingPriSrcFail.setStatus(
        "current"
    )

adGenSystemTimingSecSrcClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3, 0, 4)
)
adGenSystemTimingSecSrcClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adGenSystemTimingSecSrcClear.setStatus(
        "current"
    )

adGenSystemTimingSecSrcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 13, 3, 0, 5)
)
adGenSystemTimingSecSrcFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adGenSystemTimingSecSrcFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-SYSTEM-TIMING-MIB",
    **{"AdGenTimingSource": AdGenTimingSource,
       "AdGenTimingSourceSelection": AdGenTimingSourceSelection,
       "AdGenExternalSource": AdGenExternalSource,
       "AdGenTimingConfigurationStatus": AdGenTimingConfigurationStatus,
       "AdGenExternalSourceType": AdGenExternalSourceType,
       "AdGenTimingSourceQuality": AdGenTimingSourceQuality,
       "AdGenSystemTimingSourceHealth": AdGenSystemTimingSourceHealth,
       "adGenSystemTimingProv": adGenSystemTimingProv,
       "adGenSystemTimingProvTable": adGenSystemTimingProvTable,
       "adGenSystemTimingProvEntry": adGenSystemTimingProvEntry,
       "adGenSystemTimingSource": adGenSystemTimingSource,
       "adGenSystemTimingSelection": adGenSystemTimingSelection,
       "adGenSystemTimingInterfaceType": adGenSystemTimingInterfaceType,
       "adGenSystemTimingShelf": adGenSystemTimingShelf,
       "adGenSystemTimingSlot": adGenSystemTimingSlot,
       "adGenSystemTimingPort": adGenSystemTimingPort,
       "adGenSystemTimingConfigurationStatus": adGenSystemTimingConfigurationStatus,
       "adGenSystemTimingExternalSourceProvTable": adGenSystemTimingExternalSourceProvTable,
       "adGenSystemTimingExternalSourceProvEntry": adGenSystemTimingExternalSourceProvEntry,
       "adGenSystemTimingExternalSourceId": adGenSystemTimingExternalSourceId,
       "adGenSystemTimingExternalSourceType": adGenSystemTimingExternalSourceType,
       "adGenSystemTimingExternalSourceQuality": adGenSystemTimingExternalSourceQuality,
       "adGenSystemTimingExternalSourcePriority": adGenSystemTimingExternalSourcePriority,
       "adGenSystemTimingExternalSourceHopCount": adGenSystemTimingExternalSourceHopCount,
       "adGenSystemTimingModeRevertive": adGenSystemTimingModeRevertive,
       "adGenSystemTimingForceClockFailover": adGenSystemTimingForceClockFailover,
       "adGenSystemTimingUseHopCount": adGenSystemTimingUseHopCount,
       "adGenSystemTimingSrcSwitchAlarmEnable": adGenSystemTimingSrcSwitchAlarmEnable,
       "adGenSystemTimingPriSrcFailAlarmEnable": adGenSystemTimingPriSrcFailAlarmEnable,
       "adGenSystemTimingSecSrcFailAlarmEnable": adGenSystemTimingSecSrcFailAlarmEnable,
       "adGenSystemTimingSelectionMode": adGenSystemTimingSelectionMode,
       "adGenSystemTimingProvPortTable": adGenSystemTimingProvPortTable,
       "adGenSystemTimingProvPortEntry": adGenSystemTimingProvPortEntry,
       "adGenSystemTimingTransmitSSMEnable": adGenSystemTimingTransmitSSMEnable,
       "adGenSystemTimingStatus": adGenSystemTimingStatus,
       "adGenSystemTimingCurrentSource": adGenSystemTimingCurrentSource,
       "adGenSystemTimingLoopAClockHealth": adGenSystemTimingLoopAClockHealth,
       "adGenSystemTimingLoopBClockHealth": adGenSystemTimingLoopBClockHealth,
       "adGenSystemTimingBitsAClockHealth": adGenSystemTimingBitsAClockHealth,
       "adGenSystemTimingBitsBClockHealth": adGenSystemTimingBitsBClockHealth,
       "adGenSystemTimingPrimaryClockHealth": adGenSystemTimingPrimaryClockHealth,
       "adGenSystemTimingSecondaryClockHealth": adGenSystemTimingSecondaryClockHealth,
       "adGenSystemTimingCurrentHopCount": adGenSystemTimingCurrentHopCount,
       "adGenSystemTimingCurrentTimingSourcePriority": adGenSystemTimingCurrentTimingSourcePriority,
       "adGenSystemTimingCurrentTimingSourceQuality": adGenSystemTimingCurrentTimingSourceQuality,
       "adGenSystemTimingPrimaryHopCount": adGenSystemTimingPrimaryHopCount,
       "adGenSystemTimingPrimaryTimingSourcePriority": adGenSystemTimingPrimaryTimingSourcePriority,
       "adGenSystemTimingPrimaryTimingSourceQuality": adGenSystemTimingPrimaryTimingSourceQuality,
       "adGenSystemTimingSecondaryHopCount": adGenSystemTimingSecondaryHopCount,
       "adGenSystemTimingSecondaryTimingSourcePriority": adGenSystemTimingSecondaryTimingSourcePriority,
       "adGenSystemTimingSecondaryTimingSourceQuality": adGenSystemTimingSecondaryTimingSourceQuality,
       "adGenSystemTimingFallbackHopCount": adGenSystemTimingFallbackHopCount,
       "adGenSystemTimingFallbackTimingSourcePriority": adGenSystemTimingFallbackTimingSourcePriority,
       "adGenSystemTimingFallbackTimingSourceQuality": adGenSystemTimingFallbackTimingSourceQuality,
       "adGenSystemTimingAlarmPrefix": adGenSystemTimingAlarmPrefix,
       "adGenSystemTimingAlarms": adGenSystemTimingAlarms,
       "adGenSystemTimingSrcSwitch": adGenSystemTimingSrcSwitch,
       "adGenSystemTimingPriSrcClear": adGenSystemTimingPriSrcClear,
       "adGenSystemTimingPriSrcFail": adGenSystemTimingPriSrcFail,
       "adGenSystemTimingSecSrcClear": adGenSystemTimingSecSrcClear,
       "adGenSystemTimingSecSrcFail": adGenSystemTimingSecSrcFail,
       "adGenSystemTimingMIB": adGenSystemTimingMIB}
)
