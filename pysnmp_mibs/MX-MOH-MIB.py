# SNMP MIB module (MX-MOH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-MOH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:47 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mohMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MohMIBObjects_ObjectIdentity = ObjectIdentity
mohMIBObjects = _MohMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1)
)


class _FileUrl_Type(OctetString):
    """Custom type fileUrl based on OctetString"""
    defaultValue = OctetString("")


_FileUrl_Type.__name__ = "OctetString"
_FileUrl_Object = MibScalar
fileUrl = _FileUrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 100),
    _FileUrl_Type()
)
fileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileUrl.setStatus("current")


class _Username_Type(OctetString):
    """Custom type username based on OctetString"""
    defaultValue = OctetString("")


_Username_Type.__name__ = "OctetString"
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 200),
    _Username_Type()
)
username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _Password_Type(OctetString):
    """Custom type password based on OctetString"""
    defaultValue = OctetString("")


_Password_Type.__name__ = "OctetString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 300),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")


class _ReloadInterval_Type(Unsigned32):
    """Custom type reloadInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_ReloadInterval_Type.__name__ = "Unsigned32"
_ReloadInterval_Object = MibScalar
reloadInterval = _ReloadInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 400),
    _ReloadInterval_Type()
)
reloadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reloadInterval.setStatus("current")


class _FileStatus_Type(Integer32):
    """Custom type fileStatus based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("noFile", 100),
          ("fileReady", 200),
          ("downloading", 300),
          ("invalidFormat", 400),
          ("fileTooLarge", 500))
    )


_FileStatus_Type.__name__ = "Integer32"
_FileStatus_Object = MibScalar
fileStatus = _FileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 500),
    _FileStatus_Type()
)
fileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileStatus.setStatus("current")


class _LastTransferStatus_Type(Integer32):
    """Custom type lastTransferStatus based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("success", 100),
          ("failed", 200))
    )


_LastTransferStatus_Type.__name__ = "Integer32"
_LastTransferStatus_Object = MibScalar
lastTransferStatus = _LastTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 600),
    _LastTransferStatus_Type()
)
lastTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTransferStatus.setStatus("current")


class _LastTransferDateTime_Type(OctetString):
    """Custom type lastTransferDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LastTransferDateTime_Type.__name__ = "OctetString"
_LastTransferDateTime_Object = MibScalar
lastTransferDateTime = _LastTransferDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 700),
    _LastTransferDateTime_Type()
)
lastTransferDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTransferDateTime.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1550, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-MOH-MIB",
    **{"mohMIB": mohMIB,
       "mohMIBObjects": mohMIBObjects,
       "fileUrl": fileUrl,
       "username": username,
       "password": password,
       "reloadInterval": reloadInterval,
       "fileStatus": fileStatus,
       "lastTransferStatus": lastTransferStatus,
       "lastTransferDateTime": lastTransferDateTime,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
