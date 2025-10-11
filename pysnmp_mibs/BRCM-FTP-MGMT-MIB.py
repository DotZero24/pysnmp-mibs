# SNMP MIB module (BRCM-FTP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-FTP-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:02 2025
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

(cableDataMgmtMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtMIBObjects")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

ftpMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ftpMgmt.setRevisions(
        ("2009-08-12 00:00",
         "2009-03-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _FtpIpStackInterface_Type(Integer32):
    """Custom type ftpIpStackInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FtpIpStackInterface_Type.__name__ = "Integer32"
_FtpIpStackInterface_Object = MibScalar
ftpIpStackInterface = _FtpIpStackInterface_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 1),
    _FtpIpStackInterface_Type()
)
ftpIpStackInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpIpStackInterface.setStatus("current")
_FtpServerAddressType_Type = InetAddressType
_FtpServerAddressType_Object = MibScalar
ftpServerAddressType = _FtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 2),
    _FtpServerAddressType_Type()
)
ftpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerAddressType.setStatus("current")
_FtpServerAddress_Type = InetAddress
_FtpServerAddress_Object = MibScalar
ftpServerAddress = _FtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 3),
    _FtpServerAddress_Type()
)
ftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerAddress.setStatus("current")


class _FtpServerPort_Type(Integer32):
    """Custom type ftpServerPort based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FtpServerPort_Type.__name__ = "Integer32"
_FtpServerPort_Object = MibScalar
ftpServerPort = _FtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 4),
    _FtpServerPort_Type()
)
ftpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerPort.setStatus("current")


class _FtpUserName_Type(DisplayString):
    """Custom type ftpUserName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FtpUserName_Type.__name__ = "DisplayString"
_FtpUserName_Object = MibScalar
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 5),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("current")


class _FtpPassword_Type(DisplayString):
    """Custom type ftpPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FtpPassword_Type.__name__ = "DisplayString"
_FtpPassword_Object = MibScalar
ftpPassword = _FtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 6),
    _FtpPassword_Type()
)
ftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPassword.setStatus("current")


class _FtpFilename_Type(DisplayString):
    """Custom type ftpFilename based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FtpFilename_Type.__name__ = "DisplayString"
_FtpFilename_Object = MibScalar
ftpFilename = _FtpFilename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 7),
    _FtpFilename_Type()
)
ftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpFilename.setStatus("current")


class _FtpCommand_Type(Integer32):
    """Custom type ftpCommand based on Integer32"""
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


_FtpCommand_Type.__name__ = "Integer32"
_FtpCommand_Object = MibScalar
ftpCommand = _FtpCommand_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 8),
    _FtpCommand_Type()
)
ftpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpCommand.setStatus("current")


class _FtpTransferStatus_Type(Integer32):
    """Custom type ftpTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              150,
              200,
              221,
              226,
              230,
              331,
              421,
              530,
              550,
              600)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("fileStatusOk", 150),
          ("serviceReady", 200),
          ("sessionReady", 221),
          ("transferComplete", 226),
          ("passwordOk", 230),
          ("userNameOk", 331),
          ("serviceNotAvail", 421),
          ("invalidLogin", 530),
          ("fileNotFound", 550),
          ("socketConnectFailure", 600))
    )


_FtpTransferStatus_Type.__name__ = "Integer32"
_FtpTransferStatus_Object = MibScalar
ftpTransferStatus = _FtpTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 9),
    _FtpTransferStatus_Type()
)
ftpTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTransferStatus.setStatus("current")
_FtpTransferPayloadBytes_Type = Counter32
_FtpTransferPayloadBytes_Object = MibScalar
ftpTransferPayloadBytes = _FtpTransferPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 10),
    _FtpTransferPayloadBytes_Type()
)
ftpTransferPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTransferPayloadBytes.setStatus("current")
_FtpTransferTotalBytes_Type = Counter32
_FtpTransferTotalBytes_Object = MibScalar
ftpTransferTotalBytes = _FtpTransferTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 11),
    _FtpTransferTotalBytes_Type()
)
ftpTransferTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTransferTotalBytes.setStatus("current")
_FtpTransferElapsedTime_Type = Counter32
_FtpTransferElapsedTime_Object = MibScalar
ftpTransferElapsedTime = _FtpTransferElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 12),
    _FtpTransferElapsedTime_Type()
)
ftpTransferElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTransferElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    ftpTransferElapsedTime.setUnits("milliseconds")
_FtpTransferThroughput_Type = Unsigned32
_FtpTransferThroughput_Object = MibScalar
ftpTransferThroughput = _FtpTransferThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 12, 13),
    _FtpTransferThroughput_Type()
)
ftpTransferThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpTransferThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ftpTransferThroughput.setUnits("bits per second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-FTP-MGMT-MIB",
    **{"ftpMgmt": ftpMgmt,
       "ftpIpStackInterface": ftpIpStackInterface,
       "ftpServerAddressType": ftpServerAddressType,
       "ftpServerAddress": ftpServerAddress,
       "ftpServerPort": ftpServerPort,
       "ftpUserName": ftpUserName,
       "ftpPassword": ftpPassword,
       "ftpFilename": ftpFilename,
       "ftpCommand": ftpCommand,
       "ftpTransferStatus": ftpTransferStatus,
       "ftpTransferPayloadBytes": ftpTransferPayloadBytes,
       "ftpTransferTotalBytes": ftpTransferTotalBytes,
       "ftpTransferElapsedTime": ftpTransferElapsedTime,
       "ftpTransferThroughput": ftpTransferThroughput}
)
