# SNMP MIB module (MX-MS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-MS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:36 2025
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

(ipAddressConfig,
 ipAddressStatus,
 mediatrixConfig) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixConfig")

(sysConfigDownloadConfigFile,
 sysConfigDownloadConfigMode) = mibBuilder.importSymbols(
    "MX-SYSTEM-CONFIG-MIB",
    "sysConfigDownloadConfigFile",
    "sysConfigDownloadConfigMode")

(sysMacAddress,) = mibBuilder.importSymbols(
    "MX-SYSTEM-MGMT-MIB",
    "sysMacAddress")

(MxIpConfigSource,
 MxIpDhcpSiteSpecificCode,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxIpConfigSource",
    "MxIpDhcpSiteSpecificCode",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSelectConfigSource")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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

msMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15)
)
if mibBuilder.loadTexts:
    msMIB.setRevisions(
        ("2004-05-25 00:00",
         "1903-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusMs_ObjectIdentity = ObjectIdentity
ipAddressStatusMs = _IpAddressStatusMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 10)
)


class _MsConfigSource_Type(MxIpConfigSource):
    """Custom type msConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_MsConfigSource_Type.__name__ = "MxIpConfigSource"
_MsConfigSource_Object = MibScalar
msConfigSource = _MsConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 10, 1),
    _MsConfigSource_Type()
)
msConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msConfigSource.setStatus("current")


class _MsHost_Type(MxIpHostName):
    """Custom type msHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_MsHost_Type.__name__ = "MxIpHostName"
_MsHost_Object = MibScalar
msHost = _MsHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 10, 2),
    _MsHost_Type()
)
msHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msHost.setStatus("current")


class _MsTrapPort_Type(MxIpPort):
    """Custom type msTrapPort based on MxIpPort"""
    defaultValue = 162


_MsTrapPort_Type.__name__ = "MxIpPort"
_MsTrapPort_Object = MibScalar
msTrapPort = _MsTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 10, 3),
    _MsTrapPort_Type()
)
msTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTrapPort.setStatus("current")
_IpAddressConfigMs_ObjectIdentity = ObjectIdentity
ipAddressConfigMs = _IpAddressConfigMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10)
)


class _MsSelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type msSelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_MsSelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_MsSelectConfigSource_Object = MibScalar
msSelectConfigSource = _MsSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10, 1),
    _MsSelectConfigSource_Type()
)
msSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSelectConfigSource.setStatus("current")
_IpAddressConfigMsStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigMsStatic = _IpAddressConfigMsStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10, 10)
)


class _MsStaticHost_Type(MxIpHostName):
    """Custom type msStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_MsStaticHost_Type.__name__ = "MxIpHostName"
_MsStaticHost_Object = MibScalar
msStaticHost = _MsStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10, 10, 1),
    _MsStaticHost_Type()
)
msStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msStaticHost.setStatus("current")


class _MsStaticTrapPort_Type(MxIpPort):
    """Custom type msStaticTrapPort based on MxIpPort"""
    defaultValue = 162


_MsStaticTrapPort_Type.__name__ = "MxIpPort"
_MsStaticTrapPort_Object = MibScalar
msStaticTrapPort = _MsStaticTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10, 10, 2),
    _MsStaticTrapPort_Type()
)
msStaticTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msStaticTrapPort.setStatus("current")
_IpAddressConfigMsDhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigMsDhcp = _IpAddressConfigMsDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10, 30)
)


class _MsDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type msDhcpSiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_MsDhcpSiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_MsDhcpSiteSpecificCode_Object = MibScalar
msDhcpSiteSpecificCode = _MsDhcpSiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 10, 30, 1),
    _MsDhcpSiteSpecificCode_Type()
)
msDhcpSiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msDhcpSiteSpecificCode.setStatus("current")
_MsMIBObjects_ObjectIdentity = ObjectIdentity
msMIBObjects = _MsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 1)
)


class _MsEnable_Type(Integer32):
    """Custom type msEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsEnable_Type.__name__ = "Integer32"
_MsEnable_Object = MibScalar
msEnable = _MsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 1, 5),
    _MsEnable_Type()
)
msEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msEnable.setStatus("current")


class _MsTrapRetransmissionPeriod_Type(Unsigned32):
    """Custom type msTrapRetransmissionPeriod based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 604800000),
    )


_MsTrapRetransmissionPeriod_Type.__name__ = "Unsigned32"
_MsTrapRetransmissionPeriod_Object = MibScalar
msTrapRetransmissionPeriod = _MsTrapRetransmissionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 1, 20),
    _MsTrapRetransmissionPeriod_Type()
)
msTrapRetransmissionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTrapRetransmissionPeriod.setStatus("current")


class _MsTrapRetransmissionRetryCount_Type(Integer32):
    """Custom type msTrapRetransmissionRetryCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MsTrapRetransmissionRetryCount_Type.__name__ = "Integer32"
_MsTrapRetransmissionRetryCount_Object = MibScalar
msTrapRetransmissionRetryCount = _MsTrapRetransmissionRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 1, 21),
    _MsTrapRetransmissionRetryCount_Type()
)
msTrapRetransmissionRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTrapRetransmissionRetryCount.setStatus("current")
_MsConformance_ObjectIdentity = ObjectIdentity
msConformance = _MsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2)
)
_MsCompliances_ObjectIdentity = ObjectIdentity
msCompliances = _MsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2, 1)
)
_MsGroups_ObjectIdentity = ObjectIdentity
msGroups = _MsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2, 2)
)
_MsEvents_ObjectIdentity = ObjectIdentity
msEvents = _MsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 3)
)
_MsNotifications_ObjectIdentity = ObjectIdentity
msNotifications = _MsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 3, 2)
)

# Managed Objects groups

msBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2, 2, 1)
)
msBasicGroupVer1.setObjects(
      *(("MX-MS-MIB", "msEnable"),
        ("MX-MS-MIB", "msTrapRetransmissionPeriod"),
        ("MX-MS-MIB", "msTrapRetransmissionRetryCount"))
)
if mibBuilder.loadTexts:
    msBasicGroupVer1.setStatus("current")

msServerGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2, 2, 2)
)
msServerGroupVer1.setObjects(
      *(("MX-MS-MIB", "msConfigSource"),
        ("MX-MS-MIB", "msHost"),
        ("MX-MS-MIB", "msTrapPort"),
        ("MX-MS-MIB", "msSelectConfigSource"),
        ("MX-MS-MIB", "msStaticHost"),
        ("MX-MS-MIB", "msStaticTrapPort"),
        ("MX-MS-MIB", "msDhcpSiteSpecificCode"))
)
if mibBuilder.loadTexts:
    msServerGroupVer1.setStatus("current")


# Notification objects

msTrapConfigInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 3, 2, 700)
)
msTrapConfigInformation.setObjects(
      *(("SNMPv2-MIB", "sysObjectID"),
        ("MX-SYSTEM-MGMT-MIB", "sysMacAddress"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDownloadConfigFile"))
)
if mibBuilder.loadTexts:
    msTrapConfigInformation.setStatus(
        "current"
    )

msTrapStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 3, 2, 800)
)
msTrapStatusInformation.setObjects(
      *(("MX-SYSTEM-MGMT-MIB", "sysMacAddress"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDownloadConfigMode"))
)
if mibBuilder.loadTexts:
    msTrapStatusInformation.setStatus(
        "current"
    )

msTrapStatusConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 3, 2, 900)
)
msTrapStatusConfigFile.setObjects(
      *(("MX-SYSTEM-MGMT-MIB", "sysMacAddress"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDownloadConfigFile"))
)
if mibBuilder.loadTexts:
    msTrapStatusConfigFile.setStatus(
        "current"
    )


# Notifications groups

msBasicNotificationGroupVer1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2, 2, 3)
)
msBasicNotificationGroupVer1.setObjects(
      *(("MX-MS-MIB", "msTrapConfigInformation"),
        ("MX-MS-MIB", "msTrapStatusInformation"),
        ("MX-MS-MIB", "msTrapStatusConfigFile"))
)
if mibBuilder.loadTexts:
    msBasicNotificationGroupVer1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

msBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 15, 2, 1, 1)
)
msBasicComplVer1.setObjects(
      *(("MX-MS-MIB", "msBasicGroupVer1"),
        ("MX-MS-MIB", "msServerGroupVer1"),
        ("MX-MS-MIB", "msBasicNotificationGroupVer1"))
)
if mibBuilder.loadTexts:
    msBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-MS-MIB",
    **{"ipAddressStatusMs": ipAddressStatusMs,
       "msConfigSource": msConfigSource,
       "msHost": msHost,
       "msTrapPort": msTrapPort,
       "ipAddressConfigMs": ipAddressConfigMs,
       "msSelectConfigSource": msSelectConfigSource,
       "ipAddressConfigMsStatic": ipAddressConfigMsStatic,
       "msStaticHost": msStaticHost,
       "msStaticTrapPort": msStaticTrapPort,
       "ipAddressConfigMsDhcp": ipAddressConfigMsDhcp,
       "msDhcpSiteSpecificCode": msDhcpSiteSpecificCode,
       "msMIB": msMIB,
       "msMIBObjects": msMIBObjects,
       "msEnable": msEnable,
       "msTrapRetransmissionPeriod": msTrapRetransmissionPeriod,
       "msTrapRetransmissionRetryCount": msTrapRetransmissionRetryCount,
       "msConformance": msConformance,
       "msCompliances": msCompliances,
       "msBasicComplVer1": msBasicComplVer1,
       "msGroups": msGroups,
       "msBasicGroupVer1": msBasicGroupVer1,
       "msServerGroupVer1": msServerGroupVer1,
       "msBasicNotificationGroupVer1": msBasicNotificationGroupVer1,
       "msEvents": msEvents,
       "msNotifications": msNotifications,
       "msTrapConfigInformation": msTrapConfigInformation,
       "msTrapStatusInformation": msTrapStatusInformation,
       "msTrapStatusConfigFile": msTrapStatusConfigFile}
)
