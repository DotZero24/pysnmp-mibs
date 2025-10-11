# SNMP MIB module (ALU-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:41 2025
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

(aluHwObjs,) = mibBuilder.importSymbols(
    "ALU-CHASSIS-MIB",
    "aluHwObjs")

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

(TPortSchedulerPIR,
 TmnxAdminState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TPortSchedulerPIR",
    "TmnxAdminState")


# MODULE-IDENTITY

aluSystemMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    aluSystemMIBModule.setRevisions(
        ("1911-06-14 00:00",
         "1914-02-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluTod1PpsMessageType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cm", 1),
          ("ct", 2),
          ("irig-b000-b120", 3),
          ("irig-b001-b121", 4),
          ("irig-b002-b122", 5),
          ("irig-b003-b123", 6),
          ("irig-b004-b124", 7),
          ("irig-b005-b125", 8),
          ("irig-b006-b126", 9),
          ("irig-b007-b127", 10))
    )



class AluSysTimePriorityType(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priority8", 8),
          ("priority9", 9),
          ("priority10", 10),
          ("priority11", 11),
          ("priority12", 12),
          ("priority13", 13),
          ("priority14", 14),
          ("priority15", 15),
          ("priority16", 16),
          ("priority17", 17),
          ("holdover", 18))
    )



class AluSysTimeRefLeapSecSchedType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notScheduled", 0),
          ("forwardScheduled", 1),
          ("backwardScheduled", 2))
    )



class AluSysTimeReferenceType(TextualConvention, Integer32):
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
        *(("notApplic", 0),
          ("gnss", 1),
          ("ptp", 2),
          ("ntp", 3),
          ("sntp", 4),
          ("holdover", 5))
    )



class AluSysTimeReferenceId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_AluSystemMIBConformance_ObjectIdentity = ObjectIdentity
aluSystemMIBConformance = _AluSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13)
)
_AluSystemMIBCompliances_ObjectIdentity = ObjectIdentity
aluSystemMIBCompliances = _AluSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1)
)
_AluSystemMIBGroups_ObjectIdentity = ObjectIdentity
aluSystemMIBGroups = _AluSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2)
)
_AluSystemNotificationObjs_ObjectIdentity = ObjectIdentity
aluSystemNotificationObjs = _AluSystemNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 8)
)
_AluSystemNotifyTimeRefType_Type = AluSysTimeReferenceType
_AluSystemNotifyTimeRefType_Object = MibScalar
aluSystemNotifyTimeRefType = _AluSystemNotifyTimeRefType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 8, 1),
    _AluSystemNotifyTimeRefType_Type()
)
aluSystemNotifyTimeRefType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluSystemNotifyTimeRefType.setStatus("current")
_AluSystemNotifyTimeRefId_Type = AluSysTimeReferenceId
_AluSystemNotifyTimeRefId_Object = MibScalar
aluSystemNotifyTimeRefId = _AluSystemNotifyTimeRefId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 8, 2),
    _AluSystemNotifyTimeRefId_Type()
)
aluSystemNotifyTimeRefId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluSystemNotifyTimeRefId.setStatus("current")
_AluSystemObjs_ObjectIdentity = ObjectIdentity
aluSystemObjs = _AluSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13)
)
_AluTod1PpsInfo_ObjectIdentity = ObjectIdentity
aluTod1PpsInfo = _AluTod1PpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1)
)


class _AluTod1PpsMessageType_Type(AluTod1PpsMessageType):
    """Custom type aluTod1PpsMessageType based on AluTod1PpsMessageType"""
    defaultValue = 0


_AluTod1PpsMessageType_Type.__name__ = "AluTod1PpsMessageType"
_AluTod1PpsMessageType_Object = MibScalar
aluTod1PpsMessageType = _AluTod1PpsMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 1),
    _AluTod1PpsMessageType_Type()
)
aluTod1PpsMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTod1PpsMessageType.setStatus("current")


class _AluTod1PpsOutput_Type(TmnxAdminState):
    """Custom type aluTod1PpsOutput based on TmnxAdminState"""
    defaultValue = 3


_AluTod1PpsOutput_Type.__name__ = "TmnxAdminState"
_AluTod1PpsOutput_Object = MibScalar
aluTod1PpsOutput = _AluTod1PpsOutput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 2),
    _AluTod1PpsOutput_Type()
)
aluTod1PpsOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTod1PpsOutput.setStatus("current")


class _AluTod1PpsInput_Type(TmnxAdminState):
    """Custom type aluTod1PpsInput based on TmnxAdminState"""
    defaultValue = 3


_AluTod1PpsInput_Type.__name__ = "TmnxAdminState"
_AluTod1PpsInput_Object = MibScalar
aluTod1PpsInput = _AluTod1PpsInput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 3),
    _AluTod1PpsInput_Type()
)
aluTod1PpsInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTod1PpsInput.setStatus("current")
_AluNtpSystem_ObjectIdentity = ObjectIdentity
aluNtpSystem = _AluNtpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 2)
)


class _AluNtpMdaTimestamp_Type(TruthValue):
    """Custom type aluNtpMdaTimestamp based on TruthValue"""
    defaultValue = 2


_AluNtpMdaTimestamp_Type.__name__ = "TruthValue"
_AluNtpMdaTimestamp_Object = MibScalar
aluNtpMdaTimestamp = _AluNtpMdaTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 2, 1),
    _AluNtpMdaTimestamp_Type()
)
aluNtpMdaTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluNtpMdaTimestamp.setStatus("current")
_AluSysTimeSelector_ObjectIdentity = ObjectIdentity
aluSysTimeSelector = _AluSysTimeSelector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3)
)
_AluActiveTimeSourceType_Type = AluSysTimeReferenceType
_AluActiveTimeSourceType_Object = MibScalar
aluActiveTimeSourceType = _AluActiveTimeSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 1),
    _AluActiveTimeSourceType_Type()
)
aluActiveTimeSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluActiveTimeSourceType.setStatus("current")
_AluActiveTimeSourceId_Type = AluSysTimeReferenceId
_AluActiveTimeSourceId_Object = MibScalar
aluActiveTimeSourceId = _AluActiveTimeSourceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 2),
    _AluActiveTimeSourceId_Type()
)
aluActiveTimeSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluActiveTimeSourceId.setStatus("current")
_AluActiveTimeSourceChange_Type = TimeStamp
_AluActiveTimeSourceChange_Object = MibScalar
aluActiveTimeSourceChange = _AluActiveTimeSourceChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 3),
    _AluActiveTimeSourceChange_Type()
)
aluActiveTimeSourceChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluActiveTimeSourceChange.setStatus("current")
_AluTimeSelectorTable_Object = MibTable
aluTimeSelectorTable = _AluTimeSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4)
)
if mibBuilder.loadTexts:
    aluTimeSelectorTable.setStatus("current")
_AluTimeReferenceEntry_Object = MibTableRow
aluTimeReferenceEntry = _AluTimeReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1)
)
aluTimeReferenceEntry.setIndexNames(
    (0, "ALU-SYSTEM-MIB", "timeRefType"),
    (0, "ALU-SYSTEM-MIB", "timeRefId"),
)
if mibBuilder.loadTexts:
    aluTimeReferenceEntry.setStatus("current")
_TimeRefType_Type = AluSysTimeReferenceType
_TimeRefType_Object = MibTableColumn
timeRefType = _TimeRefType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 1),
    _TimeRefType_Type()
)
timeRefType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRefType.setStatus("current")
_TimeRefId_Type = AluSysTimeReferenceId
_TimeRefId_Object = MibTableColumn
timeRefId = _TimeRefId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 2),
    _TimeRefId_Type()
)
timeRefId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRefId.setStatus("current")
_TimeRefPriority_Type = AluSysTimePriorityType
_TimeRefPriority_Object = MibTableColumn
timeRefPriority = _TimeRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 3),
    _TimeRefPriority_Type()
)
timeRefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRefPriority.setStatus("current")
_TimeRefRowStatus_Type = RowStatus
_TimeRefRowStatus_Object = MibTableColumn
timeRefRowStatus = _TimeRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 4),
    _TimeRefRowStatus_Type()
)
timeRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRefRowStatus.setStatus("current")


class _TimeRefQualified_Type(TruthValue):
    """Custom type timeRefQualified based on TruthValue"""
    defaultValue = 2


_TimeRefQualified_Type.__name__ = "TruthValue"
_TimeRefQualified_Object = MibTableColumn
timeRefQualified = _TimeRefQualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 5),
    _TimeRefQualified_Type()
)
timeRefQualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefQualified.setStatus("current")
_TimeRefQualifiedChange_Type = TimeStamp
_TimeRefQualifiedChange_Object = MibTableColumn
timeRefQualifiedChange = _TimeRefQualifiedChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 6),
    _TimeRefQualifiedChange_Type()
)
timeRefQualifiedChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefQualifiedChange.setStatus("current")
_TimeRefPropertiesUpdate_Type = TimeStamp
_TimeRefPropertiesUpdate_Object = MibTableColumn
timeRefPropertiesUpdate = _TimeRefPropertiesUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 7),
    _TimeRefPropertiesUpdate_Type()
)
timeRefPropertiesUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefPropertiesUpdate.setStatus("current")
_TimeRefDeltaSec_Type = Integer32
_TimeRefDeltaSec_Object = MibTableColumn
timeRefDeltaSec = _TimeRefDeltaSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 8),
    _TimeRefDeltaSec_Type()
)
timeRefDeltaSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefDeltaSec.setStatus("current")
_TimeRefDeltaNs_Type = Integer32
_TimeRefDeltaNs_Object = MibTableColumn
timeRefDeltaNs = _TimeRefDeltaNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 9),
    _TimeRefDeltaNs_Type()
)
timeRefDeltaNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefDeltaNs.setStatus("current")
_TimeRefLeapSecSched_Type = AluSysTimeRefLeapSecSchedType
_TimeRefLeapSecSched_Object = MibTableColumn
timeRefLeapSecSched = _TimeRefLeapSecSched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 10),
    _TimeRefLeapSecSched_Type()
)
timeRefLeapSecSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefLeapSecSched.setStatus("current")


class _TimeRefLeapSecValid_Type(TruthValue):
    """Custom type timeRefLeapSecValid based on TruthValue"""
    defaultValue = 2


_TimeRefLeapSecValid_Type.__name__ = "TruthValue"
_TimeRefLeapSecValid_Object = MibTableColumn
timeRefLeapSecValid = _TimeRefLeapSecValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 11),
    _TimeRefLeapSecValid_Type()
)
timeRefLeapSecValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefLeapSecValid.setStatus("obsolete")
_TimeRefLeapSec_Type = Unsigned32
_TimeRefLeapSec_Object = MibTableColumn
timeRefLeapSec = _TimeRefLeapSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 12),
    _TimeRefLeapSec_Type()
)
timeRefLeapSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefLeapSec.setStatus("obsolete")
_TimeRefLeapSecUpdTime_Type = TimeStamp
_TimeRefLeapSecUpdTime_Object = MibTableColumn
timeRefLeapSecUpdTime = _TimeRefLeapSecUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 13),
    _TimeRefLeapSecUpdTime_Type()
)
timeRefLeapSecUpdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRefLeapSecUpdTime.setStatus("current")
_AluSystemSptConfig_ObjectIdentity = ObjectIdentity
aluSystemSptConfig = _AluSystemSptConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 4)
)


class _AluSystemSptSecAggRate_Type(TPortSchedulerPIR):
    """Custom type aluSystemSptSecAggRate based on TPortSchedulerPIR"""
    defaultValue = 50000


_AluSystemSptSecAggRate_Type.__name__ = "TPortSchedulerPIR"
_AluSystemSptSecAggRate_Object = MibScalar
aluSystemSptSecAggRate = _AluSystemSptSecAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 4, 1),
    _AluSystemSptSecAggRate_Type()
)
aluSystemSptSecAggRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSystemSptSecAggRate.setStatus("current")
_AluSystemNotifyPrefix_ObjectIdentity = ObjectIdentity
aluSystemNotifyPrefix = _AluSystemNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9)
)
_AluSystemNotification_ObjectIdentity = ObjectIdentity
aluSystemNotification = _AluSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0)
)

# Managed Objects groups

aluTod1PpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 1)
)
aluTod1PpsGroup.setObjects(
      *(("ALU-SYSTEM-MIB", "aluTod1PpsMessageType"),
        ("ALU-SYSTEM-MIB", "aluTod1PpsOutput"),
        ("ALU-SYSTEM-MIB", "aluTod1PpsInput"))
)
if mibBuilder.loadTexts:
    aluTod1PpsGroup.setStatus("current")

aluNtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 2)
)
aluNtpGroup.setObjects(
    ("ALU-SYSTEM-MIB", "aluNtpMdaTimestamp")
)
if mibBuilder.loadTexts:
    aluNtpGroup.setStatus("current")

aluSysTimeReferenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 3)
)
aluSysTimeReferenceGroup.setObjects(
      *(("ALU-SYSTEM-MIB", "aluActiveTimeSourceType"),
        ("ALU-SYSTEM-MIB", "aluActiveTimeSourceId"),
        ("ALU-SYSTEM-MIB", "aluActiveTimeSourceChange"),
        ("ALU-SYSTEM-MIB", "timeRefPriority"),
        ("ALU-SYSTEM-MIB", "timeRefRowStatus"),
        ("ALU-SYSTEM-MIB", "timeRefQualified"),
        ("ALU-SYSTEM-MIB", "timeRefQualifiedChange"),
        ("ALU-SYSTEM-MIB", "timeRefPropertiesUpdate"),
        ("ALU-SYSTEM-MIB", "timeRefDeltaSec"),
        ("ALU-SYSTEM-MIB", "timeRefDeltaNs"),
        ("ALU-SYSTEM-MIB", "timeRefLeapSecSched"),
        ("ALU-SYSTEM-MIB", "timeRefLeapSecValid"),
        ("ALU-SYSTEM-MIB", "timeRefLeapSec"))
)
if mibBuilder.loadTexts:
    aluSysTimeReferenceGroup.setStatus("current")

aluSysTimeNotifyObjsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 4)
)
aluSysTimeNotifyObjsV6v1Group.setObjects(
      *(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"),
        ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"))
)
if mibBuilder.loadTexts:
    aluSysTimeNotifyObjsV6v1Group.setStatus("current")

aluSysTimeReferenceV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 6)
)
aluSysTimeReferenceV6v1Group.setObjects(
      *(("ALU-SYSTEM-MIB", "aluActiveTimeSourceType"),
        ("ALU-SYSTEM-MIB", "aluActiveTimeSourceId"),
        ("ALU-SYSTEM-MIB", "aluActiveTimeSourceChange"),
        ("ALU-SYSTEM-MIB", "timeRefPriority"),
        ("ALU-SYSTEM-MIB", "timeRefRowStatus"),
        ("ALU-SYSTEM-MIB", "timeRefQualified"),
        ("ALU-SYSTEM-MIB", "timeRefQualifiedChange"),
        ("ALU-SYSTEM-MIB", "timeRefPropertiesUpdate"),
        ("ALU-SYSTEM-MIB", "timeRefDeltaSec"),
        ("ALU-SYSTEM-MIB", "timeRefDeltaNs"),
        ("ALU-SYSTEM-MIB", "timeRefLeapSecSched"),
        ("ALU-SYSTEM-MIB", "timeRefLeapSecUpdTime"))
)
if mibBuilder.loadTexts:
    aluSysTimeReferenceV6v1Group.setStatus("current")

aluSysTimeReferenceObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 7)
)
aluSysTimeReferenceObsoleteGroup.setObjects(
      *(("ALU-SYSTEM-MIB", "timeRefLeapSecValid"),
        ("ALU-SYSTEM-MIB", "timeRefLeapSec"))
)
if mibBuilder.loadTexts:
    aluSysTimeReferenceObsoleteGroup.setStatus("current")

aluSystemSptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 8)
)
aluSystemSptGroup.setObjects(
    ("ALU-SYSTEM-MIB", "aluSystemSptSecAggRate")
)
if mibBuilder.loadTexts:
    aluSystemSptGroup.setStatus("current")


# Notification objects

aluTimeRefCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 1)
)
aluTimeRefCreated.setObjects(
      *(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"),
        ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"),
        ("ALU-SYSTEM-MIB", "timeRefPriority"))
)
if mibBuilder.loadTexts:
    aluTimeRefCreated.setStatus(
        "current"
    )

aluTimeRefDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 2)
)
aluTimeRefDeleted.setObjects(
      *(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"),
        ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
)
if mibBuilder.loadTexts:
    aluTimeRefDeleted.setStatus(
        "current"
    )

aluTimeRefQualified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 3)
)
aluTimeRefQualified.setObjects(
      *(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"),
        ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
)
if mibBuilder.loadTexts:
    aluTimeRefQualified.setStatus(
        "current"
    )

aluTimeRefDisqualified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 4)
)
aluTimeRefDisqualified.setObjects(
      *(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"),
        ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
)
if mibBuilder.loadTexts:
    aluTimeRefDisqualified.setStatus(
        "current"
    )

aluTimeRefSelect = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 5)
)
aluTimeRefSelect.setObjects(
      *(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"),
        ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
)
if mibBuilder.loadTexts:
    aluTimeRefSelect.setStatus(
        "current"
    )


# Notifications groups

aluSysTimeNotificationV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 5)
)
aluSysTimeNotificationV6v1Group.setObjects(
      *(("ALU-SYSTEM-MIB", "aluTimeRefCreated"),
        ("ALU-SYSTEM-MIB", "aluTimeRefDeleted"),
        ("ALU-SYSTEM-MIB", "aluTimeRefQualified"),
        ("ALU-SYSTEM-MIB", "aluTimeRefDisqualified"),
        ("ALU-SYSTEM-MIB", "aluTimeRefSelect"))
)
if mibBuilder.loadTexts:
    aluSysTimeNotificationV6v1Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 1)
)
aluSystemMIBCompliance.setObjects(
    ("ALU-SYSTEM-MIB", "aluTod1PpsGroup")
)
if mibBuilder.loadTexts:
    aluSystemMIBCompliance.setStatus(
        "obsolete"
    )

aluSystemV6v1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 2)
)
aluSystemV6v1MIBCompliance.setObjects(
      *(("ALU-SYSTEM-MIB", "aluTod1PpsGroup"),
        ("ALU-SYSTEM-MIB", "aluNtpMdaTimestamp"),
        ("ALU-SYSTEM-MIB", "aluSysTimeReferenceGroup"),
        ("ALU-SYSTEM-MIB", "aluSysTimeNotificationV6v1Group"))
)
if mibBuilder.loadTexts:
    aluSystemV6v1MIBCompliance.setStatus(
        "obsolete"
    )

aluSystemV7v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 3)
)
aluSystemV7v0MIBCompliance.setObjects(
      *(("ALU-SYSTEM-MIB", "aluTod1PpsGroup"),
        ("ALU-SYSTEM-MIB", "aluNtpMdaTimestamp"),
        ("ALU-SYSTEM-MIB", "aluSysTimeReferenceGroup"),
        ("ALU-SYSTEM-MIB", "aluSysTimeNotificationV6v1Group"),
        ("ALU-SYSTEM-MIB", "aluSystemSptGroup"))
)
if mibBuilder.loadTexts:
    aluSystemV7v0MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-SYSTEM-MIB",
    **{"AluTod1PpsMessageType": AluTod1PpsMessageType,
       "AluSysTimePriorityType": AluSysTimePriorityType,
       "AluSysTimeRefLeapSecSchedType": AluSysTimeRefLeapSecSchedType,
       "AluSysTimeReferenceType": AluSysTimeReferenceType,
       "AluSysTimeReferenceId": AluSysTimeReferenceId,
       "aluSystemMIBModule": aluSystemMIBModule,
       "aluSystemMIBConformance": aluSystemMIBConformance,
       "aluSystemMIBCompliances": aluSystemMIBCompliances,
       "aluSystemMIBCompliance": aluSystemMIBCompliance,
       "aluSystemV6v1MIBCompliance": aluSystemV6v1MIBCompliance,
       "aluSystemV7v0MIBCompliance": aluSystemV7v0MIBCompliance,
       "aluSystemMIBGroups": aluSystemMIBGroups,
       "aluTod1PpsGroup": aluTod1PpsGroup,
       "aluNtpGroup": aluNtpGroup,
       "aluSysTimeReferenceGroup": aluSysTimeReferenceGroup,
       "aluSysTimeNotifyObjsV6v1Group": aluSysTimeNotifyObjsV6v1Group,
       "aluSysTimeNotificationV6v1Group": aluSysTimeNotificationV6v1Group,
       "aluSysTimeReferenceV6v1Group": aluSysTimeReferenceV6v1Group,
       "aluSysTimeReferenceObsoleteGroup": aluSysTimeReferenceObsoleteGroup,
       "aluSystemSptGroup": aluSystemSptGroup,
       "aluSystemNotificationObjs": aluSystemNotificationObjs,
       "aluSystemNotifyTimeRefType": aluSystemNotifyTimeRefType,
       "aluSystemNotifyTimeRefId": aluSystemNotifyTimeRefId,
       "aluSystemObjs": aluSystemObjs,
       "aluTod1PpsInfo": aluTod1PpsInfo,
       "aluTod1PpsMessageType": aluTod1PpsMessageType,
       "aluTod1PpsOutput": aluTod1PpsOutput,
       "aluTod1PpsInput": aluTod1PpsInput,
       "aluNtpSystem": aluNtpSystem,
       "aluNtpMdaTimestamp": aluNtpMdaTimestamp,
       "aluSysTimeSelector": aluSysTimeSelector,
       "aluActiveTimeSourceType": aluActiveTimeSourceType,
       "aluActiveTimeSourceId": aluActiveTimeSourceId,
       "aluActiveTimeSourceChange": aluActiveTimeSourceChange,
       "aluTimeSelectorTable": aluTimeSelectorTable,
       "aluTimeReferenceEntry": aluTimeReferenceEntry,
       "timeRefType": timeRefType,
       "timeRefId": timeRefId,
       "timeRefPriority": timeRefPriority,
       "timeRefRowStatus": timeRefRowStatus,
       "timeRefQualified": timeRefQualified,
       "timeRefQualifiedChange": timeRefQualifiedChange,
       "timeRefPropertiesUpdate": timeRefPropertiesUpdate,
       "timeRefDeltaSec": timeRefDeltaSec,
       "timeRefDeltaNs": timeRefDeltaNs,
       "timeRefLeapSecSched": timeRefLeapSecSched,
       "timeRefLeapSecValid": timeRefLeapSecValid,
       "timeRefLeapSec": timeRefLeapSec,
       "timeRefLeapSecUpdTime": timeRefLeapSecUpdTime,
       "aluSystemSptConfig": aluSystemSptConfig,
       "aluSystemSptSecAggRate": aluSystemSptSecAggRate,
       "aluSystemNotifyPrefix": aluSystemNotifyPrefix,
       "aluSystemNotification": aluSystemNotification,
       "aluTimeRefCreated": aluTimeRefCreated,
       "aluTimeRefDeleted": aluTimeRefDeleted,
       "aluTimeRefQualified": aluTimeRefQualified,
       "aluTimeRefDisqualified": aluTimeRefDisqualified,
       "aluTimeRefSelect": aluTimeRefSelect}
)
