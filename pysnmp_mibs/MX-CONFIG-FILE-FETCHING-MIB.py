# SNMP MIB module (MX-CONFIG-FILE-FETCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CONFIG-FILE-FETCHING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:40 2025
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

(MxEnableState,
 MxIpConfigSource,
 MxIpDhcpSiteSpecificCode,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
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

configFileFetchingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11)
)
if mibBuilder.loadTexts:
    configFileFetchingMIB.setRevisions(
        ("2010-12-15 00:00",
         "2006-03-06 00:00",
         "2005-04-25 00:00",
         "2004-04-27 00:00",
         "2004-03-10 00:00",
         "2004-02-12 00:00",
         "2003-11-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusConfigFileFetching_ObjectIdentity = ObjectIdentity
ipAddressStatusConfigFileFetching = _IpAddressStatusConfigFileFetching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 9)
)


class _ConfigFileFetchingConfigSource_Type(MxIpConfigSource):
    """Custom type configFileFetchingConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_ConfigFileFetchingConfigSource_Type.__name__ = "MxIpConfigSource"
_ConfigFileFetchingConfigSource_Object = MibScalar
configFileFetchingConfigSource = _ConfigFileFetchingConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 9, 50),
    _ConfigFileFetchingConfigSource_Type()
)
configFileFetchingConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileFetchingConfigSource.setStatus("current")


class _ConfigFileFetchingHost_Type(MxIpHostName):
    """Custom type configFileFetchingHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_ConfigFileFetchingHost_Type.__name__ = "MxIpHostName"
_ConfigFileFetchingHost_Object = MibScalar
configFileFetchingHost = _ConfigFileFetchingHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 9, 100),
    _ConfigFileFetchingHost_Type()
)
configFileFetchingHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileFetchingHost.setStatus("current")


class _ConfigFileFetchingPort_Type(MxIpPort):
    """Custom type configFileFetchingPort based on MxIpPort"""
    defaultValue = 69


_ConfigFileFetchingPort_Type.__name__ = "MxIpPort"
_ConfigFileFetchingPort_Object = MibScalar
configFileFetchingPort = _ConfigFileFetchingPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 9, 150),
    _ConfigFileFetchingPort_Type()
)
configFileFetchingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileFetchingPort.setStatus("current")
_IpAddressConfigFileFetching_ObjectIdentity = ObjectIdentity
ipAddressConfigFileFetching = _IpAddressConfigFileFetching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9)
)


class _ConfigFileFetchingSelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type configFileFetchingSelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_ConfigFileFetchingSelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_ConfigFileFetchingSelectConfigSource_Object = MibScalar
configFileFetchingSelectConfigSource = _ConfigFileFetchingSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9, 50),
    _ConfigFileFetchingSelectConfigSource_Type()
)
configFileFetchingSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingSelectConfigSource.setStatus("current")
_IpAddressConfigFileFetchingStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigFileFetchingStatic = _IpAddressConfigFileFetchingStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9, 100)
)


class _ConfigFileFetchingStaticHost_Type(MxIpHostName):
    """Custom type configFileFetchingStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_ConfigFileFetchingStaticHost_Type.__name__ = "MxIpHostName"
_ConfigFileFetchingStaticHost_Object = MibScalar
configFileFetchingStaticHost = _ConfigFileFetchingStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9, 100, 50),
    _ConfigFileFetchingStaticHost_Type()
)
configFileFetchingStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingStaticHost.setStatus("current")


class _ConfigFileFetchingStaticPort_Type(MxIpPort):
    """Custom type configFileFetchingStaticPort based on MxIpPort"""
    defaultValue = 69


_ConfigFileFetchingStaticPort_Type.__name__ = "MxIpPort"
_ConfigFileFetchingStaticPort_Object = MibScalar
configFileFetchingStaticPort = _ConfigFileFetchingStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9, 100, 100),
    _ConfigFileFetchingStaticPort_Type()
)
configFileFetchingStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingStaticPort.setStatus("current")
_IpAddressConfigFileFetchingDhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigFileFetchingDhcp = _IpAddressConfigFileFetchingDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9, 150)
)


class _ConfigFileFetchingDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type configFileFetchingDhcpSiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_ConfigFileFetchingDhcpSiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_ConfigFileFetchingDhcpSiteSpecificCode_Object = MibScalar
configFileFetchingDhcpSiteSpecificCode = _ConfigFileFetchingDhcpSiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 9, 150, 50),
    _ConfigFileFetchingDhcpSiteSpecificCode_Type()
)
configFileFetchingDhcpSiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingDhcpSiteSpecificCode.setStatus("current")
_ConfigFileFetchingMIBObjects_ObjectIdentity = ObjectIdentity
configFileFetchingMIBObjects = _ConfigFileFetchingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50)
)


class _ConfigFileFetchingFileName_Type(OctetString):
    """Custom type configFileFetchingFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigFileFetchingFileName_Type.__name__ = "OctetString"
_ConfigFileFetchingFileName_Object = MibScalar
configFileFetchingFileName = _ConfigFileFetchingFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 50),
    _ConfigFileFetchingFileName_Type()
)
configFileFetchingFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingFileName.setStatus("current")


class _ConfigFileFetchingSpecificFileName_Type(OctetString):
    """Custom type configFileFetchingSpecificFileName based on OctetString"""
    defaultValue = OctetString("%mac%.cfg")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigFileFetchingSpecificFileName_Type.__name__ = "OctetString"
_ConfigFileFetchingSpecificFileName_Object = MibScalar
configFileFetchingSpecificFileName = _ConfigFileFetchingSpecificFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 60),
    _ConfigFileFetchingSpecificFileName_Type()
)
configFileFetchingSpecificFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingSpecificFileName.setStatus("current")


class _ConfigFileFetchingFileLocation_Type(OctetString):
    """Custom type configFileFetchingFileLocation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigFileFetchingFileLocation_Type.__name__ = "OctetString"
_ConfigFileFetchingFileLocation_Object = MibScalar
configFileFetchingFileLocation = _ConfigFileFetchingFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 100),
    _ConfigFileFetchingFileLocation_Type()
)
configFileFetchingFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileFetchingFileLocation.setStatus("current")
_ConfigFileTransfer_ObjectIdentity = ObjectIdentity
configFileTransfer = _ConfigFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 150)
)


class _ConfigFileTransferProtocol_Type(Integer32):
    """Custom type configFileTransferProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 0),
          ("http", 1),
          ("https", 2))
    )


_ConfigFileTransferProtocol_Type.__name__ = "Integer32"
_ConfigFileTransferProtocol_Object = MibScalar
configFileTransferProtocol = _ConfigFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 150, 50),
    _ConfigFileTransferProtocol_Type()
)
configFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileTransferProtocol.setStatus("current")


class _ConfigFileTransferUsername_Type(OctetString):
    """Custom type configFileTransferUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigFileTransferUsername_Type.__name__ = "OctetString"
_ConfigFileTransferUsername_Object = MibScalar
configFileTransferUsername = _ConfigFileTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 150, 100),
    _ConfigFileTransferUsername_Type()
)
configFileTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileTransferUsername.setStatus("current")


class _ConfigFileTransferPassword_Type(OctetString):
    """Custom type configFileTransferPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigFileTransferPassword_Type.__name__ = "OctetString"
_ConfigFileTransferPassword_Object = MibScalar
configFileTransferPassword = _ConfigFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 150, 150),
    _ConfigFileTransferPassword_Type()
)
configFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileTransferPassword.setStatus("current")
_ConfigFileAutomaticUpdate_ObjectIdentity = ObjectIdentity
configFileAutomaticUpdate = _ConfigFileAutomaticUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200)
)


class _ConfigFileAutoUpdateOnRestartEnable_Type(MxEnableState):
    """Custom type configFileAutoUpdateOnRestartEnable based on MxEnableState"""
    defaultValue = 1


_ConfigFileAutoUpdateOnRestartEnable_Type.__name__ = "MxEnableState"
_ConfigFileAutoUpdateOnRestartEnable_Object = MibScalar
configFileAutoUpdateOnRestartEnable = _ConfigFileAutoUpdateOnRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200, 50),
    _ConfigFileAutoUpdateOnRestartEnable_Type()
)
configFileAutoUpdateOnRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAutoUpdateOnRestartEnable.setStatus("current")


class _ConfigFileAutoUpdatePeriodicEnable_Type(MxEnableState):
    """Custom type configFileAutoUpdatePeriodicEnable based on MxEnableState"""
    defaultValue = 0


_ConfigFileAutoUpdatePeriodicEnable_Type.__name__ = "MxEnableState"
_ConfigFileAutoUpdatePeriodicEnable_Object = MibScalar
configFileAutoUpdatePeriodicEnable = _ConfigFileAutoUpdatePeriodicEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200, 100),
    _ConfigFileAutoUpdatePeriodicEnable_Type()
)
configFileAutoUpdatePeriodicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAutoUpdatePeriodicEnable.setStatus("current")


class _ConfigFileAutoUpdateTimeUnit_Type(Integer32):
    """Custom type configFileAutoUpdateTimeUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              20)
        )
    )
    namedValues = NamedValues(
        *(("hours", 0),
          ("days", 1),
          ("minutes", 20))
    )


_ConfigFileAutoUpdateTimeUnit_Type.__name__ = "Integer32"
_ConfigFileAutoUpdateTimeUnit_Object = MibScalar
configFileAutoUpdateTimeUnit = _ConfigFileAutoUpdateTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200, 150),
    _ConfigFileAutoUpdateTimeUnit_Type()
)
configFileAutoUpdateTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAutoUpdateTimeUnit.setStatus("current")


class _ConfigFileAutoUpdatePeriod_Type(Unsigned32):
    """Custom type configFileAutoUpdatePeriod based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ConfigFileAutoUpdatePeriod_Type.__name__ = "Unsigned32"
_ConfigFileAutoUpdatePeriod_Object = MibScalar
configFileAutoUpdatePeriod = _ConfigFileAutoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200, 200),
    _ConfigFileAutoUpdatePeriod_Type()
)
configFileAutoUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAutoUpdatePeriod.setStatus("current")


class _ConfigFileAutoUpdateTimeOfDay_Type(Integer32):
    """Custom type configFileAutoUpdateTimeOfDay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 23),
    )


_ConfigFileAutoUpdateTimeOfDay_Type.__name__ = "Integer32"
_ConfigFileAutoUpdateTimeOfDay_Object = MibScalar
configFileAutoUpdateTimeOfDay = _ConfigFileAutoUpdateTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200, 250),
    _ConfigFileAutoUpdateTimeOfDay_Type()
)
configFileAutoUpdateTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAutoUpdateTimeOfDay.setStatus("deprecated")


class _ConfigFileAutoUpdateTimeRange_Type(OctetString):
    """Custom type configFileAutoUpdateTimeRange based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ConfigFileAutoUpdateTimeRange_Type.__name__ = "OctetString"
_ConfigFileAutoUpdateTimeRange_Object = MibScalar
configFileAutoUpdateTimeRange = _ConfigFileAutoUpdateTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 200, 300),
    _ConfigFileAutoUpdateTimeRange_Type()
)
configFileAutoUpdateTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAutoUpdateTimeRange.setStatus("current")
_ConfigFilePrivacy_ObjectIdentity = ObjectIdentity
configFilePrivacy = _ConfigFilePrivacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 250)
)


class _ConfigFilePrivacyEnable_Type(MxEnableState):
    """Custom type configFilePrivacyEnable based on MxEnableState"""
    defaultValue = 0


_ConfigFilePrivacyEnable_Type.__name__ = "MxEnableState"
_ConfigFilePrivacyEnable_Object = MibScalar
configFilePrivacyEnable = _ConfigFilePrivacyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 250, 50),
    _ConfigFilePrivacyEnable_Type()
)
configFilePrivacyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilePrivacyEnable.setStatus("current")


class _ConfigFilePrivacyGenericSecret_Type(OctetString):
    """Custom type configFilePrivacyGenericSecret based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ConfigFilePrivacyGenericSecret_Type.__name__ = "OctetString"
_ConfigFilePrivacyGenericSecret_Object = MibScalar
configFilePrivacyGenericSecret = _ConfigFilePrivacyGenericSecret_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 250, 100),
    _ConfigFilePrivacyGenericSecret_Type()
)
configFilePrivacyGenericSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilePrivacyGenericSecret.setStatus("current")


class _ConfigFilePrivacySpecificSecret_Type(OctetString):
    """Custom type configFilePrivacySpecificSecret based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ConfigFilePrivacySpecificSecret_Type.__name__ = "OctetString"
_ConfigFilePrivacySpecificSecret_Object = MibScalar
configFilePrivacySpecificSecret = _ConfigFilePrivacySpecificSecret_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 50, 250, 150),
    _ConfigFilePrivacySpecificSecret_Type()
)
configFilePrivacySpecificSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilePrivacySpecificSecret.setStatus("current")
_ConfigFileFetchingConformance_ObjectIdentity = ObjectIdentity
configFileFetchingConformance = _ConfigFileFetchingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100)
)
_ConfigFileFetchingCompliances_ObjectIdentity = ObjectIdentity
configFileFetchingCompliances = _ConfigFileFetchingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 50)
)
_ConfigFileFetchingGroups_ObjectIdentity = ObjectIdentity
configFileFetchingGroups = _ConfigFileFetchingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 100)
)

# Managed Objects groups

configFileFetchingBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 100, 50)
)
configFileFetchingBasicGroupVer1.setObjects(
      *(("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingFileName"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingSpecificFileName"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingFileLocation"))
)
if mibBuilder.loadTexts:
    configFileFetchingBasicGroupVer1.setStatus("current")

configFileTransferGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 100, 65)
)
configFileTransferGroupVer1.setObjects(
      *(("MX-CONFIG-FILE-FETCHING-MIB", "configFileTransferProtocol"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileTransferUsername"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileTransferPassword"))
)
if mibBuilder.loadTexts:
    configFileTransferGroupVer1.setStatus("current")

configFileAutomaticUpdateGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 100, 85)
)
configFileAutomaticUpdateGroupVer1.setObjects(
      *(("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutoUpdateOnRestartEnable"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutoUpdatePeriodicEnable"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutoUpdateTimeUnit"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutoUpdatePeriod"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutoUpdateTimeOfDay"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutoUpdateTimeRange"))
)
if mibBuilder.loadTexts:
    configFileAutomaticUpdateGroupVer1.setStatus("current")

configFileFetchingTransferServerGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 100, 100)
)
configFileFetchingTransferServerGroupVer1.setObjects(
      *(("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingConfigSource"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingHost"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingPort"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingSelectConfigSource"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingStaticHost"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingStaticPort"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingDhcpSiteSpecificCode"))
)
if mibBuilder.loadTexts:
    configFileFetchingTransferServerGroupVer1.setStatus("current")

configFilePrivacyGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 100, 105)
)
configFilePrivacyGroupVer1.setObjects(
      *(("MX-CONFIG-FILE-FETCHING-MIB", "configFilePrivacyEnable"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFilePrivacyGenericSecret"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFilePrivacySpecificSecret"))
)
if mibBuilder.loadTexts:
    configFilePrivacyGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

configFileFetchingBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 11, 100, 50, 50)
)
configFileFetchingBasicComplVer1.setObjects(
      *(("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingBasicGroupVer1"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileTransferGroupVer1"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileAutomaticUpdateGroupVer1"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFilePrivacyGroupVer1"),
        ("MX-CONFIG-FILE-FETCHING-MIB", "configFileFetchingTransferServerGroupVer1"))
)
if mibBuilder.loadTexts:
    configFileFetchingBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-CONFIG-FILE-FETCHING-MIB",
    **{"ipAddressStatusConfigFileFetching": ipAddressStatusConfigFileFetching,
       "configFileFetchingConfigSource": configFileFetchingConfigSource,
       "configFileFetchingHost": configFileFetchingHost,
       "configFileFetchingPort": configFileFetchingPort,
       "ipAddressConfigFileFetching": ipAddressConfigFileFetching,
       "configFileFetchingSelectConfigSource": configFileFetchingSelectConfigSource,
       "ipAddressConfigFileFetchingStatic": ipAddressConfigFileFetchingStatic,
       "configFileFetchingStaticHost": configFileFetchingStaticHost,
       "configFileFetchingStaticPort": configFileFetchingStaticPort,
       "ipAddressConfigFileFetchingDhcp": ipAddressConfigFileFetchingDhcp,
       "configFileFetchingDhcpSiteSpecificCode": configFileFetchingDhcpSiteSpecificCode,
       "configFileFetchingMIB": configFileFetchingMIB,
       "configFileFetchingMIBObjects": configFileFetchingMIBObjects,
       "configFileFetchingFileName": configFileFetchingFileName,
       "configFileFetchingSpecificFileName": configFileFetchingSpecificFileName,
       "configFileFetchingFileLocation": configFileFetchingFileLocation,
       "configFileTransfer": configFileTransfer,
       "configFileTransferProtocol": configFileTransferProtocol,
       "configFileTransferUsername": configFileTransferUsername,
       "configFileTransferPassword": configFileTransferPassword,
       "configFileAutomaticUpdate": configFileAutomaticUpdate,
       "configFileAutoUpdateOnRestartEnable": configFileAutoUpdateOnRestartEnable,
       "configFileAutoUpdatePeriodicEnable": configFileAutoUpdatePeriodicEnable,
       "configFileAutoUpdateTimeUnit": configFileAutoUpdateTimeUnit,
       "configFileAutoUpdatePeriod": configFileAutoUpdatePeriod,
       "configFileAutoUpdateTimeOfDay": configFileAutoUpdateTimeOfDay,
       "configFileAutoUpdateTimeRange": configFileAutoUpdateTimeRange,
       "configFilePrivacy": configFilePrivacy,
       "configFilePrivacyEnable": configFilePrivacyEnable,
       "configFilePrivacyGenericSecret": configFilePrivacyGenericSecret,
       "configFilePrivacySpecificSecret": configFilePrivacySpecificSecret,
       "configFileFetchingConformance": configFileFetchingConformance,
       "configFileFetchingCompliances": configFileFetchingCompliances,
       "configFileFetchingBasicComplVer1": configFileFetchingBasicComplVer1,
       "configFileFetchingGroups": configFileFetchingGroups,
       "configFileFetchingBasicGroupVer1": configFileFetchingBasicGroupVer1,
       "configFileTransferGroupVer1": configFileTransferGroupVer1,
       "configFileAutomaticUpdateGroupVer1": configFileAutomaticUpdateGroupVer1,
       "configFileFetchingTransferServerGroupVer1": configFileFetchingTransferServerGroupVer1,
       "configFilePrivacyGroupVer1": configFilePrivacyGroupVer1}
)
