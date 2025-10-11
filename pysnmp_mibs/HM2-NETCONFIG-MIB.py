# SNMP MIB module (HM2-NETCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-NETCONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:15 2025
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(IpAddressOriginTC,) = mibBuilder.importSymbols(
    "IP-MIB",
    "IpAddressOriginTC")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2NetConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20)
)
if mibBuilder.loadTexts:
    hm2NetConfigMib.setRevisions(
        ("2011-03-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2NetConfigMibNotifications_ObjectIdentity = ObjectIdentity
hm2NetConfigMibNotifications = _Hm2NetConfigMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 0)
)
_Hm2NetConfigMibObjects_ObjectIdentity = ObjectIdentity
hm2NetConfigMibObjects = _Hm2NetConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1)
)
_Hm2NetStaticGroup_ObjectIdentity = ObjectIdentity
hm2NetStaticGroup = _Hm2NetStaticGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1)
)


class _Hm2NetConfigProtocol_Type(Integer32):
    """Custom type hm2NetConfigProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("bootp", 2),
          ("dhcp", 3))
    )


_Hm2NetConfigProtocol_Type.__name__ = "Integer32"
_Hm2NetConfigProtocol_Object = MibScalar
hm2NetConfigProtocol = _Hm2NetConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 1),
    _Hm2NetConfigProtocol_Type()
)
hm2NetConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetConfigProtocol.setStatus("current")


class _Hm2NetLocalIPAddrType_Type(InetAddressType):
    """Custom type hm2NetLocalIPAddrType based on InetAddressType"""
    defaultValue = 1


_Hm2NetLocalIPAddrType_Type.__name__ = "InetAddressType"
_Hm2NetLocalIPAddrType_Object = MibScalar
hm2NetLocalIPAddrType = _Hm2NetLocalIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 2),
    _Hm2NetLocalIPAddrType_Type()
)
hm2NetLocalIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetLocalIPAddrType.setStatus("current")


class _Hm2NetLocalIPAddr_Type(InetAddress):
    """Custom type hm2NetLocalIPAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2NetLocalIPAddr_Type.__name__ = "InetAddress"
_Hm2NetLocalIPAddr_Object = MibScalar
hm2NetLocalIPAddr = _Hm2NetLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 3),
    _Hm2NetLocalIPAddr_Type()
)
hm2NetLocalIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetLocalIPAddr.setStatus("current")


class _Hm2NetPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hm2NetPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_Hm2NetPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_Hm2NetPrefixLength_Object = MibScalar
hm2NetPrefixLength = _Hm2NetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 4),
    _Hm2NetPrefixLength_Type()
)
hm2NetPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetPrefixLength.setStatus("current")


class _Hm2NetGatewayIPAddrType_Type(InetAddressType):
    """Custom type hm2NetGatewayIPAddrType based on InetAddressType"""
    defaultValue = 1


_Hm2NetGatewayIPAddrType_Type.__name__ = "InetAddressType"
_Hm2NetGatewayIPAddrType_Object = MibScalar
hm2NetGatewayIPAddrType = _Hm2NetGatewayIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 5),
    _Hm2NetGatewayIPAddrType_Type()
)
hm2NetGatewayIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetGatewayIPAddrType.setStatus("current")


class _Hm2NetGatewayIPAddr_Type(InetAddress):
    """Custom type hm2NetGatewayIPAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2NetGatewayIPAddr_Type.__name__ = "InetAddress"
_Hm2NetGatewayIPAddr_Object = MibScalar
hm2NetGatewayIPAddr = _Hm2NetGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 6),
    _Hm2NetGatewayIPAddr_Type()
)
hm2NetGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetGatewayIPAddr.setStatus("current")


class _Hm2NetVlanID_Type(Integer32):
    """Custom type hm2NetVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2NetVlanID_Type.__name__ = "Integer32"
_Hm2NetVlanID_Object = MibScalar
hm2NetVlanID = _Hm2NetVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 7),
    _Hm2NetVlanID_Type()
)
hm2NetVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetVlanID.setStatus("current")


class _Hm2NetVlanPriority_Type(Integer32):
    """Custom type hm2NetVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2NetVlanPriority_Type.__name__ = "Integer32"
_Hm2NetVlanPriority_Object = MibScalar
hm2NetVlanPriority = _Hm2NetVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 8),
    _Hm2NetVlanPriority_Type()
)
hm2NetVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetVlanPriority.setStatus("current")


class _Hm2NetIpDscpPriority_Type(Integer32):
    """Custom type hm2NetIpDscpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2NetIpDscpPriority_Type.__name__ = "Integer32"
_Hm2NetIpDscpPriority_Object = MibScalar
hm2NetIpDscpPriority = _Hm2NetIpDscpPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 9),
    _Hm2NetIpDscpPriority_Type()
)
hm2NetIpDscpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIpDscpPriority.setStatus("current")


class _Hm2NetMgmtPort_Type(Integer32):
    """Custom type hm2NetMgmtPort based on Integer32"""
    defaultValue = 0


_Hm2NetMgmtPort_Type.__name__ = "Integer32"
_Hm2NetMgmtPort_Object = MibScalar
hm2NetMgmtPort = _Hm2NetMgmtPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 10),
    _Hm2NetMgmtPort_Type()
)
hm2NetMgmtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetMgmtPort.setStatus("current")


class _Hm2NetDHCPClientId_Type(DisplayString):
    """Custom type hm2NetDHCPClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2NetDHCPClientId_Type.__name__ = "DisplayString"
_Hm2NetDHCPClientId_Object = MibScalar
hm2NetDHCPClientId = _Hm2NetDHCPClientId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 11),
    _Hm2NetDHCPClientId_Type()
)
hm2NetDHCPClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetDHCPClientId.setStatus("current")


class _Hm2NetDHCPClientConfigLoad_Type(HmEnabledStatus):
    """Custom type hm2NetDHCPClientConfigLoad based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetDHCPClientConfigLoad_Type.__name__ = "HmEnabledStatus"
_Hm2NetDHCPClientConfigLoad_Object = MibScalar
hm2NetDHCPClientConfigLoad = _Hm2NetDHCPClientConfigLoad_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 20),
    _Hm2NetDHCPClientConfigLoad_Type()
)
hm2NetDHCPClientConfigLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetDHCPClientConfigLoad.setStatus("current")
_Hm2NetDHCPClientLeaseTime_Type = Unsigned32
_Hm2NetDHCPClientLeaseTime_Object = MibScalar
hm2NetDHCPClientLeaseTime = _Hm2NetDHCPClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 21),
    _Hm2NetDHCPClientLeaseTime_Type()
)
hm2NetDHCPClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetDHCPClientLeaseTime.setStatus("current")


class _Hm2NetIPv6AdminStatus_Type(HmEnabledStatus):
    """Custom type hm2NetIPv6AdminStatus based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetIPv6AdminStatus_Type.__name__ = "HmEnabledStatus"
_Hm2NetIPv6AdminStatus_Object = MibScalar
hm2NetIPv6AdminStatus = _Hm2NetIPv6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 30),
    _Hm2NetIPv6AdminStatus_Type()
)
hm2NetIPv6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6AdminStatus.setStatus("current")


class _Hm2NetIPv6ConfigProtocol_Type(Integer32):
    """Custom type hm2NetIPv6ConfigProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto", 2),
          ("dhcpv6", 3),
          ("all", 4))
    )


_Hm2NetIPv6ConfigProtocol_Type.__name__ = "Integer32"
_Hm2NetIPv6ConfigProtocol_Object = MibScalar
hm2NetIPv6ConfigProtocol = _Hm2NetIPv6ConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 31),
    _Hm2NetIPv6ConfigProtocol_Type()
)
hm2NetIPv6ConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6ConfigProtocol.setStatus("current")


class _Hm2NetIPv6GatewayAddrType_Type(InetAddressType):
    """Custom type hm2NetIPv6GatewayAddrType based on InetAddressType"""
    defaultValue = 2


_Hm2NetIPv6GatewayAddrType_Type.__name__ = "InetAddressType"
_Hm2NetIPv6GatewayAddrType_Object = MibScalar
hm2NetIPv6GatewayAddrType = _Hm2NetIPv6GatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 32),
    _Hm2NetIPv6GatewayAddrType_Type()
)
hm2NetIPv6GatewayAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6GatewayAddrType.setStatus("current")


class _Hm2NetIPv6GatewayAddr_Type(InetAddress):
    """Custom type hm2NetIPv6GatewayAddr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"


_Hm2NetIPv6GatewayAddr_Type.__name__ = "InetAddress"
_Hm2NetIPv6GatewayAddr_Object = MibScalar
hm2NetIPv6GatewayAddr = _Hm2NetIPv6GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 33),
    _Hm2NetIPv6GatewayAddr_Type()
)
hm2NetIPv6GatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6GatewayAddr.setStatus("current")


class _Hm2NetIPv6DupAddrDetectTrans_Type(Integer32):
    """Custom type hm2NetIPv6DupAddrDetectTrans based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Hm2NetIPv6DupAddrDetectTrans_Type.__name__ = "Integer32"
_Hm2NetIPv6DupAddrDetectTrans_Object = MibScalar
hm2NetIPv6DupAddrDetectTrans = _Hm2NetIPv6DupAddrDetectTrans_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 34),
    _Hm2NetIPv6DupAddrDetectTrans_Type()
)
hm2NetIPv6DupAddrDetectTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6DupAddrDetectTrans.setStatus("current")


class _Hm2NetIPv6DHCPClientId_Type(DisplayString):
    """Custom type hm2NetIPv6DHCPClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2NetIPv6DHCPClientId_Type.__name__ = "DisplayString"
_Hm2NetIPv6DHCPClientId_Object = MibScalar
hm2NetIPv6DHCPClientId = _Hm2NetIPv6DHCPClientId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 35),
    _Hm2NetIPv6DHCPClientId_Type()
)
hm2NetIPv6DHCPClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetIPv6DHCPClientId.setStatus("current")
_Hm2NetIPv6LocalAddrTable_Object = MibTable
hm2NetIPv6LocalAddrTable = _Hm2NetIPv6LocalAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36)
)
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrTable.setStatus("current")
_Hm2NetIPv6LocalAddrEntry_Object = MibTableRow
hm2NetIPv6LocalAddrEntry = _Hm2NetIPv6LocalAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1)
)
hm2NetIPv6LocalAddrEntry.setIndexNames(
    (0, "HM2-NETCONFIG-MIB", "hm2NetIPv6LocalAddrPrefixType"),
    (0, "HM2-NETCONFIG-MIB", "hm2NetIPv6LocalAddrPrefix"),
    (0, "HM2-NETCONFIG-MIB", "hm2NetIPv6LocalAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrEntry.setStatus("current")
_Hm2NetIPv6LocalAddrPrefixType_Type = InetAddressType
_Hm2NetIPv6LocalAddrPrefixType_Object = MibTableColumn
hm2NetIPv6LocalAddrPrefixType = _Hm2NetIPv6LocalAddrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 1),
    _Hm2NetIPv6LocalAddrPrefixType_Type()
)
hm2NetIPv6LocalAddrPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrPrefixType.setStatus("current")
_Hm2NetIPv6LocalAddrPrefix_Type = InetAddress
_Hm2NetIPv6LocalAddrPrefix_Object = MibTableColumn
hm2NetIPv6LocalAddrPrefix = _Hm2NetIPv6LocalAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 2),
    _Hm2NetIPv6LocalAddrPrefix_Type()
)
hm2NetIPv6LocalAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrPrefix.setStatus("current")


class _Hm2NetIPv6LocalAddrPrefixLength_Type(Integer32):
    """Custom type hm2NetIPv6LocalAddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hm2NetIPv6LocalAddrPrefixLength_Type.__name__ = "Integer32"
_Hm2NetIPv6LocalAddrPrefixLength_Object = MibTableColumn
hm2NetIPv6LocalAddrPrefixLength = _Hm2NetIPv6LocalAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 3),
    _Hm2NetIPv6LocalAddrPrefixLength_Type()
)
hm2NetIPv6LocalAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrPrefixLength.setStatus("current")


class _Hm2NetIPv6LocalAddrType_Type(InetAddressType):
    """Custom type hm2NetIPv6LocalAddrType based on InetAddressType"""
    defaultValue = 2


_Hm2NetIPv6LocalAddrType_Type.__name__ = "InetAddressType"
_Hm2NetIPv6LocalAddrType_Object = MibTableColumn
hm2NetIPv6LocalAddrType = _Hm2NetIPv6LocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 4),
    _Hm2NetIPv6LocalAddrType_Type()
)
hm2NetIPv6LocalAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrType.setStatus("current")


class _Hm2NetIPv6LocalAddr_Type(InetAddress):
    """Custom type hm2NetIPv6LocalAddr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"


_Hm2NetIPv6LocalAddr_Type.__name__ = "InetAddress"
_Hm2NetIPv6LocalAddr_Object = MibTableColumn
hm2NetIPv6LocalAddr = _Hm2NetIPv6LocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 5),
    _Hm2NetIPv6LocalAddr_Type()
)
hm2NetIPv6LocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddr.setStatus("current")


class _Hm2NetIPv6LocalAddrEuiFlag_Type(HmEnabledStatus):
    """Custom type hm2NetIPv6LocalAddrEuiFlag based on HmEnabledStatus"""
    defaultValue = 2


_Hm2NetIPv6LocalAddrEuiFlag_Type.__name__ = "HmEnabledStatus"
_Hm2NetIPv6LocalAddrEuiFlag_Object = MibTableColumn
hm2NetIPv6LocalAddrEuiFlag = _Hm2NetIPv6LocalAddrEuiFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 6),
    _Hm2NetIPv6LocalAddrEuiFlag_Type()
)
hm2NetIPv6LocalAddrEuiFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrEuiFlag.setStatus("current")


class _Hm2NetIPv6LocalAddrOrigin_Type(IpAddressOriginTC):
    """Custom type hm2NetIPv6LocalAddrOrigin based on IpAddressOriginTC"""
    defaultValue = 2


_Hm2NetIPv6LocalAddrOrigin_Type.__name__ = "IpAddressOriginTC"
_Hm2NetIPv6LocalAddrOrigin_Object = MibTableColumn
hm2NetIPv6LocalAddrOrigin = _Hm2NetIPv6LocalAddrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 7),
    _Hm2NetIPv6LocalAddrOrigin_Type()
)
hm2NetIPv6LocalAddrOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrOrigin.setStatus("current")
_Hm2NetIPv6LocalAddrStatus_Type = RowStatus
_Hm2NetIPv6LocalAddrStatus_Object = MibTableColumn
hm2NetIPv6LocalAddrStatus = _Hm2NetIPv6LocalAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 36, 1, 8),
    _Hm2NetIPv6LocalAddrStatus_Type()
)
hm2NetIPv6LocalAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2NetIPv6LocalAddrStatus.setStatus("current")


class _Hm2NetAction_Type(Integer32):
    """Custom type hm2NetAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2))
    )


_Hm2NetAction_Type.__name__ = "Integer32"
_Hm2NetAction_Object = MibScalar
hm2NetAction = _Hm2NetAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 1, 50),
    _Hm2NetAction_Type()
)
hm2NetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetAction.setStatus("current")
_Hm2NetACDGroup_ObjectIdentity = ObjectIdentity
hm2NetACDGroup = _Hm2NetACDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2)
)


class _Hm2NetACDStatus_Type(HmEnabledStatus):
    """Custom type hm2NetACDStatus based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetACDStatus_Type.__name__ = "HmEnabledStatus"
_Hm2NetACDStatus_Object = MibScalar
hm2NetACDStatus = _Hm2NetACDStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 1),
    _Hm2NetACDStatus_Type()
)
hm2NetACDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDStatus.setStatus("current")


class _Hm2NetACDDetectionMode_Type(Integer32):
    """Custom type hm2NetACDDetectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeAndPassive", 1),
          ("activeDetectionOnly", 2),
          ("passiveDetectionOnly", 3))
    )


_Hm2NetACDDetectionMode_Type.__name__ = "Integer32"
_Hm2NetACDDetectionMode_Object = MibScalar
hm2NetACDDetectionMode = _Hm2NetACDDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 2),
    _Hm2NetACDDetectionMode_Type()
)
hm2NetACDDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDDetectionMode.setStatus("current")


class _Hm2NetACDOngoingProbeStatus_Type(HmEnabledStatus):
    """Custom type hm2NetACDOngoingProbeStatus based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetACDOngoingProbeStatus_Type.__name__ = "HmEnabledStatus"
_Hm2NetACDOngoingProbeStatus_Object = MibScalar
hm2NetACDOngoingProbeStatus = _Hm2NetACDOngoingProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 3),
    _Hm2NetACDOngoingProbeStatus_Type()
)
hm2NetACDOngoingProbeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDOngoingProbeStatus.setStatus("current")


class _Hm2NetACDDelay_Type(Integer32):
    """Custom type hm2NetACDDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 500),
    )


_Hm2NetACDDelay_Type.__name__ = "Integer32"
_Hm2NetACDDelay_Object = MibScalar
hm2NetACDDelay = _Hm2NetACDDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 5),
    _Hm2NetACDDelay_Type()
)
hm2NetACDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDDelay.setStatus("current")


class _Hm2NetACDReleaseDelay_Type(Integer32):
    """Custom type hm2NetACDReleaseDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_Hm2NetACDReleaseDelay_Type.__name__ = "Integer32"
_Hm2NetACDReleaseDelay_Object = MibScalar
hm2NetACDReleaseDelay = _Hm2NetACDReleaseDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 7),
    _Hm2NetACDReleaseDelay_Type()
)
hm2NetACDReleaseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDReleaseDelay.setStatus("current")


class _Hm2NetACDMaxProtection_Type(Integer32):
    """Custom type hm2NetACDMaxProtection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2NetACDMaxProtection_Type.__name__ = "Integer32"
_Hm2NetACDMaxProtection_Object = MibScalar
hm2NetACDMaxProtection = _Hm2NetACDMaxProtection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 9),
    _Hm2NetACDMaxProtection_Type()
)
hm2NetACDMaxProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDMaxProtection.setStatus("current")


class _Hm2NetACDProtectInterval_Type(Integer32):
    """Custom type hm2NetACDProtectInterval based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 10000),
    )


_Hm2NetACDProtectInterval_Type.__name__ = "Integer32"
_Hm2NetACDProtectInterval_Object = MibScalar
hm2NetACDProtectInterval = _Hm2NetACDProtectInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 11),
    _Hm2NetACDProtectInterval_Type()
)
hm2NetACDProtectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDProtectInterval.setStatus("current")


class _Hm2NetACDFaultState_Type(Integer32):
    """Custom type hm2NetACDFaultState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Hm2NetACDFaultState_Type.__name__ = "Integer32"
_Hm2NetACDFaultState_Object = MibScalar
hm2NetACDFaultState = _Hm2NetACDFaultState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 13),
    _Hm2NetACDFaultState_Type()
)
hm2NetACDFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetACDFaultState.setStatus("current")


class _Hm2NetACDTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2NetACDTrapEnable based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetACDTrapEnable_Type.__name__ = "HmEnabledStatus"
_Hm2NetACDTrapEnable_Object = MibScalar
hm2NetACDTrapEnable = _Hm2NetACDTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 15),
    _Hm2NetACDTrapEnable_Type()
)
hm2NetACDTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetACDTrapEnable.setStatus("current")
_Hm2NetACDAddrTable_Object = MibTable
hm2NetACDAddrTable = _Hm2NetACDAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20)
)
if mibBuilder.loadTexts:
    hm2NetACDAddrTable.setStatus("current")
_Hm2NetACDAddrEntry_Object = MibTableRow
hm2NetACDAddrEntry = _Hm2NetACDAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20, 1)
)
hm2NetACDAddrEntry.setIndexNames(
    (0, "HM2-NETCONFIG-MIB", "hm2NetACDTimeMark"),
)
if mibBuilder.loadTexts:
    hm2NetACDAddrEntry.setStatus("current")
_Hm2NetACDTimeMark_Type = TimeFilter
_Hm2NetACDTimeMark_Object = MibTableColumn
hm2NetACDTimeMark = _Hm2NetACDTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20, 1, 1),
    _Hm2NetACDTimeMark_Type()
)
hm2NetACDTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetACDTimeMark.setStatus("current")
_Hm2NetACDAddrType_Type = InetAddressType
_Hm2NetACDAddrType_Object = MibTableColumn
hm2NetACDAddrType = _Hm2NetACDAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20, 1, 3),
    _Hm2NetACDAddrType_Type()
)
hm2NetACDAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetACDAddrType.setStatus("current")
_Hm2NetACDIPAddr_Type = InetAddress
_Hm2NetACDIPAddr_Object = MibTableColumn
hm2NetACDIPAddr = _Hm2NetACDIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20, 1, 5),
    _Hm2NetACDIPAddr_Type()
)
hm2NetACDIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetACDIPAddr.setStatus("current")
_Hm2NetACDMAC_Type = MacAddress
_Hm2NetACDMAC_Object = MibTableColumn
hm2NetACDMAC = _Hm2NetACDMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20, 1, 7),
    _Hm2NetACDMAC_Type()
)
hm2NetACDMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetACDMAC.setStatus("current")
_Hm2NetACDifIndex_Type = InterfaceIndex
_Hm2NetACDifIndex_Object = MibTableColumn
hm2NetACDifIndex = _Hm2NetACDifIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 2, 20, 1, 9),
    _Hm2NetACDifIndex_Type()
)
hm2NetACDifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetACDifIndex.setStatus("current")
_Hm2NetMacGroup_ObjectIdentity = ObjectIdentity
hm2NetMacGroup = _Hm2NetMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 3)
)
_Hm2NetLocalBurnedInMacAddr_Type = MacAddress
_Hm2NetLocalBurnedInMacAddr_Object = MibScalar
hm2NetLocalBurnedInMacAddr = _Hm2NetLocalBurnedInMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 3, 1),
    _Hm2NetLocalBurnedInMacAddr_Type()
)
hm2NetLocalBurnedInMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetLocalBurnedInMacAddr.setStatus("current")


class _Hm2NetLocalAdminMacAddress_Type(MacAddress):
    """Custom type hm2NetLocalAdminMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_Hm2NetLocalAdminMacAddress_Type.__name__ = "MacAddress"
_Hm2NetLocalAdminMacAddress_Object = MibScalar
hm2NetLocalAdminMacAddress = _Hm2NetLocalAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 3, 2),
    _Hm2NetLocalAdminMacAddress_Type()
)
hm2NetLocalAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetLocalAdminMacAddress.setStatus("current")


class _Hm2NetMacAddressType_Type(Integer32):
    """Custom type hm2NetMacAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("burned-in", 1),
          ("local", 2))
    )


_Hm2NetMacAddressType_Type.__name__ = "Integer32"
_Hm2NetMacAddressType_Object = MibScalar
hm2NetMacAddressType = _Hm2NetMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 3, 3),
    _Hm2NetMacAddressType_Type()
)
hm2NetMacAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetMacAddressType.setStatus("current")
_Hm2NetHiDiscoveryGroup_ObjectIdentity = ObjectIdentity
hm2NetHiDiscoveryGroup = _Hm2NetHiDiscoveryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 4)
)


class _Hm2NetHiDiscoveryOperation_Type(HmEnabledStatus):
    """Custom type hm2NetHiDiscoveryOperation based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetHiDiscoveryOperation_Type.__name__ = "HmEnabledStatus"
_Hm2NetHiDiscoveryOperation_Object = MibScalar
hm2NetHiDiscoveryOperation = _Hm2NetHiDiscoveryOperation_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 4, 1),
    _Hm2NetHiDiscoveryOperation_Type()
)
hm2NetHiDiscoveryOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetHiDiscoveryOperation.setStatus("current")


class _Hm2NetHiDiscoveryMode_Type(Integer32):
    """Custom type hm2NetHiDiscoveryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readWrite", 1),
          ("readOnly", 2))
    )


_Hm2NetHiDiscoveryMode_Type.__name__ = "Integer32"
_Hm2NetHiDiscoveryMode_Object = MibScalar
hm2NetHiDiscoveryMode = _Hm2NetHiDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 4, 2),
    _Hm2NetHiDiscoveryMode_Type()
)
hm2NetHiDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetHiDiscoveryMode.setStatus("current")


class _Hm2NetHiDiscoveryBlinking_Type(HmEnabledStatus):
    """Custom type hm2NetHiDiscoveryBlinking based on HmEnabledStatus"""
    defaultValue = 2


_Hm2NetHiDiscoveryBlinking_Type.__name__ = "HmEnabledStatus"
_Hm2NetHiDiscoveryBlinking_Object = MibScalar
hm2NetHiDiscoveryBlinking = _Hm2NetHiDiscoveryBlinking_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 4, 3),
    _Hm2NetHiDiscoveryBlinking_Type()
)
hm2NetHiDiscoveryBlinking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetHiDiscoveryBlinking.setStatus("current")


class _Hm2NetHiDiscoveryProtocol_Type(Bits):
    """Custom type hm2NetHiDiscoveryProtocol based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("v1", 1),
          ("v2", 2))
    )

_Hm2NetHiDiscoveryProtocol_Type.__name__ = "Bits"
_Hm2NetHiDiscoveryProtocol_Object = MibScalar
hm2NetHiDiscoveryProtocol = _Hm2NetHiDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 4, 4),
    _Hm2NetHiDiscoveryProtocol_Type()
)
hm2NetHiDiscoveryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetHiDiscoveryProtocol.setStatus("current")


class _Hm2NetHiDiscoveryRelay_Type(HmEnabledStatus):
    """Custom type hm2NetHiDiscoveryRelay based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetHiDiscoveryRelay_Type.__name__ = "HmEnabledStatus"
_Hm2NetHiDiscoveryRelay_Object = MibScalar
hm2NetHiDiscoveryRelay = _Hm2NetHiDiscoveryRelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 4, 5),
    _Hm2NetHiDiscoveryRelay_Type()
)
hm2NetHiDiscoveryRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetHiDiscoveryRelay.setStatus("current")
_Hm2NetMacACDGroup_ObjectIdentity = ObjectIdentity
hm2NetMacACDGroup = _Hm2NetMacACDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 5)
)


class _Hm2NetMacACDStatus_Type(HmEnabledStatus):
    """Custom type hm2NetMacACDStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2NetMacACDStatus_Type.__name__ = "HmEnabledStatus"
_Hm2NetMacACDStatus_Object = MibScalar
hm2NetMacACDStatus = _Hm2NetMacACDStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 5, 1),
    _Hm2NetMacACDStatus_Type()
)
hm2NetMacACDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetMacACDStatus.setStatus("current")
_Hm2NetMacACDConflictAddress_Type = MacAddress
_Hm2NetMacACDConflictAddress_Object = MibScalar
hm2NetMacACDConflictAddress = _Hm2NetMacACDConflictAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 5, 2),
    _Hm2NetMacACDConflictAddress_Type()
)
hm2NetMacACDConflictAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetMacACDConflictAddress.setStatus("current")
_Hm2NetOobMgmtGroup_ObjectIdentity = ObjectIdentity
hm2NetOobMgmtGroup = _Hm2NetOobMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6)
)


class _Hm2NetOobMgmtAdminState_Type(HmEnabledStatus):
    """Custom type hm2NetOobMgmtAdminState based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetOobMgmtAdminState_Type.__name__ = "HmEnabledStatus"
_Hm2NetOobMgmtAdminState_Object = MibScalar
hm2NetOobMgmtAdminState = _Hm2NetOobMgmtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 1),
    _Hm2NetOobMgmtAdminState_Type()
)
hm2NetOobMgmtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtAdminState.setStatus("current")


class _Hm2NetOobMgmtProtocol_Type(Integer32):
    """Custom type hm2NetOobMgmtProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("bootp", 2),
          ("dhcp", 3))
    )


_Hm2NetOobMgmtProtocol_Type.__name__ = "Integer32"
_Hm2NetOobMgmtProtocol_Object = MibScalar
hm2NetOobMgmtProtocol = _Hm2NetOobMgmtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 2),
    _Hm2NetOobMgmtProtocol_Type()
)
hm2NetOobMgmtProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtProtocol.setStatus("current")


class _Hm2NetOobMgmtIPAddrType_Type(InetAddressType):
    """Custom type hm2NetOobMgmtIPAddrType based on InetAddressType"""
    defaultValue = 1


_Hm2NetOobMgmtIPAddrType_Type.__name__ = "InetAddressType"
_Hm2NetOobMgmtIPAddrType_Object = MibScalar
hm2NetOobMgmtIPAddrType = _Hm2NetOobMgmtIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 3),
    _Hm2NetOobMgmtIPAddrType_Type()
)
hm2NetOobMgmtIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtIPAddrType.setStatus("current")


class _Hm2NetOobMgmtIPAddr_Type(InetAddress):
    """Custom type hm2NetOobMgmtIPAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2NetOobMgmtIPAddr_Type.__name__ = "InetAddress"
_Hm2NetOobMgmtIPAddr_Object = MibScalar
hm2NetOobMgmtIPAddr = _Hm2NetOobMgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 4),
    _Hm2NetOobMgmtIPAddr_Type()
)
hm2NetOobMgmtIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtIPAddr.setStatus("current")


class _Hm2NetOobMgmtPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hm2NetOobMgmtPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_Hm2NetOobMgmtPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_Hm2NetOobMgmtPrefixLength_Object = MibScalar
hm2NetOobMgmtPrefixLength = _Hm2NetOobMgmtPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 5),
    _Hm2NetOobMgmtPrefixLength_Type()
)
hm2NetOobMgmtPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtPrefixLength.setStatus("current")


class _Hm2NetOobMgmtGatewayIPAddrType_Type(InetAddressType):
    """Custom type hm2NetOobMgmtGatewayIPAddrType based on InetAddressType"""
    defaultValue = 1


_Hm2NetOobMgmtGatewayIPAddrType_Type.__name__ = "InetAddressType"
_Hm2NetOobMgmtGatewayIPAddrType_Object = MibScalar
hm2NetOobMgmtGatewayIPAddrType = _Hm2NetOobMgmtGatewayIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 6),
    _Hm2NetOobMgmtGatewayIPAddrType_Type()
)
hm2NetOobMgmtGatewayIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtGatewayIPAddrType.setStatus("current")


class _Hm2NetOobMgmtGatewayIPAddr_Type(InetAddress):
    """Custom type hm2NetOobMgmtGatewayIPAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2NetOobMgmtGatewayIPAddr_Type.__name__ = "InetAddress"
_Hm2NetOobMgmtGatewayIPAddr_Object = MibScalar
hm2NetOobMgmtGatewayIPAddr = _Hm2NetOobMgmtGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 7),
    _Hm2NetOobMgmtGatewayIPAddr_Type()
)
hm2NetOobMgmtGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtGatewayIPAddr.setStatus("current")
_Hm2NetOobMgmtMacAddress_Type = MacAddress
_Hm2NetOobMgmtMacAddress_Object = MibScalar
hm2NetOobMgmtMacAddress = _Hm2NetOobMgmtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 8),
    _Hm2NetOobMgmtMacAddress_Type()
)
hm2NetOobMgmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetOobMgmtMacAddress.setStatus("current")


class _Hm2NetOobMgmtOperState_Type(Integer32):
    """Custom type hm2NetOobMgmtOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Hm2NetOobMgmtOperState_Type.__name__ = "Integer32"
_Hm2NetOobMgmtOperState_Object = MibScalar
hm2NetOobMgmtOperState = _Hm2NetOobMgmtOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 9),
    _Hm2NetOobMgmtOperState_Type()
)
hm2NetOobMgmtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetOobMgmtOperState.setStatus("current")
_Hm2NetOobMgmtDHCPClientLeaseTime_Type = Unsigned32
_Hm2NetOobMgmtDHCPClientLeaseTime_Object = MibScalar
hm2NetOobMgmtDHCPClientLeaseTime = _Hm2NetOobMgmtDHCPClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 10),
    _Hm2NetOobMgmtDHCPClientLeaseTime_Type()
)
hm2NetOobMgmtDHCPClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetOobMgmtDHCPClientLeaseTime.setStatus("current")


class _Hm2NetOobMgmtAction_Type(Integer32):
    """Custom type hm2NetOobMgmtAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2))
    )


_Hm2NetOobMgmtAction_Type.__name__ = "Integer32"
_Hm2NetOobMgmtAction_Object = MibScalar
hm2NetOobMgmtAction = _Hm2NetOobMgmtAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 6, 50),
    _Hm2NetOobMgmtAction_Type()
)
hm2NetOobMgmtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobMgmtAction.setStatus("current")
_Hm2NetOobUsbMgmtGroup_ObjectIdentity = ObjectIdentity
hm2NetOobUsbMgmtGroup = _Hm2NetOobUsbMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7)
)


class _Hm2NetOobUsbMgmtAdminState_Type(HmEnabledStatus):
    """Custom type hm2NetOobUsbMgmtAdminState based on HmEnabledStatus"""
    defaultValue = 1


_Hm2NetOobUsbMgmtAdminState_Type.__name__ = "HmEnabledStatus"
_Hm2NetOobUsbMgmtAdminState_Object = MibScalar
hm2NetOobUsbMgmtAdminState = _Hm2NetOobUsbMgmtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 1),
    _Hm2NetOobUsbMgmtAdminState_Type()
)
hm2NetOobUsbMgmtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtAdminState.setStatus("current")


class _Hm2NetOobUsbMgmtIPAddrType_Type(InetAddressType):
    """Custom type hm2NetOobUsbMgmtIPAddrType based on InetAddressType"""
    defaultValue = 1


_Hm2NetOobUsbMgmtIPAddrType_Type.__name__ = "InetAddressType"
_Hm2NetOobUsbMgmtIPAddrType_Object = MibScalar
hm2NetOobUsbMgmtIPAddrType = _Hm2NetOobUsbMgmtIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 3),
    _Hm2NetOobUsbMgmtIPAddrType_Type()
)
hm2NetOobUsbMgmtIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtIPAddrType.setStatus("current")


class _Hm2NetOobUsbMgmtIPAddr_Type(InetAddress):
    """Custom type hm2NetOobUsbMgmtIPAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2NetOobUsbMgmtIPAddr_Type.__name__ = "InetAddress"
_Hm2NetOobUsbMgmtIPAddr_Object = MibScalar
hm2NetOobUsbMgmtIPAddr = _Hm2NetOobUsbMgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 4),
    _Hm2NetOobUsbMgmtIPAddr_Type()
)
hm2NetOobUsbMgmtIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtIPAddr.setStatus("current")


class _Hm2NetOobUsbMgmtPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hm2NetOobUsbMgmtPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_Hm2NetOobUsbMgmtPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_Hm2NetOobUsbMgmtPrefixLength_Object = MibScalar
hm2NetOobUsbMgmtPrefixLength = _Hm2NetOobUsbMgmtPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 5),
    _Hm2NetOobUsbMgmtPrefixLength_Type()
)
hm2NetOobUsbMgmtPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtPrefixLength.setStatus("current")
_Hm2NetOobUsbMgmtHostMacAddress_Type = MacAddress
_Hm2NetOobUsbMgmtHostMacAddress_Object = MibScalar
hm2NetOobUsbMgmtHostMacAddress = _Hm2NetOobUsbMgmtHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 7),
    _Hm2NetOobUsbMgmtHostMacAddress_Type()
)
hm2NetOobUsbMgmtHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtHostMacAddress.setStatus("current")
_Hm2NetOobUsbMgmtDeviceMacAddress_Type = MacAddress
_Hm2NetOobUsbMgmtDeviceMacAddress_Object = MibScalar
hm2NetOobUsbMgmtDeviceMacAddress = _Hm2NetOobUsbMgmtDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 8),
    _Hm2NetOobUsbMgmtDeviceMacAddress_Type()
)
hm2NetOobUsbMgmtDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtDeviceMacAddress.setStatus("current")


class _Hm2NetOobUsbMgmtAction_Type(Integer32):
    """Custom type hm2NetOobUsbMgmtAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2))
    )


_Hm2NetOobUsbMgmtAction_Type.__name__ = "Integer32"
_Hm2NetOobUsbMgmtAction_Object = MibScalar
hm2NetOobUsbMgmtAction = _Hm2NetOobUsbMgmtAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 1, 7, 50),
    _Hm2NetOobUsbMgmtAction_Type()
)
hm2NetOobUsbMgmtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NetOobUsbMgmtAction.setStatus("current")

# Managed Objects groups


# Notification objects

hm2NetACDNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 0, 1)
)
hm2NetACDNotification.setObjects(
      *(("HM2-NETCONFIG-MIB", "hm2NetACDTimeMark"),
        ("HM2-NETCONFIG-MIB", "hm2NetACDAddrType"),
        ("HM2-NETCONFIG-MIB", "hm2NetACDIPAddr"),
        ("HM2-NETCONFIG-MIB", "hm2NetACDMAC"),
        ("HM2-NETCONFIG-MIB", "hm2NetACDifIndex"))
)
if mibBuilder.loadTexts:
    hm2NetACDNotification.setStatus(
        "current"
    )

hm2NetMacACDNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 20, 0, 2)
)
hm2NetMacACDNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HM2-NETCONFIG-MIB", "hm2NetMacACDConflictAddress"))
)
if mibBuilder.loadTexts:
    hm2NetMacACDNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-NETCONFIG-MIB",
    **{"hm2NetConfigMib": hm2NetConfigMib,
       "hm2NetConfigMibNotifications": hm2NetConfigMibNotifications,
       "hm2NetACDNotification": hm2NetACDNotification,
       "hm2NetMacACDNotification": hm2NetMacACDNotification,
       "hm2NetConfigMibObjects": hm2NetConfigMibObjects,
       "hm2NetStaticGroup": hm2NetStaticGroup,
       "hm2NetConfigProtocol": hm2NetConfigProtocol,
       "hm2NetLocalIPAddrType": hm2NetLocalIPAddrType,
       "hm2NetLocalIPAddr": hm2NetLocalIPAddr,
       "hm2NetPrefixLength": hm2NetPrefixLength,
       "hm2NetGatewayIPAddrType": hm2NetGatewayIPAddrType,
       "hm2NetGatewayIPAddr": hm2NetGatewayIPAddr,
       "hm2NetVlanID": hm2NetVlanID,
       "hm2NetVlanPriority": hm2NetVlanPriority,
       "hm2NetIpDscpPriority": hm2NetIpDscpPriority,
       "hm2NetMgmtPort": hm2NetMgmtPort,
       "hm2NetDHCPClientId": hm2NetDHCPClientId,
       "hm2NetDHCPClientConfigLoad": hm2NetDHCPClientConfigLoad,
       "hm2NetDHCPClientLeaseTime": hm2NetDHCPClientLeaseTime,
       "hm2NetIPv6AdminStatus": hm2NetIPv6AdminStatus,
       "hm2NetIPv6ConfigProtocol": hm2NetIPv6ConfigProtocol,
       "hm2NetIPv6GatewayAddrType": hm2NetIPv6GatewayAddrType,
       "hm2NetIPv6GatewayAddr": hm2NetIPv6GatewayAddr,
       "hm2NetIPv6DupAddrDetectTrans": hm2NetIPv6DupAddrDetectTrans,
       "hm2NetIPv6DHCPClientId": hm2NetIPv6DHCPClientId,
       "hm2NetIPv6LocalAddrTable": hm2NetIPv6LocalAddrTable,
       "hm2NetIPv6LocalAddrEntry": hm2NetIPv6LocalAddrEntry,
       "hm2NetIPv6LocalAddrPrefixType": hm2NetIPv6LocalAddrPrefixType,
       "hm2NetIPv6LocalAddrPrefix": hm2NetIPv6LocalAddrPrefix,
       "hm2NetIPv6LocalAddrPrefixLength": hm2NetIPv6LocalAddrPrefixLength,
       "hm2NetIPv6LocalAddrType": hm2NetIPv6LocalAddrType,
       "hm2NetIPv6LocalAddr": hm2NetIPv6LocalAddr,
       "hm2NetIPv6LocalAddrEuiFlag": hm2NetIPv6LocalAddrEuiFlag,
       "hm2NetIPv6LocalAddrOrigin": hm2NetIPv6LocalAddrOrigin,
       "hm2NetIPv6LocalAddrStatus": hm2NetIPv6LocalAddrStatus,
       "hm2NetAction": hm2NetAction,
       "hm2NetACDGroup": hm2NetACDGroup,
       "hm2NetACDStatus": hm2NetACDStatus,
       "hm2NetACDDetectionMode": hm2NetACDDetectionMode,
       "hm2NetACDOngoingProbeStatus": hm2NetACDOngoingProbeStatus,
       "hm2NetACDDelay": hm2NetACDDelay,
       "hm2NetACDReleaseDelay": hm2NetACDReleaseDelay,
       "hm2NetACDMaxProtection": hm2NetACDMaxProtection,
       "hm2NetACDProtectInterval": hm2NetACDProtectInterval,
       "hm2NetACDFaultState": hm2NetACDFaultState,
       "hm2NetACDTrapEnable": hm2NetACDTrapEnable,
       "hm2NetACDAddrTable": hm2NetACDAddrTable,
       "hm2NetACDAddrEntry": hm2NetACDAddrEntry,
       "hm2NetACDTimeMark": hm2NetACDTimeMark,
       "hm2NetACDAddrType": hm2NetACDAddrType,
       "hm2NetACDIPAddr": hm2NetACDIPAddr,
       "hm2NetACDMAC": hm2NetACDMAC,
       "hm2NetACDifIndex": hm2NetACDifIndex,
       "hm2NetMacGroup": hm2NetMacGroup,
       "hm2NetLocalBurnedInMacAddr": hm2NetLocalBurnedInMacAddr,
       "hm2NetLocalAdminMacAddress": hm2NetLocalAdminMacAddress,
       "hm2NetMacAddressType": hm2NetMacAddressType,
       "hm2NetHiDiscoveryGroup": hm2NetHiDiscoveryGroup,
       "hm2NetHiDiscoveryOperation": hm2NetHiDiscoveryOperation,
       "hm2NetHiDiscoveryMode": hm2NetHiDiscoveryMode,
       "hm2NetHiDiscoveryBlinking": hm2NetHiDiscoveryBlinking,
       "hm2NetHiDiscoveryProtocol": hm2NetHiDiscoveryProtocol,
       "hm2NetHiDiscoveryRelay": hm2NetHiDiscoveryRelay,
       "hm2NetMacACDGroup": hm2NetMacACDGroup,
       "hm2NetMacACDStatus": hm2NetMacACDStatus,
       "hm2NetMacACDConflictAddress": hm2NetMacACDConflictAddress,
       "hm2NetOobMgmtGroup": hm2NetOobMgmtGroup,
       "hm2NetOobMgmtAdminState": hm2NetOobMgmtAdminState,
       "hm2NetOobMgmtProtocol": hm2NetOobMgmtProtocol,
       "hm2NetOobMgmtIPAddrType": hm2NetOobMgmtIPAddrType,
       "hm2NetOobMgmtIPAddr": hm2NetOobMgmtIPAddr,
       "hm2NetOobMgmtPrefixLength": hm2NetOobMgmtPrefixLength,
       "hm2NetOobMgmtGatewayIPAddrType": hm2NetOobMgmtGatewayIPAddrType,
       "hm2NetOobMgmtGatewayIPAddr": hm2NetOobMgmtGatewayIPAddr,
       "hm2NetOobMgmtMacAddress": hm2NetOobMgmtMacAddress,
       "hm2NetOobMgmtOperState": hm2NetOobMgmtOperState,
       "hm2NetOobMgmtDHCPClientLeaseTime": hm2NetOobMgmtDHCPClientLeaseTime,
       "hm2NetOobMgmtAction": hm2NetOobMgmtAction,
       "hm2NetOobUsbMgmtGroup": hm2NetOobUsbMgmtGroup,
       "hm2NetOobUsbMgmtAdminState": hm2NetOobUsbMgmtAdminState,
       "hm2NetOobUsbMgmtIPAddrType": hm2NetOobUsbMgmtIPAddrType,
       "hm2NetOobUsbMgmtIPAddr": hm2NetOobUsbMgmtIPAddr,
       "hm2NetOobUsbMgmtPrefixLength": hm2NetOobUsbMgmtPrefixLength,
       "hm2NetOobUsbMgmtHostMacAddress": hm2NetOobUsbMgmtHostMacAddress,
       "hm2NetOobUsbMgmtDeviceMacAddress": hm2NetOobUsbMgmtDeviceMacAddress,
       "hm2NetOobUsbMgmtAction": hm2NetOobUsbMgmtAction}
)
