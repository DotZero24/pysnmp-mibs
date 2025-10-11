# SNMP MIB module (SWITCH-CCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-CCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:58 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,
 ObjName,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "ObjName",
    "PortList")


# MODULE-IDENTITY

rcCcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55)
)
if mibBuilder.loadTexts:
    rcCcp.setRevisions(
        ("2010-11-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcCpuCachePacket_ObjectIdentity = ObjectIdentity
rcCpuCachePacket = _RcCpuCachePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1)
)
_RcCpuCachePacketEnable_Type = EnableVar
_RcCpuCachePacketEnable_Object = MibScalar
rcCpuCachePacketEnable = _RcCpuCachePacketEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 1),
    _RcCpuCachePacketEnable_Type()
)
rcCpuCachePacketEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketEnable.setStatus("current")
_RcCpuCachePacketPortList_Type = PortList
_RcCpuCachePacketPortList_Object = MibScalar
rcCpuCachePacketPortList = _RcCpuCachePacketPortList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 2),
    _RcCpuCachePacketPortList_Type()
)
rcCpuCachePacketPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketPortList.setStatus("current")


class _RcCpuCachePacketLen_Type(Integer32):
    """Custom type rcCpuCachePacketLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("header", 1),
          ("all", 2))
    )


_RcCpuCachePacketLen_Type.__name__ = "Integer32"
_RcCpuCachePacketLen_Object = MibScalar
rcCpuCachePacketLen = _RcCpuCachePacketLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 3),
    _RcCpuCachePacketLen_Type()
)
rcCpuCachePacketLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketLen.setStatus("current")
_RcCpuCachePacketBufferSize_Type = Integer32
_RcCpuCachePacketBufferSize_Object = MibScalar
rcCpuCachePacketBufferSize = _RcCpuCachePacketBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 4),
    _RcCpuCachePacketBufferSize_Type()
)
rcCpuCachePacketBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketBufferSize.setStatus("current")
_RcCpuCachePacketManualUpload_Type = EnableVar
_RcCpuCachePacketManualUpload_Object = MibScalar
rcCpuCachePacketManualUpload = _RcCpuCachePacketManualUpload_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 5),
    _RcCpuCachePacketManualUpload_Type()
)
rcCpuCachePacketManualUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketManualUpload.setStatus("current")
_RcCpuCachePacketAutoUpload_Type = EnableVar
_RcCpuCachePacketAutoUpload_Object = MibScalar
rcCpuCachePacketAutoUpload = _RcCpuCachePacketAutoUpload_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 6),
    _RcCpuCachePacketAutoUpload_Type()
)
rcCpuCachePacketAutoUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketAutoUpload.setStatus("current")
_RcCpuCachePacketOverride_Type = EnableVar
_RcCpuCachePacketOverride_Object = MibScalar
rcCpuCachePacketOverride = _RcCpuCachePacketOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 7),
    _RcCpuCachePacketOverride_Type()
)
rcCpuCachePacketOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketOverride.setStatus("current")


class _RcCpuCachePacketAutoUploadTimes_Type(Integer32):
    """Custom type rcCpuCachePacketAutoUploadTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCpuCachePacketAutoUploadTimes_Type.__name__ = "Integer32"
_RcCpuCachePacketAutoUploadTimes_Object = MibScalar
rcCpuCachePacketAutoUploadTimes = _RcCpuCachePacketAutoUploadTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 8),
    _RcCpuCachePacketAutoUploadTimes_Type()
)
rcCpuCachePacketAutoUploadTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketAutoUploadTimes.setStatus("current")
_RcCpuCachePacketClear_Type = EnableVar
_RcCpuCachePacketClear_Object = MibScalar
rcCpuCachePacketClear = _RcCpuCachePacketClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 9),
    _RcCpuCachePacketClear_Type()
)
rcCpuCachePacketClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketClear.setStatus("current")
_RcCpuCachePacketsAutoUploadCounter_Type = Integer32
_RcCpuCachePacketsAutoUploadCounter_Object = MibScalar
rcCpuCachePacketsAutoUploadCounter = _RcCpuCachePacketsAutoUploadCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 10),
    _RcCpuCachePacketsAutoUploadCounter_Type()
)
rcCpuCachePacketsAutoUploadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuCachePacketsAutoUploadCounter.setStatus("current")
_RcCpuCachePacketMirrorToCpuStatus_Type = EnableVar
_RcCpuCachePacketMirrorToCpuStatus_Object = MibScalar
rcCpuCachePacketMirrorToCpuStatus = _RcCpuCachePacketMirrorToCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 11),
    _RcCpuCachePacketMirrorToCpuStatus_Type()
)
rcCpuCachePacketMirrorToCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuCachePacketMirrorToCpuStatus.setStatus("current")


class _RcCpuCachePacketBufferStatus_Type(Integer32):
    """Custom type rcCpuCachePacketBufferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-malloc", 1),
          ("not-full", 2),
          ("full", 3))
    )


_RcCpuCachePacketBufferStatus_Type.__name__ = "Integer32"
_RcCpuCachePacketBufferStatus_Object = MibScalar
rcCpuCachePacketBufferStatus = _RcCpuCachePacketBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 12),
    _RcCpuCachePacketBufferStatus_Type()
)
rcCpuCachePacketBufferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuCachePacketBufferStatus.setStatus("current")


class _RcCpuCachePacketStatus_Type(Integer32):
    """Custom type rcCpuCachePacketStatus based on Integer32"""
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
          ("uploading", 2),
          ("collecting", 3))
    )


_RcCpuCachePacketStatus_Type.__name__ = "Integer32"
_RcCpuCachePacketStatus_Object = MibScalar
rcCpuCachePacketStatus = _RcCpuCachePacketStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 13),
    _RcCpuCachePacketStatus_Type()
)
rcCpuCachePacketStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuCachePacketStatus.setStatus("current")
_RcCpuCachePacketCount_Type = Integer32
_RcCpuCachePacketCount_Object = MibScalar
rcCpuCachePacketCount = _RcCpuCachePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 14),
    _RcCpuCachePacketCount_Type()
)
rcCpuCachePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuCachePacketCount.setStatus("current")
_RcCpuCachePacketUploadedNumber_Type = Integer32
_RcCpuCachePacketUploadedNumber_Object = MibScalar
rcCpuCachePacketUploadedNumber = _RcCpuCachePacketUploadedNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 15),
    _RcCpuCachePacketUploadedNumber_Type()
)
rcCpuCachePacketUploadedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadedNumber.setStatus("current")
_RcCpuCachePacketAclTable_Object = MibTable
rcCpuCachePacketAclTable = _RcCpuCachePacketAclTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 16)
)
if mibBuilder.loadTexts:
    rcCpuCachePacketAclTable.setStatus("current")
_RcCpuCachePacketAclEntry_Object = MibTableRow
rcCpuCachePacketAclEntry = _RcCpuCachePacketAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 16, 1)
)
rcCpuCachePacketAclEntry.setIndexNames(
    (0, "SWITCH-CCP-MIB", "rcCpuCachePacketPortIndex"),
)
if mibBuilder.loadTexts:
    rcCpuCachePacketAclEntry.setStatus("current")
_RcCpuCachePacketPortIndex_Type = Integer32
_RcCpuCachePacketPortIndex_Object = MibTableColumn
rcCpuCachePacketPortIndex = _RcCpuCachePacketPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 16, 1, 1),
    _RcCpuCachePacketPortIndex_Type()
)
rcCpuCachePacketPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCpuCachePacketPortIndex.setStatus("current")


class _RcCpuCachePacketAclType_Type(Integer32):
    """Custom type rcCpuCachePacketAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-access-list", 1),
          ("mac-access-list", 2),
          ("access-list-map", 3))
    )


_RcCpuCachePacketAclType_Type.__name__ = "Integer32"
_RcCpuCachePacketAclType_Object = MibTableColumn
rcCpuCachePacketAclType = _RcCpuCachePacketAclType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 16, 1, 2),
    _RcCpuCachePacketAclType_Type()
)
rcCpuCachePacketAclType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketAclType.setStatus("current")


class _RcCpuCachePacketAclNo_Type(Integer32):
    """Custom type rcCpuCachePacketAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RcCpuCachePacketAclNo_Type.__name__ = "Integer32"
_RcCpuCachePacketAclNo_Object = MibTableColumn
rcCpuCachePacketAclNo = _RcCpuCachePacketAclNo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 16, 1, 3),
    _RcCpuCachePacketAclNo_Type()
)
rcCpuCachePacketAclNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketAclNo.setStatus("current")
_RcCpuCachePacketAclEnable_Type = EnableVar
_RcCpuCachePacketAclEnable_Object = MibTableColumn
rcCpuCachePacketAclEnable = _RcCpuCachePacketAclEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 16, 1, 4),
    _RcCpuCachePacketAclEnable_Type()
)
rcCpuCachePacketAclEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketAclEnable.setStatus("current")
_RcCpuCachePacketUploadServerTable_Object = MibTable
rcCpuCachePacketUploadServerTable = _RcCpuCachePacketUploadServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17)
)
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerTable.setStatus("current")
_RcCpuCachePacketUploadServerEntry_Object = MibTableRow
rcCpuCachePacketUploadServerEntry = _RcCpuCachePacketUploadServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1)
)
rcCpuCachePacketUploadServerEntry.setIndexNames(
    (0, "SWITCH-CCP-MIB", "rcCpuCachePacketUploadServerIndex"),
)
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerEntry.setStatus("current")
_RcCpuCachePacketUploadServerIndex_Type = Integer32
_RcCpuCachePacketUploadServerIndex_Object = MibTableColumn
rcCpuCachePacketUploadServerIndex = _RcCpuCachePacketUploadServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1, 1),
    _RcCpuCachePacketUploadServerIndex_Type()
)
rcCpuCachePacketUploadServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerIndex.setStatus("current")


class _RcCpuCachePacketUploadServerMode_Type(Integer32):
    """Custom type rcCpuCachePacketUploadServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_RcCpuCachePacketUploadServerMode_Type.__name__ = "Integer32"
_RcCpuCachePacketUploadServerMode_Object = MibTableColumn
rcCpuCachePacketUploadServerMode = _RcCpuCachePacketUploadServerMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1, 2),
    _RcCpuCachePacketUploadServerMode_Type()
)
rcCpuCachePacketUploadServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerMode.setStatus("current")
_RcCpuCachePacketUploadServerAddress_Type = IpAddress
_RcCpuCachePacketUploadServerAddress_Object = MibTableColumn
rcCpuCachePacketUploadServerAddress = _RcCpuCachePacketUploadServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1, 3),
    _RcCpuCachePacketUploadServerAddress_Type()
)
rcCpuCachePacketUploadServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerAddress.setStatus("current")
_RcCpuCachePacketUploadServerUserName_Type = ObjName
_RcCpuCachePacketUploadServerUserName_Object = MibTableColumn
rcCpuCachePacketUploadServerUserName = _RcCpuCachePacketUploadServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1, 4),
    _RcCpuCachePacketUploadServerUserName_Type()
)
rcCpuCachePacketUploadServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerUserName.setStatus("current")
_RcCpuCachePacketUploadServerPassword_Type = ObjName
_RcCpuCachePacketUploadServerPassword_Object = MibTableColumn
rcCpuCachePacketUploadServerPassword = _RcCpuCachePacketUploadServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1, 5),
    _RcCpuCachePacketUploadServerPassword_Type()
)
rcCpuCachePacketUploadServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerPassword.setStatus("current")
_RcCpuCachePacketUploadServerEnable_Type = EnableVar
_RcCpuCachePacketUploadServerEnable_Object = MibTableColumn
rcCpuCachePacketUploadServerEnable = _RcCpuCachePacketUploadServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 17, 1, 6),
    _RcCpuCachePacketUploadServerEnable_Type()
)
rcCpuCachePacketUploadServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuCachePacketUploadServerEnable.setStatus("current")
_RcCpuCachePacketPortStatisticsTable_Object = MibTable
rcCpuCachePacketPortStatisticsTable = _RcCpuCachePacketPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18)
)
if mibBuilder.loadTexts:
    rcCpuCachePacketPortStatisticsTable.setStatus("current")
_RcCpuCachePacketPortStatisticsEntry_Object = MibTableRow
rcCpuCachePacketPortStatisticsEntry = _RcCpuCachePacketPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18, 1)
)
rcCpuCachePacketPortStatisticsEntry.setIndexNames(
    (0, "SWITCH-CCP-MIB", "rcPacketPortStatisticsPortIndex"),
    (0, "SWITCH-CCP-MIB", "rcPacketPortStatisticsProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcCpuCachePacketPortStatisticsEntry.setStatus("current")
_RcPacketPortStatisticsPortIndex_Type = Integer32
_RcPacketPortStatisticsPortIndex_Object = MibTableColumn
rcPacketPortStatisticsPortIndex = _RcPacketPortStatisticsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18, 1, 1),
    _RcPacketPortStatisticsPortIndex_Type()
)
rcPacketPortStatisticsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPacketPortStatisticsPortIndex.setStatus("current")
_RcPacketPortStatisticsProtocolIndex_Type = Integer32
_RcPacketPortStatisticsProtocolIndex_Object = MibTableColumn
rcPacketPortStatisticsProtocolIndex = _RcPacketPortStatisticsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18, 1, 2),
    _RcPacketPortStatisticsProtocolIndex_Type()
)
rcPacketPortStatisticsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPacketPortStatisticsProtocolIndex.setStatus("current")
_RcPacketPortStatisticsPktCount_Type = Integer32
_RcPacketPortStatisticsPktCount_Object = MibTableColumn
rcPacketPortStatisticsPktCount = _RcPacketPortStatisticsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18, 1, 3),
    _RcPacketPortStatisticsPktCount_Type()
)
rcPacketPortStatisticsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketPortStatisticsPktCount.setStatus("current")
_RcPacketPortStatisticsAllPktRatio_Type = Integer32
_RcPacketPortStatisticsAllPktRatio_Object = MibTableColumn
rcPacketPortStatisticsAllPktRatio = _RcPacketPortStatisticsAllPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18, 1, 4),
    _RcPacketPortStatisticsAllPktRatio_Type()
)
rcPacketPortStatisticsAllPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketPortStatisticsAllPktRatio.setStatus("current")
_RcPacketPortStatisticsPortPktRatio_Type = Integer32
_RcPacketPortStatisticsPortPktRatio_Object = MibTableColumn
rcPacketPortStatisticsPortPktRatio = _RcPacketPortStatisticsPortPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 18, 1, 5),
    _RcPacketPortStatisticsPortPktRatio_Type()
)
rcPacketPortStatisticsPortPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketPortStatisticsPortPktRatio.setStatus("current")
_RcCpuCachePacketVlanStatisticsTable_Object = MibTable
rcCpuCachePacketVlanStatisticsTable = _RcCpuCachePacketVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19)
)
if mibBuilder.loadTexts:
    rcCpuCachePacketVlanStatisticsTable.setStatus("current")
_RcCpuCachePacketVlanStatisticsEntry_Object = MibTableRow
rcCpuCachePacketVlanStatisticsEntry = _RcCpuCachePacketVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19, 1)
)
rcCpuCachePacketVlanStatisticsEntry.setIndexNames(
    (0, "SWITCH-CCP-MIB", "rcPacketVlanStatisticsVlanIndex"),
    (0, "SWITCH-CCP-MIB", "rcPacketVlanStatisticsProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcCpuCachePacketVlanStatisticsEntry.setStatus("current")
_RcPacketVlanStatisticsVlanIndex_Type = Integer32
_RcPacketVlanStatisticsVlanIndex_Object = MibTableColumn
rcPacketVlanStatisticsVlanIndex = _RcPacketVlanStatisticsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19, 1, 1),
    _RcPacketVlanStatisticsVlanIndex_Type()
)
rcPacketVlanStatisticsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPacketVlanStatisticsVlanIndex.setStatus("current")
_RcPacketVlanStatisticsProtocolIndex_Type = Integer32
_RcPacketVlanStatisticsProtocolIndex_Object = MibTableColumn
rcPacketVlanStatisticsProtocolIndex = _RcPacketVlanStatisticsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19, 1, 2),
    _RcPacketVlanStatisticsProtocolIndex_Type()
)
rcPacketVlanStatisticsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPacketVlanStatisticsProtocolIndex.setStatus("current")
_RcPacketVlanStatisticsPktCount_Type = Integer32
_RcPacketVlanStatisticsPktCount_Object = MibTableColumn
rcPacketVlanStatisticsPktCount = _RcPacketVlanStatisticsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19, 1, 3),
    _RcPacketVlanStatisticsPktCount_Type()
)
rcPacketVlanStatisticsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketVlanStatisticsPktCount.setStatus("current")
_RcPacketVlanStatisticsAllPktRatio_Type = Integer32
_RcPacketVlanStatisticsAllPktRatio_Object = MibTableColumn
rcPacketVlanStatisticsAllPktRatio = _RcPacketVlanStatisticsAllPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19, 1, 4),
    _RcPacketVlanStatisticsAllPktRatio_Type()
)
rcPacketVlanStatisticsAllPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketVlanStatisticsAllPktRatio.setStatus("current")
_RcPacketVlanStatisticsVlanPktRatio_Type = Integer32
_RcPacketVlanStatisticsVlanPktRatio_Object = MibTableColumn
rcPacketVlanStatisticsVlanPktRatio = _RcPacketVlanStatisticsVlanPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 19, 1, 5),
    _RcPacketVlanStatisticsVlanPktRatio_Type()
)
rcPacketVlanStatisticsVlanPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketVlanStatisticsVlanPktRatio.setStatus("current")
_RcCpuCachePacketAllStatisticsTable_Object = MibTable
rcCpuCachePacketAllStatisticsTable = _RcCpuCachePacketAllStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 20)
)
if mibBuilder.loadTexts:
    rcCpuCachePacketAllStatisticsTable.setStatus("current")
_RcCpuCachePacketAllStatisticsEntry_Object = MibTableRow
rcCpuCachePacketAllStatisticsEntry = _RcCpuCachePacketAllStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 20, 1)
)
rcCpuCachePacketAllStatisticsEntry.setIndexNames(
    (0, "SWITCH-CCP-MIB", "rcPacketAllStatisticsProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcCpuCachePacketAllStatisticsEntry.setStatus("current")
_RcPacketAllStatisticsProtocolIndex_Type = Integer32
_RcPacketAllStatisticsProtocolIndex_Object = MibTableColumn
rcPacketAllStatisticsProtocolIndex = _RcPacketAllStatisticsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 20, 1, 1),
    _RcPacketAllStatisticsProtocolIndex_Type()
)
rcPacketAllStatisticsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPacketAllStatisticsProtocolIndex.setStatus("current")
_RcPacketAllStatisticsPktCount_Type = Integer32
_RcPacketAllStatisticsPktCount_Object = MibTableColumn
rcPacketAllStatisticsPktCount = _RcPacketAllStatisticsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 20, 1, 2),
    _RcPacketAllStatisticsPktCount_Type()
)
rcPacketAllStatisticsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketAllStatisticsPktCount.setStatus("current")
_RcPacketAllStatisticsAllPktRatio_Type = Integer32
_RcPacketAllStatisticsAllPktRatio_Object = MibTableColumn
rcPacketAllStatisticsAllPktRatio = _RcPacketAllStatisticsAllPktRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 55, 1, 20, 1, 3),
    _RcPacketAllStatisticsAllPktRatio_Type()
)
rcPacketAllStatisticsAllPktRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPacketAllStatisticsAllPktRatio.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-CCP-MIB",
    **{"rcCcp": rcCcp,
       "rcCpuCachePacket": rcCpuCachePacket,
       "rcCpuCachePacketEnable": rcCpuCachePacketEnable,
       "rcCpuCachePacketPortList": rcCpuCachePacketPortList,
       "rcCpuCachePacketLen": rcCpuCachePacketLen,
       "rcCpuCachePacketBufferSize": rcCpuCachePacketBufferSize,
       "rcCpuCachePacketManualUpload": rcCpuCachePacketManualUpload,
       "rcCpuCachePacketAutoUpload": rcCpuCachePacketAutoUpload,
       "rcCpuCachePacketOverride": rcCpuCachePacketOverride,
       "rcCpuCachePacketAutoUploadTimes": rcCpuCachePacketAutoUploadTimes,
       "rcCpuCachePacketClear": rcCpuCachePacketClear,
       "rcCpuCachePacketsAutoUploadCounter": rcCpuCachePacketsAutoUploadCounter,
       "rcCpuCachePacketMirrorToCpuStatus": rcCpuCachePacketMirrorToCpuStatus,
       "rcCpuCachePacketBufferStatus": rcCpuCachePacketBufferStatus,
       "rcCpuCachePacketStatus": rcCpuCachePacketStatus,
       "rcCpuCachePacketCount": rcCpuCachePacketCount,
       "rcCpuCachePacketUploadedNumber": rcCpuCachePacketUploadedNumber,
       "rcCpuCachePacketAclTable": rcCpuCachePacketAclTable,
       "rcCpuCachePacketAclEntry": rcCpuCachePacketAclEntry,
       "rcCpuCachePacketPortIndex": rcCpuCachePacketPortIndex,
       "rcCpuCachePacketAclType": rcCpuCachePacketAclType,
       "rcCpuCachePacketAclNo": rcCpuCachePacketAclNo,
       "rcCpuCachePacketAclEnable": rcCpuCachePacketAclEnable,
       "rcCpuCachePacketUploadServerTable": rcCpuCachePacketUploadServerTable,
       "rcCpuCachePacketUploadServerEntry": rcCpuCachePacketUploadServerEntry,
       "rcCpuCachePacketUploadServerIndex": rcCpuCachePacketUploadServerIndex,
       "rcCpuCachePacketUploadServerMode": rcCpuCachePacketUploadServerMode,
       "rcCpuCachePacketUploadServerAddress": rcCpuCachePacketUploadServerAddress,
       "rcCpuCachePacketUploadServerUserName": rcCpuCachePacketUploadServerUserName,
       "rcCpuCachePacketUploadServerPassword": rcCpuCachePacketUploadServerPassword,
       "rcCpuCachePacketUploadServerEnable": rcCpuCachePacketUploadServerEnable,
       "rcCpuCachePacketPortStatisticsTable": rcCpuCachePacketPortStatisticsTable,
       "rcCpuCachePacketPortStatisticsEntry": rcCpuCachePacketPortStatisticsEntry,
       "rcPacketPortStatisticsPortIndex": rcPacketPortStatisticsPortIndex,
       "rcPacketPortStatisticsProtocolIndex": rcPacketPortStatisticsProtocolIndex,
       "rcPacketPortStatisticsPktCount": rcPacketPortStatisticsPktCount,
       "rcPacketPortStatisticsAllPktRatio": rcPacketPortStatisticsAllPktRatio,
       "rcPacketPortStatisticsPortPktRatio": rcPacketPortStatisticsPortPktRatio,
       "rcCpuCachePacketVlanStatisticsTable": rcCpuCachePacketVlanStatisticsTable,
       "rcCpuCachePacketVlanStatisticsEntry": rcCpuCachePacketVlanStatisticsEntry,
       "rcPacketVlanStatisticsVlanIndex": rcPacketVlanStatisticsVlanIndex,
       "rcPacketVlanStatisticsProtocolIndex": rcPacketVlanStatisticsProtocolIndex,
       "rcPacketVlanStatisticsPktCount": rcPacketVlanStatisticsPktCount,
       "rcPacketVlanStatisticsAllPktRatio": rcPacketVlanStatisticsAllPktRatio,
       "rcPacketVlanStatisticsVlanPktRatio": rcPacketVlanStatisticsVlanPktRatio,
       "rcCpuCachePacketAllStatisticsTable": rcCpuCachePacketAllStatisticsTable,
       "rcCpuCachePacketAllStatisticsEntry": rcCpuCachePacketAllStatisticsEntry,
       "rcPacketAllStatisticsProtocolIndex": rcPacketAllStatisticsProtocolIndex,
       "rcPacketAllStatisticsPktCount": rcPacketAllStatisticsPktCount,
       "rcPacketAllStatisticsAllPktRatio": rcPacketAllStatisticsAllPktRatio}
)
