# SNMP MIB module (OS-EXPORT-DATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-EXPORT-DATA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:48 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

osExportData = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16)
)
if mibBuilder.loadTexts:
    osExportData.setRevisions(
        ("2013-05-23 00:00",
         "2011-06-01 00:00",
         "2009-11-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsExportDataCapabilities_ObjectIdentity = ObjectIdentity
osExportDataCapabilities = _OsExportDataCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 1)
)


class _OsExportDataSampleTypeSup_Type(Bits):
    """Custom type osExportDataSampleTypeSup based on Bits"""
    namedValues = NamedValues(
        *(("serviceCounters", 0),
          ("loopbackTests", 1),
          ("delayMeasureTests", 2),
          ("ipSlaTests", 3),
          ("rfc2544Tests", 4),
          ("delayMeasureHrTests", 5),
          ("soamTestDmStatsHistory", 6),
          ("soamTestLmStatsHistory", 7))
    )

_OsExportDataSampleTypeSup_Type.__name__ = "Bits"
_OsExportDataSampleTypeSup_Object = MibScalar
osExportDataSampleTypeSup = _OsExportDataSampleTypeSup_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 1, 1),
    _OsExportDataSampleTypeSup_Type()
)
osExportDataSampleTypeSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataSampleTypeSup.setStatus("current")


class _OsExportDataTransferProtocolSup_Type(Bits):
    """Custom type osExportDataTransferProtocolSup based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("tftpClient", 1),
          ("ftpClient", 2),
          ("scpClient", 3),
          ("sftpClient", 4))
    )

_OsExportDataTransferProtocolSup_Type.__name__ = "Bits"
_OsExportDataTransferProtocolSup_Object = MibScalar
osExportDataTransferProtocolSup = _OsExportDataTransferProtocolSup_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 1, 2),
    _OsExportDataTransferProtocolSup_Type()
)
osExportDataTransferProtocolSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataTransferProtocolSup.setStatus("current")
_OsExportDataTable_Object = MibTable
osExportDataTable = _OsExportDataTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2)
)
if mibBuilder.loadTexts:
    osExportDataTable.setStatus("current")
_OsExportDataEntry_Object = MibTableRow
osExportDataEntry = _OsExportDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1)
)
osExportDataEntry.setIndexNames(
    (0, "OS-EXPORT-DATA-MIB", "osExportDataName"),
)
if mibBuilder.loadTexts:
    osExportDataEntry.setStatus("current")


class _OsExportDataName_Type(SnmpAdminString):
    """Custom type osExportDataName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OsExportDataName_Type.__name__ = "SnmpAdminString"
_OsExportDataName_Object = MibTableColumn
osExportDataName = _OsExportDataName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 1),
    _OsExportDataName_Type()
)
osExportDataName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osExportDataName.setStatus("current")


class _OsExportDataServerAddressType_Type(InetAddressType):
    """Custom type osExportDataServerAddressType based on InetAddressType"""
    defaultValue = 1


_OsExportDataServerAddressType_Type.__name__ = "InetAddressType"
_OsExportDataServerAddressType_Object = MibTableColumn
osExportDataServerAddressType = _OsExportDataServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 2),
    _OsExportDataServerAddressType_Type()
)
osExportDataServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataServerAddressType.setStatus("current")


class _OsExportDataServerAddress_Type(InetAddress):
    """Custom type osExportDataServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OsExportDataServerAddress_Type.__name__ = "InetAddress"
_OsExportDataServerAddress_Object = MibTableColumn
osExportDataServerAddress = _OsExportDataServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 3),
    _OsExportDataServerAddress_Type()
)
osExportDataServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataServerAddress.setStatus("current")


class _OsExportDataRemoteDirName_Type(DisplayString):
    """Custom type osExportDataRemoteDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OsExportDataRemoteDirName_Type.__name__ = "DisplayString"
_OsExportDataRemoteDirName_Object = MibTableColumn
osExportDataRemoteDirName = _OsExportDataRemoteDirName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 4),
    _OsExportDataRemoteDirName_Type()
)
osExportDataRemoteDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataRemoteDirName.setStatus("current")


class _OsExportDataRemoteFileName_Type(DisplayString):
    """Custom type osExportDataRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OsExportDataRemoteFileName_Type.__name__ = "DisplayString"
_OsExportDataRemoteFileName_Object = MibTableColumn
osExportDataRemoteFileName = _OsExportDataRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 5),
    _OsExportDataRemoteFileName_Type()
)
osExportDataRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataRemoteFileName.setStatus("current")


class _OsExportDataRemoteUsername_Type(DisplayString):
    """Custom type osExportDataRemoteUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OsExportDataRemoteUsername_Type.__name__ = "DisplayString"
_OsExportDataRemoteUsername_Object = MibTableColumn
osExportDataRemoteUsername = _OsExportDataRemoteUsername_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 6),
    _OsExportDataRemoteUsername_Type()
)
osExportDataRemoteUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataRemoteUsername.setStatus("current")


class _OsExportDataRemotePassword_Type(DisplayString):
    """Custom type osExportDataRemotePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OsExportDataRemotePassword_Type.__name__ = "DisplayString"
_OsExportDataRemotePassword_Object = MibTableColumn
osExportDataRemotePassword = _OsExportDataRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 7),
    _OsExportDataRemotePassword_Type()
)
osExportDataRemotePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataRemotePassword.setStatus("current")


class _OsExportDataSampleType_Type(Integer32):
    """Custom type osExportDataSampleType based on Integer32"""
    defaultValue = 1

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
        *(("serviceCounters", 1),
          ("loopbackTests", 2),
          ("delayMeasureTests", 3),
          ("ipSlaTests", 4),
          ("rfc2544Tests", 5),
          ("delayMeasureHrTests", 6),
          ("soamTestDmStatsHistory", 7),
          ("soamTestLmStatsHistory", 8))
    )


_OsExportDataSampleType_Type.__name__ = "Integer32"
_OsExportDataSampleType_Object = MibTableColumn
osExportDataSampleType = _OsExportDataSampleType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 10),
    _OsExportDataSampleType_Type()
)
osExportDataSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataSampleType.setStatus("current")


class _OsExportDataSampleInterval_Type(Integer32):
    """Custom type osExportDataSampleInterval based on Integer32"""
    defaultValue = 1

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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("once", 1),
          ("month", 2),
          ("week", 3),
          ("day", 4),
          ("every12hrs", 5),
          ("every8hrs", 6),
          ("every6hrs", 7),
          ("every4hrs", 8),
          ("every2hrs", 9),
          ("every1hr", 10),
          ("every30mins", 11),
          ("every15mins", 12),
          ("every10mins", 13),
          ("every5mins", 14),
          ("every2mins", 15),
          ("every1min", 16),
          ("every30secs", 17),
          ("every15secs", 18),
          ("every10secs", 19),
          ("every5secs", 20),
          ("every2secs", 21),
          ("every1sec", 22))
    )


_OsExportDataSampleInterval_Type.__name__ = "Integer32"
_OsExportDataSampleInterval_Object = MibTableColumn
osExportDataSampleInterval = _OsExportDataSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 11),
    _OsExportDataSampleInterval_Type()
)
osExportDataSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataSampleInterval.setStatus("current")


class _OsExportDataSamplesCounter_Type(Integer32):
    """Custom type osExportDataSamplesCounter based on Integer32"""
    defaultValue = 0


_OsExportDataSamplesCounter_Type.__name__ = "Integer32"
_OsExportDataSamplesCounter_Object = MibTableColumn
osExportDataSamplesCounter = _OsExportDataSamplesCounter_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 12),
    _OsExportDataSamplesCounter_Type()
)
osExportDataSamplesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataSamplesCounter.setStatus("current")


class _OsExportDataTransferProtocol_Type(Integer32):
    """Custom type osExportDataTransferProtocol based on Integer32"""
    defaultValue = 3

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
        *(("other", 1),
          ("tftpClient", 2),
          ("ftpClient", 3),
          ("scpClient", 4),
          ("sftpClient", 5))
    )


_OsExportDataTransferProtocol_Type.__name__ = "Integer32"
_OsExportDataTransferProtocol_Object = MibTableColumn
osExportDataTransferProtocol = _OsExportDataTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 15),
    _OsExportDataTransferProtocol_Type()
)
osExportDataTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataTransferProtocol.setStatus("current")


class _OsExportDataTransferBlockSize_Type(Integer32):
    """Custom type osExportDataTransferBlockSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_OsExportDataTransferBlockSize_Type.__name__ = "Integer32"
_OsExportDataTransferBlockSize_Object = MibTableColumn
osExportDataTransferBlockSize = _OsExportDataTransferBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 16),
    _OsExportDataTransferBlockSize_Type()
)
osExportDataTransferBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataTransferBlockSize.setStatus("current")


class _OsExportDataTransfersCounter_Type(Integer32):
    """Custom type osExportDataTransfersCounter based on Integer32"""
    defaultValue = 0


_OsExportDataTransfersCounter_Type.__name__ = "Integer32"
_OsExportDataTransfersCounter_Object = MibTableColumn
osExportDataTransfersCounter = _OsExportDataTransfersCounter_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 17),
    _OsExportDataTransfersCounter_Type()
)
osExportDataTransfersCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataTransfersCounter.setStatus("current")


class _OsExportDataStartTime_Type(DateAndTime):
    """Custom type osExportDataStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OsExportDataStartTime_Type.__name__ = "DateAndTime"
_OsExportDataStartTime_Object = MibTableColumn
osExportDataStartTime = _OsExportDataStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 20),
    _OsExportDataStartTime_Type()
)
osExportDataStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataStartTime.setStatus("current")


class _OsExportDataLastStartTime_Type(DateAndTime):
    """Custom type osExportDataLastStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OsExportDataLastStartTime_Type.__name__ = "DateAndTime"
_OsExportDataLastStartTime_Object = MibTableColumn
osExportDataLastStartTime = _OsExportDataLastStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 21),
    _OsExportDataLastStartTime_Type()
)
osExportDataLastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataLastStartTime.setStatus("current")


class _OsExportDataNextSampleTime_Type(DateAndTime):
    """Custom type osExportDataNextSampleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OsExportDataNextSampleTime_Type.__name__ = "DateAndTime"
_OsExportDataNextSampleTime_Object = MibTableColumn
osExportDataNextSampleTime = _OsExportDataNextSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 22),
    _OsExportDataNextSampleTime_Type()
)
osExportDataNextSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataNextSampleTime.setStatus("current")


class _OsExportDataLastSampleTime_Type(DateAndTime):
    """Custom type osExportDataLastSampleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OsExportDataLastSampleTime_Type.__name__ = "DateAndTime"
_OsExportDataLastSampleTime_Object = MibTableColumn
osExportDataLastSampleTime = _OsExportDataLastSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 23),
    _OsExportDataLastSampleTime_Type()
)
osExportDataLastSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataLastSampleTime.setStatus("current")


class _OsExportDataNextTransferTime_Type(DateAndTime):
    """Custom type osExportDataNextTransferTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OsExportDataNextTransferTime_Type.__name__ = "DateAndTime"
_OsExportDataNextTransferTime_Object = MibTableColumn
osExportDataNextTransferTime = _OsExportDataNextTransferTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 24),
    _OsExportDataNextTransferTime_Type()
)
osExportDataNextTransferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataNextTransferTime.setStatus("current")


class _OsExportDataLastTransferTime_Type(DateAndTime):
    """Custom type osExportDataLastTransferTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OsExportDataLastTransferTime_Type.__name__ = "DateAndTime"
_OsExportDataLastTransferTime_Object = MibTableColumn
osExportDataLastTransferTime = _OsExportDataLastTransferTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 25),
    _OsExportDataLastTransferTime_Type()
)
osExportDataLastTransferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataLastTransferTime.setStatus("current")


class _OsExportDataOperStatus_Type(Integer32):
    """Custom type osExportDataOperStatus based on Integer32"""
    defaultValue = 1

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("waitForSchedule", 1),
          ("waitForSample", 2),
          ("sampleInProcess", 3),
          ("transferInProcess", 4),
          ("sampleCompletedOk", 5),
          ("transferCompletedOk", 6),
          ("sampleError", 7),
          ("transferError", 8),
          ("exportCanceled", 9))
    )


_OsExportDataOperStatus_Type.__name__ = "Integer32"
_OsExportDataOperStatus_Object = MibTableColumn
osExportDataOperStatus = _OsExportDataOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 30),
    _OsExportDataOperStatus_Type()
)
osExportDataOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataOperStatus.setStatus("current")


class _OsExportDataAdminStatus_Type(Integer32):
    """Custom type osExportDataAdminStatus based on Integer32"""
    defaultValue = 1

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
        *(("stop", 1),
          ("start", 2),
          ("continue", 3),
          ("sample", 4),
          ("transfer", 5),
          ("invalid", 6),
          ("waitForInit", 7))
    )


_OsExportDataAdminStatus_Type.__name__ = "Integer32"
_OsExportDataAdminStatus_Object = MibTableColumn
osExportDataAdminStatus = _OsExportDataAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 31),
    _OsExportDataAdminStatus_Type()
)
osExportDataAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataAdminStatus.setStatus("current")


class _OsExportDataErrorStatus_Type(Integer32):
    """Custom type osExportDataErrorStatus based on Integer32"""
    defaultValue = 1

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
        *(("noError", 1),
          ("transferFailure", 2),
          ("sampleFailure", 3),
          ("stopFailure", 4),
          ("startFailure", 5),
          ("deleteFailure", 6),
          ("unknownError", 7))
    )


_OsExportDataErrorStatus_Type.__name__ = "Integer32"
_OsExportDataErrorStatus_Object = MibTableColumn
osExportDataErrorStatus = _OsExportDataErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 32),
    _OsExportDataErrorStatus_Type()
)
osExportDataErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataErrorStatus.setStatus("current")


class _OsExportDataDescription_Type(DisplayString):
    """Custom type osExportDataDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_OsExportDataDescription_Type.__name__ = "DisplayString"
_OsExportDataDescription_Object = MibTableColumn
osExportDataDescription = _OsExportDataDescription_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 40),
    _OsExportDataDescription_Type()
)
osExportDataDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataDescription.setStatus("current")


class _OsExportDataClientId_Type(DisplayString):
    """Custom type osExportDataClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OsExportDataClientId_Type.__name__ = "DisplayString"
_OsExportDataClientId_Object = MibTableColumn
osExportDataClientId = _OsExportDataClientId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 2, 1, 41),
    _OsExportDataClientId_Type()
)
osExportDataClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataClientId.setStatus("current")
_OsExportDataExtTable_Object = MibTable
osExportDataExtTable = _OsExportDataExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 3)
)
if mibBuilder.loadTexts:
    osExportDataExtTable.setStatus("current")
_OsExportDataExtEntry_Object = MibTableRow
osExportDataExtEntry = _OsExportDataExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    osExportDataExtEntry.setStatus("current")


class _OsExportDataSecureRemotePassword_Type(DisplayString):
    """Custom type osExportDataSecureRemotePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OsExportDataSecureRemotePassword_Type.__name__ = "DisplayString"
_OsExportDataSecureRemotePassword_Object = MibTableColumn
osExportDataSecureRemotePassword = _OsExportDataSecureRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 3, 1, 1),
    _OsExportDataSecureRemotePassword_Type()
)
osExportDataSecureRemotePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osExportDataSecureRemotePassword.setStatus("current")


class _OsExportDataSecureMode_Type(Integer32):
    """Custom type osExportDataSecureMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plainPassword", 1),
          ("encryptedPassword", 2))
    )


_OsExportDataSecureMode_Type.__name__ = "Integer32"
_OsExportDataSecureMode_Object = MibTableColumn
osExportDataSecureMode = _OsExportDataSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 3, 1, 2),
    _OsExportDataSecureMode_Type()
)
osExportDataSecureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osExportDataSecureMode.setStatus("current")
_OsExportDataConformance_ObjectIdentity = ObjectIdentity
osExportDataConformance = _OsExportDataConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 100)
)
_OsExportDataMIBCompliances_ObjectIdentity = ObjectIdentity
osExportDataMIBCompliances = _OsExportDataMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 100, 1)
)
_OsExportDataMIBGroups_ObjectIdentity = ObjectIdentity
osExportDataMIBGroups = _OsExportDataMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 100, 2)
)
osExportDataEntry.registerAugmentions(
    ("OS-EXPORT-DATA-MIB",
     "osExportDataExtEntry")
)
osExportDataExtEntry.setIndexNames(*osExportDataEntry.getIndexNames())

# Managed Objects groups

osExportMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 100, 2, 1)
)
osExportMandatoryGroup.setObjects(
      *(("OS-EXPORT-DATA-MIB", "osExportDataSampleTypeSup"),
        ("OS-EXPORT-DATA-MIB", "osExportDataTransferProtocolSup"),
        ("OS-EXPORT-DATA-MIB", "osExportDataServerAddressType"),
        ("OS-EXPORT-DATA-MIB", "osExportDataServerAddress"),
        ("OS-EXPORT-DATA-MIB", "osExportDataRemoteDirName"),
        ("OS-EXPORT-DATA-MIB", "osExportDataRemoteFileName"),
        ("OS-EXPORT-DATA-MIB", "osExportDataRemoteUsername"),
        ("OS-EXPORT-DATA-MIB", "osExportDataRemotePassword"),
        ("OS-EXPORT-DATA-MIB", "osExportDataSampleType"),
        ("OS-EXPORT-DATA-MIB", "osExportDataSampleInterval"),
        ("OS-EXPORT-DATA-MIB", "osExportDataSamplesCounter"),
        ("OS-EXPORT-DATA-MIB", "osExportDataTransferProtocol"),
        ("OS-EXPORT-DATA-MIB", "osExportDataTransferBlockSize"),
        ("OS-EXPORT-DATA-MIB", "osExportDataTransfersCounter"),
        ("OS-EXPORT-DATA-MIB", "osExportDataStartTime"),
        ("OS-EXPORT-DATA-MIB", "osExportDataLastStartTime"),
        ("OS-EXPORT-DATA-MIB", "osExportDataNextSampleTime"),
        ("OS-EXPORT-DATA-MIB", "osExportDataLastSampleTime"),
        ("OS-EXPORT-DATA-MIB", "osExportDataNextTransferTime"),
        ("OS-EXPORT-DATA-MIB", "osExportDataLastTransferTime"),
        ("OS-EXPORT-DATA-MIB", "osExportDataOperStatus"),
        ("OS-EXPORT-DATA-MIB", "osExportDataAdminStatus"),
        ("OS-EXPORT-DATA-MIB", "osExportDataErrorStatus"),
        ("OS-EXPORT-DATA-MIB", "osExportDataDescription"),
        ("OS-EXPORT-DATA-MIB", "osExportDataClientId"),
        ("OS-EXPORT-DATA-MIB", "osExportDataSecureRemotePassword"),
        ("OS-EXPORT-DATA-MIB", "osExportDataSecureMode"))
)
if mibBuilder.loadTexts:
    osExportMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osExportMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 16, 100, 1, 1)
)
osExportMIBCompliance.setObjects(
    ("OS-EXPORT-DATA-MIB", "osExportMandatoryGroup")
)
if mibBuilder.loadTexts:
    osExportMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-EXPORT-DATA-MIB",
    **{"osExportData": osExportData,
       "osExportDataCapabilities": osExportDataCapabilities,
       "osExportDataSampleTypeSup": osExportDataSampleTypeSup,
       "osExportDataTransferProtocolSup": osExportDataTransferProtocolSup,
       "osExportDataTable": osExportDataTable,
       "osExportDataEntry": osExportDataEntry,
       "osExportDataName": osExportDataName,
       "osExportDataServerAddressType": osExportDataServerAddressType,
       "osExportDataServerAddress": osExportDataServerAddress,
       "osExportDataRemoteDirName": osExportDataRemoteDirName,
       "osExportDataRemoteFileName": osExportDataRemoteFileName,
       "osExportDataRemoteUsername": osExportDataRemoteUsername,
       "osExportDataRemotePassword": osExportDataRemotePassword,
       "osExportDataSampleType": osExportDataSampleType,
       "osExportDataSampleInterval": osExportDataSampleInterval,
       "osExportDataSamplesCounter": osExportDataSamplesCounter,
       "osExportDataTransferProtocol": osExportDataTransferProtocol,
       "osExportDataTransferBlockSize": osExportDataTransferBlockSize,
       "osExportDataTransfersCounter": osExportDataTransfersCounter,
       "osExportDataStartTime": osExportDataStartTime,
       "osExportDataLastStartTime": osExportDataLastStartTime,
       "osExportDataNextSampleTime": osExportDataNextSampleTime,
       "osExportDataLastSampleTime": osExportDataLastSampleTime,
       "osExportDataNextTransferTime": osExportDataNextTransferTime,
       "osExportDataLastTransferTime": osExportDataLastTransferTime,
       "osExportDataOperStatus": osExportDataOperStatus,
       "osExportDataAdminStatus": osExportDataAdminStatus,
       "osExportDataErrorStatus": osExportDataErrorStatus,
       "osExportDataDescription": osExportDataDescription,
       "osExportDataClientId": osExportDataClientId,
       "osExportDataExtTable": osExportDataExtTable,
       "osExportDataExtEntry": osExportDataExtEntry,
       "osExportDataSecureRemotePassword": osExportDataSecureRemotePassword,
       "osExportDataSecureMode": osExportDataSecureMode,
       "osExportDataConformance": osExportDataConformance,
       "osExportDataMIBCompliances": osExportDataMIBCompliances,
       "osExportMIBCompliance": osExportMIBCompliance,
       "osExportDataMIBGroups": osExportDataMIBGroups,
       "osExportMandatoryGroup": osExportMandatoryGroup}
)
