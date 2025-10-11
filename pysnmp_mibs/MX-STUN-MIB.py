# SNMP MIB module (MX-STUN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-STUN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:48 2025
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
 MxIpHostName,
 MxIpPort) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpHostName",
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

stunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200)
)
if mibBuilder.loadTexts:
    stunMIB.setRevisions(
        ("2004-12-10 00:00",
         "2004-11-16 00:00",
         "2004-11-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusStun_ObjectIdentity = ObjectIdentity
ipAddressStatusStun = _IpAddressStatusStun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 200)
)
_StunTable_Object = MibTable
stunTable = _StunTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 200, 50)
)
if mibBuilder.loadTexts:
    stunTable.setStatus("current")
_StunEntry_Object = MibTableRow
stunEntry = _StunEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 200, 50, 50)
)
stunEntry.setIndexNames(
    (0, "MX-STUN-MIB", "stunIndex"),
)
if mibBuilder.loadTexts:
    stunEntry.setStatus("current")


class _StunIndex_Type(Unsigned32):
    """Custom type stunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StunIndex_Type.__name__ = "Unsigned32"
_StunIndex_Object = MibTableColumn
stunIndex = _StunIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 200, 50, 50, 10),
    _StunIndex_Type()
)
stunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunIndex.setStatus("current")


class _StunHost_Type(MxIpHostName):
    """Custom type stunHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_StunHost_Type.__name__ = "MxIpHostName"
_StunHost_Object = MibTableColumn
stunHost = _StunHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 200, 50, 50, 50),
    _StunHost_Type()
)
stunHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunHost.setStatus("current")


class _StunPort_Type(MxIpPort):
    """Custom type stunPort based on MxIpPort"""
    defaultValue = 3478


_StunPort_Type.__name__ = "MxIpPort"
_StunPort_Object = MibTableColumn
stunPort = _StunPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 200, 50, 50, 100),
    _StunPort_Type()
)
stunPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunPort.setStatus("current")
_IpAddressConfigStun_ObjectIdentity = ObjectIdentity
ipAddressConfigStun = _IpAddressConfigStun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200)
)
_IpAddressConfigStunStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigStunStatic = _IpAddressConfigStunStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200, 50)
)
_StunStaticTable_Object = MibTable
stunStaticTable = _StunStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200, 50, 50)
)
if mibBuilder.loadTexts:
    stunStaticTable.setStatus("current")
_StunStaticEntry_Object = MibTableRow
stunStaticEntry = _StunStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200, 50, 50, 50)
)
stunStaticEntry.setIndexNames(
    (0, "MX-STUN-MIB", "stunStaticIndex"),
)
if mibBuilder.loadTexts:
    stunStaticEntry.setStatus("current")


class _StunStaticIndex_Type(Unsigned32):
    """Custom type stunStaticIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StunStaticIndex_Type.__name__ = "Unsigned32"
_StunStaticIndex_Object = MibTableColumn
stunStaticIndex = _StunStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200, 50, 50, 50, 10),
    _StunStaticIndex_Type()
)
stunStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunStaticIndex.setStatus("current")


class _StunStaticHost_Type(MxIpHostName):
    """Custom type stunStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_StunStaticHost_Type.__name__ = "MxIpHostName"
_StunStaticHost_Object = MibTableColumn
stunStaticHost = _StunStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200, 50, 50, 50, 50),
    _StunStaticHost_Type()
)
stunStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunStaticHost.setStatus("current")


class _StunStaticPort_Type(MxIpPort):
    """Custom type stunStaticPort based on MxIpPort"""
    defaultValue = 3478


_StunStaticPort_Type.__name__ = "MxIpPort"
_StunStaticPort_Object = MibTableColumn
stunStaticPort = _StunStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 200, 50, 50, 50, 100),
    _StunStaticPort_Type()
)
stunStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunStaticPort.setStatus("current")
_StunMIBObjects_ObjectIdentity = ObjectIdentity
stunMIBObjects = _StunMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 1)
)


class _StunEnable_Type(MxEnableState):
    """Custom type stunEnable based on MxEnableState"""
    defaultValue = 0


_StunEnable_Type.__name__ = "MxEnableState"
_StunEnable_Object = MibScalar
stunEnable = _StunEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 1, 50),
    _StunEnable_Type()
)
stunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunEnable.setStatus("current")


class _StunQueryCacheDuration_Type(Unsigned32):
    """Custom type stunQueryCacheDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_StunQueryCacheDuration_Type.__name__ = "Unsigned32"
_StunQueryCacheDuration_Object = MibScalar
stunQueryCacheDuration = _StunQueryCacheDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 1, 100),
    _StunQueryCacheDuration_Type()
)
stunQueryCacheDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunQueryCacheDuration.setStatus("current")


class _StunQueryTimeout_Type(Unsigned32):
    """Custom type stunQueryTimeout based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_StunQueryTimeout_Type.__name__ = "Unsigned32"
_StunQueryTimeout_Object = MibScalar
stunQueryTimeout = _StunQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 1, 150),
    _StunQueryTimeout_Type()
)
stunQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunQueryTimeout.setStatus("current")


class _StunKeepAliveInterval_Type(Unsigned32):
    """Custom type stunKeepAliveInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_StunKeepAliveInterval_Type.__name__ = "Unsigned32"
_StunKeepAliveInterval_Object = MibScalar
stunKeepAliveInterval = _StunKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 1, 200),
    _StunKeepAliveInterval_Type()
)
stunKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunKeepAliveInterval.setStatus("current")


class _StunNatBindingQueryInterval_Type(Unsigned32):
    """Custom type stunNatBindingQueryInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 600),
    )


_StunNatBindingQueryInterval_Type.__name__ = "Unsigned32"
_StunNatBindingQueryInterval_Object = MibScalar
stunNatBindingQueryInterval = _StunNatBindingQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 1, 250),
    _StunNatBindingQueryInterval_Type()
)
stunNatBindingQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunNatBindingQueryInterval.setStatus("current")
_StunConformance_ObjectIdentity = ObjectIdentity
stunConformance = _StunConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 2)
)
_StunCompliances_ObjectIdentity = ObjectIdentity
stunCompliances = _StunCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 2, 1)
)
_StunGroups_ObjectIdentity = ObjectIdentity
stunGroups = _StunGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 2, 2)
)

# Managed Objects groups

stunBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 2, 2, 1)
)
stunBasicGroupVer1.setObjects(
      *(("MX-STUN-MIB", "stunEnable"),
        ("MX-STUN-MIB", "stunQueryCacheDuration"),
        ("MX-STUN-MIB", "stunQueryTimeout"),
        ("MX-STUN-MIB", "stunKeepAliveInterval"),
        ("MX-STUN-MIB", "stunNatBindingQueryInterval"))
)
if mibBuilder.loadTexts:
    stunBasicGroupVer1.setStatus("current")

stunServerGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 2, 2, 2)
)
stunServerGroupVer1.setObjects(
      *(("MX-STUN-MIB", "stunHost"),
        ("MX-STUN-MIB", "stunPort"),
        ("MX-STUN-MIB", "stunStaticHost"),
        ("MX-STUN-MIB", "stunStaticPort"))
)
if mibBuilder.loadTexts:
    stunServerGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

stunComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 200, 2, 1, 1)
)
stunComplVer1.setObjects(
      *(("MX-STUN-MIB", "stunBasicGroupVer1"),
        ("MX-STUN-MIB", "stunServerGroupVer1"))
)
if mibBuilder.loadTexts:
    stunComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-STUN-MIB",
    **{"ipAddressStatusStun": ipAddressStatusStun,
       "stunTable": stunTable,
       "stunEntry": stunEntry,
       "stunIndex": stunIndex,
       "stunHost": stunHost,
       "stunPort": stunPort,
       "ipAddressConfigStun": ipAddressConfigStun,
       "ipAddressConfigStunStatic": ipAddressConfigStunStatic,
       "stunStaticTable": stunStaticTable,
       "stunStaticEntry": stunStaticEntry,
       "stunStaticIndex": stunStaticIndex,
       "stunStaticHost": stunStaticHost,
       "stunStaticPort": stunStaticPort,
       "stunMIB": stunMIB,
       "stunMIBObjects": stunMIBObjects,
       "stunEnable": stunEnable,
       "stunQueryCacheDuration": stunQueryCacheDuration,
       "stunQueryTimeout": stunQueryTimeout,
       "stunKeepAliveInterval": stunKeepAliveInterval,
       "stunNatBindingQueryInterval": stunNatBindingQueryInterval,
       "stunConformance": stunConformance,
       "stunCompliances": stunCompliances,
       "stunComplVer1": stunComplVer1,
       "stunGroups": stunGroups,
       "stunBasicGroupVer1": stunBasicGroupVer1,
       "stunServerGroupVer1": stunServerGroupVer1}
)
