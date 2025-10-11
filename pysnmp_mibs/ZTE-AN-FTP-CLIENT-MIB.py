# SNMP MIB module (ZTE-AN-FTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-FTP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:54 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(zxAnSysObjects,) = mibBuilder.importSymbols(
    "ZTE-AN-SYS-MIB",
    "zxAnSysObjects")


# MODULE-IDENTITY

zxAnFtpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnFtpClientMIBObjects_ObjectIdentity = ObjectIdentity
zxAnFtpClientMIBObjects = _ZxAnFtpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1)
)


class _ZxAnFileFtpFileType_Type(Integer32):
    """Custom type zxAnFileFtpFileType based on Integer32"""
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
              51,
              52,
              53,
              257,
              258,
              259,
              513)
        )
    )
    namedValues = NamedValues(
        *(("sys_conf_startup", 1),
          ("sys_conf_running", 2),
          ("sys-conf-onu", 3),
          ("sys-version-onu", 4),
          ("sys-conf-narrowband", 5),
          ("sys-license-narrowband", 6),
          ("sys-log-debugging", 7),
          ("sys-log-snmp", 8),
          ("sys-log-running", 9),
          ("sys-log-clioperation", 10),
          ("xmlForPmMeasurementPoints", 51),
          ("xmlForThresholdCrossingAlert", 52),
          ("csvForPmData", 53),
          ("adsl_port_log", 257),
          ("gpon_port_log", 258),
          ("dataBulkMeasurement", 259),
          ("selfswitchTelFile", 513))
    )


_ZxAnFileFtpFileType_Type.__name__ = "Integer32"
_ZxAnFileFtpFileType_Object = MibScalar
zxAnFileFtpFileType = _ZxAnFileFtpFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 1),
    _ZxAnFileFtpFileType_Type()
)
zxAnFileFtpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpFileType.setStatus("current")


class _ZxAnFileFtpOperType_Type(Integer32):
    """Custom type zxAnFileFtpOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2))
    )


_ZxAnFileFtpOperType_Type.__name__ = "Integer32"
_ZxAnFileFtpOperType_Object = MibScalar
zxAnFileFtpOperType = _ZxAnFileFtpOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 2),
    _ZxAnFileFtpOperType_Type()
)
zxAnFileFtpOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpOperType.setStatus("current")
_ZxAnFileFtpSvrIpAddress_Type = IpAddress
_ZxAnFileFtpSvrIpAddress_Object = MibScalar
zxAnFileFtpSvrIpAddress = _ZxAnFileFtpSvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 3),
    _ZxAnFileFtpSvrIpAddress_Type()
)
zxAnFileFtpSvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpSvrIpAddress.setStatus("current")


class _ZxAnFileFtpSvrUserName_Type(DisplayString):
    """Custom type zxAnFileFtpSvrUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnFileFtpSvrUserName_Type.__name__ = "DisplayString"
_ZxAnFileFtpSvrUserName_Object = MibScalar
zxAnFileFtpSvrUserName = _ZxAnFileFtpSvrUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 4),
    _ZxAnFileFtpSvrUserName_Type()
)
zxAnFileFtpSvrUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpSvrUserName.setStatus("current")


class _ZxAnFileFtpSvrUserPwd_Type(DisplayString):
    """Custom type zxAnFileFtpSvrUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnFileFtpSvrUserPwd_Type.__name__ = "DisplayString"
_ZxAnFileFtpSvrUserPwd_Object = MibScalar
zxAnFileFtpSvrUserPwd = _ZxAnFileFtpSvrUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 5),
    _ZxAnFileFtpSvrUserPwd_Type()
)
zxAnFileFtpSvrUserPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpSvrUserPwd.setStatus("current")


class _ZxAnFileFtpSvrFilePath_Type(DisplayString):
    """Custom type zxAnFileFtpSvrFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFileFtpSvrFilePath_Type.__name__ = "DisplayString"
_ZxAnFileFtpSvrFilePath_Object = MibScalar
zxAnFileFtpSvrFilePath = _ZxAnFileFtpSvrFilePath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 6),
    _ZxAnFileFtpSvrFilePath_Type()
)
zxAnFileFtpSvrFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpSvrFilePath.setStatus("current")


class _ZxAnFileFtpSvrFileName_Type(DisplayString):
    """Custom type zxAnFileFtpSvrFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZxAnFileFtpSvrFileName_Type.__name__ = "DisplayString"
_ZxAnFileFtpSvrFileName_Object = MibScalar
zxAnFileFtpSvrFileName = _ZxAnFileFtpSvrFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 7),
    _ZxAnFileFtpSvrFileName_Type()
)
zxAnFileFtpSvrFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpSvrFileName.setStatus("current")


class _ZxAnFileFtpAction_Type(Integer32):
    """Custom type zxAnFileFtpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancleCurrentFtpSession", 1)
    )


_ZxAnFileFtpAction_Type.__name__ = "Integer32"
_ZxAnFileFtpAction_Object = MibScalar
zxAnFileFtpAction = _ZxAnFileFtpAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 8),
    _ZxAnFileFtpAction_Type()
)
zxAnFileFtpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpAction.setStatus("current")


class _ZxAnFileFtpOperStatus_Type(Integer32):
    """Custom type zxAnFileFtpOperStatus based on Integer32"""
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
        *(("notstarted", 1),
          ("inprogress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnFileFtpOperStatus_Type.__name__ = "Integer32"
_ZxAnFileFtpOperStatus_Object = MibScalar
zxAnFileFtpOperStatus = _ZxAnFileFtpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 9),
    _ZxAnFileFtpOperStatus_Type()
)
zxAnFileFtpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileFtpOperStatus.setStatus("current")


class _ZxAnFileFtpFailedReason_Type(DisplayString):
    """Custom type zxAnFileFtpFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFileFtpFailedReason_Type.__name__ = "DisplayString"
_ZxAnFileFtpFailedReason_Object = MibScalar
zxAnFileFtpFailedReason = _ZxAnFileFtpFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 10),
    _ZxAnFileFtpFailedReason_Type()
)
zxAnFileFtpFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileFtpFailedReason.setStatus("current")


class _ZxAnFileFtpSvrProtocolType_Type(Integer32):
    """Custom type zxAnFileFtpSvrProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_ZxAnFileFtpSvrProtocolType_Type.__name__ = "Integer32"
_ZxAnFileFtpSvrProtocolType_Object = MibScalar
zxAnFileFtpSvrProtocolType = _ZxAnFileFtpSvrProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 11),
    _ZxAnFileFtpSvrProtocolType_Type()
)
zxAnFileFtpSvrProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpSvrProtocolType.setStatus("current")


class _ZxAnFileFtpProgress_Type(Integer32):
    """Custom type zxAnFileFtpProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnFileFtpProgress_Type.__name__ = "Integer32"
_ZxAnFileFtpProgress_Object = MibScalar
zxAnFileFtpProgress = _ZxAnFileFtpProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 12),
    _ZxAnFileFtpProgress_Type()
)
zxAnFileFtpProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileFtpProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileFtpProgress.setUnits("%")


class _ZxAnFileFtpPerfLogType_Type(Integer32):
    """Custom type zxAnFileFtpPerfLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("for15Minutes", 1),
          ("for24Hours", 2))
    )


_ZxAnFileFtpPerfLogType_Type.__name__ = "Integer32"
_ZxAnFileFtpPerfLogType_Object = MibScalar
zxAnFileFtpPerfLogType = _ZxAnFileFtpPerfLogType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 13),
    _ZxAnFileFtpPerfLogType_Type()
)
zxAnFileFtpPerfLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpPerfLogType.setStatus("current")
_ZxAnFileFtpFileRetrieveStartTime_Type = DisplayString
_ZxAnFileFtpFileRetrieveStartTime_Object = MibScalar
zxAnFileFtpFileRetrieveStartTime = _ZxAnFileFtpFileRetrieveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 14),
    _ZxAnFileFtpFileRetrieveStartTime_Type()
)
zxAnFileFtpFileRetrieveStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpFileRetrieveStartTime.setStatus("current")
_ZxAnFileFtpFileRetrieveEndTime_Type = DisplayString
_ZxAnFileFtpFileRetrieveEndTime_Object = MibScalar
zxAnFileFtpFileRetrieveEndTime = _ZxAnFileFtpFileRetrieveEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 50, 1, 15),
    _ZxAnFileFtpFileRetrieveEndTime_Type()
)
zxAnFileFtpFileRetrieveEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileFtpFileRetrieveEndTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-FTP-CLIENT-MIB",
    **{"zxAnFtpClientMIB": zxAnFtpClientMIB,
       "zxAnFtpClientMIBObjects": zxAnFtpClientMIBObjects,
       "zxAnFileFtpFileType": zxAnFileFtpFileType,
       "zxAnFileFtpOperType": zxAnFileFtpOperType,
       "zxAnFileFtpSvrIpAddress": zxAnFileFtpSvrIpAddress,
       "zxAnFileFtpSvrUserName": zxAnFileFtpSvrUserName,
       "zxAnFileFtpSvrUserPwd": zxAnFileFtpSvrUserPwd,
       "zxAnFileFtpSvrFilePath": zxAnFileFtpSvrFilePath,
       "zxAnFileFtpSvrFileName": zxAnFileFtpSvrFileName,
       "zxAnFileFtpAction": zxAnFileFtpAction,
       "zxAnFileFtpOperStatus": zxAnFileFtpOperStatus,
       "zxAnFileFtpFailedReason": zxAnFileFtpFailedReason,
       "zxAnFileFtpSvrProtocolType": zxAnFileFtpSvrProtocolType,
       "zxAnFileFtpProgress": zxAnFileFtpProgress,
       "zxAnFileFtpPerfLogType": zxAnFileFtpPerfLogType,
       "zxAnFileFtpFileRetrieveStartTime": zxAnFileFtpFileRetrieveStartTime,
       "zxAnFileFtpFileRetrieveEndTime": zxAnFileFtpFileRetrieveEndTime}
)
