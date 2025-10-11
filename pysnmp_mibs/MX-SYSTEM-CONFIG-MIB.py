# SNMP MIB module (MX-SYSTEM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SYSTEM-CONFIG-MIB
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
 mediatrixConfig,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixConfig",
    "mediatrixMgmt")

(MxEnableState,
 MxIpAddress,
 MxIpConfigSource,
 MxIpPort,
 MxIpSelectConfigSource,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpAddress",
    "MxIpConfigSource",
    "MxIpPort",
    "MxIpSelectConfigSource",
    "MxIpSubnetMask")

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

sysConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3)
)
if mibBuilder.loadTexts:
    sysConfigMIB.setRevisions(
        ("2008-08-25 00:00",
         "2006-11-23 00:00",
         "2006-07-12 00:00",
         "2005-08-31 00:00",
         "2005-05-09 00:00",
         "2004-09-20 00:00",
         "2004-02-12 00:00",
         "2003-11-14 00:00",
         "2003-11-13 00:00",
         "2003-09-11 00:00",
         "2003-07-16 00:00",
         "2003-04-10 00:00",
         "2003-04-07 00:00",
         "2003-04-03 00:00",
         "2003-03-11 00:00",
         "2002-08-19 00:00",
         "2002-07-10 00:00",
         "2002-01-10 00:00",
         "2001-08-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusLocalHost_ObjectIdentity = ObjectIdentity
ipAddressStatusLocalHost = _IpAddressStatusLocalHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1)
)


class _LocalHostConfigSource_Type(MxIpConfigSource):
    """Custom type localHostConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_LocalHostConfigSource_Type.__name__ = "MxIpConfigSource"
_LocalHostConfigSource_Object = MibScalar
localHostConfigSource = _LocalHostConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 1),
    _LocalHostConfigSource_Type()
)
localHostConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostConfigSource.setStatus("current")


class _LocalHostAddress_Type(MxIpAddress):
    """Custom type localHostAddress based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.1")


_LocalHostAddress_Type.__name__ = "MxIpAddress"
_LocalHostAddress_Object = MibScalar
localHostAddress = _LocalHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 2),
    _LocalHostAddress_Type()
)
localHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostAddress.setStatus("current")


class _LocalHostDhcpServer_Type(MxIpAddress):
    """Custom type localHostDhcpServer based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostDhcpServer_Type.__name__ = "MxIpAddress"
_LocalHostDhcpServer_Object = MibScalar
localHostDhcpServer = _LocalHostDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 3),
    _LocalHostDhcpServer_Type()
)
localHostDhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostDhcpServer.setStatus("current")


class _LocalHostPrimaryDns_Type(MxIpAddress):
    """Custom type localHostPrimaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostPrimaryDns_Type.__name__ = "MxIpAddress"
_LocalHostPrimaryDns_Object = MibScalar
localHostPrimaryDns = _LocalHostPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 4),
    _LocalHostPrimaryDns_Type()
)
localHostPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostPrimaryDns.setStatus("current")


class _LocalHostSecondaryDns_Type(MxIpAddress):
    """Custom type localHostSecondaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostSecondaryDns_Type.__name__ = "MxIpAddress"
_LocalHostSecondaryDns_Object = MibScalar
localHostSecondaryDns = _LocalHostSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 5),
    _LocalHostSecondaryDns_Type()
)
localHostSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostSecondaryDns.setStatus("current")


class _LocalHostDefaultRouter_Type(MxIpAddress):
    """Custom type localHostDefaultRouter based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostDefaultRouter_Type.__name__ = "MxIpAddress"
_LocalHostDefaultRouter_Object = MibScalar
localHostDefaultRouter = _LocalHostDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 6),
    _LocalHostDefaultRouter_Type()
)
localHostDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostDefaultRouter.setStatus("current")


class _LocalHostSnmpPort_Type(MxIpPort):
    """Custom type localHostSnmpPort based on MxIpPort"""
    defaultValue = 161


_LocalHostSnmpPort_Type.__name__ = "MxIpPort"
_LocalHostSnmpPort_Object = MibScalar
localHostSnmpPort = _LocalHostSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 7),
    _LocalHostSnmpPort_Type()
)
localHostSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostSnmpPort.setStatus("current")


class _LocalHostSubnetMask_Type(MxIpSubnetMask):
    """Custom type localHostSubnetMask based on MxIpSubnetMask"""
    defaultValue = OctetString("255.255.255.0")


_LocalHostSubnetMask_Type.__name__ = "MxIpSubnetMask"
_LocalHostSubnetMask_Object = MibScalar
localHostSubnetMask = _LocalHostSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 8),
    _LocalHostSubnetMask_Type()
)
localHostSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostSubnetMask.setStatus("current")


class _LocalHostFqdnConfigSource_Type(Integer32):
    """Custom type localHostFqdnConfigSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcp", 1),
          ("dns", 2),
          ("none", 3))
    )


_LocalHostFqdnConfigSource_Type.__name__ = "Integer32"
_LocalHostFqdnConfigSource_Object = MibScalar
localHostFqdnConfigSource = _LocalHostFqdnConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 9),
    _LocalHostFqdnConfigSource_Type()
)
localHostFqdnConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostFqdnConfigSource.setStatus("current")


class _LocalHostFqdn_Type(OctetString):
    """Custom type localHostFqdn based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHostFqdn_Type.__name__ = "OctetString"
_LocalHostFqdn_Object = MibScalar
localHostFqdn = _LocalHostFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 10),
    _LocalHostFqdn_Type()
)
localHostFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostFqdn.setStatus("current")


class _LocalHostWanAddressConfigSource_Type(Integer32):
    """Custom type localHostWanAddressConfigSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localAddress", 0),
          ("static", 1),
          ("pppoe", 2),
          ("pppoa", 3))
    )


_LocalHostWanAddressConfigSource_Type.__name__ = "Integer32"
_LocalHostWanAddressConfigSource_Object = MibScalar
localHostWanAddressConfigSource = _LocalHostWanAddressConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 15),
    _LocalHostWanAddressConfigSource_Type()
)
localHostWanAddressConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostWanAddressConfigSource.setStatus("current")


class _LocalHostWanAddress_Type(MxIpAddress):
    """Custom type localHostWanAddress based on MxIpAddress"""
    defaultValue = OctetString("0.0.0.0")


_LocalHostWanAddress_Type.__name__ = "MxIpAddress"
_LocalHostWanAddress_Object = MibScalar
localHostWanAddress = _LocalHostWanAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 1, 20),
    _LocalHostWanAddress_Type()
)
localHostWanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHostWanAddress.setStatus("current")
_IpAddressStatusTelephonyDns_ObjectIdentity = ObjectIdentity
ipAddressStatusTelephonyDns = _IpAddressStatusTelephonyDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 100)
)


class _TelephonyDnsPrimaryDns_Type(MxIpAddress):
    """Custom type telephonyDnsPrimaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_TelephonyDnsPrimaryDns_Type.__name__ = "MxIpAddress"
_TelephonyDnsPrimaryDns_Object = MibScalar
telephonyDnsPrimaryDns = _TelephonyDnsPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 100, 10),
    _TelephonyDnsPrimaryDns_Type()
)
telephonyDnsPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyDnsPrimaryDns.setStatus("current")


class _TelephonyDnsSecondaryDns_Type(MxIpAddress):
    """Custom type telephonyDnsSecondaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_TelephonyDnsSecondaryDns_Type.__name__ = "MxIpAddress"
_TelephonyDnsSecondaryDns_Object = MibScalar
telephonyDnsSecondaryDns = _TelephonyDnsSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 100, 15),
    _TelephonyDnsSecondaryDns_Type()
)
telephonyDnsSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyDnsSecondaryDns.setStatus("current")
_IpAddressConfigLocalHost_ObjectIdentity = ObjectIdentity
ipAddressConfigLocalHost = _IpAddressConfigLocalHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1)
)


class _LocalHostSelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type localHostSelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_LocalHostSelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_LocalHostSelectConfigSource_Object = MibScalar
localHostSelectConfigSource = _LocalHostSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 1),
    _LocalHostSelectConfigSource_Type()
)
localHostSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostSelectConfigSource.setStatus("current")


class _LocalHostFqdnSelectConfigSource_Type(Integer32):
    """Custom type localHostFqdnSelectConfigSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcp", 1),
          ("dns", 2),
          ("none", 3))
    )


_LocalHostFqdnSelectConfigSource_Type.__name__ = "Integer32"
_LocalHostFqdnSelectConfigSource_Object = MibScalar
localHostFqdnSelectConfigSource = _LocalHostFqdnSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 2),
    _LocalHostFqdnSelectConfigSource_Type()
)
localHostFqdnSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostFqdnSelectConfigSource.setStatus("current")


class _LocalHostWanAddressSelectConfigSource_Type(Integer32):
    """Custom type localHostWanAddressSelectConfigSource based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("localAddress", 0),
          ("static", 1),
          ("pppoe", 2),
          ("pppoa", 3),
          ("automatic", 9999))
    )


_LocalHostWanAddressSelectConfigSource_Type.__name__ = "Integer32"
_LocalHostWanAddressSelectConfigSource_Object = MibScalar
localHostWanAddressSelectConfigSource = _LocalHostWanAddressSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 5),
    _LocalHostWanAddressSelectConfigSource_Type()
)
localHostWanAddressSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostWanAddressSelectConfigSource.setStatus("current")


class _LocalHostDnsOverrideEnable_Type(MxEnableState):
    """Custom type localHostDnsOverrideEnable based on MxEnableState"""
    defaultValue = 0


_LocalHostDnsOverrideEnable_Type.__name__ = "MxEnableState"
_LocalHostDnsOverrideEnable_Object = MibScalar
localHostDnsOverrideEnable = _LocalHostDnsOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 6),
    _LocalHostDnsOverrideEnable_Type()
)
localHostDnsOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostDnsOverrideEnable.setStatus("current")
_IpAddressConfigLocalHostStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigLocalHostStatic = _IpAddressConfigLocalHostStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10)
)


class _LocalHostStaticAddress_Type(MxIpAddress):
    """Custom type localHostStaticAddress based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.1")


_LocalHostStaticAddress_Type.__name__ = "MxIpAddress"
_LocalHostStaticAddress_Object = MibScalar
localHostStaticAddress = _LocalHostStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 1),
    _LocalHostStaticAddress_Type()
)
localHostStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticAddress.setStatus("current")


class _LocalHostStaticPrimaryDns_Type(MxIpAddress):
    """Custom type localHostStaticPrimaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostStaticPrimaryDns_Type.__name__ = "MxIpAddress"
_LocalHostStaticPrimaryDns_Object = MibScalar
localHostStaticPrimaryDns = _LocalHostStaticPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 2),
    _LocalHostStaticPrimaryDns_Type()
)
localHostStaticPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticPrimaryDns.setStatus("current")


class _LocalHostStaticSecondaryDns_Type(MxIpAddress):
    """Custom type localHostStaticSecondaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostStaticSecondaryDns_Type.__name__ = "MxIpAddress"
_LocalHostStaticSecondaryDns_Object = MibScalar
localHostStaticSecondaryDns = _LocalHostStaticSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 3),
    _LocalHostStaticSecondaryDns_Type()
)
localHostStaticSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticSecondaryDns.setStatus("current")


class _LocalHostStaticDefaultRouter_Type(MxIpAddress):
    """Custom type localHostStaticDefaultRouter based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_LocalHostStaticDefaultRouter_Type.__name__ = "MxIpAddress"
_LocalHostStaticDefaultRouter_Object = MibScalar
localHostStaticDefaultRouter = _LocalHostStaticDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 4),
    _LocalHostStaticDefaultRouter_Type()
)
localHostStaticDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticDefaultRouter.setStatus("current")


class _LocalHostStaticSnmpPort_Type(MxIpPort):
    """Custom type localHostStaticSnmpPort based on MxIpPort"""
    defaultValue = 161


_LocalHostStaticSnmpPort_Type.__name__ = "MxIpPort"
_LocalHostStaticSnmpPort_Object = MibScalar
localHostStaticSnmpPort = _LocalHostStaticSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 5),
    _LocalHostStaticSnmpPort_Type()
)
localHostStaticSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticSnmpPort.setStatus("current")


class _LocalHostStaticSubnetMask_Type(MxIpSubnetMask):
    """Custom type localHostStaticSubnetMask based on MxIpSubnetMask"""
    defaultValue = OctetString("255.255.255.0")


_LocalHostStaticSubnetMask_Type.__name__ = "MxIpSubnetMask"
_LocalHostStaticSubnetMask_Object = MibScalar
localHostStaticSubnetMask = _LocalHostStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 6),
    _LocalHostStaticSubnetMask_Type()
)
localHostStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticSubnetMask.setStatus("current")


class _LocalHostStaticFqdn_Type(OctetString):
    """Custom type localHostStaticFqdn based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHostStaticFqdn_Type.__name__ = "OctetString"
_LocalHostStaticFqdn_Object = MibScalar
localHostStaticFqdn = _LocalHostStaticFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 7),
    _LocalHostStaticFqdn_Type()
)
localHostStaticFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticFqdn.setStatus("current")


class _LocalHostStaticWanAddress_Type(MxIpAddress):
    """Custom type localHostStaticWanAddress based on MxIpAddress"""
    defaultValue = OctetString("0.0.0.0")


_LocalHostStaticWanAddress_Type.__name__ = "MxIpAddress"
_LocalHostStaticWanAddress_Object = MibScalar
localHostStaticWanAddress = _LocalHostStaticWanAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 1, 10, 10),
    _LocalHostStaticWanAddress_Type()
)
localHostStaticWanAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHostStaticWanAddress.setStatus("current")
_IpAddressConfigTelephonyDns_ObjectIdentity = ObjectIdentity
ipAddressConfigTelephonyDns = _IpAddressConfigTelephonyDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 120)
)


class _TelephonyDnsOverrideEnable_Type(MxEnableState):
    """Custom type telephonyDnsOverrideEnable based on MxEnableState"""
    defaultValue = 0


_TelephonyDnsOverrideEnable_Type.__name__ = "MxEnableState"
_TelephonyDnsOverrideEnable_Object = MibScalar
telephonyDnsOverrideEnable = _TelephonyDnsOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 120, 1),
    _TelephonyDnsOverrideEnable_Type()
)
telephonyDnsOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyDnsOverrideEnable.setStatus("current")
_IpAddressConfigTelephonyDnsStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigTelephonyDnsStatic = _IpAddressConfigTelephonyDnsStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 120, 50)
)


class _TelephonyDnsStaticPrimaryDns_Type(MxIpAddress):
    """Custom type telephonyDnsStaticPrimaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_TelephonyDnsStaticPrimaryDns_Type.__name__ = "MxIpAddress"
_TelephonyDnsStaticPrimaryDns_Object = MibScalar
telephonyDnsStaticPrimaryDns = _TelephonyDnsStaticPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 120, 50, 10),
    _TelephonyDnsStaticPrimaryDns_Type()
)
telephonyDnsStaticPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyDnsStaticPrimaryDns.setStatus("current")


class _TelephonyDnsStaticSecondaryDns_Type(MxIpAddress):
    """Custom type telephonyDnsStaticSecondaryDns based on MxIpAddress"""
    defaultValue = OctetString("192.168.0.10")


_TelephonyDnsStaticSecondaryDns_Type.__name__ = "MxIpAddress"
_TelephonyDnsStaticSecondaryDns_Object = MibScalar
telephonyDnsStaticSecondaryDns = _TelephonyDnsStaticSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 120, 50, 15),
    _TelephonyDnsStaticSecondaryDns_Type()
)
telephonyDnsStaticSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyDnsStaticSecondaryDns.setStatus("current")
_SysConfigMIBObjects_ObjectIdentity = ObjectIdentity
sysConfigMIBObjects = _SysConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1)
)


class _SysConfigNetworkEthernetSpeed_Type(Integer32):
    """Custom type sysConfigNetworkEthernetSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 0),
          ("at-10Mbs-HalfDuplex", 1),
          ("at-100Mbs-HalfDuplex", 2),
          ("at-10Mbs-FullDuplex", 3),
          ("at-100Mbs-FullDuplex", 4))
    )


_SysConfigNetworkEthernetSpeed_Type.__name__ = "Integer32"
_SysConfigNetworkEthernetSpeed_Object = MibScalar
sysConfigNetworkEthernetSpeed = _SysConfigNetworkEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 10),
    _SysConfigNetworkEthernetSpeed_Type()
)
sysConfigNetworkEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigNetworkEthernetSpeed.setStatus("current")


class _SysConfigComputerEthernetSpeed_Type(Integer32):
    """Custom type sysConfigComputerEthernetSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 0),
          ("at-10Mbs-HalfDuplex", 1),
          ("at-100Mbs-HalfDuplex", 2),
          ("at-10Mbs-FullDuplex", 3),
          ("at-100Mbs-FullDuplex", 4))
    )


_SysConfigComputerEthernetSpeed_Type.__name__ = "Integer32"
_SysConfigComputerEthernetSpeed_Object = MibScalar
sysConfigComputerEthernetSpeed = _SysConfigComputerEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 12),
    _SysConfigComputerEthernetSpeed_Type()
)
sysConfigComputerEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigComputerEthernetSpeed.setStatus("current")


class _SysConfigMinDynamicPort_Type(Unsigned32):
    """Custom type sysConfigMinDynamicPort based on Unsigned32"""
    defaultValue = 31001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SysConfigMinDynamicPort_Type.__name__ = "Unsigned32"
_SysConfigMinDynamicPort_Object = MibScalar
sysConfigMinDynamicPort = _SysConfigMinDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 14),
    _SysConfigMinDynamicPort_Type()
)
sysConfigMinDynamicPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMinDynamicPort.setStatus("current")


class _SysConfigMaxDynamicPort_Type(Unsigned32):
    """Custom type sysConfigMaxDynamicPort based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SysConfigMaxDynamicPort_Type.__name__ = "Unsigned32"
_SysConfigMaxDynamicPort_Object = MibScalar
sysConfigMaxDynamicPort = _SysConfigMaxDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 16),
    _SysConfigMaxDynamicPort_Type()
)
sysConfigMaxDynamicPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMaxDynamicPort.setStatus("current")


class _SysConfigDhcpWait_Type(MxEnableState):
    """Custom type sysConfigDhcpWait based on MxEnableState"""
    defaultValue = 1


_SysConfigDhcpWait_Type.__name__ = "MxEnableState"
_SysConfigDhcpWait_Object = MibScalar
sysConfigDhcpWait = _SysConfigDhcpWait_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 19),
    _SysConfigDhcpWait_Type()
)
sysConfigDhcpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigDhcpWait.setStatus("current")


class _SysConfigDhcpWaitDelay_Type(Unsigned32):
    """Custom type sysConfigDhcpWaitDelay based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_SysConfigDhcpWaitDelay_Type.__name__ = "Unsigned32"
_SysConfigDhcpWaitDelay_Object = MibScalar
sysConfigDhcpWaitDelay = _SysConfigDhcpWaitDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 22),
    _SysConfigDhcpWaitDelay_Type()
)
sysConfigDhcpWaitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigDhcpWaitDelay.setStatus("current")


class _SysConfigBootpFlags_Type(Integer32):
    """Custom type sysConfigBootpFlags based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noFlags", 0),
          ("broadcastFlag", 1))
    )


_SysConfigBootpFlags_Type.__name__ = "Integer32"
_SysConfigBootpFlags_Object = MibScalar
sysConfigBootpFlags = _SysConfigBootpFlags_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 23),
    _SysConfigBootpFlags_Type()
)
sysConfigBootpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigBootpFlags.setStatus("current")


class _SysConfigProductNamePadding_Type(OctetString):
    """Custom type sysConfigProductNamePadding based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysConfigProductNamePadding_Type.__name__ = "OctetString"
_SysConfigProductNamePadding_Object = MibScalar
sysConfigProductNamePadding = _SysConfigProductNamePadding_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 24),
    _SysConfigProductNamePadding_Type()
)
sysConfigProductNamePadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigProductNamePadding.setStatus("current")
_SysConfigStats_ObjectIdentity = ObjectIdentity
sysConfigStats = _SysConfigStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 25)
)


class _SysConfigStatsPeriodLength_Type(Unsigned32):
    """Custom type sysConfigStatsPeriodLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 288),
    )


_SysConfigStatsPeriodLength_Type.__name__ = "Unsigned32"
_SysConfigStatsPeriodLength_Object = MibScalar
sysConfigStatsPeriodLength = _SysConfigStatsPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 25, 1),
    _SysConfigStatsPeriodLength_Type()
)
sysConfigStatsPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigStatsPeriodLength.setStatus("current")


class _SysConfigStatsNumberPeriods_Type(Unsigned32):
    """Custom type sysConfigStatsNumberPeriods based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_SysConfigStatsNumberPeriods_Type.__name__ = "Unsigned32"
_SysConfigStatsNumberPeriods_Object = MibScalar
sysConfigStatsNumberPeriods = _SysConfigStatsNumberPeriods_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 25, 2),
    _SysConfigStatsNumberPeriods_Type()
)
sysConfigStatsNumberPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigStatsNumberPeriods.setStatus("current")


class _SysConfigStatsBySyslogEnable_Type(MxEnableState):
    """Custom type sysConfigStatsBySyslogEnable based on MxEnableState"""
    defaultValue = 0


_SysConfigStatsBySyslogEnable_Type.__name__ = "MxEnableState"
_SysConfigStatsBySyslogEnable_Object = MibScalar
sysConfigStatsBySyslogEnable = _SysConfigStatsBySyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 25, 10),
    _SysConfigStatsBySyslogEnable_Type()
)
sysConfigStatsBySyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigStatsBySyslogEnable.setStatus("current")
_SysConfigDownloadConfig_ObjectIdentity = ObjectIdentity
sysConfigDownloadConfig = _SysConfigDownloadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 30)
)


class _SysConfigDownloadConfigFile_Type(Integer32):
    """Custom type sysConfigDownloadConfigFile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noFileDownload", 0),
          ("requestFileDownload", 1),
          ("automaticInitiateFileDownload", 3))
    )


_SysConfigDownloadConfigFile_Type.__name__ = "Integer32"
_SysConfigDownloadConfigFile_Object = MibScalar
sysConfigDownloadConfigFile = _SysConfigDownloadConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 30, 1),
    _SysConfigDownloadConfigFile_Type()
)
sysConfigDownloadConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigDownloadConfigFile.setStatus("current")


class _SysConfigDownloadConfigMode_Type(Integer32):
    """Custom type sysConfigDownloadConfigMode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", -1),
          ("record", 0),
          ("commit", 1),
          ("undo", 2))
    )


_SysConfigDownloadConfigMode_Type.__name__ = "Integer32"
_SysConfigDownloadConfigMode_Object = MibScalar
sysConfigDownloadConfigMode = _SysConfigDownloadConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 1, 30, 2),
    _SysConfigDownloadConfigMode_Type()
)
sysConfigDownloadConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigDownloadConfigMode.setStatus("current")
_SysConfigConformance_ObjectIdentity = ObjectIdentity
sysConfigConformance = _SysConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2)
)
_SysConfigCompliances_ObjectIdentity = ObjectIdentity
sysConfigCompliances = _SysConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2, 1)
)
_SysConfigGroups_ObjectIdentity = ObjectIdentity
sysConfigGroups = _SysConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2, 2)
)

# Managed Objects groups

sysConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2, 2, 1)
)
sysConfigGroupVer1.setObjects(
      *(("MX-SYSTEM-CONFIG-MIB", "sysConfigNetworkEthernetSpeed"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigComputerEthernetSpeed"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigMinDynamicPort"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigMaxDynamicPort"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDhcpWait"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDhcpWaitDelay"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigBootpFlags"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigProductNamePadding"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigStatsPeriodLength"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigStatsNumberPeriods"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigStatsBySyslogEnable"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDownloadConfigFile"),
        ("MX-SYSTEM-CONFIG-MIB", "sysConfigDownloadConfigMode"))
)
if mibBuilder.loadTexts:
    sysConfigGroupVer1.setStatus("current")

commonLocalHostGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2, 2, 2)
)
commonLocalHostGroupVer1.setObjects(
      *(("MX-SYSTEM-CONFIG-MIB", "localHostConfigSource"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostAddress"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostDhcpServer"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostPrimaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostSecondaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostDefaultRouter"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostSnmpPort"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostSubnetMask"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostFqdnConfigSource"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostFqdn"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostWanAddressConfigSource"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostWanAddress"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostSelectConfigSource"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostFqdnSelectConfigSource"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostWanAddressSelectConfigSource"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostDnsOverrideEnable"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticAddress"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticPrimaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticSecondaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticDefaultRouter"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticSnmpPort"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticSubnetMask"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticFqdn"),
        ("MX-SYSTEM-CONFIG-MIB", "localHostStaticWanAddress"))
)
if mibBuilder.loadTexts:
    commonLocalHostGroupVer1.setStatus("current")

telephonyDnsGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2, 2, 5)
)
telephonyDnsGroupVer1.setObjects(
      *(("MX-SYSTEM-CONFIG-MIB", "telephonyDnsOverrideEnable"),
        ("MX-SYSTEM-CONFIG-MIB", "telephonyDnsStaticPrimaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "telephonyDnsStaticSecondaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "telephonyDnsPrimaryDns"),
        ("MX-SYSTEM-CONFIG-MIB", "telephonyDnsSecondaryDns"))
)
if mibBuilder.loadTexts:
    telephonyDnsGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sysConfigComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 3, 2, 1, 1)
)
sysConfigComplVer1.setObjects(
      *(("MX-SYSTEM-CONFIG-MIB", "sysConfigGroupVer1"),
        ("MX-SYSTEM-CONFIG-MIB", "commonLocalHostGroupVer1"),
        ("MX-SYSTEM-CONFIG-MIB", "telephonyDnsGroupVer1"))
)
if mibBuilder.loadTexts:
    sysConfigComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SYSTEM-CONFIG-MIB",
    **{"ipAddressStatusLocalHost": ipAddressStatusLocalHost,
       "localHostConfigSource": localHostConfigSource,
       "localHostAddress": localHostAddress,
       "localHostDhcpServer": localHostDhcpServer,
       "localHostPrimaryDns": localHostPrimaryDns,
       "localHostSecondaryDns": localHostSecondaryDns,
       "localHostDefaultRouter": localHostDefaultRouter,
       "localHostSnmpPort": localHostSnmpPort,
       "localHostSubnetMask": localHostSubnetMask,
       "localHostFqdnConfigSource": localHostFqdnConfigSource,
       "localHostFqdn": localHostFqdn,
       "localHostWanAddressConfigSource": localHostWanAddressConfigSource,
       "localHostWanAddress": localHostWanAddress,
       "ipAddressStatusTelephonyDns": ipAddressStatusTelephonyDns,
       "telephonyDnsPrimaryDns": telephonyDnsPrimaryDns,
       "telephonyDnsSecondaryDns": telephonyDnsSecondaryDns,
       "ipAddressConfigLocalHost": ipAddressConfigLocalHost,
       "localHostSelectConfigSource": localHostSelectConfigSource,
       "localHostFqdnSelectConfigSource": localHostFqdnSelectConfigSource,
       "localHostWanAddressSelectConfigSource": localHostWanAddressSelectConfigSource,
       "localHostDnsOverrideEnable": localHostDnsOverrideEnable,
       "ipAddressConfigLocalHostStatic": ipAddressConfigLocalHostStatic,
       "localHostStaticAddress": localHostStaticAddress,
       "localHostStaticPrimaryDns": localHostStaticPrimaryDns,
       "localHostStaticSecondaryDns": localHostStaticSecondaryDns,
       "localHostStaticDefaultRouter": localHostStaticDefaultRouter,
       "localHostStaticSnmpPort": localHostStaticSnmpPort,
       "localHostStaticSubnetMask": localHostStaticSubnetMask,
       "localHostStaticFqdn": localHostStaticFqdn,
       "localHostStaticWanAddress": localHostStaticWanAddress,
       "ipAddressConfigTelephonyDns": ipAddressConfigTelephonyDns,
       "telephonyDnsOverrideEnable": telephonyDnsOverrideEnable,
       "ipAddressConfigTelephonyDnsStatic": ipAddressConfigTelephonyDnsStatic,
       "telephonyDnsStaticPrimaryDns": telephonyDnsStaticPrimaryDns,
       "telephonyDnsStaticSecondaryDns": telephonyDnsStaticSecondaryDns,
       "sysConfigMIB": sysConfigMIB,
       "sysConfigMIBObjects": sysConfigMIBObjects,
       "sysConfigNetworkEthernetSpeed": sysConfigNetworkEthernetSpeed,
       "sysConfigComputerEthernetSpeed": sysConfigComputerEthernetSpeed,
       "sysConfigMinDynamicPort": sysConfigMinDynamicPort,
       "sysConfigMaxDynamicPort": sysConfigMaxDynamicPort,
       "sysConfigDhcpWait": sysConfigDhcpWait,
       "sysConfigDhcpWaitDelay": sysConfigDhcpWaitDelay,
       "sysConfigBootpFlags": sysConfigBootpFlags,
       "sysConfigProductNamePadding": sysConfigProductNamePadding,
       "sysConfigStats": sysConfigStats,
       "sysConfigStatsPeriodLength": sysConfigStatsPeriodLength,
       "sysConfigStatsNumberPeriods": sysConfigStatsNumberPeriods,
       "sysConfigStatsBySyslogEnable": sysConfigStatsBySyslogEnable,
       "sysConfigDownloadConfig": sysConfigDownloadConfig,
       "sysConfigDownloadConfigFile": sysConfigDownloadConfigFile,
       "sysConfigDownloadConfigMode": sysConfigDownloadConfigMode,
       "sysConfigConformance": sysConfigConformance,
       "sysConfigCompliances": sysConfigCompliances,
       "sysConfigComplVer1": sysConfigComplVer1,
       "sysConfigGroups": sysConfigGroups,
       "sysConfigGroupVer1": sysConfigGroupVer1,
       "commonLocalHostGroupVer1": commonLocalHostGroupVer1,
       "telephonyDnsGroupVer1": telephonyDnsGroupVer1}
)
