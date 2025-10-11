# SNMP MIB module (MX-IP-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-IP-ROUTING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:27 2025
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
 mediatrixConfig,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "mediatrixConfig",
    "mediatrixMgmt")

(MxEnableState,
 MxIpAddress,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpAddress",
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

ipRoutingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110)
)
if mibBuilder.loadTexts:
    ipRoutingMIB.setRevisions(
        ("2011-05-09 00:00",
         "2008-07-03 00:00",
         "2006-03-06 00:00",
         "2005-09-16 00:00",
         "2005-08-12 00:00",
         "2005-05-20 00:00",
         "2005-04-22 00:00",
         "2004-09-28 00:00",
         "2004-07-14 00:00",
         "2004-02-13 00:00",
         "2003-10-24 00:00",
         "2003-10-01 00:00",
         "2003-09-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpRoutingStatus_ObjectIdentity = ObjectIdentity
ipRoutingStatus = _IpRoutingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 70)
)


class _IpRoutingMacAddress_Type(OctetString):
    """Custom type ipRoutingMacAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
    )


_IpRoutingMacAddress_Type.__name__ = "OctetString"
_IpRoutingMacAddress_Object = MibScalar
ipRoutingMacAddress = _IpRoutingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 70, 25),
    _IpRoutingMacAddress_Type()
)
ipRoutingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutingMacAddress.setStatus("current")
_IpAddressConfigLanInterface_ObjectIdentity = ObjectIdentity
ipAddressConfigLanInterface = _IpAddressConfigLanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 100)
)


class _LanStaticAddressActivation_Type(Integer32):
    """Custom type lanStaticAddressActivation based on Integer32"""
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
        *(("ipRouting", 0),
          ("vlanSubstitution", 1),
          ("always", 2))
    )


_LanStaticAddressActivation_Type.__name__ = "Integer32"
_LanStaticAddressActivation_Object = MibScalar
lanStaticAddressActivation = _LanStaticAddressActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 100, 3),
    _LanStaticAddressActivation_Type()
)
lanStaticAddressActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanStaticAddressActivation.setStatus("current")


class _LanStaticAddress_Type(MxIpAddress):
    """Custom type lanStaticAddress based on MxIpAddress"""
    defaultValue = OctetString("192.168.10.1")


_LanStaticAddress_Type.__name__ = "MxIpAddress"
_LanStaticAddress_Object = MibScalar
lanStaticAddress = _LanStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 100, 5),
    _LanStaticAddress_Type()
)
lanStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanStaticAddress.setStatus("current")


class _LanStaticNetworkMask_Type(MxIpSubnetMask):
    """Custom type lanStaticNetworkMask based on MxIpSubnetMask"""
    defaultValue = OctetString("255.255.255.0")


_LanStaticNetworkMask_Type.__name__ = "MxIpSubnetMask"
_LanStaticNetworkMask_Object = MibScalar
lanStaticNetworkMask = _LanStaticNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 100, 10),
    _LanStaticNetworkMask_Type()
)
lanStaticNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanStaticNetworkMask.setStatus("current")
_IpRoutingMIBObjects_ObjectIdentity = ObjectIdentity
ipRoutingMIBObjects = _IpRoutingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1)
)


class _IpRoutingEnable_Type(MxEnableState):
    """Custom type ipRoutingEnable based on MxEnableState"""
    defaultValue = 0


_IpRoutingEnable_Type.__name__ = "MxEnableState"
_IpRoutingEnable_Object = MibScalar
ipRoutingEnable = _IpRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 5),
    _IpRoutingEnable_Type()
)
ipRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingEnable.setStatus("current")


class _IpRoutingMode_Type(Integer32):
    """Custom type ipRoutingMode based on Integer32"""
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
        *(("tas", 0),
          ("nat", 1),
          ("normal", 2))
    )


_IpRoutingMode_Type.__name__ = "Integer32"
_IpRoutingMode_Object = MibScalar
ipRoutingMode = _IpRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 7),
    _IpRoutingMode_Type()
)
ipRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingMode.setStatus("current")
_IpRoutingDhcp_ObjectIdentity = ObjectIdentity
ipRoutingDhcp = _IpRoutingDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10)
)


class _IpRoutingDhcpServerEnable_Type(MxEnableState):
    """Custom type ipRoutingDhcpServerEnable based on MxEnableState"""
    defaultValue = 1


_IpRoutingDhcpServerEnable_Type.__name__ = "MxEnableState"
_IpRoutingDhcpServerEnable_Object = MibScalar
ipRoutingDhcpServerEnable = _IpRoutingDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 3),
    _IpRoutingDhcpServerEnable_Type()
)
ipRoutingDhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpServerEnable.setStatus("current")


class _IpRoutingDhcpServerLeaseTime_Type(Unsigned32):
    """Custom type ipRoutingDhcpServerLeaseTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 172800),
    )


_IpRoutingDhcpServerLeaseTime_Type.__name__ = "Unsigned32"
_IpRoutingDhcpServerLeaseTime_Object = MibScalar
ipRoutingDhcpServerLeaseTime = _IpRoutingDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 5),
    _IpRoutingDhcpServerLeaseTime_Type()
)
ipRoutingDhcpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpServerLeaseTime.setStatus("current")


class _IpRoutingDhcpIpLeaseRangeStart_Type(MxIpAddress):
    """Custom type ipRoutingDhcpIpLeaseRangeStart based on MxIpAddress"""
    defaultValue = OctetString("192.168.10.2")


_IpRoutingDhcpIpLeaseRangeStart_Type.__name__ = "MxIpAddress"
_IpRoutingDhcpIpLeaseRangeStart_Object = MibScalar
ipRoutingDhcpIpLeaseRangeStart = _IpRoutingDhcpIpLeaseRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 50),
    _IpRoutingDhcpIpLeaseRangeStart_Type()
)
ipRoutingDhcpIpLeaseRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpIpLeaseRangeStart.setStatus("current")


class _IpRoutingDhcpIpLeaseRangeEnd_Type(MxIpAddress):
    """Custom type ipRoutingDhcpIpLeaseRangeEnd based on MxIpAddress"""
    defaultValue = OctetString("192.168.10.254")


_IpRoutingDhcpIpLeaseRangeEnd_Type.__name__ = "MxIpAddress"
_IpRoutingDhcpIpLeaseRangeEnd_Object = MibScalar
ipRoutingDhcpIpLeaseRangeEnd = _IpRoutingDhcpIpLeaseRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 100),
    _IpRoutingDhcpIpLeaseRangeEnd_Type()
)
ipRoutingDhcpIpLeaseRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpIpLeaseRangeEnd.setStatus("current")


class _IpRoutingDhcpServerDnsFallbackEnable_Type(MxEnableState):
    """Custom type ipRoutingDhcpServerDnsFallbackEnable based on MxEnableState"""
    defaultValue = 0


_IpRoutingDhcpServerDnsFallbackEnable_Type.__name__ = "MxEnableState"
_IpRoutingDhcpServerDnsFallbackEnable_Object = MibScalar
ipRoutingDhcpServerDnsFallbackEnable = _IpRoutingDhcpServerDnsFallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 150),
    _IpRoutingDhcpServerDnsFallbackEnable_Type()
)
ipRoutingDhcpServerDnsFallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpServerDnsFallbackEnable.setStatus("current")


class _IpRoutingDhcpServerNoWanLeaseEnable_Type(MxEnableState):
    """Custom type ipRoutingDhcpServerNoWanLeaseEnable based on MxEnableState"""
    defaultValue = 0


_IpRoutingDhcpServerNoWanLeaseEnable_Type.__name__ = "MxEnableState"
_IpRoutingDhcpServerNoWanLeaseEnable_Object = MibScalar
ipRoutingDhcpServerNoWanLeaseEnable = _IpRoutingDhcpServerNoWanLeaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 200),
    _IpRoutingDhcpServerNoWanLeaseEnable_Type()
)
ipRoutingDhcpServerNoWanLeaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpServerNoWanLeaseEnable.setStatus("current")


class _IpRoutingDhcpServerNoWanLeaseTime_Type(Unsigned32):
    """Custom type ipRoutingDhcpServerNoWanLeaseTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 172800),
    )


_IpRoutingDhcpServerNoWanLeaseTime_Type.__name__ = "Unsigned32"
_IpRoutingDhcpServerNoWanLeaseTime_Object = MibScalar
ipRoutingDhcpServerNoWanLeaseTime = _IpRoutingDhcpServerNoWanLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 10, 250),
    _IpRoutingDhcpServerNoWanLeaseTime_Type()
)
ipRoutingDhcpServerNoWanLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingDhcpServerNoWanLeaseTime.setStatus("current")
_IpRoutingQos_ObjectIdentity = ObjectIdentity
ipRoutingQos = _IpRoutingQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 15)
)


class _IpRoutingQosDiffServSubstitutionEnable_Type(MxEnableState):
    """Custom type ipRoutingQosDiffServSubstitutionEnable based on MxEnableState"""
    defaultValue = 0


_IpRoutingQosDiffServSubstitutionEnable_Type.__name__ = "MxEnableState"
_IpRoutingQosDiffServSubstitutionEnable_Object = MibScalar
ipRoutingQosDiffServSubstitutionEnable = _IpRoutingQosDiffServSubstitutionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 15, 5),
    _IpRoutingQosDiffServSubstitutionEnable_Type()
)
ipRoutingQosDiffServSubstitutionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingQosDiffServSubstitutionEnable.setStatus("current")


class _IpRoutingQosDiffServSubstitution_Type(Unsigned32):
    """Custom type ipRoutingQosDiffServSubstitution based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpRoutingQosDiffServSubstitution_Type.__name__ = "Unsigned32"
_IpRoutingQosDiffServSubstitution_Object = MibScalar
ipRoutingQosDiffServSubstitution = _IpRoutingQosDiffServSubstitution_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 15, 10),
    _IpRoutingQosDiffServSubstitution_Type()
)
ipRoutingQosDiffServSubstitution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingQosDiffServSubstitution.setStatus("current")
_IpRoutingMacSpoof_ObjectIdentity = ObjectIdentity
ipRoutingMacSpoof = _IpRoutingMacSpoof_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 20)
)


class _IpRoutingMacSpoofEnable_Type(MxEnableState):
    """Custom type ipRoutingMacSpoofEnable based on MxEnableState"""
    defaultValue = 0


_IpRoutingMacSpoofEnable_Type.__name__ = "MxEnableState"
_IpRoutingMacSpoofEnable_Object = MibScalar
ipRoutingMacSpoofEnable = _IpRoutingMacSpoofEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 20, 10),
    _IpRoutingMacSpoofEnable_Type()
)
ipRoutingMacSpoofEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingMacSpoofEnable.setStatus("current")


class _IpRoutingMacSpoofAddress_Type(OctetString):
    """Custom type ipRoutingMacSpoofAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
    )


_IpRoutingMacSpoofAddress_Type.__name__ = "OctetString"
_IpRoutingMacSpoofAddress_Object = MibScalar
ipRoutingMacSpoofAddress = _IpRoutingMacSpoofAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 20, 20),
    _IpRoutingMacSpoofAddress_Type()
)
ipRoutingMacSpoofAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingMacSpoofAddress.setStatus("current")
_IpRoutingBandwidthControl_ObjectIdentity = ObjectIdentity
ipRoutingBandwidthControl = _IpRoutingBandwidthControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 30)
)


class _IpRoutingBandwidthControlEnable_Type(MxEnableState):
    """Custom type ipRoutingBandwidthControlEnable based on MxEnableState"""
    defaultValue = 0


_IpRoutingBandwidthControlEnable_Type.__name__ = "MxEnableState"
_IpRoutingBandwidthControlEnable_Object = MibScalar
ipRoutingBandwidthControlEnable = _IpRoutingBandwidthControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 30, 5),
    _IpRoutingBandwidthControlEnable_Type()
)
ipRoutingBandwidthControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingBandwidthControlEnable.setStatus("current")


class _IpRoutingWanUpstreamBandwidth_Type(Unsigned32):
    """Custom type ipRoutingWanUpstreamBandwidth based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4096),
    )


_IpRoutingWanUpstreamBandwidth_Type.__name__ = "Unsigned32"
_IpRoutingWanUpstreamBandwidth_Object = MibScalar
ipRoutingWanUpstreamBandwidth = _IpRoutingWanUpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 1, 30, 10),
    _IpRoutingWanUpstreamBandwidth_Type()
)
ipRoutingWanUpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingWanUpstreamBandwidth.setStatus("current")
_IpRoutingConformance_ObjectIdentity = ObjectIdentity
ipRoutingConformance = _IpRoutingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2)
)
_IpRoutingCompliances_ObjectIdentity = ObjectIdentity
ipRoutingCompliances = _IpRoutingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 1)
)
_IpRoutingGroups_ObjectIdentity = ObjectIdentity
ipRoutingGroups = _IpRoutingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5)
)

# Managed Objects groups

ipRoutingGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5, 5)
)
ipRoutingGroupVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "ipRoutingEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingMode"))
)
if mibBuilder.loadTexts:
    ipRoutingGroupVer1.setStatus("current")

ipRoutingDhcpGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5, 10)
)
ipRoutingDhcpGroupVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "ipRoutingDhcpServerEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpServerLeaseTime"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpIpLeaseRangeStart"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpIpLeaseRangeEnd"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpServerDnsFallbackEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpServerNoWanLeaseEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpServerNoWanLeaseTime"))
)
if mibBuilder.loadTexts:
    ipRoutingDhcpGroupVer1.setStatus("current")

ipRoutingQosGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5, 15)
)
ipRoutingQosGroupVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "ipRoutingQosDiffServSubstitutionEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingQosDiffServSubstitution"))
)
if mibBuilder.loadTexts:
    ipRoutingQosGroupVer1.setStatus("current")

ipRoutingLanInterfaceGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5, 20)
)
ipRoutingLanInterfaceGroupVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "lanStaticAddress"),
        ("MX-IP-ROUTING-MIB", "lanStaticNetworkMask"))
)
if mibBuilder.loadTexts:
    ipRoutingLanInterfaceGroupVer1.setStatus("current")

ipRoutingMacSpoofGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5, 25)
)
ipRoutingMacSpoofGroupVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "ipRoutingMacSpoofEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingMacSpoofAddress"))
)
if mibBuilder.loadTexts:
    ipRoutingMacSpoofGroupVer1.setStatus("current")

ipRoutingBandwidthControlGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 5, 30)
)
ipRoutingBandwidthControlGroupVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "ipRoutingBandwidthControlEnable"),
        ("MX-IP-ROUTING-MIB", "ipRoutingWanUpstreamBandwidth"))
)
if mibBuilder.loadTexts:
    ipRoutingBandwidthControlGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipRoutingComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 110, 2, 1, 1)
)
ipRoutingComplVer1.setObjects(
      *(("MX-IP-ROUTING-MIB", "ipRoutingGroupVer1"),
        ("MX-IP-ROUTING-MIB", "ipRoutingDhcpGroupVer1"),
        ("MX-IP-ROUTING-MIB", "ipRoutingQosGroupVer1"),
        ("MX-IP-ROUTING-MIB", "ipRoutingLanInterfaceGroupVer1"),
        ("MX-IP-ROUTING-MIB", "ipRoutingMacSpoofGroupVer1"),
        ("MX-IP-ROUTING-MIB", "ipRoutingBandwidthControlGroupVer1"))
)
if mibBuilder.loadTexts:
    ipRoutingComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-IP-ROUTING-MIB",
    **{"ipRoutingStatus": ipRoutingStatus,
       "ipRoutingMacAddress": ipRoutingMacAddress,
       "ipAddressConfigLanInterface": ipAddressConfigLanInterface,
       "lanStaticAddressActivation": lanStaticAddressActivation,
       "lanStaticAddress": lanStaticAddress,
       "lanStaticNetworkMask": lanStaticNetworkMask,
       "ipRoutingMIB": ipRoutingMIB,
       "ipRoutingMIBObjects": ipRoutingMIBObjects,
       "ipRoutingEnable": ipRoutingEnable,
       "ipRoutingMode": ipRoutingMode,
       "ipRoutingDhcp": ipRoutingDhcp,
       "ipRoutingDhcpServerEnable": ipRoutingDhcpServerEnable,
       "ipRoutingDhcpServerLeaseTime": ipRoutingDhcpServerLeaseTime,
       "ipRoutingDhcpIpLeaseRangeStart": ipRoutingDhcpIpLeaseRangeStart,
       "ipRoutingDhcpIpLeaseRangeEnd": ipRoutingDhcpIpLeaseRangeEnd,
       "ipRoutingDhcpServerDnsFallbackEnable": ipRoutingDhcpServerDnsFallbackEnable,
       "ipRoutingDhcpServerNoWanLeaseEnable": ipRoutingDhcpServerNoWanLeaseEnable,
       "ipRoutingDhcpServerNoWanLeaseTime": ipRoutingDhcpServerNoWanLeaseTime,
       "ipRoutingQos": ipRoutingQos,
       "ipRoutingQosDiffServSubstitutionEnable": ipRoutingQosDiffServSubstitutionEnable,
       "ipRoutingQosDiffServSubstitution": ipRoutingQosDiffServSubstitution,
       "ipRoutingMacSpoof": ipRoutingMacSpoof,
       "ipRoutingMacSpoofEnable": ipRoutingMacSpoofEnable,
       "ipRoutingMacSpoofAddress": ipRoutingMacSpoofAddress,
       "ipRoutingBandwidthControl": ipRoutingBandwidthControl,
       "ipRoutingBandwidthControlEnable": ipRoutingBandwidthControlEnable,
       "ipRoutingWanUpstreamBandwidth": ipRoutingWanUpstreamBandwidth,
       "ipRoutingConformance": ipRoutingConformance,
       "ipRoutingCompliances": ipRoutingCompliances,
       "ipRoutingComplVer1": ipRoutingComplVer1,
       "ipRoutingGroups": ipRoutingGroups,
       "ipRoutingGroupVer1": ipRoutingGroupVer1,
       "ipRoutingDhcpGroupVer1": ipRoutingDhcpGroupVer1,
       "ipRoutingQosGroupVer1": ipRoutingQosGroupVer1,
       "ipRoutingLanInterfaceGroupVer1": ipRoutingLanInterfaceGroupVer1,
       "ipRoutingMacSpoofGroupVer1": ipRoutingMacSpoofGroupVer1,
       "ipRoutingBandwidthControlGroupVer1": ipRoutingBandwidthControlGroupVer1}
)
