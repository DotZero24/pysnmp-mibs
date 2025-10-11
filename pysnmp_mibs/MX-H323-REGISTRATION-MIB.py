# SNMP MIB module (MX-H323-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-H323-REGISTRATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:38 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(h323,
 ipAddressConfigH323Dhcp,
 ipAddressConfigH323Static,
 ipAddressStatusH323) = mibBuilder.importSymbols(
    "MX-H323-MIB",
    "h323",
    "ipAddressConfigH323Dhcp",
    "ipAddressConfigH323Static",
    "ipAddressStatusH323")

(groupIndex,) = mibBuilder.importSymbols(
    "MX-LINE-GROUPING-MIB",
    "groupIndex")

(ipAddressConfig,
 ipAddressStatus) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus")

(MxEnableState,
 MxIpAddress,
 MxIpDhcpSiteSpecificCode,
 MxIpPort) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpAddress",
    "MxIpDhcpSiteSpecificCode",
    "MxIpPort")

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

h323RegistrationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1)
)
if mibBuilder.loadTexts:
    h323RegistrationMIB.setRevisions(
        ("1903-03-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusH323GatekeeperTable_Object = MibTable
ipAddressStatusH323GatekeeperTable = _IpAddressStatusH323GatekeeperTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 20)
)
if mibBuilder.loadTexts:
    ipAddressStatusH323GatekeeperTable.setStatus("current")
_IpAddressStatusH323GatekeeperEntry_Object = MibTableRow
ipAddressStatusH323GatekeeperEntry = _IpAddressStatusH323GatekeeperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 20, 1)
)
ipAddressStatusH323GatekeeperEntry.setIndexNames(
    (0, "MX-H323-REGISTRATION-MIB", "ipAddressStatusH323GkIndex"),
)
if mibBuilder.loadTexts:
    ipAddressStatusH323GatekeeperEntry.setStatus("current")
_IpAddressStatusH323GkIndex_Type = Unsigned32
_IpAddressStatusH323GkIndex_Object = MibTableColumn
ipAddressStatusH323GkIndex = _IpAddressStatusH323GkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 20, 1, 5),
    _IpAddressStatusH323GkIndex_Type()
)
ipAddressStatusH323GkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressStatusH323GkIndex.setStatus("current")


class _IpAddressStatusH323GkHost_Type(MxIpAddress):
    """Custom type ipAddressStatusH323GkHost based on MxIpAddress"""
    defaultValue = OctetString("")


_IpAddressStatusH323GkHost_Type.__name__ = "MxIpAddress"
_IpAddressStatusH323GkHost_Object = MibTableColumn
ipAddressStatusH323GkHost = _IpAddressStatusH323GkHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 20, 1, 10),
    _IpAddressStatusH323GkHost_Type()
)
ipAddressStatusH323GkHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatusH323GkHost.setStatus("current")


class _IpAddressStatusH323GkPort_Type(MxIpPort):
    """Custom type ipAddressStatusH323GkPort based on MxIpPort"""
    defaultValue = 1719


_IpAddressStatusH323GkPort_Type.__name__ = "MxIpPort"
_IpAddressStatusH323GkPort_Object = MibTableColumn
ipAddressStatusH323GkPort = _IpAddressStatusH323GkPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 20, 1, 15),
    _IpAddressStatusH323GkPort_Type()
)
ipAddressStatusH323GkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatusH323GkPort.setStatus("current")
_IpAddressConfigH323GatekeeperTable_Object = MibTable
ipAddressConfigH323GatekeeperTable = _IpAddressConfigH323GatekeeperTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10, 15)
)
if mibBuilder.loadTexts:
    ipAddressConfigH323GatekeeperTable.setStatus("current")
_IpAddressConfigH323GatekeeperEntry_Object = MibTableRow
ipAddressConfigH323GatekeeperEntry = _IpAddressConfigH323GatekeeperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10, 15, 1)
)
ipAddressConfigH323GatekeeperEntry.setIndexNames(
    (0, "MX-H323-REGISTRATION-MIB", "ipAddressConfigH323GkIndex"),
)
if mibBuilder.loadTexts:
    ipAddressConfigH323GatekeeperEntry.setStatus("current")
_IpAddressConfigH323GkIndex_Type = Unsigned32
_IpAddressConfigH323GkIndex_Object = MibTableColumn
ipAddressConfigH323GkIndex = _IpAddressConfigH323GkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10, 15, 1, 5),
    _IpAddressConfigH323GkIndex_Type()
)
ipAddressConfigH323GkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressConfigH323GkIndex.setStatus("current")


class _IpAddressConfigH323GkStaticHost_Type(MxIpAddress):
    """Custom type ipAddressConfigH323GkStaticHost based on MxIpAddress"""
    defaultValue = OctetString("")


_IpAddressConfigH323GkStaticHost_Type.__name__ = "MxIpAddress"
_IpAddressConfigH323GkStaticHost_Object = MibTableColumn
ipAddressConfigH323GkStaticHost = _IpAddressConfigH323GkStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10, 15, 1, 10),
    _IpAddressConfigH323GkStaticHost_Type()
)
ipAddressConfigH323GkStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressConfigH323GkStaticHost.setStatus("current")


class _IpAddressConfigH323GkStaticPort_Type(MxIpPort):
    """Custom type ipAddressConfigH323GkStaticPort based on MxIpPort"""
    defaultValue = 1719


_IpAddressConfigH323GkStaticPort_Type.__name__ = "MxIpPort"
_IpAddressConfigH323GkStaticPort_Object = MibTableColumn
ipAddressConfigH323GkStaticPort = _IpAddressConfigH323GkStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10, 15, 1, 15),
    _IpAddressConfigH323GkStaticPort_Type()
)
ipAddressConfigH323GkStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressConfigH323GkStaticPort.setStatus("current")


class _H323GkDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type h323GkDhcpSiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_H323GkDhcpSiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_H323GkDhcpSiteSpecificCode_Object = MibScalar
h323GkDhcpSiteSpecificCode = _H323GkDhcpSiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 15, 10),
    _H323GkDhcpSiteSpecificCode_Type()
)
h323GkDhcpSiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GkDhcpSiteSpecificCode.setStatus("current")
_H323RegistrationMIBObjects_ObjectIdentity = ObjectIdentity
h323RegistrationMIBObjects = _H323RegistrationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1)
)


class _H323RegMethod_Type(Integer32):
    """Custom type h323RegMethod based on Integer32"""
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
        *(("none", 0),
          ("single", 1),
          ("multiple", 2))
    )


_H323RegMethod_Type.__name__ = "Integer32"
_H323RegMethod_Object = MibScalar
h323RegMethod = _H323RegMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 5),
    _H323RegMethod_Type()
)
h323RegMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323RegMethod.setStatus("current")
_H323RegistrationSingleRegistration_ObjectIdentity = ObjectIdentity
h323RegistrationSingleRegistration = _H323RegistrationSingleRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10)
)


class _H323SingleRegGkDiscoveryMode_Type(Integer32):
    """Custom type h323SingleRegGkDiscoveryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_H323SingleRegGkDiscoveryMode_Type.__name__ = "Integer32"
_H323SingleRegGkDiscoveryMode_Object = MibScalar
h323SingleRegGkDiscoveryMode = _H323SingleRegGkDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 5),
    _H323SingleRegGkDiscoveryMode_Type()
)
h323SingleRegGkDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegGkDiscoveryMode.setStatus("current")


class _H323SingleRegRetryTime_Type(Unsigned32):
    """Custom type h323SingleRegRetryTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H323SingleRegRetryTime_Type.__name__ = "Unsigned32"
_H323SingleRegRetryTime_Object = MibScalar
h323SingleRegRetryTime = _H323SingleRegRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 10),
    _H323SingleRegRetryTime_Type()
)
h323SingleRegRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegRetryTime.setStatus("current")


class _H323SingleRegLightweightEnable_Type(MxEnableState):
    """Custom type h323SingleRegLightweightEnable based on MxEnableState"""
    defaultValue = 1


_H323SingleRegLightweightEnable_Type.__name__ = "MxEnableState"
_H323SingleRegLightweightEnable_Object = MibScalar
h323SingleRegLightweightEnable = _H323SingleRegLightweightEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 15),
    _H323SingleRegLightweightEnable_Type()
)
h323SingleRegLightweightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegLightweightEnable.setStatus("current")


class _H323SingleRegLightweightTimeToLive_Type(Unsigned32):
    """Custom type h323SingleRegLightweightTimeToLive based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H323SingleRegLightweightTimeToLive_Type.__name__ = "Unsigned32"
_H323SingleRegLightweightTimeToLive_Object = MibScalar
h323SingleRegLightweightTimeToLive = _H323SingleRegLightweightTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 20),
    _H323SingleRegLightweightTimeToLive_Type()
)
h323SingleRegLightweightTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegLightweightTimeToLive.setStatus("current")


class _H323SingleRegRasPortSource_Type(Integer32):
    """Custom type h323SingleRegRasPortSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_H323SingleRegRasPortSource_Type.__name__ = "Integer32"
_H323SingleRegRasPortSource_Object = MibScalar
h323SingleRegRasPortSource = _H323SingleRegRasPortSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 30),
    _H323SingleRegRasPortSource_Type()
)
h323SingleRegRasPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegRasPortSource.setStatus("current")


class _H323SingleRegStaticRasPort_Type(Unsigned32):
    """Custom type h323SingleRegStaticRasPort based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1719, 1720),
        ValueRangeConstraint(7000, 65535),
    )


_H323SingleRegStaticRasPort_Type.__name__ = "Unsigned32"
_H323SingleRegStaticRasPort_Object = MibScalar
h323SingleRegStaticRasPort = _H323SingleRegStaticRasPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 35),
    _H323SingleRegStaticRasPort_Type()
)
h323SingleRegStaticRasPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegStaticRasPort.setStatus("current")


class _H323SingleRegCallSignalingPortSource_Type(Integer32):
    """Custom type h323SingleRegCallSignalingPortSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_H323SingleRegCallSignalingPortSource_Type.__name__ = "Integer32"
_H323SingleRegCallSignalingPortSource_Object = MibScalar
h323SingleRegCallSignalingPortSource = _H323SingleRegCallSignalingPortSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 40),
    _H323SingleRegCallSignalingPortSource_Type()
)
h323SingleRegCallSignalingPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegCallSignalingPortSource.setStatus("current")


class _H323SingleRegStaticCallSignalingPort_Type(Unsigned32):
    """Custom type h323SingleRegStaticCallSignalingPort based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1719, 1720),
        ValueRangeConstraint(7000, 65535),
    )


_H323SingleRegStaticCallSignalingPort_Type.__name__ = "Unsigned32"
_H323SingleRegStaticCallSignalingPort_Object = MibScalar
h323SingleRegStaticCallSignalingPort = _H323SingleRegStaticCallSignalingPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 10, 45),
    _H323SingleRegStaticCallSignalingPort_Type()
)
h323SingleRegStaticCallSignalingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SingleRegStaticCallSignalingPort.setStatus("current")
_H323RegistrationMultipleRegistrationIfTable_Object = MibTable
h323RegistrationMultipleRegistrationIfTable = _H323RegistrationMultipleRegistrationIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15)
)
if mibBuilder.loadTexts:
    h323RegistrationMultipleRegistrationIfTable.setStatus("current")
_H323RegistrationMultipleRegistrationIfEntry_Object = MibTableRow
h323RegistrationMultipleRegistrationIfEntry = _H323RegistrationMultipleRegistrationIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1)
)
h323RegistrationMultipleRegistrationIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323RegistrationMultipleRegistrationIfEntry.setStatus("current")


class _H323MultipleRegGroupIndex_Type(Unsigned32):
    """Custom type h323MultipleRegGroupIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_H323MultipleRegGroupIndex_Type.__name__ = "Unsigned32"
_H323MultipleRegGroupIndex_Object = MibTableColumn
h323MultipleRegGroupIndex = _H323MultipleRegGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 5),
    _H323MultipleRegGroupIndex_Type()
)
h323MultipleRegGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323MultipleRegGroupIndex.setStatus("current")


class _H323MultipleRegEnable_Type(MxEnableState):
    """Custom type h323MultipleRegEnable based on MxEnableState"""
    defaultValue = 1


_H323MultipleRegEnable_Type.__name__ = "MxEnableState"
_H323MultipleRegEnable_Object = MibTableColumn
h323MultipleRegEnable = _H323MultipleRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 10),
    _H323MultipleRegEnable_Type()
)
h323MultipleRegEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegEnable.setStatus("current")


class _H323MultipleRegGkDiscoveryMode_Type(Integer32):
    """Custom type h323MultipleRegGkDiscoveryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_H323MultipleRegGkDiscoveryMode_Type.__name__ = "Integer32"
_H323MultipleRegGkDiscoveryMode_Object = MibTableColumn
h323MultipleRegGkDiscoveryMode = _H323MultipleRegGkDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 15),
    _H323MultipleRegGkDiscoveryMode_Type()
)
h323MultipleRegGkDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegGkDiscoveryMode.setStatus("current")


class _H323MultipleRegRetryTime_Type(Unsigned32):
    """Custom type h323MultipleRegRetryTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H323MultipleRegRetryTime_Type.__name__ = "Unsigned32"
_H323MultipleRegRetryTime_Object = MibTableColumn
h323MultipleRegRetryTime = _H323MultipleRegRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 20),
    _H323MultipleRegRetryTime_Type()
)
h323MultipleRegRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegRetryTime.setStatus("current")


class _H323MultipleRegLightweightEnable_Type(MxEnableState):
    """Custom type h323MultipleRegLightweightEnable based on MxEnableState"""
    defaultValue = 1


_H323MultipleRegLightweightEnable_Type.__name__ = "MxEnableState"
_H323MultipleRegLightweightEnable_Object = MibTableColumn
h323MultipleRegLightweightEnable = _H323MultipleRegLightweightEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 25),
    _H323MultipleRegLightweightEnable_Type()
)
h323MultipleRegLightweightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegLightweightEnable.setStatus("current")


class _H323MultipleRegLightweightTimeToLive_Type(Unsigned32):
    """Custom type h323MultipleRegLightweightTimeToLive based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H323MultipleRegLightweightTimeToLive_Type.__name__ = "Unsigned32"
_H323MultipleRegLightweightTimeToLive_Object = MibTableColumn
h323MultipleRegLightweightTimeToLive = _H323MultipleRegLightweightTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 30),
    _H323MultipleRegLightweightTimeToLive_Type()
)
h323MultipleRegLightweightTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegLightweightTimeToLive.setStatus("current")


class _H323MultipleRegRasPortSource_Type(Integer32):
    """Custom type h323MultipleRegRasPortSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_H323MultipleRegRasPortSource_Type.__name__ = "Integer32"
_H323MultipleRegRasPortSource_Object = MibTableColumn
h323MultipleRegRasPortSource = _H323MultipleRegRasPortSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 35),
    _H323MultipleRegRasPortSource_Type()
)
h323MultipleRegRasPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegRasPortSource.setStatus("current")


class _H323MultipleRegStaticRasPort_Type(Unsigned32):
    """Custom type h323MultipleRegStaticRasPort based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1719, 1720),
        ValueRangeConstraint(7000, 65535),
    )


_H323MultipleRegStaticRasPort_Type.__name__ = "Unsigned32"
_H323MultipleRegStaticRasPort_Object = MibTableColumn
h323MultipleRegStaticRasPort = _H323MultipleRegStaticRasPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 40),
    _H323MultipleRegStaticRasPort_Type()
)
h323MultipleRegStaticRasPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegStaticRasPort.setStatus("current")


class _H323MultipleRegCallSignalingPortSource_Type(Integer32):
    """Custom type h323MultipleRegCallSignalingPortSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_H323MultipleRegCallSignalingPortSource_Type.__name__ = "Integer32"
_H323MultipleRegCallSignalingPortSource_Object = MibTableColumn
h323MultipleRegCallSignalingPortSource = _H323MultipleRegCallSignalingPortSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 45),
    _H323MultipleRegCallSignalingPortSource_Type()
)
h323MultipleRegCallSignalingPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegCallSignalingPortSource.setStatus("current")


class _H323MultipleRegStaticCallSignalingPort_Type(Unsigned32):
    """Custom type h323MultipleRegStaticCallSignalingPort based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1719, 1720),
        ValueRangeConstraint(7000, 65535),
    )


_H323MultipleRegStaticCallSignalingPort_Type.__name__ = "Unsigned32"
_H323MultipleRegStaticCallSignalingPort_Object = MibTableColumn
h323MultipleRegStaticCallSignalingPort = _H323MultipleRegStaticCallSignalingPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 15, 1, 50),
    _H323MultipleRegStaticCallSignalingPort_Type()
)
h323MultipleRegStaticCallSignalingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MultipleRegStaticCallSignalingPort.setStatus("current")
_H323RegistrationMultipleRegistrationGroupTable_Object = MibTable
h323RegistrationMultipleRegistrationGroupTable = _H323RegistrationMultipleRegistrationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17)
)
if mibBuilder.loadTexts:
    h323RegistrationMultipleRegistrationGroupTable.setStatus("current")
_H323RegistrationMultipleRegistrationGroupEntry_Object = MibTableRow
h323RegistrationMultipleRegistrationGroupEntry = _H323RegistrationMultipleRegistrationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1)
)
h323RegistrationMultipleRegistrationGroupEntry.setIndexNames(
    (0, "MX-LINE-GROUPING-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    h323RegistrationMultipleRegistrationGroupEntry.setStatus("current")


class _H323GroupMultipleRegEnable_Type(MxEnableState):
    """Custom type h323GroupMultipleRegEnable based on MxEnableState"""
    defaultValue = 1


_H323GroupMultipleRegEnable_Type.__name__ = "MxEnableState"
_H323GroupMultipleRegEnable_Object = MibTableColumn
h323GroupMultipleRegEnable = _H323GroupMultipleRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 5),
    _H323GroupMultipleRegEnable_Type()
)
h323GroupMultipleRegEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegEnable.setStatus("current")


class _H323GroupMultipleRegGkDiscoveryMode_Type(Integer32):
    """Custom type h323GroupMultipleRegGkDiscoveryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_H323GroupMultipleRegGkDiscoveryMode_Type.__name__ = "Integer32"
_H323GroupMultipleRegGkDiscoveryMode_Object = MibTableColumn
h323GroupMultipleRegGkDiscoveryMode = _H323GroupMultipleRegGkDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 10),
    _H323GroupMultipleRegGkDiscoveryMode_Type()
)
h323GroupMultipleRegGkDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegGkDiscoveryMode.setStatus("current")


class _H323GroupMultipleRegRetryTime_Type(Unsigned32):
    """Custom type h323GroupMultipleRegRetryTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H323GroupMultipleRegRetryTime_Type.__name__ = "Unsigned32"
_H323GroupMultipleRegRetryTime_Object = MibTableColumn
h323GroupMultipleRegRetryTime = _H323GroupMultipleRegRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 15),
    _H323GroupMultipleRegRetryTime_Type()
)
h323GroupMultipleRegRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegRetryTime.setStatus("current")


class _H323GroupMultipleRegLightweightEnable_Type(MxEnableState):
    """Custom type h323GroupMultipleRegLightweightEnable based on MxEnableState"""
    defaultValue = 1


_H323GroupMultipleRegLightweightEnable_Type.__name__ = "MxEnableState"
_H323GroupMultipleRegLightweightEnable_Object = MibTableColumn
h323GroupMultipleRegLightweightEnable = _H323GroupMultipleRegLightweightEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 20),
    _H323GroupMultipleRegLightweightEnable_Type()
)
h323GroupMultipleRegLightweightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegLightweightEnable.setStatus("current")


class _H323GroupMultipleRegLightweightTimeToLive_Type(Unsigned32):
    """Custom type h323GroupMultipleRegLightweightTimeToLive based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H323GroupMultipleRegLightweightTimeToLive_Type.__name__ = "Unsigned32"
_H323GroupMultipleRegLightweightTimeToLive_Object = MibTableColumn
h323GroupMultipleRegLightweightTimeToLive = _H323GroupMultipleRegLightweightTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 25),
    _H323GroupMultipleRegLightweightTimeToLive_Type()
)
h323GroupMultipleRegLightweightTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegLightweightTimeToLive.setStatus("current")


class _H323GroupMultipleRegRasPortSource_Type(Integer32):
    """Custom type h323GroupMultipleRegRasPortSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_H323GroupMultipleRegRasPortSource_Type.__name__ = "Integer32"
_H323GroupMultipleRegRasPortSource_Object = MibTableColumn
h323GroupMultipleRegRasPortSource = _H323GroupMultipleRegRasPortSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 30),
    _H323GroupMultipleRegRasPortSource_Type()
)
h323GroupMultipleRegRasPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegRasPortSource.setStatus("current")


class _H323GroupMultipleRegStaticRasPort_Type(Unsigned32):
    """Custom type h323GroupMultipleRegStaticRasPort based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1719, 1720),
        ValueRangeConstraint(7000, 65535),
    )


_H323GroupMultipleRegStaticRasPort_Type.__name__ = "Unsigned32"
_H323GroupMultipleRegStaticRasPort_Object = MibTableColumn
h323GroupMultipleRegStaticRasPort = _H323GroupMultipleRegStaticRasPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 35),
    _H323GroupMultipleRegStaticRasPort_Type()
)
h323GroupMultipleRegStaticRasPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegStaticRasPort.setStatus("current")


class _H323GroupMultipleRegCallSignalingPortSource_Type(Integer32):
    """Custom type h323GroupMultipleRegCallSignalingPortSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_H323GroupMultipleRegCallSignalingPortSource_Type.__name__ = "Integer32"
_H323GroupMultipleRegCallSignalingPortSource_Object = MibTableColumn
h323GroupMultipleRegCallSignalingPortSource = _H323GroupMultipleRegCallSignalingPortSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 40),
    _H323GroupMultipleRegCallSignalingPortSource_Type()
)
h323GroupMultipleRegCallSignalingPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegCallSignalingPortSource.setStatus("current")


class _H323GroupMultipleRegStaticCallSignalingPort_Type(Unsigned32):
    """Custom type h323GroupMultipleRegStaticCallSignalingPort based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1719, 1720),
        ValueRangeConstraint(7000, 65535),
    )


_H323GroupMultipleRegStaticCallSignalingPort_Type.__name__ = "Unsigned32"
_H323GroupMultipleRegStaticCallSignalingPort_Object = MibTableColumn
h323GroupMultipleRegStaticCallSignalingPort = _H323GroupMultipleRegStaticCallSignalingPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 17, 1, 45),
    _H323GroupMultipleRegStaticCallSignalingPort_Type()
)
h323GroupMultipleRegStaticCallSignalingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupMultipleRegStaticCallSignalingPort.setStatus("current")
_H323RegistrationStatusIfTable_Object = MibTable
h323RegistrationStatusIfTable = _H323RegistrationStatusIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 19)
)
if mibBuilder.loadTexts:
    h323RegistrationStatusIfTable.setStatus("current")
_H323RegistrationStatusIfEntry_Object = MibTableRow
h323RegistrationStatusIfEntry = _H323RegistrationStatusIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 19, 1)
)
h323RegistrationStatusIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323RegistrationStatusIfEntry.setStatus("current")


class _H323RegistrationGkHost_Type(MxIpAddress):
    """Custom type h323RegistrationGkHost based on MxIpAddress"""
    defaultValue = OctetString("")


_H323RegistrationGkHost_Type.__name__ = "MxIpAddress"
_H323RegistrationGkHost_Object = MibTableColumn
h323RegistrationGkHost = _H323RegistrationGkHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 19, 1, 5),
    _H323RegistrationGkHost_Type()
)
h323RegistrationGkHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegistrationGkHost.setStatus("current")


class _H323RegistrationGkPort_Type(OctetString):
    """Custom type h323RegistrationGkPort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_H323RegistrationGkPort_Type.__name__ = "OctetString"
_H323RegistrationGkPort_Object = MibTableColumn
h323RegistrationGkPort = _H323RegistrationGkPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 19, 1, 10),
    _H323RegistrationGkPort_Type()
)
h323RegistrationGkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegistrationGkPort.setStatus("current")


class _H323RegistrationTimeToLive_Type(OctetString):
    """Custom type h323RegistrationTimeToLive based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_H323RegistrationTimeToLive_Type.__name__ = "OctetString"
_H323RegistrationTimeToLive_Object = MibTableColumn
h323RegistrationTimeToLive = _H323RegistrationTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 1, 19, 1, 15),
    _H323RegistrationTimeToLive_Type()
)
h323RegistrationTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegistrationTimeToLive.setStatus("current")
_H323RegistrationConformance_ObjectIdentity = ObjectIdentity
h323RegistrationConformance = _H323RegistrationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2)
)
_H323RegistrationCompliances_ObjectIdentity = ObjectIdentity
h323RegistrationCompliances = _H323RegistrationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 1)
)
_H323RegistrationGroups_ObjectIdentity = ObjectIdentity
h323RegistrationGroups = _H323RegistrationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 2)
)

# Managed Objects groups

h323RegistrationSingleRegistrationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 2, 5)
)
h323RegistrationSingleRegistrationGroupVer1.setObjects(
      *(("MX-H323-REGISTRATION-MIB", "h323SingleRegGkDiscoveryMode"),
        ("MX-H323-REGISTRATION-MIB", "h323SingleRegRetryTime"),
        ("MX-H323-REGISTRATION-MIB", "h323SingleRegLightweightEnable"),
        ("MX-H323-REGISTRATION-MIB", "h323SingleRegLightweightTimeToLive"),
        ("MX-H323-REGISTRATION-MIB", "h323SingleRegRasPortSource"),
        ("MX-H323-REGISTRATION-MIB", "h323SingleRegStaticRasPort"))
)
if mibBuilder.loadTexts:
    h323RegistrationSingleRegistrationGroupVer1.setStatus("current")

h323RegistrationMultipleRegistrationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 2, 10)
)
h323RegistrationMultipleRegistrationGroupVer1.setObjects(
      *(("MX-H323-REGISTRATION-MIB", "h323MultipleRegEnable"),
        ("MX-H323-REGISTRATION-MIB", "h323MultipleRegGkDiscoveryMode"),
        ("MX-H323-REGISTRATION-MIB", "h323MultipleRegRetryTime"),
        ("MX-H323-REGISTRATION-MIB", "h323MultipleRegLightweightEnable"),
        ("MX-H323-REGISTRATION-MIB", "h323MultipleRegLightweightTimeToLive"),
        ("MX-H323-REGISTRATION-MIB", "h323MultipleRegRasPortSource"),
        ("MX-H323-REGISTRATION-MIB", "h323MultipleRegStaticRasPort"))
)
if mibBuilder.loadTexts:
    h323RegistrationMultipleRegistrationGroupVer1.setStatus("current")

h323RegistrationMultipleGroupRegistrationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 2, 15)
)
h323RegistrationMultipleGroupRegistrationGroupVer1.setObjects(
      *(("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegEnable"),
        ("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegGkDiscoveryMode"),
        ("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegRetryTime"),
        ("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegLightweightEnable"),
        ("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegLightweightTimeToLive"),
        ("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegRasPortSource"),
        ("MX-H323-REGISTRATION-MIB", "h323GroupMultipleRegStaticRasPort"))
)
if mibBuilder.loadTexts:
    h323RegistrationMultipleGroupRegistrationGroupVer1.setStatus("current")

h323RegistrationStatusGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 2, 20)
)
h323RegistrationStatusGroupVer1.setObjects(
      *(("MX-H323-REGISTRATION-MIB", "h323RegistrationGkHost"),
        ("MX-H323-REGISTRATION-MIB", "h323RegistrationGkPort"),
        ("MX-H323-REGISTRATION-MIB", "h323RegistrationTimeToLive"))
)
if mibBuilder.loadTexts:
    h323RegistrationStatusGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h323RegistrationBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 1, 2, 1, 5)
)
h323RegistrationBasicComplVer1.setObjects(
      *(("MX-H323-REGISTRATION-MIB", "h323RegistrationSingleRegistrationGroupVer1"),
        ("MX-H323-REGISTRATION-MIB", "h323RegistrationMultipleRegistrationGroupVer1"),
        ("MX-H323-REGISTRATION-MIB", "h323RegistrationMultipleGroupRegistrationGroupVer1"),
        ("MX-H323-REGISTRATION-MIB", "h323RegistrationStatusGroupVer1"))
)
if mibBuilder.loadTexts:
    h323RegistrationBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-H323-REGISTRATION-MIB",
    **{"ipAddressStatusH323GatekeeperTable": ipAddressStatusH323GatekeeperTable,
       "ipAddressStatusH323GatekeeperEntry": ipAddressStatusH323GatekeeperEntry,
       "ipAddressStatusH323GkIndex": ipAddressStatusH323GkIndex,
       "ipAddressStatusH323GkHost": ipAddressStatusH323GkHost,
       "ipAddressStatusH323GkPort": ipAddressStatusH323GkPort,
       "ipAddressConfigH323GatekeeperTable": ipAddressConfigH323GatekeeperTable,
       "ipAddressConfigH323GatekeeperEntry": ipAddressConfigH323GatekeeperEntry,
       "ipAddressConfigH323GkIndex": ipAddressConfigH323GkIndex,
       "ipAddressConfigH323GkStaticHost": ipAddressConfigH323GkStaticHost,
       "ipAddressConfigH323GkStaticPort": ipAddressConfigH323GkStaticPort,
       "h323GkDhcpSiteSpecificCode": h323GkDhcpSiteSpecificCode,
       "h323RegistrationMIB": h323RegistrationMIB,
       "h323RegistrationMIBObjects": h323RegistrationMIBObjects,
       "h323RegMethod": h323RegMethod,
       "h323RegistrationSingleRegistration": h323RegistrationSingleRegistration,
       "h323SingleRegGkDiscoveryMode": h323SingleRegGkDiscoveryMode,
       "h323SingleRegRetryTime": h323SingleRegRetryTime,
       "h323SingleRegLightweightEnable": h323SingleRegLightweightEnable,
       "h323SingleRegLightweightTimeToLive": h323SingleRegLightweightTimeToLive,
       "h323SingleRegRasPortSource": h323SingleRegRasPortSource,
       "h323SingleRegStaticRasPort": h323SingleRegStaticRasPort,
       "h323SingleRegCallSignalingPortSource": h323SingleRegCallSignalingPortSource,
       "h323SingleRegStaticCallSignalingPort": h323SingleRegStaticCallSignalingPort,
       "h323RegistrationMultipleRegistrationIfTable": h323RegistrationMultipleRegistrationIfTable,
       "h323RegistrationMultipleRegistrationIfEntry": h323RegistrationMultipleRegistrationIfEntry,
       "h323MultipleRegGroupIndex": h323MultipleRegGroupIndex,
       "h323MultipleRegEnable": h323MultipleRegEnable,
       "h323MultipleRegGkDiscoveryMode": h323MultipleRegGkDiscoveryMode,
       "h323MultipleRegRetryTime": h323MultipleRegRetryTime,
       "h323MultipleRegLightweightEnable": h323MultipleRegLightweightEnable,
       "h323MultipleRegLightweightTimeToLive": h323MultipleRegLightweightTimeToLive,
       "h323MultipleRegRasPortSource": h323MultipleRegRasPortSource,
       "h323MultipleRegStaticRasPort": h323MultipleRegStaticRasPort,
       "h323MultipleRegCallSignalingPortSource": h323MultipleRegCallSignalingPortSource,
       "h323MultipleRegStaticCallSignalingPort": h323MultipleRegStaticCallSignalingPort,
       "h323RegistrationMultipleRegistrationGroupTable": h323RegistrationMultipleRegistrationGroupTable,
       "h323RegistrationMultipleRegistrationGroupEntry": h323RegistrationMultipleRegistrationGroupEntry,
       "h323GroupMultipleRegEnable": h323GroupMultipleRegEnable,
       "h323GroupMultipleRegGkDiscoveryMode": h323GroupMultipleRegGkDiscoveryMode,
       "h323GroupMultipleRegRetryTime": h323GroupMultipleRegRetryTime,
       "h323GroupMultipleRegLightweightEnable": h323GroupMultipleRegLightweightEnable,
       "h323GroupMultipleRegLightweightTimeToLive": h323GroupMultipleRegLightweightTimeToLive,
       "h323GroupMultipleRegRasPortSource": h323GroupMultipleRegRasPortSource,
       "h323GroupMultipleRegStaticRasPort": h323GroupMultipleRegStaticRasPort,
       "h323GroupMultipleRegCallSignalingPortSource": h323GroupMultipleRegCallSignalingPortSource,
       "h323GroupMultipleRegStaticCallSignalingPort": h323GroupMultipleRegStaticCallSignalingPort,
       "h323RegistrationStatusIfTable": h323RegistrationStatusIfTable,
       "h323RegistrationStatusIfEntry": h323RegistrationStatusIfEntry,
       "h323RegistrationGkHost": h323RegistrationGkHost,
       "h323RegistrationGkPort": h323RegistrationGkPort,
       "h323RegistrationTimeToLive": h323RegistrationTimeToLive,
       "h323RegistrationConformance": h323RegistrationConformance,
       "h323RegistrationCompliances": h323RegistrationCompliances,
       "h323RegistrationBasicComplVer1": h323RegistrationBasicComplVer1,
       "h323RegistrationGroups": h323RegistrationGroups,
       "h323RegistrationSingleRegistrationGroupVer1": h323RegistrationSingleRegistrationGroupVer1,
       "h323RegistrationMultipleRegistrationGroupVer1": h323RegistrationMultipleRegistrationGroupVer1,
       "h323RegistrationMultipleGroupRegistrationGroupVer1": h323RegistrationMultipleGroupRegistrationGroupVer1,
       "h323RegistrationStatusGroupVer1": h323RegistrationStatusGroupVer1}
)
