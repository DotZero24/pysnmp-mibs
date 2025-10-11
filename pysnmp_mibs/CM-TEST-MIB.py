# SNMP MIB module (CM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/CM-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:18:14 2025
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

(InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

cmTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61)
)
if mibBuilder.loadTexts:
    cmTestMib.setRevisions(
        ("2011-05-20 10:00",
         "2010-03-26 10:00",
         "2009-12-16 10:00",
         "2009-05-11 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gi_ObjectIdentity = ObjectIdentity
gi = _Gi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166)
)
_Giproducts_ObjectIdentity = ObjectIdentity
giproducts = _Giproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1)
)
_Cm_ObjectIdentity = ObjectIdentity
cm = _Cm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19)
)
_CmTestFtpDownstreamSpeed_ObjectIdentity = ObjectIdentity
cmTestFtpDownstreamSpeed = _CmTestFtpDownstreamSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1)
)
_CmTestFtpServerAddressType_Type = InetAddressType
_CmTestFtpServerAddressType_Object = MibScalar
cmTestFtpServerAddressType = _CmTestFtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 1),
    _CmTestFtpServerAddressType_Type()
)
cmTestFtpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpServerAddressType.setStatus("current")


class _CmTestFtpServerAddress_Type(DisplayString):
    """Custom type cmTestFtpServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmTestFtpServerAddress_Type.__name__ = "DisplayString"
_CmTestFtpServerAddress_Object = MibScalar
cmTestFtpServerAddress = _CmTestFtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 2),
    _CmTestFtpServerAddress_Type()
)
cmTestFtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpServerAddress.setStatus("current")


class _CmTestFtpServerPort_Type(InetPortNumber):
    """Custom type cmTestFtpServerPort based on InetPortNumber"""
    defaultValue = 21


_CmTestFtpServerPort_Type.__name__ = "InetPortNumber"
_CmTestFtpServerPort_Object = MibScalar
cmTestFtpServerPort = _CmTestFtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 3),
    _CmTestFtpServerPort_Type()
)
cmTestFtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpServerPort.setStatus("current")


class _CmTestFtpUserName_Type(DisplayString):
    """Custom type cmTestFtpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmTestFtpUserName_Type.__name__ = "DisplayString"
_CmTestFtpUserName_Object = MibScalar
cmTestFtpUserName = _CmTestFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 4),
    _CmTestFtpUserName_Type()
)
cmTestFtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUserName.setStatus("current")


class _CmTestFtpPassword_Type(DisplayString):
    """Custom type cmTestFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmTestFtpPassword_Type.__name__ = "DisplayString"
_CmTestFtpPassword_Object = MibScalar
cmTestFtpPassword = _CmTestFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 5),
    _CmTestFtpPassword_Type()
)
cmTestFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpPassword.setStatus("current")


class _CmTestFtpFilename_Type(DisplayString):
    """Custom type cmTestFtpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmTestFtpFilename_Type.__name__ = "DisplayString"
_CmTestFtpFilename_Object = MibScalar
cmTestFtpFilename = _CmTestFtpFilename_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 6),
    _CmTestFtpFilename_Type()
)
cmTestFtpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpFilename.setStatus("current")


class _CmTestFtpCommand_Type(Integer32):
    """Custom type cmTestFtpCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 0),
          ("get", 1))
    )


_CmTestFtpCommand_Type.__name__ = "Integer32"
_CmTestFtpCommand_Object = MibScalar
cmTestFtpCommand = _CmTestFtpCommand_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 7),
    _CmTestFtpCommand_Type()
)
cmTestFtpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpCommand.setStatus("current")


class _CmTestFtpTransferStatus_Type(Integer32):
    """Custom type cmTestFtpTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              226,
              421,
              530,
              550)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("inProgress", 1),
          ("transferComplete", 226),
          ("serviceNotAvail", 421),
          ("invalidLogin", 530),
          ("fileNotFound", 550))
    )


_CmTestFtpTransferStatus_Type.__name__ = "Integer32"
_CmTestFtpTransferStatus_Object = MibScalar
cmTestFtpTransferStatus = _CmTestFtpTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 8),
    _CmTestFtpTransferStatus_Type()
)
cmTestFtpTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpTransferStatus.setStatus("current")
_CmTestFtpTransferPayloadBytes_Type = Counter32
_CmTestFtpTransferPayloadBytes_Object = MibScalar
cmTestFtpTransferPayloadBytes = _CmTestFtpTransferPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 9),
    _CmTestFtpTransferPayloadBytes_Type()
)
cmTestFtpTransferPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpTransferPayloadBytes.setStatus("current")
_CmTestFtpTransferTotalBytes_Type = Counter32
_CmTestFtpTransferTotalBytes_Object = MibScalar
cmTestFtpTransferTotalBytes = _CmTestFtpTransferTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 10),
    _CmTestFtpTransferTotalBytes_Type()
)
cmTestFtpTransferTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpTransferTotalBytes.setStatus("current")
_CmTestFtpTransferElapsedTime_Type = TimeInterval
_CmTestFtpTransferElapsedTime_Object = MibScalar
cmTestFtpTransferElapsedTime = _CmTestFtpTransferElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 11),
    _CmTestFtpTransferElapsedTime_Type()
)
cmTestFtpTransferElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpTransferElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    cmTestFtpTransferElapsedTime.setUnits("milliseconds")
_CmTestFtpTransferThroughput_Type = Unsigned32
_CmTestFtpTransferThroughput_Object = MibScalar
cmTestFtpTransferThroughput = _CmTestFtpTransferThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 1, 12),
    _CmTestFtpTransferThroughput_Type()
)
cmTestFtpTransferThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpTransferThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cmTestFtpTransferThroughput.setUnits("bits per second")
_CmTestFtpUpstreamSpeed_ObjectIdentity = ObjectIdentity
cmTestFtpUpstreamSpeed = _CmTestFtpUpstreamSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2)
)
_CmTestFtpUpstreamServerAddressType_Type = InetAddressType
_CmTestFtpUpstreamServerAddressType_Object = MibScalar
cmTestFtpUpstreamServerAddressType = _CmTestFtpUpstreamServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 1),
    _CmTestFtpUpstreamServerAddressType_Type()
)
cmTestFtpUpstreamServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamServerAddressType.setStatus("current")


class _CmTestFtpUpstreamServerAddress_Type(DisplayString):
    """Custom type cmTestFtpUpstreamServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmTestFtpUpstreamServerAddress_Type.__name__ = "DisplayString"
_CmTestFtpUpstreamServerAddress_Object = MibScalar
cmTestFtpUpstreamServerAddress = _CmTestFtpUpstreamServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 2),
    _CmTestFtpUpstreamServerAddress_Type()
)
cmTestFtpUpstreamServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamServerAddress.setStatus("current")


class _CmTestFtpUpstreamServerPort_Type(InetPortNumber):
    """Custom type cmTestFtpUpstreamServerPort based on InetPortNumber"""
    defaultValue = 21


_CmTestFtpUpstreamServerPort_Type.__name__ = "InetPortNumber"
_CmTestFtpUpstreamServerPort_Object = MibScalar
cmTestFtpUpstreamServerPort = _CmTestFtpUpstreamServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 3),
    _CmTestFtpUpstreamServerPort_Type()
)
cmTestFtpUpstreamServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamServerPort.setStatus("current")


class _CmTestFtpUpstreamUserName_Type(DisplayString):
    """Custom type cmTestFtpUpstreamUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmTestFtpUpstreamUserName_Type.__name__ = "DisplayString"
_CmTestFtpUpstreamUserName_Object = MibScalar
cmTestFtpUpstreamUserName = _CmTestFtpUpstreamUserName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 4),
    _CmTestFtpUpstreamUserName_Type()
)
cmTestFtpUpstreamUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamUserName.setStatus("current")


class _CmTestFtpUpstreamPassword_Type(DisplayString):
    """Custom type cmTestFtpUpstreamPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmTestFtpUpstreamPassword_Type.__name__ = "DisplayString"
_CmTestFtpUpstreamPassword_Object = MibScalar
cmTestFtpUpstreamPassword = _CmTestFtpUpstreamPassword_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 5),
    _CmTestFtpUpstreamPassword_Type()
)
cmTestFtpUpstreamPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamPassword.setStatus("current")


class _CmTestFtpUpstreamFilename_Type(DisplayString):
    """Custom type cmTestFtpUpstreamFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmTestFtpUpstreamFilename_Type.__name__ = "DisplayString"
_CmTestFtpUpstreamFilename_Object = MibScalar
cmTestFtpUpstreamFilename = _CmTestFtpUpstreamFilename_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 6),
    _CmTestFtpUpstreamFilename_Type()
)
cmTestFtpUpstreamFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamFilename.setStatus("current")
_CmTestFtpUpstreamFileSize_Type = Counter32
_CmTestFtpUpstreamFileSize_Object = MibScalar
cmTestFtpUpstreamFileSize = _CmTestFtpUpstreamFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 7),
    _CmTestFtpUpstreamFileSize_Type()
)
cmTestFtpUpstreamFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamFileSize.setStatus("current")


class _CmTestFtpUpstreamCommand_Type(Integer32):
    """Custom type cmTestFtpUpstreamCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 0),
          ("put", 1))
    )


_CmTestFtpUpstreamCommand_Type.__name__ = "Integer32"
_CmTestFtpUpstreamCommand_Object = MibScalar
cmTestFtpUpstreamCommand = _CmTestFtpUpstreamCommand_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 8),
    _CmTestFtpUpstreamCommand_Type()
)
cmTestFtpUpstreamCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamCommand.setStatus("current")


class _CmTestFtpUpstreamTransferStatus_Type(Integer32):
    """Custom type cmTestFtpUpstreamTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              226,
              421,
              530)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("inProgress", 1),
          ("transferComplete", 226),
          ("serviceNotAvail", 421),
          ("invalidLogin", 530))
    )


_CmTestFtpUpstreamTransferStatus_Type.__name__ = "Integer32"
_CmTestFtpUpstreamTransferStatus_Object = MibScalar
cmTestFtpUpstreamTransferStatus = _CmTestFtpUpstreamTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 9),
    _CmTestFtpUpstreamTransferStatus_Type()
)
cmTestFtpUpstreamTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferStatus.setStatus("current")
_CmTestFtpUpstreamTransferPayloadBytes_Type = Counter32
_CmTestFtpUpstreamTransferPayloadBytes_Object = MibScalar
cmTestFtpUpstreamTransferPayloadBytes = _CmTestFtpUpstreamTransferPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 10),
    _CmTestFtpUpstreamTransferPayloadBytes_Type()
)
cmTestFtpUpstreamTransferPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferPayloadBytes.setStatus("current")
_CmTestFtpUpstreamTransferTotalBytes_Type = Counter32
_CmTestFtpUpstreamTransferTotalBytes_Object = MibScalar
cmTestFtpUpstreamTransferTotalBytes = _CmTestFtpUpstreamTransferTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 11),
    _CmTestFtpUpstreamTransferTotalBytes_Type()
)
cmTestFtpUpstreamTransferTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferTotalBytes.setStatus("current")
_CmTestFtpUpstreamTransferElapsedTime_Type = TimeInterval
_CmTestFtpUpstreamTransferElapsedTime_Object = MibScalar
cmTestFtpUpstreamTransferElapsedTime = _CmTestFtpUpstreamTransferElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 12),
    _CmTestFtpUpstreamTransferElapsedTime_Type()
)
cmTestFtpUpstreamTransferElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferElapsedTime.setUnits("milliseconds")
_CmTestFtpUpstreamTransferThroughput_Type = Unsigned32
_CmTestFtpUpstreamTransferThroughput_Object = MibScalar
cmTestFtpUpstreamTransferThroughput = _CmTestFtpUpstreamTransferThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 61, 2, 13),
    _CmTestFtpUpstreamTransferThroughput_Type()
)
cmTestFtpUpstreamTransferThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cmTestFtpUpstreamTransferThroughput.setUnits("bits per second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-TEST-MIB",
    **{"gi": gi,
       "giproducts": giproducts,
       "cm": cm,
       "cmTestMib": cmTestMib,
       "cmTestFtpDownstreamSpeed": cmTestFtpDownstreamSpeed,
       "cmTestFtpServerAddressType": cmTestFtpServerAddressType,
       "cmTestFtpServerAddress": cmTestFtpServerAddress,
       "cmTestFtpServerPort": cmTestFtpServerPort,
       "cmTestFtpUserName": cmTestFtpUserName,
       "cmTestFtpPassword": cmTestFtpPassword,
       "cmTestFtpFilename": cmTestFtpFilename,
       "cmTestFtpCommand": cmTestFtpCommand,
       "cmTestFtpTransferStatus": cmTestFtpTransferStatus,
       "cmTestFtpTransferPayloadBytes": cmTestFtpTransferPayloadBytes,
       "cmTestFtpTransferTotalBytes": cmTestFtpTransferTotalBytes,
       "cmTestFtpTransferElapsedTime": cmTestFtpTransferElapsedTime,
       "cmTestFtpTransferThroughput": cmTestFtpTransferThroughput,
       "cmTestFtpUpstreamSpeed": cmTestFtpUpstreamSpeed,
       "cmTestFtpUpstreamServerAddressType": cmTestFtpUpstreamServerAddressType,
       "cmTestFtpUpstreamServerAddress": cmTestFtpUpstreamServerAddress,
       "cmTestFtpUpstreamServerPort": cmTestFtpUpstreamServerPort,
       "cmTestFtpUpstreamUserName": cmTestFtpUpstreamUserName,
       "cmTestFtpUpstreamPassword": cmTestFtpUpstreamPassword,
       "cmTestFtpUpstreamFilename": cmTestFtpUpstreamFilename,
       "cmTestFtpUpstreamFileSize": cmTestFtpUpstreamFileSize,
       "cmTestFtpUpstreamCommand": cmTestFtpUpstreamCommand,
       "cmTestFtpUpstreamTransferStatus": cmTestFtpUpstreamTransferStatus,
       "cmTestFtpUpstreamTransferPayloadBytes": cmTestFtpUpstreamTransferPayloadBytes,
       "cmTestFtpUpstreamTransferTotalBytes": cmTestFtpUpstreamTransferTotalBytes,
       "cmTestFtpUpstreamTransferElapsedTime": cmTestFtpUpstreamTransferElapsedTime,
       "cmTestFtpUpstreamTransferThroughput": cmTestFtpUpstreamTransferThroughput}
)
