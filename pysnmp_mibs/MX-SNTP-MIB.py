# SNMP MIB module (MX-SNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SNTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:57 2025
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

(MxIpConfigSource,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxIpConfigSource",
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

sntpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65)
)
if mibBuilder.loadTexts:
    sntpMIB.setRevisions(
        ("1907-10-24 00:00",
         "1903-02-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusSntp_ObjectIdentity = ObjectIdentity
ipAddressStatusSntp = _IpAddressStatusSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 80)
)


class _SntpConfigSource_Type(MxIpConfigSource):
    """Custom type sntpConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_SntpConfigSource_Type.__name__ = "MxIpConfigSource"
_SntpConfigSource_Object = MibScalar
sntpConfigSource = _SntpConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 80, 1),
    _SntpConfigSource_Type()
)
sntpConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpConfigSource.setStatus("current")


class _SntpHost_Type(MxIpHostName):
    """Custom type sntpHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_SntpHost_Type.__name__ = "MxIpHostName"
_SntpHost_Object = MibScalar
sntpHost = _SntpHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 80, 10),
    _SntpHost_Type()
)
sntpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpHost.setStatus("current")


class _SntpPort_Type(MxIpPort):
    """Custom type sntpPort based on MxIpPort"""
    defaultValue = 123


_SntpPort_Type.__name__ = "MxIpPort"
_SntpPort_Object = MibScalar
sntpPort = _SntpPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 80, 11),
    _SntpPort_Type()
)
sntpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpPort.setStatus("current")
_IpAddressConfigSntp_ObjectIdentity = ObjectIdentity
ipAddressConfigSntp = _IpAddressConfigSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 80)
)


class _SntpSelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type sntpSelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_SntpSelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_SntpSelectConfigSource_Object = MibScalar
sntpSelectConfigSource = _SntpSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 80, 1),
    _SntpSelectConfigSource_Type()
)
sntpSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSelectConfigSource.setStatus("current")
_IpAddressConfigSntpStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigSntpStatic = _IpAddressConfigSntpStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 80, 10)
)


class _SntpStaticHost_Type(MxIpHostName):
    """Custom type sntpStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_SntpStaticHost_Type.__name__ = "MxIpHostName"
_SntpStaticHost_Object = MibScalar
sntpStaticHost = _SntpStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 80, 10, 10),
    _SntpStaticHost_Type()
)
sntpStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStaticHost.setStatus("current")


class _SntpStaticPort_Type(MxIpPort):
    """Custom type sntpStaticPort based on MxIpPort"""
    defaultValue = 123


_SntpStaticPort_Type.__name__ = "MxIpPort"
_SntpStaticPort_Object = MibScalar
sntpStaticPort = _SntpStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 80, 10, 11),
    _SntpStaticPort_Type()
)
sntpStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStaticPort.setStatus("current")
_SntpMIBObjects_ObjectIdentity = ObjectIdentity
sntpMIBObjects = _SntpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1)
)


class _SntpEnable_Type(Integer32):
    """Custom type sntpEnable based on Integer32"""
    defaultValue = 0

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


_SntpEnable_Type.__name__ = "Integer32"
_SntpEnable_Object = MibScalar
sntpEnable = _SntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1, 5),
    _SntpEnable_Type()
)
sntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpEnable.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1, 15),
    _SntpSynchronizationPeriodOnError_Type()
)
sntpSynchronizationPeriodOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSynchronizationPeriodOnError.setStatus("current")
_SntpTimeZoneConfig_ObjectIdentity = ObjectIdentity
sntpTimeZoneConfig = _SntpTimeZoneConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1, 25)
)


class _SntpTimeZoneString_Type(OctetString):
    """Custom type sntpTimeZoneString based on OctetString"""
    defaultValue = OctetString("EST5DST4,M3.2.0/02:00:00,M11.1.0/02:00:00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SntpTimeZoneString_Type.__name__ = "OctetString"
_SntpTimeZoneString_Object = MibScalar
sntpTimeZoneString = _SntpTimeZoneString_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1, 25, 15),
    _SntpTimeZoneString_Type()
)
sntpTimeZoneString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeZoneString.setStatus("current")


class _SntpTimeZoneStringIsValid_Type(Integer32):
    """Custom type sntpTimeZoneStringIsValid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_SntpTimeZoneStringIsValid_Type.__name__ = "Integer32"
_SntpTimeZoneStringIsValid_Object = MibScalar
sntpTimeZoneStringIsValid = _SntpTimeZoneStringIsValid_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 1, 25, 20),
    _SntpTimeZoneStringIsValid_Type()
)
sntpTimeZoneStringIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpTimeZoneStringIsValid.setStatus("deprecated")
_SntpConformance_ObjectIdentity = ObjectIdentity
sntpConformance = _SntpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 2)
)
_SntpCompliances_ObjectIdentity = ObjectIdentity
sntpCompliances = _SntpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 2, 1)
)
_SntpGroups_ObjectIdentity = ObjectIdentity
sntpGroups = _SntpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 2, 2)
)

# Managed Objects groups

sntpBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 2, 2, 1)
)
sntpBasicGroupVer1.setObjects(
      *(("MX-SNTP-MIB", "sntpEnable"),
        ("MX-SNTP-MIB", "sntpSynchronizationPeriod"),
        ("MX-SNTP-MIB", "sntpSynchronizationPeriodOnError"),
        ("MX-SNTP-MIB", "sntpTimeZoneString"),
        ("MX-SNTP-MIB", "sntpTimeZoneStringIsValid"))
)
if mibBuilder.loadTexts:
    sntpBasicGroupVer1.setStatus("current")

sntpServerGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 2, 2, 2)
)
sntpServerGroupVer1.setObjects(
      *(("MX-SNTP-MIB", "sntpConfigSource"),
        ("MX-SNTP-MIB", "sntpHost"),
        ("MX-SNTP-MIB", "sntpPort"),
        ("MX-SNTP-MIB", "sntpSelectConfigSource"),
        ("MX-SNTP-MIB", "sntpStaticHost"),
        ("MX-SNTP-MIB", "sntpStaticPort"))
)
if mibBuilder.loadTexts:
    sntpServerGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sntpBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 65, 2, 1, 1)
)
sntpBasicComplVer1.setObjects(
      *(("MX-SNTP-MIB", "sntpBasicGroupVer1"),
        ("MX-SNTP-MIB", "sntpServerGroupVer1"))
)
if mibBuilder.loadTexts:
    sntpBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SNTP-MIB",
    **{"ipAddressStatusSntp": ipAddressStatusSntp,
       "sntpConfigSource": sntpConfigSource,
       "sntpHost": sntpHost,
       "sntpPort": sntpPort,
       "ipAddressConfigSntp": ipAddressConfigSntp,
       "sntpSelectConfigSource": sntpSelectConfigSource,
       "ipAddressConfigSntpStatic": ipAddressConfigSntpStatic,
       "sntpStaticHost": sntpStaticHost,
       "sntpStaticPort": sntpStaticPort,
       "sntpMIB": sntpMIB,
       "sntpMIBObjects": sntpMIBObjects,
       "sntpEnable": sntpEnable,
       "sntpSynchronizationPeriod": sntpSynchronizationPeriod,
       "sntpSynchronizationPeriodOnError": sntpSynchronizationPeriodOnError,
       "sntpTimeZoneConfig": sntpTimeZoneConfig,
       "sntpTimeZoneString": sntpTimeZoneString,
       "sntpTimeZoneStringIsValid": sntpTimeZoneStringIsValid,
       "sntpConformance": sntpConformance,
       "sntpCompliances": sntpCompliances,
       "sntpBasicComplVer1": sntpBasicComplVer1,
       "sntpGroups": sntpGroups,
       "sntpBasicGroupVer1": sntpBasicGroupVer1,
       "sntpServerGroupVer1": sntpServerGroupVer1}
)
