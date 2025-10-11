# SNMP MIB module (TIMETRA-CALLTRACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-CALLTRACE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:52:26 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxSlotNum,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxSlotNum")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxEncapVal,
 TmnxPortID,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxVRtrID")


# MODULE-IDENTITY

timetraCallTraceMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 102)
)
if mibBuilder.loadTexts:
    timetraCallTraceMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2015-02-01 00:00",
         "2015-02-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxCallTraceSizeLimit(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



class TmnxCallTraceTimeLimit(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )



class TmnxCallTraceJobStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("finished", 1))
    )



class TmnxCallTraceCFlashId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cf1", 1),
          ("cf2", 2))
    )



class TmnxCallTraceApplications(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("connectivityManagement", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("radiusAuth", 4),
          ("radiusAcct", 5),
          ("python", 6),
          ("ludb", 7),
          ("msap", 8),
          ("reserved9", 9),
          ("reserved10", 10),
          ("pppEvent", 11))
    )


class TmnxCallTraceHostType(TextualConvention, Integer32):
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
        *(("ue", 1),
          ("ipoe", 2),
          ("pppoe", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxCallTraceConformance_ObjectIdentity = ObjectIdentity
tmnxCallTraceConformance = _TmnxCallTraceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102)
)
_TmnxCallTraceCompliances_ObjectIdentity = ObjectIdentity
tmnxCallTraceCompliances = _TmnxCallTraceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 1)
)
_TmnxCallTraceGroups_ObjectIdentity = ObjectIdentity
tmnxCallTraceGroups = _TmnxCallTraceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2)
)
_TmnxCallTraceInitialGroups_ObjectIdentity = ObjectIdentity
tmnxCallTraceInitialGroups = _TmnxCallTraceInitialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1)
)
_TmnxCallTraceIpoeGroups_ObjectIdentity = ObjectIdentity
tmnxCallTraceIpoeGroups = _TmnxCallTraceIpoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 2)
)
_TmnxCallTraceObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceObjs = _TmnxCallTraceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102)
)
_TmnxCallTraceScalarObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceScalarObjs = _TmnxCallTraceScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1)
)
_TmnxCallTraceLastChangedObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceLastChangedObjs = _TmnxCallTraceLastChangedObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 1)
)
_TmnxCallTraceProfileTblLstChgd_Type = TimeStamp
_TmnxCallTraceProfileTblLstChgd_Object = MibScalar
tmnxCallTraceProfileTblLstChgd = _TmnxCallTraceProfileTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 1, 1),
    _TmnxCallTraceProfileTblLstChgd_Type()
)
tmnxCallTraceProfileTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileTblLstChgd.setStatus("current")
_TmnxCallTraceLocationTblLstChgd_Type = TimeStamp
_TmnxCallTraceLocationTblLstChgd_Object = MibScalar
tmnxCallTraceLocationTblLstChgd = _TmnxCallTraceLocationTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 1, 2),
    _TmnxCallTraceLocationTblLstChgd_Type()
)
tmnxCallTraceLocationTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationTblLstChgd.setStatus("current")
_TmnxCallTraceScalarConfigObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceScalarConfigObjs = _TmnxCallTraceScalarConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 2)
)


class _TmnxCallTraceMaxFilesNumber_Type(Unsigned32):
    """Custom type tmnxCallTraceMaxFilesNumber based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxCallTraceMaxFilesNumber_Type.__name__ = "Unsigned32"
_TmnxCallTraceMaxFilesNumber_Object = MibScalar
tmnxCallTraceMaxFilesNumber = _TmnxCallTraceMaxFilesNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 2, 1),
    _TmnxCallTraceMaxFilesNumber_Type()
)
tmnxCallTraceMaxFilesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCallTraceMaxFilesNumber.setStatus("current")


class _TmnxCallTracePrimaryCFlash_Type(TmnxCallTraceCFlashId):
    """Custom type tmnxCallTracePrimaryCFlash based on TmnxCallTraceCFlashId"""
    defaultValue = 1


_TmnxCallTracePrimaryCFlash_Type.__name__ = "TmnxCallTraceCFlashId"
_TmnxCallTracePrimaryCFlash_Object = MibScalar
tmnxCallTracePrimaryCFlash = _TmnxCallTracePrimaryCFlash_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 2, 2),
    _TmnxCallTracePrimaryCFlash_Type()
)
tmnxCallTracePrimaryCFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCallTracePrimaryCFlash.setStatus("current")


class _TmnxCallTraceBuffering_Type(TruthValue):
    """Custom type tmnxCallTraceBuffering based on TruthValue"""
    defaultValue = 2


_TmnxCallTraceBuffering_Type.__name__ = "TruthValue"
_TmnxCallTraceBuffering_Object = MibScalar
tmnxCallTraceBuffering = _TmnxCallTraceBuffering_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 2, 3),
    _TmnxCallTraceBuffering_Type()
)
tmnxCallTraceBuffering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCallTraceBuffering.setStatus("current")
_TmnxCallTraceScalarStatsObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceScalarStatsObjs = _TmnxCallTraceScalarStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 3)
)


class _TmnxCallTraceUsedFilesNumber_Type(Unsigned32):
    """Custom type tmnxCallTraceUsedFilesNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TmnxCallTraceUsedFilesNumber_Type.__name__ = "Unsigned32"
_TmnxCallTraceUsedFilesNumber_Object = MibScalar
tmnxCallTraceUsedFilesNumber = _TmnxCallTraceUsedFilesNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 3, 1),
    _TmnxCallTraceUsedFilesNumber_Type()
)
tmnxCallTraceUsedFilesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceUsedFilesNumber.setStatus("current")


class _TmnxCallTraceAvailFilesNumber_Type(Unsigned32):
    """Custom type tmnxCallTraceAvailFilesNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TmnxCallTraceAvailFilesNumber_Type.__name__ = "Unsigned32"
_TmnxCallTraceAvailFilesNumber_Object = MibScalar
tmnxCallTraceAvailFilesNumber = _TmnxCallTraceAvailFilesNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 1, 3, 2),
    _TmnxCallTraceAvailFilesNumber_Type()
)
tmnxCallTraceAvailFilesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceAvailFilesNumber.setStatus("current")
_TmnxCallTraceConfigObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceConfigObjs = _TmnxCallTraceConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2)
)
_TmnxCallTraceProfileTable_Object = MibTable
tmnxCallTraceProfileTable = _TmnxCallTraceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxCallTraceProfileTable.setStatus("current")
_TmnxCallTraceProfileEntry_Object = MibTableRow
tmnxCallTraceProfileEntry = _TmnxCallTraceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1)
)
tmnxCallTraceProfileEntry.setIndexNames(
    (1, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileName"),
)
if mibBuilder.loadTexts:
    tmnxCallTraceProfileEntry.setStatus("current")
_TmnxCallTraceProfileName_Type = TNamedItem
_TmnxCallTraceProfileName_Object = MibTableColumn
tmnxCallTraceProfileName = _TmnxCallTraceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 1),
    _TmnxCallTraceProfileName_Type()
)
tmnxCallTraceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileName.setStatus("current")
_TmnxCallTraceProfileLstChgd_Type = TimeStamp
_TmnxCallTraceProfileLstChgd_Object = MibTableColumn
tmnxCallTraceProfileLstChgd = _TmnxCallTraceProfileLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 2),
    _TmnxCallTraceProfileLstChgd_Type()
)
tmnxCallTraceProfileLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileLstChgd.setStatus("current")
_TmnxCallTraceProfileRowStatus_Type = RowStatus
_TmnxCallTraceProfileRowStatus_Object = MibTableColumn
tmnxCallTraceProfileRowStatus = _TmnxCallTraceProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 3),
    _TmnxCallTraceProfileRowStatus_Type()
)
tmnxCallTraceProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileRowStatus.setStatus("current")


class _TmnxCallTraceProfileDescription_Type(TItemDescription):
    """Custom type tmnxCallTraceProfileDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxCallTraceProfileDescription_Type.__name__ = "TItemDescription"
_TmnxCallTraceProfileDescription_Object = MibTableColumn
tmnxCallTraceProfileDescription = _TmnxCallTraceProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 4),
    _TmnxCallTraceProfileDescription_Type()
)
tmnxCallTraceProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileDescription.setStatus("current")


class _TmnxCallTraceProfileSizeLimit_Type(TmnxCallTraceSizeLimit):
    """Custom type tmnxCallTraceProfileSizeLimit based on TmnxCallTraceSizeLimit"""
    defaultValue = 10


_TmnxCallTraceProfileSizeLimit_Type.__name__ = "TmnxCallTraceSizeLimit"
_TmnxCallTraceProfileSizeLimit_Object = MibTableColumn
tmnxCallTraceProfileSizeLimit = _TmnxCallTraceProfileSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 5),
    _TmnxCallTraceProfileSizeLimit_Type()
)
tmnxCallTraceProfileSizeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileSizeLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileSizeLimit.setUnits("megabytes")


class _TmnxCallTraceProfileTimeLimit_Type(TmnxCallTraceTimeLimit):
    """Custom type tmnxCallTraceProfileTimeLimit based on TmnxCallTraceTimeLimit"""
    defaultValue = 86400


_TmnxCallTraceProfileTimeLimit_Type.__name__ = "TmnxCallTraceTimeLimit"
_TmnxCallTraceProfileTimeLimit_Object = MibTableColumn
tmnxCallTraceProfileTimeLimit = _TmnxCallTraceProfileTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 6),
    _TmnxCallTraceProfileTimeLimit_Type()
)
tmnxCallTraceProfileTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileTimeLimit.setUnits("sec")


class _TmnxCallTraceProfileDstAddrType_Type(InetAddressType):
    """Custom type tmnxCallTraceProfileDstAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxCallTraceProfileDstAddrType_Type.__name__ = "InetAddressType"
_TmnxCallTraceProfileDstAddrType_Object = MibTableColumn
tmnxCallTraceProfileDstAddrType = _TmnxCallTraceProfileDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 7),
    _TmnxCallTraceProfileDstAddrType_Type()
)
tmnxCallTraceProfileDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileDstAddrType.setStatus("current")


class _TmnxCallTraceProfileDstAddr_Type(InetAddress):
    """Custom type tmnxCallTraceProfileDstAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCallTraceProfileDstAddr_Type.__name__ = "InetAddress"
_TmnxCallTraceProfileDstAddr_Object = MibTableColumn
tmnxCallTraceProfileDstAddr = _TmnxCallTraceProfileDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 8),
    _TmnxCallTraceProfileDstAddr_Type()
)
tmnxCallTraceProfileDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileDstAddr.setStatus("current")


class _TmnxCallTraceProfileDstPort_Type(InetPortNumber):
    """Custom type tmnxCallTraceProfileDstPort based on InetPortNumber"""
    defaultValue = 29770

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxCallTraceProfileDstPort_Type.__name__ = "InetPortNumber"
_TmnxCallTraceProfileDstPort_Object = MibTableColumn
tmnxCallTraceProfileDstPort = _TmnxCallTraceProfileDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 9),
    _TmnxCallTraceProfileDstPort_Type()
)
tmnxCallTraceProfileDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileDstPort.setStatus("current")


class _TmnxCallTraceProfileVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxCallTraceProfileVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxCallTraceProfileVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxCallTraceProfileVRtrId_Object = MibTableColumn
tmnxCallTraceProfileVRtrId = _TmnxCallTraceProfileVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 10),
    _TmnxCallTraceProfileVRtrId_Type()
)
tmnxCallTraceProfileVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileVRtrId.setStatus("current")
_TmnxCallTraceProfileApplications_Type = TmnxCallTraceApplications
_TmnxCallTraceProfileApplications_Object = MibTableColumn
tmnxCallTraceProfileApplications = _TmnxCallTraceProfileApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 11),
    _TmnxCallTraceProfileApplications_Type()
)
tmnxCallTraceProfileApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileApplications.setStatus("current")


class _TmnxCallTraceProfileDbgOutput_Type(TruthValue):
    """Custom type tmnxCallTraceProfileDbgOutput based on TruthValue"""
    defaultValue = 2


_TmnxCallTraceProfileDbgOutput_Type.__name__ = "TruthValue"
_TmnxCallTraceProfileDbgOutput_Object = MibTableColumn
tmnxCallTraceProfileDbgOutput = _TmnxCallTraceProfileDbgOutput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 12),
    _TmnxCallTraceProfileDbgOutput_Type()
)
tmnxCallTraceProfileDbgOutput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileDbgOutput.setStatus("current")


class _TmnxCallTraceProfileEvents_Type(Integer32):
    """Custom type tmnxCallTraceProfileEvents based on Integer32"""
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
        *(("none", 1),
          ("publicOnly", 2),
          ("all", 3))
    )


_TmnxCallTraceProfileEvents_Type.__name__ = "Integer32"
_TmnxCallTraceProfileEvents_Object = MibTableColumn
tmnxCallTraceProfileEvents = _TmnxCallTraceProfileEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 1, 1, 13),
    _TmnxCallTraceProfileEvents_Type()
)
tmnxCallTraceProfileEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCallTraceProfileEvents.setStatus("current")
_TmnxCallTraceLocationTable_Object = MibTable
tmnxCallTraceLocationTable = _TmnxCallTraceLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxCallTraceLocationTable.setStatus("current")
_TmnxCallTraceLocationEntry_Object = MibTableRow
tmnxCallTraceLocationEntry = _TmnxCallTraceLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 2, 1)
)
tmnxCallTraceLocationEntry.setIndexNames(
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationCFlashId"),
)
if mibBuilder.loadTexts:
    tmnxCallTraceLocationEntry.setStatus("current")


class _TmnxCallTraceLocationCFlashId_Type(Unsigned32):
    """Custom type tmnxCallTraceLocationCFlashId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxCallTraceLocationCFlashId_Type.__name__ = "Unsigned32"
_TmnxCallTraceLocationCFlashId_Object = MibTableColumn
tmnxCallTraceLocationCFlashId = _TmnxCallTraceLocationCFlashId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 2, 1, 1),
    _TmnxCallTraceLocationCFlashId_Type()
)
tmnxCallTraceLocationCFlashId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationCFlashId.setStatus("current")
_TmnxCallTraceLocationLstChgd_Type = TimeStamp
_TmnxCallTraceLocationLstChgd_Object = MibTableColumn
tmnxCallTraceLocationLstChgd = _TmnxCallTraceLocationLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 2, 1, 2),
    _TmnxCallTraceLocationLstChgd_Type()
)
tmnxCallTraceLocationLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationLstChgd.setStatus("current")


class _TmnxCallTraceLocationSizeLimit_Type(Unsigned32):
    """Custom type tmnxCallTraceLocationSizeLimit based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TmnxCallTraceLocationSizeLimit_Type.__name__ = "Unsigned32"
_TmnxCallTraceLocationSizeLimit_Object = MibTableColumn
tmnxCallTraceLocationSizeLimit = _TmnxCallTraceLocationSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 2, 1, 3),
    _TmnxCallTraceLocationSizeLimit_Type()
)
tmnxCallTraceLocationSizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationSizeLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationSizeLimit.setUnits("megabytes")


class _TmnxCallTraceLocationDisable_Type(TruthValue):
    """Custom type tmnxCallTraceLocationDisable based on TruthValue"""
    defaultValue = 2


_TmnxCallTraceLocationDisable_Type.__name__ = "TruthValue"
_TmnxCallTraceLocationDisable_Object = MibTableColumn
tmnxCallTraceLocationDisable = _TmnxCallTraceLocationDisable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 2, 1, 4),
    _TmnxCallTraceLocationDisable_Type()
)
tmnxCallTraceLocationDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationDisable.setStatus("current")
_TmnxCallTraceLocationStatsTable_Object = MibTable
tmnxCallTraceLocationStatsTable = _TmnxCallTraceLocationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxCallTraceLocationStatsTable.setStatus("current")
_TmnxCallTraceLocationStatsEntry_Object = MibTableRow
tmnxCallTraceLocationStatsEntry = _TmnxCallTraceLocationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxCallTraceLocationStatsEntry.setStatus("current")
_TmnxCallTraceLocationUsedSpace_Type = Unsigned32
_TmnxCallTraceLocationUsedSpace_Object = MibTableColumn
tmnxCallTraceLocationUsedSpace = _TmnxCallTraceLocationUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 3, 1, 1),
    _TmnxCallTraceLocationUsedSpace_Type()
)
tmnxCallTraceLocationUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationUsedSpace.setUnits("megabytes")
_TmnxCallTraceLocationAvailSpace_Type = Unsigned32
_TmnxCallTraceLocationAvailSpace_Object = MibTableColumn
tmnxCallTraceLocationAvailSpace = _TmnxCallTraceLocationAvailSpace_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 2, 3, 1, 2),
    _TmnxCallTraceLocationAvailSpace_Type()
)
tmnxCallTraceLocationAvailSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationAvailSpace.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceLocationAvailSpace.setUnits("megabytes")
_TmnxCallTraceStatsObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceStatsObjs = _TmnxCallTraceStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3)
)
_TmnxCallTraceJobTable_Object = MibTable
tmnxCallTraceJobTable = _TmnxCallTraceJobTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxCallTraceJobTable.setStatus("current")
_TmnxCallTraceJobEntry_Object = MibTableRow
tmnxCallTraceJobEntry = _TmnxCallTraceJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1)
)
tmnxCallTraceJobEntry.setIndexNames(
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobId"),
)
if mibBuilder.loadTexts:
    tmnxCallTraceJobEntry.setStatus("current")


class _TmnxCallTraceJobId_Type(Unsigned32):
    """Custom type tmnxCallTraceJobId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxCallTraceJobId_Type.__name__ = "Unsigned32"
_TmnxCallTraceJobId_Object = MibTableColumn
tmnxCallTraceJobId = _TmnxCallTraceJobId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 1),
    _TmnxCallTraceJobId_Type()
)
tmnxCallTraceJobId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceJobId.setStatus("current")
_TmnxCallTraceJobType_Type = TmnxCallTraceHostType
_TmnxCallTraceJobType_Object = MibTableColumn
tmnxCallTraceJobType = _TmnxCallTraceJobType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 2),
    _TmnxCallTraceJobType_Type()
)
tmnxCallTraceJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobType.setStatus("current")
_TmnxCallTraceJobWlanGwUeIeeeAddr_Type = MacAddress
_TmnxCallTraceJobWlanGwUeIeeeAddr_Object = MibTableColumn
tmnxCallTraceJobWlanGwUeIeeeAddr = _TmnxCallTraceJobWlanGwUeIeeeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 3),
    _TmnxCallTraceJobWlanGwUeIeeeAddr_Type()
)
tmnxCallTraceJobWlanGwUeIeeeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobWlanGwUeIeeeAddr.setStatus("current")
_TmnxCallTraceJobStatus_Type = TmnxCallTraceJobStatus
_TmnxCallTraceJobStatus_Object = MibTableColumn
tmnxCallTraceJobStatus = _TmnxCallTraceJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 4),
    _TmnxCallTraceJobStatus_Type()
)
tmnxCallTraceJobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobStatus.setStatus("current")
_TmnxCallTraceJobProfileName_Type = TNamedItem
_TmnxCallTraceJobProfileName_Object = MibTableColumn
tmnxCallTraceJobProfileName = _TmnxCallTraceJobProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 5),
    _TmnxCallTraceJobProfileName_Type()
)
tmnxCallTraceJobProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobProfileName.setStatus("current")
_TmnxCallTraceJobSizeLimit_Type = TmnxCallTraceSizeLimit
_TmnxCallTraceJobSizeLimit_Object = MibTableColumn
tmnxCallTraceJobSizeLimit = _TmnxCallTraceJobSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 6),
    _TmnxCallTraceJobSizeLimit_Type()
)
tmnxCallTraceJobSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobSizeLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceJobSizeLimit.setUnits("megabytes")
_TmnxCallTraceJobTimeLimit_Type = TmnxCallTraceTimeLimit
_TmnxCallTraceJobTimeLimit_Object = MibTableColumn
tmnxCallTraceJobTimeLimit = _TmnxCallTraceJobTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 7),
    _TmnxCallTraceJobTimeLimit_Type()
)
tmnxCallTraceJobTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceJobTimeLimit.setUnits("sec")


class _TmnxCallTraceJobCaptureFormat_Type(Integer32):
    """Custom type tmnxCallTraceJobCaptureFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("pcap", 1)
    )


_TmnxCallTraceJobCaptureFormat_Type.__name__ = "Integer32"
_TmnxCallTraceJobCaptureFormat_Object = MibTableColumn
tmnxCallTraceJobCaptureFormat = _TmnxCallTraceJobCaptureFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 8),
    _TmnxCallTraceJobCaptureFormat_Type()
)
tmnxCallTraceJobCaptureFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobCaptureFormat.setStatus("obsolete")
_TmnxCallTraceJobDstAddrType_Type = InetAddressType
_TmnxCallTraceJobDstAddrType_Object = MibTableColumn
tmnxCallTraceJobDstAddrType = _TmnxCallTraceJobDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 9),
    _TmnxCallTraceJobDstAddrType_Type()
)
tmnxCallTraceJobDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobDstAddrType.setStatus("current")


class _TmnxCallTraceJobDstAddr_Type(InetAddress):
    """Custom type tmnxCallTraceJobDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCallTraceJobDstAddr_Type.__name__ = "InetAddress"
_TmnxCallTraceJobDstAddr_Object = MibTableColumn
tmnxCallTraceJobDstAddr = _TmnxCallTraceJobDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 10),
    _TmnxCallTraceJobDstAddr_Type()
)
tmnxCallTraceJobDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobDstAddr.setStatus("current")
_TmnxCallTraceJobDstResAddrType_Type = InetAddressType
_TmnxCallTraceJobDstResAddrType_Object = MibTableColumn
tmnxCallTraceJobDstResAddrType = _TmnxCallTraceJobDstResAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 11),
    _TmnxCallTraceJobDstResAddrType_Type()
)
tmnxCallTraceJobDstResAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobDstResAddrType.setStatus("current")


class _TmnxCallTraceJobDstResAddr_Type(InetAddress):
    """Custom type tmnxCallTraceJobDstResAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCallTraceJobDstResAddr_Type.__name__ = "InetAddress"
_TmnxCallTraceJobDstResAddr_Object = MibTableColumn
tmnxCallTraceJobDstResAddr = _TmnxCallTraceJobDstResAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 12),
    _TmnxCallTraceJobDstResAddr_Type()
)
tmnxCallTraceJobDstResAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobDstResAddr.setStatus("current")


class _TmnxCallTraceJobDstPort_Type(InetPortNumber):
    """Custom type tmnxCallTraceJobDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxCallTraceJobDstPort_Type.__name__ = "InetPortNumber"
_TmnxCallTraceJobDstPort_Object = MibTableColumn
tmnxCallTraceJobDstPort = _TmnxCallTraceJobDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 13),
    _TmnxCallTraceJobDstPort_Type()
)
tmnxCallTraceJobDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobDstPort.setStatus("current")
_TmnxCallTraceJobVRtrId_Type = TmnxVRtrID
_TmnxCallTraceJobVRtrId_Object = MibTableColumn
tmnxCallTraceJobVRtrId = _TmnxCallTraceJobVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 14),
    _TmnxCallTraceJobVRtrId_Type()
)
tmnxCallTraceJobVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobVRtrId.setStatus("current")
_TmnxCallTraceJobStartTime_Type = DateAndTime
_TmnxCallTraceJobStartTime_Object = MibTableColumn
tmnxCallTraceJobStartTime = _TmnxCallTraceJobStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 15),
    _TmnxCallTraceJobStartTime_Type()
)
tmnxCallTraceJobStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobStartTime.setStatus("current")
_TmnxCallTraceJobCaptMsgsCnt_Type = Unsigned32
_TmnxCallTraceJobCaptMsgsCnt_Object = MibTableColumn
tmnxCallTraceJobCaptMsgsCnt = _TmnxCallTraceJobCaptMsgsCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 16),
    _TmnxCallTraceJobCaptMsgsCnt_Type()
)
tmnxCallTraceJobCaptMsgsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobCaptMsgsCnt.setStatus("current")
_TmnxCallTraceJobCaptMsgsSize_Type = Unsigned32
_TmnxCallTraceJobCaptMsgsSize_Object = MibTableColumn
tmnxCallTraceJobCaptMsgsSize = _TmnxCallTraceJobCaptMsgsSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 17),
    _TmnxCallTraceJobCaptMsgsSize_Type()
)
tmnxCallTraceJobCaptMsgsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobCaptMsgsSize.setStatus("current")
_TmnxCallTraceJobSapPortId_Type = TmnxPortID
_TmnxCallTraceJobSapPortId_Object = MibTableColumn
tmnxCallTraceJobSapPortId = _TmnxCallTraceJobSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 18),
    _TmnxCallTraceJobSapPortId_Type()
)
tmnxCallTraceJobSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobSapPortId.setStatus("current")
_TmnxCallTraceJobSapEncapVal_Type = TmnxEncapVal
_TmnxCallTraceJobSapEncapVal_Object = MibTableColumn
tmnxCallTraceJobSapEncapVal = _TmnxCallTraceJobSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 19),
    _TmnxCallTraceJobSapEncapVal_Type()
)
tmnxCallTraceJobSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobSapEncapVal.setStatus("current")
_TmnxCallTraceJobIpoeIeeeAddr_Type = MacAddress
_TmnxCallTraceJobIpoeIeeeAddr_Object = MibTableColumn
tmnxCallTraceJobIpoeIeeeAddr = _TmnxCallTraceJobIpoeIeeeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 20),
    _TmnxCallTraceJobIpoeIeeeAddr_Type()
)
tmnxCallTraceJobIpoeIeeeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobIpoeIeeeAddr.setStatus("current")


class _TmnxCallTraceJobCircuitId_Type(OctetString):
    """Custom type tmnxCallTraceJobCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCallTraceJobCircuitId_Type.__name__ = "OctetString"
_TmnxCallTraceJobCircuitId_Object = MibTableColumn
tmnxCallTraceJobCircuitId = _TmnxCallTraceJobCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 21),
    _TmnxCallTraceJobCircuitId_Type()
)
tmnxCallTraceJobCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobCircuitId.setStatus("current")


class _TmnxCallTraceJobRemoteId_Type(OctetString):
    """Custom type tmnxCallTraceJobRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCallTraceJobRemoteId_Type.__name__ = "OctetString"
_TmnxCallTraceJobRemoteId_Object = MibTableColumn
tmnxCallTraceJobRemoteId = _TmnxCallTraceJobRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 22),
    _TmnxCallTraceJobRemoteId_Type()
)
tmnxCallTraceJobRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobRemoteId.setStatus("current")
_TmnxCallTraceJobTraceName_Type = TNamedItemOrEmpty
_TmnxCallTraceJobTraceName_Object = MibTableColumn
tmnxCallTraceJobTraceName = _TmnxCallTraceJobTraceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 23),
    _TmnxCallTraceJobTraceName_Type()
)
tmnxCallTraceJobTraceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobTraceName.setStatus("current")


class _TmnxCallTraceJobDstType_Type(Integer32):
    """Custom type tmnxCallTraceJobDstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cflash", 1),
          ("live-output", 2),
          ("debug-output", 3))
    )


_TmnxCallTraceJobDstType_Type.__name__ = "Integer32"
_TmnxCallTraceJobDstType_Object = MibTableColumn
tmnxCallTraceJobDstType = _TmnxCallTraceJobDstType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 24),
    _TmnxCallTraceJobDstType_Type()
)
tmnxCallTraceJobDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobDstType.setStatus("current")


class _TmnxCallTraceJobUserName_Type(OctetString):
    """Custom type tmnxCallTraceJobUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_TmnxCallTraceJobUserName_Type.__name__ = "OctetString"
_TmnxCallTraceJobUserName_Object = MibTableColumn
tmnxCallTraceJobUserName = _TmnxCallTraceJobUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 1, 1, 25),
    _TmnxCallTraceJobUserName_Type()
)
tmnxCallTraceJobUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceJobUserName.setStatus("current")
_TmnxCallTraceFileTable_Object = MibTable
tmnxCallTraceFileTable = _TmnxCallTraceFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxCallTraceFileTable.setStatus("current")
_TmnxCallTraceFileEntry_Object = MibTableRow
tmnxCallTraceFileEntry = _TmnxCallTraceFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1)
)
tmnxCallTraceFileEntry.setIndexNames(
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileJobStatus"),
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileCpmSlotNum"),
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileCFlashId"),
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileName"),
)
if mibBuilder.loadTexts:
    tmnxCallTraceFileEntry.setStatus("current")
_TmnxCallTraceFileJobStatus_Type = TmnxCallTraceJobStatus
_TmnxCallTraceFileJobStatus_Object = MibTableColumn
tmnxCallTraceFileJobStatus = _TmnxCallTraceFileJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 1),
    _TmnxCallTraceFileJobStatus_Type()
)
tmnxCallTraceFileJobStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceFileJobStatus.setStatus("current")
_TmnxCallTraceFileCpmSlotNum_Type = TmnxSlotNum
_TmnxCallTraceFileCpmSlotNum_Object = MibTableColumn
tmnxCallTraceFileCpmSlotNum = _TmnxCallTraceFileCpmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 2),
    _TmnxCallTraceFileCpmSlotNum_Type()
)
tmnxCallTraceFileCpmSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceFileCpmSlotNum.setStatus("current")
_TmnxCallTraceFileCFlashId_Type = TmnxCallTraceCFlashId
_TmnxCallTraceFileCFlashId_Object = MibTableColumn
tmnxCallTraceFileCFlashId = _TmnxCallTraceFileCFlashId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 3),
    _TmnxCallTraceFileCFlashId_Type()
)
tmnxCallTraceFileCFlashId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceFileCFlashId.setStatus("current")


class _TmnxCallTraceFileName_Type(DisplayString):
    """Custom type tmnxCallTraceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(38, 83),
    )


_TmnxCallTraceFileName_Type.__name__ = "DisplayString"
_TmnxCallTraceFileName_Object = MibTableColumn
tmnxCallTraceFileName = _TmnxCallTraceFileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 4),
    _TmnxCallTraceFileName_Type()
)
tmnxCallTraceFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceFileName.setStatus("current")


class _TmnxCallTraceFileDir_Type(DisplayString):
    """Custom type tmnxCallTraceFileDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 19),
    )


_TmnxCallTraceFileDir_Type.__name__ = "DisplayString"
_TmnxCallTraceFileDir_Object = MibTableColumn
tmnxCallTraceFileDir = _TmnxCallTraceFileDir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 5),
    _TmnxCallTraceFileDir_Type()
)
tmnxCallTraceFileDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceFileDir.setStatus("current")
_TmnxCallTraceFileSize_Type = Unsigned32
_TmnxCallTraceFileSize_Object = MibTableColumn
tmnxCallTraceFileSize = _TmnxCallTraceFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 6),
    _TmnxCallTraceFileSize_Type()
)
tmnxCallTraceFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceFileSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCallTraceFileSize.setUnits("bytes")
_TmnxCallTraceFileLastDataModif_Type = DateAndTime
_TmnxCallTraceFileLastDataModif_Object = MibTableColumn
tmnxCallTraceFileLastDataModif = _TmnxCallTraceFileLastDataModif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 2, 1, 7),
    _TmnxCallTraceFileLastDataModif_Type()
)
tmnxCallTraceFileLastDataModif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceFileLastDataModif.setStatus("current")
_TmnxCallTraceTraceTable_Object = MibTable
tmnxCallTraceTraceTable = _TmnxCallTraceTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxCallTraceTraceTable.setStatus("current")
_TmnxCallTraceTraceEntry_Object = MibTableRow
tmnxCallTraceTraceEntry = _TmnxCallTraceTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1)
)
tmnxCallTraceTraceEntry.setIndexNames(
    (0, "TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceId"),
)
if mibBuilder.loadTexts:
    tmnxCallTraceTraceEntry.setStatus("current")


class _TmnxCallTraceTraceId_Type(Unsigned32):
    """Custom type tmnxCallTraceTraceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxCallTraceTraceId_Type.__name__ = "Unsigned32"
_TmnxCallTraceTraceId_Object = MibTableColumn
tmnxCallTraceTraceId = _TmnxCallTraceTraceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 1),
    _TmnxCallTraceTraceId_Type()
)
tmnxCallTraceTraceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceId.setStatus("current")
_TmnxCallTraceTraceType_Type = TmnxCallTraceHostType
_TmnxCallTraceTraceType_Object = MibTableColumn
tmnxCallTraceTraceType = _TmnxCallTraceTraceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 2),
    _TmnxCallTraceTraceType_Type()
)
tmnxCallTraceTraceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceType.setStatus("current")


class _TmnxCallTraceTraceSapId_Type(DisplayString):
    """Custom type tmnxCallTraceTraceSapId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_TmnxCallTraceTraceSapId_Type.__name__ = "DisplayString"
_TmnxCallTraceTraceSapId_Object = MibTableColumn
tmnxCallTraceTraceSapId = _TmnxCallTraceTraceSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 3),
    _TmnxCallTraceTraceSapId_Type()
)
tmnxCallTraceTraceSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceSapId.setStatus("current")


class _TmnxCallTraceTraceIeeeAddr_Type(DisplayString):
    """Custom type tmnxCallTraceTraceIeeeAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_TmnxCallTraceTraceIeeeAddr_Type.__name__ = "DisplayString"
_TmnxCallTraceTraceIeeeAddr_Object = MibTableColumn
tmnxCallTraceTraceIeeeAddr = _TmnxCallTraceTraceIeeeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 4),
    _TmnxCallTraceTraceIeeeAddr_Type()
)
tmnxCallTraceTraceIeeeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceIeeeAddr.setStatus("current")


class _TmnxCallTraceTraceCircuitId_Type(DisplayString):
    """Custom type tmnxCallTraceTraceCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCallTraceTraceCircuitId_Type.__name__ = "DisplayString"
_TmnxCallTraceTraceCircuitId_Object = MibTableColumn
tmnxCallTraceTraceCircuitId = _TmnxCallTraceTraceCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 5),
    _TmnxCallTraceTraceCircuitId_Type()
)
tmnxCallTraceTraceCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceCircuitId.setStatus("current")


class _TmnxCallTraceTraceRemoteId_Type(DisplayString):
    """Custom type tmnxCallTraceTraceRemoteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCallTraceTraceRemoteId_Type.__name__ = "DisplayString"
_TmnxCallTraceTraceRemoteId_Object = MibTableColumn
tmnxCallTraceTraceRemoteId = _TmnxCallTraceTraceRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 6),
    _TmnxCallTraceTraceRemoteId_Type()
)
tmnxCallTraceTraceRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceRemoteId.setStatus("current")
_TmnxCallTraceTraceName_Type = TNamedItem
_TmnxCallTraceTraceName_Object = MibTableColumn
tmnxCallTraceTraceName = _TmnxCallTraceTraceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 7),
    _TmnxCallTraceTraceName_Type()
)
tmnxCallTraceTraceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceName.setStatus("current")


class _TmnxCallTraceTraceMaxJobs_Type(Unsigned32):
    """Custom type tmnxCallTraceTraceMaxJobs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxCallTraceTraceMaxJobs_Type.__name__ = "Unsigned32"
_TmnxCallTraceTraceMaxJobs_Object = MibTableColumn
tmnxCallTraceTraceMaxJobs = _TmnxCallTraceTraceMaxJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 3, 3, 1, 8),
    _TmnxCallTraceTraceMaxJobs_Type()
)
tmnxCallTraceTraceMaxJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCallTraceTraceMaxJobs.setStatus("current")
_TmnxCallTraceNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxCallTraceNotificationObjs = _TmnxCallTraceNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 102, 20)
)
_TmnxCallTraceNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxCallTraceNotifyPrefix = _TmnxCallTraceNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 102)
)
_TmnxCallTraceNotifications_ObjectIdentity = ObjectIdentity
tmnxCallTraceNotifications = _TmnxCallTraceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 102, 0)
)
tmnxCallTraceLocationEntry.registerAugmentions(
    ("TIMETRA-CALLTRACE-MIB",
     "tmnxCallTraceLocationStatsEntry")
)
tmnxCallTraceLocationStatsEntry.setIndexNames(*tmnxCallTraceLocationEntry.getIndexNames())

# Managed Objects groups

tmnxCallTraceProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 1)
)
tmnxCallTraceProfileGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileTblLstChgd"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileLstChgd"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileRowStatus"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileDescription"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileSizeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileTimeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileDstAddrType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileDstAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileDstPort"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileVRtrId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileApplications"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileDbgOutput"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileEvents"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceProfileGroup.setStatus("current")

tmnxCallTraceLocStoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 2)
)
tmnxCallTraceLocStoreGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationTblLstChgd"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationLstChgd"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationSizeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationDisable"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationUsedSpace"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationAvailSpace"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceLocStoreGroup.setStatus("current")

tmnxCallTraceScalarCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 3)
)
tmnxCallTraceScalarCfgGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceMaxFilesNumber"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTracePrimaryCFlash"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceScalarCfgGroup.setStatus("current")

tmnxCallTraceJobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 4)
)
tmnxCallTraceJobGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobWlanGwUeIeeeAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobStatus"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobProfileName"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobSizeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobTimeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCaptureFormat"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstAddrType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstResAddrType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstResAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstPort"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobVRtrId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobStartTime"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCaptMsgsCnt"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCaptMsgsSize"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceJobGroup.setStatus("obsolete")

tmnxCallTraceFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 6)
)
tmnxCallTraceFileGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileDir"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileSize"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileLastDataModif"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceFileGroup.setStatus("current")

tmnxCallTraceScalarStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 7)
)
tmnxCallTraceScalarStatsGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceUsedFilesNumber"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceAvailFilesNumber"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceScalarStatsGroup.setStatus("current")

tmnxCallTraceJob15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 8)
)
tmnxCallTraceJob15v0Group.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobWlanGwUeIeeeAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobStatus"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobProfileName"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobSizeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobTimeLimit"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstAddrType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstResAddrType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstResAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstPort"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobVRtrId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobStartTime"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCaptMsgsCnt"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCaptMsgsSize"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobDstType"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceJob15v0Group.setStatus("current")

tmnxCallTraceJobObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 9)
)
tmnxCallTraceJobObsoletedGroup.setObjects(
    ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCaptureFormat")
)
if mibBuilder.loadTexts:
    tmnxCallTraceJobObsoletedGroup.setStatus("current")

tmnxCallTraceScalarCfg20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 10)
)
tmnxCallTraceScalarCfg20v0Group.setObjects(
    ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceBuffering")
)
if mibBuilder.loadTexts:
    tmnxCallTraceScalarCfg20v0Group.setStatus("current")

tmnxCallTraceJob20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 11)
)
tmnxCallTraceJob20v0Group.setObjects(
    ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobUserName")
)
if mibBuilder.loadTexts:
    tmnxCallTraceJob20v0Group.setStatus("current")

tmnxCallTraceIpoeJobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 2, 1)
)
tmnxCallTraceIpoeJobGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobSapPortId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobSapEncapVal"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobIpoeIeeeAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobCircuitId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobRemoteId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobTraceName"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceSapId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceIeeeAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceCircuitId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceRemoteId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceName"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceMaxJobs"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceIpoeJobGroup.setStatus("current")

tmnxCallTraceIpoeTraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 2, 2)
)
tmnxCallTraceIpoeTraceGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceType"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceSapId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceIeeeAddr"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceCircuitId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceRemoteId"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceName"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceTraceMaxJobs"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceIpoeTraceGroup.setStatus("current")


# Notification objects

tmnxCallTraceMaxFilesNumReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 102, 0, 1)
)
tmnxCallTraceMaxFilesNumReached.setObjects(
    ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceMaxFilesNumber")
)
if mibBuilder.loadTexts:
    tmnxCallTraceMaxFilesNumReached.setStatus(
        "current"
    )

tmnxCallTraceLocSizeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 102, 0, 2)
)
tmnxCallTraceLocSizeLimitReached.setObjects(
    ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocationSizeLimit")
)
if mibBuilder.loadTexts:
    tmnxCallTraceLocSizeLimitReached.setStatus(
        "current"
    )


# Notifications groups

tmnxCallTraceNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 2, 1, 5)
)
tmnxCallTraceNotifyGroup.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceMaxFilesNumReached"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocSizeLimitReached"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxCallTraceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 1, 1)
)
tmnxCallTraceCompliance.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocStoreGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarCfgGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJobGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceNotifyGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarStatsGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceIpoeJobGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceIpoeTraceGroup"))
)
if mibBuilder.loadTexts:
    tmnxCallTraceCompliance.setStatus(
        "obsolete"
    )

tmnxCallTrace15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 1, 2)
)
tmnxCallTrace15v0Compliance.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocStoreGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarCfgGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJob15v0Group"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceNotifyGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarStatsGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceIpoeJobGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceIpoeTraceGroup"))
)
if mibBuilder.loadTexts:
    tmnxCallTrace15v0Compliance.setStatus(
        "obsolete"
    )

tmnxCallTrace20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 102, 1, 3)
)
tmnxCallTrace20v0Compliance.setObjects(
      *(("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceProfileGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceLocStoreGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarCfgGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJob15v0Group"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceNotifyGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceFileGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarStatsGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceIpoeJobGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceIpoeTraceGroup"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceScalarCfg20v0Group"),
        ("TIMETRA-CALLTRACE-MIB", "tmnxCallTraceJob20v0Group"))
)
if mibBuilder.loadTexts:
    tmnxCallTrace20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CALLTRACE-MIB",
    **{"TmnxCallTraceSizeLimit": TmnxCallTraceSizeLimit,
       "TmnxCallTraceTimeLimit": TmnxCallTraceTimeLimit,
       "TmnxCallTraceJobStatus": TmnxCallTraceJobStatus,
       "TmnxCallTraceCFlashId": TmnxCallTraceCFlashId,
       "TmnxCallTraceApplications": TmnxCallTraceApplications,
       "TmnxCallTraceHostType": TmnxCallTraceHostType,
       "timetraCallTraceMIBModule": timetraCallTraceMIBModule,
       "tmnxCallTraceConformance": tmnxCallTraceConformance,
       "tmnxCallTraceCompliances": tmnxCallTraceCompliances,
       "tmnxCallTraceCompliance": tmnxCallTraceCompliance,
       "tmnxCallTrace15v0Compliance": tmnxCallTrace15v0Compliance,
       "tmnxCallTrace20v0Compliance": tmnxCallTrace20v0Compliance,
       "tmnxCallTraceGroups": tmnxCallTraceGroups,
       "tmnxCallTraceInitialGroups": tmnxCallTraceInitialGroups,
       "tmnxCallTraceProfileGroup": tmnxCallTraceProfileGroup,
       "tmnxCallTraceLocStoreGroup": tmnxCallTraceLocStoreGroup,
       "tmnxCallTraceScalarCfgGroup": tmnxCallTraceScalarCfgGroup,
       "tmnxCallTraceJobGroup": tmnxCallTraceJobGroup,
       "tmnxCallTraceNotifyGroup": tmnxCallTraceNotifyGroup,
       "tmnxCallTraceFileGroup": tmnxCallTraceFileGroup,
       "tmnxCallTraceScalarStatsGroup": tmnxCallTraceScalarStatsGroup,
       "tmnxCallTraceJob15v0Group": tmnxCallTraceJob15v0Group,
       "tmnxCallTraceJobObsoletedGroup": tmnxCallTraceJobObsoletedGroup,
       "tmnxCallTraceScalarCfg20v0Group": tmnxCallTraceScalarCfg20v0Group,
       "tmnxCallTraceJob20v0Group": tmnxCallTraceJob20v0Group,
       "tmnxCallTraceIpoeGroups": tmnxCallTraceIpoeGroups,
       "tmnxCallTraceIpoeJobGroup": tmnxCallTraceIpoeJobGroup,
       "tmnxCallTraceIpoeTraceGroup": tmnxCallTraceIpoeTraceGroup,
       "tmnxCallTraceObjs": tmnxCallTraceObjs,
       "tmnxCallTraceScalarObjs": tmnxCallTraceScalarObjs,
       "tmnxCallTraceLastChangedObjs": tmnxCallTraceLastChangedObjs,
       "tmnxCallTraceProfileTblLstChgd": tmnxCallTraceProfileTblLstChgd,
       "tmnxCallTraceLocationTblLstChgd": tmnxCallTraceLocationTblLstChgd,
       "tmnxCallTraceScalarConfigObjs": tmnxCallTraceScalarConfigObjs,
       "tmnxCallTraceMaxFilesNumber": tmnxCallTraceMaxFilesNumber,
       "tmnxCallTracePrimaryCFlash": tmnxCallTracePrimaryCFlash,
       "tmnxCallTraceBuffering": tmnxCallTraceBuffering,
       "tmnxCallTraceScalarStatsObjs": tmnxCallTraceScalarStatsObjs,
       "tmnxCallTraceUsedFilesNumber": tmnxCallTraceUsedFilesNumber,
       "tmnxCallTraceAvailFilesNumber": tmnxCallTraceAvailFilesNumber,
       "tmnxCallTraceConfigObjs": tmnxCallTraceConfigObjs,
       "tmnxCallTraceProfileTable": tmnxCallTraceProfileTable,
       "tmnxCallTraceProfileEntry": tmnxCallTraceProfileEntry,
       "tmnxCallTraceProfileName": tmnxCallTraceProfileName,
       "tmnxCallTraceProfileLstChgd": tmnxCallTraceProfileLstChgd,
       "tmnxCallTraceProfileRowStatus": tmnxCallTraceProfileRowStatus,
       "tmnxCallTraceProfileDescription": tmnxCallTraceProfileDescription,
       "tmnxCallTraceProfileSizeLimit": tmnxCallTraceProfileSizeLimit,
       "tmnxCallTraceProfileTimeLimit": tmnxCallTraceProfileTimeLimit,
       "tmnxCallTraceProfileDstAddrType": tmnxCallTraceProfileDstAddrType,
       "tmnxCallTraceProfileDstAddr": tmnxCallTraceProfileDstAddr,
       "tmnxCallTraceProfileDstPort": tmnxCallTraceProfileDstPort,
       "tmnxCallTraceProfileVRtrId": tmnxCallTraceProfileVRtrId,
       "tmnxCallTraceProfileApplications": tmnxCallTraceProfileApplications,
       "tmnxCallTraceProfileDbgOutput": tmnxCallTraceProfileDbgOutput,
       "tmnxCallTraceProfileEvents": tmnxCallTraceProfileEvents,
       "tmnxCallTraceLocationTable": tmnxCallTraceLocationTable,
       "tmnxCallTraceLocationEntry": tmnxCallTraceLocationEntry,
       "tmnxCallTraceLocationCFlashId": tmnxCallTraceLocationCFlashId,
       "tmnxCallTraceLocationLstChgd": tmnxCallTraceLocationLstChgd,
       "tmnxCallTraceLocationSizeLimit": tmnxCallTraceLocationSizeLimit,
       "tmnxCallTraceLocationDisable": tmnxCallTraceLocationDisable,
       "tmnxCallTraceLocationStatsTable": tmnxCallTraceLocationStatsTable,
       "tmnxCallTraceLocationStatsEntry": tmnxCallTraceLocationStatsEntry,
       "tmnxCallTraceLocationUsedSpace": tmnxCallTraceLocationUsedSpace,
       "tmnxCallTraceLocationAvailSpace": tmnxCallTraceLocationAvailSpace,
       "tmnxCallTraceStatsObjs": tmnxCallTraceStatsObjs,
       "tmnxCallTraceJobTable": tmnxCallTraceJobTable,
       "tmnxCallTraceJobEntry": tmnxCallTraceJobEntry,
       "tmnxCallTraceJobId": tmnxCallTraceJobId,
       "tmnxCallTraceJobType": tmnxCallTraceJobType,
       "tmnxCallTraceJobWlanGwUeIeeeAddr": tmnxCallTraceJobWlanGwUeIeeeAddr,
       "tmnxCallTraceJobStatus": tmnxCallTraceJobStatus,
       "tmnxCallTraceJobProfileName": tmnxCallTraceJobProfileName,
       "tmnxCallTraceJobSizeLimit": tmnxCallTraceJobSizeLimit,
       "tmnxCallTraceJobTimeLimit": tmnxCallTraceJobTimeLimit,
       "tmnxCallTraceJobCaptureFormat": tmnxCallTraceJobCaptureFormat,
       "tmnxCallTraceJobDstAddrType": tmnxCallTraceJobDstAddrType,
       "tmnxCallTraceJobDstAddr": tmnxCallTraceJobDstAddr,
       "tmnxCallTraceJobDstResAddrType": tmnxCallTraceJobDstResAddrType,
       "tmnxCallTraceJobDstResAddr": tmnxCallTraceJobDstResAddr,
       "tmnxCallTraceJobDstPort": tmnxCallTraceJobDstPort,
       "tmnxCallTraceJobVRtrId": tmnxCallTraceJobVRtrId,
       "tmnxCallTraceJobStartTime": tmnxCallTraceJobStartTime,
       "tmnxCallTraceJobCaptMsgsCnt": tmnxCallTraceJobCaptMsgsCnt,
       "tmnxCallTraceJobCaptMsgsSize": tmnxCallTraceJobCaptMsgsSize,
       "tmnxCallTraceJobSapPortId": tmnxCallTraceJobSapPortId,
       "tmnxCallTraceJobSapEncapVal": tmnxCallTraceJobSapEncapVal,
       "tmnxCallTraceJobIpoeIeeeAddr": tmnxCallTraceJobIpoeIeeeAddr,
       "tmnxCallTraceJobCircuitId": tmnxCallTraceJobCircuitId,
       "tmnxCallTraceJobRemoteId": tmnxCallTraceJobRemoteId,
       "tmnxCallTraceJobTraceName": tmnxCallTraceJobTraceName,
       "tmnxCallTraceJobDstType": tmnxCallTraceJobDstType,
       "tmnxCallTraceJobUserName": tmnxCallTraceJobUserName,
       "tmnxCallTraceFileTable": tmnxCallTraceFileTable,
       "tmnxCallTraceFileEntry": tmnxCallTraceFileEntry,
       "tmnxCallTraceFileJobStatus": tmnxCallTraceFileJobStatus,
       "tmnxCallTraceFileCpmSlotNum": tmnxCallTraceFileCpmSlotNum,
       "tmnxCallTraceFileCFlashId": tmnxCallTraceFileCFlashId,
       "tmnxCallTraceFileName": tmnxCallTraceFileName,
       "tmnxCallTraceFileDir": tmnxCallTraceFileDir,
       "tmnxCallTraceFileSize": tmnxCallTraceFileSize,
       "tmnxCallTraceFileLastDataModif": tmnxCallTraceFileLastDataModif,
       "tmnxCallTraceTraceTable": tmnxCallTraceTraceTable,
       "tmnxCallTraceTraceEntry": tmnxCallTraceTraceEntry,
       "tmnxCallTraceTraceId": tmnxCallTraceTraceId,
       "tmnxCallTraceTraceType": tmnxCallTraceTraceType,
       "tmnxCallTraceTraceSapId": tmnxCallTraceTraceSapId,
       "tmnxCallTraceTraceIeeeAddr": tmnxCallTraceTraceIeeeAddr,
       "tmnxCallTraceTraceCircuitId": tmnxCallTraceTraceCircuitId,
       "tmnxCallTraceTraceRemoteId": tmnxCallTraceTraceRemoteId,
       "tmnxCallTraceTraceName": tmnxCallTraceTraceName,
       "tmnxCallTraceTraceMaxJobs": tmnxCallTraceTraceMaxJobs,
       "tmnxCallTraceNotificationObjs": tmnxCallTraceNotificationObjs,
       "tmnxCallTraceNotifyPrefix": tmnxCallTraceNotifyPrefix,
       "tmnxCallTraceNotifications": tmnxCallTraceNotifications,
       "tmnxCallTraceMaxFilesNumReached": tmnxCallTraceMaxFilesNumReached,
       "tmnxCallTraceLocSizeLimitReached": tmnxCallTraceLocSizeLimitReached}
)
