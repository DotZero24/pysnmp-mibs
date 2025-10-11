# SNMP MIB module (CHECKPOINT-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/checkpoint/CHECKPOINT-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:21:42 2025
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

(asgNetIfName,
 fanSpeedSensorName,
 fanSpeedSensorStatus,
 fanSpeedSensorType,
 fanSpeedSensorUnit,
 fanSpeedSensorValue,
 fwLSConnName,
 fwLSConnOverall,
 fwLSConnOverallDesc,
 fwLSConnState,
 fwLSConnStateDesc,
 fwLocalLoggingDesc,
 fwLocalLoggingStat,
 haBlockState,
 haClusterXLFailover,
 haIP,
 haIdentifier,
 haIfName,
 haProblemDescr,
 haProblemName,
 haProblemPriority,
 haProblemStatus,
 haProblemVerified,
 haShared,
 haStatCode,
 haStatLong,
 haStatShort,
 haState,
 haStatus,
 haTrusted,
 memActiveReal64,
 memActiveVirtual64,
 memTotalReal64,
 memTotalVirtual64,
 multiDiskFreeAvailablePercent,
 multiDiskName,
 multiProcIdleTime,
 multiProcIndex,
 multiProcInterrupts,
 multiProcRunQueue,
 multiProcSystemTime,
 multiProcUsage,
 multiProcUserTime,
 raidDiskFlags,
 raidDiskID,
 raidDiskState,
 raidDiskVolumeID,
 raidVolumeID,
 raidVolumeState,
 svnNetIfAddress,
 svnNetIfName,
 svnNetIfOperState,
 svnNetIfRXDrops,
 svnNetIfState,
 tempertureSensorName,
 tempertureSensorStatus,
 tempertureSensorType,
 tempertureSensorUnit,
 tempertureSensorValue,
 voltageSensorName,
 voltageSensorStatus,
 voltageSensorType,
 voltageSensorUnit,
 voltageSensorValue) = mibBuilder.importSymbols(
    "CHECKPOINT-MIB",
    "asgNetIfName",
    "fanSpeedSensorName",
    "fanSpeedSensorStatus",
    "fanSpeedSensorType",
    "fanSpeedSensorUnit",
    "fanSpeedSensorValue",
    "fwLSConnName",
    "fwLSConnOverall",
    "fwLSConnOverallDesc",
    "fwLSConnState",
    "fwLSConnStateDesc",
    "fwLocalLoggingDesc",
    "fwLocalLoggingStat",
    "haBlockState",
    "haClusterXLFailover",
    "haIP",
    "haIdentifier",
    "haIfName",
    "haProblemDescr",
    "haProblemName",
    "haProblemPriority",
    "haProblemStatus",
    "haProblemVerified",
    "haShared",
    "haStatCode",
    "haStatLong",
    "haStatShort",
    "haState",
    "haStatus",
    "haTrusted",
    "memActiveReal64",
    "memActiveVirtual64",
    "memTotalReal64",
    "memTotalVirtual64",
    "multiDiskFreeAvailablePercent",
    "multiDiskName",
    "multiProcIdleTime",
    "multiProcIndex",
    "multiProcInterrupts",
    "multiProcRunQueue",
    "multiProcSystemTime",
    "multiProcUsage",
    "multiProcUserTime",
    "raidDiskFlags",
    "raidDiskID",
    "raidDiskState",
    "raidDiskVolumeID",
    "raidVolumeID",
    "raidVolumeState",
    "svnNetIfAddress",
    "svnNetIfName",
    "svnNetIfOperState",
    "svnNetIfRXDrops",
    "svnNetIfState",
    "tempertureSensorName",
    "tempertureSensorStatus",
    "tempertureSensorType",
    "tempertureSensorUnit",
    "tempertureSensorValue",
    "voltageSensorName",
    "voltageSensorStatus",
    "voltageSensorType",
    "voltageSensorUnit",
    "voltageSensorValue")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

chkpntTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 0)
)
if mibBuilder.loadTexts:
    chkpntTrapMibModule.setRevisions(
        ("2013-12-26 13:09",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Checkpoint_ObjectIdentity = ObjectIdentity
checkpoint = _Checkpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1)
)
_ChkpntTrap_ObjectIdentity = ObjectIdentity
chkpntTrap = _ChkpntTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000)
)
_ChkpntTrapInfo_ObjectIdentity = ObjectIdentity
chkpntTrapInfo = _ChkpntTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0)
)
_ChkpntTrapOID_Type = DisplayString
_ChkpntTrapOID_Object = MibScalar
chkpntTrapOID = _ChkpntTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 10),
    _ChkpntTrapOID_Type()
)
chkpntTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapOID.setStatus("current")
_ChkpntTrapOIDValue_Type = DisplayString
_ChkpntTrapOIDValue_Object = MibScalar
chkpntTrapOIDValue = _ChkpntTrapOIDValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 11),
    _ChkpntTrapOIDValue_Type()
)
chkpntTrapOIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapOIDValue.setStatus("current")
_ChkpntTrapMsgText_Type = DisplayString
_ChkpntTrapMsgText_Object = MibScalar
chkpntTrapMsgText = _ChkpntTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 12),
    _ChkpntTrapMsgText_Type()
)
chkpntTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapMsgText.setStatus("current")


class _ChkpntTrapSeverity_Type(Integer32):
    """Custom type chkpntTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChkpntTrapSeverity_Type.__name__ = "Integer32"
_ChkpntTrapSeverity_Object = MibScalar
chkpntTrapSeverity = _ChkpntTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 13),
    _ChkpntTrapSeverity_Type()
)
chkpntTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapSeverity.setStatus("current")
_ChkpntTrapCategory_Type = DisplayString
_ChkpntTrapCategory_Object = MibScalar
chkpntTrapCategory = _ChkpntTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 14),
    _ChkpntTrapCategory_Type()
)
chkpntTrapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapCategory.setStatus("current")


class _ChkpntTrapChassisId_Type(Integer32):
    """Custom type chkpntTrapChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChkpntTrapChassisId_Type.__name__ = "Integer32"
_ChkpntTrapChassisId_Object = MibScalar
chkpntTrapChassisId = _ChkpntTrapChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 15),
    _ChkpntTrapChassisId_Type()
)
chkpntTrapChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapChassisId.setStatus("current")


class _ChkpntTrapBladeId_Type(Integer32):
    """Custom type chkpntTrapBladeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChkpntTrapBladeId_Type.__name__ = "Integer32"
_ChkpntTrapBladeId_Object = MibScalar
chkpntTrapBladeId = _ChkpntTrapBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 16),
    _ChkpntTrapBladeId_Type()
)
chkpntTrapBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapBladeId.setStatus("current")
_MultiDiskName_Type = DisplayString
_MultiDiskName_Object = MibScalar
multiDiskName = _MultiDiskName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 17),
    _MultiDiskName_Type()
)
multiDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskName.setStatus("current")


class _MultiDiskFreeAvailablePercent_Type(Integer32):
    """Custom type multiDiskFreeAvailablePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MultiDiskFreeAvailablePercent_Type.__name__ = "Integer32"
_MultiDiskFreeAvailablePercent_Object = MibScalar
multiDiskFreeAvailablePercent = _MultiDiskFreeAvailablePercent_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 18),
    _MultiDiskFreeAvailablePercent_Type()
)
multiDiskFreeAvailablePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskFreeAvailablePercent.setStatus("current")


class _RaidVolumeID_Type(Integer32):
    """Custom type raidVolumeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidVolumeID_Type.__name__ = "Integer32"
_RaidVolumeID_Object = MibScalar
raidVolumeID = _RaidVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 19),
    _RaidVolumeID_Type()
)
raidVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeID.setStatus("current")


class _RaidVolumeState_Type(Integer32):
    """Custom type raidVolumeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidVolumeState_Type.__name__ = "Integer32"
_RaidVolumeState_Object = MibScalar
raidVolumeState = _RaidVolumeState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 20),
    _RaidVolumeState_Type()
)
raidVolumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeState.setStatus("current")


class _RaidDiskVolumeID_Type(Integer32):
    """Custom type raidDiskVolumeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidDiskVolumeID_Type.__name__ = "Integer32"
_RaidDiskVolumeID_Object = MibScalar
raidDiskVolumeID = _RaidDiskVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 21),
    _RaidDiskVolumeID_Type()
)
raidDiskVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskVolumeID.setStatus("current")


class _RaidDiskID_Type(Integer32):
    """Custom type raidDiskID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidDiskID_Type.__name__ = "Integer32"
_RaidDiskID_Object = MibScalar
raidDiskID = _RaidDiskID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 22),
    _RaidDiskID_Type()
)
raidDiskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskID.setStatus("current")


class _RaidDiskState_Type(Integer32):
    """Custom type raidDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidDiskState_Type.__name__ = "Integer32"
_RaidDiskState_Object = MibScalar
raidDiskState = _RaidDiskState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 23),
    _RaidDiskState_Type()
)
raidDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskState.setStatus("current")


class _RaidDiskFlags_Type(Integer32):
    """Custom type raidDiskFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidDiskFlags_Type.__name__ = "Integer32"
_RaidDiskFlags_Object = MibScalar
raidDiskFlags = _RaidDiskFlags_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 24),
    _RaidDiskFlags_Type()
)
raidDiskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskFlags.setStatus("current")
_MultiProcIndex_Type = Unsigned32
_MultiProcIndex_Object = MibScalar
multiProcIndex = _MultiProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 25),
    _MultiProcIndex_Type()
)
multiProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcIndex.setStatus("current")
_MultiProcUserTime_Type = Unsigned32
_MultiProcUserTime_Object = MibScalar
multiProcUserTime = _MultiProcUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 26),
    _MultiProcUserTime_Type()
)
multiProcUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcUserTime.setStatus("current")
_MultiProcSystemTime_Type = Unsigned32
_MultiProcSystemTime_Object = MibScalar
multiProcSystemTime = _MultiProcSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 27),
    _MultiProcSystemTime_Type()
)
multiProcSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcSystemTime.setStatus("current")
_MultiProcIdleTime_Type = Unsigned32
_MultiProcIdleTime_Object = MibScalar
multiProcIdleTime = _MultiProcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 28),
    _MultiProcIdleTime_Type()
)
multiProcIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcIdleTime.setStatus("current")
_MultiProcUsage_Type = Unsigned32
_MultiProcUsage_Object = MibScalar
multiProcUsage = _MultiProcUsage_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 29),
    _MultiProcUsage_Type()
)
multiProcUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcUsage.setStatus("current")


class _MultiProcRunQueue_Type(Integer32):
    """Custom type multiProcRunQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MultiProcRunQueue_Type.__name__ = "Integer32"
_MultiProcRunQueue_Object = MibScalar
multiProcRunQueue = _MultiProcRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 30),
    _MultiProcRunQueue_Type()
)
multiProcRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcRunQueue.setStatus("current")
_MultiProcInterrupts_Type = Unsigned32
_MultiProcInterrupts_Object = MibScalar
multiProcInterrupts = _MultiProcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 31),
    _MultiProcInterrupts_Type()
)
multiProcInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcInterrupts.setStatus("current")


class _MemTotalVirtual64_Type(DisplayString):
    """Custom type memTotalVirtual64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemTotalVirtual64_Type.__name__ = "DisplayString"
_MemTotalVirtual64_Object = MibScalar
memTotalVirtual64 = _MemTotalVirtual64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 32),
    _MemTotalVirtual64_Type()
)
memTotalVirtual64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalVirtual64.setStatus("current")


class _MemActiveVirtual64_Type(DisplayString):
    """Custom type memActiveVirtual64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemActiveVirtual64_Type.__name__ = "DisplayString"
_MemActiveVirtual64_Object = MibScalar
memActiveVirtual64 = _MemActiveVirtual64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 33),
    _MemActiveVirtual64_Type()
)
memActiveVirtual64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveVirtual64.setStatus("current")


class _MemTotalReal64_Type(DisplayString):
    """Custom type memTotalReal64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemTotalReal64_Type.__name__ = "DisplayString"
_MemTotalReal64_Object = MibScalar
memTotalReal64 = _MemTotalReal64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 34),
    _MemTotalReal64_Type()
)
memTotalReal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal64.setStatus("current")


class _MemActiveReal64_Type(DisplayString):
    """Custom type memActiveReal64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemActiveReal64_Type.__name__ = "DisplayString"
_MemActiveReal64_Object = MibScalar
memActiveReal64 = _MemActiveReal64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 35),
    _MemActiveReal64_Type()
)
memActiveReal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveReal64.setStatus("current")


class _TempertureSensorName_Type(DisplayString):
    """Custom type tempertureSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorName_Type.__name__ = "DisplayString"
_TempertureSensorName_Object = MibScalar
tempertureSensorName = _TempertureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 36),
    _TempertureSensorName_Type()
)
tempertureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorName.setStatus("current")


class _TempertureSensorValue_Type(DisplayString):
    """Custom type tempertureSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorValue_Type.__name__ = "DisplayString"
_TempertureSensorValue_Object = MibScalar
tempertureSensorValue = _TempertureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 37),
    _TempertureSensorValue_Type()
)
tempertureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorValue.setStatus("current")


class _TempertureSensorUnit_Type(DisplayString):
    """Custom type tempertureSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorUnit_Type.__name__ = "DisplayString"
_TempertureSensorUnit_Object = MibScalar
tempertureSensorUnit = _TempertureSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 38),
    _TempertureSensorUnit_Type()
)
tempertureSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorUnit.setStatus("current")


class _TempertureSensorType_Type(DisplayString):
    """Custom type tempertureSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorType_Type.__name__ = "DisplayString"
_TempertureSensorType_Object = MibScalar
tempertureSensorType = _TempertureSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 39),
    _TempertureSensorType_Type()
)
tempertureSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorType.setStatus("current")


class _TempertureSensorStatus_Type(Integer32):
    """Custom type tempertureSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TempertureSensorStatus_Type.__name__ = "Integer32"
_TempertureSensorStatus_Object = MibScalar
tempertureSensorStatus = _TempertureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 40),
    _TempertureSensorStatus_Type()
)
tempertureSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorStatus.setStatus("current")


class _FanSpeedSensorName_Type(DisplayString):
    """Custom type fanSpeedSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorName_Type.__name__ = "DisplayString"
_FanSpeedSensorName_Object = MibScalar
fanSpeedSensorName = _FanSpeedSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 41),
    _FanSpeedSensorName_Type()
)
fanSpeedSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorName.setStatus("current")


class _FanSpeedSensorValue_Type(DisplayString):
    """Custom type fanSpeedSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorValue_Type.__name__ = "DisplayString"
_FanSpeedSensorValue_Object = MibScalar
fanSpeedSensorValue = _FanSpeedSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 42),
    _FanSpeedSensorValue_Type()
)
fanSpeedSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorValue.setStatus("current")


class _FanSpeedSensorUnit_Type(DisplayString):
    """Custom type fanSpeedSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorUnit_Type.__name__ = "DisplayString"
_FanSpeedSensorUnit_Object = MibScalar
fanSpeedSensorUnit = _FanSpeedSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 43),
    _FanSpeedSensorUnit_Type()
)
fanSpeedSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorUnit.setStatus("current")


class _FanSpeedSensorType_Type(DisplayString):
    """Custom type fanSpeedSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorType_Type.__name__ = "DisplayString"
_FanSpeedSensorType_Object = MibScalar
fanSpeedSensorType = _FanSpeedSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 44),
    _FanSpeedSensorType_Type()
)
fanSpeedSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorType.setStatus("current")


class _FanSpeedSensorStatus_Type(Integer32):
    """Custom type fanSpeedSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FanSpeedSensorStatus_Type.__name__ = "Integer32"
_FanSpeedSensorStatus_Object = MibScalar
fanSpeedSensorStatus = _FanSpeedSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 45),
    _FanSpeedSensorStatus_Type()
)
fanSpeedSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorStatus.setStatus("current")


class _VoltageSensorName_Type(DisplayString):
    """Custom type voltageSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorName_Type.__name__ = "DisplayString"
_VoltageSensorName_Object = MibScalar
voltageSensorName = _VoltageSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 46),
    _VoltageSensorName_Type()
)
voltageSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorName.setStatus("current")


class _VoltageSensorValue_Type(DisplayString):
    """Custom type voltageSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorValue_Type.__name__ = "DisplayString"
_VoltageSensorValue_Object = MibScalar
voltageSensorValue = _VoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 47),
    _VoltageSensorValue_Type()
)
voltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValue.setStatus("current")


class _VoltageSensorUnit_Type(DisplayString):
    """Custom type voltageSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorUnit_Type.__name__ = "DisplayString"
_VoltageSensorUnit_Object = MibScalar
voltageSensorUnit = _VoltageSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 48),
    _VoltageSensorUnit_Type()
)
voltageSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorUnit.setStatus("current")


class _VoltageSensorType_Type(DisplayString):
    """Custom type voltageSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorType_Type.__name__ = "DisplayString"
_VoltageSensorType_Object = MibScalar
voltageSensorType = _VoltageSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 49),
    _VoltageSensorType_Type()
)
voltageSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorType.setStatus("current")


class _VoltageSensorStatus_Type(Integer32):
    """Custom type voltageSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VoltageSensorStatus_Type.__name__ = "Integer32"
_VoltageSensorStatus_Object = MibScalar
voltageSensorStatus = _VoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 50),
    _VoltageSensorStatus_Type()
)
voltageSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorStatus.setStatus("current")
_ChkpntTrapNet_ObjectIdentity = ObjectIdentity
chkpntTrapNet = _ChkpntTrapNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1)
)
_ChkpntTrapDisk_ObjectIdentity = ObjectIdentity
chkpntTrapDisk = _ChkpntTrapDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2)
)
_ChkpntTrapCPU_ObjectIdentity = ObjectIdentity
chkpntTrapCPU = _ChkpntTrapCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3)
)
_ChkpntTrapMemory_ObjectIdentity = ObjectIdentity
chkpntTrapMemory = _ChkpntTrapMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4)
)
_ChkpntTrapHWSensor_ObjectIdentity = ObjectIdentity
chkpntTrapHWSensor = _ChkpntTrapHWSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5)
)
_ChkpntTrapTempertureSensor_ObjectIdentity = ObjectIdentity
chkpntTrapTempertureSensor = _ChkpntTrapTempertureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 1)
)
_ChkpntTrapFanSpeedSensor_ObjectIdentity = ObjectIdentity
chkpntTrapFanSpeedSensor = _ChkpntTrapFanSpeedSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 2)
)
_ChkpntTrapVoltageSensor_ObjectIdentity = ObjectIdentity
chkpntTrapVoltageSensor = _ChkpntTrapVoltageSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 3)
)
_ChkpntTrapHA_ObjectIdentity = ObjectIdentity
chkpntTrapHA = _ChkpntTrapHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6)
)
_ChkpntTrapLSConn_ObjectIdentity = ObjectIdentity
chkpntTrapLSConn = _ChkpntTrapLSConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7)
)
_AsgTrap_ObjectIdentity = ObjectIdentity
asgTrap = _AsgTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001)
)
_AsgTrapInfo_ObjectIdentity = ObjectIdentity
asgTrapInfo = _AsgTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0)
)
_AsgTrapChassisId_Type = DisplayString
_AsgTrapChassisId_Object = MibScalar
asgTrapChassisId = _AsgTrapChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 10),
    _AsgTrapChassisId_Type()
)
asgTrapChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapChassisId.setStatus("current")
_AsgTrapBladeId_Type = DisplayString
_AsgTrapBladeId_Object = MibScalar
asgTrapBladeId = _AsgTrapBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 11),
    _AsgTrapBladeId_Type()
)
asgTrapBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapBladeId.setStatus("current")
_AsgTrapMsgText_Type = DisplayString
_AsgTrapMsgText_Object = MibScalar
asgTrapMsgText = _AsgTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 12),
    _AsgTrapMsgText_Type()
)
asgTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapMsgText.setStatus("current")


class _AsgTrapPriority_Type(Integer32):
    """Custom type asgTrapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AsgTrapPriority_Type.__name__ = "Integer32"
_AsgTrapPriority_Object = MibScalar
asgTrapPriority = _AsgTrapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 13),
    _AsgTrapPriority_Type()
)
asgTrapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapPriority.setStatus("current")
_AsgTrapOID_Type = DisplayString
_AsgTrapOID_Object = MibScalar
asgTrapOID = _AsgTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 14),
    _AsgTrapOID_Type()
)
asgTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapOID.setStatus("current")
_AsgTrapOIDValue_Type = DisplayString
_AsgTrapOIDValue_Object = MibScalar
asgTrapOIDValue = _AsgTrapOIDValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 15),
    _AsgTrapOIDValue_Type()
)
asgTrapOIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapOIDValue.setStatus("current")
_AsgTrapSN_Type = DisplayString
_AsgTrapSN_Object = MibScalar
asgTrapSN = _AsgTrapSN_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 16),
    _AsgTrapSN_Type()
)
asgTrapSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapSN.setStatus("current")
_AsgCoreId_Type = DisplayString
_AsgCoreId_Object = MibScalar
asgCoreId = _AsgCoreId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 17),
    _AsgCoreId_Type()
)
asgCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgCoreId.setStatus("current")
_AsgTrapCategory_Type = DisplayString
_AsgTrapCategory_Object = MibScalar
asgTrapCategory = _AsgTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 0, 18),
    _AsgTrapCategory_Type()
)
asgTrapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asgTrapCategory.setStatus("current")
_AsgTrapHA_ObjectIdentity = ObjectIdentity
asgTrapHA = _AsgTrapHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 1)
)
_AsgTrapNet_ObjectIdentity = ObjectIdentity
asgTrapNet = _AsgTrapNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 2)
)
_AsgTrapDisk_ObjectIdentity = ObjectIdentity
asgTrapDisk = _AsgTrapDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 3)
)
_AsgTrapCPU_ObjectIdentity = ObjectIdentity
asgTrapCPU = _AsgTrapCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 4)
)
_AsgTrapMemory_ObjectIdentity = ObjectIdentity
asgTrapMemory = _AsgTrapMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 5)
)
_AsgTrapCplic_ObjectIdentity = ObjectIdentity
asgTrapCplic = _AsgTrapCplic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 6)
)
_AsgTrapHWSensor_ObjectIdentity = ObjectIdentity
asgTrapHWSensor = _AsgTrapHWSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7)
)
_AsgTrapTempertureSensor_ObjectIdentity = ObjectIdentity
asgTrapTempertureSensor = _AsgTrapTempertureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 1)
)
_AsgTrapFanSpeedSensor_ObjectIdentity = ObjectIdentity
asgTrapFanSpeedSensor = _AsgTrapFanSpeedSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 2)
)
_AsgTrapVoltageSensor_ObjectIdentity = ObjectIdentity
asgTrapVoltageSensor = _AsgTrapVoltageSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 3)
)
_AsgTrapSSMSensor_ObjectIdentity = ObjectIdentity
asgTrapSSMSensor = _AsgTrapSSMSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 4)
)
_AsgTrapCMMSensor_ObjectIdentity = ObjectIdentity
asgTrapCMMSensor = _AsgTrapCMMSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 5)
)
_AsgTrapPerf_ObjectIdentity = ObjectIdentity
asgTrapPerf = _AsgTrapPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8)
)
_AsgTrapGeneral_ObjectIdentity = ObjectIdentity
asgTrapGeneral = _AsgTrapGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10)
)
_ChkpntTrapMIBConformance_ObjectIdentity = ObjectIdentity
chkpntTrapMIBConformance = _ChkpntTrapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2)
)
_ChkpntTrapMIBCompliances_ObjectIdentity = ObjectIdentity
chkpntTrapMIBCompliances = _ChkpntTrapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2, 1)
)
_ChkpntTrapMIBGroups_ObjectIdentity = ObjectIdentity
chkpntTrapMIBGroups = _ChkpntTrapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2, 2)
)
_ChkpntNotificationGroups_ObjectIdentity = ObjectIdentity
chkpntNotificationGroups = _ChkpntNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2, 3)
)

# Managed Objects groups

chkpntTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2620, 2, 2, 1)
)
chkpntTrapGroup.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiDiskName"),
        ("CHECKPOINT-MIB", "multiDiskFreeAvailablePercent"),
        ("CHECKPOINT-MIB", "raidVolumeID"),
        ("CHECKPOINT-MIB", "raidVolumeState"),
        ("CHECKPOINT-MIB", "raidDiskVolumeID"),
        ("CHECKPOINT-MIB", "raidDiskID"),
        ("CHECKPOINT-MIB", "raidDiskState"),
        ("CHECKPOINT-MIB", "raidDiskFlags"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapBladeId"),
        ("CHECKPOINT-MIB", "multiProcIndex"),
        ("CHECKPOINT-MIB", "multiProcUserTime"),
        ("CHECKPOINT-MIB", "multiProcSystemTime"),
        ("CHECKPOINT-MIB", "multiProcIdleTime"),
        ("CHECKPOINT-MIB", "multiProcUsage"),
        ("CHECKPOINT-MIB", "multiProcRunQueue"),
        ("CHECKPOINT-MIB", "multiProcInterrupts"),
        ("CHECKPOINT-MIB", "memTotalVirtual64"),
        ("CHECKPOINT-MIB", "memActiveVirtual64"),
        ("CHECKPOINT-MIB", "memTotalReal64"),
        ("CHECKPOINT-MIB", "memActiveReal64"),
        ("CHECKPOINT-MIB", "tempertureSensorName"),
        ("CHECKPOINT-MIB", "tempertureSensorValue"),
        ("CHECKPOINT-MIB", "tempertureSensorUnit"),
        ("CHECKPOINT-MIB", "tempertureSensorType"),
        ("CHECKPOINT-MIB", "tempertureSensorStatus"),
        ("CHECKPOINT-MIB", "fanSpeedSensorName"),
        ("CHECKPOINT-MIB", "fanSpeedSensorValue"),
        ("CHECKPOINT-MIB", "fanSpeedSensorUnit"),
        ("CHECKPOINT-MIB", "fanSpeedSensorType"),
        ("CHECKPOINT-MIB", "fanSpeedSensorStatus"),
        ("CHECKPOINT-MIB", "voltageSensorName"),
        ("CHECKPOINT-MIB", "voltageSensorValue"),
        ("CHECKPOINT-MIB", "voltageSensorUnit"),
        ("CHECKPOINT-MIB", "voltageSensorType"),
        ("CHECKPOINT-MIB", "voltageSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntTrapGroup.setStatus("current")


# Notification objects

chkpntTrapNetIfState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 1)
)
chkpntTrapNetIfState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfAddress"),
        ("CHECKPOINT-MIB", "svnNetIfState"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfState.setStatus(
        "current"
    )

chkpntTrapNetIfUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 2)
)
chkpntTrapNetIfUnplugged.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfAddress"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfUnplugged.setStatus(
        "current"
    )

chkpntTrapNewConnRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 3)
)
chkpntTrapNewConnRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapNewConnRate.setStatus(
        "current"
    )

chkpntTrapConcurrentConnRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 4)
)
chkpntTrapConcurrentConnRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapConcurrentConnRate.setStatus(
        "current"
    )

chkpntTrapBytesThroughput = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 5)
)
chkpntTrapBytesThroughput.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapBytesThroughput.setStatus(
        "current"
    )

chkpntTrapAcceptedPacketRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 6)
)
chkpntTrapAcceptedPacketRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapAcceptedPacketRate.setStatus(
        "current"
    )

chkpntTrapNetIfOperState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 7)
)
chkpntTrapNetIfOperState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfAddress"),
        ("CHECKPOINT-MIB", "svnNetIfOperState"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfOperState.setStatus(
        "current"
    )

chkpntTrapNetIfRXDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 8)
)
chkpntTrapNetIfRXDrop.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfState"),
        ("CHECKPOINT-MIB", "svnNetIfRXDrops"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfRXDrop.setStatus(
        "current"
    )

chkpntDiskSpaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 1)
)
chkpntDiskSpaceTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiDiskName"),
        ("CHECKPOINT-MIB", "multiDiskFreeAvailablePercent"))
)
if mibBuilder.loadTexts:
    chkpntDiskSpaceTrap.setStatus(
        "current"
    )

chkpntRAIDVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 2)
)
chkpntRAIDVolumeTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "raidVolumeID"),
        ("CHECKPOINT-MIB", "raidVolumeState"))
)
if mibBuilder.loadTexts:
    chkpntRAIDVolumeTrap.setStatus(
        "current"
    )

chkpntRAIDDiskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 3)
)
chkpntRAIDDiskTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "raidDiskVolumeID"),
        ("CHECKPOINT-MIB", "raidDiskID"),
        ("CHECKPOINT-MIB", "raidDiskState"))
)
if mibBuilder.loadTexts:
    chkpntRAIDDiskTrap.setStatus(
        "current"
    )

chkpntRAIDDiskFlagsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 4)
)
chkpntRAIDDiskFlagsTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "raidDiskVolumeID"),
        ("CHECKPOINT-MIB", "raidDiskID"),
        ("CHECKPOINT-MIB", "raidDiskState"),
        ("CHECKPOINT-MIB", "raidDiskFlags"))
)
if mibBuilder.loadTexts:
    chkpntRAIDDiskFlagsTrap.setStatus(
        "current"
    )

chkpntCPUCoreUtilTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3, 1)
)
chkpntCPUCoreUtilTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiProcIndex"),
        ("CHECKPOINT-MIB", "multiProcUserTime"),
        ("CHECKPOINT-MIB", "multiProcSystemTime"),
        ("CHECKPOINT-MIB", "multiProcIdleTime"),
        ("CHECKPOINT-MIB", "multiProcUsage"),
        ("CHECKPOINT-MIB", "multiProcRunQueue"),
        ("CHECKPOINT-MIB", "multiProcInterrupts"))
)
if mibBuilder.loadTexts:
    chkpntCPUCoreUtilTrap.setStatus(
        "current"
    )

chkpntCPUCoreInterruptsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3, 2)
)
chkpntCPUCoreInterruptsTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiProcIndex"),
        ("CHECKPOINT-MIB", "multiProcUserTime"),
        ("CHECKPOINT-MIB", "multiProcSystemTime"),
        ("CHECKPOINT-MIB", "multiProcIdleTime"),
        ("CHECKPOINT-MIB", "multiProcUsage"),
        ("CHECKPOINT-MIB", "multiProcRunQueue"),
        ("CHECKPOINT-MIB", "multiProcInterrupts"))
)
if mibBuilder.loadTexts:
    chkpntCPUCoreInterruptsTrap.setStatus(
        "current"
    )

chkpntSwapMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4, 1)
)
chkpntSwapMemoryTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "memTotalVirtual64"),
        ("CHECKPOINT-MIB", "memActiveVirtual64"))
)
if mibBuilder.loadTexts:
    chkpntSwapMemoryTrap.setStatus(
        "current"
    )

chkpntRealMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4, 2)
)
chkpntRealMemoryTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "memTotalReal64"),
        ("CHECKPOINT-MIB", "memActiveReal64"))
)
if mibBuilder.loadTexts:
    chkpntRealMemoryTrap.setStatus(
        "current"
    )

chkpntTempertureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 1, 1)
)
chkpntTempertureTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "tempertureSensorName"),
        ("CHECKPOINT-MIB", "tempertureSensorValue"),
        ("CHECKPOINT-MIB", "tempertureSensorUnit"),
        ("CHECKPOINT-MIB", "tempertureSensorType"),
        ("CHECKPOINT-MIB", "tempertureSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntTempertureTrap.setStatus(
        "current"
    )

chkpntFanSpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 2, 1)
)
chkpntFanSpeedTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fanSpeedSensorName"),
        ("CHECKPOINT-MIB", "fanSpeedSensorValue"),
        ("CHECKPOINT-MIB", "fanSpeedSensorUnit"),
        ("CHECKPOINT-MIB", "fanSpeedSensorType"),
        ("CHECKPOINT-MIB", "fanSpeedSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntFanSpeedTrap.setStatus(
        "current"
    )

chkpntVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 3, 1)
)
chkpntVoltageTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "voltageSensorName"),
        ("CHECKPOINT-MIB", "voltageSensorValue"),
        ("CHECKPOINT-MIB", "voltageSensorUnit"),
        ("CHECKPOINT-MIB", "voltageSensorType"),
        ("CHECKPOINT-MIB", "voltageSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntVoltageTrap.setStatus(
        "current"
    )

chkpntClusterMemberStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 1)
)
chkpntClusterMemberStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIdentifier"),
        ("CHECKPOINT-MIB", "haState"))
)
if mibBuilder.loadTexts:
    chkpntClusterMemberStateTrap.setStatus(
        "current"
    )

chkpntClusterBlockStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 2)
)
chkpntClusterBlockStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIdentifier"),
        ("CHECKPOINT-MIB", "haBlockState"),
        ("CHECKPOINT-MIB", "haState"))
)
if mibBuilder.loadTexts:
    chkpntClusterBlockStateTrap.setStatus(
        "current"
    )

chkpntClusterStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 3)
)
chkpntClusterStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIdentifier"),
        ("CHECKPOINT-MIB", "haBlockState"),
        ("CHECKPOINT-MIB", "haState"),
        ("CHECKPOINT-MIB", "haStatCode"),
        ("CHECKPOINT-MIB", "haStatShort"),
        ("CHECKPOINT-MIB", "haStatLong"))
)
if mibBuilder.loadTexts:
    chkpntClusterStateTrap.setStatus(
        "current"
    )

chkpntClusterProblemStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 4)
)
chkpntClusterProblemStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haProblemName"),
        ("CHECKPOINT-MIB", "haProblemStatus"),
        ("CHECKPOINT-MIB", "haProblemPriority"),
        ("CHECKPOINT-MIB", "haProblemVerified"),
        ("CHECKPOINT-MIB", "haProblemDescr"))
)
if mibBuilder.loadTexts:
    chkpntClusterProblemStateTrap.setStatus(
        "current"
    )

chkpntClusterInterfaceStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 5)
)
chkpntClusterInterfaceStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIfName"),
        ("CHECKPOINT-MIB", "haIP"),
        ("CHECKPOINT-MIB", "haStatus"),
        ("CHECKPOINT-MIB", "haTrusted"),
        ("CHECKPOINT-MIB", "haShared"))
)
if mibBuilder.loadTexts:
    chkpntClusterInterfaceStateTrap.setStatus(
        "current"
    )

chkpntClusterXLFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 6)
)
chkpntClusterXLFailoverTrap.setObjects(
    ("CHECKPOINT-MIB", "haClusterXLFailover")
)
if mibBuilder.loadTexts:
    chkpntClusterXLFailoverTrap.setStatus(
        "current"
    )

chkpntTrapLSConnState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 1)
)
chkpntTrapLSConnState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fwLSConnName"),
        ("CHECKPOINT-MIB", "fwLSConnState"),
        ("CHECKPOINT-MIB", "fwLSConnStateDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
)
if mibBuilder.loadTexts:
    chkpntTrapLSConnState.setStatus(
        "current"
    )

chkpntTrapOverallLSConnState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 2)
)
chkpntTrapOverallLSConnState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fwLSConnOverall"),
        ("CHECKPOINT-MIB", "fwLSConnOverallDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
)
if mibBuilder.loadTexts:
    chkpntTrapOverallLSConnState.setStatus(
        "current"
    )

chkpntTrapLocalLoggingState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 3)
)
chkpntTrapLocalLoggingState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fwLSConnOverall"),
        ("CHECKPOINT-MIB", "fwLSConnOverallDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
)
if mibBuilder.loadTexts:
    chkpntTrapLocalLoggingState.setStatus(
        "current"
    )

asgChassisStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 1, 1)
)
asgChassisStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgChassisStateTrap.setStatus(
        "current"
    )

asgBladeStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 1, 2)
)
asgBladeStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgBladeStateTrap.setStatus(
        "current"
    )

asgClusterProblemStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 1, 3)
)
asgClusterProblemStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapCategory"),
        ("CHECKPOINT-MIB", "haProblemName"),
        ("CHECKPOINT-MIB", "haProblemStatus"),
        ("CHECKPOINT-MIB", "haProblemPriority"),
        ("CHECKPOINT-MIB", "haProblemVerified"),
        ("CHECKPOINT-MIB", "haProblemDescr"))
)
if mibBuilder.loadTexts:
    asgClusterProblemStateTrap.setStatus(
        "current"
    )

asgMonitorStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 1, 5)
)
asgMonitorStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgMonitorStateTrap.setStatus(
        "current"
    )

asgTrapNetIfState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 2, 1)
)
asgTrapNetIfState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapCategory"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-MIB", "asgNetIfName"))
)
if mibBuilder.loadTexts:
    asgTrapNetIfState.setStatus(
        "current"
    )

asgTrapNetAdminState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 2, 2)
)
asgTrapNetAdminState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapCategory"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-MIB", "asgNetIfName"))
)
if mibBuilder.loadTexts:
    asgTrapNetAdminState.setStatus(
        "current"
    )

asgDiskSpaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 3, 1)
)
asgDiskSpaceTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgDiskSpaceTrap.setStatus(
        "current"
    )

asgRAIDVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 3, 2)
)
asgRAIDVolumeTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapCategory"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-MIB", "raidVolumeID"),
        ("CHECKPOINT-MIB", "raidVolumeState"))
)
if mibBuilder.loadTexts:
    asgRAIDVolumeTrap.setStatus(
        "current"
    )

asgRAIDDiskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 3, 3)
)
asgRAIDDiskTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapCategory"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-MIB", "raidDiskVolumeID"),
        ("CHECKPOINT-MIB", "raidDiskID"),
        ("CHECKPOINT-MIB", "raidDiskState"))
)
if mibBuilder.loadTexts:
    asgRAIDDiskTrap.setStatus(
        "current"
    )

asgCPUCoreUtilTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 4, 1)
)
asgCPUCoreUtilTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgCPUCoreUtilTrap.setStatus(
        "current"
    )

asgCPUCoreInterruptsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 4, 2)
)
asgCPUCoreInterruptsTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapCategory"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-MIB", "multiProcIndex"),
        ("CHECKPOINT-MIB", "multiProcUserTime"),
        ("CHECKPOINT-MIB", "multiProcSystemTime"),
        ("CHECKPOINT-MIB", "multiProcIdleTime"),
        ("CHECKPOINT-MIB", "multiProcUsage"),
        ("CHECKPOINT-MIB", "multiProcRunQueue"),
        ("CHECKPOINT-MIB", "multiProcInterrupts"))
)
if mibBuilder.loadTexts:
    asgCPUCoreInterruptsTrap.setStatus(
        "current"
    )

asgSwapMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 5, 1)
)
asgSwapMemoryTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"))
)
if mibBuilder.loadTexts:
    asgSwapMemoryTrap.setStatus(
        "current"
    )

asgRealMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 5, 2)
)
asgRealMemoryTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgRealMemoryTrap.setStatus(
        "current"
    )

asgTempertureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 1, 1)
)
asgTempertureTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTempertureTrap.setStatus(
        "current"
    )

asgTempertureSensorStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 1, 2)
)
asgTempertureSensorStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTempertureSensorStateTrap.setStatus(
        "current"
    )

asgFanSpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 2, 1)
)
asgFanSpeedTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgFanSpeedTrap.setStatus(
        "current"
    )

asgFanSpeedSensorStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 2, 2)
)
asgFanSpeedSensorStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgFanSpeedSensorStateTrap.setStatus(
        "current"
    )

asgVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 3, 1)
)
asgVoltageTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgVoltageTrap.setStatus(
        "current"
    )

asgVoltageSensorStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 3, 2)
)
asgVoltageSensorStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgVoltageSensorStateTrap.setStatus(
        "current"
    )

asgSSMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 4, 1)
)
asgSSMTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgSSMTrap.setStatus(
        "current"
    )

asgSSMPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 4, 2)
)
asgSSMPortTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgSSMPortTrap.setStatus(
        "current"
    )

asgCMMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 7, 5, 1)
)
asgCMMTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgCMMTrap.setStatus(
        "current"
    )

asgTrapConnRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 1)
)
asgTrapConnRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapConnRate.setStatus(
        "current"
    )

asgTrapConcurrentConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 2)
)
asgTrapConcurrentConn.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapConcurrentConn.setStatus(
        "current"
    )

asgTrapConcurrentConnectionsTotal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 3)
)
asgTrapConcurrentConnectionsTotal.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapConcurrentConnectionsTotal.setStatus(
        "current"
    )

asgTrapConnRateTotal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 4)
)
asgTrapConnRateTotal.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapConnRateTotal.setStatus(
        "current"
    )

asgTrapThroughput = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 5)
)
asgTrapThroughput.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapThroughput.setStatus(
        "current"
    )

asgTrapThroughputTotal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 6)
)
asgTrapThroughputTotal.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapThroughputTotal.setStatus(
        "current"
    )

asgTrapPacketRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 7)
)
asgTrapPacketRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapPacketRate.setStatus(
        "current"
    )

asgTrapPacketRateTotal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 8, 8)
)
asgTrapPacketRateTotal.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapPacketRateTotal.setStatus(
        "current"
    )

asgRouteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10, 1)
)
asgRouteTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgRouteTrap.setStatus(
        "current"
    )

asgDiagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10, 2)
)
asgDiagTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgDiagTrap.setStatus(
        "current"
    )

asgPingableHostsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10, 3)
)
asgPingableHostsTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgPingableHostsTrap.setStatus(
        "current"
    )

asgMemoryLeakDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10, 4)
)
asgMemoryLeakDetectTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgMemoryLeakDetectTrap.setStatus(
        "current"
    )

asgTrapSynatk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10, 5)
)
asgTrapSynatk.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgTrapSynatk.setStatus(
        "current"
    )

asgLspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2001, 10, 6)
)
asgLspTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "asgTrapChassisId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapBladeId"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapPriority"))
)
if mibBuilder.loadTexts:
    asgLspTrap.setStatus(
        "current"
    )


# Notifications groups

chkpntNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2620, 2, 3, 1)
)
chkpntNotificationGroup.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntDiskSpaceTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntRAIDVolumeTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntRAIDDiskTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntRAIDDiskFlagsTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNetIfState"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNetIfUnplugged"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNetIfOperState"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNetIfRXDrop"),
        ("CHECKPOINT-TRAP-MIB", "chkpntCPUCoreInterruptsTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntSwapMemoryTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntCPUCoreUtilTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntRealMemoryTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTempertureTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntFanSpeedTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntVoltageTrap"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNewConnRate"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapConcurrentConnRate"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapBytesThroughput"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapAcceptedPacketRate"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNetIfOperState"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapNetIfRXDrop"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapNetIfState"),
        ("CHECKPOINT-TRAP-MIB", "asgTrapNetAdminState"))
)
if mibBuilder.loadTexts:
    chkpntNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

chkpntTrapBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2620, 2, 1, 1)
)
chkpntTrapBasicCompliance.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapGroup"),
        ("CHECKPOINT-TRAP-MIB", "chkpntNotificationGroup"))
)
if mibBuilder.loadTexts:
    chkpntTrapBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHECKPOINT-TRAP-MIB",
    **{"checkpoint": checkpoint,
       "products": products,
       "chkpntTrap": chkpntTrap,
       "chkpntTrapInfo": chkpntTrapInfo,
       "chkpntTrapMibModule": chkpntTrapMibModule,
       "chkpntTrapOID": chkpntTrapOID,
       "chkpntTrapOIDValue": chkpntTrapOIDValue,
       "chkpntTrapMsgText": chkpntTrapMsgText,
       "chkpntTrapSeverity": chkpntTrapSeverity,
       "chkpntTrapCategory": chkpntTrapCategory,
       "chkpntTrapChassisId": chkpntTrapChassisId,
       "chkpntTrapBladeId": chkpntTrapBladeId,
       "multiDiskName": multiDiskName,
       "multiDiskFreeAvailablePercent": multiDiskFreeAvailablePercent,
       "raidVolumeID": raidVolumeID,
       "raidVolumeState": raidVolumeState,
       "raidDiskVolumeID": raidDiskVolumeID,
       "raidDiskID": raidDiskID,
       "raidDiskState": raidDiskState,
       "raidDiskFlags": raidDiskFlags,
       "multiProcIndex": multiProcIndex,
       "multiProcUserTime": multiProcUserTime,
       "multiProcSystemTime": multiProcSystemTime,
       "multiProcIdleTime": multiProcIdleTime,
       "multiProcUsage": multiProcUsage,
       "multiProcRunQueue": multiProcRunQueue,
       "multiProcInterrupts": multiProcInterrupts,
       "memTotalVirtual64": memTotalVirtual64,
       "memActiveVirtual64": memActiveVirtual64,
       "memTotalReal64": memTotalReal64,
       "memActiveReal64": memActiveReal64,
       "tempertureSensorName": tempertureSensorName,
       "tempertureSensorValue": tempertureSensorValue,
       "tempertureSensorUnit": tempertureSensorUnit,
       "tempertureSensorType": tempertureSensorType,
       "tempertureSensorStatus": tempertureSensorStatus,
       "fanSpeedSensorName": fanSpeedSensorName,
       "fanSpeedSensorValue": fanSpeedSensorValue,
       "fanSpeedSensorUnit": fanSpeedSensorUnit,
       "fanSpeedSensorType": fanSpeedSensorType,
       "fanSpeedSensorStatus": fanSpeedSensorStatus,
       "voltageSensorName": voltageSensorName,
       "voltageSensorValue": voltageSensorValue,
       "voltageSensorUnit": voltageSensorUnit,
       "voltageSensorType": voltageSensorType,
       "voltageSensorStatus": voltageSensorStatus,
       "chkpntTrapNet": chkpntTrapNet,
       "chkpntTrapNetIfState": chkpntTrapNetIfState,
       "chkpntTrapNetIfUnplugged": chkpntTrapNetIfUnplugged,
       "chkpntTrapNewConnRate": chkpntTrapNewConnRate,
       "chkpntTrapConcurrentConnRate": chkpntTrapConcurrentConnRate,
       "chkpntTrapBytesThroughput": chkpntTrapBytesThroughput,
       "chkpntTrapAcceptedPacketRate": chkpntTrapAcceptedPacketRate,
       "chkpntTrapNetIfOperState": chkpntTrapNetIfOperState,
       "chkpntTrapNetIfRXDrop": chkpntTrapNetIfRXDrop,
       "chkpntTrapDisk": chkpntTrapDisk,
       "chkpntDiskSpaceTrap": chkpntDiskSpaceTrap,
       "chkpntRAIDVolumeTrap": chkpntRAIDVolumeTrap,
       "chkpntRAIDDiskTrap": chkpntRAIDDiskTrap,
       "chkpntRAIDDiskFlagsTrap": chkpntRAIDDiskFlagsTrap,
       "chkpntTrapCPU": chkpntTrapCPU,
       "chkpntCPUCoreUtilTrap": chkpntCPUCoreUtilTrap,
       "chkpntCPUCoreInterruptsTrap": chkpntCPUCoreInterruptsTrap,
       "chkpntTrapMemory": chkpntTrapMemory,
       "chkpntSwapMemoryTrap": chkpntSwapMemoryTrap,
       "chkpntRealMemoryTrap": chkpntRealMemoryTrap,
       "chkpntTrapHWSensor": chkpntTrapHWSensor,
       "chkpntTrapTempertureSensor": chkpntTrapTempertureSensor,
       "chkpntTempertureTrap": chkpntTempertureTrap,
       "chkpntTrapFanSpeedSensor": chkpntTrapFanSpeedSensor,
       "chkpntFanSpeedTrap": chkpntFanSpeedTrap,
       "chkpntTrapVoltageSensor": chkpntTrapVoltageSensor,
       "chkpntVoltageTrap": chkpntVoltageTrap,
       "chkpntTrapHA": chkpntTrapHA,
       "chkpntClusterMemberStateTrap": chkpntClusterMemberStateTrap,
       "chkpntClusterBlockStateTrap": chkpntClusterBlockStateTrap,
       "chkpntClusterStateTrap": chkpntClusterStateTrap,
       "chkpntClusterProblemStateTrap": chkpntClusterProblemStateTrap,
       "chkpntClusterInterfaceStateTrap": chkpntClusterInterfaceStateTrap,
       "chkpntClusterXLFailoverTrap": chkpntClusterXLFailoverTrap,
       "chkpntTrapLSConn": chkpntTrapLSConn,
       "chkpntTrapLSConnState": chkpntTrapLSConnState,
       "chkpntTrapOverallLSConnState": chkpntTrapOverallLSConnState,
       "chkpntTrapLocalLoggingState": chkpntTrapLocalLoggingState,
       "asgTrap": asgTrap,
       "asgTrapInfo": asgTrapInfo,
       "asgTrapChassisId": asgTrapChassisId,
       "asgTrapBladeId": asgTrapBladeId,
       "asgTrapMsgText": asgTrapMsgText,
       "asgTrapPriority": asgTrapPriority,
       "asgTrapOID": asgTrapOID,
       "asgTrapOIDValue": asgTrapOIDValue,
       "asgTrapSN": asgTrapSN,
       "asgCoreId": asgCoreId,
       "asgTrapCategory": asgTrapCategory,
       "asgTrapHA": asgTrapHA,
       "asgChassisStateTrap": asgChassisStateTrap,
       "asgBladeStateTrap": asgBladeStateTrap,
       "asgClusterProblemStateTrap": asgClusterProblemStateTrap,
       "asgMonitorStateTrap": asgMonitorStateTrap,
       "asgTrapNet": asgTrapNet,
       "asgTrapNetIfState": asgTrapNetIfState,
       "asgTrapNetAdminState": asgTrapNetAdminState,
       "asgTrapDisk": asgTrapDisk,
       "asgDiskSpaceTrap": asgDiskSpaceTrap,
       "asgRAIDVolumeTrap": asgRAIDVolumeTrap,
       "asgRAIDDiskTrap": asgRAIDDiskTrap,
       "asgTrapCPU": asgTrapCPU,
       "asgCPUCoreUtilTrap": asgCPUCoreUtilTrap,
       "asgCPUCoreInterruptsTrap": asgCPUCoreInterruptsTrap,
       "asgTrapMemory": asgTrapMemory,
       "asgSwapMemoryTrap": asgSwapMemoryTrap,
       "asgRealMemoryTrap": asgRealMemoryTrap,
       "asgTrapCplic": asgTrapCplic,
       "asgTrapHWSensor": asgTrapHWSensor,
       "asgTrapTempertureSensor": asgTrapTempertureSensor,
       "asgTempertureTrap": asgTempertureTrap,
       "asgTempertureSensorStateTrap": asgTempertureSensorStateTrap,
       "asgTrapFanSpeedSensor": asgTrapFanSpeedSensor,
       "asgFanSpeedTrap": asgFanSpeedTrap,
       "asgFanSpeedSensorStateTrap": asgFanSpeedSensorStateTrap,
       "asgTrapVoltageSensor": asgTrapVoltageSensor,
       "asgVoltageTrap": asgVoltageTrap,
       "asgVoltageSensorStateTrap": asgVoltageSensorStateTrap,
       "asgTrapSSMSensor": asgTrapSSMSensor,
       "asgSSMTrap": asgSSMTrap,
       "asgSSMPortTrap": asgSSMPortTrap,
       "asgTrapCMMSensor": asgTrapCMMSensor,
       "asgCMMTrap": asgCMMTrap,
       "asgTrapPerf": asgTrapPerf,
       "asgTrapConnRate": asgTrapConnRate,
       "asgTrapConcurrentConn": asgTrapConcurrentConn,
       "asgTrapConcurrentConnectionsTotal": asgTrapConcurrentConnectionsTotal,
       "asgTrapConnRateTotal": asgTrapConnRateTotal,
       "asgTrapThroughput": asgTrapThroughput,
       "asgTrapThroughputTotal": asgTrapThroughputTotal,
       "asgTrapPacketRate": asgTrapPacketRate,
       "asgTrapPacketRateTotal": asgTrapPacketRateTotal,
       "asgTrapGeneral": asgTrapGeneral,
       "asgRouteTrap": asgRouteTrap,
       "asgDiagTrap": asgDiagTrap,
       "asgPingableHostsTrap": asgPingableHostsTrap,
       "asgMemoryLeakDetectTrap": asgMemoryLeakDetectTrap,
       "asgTrapSynatk": asgTrapSynatk,
       "asgLspTrap": asgLspTrap,
       "chkpntTrapMIBConformance": chkpntTrapMIBConformance,
       "chkpntTrapMIBCompliances": chkpntTrapMIBCompliances,
       "chkpntTrapBasicCompliance": chkpntTrapBasicCompliance,
       "chkpntTrapMIBGroups": chkpntTrapMIBGroups,
       "chkpntTrapGroup": chkpntTrapGroup,
       "chkpntNotificationGroups": chkpntNotificationGroups,
       "chkpntNotificationGroup": chkpntNotificationGroup}
)
