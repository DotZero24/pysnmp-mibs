# SNMP MIB module (MX-HOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-HOC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:55 2025
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

hocMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HocMIBObjects_ObjectIdentity = ObjectIdentity
hocMIBObjects = _HocMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1)
)


class _ManagementInterface_Type(OctetString):
    """Custom type managementInterface based on OctetString"""
    defaultValue = OctetString("Lan1")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ManagementInterface_Type.__name__ = "OctetString"
_ManagementInterface_Object = MibScalar
managementInterface = _ManagementInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 100),
    _ManagementInterface_Type()
)
managementInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementInterface.setStatus("current")


class _AutomaticConfigurationInterface_Type(OctetString):
    """Custom type automaticConfigurationInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AutomaticConfigurationInterface_Type.__name__ = "OctetString"
_AutomaticConfigurationInterface_Object = MibScalar
automaticConfigurationInterface = _AutomaticConfigurationInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 150),
    _AutomaticConfigurationInterface_Type()
)
automaticConfigurationInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automaticConfigurationInterface.setStatus("current")


class _Ipv6AutomaticConfigurationInterface_Type(OctetString):
    """Custom type ipv6AutomaticConfigurationInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Ipv6AutomaticConfigurationInterface_Type.__name__ = "OctetString"
_Ipv6AutomaticConfigurationInterface_Object = MibScalar
ipv6AutomaticConfigurationInterface = _Ipv6AutomaticConfigurationInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 175),
    _Ipv6AutomaticConfigurationInterface_Type()
)
ipv6AutomaticConfigurationInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6AutomaticConfigurationInterface.setStatus("current")


class _HostName_Type(MxIpHostName):
    """Custom type hostName based on MxIpHostName"""
    defaultValue = OctetString("")


_HostName_Type.__name__ = "MxIpHostName"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 200),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_TimeGroup_ObjectIdentity = ObjectIdentity
timeGroup = _TimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 250)
)
_SystemTime_Type = OctetString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 250, 100),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemUptime_Type = OctetString
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 250, 150),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")


class _StaticTimeZone_Type(OctetString):
    """Custom type staticTimeZone based on OctetString"""
    defaultValue = OctetString("EST5EDT4,M3.2.0/02:00:00,M11.1.0/02:00:00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StaticTimeZone_Type.__name__ = "OctetString"
_StaticTimeZone_Object = MibScalar
staticTimeZone = _StaticTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 250, 200),
    _StaticTimeZone_Type()
)
staticTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticTimeZone.setStatus("current")
_DomainNameGroup_ObjectIdentity = ObjectIdentity
domainNameGroup = _DomainNameGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 300)
)


class _DomainNameConfigSource_Type(Integer32):
    """Custom type domainNameConfigSource based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 100),
          ("automaticIpv6", 150),
          ("static", 200))
    )


_DomainNameConfigSource_Type.__name__ = "Integer32"
_DomainNameConfigSource_Object = MibScalar
domainNameConfigSource = _DomainNameConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 300, 100),
    _DomainNameConfigSource_Type()
)
domainNameConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainNameConfigSource.setStatus("current")
_DomainNameInfo_Type = MxIpHostName
_DomainNameInfo_Object = MibScalar
domainNameInfo = _DomainNameInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 300, 200),
    _DomainNameInfo_Type()
)
domainNameInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainNameInfo.setStatus("current")


class _StaticDomainName_Type(MxIpHostName):
    """Custom type staticDomainName based on MxIpHostName"""
    defaultValue = OctetString("")


_StaticDomainName_Type.__name__ = "MxIpHostName"
_StaticDomainName_Object = MibScalar
staticDomainName = _StaticDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 300, 300),
    _StaticDomainName_Type()
)
staticDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDomainName.setStatus("current")
_SntpGroup_ObjectIdentity = ObjectIdentity
sntpGroup = _SntpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400)
)


class _SntpConfigSource_Type(Integer32):
    """Custom type sntpConfigSource based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              150,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 100),
          ("automaticIpv6", 150),
          ("static", 200),
          ("automaticWithFallback", 300))
    )


_SntpConfigSource_Type.__name__ = "Integer32"
_SntpConfigSource_Object = MibScalar
sntpConfigSource = _SntpConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 100),
    _SntpConfigSource_Type()
)
sntpConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpConfigSource.setStatus("current")


class _SntpSynchronizationPeriod_Type(Unsigned32):
    """Custom type sntpSynchronizationPeriod based on Unsigned32"""
    defaultValue = 1440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SntpSynchronizationPeriod_Type.__name__ = "Unsigned32"
_SntpSynchronizationPeriod_Object = MibScalar
sntpSynchronizationPeriod = _SntpSynchronizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 200),
    _SntpSynchronizationPeriod_Type()
)
sntpSynchronizationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSynchronizationPeriod.setStatus("current")


class _SntpSynchronizationPeriodOnError_Type(Unsigned32):
    """Custom type sntpSynchronizationPeriodOnError based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SntpSynchronizationPeriodOnError_Type.__name__ = "Unsigned32"
_SntpSynchronizationPeriodOnError_Object = MibScalar
sntpSynchronizationPeriodOnError = _SntpSynchronizationPeriodOnError_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 300),
    _SntpSynchronizationPeriodOnError_Type()
)
sntpSynchronizationPeriodOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSynchronizationPeriodOnError.setStatus("current")


class _SntpTimeZone_Type(OctetString):
    """Custom type sntpTimeZone based on OctetString"""
    defaultValue = OctetString("EST5EDT4,M3.2.0/02:00:00,M11.1.0/02:00:00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SntpTimeZone_Type.__name__ = "OctetString"
_SntpTimeZone_Object = MibScalar
sntpTimeZone = _SntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 400),
    _SntpTimeZone_Type()
)
sntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeZone.setStatus("obsolete")
_SntpServerHostInfo_Type = MxIpHostNamePort
_SntpServerHostInfo_Object = MibScalar
sntpServerHostInfo = _SntpServerHostInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 500),
    _SntpServerHostInfo_Type()
)
sntpServerHostInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerHostInfo.setStatus("obsolete")


class _StaticSntpServerHost_Type(MxIpHostNamePort):
    """Custom type staticSntpServerHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.10.10:123")


_StaticSntpServerHost_Type.__name__ = "MxIpHostNamePort"
_StaticSntpServerHost_Object = MibScalar
staticSntpServerHost = _StaticSntpServerHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 700),
    _StaticSntpServerHost_Type()
)
staticSntpServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticSntpServerHost.setStatus("obsolete")
_SntpCurrentSource_Type = MxIpHostNamePort
_SntpCurrentSource_Object = MibScalar
sntpCurrentSource = _SntpCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 750),
    _SntpCurrentSource_Type()
)
sntpCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpCurrentSource.setStatus("current")
_SntpServersInfoTable_Object = MibTable
sntpServersInfoTable = _SntpServersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 800)
)
if mibBuilder.loadTexts:
    sntpServersInfoTable.setStatus("current")
_SntpServersInfoEntry_Object = MibTableRow
sntpServersInfoEntry = _SntpServersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 800, 1)
)
sntpServersInfoEntry.setIndexNames(
    (0, "MX-HOC-MIB", "sntpServersInfoPriority"),
)
if mibBuilder.loadTexts:
    sntpServersInfoEntry.setStatus("current")


class _SntpServersInfoPriority_Type(Unsigned32):
    """Custom type sntpServersInfoPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SntpServersInfoPriority_Type.__name__ = "Unsigned32"
_SntpServersInfoPriority_Object = MibTableColumn
sntpServersInfoPriority = _SntpServersInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 800, 1, 100),
    _SntpServersInfoPriority_Type()
)
sntpServersInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServersInfoPriority.setStatus("current")


class _SntpServersInfoHostName_Type(MxIpHostNamePort):
    """Custom type sntpServersInfoHostName based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_SntpServersInfoHostName_Type.__name__ = "MxIpHostNamePort"
_SntpServersInfoHostName_Object = MibTableColumn
sntpServersInfoHostName = _SntpServersInfoHostName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 800, 1, 200),
    _SntpServersInfoHostName_Type()
)
sntpServersInfoHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServersInfoHostName.setStatus("current")
_StaticSntpServersTable_Object = MibTable
staticSntpServersTable = _StaticSntpServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 900)
)
if mibBuilder.loadTexts:
    staticSntpServersTable.setStatus("current")
_StaticSntpServersEntry_Object = MibTableRow
staticSntpServersEntry = _StaticSntpServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 900, 1)
)
staticSntpServersEntry.setIndexNames(
    (0, "MX-HOC-MIB", "staticSntpServersPriority"),
)
if mibBuilder.loadTexts:
    staticSntpServersEntry.setStatus("current")


class _StaticSntpServersPriority_Type(Unsigned32):
    """Custom type staticSntpServersPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StaticSntpServersPriority_Type.__name__ = "Unsigned32"
_StaticSntpServersPriority_Object = MibTableColumn
staticSntpServersPriority = _StaticSntpServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 900, 1, 100),
    _StaticSntpServersPriority_Type()
)
staticSntpServersPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticSntpServersPriority.setStatus("current")


class _StaticSntpServersHostName_Type(MxIpHostNamePort):
    """Custom type staticSntpServersHostName based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_StaticSntpServersHostName_Type.__name__ = "MxIpHostNamePort"
_StaticSntpServersHostName_Object = MibTableColumn
staticSntpServersHostName = _StaticSntpServersHostName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 400, 900, 1, 200),
    _StaticSntpServersHostName_Type()
)
staticSntpServersHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticSntpServersHostName.setStatus("current")
_DefaultRouterGroup_ObjectIdentity = ObjectIdentity
defaultRouterGroup = _DefaultRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500)
)


class _DefaultRouterConfigSource_Type(Integer32):
    """Custom type defaultRouterConfigSource based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 100),
          ("static", 200))
    )


_DefaultRouterConfigSource_Type.__name__ = "Integer32"
_DefaultRouterConfigSource_Object = MibScalar
defaultRouterConfigSource = _DefaultRouterConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500, 100),
    _DefaultRouterConfigSource_Type()
)
defaultRouterConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRouterConfigSource.setStatus("current")


class _DefaultIpv6RouterConfigSource_Type(Integer32):
    """Custom type defaultIpv6RouterConfigSource based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("automaticIpv6", 150),
          ("static", 200))
    )


_DefaultIpv6RouterConfigSource_Type.__name__ = "Integer32"
_DefaultIpv6RouterConfigSource_Object = MibScalar
defaultIpv6RouterConfigSource = _DefaultIpv6RouterConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500, 150),
    _DefaultIpv6RouterConfigSource_Type()
)
defaultIpv6RouterConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultIpv6RouterConfigSource.setStatus("current")
_DefaultRouterInfo_Type = MxIpAddr
_DefaultRouterInfo_Object = MibScalar
defaultRouterInfo = _DefaultRouterInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500, 200),
    _DefaultRouterInfo_Type()
)
defaultRouterInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultRouterInfo.setStatus("current")
_DefaultIpv6RouterInfo_Type = MxIpAddress
_DefaultIpv6RouterInfo_Object = MibScalar
defaultIpv6RouterInfo = _DefaultIpv6RouterInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500, 250),
    _DefaultIpv6RouterInfo_Type()
)
defaultIpv6RouterInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultIpv6RouterInfo.setStatus("current")


class _StaticDefaultRouter_Type(MxIpAddr):
    """Custom type staticDefaultRouter based on MxIpAddr"""
    defaultValue = OctetString("192.168.10.10")


_StaticDefaultRouter_Type.__name__ = "MxIpAddr"
_StaticDefaultRouter_Object = MibScalar
staticDefaultRouter = _StaticDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500, 300),
    _StaticDefaultRouter_Type()
)
staticDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDefaultRouter.setStatus("current")


class _StaticDefaultIpv6Router_Type(MxIpAddress):
    """Custom type staticDefaultIpv6Router based on MxIpAddress"""
    defaultValue = OctetString("")


_StaticDefaultIpv6Router_Type.__name__ = "MxIpAddress"
_StaticDefaultIpv6Router_Object = MibScalar
staticDefaultIpv6Router = _StaticDefaultIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 500, 350),
    _StaticDefaultIpv6Router_Type()
)
staticDefaultIpv6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDefaultIpv6Router.setStatus("current")
_DnsServersGroup_ObjectIdentity = ObjectIdentity
dnsServersGroup = _DnsServersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600)
)


class _DnsServersConfigSource_Type(Integer32):
    """Custom type dnsServersConfigSource based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 100),
          ("automaticIpv6", 150),
          ("static", 200))
    )


_DnsServersConfigSource_Type.__name__ = "Integer32"
_DnsServersConfigSource_Object = MibScalar
dnsServersConfigSource = _DnsServersConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 100),
    _DnsServersConfigSource_Type()
)
dnsServersConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServersConfigSource.setStatus("current")


class _DnsCacheRandomization_Type(MxEnableState):
    """Custom type dnsCacheRandomization based on MxEnableState"""
    defaultValue = 0


_DnsCacheRandomization_Type.__name__ = "MxEnableState"
_DnsCacheRandomization_Object = MibScalar
dnsCacheRandomization = _DnsCacheRandomization_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 150),
    _DnsCacheRandomization_Type()
)
dnsCacheRandomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsCacheRandomization.setStatus("current")
_DnsServersInfoTable_Object = MibTable
dnsServersInfoTable = _DnsServersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 200)
)
if mibBuilder.loadTexts:
    dnsServersInfoTable.setStatus("current")
_DnsServersInfoEntry_Object = MibTableRow
dnsServersInfoEntry = _DnsServersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 200, 1)
)
dnsServersInfoEntry.setIndexNames(
    (0, "MX-HOC-MIB", "dnsServersInfoPriority"),
)
if mibBuilder.loadTexts:
    dnsServersInfoEntry.setStatus("current")


class _DnsServersInfoPriority_Type(Unsigned32):
    """Custom type dnsServersInfoPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DnsServersInfoPriority_Type.__name__ = "Unsigned32"
_DnsServersInfoPriority_Object = MibTableColumn
dnsServersInfoPriority = _DnsServersInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 200, 1, 100),
    _DnsServersInfoPriority_Type()
)
dnsServersInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoPriority.setStatus("current")
_DnsServersInfoIpAddress_Type = MxIpAddress
_DnsServersInfoIpAddress_Object = MibTableColumn
dnsServersInfoIpAddress = _DnsServersInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 200, 1, 200),
    _DnsServersInfoIpAddress_Type()
)
dnsServersInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoIpAddress.setStatus("current")
_StaticDnsServersTable_Object = MibTable
staticDnsServersTable = _StaticDnsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 300)
)
if mibBuilder.loadTexts:
    staticDnsServersTable.setStatus("current")
_StaticDnsServersEntry_Object = MibTableRow
staticDnsServersEntry = _StaticDnsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 300, 1)
)
staticDnsServersEntry.setIndexNames(
    (0, "MX-HOC-MIB", "staticDnsServersPriority"),
)
if mibBuilder.loadTexts:
    staticDnsServersEntry.setStatus("current")


class _StaticDnsServersPriority_Type(Unsigned32):
    """Custom type staticDnsServersPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StaticDnsServersPriority_Type.__name__ = "Unsigned32"
_StaticDnsServersPriority_Object = MibTableColumn
staticDnsServersPriority = _StaticDnsServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 300, 1, 100),
    _StaticDnsServersPriority_Type()
)
staticDnsServersPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticDnsServersPriority.setStatus("current")
_StaticDnsServersIpAddress_Type = MxIpAddress
_StaticDnsServersIpAddress_Object = MibTableColumn
staticDnsServersIpAddress = _StaticDnsServersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 600, 300, 1, 200),
    _StaticDnsServersIpAddress_Type()
)
staticDnsServersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDnsServersIpAddress.setStatus("current")
_HostsGroup_ObjectIdentity = ObjectIdentity
hostsGroup = _HostsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650)
)
_StaticHostsTable_Object = MibTable
staticHostsTable = _StaticHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650, 100)
)
if mibBuilder.loadTexts:
    staticHostsTable.setStatus("current")
_StaticHostsEntry_Object = MibTableRow
staticHostsEntry = _StaticHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650, 100, 1)
)
staticHostsEntry.setIndexNames(
    (0, "MX-HOC-MIB", "staticHostsIndex"),
)
if mibBuilder.loadTexts:
    staticHostsEntry.setStatus("current")
_StaticHostsIndex_Type = Unsigned32
_StaticHostsIndex_Object = MibTableColumn
staticHostsIndex = _StaticHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650, 100, 1, 100),
    _StaticHostsIndex_Type()
)
staticHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticHostsIndex.setStatus("current")


class _StaticHostsName_Type(OctetString):
    """Custom type staticHostsName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_StaticHostsName_Type.__name__ = "OctetString"
_StaticHostsName_Object = MibTableColumn
staticHostsName = _StaticHostsName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650, 100, 1, 200),
    _StaticHostsName_Type()
)
staticHostsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticHostsName.setStatus("current")


class _StaticHostsIpAddresses_Type(OctetString):
    """Custom type staticHostsIpAddresses based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StaticHostsIpAddresses_Type.__name__ = "OctetString"
_StaticHostsIpAddresses_Object = MibTableColumn
staticHostsIpAddresses = _StaticHostsIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650, 100, 1, 300),
    _StaticHostsIpAddresses_Type()
)
staticHostsIpAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticHostsIpAddresses.setStatus("current")


class _StaticHostsDelete_Type(Integer32):
    """Custom type staticHostsDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_StaticHostsDelete_Type.__name__ = "Integer32"
_StaticHostsDelete_Object = MibTableColumn
staticHostsDelete = _StaticHostsDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 650, 100, 1, 1000),
    _StaticHostsDelete_Type()
)
staticHostsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticHostsDelete.setStatus("current")
_SystemGroup_ObjectIdentity = ObjectIdentity
systemGroup = _SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 800)
)


class _SystemContact_Type(OctetString):
    """Custom type systemContact based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemContact_Type.__name__ = "OctetString"
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 800, 100),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")


class _SystemName_Type(OctetString):
    """Custom type systemName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemName_Type.__name__ = "OctetString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 800, 200),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SystemLocation_Type(OctetString):
    """Custom type systemLocation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemLocation_Type.__name__ = "OctetString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 800, 300),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")
_HttpClientGroup_ObjectIdentity = ObjectIdentity
httpClientGroup = _HttpClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 800, 1000)
)


class _HttpUaHeaderFormat_Type(OctetString):
    """Custom type httpUaHeaderFormat based on OctetString"""
    defaultValue = OctetString("%product%/v%version% %profile%")


_HttpUaHeaderFormat_Type.__name__ = "OctetString"
_HttpUaHeaderFormat_Object = MibScalar
httpUaHeaderFormat = _HttpUaHeaderFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 800, 1000, 100),
    _HttpUaHeaderFormat_Type()
)
httpUaHeaderFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUaHeaderFormat.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 700, 1, 60020, 100),
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
    "MX-HOC-MIB",
    **{"hocMIB": hocMIB,
       "hocMIBObjects": hocMIBObjects,
       "managementInterface": managementInterface,
       "automaticConfigurationInterface": automaticConfigurationInterface,
       "ipv6AutomaticConfigurationInterface": ipv6AutomaticConfigurationInterface,
       "hostName": hostName,
       "timeGroup": timeGroup,
       "systemTime": systemTime,
       "systemUptime": systemUptime,
       "staticTimeZone": staticTimeZone,
       "domainNameGroup": domainNameGroup,
       "domainNameConfigSource": domainNameConfigSource,
       "domainNameInfo": domainNameInfo,
       "staticDomainName": staticDomainName,
       "sntpGroup": sntpGroup,
       "sntpConfigSource": sntpConfigSource,
       "sntpSynchronizationPeriod": sntpSynchronizationPeriod,
       "sntpSynchronizationPeriodOnError": sntpSynchronizationPeriodOnError,
       "sntpTimeZone": sntpTimeZone,
       "sntpServerHostInfo": sntpServerHostInfo,
       "staticSntpServerHost": staticSntpServerHost,
       "sntpCurrentSource": sntpCurrentSource,
       "sntpServersInfoTable": sntpServersInfoTable,
       "sntpServersInfoEntry": sntpServersInfoEntry,
       "sntpServersInfoPriority": sntpServersInfoPriority,
       "sntpServersInfoHostName": sntpServersInfoHostName,
       "staticSntpServersTable": staticSntpServersTable,
       "staticSntpServersEntry": staticSntpServersEntry,
       "staticSntpServersPriority": staticSntpServersPriority,
       "staticSntpServersHostName": staticSntpServersHostName,
       "defaultRouterGroup": defaultRouterGroup,
       "defaultRouterConfigSource": defaultRouterConfigSource,
       "defaultIpv6RouterConfigSource": defaultIpv6RouterConfigSource,
       "defaultRouterInfo": defaultRouterInfo,
       "defaultIpv6RouterInfo": defaultIpv6RouterInfo,
       "staticDefaultRouter": staticDefaultRouter,
       "staticDefaultIpv6Router": staticDefaultIpv6Router,
       "dnsServersGroup": dnsServersGroup,
       "dnsServersConfigSource": dnsServersConfigSource,
       "dnsCacheRandomization": dnsCacheRandomization,
       "dnsServersInfoTable": dnsServersInfoTable,
       "dnsServersInfoEntry": dnsServersInfoEntry,
       "dnsServersInfoPriority": dnsServersInfoPriority,
       "dnsServersInfoIpAddress": dnsServersInfoIpAddress,
       "staticDnsServersTable": staticDnsServersTable,
       "staticDnsServersEntry": staticDnsServersEntry,
       "staticDnsServersPriority": staticDnsServersPriority,
       "staticDnsServersIpAddress": staticDnsServersIpAddress,
       "hostsGroup": hostsGroup,
       "staticHostsTable": staticHostsTable,
       "staticHostsEntry": staticHostsEntry,
       "staticHostsIndex": staticHostsIndex,
       "staticHostsName": staticHostsName,
       "staticHostsIpAddresses": staticHostsIpAddresses,
       "staticHostsDelete": staticHostsDelete,
       "systemGroup": systemGroup,
       "systemContact": systemContact,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "httpClientGroup": httpClientGroup,
       "httpUaHeaderFormat": httpUaHeaderFormat,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
