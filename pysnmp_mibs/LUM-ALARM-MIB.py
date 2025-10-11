# SNMP MIB module (LUM-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:45 2025
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

(lumAlarmMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumAlarmMIB",
    "lumModules")

(CommandString,
 FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "FaultStatus",
    "MgmtNameString")

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
 PhysAddress,
 RowPointer,
 TextualConvention,
 TestAndIncr,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TestAndIncr",
    "VariablePointer")


# MODULE-IDENTITY

lumAlarmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lumAlarmMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2011-03-24 00:00",
         "2005-09-19 00:00",
         "2005-07-07 00:00",
         "2005-04-29 00:00",
         "2005-02-07 00:00",
         "2004-09-30 00:00",
         "2003-09-23 00:00",
         "2003-08-07 00:00",
         "2003-03-05 00:00",
         "2002-01-10 00:00",
         "2001-10-30 00:00",
         "2001-10-11 00:00",
         "2001-09-13 00:00",
         "2001-07-17 00:00",
         "2001-05-10 00:00",
         "2001-03-12 00:00",
         "2001-03-08 00:00",
         "2001-03-05 00:00",
         "2001-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmNotificationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("communications", 1),
          ("qualityOfService", 2),
          ("processingError", 3),
          ("equipment", 4),
          ("environmental", 5))
    )



class AlarmPerceivedSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("cleared", 1),
          ("indeterminate", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )



class AlarmProbableCause(TextualConvention, Integer32):
    status = "current"
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("adapterError", 1),
          ("applicationSubsystemFailure", 2),
          ("bandwidthReduced", 3),
          ("callEstablishmentError", 4),
          ("communicationsProtocolError", 5),
          ("communicationsSubsystemFailure", 6),
          ("configurationOrCustomizationError", 7),
          ("congestion", 8),
          ("corruptData", 9),
          ("cpuCyclesLimitExceeded", 10),
          ("dTEdCEInterfaceError", 11),
          ("datasetOrModemError", 12),
          ("degradedSignal", 13),
          ("enclosureDoorOpen", 14),
          ("equipmentMalfunction", 15),
          ("excessiveVibration", 16),
          ("fileError", 17),
          ("fireDetected", 18),
          ("floodDetected", 19),
          ("framingError", 20),
          ("heatingOrVentilationOrCoolingSystemProblem", 21),
          ("humidityUnacceptable", 22),
          ("inputDeviceError", 23),
          ("inputOutputDeviceError", 24),
          ("lANError", 25),
          ("leakDetected", 26),
          ("localNodeTransmissionError", 27),
          ("lossOfFrame", 28),
          ("lossOfSignal", 29),
          ("materialSupplyExhausted", 30),
          ("multiplexerProblem", 31),
          ("outOfMemory", 32),
          ("outputDeviceError", 33),
          ("performanceDegraded", 34),
          ("powerProblem", 35),
          ("pressureUnacceptable", 36),
          ("processorProblem", 37),
          ("pumpFailure", 38),
          ("queueSizeExceeded", 39),
          ("receiveFailure", 40),
          ("receiverFailure", 41),
          ("remoteNodeTransmissionError", 42),
          ("resourceAtOrNearingCapacity", 43),
          ("responseTimeExcessive", 44),
          ("retransmissionRateExcessive", 45),
          ("softwareProgramError", 46),
          ("softwareError", 47),
          ("softwareProgramAbnormallyTerminated", 48),
          ("storageCapacityProblem", 49),
          ("temperatureUnacceptable", 50),
          ("thresholdCrossed", 51),
          ("timingProblem", 52),
          ("toxicLeakDetected", 53),
          ("transmitFailure", 54),
          ("transmitterFailure", 55),
          ("underlyingResourceUnavailable", 56),
          ("versionMismatch", 57))
    )



class AlarmEventCategory(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("state", 1),
          ("configuration", 2),
          ("maintenance", 3),
          ("alarm", 4),
          ("auth", 5),
          ("authPriv", 6))
    )



# MIB Managed Objects in the order of their OIDs

_LumAlarmConfs_ObjectIdentity = ObjectIdentity
lumAlarmConfs = _LumAlarmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1)
)
_LumAlarmGroups_ObjectIdentity = ObjectIdentity
lumAlarmGroups = _LumAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1)
)
_LumAlarmCompl_ObjectIdentity = ObjectIdentity
lumAlarmCompl = _LumAlarmCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2)
)
_LumAlarmMinimalGroups_ObjectIdentity = ObjectIdentity
lumAlarmMinimalGroups = _LumAlarmMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 3)
)
_LumAlarmMinimalCompl_ObjectIdentity = ObjectIdentity
lumAlarmMinimalCompl = _LumAlarmMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 4)
)
_LumAlarmMIBObjects_ObjectIdentity = ObjectIdentity
lumAlarmMIBObjects = _LumAlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2)
)
_AlarmGeneral_ObjectIdentity = ObjectIdentity
alarmGeneral = _AlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1)
)
_AlarmGeneralLastChangeTime_Type = DateAndTime
_AlarmGeneralLastChangeTime_Object = MibScalar
alarmGeneralLastChangeTime = _AlarmGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 1),
    _AlarmGeneralLastChangeTime_Type()
)
alarmGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralLastChangeTime.setStatus("current")


class _AlarmGeneralLogSize_Type(Unsigned32):
    """Custom type alarmGeneralLogSize based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_AlarmGeneralLogSize_Type.__name__ = "Unsigned32"
_AlarmGeneralLogSize_Object = MibScalar
alarmGeneralLogSize = _AlarmGeneralLogSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 2),
    _AlarmGeneralLogSize_Type()
)
alarmGeneralLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralLogSize.setStatus("current")
_AlarmGeneralLastSeqNumber_Type = Counter32
_AlarmGeneralLastSeqNumber_Object = MibScalar
alarmGeneralLastSeqNumber = _AlarmGeneralLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 3),
    _AlarmGeneralLastSeqNumber_Type()
)
alarmGeneralLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralLastSeqNumber.setStatus("current")


class _AlarmGeneralReplayBufferSize_Type(Unsigned32):
    """Custom type alarmGeneralReplayBufferSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlarmGeneralReplayBufferSize_Type.__name__ = "Unsigned32"
_AlarmGeneralReplayBufferSize_Object = MibScalar
alarmGeneralReplayBufferSize = _AlarmGeneralReplayBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 4),
    _AlarmGeneralReplayBufferSize_Type()
)
alarmGeneralReplayBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralReplayBufferSize.setStatus("deprecated")


class _AlarmGeneralReplayRequestSeq_Type(Unsigned32):
    """Custom type alarmGeneralReplayRequestSeq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlarmGeneralReplayRequestSeq_Type.__name__ = "Unsigned32"
_AlarmGeneralReplayRequestSeq_Object = MibScalar
alarmGeneralReplayRequestSeq = _AlarmGeneralReplayRequestSeq_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 5),
    _AlarmGeneralReplayRequestSeq_Type()
)
alarmGeneralReplayRequestSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralReplayRequestSeq.setStatus("deprecated")
_AlarmGeneralReplayRequestTime_Type = DateAndTime
_AlarmGeneralReplayRequestTime_Object = MibScalar
alarmGeneralReplayRequestTime = _AlarmGeneralReplayRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 6),
    _AlarmGeneralReplayRequestTime_Type()
)
alarmGeneralReplayRequestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralReplayRequestTime.setStatus("deprecated")
_AlarmGeneralTestAndIncr_Type = TestAndIncr
_AlarmGeneralTestAndIncr_Object = MibScalar
alarmGeneralTestAndIncr = _AlarmGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 7),
    _AlarmGeneralTestAndIncr_Type()
)
alarmGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralTestAndIncr.setStatus("current")


class _AlarmGeneralMibSpecVersion_Type(DisplayString):
    """Custom type alarmGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_AlarmGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_AlarmGeneralMibSpecVersion_Object = MibScalar
alarmGeneralMibSpecVersion = _AlarmGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 8),
    _AlarmGeneralMibSpecVersion_Type()
)
alarmGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralMibSpecVersion.setStatus("current")


class _AlarmGeneralMibImplVersion_Type(DisplayString):
    """Custom type alarmGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_AlarmGeneralMibImplVersion_Type.__name__ = "DisplayString"
_AlarmGeneralMibImplVersion_Object = MibScalar
alarmGeneralMibImplVersion = _AlarmGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 9),
    _AlarmGeneralMibImplVersion_Type()
)
alarmGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralMibImplVersion.setStatus("current")


class _AlarmGeneralSuppressionMode_Type(Integer32):
    """Custom type alarmGeneralSuppressionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmGeneralSuppressionMode_Type.__name__ = "Integer32"
_AlarmGeneralSuppressionMode_Object = MibScalar
alarmGeneralSuppressionMode = _AlarmGeneralSuppressionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 10),
    _AlarmGeneralSuppressionMode_Type()
)
alarmGeneralSuppressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralSuppressionMode.setStatus("current")


class _AlarmGeneralFilterMode_Type(Integer32):
    """Custom type alarmGeneralFilterMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmGeneralFilterMode_Type.__name__ = "Integer32"
_AlarmGeneralFilterMode_Object = MibScalar
alarmGeneralFilterMode = _AlarmGeneralFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 11),
    _AlarmGeneralFilterMode_Type()
)
alarmGeneralFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralFilterMode.setStatus("current")
_AlarmGeneralConfigLastChangeTime_Type = DateAndTime
_AlarmGeneralConfigLastChangeTime_Object = MibScalar
alarmGeneralConfigLastChangeTime = _AlarmGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 12),
    _AlarmGeneralConfigLastChangeTime_Type()
)
alarmGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralConfigLastChangeTime.setStatus("current")
_AlarmGeneralAlarmTableSize_Type = Unsigned32
_AlarmGeneralAlarmTableSize_Object = MibScalar
alarmGeneralAlarmTableSize = _AlarmGeneralAlarmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 13),
    _AlarmGeneralAlarmTableSize_Type()
)
alarmGeneralAlarmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralAlarmTableSize.setStatus("current")
_AlarmGeneralAlarmLogTableSize_Type = Unsigned32
_AlarmGeneralAlarmLogTableSize_Object = MibScalar
alarmGeneralAlarmLogTableSize = _AlarmGeneralAlarmLogTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 14),
    _AlarmGeneralAlarmLogTableSize_Type()
)
alarmGeneralAlarmLogTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralAlarmLogTableSize.setStatus("current")


class _AlarmGeneralHeartBeatInterval_Type(Unsigned32):
    """Custom type alarmGeneralHeartBeatInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlarmGeneralHeartBeatInterval_Type.__name__ = "Unsigned32"
_AlarmGeneralHeartBeatInterval_Object = MibScalar
alarmGeneralHeartBeatInterval = _AlarmGeneralHeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 15),
    _AlarmGeneralHeartBeatInterval_Type()
)
alarmGeneralHeartBeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralHeartBeatInterval.setStatus("current")
_AlarmGeneralAlarmLog2TableSize_Type = Unsigned32
_AlarmGeneralAlarmLog2TableSize_Object = MibScalar
alarmGeneralAlarmLog2TableSize = _AlarmGeneralAlarmLog2TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 16),
    _AlarmGeneralAlarmLog2TableSize_Type()
)
alarmGeneralAlarmLog2TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralAlarmLog2TableSize.setStatus("current")


class _AlarmGeneralAlarmNotificationVersion_Type(Integer32):
    """Custom type alarmGeneralAlarmNotificationVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_AlarmGeneralAlarmNotificationVersion_Type.__name__ = "Integer32"
_AlarmGeneralAlarmNotificationVersion_Object = MibScalar
alarmGeneralAlarmNotificationVersion = _AlarmGeneralAlarmNotificationVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 17),
    _AlarmGeneralAlarmNotificationVersion_Type()
)
alarmGeneralAlarmNotificationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralAlarmNotificationVersion.setStatus("current")


class _AlarmGeneralAlarmLog2Size_Type(Unsigned32):
    """Custom type alarmGeneralAlarmLog2Size based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_AlarmGeneralAlarmLog2Size_Type.__name__ = "Unsigned32"
_AlarmGeneralAlarmLog2Size_Object = MibScalar
alarmGeneralAlarmLog2Size = _AlarmGeneralAlarmLog2Size_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 18),
    _AlarmGeneralAlarmLog2Size_Type()
)
alarmGeneralAlarmLog2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralAlarmLog2Size.setStatus("current")
_AlarmGeneralHighestSeverity_Type = AlarmPerceivedSeverity
_AlarmGeneralHighestSeverity_Object = MibScalar
alarmGeneralHighestSeverity = _AlarmGeneralHighestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 19),
    _AlarmGeneralHighestSeverity_Type()
)
alarmGeneralHighestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralHighestSeverity.setStatus("current")
_AlarmGeneralEventLogTableSize_Type = Unsigned32
_AlarmGeneralEventLogTableSize_Object = MibScalar
alarmGeneralEventLogTableSize = _AlarmGeneralEventLogTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 20),
    _AlarmGeneralEventLogTableSize_Type()
)
alarmGeneralEventLogTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralEventLogTableSize.setStatus("current")


class _AlarmGeneralEventLogSize_Type(Unsigned32):
    """Custom type alarmGeneralEventLogSize based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_AlarmGeneralEventLogSize_Type.__name__ = "Unsigned32"
_AlarmGeneralEventLogSize_Object = MibScalar
alarmGeneralEventLogSize = _AlarmGeneralEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 21),
    _AlarmGeneralEventLogSize_Type()
)
alarmGeneralEventLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralEventLogSize.setStatus("current")
_AlarmGeneralEventLastSeqNumber_Type = Counter32
_AlarmGeneralEventLastSeqNumber_Object = MibScalar
alarmGeneralEventLastSeqNumber = _AlarmGeneralEventLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 22),
    _AlarmGeneralEventLastSeqNumber_Type()
)
alarmGeneralEventLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneralEventLastSeqNumber.setStatus("current")


class _AlarmGeneralSoakInInterval_Type(Unsigned32):
    """Custom type alarmGeneralSoakInInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AlarmGeneralSoakInInterval_Type.__name__ = "Unsigned32"
_AlarmGeneralSoakInInterval_Object = MibScalar
alarmGeneralSoakInInterval = _AlarmGeneralSoakInInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 1, 23),
    _AlarmGeneralSoakInInterval_Type()
)
alarmGeneralSoakInInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGeneralSoakInInterval.setStatus("current")
_AlarmList_ObjectIdentity = ObjectIdentity
alarmList = _AlarmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "LUM-ALARM-MIB", "alarmSeqNumber"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmIndex_Type(Unsigned32):
    """Custom type alarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmIndex_Type.__name__ = "Unsigned32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmObject_Type = RowPointer
_AlarmObject_Object = MibTableColumn
alarmObject = _AlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 2),
    _AlarmObject_Type()
)
alarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmObject.setStatus("current")
_AlarmFaultStatus_Type = VariablePointer
_AlarmFaultStatus_Object = MibTableColumn
alarmFaultStatus = _AlarmFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 3),
    _AlarmFaultStatus_Type()
)
alarmFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmFaultStatus.setStatus("current")
_AlarmMgmtName_Type = MgmtNameString
_AlarmMgmtName_Object = MibTableColumn
alarmMgmtName = _AlarmMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 4),
    _AlarmMgmtName_Type()
)
alarmMgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMgmtName.setStatus("current")


class _AlarmInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type alarmInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmInvPhysIndexOrZero_Object = MibTableColumn
alarmInvPhysIndexOrZero = _AlarmInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 5),
    _AlarmInvPhysIndexOrZero_Type()
)
alarmInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInvPhysIndexOrZero.setStatus("current")


class _AlarmInvLogicalIndexOrZero_Type(Unsigned32):
    """Custom type alarmInvLogicalIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmInvLogicalIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmInvLogicalIndexOrZero_Object = MibTableColumn
alarmInvLogicalIndexOrZero = _AlarmInvLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 6),
    _AlarmInvLogicalIndexOrZero_Type()
)
alarmInvLogicalIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInvLogicalIndexOrZero.setStatus("current")
_AlarmType_Type = AlarmNotificationType
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 7),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmCause_Type = AlarmProbableCause
_AlarmCause_Object = MibTableColumn
alarmCause = _AlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 8),
    _AlarmCause_Type()
)
alarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCause.setStatus("current")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibTableColumn
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 9),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("current")
_AlarmSeverity_Type = AlarmPerceivedSeverity
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 10),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmCreatedTime_Type = DateAndTime
_AlarmCreatedTime_Object = MibTableColumn
alarmCreatedTime = _AlarmCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 11),
    _AlarmCreatedTime_Type()
)
alarmCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCreatedTime.setStatus("current")
_AlarmLastChangeTime_Type = DateAndTime
_AlarmLastChangeTime_Object = MibTableColumn
alarmLastChangeTime = _AlarmLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 12),
    _AlarmLastChangeTime_Type()
)
alarmLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLastChangeTime.setStatus("current")
_AlarmSeqNumber_Type = Counter32
_AlarmSeqNumber_Object = MibTableColumn
alarmSeqNumber = _AlarmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 13),
    _AlarmSeqNumber_Type()
)
alarmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeqNumber.setStatus("current")
_AlarmNeName_Type = DisplayString
_AlarmNeName_Object = MibTableColumn
alarmNeName = _AlarmNeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 14),
    _AlarmNeName_Type()
)
alarmNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNeName.setStatus("current")
_AlarmNeIpAddress_Type = IpAddress
_AlarmNeIpAddress_Object = MibTableColumn
alarmNeIpAddress = _AlarmNeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 2, 1, 1, 15),
    _AlarmNeIpAddress_Type()
)
alarmNeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNeIpAddress.setStatus("current")
_LumentisAlarmNotifications_ObjectIdentity = ObjectIdentity
lumentisAlarmNotifications = _LumentisAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3)
)
_AlarmNotifyPrefix_ObjectIdentity = ObjectIdentity
alarmNotifyPrefix = _AlarmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0)
)
_AlarmSum_ObjectIdentity = ObjectIdentity
alarmSum = _AlarmSum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4)
)
_AlarmSumActiveIndeterminate_Type = Counter32
_AlarmSumActiveIndeterminate_Object = MibScalar
alarmSumActiveIndeterminate = _AlarmSumActiveIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 1),
    _AlarmSumActiveIndeterminate_Type()
)
alarmSumActiveIndeterminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumActiveIndeterminate.setStatus("current")
_AlarmSumTotalIndeterminate_Type = Counter32
_AlarmSumTotalIndeterminate_Object = MibScalar
alarmSumTotalIndeterminate = _AlarmSumTotalIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 2),
    _AlarmSumTotalIndeterminate_Type()
)
alarmSumTotalIndeterminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumTotalIndeterminate.setStatus("current")
_AlarmSumActiveWarning_Type = Counter32
_AlarmSumActiveWarning_Object = MibScalar
alarmSumActiveWarning = _AlarmSumActiveWarning_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 3),
    _AlarmSumActiveWarning_Type()
)
alarmSumActiveWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumActiveWarning.setStatus("current")
_AlarmSumTotalWarning_Type = Counter32
_AlarmSumTotalWarning_Object = MibScalar
alarmSumTotalWarning = _AlarmSumTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 4),
    _AlarmSumTotalWarning_Type()
)
alarmSumTotalWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumTotalWarning.setStatus("current")
_AlarmSumActiveMinor_Type = Counter32
_AlarmSumActiveMinor_Object = MibScalar
alarmSumActiveMinor = _AlarmSumActiveMinor_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 5),
    _AlarmSumActiveMinor_Type()
)
alarmSumActiveMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumActiveMinor.setStatus("current")
_AlarmSumTotalMinor_Type = Counter32
_AlarmSumTotalMinor_Object = MibScalar
alarmSumTotalMinor = _AlarmSumTotalMinor_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 6),
    _AlarmSumTotalMinor_Type()
)
alarmSumTotalMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumTotalMinor.setStatus("current")
_AlarmSumActiveMajor_Type = Counter32
_AlarmSumActiveMajor_Object = MibScalar
alarmSumActiveMajor = _AlarmSumActiveMajor_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 7),
    _AlarmSumActiveMajor_Type()
)
alarmSumActiveMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumActiveMajor.setStatus("current")
_AlarmSumTotalMajor_Type = Counter32
_AlarmSumTotalMajor_Object = MibScalar
alarmSumTotalMajor = _AlarmSumTotalMajor_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 8),
    _AlarmSumTotalMajor_Type()
)
alarmSumTotalMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumTotalMajor.setStatus("current")
_AlarmSumActiveCritical_Type = Counter32
_AlarmSumActiveCritical_Object = MibScalar
alarmSumActiveCritical = _AlarmSumActiveCritical_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 9),
    _AlarmSumActiveCritical_Type()
)
alarmSumActiveCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumActiveCritical.setStatus("current")
_AlarmSumTotalCritical_Type = Counter32
_AlarmSumTotalCritical_Object = MibScalar
alarmSumTotalCritical = _AlarmSumTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 10),
    _AlarmSumTotalCritical_Type()
)
alarmSumTotalCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumTotalCritical.setStatus("current")
_AlarmSumTotalActive_Type = Counter32
_AlarmSumTotalActive_Object = MibScalar
alarmSumTotalActive = _AlarmSumTotalActive_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 4, 11),
    _AlarmSumTotalActive_Type()
)
alarmSumTotalActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSumTotalActive.setStatus("current")
_AlarmTest_ObjectIdentity = ObjectIdentity
alarmTest = _AlarmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5)
)
_AlarmTestCommunication_Type = FaultStatus
_AlarmTestCommunication_Object = MibScalar
alarmTestCommunication = _AlarmTestCommunication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 1),
    _AlarmTestCommunication_Type()
)
alarmTestCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTestCommunication.setStatus("current")
_AlarmTestQualityOfService_Type = FaultStatus
_AlarmTestQualityOfService_Object = MibScalar
alarmTestQualityOfService = _AlarmTestQualityOfService_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 2),
    _AlarmTestQualityOfService_Type()
)
alarmTestQualityOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTestQualityOfService.setStatus("current")
_AlarmTestProcessingError_Type = FaultStatus
_AlarmTestProcessingError_Object = MibScalar
alarmTestProcessingError = _AlarmTestProcessingError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 3),
    _AlarmTestProcessingError_Type()
)
alarmTestProcessingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTestProcessingError.setStatus("current")
_AlarmTestEquipment_Type = FaultStatus
_AlarmTestEquipment_Object = MibScalar
alarmTestEquipment = _AlarmTestEquipment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 4),
    _AlarmTestEquipment_Type()
)
alarmTestEquipment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTestEquipment.setStatus("current")
_AlarmTestEnvironmental_Type = FaultStatus
_AlarmTestEnvironmental_Object = MibScalar
alarmTestEnvironmental = _AlarmTestEnvironmental_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 5),
    _AlarmTestEnvironmental_Type()
)
alarmTestEnvironmental.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTestEnvironmental.setStatus("current")
_AlarmTestNonPrintable_Type = OctetString
_AlarmTestNonPrintable_Object = MibScalar
alarmTestNonPrintable = _AlarmTestNonPrintable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 6),
    _AlarmTestNonPrintable_Type()
)
alarmTestNonPrintable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTestNonPrintable.setStatus("current")
_AlarmTestConfirm_Type = DisplayString
_AlarmTestConfirm_Object = MibScalar
alarmTestConfirm = _AlarmTestConfirm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 7),
    _AlarmTestConfirm_Type()
)
alarmTestConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestConfirm.setStatus("current")
_AlarmTestMsg_Type = DisplayString
_AlarmTestMsg_Object = MibScalar
alarmTestMsg = _AlarmTestMsg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 8),
    _AlarmTestMsg_Type()
)
alarmTestMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestMsg.setStatus("current")
_AlarmTestSetAlarms_Type = CommandString
_AlarmTestSetAlarms_Object = MibScalar
alarmTestSetAlarms = _AlarmTestSetAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 9),
    _AlarmTestSetAlarms_Type()
)
alarmTestSetAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestSetAlarms.setStatus("current")
_AlarmTestQueryAlarms_Type = CommandString
_AlarmTestQueryAlarms_Object = MibScalar
alarmTestQueryAlarms = _AlarmTestQueryAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 10),
    _AlarmTestQueryAlarms_Type()
)
alarmTestQueryAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestQueryAlarms.setStatus("current")


class _AlarmTestSetCommunication_Type(Integer32):
    """Custom type alarmTestSetCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_AlarmTestSetCommunication_Type.__name__ = "Integer32"
_AlarmTestSetCommunication_Object = MibScalar
alarmTestSetCommunication = _AlarmTestSetCommunication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 11),
    _AlarmTestSetCommunication_Type()
)
alarmTestSetCommunication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestSetCommunication.setStatus("current")


class _AlarmTestSetQualityOfService_Type(Integer32):
    """Custom type alarmTestSetQualityOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_AlarmTestSetQualityOfService_Type.__name__ = "Integer32"
_AlarmTestSetQualityOfService_Object = MibScalar
alarmTestSetQualityOfService = _AlarmTestSetQualityOfService_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 12),
    _AlarmTestSetQualityOfService_Type()
)
alarmTestSetQualityOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestSetQualityOfService.setStatus("current")


class _AlarmTestSetProcessingError_Type(Integer32):
    """Custom type alarmTestSetProcessingError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_AlarmTestSetProcessingError_Type.__name__ = "Integer32"
_AlarmTestSetProcessingError_Object = MibScalar
alarmTestSetProcessingError = _AlarmTestSetProcessingError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 13),
    _AlarmTestSetProcessingError_Type()
)
alarmTestSetProcessingError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestSetProcessingError.setStatus("current")


class _AlarmTestSetEquipment_Type(Integer32):
    """Custom type alarmTestSetEquipment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_AlarmTestSetEquipment_Type.__name__ = "Integer32"
_AlarmTestSetEquipment_Object = MibScalar
alarmTestSetEquipment = _AlarmTestSetEquipment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 14),
    _AlarmTestSetEquipment_Type()
)
alarmTestSetEquipment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestSetEquipment.setStatus("current")


class _AlarmTestSetEnvironmental_Type(Integer32):
    """Custom type alarmTestSetEnvironmental based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_AlarmTestSetEnvironmental_Type.__name__ = "Integer32"
_AlarmTestSetEnvironmental_Object = MibScalar
alarmTestSetEnvironmental = _AlarmTestSetEnvironmental_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 5, 15),
    _AlarmTestSetEnvironmental_Type()
)
alarmTestSetEnvironmental.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTestSetEnvironmental.setStatus("current")
_AlarmLog_ObjectIdentity = ObjectIdentity
alarmLog = _AlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6)
)
_AlarmLogTable_Object = MibTable
alarmLogTable = _AlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    alarmLogTable.setStatus("current")
_AlarmLogEntry_Object = MibTableRow
alarmLogEntry = _AlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1)
)
alarmLogEntry.setIndexNames(
    (0, "LUM-ALARM-MIB", "alarmLogSeqNumber"),
)
if mibBuilder.loadTexts:
    alarmLogEntry.setStatus("current")


class _AlarmLogIndex_Type(Unsigned32):
    """Custom type alarmLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmLogIndex_Type.__name__ = "Unsigned32"
_AlarmLogIndex_Object = MibTableColumn
alarmLogIndex = _AlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 1),
    _AlarmLogIndex_Type()
)
alarmLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogIndex.setStatus("current")
_AlarmLogObject_Type = RowPointer
_AlarmLogObject_Object = MibTableColumn
alarmLogObject = _AlarmLogObject_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 2),
    _AlarmLogObject_Type()
)
alarmLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogObject.setStatus("current")
_AlarmLogFaultStatus_Type = VariablePointer
_AlarmLogFaultStatus_Object = MibTableColumn
alarmLogFaultStatus = _AlarmLogFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 3),
    _AlarmLogFaultStatus_Type()
)
alarmLogFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogFaultStatus.setStatus("current")
_AlarmLogMgmtName_Type = MgmtNameString
_AlarmLogMgmtName_Object = MibTableColumn
alarmLogMgmtName = _AlarmLogMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 4),
    _AlarmLogMgmtName_Type()
)
alarmLogMgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogMgmtName.setStatus("current")


class _AlarmLogInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type alarmLogInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmLogInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmLogInvPhysIndexOrZero_Object = MibTableColumn
alarmLogInvPhysIndexOrZero = _AlarmLogInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 5),
    _AlarmLogInvPhysIndexOrZero_Type()
)
alarmLogInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogInvPhysIndexOrZero.setStatus("current")


class _AlarmLogInvLogicalIndexOrZero_Type(Unsigned32):
    """Custom type alarmLogInvLogicalIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmLogInvLogicalIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmLogInvLogicalIndexOrZero_Object = MibTableColumn
alarmLogInvLogicalIndexOrZero = _AlarmLogInvLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 6),
    _AlarmLogInvLogicalIndexOrZero_Type()
)
alarmLogInvLogicalIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogInvLogicalIndexOrZero.setStatus("current")
_AlarmLogType_Type = AlarmNotificationType
_AlarmLogType_Object = MibTableColumn
alarmLogType = _AlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 7),
    _AlarmLogType_Type()
)
alarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogType.setStatus("current")
_AlarmLogCause_Type = AlarmProbableCause
_AlarmLogCause_Object = MibTableColumn
alarmLogCause = _AlarmLogCause_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 8),
    _AlarmLogCause_Type()
)
alarmLogCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogCause.setStatus("current")
_AlarmLogText_Type = DisplayString
_AlarmLogText_Object = MibTableColumn
alarmLogText = _AlarmLogText_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 9),
    _AlarmLogText_Type()
)
alarmLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogText.setStatus("current")
_AlarmLogSeverity_Type = AlarmPerceivedSeverity
_AlarmLogSeverity_Object = MibTableColumn
alarmLogSeverity = _AlarmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 10),
    _AlarmLogSeverity_Type()
)
alarmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogSeverity.setStatus("current")
_AlarmLogCreatedTime_Type = DateAndTime
_AlarmLogCreatedTime_Object = MibTableColumn
alarmLogCreatedTime = _AlarmLogCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 11),
    _AlarmLogCreatedTime_Type()
)
alarmLogCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogCreatedTime.setStatus("current")
_AlarmLogLastChangeTime_Type = DateAndTime
_AlarmLogLastChangeTime_Object = MibTableColumn
alarmLogLastChangeTime = _AlarmLogLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 12),
    _AlarmLogLastChangeTime_Type()
)
alarmLogLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogLastChangeTime.setStatus("current")
_AlarmLogSeqNumber_Type = Counter32
_AlarmLogSeqNumber_Object = MibTableColumn
alarmLogSeqNumber = _AlarmLogSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 13),
    _AlarmLogSeqNumber_Type()
)
alarmLogSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogSeqNumber.setStatus("current")
_AlarmLogPrevSeverity_Type = AlarmPerceivedSeverity
_AlarmLogPrevSeverity_Object = MibTableColumn
alarmLogPrevSeverity = _AlarmLogPrevSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 14),
    _AlarmLogPrevSeverity_Type()
)
alarmLogPrevSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogPrevSeverity.setStatus("current")


class _AlarmLogNeName_Type(DisplayString):
    """Custom type alarmLogNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmLogNeName_Type.__name__ = "DisplayString"
_AlarmLogNeName_Object = MibTableColumn
alarmLogNeName = _AlarmLogNeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 15),
    _AlarmLogNeName_Type()
)
alarmLogNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogNeName.setStatus("current")
_AlarmLogNeIpAddress_Type = IpAddress
_AlarmLogNeIpAddress_Object = MibTableColumn
alarmLogNeIpAddress = _AlarmLogNeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 6, 1, 1, 16),
    _AlarmLogNeIpAddress_Type()
)
alarmLogNeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogNeIpAddress.setStatus("current")
_AlarmRemote_ObjectIdentity = ObjectIdentity
alarmRemote = _AlarmRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7)
)
_AlarmRemoteNotReachable_Type = FaultStatus
_AlarmRemoteNotReachable_Object = MibScalar
alarmRemoteNotReachable = _AlarmRemoteNotReachable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 1),
    _AlarmRemoteNotReachable_Type()
)
alarmRemoteNotReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteNotReachable.setStatus("current")
_AlarmRemoteConnectionFailed_Type = FaultStatus
_AlarmRemoteConnectionFailed_Object = MibScalar
alarmRemoteConnectionFailed = _AlarmRemoteConnectionFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 2),
    _AlarmRemoteConnectionFailed_Type()
)
alarmRemoteConnectionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteConnectionFailed.setStatus("current")
_AlarmTimeWindowFailed_Type = FaultStatus
_AlarmTimeWindowFailed_Object = MibScalar
alarmTimeWindowFailed = _AlarmTimeWindowFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 3),
    _AlarmTimeWindowFailed_Type()
)
alarmTimeWindowFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTimeWindowFailed.setStatus("current")
_AlarmRemoteLoginFailed_Type = FaultStatus
_AlarmRemoteLoginFailed_Object = MibScalar
alarmRemoteLoginFailed = _AlarmRemoteLoginFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 4),
    _AlarmRemoteLoginFailed_Type()
)
alarmRemoteLoginFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteLoginFailed.setStatus("current")
_AlarmRemoteMibRefreshFailed_Type = FaultStatus
_AlarmRemoteMibRefreshFailed_Object = MibScalar
alarmRemoteMibRefreshFailed = _AlarmRemoteMibRefreshFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 5),
    _AlarmRemoteMibRefreshFailed_Type()
)
alarmRemoteMibRefreshFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteMibRefreshFailed.setStatus("current")
_AlarmRemoteLocalTimeDiffFailed_Type = FaultStatus
_AlarmRemoteLocalTimeDiffFailed_Object = MibScalar
alarmRemoteLocalTimeDiffFailed = _AlarmRemoteLocalTimeDiffFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 6),
    _AlarmRemoteLocalTimeDiffFailed_Type()
)
alarmRemoteLocalTimeDiffFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteLocalTimeDiffFailed.setStatus("current")
_AlarmRemoteBackupUnsavedFailed_Type = FaultStatus
_AlarmRemoteBackupUnsavedFailed_Object = MibScalar
alarmRemoteBackupUnsavedFailed = _AlarmRemoteBackupUnsavedFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 7),
    _AlarmRemoteBackupUnsavedFailed_Type()
)
alarmRemoteBackupUnsavedFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteBackupUnsavedFailed.setStatus("current")
_AlarmRemotePmFtpFailed_Type = FaultStatus
_AlarmRemotePmFtpFailed_Object = MibScalar
alarmRemotePmFtpFailed = _AlarmRemotePmFtpFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 8),
    _AlarmRemotePmFtpFailed_Type()
)
alarmRemotePmFtpFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemotePmFtpFailed.setStatus("current")
_AlarmRemoteNotificationOverflowFailed_Type = FaultStatus
_AlarmRemoteNotificationOverflowFailed_Object = MibScalar
alarmRemoteNotificationOverflowFailed = _AlarmRemoteNotificationOverflowFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 9),
    _AlarmRemoteNotificationOverflowFailed_Type()
)
alarmRemoteNotificationOverflowFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteNotificationOverflowFailed.setStatus("current")
_AlarmRemoteAlarmsIgnored_Type = FaultStatus
_AlarmRemoteAlarmsIgnored_Object = MibScalar
alarmRemoteAlarmsIgnored = _AlarmRemoteAlarmsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 10),
    _AlarmRemoteAlarmsIgnored_Type()
)
alarmRemoteAlarmsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteAlarmsIgnored.setStatus("current")
_AlarmRemoteSoftwareNotSupported_Type = FaultStatus
_AlarmRemoteSoftwareNotSupported_Object = MibScalar
alarmRemoteSoftwareNotSupported = _AlarmRemoteSoftwareNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 11),
    _AlarmRemoteSoftwareNotSupported_Type()
)
alarmRemoteSoftwareNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteSoftwareNotSupported.setStatus("current")
_AlarmRemoteUnexpectedNodeFamily_Type = FaultStatus
_AlarmRemoteUnexpectedNodeFamily_Object = MibScalar
alarmRemoteUnexpectedNodeFamily = _AlarmRemoteUnexpectedNodeFamily_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 12),
    _AlarmRemoteUnexpectedNodeFamily_Type()
)
alarmRemoteUnexpectedNodeFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteUnexpectedNodeFamily.setStatus("current")
_AlarmRemoteSetAccessFailed_Type = FaultStatus
_AlarmRemoteSetAccessFailed_Object = MibScalar
alarmRemoteSetAccessFailed = _AlarmRemoteSetAccessFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 13),
    _AlarmRemoteSetAccessFailed_Type()
)
alarmRemoteSetAccessFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteSetAccessFailed.setStatus("current")
_AlarmRemoteConnectionTimedOut_Type = FaultStatus
_AlarmRemoteConnectionTimedOut_Object = MibScalar
alarmRemoteConnectionTimedOut = _AlarmRemoteConnectionTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 14),
    _AlarmRemoteConnectionTimedOut_Type()
)
alarmRemoteConnectionTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteConnectionTimedOut.setStatus("current")
_AlarmRemoteLogEntriesLost_Type = FaultStatus
_AlarmRemoteLogEntriesLost_Object = MibScalar
alarmRemoteLogEntriesLost = _AlarmRemoteLogEntriesLost_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 15),
    _AlarmRemoteLogEntriesLost_Type()
)
alarmRemoteLogEntriesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteLogEntriesLost.setStatus("current")
_AlarmRemoteBackupReplicationRetryFailed_Type = FaultStatus
_AlarmRemoteBackupReplicationRetryFailed_Object = MibScalar
alarmRemoteBackupReplicationRetryFailed = _AlarmRemoteBackupReplicationRetryFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 16),
    _AlarmRemoteBackupReplicationRetryFailed_Type()
)
alarmRemoteBackupReplicationRetryFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteBackupReplicationRetryFailed.setStatus("current")
_AlarmRemoteBackupReplicationFileNotAvailable_Type = FaultStatus
_AlarmRemoteBackupReplicationFileNotAvailable_Object = MibScalar
alarmRemoteBackupReplicationFileNotAvailable = _AlarmRemoteBackupReplicationFileNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 17),
    _AlarmRemoteBackupReplicationFileNotAvailable_Type()
)
alarmRemoteBackupReplicationFileNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteBackupReplicationFileNotAvailable.setStatus("current")
_AlarmRemoteBackupReplicationRestoreFailed_Type = FaultStatus
_AlarmRemoteBackupReplicationRestoreFailed_Object = MibScalar
alarmRemoteBackupReplicationRestoreFailed = _AlarmRemoteBackupReplicationRestoreFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 7, 18),
    _AlarmRemoteBackupReplicationRestoreFailed_Type()
)
alarmRemoteBackupReplicationRestoreFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRemoteBackupReplicationRestoreFailed.setStatus("current")
_AlarmExternal_ObjectIdentity = ObjectIdentity
alarmExternal = _AlarmExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 8)
)
_AlarmExternal1_Type = FaultStatus
_AlarmExternal1_Object = MibScalar
alarmExternal1 = _AlarmExternal1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 8, 1),
    _AlarmExternal1_Type()
)
alarmExternal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmExternal1.setStatus("current")
_AlarmExternal2_Type = FaultStatus
_AlarmExternal2_Object = MibScalar
alarmExternal2 = _AlarmExternal2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 8, 2),
    _AlarmExternal2_Type()
)
alarmExternal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmExternal2.setStatus("current")
_AlarmExternal3_Type = FaultStatus
_AlarmExternal3_Object = MibScalar
alarmExternal3 = _AlarmExternal3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 8, 3),
    _AlarmExternal3_Type()
)
alarmExternal3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmExternal3.setStatus("current")
_AlarmLog2_ObjectIdentity = ObjectIdentity
alarmLog2 = _AlarmLog2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9)
)
_AlarmLog2Table_Object = MibTable
alarmLog2Table = _AlarmLog2Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    alarmLog2Table.setStatus("current")
_AlarmLog2Entry_Object = MibTableRow
alarmLog2Entry = _AlarmLog2Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1)
)
alarmLog2Entry.setIndexNames(
    (0, "LUM-ALARM-MIB", "alarmLog2SeqNumber"),
)
if mibBuilder.loadTexts:
    alarmLog2Entry.setStatus("current")


class _AlarmLog2Index_Type(Unsigned32):
    """Custom type alarmLog2Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmLog2Index_Type.__name__ = "Unsigned32"
_AlarmLog2Index_Object = MibTableColumn
alarmLog2Index = _AlarmLog2Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 1),
    _AlarmLog2Index_Type()
)
alarmLog2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2Index.setStatus("current")
_AlarmLog2Object_Type = RowPointer
_AlarmLog2Object_Object = MibTableColumn
alarmLog2Object = _AlarmLog2Object_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 2),
    _AlarmLog2Object_Type()
)
alarmLog2Object.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2Object.setStatus("current")
_AlarmLog2FaultStatus_Type = VariablePointer
_AlarmLog2FaultStatus_Object = MibTableColumn
alarmLog2FaultStatus = _AlarmLog2FaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 3),
    _AlarmLog2FaultStatus_Type()
)
alarmLog2FaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2FaultStatus.setStatus("current")
_AlarmLog2MgmtName_Type = MgmtNameString
_AlarmLog2MgmtName_Object = MibTableColumn
alarmLog2MgmtName = _AlarmLog2MgmtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 4),
    _AlarmLog2MgmtName_Type()
)
alarmLog2MgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2MgmtName.setStatus("current")


class _AlarmLog2InvPhysIndexOrZero_Type(Unsigned32):
    """Custom type alarmLog2InvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmLog2InvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmLog2InvPhysIndexOrZero_Object = MibTableColumn
alarmLog2InvPhysIndexOrZero = _AlarmLog2InvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 5),
    _AlarmLog2InvPhysIndexOrZero_Type()
)
alarmLog2InvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2InvPhysIndexOrZero.setStatus("current")


class _AlarmLog2InvLogicalIndexOrZero_Type(Unsigned32):
    """Custom type alarmLog2InvLogicalIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmLog2InvLogicalIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmLog2InvLogicalIndexOrZero_Object = MibTableColumn
alarmLog2InvLogicalIndexOrZero = _AlarmLog2InvLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 6),
    _AlarmLog2InvLogicalIndexOrZero_Type()
)
alarmLog2InvLogicalIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2InvLogicalIndexOrZero.setStatus("current")
_AlarmLog2Type_Type = AlarmNotificationType
_AlarmLog2Type_Object = MibTableColumn
alarmLog2Type = _AlarmLog2Type_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 7),
    _AlarmLog2Type_Type()
)
alarmLog2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2Type.setStatus("current")
_AlarmLog2Cause_Type = AlarmProbableCause
_AlarmLog2Cause_Object = MibTableColumn
alarmLog2Cause = _AlarmLog2Cause_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 8),
    _AlarmLog2Cause_Type()
)
alarmLog2Cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2Cause.setStatus("current")
_AlarmLog2Text_Type = DisplayString
_AlarmLog2Text_Object = MibTableColumn
alarmLog2Text = _AlarmLog2Text_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 9),
    _AlarmLog2Text_Type()
)
alarmLog2Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2Text.setStatus("current")
_AlarmLog2Severity_Type = AlarmPerceivedSeverity
_AlarmLog2Severity_Object = MibTableColumn
alarmLog2Severity = _AlarmLog2Severity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 10),
    _AlarmLog2Severity_Type()
)
alarmLog2Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2Severity.setStatus("current")
_AlarmLog2CreatedTime_Type = DateAndTime
_AlarmLog2CreatedTime_Object = MibTableColumn
alarmLog2CreatedTime = _AlarmLog2CreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 11),
    _AlarmLog2CreatedTime_Type()
)
alarmLog2CreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2CreatedTime.setStatus("current")
_AlarmLog2LastChangeTime_Type = DateAndTime
_AlarmLog2LastChangeTime_Object = MibTableColumn
alarmLog2LastChangeTime = _AlarmLog2LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 12),
    _AlarmLog2LastChangeTime_Type()
)
alarmLog2LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2LastChangeTime.setStatus("current")
_AlarmLog2SeqNumber_Type = Counter32
_AlarmLog2SeqNumber_Object = MibTableColumn
alarmLog2SeqNumber = _AlarmLog2SeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 13),
    _AlarmLog2SeqNumber_Type()
)
alarmLog2SeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2SeqNumber.setStatus("current")
_AlarmLog2NeName_Type = DisplayString
_AlarmLog2NeName_Object = MibTableColumn
alarmLog2NeName = _AlarmLog2NeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 14),
    _AlarmLog2NeName_Type()
)
alarmLog2NeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2NeName.setStatus("current")
_AlarmLog2NeIpAddress_Type = IpAddress
_AlarmLog2NeIpAddress_Object = MibTableColumn
alarmLog2NeIpAddress = _AlarmLog2NeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 9, 1, 1, 15),
    _AlarmLog2NeIpAddress_Type()
)
alarmLog2NeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLog2NeIpAddress.setStatus("current")
_AlarmEvent_ObjectIdentity = ObjectIdentity
alarmEvent = _AlarmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10)
)
_AlarmEventTable_Object = MibTable
alarmEventTable = _AlarmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    alarmEventTable.setStatus("current")
_AlarmEventEntry_Object = MibTableRow
alarmEventEntry = _AlarmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1)
)
alarmEventEntry.setIndexNames(
    (0, "LUM-ALARM-MIB", "alarmEventSeqNumber"),
)
if mibBuilder.loadTexts:
    alarmEventEntry.setStatus("current")


class _AlarmEventIndex_Type(Unsigned32):
    """Custom type alarmEventIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmEventIndex_Type.__name__ = "Unsigned32"
_AlarmEventIndex_Object = MibTableColumn
alarmEventIndex = _AlarmEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 1),
    _AlarmEventIndex_Type()
)
alarmEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventIndex.setStatus("current")
_AlarmEventMgmtName_Type = MgmtNameString
_AlarmEventMgmtName_Object = MibTableColumn
alarmEventMgmtName = _AlarmEventMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 2),
    _AlarmEventMgmtName_Type()
)
alarmEventMgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventMgmtName.setStatus("current")


class _AlarmEventInvLogicalIndexOrZero_Type(Unsigned32):
    """Custom type alarmEventInvLogicalIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmEventInvLogicalIndexOrZero_Type.__name__ = "Unsigned32"
_AlarmEventInvLogicalIndexOrZero_Object = MibTableColumn
alarmEventInvLogicalIndexOrZero = _AlarmEventInvLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 3),
    _AlarmEventInvLogicalIndexOrZero_Type()
)
alarmEventInvLogicalIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventInvLogicalIndexOrZero.setStatus("current")
_AlarmEventCategory_Type = AlarmEventCategory
_AlarmEventCategory_Object = MibTableColumn
alarmEventCategory = _AlarmEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 4),
    _AlarmEventCategory_Type()
)
alarmEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventCategory.setStatus("current")
_AlarmEventText_Type = DisplayString
_AlarmEventText_Object = MibTableColumn
alarmEventText = _AlarmEventText_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 5),
    _AlarmEventText_Type()
)
alarmEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventText.setStatus("current")
_AlarmEventOccurredTime_Type = DateAndTime
_AlarmEventOccurredTime_Object = MibTableColumn
alarmEventOccurredTime = _AlarmEventOccurredTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 6),
    _AlarmEventOccurredTime_Type()
)
alarmEventOccurredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventOccurredTime.setStatus("current")
_AlarmEventSeqNumber_Type = Counter32
_AlarmEventSeqNumber_Object = MibTableColumn
alarmEventSeqNumber = _AlarmEventSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 7),
    _AlarmEventSeqNumber_Type()
)
alarmEventSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventSeqNumber.setStatus("current")
_AlarmEventUserInfo_Type = DisplayString
_AlarmEventUserInfo_Object = MibTableColumn
alarmEventUserInfo = _AlarmEventUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 8),
    _AlarmEventUserInfo_Type()
)
alarmEventUserInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventUserInfo.setStatus("current")
_AlarmEventLongName_Type = MgmtNameString
_AlarmEventLongName_Object = MibTableColumn
alarmEventLongName = _AlarmEventLongName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 10, 1, 1, 9),
    _AlarmEventLongName_Type()
)
alarmEventLongName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventLongName.setStatus("current")

# Managed Objects groups

alarmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 1)
)
alarmGeneralGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralTestAndIncr"),
        ("LUM-ALARM-MIB", "alarmGeneralReplayBufferSize"),
        ("LUM-ALARM-MIB", "alarmGeneralReplayRequestSeq"),
        ("LUM-ALARM-MIB", "alarmGeneralReplayRequestTime"),
        ("LUM-ALARM-MIB", "alarmGeneralMibSpecVersion"),
        ("LUM-ALARM-MIB", "alarmGeneralMibImplVersion"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroup.setStatus("deprecated")

alarmListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 2)
)
alarmListGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmListGroup.setStatus("deprecated")

alarmSumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 4)
)
alarmSumGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmSumActiveIndeterminate"),
        ("LUM-ALARM-MIB", "alarmSumTotalIndeterminate"),
        ("LUM-ALARM-MIB", "alarmSumActiveWarning"),
        ("LUM-ALARM-MIB", "alarmSumTotalWarning"),
        ("LUM-ALARM-MIB", "alarmSumActiveMinor"),
        ("LUM-ALARM-MIB", "alarmSumTotalMinor"),
        ("LUM-ALARM-MIB", "alarmSumActiveMajor"),
        ("LUM-ALARM-MIB", "alarmSumTotalMajor"),
        ("LUM-ALARM-MIB", "alarmSumActiveCritical"),
        ("LUM-ALARM-MIB", "alarmSumTotalCritical"),
        ("LUM-ALARM-MIB", "alarmSumTotalActive"))
)
if mibBuilder.loadTexts:
    alarmSumGroup.setStatus("current")

alarmTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 5)
)
alarmTestGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmTestCommunication"),
        ("LUM-ALARM-MIB", "alarmTestQualityOfService"),
        ("LUM-ALARM-MIB", "alarmTestProcessingError"),
        ("LUM-ALARM-MIB", "alarmTestEquipment"),
        ("LUM-ALARM-MIB", "alarmTestEnvironmental"))
)
if mibBuilder.loadTexts:
    alarmTestGroup.setStatus("deprecated")

alarmGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 6)
)
alarmGeneralGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV2.setStatus("deprecated")

alarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 7)
)
alarmLogGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmLogIndex"),
        ("LUM-ALARM-MIB", "alarmLogObject"),
        ("LUM-ALARM-MIB", "alarmLogFaultStatus"),
        ("LUM-ALARM-MIB", "alarmLogMgmtName"),
        ("LUM-ALARM-MIB", "alarmLogInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLogInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLogType"),
        ("LUM-ALARM-MIB", "alarmLogCause"),
        ("LUM-ALARM-MIB", "alarmLogSeverity"),
        ("LUM-ALARM-MIB", "alarmLogText"),
        ("LUM-ALARM-MIB", "alarmLogCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLogLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmLogSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmLogGroup.setStatus("deprecated")

alarmGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 8)
)
alarmGeneralGroupV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV3.setStatus("deprecated")

alarmGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 9)
)
alarmGeneralGroupV4.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV4.setStatus("deprecated")

alarmTestGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 10)
)
alarmTestGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmTestCommunication"),
        ("LUM-ALARM-MIB", "alarmTestQualityOfService"),
        ("LUM-ALARM-MIB", "alarmTestProcessingError"),
        ("LUM-ALARM-MIB", "alarmTestEquipment"),
        ("LUM-ALARM-MIB", "alarmTestEnvironmental"),
        ("LUM-ALARM-MIB", "alarmTestNonPrintable"),
        ("LUM-ALARM-MIB", "alarmTestConfirm"),
        ("LUM-ALARM-MIB", "alarmTestMsg"),
        ("LUM-ALARM-MIB", "alarmTestSetAlarms"),
        ("LUM-ALARM-MIB", "alarmTestQueryAlarms"))
)
if mibBuilder.loadTexts:
    alarmTestGroupV2.setStatus("deprecated")

alarmGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 11)
)
alarmGeneralGroupV5.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV5.setStatus("current")

alarmRemoteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 12)
)
alarmRemoteGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroup.setStatus("current")

alarmTestGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 13)
)
alarmTestGroupV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmTestCommunication"),
        ("LUM-ALARM-MIB", "alarmTestQualityOfService"),
        ("LUM-ALARM-MIB", "alarmTestProcessingError"),
        ("LUM-ALARM-MIB", "alarmTestEquipment"),
        ("LUM-ALARM-MIB", "alarmTestEnvironmental"),
        ("LUM-ALARM-MIB", "alarmTestNonPrintable"),
        ("LUM-ALARM-MIB", "alarmTestConfirm"),
        ("LUM-ALARM-MIB", "alarmTestMsg"),
        ("LUM-ALARM-MIB", "alarmTestSetAlarms"),
        ("LUM-ALARM-MIB", "alarmTestQueryAlarms"),
        ("LUM-ALARM-MIB", "alarmTestSetCommunication"),
        ("LUM-ALARM-MIB", "alarmTestSetQualityOfService"),
        ("LUM-ALARM-MIB", "alarmTestSetProcessingError"),
        ("LUM-ALARM-MIB", "alarmTestSetEquipment"),
        ("LUM-ALARM-MIB", "alarmTestSetEnvironmental"))
)
if mibBuilder.loadTexts:
    alarmTestGroupV3.setStatus("current")

alarmLogGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 14)
)
alarmLogGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmLogIndex"),
        ("LUM-ALARM-MIB", "alarmLogObject"),
        ("LUM-ALARM-MIB", "alarmLogFaultStatus"),
        ("LUM-ALARM-MIB", "alarmLogMgmtName"),
        ("LUM-ALARM-MIB", "alarmLogInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLogInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLogType"),
        ("LUM-ALARM-MIB", "alarmLogCause"),
        ("LUM-ALARM-MIB", "alarmLogSeverity"),
        ("LUM-ALARM-MIB", "alarmLogText"),
        ("LUM-ALARM-MIB", "alarmLogCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLogLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmLogSeqNumber"),
        ("LUM-ALARM-MIB", "alarmLogPrevSeverity"))
)
if mibBuilder.loadTexts:
    alarmLogGroupV2.setStatus("deprecated")

alarmGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 15)
)
alarmGeneralGroupV6.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLogTableSize"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV6.setStatus("deprecated")

alarmRemoteGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 16)
)
alarmRemoteGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV2.setStatus("deprecated")

alarmGeneralGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 17)
)
alarmGeneralGroupV7.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV7.setStatus("current")

alarmExternalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 19)
)
alarmExternalGroupV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmExternal1"),
        ("LUM-ALARM-MIB", "alarmExternal2"),
        ("LUM-ALARM-MIB", "alarmExternal3"))
)
if mibBuilder.loadTexts:
    alarmExternalGroupV1.setStatus("current")

alarmGeneralGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 22)
)
alarmGeneralGroupV8.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2TableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmNotificationVersion"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2Size"),
        ("LUM-ALARM-MIB", "alarmGeneralHighestSeverity"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV8.setStatus("deprecated")

alarmListGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 23)
)
alarmListGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmListGroupV2.setStatus("current")

alarmLogGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 24)
)
alarmLogGroupV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmLogIndex"),
        ("LUM-ALARM-MIB", "alarmLogObject"),
        ("LUM-ALARM-MIB", "alarmLogFaultStatus"),
        ("LUM-ALARM-MIB", "alarmLogMgmtName"),
        ("LUM-ALARM-MIB", "alarmLogInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLogInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLogType"),
        ("LUM-ALARM-MIB", "alarmLogCause"),
        ("LUM-ALARM-MIB", "alarmLogSeverity"),
        ("LUM-ALARM-MIB", "alarmLogText"),
        ("LUM-ALARM-MIB", "alarmLogCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLogLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmLogSeqNumber"),
        ("LUM-ALARM-MIB", "alarmLogPrevSeverity"),
        ("LUM-ALARM-MIB", "alarmLogNeName"),
        ("LUM-ALARM-MIB", "alarmLogNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmLogGroupV3.setStatus("current")

alarmLog2LogGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 25)
)
alarmLog2LogGroupV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmLog2Index"),
        ("LUM-ALARM-MIB", "alarmLog2Object"),
        ("LUM-ALARM-MIB", "alarmLog2FaultStatus"),
        ("LUM-ALARM-MIB", "alarmLog2MgmtName"),
        ("LUM-ALARM-MIB", "alarmLog2InvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLog2InvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmLog2Type"),
        ("LUM-ALARM-MIB", "alarmLog2Cause"),
        ("LUM-ALARM-MIB", "alarmLog2Severity"),
        ("LUM-ALARM-MIB", "alarmLog2Text"),
        ("LUM-ALARM-MIB", "alarmLog2CreatedTime"),
        ("LUM-ALARM-MIB", "alarmLog2LastChangeTime"),
        ("LUM-ALARM-MIB", "alarmLog2SeqNumber"),
        ("LUM-ALARM-MIB", "alarmLog2NeName"),
        ("LUM-ALARM-MIB", "alarmLog2NeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmLog2LogGroupV1.setStatus("current")

alarmRemoteGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 26)
)
alarmRemoteGroupV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV3.setStatus("deprecated")

alarmGeneralGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 27)
)
alarmGeneralGroupV9.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2TableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmNotificationVersion"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2Size"),
        ("LUM-ALARM-MIB", "alarmGeneralHighestSeverity"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLastSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV9.setStatus("deprecated")

alarmEventGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 28)
)
alarmEventGroupV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmEventIndex"),
        ("LUM-ALARM-MIB", "alarmEventMgmtName"),
        ("LUM-ALARM-MIB", "alarmEventInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmEventCategory"),
        ("LUM-ALARM-MIB", "alarmEventText"),
        ("LUM-ALARM-MIB", "alarmEventOccurredTime"),
        ("LUM-ALARM-MIB", "alarmEventSeqNumber"),
        ("LUM-ALARM-MIB", "alarmEventUserInfo"))
)
if mibBuilder.loadTexts:
    alarmEventGroupV1.setStatus("current")

alarmEventGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 29)
)
alarmEventGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmEventIndex"),
        ("LUM-ALARM-MIB", "alarmEventMgmtName"),
        ("LUM-ALARM-MIB", "alarmEventInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmEventCategory"),
        ("LUM-ALARM-MIB", "alarmEventText"),
        ("LUM-ALARM-MIB", "alarmEventOccurredTime"),
        ("LUM-ALARM-MIB", "alarmEventSeqNumber"),
        ("LUM-ALARM-MIB", "alarmEventUserInfo"),
        ("LUM-ALARM-MIB", "alarmEventLongName"))
)
if mibBuilder.loadTexts:
    alarmEventGroupV2.setStatus("current")

alarmRemoteGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 30)
)
alarmRemoteGroupV4.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV4.setStatus("current")

alarmRemoteGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 31)
)
alarmRemoteGroupV5.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV5.setStatus("current")

alarmRemoteGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 32)
)
alarmRemoteGroupV6.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteSoftwareNotSupported"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV6.setStatus("current")

alarmRemoteGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 33)
)
alarmRemoteGroupV7.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteSoftwareNotSupported"),
        ("LUM-ALARM-MIB", "alarmRemoteUnexpectedNodeFamily"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV7.setStatus("current")

alarmRemoteGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 34)
)
alarmRemoteGroupV8.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteSoftwareNotSupported"),
        ("LUM-ALARM-MIB", "alarmRemoteUnexpectedNodeFamily"),
        ("LUM-ALARM-MIB", "alarmRemoteSetAccessFailed"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV8.setStatus("current")

alarmRemoteGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 35)
)
alarmRemoteGroupV9.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteSoftwareNotSupported"),
        ("LUM-ALARM-MIB", "alarmRemoteUnexpectedNodeFamily"),
        ("LUM-ALARM-MIB", "alarmRemoteSetAccessFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionTimedOut"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV9.setStatus("deprecated")

alarmGeneralGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 36)
)
alarmGeneralGroupV10.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSuppressionMode"),
        ("LUM-ALARM-MIB", "alarmGeneralFilterMode"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2TableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmNotificationVersion"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2Size"),
        ("LUM-ALARM-MIB", "alarmGeneralHighestSeverity"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralSoakInInterval"))
)
if mibBuilder.loadTexts:
    alarmGeneralGroupV10.setStatus("current")

alarmRemoteGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 37)
)
alarmRemoteGroupV10.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteSoftwareNotSupported"),
        ("LUM-ALARM-MIB", "alarmRemoteUnexpectedNodeFamily"),
        ("LUM-ALARM-MIB", "alarmRemoteSetAccessFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionTimedOut"),
        ("LUM-ALARM-MIB", "alarmRemoteLogEntriesLost"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV10.setStatus("deprecated")

alarmRemoteGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 38)
)
alarmRemoteGroupV11.setObjects(
      *(("LUM-ALARM-MIB", "alarmRemoteNotReachable"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLoginFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteMibRefreshFailed"),
        ("LUM-ALARM-MIB", "alarmTimeWindowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteLocalTimeDiffFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupUnsavedFailed"),
        ("LUM-ALARM-MIB", "alarmRemotePmFtpFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteAlarmsIgnored"),
        ("LUM-ALARM-MIB", "alarmRemoteNotificationOverflowFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteSoftwareNotSupported"),
        ("LUM-ALARM-MIB", "alarmRemoteUnexpectedNodeFamily"),
        ("LUM-ALARM-MIB", "alarmRemoteSetAccessFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteConnectionTimedOut"),
        ("LUM-ALARM-MIB", "alarmRemoteLogEntriesLost"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupReplicationRetryFailed"),
        ("LUM-ALARM-MIB", "alarmRemoteBackupReplicationFileNotAvailable"))
)
if mibBuilder.loadTexts:
    alarmRemoteGroupV11.setStatus("current")

alarmGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 3, 1)
)
alarmGeneralMinimalGroupV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"))
)
if mibBuilder.loadTexts:
    alarmGeneralMinimalGroupV1.setStatus("current")

alarmListMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 3, 2)
)
alarmListMinimalGroupV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"))
)
if mibBuilder.loadTexts:
    alarmListMinimalGroupV1.setStatus("deprecated")

alarmGeneralMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 3, 3)
)
alarmGeneralMinimalGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmNotificationVersion"),
        ("LUM-ALARM-MIB", "alarmGeneralHighestSeverity"))
)
if mibBuilder.loadTexts:
    alarmGeneralMinimalGroupV2.setStatus("deprecated")

alarmListMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 3, 4)
)
alarmListMinimalGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmListMinimalGroupV2.setStatus("current")

alarmGeneralMinimalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 3, 5)
)
alarmGeneralMinimalGroupV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralLastSeqNumber"),
        ("LUM-ALARM-MIB", "alarmGeneralConfigLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralHeartBeatInterval"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmNotificationVersion"),
        ("LUM-ALARM-MIB", "alarmGeneralHighestSeverity"),
        ("LUM-ALARM-MIB", "alarmGeneralAlarmLog2Size"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLogTableSize"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLogSize"),
        ("LUM-ALARM-MIB", "alarmGeneralEventLastSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmGeneralMinimalGroupV3.setStatus("current")


# Notification objects

alarmNotificationColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 1)
)
alarmNotificationColdStart.setObjects(
    ("LUM-ALARM-MIB", "alarmGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    alarmNotificationColdStart.setStatus(
        "current"
    )

alarmNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 2)
)
alarmNotificationCleared.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmNotificationCleared.setStatus(
        "current"
    )

alarmNotificationIndeterminate = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 3)
)
alarmNotificationIndeterminate.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmNotificationIndeterminate.setStatus(
        "current"
    )

alarmNotificationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 4)
)
alarmNotificationWarning.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmNotificationWarning.setStatus(
        "current"
    )

alarmNotificationMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 5)
)
alarmNotificationMinor.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmNotificationMinor.setStatus(
        "current"
    )

alarmNotificationMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 6)
)
alarmNotificationMajor.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmNotificationMajor.setStatus(
        "current"
    )

alarmNotificationCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 7)
)
alarmNotificationCritical.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"))
)
if mibBuilder.loadTexts:
    alarmNotificationCritical.setStatus(
        "current"
    )

alarmNotificationHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 8)
)
if mibBuilder.loadTexts:
    alarmNotificationHeartBeat.setStatus(
        "current"
    )

alarmNotificationClearedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 9)
)
alarmNotificationClearedV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationClearedV2.setStatus(
        "current"
    )

alarmNotificationIndeterminateV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 10)
)
alarmNotificationIndeterminateV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationIndeterminateV2.setStatus(
        "current"
    )

alarmNotificationWarningV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 11)
)
alarmNotificationWarningV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationWarningV2.setStatus(
        "current"
    )

alarmNotificationMinorV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 12)
)
alarmNotificationMinorV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationMinorV2.setStatus(
        "current"
    )

alarmNotificationMajorV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 13)
)
alarmNotificationMajorV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationMajorV2.setStatus(
        "current"
    )

alarmNotificationCriticalV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 14)
)
alarmNotificationCriticalV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmIndex"),
        ("LUM-ALARM-MIB", "alarmObject"),
        ("LUM-ALARM-MIB", "alarmFaultStatus"),
        ("LUM-ALARM-MIB", "alarmMgmtName"),
        ("LUM-ALARM-MIB", "alarmInvPhysIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmInvLogicalIndexOrZero"),
        ("LUM-ALARM-MIB", "alarmType"),
        ("LUM-ALARM-MIB", "alarmCause"),
        ("LUM-ALARM-MIB", "alarmText"),
        ("LUM-ALARM-MIB", "alarmSeverity"),
        ("LUM-ALARM-MIB", "alarmCreatedTime"),
        ("LUM-ALARM-MIB", "alarmLastChangeTime"),
        ("LUM-ALARM-MIB", "alarmSeqNumber"),
        ("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationCriticalV2.setStatus(
        "current"
    )

alarmNotificationHeartBeatV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 2, 3, 0, 15)
)
alarmNotificationHeartBeatV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmNeName"),
        ("LUM-ALARM-MIB", "alarmNeIpAddress"))
)
if mibBuilder.loadTexts:
    alarmNotificationHeartBeatV2.setStatus(
        "current"
    )


# Notifications groups

alarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 3)
)
alarmNotificationGroup.setObjects(
      *(("LUM-ALARM-MIB", "alarmNotificationColdStart"),
        ("LUM-ALARM-MIB", "alarmNotificationCleared"),
        ("LUM-ALARM-MIB", "alarmNotificationIndeterminate"),
        ("LUM-ALARM-MIB", "alarmNotificationWarning"),
        ("LUM-ALARM-MIB", "alarmNotificationMinor"),
        ("LUM-ALARM-MIB", "alarmNotificationMajor"),
        ("LUM-ALARM-MIB", "alarmNotificationCritical"))
)
if mibBuilder.loadTexts:
    alarmNotificationGroup.setStatus(
        "deprecated"
    )

alarmNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 18)
)
alarmNotificationGroupV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmNotificationColdStart"),
        ("LUM-ALARM-MIB", "alarmNotificationCleared"),
        ("LUM-ALARM-MIB", "alarmNotificationIndeterminate"),
        ("LUM-ALARM-MIB", "alarmNotificationWarning"),
        ("LUM-ALARM-MIB", "alarmNotificationMinor"),
        ("LUM-ALARM-MIB", "alarmNotificationMajor"),
        ("LUM-ALARM-MIB", "alarmNotificationCritical"),
        ("LUM-ALARM-MIB", "alarmNotificationHeartBeat"))
)
if mibBuilder.loadTexts:
    alarmNotificationGroupV2.setStatus(
        "deprecated"
    )

alarmNotificationGroupV3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 1, 21)
)
alarmNotificationGroupV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmNotificationColdStart"),
        ("LUM-ALARM-MIB", "alarmNotificationCleared"),
        ("LUM-ALARM-MIB", "alarmNotificationIndeterminate"),
        ("LUM-ALARM-MIB", "alarmNotificationWarning"),
        ("LUM-ALARM-MIB", "alarmNotificationMinor"),
        ("LUM-ALARM-MIB", "alarmNotificationMajor"),
        ("LUM-ALARM-MIB", "alarmNotificationCritical"),
        ("LUM-ALARM-MIB", "alarmNotificationHeartBeat"),
        ("LUM-ALARM-MIB", "alarmNotificationClearedV2"),
        ("LUM-ALARM-MIB", "alarmNotificationIndeterminateV2"),
        ("LUM-ALARM-MIB", "alarmNotificationWarningV2"),
        ("LUM-ALARM-MIB", "alarmNotificationMinorV2"),
        ("LUM-ALARM-MIB", "alarmNotificationMajorV2"),
        ("LUM-ALARM-MIB", "alarmNotificationCriticalV2"),
        ("LUM-ALARM-MIB", "alarmNotificationHeartBeatV2"))
)
if mibBuilder.loadTexts:
    alarmNotificationGroupV3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumAlarmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 1)
)
lumAlarmBasicComplV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroup"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV1.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 2)
)
lumAlarmBasicComplV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV2"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV2.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 3)
)
lumAlarmBasicComplV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV2"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroup"),
        ("LUM-ALARM-MIB", "alarmLogGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV3.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 4)
)
lumAlarmBasicComplV4.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV3"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroup"),
        ("LUM-ALARM-MIB", "alarmLogGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV4.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 5)
)
lumAlarmBasicComplV5.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV4"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroup"),
        ("LUM-ALARM-MIB", "alarmLogGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV5.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 6)
)
lumAlarmBasicComplV6.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV4"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroup"),
        ("LUM-ALARM-MIB", "alarmLogGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV6.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 7)
)
lumAlarmBasicComplV7.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV4"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV2"),
        ("LUM-ALARM-MIB", "alarmLogGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV7.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 8)
)
lumAlarmBasicComplV8.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV5"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV2"),
        ("LUM-ALARM-MIB", "alarmLogGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV8.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 9)
)
lumAlarmBasicComplV9.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV5"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV2"),
        ("LUM-ALARM-MIB", "alarmLogGroup"),
        ("LUM-ALARM-MIB", "alarmRemoteGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV9.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 10)
)
lumAlarmBasicComplV10.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV5"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroup"),
        ("LUM-ALARM-MIB", "alarmRemoteGroup"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV10.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 11)
)
lumAlarmBasicComplV11.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV6"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroup"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV2"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV11.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 12)
)
lumAlarmBasicComplV12.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV7"),
        ("LUM-ALARM-MIB", "alarmListGroup"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV2"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV2"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV12.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 13)
)
lumAlarmBasicComplV13.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV8"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV3"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV13.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 14)
)
lumAlarmBasicComplV14.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV3"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV1"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV14.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 15)
)
lumAlarmBasicComplV15.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV3"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV15.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 16)
)
lumAlarmBasicComplV16.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV4"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV16.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 17)
)
lumAlarmBasicComplV17.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV5"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV17.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 18)
)
lumAlarmBasicComplV18.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV6"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV18.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 19)
)
lumAlarmBasicComplV19.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV7"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV19.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 20)
)
lumAlarmBasicComplV20.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV8"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV20.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 21)
)
lumAlarmBasicComplV21.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV9"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV9"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV21.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 22)
)
lumAlarmBasicComplV22.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV10"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV10"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV22.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 23)
)
lumAlarmBasicComplV23.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV10"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV11"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV23.setStatus(
        "deprecated"
    )

lumAlarmBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 2, 24)
)
lumAlarmBasicComplV24.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralGroupV10"),
        ("LUM-ALARM-MIB", "alarmListGroupV2"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmSumGroup"),
        ("LUM-ALARM-MIB", "alarmTestGroupV3"),
        ("LUM-ALARM-MIB", "alarmLogGroupV3"),
        ("LUM-ALARM-MIB", "alarmRemoteGroupV11"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"),
        ("LUM-ALARM-MIB", "alarmEventGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmBasicComplV24.setStatus(
        "current"
    )

lumAlarmMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 4, 1)
)
lumAlarmMinimalComplV1.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralMinimalGroupV1"),
        ("LUM-ALARM-MIB", "alarmListMinimalGroupV1"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumAlarmMinimalComplV1.setStatus(
        "deprecated"
    )

lumAlarmMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 4, 2)
)
lumAlarmMinimalComplV2.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralMinimalGroupV2"),
        ("LUM-ALARM-MIB", "alarmListMinimalGroupV2"),
        ("LUM-ALARM-MIB", "alarmExternalGroupV1"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"))
)
if mibBuilder.loadTexts:
    lumAlarmMinimalComplV2.setStatus(
        "deprecated"
    )

lumAlarmMinimalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 4, 3)
)
lumAlarmMinimalComplV3.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralMinimalGroupV3"),
        ("LUM-ALARM-MIB", "alarmListMinimalGroupV2"),
        ("LUM-ALARM-MIB", "alarmExternalGroupV1"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmEventGroupV1"))
)
if mibBuilder.loadTexts:
    lumAlarmMinimalComplV3.setStatus(
        "deprecated"
    )

lumAlarmMinimalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 4, 4)
)
lumAlarmMinimalComplV4.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralMinimalGroupV3"),
        ("LUM-ALARM-MIB", "alarmListMinimalGroupV2"),
        ("LUM-ALARM-MIB", "alarmExternalGroupV1"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmEventGroupV1"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"))
)
if mibBuilder.loadTexts:
    lumAlarmMinimalComplV4.setStatus(
        "deprecated"
    )

lumAlarmMinimalComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1, 1, 4, 5)
)
lumAlarmMinimalComplV5.setObjects(
      *(("LUM-ALARM-MIB", "alarmGeneralMinimalGroupV3"),
        ("LUM-ALARM-MIB", "alarmListMinimalGroupV2"),
        ("LUM-ALARM-MIB", "alarmExternalGroupV1"),
        ("LUM-ALARM-MIB", "alarmNotificationGroupV3"),
        ("LUM-ALARM-MIB", "alarmEventGroupV1"),
        ("LUM-ALARM-MIB", "alarmLog2LogGroupV1"))
)
if mibBuilder.loadTexts:
    lumAlarmMinimalComplV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-ALARM-MIB",
    **{"AlarmNotificationType": AlarmNotificationType,
       "AlarmPerceivedSeverity": AlarmPerceivedSeverity,
       "AlarmProbableCause": AlarmProbableCause,
       "AlarmEventCategory": AlarmEventCategory,
       "lumAlarmMIBModule": lumAlarmMIBModule,
       "lumAlarmConfs": lumAlarmConfs,
       "lumAlarmGroups": lumAlarmGroups,
       "alarmGeneralGroup": alarmGeneralGroup,
       "alarmListGroup": alarmListGroup,
       "alarmNotificationGroup": alarmNotificationGroup,
       "alarmSumGroup": alarmSumGroup,
       "alarmTestGroup": alarmTestGroup,
       "alarmGeneralGroupV2": alarmGeneralGroupV2,
       "alarmLogGroup": alarmLogGroup,
       "alarmGeneralGroupV3": alarmGeneralGroupV3,
       "alarmGeneralGroupV4": alarmGeneralGroupV4,
       "alarmTestGroupV2": alarmTestGroupV2,
       "alarmGeneralGroupV5": alarmGeneralGroupV5,
       "alarmRemoteGroup": alarmRemoteGroup,
       "alarmTestGroupV3": alarmTestGroupV3,
       "alarmLogGroupV2": alarmLogGroupV2,
       "alarmGeneralGroupV6": alarmGeneralGroupV6,
       "alarmRemoteGroupV2": alarmRemoteGroupV2,
       "alarmGeneralGroupV7": alarmGeneralGroupV7,
       "alarmNotificationGroupV2": alarmNotificationGroupV2,
       "alarmExternalGroupV1": alarmExternalGroupV1,
       "alarmNotificationGroupV3": alarmNotificationGroupV3,
       "alarmGeneralGroupV8": alarmGeneralGroupV8,
       "alarmListGroupV2": alarmListGroupV2,
       "alarmLogGroupV3": alarmLogGroupV3,
       "alarmLog2LogGroupV1": alarmLog2LogGroupV1,
       "alarmRemoteGroupV3": alarmRemoteGroupV3,
       "alarmGeneralGroupV9": alarmGeneralGroupV9,
       "alarmEventGroupV1": alarmEventGroupV1,
       "alarmEventGroupV2": alarmEventGroupV2,
       "alarmRemoteGroupV4": alarmRemoteGroupV4,
       "alarmRemoteGroupV5": alarmRemoteGroupV5,
       "alarmRemoteGroupV6": alarmRemoteGroupV6,
       "alarmRemoteGroupV7": alarmRemoteGroupV7,
       "alarmRemoteGroupV8": alarmRemoteGroupV8,
       "alarmRemoteGroupV9": alarmRemoteGroupV9,
       "alarmGeneralGroupV10": alarmGeneralGroupV10,
       "alarmRemoteGroupV10": alarmRemoteGroupV10,
       "alarmRemoteGroupV11": alarmRemoteGroupV11,
       "lumAlarmCompl": lumAlarmCompl,
       "lumAlarmBasicComplV1": lumAlarmBasicComplV1,
       "lumAlarmBasicComplV2": lumAlarmBasicComplV2,
       "lumAlarmBasicComplV3": lumAlarmBasicComplV3,
       "lumAlarmBasicComplV4": lumAlarmBasicComplV4,
       "lumAlarmBasicComplV5": lumAlarmBasicComplV5,
       "lumAlarmBasicComplV6": lumAlarmBasicComplV6,
       "lumAlarmBasicComplV7": lumAlarmBasicComplV7,
       "lumAlarmBasicComplV8": lumAlarmBasicComplV8,
       "lumAlarmBasicComplV9": lumAlarmBasicComplV9,
       "lumAlarmBasicComplV10": lumAlarmBasicComplV10,
       "lumAlarmBasicComplV11": lumAlarmBasicComplV11,
       "lumAlarmBasicComplV12": lumAlarmBasicComplV12,
       "lumAlarmBasicComplV13": lumAlarmBasicComplV13,
       "lumAlarmBasicComplV14": lumAlarmBasicComplV14,
       "lumAlarmBasicComplV15": lumAlarmBasicComplV15,
       "lumAlarmBasicComplV16": lumAlarmBasicComplV16,
       "lumAlarmBasicComplV17": lumAlarmBasicComplV17,
       "lumAlarmBasicComplV18": lumAlarmBasicComplV18,
       "lumAlarmBasicComplV19": lumAlarmBasicComplV19,
       "lumAlarmBasicComplV20": lumAlarmBasicComplV20,
       "lumAlarmBasicComplV21": lumAlarmBasicComplV21,
       "lumAlarmBasicComplV22": lumAlarmBasicComplV22,
       "lumAlarmBasicComplV23": lumAlarmBasicComplV23,
       "lumAlarmBasicComplV24": lumAlarmBasicComplV24,
       "lumAlarmMinimalGroups": lumAlarmMinimalGroups,
       "alarmGeneralMinimalGroupV1": alarmGeneralMinimalGroupV1,
       "alarmListMinimalGroupV1": alarmListMinimalGroupV1,
       "alarmGeneralMinimalGroupV2": alarmGeneralMinimalGroupV2,
       "alarmListMinimalGroupV2": alarmListMinimalGroupV2,
       "alarmGeneralMinimalGroupV3": alarmGeneralMinimalGroupV3,
       "lumAlarmMinimalCompl": lumAlarmMinimalCompl,
       "lumAlarmMinimalComplV1": lumAlarmMinimalComplV1,
       "lumAlarmMinimalComplV2": lumAlarmMinimalComplV2,
       "lumAlarmMinimalComplV3": lumAlarmMinimalComplV3,
       "lumAlarmMinimalComplV4": lumAlarmMinimalComplV4,
       "lumAlarmMinimalComplV5": lumAlarmMinimalComplV5,
       "lumAlarmMIBObjects": lumAlarmMIBObjects,
       "alarmGeneral": alarmGeneral,
       "alarmGeneralLastChangeTime": alarmGeneralLastChangeTime,
       "alarmGeneralLogSize": alarmGeneralLogSize,
       "alarmGeneralLastSeqNumber": alarmGeneralLastSeqNumber,
       "alarmGeneralReplayBufferSize": alarmGeneralReplayBufferSize,
       "alarmGeneralReplayRequestSeq": alarmGeneralReplayRequestSeq,
       "alarmGeneralReplayRequestTime": alarmGeneralReplayRequestTime,
       "alarmGeneralTestAndIncr": alarmGeneralTestAndIncr,
       "alarmGeneralMibSpecVersion": alarmGeneralMibSpecVersion,
       "alarmGeneralMibImplVersion": alarmGeneralMibImplVersion,
       "alarmGeneralSuppressionMode": alarmGeneralSuppressionMode,
       "alarmGeneralFilterMode": alarmGeneralFilterMode,
       "alarmGeneralConfigLastChangeTime": alarmGeneralConfigLastChangeTime,
       "alarmGeneralAlarmTableSize": alarmGeneralAlarmTableSize,
       "alarmGeneralAlarmLogTableSize": alarmGeneralAlarmLogTableSize,
       "alarmGeneralHeartBeatInterval": alarmGeneralHeartBeatInterval,
       "alarmGeneralAlarmLog2TableSize": alarmGeneralAlarmLog2TableSize,
       "alarmGeneralAlarmNotificationVersion": alarmGeneralAlarmNotificationVersion,
       "alarmGeneralAlarmLog2Size": alarmGeneralAlarmLog2Size,
       "alarmGeneralHighestSeverity": alarmGeneralHighestSeverity,
       "alarmGeneralEventLogTableSize": alarmGeneralEventLogTableSize,
       "alarmGeneralEventLogSize": alarmGeneralEventLogSize,
       "alarmGeneralEventLastSeqNumber": alarmGeneralEventLastSeqNumber,
       "alarmGeneralSoakInInterval": alarmGeneralSoakInInterval,
       "alarmList": alarmList,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmObject": alarmObject,
       "alarmFaultStatus": alarmFaultStatus,
       "alarmMgmtName": alarmMgmtName,
       "alarmInvPhysIndexOrZero": alarmInvPhysIndexOrZero,
       "alarmInvLogicalIndexOrZero": alarmInvLogicalIndexOrZero,
       "alarmType": alarmType,
       "alarmCause": alarmCause,
       "alarmText": alarmText,
       "alarmSeverity": alarmSeverity,
       "alarmCreatedTime": alarmCreatedTime,
       "alarmLastChangeTime": alarmLastChangeTime,
       "alarmSeqNumber": alarmSeqNumber,
       "alarmNeName": alarmNeName,
       "alarmNeIpAddress": alarmNeIpAddress,
       "lumentisAlarmNotifications": lumentisAlarmNotifications,
       "alarmNotifyPrefix": alarmNotifyPrefix,
       "alarmNotificationColdStart": alarmNotificationColdStart,
       "alarmNotificationCleared": alarmNotificationCleared,
       "alarmNotificationIndeterminate": alarmNotificationIndeterminate,
       "alarmNotificationWarning": alarmNotificationWarning,
       "alarmNotificationMinor": alarmNotificationMinor,
       "alarmNotificationMajor": alarmNotificationMajor,
       "alarmNotificationCritical": alarmNotificationCritical,
       "alarmNotificationHeartBeat": alarmNotificationHeartBeat,
       "alarmNotificationClearedV2": alarmNotificationClearedV2,
       "alarmNotificationIndeterminateV2": alarmNotificationIndeterminateV2,
       "alarmNotificationWarningV2": alarmNotificationWarningV2,
       "alarmNotificationMinorV2": alarmNotificationMinorV2,
       "alarmNotificationMajorV2": alarmNotificationMajorV2,
       "alarmNotificationCriticalV2": alarmNotificationCriticalV2,
       "alarmNotificationHeartBeatV2": alarmNotificationHeartBeatV2,
       "alarmSum": alarmSum,
       "alarmSumActiveIndeterminate": alarmSumActiveIndeterminate,
       "alarmSumTotalIndeterminate": alarmSumTotalIndeterminate,
       "alarmSumActiveWarning": alarmSumActiveWarning,
       "alarmSumTotalWarning": alarmSumTotalWarning,
       "alarmSumActiveMinor": alarmSumActiveMinor,
       "alarmSumTotalMinor": alarmSumTotalMinor,
       "alarmSumActiveMajor": alarmSumActiveMajor,
       "alarmSumTotalMajor": alarmSumTotalMajor,
       "alarmSumActiveCritical": alarmSumActiveCritical,
       "alarmSumTotalCritical": alarmSumTotalCritical,
       "alarmSumTotalActive": alarmSumTotalActive,
       "alarmTest": alarmTest,
       "alarmTestCommunication": alarmTestCommunication,
       "alarmTestQualityOfService": alarmTestQualityOfService,
       "alarmTestProcessingError": alarmTestProcessingError,
       "alarmTestEquipment": alarmTestEquipment,
       "alarmTestEnvironmental": alarmTestEnvironmental,
       "alarmTestNonPrintable": alarmTestNonPrintable,
       "alarmTestConfirm": alarmTestConfirm,
       "alarmTestMsg": alarmTestMsg,
       "alarmTestSetAlarms": alarmTestSetAlarms,
       "alarmTestQueryAlarms": alarmTestQueryAlarms,
       "alarmTestSetCommunication": alarmTestSetCommunication,
       "alarmTestSetQualityOfService": alarmTestSetQualityOfService,
       "alarmTestSetProcessingError": alarmTestSetProcessingError,
       "alarmTestSetEquipment": alarmTestSetEquipment,
       "alarmTestSetEnvironmental": alarmTestSetEnvironmental,
       "alarmLog": alarmLog,
       "alarmLogTable": alarmLogTable,
       "alarmLogEntry": alarmLogEntry,
       "alarmLogIndex": alarmLogIndex,
       "alarmLogObject": alarmLogObject,
       "alarmLogFaultStatus": alarmLogFaultStatus,
       "alarmLogMgmtName": alarmLogMgmtName,
       "alarmLogInvPhysIndexOrZero": alarmLogInvPhysIndexOrZero,
       "alarmLogInvLogicalIndexOrZero": alarmLogInvLogicalIndexOrZero,
       "alarmLogType": alarmLogType,
       "alarmLogCause": alarmLogCause,
       "alarmLogText": alarmLogText,
       "alarmLogSeverity": alarmLogSeverity,
       "alarmLogCreatedTime": alarmLogCreatedTime,
       "alarmLogLastChangeTime": alarmLogLastChangeTime,
       "alarmLogSeqNumber": alarmLogSeqNumber,
       "alarmLogPrevSeverity": alarmLogPrevSeverity,
       "alarmLogNeName": alarmLogNeName,
       "alarmLogNeIpAddress": alarmLogNeIpAddress,
       "alarmRemote": alarmRemote,
       "alarmRemoteNotReachable": alarmRemoteNotReachable,
       "alarmRemoteConnectionFailed": alarmRemoteConnectionFailed,
       "alarmTimeWindowFailed": alarmTimeWindowFailed,
       "alarmRemoteLoginFailed": alarmRemoteLoginFailed,
       "alarmRemoteMibRefreshFailed": alarmRemoteMibRefreshFailed,
       "alarmRemoteLocalTimeDiffFailed": alarmRemoteLocalTimeDiffFailed,
       "alarmRemoteBackupUnsavedFailed": alarmRemoteBackupUnsavedFailed,
       "alarmRemotePmFtpFailed": alarmRemotePmFtpFailed,
       "alarmRemoteNotificationOverflowFailed": alarmRemoteNotificationOverflowFailed,
       "alarmRemoteAlarmsIgnored": alarmRemoteAlarmsIgnored,
       "alarmRemoteSoftwareNotSupported": alarmRemoteSoftwareNotSupported,
       "alarmRemoteUnexpectedNodeFamily": alarmRemoteUnexpectedNodeFamily,
       "alarmRemoteSetAccessFailed": alarmRemoteSetAccessFailed,
       "alarmRemoteConnectionTimedOut": alarmRemoteConnectionTimedOut,
       "alarmRemoteLogEntriesLost": alarmRemoteLogEntriesLost,
       "alarmRemoteBackupReplicationRetryFailed": alarmRemoteBackupReplicationRetryFailed,
       "alarmRemoteBackupReplicationFileNotAvailable": alarmRemoteBackupReplicationFileNotAvailable,
       "alarmRemoteBackupReplicationRestoreFailed": alarmRemoteBackupReplicationRestoreFailed,
       "alarmExternal": alarmExternal,
       "alarmExternal1": alarmExternal1,
       "alarmExternal2": alarmExternal2,
       "alarmExternal3": alarmExternal3,
       "alarmLog2": alarmLog2,
       "alarmLog2Table": alarmLog2Table,
       "alarmLog2Entry": alarmLog2Entry,
       "alarmLog2Index": alarmLog2Index,
       "alarmLog2Object": alarmLog2Object,
       "alarmLog2FaultStatus": alarmLog2FaultStatus,
       "alarmLog2MgmtName": alarmLog2MgmtName,
       "alarmLog2InvPhysIndexOrZero": alarmLog2InvPhysIndexOrZero,
       "alarmLog2InvLogicalIndexOrZero": alarmLog2InvLogicalIndexOrZero,
       "alarmLog2Type": alarmLog2Type,
       "alarmLog2Cause": alarmLog2Cause,
       "alarmLog2Text": alarmLog2Text,
       "alarmLog2Severity": alarmLog2Severity,
       "alarmLog2CreatedTime": alarmLog2CreatedTime,
       "alarmLog2LastChangeTime": alarmLog2LastChangeTime,
       "alarmLog2SeqNumber": alarmLog2SeqNumber,
       "alarmLog2NeName": alarmLog2NeName,
       "alarmLog2NeIpAddress": alarmLog2NeIpAddress,
       "alarmEvent": alarmEvent,
       "alarmEventTable": alarmEventTable,
       "alarmEventEntry": alarmEventEntry,
       "alarmEventIndex": alarmEventIndex,
       "alarmEventMgmtName": alarmEventMgmtName,
       "alarmEventInvLogicalIndexOrZero": alarmEventInvLogicalIndexOrZero,
       "alarmEventCategory": alarmEventCategory,
       "alarmEventText": alarmEventText,
       "alarmEventOccurredTime": alarmEventOccurredTime,
       "alarmEventSeqNumber": alarmEventSeqNumber,
       "alarmEventUserInfo": alarmEventUserInfo,
       "alarmEventLongName": alarmEventLongName}
)
