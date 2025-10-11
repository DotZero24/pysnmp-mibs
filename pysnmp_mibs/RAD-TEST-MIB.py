# SNMP MIB module (RAD-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:01 2025
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

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(systems,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "systems")

(RadTestPbitValues,
 RadTestResult) = mibBuilder.importSymbols(
    "RAD-TC",
    "RadTestPbitValues",
    "RadTestResult")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

radTest = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadTestPerfRepFrameSize(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("s64", 0),
          ("s128", 1),
          ("s256", 2),
          ("s512", 3),
          ("s1024", 4),
          ("s1280", 5),
          ("s1518", 6),
          ("s1700", 7),
          ("s1900", 8),
          ("s2000", 9),
          ("s2048", 10),
          ("s4096", 11),
          ("s9600", 12),
          ("custom", 13))
    )


class RadTestPerfresultFrameSize(TextualConvention, Integer32):
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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("s64", 1),
          ("s128", 2),
          ("s256", 3),
          ("s512", 4),
          ("s1024", 5),
          ("s1280", 6),
          ("s1518", 7),
          ("s1700", 8),
          ("s1900", 9),
          ("s2000", 10),
          ("s2048", 11),
          ("s4096", 12),
          ("s9600", 13),
          ("custom", 14))
    )



class RadTestPbitIndex(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("pbit0", 0),
          ("pbit1", 1),
          ("pbit2", 2),
          ("pbit3", 3),
          ("pbit4", 4),
          ("pbit5", 5),
          ("pbit6", 6),
          ("pbit7", 7))
    )



# MIB Managed Objects in the order of their OIDs

_RadTestPrefRepEvents_ObjectIdentity = ObjectIdentity
radTestPrefRepEvents = _RadTestPrefRepEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0)
)
_RadTestPrefRepProfile_ObjectIdentity = ObjectIdentity
radTestPrefRepProfile = _RadTestPrefRepProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1)
)
_TstNePerfRepProfileTable_Object = MibTable
tstNePerfRepProfileTable = _TstNePerfRepProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    tstNePerfRepProfileTable.setStatus("current")
_TstNePerfRepProfileEntry_Object = MibTableRow
tstNePerfRepProfileEntry = _TstNePerfRepProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1)
)
tstNePerfRepProfileEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepProfileId"),
)
if mibBuilder.loadTexts:
    tstNePerfRepProfileEntry.setStatus("current")
_TstNePerfRepProfileId_Type = Unsigned32
_TstNePerfRepProfileId_Object = MibTableColumn
tstNePerfRepProfileId = _TstNePerfRepProfileId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 1),
    _TstNePerfRepProfileId_Type()
)
tstNePerfRepProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tstNePerfRepProfileId.setStatus("current")
_TstNePerfRepProfileName_Type = SnmpAdminString
_TstNePerfRepProfileName_Object = MibTableColumn
tstNePerfRepProfileName = _TstNePerfRepProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 2),
    _TstNePerfRepProfileName_Type()
)
tstNePerfRepProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileName.setStatus("current")
_TstNePerfRepProfileRowStatus_Type = RowStatus
_TstNePerfRepProfileRowStatus_Object = MibTableColumn
tstNePerfRepProfileRowStatus = _TstNePerfRepProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 3),
    _TstNePerfRepProfileRowStatus_Type()
)
tstNePerfRepProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileRowStatus.setStatus("current")
_TstNePerfRepProfileFrameSize_Type = RadTestPerfRepFrameSize
_TstNePerfRepProfileFrameSize_Object = MibTableColumn
tstNePerfRepProfileFrameSize = _TstNePerfRepProfileFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 4),
    _TstNePerfRepProfileFrameSize_Type()
)
tstNePerfRepProfileFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileFrameSize.setStatus("current")


class _TstNePerfRepProfilePattern_Type(Integer32):
    """Custom type tstNePerfRepProfilePattern based on Integer32"""
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
        *(("notApplicable", 1),
          ("allOnes", 2),
          ("allZerosWithoutCrc", 3),
          ("allZerosWithCrc", 4),
          ("alternate", 5),
          ("prbsWithCrc", 6),
          ("prbsWithoutCrc", 7))
    )


_TstNePerfRepProfilePattern_Type.__name__ = "Integer32"
_TstNePerfRepProfilePattern_Object = MibTableColumn
tstNePerfRepProfilePattern = _TstNePerfRepProfilePattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 5),
    _TstNePerfRepProfilePattern_Type()
)
tstNePerfRepProfilePattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfilePattern.setStatus("current")


class _TstNePerfRepProfileDirection_Type(Integer32):
    """Custom type tstNePerfRepProfileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("uniDirectional", 2),
          ("biDirectional", 3))
    )


_TstNePerfRepProfileDirection_Type.__name__ = "Integer32"
_TstNePerfRepProfileDirection_Object = MibTableColumn
tstNePerfRepProfileDirection = _TstNePerfRepProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 6),
    _TstNePerfRepProfileDirection_Type()
)
tstNePerfRepProfileDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileDirection.setStatus("current")


class _TstNePerfRepProfileTlv_Type(Integer32):
    """Custom type tstNePerfRepProfileTlv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("test", 1),
          ("data", 2))
    )


_TstNePerfRepProfileTlv_Type.__name__ = "Integer32"
_TstNePerfRepProfileTlv_Object = MibTableColumn
tstNePerfRepProfileTlv = _TstNePerfRepProfileTlv_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 7),
    _TstNePerfRepProfileTlv_Type()
)
tstNePerfRepProfileTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileTlv.setStatus("current")
_TstNePerfRepProfileNumberOfFramesInOneBurst_Type = Unsigned32
_TstNePerfRepProfileNumberOfFramesInOneBurst_Object = MibTableColumn
tstNePerfRepProfileNumberOfFramesInOneBurst = _TstNePerfRepProfileNumberOfFramesInOneBurst_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 8),
    _TstNePerfRepProfileNumberOfFramesInOneBurst_Type()
)
tstNePerfRepProfileNumberOfFramesInOneBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileNumberOfFramesInOneBurst.setStatus("current")
_TstNePerfRepProfileFrameLossTolerance_Type = Unsigned32
_TstNePerfRepProfileFrameLossTolerance_Object = MibTableColumn
tstNePerfRepProfileFrameLossTolerance = _TstNePerfRepProfileFrameLossTolerance_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 9),
    _TstNePerfRepProfileFrameLossTolerance_Type()
)
tstNePerfRepProfileFrameLossTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileFrameLossTolerance.setStatus("current")
_TstNePerfRepProfileBinarySearchResolution_Type = Unsigned32
_TstNePerfRepProfileBinarySearchResolution_Object = MibTableColumn
tstNePerfRepProfileBinarySearchResolution = _TstNePerfRepProfileBinarySearchResolution_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 10),
    _TstNePerfRepProfileBinarySearchResolution_Type()
)
tstNePerfRepProfileBinarySearchResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileBinarySearchResolution.setStatus("current")
_TstNePerfRepProfileNumberOfTrials_Type = Unsigned32
_TstNePerfRepProfileNumberOfTrials_Object = MibTableColumn
tstNePerfRepProfileNumberOfTrials = _TstNePerfRepProfileNumberOfTrials_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 11),
    _TstNePerfRepProfileNumberOfTrials_Type()
)
tstNePerfRepProfileNumberOfTrials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileNumberOfTrials.setStatus("current")


class _TstNePerfRepProfileLearningFramesMode_Type(Integer32):
    """Custom type tstNePerfRepProfileLearningFramesMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("once", 3),
          ("oncePerTrial", 4))
    )


_TstNePerfRepProfileLearningFramesMode_Type.__name__ = "Integer32"
_TstNePerfRepProfileLearningFramesMode_Object = MibTableColumn
tstNePerfRepProfileLearningFramesMode = _TstNePerfRepProfileLearningFramesMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 12),
    _TstNePerfRepProfileLearningFramesMode_Type()
)
tstNePerfRepProfileLearningFramesMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileLearningFramesMode.setStatus("current")
_TstNePerfRepProfileLearningFrames_Type = Unsigned32
_TstNePerfRepProfileLearningFrames_Object = MibTableColumn
tstNePerfRepProfileLearningFrames = _TstNePerfRepProfileLearningFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 13),
    _TstNePerfRepProfileLearningFrames_Type()
)
tstNePerfRepProfileLearningFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileLearningFrames.setStatus("current")
_TstNePerfRepProfileCustomSize_Type = Unsigned32
_TstNePerfRepProfileCustomSize_Object = MibTableColumn
tstNePerfRepProfileCustomSize = _TstNePerfRepProfileCustomSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 14),
    _TstNePerfRepProfileCustomSize_Type()
)
tstNePerfRepProfileCustomSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileCustomSize.setStatus("current")


class _TstNePerfRepProfileTransmitLck_Type(TruthValue):
    """Custom type tstNePerfRepProfileTransmitLck based on TruthValue"""
    defaultValue = 1


_TstNePerfRepProfileTransmitLck_Type.__name__ = "TruthValue"
_TstNePerfRepProfileTransmitLck_Object = MibTableColumn
tstNePerfRepProfileTransmitLck = _TstNePerfRepProfileTransmitLck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 1, 1, 15),
    _TstNePerfRepProfileTransmitLck_Type()
)
tstNePerfRepProfileTransmitLck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepProfileTransmitLck.setStatus("current")
_TstMepFlowTable_Object = MibTable
tstMepFlowTable = _TstMepFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    tstMepFlowTable.setStatus("current")
_TstMepFlowEntry_Object = MibTableRow
tstMepFlowEntry = _TstMepFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 2, 1)
)
tstMepFlowEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAD-TEST-MIB", "tstMepFlowIndex"),
)
if mibBuilder.loadTexts:
    tstMepFlowEntry.setStatus("current")
_TstMepFlowIndex_Type = Unsigned32
_TstMepFlowIndex_Object = MibTableColumn
tstMepFlowIndex = _TstMepFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 2, 1, 1),
    _TstMepFlowIndex_Type()
)
tstMepFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tstMepFlowIndex.setStatus("current")
_TstMepFlowFlowIdx_Type = RowPointer
_TstMepFlowFlowIdx_Object = MibTableColumn
tstMepFlowFlowIdx = _TstMepFlowFlowIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 2, 1, 2),
    _TstMepFlowFlowIdx_Type()
)
tstMepFlowFlowIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstMepFlowFlowIdx.setStatus("current")
_ItuSatProfileTable_Object = MibTable
ituSatProfileTable = _ItuSatProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3)
)
if mibBuilder.loadTexts:
    ituSatProfileTable.setStatus("current")
_ItuSatProfileEntry_Object = MibTableRow
ituSatProfileEntry = _ItuSatProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1)
)
ituSatProfileEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatProfileIndex"),
)
if mibBuilder.loadTexts:
    ituSatProfileEntry.setStatus("current")
_ItuSatProfileIndex_Type = Unsigned32
_ItuSatProfileIndex_Object = MibTableColumn
ituSatProfileIndex = _ItuSatProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 1),
    _ItuSatProfileIndex_Type()
)
ituSatProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatProfileIndex.setStatus("current")


class _ItuSatProfileName_Type(SnmpAdminString):
    """Custom type ituSatProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ItuSatProfileName_Type.__name__ = "SnmpAdminString"
_ItuSatProfileName_Object = MibTableColumn
ituSatProfileName = _ItuSatProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 2),
    _ItuSatProfileName_Type()
)
ituSatProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileName.setStatus("current")
_ItuSatProfileRowStatus_Type = RowStatus
_ItuSatProfileRowStatus_Object = MibTableColumn
ituSatProfileRowStatus = _ItuSatProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 3),
    _ItuSatProfileRowStatus_Type()
)
ituSatProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileRowStatus.setStatus("current")


class _ItuSatProfileEtherType_Type(OctetString):
    """Custom type ituSatProfileEtherType based on OctetString"""
    defaultHexValue = "22E8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ItuSatProfileEtherType_Type.__name__ = "OctetString"
_ItuSatProfileEtherType_Object = MibTableColumn
ituSatProfileEtherType = _ItuSatProfileEtherType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 4),
    _ItuSatProfileEtherType_Type()
)
ituSatProfileEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileEtherType.setStatus("current")


class _ItuSatProfileFrameSize_Type(Unsigned32):
    """Custom type ituSatProfileFrameSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12000),
    )


_ItuSatProfileFrameSize_Type.__name__ = "Unsigned32"
_ItuSatProfileFrameSize_Object = MibTableColumn
ituSatProfileFrameSize = _ItuSatProfileFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 5),
    _ItuSatProfileFrameSize_Type()
)
ituSatProfileFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileFrameSize.setUnits("bytes")


class _ItuSatProfileUniFlrThreshold_Type(Unsigned32):
    """Custom type ituSatProfileUniFlrThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfileUniFlrThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileUniFlrThreshold_Object = MibTableColumn
ituSatProfileUniFlrThreshold = _ItuSatProfileUniFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 6),
    _ItuSatProfileUniFlrThreshold_Type()
)
ituSatProfileUniFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileUniFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileUniFlrThreshold.setUnits("ppm")


class _ItuSatProfileUniFtdThreshold_Type(Unsigned32):
    """Custom type ituSatProfileUniFtdThreshold based on Unsigned32"""
    defaultValue = 13000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfileUniFtdThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileUniFtdThreshold_Object = MibTableColumn
ituSatProfileUniFtdThreshold = _ItuSatProfileUniFtdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 7),
    _ItuSatProfileUniFtdThreshold_Type()
)
ituSatProfileUniFtdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileUniFtdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileUniFtdThreshold.setUnits("micro seconds")


class _ItuSatProfileUniFdvThreshold_Type(Unsigned32):
    """Custom type ituSatProfileUniFdvThreshold based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfileUniFdvThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileUniFdvThreshold_Object = MibTableColumn
ituSatProfileUniFdvThreshold = _ItuSatProfileUniFdvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 8),
    _ItuSatProfileUniFdvThreshold_Type()
)
ituSatProfileUniFdvThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileUniFdvThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileUniFdvThreshold.setUnits("micro seconds")


class _ItuSatProfileUniAvailThreshold_Type(Unsigned32):
    """Custom type ituSatProfileUniAvailThreshold based on Unsigned32"""
    defaultValue = 9990

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ItuSatProfileUniAvailThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileUniAvailThreshold_Object = MibTableColumn
ituSatProfileUniAvailThreshold = _ItuSatProfileUniAvailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 9),
    _ItuSatProfileUniAvailThreshold_Type()
)
ituSatProfileUniAvailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileUniAvailThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileUniAvailThreshold.setUnits("hundredth of percent")


class _ItuSatProfileBiFlrThreshold_Type(Unsigned32):
    """Custom type ituSatProfileBiFlrThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfileBiFlrThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileBiFlrThreshold_Object = MibTableColumn
ituSatProfileBiFlrThreshold = _ItuSatProfileBiFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 10),
    _ItuSatProfileBiFlrThreshold_Type()
)
ituSatProfileBiFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileBiFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileBiFlrThreshold.setUnits("ppm")


class _ItuSatProfileBiFtdThreshold_Type(Unsigned32):
    """Custom type ituSatProfileBiFtdThreshold based on Unsigned32"""
    defaultValue = 26000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfileBiFtdThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileBiFtdThreshold_Object = MibTableColumn
ituSatProfileBiFtdThreshold = _ItuSatProfileBiFtdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 11),
    _ItuSatProfileBiFtdThreshold_Type()
)
ituSatProfileBiFtdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileBiFtdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileBiFtdThreshold.setUnits("micro seconds")


class _ItuSatProfileBiFdvThreshold_Type(Unsigned32):
    """Custom type ituSatProfileBiFdvThreshold based on Unsigned32"""
    defaultValue = 11000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfileBiFdvThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileBiFdvThreshold_Object = MibTableColumn
ituSatProfileBiFdvThreshold = _ItuSatProfileBiFdvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 12),
    _ItuSatProfileBiFdvThreshold_Type()
)
ituSatProfileBiFdvThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileBiFdvThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileBiFdvThreshold.setUnits("micro seconds")


class _ItuSatProfileBiAvailThreshold_Type(Unsigned32):
    """Custom type ituSatProfileBiAvailThreshold based on Unsigned32"""
    defaultValue = 9990

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ItuSatProfileBiAvailThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfileBiAvailThreshold_Object = MibTableColumn
ituSatProfileBiAvailThreshold = _ItuSatProfileBiAvailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 13),
    _ItuSatProfileBiAvailThreshold_Type()
)
ituSatProfileBiAvailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileBiAvailThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileBiAvailThreshold.setUnits("hundredth of percent")


class _ItuSatProfileScope_Type(Bits):
    """Custom type ituSatProfileScope based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("configuration", 0),
          ("performance", 1))
    )

_ItuSatProfileScope_Type.__name__ = "Bits"
_ItuSatProfileScope_Object = MibTableColumn
ituSatProfileScope = _ItuSatProfileScope_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 14),
    _ItuSatProfileScope_Type()
)
ituSatProfileScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileScope.setStatus("current")


class _ItuSatProfileDirection_Type(Integer32):
    """Custom type ituSatProfileDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_ItuSatProfileDirection_Type.__name__ = "Integer32"
_ItuSatProfileDirection_Object = MibTableColumn
ituSatProfileDirection = _ItuSatProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 15),
    _ItuSatProfileDirection_Type()
)
ituSatProfileDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileDirection.setStatus("current")


class _ItuSatProfileColorMode_Type(Integer32):
    """Custom type ituSatProfileColorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )


_ItuSatProfileColorMode_Type.__name__ = "Integer32"
_ItuSatProfileColorMode_Object = MibTableColumn
ituSatProfileColorMode = _ItuSatProfileColorMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 16),
    _ItuSatProfileColorMode_Type()
)
ituSatProfileColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileColorMode.setStatus("current")


class _ItuSatProfileTrafficPolicing_Type(Integer32):
    """Custom type ituSatProfileTrafficPolicing based on Integer32"""
    defaultValue = 1

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


_ItuSatProfileTrafficPolicing_Type.__name__ = "Integer32"
_ItuSatProfileTrafficPolicing_Object = MibTableColumn
ituSatProfileTrafficPolicing = _ItuSatProfileTrafficPolicing_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 17),
    _ItuSatProfileTrafficPolicing_Type()
)
ituSatProfileTrafficPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileTrafficPolicing.setStatus("current")


class _ItuSatProfileCirSteps_Type(OctetString):
    """Custom type ituSatProfileCirSteps based on OctetString"""
    defaultHexValue = "19324B64"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ItuSatProfileCirSteps_Type.__name__ = "OctetString"
_ItuSatProfileCirSteps_Object = MibTableColumn
ituSatProfileCirSteps = _ItuSatProfileCirSteps_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 18),
    _ItuSatProfileCirSteps_Type()
)
ituSatProfileCirSteps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileCirSteps.setStatus("current")


class _ItuSatProfileConfDuration_Type(Unsigned32):
    """Custom type ituSatProfileConfDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 360),
    )


_ItuSatProfileConfDuration_Type.__name__ = "Unsigned32"
_ItuSatProfileConfDuration_Object = MibTableColumn
ituSatProfileConfDuration = _ItuSatProfileConfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 19),
    _ItuSatProfileConfDuration_Type()
)
ituSatProfileConfDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileConfDuration.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfileConfDuration.setUnits("seconds")


class _ItuSatProfilePerfDuration_Type(Unsigned32):
    """Custom type ituSatProfilePerfDuration based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_ItuSatProfilePerfDuration_Type.__name__ = "Unsigned32"
_ItuSatProfilePerfDuration_Object = MibTableColumn
ituSatProfilePerfDuration = _ItuSatProfilePerfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 20),
    _ItuSatProfilePerfDuration_Type()
)
ituSatProfilePerfDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePerfDuration.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePerfDuration.setUnits("minutes")


class _ItuSatProfileRateConvention_Type(Integer32):
    """Custom type ituSatProfileRateConvention based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataRate", 1),
          ("lineRate", 2))
    )


_ItuSatProfileRateConvention_Type.__name__ = "Integer32"
_ItuSatProfileRateConvention_Object = MibTableColumn
ituSatProfileRateConvention = _ItuSatProfileRateConvention_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 21),
    _ItuSatProfileRateConvention_Type()
)
ituSatProfileRateConvention.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileRateConvention.setStatus("current")


class _ItuSatProfileResponderType_Type(Integer32):
    """Custom type ituSatProfileResponderType based on Integer32"""
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
        *(("y1564", 1),
          ("macSwapLoopback", 2),
          ("mef46Ll", 3))
    )


_ItuSatProfileResponderType_Type.__name__ = "Integer32"
_ItuSatProfileResponderType_Object = MibTableColumn
ituSatProfileResponderType = _ItuSatProfileResponderType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 3, 1, 22),
    _ItuSatProfileResponderType_Type()
)
ituSatProfileResponderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfileResponderType.setStatus("current")
_ItuSatProfilePbitTable_Object = MibTable
ituSatProfilePbitTable = _ItuSatProfilePbitTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4)
)
if mibBuilder.loadTexts:
    ituSatProfilePbitTable.setStatus("current")
_ItuSatProfilePbitEntry_Object = MibTableRow
ituSatProfilePbitEntry = _ItuSatProfilePbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1)
)
ituSatProfilePbitEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatProfileIndex"),
    (0, "RAD-TEST-MIB", "ituSatProfilePbitIndex"),
)
if mibBuilder.loadTexts:
    ituSatProfilePbitEntry.setStatus("current")
_ItuSatProfilePbitIndex_Type = RadTestPbitIndex
_ItuSatProfilePbitIndex_Object = MibTableColumn
ituSatProfilePbitIndex = _ItuSatProfilePbitIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 1),
    _ItuSatProfilePbitIndex_Type()
)
ituSatProfilePbitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatProfilePbitIndex.setStatus("current")
_ItuSatProfilePbitRowStatus_Type = RowStatus
_ItuSatProfilePbitRowStatus_Object = MibTableColumn
ituSatProfilePbitRowStatus = _ItuSatProfilePbitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 2),
    _ItuSatProfilePbitRowStatus_Type()
)
ituSatProfilePbitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitRowStatus.setStatus("current")


class _ItuSatProfilePbitFrameSize_Type(Unsigned32):
    """Custom type ituSatProfilePbitFrameSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12000),
    )


_ItuSatProfilePbitFrameSize_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitFrameSize_Object = MibTableColumn
ituSatProfilePbitFrameSize = _ItuSatProfilePbitFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 3),
    _ItuSatProfilePbitFrameSize_Type()
)
ituSatProfilePbitFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitFrameSize.setUnits("bytes")


class _ItuSatProfilePbitUniFlrThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitUniFlrThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfilePbitUniFlrThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitUniFlrThreshold_Object = MibTableColumn
ituSatProfilePbitUniFlrThreshold = _ItuSatProfilePbitUniFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 4),
    _ItuSatProfilePbitUniFlrThreshold_Type()
)
ituSatProfilePbitUniFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniFlrThreshold.setUnits("ppm")


class _ItuSatProfilePbitUniFtdThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitUniFtdThreshold based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfilePbitUniFtdThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitUniFtdThreshold_Object = MibTableColumn
ituSatProfilePbitUniFtdThreshold = _ItuSatProfilePbitUniFtdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 5),
    _ItuSatProfilePbitUniFtdThreshold_Type()
)
ituSatProfilePbitUniFtdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniFtdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniFtdThreshold.setUnits("micro seconds")


class _ItuSatProfilePbitUniFdvThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitUniFdvThreshold based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfilePbitUniFdvThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitUniFdvThreshold_Object = MibTableColumn
ituSatProfilePbitUniFdvThreshold = _ItuSatProfilePbitUniFdvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 6),
    _ItuSatProfilePbitUniFdvThreshold_Type()
)
ituSatProfilePbitUniFdvThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniFdvThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniFdvThreshold.setUnits("micro seconds")


class _ItuSatProfilePbitUniAvailThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitUniAvailThreshold based on Unsigned32"""
    defaultValue = 9990

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ItuSatProfilePbitUniAvailThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitUniAvailThreshold_Object = MibTableColumn
ituSatProfilePbitUniAvailThreshold = _ItuSatProfilePbitUniAvailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 7),
    _ItuSatProfilePbitUniAvailThreshold_Type()
)
ituSatProfilePbitUniAvailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniAvailThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitUniAvailThreshold.setUnits("hundredth of percent")


class _ItuSatProfilePbitBiFlrThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitBiFlrThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfilePbitBiFlrThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitBiFlrThreshold_Object = MibTableColumn
ituSatProfilePbitBiFlrThreshold = _ItuSatProfilePbitBiFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 8),
    _ItuSatProfilePbitBiFlrThreshold_Type()
)
ituSatProfilePbitBiFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiFlrThreshold.setUnits("ppm")


class _ItuSatProfilePbitBiFtdThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitBiFtdThreshold based on Unsigned32"""
    defaultValue = 26

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfilePbitBiFtdThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitBiFtdThreshold_Object = MibTableColumn
ituSatProfilePbitBiFtdThreshold = _ItuSatProfilePbitBiFtdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 9),
    _ItuSatProfilePbitBiFtdThreshold_Type()
)
ituSatProfilePbitBiFtdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiFtdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiFtdThreshold.setUnits("micro seconds")


class _ItuSatProfilePbitBiFdvThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitBiFdvThreshold based on Unsigned32"""
    defaultValue = 11

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ItuSatProfilePbitBiFdvThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitBiFdvThreshold_Object = MibTableColumn
ituSatProfilePbitBiFdvThreshold = _ItuSatProfilePbitBiFdvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 10),
    _ItuSatProfilePbitBiFdvThreshold_Type()
)
ituSatProfilePbitBiFdvThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiFdvThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiFdvThreshold.setUnits("micro seconds")


class _ItuSatProfilePbitBiAvailThreshold_Type(Unsigned32):
    """Custom type ituSatProfilePbitBiAvailThreshold based on Unsigned32"""
    defaultValue = 9990

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ItuSatProfilePbitBiAvailThreshold_Type.__name__ = "Unsigned32"
_ItuSatProfilePbitBiAvailThreshold_Object = MibTableColumn
ituSatProfilePbitBiAvailThreshold = _ItuSatProfilePbitBiAvailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 4, 1, 11),
    _ItuSatProfilePbitBiAvailThreshold_Type()
)
ituSatProfilePbitBiAvailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiAvailThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ituSatProfilePbitBiAvailThreshold.setUnits("hundredth of percent")
_TwampTestProfileTable_Object = MibTable
twampTestProfileTable = _TwampTestProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5)
)
if mibBuilder.loadTexts:
    twampTestProfileTable.setStatus("current")
_TwampTestProfileEntry_Object = MibTableRow
twampTestProfileEntry = _TwampTestProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1)
)
twampTestProfileEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampTestProfileId"),
)
if mibBuilder.loadTexts:
    twampTestProfileEntry.setStatus("current")
_TwampTestProfileId_Type = Unsigned32
_TwampTestProfileId_Object = MibTableColumn
twampTestProfileId = _TwampTestProfileId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 1),
    _TwampTestProfileId_Type()
)
twampTestProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampTestProfileId.setStatus("current")
_TwampTestProfileRowStatus_Type = RowStatus
_TwampTestProfileRowStatus_Object = MibTableColumn
twampTestProfileRowStatus = _TwampTestProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 2),
    _TwampTestProfileRowStatus_Type()
)
twampTestProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileRowStatus.setStatus("current")


class _TwampTestProfileName_Type(SnmpAdminString):
    """Custom type twampTestProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TwampTestProfileName_Type.__name__ = "SnmpAdminString"
_TwampTestProfileName_Object = MibTableColumn
twampTestProfileName = _TwampTestProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 3),
    _TwampTestProfileName_Type()
)
twampTestProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileName.setStatus("current")
_TwampTestProfilePayloadLength_Type = Unsigned32
_TwampTestProfilePayloadLength_Object = MibTableColumn
twampTestProfilePayloadLength = _TwampTestProfilePayloadLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 4),
    _TwampTestProfilePayloadLength_Type()
)
twampTestProfilePayloadLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfilePayloadLength.setStatus("current")
if mibBuilder.loadTexts:
    twampTestProfilePayloadLength.setUnits("bytes")
_TwampTestProfileTxRate_Type = Unsigned32
_TwampTestProfileTxRate_Object = MibTableColumn
twampTestProfileTxRate = _TwampTestProfileTxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 5),
    _TwampTestProfileTxRate_Type()
)
twampTestProfileTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileTxRate.setStatus("current")
_TwampTestProfileLossTimeout_Type = Unsigned32
_TwampTestProfileLossTimeout_Object = MibTableColumn
twampTestProfileLossTimeout = _TwampTestProfileLossTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 6),
    _TwampTestProfileLossTimeout_Type()
)
twampTestProfileLossTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    twampTestProfileLossTimeout.setUnits("micro seconds")
_TwampTestProfileLossRatioThreshold_Type = Unsigned32
_TwampTestProfileLossRatioThreshold_Object = MibTableColumn
twampTestProfileLossRatioThreshold = _TwampTestProfileLossRatioThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 7),
    _TwampTestProfileLossRatioThreshold_Type()
)
twampTestProfileLossRatioThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileLossRatioThreshold.setStatus("current")
_TwampTestProfileDelayThreshold_Type = Unsigned32
_TwampTestProfileDelayThreshold_Object = MibTableColumn
twampTestProfileDelayThreshold = _TwampTestProfileDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 8),
    _TwampTestProfileDelayThreshold_Type()
)
twampTestProfileDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileDelayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    twampTestProfileDelayThreshold.setUnits("micro seconds")
_TwampTestProfileDelayVarThreshold_Type = Unsigned32
_TwampTestProfileDelayVarThreshold_Object = MibTableColumn
twampTestProfileDelayVarThreshold = _TwampTestProfileDelayVarThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 9),
    _TwampTestProfileDelayVarThreshold_Type()
)
twampTestProfileDelayVarThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileDelayVarThreshold.setStatus("current")
if mibBuilder.loadTexts:
    twampTestProfileDelayVarThreshold.setUnits("micro seconds")


class _TwampTestProfileDelayVarEventType_Type(Integer32):
    """Custom type twampTestProfileDelayVarEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pdvMax", 2),
          ("ipdvMax", 3))
    )


_TwampTestProfileDelayVarEventType_Type.__name__ = "Integer32"
_TwampTestProfileDelayVarEventType_Object = MibTableColumn
twampTestProfileDelayVarEventType = _TwampTestProfileDelayVarEventType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 5, 1, 10),
    _TwampTestProfileDelayVarEventType_Type()
)
twampTestProfileDelayVarEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampTestProfileDelayVarEventType.setStatus("current")
_RadTestPrefRepTest_ObjectIdentity = ObjectIdentity
radTestPrefRepTest = _RadTestPrefRepTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2)
)
_TstNePerfRepTestTable_Object = MibTable
tstNePerfRepTestTable = _TstNePerfRepTestTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    tstNePerfRepTestTable.setStatus("current")
_TstNePerfRepTestEntry_Object = MibTableRow
tstNePerfRepTestEntry = _TstNePerfRepTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1)
)
tstNePerfRepTestEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
)
if mibBuilder.loadTexts:
    tstNePerfRepTestEntry.setStatus("current")
_TstNePerfRepTestId_Type = Unsigned32
_TstNePerfRepTestId_Object = MibTableColumn
tstNePerfRepTestId = _TstNePerfRepTestId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 1),
    _TstNePerfRepTestId_Type()
)
tstNePerfRepTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tstNePerfRepTestId.setStatus("current")
_TstNePerfRepTestRowStatus_Type = RowStatus
_TstNePerfRepTestRowStatus_Object = MibTableColumn
tstNePerfRepTestRowStatus = _TstNePerfRepTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 2),
    _TstNePerfRepTestRowStatus_Type()
)
tstNePerfRepTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestRowStatus.setStatus("current")


class _TstNePerfRepTestType_Type(Bits):
    """Custom type tstNePerfRepTestType based on Bits"""
    namedValues = NamedValues(
        *(("throughput", 0),
          ("frameloss", 1),
          ("latency", 2))
    )

_TstNePerfRepTestType_Type.__name__ = "Bits"
_TstNePerfRepTestType_Object = MibTableColumn
tstNePerfRepTestType = _TstNePerfRepTestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 3),
    _TstNePerfRepTestType_Type()
)
tstNePerfRepTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestType.setStatus("current")
_TstNePerfRepTestProfileId_Type = Unsigned32
_TstNePerfRepTestProfileId_Object = MibTableColumn
tstNePerfRepTestProfileId = _TstNePerfRepTestProfileId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 4),
    _TstNePerfRepTestProfileId_Type()
)
tstNePerfRepTestProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestProfileId.setStatus("current")
_TstNePerfRepTestEntity_Type = RowPointer
_TstNePerfRepTestEntity_Object = MibTableColumn
tstNePerfRepTestEntity = _TstNePerfRepTestEntity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 5),
    _TstNePerfRepTestEntity_Type()
)
tstNePerfRepTestEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestEntity.setStatus("current")


class _TstNePerfRepTestActivation_Type(Integer32):
    """Custom type tstNePerfRepTestActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("now", 2),
          ("dateAndTime", 3),
          ("daily", 4),
          ("cancelTest", 255))
    )


_TstNePerfRepTestActivation_Type.__name__ = "Integer32"
_TstNePerfRepTestActivation_Object = MibTableColumn
tstNePerfRepTestActivation = _TstNePerfRepTestActivation_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 6),
    _TstNePerfRepTestActivation_Type()
)
tstNePerfRepTestActivation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestActivation.setStatus("current")


class _TstNePerfRepTestStatus_Type(Integer32):
    """Custom type tstNePerfRepTestStatus based on Integer32"""
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
        *(("adminOff", 1),
          ("inProgress", 2),
          ("pending", 3),
          ("completed", 4),
          ("timeOut", 5))
    )


_TstNePerfRepTestStatus_Type.__name__ = "Integer32"
_TstNePerfRepTestStatus_Object = MibTableColumn
tstNePerfRepTestStatus = _TstNePerfRepTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 7),
    _TstNePerfRepTestStatus_Type()
)
tstNePerfRepTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepTestStatus.setStatus("current")
_TstNePerfRepTestActivationDateAndTime_Type = DateAndTime
_TstNePerfRepTestActivationDateAndTime_Object = MibTableColumn
tstNePerfRepTestActivationDateAndTime = _TstNePerfRepTestActivationDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 8),
    _TstNePerfRepTestActivationDateAndTime_Type()
)
tstNePerfRepTestActivationDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestActivationDateAndTime.setStatus("current")
_TstNePerfRepTestActivationRecurrenceTime_Type = Unsigned32
_TstNePerfRepTestActivationRecurrenceTime_Object = MibTableColumn
tstNePerfRepTestActivationRecurrenceTime = _TstNePerfRepTestActivationRecurrenceTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 9),
    _TstNePerfRepTestActivationRecurrenceTime_Type()
)
tstNePerfRepTestActivationRecurrenceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestActivationRecurrenceTime.setStatus("current")
_TstNePerfRepTestMaxRate_Type = Unsigned32
_TstNePerfRepTestMaxRate_Object = MibTableColumn
tstNePerfRepTestMaxRate = _TstNePerfRepTestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 10),
    _TstNePerfRepTestMaxRate_Type()
)
tstNePerfRepTestMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestMaxRate.setStatus("current")
_TstNePerfRepTestElapsedTime_Type = TimeTicks
_TstNePerfRepTestElapsedTime_Object = MibTableColumn
tstNePerfRepTestElapsedTime = _TstNePerfRepTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 11),
    _TstNePerfRepTestElapsedTime_Type()
)
tstNePerfRepTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepTestElapsedTime.setStatus("current")


class _TstNePerfRepTestResetResults_Type(Integer32):
    """Custom type tstNePerfRepTestResetResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_TstNePerfRepTestResetResults_Type.__name__ = "Integer32"
_TstNePerfRepTestResetResults_Object = MibTableColumn
tstNePerfRepTestResetResults = _TstNePerfRepTestResetResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 12),
    _TstNePerfRepTestResetResults_Type()
)
tstNePerfRepTestResetResults.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestResetResults.setStatus("current")


class _TstNePerfRepTestRateConvention_Type(Integer32):
    """Custom type tstNePerfRepTestRateConvention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineRate", 2),
          ("dataRate", 3))
    )


_TstNePerfRepTestRateConvention_Type.__name__ = "Integer32"
_TstNePerfRepTestRateConvention_Object = MibTableColumn
tstNePerfRepTestRateConvention = _TstNePerfRepTestRateConvention_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 13),
    _TstNePerfRepTestRateConvention_Type()
)
tstNePerfRepTestRateConvention.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestRateConvention.setStatus("current")
_TstNePerfRepTestFrameCompensation_Type = Unsigned32
_TstNePerfRepTestFrameCompensation_Object = MibTableColumn
tstNePerfRepTestFrameCompensation = _TstNePerfRepTestFrameCompensation_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 14),
    _TstNePerfRepTestFrameCompensation_Type()
)
tstNePerfRepTestFrameCompensation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestFrameCompensation.setStatus("current")


class _TstNePerfRepTestMaxTestDuration_Type(Unsigned32):
    """Custom type tstNePerfRepTestMaxTestDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_TstNePerfRepTestMaxTestDuration_Type.__name__ = "Unsigned32"
_TstNePerfRepTestMaxTestDuration_Object = MibTableColumn
tstNePerfRepTestMaxTestDuration = _TstNePerfRepTestMaxTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 15),
    _TstNePerfRepTestMaxTestDuration_Type()
)
tstNePerfRepTestMaxTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestMaxTestDuration.setStatus("current")
_TstNePerfRepTestAssociatedFlow_Type = RowPointer
_TstNePerfRepTestAssociatedFlow_Object = MibTableColumn
tstNePerfRepTestAssociatedFlow = _TstNePerfRepTestAssociatedFlow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 1, 1, 16),
    _TstNePerfRepTestAssociatedFlow_Type()
)
tstNePerfRepTestAssociatedFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tstNePerfRepTestAssociatedFlow.setStatus("current")
_ItuSatGeneratorTable_Object = MibTable
ituSatGeneratorTable = _ItuSatGeneratorTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    ituSatGeneratorTable.setStatus("current")
_ItuSatGeneratorEntry_Object = MibTableRow
ituSatGeneratorEntry = _ItuSatGeneratorEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1)
)
ituSatGeneratorEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatGeneratorIndex"),
)
if mibBuilder.loadTexts:
    ituSatGeneratorEntry.setStatus("current")
_ItuSatGeneratorIndex_Type = Unsigned32
_ItuSatGeneratorIndex_Object = MibTableColumn
ituSatGeneratorIndex = _ItuSatGeneratorIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 1),
    _ItuSatGeneratorIndex_Type()
)
ituSatGeneratorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatGeneratorIndex.setStatus("current")


class _ItuSatGeneratorName_Type(SnmpAdminString):
    """Custom type ituSatGeneratorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ItuSatGeneratorName_Type.__name__ = "SnmpAdminString"
_ItuSatGeneratorName_Object = MibTableColumn
ituSatGeneratorName = _ItuSatGeneratorName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 2),
    _ItuSatGeneratorName_Type()
)
ituSatGeneratorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorName.setStatus("current")
_ItuSatGeneratorRowStatus_Type = RowStatus
_ItuSatGeneratorRowStatus_Object = MibTableColumn
ituSatGeneratorRowStatus = _ItuSatGeneratorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 3),
    _ItuSatGeneratorRowStatus_Type()
)
ituSatGeneratorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorRowStatus.setStatus("current")
_ItuSatGeneratorServicePointer_Type = RowPointer
_ItuSatGeneratorServicePointer_Object = MibTableColumn
ituSatGeneratorServicePointer = _ItuSatGeneratorServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 4),
    _ItuSatGeneratorServicePointer_Type()
)
ituSatGeneratorServicePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorServicePointer.setStatus("current")


class _ItuSatGeneratorProvisionedPbits_Type(RadTestPbitValues):
    """Custom type ituSatGeneratorProvisionedPbits based on RadTestPbitValues"""
    defaultBinValue = "0"


_ItuSatGeneratorProvisionedPbits_Type.__name__ = "RadTestPbitValues"
_ItuSatGeneratorProvisionedPbits_Object = MibTableColumn
ituSatGeneratorProvisionedPbits = _ItuSatGeneratorProvisionedPbits_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 5),
    _ItuSatGeneratorProvisionedPbits_Type()
)
ituSatGeneratorProvisionedPbits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorProvisionedPbits.setStatus("current")


class _ItuSatGeneratorProfile_Type(Unsigned32):
    """Custom type ituSatGeneratorProfile based on Unsigned32"""
    defaultValue = 0


_ItuSatGeneratorProfile_Type.__name__ = "Unsigned32"
_ItuSatGeneratorProfile_Object = MibTableColumn
ituSatGeneratorProfile = _ItuSatGeneratorProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 6),
    _ItuSatGeneratorProfile_Type()
)
ituSatGeneratorProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorProfile.setStatus("current")


class _ItuSatGeneratorCmd_Type(Integer32):
    """Custom type ituSatGeneratorCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_ItuSatGeneratorCmd_Type.__name__ = "Integer32"
_ItuSatGeneratorCmd_Object = MibTableColumn
ituSatGeneratorCmd = _ItuSatGeneratorCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 7),
    _ItuSatGeneratorCmd_Type()
)
ituSatGeneratorCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorCmd.setStatus("current")
_ItuSatGeneratorConfChanged_Type = TruthValue
_ItuSatGeneratorConfChanged_Object = MibTableColumn
ituSatGeneratorConfChanged = _ItuSatGeneratorConfChanged_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 8),
    _ItuSatGeneratorConfChanged_Type()
)
ituSatGeneratorConfChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorConfChanged.setStatus("current")


class _ItuSatGeneratorStatus_Type(Integer32):
    """Custom type ituSatGeneratorStatus based on Integer32"""
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
        *(("idle", 1),
          ("ready", 2),
          ("inProgress", 3),
          ("passed", 4),
          ("failed", 5),
          ("userAborted", 6),
          ("systemAborted", 7),
          ("llFailure", 8))
    )


_ItuSatGeneratorStatus_Type.__name__ = "Integer32"
_ItuSatGeneratorStatus_Object = MibTableColumn
ituSatGeneratorStatus = _ItuSatGeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 9),
    _ItuSatGeneratorStatus_Type()
)
ituSatGeneratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorStatus.setStatus("current")
_ItuSatGeneratorTimeRemaining_Type = Unsigned32
_ItuSatGeneratorTimeRemaining_Object = MibTableColumn
ituSatGeneratorTimeRemaining = _ItuSatGeneratorTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 10),
    _ItuSatGeneratorTimeRemaining_Type()
)
ituSatGeneratorTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorTimeRemaining.setUnits("seconds")


class _ItuSatGeneratorCurrentPhase_Type(Integer32):
    """Custom type ituSatGeneratorCurrentPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("configuration", 2),
          ("performance", 3))
    )


_ItuSatGeneratorCurrentPhase_Type.__name__ = "Integer32"
_ItuSatGeneratorCurrentPhase_Object = MibTableColumn
ituSatGeneratorCurrentPhase = _ItuSatGeneratorCurrentPhase_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 11),
    _ItuSatGeneratorCurrentPhase_Type()
)
ituSatGeneratorCurrentPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorCurrentPhase.setStatus("current")
_ItuSatGeneratorDestination_Type = MacAddress
_ItuSatGeneratorDestination_Object = MibTableColumn
ituSatGeneratorDestination = _ItuSatGeneratorDestination_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 12),
    _ItuSatGeneratorDestination_Type()
)
ituSatGeneratorDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorDestination.setStatus("current")
_ItuSatGeneratorSource_Type = MacAddress
_ItuSatGeneratorSource_Object = MibTableColumn
ituSatGeneratorSource = _ItuSatGeneratorSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 13),
    _ItuSatGeneratorSource_Type()
)
ituSatGeneratorSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorSource.setStatus("current")


class _ItuSatGeneratorInnerTag_Type(Unsigned32):
    """Custom type ituSatGeneratorInnerTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ItuSatGeneratorInnerTag_Type.__name__ = "Unsigned32"
_ItuSatGeneratorInnerTag_Object = MibTableColumn
ituSatGeneratorInnerTag = _ItuSatGeneratorInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 14),
    _ItuSatGeneratorInnerTag_Type()
)
ituSatGeneratorInnerTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorInnerTag.setStatus("current")


class _ItuSatGeneratorOuterTag_Type(Unsigned32):
    """Custom type ituSatGeneratorOuterTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ItuSatGeneratorOuterTag_Type.__name__ = "Unsigned32"
_ItuSatGeneratorOuterTag_Object = MibTableColumn
ituSatGeneratorOuterTag = _ItuSatGeneratorOuterTag_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 15),
    _ItuSatGeneratorOuterTag_Type()
)
ituSatGeneratorOuterTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorOuterTag.setStatus("current")
_ItuSatGeneratorTestedPbits_Type = RadTestPbitValues
_ItuSatGeneratorTestedPbits_Object = MibTableColumn
ituSatGeneratorTestedPbits = _ItuSatGeneratorTestedPbits_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 16),
    _ItuSatGeneratorTestedPbits_Type()
)
ituSatGeneratorTestedPbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorTestedPbits.setStatus("current")
_ItuSatGeneratorStartTime_Type = DateAndTime
_ItuSatGeneratorStartTime_Object = MibTableColumn
ituSatGeneratorStartTime = _ItuSatGeneratorStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 17),
    _ItuSatGeneratorStartTime_Type()
)
ituSatGeneratorStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorStartTime.setStatus("current")
_ItuSatGeneratorEndTime_Type = DateAndTime
_ItuSatGeneratorEndTime_Object = MibTableColumn
ituSatGeneratorEndTime = _ItuSatGeneratorEndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 18),
    _ItuSatGeneratorEndTime_Type()
)
ituSatGeneratorEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorEndTime.setStatus("current")
_ItuSatGeneratorTimeElapsed_Type = Unsigned32
_ItuSatGeneratorTimeElapsed_Object = MibTableColumn
ituSatGeneratorTimeElapsed = _ItuSatGeneratorTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 19),
    _ItuSatGeneratorTimeElapsed_Type()
)
ituSatGeneratorTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorTimeElapsed.setUnits("seconds")
_ItuSatGeneratorConfResult_Type = RadTestResult
_ItuSatGeneratorConfResult_Object = MibTableColumn
ituSatGeneratorConfResult = _ItuSatGeneratorConfResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 20),
    _ItuSatGeneratorConfResult_Type()
)
ituSatGeneratorConfResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorConfResult.setStatus("current")
_ItuSatGeneratorPerfResult_Type = RadTestResult
_ItuSatGeneratorPerfResult_Object = MibTableColumn
ituSatGeneratorPerfResult = _ItuSatGeneratorPerfResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 21),
    _ItuSatGeneratorPerfResult_Type()
)
ituSatGeneratorPerfResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorPerfResult.setStatus("current")


class _ItuSatGeneratorConfDuration_Type(Unsigned32):
    """Custom type ituSatGeneratorConfDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 360),
    )


_ItuSatGeneratorConfDuration_Type.__name__ = "Unsigned32"
_ItuSatGeneratorConfDuration_Object = MibTableColumn
ituSatGeneratorConfDuration = _ItuSatGeneratorConfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 22),
    _ItuSatGeneratorConfDuration_Type()
)
ituSatGeneratorConfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorConfDuration.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorConfDuration.setUnits("seconds")


class _ItuSatGeneratorPerfDuration_Type(Unsigned32):
    """Custom type ituSatGeneratorPerfDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 7200),
    )


_ItuSatGeneratorPerfDuration_Type.__name__ = "Unsigned32"
_ItuSatGeneratorPerfDuration_Object = MibTableColumn
ituSatGeneratorPerfDuration = _ItuSatGeneratorPerfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 23),
    _ItuSatGeneratorPerfDuration_Type()
)
ituSatGeneratorPerfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorPerfDuration.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorPerfDuration.setUnits("minutes")


class _ItuSatGeneratorScope_Type(Bits):
    """Custom type ituSatGeneratorScope based on Bits"""
    namedValues = NamedValues(
        *(("configuration", 0),
          ("performance", 1))
    )

_ItuSatGeneratorScope_Type.__name__ = "Bits"
_ItuSatGeneratorScope_Object = MibTableColumn
ituSatGeneratorScope = _ItuSatGeneratorScope_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 24),
    _ItuSatGeneratorScope_Type()
)
ituSatGeneratorScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorScope.setStatus("current")


class _ItuSatGeneratorServiceBinding_Type(Integer32):
    """Custom type ituSatGeneratorServiceBinding based on Integer32"""
    defaultValue = 1

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
        *(("ma", 1),
          ("singleMultiCosFlow", 2),
          ("multipleSingleCosFlows", 3),
          ("serviceNameAndEgressPort", 4))
    )


_ItuSatGeneratorServiceBinding_Type.__name__ = "Integer32"
_ItuSatGeneratorServiceBinding_Object = MibTableColumn
ituSatGeneratorServiceBinding = _ItuSatGeneratorServiceBinding_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 25),
    _ItuSatGeneratorServiceBinding_Type()
)
ituSatGeneratorServiceBinding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorServiceBinding.setStatus("current")


class _ItuSatGeneratorServiceName_Type(SnmpAdminString):
    """Custom type ituSatGeneratorServiceName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ItuSatGeneratorServiceName_Type.__name__ = "SnmpAdminString"
_ItuSatGeneratorServiceName_Object = MibTableColumn
ituSatGeneratorServiceName = _ItuSatGeneratorServiceName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 26),
    _ItuSatGeneratorServiceName_Type()
)
ituSatGeneratorServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorServiceName.setStatus("current")


class _ItuSatGeneratorEgressPort_Type(InterfaceIndexOrZero):
    """Custom type ituSatGeneratorEgressPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_ItuSatGeneratorEgressPort_Type.__name__ = "InterfaceIndexOrZero"
_ItuSatGeneratorEgressPort_Object = MibTableColumn
ituSatGeneratorEgressPort = _ItuSatGeneratorEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 27),
    _ItuSatGeneratorEgressPort_Type()
)
ituSatGeneratorEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorEgressPort.setStatus("current")


class _ItuSatGeneratorProvisionedDestination_Type(MacAddress):
    """Custom type ituSatGeneratorProvisionedDestination based on MacAddress"""
    defaultHexValue = "000000000000"


_ItuSatGeneratorProvisionedDestination_Type.__name__ = "MacAddress"
_ItuSatGeneratorProvisionedDestination_Object = MibTableColumn
ituSatGeneratorProvisionedDestination = _ItuSatGeneratorProvisionedDestination_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 2, 1, 28),
    _ItuSatGeneratorProvisionedDestination_Type()
)
ituSatGeneratorProvisionedDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorProvisionedDestination.setStatus("current")
_ItuSatGeneratorFlowTable_Object = MibTable
ituSatGeneratorFlowTable = _ItuSatGeneratorFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    ituSatGeneratorFlowTable.setStatus("current")
_ItuSatGeneratorFlowEntry_Object = MibTableRow
ituSatGeneratorFlowEntry = _ItuSatGeneratorFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1)
)
ituSatGeneratorFlowEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatGeneratorIndex"),
    (0, "RAD-TEST-MIB", "ituSatGeneratorFlowPbitIndex"),
)
if mibBuilder.loadTexts:
    ituSatGeneratorFlowEntry.setStatus("current")
_ItuSatGeneratorFlowPbitIndex_Type = RadTestPbitIndex
_ItuSatGeneratorFlowPbitIndex_Object = MibTableColumn
ituSatGeneratorFlowPbitIndex = _ItuSatGeneratorFlowPbitIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 1),
    _ItuSatGeneratorFlowPbitIndex_Type()
)
ituSatGeneratorFlowPbitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowPbitIndex.setStatus("current")
_ItuSatGeneratorFlowNameTx_Type = SnmpAdminString
_ItuSatGeneratorFlowNameTx_Object = MibTableColumn
ituSatGeneratorFlowNameTx = _ItuSatGeneratorFlowNameTx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 2),
    _ItuSatGeneratorFlowNameTx_Type()
)
ituSatGeneratorFlowNameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowNameTx.setStatus("current")
_ItuSatGeneratorFlowNameRx_Type = SnmpAdminString
_ItuSatGeneratorFlowNameRx_Object = MibTableColumn
ituSatGeneratorFlowNameRx = _ItuSatGeneratorFlowNameRx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 3),
    _ItuSatGeneratorFlowNameRx_Type()
)
ituSatGeneratorFlowNameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowNameRx.setStatus("current")
_ItuSatGeneratorFlowCir_Type = Unsigned32
_ItuSatGeneratorFlowCir_Object = MibTableColumn
ituSatGeneratorFlowCir = _ItuSatGeneratorFlowCir_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 4),
    _ItuSatGeneratorFlowCir_Type()
)
ituSatGeneratorFlowCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowCir.setStatus("current")
_ItuSatGeneratorFlowEir_Type = Unsigned32
_ItuSatGeneratorFlowEir_Object = MibTableColumn
ituSatGeneratorFlowEir = _ItuSatGeneratorFlowEir_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 5),
    _ItuSatGeneratorFlowEir_Type()
)
ituSatGeneratorFlowEir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowEir.setStatus("current")


class _ItuSatGeneratorFlowAssociatedMEP_Type(Unsigned32):
    """Custom type ituSatGeneratorFlowAssociatedMEP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_ItuSatGeneratorFlowAssociatedMEP_Type.__name__ = "Unsigned32"
_ItuSatGeneratorFlowAssociatedMEP_Object = MibTableColumn
ituSatGeneratorFlowAssociatedMEP = _ItuSatGeneratorFlowAssociatedMEP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 6),
    _ItuSatGeneratorFlowAssociatedMEP_Type()
)
ituSatGeneratorFlowAssociatedMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowAssociatedMEP.setStatus("current")


class _ItuSatGeneratorFlowAssociatedService_Type(Unsigned32):
    """Custom type ituSatGeneratorFlowAssociatedService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ItuSatGeneratorFlowAssociatedService_Type.__name__ = "Unsigned32"
_ItuSatGeneratorFlowAssociatedService_Object = MibTableColumn
ituSatGeneratorFlowAssociatedService = _ItuSatGeneratorFlowAssociatedService_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 7),
    _ItuSatGeneratorFlowAssociatedService_Type()
)
ituSatGeneratorFlowAssociatedService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowAssociatedService.setStatus("current")


class _ItuSatGeneratorFlowBwpInUse_Type(Integer32):
    """Custom type ituSatGeneratorFlowBwpInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flow", 1),
          ("test", 2))
    )


_ItuSatGeneratorFlowBwpInUse_Type.__name__ = "Integer32"
_ItuSatGeneratorFlowBwpInUse_Object = MibTableColumn
ituSatGeneratorFlowBwpInUse = _ItuSatGeneratorFlowBwpInUse_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 3, 1, 8),
    _ItuSatGeneratorFlowBwpInUse_Type()
)
ituSatGeneratorFlowBwpInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatGeneratorFlowBwpInUse.setStatus("current")
_ItuSatResponderTable_Object = MibTable
ituSatResponderTable = _ItuSatResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4)
)
if mibBuilder.loadTexts:
    ituSatResponderTable.setStatus("current")
_ItuSatResponderEntry_Object = MibTableRow
ituSatResponderEntry = _ItuSatResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1)
)
ituSatResponderEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatResponderIndex"),
)
if mibBuilder.loadTexts:
    ituSatResponderEntry.setStatus("current")
_ItuSatResponderIndex_Type = Unsigned32
_ItuSatResponderIndex_Object = MibTableColumn
ituSatResponderIndex = _ItuSatResponderIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 1),
    _ItuSatResponderIndex_Type()
)
ituSatResponderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatResponderIndex.setStatus("current")


class _ItuSatResponderName_Type(SnmpAdminString):
    """Custom type ituSatResponderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ItuSatResponderName_Type.__name__ = "SnmpAdminString"
_ItuSatResponderName_Object = MibTableColumn
ituSatResponderName = _ItuSatResponderName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 2),
    _ItuSatResponderName_Type()
)
ituSatResponderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderName.setStatus("current")
_ItuSatResponderRowStatus_Type = RowStatus
_ItuSatResponderRowStatus_Object = MibTableColumn
ituSatResponderRowStatus = _ItuSatResponderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 3),
    _ItuSatResponderRowStatus_Type()
)
ituSatResponderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderRowStatus.setStatus("current")
_ItuSatResponderServicePointer_Type = RowPointer
_ItuSatResponderServicePointer_Object = MibTableColumn
ituSatResponderServicePointer = _ItuSatResponderServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 4),
    _ItuSatResponderServicePointer_Type()
)
ituSatResponderServicePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderServicePointer.setStatus("current")


class _ItuSatResponderProfile_Type(Unsigned32):
    """Custom type ituSatResponderProfile based on Unsigned32"""
    defaultValue = 0


_ItuSatResponderProfile_Type.__name__ = "Unsigned32"
_ItuSatResponderProfile_Object = MibTableColumn
ituSatResponderProfile = _ItuSatResponderProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 5),
    _ItuSatResponderProfile_Type()
)
ituSatResponderProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderProfile.setStatus("current")


class _ItuSatResponderCmd_Type(Integer32):
    """Custom type ituSatResponderCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_ItuSatResponderCmd_Type.__name__ = "Integer32"
_ItuSatResponderCmd_Object = MibTableColumn
ituSatResponderCmd = _ItuSatResponderCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 6),
    _ItuSatResponderCmd_Type()
)
ituSatResponderCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderCmd.setStatus("current")


class _ItuSatResponderStatus_Type(Integer32):
    """Custom type ituSatResponderStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("ready", 2),
          ("inProgress", 3))
    )


_ItuSatResponderStatus_Type.__name__ = "Integer32"
_ItuSatResponderStatus_Object = MibTableColumn
ituSatResponderStatus = _ItuSatResponderStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 7),
    _ItuSatResponderStatus_Type()
)
ituSatResponderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatResponderStatus.setStatus("current")


class _ItuSatResponderServiceBinding_Type(Integer32):
    """Custom type ituSatResponderServiceBinding based on Integer32"""
    defaultValue = 1

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
        *(("ma", 1),
          ("singleMultiCosFlow", 2),
          ("multipleSingleCosFlows", 3),
          ("serviceNameAndEgressPort", 4))
    )


_ItuSatResponderServiceBinding_Type.__name__ = "Integer32"
_ItuSatResponderServiceBinding_Object = MibTableColumn
ituSatResponderServiceBinding = _ItuSatResponderServiceBinding_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 8),
    _ItuSatResponderServiceBinding_Type()
)
ituSatResponderServiceBinding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderServiceBinding.setStatus("current")


class _ItuSatResponderServiceName_Type(SnmpAdminString):
    """Custom type ituSatResponderServiceName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ItuSatResponderServiceName_Type.__name__ = "SnmpAdminString"
_ItuSatResponderServiceName_Object = MibTableColumn
ituSatResponderServiceName = _ItuSatResponderServiceName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 9),
    _ItuSatResponderServiceName_Type()
)
ituSatResponderServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderServiceName.setStatus("current")


class _ItuSatResponderEgressPort_Type(InterfaceIndexOrZero):
    """Custom type ituSatResponderEgressPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_ItuSatResponderEgressPort_Type.__name__ = "InterfaceIndexOrZero"
_ItuSatResponderEgressPort_Object = MibTableColumn
ituSatResponderEgressPort = _ItuSatResponderEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 4, 1, 10),
    _ItuSatResponderEgressPort_Type()
)
ituSatResponderEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatResponderEgressPort.setStatus("current")
_ItuSatGeneratorPolicerTable_Object = MibTable
ituSatGeneratorPolicerTable = _ItuSatGeneratorPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5)
)
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerTable.setStatus("current")
_ItuSatGeneratorPolicerEntry_Object = MibTableRow
ituSatGeneratorPolicerEntry = _ItuSatGeneratorPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1)
)
ituSatGeneratorPolicerEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatGeneratorIndex"),
    (0, "RAD-TEST-MIB", "ituSatGeneratorPolicerPbitIndex"),
)
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerEntry.setStatus("current")
_ItuSatGeneratorPolicerPbitIndex_Type = RadTestPbitIndex
_ItuSatGeneratorPolicerPbitIndex_Object = MibTableColumn
ituSatGeneratorPolicerPbitIndex = _ItuSatGeneratorPolicerPbitIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 1),
    _ItuSatGeneratorPolicerPbitIndex_Type()
)
ituSatGeneratorPolicerPbitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerPbitIndex.setStatus("current")
_ItuSatGeneratorPolicerRowStatus_Type = RowStatus
_ItuSatGeneratorPolicerRowStatus_Object = MibTableColumn
ituSatGeneratorPolicerRowStatus = _ItuSatGeneratorPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 2),
    _ItuSatGeneratorPolicerRowStatus_Type()
)
ituSatGeneratorPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerRowStatus.setStatus("current")


class _ItuSatGeneratorPolicerCir_Type(Gauge32):
    """Custom type ituSatGeneratorPolicerCir based on Gauge32"""
    defaultValue = 0


_ItuSatGeneratorPolicerCir_Type.__name__ = "Gauge32"
_ItuSatGeneratorPolicerCir_Object = MibTableColumn
ituSatGeneratorPolicerCir = _ItuSatGeneratorPolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 3),
    _ItuSatGeneratorPolicerCir_Type()
)
ituSatGeneratorPolicerCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerCir.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerCir.setUnits("kbps")


class _ItuSatGeneratorPolicerCbs_Type(Gauge32):
    """Custom type ituSatGeneratorPolicerCbs based on Gauge32"""
    defaultValue = 0


_ItuSatGeneratorPolicerCbs_Type.__name__ = "Gauge32"
_ItuSatGeneratorPolicerCbs_Object = MibTableColumn
ituSatGeneratorPolicerCbs = _ItuSatGeneratorPolicerCbs_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 4),
    _ItuSatGeneratorPolicerCbs_Type()
)
ituSatGeneratorPolicerCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerCbs.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerCbs.setUnits("bytes")


class _ItuSatGeneratorPolicerEir_Type(Gauge32):
    """Custom type ituSatGeneratorPolicerEir based on Gauge32"""
    defaultValue = 0


_ItuSatGeneratorPolicerEir_Type.__name__ = "Gauge32"
_ItuSatGeneratorPolicerEir_Object = MibTableColumn
ituSatGeneratorPolicerEir = _ItuSatGeneratorPolicerEir_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 5),
    _ItuSatGeneratorPolicerEir_Type()
)
ituSatGeneratorPolicerEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerEir.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerEir.setUnits("kbps")


class _ItuSatGeneratorPolicerEbs_Type(Gauge32):
    """Custom type ituSatGeneratorPolicerEbs based on Gauge32"""
    defaultValue = 0


_ItuSatGeneratorPolicerEbs_Type.__name__ = "Gauge32"
_ItuSatGeneratorPolicerEbs_Object = MibTableColumn
ituSatGeneratorPolicerEbs = _ItuSatGeneratorPolicerEbs_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 6),
    _ItuSatGeneratorPolicerEbs_Type()
)
ituSatGeneratorPolicerEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerEbs.setStatus("current")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerEbs.setUnits("bytes")


class _ItuSatGeneratorPolicerProfile_Type(Unsigned32):
    """Custom type ituSatGeneratorPolicerProfile based on Unsigned32"""
    defaultValue = 0


_ItuSatGeneratorPolicerProfile_Type.__name__ = "Unsigned32"
_ItuSatGeneratorPolicerProfile_Object = MibTableColumn
ituSatGeneratorPolicerProfile = _ItuSatGeneratorPolicerProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 5, 1, 7),
    _ItuSatGeneratorPolicerProfile_Type()
)
ituSatGeneratorPolicerProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatGeneratorPolicerProfile.setStatus("current")
_TwampControllerTable_Object = MibTable
twampControllerTable = _TwampControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6)
)
if mibBuilder.loadTexts:
    twampControllerTable.setStatus("current")
_TwampControllerEntry_Object = MibTableRow
twampControllerEntry = _TwampControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1)
)
twampControllerEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampControllerId"),
)
if mibBuilder.loadTexts:
    twampControllerEntry.setStatus("current")
_TwampControllerId_Type = Unsigned32
_TwampControllerId_Object = MibTableColumn
twampControllerId = _TwampControllerId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 1),
    _TwampControllerId_Type()
)
twampControllerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampControllerId.setStatus("current")
_TwampControllerRowStatus_Type = RowStatus
_TwampControllerRowStatus_Object = MibTableColumn
twampControllerRowStatus = _TwampControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 2),
    _TwampControllerRowStatus_Type()
)
twampControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerRowStatus.setStatus("current")


class _TwampControllerName_Type(SnmpAdminString):
    """Custom type twampControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TwampControllerName_Type.__name__ = "SnmpAdminString"
_TwampControllerName_Object = MibTableColumn
twampControllerName = _TwampControllerName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 3),
    _TwampControllerName_Type()
)
twampControllerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerName.setStatus("current")


class _TwampControllerStatus_Type(Integer32):
    """Custom type twampControllerStatus based on Integer32"""
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
        *(("adminOff", 1),
          ("idle", 2),
          ("ready", 3),
          ("inProgress", 4))
    )


_TwampControllerStatus_Type.__name__ = "Integer32"
_TwampControllerStatus_Object = MibTableColumn
twampControllerStatus = _TwampControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 4),
    _TwampControllerStatus_Type()
)
twampControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampControllerStatus.setStatus("current")


class _TwampControllerType_Type(Integer32):
    """Custom type twampControllerType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twamp", 2),
          ("twampLight", 3))
    )


_TwampControllerType_Type.__name__ = "Integer32"
_TwampControllerType_Object = MibTableColumn
twampControllerType = _TwampControllerType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 5),
    _TwampControllerType_Type()
)
twampControllerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerType.setStatus("current")


class _TwampControllerL2Probe_Type(Integer32):
    """Custom type twampControllerL2Probe based on Integer32"""
    defaultValue = 1

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


_TwampControllerL2Probe_Type.__name__ = "Integer32"
_TwampControllerL2Probe_Object = MibTableColumn
twampControllerL2Probe = _TwampControllerL2Probe_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 6),
    _TwampControllerL2Probe_Type()
)
twampControllerL2Probe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerL2Probe.setStatus("current")
_TwampControllerIngressEgressPort_Type = InterfaceIndexOrZero
_TwampControllerIngressEgressPort_Object = MibTableColumn
twampControllerIngressEgressPort = _TwampControllerIngressEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 7),
    _TwampControllerIngressEgressPort_Type()
)
twampControllerIngressEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerIngressEgressPort.setStatus("current")


class _TwampControllerOuterVlan_Type(Unsigned32):
    """Custom type twampControllerOuterVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TwampControllerOuterVlan_Type.__name__ = "Unsigned32"
_TwampControllerOuterVlan_Object = MibTableColumn
twampControllerOuterVlan = _TwampControllerOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 8),
    _TwampControllerOuterVlan_Type()
)
twampControllerOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerOuterVlan.setStatus("current")


class _TwampControllerInnerVlan_Type(Unsigned32):
    """Custom type twampControllerInnerVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TwampControllerInnerVlan_Type.__name__ = "Unsigned32"
_TwampControllerInnerVlan_Object = MibTableColumn
twampControllerInnerVlan = _TwampControllerInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 9),
    _TwampControllerInnerVlan_Type()
)
twampControllerInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerInnerVlan.setStatus("current")


class _TwampControllerOuterPbit_Type(Unsigned32):
    """Custom type twampControllerOuterPbit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TwampControllerOuterPbit_Type.__name__ = "Unsigned32"
_TwampControllerOuterPbit_Object = MibTableColumn
twampControllerOuterPbit = _TwampControllerOuterPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 10),
    _TwampControllerOuterPbit_Type()
)
twampControllerOuterPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerOuterPbit.setStatus("current")


class _TwampControllerInnerPbit_Type(Unsigned32):
    """Custom type twampControllerInnerPbit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TwampControllerInnerPbit_Type.__name__ = "Unsigned32"
_TwampControllerInnerPbit_Object = MibTableColumn
twampControllerInnerPbit = _TwampControllerInnerPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 11),
    _TwampControllerInnerPbit_Type()
)
twampControllerInnerPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerInnerPbit.setStatus("current")
_TwampControllerRouterEntity_Type = Unsigned32
_TwampControllerRouterEntity_Object = MibTableColumn
twampControllerRouterEntity = _TwampControllerRouterEntity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 12),
    _TwampControllerRouterEntity_Type()
)
twampControllerRouterEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerRouterEntity.setStatus("current")
_TwampControllerLocalAddrType_Type = InetAddressType
_TwampControllerLocalAddrType_Object = MibTableColumn
twampControllerLocalAddrType = _TwampControllerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 13),
    _TwampControllerLocalAddrType_Type()
)
twampControllerLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerLocalAddrType.setStatus("current")
_TwampControllerLocalAddr_Type = InetAddress
_TwampControllerLocalAddr_Object = MibTableColumn
twampControllerLocalAddr = _TwampControllerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 14),
    _TwampControllerLocalAddr_Type()
)
twampControllerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampControllerLocalAddr.setStatus("current")
_TwampControllerAssociatedRI_Type = InterfaceIndexOrZero
_TwampControllerAssociatedRI_Object = MibTableColumn
twampControllerAssociatedRI = _TwampControllerAssociatedRI_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 15),
    _TwampControllerAssociatedRI_Type()
)
twampControllerAssociatedRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampControllerAssociatedRI.setStatus("current")


class _TwampControllerTodStatus_Type(Integer32):
    """Custom type twampControllerTodStatus based on Integer32"""
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
        *(("unknown", 1),
          ("outOfSync", 2),
          ("sync", 3),
          ("notApplicable", 4))
    )


_TwampControllerTodStatus_Type.__name__ = "Integer32"
_TwampControllerTodStatus_Object = MibTableColumn
twampControllerTodStatus = _TwampControllerTodStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 6, 1, 16),
    _TwampControllerTodStatus_Type()
)
twampControllerTodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampControllerTodStatus.setStatus("current")
_TwampPeerTable_Object = MibTable
twampPeerTable = _TwampPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7)
)
if mibBuilder.loadTexts:
    twampPeerTable.setStatus("current")
_TwampPeerEntry_Object = MibTableRow
twampPeerEntry = _TwampPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1)
)
twampPeerEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampControllerId"),
    (0, "RAD-TEST-MIB", "twampPeerAddrType"),
    (0, "RAD-TEST-MIB", "twampPeerAddr"),
)
if mibBuilder.loadTexts:
    twampPeerEntry.setStatus("current")
_TwampPeerAddrType_Type = InetAddressType
_TwampPeerAddrType_Object = MibTableColumn
twampPeerAddrType = _TwampPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 1),
    _TwampPeerAddrType_Type()
)
twampPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampPeerAddrType.setStatus("current")
_TwampPeerAddr_Type = InetAddress
_TwampPeerAddr_Object = MibTableColumn
twampPeerAddr = _TwampPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 2),
    _TwampPeerAddr_Type()
)
twampPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampPeerAddr.setStatus("current")
_TwampPeerRowStatus_Type = RowStatus
_TwampPeerRowStatus_Object = MibTableColumn
twampPeerRowStatus = _TwampPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 3),
    _TwampPeerRowStatus_Type()
)
twampPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPeerRowStatus.setStatus("current")


class _TwampPeerActivateCmd_Type(Integer32):
    """Custom type twampPeerActivateCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_TwampPeerActivateCmd_Type.__name__ = "Integer32"
_TwampPeerActivateCmd_Object = MibTableColumn
twampPeerActivateCmd = _TwampPeerActivateCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 4),
    _TwampPeerActivateCmd_Type()
)
twampPeerActivateCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPeerActivateCmd.setStatus("current")
_TwampPeerActivateDuration_Type = Unsigned32
_TwampPeerActivateDuration_Object = MibTableColumn
twampPeerActivateDuration = _TwampPeerActivateDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 5),
    _TwampPeerActivateDuration_Type()
)
twampPeerActivateDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPeerActivateDuration.setStatus("current")
if mibBuilder.loadTexts:
    twampPeerActivateDuration.setUnits("minutes")
_TwampPeerStartDateAndTime_Type = DateAndTime
_TwampPeerStartDateAndTime_Object = MibTableColumn
twampPeerStartDateAndTime = _TwampPeerStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 6),
    _TwampPeerStartDateAndTime_Type()
)
twampPeerStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampPeerStartDateAndTime.setStatus("current")


class _TwampPeerCalcMode_Type(Integer32):
    """Custom type twampPeerCalcMode based on Integer32"""
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
        *(("roundTrip", 1),
          ("oneWay", 2),
          ("oneWayRadm", 3))
    )


_TwampPeerCalcMode_Type.__name__ = "Integer32"
_TwampPeerCalcMode_Object = MibTableColumn
twampPeerCalcMode = _TwampPeerCalcMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 7),
    _TwampPeerCalcMode_Type()
)
twampPeerCalcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPeerCalcMode.setStatus("current")


class _TwampPeerResponderSeqNum_Type(Integer32):
    """Custom type twampPeerResponderSeqNum based on Integer32"""
    defaultValue = 1

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


_TwampPeerResponderSeqNum_Type.__name__ = "Integer32"
_TwampPeerResponderSeqNum_Object = MibTableColumn
twampPeerResponderSeqNum = _TwampPeerResponderSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 8),
    _TwampPeerResponderSeqNum_Type()
)
twampPeerResponderSeqNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPeerResponderSeqNum.setStatus("current")


class _TwampPeerResponderTodStatus_Type(Integer32):
    """Custom type twampPeerResponderTodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("outOfSync", 2),
          ("sync", 3))
    )


_TwampPeerResponderTodStatus_Type.__name__ = "Integer32"
_TwampPeerResponderTodStatus_Object = MibTableColumn
twampPeerResponderTodStatus = _TwampPeerResponderTodStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 9),
    _TwampPeerResponderTodStatus_Type()
)
twampPeerResponderTodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampPeerResponderTodStatus.setStatus("current")
_TwampPeerElapsedTime_Type = Unsigned32
_TwampPeerElapsedTime_Object = MibTableColumn
twampPeerElapsedTime = _TwampPeerElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 10),
    _TwampPeerElapsedTime_Type()
)
twampPeerElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampPeerElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    twampPeerElapsedTime.setUnits("seconds")


class _TwampPeerDescr_Type(SnmpAdminString):
    """Custom type twampPeerDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TwampPeerDescr_Type.__name__ = "SnmpAdminString"
_TwampPeerDescr_Object = MibTableColumn
twampPeerDescr = _TwampPeerDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 11),
    _TwampPeerDescr_Type()
)
twampPeerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPeerDescr.setStatus("current")


class _TwampPeerLastCalcMode_Type(Integer32):
    """Custom type twampPeerLastCalcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roundTrip", 1),
          ("oneWay", 2),
          ("oneWayRadm", 3))
    )


_TwampPeerLastCalcMode_Type.__name__ = "Integer32"
_TwampPeerLastCalcMode_Object = MibTableColumn
twampPeerLastCalcMode = _TwampPeerLastCalcMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 12),
    _TwampPeerLastCalcMode_Type()
)
twampPeerLastCalcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampPeerLastCalcMode.setStatus("current")


class _TwampPeerLastResponderSeqNum_Type(Integer32):
    """Custom type twampPeerLastResponderSeqNum based on Integer32"""
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


_TwampPeerLastResponderSeqNum_Type.__name__ = "Integer32"
_TwampPeerLastResponderSeqNum_Object = MibTableColumn
twampPeerLastResponderSeqNum = _TwampPeerLastResponderSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 7, 1, 13),
    _TwampPeerLastResponderSeqNum_Type()
)
twampPeerLastResponderSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampPeerLastResponderSeqNum.setStatus("current")
_TwampContSessionTable_Object = MibTable
twampContSessionTable = _TwampContSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8)
)
if mibBuilder.loadTexts:
    twampContSessionTable.setStatus("current")
_TwampContSessionEntry_Object = MibTableRow
twampContSessionEntry = _TwampContSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1)
)
twampContSessionEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampControllerId"),
    (0, "RAD-TEST-MIB", "twampPeerAddrType"),
    (0, "RAD-TEST-MIB", "twampPeerAddr"),
    (0, "RAD-TEST-MIB", "twampContSessionId"),
)
if mibBuilder.loadTexts:
    twampContSessionEntry.setStatus("current")
_TwampContSessionId_Type = Unsigned32
_TwampContSessionId_Object = MibTableColumn
twampContSessionId = _TwampContSessionId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 1),
    _TwampContSessionId_Type()
)
twampContSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampContSessionId.setStatus("current")
_TwampContSessionRowStatus_Type = RowStatus
_TwampContSessionRowStatus_Object = MibTableColumn
twampContSessionRowStatus = _TwampContSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 2),
    _TwampContSessionRowStatus_Type()
)
twampContSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampContSessionRowStatus.setStatus("current")


class _TwampContSessionName_Type(SnmpAdminString):
    """Custom type twampContSessionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TwampContSessionName_Type.__name__ = "SnmpAdminString"
_TwampContSessionName_Object = MibTableColumn
twampContSessionName = _TwampContSessionName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 3),
    _TwampContSessionName_Type()
)
twampContSessionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampContSessionName.setStatus("current")
_TwampContSessionStartDateAndTime_Type = DateAndTime
_TwampContSessionStartDateAndTime_Object = MibTableColumn
twampContSessionStartDateAndTime = _TwampContSessionStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 4),
    _TwampContSessionStartDateAndTime_Type()
)
twampContSessionStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionStartDateAndTime.setStatus("current")


class _TwampContSessionStatus_Type(Integer32):
    """Custom type twampContSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("ready", 3),
          ("inProgress", 4),
          ("completed", 5),
          ("userAborted", 6),
          ("systemAborted", 7))
    )


_TwampContSessionStatus_Type.__name__ = "Integer32"
_TwampContSessionStatus_Object = MibTableColumn
twampContSessionStatus = _TwampContSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 5),
    _TwampContSessionStatus_Type()
)
twampContSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionStatus.setStatus("current")
_TwampContSessionLocalL4PortNumber_Type = InetPortNumber
_TwampContSessionLocalL4PortNumber_Object = MibTableColumn
twampContSessionLocalL4PortNumber = _TwampContSessionLocalL4PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 6),
    _TwampContSessionLocalL4PortNumber_Type()
)
twampContSessionLocalL4PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionLocalL4PortNumber.setStatus("current")
_TwampContSessionPeerL4PortNumber_Type = InetPortNumber
_TwampContSessionPeerL4PortNumber_Object = MibTableColumn
twampContSessionPeerL4PortNumber = _TwampContSessionPeerL4PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 7),
    _TwampContSessionPeerL4PortNumber_Type()
)
twampContSessionPeerL4PortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampContSessionPeerL4PortNumber.setStatus("current")


class _TwampContSessionPeerDscp_Type(Unsigned32):
    """Custom type twampContSessionPeerDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TwampContSessionPeerDscp_Type.__name__ = "Unsigned32"
_TwampContSessionPeerDscp_Object = MibTableColumn
twampContSessionPeerDscp = _TwampContSessionPeerDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 8),
    _TwampContSessionPeerDscp_Type()
)
twampContSessionPeerDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampContSessionPeerDscp.setStatus("current")
_TwampContSessionTestProfileId_Type = Unsigned32
_TwampContSessionTestProfileId_Object = MibTableColumn
twampContSessionTestProfileId = _TwampContSessionTestProfileId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 9),
    _TwampContSessionTestProfileId_Type()
)
twampContSessionTestProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampContSessionTestProfileId.setStatus("current")
_TwampContSessionTxPackets_Type = Counter64
_TwampContSessionTxPackets_Object = MibTableColumn
twampContSessionTxPackets = _TwampContSessionTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 10),
    _TwampContSessionTxPackets_Type()
)
twampContSessionTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionTxPackets.setStatus("current")
_TwampContSessionRxPackets_Type = Counter64
_TwampContSessionRxPackets_Object = MibTableColumn
twampContSessionRxPackets = _TwampContSessionRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 11),
    _TwampContSessionRxPackets_Type()
)
twampContSessionRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionRxPackets.setStatus("current")


class _TwampContSessionResult_Type(Bits):
    """Custom type twampContSessionResult based on Bits"""
    namedValues = NamedValues(
        *(("lossTca", 0),
          ("delayTca", 1),
          ("dvTca", 2))
    )

_TwampContSessionResult_Type.__name__ = "Bits"
_TwampContSessionResult_Object = MibTableColumn
twampContSessionResult = _TwampContSessionResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 12),
    _TwampContSessionResult_Type()
)
twampContSessionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionResult.setStatus("current")
_TwampContSessionConfChanged_Type = TruthValue
_TwampContSessionConfChanged_Object = MibTableColumn
twampContSessionConfChanged = _TwampContSessionConfChanged_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 13),
    _TwampContSessionConfChanged_Type()
)
twampContSessionConfChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionConfChanged.setStatus("current")
_TwampContSessionConvertedIndex_Type = Unsigned32
_TwampContSessionConvertedIndex_Object = MibTableColumn
twampContSessionConvertedIndex = _TwampContSessionConvertedIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 14),
    _TwampContSessionConvertedIndex_Type()
)
twampContSessionConvertedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionConvertedIndex.setStatus("current")


class _TwampContSessionResultFwd_Type(Bits):
    """Custom type twampContSessionResultFwd based on Bits"""
    namedValues = NamedValues(
        *(("lossTca", 0),
          ("delayTca", 1),
          ("dvTca", 2))
    )

_TwampContSessionResultFwd_Type.__name__ = "Bits"
_TwampContSessionResultFwd_Object = MibTableColumn
twampContSessionResultFwd = _TwampContSessionResultFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 15),
    _TwampContSessionResultFwd_Type()
)
twampContSessionResultFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionResultFwd.setStatus("current")


class _TwampContSessionResultBck_Type(Bits):
    """Custom type twampContSessionResultBck based on Bits"""
    namedValues = NamedValues(
        *(("lossTca", 0),
          ("delayTca", 1),
          ("dvTca", 2))
    )

_TwampContSessionResultBck_Type.__name__ = "Bits"
_TwampContSessionResultBck_Object = MibTableColumn
twampContSessionResultBck = _TwampContSessionResultBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 8, 1, 16),
    _TwampContSessionResultBck_Type()
)
twampContSessionResultBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampContSessionResultBck.setStatus("current")
_TwampResponderTable_Object = MibTable
twampResponderTable = _TwampResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9)
)
if mibBuilder.loadTexts:
    twampResponderTable.setStatus("current")
_TwampResponderEntry_Object = MibTableRow
twampResponderEntry = _TwampResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1)
)
twampResponderEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampResponderId"),
)
if mibBuilder.loadTexts:
    twampResponderEntry.setStatus("current")
_TwampResponderId_Type = Unsigned32
_TwampResponderId_Object = MibTableColumn
twampResponderId = _TwampResponderId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 1),
    _TwampResponderId_Type()
)
twampResponderId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampResponderId.setStatus("current")
_TwampResponderRowStatus_Type = RowStatus
_TwampResponderRowStatus_Object = MibTableColumn
twampResponderRowStatus = _TwampResponderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 2),
    _TwampResponderRowStatus_Type()
)
twampResponderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderRowStatus.setStatus("current")


class _TwampResponderName_Type(SnmpAdminString):
    """Custom type twampResponderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TwampResponderName_Type.__name__ = "SnmpAdminString"
_TwampResponderName_Object = MibTableColumn
twampResponderName = _TwampResponderName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 3),
    _TwampResponderName_Type()
)
twampResponderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderName.setStatus("current")


class _TwampResponderStatus_Type(Integer32):
    """Custom type twampResponderStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminOff", 1),
          ("idle", 2),
          ("ready", 3))
    )


_TwampResponderStatus_Type.__name__ = "Integer32"
_TwampResponderStatus_Object = MibTableColumn
twampResponderStatus = _TwampResponderStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 4),
    _TwampResponderStatus_Type()
)
twampResponderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampResponderStatus.setStatus("current")


class _TwampResponderType_Type(Integer32):
    """Custom type twampResponderType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("twamp", 2),
          ("twampLight", 3),
          ("udpEchoPlus", 4))
    )


_TwampResponderType_Type.__name__ = "Integer32"
_TwampResponderType_Object = MibTableColumn
twampResponderType = _TwampResponderType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 5),
    _TwampResponderType_Type()
)
twampResponderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderType.setStatus("current")


class _TwampResponderL2Probe_Type(Integer32):
    """Custom type twampResponderL2Probe based on Integer32"""
    defaultValue = 1

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


_TwampResponderL2Probe_Type.__name__ = "Integer32"
_TwampResponderL2Probe_Object = MibTableColumn
twampResponderL2Probe = _TwampResponderL2Probe_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 6),
    _TwampResponderL2Probe_Type()
)
twampResponderL2Probe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderL2Probe.setStatus("current")
_TwampResponderIngressEgressPort_Type = InterfaceIndexOrZero
_TwampResponderIngressEgressPort_Object = MibTableColumn
twampResponderIngressEgressPort = _TwampResponderIngressEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 7),
    _TwampResponderIngressEgressPort_Type()
)
twampResponderIngressEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderIngressEgressPort.setStatus("current")


class _TwampResponderOuterVlan_Type(Unsigned32):
    """Custom type twampResponderOuterVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TwampResponderOuterVlan_Type.__name__ = "Unsigned32"
_TwampResponderOuterVlan_Object = MibTableColumn
twampResponderOuterVlan = _TwampResponderOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 8),
    _TwampResponderOuterVlan_Type()
)
twampResponderOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderOuterVlan.setStatus("current")


class _TwampResponderInnerVlan_Type(Unsigned32):
    """Custom type twampResponderInnerVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TwampResponderInnerVlan_Type.__name__ = "Unsigned32"
_TwampResponderInnerVlan_Object = MibTableColumn
twampResponderInnerVlan = _TwampResponderInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 9),
    _TwampResponderInnerVlan_Type()
)
twampResponderInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderInnerVlan.setStatus("current")


class _TwampResponderOuterPbit_Type(Unsigned32):
    """Custom type twampResponderOuterPbit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(254, 254),
    )


_TwampResponderOuterPbit_Type.__name__ = "Unsigned32"
_TwampResponderOuterPbit_Object = MibTableColumn
twampResponderOuterPbit = _TwampResponderOuterPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 10),
    _TwampResponderOuterPbit_Type()
)
twampResponderOuterPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderOuterPbit.setStatus("current")


class _TwampResponderInnerPbit_Type(Unsigned32):
    """Custom type twampResponderInnerPbit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(254, 254),
    )


_TwampResponderInnerPbit_Type.__name__ = "Unsigned32"
_TwampResponderInnerPbit_Object = MibTableColumn
twampResponderInnerPbit = _TwampResponderInnerPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 11),
    _TwampResponderInnerPbit_Type()
)
twampResponderInnerPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderInnerPbit.setStatus("current")
_TwampResponderRouterEntity_Type = Unsigned32
_TwampResponderRouterEntity_Object = MibTableColumn
twampResponderRouterEntity = _TwampResponderRouterEntity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 12),
    _TwampResponderRouterEntity_Type()
)
twampResponderRouterEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderRouterEntity.setStatus("current")
_TwampResponderLocalAddrType_Type = InetAddressType
_TwampResponderLocalAddrType_Object = MibTableColumn
twampResponderLocalAddrType = _TwampResponderLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 13),
    _TwampResponderLocalAddrType_Type()
)
twampResponderLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderLocalAddrType.setStatus("current")
_TwampResponderLocalAddr_Type = InetAddress
_TwampResponderLocalAddr_Object = MibTableColumn
twampResponderLocalAddr = _TwampResponderLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 14),
    _TwampResponderLocalAddr_Type()
)
twampResponderLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderLocalAddr.setStatus("current")
_TwampResponderAssociatedRI_Type = InterfaceIndexOrZero
_TwampResponderAssociatedRI_Object = MibTableColumn
twampResponderAssociatedRI = _TwampResponderAssociatedRI_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 15),
    _TwampResponderAssociatedRI_Type()
)
twampResponderAssociatedRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampResponderAssociatedRI.setStatus("current")


class _TwampResponderTxSeqNum_Type(Integer32):
    """Custom type twampResponderTxSeqNum based on Integer32"""
    defaultValue = 1

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


_TwampResponderTxSeqNum_Type.__name__ = "Integer32"
_TwampResponderTxSeqNum_Object = MibTableColumn
twampResponderTxSeqNum = _TwampResponderTxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 16),
    _TwampResponderTxSeqNum_Type()
)
twampResponderTxSeqNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderTxSeqNum.setStatus("current")


class _TwampResponderTxExtendedInfo_Type(Integer32):
    """Custom type twampResponderTxExtendedInfo based on Integer32"""
    defaultValue = 1

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


_TwampResponderTxExtendedInfo_Type.__name__ = "Integer32"
_TwampResponderTxExtendedInfo_Object = MibTableColumn
twampResponderTxExtendedInfo = _TwampResponderTxExtendedInfo_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 9, 1, 17),
    _TwampResponderTxExtendedInfo_Type()
)
twampResponderTxExtendedInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResponderTxExtendedInfo.setStatus("current")
_TwampResSessionTable_Object = MibTable
twampResSessionTable = _TwampResSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10)
)
if mibBuilder.loadTexts:
    twampResSessionTable.setStatus("current")
_TwampResSessionEntry_Object = MibTableRow
twampResSessionEntry = _TwampResSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1)
)
twampResSessionEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampResponderId"),
    (0, "RAD-TEST-MIB", "twampResSessionId"),
)
if mibBuilder.loadTexts:
    twampResSessionEntry.setStatus("current")
_TwampResSessionId_Type = Unsigned32
_TwampResSessionId_Object = MibTableColumn
twampResSessionId = _TwampResSessionId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1, 1),
    _TwampResSessionId_Type()
)
twampResSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampResSessionId.setStatus("current")
_TwampResSessionRowStatus_Type = RowStatus
_TwampResSessionRowStatus_Object = MibTableColumn
twampResSessionRowStatus = _TwampResSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1, 2),
    _TwampResSessionRowStatus_Type()
)
twampResSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResSessionRowStatus.setStatus("current")


class _TwampResSessionName_Type(SnmpAdminString):
    """Custom type twampResSessionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TwampResSessionName_Type.__name__ = "SnmpAdminString"
_TwampResSessionName_Object = MibTableColumn
twampResSessionName = _TwampResSessionName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1, 3),
    _TwampResSessionName_Type()
)
twampResSessionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResSessionName.setStatus("current")
_TwampResSessionLocalL4PortNumber_Type = InetPortNumber
_TwampResSessionLocalL4PortNumber_Object = MibTableColumn
twampResSessionLocalL4PortNumber = _TwampResSessionLocalL4PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1, 4),
    _TwampResSessionLocalL4PortNumber_Type()
)
twampResSessionLocalL4PortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampResSessionLocalL4PortNumber.setStatus("current")
_TwampResSessionTxPackets_Type = Counter64
_TwampResSessionTxPackets_Object = MibTableColumn
twampResSessionTxPackets = _TwampResSessionTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1, 5),
    _TwampResSessionTxPackets_Type()
)
twampResSessionTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampResSessionTxPackets.setStatus("current")
_TwampResSessionRxPackets_Type = Counter64
_TwampResSessionRxPackets_Object = MibTableColumn
twampResSessionRxPackets = _TwampResSessionRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 10, 1, 6),
    _TwampResSessionRxPackets_Type()
)
twampResSessionRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampResSessionRxPackets.setStatus("current")
_ItuSatSingleCosFlowTable_Object = MibTable
ituSatSingleCosFlowTable = _ItuSatSingleCosFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15)
)
if mibBuilder.loadTexts:
    ituSatSingleCosFlowTable.setStatus("current")
_ItuSatSingleCosFlowEntry_Object = MibTableRow
ituSatSingleCosFlowEntry = _ItuSatSingleCosFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15, 1)
)
ituSatSingleCosFlowEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatSingleCosFlowFunction"),
    (0, "RAD-TEST-MIB", "ituSatSingleCosFlowFunctionIndex"),
    (0, "RAD-TEST-MIB", "ituSatSingleCosFlowIdx1"),
    (0, "RAD-TEST-MIB", "ituSatSingleCosFlowIdx2"),
)
if mibBuilder.loadTexts:
    ituSatSingleCosFlowEntry.setStatus("current")


class _ItuSatSingleCosFlowFunction_Type(Integer32):
    """Custom type ituSatSingleCosFlowFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generator", 1),
          ("responder", 2))
    )


_ItuSatSingleCosFlowFunction_Type.__name__ = "Integer32"
_ItuSatSingleCosFlowFunction_Object = MibTableColumn
ituSatSingleCosFlowFunction = _ItuSatSingleCosFlowFunction_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15, 1, 1),
    _ItuSatSingleCosFlowFunction_Type()
)
ituSatSingleCosFlowFunction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatSingleCosFlowFunction.setStatus("current")
_ItuSatSingleCosFlowFunctionIndex_Type = Unsigned32
_ItuSatSingleCosFlowFunctionIndex_Object = MibTableColumn
ituSatSingleCosFlowFunctionIndex = _ItuSatSingleCosFlowFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15, 1, 2),
    _ItuSatSingleCosFlowFunctionIndex_Type()
)
ituSatSingleCosFlowFunctionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatSingleCosFlowFunctionIndex.setStatus("current")
_ItuSatSingleCosFlowIdx1_Type = Unsigned32
_ItuSatSingleCosFlowIdx1_Object = MibTableColumn
ituSatSingleCosFlowIdx1 = _ItuSatSingleCosFlowIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15, 1, 3),
    _ItuSatSingleCosFlowIdx1_Type()
)
ituSatSingleCosFlowIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatSingleCosFlowIdx1.setStatus("current")
_ItuSatSingleCosFlowIdx2_Type = Unsigned32
_ItuSatSingleCosFlowIdx2_Object = MibTableColumn
ituSatSingleCosFlowIdx2 = _ItuSatSingleCosFlowIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15, 1, 4),
    _ItuSatSingleCosFlowIdx2_Type()
)
ituSatSingleCosFlowIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatSingleCosFlowIdx2.setStatus("current")
_ItuSatSingleCosFlowRowStatus_Type = RowStatus
_ItuSatSingleCosFlowRowStatus_Object = MibTableColumn
ituSatSingleCosFlowRowStatus = _ItuSatSingleCosFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 15, 1, 5),
    _ItuSatSingleCosFlowRowStatus_Type()
)
ituSatSingleCosFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ituSatSingleCosFlowRowStatus.setStatus("current")
_RadTestPerfRepResults_ObjectIdentity = ObjectIdentity
radTestPerfRepResults = _RadTestPerfRepResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3)
)
_TstNePerfRepGeneralResultsTable_Object = MibTable
tstNePerfRepGeneralResultsTable = _TstNePerfRepGeneralResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    tstNePerfRepGeneralResultsTable.setStatus("current")
_TstNePerfRepGeneralResultsEntry_Object = MibTableRow
tstNePerfRepGeneralResultsEntry = _TstNePerfRepGeneralResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 1, 1)
)
tstNePerfRepGeneralResultsEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
    (0, "RAD-TEST-MIB", "tstNePerfRepIteration"),
    (0, "RAD-TEST-MIB", "tstNePerfRepGeneralResultsTestType"),
    (0, "RAD-TEST-MIB", "tstNePerfRepGeneralResultsTrialNumber"),
)
if mibBuilder.loadTexts:
    tstNePerfRepGeneralResultsEntry.setStatus("current")


class _TstNePerfRepGeneralResultsTestType_Type(Integer32):
    """Custom type tstNePerfRepGeneralResultsTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("throughput", 1),
          ("frameloss", 2),
          ("latency", 3))
    )


_TstNePerfRepGeneralResultsTestType_Type.__name__ = "Integer32"
_TstNePerfRepGeneralResultsTestType_Object = MibTableColumn
tstNePerfRepGeneralResultsTestType = _TstNePerfRepGeneralResultsTestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 1, 1, 1),
    _TstNePerfRepGeneralResultsTestType_Type()
)
tstNePerfRepGeneralResultsTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepGeneralResultsTestType.setStatus("current")
_TstNePerfRepGeneralResultsTrialNumber_Type = Unsigned32
_TstNePerfRepGeneralResultsTrialNumber_Object = MibTableColumn
tstNePerfRepGeneralResultsTrialNumber = _TstNePerfRepGeneralResultsTrialNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 1, 1, 2),
    _TstNePerfRepGeneralResultsTrialNumber_Type()
)
tstNePerfRepGeneralResultsTrialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tstNePerfRepGeneralResultsTrialNumber.setStatus("current")


class _TstNePerfRepGeneralResultsStatus_Type(Integer32):
    """Custom type tstNePerfRepGeneralResultsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2),
          ("linkDown", 3),
          ("oamConnectivityFailure", 4),
          ("timeOut", 5),
          ("notApplicable", 255))
    )


_TstNePerfRepGeneralResultsStatus_Type.__name__ = "Integer32"
_TstNePerfRepGeneralResultsStatus_Object = MibTableColumn
tstNePerfRepGeneralResultsStatus = _TstNePerfRepGeneralResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 1, 1, 3),
    _TstNePerfRepGeneralResultsStatus_Type()
)
tstNePerfRepGeneralResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepGeneralResultsStatus.setStatus("current")
_TstNePerfRepGeneralResultsDuration_Type = TimeTicks
_TstNePerfRepGeneralResultsDuration_Object = MibTableColumn
tstNePerfRepGeneralResultsDuration = _TstNePerfRepGeneralResultsDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 1, 1, 4),
    _TstNePerfRepGeneralResultsDuration_Type()
)
tstNePerfRepGeneralResultsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepGeneralResultsDuration.setStatus("current")
_ThroughputReportTable_Object = MibTable
throughputReportTable = _ThroughputReportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2)
)
if mibBuilder.loadTexts:
    throughputReportTable.setStatus("current")
_ThroughputReportEntry_Object = MibTableRow
throughputReportEntry = _ThroughputReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1)
)
throughputReportEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
    (0, "RAD-TEST-MIB", "tstNePerfRepIteration"),
    (0, "RAD-TEST-MIB", "throughputReportTrialNumber"),
    (0, "RAD-TEST-MIB", "throughputReportPacketSize"),
)
if mibBuilder.loadTexts:
    throughputReportEntry.setStatus("current")
_ThroughputReportTrialNumber_Type = Unsigned32
_ThroughputReportTrialNumber_Object = MibTableColumn
throughputReportTrialNumber = _ThroughputReportTrialNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 1),
    _ThroughputReportTrialNumber_Type()
)
throughputReportTrialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    throughputReportTrialNumber.setStatus("current")
_ThroughputReportPacketSize_Type = RadTestPerfresultFrameSize
_ThroughputReportPacketSize_Object = MibTableColumn
throughputReportPacketSize = _ThroughputReportPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 2),
    _ThroughputReportPacketSize_Type()
)
throughputReportPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    throughputReportPacketSize.setStatus("current")
_ThroughputReportThroughputTheoretical_Type = Gauge32
_ThroughputReportThroughputTheoretical_Object = MibTableColumn
throughputReportThroughputTheoretical = _ThroughputReportThroughputTheoretical_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 3),
    _ThroughputReportThroughputTheoretical_Type()
)
throughputReportThroughputTheoretical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    throughputReportThroughputTheoretical.setStatus("current")
_ThroughputReportResults_Type = Gauge32
_ThroughputReportResults_Object = MibTableColumn
throughputReportResults = _ThroughputReportResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 4),
    _ThroughputReportResults_Type()
)
throughputReportResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    throughputReportResults.setStatus("current")


class _ThroughputReportDataPattern_Type(Integer32):
    """Custom type throughputReportDataPattern based on Integer32"""
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
        *(("notApplicable", 1),
          ("allOnes", 2),
          ("allZerosWithoutCrc", 3),
          ("allZerosWithCrc", 4),
          ("alternate", 5),
          ("prbsWithCrc", 6),
          ("prbsWithoutCrc", 7))
    )


_ThroughputReportDataPattern_Type.__name__ = "Integer32"
_ThroughputReportDataPattern_Object = MibTableColumn
throughputReportDataPattern = _ThroughputReportDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 5),
    _ThroughputReportDataPattern_Type()
)
throughputReportDataPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    throughputReportDataPattern.setStatus("current")
_ThroughputReportResultsBps_Type = Gauge32
_ThroughputReportResultsBps_Object = MibTableColumn
throughputReportResultsBps = _ThroughputReportResultsBps_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 6),
    _ThroughputReportResultsBps_Type()
)
throughputReportResultsBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    throughputReportResultsBps.setStatus("current")
_ThroughputReportCustomPacketSize_Type = Unsigned32
_ThroughputReportCustomPacketSize_Object = MibTableColumn
throughputReportCustomPacketSize = _ThroughputReportCustomPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 2, 1, 7),
    _ThroughputReportCustomPacketSize_Type()
)
throughputReportCustomPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    throughputReportCustomPacketSize.setStatus("current")
_LatencyReportTable_Object = MibTable
latencyReportTable = _LatencyReportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3)
)
if mibBuilder.loadTexts:
    latencyReportTable.setStatus("current")
_LatencyReportEntry_Object = MibTableRow
latencyReportEntry = _LatencyReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3, 1)
)
latencyReportEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
    (0, "RAD-TEST-MIB", "tstNePerfRepIteration"),
    (0, "RAD-TEST-MIB", "latencyReportTrialNumber"),
    (0, "RAD-TEST-MIB", "latencyReportPacketSize"),
)
if mibBuilder.loadTexts:
    latencyReportEntry.setStatus("current")
_LatencyReportTrialNumber_Type = Unsigned32
_LatencyReportTrialNumber_Object = MibTableColumn
latencyReportTrialNumber = _LatencyReportTrialNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3, 1, 1),
    _LatencyReportTrialNumber_Type()
)
latencyReportTrialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    latencyReportTrialNumber.setStatus("current")
_LatencyReportPacketSize_Type = RadTestPerfresultFrameSize
_LatencyReportPacketSize_Object = MibTableColumn
latencyReportPacketSize = _LatencyReportPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3, 1, 2),
    _LatencyReportPacketSize_Type()
)
latencyReportPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    latencyReportPacketSize.setStatus("current")


class _LatencyReportType_Type(Integer32):
    """Custom type latencyReportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("storeAndForward", 1),
          ("bitForwarding", 2))
    )


_LatencyReportType_Type.__name__ = "Integer32"
_LatencyReportType_Object = MibTableColumn
latencyReportType = _LatencyReportType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3, 1, 3),
    _LatencyReportType_Type()
)
latencyReportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyReportType.setStatus("current")
_LatencyReportResult_Type = Gauge32
_LatencyReportResult_Object = MibTableColumn
latencyReportResult = _LatencyReportResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3, 1, 4),
    _LatencyReportResult_Type()
)
latencyReportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyReportResult.setStatus("current")
if mibBuilder.loadTexts:
    latencyReportResult.setUnits("micro seconds")
_LatencyReportCustomPacketSize_Type = Unsigned32
_LatencyReportCustomPacketSize_Object = MibTableColumn
latencyReportCustomPacketSize = _LatencyReportCustomPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 3, 1, 5),
    _LatencyReportCustomPacketSize_Type()
)
latencyReportCustomPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    latencyReportCustomPacketSize.setStatus("current")
_FramelossRateReportTable_Object = MibTable
framelossRateReportTable = _FramelossRateReportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4)
)
if mibBuilder.loadTexts:
    framelossRateReportTable.setStatus("current")
_FramelossRateReportEntry_Object = MibTableRow
framelossRateReportEntry = _FramelossRateReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4, 1)
)
framelossRateReportEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
    (0, "RAD-TEST-MIB", "tstNePerfRepIteration"),
    (0, "RAD-TEST-MIB", "framelossRateReportTrialNumber"),
    (0, "RAD-TEST-MIB", "framelossRateReportPacketSize"),
    (0, "RAD-TEST-MIB", "framelossRateReportInputRate"),
)
if mibBuilder.loadTexts:
    framelossRateReportEntry.setStatus("current")
_FramelossRateReportTrialNumber_Type = Unsigned32
_FramelossRateReportTrialNumber_Object = MibTableColumn
framelossRateReportTrialNumber = _FramelossRateReportTrialNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4, 1, 1),
    _FramelossRateReportTrialNumber_Type()
)
framelossRateReportTrialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    framelossRateReportTrialNumber.setStatus("current")
_FramelossRateReportPacketSize_Type = RadTestPerfresultFrameSize
_FramelossRateReportPacketSize_Object = MibTableColumn
framelossRateReportPacketSize = _FramelossRateReportPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4, 1, 2),
    _FramelossRateReportPacketSize_Type()
)
framelossRateReportPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    framelossRateReportPacketSize.setStatus("current")
_FramelossRateReportInputRate_Type = Unsigned32
_FramelossRateReportInputRate_Object = MibTableColumn
framelossRateReportInputRate = _FramelossRateReportInputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4, 1, 3),
    _FramelossRateReportInputRate_Type()
)
framelossRateReportInputRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    framelossRateReportInputRate.setStatus("current")
_FramelossRateReportResults_Type = Gauge32
_FramelossRateReportResults_Object = MibTableColumn
framelossRateReportResults = _FramelossRateReportResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4, 1, 4),
    _FramelossRateReportResults_Type()
)
framelossRateReportResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    framelossRateReportResults.setStatus("current")
_FramelossRateReportCustomPacketSize_Type = Unsigned32
_FramelossRateReportCustomPacketSize_Object = MibTableColumn
framelossRateReportCustomPacketSize = _FramelossRateReportCustomPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 4, 1, 5),
    _FramelossRateReportCustomPacketSize_Type()
)
framelossRateReportCustomPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    framelossRateReportCustomPacketSize.setStatus("current")
_TstNePerfRepStatusTable_Object = MibTable
tstNePerfRepStatusTable = _TstNePerfRepStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5)
)
if mibBuilder.loadTexts:
    tstNePerfRepStatusTable.setStatus("current")
_TstNePerfRepStatusEntry_Object = MibTableRow
tstNePerfRepStatusEntry = _TstNePerfRepStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1)
)
tstNePerfRepStatusEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
    (0, "RAD-TEST-MIB", "tstNePerfRepIteration"),
)
if mibBuilder.loadTexts:
    tstNePerfRepStatusEntry.setStatus("current")
_TstNePerfRepIteration_Type = Unsigned32
_TstNePerfRepIteration_Object = MibTableColumn
tstNePerfRepIteration = _TstNePerfRepIteration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 1),
    _TstNePerfRepIteration_Type()
)
tstNePerfRepIteration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepIteration.setStatus("current")
_TstNePerfRepStartTime_Type = DateAndTime
_TstNePerfRepStartTime_Object = MibTableColumn
tstNePerfRepStartTime = _TstNePerfRepStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 2),
    _TstNePerfRepStartTime_Type()
)
tstNePerfRepStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepStartTime.setStatus("current")
_TstNePerfRepDuration_Type = TimeTicks
_TstNePerfRepDuration_Object = MibTableColumn
tstNePerfRepDuration = _TstNePerfRepDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 3),
    _TstNePerfRepDuration_Type()
)
tstNePerfRepDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepDuration.setStatus("current")


class _TstNePerfRepStatus_Type(Integer32):
    """Custom type tstNePerfRepStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("success", 3),
          ("fail", 4),
          ("oamConnectivityFailure", 5),
          ("other", 6),
          ("timeOut", 7),
          ("pending", 8))
    )


_TstNePerfRepStatus_Type.__name__ = "Integer32"
_TstNePerfRepStatus_Object = MibTableColumn
tstNePerfRepStatus = _TstNePerfRepStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 4),
    _TstNePerfRepStatus_Type()
)
tstNePerfRepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepStatus.setStatus("current")


class _TstNePerfRepType_Type(Integer32):
    """Custom type tstNePerfRepType based on Integer32"""
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
        *(("notApplicable", 1),
          ("throughput", 2),
          ("frameloss", 3),
          ("latency", 4))
    )


_TstNePerfRepType_Type.__name__ = "Integer32"
_TstNePerfRepType_Object = MibTableColumn
tstNePerfRepType = _TstNePerfRepType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 5),
    _TstNePerfRepType_Type()
)
tstNePerfRepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepType.setStatus("current")
_TstNePerfRepIterationNum_Type = Unsigned32
_TstNePerfRepIterationNum_Object = MibTableColumn
tstNePerfRepIterationNum = _TstNePerfRepIterationNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 6),
    _TstNePerfRepIterationNum_Type()
)
tstNePerfRepIterationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepIterationNum.setStatus("current")
_TstNePerfRepTrial_Type = Unsigned32
_TstNePerfRepTrial_Object = MibTableColumn
tstNePerfRepTrial = _TstNePerfRepTrial_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 7),
    _TstNePerfRepTrial_Type()
)
tstNePerfRepTrial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepTrial.setStatus("current")
_TstNePerfRepAttemptNum_Type = Unsigned32
_TstNePerfRepAttemptNum_Object = MibTableColumn
tstNePerfRepAttemptNum = _TstNePerfRepAttemptNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 8),
    _TstNePerfRepAttemptNum_Type()
)
tstNePerfRepAttemptNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepAttemptNum.setStatus("current")
_TstNePerfRepFrameSize_Type = Unsigned32
_TstNePerfRepFrameSize_Object = MibTableColumn
tstNePerfRepFrameSize = _TstNePerfRepFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 9),
    _TstNePerfRepFrameSize_Type()
)
tstNePerfRepFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepFrameSize.setStatus("current")
_TstNePerfRepLatencyNum_Type = Unsigned32
_TstNePerfRepLatencyNum_Object = MibTableColumn
tstNePerfRepLatencyNum = _TstNePerfRepLatencyNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 5, 1, 10),
    _TstNePerfRepLatencyNum_Type()
)
tstNePerfRepLatencyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNePerfRepLatencyNum.setStatus("current")
_ItuSatReportTable_Object = MibTable
ituSatReportTable = _ItuSatReportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6)
)
if mibBuilder.loadTexts:
    ituSatReportTable.setStatus("current")
_ItuSatReportEntry_Object = MibTableRow
ituSatReportEntry = _ItuSatReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1)
)
ituSatReportEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatGeneratorIndex"),
    (0, "RAD-TEST-MIB", "ituSatReportPbitIndex"),
    (0, "RAD-TEST-MIB", "ituSatReportTestTypeIndex"),
    (0, "RAD-TEST-MIB", "ituSatReportDirectionIndex"),
)
if mibBuilder.loadTexts:
    ituSatReportEntry.setStatus("current")
_ItuSatReportPbitIndex_Type = RadTestPbitIndex
_ItuSatReportPbitIndex_Object = MibTableColumn
ituSatReportPbitIndex = _ItuSatReportPbitIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 1),
    _ItuSatReportPbitIndex_Type()
)
ituSatReportPbitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatReportPbitIndex.setStatus("current")


class _ItuSatReportTestTypeIndex_Type(Integer32):
    """Custom type ituSatReportTestTypeIndex based on Integer32"""
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
        *(("cirStep1", 1),
          ("cirStep2", 2),
          ("cirStep3", 3),
          ("cirStep4", 4),
          ("eir", 5),
          ("policing", 6),
          ("performance", 7))
    )


_ItuSatReportTestTypeIndex_Type.__name__ = "Integer32"
_ItuSatReportTestTypeIndex_Object = MibTableColumn
ituSatReportTestTypeIndex = _ItuSatReportTestTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 2),
    _ItuSatReportTestTypeIndex_Type()
)
ituSatReportTestTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatReportTestTypeIndex.setStatus("current")


class _ItuSatReportDirectionIndex_Type(Integer32):
    """Custom type ituSatReportDirectionIndex based on Integer32"""
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
          ("backward", 2),
          ("roundTrip", 3))
    )


_ItuSatReportDirectionIndex_Type.__name__ = "Integer32"
_ItuSatReportDirectionIndex_Object = MibTableColumn
ituSatReportDirectionIndex = _ItuSatReportDirectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 3),
    _ItuSatReportDirectionIndex_Type()
)
ituSatReportDirectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatReportDirectionIndex.setStatus("current")
_ItuSatReportResult_Type = RadTestResult
_ItuSatReportResult_Object = MibTableColumn
ituSatReportResult = _ItuSatReportResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 4),
    _ItuSatReportResult_Type()
)
ituSatReportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportResult.setStatus("current")
_ItuSatReportTxRate_Type = Gauge32
_ItuSatReportTxRate_Object = MibTableColumn
ituSatReportTxRate = _ItuSatReportTxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 5),
    _ItuSatReportTxRate_Type()
)
ituSatReportTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportTxRate.setUnits("Kbps")
_ItuSatReportIrMin_Type = Gauge32
_ItuSatReportIrMin_Object = MibTableColumn
ituSatReportIrMin = _ItuSatReportIrMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 6),
    _ItuSatReportIrMin_Type()
)
ituSatReportIrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportIrMin.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportIrMin.setUnits("Kbps")
_ItuSatReportIrAverage_Type = Gauge32
_ItuSatReportIrAverage_Object = MibTableColumn
ituSatReportIrAverage = _ItuSatReportIrAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 7),
    _ItuSatReportIrAverage_Type()
)
ituSatReportIrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportIrAverage.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportIrAverage.setUnits("Kbps")
_ItuSatReportIrMax_Type = Gauge32
_ItuSatReportIrMax_Object = MibTableColumn
ituSatReportIrMax = _ItuSatReportIrMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 8),
    _ItuSatReportIrMax_Type()
)
ituSatReportIrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportIrMax.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportIrMax.setUnits("Kbps")
_ItuSatReportTxFrames_Type = Counter64
_ItuSatReportTxFrames_Object = MibTableColumn
ituSatReportTxFrames = _ItuSatReportTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 9),
    _ItuSatReportTxFrames_Type()
)
ituSatReportTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportTxFrames.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportTxFrames.setUnits("frames")
_ItuSatReportLostFrames_Type = Counter64
_ItuSatReportLostFrames_Object = MibTableColumn
ituSatReportLostFrames = _ItuSatReportLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 10),
    _ItuSatReportLostFrames_Type()
)
ituSatReportLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportLostFrames.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportLostFrames.setUnits("frames")
_ItuSatReportFtdMin_Type = Gauge32
_ItuSatReportFtdMin_Object = MibTableColumn
ituSatReportFtdMin = _ItuSatReportFtdMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 11),
    _ItuSatReportFtdMin_Type()
)
ituSatReportFtdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportFtdMin.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportFtdMin.setUnits("micro seconds")
_ItuSatReportFtdAverage_Type = Gauge32
_ItuSatReportFtdAverage_Object = MibTableColumn
ituSatReportFtdAverage = _ItuSatReportFtdAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 12),
    _ItuSatReportFtdAverage_Type()
)
ituSatReportFtdAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportFtdAverage.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportFtdAverage.setUnits("micro seconds")
_ItuSatReportFtdMax_Type = Gauge32
_ItuSatReportFtdMax_Object = MibTableColumn
ituSatReportFtdMax = _ItuSatReportFtdMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 13),
    _ItuSatReportFtdMax_Type()
)
ituSatReportFtdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportFtdMax.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportFtdMax.setUnits("micro seconds")
_ItuSatReportFtdStd_Type = Gauge32
_ItuSatReportFtdStd_Object = MibTableColumn
ituSatReportFtdStd = _ItuSatReportFtdStd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 14),
    _ItuSatReportFtdStd_Type()
)
ituSatReportFtdStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportFtdStd.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportFtdStd.setUnits("micro seconds")
_ItuSatReportFdvAverage_Type = Gauge32
_ItuSatReportFdvAverage_Object = MibTableColumn
ituSatReportFdvAverage = _ItuSatReportFdvAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 15),
    _ItuSatReportFdvAverage_Type()
)
ituSatReportFdvAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportFdvAverage.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportFdvAverage.setUnits("micro seconds")
_ItuSatReportFdvMax_Type = Gauge32
_ItuSatReportFdvMax_Object = MibTableColumn
ituSatReportFdvMax = _ItuSatReportFdvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 16),
    _ItuSatReportFdvMax_Type()
)
ituSatReportFdvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportFdvMax.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportFdvMax.setUnits("micro seconds")
_ItuSatReportUas_Type = Counter32
_ItuSatReportUas_Object = MibTableColumn
ituSatReportUas = _ItuSatReportUas_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 17),
    _ItuSatReportUas_Type()
)
ituSatReportUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportUas.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportUas.setUnits("seconds")


class _ItuSatReportAvailability_Type(Unsigned32):
    """Custom type ituSatReportAvailability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ItuSatReportAvailability_Type.__name__ = "Unsigned32"
_ItuSatReportAvailability_Object = MibTableColumn
ituSatReportAvailability = _ItuSatReportAvailability_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 18),
    _ItuSatReportAvailability_Type()
)
ituSatReportAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportAvailability.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportAvailability.setUnits("hundredth of percent")
_ItuSatReportTotalTxRate_Type = Gauge32
_ItuSatReportTotalTxRate_Object = MibTableColumn
ituSatReportTotalTxRate = _ItuSatReportTotalTxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 19),
    _ItuSatReportTotalTxRate_Type()
)
ituSatReportTotalTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportTotalTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportTotalTxRate.setUnits("kbps")
_ItuSatReportTotalIrAverage_Type = Gauge32
_ItuSatReportTotalIrAverage_Object = MibTableColumn
ituSatReportTotalIrAverage = _ItuSatReportTotalIrAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 20),
    _ItuSatReportTotalIrAverage_Type()
)
ituSatReportTotalIrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportTotalIrAverage.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportTotalIrAverage.setUnits("kbps")
_ItuSatReportTotalTxFrames_Type = Counter64
_ItuSatReportTotalTxFrames_Object = MibTableColumn
ituSatReportTotalTxFrames = _ItuSatReportTotalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 21),
    _ItuSatReportTotalTxFrames_Type()
)
ituSatReportTotalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportTotalTxFrames.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportTotalTxFrames.setUnits("frames")
_ItuSatReportTotalLostFrames_Type = Counter64
_ItuSatReportTotalLostFrames_Object = MibTableColumn
ituSatReportTotalLostFrames = _ItuSatReportTotalLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 6, 1, 22),
    _ItuSatReportTotalLostFrames_Type()
)
ituSatReportTotalLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatReportTotalLostFrames.setStatus("current")
if mibBuilder.loadTexts:
    ituSatReportTotalLostFrames.setUnits("frames")
_ItuSatResponderPerfTable_Object = MibTable
ituSatResponderPerfTable = _ItuSatResponderPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7)
)
if mibBuilder.loadTexts:
    ituSatResponderPerfTable.setStatus("current")
_ItuSatResponderPerfEntry_Object = MibTableRow
ituSatResponderPerfEntry = _ItuSatResponderPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7, 1)
)
ituSatResponderPerfEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatResponderIndex"),
    (0, "RAD-TEST-MIB", "ituSatResponderPerfPbitIndex"),
)
if mibBuilder.loadTexts:
    ituSatResponderPerfEntry.setStatus("current")
_ItuSatResponderPerfPbitIndex_Type = RadTestPbitIndex
_ItuSatResponderPerfPbitIndex_Object = MibTableColumn
ituSatResponderPerfPbitIndex = _ItuSatResponderPerfPbitIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7, 1, 1),
    _ItuSatResponderPerfPbitIndex_Type()
)
ituSatResponderPerfPbitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatResponderPerfPbitIndex.setStatus("current")
_ItuSatResponderPerfRxFrames_Type = Counter64
_ItuSatResponderPerfRxFrames_Object = MibTableColumn
ituSatResponderPerfRxFrames = _ItuSatResponderPerfRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7, 1, 2),
    _ItuSatResponderPerfRxFrames_Type()
)
ituSatResponderPerfRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatResponderPerfRxFrames.setStatus("current")
_ItuSatResponderPerfTxFrames_Type = Counter64
_ItuSatResponderPerfTxFrames_Object = MibTableColumn
ituSatResponderPerfTxFrames = _ItuSatResponderPerfTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7, 1, 3),
    _ItuSatResponderPerfTxFrames_Type()
)
ituSatResponderPerfTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatResponderPerfTxFrames.setStatus("current")


class _ItuSatResponderPerfAssociatedMEP_Type(Unsigned32):
    """Custom type ituSatResponderPerfAssociatedMEP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_ItuSatResponderPerfAssociatedMEP_Type.__name__ = "Unsigned32"
_ItuSatResponderPerfAssociatedMEP_Object = MibTableColumn
ituSatResponderPerfAssociatedMEP = _ItuSatResponderPerfAssociatedMEP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7, 1, 4),
    _ItuSatResponderPerfAssociatedMEP_Type()
)
ituSatResponderPerfAssociatedMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatResponderPerfAssociatedMEP.setStatus("current")


class _ItuSatResponderPerfAssociatedService_Type(Unsigned32):
    """Custom type ituSatResponderPerfAssociatedService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ItuSatResponderPerfAssociatedService_Type.__name__ = "Unsigned32"
_ItuSatResponderPerfAssociatedService_Object = MibTableColumn
ituSatResponderPerfAssociatedService = _ItuSatResponderPerfAssociatedService_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 7, 1, 5),
    _ItuSatResponderPerfAssociatedService_Type()
)
ituSatResponderPerfAssociatedService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatResponderPerfAssociatedService.setStatus("current")
_ItuSatConfPbitTable_Object = MibTable
ituSatConfPbitTable = _ItuSatConfPbitTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 8)
)
if mibBuilder.loadTexts:
    ituSatConfPbitTable.setStatus("current")
_ItuSatConfPbitEntry_Object = MibTableRow
ituSatConfPbitEntry = _ItuSatConfPbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 8, 1)
)
ituSatConfPbitEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "ituSatGeneratorIndex"),
    (0, "RAD-TEST-MIB", "ituSatConfPbitIndex"),
    (0, "RAD-TEST-MIB", "ituSatConfPbitDirectionIndex"),
)
if mibBuilder.loadTexts:
    ituSatConfPbitEntry.setStatus("current")
_ItuSatConfPbitIndex_Type = RadTestPbitIndex
_ItuSatConfPbitIndex_Object = MibTableColumn
ituSatConfPbitIndex = _ItuSatConfPbitIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 8, 1, 1),
    _ItuSatConfPbitIndex_Type()
)
ituSatConfPbitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatConfPbitIndex.setStatus("current")


class _ItuSatConfPbitDirectionIndex_Type(Integer32):
    """Custom type ituSatConfPbitDirectionIndex based on Integer32"""
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
          ("backward", 2),
          ("roundTrip", 3))
    )


_ItuSatConfPbitDirectionIndex_Type.__name__ = "Integer32"
_ItuSatConfPbitDirectionIndex_Object = MibTableColumn
ituSatConfPbitDirectionIndex = _ItuSatConfPbitDirectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 8, 1, 2),
    _ItuSatConfPbitDirectionIndex_Type()
)
ituSatConfPbitDirectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituSatConfPbitDirectionIndex.setStatus("current")
_ItuSatConfPbitResult_Type = RadTestResult
_ItuSatConfPbitResult_Object = MibTableColumn
ituSatConfPbitResult = _ItuSatConfPbitResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 8, 1, 3),
    _ItuSatConfPbitResult_Type()
)
ituSatConfPbitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituSatConfPbitResult.setStatus("current")
_TwampReportCurrentTable_Object = MibTable
twampReportCurrentTable = _TwampReportCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9)
)
if mibBuilder.loadTexts:
    twampReportCurrentTable.setStatus("current")
_TwampReportCurrentEntry_Object = MibTableRow
twampReportCurrentEntry = _TwampReportCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1)
)
twampReportCurrentEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampControllerId"),
    (0, "RAD-TEST-MIB", "twampPeerAddrType"),
    (0, "RAD-TEST-MIB", "twampPeerAddr"),
    (0, "RAD-TEST-MIB", "twampContSessionId"),
)
if mibBuilder.loadTexts:
    twampReportCurrentEntry.setStatus("current")
_TwampReportCurrentStartDateAndTime_Type = DateAndTime
_TwampReportCurrentStartDateAndTime_Object = MibTableColumn
twampReportCurrentStartDateAndTime = _TwampReportCurrentStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 1),
    _TwampReportCurrentStartDateAndTime_Type()
)
twampReportCurrentStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentStartDateAndTime.setStatus("current")
_TwampReportCurrentElapsedTime_Type = Unsigned32
_TwampReportCurrentElapsedTime_Object = MibTableColumn
twampReportCurrentElapsedTime = _TwampReportCurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 2),
    _TwampReportCurrentElapsedTime_Type()
)
twampReportCurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentElapsedTime.setStatus("current")
_TwampReportCurrentTxPackets_Type = Counter64
_TwampReportCurrentTxPackets_Object = MibTableColumn
twampReportCurrentTxPackets = _TwampReportCurrentTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 3),
    _TwampReportCurrentTxPackets_Type()
)
twampReportCurrentTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentTxPackets.setStatus("current")
_TwampReportCurrentRxValidPackets_Type = Counter64
_TwampReportCurrentRxValidPackets_Object = MibTableColumn
twampReportCurrentRxValidPackets = _TwampReportCurrentRxValidPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 4),
    _TwampReportCurrentRxValidPackets_Type()
)
twampReportCurrentRxValidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentRxValidPackets.setStatus("current")
_TwampReportCurrentLossPackets_Type = Counter64
_TwampReportCurrentLossPackets_Object = MibTableColumn
twampReportCurrentLossPackets = _TwampReportCurrentLossPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 5),
    _TwampReportCurrentLossPackets_Type()
)
twampReportCurrentLossPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentLossPackets.setStatus("current")
_TwampReportCurrentAvailableSeconds_Type = Counter32
_TwampReportCurrentAvailableSeconds_Object = MibTableColumn
twampReportCurrentAvailableSeconds = _TwampReportCurrentAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 6),
    _TwampReportCurrentAvailableSeconds_Type()
)
twampReportCurrentAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentAvailableSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentAvailableSeconds.setUnits("seconds")
_TwampReportCurrentDelayMin_Type = Counter32
_TwampReportCurrentDelayMin_Object = MibTableColumn
twampReportCurrentDelayMin = _TwampReportCurrentDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 7),
    _TwampReportCurrentDelayMin_Type()
)
twampReportCurrentDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayMin.setUnits("micro seconds")
_TwampReportCurrentDelayMax_Type = Counter32
_TwampReportCurrentDelayMax_Object = MibTableColumn
twampReportCurrentDelayMax = _TwampReportCurrentDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 8),
    _TwampReportCurrentDelayMax_Type()
)
twampReportCurrentDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayMax.setUnits("micro seconds")
_TwampReportCurrentDelaySum_Type = Counter64
_TwampReportCurrentDelaySum_Object = MibTableColumn
twampReportCurrentDelaySum = _TwampReportCurrentDelaySum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 9),
    _TwampReportCurrentDelaySum_Type()
)
twampReportCurrentDelaySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelaySum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelaySum.setUnits("micro seconds")
_TwampReportCurrentDelayAverage_Type = Counter32
_TwampReportCurrentDelayAverage_Object = MibTableColumn
twampReportCurrentDelayAverage = _TwampReportCurrentDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 10),
    _TwampReportCurrentDelayAverage_Type()
)
twampReportCurrentDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayAverage.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayAverage.setUnits("micro seconds")
_TwampReportCurrentDelayedPackets_Type = Counter32
_TwampReportCurrentDelayedPackets_Object = MibTableColumn
twampReportCurrentDelayedPackets = _TwampReportCurrentDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 11),
    _TwampReportCurrentDelayedPackets_Type()
)
twampReportCurrentDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayedPackets.setStatus("current")
_TwampReportCurrentPdvMax_Type = Counter32
_TwampReportCurrentPdvMax_Object = MibTableColumn
twampReportCurrentPdvMax = _TwampReportCurrentPdvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 12),
    _TwampReportCurrentPdvMax_Type()
)
twampReportCurrentPdvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentPdvMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentPdvMax.setUnits("micro seconds")
_TwampReportCurrentIpdvMax_Type = Counter32
_TwampReportCurrentIpdvMax_Object = MibTableColumn
twampReportCurrentIpdvMax = _TwampReportCurrentIpdvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 13),
    _TwampReportCurrentIpdvMax_Type()
)
twampReportCurrentIpdvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvMax.setUnits("micro seconds")
_TwampReportCurrentIpdvSum_Type = Counter64
_TwampReportCurrentIpdvSum_Object = MibTableColumn
twampReportCurrentIpdvSum = _TwampReportCurrentIpdvSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 14),
    _TwampReportCurrentIpdvSum_Type()
)
twampReportCurrentIpdvSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvSum.setUnits("micro seconds")
_TwampReportCurrentIpdvValidResults_Type = Counter64
_TwampReportCurrentIpdvValidResults_Object = MibTableColumn
twampReportCurrentIpdvValidResults = _TwampReportCurrentIpdvValidResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 15),
    _TwampReportCurrentIpdvValidResults_Type()
)
twampReportCurrentIpdvValidResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvValidResults.setStatus("current")
_TwampReportCurrentIpdvFwdMax_Type = Counter64
_TwampReportCurrentIpdvFwdMax_Object = MibTableColumn
twampReportCurrentIpdvFwdMax = _TwampReportCurrentIpdvFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 16),
    _TwampReportCurrentIpdvFwdMax_Type()
)
twampReportCurrentIpdvFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvFwdMax.setUnits("micro seconds")
_TwampReportCurrentIpdvFwdSum_Type = Counter64
_TwampReportCurrentIpdvFwdSum_Object = MibTableColumn
twampReportCurrentIpdvFwdSum = _TwampReportCurrentIpdvFwdSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 17),
    _TwampReportCurrentIpdvFwdSum_Type()
)
twampReportCurrentIpdvFwdSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvFwdSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvFwdSum.setUnits("micro seconds")
_TwampReportCurrentIpdvFwdValidResults_Type = Counter64
_TwampReportCurrentIpdvFwdValidResults_Object = MibTableColumn
twampReportCurrentIpdvFwdValidResults = _TwampReportCurrentIpdvFwdValidResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 18),
    _TwampReportCurrentIpdvFwdValidResults_Type()
)
twampReportCurrentIpdvFwdValidResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvFwdValidResults.setStatus("current")
_TwampReportCurrentIpdvBckMax_Type = Counter64
_TwampReportCurrentIpdvBckMax_Object = MibTableColumn
twampReportCurrentIpdvBckMax = _TwampReportCurrentIpdvBckMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 19),
    _TwampReportCurrentIpdvBckMax_Type()
)
twampReportCurrentIpdvBckMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvBckMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvBckMax.setUnits("micro seconds")
_TwampReportCurrentIpdvBckSum_Type = Counter64
_TwampReportCurrentIpdvBckSum_Object = MibTableColumn
twampReportCurrentIpdvBckSum = _TwampReportCurrentIpdvBckSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 20),
    _TwampReportCurrentIpdvBckSum_Type()
)
twampReportCurrentIpdvBckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvBckSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvBckSum.setUnits("micro seconds")
_TwampReportCurrentIpdvBckValidResults_Type = Counter64
_TwampReportCurrentIpdvBckValidResults_Object = MibTableColumn
twampReportCurrentIpdvBckValidResults = _TwampReportCurrentIpdvBckValidResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 21),
    _TwampReportCurrentIpdvBckValidResults_Type()
)
twampReportCurrentIpdvBckValidResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentIpdvBckValidResults.setStatus("current")
_TwampReportCurrentReorderedFwd_Type = Counter32
_TwampReportCurrentReorderedFwd_Object = MibTableColumn
twampReportCurrentReorderedFwd = _TwampReportCurrentReorderedFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 22),
    _TwampReportCurrentReorderedFwd_Type()
)
twampReportCurrentReorderedFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentReorderedFwd.setStatus("current")
_TwampReportCurrentReorderedBck_Type = Counter32
_TwampReportCurrentReorderedBck_Object = MibTableColumn
twampReportCurrentReorderedBck = _TwampReportCurrentReorderedBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 23),
    _TwampReportCurrentReorderedBck_Type()
)
twampReportCurrentReorderedBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentReorderedBck.setStatus("current")
_TwampReportCurrentDuplicateFwd_Type = Counter32
_TwampReportCurrentDuplicateFwd_Object = MibTableColumn
twampReportCurrentDuplicateFwd = _TwampReportCurrentDuplicateFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 24),
    _TwampReportCurrentDuplicateFwd_Type()
)
twampReportCurrentDuplicateFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDuplicateFwd.setStatus("current")
_TwampReportCurrentDuplicateBck_Type = Counter32
_TwampReportCurrentDuplicateBck_Object = MibTableColumn
twampReportCurrentDuplicateBck = _TwampReportCurrentDuplicateBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 25),
    _TwampReportCurrentDuplicateBck_Type()
)
twampReportCurrentDuplicateBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDuplicateBck.setStatus("current")
_TwampReportCurrentFragmentedFwd_Type = Counter32
_TwampReportCurrentFragmentedFwd_Object = MibTableColumn
twampReportCurrentFragmentedFwd = _TwampReportCurrentFragmentedFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 26),
    _TwampReportCurrentFragmentedFwd_Type()
)
twampReportCurrentFragmentedFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentFragmentedFwd.setStatus("current")
_TwampReportCurrentFragmentedBck_Type = Counter32
_TwampReportCurrentFragmentedBck_Object = MibTableColumn
twampReportCurrentFragmentedBck = _TwampReportCurrentFragmentedBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 27),
    _TwampReportCurrentFragmentedBck_Type()
)
twampReportCurrentFragmentedBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentFragmentedBck.setStatus("current")
_TwampReportCurrentDelayFwdMin_Type = Counter32
_TwampReportCurrentDelayFwdMin_Object = MibTableColumn
twampReportCurrentDelayFwdMin = _TwampReportCurrentDelayFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 28),
    _TwampReportCurrentDelayFwdMin_Type()
)
twampReportCurrentDelayFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayFwdMin.setUnits("micro seconds")
_TwampReportCurrentDelayFwdMax_Type = Counter32
_TwampReportCurrentDelayFwdMax_Object = MibTableColumn
twampReportCurrentDelayFwdMax = _TwampReportCurrentDelayFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 29),
    _TwampReportCurrentDelayFwdMax_Type()
)
twampReportCurrentDelayFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayFwdMax.setUnits("micro seconds")
_TwampReportCurrentDelayFwdSum_Type = Counter64
_TwampReportCurrentDelayFwdSum_Object = MibTableColumn
twampReportCurrentDelayFwdSum = _TwampReportCurrentDelayFwdSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 30),
    _TwampReportCurrentDelayFwdSum_Type()
)
twampReportCurrentDelayFwdSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayFwdSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayFwdSum.setUnits("micro seconds")
_TwampReportCurrentDelayBckMin_Type = Counter32
_TwampReportCurrentDelayBckMin_Object = MibTableColumn
twampReportCurrentDelayBckMin = _TwampReportCurrentDelayBckMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 31),
    _TwampReportCurrentDelayBckMin_Type()
)
twampReportCurrentDelayBckMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayBckMin.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayBckMin.setUnits("micro seconds")
_TwampReportCurrentDelayBckMax_Type = Counter32
_TwampReportCurrentDelayBckMax_Object = MibTableColumn
twampReportCurrentDelayBckMax = _TwampReportCurrentDelayBckMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 32),
    _TwampReportCurrentDelayBckMax_Type()
)
twampReportCurrentDelayBckMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayBckMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayBckMax.setUnits("micro seconds")
_TwampReportCurrentDelayBckSum_Type = Counter64
_TwampReportCurrentDelayBckSum_Object = MibTableColumn
twampReportCurrentDelayBckSum = _TwampReportCurrentDelayBckSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 33),
    _TwampReportCurrentDelayBckSum_Type()
)
twampReportCurrentDelayBckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayBckSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentDelayBckSum.setUnits("micro seconds")
_TwampReportCurrentDelayedPacketsFwd_Type = Counter32
_TwampReportCurrentDelayedPacketsFwd_Object = MibTableColumn
twampReportCurrentDelayedPacketsFwd = _TwampReportCurrentDelayedPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 34),
    _TwampReportCurrentDelayedPacketsFwd_Type()
)
twampReportCurrentDelayedPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayedPacketsFwd.setStatus("current")
_TwampReportCurrentDelayedPacketsBck_Type = Counter32
_TwampReportCurrentDelayedPacketsBck_Object = MibTableColumn
twampReportCurrentDelayedPacketsBck = _TwampReportCurrentDelayedPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 35),
    _TwampReportCurrentDelayedPacketsBck_Type()
)
twampReportCurrentDelayedPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentDelayedPacketsBck.setStatus("current")
_TwampReportCurrentPdvMaxFwd_Type = Counter32
_TwampReportCurrentPdvMaxFwd_Object = MibTableColumn
twampReportCurrentPdvMaxFwd = _TwampReportCurrentPdvMaxFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 36),
    _TwampReportCurrentPdvMaxFwd_Type()
)
twampReportCurrentPdvMaxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentPdvMaxFwd.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentPdvMaxFwd.setUnits("micro seconds")
_TwampReportCurrentPdvMaxBck_Type = Counter32
_TwampReportCurrentPdvMaxBck_Object = MibTableColumn
twampReportCurrentPdvMaxBck = _TwampReportCurrentPdvMaxBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 37),
    _TwampReportCurrentPdvMaxBck_Type()
)
twampReportCurrentPdvMaxBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentPdvMaxBck.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentPdvMaxBck.setUnits("micro seconds")
_TwampReportCurrentTxPacketsFwd_Type = Counter64
_TwampReportCurrentTxPacketsFwd_Object = MibTableColumn
twampReportCurrentTxPacketsFwd = _TwampReportCurrentTxPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 38),
    _TwampReportCurrentTxPacketsFwd_Type()
)
twampReportCurrentTxPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentTxPacketsFwd.setStatus("current")
_TwampReportCurrentTxPacketsBck_Type = Counter64
_TwampReportCurrentTxPacketsBck_Object = MibTableColumn
twampReportCurrentTxPacketsBck = _TwampReportCurrentTxPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 39),
    _TwampReportCurrentTxPacketsBck_Type()
)
twampReportCurrentTxPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentTxPacketsBck.setStatus("current")
_TwampReportCurrentRxValidPacketsFwd_Type = Counter64
_TwampReportCurrentRxValidPacketsFwd_Object = MibTableColumn
twampReportCurrentRxValidPacketsFwd = _TwampReportCurrentRxValidPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 40),
    _TwampReportCurrentRxValidPacketsFwd_Type()
)
twampReportCurrentRxValidPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentRxValidPacketsFwd.setStatus("current")
_TwampReportCurrentRxValidPacketsBck_Type = Counter64
_TwampReportCurrentRxValidPacketsBck_Object = MibTableColumn
twampReportCurrentRxValidPacketsBck = _TwampReportCurrentRxValidPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 41),
    _TwampReportCurrentRxValidPacketsBck_Type()
)
twampReportCurrentRxValidPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentRxValidPacketsBck.setStatus("current")
_TwampReportCurrentLossPacketsFwd_Type = Counter64
_TwampReportCurrentLossPacketsFwd_Object = MibTableColumn
twampReportCurrentLossPacketsFwd = _TwampReportCurrentLossPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 42),
    _TwampReportCurrentLossPacketsFwd_Type()
)
twampReportCurrentLossPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentLossPacketsFwd.setStatus("current")
_TwampReportCurrentLossPacketsBck_Type = Counter64
_TwampReportCurrentLossPacketsBck_Object = MibTableColumn
twampReportCurrentLossPacketsBck = _TwampReportCurrentLossPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 43),
    _TwampReportCurrentLossPacketsBck_Type()
)
twampReportCurrentLossPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentLossPacketsBck.setStatus("current")
_TwampReportCurrentAvailableSecondsFwd_Type = Counter32
_TwampReportCurrentAvailableSecondsFwd_Object = MibTableColumn
twampReportCurrentAvailableSecondsFwd = _TwampReportCurrentAvailableSecondsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 44),
    _TwampReportCurrentAvailableSecondsFwd_Type()
)
twampReportCurrentAvailableSecondsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentAvailableSecondsFwd.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentAvailableSecondsFwd.setUnits("seconds")
_TwampReportCurrentAvailableSecondsBck_Type = Counter32
_TwampReportCurrentAvailableSecondsBck_Object = MibTableColumn
twampReportCurrentAvailableSecondsBck = _TwampReportCurrentAvailableSecondsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 45),
    _TwampReportCurrentAvailableSecondsBck_Type()
)
twampReportCurrentAvailableSecondsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentAvailableSecondsBck.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentAvailableSecondsBck.setUnits("seconds")
_TwampReportCurrentRxSyncValidPacketsFwd_Type = Counter64
_TwampReportCurrentRxSyncValidPacketsFwd_Object = MibTableColumn
twampReportCurrentRxSyncValidPacketsFwd = _TwampReportCurrentRxSyncValidPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 46),
    _TwampReportCurrentRxSyncValidPacketsFwd_Type()
)
twampReportCurrentRxSyncValidPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentRxSyncValidPacketsFwd.setStatus("current")
_TwampReportCurrentRxSyncValidPacketsBck_Type = Counter64
_TwampReportCurrentRxSyncValidPacketsBck_Object = MibTableColumn
twampReportCurrentRxSyncValidPacketsBck = _TwampReportCurrentRxSyncValidPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 47),
    _TwampReportCurrentRxSyncValidPacketsBck_Type()
)
twampReportCurrentRxSyncValidPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentRxSyncValidPacketsBck.setStatus("current")
_TwampReportCurrentSyncSeconds_Type = Counter32
_TwampReportCurrentSyncSeconds_Object = MibTableColumn
twampReportCurrentSyncSeconds = _TwampReportCurrentSyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 9, 1, 48),
    _TwampReportCurrentSyncSeconds_Type()
)
twampReportCurrentSyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportCurrentSyncSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twampReportCurrentSyncSeconds.setUnits("seconds")
_TwampReportIntervalTable_Object = MibTable
twampReportIntervalTable = _TwampReportIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10)
)
if mibBuilder.loadTexts:
    twampReportIntervalTable.setStatus("current")
_TwampReportIntervalEntry_Object = MibTableRow
twampReportIntervalEntry = _TwampReportIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1)
)
twampReportIntervalEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "twampControllerId"),
    (0, "RAD-TEST-MIB", "twampPeerAddrType"),
    (0, "RAD-TEST-MIB", "twampPeerAddr"),
    (0, "RAD-TEST-MIB", "twampContSessionId"),
    (0, "RAD-TEST-MIB", "twampReportIntervalNumber"),
)
if mibBuilder.loadTexts:
    twampReportIntervalEntry.setStatus("current")
_TwampReportIntervalNumber_Type = Unsigned32
_TwampReportIntervalNumber_Object = MibTableColumn
twampReportIntervalNumber = _TwampReportIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 1),
    _TwampReportIntervalNumber_Type()
)
twampReportIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twampReportIntervalNumber.setStatus("current")
_TwampReportIntervalStartDateAndTime_Type = DateAndTime
_TwampReportIntervalStartDateAndTime_Object = MibTableColumn
twampReportIntervalStartDateAndTime = _TwampReportIntervalStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 2),
    _TwampReportIntervalStartDateAndTime_Type()
)
twampReportIntervalStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalStartDateAndTime.setStatus("current")
_TwampReportIntervalElapsedTime_Type = Unsigned32
_TwampReportIntervalElapsedTime_Object = MibTableColumn
twampReportIntervalElapsedTime = _TwampReportIntervalElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 3),
    _TwampReportIntervalElapsedTime_Type()
)
twampReportIntervalElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalElapsedTime.setStatus("current")
_TwampReportIntervalTxPackets_Type = Counter64
_TwampReportIntervalTxPackets_Object = MibTableColumn
twampReportIntervalTxPackets = _TwampReportIntervalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 4),
    _TwampReportIntervalTxPackets_Type()
)
twampReportIntervalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalTxPackets.setStatus("current")
_TwampReportIntervalRxValidPackets_Type = Counter64
_TwampReportIntervalRxValidPackets_Object = MibTableColumn
twampReportIntervalRxValidPackets = _TwampReportIntervalRxValidPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 5),
    _TwampReportIntervalRxValidPackets_Type()
)
twampReportIntervalRxValidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalRxValidPackets.setStatus("current")
_TwampReportIntervalLossPackets_Type = Counter64
_TwampReportIntervalLossPackets_Object = MibTableColumn
twampReportIntervalLossPackets = _TwampReportIntervalLossPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 6),
    _TwampReportIntervalLossPackets_Type()
)
twampReportIntervalLossPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalLossPackets.setStatus("current")
_TwampReportIntervalAvailableSeconds_Type = Counter32
_TwampReportIntervalAvailableSeconds_Object = MibTableColumn
twampReportIntervalAvailableSeconds = _TwampReportIntervalAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 7),
    _TwampReportIntervalAvailableSeconds_Type()
)
twampReportIntervalAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalAvailableSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalAvailableSeconds.setUnits("seconds")
_TwampReportIntervalDelayMin_Type = Counter32
_TwampReportIntervalDelayMin_Object = MibTableColumn
twampReportIntervalDelayMin = _TwampReportIntervalDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 8),
    _TwampReportIntervalDelayMin_Type()
)
twampReportIntervalDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayMin.setUnits("micro seconds")
_TwampReportIntervalDelayMax_Type = Counter32
_TwampReportIntervalDelayMax_Object = MibTableColumn
twampReportIntervalDelayMax = _TwampReportIntervalDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 9),
    _TwampReportIntervalDelayMax_Type()
)
twampReportIntervalDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayMax.setUnits("micro seconds")
_TwampReportIntervalDelaySum_Type = Counter64
_TwampReportIntervalDelaySum_Object = MibTableColumn
twampReportIntervalDelaySum = _TwampReportIntervalDelaySum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 10),
    _TwampReportIntervalDelaySum_Type()
)
twampReportIntervalDelaySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelaySum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelaySum.setUnits("micro seconds")
_TwampReportIntervalDelayAverage_Type = Counter32
_TwampReportIntervalDelayAverage_Object = MibTableColumn
twampReportIntervalDelayAverage = _TwampReportIntervalDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 11),
    _TwampReportIntervalDelayAverage_Type()
)
twampReportIntervalDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayAverage.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayAverage.setUnits("micro seconds")
_TwampReportIntervalDelayedPackets_Type = Counter32
_TwampReportIntervalDelayedPackets_Object = MibTableColumn
twampReportIntervalDelayedPackets = _TwampReportIntervalDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 12),
    _TwampReportIntervalDelayedPackets_Type()
)
twampReportIntervalDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayedPackets.setStatus("current")
_TwampReportIntervalPdvMax_Type = Counter32
_TwampReportIntervalPdvMax_Object = MibTableColumn
twampReportIntervalPdvMax = _TwampReportIntervalPdvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 13),
    _TwampReportIntervalPdvMax_Type()
)
twampReportIntervalPdvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalPdvMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalPdvMax.setUnits("micro seconds")
_TwampReportIntervalIpdvMax_Type = Counter32
_TwampReportIntervalIpdvMax_Object = MibTableColumn
twampReportIntervalIpdvMax = _TwampReportIntervalIpdvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 14),
    _TwampReportIntervalIpdvMax_Type()
)
twampReportIntervalIpdvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvMax.setUnits("micro seconds")
_TwampReportIntervalIpdvSum_Type = Counter64
_TwampReportIntervalIpdvSum_Object = MibTableColumn
twampReportIntervalIpdvSum = _TwampReportIntervalIpdvSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 15),
    _TwampReportIntervalIpdvSum_Type()
)
twampReportIntervalIpdvSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvSum.setUnits("micro seconds")
_TwampReportIntervalIpdvValidResults_Type = Counter64
_TwampReportIntervalIpdvValidResults_Object = MibTableColumn
twampReportIntervalIpdvValidResults = _TwampReportIntervalIpdvValidResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 16),
    _TwampReportIntervalIpdvValidResults_Type()
)
twampReportIntervalIpdvValidResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvValidResults.setStatus("current")
_TwampReportIntervalIpdvFwdMax_Type = Counter64
_TwampReportIntervalIpdvFwdMax_Object = MibTableColumn
twampReportIntervalIpdvFwdMax = _TwampReportIntervalIpdvFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 17),
    _TwampReportIntervalIpdvFwdMax_Type()
)
twampReportIntervalIpdvFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvFwdMax.setUnits("micro seconds")
_TwampReportIntervalIpdvFwdSum_Type = Counter64
_TwampReportIntervalIpdvFwdSum_Object = MibTableColumn
twampReportIntervalIpdvFwdSum = _TwampReportIntervalIpdvFwdSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 18),
    _TwampReportIntervalIpdvFwdSum_Type()
)
twampReportIntervalIpdvFwdSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvFwdSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvFwdSum.setUnits("micro seconds")
_TwampReportIntervalIpdvFwdValidResults_Type = Counter64
_TwampReportIntervalIpdvFwdValidResults_Object = MibTableColumn
twampReportIntervalIpdvFwdValidResults = _TwampReportIntervalIpdvFwdValidResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 19),
    _TwampReportIntervalIpdvFwdValidResults_Type()
)
twampReportIntervalIpdvFwdValidResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvFwdValidResults.setStatus("current")
_TwampReportIntervalIpdvBckMax_Type = Counter64
_TwampReportIntervalIpdvBckMax_Object = MibTableColumn
twampReportIntervalIpdvBckMax = _TwampReportIntervalIpdvBckMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 20),
    _TwampReportIntervalIpdvBckMax_Type()
)
twampReportIntervalIpdvBckMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvBckMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvBckMax.setUnits("micro seconds")
_TwampReportIntervalIpdvBckSum_Type = Counter64
_TwampReportIntervalIpdvBckSum_Object = MibTableColumn
twampReportIntervalIpdvBckSum = _TwampReportIntervalIpdvBckSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 21),
    _TwampReportIntervalIpdvBckSum_Type()
)
twampReportIntervalIpdvBckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvBckSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvBckSum.setUnits("micro seconds")
_TwampReportIntervalIpdvBckValidResults_Type = Counter64
_TwampReportIntervalIpdvBckValidResults_Object = MibTableColumn
twampReportIntervalIpdvBckValidResults = _TwampReportIntervalIpdvBckValidResults_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 22),
    _TwampReportIntervalIpdvBckValidResults_Type()
)
twampReportIntervalIpdvBckValidResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalIpdvBckValidResults.setStatus("current")
_TwampReportIntervalReorderedFwd_Type = Counter32
_TwampReportIntervalReorderedFwd_Object = MibTableColumn
twampReportIntervalReorderedFwd = _TwampReportIntervalReorderedFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 23),
    _TwampReportIntervalReorderedFwd_Type()
)
twampReportIntervalReorderedFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalReorderedFwd.setStatus("current")
_TwampReportIntervalReorderedBck_Type = Counter32
_TwampReportIntervalReorderedBck_Object = MibTableColumn
twampReportIntervalReorderedBck = _TwampReportIntervalReorderedBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 24),
    _TwampReportIntervalReorderedBck_Type()
)
twampReportIntervalReorderedBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalReorderedBck.setStatus("current")
_TwampReportIntervalDuplicateFwd_Type = Counter32
_TwampReportIntervalDuplicateFwd_Object = MibTableColumn
twampReportIntervalDuplicateFwd = _TwampReportIntervalDuplicateFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 25),
    _TwampReportIntervalDuplicateFwd_Type()
)
twampReportIntervalDuplicateFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDuplicateFwd.setStatus("current")
_TwampReportIntervalDuplicateBck_Type = Counter32
_TwampReportIntervalDuplicateBck_Object = MibTableColumn
twampReportIntervalDuplicateBck = _TwampReportIntervalDuplicateBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 26),
    _TwampReportIntervalDuplicateBck_Type()
)
twampReportIntervalDuplicateBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDuplicateBck.setStatus("current")
_TwampReportIntervalFragmentedFwd_Type = Counter32
_TwampReportIntervalFragmentedFwd_Object = MibTableColumn
twampReportIntervalFragmentedFwd = _TwampReportIntervalFragmentedFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 27),
    _TwampReportIntervalFragmentedFwd_Type()
)
twampReportIntervalFragmentedFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalFragmentedFwd.setStatus("current")
_TwampReportIntervalFragmentedBck_Type = Counter32
_TwampReportIntervalFragmentedBck_Object = MibTableColumn
twampReportIntervalFragmentedBck = _TwampReportIntervalFragmentedBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 28),
    _TwampReportIntervalFragmentedBck_Type()
)
twampReportIntervalFragmentedBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalFragmentedBck.setStatus("current")
_TwampReportIntervalDelayFwdMin_Type = Counter32
_TwampReportIntervalDelayFwdMin_Object = MibTableColumn
twampReportIntervalDelayFwdMin = _TwampReportIntervalDelayFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 29),
    _TwampReportIntervalDelayFwdMin_Type()
)
twampReportIntervalDelayFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayFwdMin.setUnits("micro seconds")
_TwampReportIntervalDelayFwdMax_Type = Counter32
_TwampReportIntervalDelayFwdMax_Object = MibTableColumn
twampReportIntervalDelayFwdMax = _TwampReportIntervalDelayFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 30),
    _TwampReportIntervalDelayFwdMax_Type()
)
twampReportIntervalDelayFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayFwdMax.setUnits("micro seconds")
_TwampReportIntervalDelayFwdSum_Type = Counter64
_TwampReportIntervalDelayFwdSum_Object = MibTableColumn
twampReportIntervalDelayFwdSum = _TwampReportIntervalDelayFwdSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 31),
    _TwampReportIntervalDelayFwdSum_Type()
)
twampReportIntervalDelayFwdSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayFwdSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayFwdSum.setUnits("micro seconds")
_TwampReportIntervalDelayBckMin_Type = Counter32
_TwampReportIntervalDelayBckMin_Object = MibTableColumn
twampReportIntervalDelayBckMin = _TwampReportIntervalDelayBckMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 32),
    _TwampReportIntervalDelayBckMin_Type()
)
twampReportIntervalDelayBckMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayBckMin.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayBckMin.setUnits("micro seconds")
_TwampReportIntervalDelayBckMax_Type = Counter32
_TwampReportIntervalDelayBckMax_Object = MibTableColumn
twampReportIntervalDelayBckMax = _TwampReportIntervalDelayBckMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 33),
    _TwampReportIntervalDelayBckMax_Type()
)
twampReportIntervalDelayBckMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayBckMax.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayBckMax.setUnits("micro seconds")
_TwampReportIntervalDelayBckSum_Type = Counter64
_TwampReportIntervalDelayBckSum_Object = MibTableColumn
twampReportIntervalDelayBckSum = _TwampReportIntervalDelayBckSum_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 34),
    _TwampReportIntervalDelayBckSum_Type()
)
twampReportIntervalDelayBckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayBckSum.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalDelayBckSum.setUnits("micro seconds")
_TwampReportIntervalDelayedPacketsFwd_Type = Counter32
_TwampReportIntervalDelayedPacketsFwd_Object = MibTableColumn
twampReportIntervalDelayedPacketsFwd = _TwampReportIntervalDelayedPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 35),
    _TwampReportIntervalDelayedPacketsFwd_Type()
)
twampReportIntervalDelayedPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayedPacketsFwd.setStatus("current")
_TwampReportIntervalDelayedPacketsBck_Type = Counter32
_TwampReportIntervalDelayedPacketsBck_Object = MibTableColumn
twampReportIntervalDelayedPacketsBck = _TwampReportIntervalDelayedPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 36),
    _TwampReportIntervalDelayedPacketsBck_Type()
)
twampReportIntervalDelayedPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalDelayedPacketsBck.setStatus("current")
_TwampReportIntervalPdvMaxFwd_Type = Counter32
_TwampReportIntervalPdvMaxFwd_Object = MibTableColumn
twampReportIntervalPdvMaxFwd = _TwampReportIntervalPdvMaxFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 37),
    _TwampReportIntervalPdvMaxFwd_Type()
)
twampReportIntervalPdvMaxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalPdvMaxFwd.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalPdvMaxFwd.setUnits("micro seconds")
_TwampReportIntervalPdvMaxBck_Type = Counter32
_TwampReportIntervalPdvMaxBck_Object = MibTableColumn
twampReportIntervalPdvMaxBck = _TwampReportIntervalPdvMaxBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 38),
    _TwampReportIntervalPdvMaxBck_Type()
)
twampReportIntervalPdvMaxBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalPdvMaxBck.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalPdvMaxBck.setUnits("micro seconds")
_TwampReportIntervalTxPacketsFwd_Type = Counter64
_TwampReportIntervalTxPacketsFwd_Object = MibTableColumn
twampReportIntervalTxPacketsFwd = _TwampReportIntervalTxPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 39),
    _TwampReportIntervalTxPacketsFwd_Type()
)
twampReportIntervalTxPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalTxPacketsFwd.setStatus("current")
_TwampReportIntervalValidData_Type = TruthValue
_TwampReportIntervalValidData_Object = MibTableColumn
twampReportIntervalValidData = _TwampReportIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 40),
    _TwampReportIntervalValidData_Type()
)
twampReportIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalValidData.setStatus("current")
_TwampReportIntervalTxPacketsBck_Type = Counter64
_TwampReportIntervalTxPacketsBck_Object = MibTableColumn
twampReportIntervalTxPacketsBck = _TwampReportIntervalTxPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 41),
    _TwampReportIntervalTxPacketsBck_Type()
)
twampReportIntervalTxPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalTxPacketsBck.setStatus("current")
_TwampReportIntervalRxValidPacketsFwd_Type = Counter64
_TwampReportIntervalRxValidPacketsFwd_Object = MibTableColumn
twampReportIntervalRxValidPacketsFwd = _TwampReportIntervalRxValidPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 42),
    _TwampReportIntervalRxValidPacketsFwd_Type()
)
twampReportIntervalRxValidPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalRxValidPacketsFwd.setStatus("current")
_TwampReportIntervalRxValidPacketsBck_Type = Counter64
_TwampReportIntervalRxValidPacketsBck_Object = MibTableColumn
twampReportIntervalRxValidPacketsBck = _TwampReportIntervalRxValidPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 43),
    _TwampReportIntervalRxValidPacketsBck_Type()
)
twampReportIntervalRxValidPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalRxValidPacketsBck.setStatus("current")
_TwampReportIntervalLossPacketsFwd_Type = Counter64
_TwampReportIntervalLossPacketsFwd_Object = MibTableColumn
twampReportIntervalLossPacketsFwd = _TwampReportIntervalLossPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 44),
    _TwampReportIntervalLossPacketsFwd_Type()
)
twampReportIntervalLossPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalLossPacketsFwd.setStatus("current")
_TwampReportIntervalLossPacketsBck_Type = Counter64
_TwampReportIntervalLossPacketsBck_Object = MibTableColumn
twampReportIntervalLossPacketsBck = _TwampReportIntervalLossPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 45),
    _TwampReportIntervalLossPacketsBck_Type()
)
twampReportIntervalLossPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalLossPacketsBck.setStatus("current")
_TwampReportIntervalAvailableSecondsFwd_Type = Counter32
_TwampReportIntervalAvailableSecondsFwd_Object = MibTableColumn
twampReportIntervalAvailableSecondsFwd = _TwampReportIntervalAvailableSecondsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 46),
    _TwampReportIntervalAvailableSecondsFwd_Type()
)
twampReportIntervalAvailableSecondsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalAvailableSecondsFwd.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalAvailableSecondsFwd.setUnits("seconds")
_TwampReportIntervalAvailableSecondsBck_Type = Counter32
_TwampReportIntervalAvailableSecondsBck_Object = MibTableColumn
twampReportIntervalAvailableSecondsBck = _TwampReportIntervalAvailableSecondsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 47),
    _TwampReportIntervalAvailableSecondsBck_Type()
)
twampReportIntervalAvailableSecondsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalAvailableSecondsBck.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalAvailableSecondsBck.setUnits("seconds")
_TwampReportIntervalRxSyncValidPacketsFwd_Type = Counter64
_TwampReportIntervalRxSyncValidPacketsFwd_Object = MibTableColumn
twampReportIntervalRxSyncValidPacketsFwd = _TwampReportIntervalRxSyncValidPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 48),
    _TwampReportIntervalRxSyncValidPacketsFwd_Type()
)
twampReportIntervalRxSyncValidPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalRxSyncValidPacketsFwd.setStatus("current")
_TwampReportIntervalRxSyncValidPacketsBck_Type = Counter64
_TwampReportIntervalRxSyncValidPacketsBck_Object = MibTableColumn
twampReportIntervalRxSyncValidPacketsBck = _TwampReportIntervalRxSyncValidPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 49),
    _TwampReportIntervalRxSyncValidPacketsBck_Type()
)
twampReportIntervalRxSyncValidPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalRxSyncValidPacketsBck.setStatus("current")
_TwampReportIntervalSyncSeconds_Type = Counter32
_TwampReportIntervalSyncSeconds_Object = MibTableColumn
twampReportIntervalSyncSeconds = _TwampReportIntervalSyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 10, 1, 50),
    _TwampReportIntervalSyncSeconds_Type()
)
twampReportIntervalSyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampReportIntervalSyncSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twampReportIntervalSyncSeconds.setUnits("seconds")
_TstNeThroughputIterationTable_Object = MibTable
tstNeThroughputIterationTable = _TstNeThroughputIterationTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 12)
)
if mibBuilder.loadTexts:
    tstNeThroughputIterationTable.setStatus("current")
_TstNeThroughputIterationEntry_Object = MibTableRow
tstNeThroughputIterationEntry = _TstNeThroughputIterationEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 12, 1)
)
tstNeThroughputIterationEntry.setIndexNames(
    (0, "RAD-TEST-MIB", "tstNePerfRepTestId"),
    (0, "RAD-TEST-MIB", "throughputReportTrialNumber"),
    (0, "RAD-TEST-MIB", "throughputReportPacketSize"),
    (0, "RAD-TEST-MIB", "tstNeThroughputIteration"),
)
if mibBuilder.loadTexts:
    tstNeThroughputIterationEntry.setStatus("current")
_TstNeThroughputIteration_Type = Gauge32
_TstNeThroughputIteration_Object = MibTableColumn
tstNeThroughputIteration = _TstNeThroughputIteration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 12, 1, 1),
    _TstNeThroughputIteration_Type()
)
tstNeThroughputIteration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tstNeThroughputIteration.setStatus("current")
_TstNeThroughputIterationBPS_Type = Unsigned32
_TstNeThroughputIterationBPS_Object = MibTableColumn
tstNeThroughputIterationBPS = _TstNeThroughputIterationBPS_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 12, 1, 2),
    _TstNeThroughputIterationBPS_Type()
)
tstNeThroughputIterationBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNeThroughputIterationBPS.setStatus("current")
_TstNeThroughputLossPacket_Type = Gauge32
_TstNeThroughputLossPacket_Object = MibTableColumn
tstNeThroughputLossPacket = _TstNeThroughputLossPacket_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 12, 1, 3),
    _TstNeThroughputLossPacket_Type()
)
tstNeThroughputLossPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tstNeThroughputLossPacket.setStatus("current")

# Managed Objects groups


# Notification objects

systemRfc2544TestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 2)
)
systemRfc2544TestStart.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "tstNePerfRepTestType"))
)
if mibBuilder.loadTexts:
    systemRfc2544TestStart.setStatus(
        "current"
    )

systemRfc2544TestEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 3)
)
systemRfc2544TestEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "tstNePerfRepTestType"))
)
if mibBuilder.loadTexts:
    systemRfc2544TestEnd.setStatus(
        "current"
    )

systemItuSatTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 4)
)
systemItuSatTestStart.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "ituSatGeneratorStatus"),
        ("RAD-TEST-MIB", "ituSatGeneratorName"))
)
if mibBuilder.loadTexts:
    systemItuSatTestStart.setStatus(
        "current"
    )

systemItuSatConfigurationTestEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 5)
)
systemItuSatConfigurationTestEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "ituSatGeneratorConfResult"),
        ("RAD-TEST-MIB", "ituSatGeneratorName"))
)
if mibBuilder.loadTexts:
    systemItuSatConfigurationTestEnd.setStatus(
        "current"
    )

systemItuSatPerformanceTestEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 6)
)
systemItuSatPerformanceTestEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "ituSatGeneratorPerfResult"),
        ("RAD-TEST-MIB", "ituSatGeneratorName"))
)
if mibBuilder.loadTexts:
    systemItuSatPerformanceTestEnd.setStatus(
        "current"
    )

systemItuSatResponderActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 7)
)
systemItuSatResponderActivated.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "ituSatResponderStatus"),
        ("RAD-TEST-MIB", "ituSatResponderName"))
)
if mibBuilder.loadTexts:
    systemItuSatResponderActivated.setStatus(
        "current"
    )

systemItuSatResponderDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 8)
)
systemItuSatResponderDeactivated.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-TEST-MIB", "ituSatResponderStatus"),
        ("RAD-TEST-MIB", "ituSatResponderName"))
)
if mibBuilder.loadTexts:
    systemItuSatResponderDeactivated.setStatus(
        "current"
    )

twampPeerTestStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 9)
)
twampPeerTestStarted.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampPeerDescr"))
)
if mibBuilder.loadTexts:
    twampPeerTestStarted.setStatus(
        "current"
    )

twampPeerTestStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 10)
)
twampPeerTestStopped.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampPeerDescr"))
)
if mibBuilder.loadTexts:
    twampPeerTestStopped.setStatus(
        "current"
    )

twampSessionLossRatioTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 11)
)
twampSessionLossRatioTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"))
)
if mibBuilder.loadTexts:
    twampSessionLossRatioTca.setStatus(
        "current"
    )

twampSessionDelayTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 12)
)
twampSessionDelayTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"))
)
if mibBuilder.loadTexts:
    twampSessionDelayTca.setStatus(
        "current"
    )

twampSessionDelayVarTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 13)
)
twampSessionDelayVarTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"),
        ("RAD-TEST-MIB", "twampTestProfileDelayVarEventType"))
)
if mibBuilder.loadTexts:
    twampSessionDelayVarTca.setStatus(
        "current"
    )

twampSessionUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 14)
)
twampSessionUnavailable.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampControllerName"))
)
if mibBuilder.loadTexts:
    twampSessionUnavailable.setStatus(
        "current"
    )

twampSessionForwardUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 15)
)
twampSessionForwardUnavailable.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampControllerName"))
)
if mibBuilder.loadTexts:
    twampSessionForwardUnavailable.setStatus(
        "current"
    )

twampSessionBackwardUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 16)
)
twampSessionBackwardUnavailable.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampControllerName"))
)
if mibBuilder.loadTexts:
    twampSessionBackwardUnavailable.setStatus(
        "current"
    )

twampSessionForwardLossRatioTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 17)
)
twampSessionForwardLossRatioTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"))
)
if mibBuilder.loadTexts:
    twampSessionForwardLossRatioTca.setStatus(
        "current"
    )

twampSessionForwardDelayTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 18)
)
twampSessionForwardDelayTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"))
)
if mibBuilder.loadTexts:
    twampSessionForwardDelayTca.setStatus(
        "current"
    )

twampSessionForwardDelayVarTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 19)
)
twampSessionForwardDelayVarTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"),
        ("RAD-TEST-MIB", "twampTestProfileDelayVarEventType"))
)
if mibBuilder.loadTexts:
    twampSessionForwardDelayVarTca.setStatus(
        "current"
    )

twampSessionBackwardLossRatioTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 20)
)
twampSessionBackwardLossRatioTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"))
)
if mibBuilder.loadTexts:
    twampSessionBackwardLossRatioTca.setStatus(
        "current"
    )

twampSessionBackwardDelayTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 21)
)
twampSessionBackwardDelayTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"))
)
if mibBuilder.loadTexts:
    twampSessionBackwardDelayTca.setStatus(
        "current"
    )

twampSessionBackwardDelayVarTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 22)
)
twampSessionBackwardDelayVarTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampContSessionName"),
        ("RAD-TEST-MIB", "twampContSessionStatus"),
        ("RAD-TEST-MIB", "twampTestProfileDelayVarEventType"))
)
if mibBuilder.loadTexts:
    twampSessionBackwardDelayVarTca.setStatus(
        "current"
    )

twampPeerTodAccuracyOutOfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 37)
)
twampPeerTodAccuracyOutOfLimit.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-TEST-MIB", "twampPeerDescr"))
)
if mibBuilder.loadTexts:
    twampPeerTodAccuracyOutOfLimit.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-TEST-MIB",
    **{"RadTestPerfRepFrameSize": RadTestPerfRepFrameSize,
       "RadTestPerfresultFrameSize": RadTestPerfresultFrameSize,
       "RadTestPbitIndex": RadTestPbitIndex,
       "radTest": radTest,
       "radTestPrefRepEvents": radTestPrefRepEvents,
       "systemRfc2544TestStart": systemRfc2544TestStart,
       "systemRfc2544TestEnd": systemRfc2544TestEnd,
       "systemItuSatTestStart": systemItuSatTestStart,
       "systemItuSatConfigurationTestEnd": systemItuSatConfigurationTestEnd,
       "systemItuSatPerformanceTestEnd": systemItuSatPerformanceTestEnd,
       "systemItuSatResponderActivated": systemItuSatResponderActivated,
       "systemItuSatResponderDeactivated": systemItuSatResponderDeactivated,
       "twampPeerTestStarted": twampPeerTestStarted,
       "twampPeerTestStopped": twampPeerTestStopped,
       "twampSessionLossRatioTca": twampSessionLossRatioTca,
       "twampSessionDelayTca": twampSessionDelayTca,
       "twampSessionDelayVarTca": twampSessionDelayVarTca,
       "twampSessionUnavailable": twampSessionUnavailable,
       "twampSessionForwardUnavailable": twampSessionForwardUnavailable,
       "twampSessionBackwardUnavailable": twampSessionBackwardUnavailable,
       "twampSessionForwardLossRatioTca": twampSessionForwardLossRatioTca,
       "twampSessionForwardDelayTca": twampSessionForwardDelayTca,
       "twampSessionForwardDelayVarTca": twampSessionForwardDelayVarTca,
       "twampSessionBackwardLossRatioTca": twampSessionBackwardLossRatioTca,
       "twampSessionBackwardDelayTca": twampSessionBackwardDelayTca,
       "twampSessionBackwardDelayVarTca": twampSessionBackwardDelayVarTca,
       "twampPeerTodAccuracyOutOfLimit": twampPeerTodAccuracyOutOfLimit,
       "radTestPrefRepProfile": radTestPrefRepProfile,
       "tstNePerfRepProfileTable": tstNePerfRepProfileTable,
       "tstNePerfRepProfileEntry": tstNePerfRepProfileEntry,
       "tstNePerfRepProfileId": tstNePerfRepProfileId,
       "tstNePerfRepProfileName": tstNePerfRepProfileName,
       "tstNePerfRepProfileRowStatus": tstNePerfRepProfileRowStatus,
       "tstNePerfRepProfileFrameSize": tstNePerfRepProfileFrameSize,
       "tstNePerfRepProfilePattern": tstNePerfRepProfilePattern,
       "tstNePerfRepProfileDirection": tstNePerfRepProfileDirection,
       "tstNePerfRepProfileTlv": tstNePerfRepProfileTlv,
       "tstNePerfRepProfileNumberOfFramesInOneBurst": tstNePerfRepProfileNumberOfFramesInOneBurst,
       "tstNePerfRepProfileFrameLossTolerance": tstNePerfRepProfileFrameLossTolerance,
       "tstNePerfRepProfileBinarySearchResolution": tstNePerfRepProfileBinarySearchResolution,
       "tstNePerfRepProfileNumberOfTrials": tstNePerfRepProfileNumberOfTrials,
       "tstNePerfRepProfileLearningFramesMode": tstNePerfRepProfileLearningFramesMode,
       "tstNePerfRepProfileLearningFrames": tstNePerfRepProfileLearningFrames,
       "tstNePerfRepProfileCustomSize": tstNePerfRepProfileCustomSize,
       "tstNePerfRepProfileTransmitLck": tstNePerfRepProfileTransmitLck,
       "tstMepFlowTable": tstMepFlowTable,
       "tstMepFlowEntry": tstMepFlowEntry,
       "tstMepFlowIndex": tstMepFlowIndex,
       "tstMepFlowFlowIdx": tstMepFlowFlowIdx,
       "ituSatProfileTable": ituSatProfileTable,
       "ituSatProfileEntry": ituSatProfileEntry,
       "ituSatProfileIndex": ituSatProfileIndex,
       "ituSatProfileName": ituSatProfileName,
       "ituSatProfileRowStatus": ituSatProfileRowStatus,
       "ituSatProfileEtherType": ituSatProfileEtherType,
       "ituSatProfileFrameSize": ituSatProfileFrameSize,
       "ituSatProfileUniFlrThreshold": ituSatProfileUniFlrThreshold,
       "ituSatProfileUniFtdThreshold": ituSatProfileUniFtdThreshold,
       "ituSatProfileUniFdvThreshold": ituSatProfileUniFdvThreshold,
       "ituSatProfileUniAvailThreshold": ituSatProfileUniAvailThreshold,
       "ituSatProfileBiFlrThreshold": ituSatProfileBiFlrThreshold,
       "ituSatProfileBiFtdThreshold": ituSatProfileBiFtdThreshold,
       "ituSatProfileBiFdvThreshold": ituSatProfileBiFdvThreshold,
       "ituSatProfileBiAvailThreshold": ituSatProfileBiAvailThreshold,
       "ituSatProfileScope": ituSatProfileScope,
       "ituSatProfileDirection": ituSatProfileDirection,
       "ituSatProfileColorMode": ituSatProfileColorMode,
       "ituSatProfileTrafficPolicing": ituSatProfileTrafficPolicing,
       "ituSatProfileCirSteps": ituSatProfileCirSteps,
       "ituSatProfileConfDuration": ituSatProfileConfDuration,
       "ituSatProfilePerfDuration": ituSatProfilePerfDuration,
       "ituSatProfileRateConvention": ituSatProfileRateConvention,
       "ituSatProfileResponderType": ituSatProfileResponderType,
       "ituSatProfilePbitTable": ituSatProfilePbitTable,
       "ituSatProfilePbitEntry": ituSatProfilePbitEntry,
       "ituSatProfilePbitIndex": ituSatProfilePbitIndex,
       "ituSatProfilePbitRowStatus": ituSatProfilePbitRowStatus,
       "ituSatProfilePbitFrameSize": ituSatProfilePbitFrameSize,
       "ituSatProfilePbitUniFlrThreshold": ituSatProfilePbitUniFlrThreshold,
       "ituSatProfilePbitUniFtdThreshold": ituSatProfilePbitUniFtdThreshold,
       "ituSatProfilePbitUniFdvThreshold": ituSatProfilePbitUniFdvThreshold,
       "ituSatProfilePbitUniAvailThreshold": ituSatProfilePbitUniAvailThreshold,
       "ituSatProfilePbitBiFlrThreshold": ituSatProfilePbitBiFlrThreshold,
       "ituSatProfilePbitBiFtdThreshold": ituSatProfilePbitBiFtdThreshold,
       "ituSatProfilePbitBiFdvThreshold": ituSatProfilePbitBiFdvThreshold,
       "ituSatProfilePbitBiAvailThreshold": ituSatProfilePbitBiAvailThreshold,
       "twampTestProfileTable": twampTestProfileTable,
       "twampTestProfileEntry": twampTestProfileEntry,
       "twampTestProfileId": twampTestProfileId,
       "twampTestProfileRowStatus": twampTestProfileRowStatus,
       "twampTestProfileName": twampTestProfileName,
       "twampTestProfilePayloadLength": twampTestProfilePayloadLength,
       "twampTestProfileTxRate": twampTestProfileTxRate,
       "twampTestProfileLossTimeout": twampTestProfileLossTimeout,
       "twampTestProfileLossRatioThreshold": twampTestProfileLossRatioThreshold,
       "twampTestProfileDelayThreshold": twampTestProfileDelayThreshold,
       "twampTestProfileDelayVarThreshold": twampTestProfileDelayVarThreshold,
       "twampTestProfileDelayVarEventType": twampTestProfileDelayVarEventType,
       "radTestPrefRepTest": radTestPrefRepTest,
       "tstNePerfRepTestTable": tstNePerfRepTestTable,
       "tstNePerfRepTestEntry": tstNePerfRepTestEntry,
       "tstNePerfRepTestId": tstNePerfRepTestId,
       "tstNePerfRepTestRowStatus": tstNePerfRepTestRowStatus,
       "tstNePerfRepTestType": tstNePerfRepTestType,
       "tstNePerfRepTestProfileId": tstNePerfRepTestProfileId,
       "tstNePerfRepTestEntity": tstNePerfRepTestEntity,
       "tstNePerfRepTestActivation": tstNePerfRepTestActivation,
       "tstNePerfRepTestStatus": tstNePerfRepTestStatus,
       "tstNePerfRepTestActivationDateAndTime": tstNePerfRepTestActivationDateAndTime,
       "tstNePerfRepTestActivationRecurrenceTime": tstNePerfRepTestActivationRecurrenceTime,
       "tstNePerfRepTestMaxRate": tstNePerfRepTestMaxRate,
       "tstNePerfRepTestElapsedTime": tstNePerfRepTestElapsedTime,
       "tstNePerfRepTestResetResults": tstNePerfRepTestResetResults,
       "tstNePerfRepTestRateConvention": tstNePerfRepTestRateConvention,
       "tstNePerfRepTestFrameCompensation": tstNePerfRepTestFrameCompensation,
       "tstNePerfRepTestMaxTestDuration": tstNePerfRepTestMaxTestDuration,
       "tstNePerfRepTestAssociatedFlow": tstNePerfRepTestAssociatedFlow,
       "ituSatGeneratorTable": ituSatGeneratorTable,
       "ituSatGeneratorEntry": ituSatGeneratorEntry,
       "ituSatGeneratorIndex": ituSatGeneratorIndex,
       "ituSatGeneratorName": ituSatGeneratorName,
       "ituSatGeneratorRowStatus": ituSatGeneratorRowStatus,
       "ituSatGeneratorServicePointer": ituSatGeneratorServicePointer,
       "ituSatGeneratorProvisionedPbits": ituSatGeneratorProvisionedPbits,
       "ituSatGeneratorProfile": ituSatGeneratorProfile,
       "ituSatGeneratorCmd": ituSatGeneratorCmd,
       "ituSatGeneratorConfChanged": ituSatGeneratorConfChanged,
       "ituSatGeneratorStatus": ituSatGeneratorStatus,
       "ituSatGeneratorTimeRemaining": ituSatGeneratorTimeRemaining,
       "ituSatGeneratorCurrentPhase": ituSatGeneratorCurrentPhase,
       "ituSatGeneratorDestination": ituSatGeneratorDestination,
       "ituSatGeneratorSource": ituSatGeneratorSource,
       "ituSatGeneratorInnerTag": ituSatGeneratorInnerTag,
       "ituSatGeneratorOuterTag": ituSatGeneratorOuterTag,
       "ituSatGeneratorTestedPbits": ituSatGeneratorTestedPbits,
       "ituSatGeneratorStartTime": ituSatGeneratorStartTime,
       "ituSatGeneratorEndTime": ituSatGeneratorEndTime,
       "ituSatGeneratorTimeElapsed": ituSatGeneratorTimeElapsed,
       "ituSatGeneratorConfResult": ituSatGeneratorConfResult,
       "ituSatGeneratorPerfResult": ituSatGeneratorPerfResult,
       "ituSatGeneratorConfDuration": ituSatGeneratorConfDuration,
       "ituSatGeneratorPerfDuration": ituSatGeneratorPerfDuration,
       "ituSatGeneratorScope": ituSatGeneratorScope,
       "ituSatGeneratorServiceBinding": ituSatGeneratorServiceBinding,
       "ituSatGeneratorServiceName": ituSatGeneratorServiceName,
       "ituSatGeneratorEgressPort": ituSatGeneratorEgressPort,
       "ituSatGeneratorProvisionedDestination": ituSatGeneratorProvisionedDestination,
       "ituSatGeneratorFlowTable": ituSatGeneratorFlowTable,
       "ituSatGeneratorFlowEntry": ituSatGeneratorFlowEntry,
       "ituSatGeneratorFlowPbitIndex": ituSatGeneratorFlowPbitIndex,
       "ituSatGeneratorFlowNameTx": ituSatGeneratorFlowNameTx,
       "ituSatGeneratorFlowNameRx": ituSatGeneratorFlowNameRx,
       "ituSatGeneratorFlowCir": ituSatGeneratorFlowCir,
       "ituSatGeneratorFlowEir": ituSatGeneratorFlowEir,
       "ituSatGeneratorFlowAssociatedMEP": ituSatGeneratorFlowAssociatedMEP,
       "ituSatGeneratorFlowAssociatedService": ituSatGeneratorFlowAssociatedService,
       "ituSatGeneratorFlowBwpInUse": ituSatGeneratorFlowBwpInUse,
       "ituSatResponderTable": ituSatResponderTable,
       "ituSatResponderEntry": ituSatResponderEntry,
       "ituSatResponderIndex": ituSatResponderIndex,
       "ituSatResponderName": ituSatResponderName,
       "ituSatResponderRowStatus": ituSatResponderRowStatus,
       "ituSatResponderServicePointer": ituSatResponderServicePointer,
       "ituSatResponderProfile": ituSatResponderProfile,
       "ituSatResponderCmd": ituSatResponderCmd,
       "ituSatResponderStatus": ituSatResponderStatus,
       "ituSatResponderServiceBinding": ituSatResponderServiceBinding,
       "ituSatResponderServiceName": ituSatResponderServiceName,
       "ituSatResponderEgressPort": ituSatResponderEgressPort,
       "ituSatGeneratorPolicerTable": ituSatGeneratorPolicerTable,
       "ituSatGeneratorPolicerEntry": ituSatGeneratorPolicerEntry,
       "ituSatGeneratorPolicerPbitIndex": ituSatGeneratorPolicerPbitIndex,
       "ituSatGeneratorPolicerRowStatus": ituSatGeneratorPolicerRowStatus,
       "ituSatGeneratorPolicerCir": ituSatGeneratorPolicerCir,
       "ituSatGeneratorPolicerCbs": ituSatGeneratorPolicerCbs,
       "ituSatGeneratorPolicerEir": ituSatGeneratorPolicerEir,
       "ituSatGeneratorPolicerEbs": ituSatGeneratorPolicerEbs,
       "ituSatGeneratorPolicerProfile": ituSatGeneratorPolicerProfile,
       "twampControllerTable": twampControllerTable,
       "twampControllerEntry": twampControllerEntry,
       "twampControllerId": twampControllerId,
       "twampControllerRowStatus": twampControllerRowStatus,
       "twampControllerName": twampControllerName,
       "twampControllerStatus": twampControllerStatus,
       "twampControllerType": twampControllerType,
       "twampControllerL2Probe": twampControllerL2Probe,
       "twampControllerIngressEgressPort": twampControllerIngressEgressPort,
       "twampControllerOuterVlan": twampControllerOuterVlan,
       "twampControllerInnerVlan": twampControllerInnerVlan,
       "twampControllerOuterPbit": twampControllerOuterPbit,
       "twampControllerInnerPbit": twampControllerInnerPbit,
       "twampControllerRouterEntity": twampControllerRouterEntity,
       "twampControllerLocalAddrType": twampControllerLocalAddrType,
       "twampControllerLocalAddr": twampControllerLocalAddr,
       "twampControllerAssociatedRI": twampControllerAssociatedRI,
       "twampControllerTodStatus": twampControllerTodStatus,
       "twampPeerTable": twampPeerTable,
       "twampPeerEntry": twampPeerEntry,
       "twampPeerAddrType": twampPeerAddrType,
       "twampPeerAddr": twampPeerAddr,
       "twampPeerRowStatus": twampPeerRowStatus,
       "twampPeerActivateCmd": twampPeerActivateCmd,
       "twampPeerActivateDuration": twampPeerActivateDuration,
       "twampPeerStartDateAndTime": twampPeerStartDateAndTime,
       "twampPeerCalcMode": twampPeerCalcMode,
       "twampPeerResponderSeqNum": twampPeerResponderSeqNum,
       "twampPeerResponderTodStatus": twampPeerResponderTodStatus,
       "twampPeerElapsedTime": twampPeerElapsedTime,
       "twampPeerDescr": twampPeerDescr,
       "twampPeerLastCalcMode": twampPeerLastCalcMode,
       "twampPeerLastResponderSeqNum": twampPeerLastResponderSeqNum,
       "twampContSessionTable": twampContSessionTable,
       "twampContSessionEntry": twampContSessionEntry,
       "twampContSessionId": twampContSessionId,
       "twampContSessionRowStatus": twampContSessionRowStatus,
       "twampContSessionName": twampContSessionName,
       "twampContSessionStartDateAndTime": twampContSessionStartDateAndTime,
       "twampContSessionStatus": twampContSessionStatus,
       "twampContSessionLocalL4PortNumber": twampContSessionLocalL4PortNumber,
       "twampContSessionPeerL4PortNumber": twampContSessionPeerL4PortNumber,
       "twampContSessionPeerDscp": twampContSessionPeerDscp,
       "twampContSessionTestProfileId": twampContSessionTestProfileId,
       "twampContSessionTxPackets": twampContSessionTxPackets,
       "twampContSessionRxPackets": twampContSessionRxPackets,
       "twampContSessionResult": twampContSessionResult,
       "twampContSessionConfChanged": twampContSessionConfChanged,
       "twampContSessionConvertedIndex": twampContSessionConvertedIndex,
       "twampContSessionResultFwd": twampContSessionResultFwd,
       "twampContSessionResultBck": twampContSessionResultBck,
       "twampResponderTable": twampResponderTable,
       "twampResponderEntry": twampResponderEntry,
       "twampResponderId": twampResponderId,
       "twampResponderRowStatus": twampResponderRowStatus,
       "twampResponderName": twampResponderName,
       "twampResponderStatus": twampResponderStatus,
       "twampResponderType": twampResponderType,
       "twampResponderL2Probe": twampResponderL2Probe,
       "twampResponderIngressEgressPort": twampResponderIngressEgressPort,
       "twampResponderOuterVlan": twampResponderOuterVlan,
       "twampResponderInnerVlan": twampResponderInnerVlan,
       "twampResponderOuterPbit": twampResponderOuterPbit,
       "twampResponderInnerPbit": twampResponderInnerPbit,
       "twampResponderRouterEntity": twampResponderRouterEntity,
       "twampResponderLocalAddrType": twampResponderLocalAddrType,
       "twampResponderLocalAddr": twampResponderLocalAddr,
       "twampResponderAssociatedRI": twampResponderAssociatedRI,
       "twampResponderTxSeqNum": twampResponderTxSeqNum,
       "twampResponderTxExtendedInfo": twampResponderTxExtendedInfo,
       "twampResSessionTable": twampResSessionTable,
       "twampResSessionEntry": twampResSessionEntry,
       "twampResSessionId": twampResSessionId,
       "twampResSessionRowStatus": twampResSessionRowStatus,
       "twampResSessionName": twampResSessionName,
       "twampResSessionLocalL4PortNumber": twampResSessionLocalL4PortNumber,
       "twampResSessionTxPackets": twampResSessionTxPackets,
       "twampResSessionRxPackets": twampResSessionRxPackets,
       "ituSatSingleCosFlowTable": ituSatSingleCosFlowTable,
       "ituSatSingleCosFlowEntry": ituSatSingleCosFlowEntry,
       "ituSatSingleCosFlowFunction": ituSatSingleCosFlowFunction,
       "ituSatSingleCosFlowFunctionIndex": ituSatSingleCosFlowFunctionIndex,
       "ituSatSingleCosFlowIdx1": ituSatSingleCosFlowIdx1,
       "ituSatSingleCosFlowIdx2": ituSatSingleCosFlowIdx2,
       "ituSatSingleCosFlowRowStatus": ituSatSingleCosFlowRowStatus,
       "radTestPerfRepResults": radTestPerfRepResults,
       "tstNePerfRepGeneralResultsTable": tstNePerfRepGeneralResultsTable,
       "tstNePerfRepGeneralResultsEntry": tstNePerfRepGeneralResultsEntry,
       "tstNePerfRepGeneralResultsTestType": tstNePerfRepGeneralResultsTestType,
       "tstNePerfRepGeneralResultsTrialNumber": tstNePerfRepGeneralResultsTrialNumber,
       "tstNePerfRepGeneralResultsStatus": tstNePerfRepGeneralResultsStatus,
       "tstNePerfRepGeneralResultsDuration": tstNePerfRepGeneralResultsDuration,
       "throughputReportTable": throughputReportTable,
       "throughputReportEntry": throughputReportEntry,
       "throughputReportTrialNumber": throughputReportTrialNumber,
       "throughputReportPacketSize": throughputReportPacketSize,
       "throughputReportThroughputTheoretical": throughputReportThroughputTheoretical,
       "throughputReportResults": throughputReportResults,
       "throughputReportDataPattern": throughputReportDataPattern,
       "throughputReportResultsBps": throughputReportResultsBps,
       "throughputReportCustomPacketSize": throughputReportCustomPacketSize,
       "latencyReportTable": latencyReportTable,
       "latencyReportEntry": latencyReportEntry,
       "latencyReportTrialNumber": latencyReportTrialNumber,
       "latencyReportPacketSize": latencyReportPacketSize,
       "latencyReportType": latencyReportType,
       "latencyReportResult": latencyReportResult,
       "latencyReportCustomPacketSize": latencyReportCustomPacketSize,
       "framelossRateReportTable": framelossRateReportTable,
       "framelossRateReportEntry": framelossRateReportEntry,
       "framelossRateReportTrialNumber": framelossRateReportTrialNumber,
       "framelossRateReportPacketSize": framelossRateReportPacketSize,
       "framelossRateReportInputRate": framelossRateReportInputRate,
       "framelossRateReportResults": framelossRateReportResults,
       "framelossRateReportCustomPacketSize": framelossRateReportCustomPacketSize,
       "tstNePerfRepStatusTable": tstNePerfRepStatusTable,
       "tstNePerfRepStatusEntry": tstNePerfRepStatusEntry,
       "tstNePerfRepIteration": tstNePerfRepIteration,
       "tstNePerfRepStartTime": tstNePerfRepStartTime,
       "tstNePerfRepDuration": tstNePerfRepDuration,
       "tstNePerfRepStatus": tstNePerfRepStatus,
       "tstNePerfRepType": tstNePerfRepType,
       "tstNePerfRepIterationNum": tstNePerfRepIterationNum,
       "tstNePerfRepTrial": tstNePerfRepTrial,
       "tstNePerfRepAttemptNum": tstNePerfRepAttemptNum,
       "tstNePerfRepFrameSize": tstNePerfRepFrameSize,
       "tstNePerfRepLatencyNum": tstNePerfRepLatencyNum,
       "ituSatReportTable": ituSatReportTable,
       "ituSatReportEntry": ituSatReportEntry,
       "ituSatReportPbitIndex": ituSatReportPbitIndex,
       "ituSatReportTestTypeIndex": ituSatReportTestTypeIndex,
       "ituSatReportDirectionIndex": ituSatReportDirectionIndex,
       "ituSatReportResult": ituSatReportResult,
       "ituSatReportTxRate": ituSatReportTxRate,
       "ituSatReportIrMin": ituSatReportIrMin,
       "ituSatReportIrAverage": ituSatReportIrAverage,
       "ituSatReportIrMax": ituSatReportIrMax,
       "ituSatReportTxFrames": ituSatReportTxFrames,
       "ituSatReportLostFrames": ituSatReportLostFrames,
       "ituSatReportFtdMin": ituSatReportFtdMin,
       "ituSatReportFtdAverage": ituSatReportFtdAverage,
       "ituSatReportFtdMax": ituSatReportFtdMax,
       "ituSatReportFtdStd": ituSatReportFtdStd,
       "ituSatReportFdvAverage": ituSatReportFdvAverage,
       "ituSatReportFdvMax": ituSatReportFdvMax,
       "ituSatReportUas": ituSatReportUas,
       "ituSatReportAvailability": ituSatReportAvailability,
       "ituSatReportTotalTxRate": ituSatReportTotalTxRate,
       "ituSatReportTotalIrAverage": ituSatReportTotalIrAverage,
       "ituSatReportTotalTxFrames": ituSatReportTotalTxFrames,
       "ituSatReportTotalLostFrames": ituSatReportTotalLostFrames,
       "ituSatResponderPerfTable": ituSatResponderPerfTable,
       "ituSatResponderPerfEntry": ituSatResponderPerfEntry,
       "ituSatResponderPerfPbitIndex": ituSatResponderPerfPbitIndex,
       "ituSatResponderPerfRxFrames": ituSatResponderPerfRxFrames,
       "ituSatResponderPerfTxFrames": ituSatResponderPerfTxFrames,
       "ituSatResponderPerfAssociatedMEP": ituSatResponderPerfAssociatedMEP,
       "ituSatResponderPerfAssociatedService": ituSatResponderPerfAssociatedService,
       "ituSatConfPbitTable": ituSatConfPbitTable,
       "ituSatConfPbitEntry": ituSatConfPbitEntry,
       "ituSatConfPbitIndex": ituSatConfPbitIndex,
       "ituSatConfPbitDirectionIndex": ituSatConfPbitDirectionIndex,
       "ituSatConfPbitResult": ituSatConfPbitResult,
       "twampReportCurrentTable": twampReportCurrentTable,
       "twampReportCurrentEntry": twampReportCurrentEntry,
       "twampReportCurrentStartDateAndTime": twampReportCurrentStartDateAndTime,
       "twampReportCurrentElapsedTime": twampReportCurrentElapsedTime,
       "twampReportCurrentTxPackets": twampReportCurrentTxPackets,
       "twampReportCurrentRxValidPackets": twampReportCurrentRxValidPackets,
       "twampReportCurrentLossPackets": twampReportCurrentLossPackets,
       "twampReportCurrentAvailableSeconds": twampReportCurrentAvailableSeconds,
       "twampReportCurrentDelayMin": twampReportCurrentDelayMin,
       "twampReportCurrentDelayMax": twampReportCurrentDelayMax,
       "twampReportCurrentDelaySum": twampReportCurrentDelaySum,
       "twampReportCurrentDelayAverage": twampReportCurrentDelayAverage,
       "twampReportCurrentDelayedPackets": twampReportCurrentDelayedPackets,
       "twampReportCurrentPdvMax": twampReportCurrentPdvMax,
       "twampReportCurrentIpdvMax": twampReportCurrentIpdvMax,
       "twampReportCurrentIpdvSum": twampReportCurrentIpdvSum,
       "twampReportCurrentIpdvValidResults": twampReportCurrentIpdvValidResults,
       "twampReportCurrentIpdvFwdMax": twampReportCurrentIpdvFwdMax,
       "twampReportCurrentIpdvFwdSum": twampReportCurrentIpdvFwdSum,
       "twampReportCurrentIpdvFwdValidResults": twampReportCurrentIpdvFwdValidResults,
       "twampReportCurrentIpdvBckMax": twampReportCurrentIpdvBckMax,
       "twampReportCurrentIpdvBckSum": twampReportCurrentIpdvBckSum,
       "twampReportCurrentIpdvBckValidResults": twampReportCurrentIpdvBckValidResults,
       "twampReportCurrentReorderedFwd": twampReportCurrentReorderedFwd,
       "twampReportCurrentReorderedBck": twampReportCurrentReorderedBck,
       "twampReportCurrentDuplicateFwd": twampReportCurrentDuplicateFwd,
       "twampReportCurrentDuplicateBck": twampReportCurrentDuplicateBck,
       "twampReportCurrentFragmentedFwd": twampReportCurrentFragmentedFwd,
       "twampReportCurrentFragmentedBck": twampReportCurrentFragmentedBck,
       "twampReportCurrentDelayFwdMin": twampReportCurrentDelayFwdMin,
       "twampReportCurrentDelayFwdMax": twampReportCurrentDelayFwdMax,
       "twampReportCurrentDelayFwdSum": twampReportCurrentDelayFwdSum,
       "twampReportCurrentDelayBckMin": twampReportCurrentDelayBckMin,
       "twampReportCurrentDelayBckMax": twampReportCurrentDelayBckMax,
       "twampReportCurrentDelayBckSum": twampReportCurrentDelayBckSum,
       "twampReportCurrentDelayedPacketsFwd": twampReportCurrentDelayedPacketsFwd,
       "twampReportCurrentDelayedPacketsBck": twampReportCurrentDelayedPacketsBck,
       "twampReportCurrentPdvMaxFwd": twampReportCurrentPdvMaxFwd,
       "twampReportCurrentPdvMaxBck": twampReportCurrentPdvMaxBck,
       "twampReportCurrentTxPacketsFwd": twampReportCurrentTxPacketsFwd,
       "twampReportCurrentTxPacketsBck": twampReportCurrentTxPacketsBck,
       "twampReportCurrentRxValidPacketsFwd": twampReportCurrentRxValidPacketsFwd,
       "twampReportCurrentRxValidPacketsBck": twampReportCurrentRxValidPacketsBck,
       "twampReportCurrentLossPacketsFwd": twampReportCurrentLossPacketsFwd,
       "twampReportCurrentLossPacketsBck": twampReportCurrentLossPacketsBck,
       "twampReportCurrentAvailableSecondsFwd": twampReportCurrentAvailableSecondsFwd,
       "twampReportCurrentAvailableSecondsBck": twampReportCurrentAvailableSecondsBck,
       "twampReportCurrentRxSyncValidPacketsFwd": twampReportCurrentRxSyncValidPacketsFwd,
       "twampReportCurrentRxSyncValidPacketsBck": twampReportCurrentRxSyncValidPacketsBck,
       "twampReportCurrentSyncSeconds": twampReportCurrentSyncSeconds,
       "twampReportIntervalTable": twampReportIntervalTable,
       "twampReportIntervalEntry": twampReportIntervalEntry,
       "twampReportIntervalNumber": twampReportIntervalNumber,
       "twampReportIntervalStartDateAndTime": twampReportIntervalStartDateAndTime,
       "twampReportIntervalElapsedTime": twampReportIntervalElapsedTime,
       "twampReportIntervalTxPackets": twampReportIntervalTxPackets,
       "twampReportIntervalRxValidPackets": twampReportIntervalRxValidPackets,
       "twampReportIntervalLossPackets": twampReportIntervalLossPackets,
       "twampReportIntervalAvailableSeconds": twampReportIntervalAvailableSeconds,
       "twampReportIntervalDelayMin": twampReportIntervalDelayMin,
       "twampReportIntervalDelayMax": twampReportIntervalDelayMax,
       "twampReportIntervalDelaySum": twampReportIntervalDelaySum,
       "twampReportIntervalDelayAverage": twampReportIntervalDelayAverage,
       "twampReportIntervalDelayedPackets": twampReportIntervalDelayedPackets,
       "twampReportIntervalPdvMax": twampReportIntervalPdvMax,
       "twampReportIntervalIpdvMax": twampReportIntervalIpdvMax,
       "twampReportIntervalIpdvSum": twampReportIntervalIpdvSum,
       "twampReportIntervalIpdvValidResults": twampReportIntervalIpdvValidResults,
       "twampReportIntervalIpdvFwdMax": twampReportIntervalIpdvFwdMax,
       "twampReportIntervalIpdvFwdSum": twampReportIntervalIpdvFwdSum,
       "twampReportIntervalIpdvFwdValidResults": twampReportIntervalIpdvFwdValidResults,
       "twampReportIntervalIpdvBckMax": twampReportIntervalIpdvBckMax,
       "twampReportIntervalIpdvBckSum": twampReportIntervalIpdvBckSum,
       "twampReportIntervalIpdvBckValidResults": twampReportIntervalIpdvBckValidResults,
       "twampReportIntervalReorderedFwd": twampReportIntervalReorderedFwd,
       "twampReportIntervalReorderedBck": twampReportIntervalReorderedBck,
       "twampReportIntervalDuplicateFwd": twampReportIntervalDuplicateFwd,
       "twampReportIntervalDuplicateBck": twampReportIntervalDuplicateBck,
       "twampReportIntervalFragmentedFwd": twampReportIntervalFragmentedFwd,
       "twampReportIntervalFragmentedBck": twampReportIntervalFragmentedBck,
       "twampReportIntervalDelayFwdMin": twampReportIntervalDelayFwdMin,
       "twampReportIntervalDelayFwdMax": twampReportIntervalDelayFwdMax,
       "twampReportIntervalDelayFwdSum": twampReportIntervalDelayFwdSum,
       "twampReportIntervalDelayBckMin": twampReportIntervalDelayBckMin,
       "twampReportIntervalDelayBckMax": twampReportIntervalDelayBckMax,
       "twampReportIntervalDelayBckSum": twampReportIntervalDelayBckSum,
       "twampReportIntervalDelayedPacketsFwd": twampReportIntervalDelayedPacketsFwd,
       "twampReportIntervalDelayedPacketsBck": twampReportIntervalDelayedPacketsBck,
       "twampReportIntervalPdvMaxFwd": twampReportIntervalPdvMaxFwd,
       "twampReportIntervalPdvMaxBck": twampReportIntervalPdvMaxBck,
       "twampReportIntervalTxPacketsFwd": twampReportIntervalTxPacketsFwd,
       "twampReportIntervalValidData": twampReportIntervalValidData,
       "twampReportIntervalTxPacketsBck": twampReportIntervalTxPacketsBck,
       "twampReportIntervalRxValidPacketsFwd": twampReportIntervalRxValidPacketsFwd,
       "twampReportIntervalRxValidPacketsBck": twampReportIntervalRxValidPacketsBck,
       "twampReportIntervalLossPacketsFwd": twampReportIntervalLossPacketsFwd,
       "twampReportIntervalLossPacketsBck": twampReportIntervalLossPacketsBck,
       "twampReportIntervalAvailableSecondsFwd": twampReportIntervalAvailableSecondsFwd,
       "twampReportIntervalAvailableSecondsBck": twampReportIntervalAvailableSecondsBck,
       "twampReportIntervalRxSyncValidPacketsFwd": twampReportIntervalRxSyncValidPacketsFwd,
       "twampReportIntervalRxSyncValidPacketsBck": twampReportIntervalRxSyncValidPacketsBck,
       "twampReportIntervalSyncSeconds": twampReportIntervalSyncSeconds,
       "tstNeThroughputIterationTable": tstNeThroughputIterationTable,
       "tstNeThroughputIterationEntry": tstNeThroughputIterationEntry,
       "tstNeThroughputIteration": tstNeThroughputIteration,
       "tstNeThroughputIterationBPS": tstNeThroughputIterationBPS,
       "tstNeThroughputLossPacket": tstNeThroughputLossPacket}
)
