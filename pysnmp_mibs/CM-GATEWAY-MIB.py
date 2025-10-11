# SNMP MIB module (CM-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/CM-GATEWAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:21:28 2025
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cmGw = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52)
)
if mibBuilder.loadTexts:
    cmGw.setRevisions(
        ("2013-06-07 00:00",
         "2013-06-07 00:00",
         "2013-06-07 00:00",
         "2012-12-13 00:00",
         "2012-12-12 00:00",
         "2012-12-04 00:00",
         "2012-04-17 00:00",
         "2012-04-11 00:00",
         "2011-12-19 00:00",
         "2011-05-24 00:00",
         "2009-11-17 00:00",
         "2009-06-10 00:00",
         "2009-04-28 00:00",
         "2009-01-20 00:00",
         "2008-11-18 00:00",
         "2003-07-15 00:00",
         "2002-12-09 00:00",
         "2002-10-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmGwLanClientId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class CmGwNatPacketMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("napt", 1),
          ("passthrough", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Gi_ObjectIdentity = ObjectIdentity
gi = _Gi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166)
)
_Giproducts_ObjectIdentity = ObjectIdentity
giproducts = _Giproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1)
)
_Cm_ObjectIdentity = ObjectIdentity
cm = _Cm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19)
)
_CmGwObjects_ObjectIdentity = ObjectIdentity
cmGwObjects = _CmGwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1)
)
_CmGwBaseMib_ObjectIdentity = ObjectIdentity
cmGwBaseMib = _CmGwBaseMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1)
)
_CmGwWanMacAddress_Type = PhysAddress
_CmGwWanMacAddress_Object = MibScalar
cmGwWanMacAddress = _CmGwWanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 1),
    _CmGwWanMacAddress_Type()
)
cmGwWanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwWanMacAddress.setStatus("current")
_CmGwWanSetToFactory_Type = TruthValue
_CmGwWanSetToFactory_Object = MibScalar
cmGwWanSetToFactory = _CmGwWanSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 2),
    _CmGwWanSetToFactory_Type()
)
cmGwWanSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanSetToFactory.setStatus("current")


class _CmGwWanDhcpcAdminStatus_Type(Integer32):
    """Custom type cmGwWanDhcpcAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CmGwWanDhcpcAdminStatus_Type.__name__ = "Integer32"
_CmGwWanDhcpcAdminStatus_Object = MibScalar
cmGwWanDhcpcAdminStatus = _CmGwWanDhcpcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 3),
    _CmGwWanDhcpcAdminStatus_Type()
)
cmGwWanDhcpcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanDhcpcAdminStatus.setStatus("current")
_CmGwWanInetAddressType_Type = InetAddressType
_CmGwWanInetAddressType_Object = MibScalar
cmGwWanInetAddressType = _CmGwWanInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 4),
    _CmGwWanInetAddressType_Type()
)
cmGwWanInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanInetAddressType.setStatus("current")
_CmGwWanInetAddress_Type = InetAddress
_CmGwWanInetAddress_Object = MibScalar
cmGwWanInetAddress = _CmGwWanInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 5),
    _CmGwWanInetAddress_Type()
)
cmGwWanInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanInetAddress.setStatus("current")


class _CmGwWanHostName_Type(SnmpAdminString):
    """Custom type cmGwWanHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CmGwWanHostName_Type.__name__ = "SnmpAdminString"
_CmGwWanHostName_Object = MibScalar
cmGwWanHostName = _CmGwWanHostName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 6),
    _CmGwWanHostName_Type()
)
cmGwWanHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanHostName.setStatus("current")
_CmGwWanSubnetMaskType_Type = InetAddressType
_CmGwWanSubnetMaskType_Object = MibScalar
cmGwWanSubnetMaskType = _CmGwWanSubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 7),
    _CmGwWanSubnetMaskType_Type()
)
cmGwWanSubnetMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanSubnetMaskType.setStatus("current")
_CmGwWanSubnetMask_Type = InetAddress
_CmGwWanSubnetMask_Object = MibScalar
cmGwWanSubnetMask = _CmGwWanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 8),
    _CmGwWanSubnetMask_Type()
)
cmGwWanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanSubnetMask.setStatus("current")
_CmGwWanRouterType_Type = InetAddressType
_CmGwWanRouterType_Object = MibScalar
cmGwWanRouterType = _CmGwWanRouterType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 9),
    _CmGwWanRouterType_Type()
)
cmGwWanRouterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanRouterType.setStatus("current")
_CmGwWanRouter_Type = InetAddress
_CmGwWanRouter_Object = MibScalar
cmGwWanRouter = _CmGwWanRouter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 10),
    _CmGwWanRouter_Type()
)
cmGwWanRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanRouter.setStatus("current")
_CmGwWanDnsServerTable_Object = MibTable
cmGwWanDnsServerTable = _CmGwWanDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cmGwWanDnsServerTable.setStatus("current")
_CmGwWanDnsServerEntry_Object = MibTableRow
cmGwWanDnsServerEntry = _CmGwWanDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 12, 1)
)
cmGwWanDnsServerEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwWanAddrDnsServerOrder"),
)
if mibBuilder.loadTexts:
    cmGwWanDnsServerEntry.setStatus("current")


class _CmGwWanAddrDnsServerOrder_Type(Integer32):
    """Custom type cmGwWanAddrDnsServerOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_CmGwWanAddrDnsServerOrder_Type.__name__ = "Integer32"
_CmGwWanAddrDnsServerOrder_Object = MibTableColumn
cmGwWanAddrDnsServerOrder = _CmGwWanAddrDnsServerOrder_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 12, 1, 1),
    _CmGwWanAddrDnsServerOrder_Type()
)
cmGwWanAddrDnsServerOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwWanAddrDnsServerOrder.setStatus("current")
_CmGwWanAddrDnsIpType_Type = InetAddressType
_CmGwWanAddrDnsIpType_Object = MibTableColumn
cmGwWanAddrDnsIpType = _CmGwWanAddrDnsIpType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 12, 1, 2),
    _CmGwWanAddrDnsIpType_Type()
)
cmGwWanAddrDnsIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanAddrDnsIpType.setStatus("current")
_CmGwWanAddrDnsIp_Type = InetAddress
_CmGwWanAddrDnsIp_Object = MibTableColumn
cmGwWanAddrDnsIp = _CmGwWanAddrDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 12, 1, 3),
    _CmGwWanAddrDnsIp_Type()
)
cmGwWanAddrDnsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwWanAddrDnsIp.setStatus("current")
_CmGwWanAddrDnsRowStatus_Type = RowStatus
_CmGwWanAddrDnsRowStatus_Object = MibTableColumn
cmGwWanAddrDnsRowStatus = _CmGwWanAddrDnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1, 12, 1, 4),
    _CmGwWanAddrDnsRowStatus_Type()
)
cmGwWanAddrDnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwWanAddrDnsRowStatus.setStatus("current")
_CmGwDhcpMib_ObjectIdentity = ObjectIdentity
cmGwDhcpMib = _CmGwDhcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2)
)
_CmGwDhcpObjects_ObjectIdentity = ObjectIdentity
cmGwDhcpObjects = _CmGwDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1)
)
_CmGwDhcpBase_ObjectIdentity = ObjectIdentity
cmGwDhcpBase = _CmGwDhcpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 1)
)
_CmGwLanDhcpsSetToFactory_Type = TruthValue
_CmGwLanDhcpsSetToFactory_Object = MibScalar
cmGwLanDhcpsSetToFactory = _CmGwLanDhcpsSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 1, 1),
    _CmGwLanDhcpsSetToFactory_Type()
)
cmGwLanDhcpsSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsSetToFactory.setStatus("current")
_CmGwDhcpServer_ObjectIdentity = ObjectIdentity
cmGwDhcpServer = _CmGwDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2)
)


class _CmGwLanDhcpsAddressPoolStartType_Type(InetAddressType):
    """Custom type cmGwLanDhcpsAddressPoolStartType based on InetAddressType"""
    defaultValue = 1


_CmGwLanDhcpsAddressPoolStartType_Type.__name__ = "InetAddressType"
_CmGwLanDhcpsAddressPoolStartType_Object = MibScalar
cmGwLanDhcpsAddressPoolStartType = _CmGwLanDhcpsAddressPoolStartType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 1),
    _CmGwLanDhcpsAddressPoolStartType_Type()
)
cmGwLanDhcpsAddressPoolStartType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsAddressPoolStartType.setStatus("current")


class _CmGwLanDhcpsAddressPoolStart_Type(InetAddress):
    """Custom type cmGwLanDhcpsAddressPoolStart based on InetAddress"""
    defaultHexValue = "c0a80002"


_CmGwLanDhcpsAddressPoolStart_Type.__name__ = "InetAddress"
_CmGwLanDhcpsAddressPoolStart_Object = MibScalar
cmGwLanDhcpsAddressPoolStart = _CmGwLanDhcpsAddressPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 2),
    _CmGwLanDhcpsAddressPoolStart_Type()
)
cmGwLanDhcpsAddressPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsAddressPoolStart.setStatus("current")


class _CmGwLanDhcpsNetworkNumberType_Type(InetAddressType):
    """Custom type cmGwLanDhcpsNetworkNumberType based on InetAddressType"""
    defaultValue = 1


_CmGwLanDhcpsNetworkNumberType_Type.__name__ = "InetAddressType"
_CmGwLanDhcpsNetworkNumberType_Object = MibScalar
cmGwLanDhcpsNetworkNumberType = _CmGwLanDhcpsNetworkNumberType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 3),
    _CmGwLanDhcpsNetworkNumberType_Type()
)
cmGwLanDhcpsNetworkNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsNetworkNumberType.setStatus("current")


class _CmGwLanDhcpsNetworkNumber_Type(InetAddress):
    """Custom type cmGwLanDhcpsNetworkNumber based on InetAddress"""
    defaultHexValue = "c0a80000"


_CmGwLanDhcpsNetworkNumber_Type.__name__ = "InetAddress"
_CmGwLanDhcpsNetworkNumber_Object = MibScalar
cmGwLanDhcpsNetworkNumber = _CmGwLanDhcpsNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 4),
    _CmGwLanDhcpsNetworkNumber_Type()
)
cmGwLanDhcpsNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsNetworkNumber.setStatus("current")


class _CmGwLanDhcpsSubnetMaskType_Type(InetAddressType):
    """Custom type cmGwLanDhcpsSubnetMaskType based on InetAddressType"""
    defaultValue = 1


_CmGwLanDhcpsSubnetMaskType_Type.__name__ = "InetAddressType"
_CmGwLanDhcpsSubnetMaskType_Object = MibScalar
cmGwLanDhcpsSubnetMaskType = _CmGwLanDhcpsSubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 5),
    _CmGwLanDhcpsSubnetMaskType_Type()
)
cmGwLanDhcpsSubnetMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsSubnetMaskType.setStatus("current")


class _CmGwLanDhcpsSubnetMask_Type(InetAddress):
    """Custom type cmGwLanDhcpsSubnetMask based on InetAddress"""
    defaultHexValue = "ffffff00"


_CmGwLanDhcpsSubnetMask_Type.__name__ = "InetAddress"
_CmGwLanDhcpsSubnetMask_Object = MibScalar
cmGwLanDhcpsSubnetMask = _CmGwLanDhcpsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 6),
    _CmGwLanDhcpsSubnetMask_Type()
)
cmGwLanDhcpsSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsSubnetMask.setStatus("current")


class _CmGwLanDhcpsDomainName_Type(SnmpAdminString):
    """Custom type cmGwLanDhcpsDomainName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmGwLanDhcpsDomainName_Type.__name__ = "SnmpAdminString"
_CmGwLanDhcpsDomainName_Object = MibScalar
cmGwLanDhcpsDomainName = _CmGwLanDhcpsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 7),
    _CmGwLanDhcpsDomainName_Type()
)
cmGwLanDhcpsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsDomainName.setStatus("current")


class _CmGwLanDhcpsTTL_Type(Integer32):
    """Custom type cmGwLanDhcpsTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmGwLanDhcpsTTL_Type.__name__ = "Integer32"
_CmGwLanDhcpsTTL_Object = MibScalar
cmGwLanDhcpsTTL = _CmGwLanDhcpsTTL_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 8),
    _CmGwLanDhcpsTTL_Type()
)
cmGwLanDhcpsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsTTL.setStatus("current")


class _CmGwLanDhcpsInterfaceMTU_Type(Integer32):
    """Custom type cmGwLanDhcpsInterfaceMTU based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 4096),
    )


_CmGwLanDhcpsInterfaceMTU_Type.__name__ = "Integer32"
_CmGwLanDhcpsInterfaceMTU_Object = MibScalar
cmGwLanDhcpsInterfaceMTU = _CmGwLanDhcpsInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 9),
    _CmGwLanDhcpsInterfaceMTU_Type()
)
cmGwLanDhcpsInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsInterfaceMTU.setStatus("current")


class _CmGwLanDhcpsLeaseTime_Type(Unsigned32):
    """Custom type cmGwLanDhcpsLeaseTime based on Unsigned32"""
    defaultValue = 3600


_CmGwLanDhcpsLeaseTime_Type.__name__ = "Unsigned32"
_CmGwLanDhcpsLeaseTime_Object = MibScalar
cmGwLanDhcpsLeaseTime = _CmGwLanDhcpsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 10),
    _CmGwLanDhcpsLeaseTime_Type()
)
cmGwLanDhcpsLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    cmGwLanDhcpsLeaseTime.setUnits("seconds")


class _CmGwLanDhcpsInetAddressType_Type(InetAddressType):
    """Custom type cmGwLanDhcpsInetAddressType based on InetAddressType"""
    defaultValue = 1


_CmGwLanDhcpsInetAddressType_Type.__name__ = "InetAddressType"
_CmGwLanDhcpsInetAddressType_Object = MibScalar
cmGwLanDhcpsInetAddressType = _CmGwLanDhcpsInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 11),
    _CmGwLanDhcpsInetAddressType_Type()
)
cmGwLanDhcpsInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsInetAddressType.setStatus("current")


class _CmGwLanDhcpsInetAddress_Type(InetAddress):
    """Custom type cmGwLanDhcpsInetAddress based on InetAddress"""
    defaultHexValue = "c0a80001"


_CmGwLanDhcpsInetAddress_Type.__name__ = "InetAddress"
_CmGwLanDhcpsInetAddress_Object = MibScalar
cmGwLanDhcpsInetAddress = _CmGwLanDhcpsInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 12),
    _CmGwLanDhcpsInetAddress_Type()
)
cmGwLanDhcpsInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsInetAddress.setStatus("current")


class _CmGwLanDhcpsMaxAddressCount_Type(Unsigned32):
    """Custom type cmGwLanDhcpsMaxAddressCount based on Unsigned32"""
    defaultValue = 253

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_CmGwLanDhcpsMaxAddressCount_Type.__name__ = "Unsigned32"
_CmGwLanDhcpsMaxAddressCount_Object = MibScalar
cmGwLanDhcpsMaxAddressCount = _CmGwLanDhcpsMaxAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 13),
    _CmGwLanDhcpsMaxAddressCount_Type()
)
cmGwLanDhcpsMaxAddressCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsMaxAddressCount.setStatus("current")
_CmGwLanDhcpsCurrentLeaseCount_Type = Unsigned32
_CmGwLanDhcpsCurrentLeaseCount_Object = MibScalar
cmGwLanDhcpsCurrentLeaseCount = _CmGwLanDhcpsCurrentLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 14),
    _CmGwLanDhcpsCurrentLeaseCount_Type()
)
cmGwLanDhcpsCurrentLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwLanDhcpsCurrentLeaseCount.setStatus("current")


class _CmGwLanDhcpsControl_Type(Integer32):
    """Custom type cmGwLanDhcpsControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restoreConfig", 1),
          ("commitConfig", 2))
    )


_CmGwLanDhcpsControl_Type.__name__ = "Integer32"
_CmGwLanDhcpsControl_Object = MibScalar
cmGwLanDhcpsControl = _CmGwLanDhcpsControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 15),
    _CmGwLanDhcpsControl_Type()
)
cmGwLanDhcpsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwLanDhcpsControl.setStatus("current")


class _CmGwLanDhcpsCommitStatus_Type(Integer32):
    """Custom type cmGwLanDhcpsCommitStatus based on Integer32"""
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
        *(("commitSucceeded", 1),
          ("commitNeeded", 2),
          ("commitFailed", 3))
    )


_CmGwLanDhcpsCommitStatus_Type.__name__ = "Integer32"
_CmGwLanDhcpsCommitStatus_Object = MibScalar
cmGwLanDhcpsCommitStatus = _CmGwLanDhcpsCommitStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 2, 16),
    _CmGwLanDhcpsCommitStatus_Type()
)
cmGwLanDhcpsCommitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwLanDhcpsCommitStatus.setStatus("current")
_CmGwDhcpAddr_ObjectIdentity = ObjectIdentity
cmGwDhcpAddr = _CmGwDhcpAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3)
)
_CmGwLanAddrTable_Object = MibTable
cmGwLanAddrTable = _CmGwLanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmGwLanAddrTable.setStatus("current")
_CmGwLanAddrEntry_Object = MibTableRow
cmGwLanAddrEntry = _CmGwLanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1)
)
cmGwLanAddrEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwLanAddrIpType"),
    (0, "CM-GATEWAY-MIB", "cmGwLanAddrIp"),
)
if mibBuilder.loadTexts:
    cmGwLanAddrEntry.setStatus("current")
_CmGwLanAddrIpType_Type = InetAddressType
_CmGwLanAddrIpType_Object = MibTableColumn
cmGwLanAddrIpType = _CmGwLanAddrIpType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 1),
    _CmGwLanAddrIpType_Type()
)
cmGwLanAddrIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwLanAddrIpType.setStatus("current")
_CmGwLanAddrIp_Type = InetAddress
_CmGwLanAddrIp_Object = MibTableColumn
cmGwLanAddrIp = _CmGwLanAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 2),
    _CmGwLanAddrIp_Type()
)
cmGwLanAddrIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwLanAddrIp.setStatus("current")
_CmGwLanAddrClientID_Type = CmGwLanClientId
_CmGwLanAddrClientID_Object = MibTableColumn
cmGwLanAddrClientID = _CmGwLanAddrClientID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 3),
    _CmGwLanAddrClientID_Type()
)
cmGwLanAddrClientID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwLanAddrClientID.setStatus("current")
_CmGwLanAddrLeaseCreateTime_Type = DateAndTime
_CmGwLanAddrLeaseCreateTime_Object = MibTableColumn
cmGwLanAddrLeaseCreateTime = _CmGwLanAddrLeaseCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 4),
    _CmGwLanAddrLeaseCreateTime_Type()
)
cmGwLanAddrLeaseCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwLanAddrLeaseCreateTime.setStatus("current")
_CmGwLanAddrLeaseExpireTime_Type = DateAndTime
_CmGwLanAddrLeaseExpireTime_Object = MibTableColumn
cmGwLanAddrLeaseExpireTime = _CmGwLanAddrLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 5),
    _CmGwLanAddrLeaseExpireTime_Type()
)
cmGwLanAddrLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwLanAddrLeaseExpireTime.setStatus("current")


class _CmGwLanAddrMethod_Type(Integer32):
    """Custom type cmGwLanAddrMethod based on Integer32"""
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
        *(("staticInactive", 1),
          ("staticActive", 2),
          ("dynamicInactive", 3),
          ("dynamicActive", 4))
    )


_CmGwLanAddrMethod_Type.__name__ = "Integer32"
_CmGwLanAddrMethod_Object = MibTableColumn
cmGwLanAddrMethod = _CmGwLanAddrMethod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 6),
    _CmGwLanAddrMethod_Type()
)
cmGwLanAddrMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwLanAddrMethod.setStatus("current")


class _CmGwLanAddrHostName_Type(SnmpAdminString):
    """Custom type cmGwLanAddrHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CmGwLanAddrHostName_Type.__name__ = "SnmpAdminString"
_CmGwLanAddrHostName_Object = MibTableColumn
cmGwLanAddrHostName = _CmGwLanAddrHostName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 7),
    _CmGwLanAddrHostName_Type()
)
cmGwLanAddrHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwLanAddrHostName.setStatus("current")
_CmGwLanAddrRowStatus_Type = RowStatus
_CmGwLanAddrRowStatus_Object = MibTableColumn
cmGwLanAddrRowStatus = _CmGwLanAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 2, 1, 3, 1, 1, 8),
    _CmGwLanAddrRowStatus_Type()
)
cmGwLanAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwLanAddrRowStatus.setStatus("current")
_CmGwNatMib_ObjectIdentity = ObjectIdentity
cmGwNatMib = _CmGwNatMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3)
)
_CmGwNatObjects_ObjectIdentity = ObjectIdentity
cmGwNatObjects = _CmGwNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1)
)
_CmGwNatBase_ObjectIdentity = ObjectIdentity
cmGwNatBase = _CmGwNatBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1)
)
_CmGwNatSetToFactory_Type = TruthValue
_CmGwNatSetToFactory_Object = MibScalar
cmGwNatSetToFactory = _CmGwNatSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 1),
    _CmGwNatSetToFactory_Type()
)
cmGwNatSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatSetToFactory.setStatus("current")


class _CmGwNatTcpTimeWait_Type(Unsigned32):
    """Custom type cmGwNatTcpTimeWait based on Unsigned32"""
    defaultValue = 86400


_CmGwNatTcpTimeWait_Type.__name__ = "Unsigned32"
_CmGwNatTcpTimeWait_Object = MibScalar
cmGwNatTcpTimeWait = _CmGwNatTcpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 2),
    _CmGwNatTcpTimeWait_Type()
)
cmGwNatTcpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatTcpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cmGwNatTcpTimeWait.setUnits("seconds")


class _CmGwNatUdpTimeWait_Type(Unsigned32):
    """Custom type cmGwNatUdpTimeWait based on Unsigned32"""
    defaultValue = 300


_CmGwNatUdpTimeWait_Type.__name__ = "Unsigned32"
_CmGwNatUdpTimeWait_Object = MibScalar
cmGwNatUdpTimeWait = _CmGwNatUdpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 3),
    _CmGwNatUdpTimeWait_Type()
)
cmGwNatUdpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatUdpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cmGwNatUdpTimeWait.setUnits("seconds")


class _CmGwNatIcmpTimeWait_Type(Unsigned32):
    """Custom type cmGwNatIcmpTimeWait based on Unsigned32"""
    defaultValue = 300


_CmGwNatIcmpTimeWait_Type.__name__ = "Unsigned32"
_CmGwNatIcmpTimeWait_Object = MibScalar
cmGwNatIcmpTimeWait = _CmGwNatIcmpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 4),
    _CmGwNatIcmpTimeWait_Type()
)
cmGwNatIcmpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatIcmpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cmGwNatIcmpTimeWait.setUnits("seconds")


class _CmGwNatPrimaryMode_Type(CmGwNatPacketMode):
    """Custom type cmGwNatPrimaryMode based on CmGwNatPacketMode"""
    defaultValue = 1


_CmGwNatPrimaryMode_Type.__name__ = "CmGwNatPacketMode"
_CmGwNatPrimaryMode_Object = MibScalar
cmGwNatPrimaryMode = _CmGwNatPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 5),
    _CmGwNatPrimaryMode_Type()
)
cmGwNatPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatPrimaryMode.setStatus("current")


class _CmGwNatGamingDMZIpAddrType_Type(InetAddressType):
    """Custom type cmGwNatGamingDMZIpAddrType based on InetAddressType"""
    defaultValue = 1


_CmGwNatGamingDMZIpAddrType_Type.__name__ = "InetAddressType"
_CmGwNatGamingDMZIpAddrType_Object = MibScalar
cmGwNatGamingDMZIpAddrType = _CmGwNatGamingDMZIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 6),
    _CmGwNatGamingDMZIpAddrType_Type()
)
cmGwNatGamingDMZIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatGamingDMZIpAddrType.setStatus("current")


class _CmGwNatGamingDMZIpAddr_Type(InetAddress):
    """Custom type cmGwNatGamingDMZIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_CmGwNatGamingDMZIpAddr_Type.__name__ = "InetAddress"
_CmGwNatGamingDMZIpAddr_Object = MibScalar
cmGwNatGamingDMZIpAddr = _CmGwNatGamingDMZIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 1, 7),
    _CmGwNatGamingDMZIpAddr_Type()
)
cmGwNatGamingDMZIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwNatGamingDMZIpAddr.setStatus("current")
_CmGwNatMap_ObjectIdentity = ObjectIdentity
cmGwNatMap = _CmGwNatMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2)
)
_CmGwNatMappingTable_Object = MibTable
cmGwNatMappingTable = _CmGwNatMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmGwNatMappingTable.setStatus("current")
_CmGwNatMappingEntry_Object = MibTableRow
cmGwNatMappingEntry = _CmGwNatMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1)
)
cmGwNatMappingEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwNatMappingIndex"),
)
if mibBuilder.loadTexts:
    cmGwNatMappingEntry.setStatus("current")


class _CmGwNatMappingIndex_Type(Integer32):
    """Custom type cmGwNatMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmGwNatMappingIndex_Type.__name__ = "Integer32"
_CmGwNatMappingIndex_Object = MibTableColumn
cmGwNatMappingIndex = _CmGwNatMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 1),
    _CmGwNatMappingIndex_Type()
)
cmGwNatMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwNatMappingIndex.setStatus("current")


class _CmGwNatMappingWanAddrType_Type(InetAddressType):
    """Custom type cmGwNatMappingWanAddrType based on InetAddressType"""
    defaultValue = 1


_CmGwNatMappingWanAddrType_Type.__name__ = "InetAddressType"
_CmGwNatMappingWanAddrType_Object = MibTableColumn
cmGwNatMappingWanAddrType = _CmGwNatMappingWanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 2),
    _CmGwNatMappingWanAddrType_Type()
)
cmGwNatMappingWanAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingWanAddrType.setStatus("current")
_CmGwNatMappingWanAddr_Type = InetAddress
_CmGwNatMappingWanAddr_Object = MibTableColumn
cmGwNatMappingWanAddr = _CmGwNatMappingWanAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 3),
    _CmGwNatMappingWanAddr_Type()
)
cmGwNatMappingWanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingWanAddr.setStatus("current")


class _CmGwNatMappingWanPort_Type(InetPortNumber):
    """Custom type cmGwNatMappingWanPort based on InetPortNumber"""
    defaultValue = 0


_CmGwNatMappingWanPort_Type.__name__ = "InetPortNumber"
_CmGwNatMappingWanPort_Object = MibTableColumn
cmGwNatMappingWanPort = _CmGwNatMappingWanPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 4),
    _CmGwNatMappingWanPort_Type()
)
cmGwNatMappingWanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingWanPort.setStatus("current")


class _CmGwNatMappingLanAddrType_Type(InetAddressType):
    """Custom type cmGwNatMappingLanAddrType based on InetAddressType"""
    defaultValue = 1


_CmGwNatMappingLanAddrType_Type.__name__ = "InetAddressType"
_CmGwNatMappingLanAddrType_Object = MibTableColumn
cmGwNatMappingLanAddrType = _CmGwNatMappingLanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 5),
    _CmGwNatMappingLanAddrType_Type()
)
cmGwNatMappingLanAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingLanAddrType.setStatus("current")
_CmGwNatMappingLanAddr_Type = InetAddress
_CmGwNatMappingLanAddr_Object = MibTableColumn
cmGwNatMappingLanAddr = _CmGwNatMappingLanAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 6),
    _CmGwNatMappingLanAddr_Type()
)
cmGwNatMappingLanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingLanAddr.setStatus("current")


class _CmGwNatMappingLanPort_Type(InetPortNumber):
    """Custom type cmGwNatMappingLanPort based on InetPortNumber"""
    defaultValue = 0


_CmGwNatMappingLanPort_Type.__name__ = "InetPortNumber"
_CmGwNatMappingLanPort_Object = MibTableColumn
cmGwNatMappingLanPort = _CmGwNatMappingLanPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 7),
    _CmGwNatMappingLanPort_Type()
)
cmGwNatMappingLanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingLanPort.setStatus("current")


class _CmGwNatMappingMethod_Type(Integer32):
    """Custom type cmGwNatMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_CmGwNatMappingMethod_Type.__name__ = "Integer32"
_CmGwNatMappingMethod_Object = MibTableColumn
cmGwNatMappingMethod = _CmGwNatMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 8),
    _CmGwNatMappingMethod_Type()
)
cmGwNatMappingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingMethod.setStatus("current")


class _CmGwNatMappingProtocol_Type(Integer32):
    """Custom type cmGwNatMappingProtocol based on Integer32"""
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
        *(("other", 1),
          ("icmp", 2),
          ("udp", 3),
          ("tcp", 4))
    )


_CmGwNatMappingProtocol_Type.__name__ = "Integer32"
_CmGwNatMappingProtocol_Object = MibTableColumn
cmGwNatMappingProtocol = _CmGwNatMappingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 9),
    _CmGwNatMappingProtocol_Type()
)
cmGwNatMappingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingProtocol.setStatus("current")
_CmGwNatMappingRowStatus_Type = RowStatus
_CmGwNatMappingRowStatus_Object = MibTableColumn
cmGwNatMappingRowStatus = _CmGwNatMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 1, 1, 10),
    _CmGwNatMappingRowStatus_Type()
)
cmGwNatMappingRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwNatMappingRowStatus.setStatus("current")
_CmGwNatPassthroughTable_Object = MibTable
cmGwNatPassthroughTable = _CmGwNatPassthroughTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmGwNatPassthroughTable.setStatus("current")
_CmGwNatPassthroughEntry_Object = MibTableRow
cmGwNatPassthroughEntry = _CmGwNatPassthroughEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 2, 1)
)
cmGwNatPassthroughEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwNatPassthroughIndex"),
)
if mibBuilder.loadTexts:
    cmGwNatPassthroughEntry.setStatus("current")


class _CmGwNatPassthroughIndex_Type(Integer32):
    """Custom type cmGwNatPassthroughIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmGwNatPassthroughIndex_Type.__name__ = "Integer32"
_CmGwNatPassthroughIndex_Object = MibTableColumn
cmGwNatPassthroughIndex = _CmGwNatPassthroughIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 2, 1, 1),
    _CmGwNatPassthroughIndex_Type()
)
cmGwNatPassthroughIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwNatPassthroughIndex.setStatus("current")
_CmGwNatPassthroughMACAddr_Type = PhysAddress
_CmGwNatPassthroughMACAddr_Object = MibTableColumn
cmGwNatPassthroughMACAddr = _CmGwNatPassthroughMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 2, 1, 2),
    _CmGwNatPassthroughMACAddr_Type()
)
cmGwNatPassthroughMACAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwNatPassthroughMACAddr.setStatus("current")
_CmGwNatPassthroughDMZEnable_Type = TruthValue
_CmGwNatPassthroughDMZEnable_Object = MibTableColumn
cmGwNatPassthroughDMZEnable = _CmGwNatPassthroughDMZEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 2, 1, 3),
    _CmGwNatPassthroughDMZEnable_Type()
)
cmGwNatPassthroughDMZEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwNatPassthroughDMZEnable.setStatus("current")
_CmGwNatPassthroughRowStatus_Type = RowStatus
_CmGwNatPassthroughRowStatus_Object = MibTableColumn
cmGwNatPassthroughRowStatus = _CmGwNatPassthroughRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 3, 1, 2, 2, 1, 4),
    _CmGwNatPassthroughRowStatus_Type()
)
cmGwNatPassthroughRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwNatPassthroughRowStatus.setStatus("current")
_CmGwLogMib_ObjectIdentity = ObjectIdentity
cmGwLogMib = _CmGwLogMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4)
)
_CmGwDevEvent_ObjectIdentity = ObjectIdentity
cmGwDevEvent = _CmGwDevEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1)
)


class _CmGwDevEvControl_Type(Integer32):
    """Custom type cmGwDevEvControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetLog", 1)
    )


_CmGwDevEvControl_Type.__name__ = "Integer32"
_CmGwDevEvControl_Object = MibScalar
cmGwDevEvControl = _CmGwDevEvControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 1),
    _CmGwDevEvControl_Type()
)
cmGwDevEvControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwDevEvControl.setStatus("current")
_CmGwDevEventTable_Object = MibTable
cmGwDevEventTable = _CmGwDevEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cmGwDevEventTable.setStatus("current")
_CmGwDevEventEntry_Object = MibTableRow
cmGwDevEventEntry = _CmGwDevEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1)
)
cmGwDevEventEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwDevEvIndex"),
)
if mibBuilder.loadTexts:
    cmGwDevEventEntry.setStatus("current")


class _CmGwDevEvIndex_Type(Integer32):
    """Custom type cmGwDevEvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmGwDevEvIndex_Type.__name__ = "Integer32"
_CmGwDevEvIndex_Object = MibTableColumn
cmGwDevEvIndex = _CmGwDevEvIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 1),
    _CmGwDevEvIndex_Type()
)
cmGwDevEvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwDevEvIndex.setStatus("current")
_CmGwDevEvFirstTime_Type = DateAndTime
_CmGwDevEvFirstTime_Object = MibTableColumn
cmGwDevEvFirstTime = _CmGwDevEvFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 2),
    _CmGwDevEvFirstTime_Type()
)
cmGwDevEvFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwDevEvFirstTime.setStatus("current")
_CmGwDevEvLastTime_Type = DateAndTime
_CmGwDevEvLastTime_Object = MibTableColumn
cmGwDevEvLastTime = _CmGwDevEvLastTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 3),
    _CmGwDevEvLastTime_Type()
)
cmGwDevEvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwDevEvLastTime.setStatus("current")
_CmGwDevEvCounts_Type = Counter32
_CmGwDevEvCounts_Object = MibTableColumn
cmGwDevEvCounts = _CmGwDevEvCounts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 4),
    _CmGwDevEvCounts_Type()
)
cmGwDevEvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwDevEvCounts.setStatus("current")


class _CmGwDevEvLevel_Type(Integer32):
    """Custom type cmGwDevEvLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("information", 7),
          ("debug", 8))
    )


_CmGwDevEvLevel_Type.__name__ = "Integer32"
_CmGwDevEvLevel_Object = MibTableColumn
cmGwDevEvLevel = _CmGwDevEvLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 5),
    _CmGwDevEvLevel_Type()
)
cmGwDevEvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwDevEvLevel.setStatus("current")
_CmGwDevEvId_Type = Unsigned32
_CmGwDevEvId_Object = MibTableColumn
cmGwDevEvId = _CmGwDevEvId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 6),
    _CmGwDevEvId_Type()
)
cmGwDevEvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwDevEvId.setStatus("current")
_CmGwDevEvText_Type = SnmpAdminString
_CmGwDevEvText_Object = MibTableColumn
cmGwDevEvText = _CmGwDevEvText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 4, 1, 2, 1, 7),
    _CmGwDevEvText_Type()
)
cmGwDevEvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwDevEvText.setStatus("current")
_CmGwAlgMib_ObjectIdentity = ObjectIdentity
cmGwAlgMib = _CmGwAlgMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000)
)
_CmGwAlgObjects_ObjectIdentity = ObjectIdentity
cmGwAlgObjects = _CmGwAlgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1)
)
_CmGwAlgSetToFactory_Type = TruthValue
_CmGwAlgSetToFactory_Object = MibScalar
cmGwAlgSetToFactory = _CmGwAlgSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 1),
    _CmGwAlgSetToFactory_Type()
)
cmGwAlgSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwAlgSetToFactory.setStatus("current")
_CmGwAlgTable_Object = MibTable
cmGwAlgTable = _CmGwAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2)
)
if mibBuilder.loadTexts:
    cmGwAlgTable.setStatus("current")
_CmGwAlgEntry_Object = MibTableRow
cmGwAlgEntry = _CmGwAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1)
)
cmGwAlgEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwAlgIndex"),
)
if mibBuilder.loadTexts:
    cmGwAlgEntry.setStatus("current")


class _CmGwAlgIndex_Type(Unsigned32):
    """Custom type cmGwAlgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 47),
    )


_CmGwAlgIndex_Type.__name__ = "Unsigned32"
_CmGwAlgIndex_Object = MibTableColumn
cmGwAlgIndex = _CmGwAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 1),
    _CmGwAlgIndex_Type()
)
cmGwAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwAlgIndex.setStatus("current")


class _CmGwAlgName_Type(SnmpAdminString):
    """Custom type cmGwAlgName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmGwAlgName_Type.__name__ = "SnmpAdminString"
_CmGwAlgName_Object = MibTableColumn
cmGwAlgName = _CmGwAlgName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 2),
    _CmGwAlgName_Type()
)
cmGwAlgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgName.setStatus("current")


class _CmGwAlgProtocol_Type(Integer32):
    """Custom type cmGwAlgProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_CmGwAlgProtocol_Type.__name__ = "Integer32"
_CmGwAlgProtocol_Object = MibTableColumn
cmGwAlgProtocol = _CmGwAlgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 3),
    _CmGwAlgProtocol_Type()
)
cmGwAlgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgProtocol.setStatus("current")
_CmGwAlgPortFrom_Type = InetPortNumber
_CmGwAlgPortFrom_Object = MibTableColumn
cmGwAlgPortFrom = _CmGwAlgPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 4),
    _CmGwAlgPortFrom_Type()
)
cmGwAlgPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgPortFrom.setStatus("current")
_CmGwAlgPortTo_Type = InetPortNumber
_CmGwAlgPortTo_Object = MibTableColumn
cmGwAlgPortTo = _CmGwAlgPortTo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 5),
    _CmGwAlgPortTo_Type()
)
cmGwAlgPortTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgPortTo.setStatus("current")


class _CmGwAlgSessionChaining_Type(Integer32):
    """Custom type cmGwAlgSessionChaining based on Integer32"""
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
        *(("disabled", 1),
          ("tcp", 2),
          ("tcpAndUdp", 3))
    )


_CmGwAlgSessionChaining_Type.__name__ = "Integer32"
_CmGwAlgSessionChaining_Object = MibTableColumn
cmGwAlgSessionChaining = _CmGwAlgSessionChaining_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 6),
    _CmGwAlgSessionChaining_Type()
)
cmGwAlgSessionChaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgSessionChaining.setStatus("current")


class _CmGwAlgSessionInterval_Type(Unsigned32):
    """Custom type cmGwAlgSessionInterval based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_CmGwAlgSessionInterval_Type.__name__ = "Unsigned32"
_CmGwAlgSessionInterval_Object = MibTableColumn
cmGwAlgSessionInterval = _CmGwAlgSessionInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 7),
    _CmGwAlgSessionInterval_Type()
)
cmGwAlgSessionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgSessionInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmGwAlgSessionInterval.setUnits("seconds")


class _CmGwAlgAddressReplacement_Type(Integer32):
    """Custom type cmGwAlgAddressReplacement based on Integer32"""
    defaultValue = 4

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
        *(("disabled", 1),
          ("tcp", 2),
          ("udp", 3),
          ("tcpAndUdp", 4))
    )


_CmGwAlgAddressReplacement_Type.__name__ = "Integer32"
_CmGwAlgAddressReplacement_Object = MibTableColumn
cmGwAlgAddressReplacement = _CmGwAlgAddressReplacement_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 8),
    _CmGwAlgAddressReplacement_Type()
)
cmGwAlgAddressReplacement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgAddressReplacement.setStatus("current")


class _CmGwAlgMultipleHostEnable_Type(TruthValue):
    """Custom type cmGwAlgMultipleHostEnable based on TruthValue"""
    defaultValue = 2


_CmGwAlgMultipleHostEnable_Type.__name__ = "TruthValue"
_CmGwAlgMultipleHostEnable_Object = MibTableColumn
cmGwAlgMultipleHostEnable = _CmGwAlgMultipleHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 9),
    _CmGwAlgMultipleHostEnable_Type()
)
cmGwAlgMultipleHostEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgMultipleHostEnable.setStatus("current")


class _CmGwAlgEnable_Type(TruthValue):
    """Custom type cmGwAlgEnable based on TruthValue"""
    defaultValue = 1


_CmGwAlgEnable_Type.__name__ = "TruthValue"
_CmGwAlgEnable_Object = MibTableColumn
cmGwAlgEnable = _CmGwAlgEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 10),
    _CmGwAlgEnable_Type()
)
cmGwAlgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgEnable.setStatus("current")
_CmGwAlgStatus_Type = RowStatus
_CmGwAlgStatus_Object = MibTableColumn
cmGwAlgStatus = _CmGwAlgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1000, 1, 2, 1, 11),
    _CmGwAlgStatus_Type()
)
cmGwAlgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwAlgStatus.setStatus("current")
_CmGwVirtualServerMib_ObjectIdentity = ObjectIdentity
cmGwVirtualServerMib = _CmGwVirtualServerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001)
)
_CmGwVirtualServerObjects_ObjectIdentity = ObjectIdentity
cmGwVirtualServerObjects = _CmGwVirtualServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1)
)
_CmGwVirtualServerSetToFactory_Type = TruthValue
_CmGwVirtualServerSetToFactory_Object = MibScalar
cmGwVirtualServerSetToFactory = _CmGwVirtualServerSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 1),
    _CmGwVirtualServerSetToFactory_Type()
)
cmGwVirtualServerSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwVirtualServerSetToFactory.setStatus("current")
_CmGwVirtualServerTable_Object = MibTable
cmGwVirtualServerTable = _CmGwVirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2)
)
if mibBuilder.loadTexts:
    cmGwVirtualServerTable.setStatus("current")
_CmGwVirtualServerEntry_Object = MibTableRow
cmGwVirtualServerEntry = _CmGwVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1)
)
cmGwVirtualServerEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwVirtualServerIndex"),
)
if mibBuilder.loadTexts:
    cmGwVirtualServerEntry.setStatus("current")


class _CmGwVirtualServerIndex_Type(Integer32):
    """Custom type cmGwVirtualServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CmGwVirtualServerIndex_Type.__name__ = "Integer32"
_CmGwVirtualServerIndex_Object = MibTableColumn
cmGwVirtualServerIndex = _CmGwVirtualServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 1),
    _CmGwVirtualServerIndex_Type()
)
cmGwVirtualServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwVirtualServerIndex.setStatus("current")


class _CmGwVirtualServerName_Type(SnmpAdminString):
    """Custom type cmGwVirtualServerName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmGwVirtualServerName_Type.__name__ = "SnmpAdminString"
_CmGwVirtualServerName_Object = MibTableColumn
cmGwVirtualServerName = _CmGwVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 2),
    _CmGwVirtualServerName_Type()
)
cmGwVirtualServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerName.setStatus("current")


class _CmGwVirtualServerType_Type(Integer32):
    """Custom type cmGwVirtualServerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wanPortRange", 1)
    )


_CmGwVirtualServerType_Type.__name__ = "Integer32"
_CmGwVirtualServerType_Object = MibTableColumn
cmGwVirtualServerType = _CmGwVirtualServerType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 3),
    _CmGwVirtualServerType_Type()
)
cmGwVirtualServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerType.setStatus("current")


class _CmGwVirtualServerPort1_Type(InetPortNumber):
    """Custom type cmGwVirtualServerPort1 based on InetPortNumber"""
    defaultValue = 0


_CmGwVirtualServerPort1_Type.__name__ = "InetPortNumber"
_CmGwVirtualServerPort1_Object = MibTableColumn
cmGwVirtualServerPort1 = _CmGwVirtualServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 4),
    _CmGwVirtualServerPort1_Type()
)
cmGwVirtualServerPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerPort1.setStatus("current")


class _CmGwVirtualServerPort2_Type(InetPortNumber):
    """Custom type cmGwVirtualServerPort2 based on InetPortNumber"""
    defaultValue = 0


_CmGwVirtualServerPort2_Type.__name__ = "InetPortNumber"
_CmGwVirtualServerPort2_Object = MibTableColumn
cmGwVirtualServerPort2 = _CmGwVirtualServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 5),
    _CmGwVirtualServerPort2_Type()
)
cmGwVirtualServerPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerPort2.setStatus("current")


class _CmGwVirtualServerLanAddrType_Type(InetAddressType):
    """Custom type cmGwVirtualServerLanAddrType based on InetAddressType"""
    defaultValue = 1


_CmGwVirtualServerLanAddrType_Type.__name__ = "InetAddressType"
_CmGwVirtualServerLanAddrType_Object = MibTableColumn
cmGwVirtualServerLanAddrType = _CmGwVirtualServerLanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 6),
    _CmGwVirtualServerLanAddrType_Type()
)
cmGwVirtualServerLanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerLanAddrType.setStatus("current")


class _CmGwVirtualServerLanAddr_Type(InetAddress):
    """Custom type cmGwVirtualServerLanAddr based on InetAddress"""
    defaultValue = OctetString("192.168.0.0")


_CmGwVirtualServerLanAddr_Type.__name__ = "InetAddress"
_CmGwVirtualServerLanAddr_Object = MibTableColumn
cmGwVirtualServerLanAddr = _CmGwVirtualServerLanAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 7),
    _CmGwVirtualServerLanAddr_Type()
)
cmGwVirtualServerLanAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerLanAddr.setStatus("current")


class _CmGwVirtualServerEnable_Type(TruthValue):
    """Custom type cmGwVirtualServerEnable based on TruthValue"""
    defaultValue = 1


_CmGwVirtualServerEnable_Type.__name__ = "TruthValue"
_CmGwVirtualServerEnable_Object = MibTableColumn
cmGwVirtualServerEnable = _CmGwVirtualServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 8),
    _CmGwVirtualServerEnable_Type()
)
cmGwVirtualServerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerEnable.setStatus("current")
_CmGwVirtualServerRowStatus_Type = RowStatus
_CmGwVirtualServerRowStatus_Object = MibTableColumn
cmGwVirtualServerRowStatus = _CmGwVirtualServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 9),
    _CmGwVirtualServerRowStatus_Type()
)
cmGwVirtualServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerRowStatus.setStatus("current")


class _CmGwVirtualServerProtocol_Type(Integer32):
    """Custom type cmGwVirtualServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("both", 3))
    )


_CmGwVirtualServerProtocol_Type.__name__ = "Integer32"
_CmGwVirtualServerProtocol_Object = MibTableColumn
cmGwVirtualServerProtocol = _CmGwVirtualServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 2, 1, 10),
    _CmGwVirtualServerProtocol_Type()
)
cmGwVirtualServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwVirtualServerProtocol.setStatus("current")


class _CmGwVirtualServerUSBAppsPort_Type(InetPortNumber):
    """Custom type cmGwVirtualServerUSBAppsPort based on InetPortNumber"""
    defaultValue = 9880


_CmGwVirtualServerUSBAppsPort_Type.__name__ = "InetPortNumber"
_CmGwVirtualServerUSBAppsPort_Object = MibScalar
cmGwVirtualServerUSBAppsPort = _CmGwVirtualServerUSBAppsPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1001, 1, 3),
    _CmGwVirtualServerUSBAppsPort_Type()
)
cmGwVirtualServerUSBAppsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwVirtualServerUSBAppsPort.setStatus("current")
_CmGwAlgPredefinedMib_ObjectIdentity = ObjectIdentity
cmGwAlgPredefinedMib = _CmGwAlgPredefinedMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002)
)
_CmGwAlgPredfinedObjects_ObjectIdentity = ObjectIdentity
cmGwAlgPredfinedObjects = _CmGwAlgPredfinedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002, 1)
)
_CmGwAlgPredefinedTable_Object = MibTable
cmGwAlgPredefinedTable = _CmGwAlgPredefinedTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002, 1, 1)
)
if mibBuilder.loadTexts:
    cmGwAlgPredefinedTable.setStatus("current")
_CmGwAlgPredefinedEntry_Object = MibTableRow
cmGwAlgPredefinedEntry = _CmGwAlgPredefinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002, 1, 1, 1)
)
cmGwAlgPredefinedEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwAlgPredefinedIndex"),
)
if mibBuilder.loadTexts:
    cmGwAlgPredefinedEntry.setStatus("current")
_CmGwAlgPredefinedIndex_Type = Unsigned32
_CmGwAlgPredefinedIndex_Object = MibTableColumn
cmGwAlgPredefinedIndex = _CmGwAlgPredefinedIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002, 1, 1, 1, 1),
    _CmGwAlgPredefinedIndex_Type()
)
cmGwAlgPredefinedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwAlgPredefinedIndex.setStatus("current")
_CmGwAlgPredefinedName_Type = SnmpAdminString
_CmGwAlgPredefinedName_Object = MibTableColumn
cmGwAlgPredefinedName = _CmGwAlgPredefinedName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002, 1, 1, 1, 2),
    _CmGwAlgPredefinedName_Type()
)
cmGwAlgPredefinedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwAlgPredefinedName.setStatus("current")
_CmGwAlgPredefinedEnable_Type = TruthValue
_CmGwAlgPredefinedEnable_Object = MibTableColumn
cmGwAlgPredefinedEnable = _CmGwAlgPredefinedEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1002, 1, 1, 1, 3),
    _CmGwAlgPredefinedEnable_Type()
)
cmGwAlgPredefinedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwAlgPredefinedEnable.setStatus("current")
_CmGwAdvCfgMib_ObjectIdentity = ObjectIdentity
cmGwAdvCfgMib = _CmGwAdvCfgMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1003)
)
_CmGwAdvCfgObjects_ObjectIdentity = ObjectIdentity
cmGwAdvCfgObjects = _CmGwAdvCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1003, 1)
)
_CmGwAdvCfgUPnPEnable_Type = TruthValue
_CmGwAdvCfgUPnPEnable_Object = MibScalar
cmGwAdvCfgUPnPEnable = _CmGwAdvCfgUPnPEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1003, 1, 1),
    _CmGwAdvCfgUPnPEnable_Type()
)
cmGwAdvCfgUPnPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwAdvCfgUPnPEnable.setStatus("current")
_CmGwAdvCfgIpsecPassThroughEnable_Type = TruthValue
_CmGwAdvCfgIpsecPassThroughEnable_Object = MibScalar
cmGwAdvCfgIpsecPassThroughEnable = _CmGwAdvCfgIpsecPassThroughEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1003, 1, 2),
    _CmGwAdvCfgIpsecPassThroughEnable_Type()
)
cmGwAdvCfgIpsecPassThroughEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwAdvCfgIpsecPassThroughEnable.setStatus("current")
_CmGwAdvCfgPptpPassThroughEnable_Type = TruthValue
_CmGwAdvCfgPptpPassThroughEnable_Object = MibScalar
cmGwAdvCfgPptpPassThroughEnable = _CmGwAdvCfgPptpPassThroughEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1003, 1, 3),
    _CmGwAdvCfgPptpPassThroughEnable_Type()
)
cmGwAdvCfgPptpPassThroughEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwAdvCfgPptpPassThroughEnable.setStatus("current")


class _CmGwAdvCfgParentalControl_Type(DisplayString):
    """Custom type cmGwAdvCfgParentalControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmGwAdvCfgParentalControl_Type.__name__ = "DisplayString"
_CmGwAdvCfgParentalControl_Object = MibScalar
cmGwAdvCfgParentalControl = _CmGwAdvCfgParentalControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1003, 1, 4),
    _CmGwAdvCfgParentalControl_Type()
)
cmGwAdvCfgParentalControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGwAdvCfgParentalControl.setStatus("current")
_CmGwPortTriggerMib_ObjectIdentity = ObjectIdentity
cmGwPortTriggerMib = _CmGwPortTriggerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004)
)
_CmGwPortTriggerObjects_ObjectIdentity = ObjectIdentity
cmGwPortTriggerObjects = _CmGwPortTriggerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1)
)
_CmGwPortTriggerSetToFactory_Type = TruthValue
_CmGwPortTriggerSetToFactory_Object = MibScalar
cmGwPortTriggerSetToFactory = _CmGwPortTriggerSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 1),
    _CmGwPortTriggerSetToFactory_Type()
)
cmGwPortTriggerSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwPortTriggerSetToFactory.setStatus("current")
_CmGwPortTriggerTable_Object = MibTable
cmGwPortTriggerTable = _CmGwPortTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2)
)
if mibBuilder.loadTexts:
    cmGwPortTriggerTable.setStatus("current")
_CmGwPortTriggerEntry_Object = MibTableRow
cmGwPortTriggerEntry = _CmGwPortTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1)
)
cmGwPortTriggerEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwPortTriggerIndex"),
)
if mibBuilder.loadTexts:
    cmGwPortTriggerEntry.setStatus("current")
_CmGwPortTriggerIndex_Type = Unsigned32
_CmGwPortTriggerIndex_Object = MibTableColumn
cmGwPortTriggerIndex = _CmGwPortTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 1),
    _CmGwPortTriggerIndex_Type()
)
cmGwPortTriggerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwPortTriggerIndex.setStatus("current")
_CmGwPortTriggerStartPortTriggerRange_Type = InetPortNumber
_CmGwPortTriggerStartPortTriggerRange_Object = MibTableColumn
cmGwPortTriggerStartPortTriggerRange = _CmGwPortTriggerStartPortTriggerRange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 2),
    _CmGwPortTriggerStartPortTriggerRange_Type()
)
cmGwPortTriggerStartPortTriggerRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerStartPortTriggerRange.setStatus("current")
_CmGwPortTriggerEndPortTriggerRange_Type = InetPortNumber
_CmGwPortTriggerEndPortTriggerRange_Object = MibTableColumn
cmGwPortTriggerEndPortTriggerRange = _CmGwPortTriggerEndPortTriggerRange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 3),
    _CmGwPortTriggerEndPortTriggerRange_Type()
)
cmGwPortTriggerEndPortTriggerRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerEndPortTriggerRange.setStatus("current")
_CmGwPortTriggerStartPortTargetRange_Type = InetPortNumber
_CmGwPortTriggerStartPortTargetRange_Object = MibTableColumn
cmGwPortTriggerStartPortTargetRange = _CmGwPortTriggerStartPortTargetRange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 4),
    _CmGwPortTriggerStartPortTargetRange_Type()
)
cmGwPortTriggerStartPortTargetRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerStartPortTargetRange.setStatus("current")
_CmGwPortTriggerEndPortTargetRange_Type = InetPortNumber
_CmGwPortTriggerEndPortTargetRange_Object = MibTableColumn
cmGwPortTriggerEndPortTargetRange = _CmGwPortTriggerEndPortTargetRange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 5),
    _CmGwPortTriggerEndPortTargetRange_Type()
)
cmGwPortTriggerEndPortTargetRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerEndPortTargetRange.setStatus("current")


class _CmGwPortTriggerProtocol_Type(Integer32):
    """Custom type cmGwPortTriggerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("both", 3))
    )


_CmGwPortTriggerProtocol_Type.__name__ = "Integer32"
_CmGwPortTriggerProtocol_Object = MibTableColumn
cmGwPortTriggerProtocol = _CmGwPortTriggerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 6),
    _CmGwPortTriggerProtocol_Type()
)
cmGwPortTriggerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerProtocol.setStatus("current")


class _CmGwPortTriggerEnable_Type(TruthValue):
    """Custom type cmGwPortTriggerEnable based on TruthValue"""
    defaultValue = 1


_CmGwPortTriggerEnable_Type.__name__ = "TruthValue"
_CmGwPortTriggerEnable_Object = MibTableColumn
cmGwPortTriggerEnable = _CmGwPortTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 7),
    _CmGwPortTriggerEnable_Type()
)
cmGwPortTriggerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerEnable.setStatus("current")
_CmGwPortTriggerRowStatus_Type = RowStatus
_CmGwPortTriggerRowStatus_Object = MibTableColumn
cmGwPortTriggerRowStatus = _CmGwPortTriggerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1004, 1, 2, 1, 8),
    _CmGwPortTriggerRowStatus_Type()
)
cmGwPortTriggerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwPortTriggerRowStatus.setStatus("current")
_CmGwFiltersMib_ObjectIdentity = ObjectIdentity
cmGwFiltersMib = _CmGwFiltersMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005)
)
_CmGwFiltersObjects_ObjectIdentity = ObjectIdentity
cmGwFiltersObjects = _CmGwFiltersObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1)
)
_CmGwFiltersIpFilter_ObjectIdentity = ObjectIdentity
cmGwFiltersIpFilter = _CmGwFiltersIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1)
)
_CmGwFiltersIpFilterSetToFactory_Type = TruthValue
_CmGwFiltersIpFilterSetToFactory_Object = MibScalar
cmGwFiltersIpFilterSetToFactory = _CmGwFiltersIpFilterSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 1),
    _CmGwFiltersIpFilterSetToFactory_Type()
)
cmGwFiltersIpFilterSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterSetToFactory.setStatus("current")
_CmGwFiltersIpFilterTable_Object = MibTable
cmGwFiltersIpFilterTable = _CmGwFiltersIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterTable.setStatus("current")
_CmGwFiltersIpFilterEntry_Object = MibTableRow
cmGwFiltersIpFilterEntry = _CmGwFiltersIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1)
)
cmGwFiltersIpFilterEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwFiltersIpFilterIndex"),
)
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterEntry.setStatus("current")
_CmGwFiltersIpFilterIndex_Type = Unsigned32
_CmGwFiltersIpFilterIndex_Object = MibTableColumn
cmGwFiltersIpFilterIndex = _CmGwFiltersIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1, 1),
    _CmGwFiltersIpFilterIndex_Type()
)
cmGwFiltersIpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterIndex.setStatus("current")


class _CmGwFiltersIpFilterAddressType_Type(InetAddressType):
    """Custom type cmGwFiltersIpFilterAddressType based on InetAddressType"""
    defaultValue = 1


_CmGwFiltersIpFilterAddressType_Type.__name__ = "InetAddressType"
_CmGwFiltersIpFilterAddressType_Object = MibTableColumn
cmGwFiltersIpFilterAddressType = _CmGwFiltersIpFilterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1, 2),
    _CmGwFiltersIpFilterAddressType_Type()
)
cmGwFiltersIpFilterAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterAddressType.setStatus("current")
_CmGwFiltersIpFilterStartAddress_Type = InetAddress
_CmGwFiltersIpFilterStartAddress_Object = MibTableColumn
cmGwFiltersIpFilterStartAddress = _CmGwFiltersIpFilterStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1, 3),
    _CmGwFiltersIpFilterStartAddress_Type()
)
cmGwFiltersIpFilterStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterStartAddress.setStatus("current")
_CmGwFiltersIpFilterEndAddress_Type = InetAddress
_CmGwFiltersIpFilterEndAddress_Object = MibTableColumn
cmGwFiltersIpFilterEndAddress = _CmGwFiltersIpFilterEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1, 4),
    _CmGwFiltersIpFilterEndAddress_Type()
)
cmGwFiltersIpFilterEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterEndAddress.setStatus("current")


class _CmGwFiltersIpFilterEnable_Type(TruthValue):
    """Custom type cmGwFiltersIpFilterEnable based on TruthValue"""
    defaultValue = 1


_CmGwFiltersIpFilterEnable_Type.__name__ = "TruthValue"
_CmGwFiltersIpFilterEnable_Object = MibTableColumn
cmGwFiltersIpFilterEnable = _CmGwFiltersIpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1, 5),
    _CmGwFiltersIpFilterEnable_Type()
)
cmGwFiltersIpFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterEnable.setStatus("current")
_CmGwFiltersIpFilterRowStatus_Type = RowStatus
_CmGwFiltersIpFilterRowStatus_Object = MibTableColumn
cmGwFiltersIpFilterRowStatus = _CmGwFiltersIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 1, 2, 1, 6),
    _CmGwFiltersIpFilterRowStatus_Type()
)
cmGwFiltersIpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersIpFilterRowStatus.setStatus("current")
_CmGwFiltersMacFilter_ObjectIdentity = ObjectIdentity
cmGwFiltersMacFilter = _CmGwFiltersMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2)
)
_CmGwFiltersMacFilterSetToFactory_Type = TruthValue
_CmGwFiltersMacFilterSetToFactory_Object = MibScalar
cmGwFiltersMacFilterSetToFactory = _CmGwFiltersMacFilterSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2, 1),
    _CmGwFiltersMacFilterSetToFactory_Type()
)
cmGwFiltersMacFilterSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFiltersMacFilterSetToFactory.setStatus("current")
_CmGwFiltersMacFilterTable_Object = MibTable
cmGwFiltersMacFilterTable = _CmGwFiltersMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmGwFiltersMacFilterTable.setStatus("current")
_CmGwFiltersMacFilterEntry_Object = MibTableRow
cmGwFiltersMacFilterEntry = _CmGwFiltersMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2, 2, 1)
)
cmGwFiltersMacFilterEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwFiltersMacFilterIndex"),
)
if mibBuilder.loadTexts:
    cmGwFiltersMacFilterEntry.setStatus("current")
_CmGwFiltersMacFilterIndex_Type = Unsigned32
_CmGwFiltersMacFilterIndex_Object = MibTableColumn
cmGwFiltersMacFilterIndex = _CmGwFiltersMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2, 2, 1, 1),
    _CmGwFiltersMacFilterIndex_Type()
)
cmGwFiltersMacFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwFiltersMacFilterIndex.setStatus("current")
_CmGwFiltersMacFilterMacAddress_Type = PhysAddress
_CmGwFiltersMacFilterMacAddress_Object = MibTableColumn
cmGwFiltersMacFilterMacAddress = _CmGwFiltersMacFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2, 2, 1, 2),
    _CmGwFiltersMacFilterMacAddress_Type()
)
cmGwFiltersMacFilterMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersMacFilterMacAddress.setStatus("current")
_CmGwFiltersMacFilterRowStatus_Type = RowStatus
_CmGwFiltersMacFilterRowStatus_Object = MibTableColumn
cmGwFiltersMacFilterRowStatus = _CmGwFiltersMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 2, 2, 1, 3),
    _CmGwFiltersMacFilterRowStatus_Type()
)
cmGwFiltersMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersMacFilterRowStatus.setStatus("current")
_CmGwFiltersPortFilter_ObjectIdentity = ObjectIdentity
cmGwFiltersPortFilter = _CmGwFiltersPortFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3)
)
_CmGwFiltersPortFilterSetToFactory_Type = TruthValue
_CmGwFiltersPortFilterSetToFactory_Object = MibScalar
cmGwFiltersPortFilterSetToFactory = _CmGwFiltersPortFilterSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 1),
    _CmGwFiltersPortFilterSetToFactory_Type()
)
cmGwFiltersPortFilterSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterSetToFactory.setStatus("current")
_CmGwFiltersPortFilterTable_Object = MibTable
cmGwFiltersPortFilterTable = _CmGwFiltersPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterTable.setStatus("current")
_CmGwFiltersPortFilterEntry_Object = MibTableRow
cmGwFiltersPortFilterEntry = _CmGwFiltersPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1)
)
cmGwFiltersPortFilterEntry.setIndexNames(
    (0, "CM-GATEWAY-MIB", "cmGwFiltersPortFilterIndex"),
)
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterEntry.setStatus("current")
_CmGwFiltersPortFilterIndex_Type = Unsigned32
_CmGwFiltersPortFilterIndex_Object = MibTableColumn
cmGwFiltersPortFilterIndex = _CmGwFiltersPortFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1, 1),
    _CmGwFiltersPortFilterIndex_Type()
)
cmGwFiltersPortFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterIndex.setStatus("current")
_CmGwFiltersPortFilterStartPort_Type = InetPortNumber
_CmGwFiltersPortFilterStartPort_Object = MibTableColumn
cmGwFiltersPortFilterStartPort = _CmGwFiltersPortFilterStartPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1, 2),
    _CmGwFiltersPortFilterStartPort_Type()
)
cmGwFiltersPortFilterStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterStartPort.setStatus("current")
_CmGwFiltersPortFilterEndPort_Type = InetPortNumber
_CmGwFiltersPortFilterEndPort_Object = MibTableColumn
cmGwFiltersPortFilterEndPort = _CmGwFiltersPortFilterEndPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1, 3),
    _CmGwFiltersPortFilterEndPort_Type()
)
cmGwFiltersPortFilterEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterEndPort.setStatus("current")


class _CmGwFiltersPortFilterProtocol_Type(Integer32):
    """Custom type cmGwFiltersPortFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("both", 3))
    )


_CmGwFiltersPortFilterProtocol_Type.__name__ = "Integer32"
_CmGwFiltersPortFilterProtocol_Object = MibTableColumn
cmGwFiltersPortFilterProtocol = _CmGwFiltersPortFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1, 4),
    _CmGwFiltersPortFilterProtocol_Type()
)
cmGwFiltersPortFilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterProtocol.setStatus("current")


class _CmGwFiltersPortFilterEnable_Type(TruthValue):
    """Custom type cmGwFiltersPortFilterEnable based on TruthValue"""
    defaultValue = 1


_CmGwFiltersPortFilterEnable_Type.__name__ = "TruthValue"
_CmGwFiltersPortFilterEnable_Object = MibTableColumn
cmGwFiltersPortFilterEnable = _CmGwFiltersPortFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1, 5),
    _CmGwFiltersPortFilterEnable_Type()
)
cmGwFiltersPortFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterEnable.setStatus("current")
_CmGwFiltersPortFilterRowStatus_Type = RowStatus
_CmGwFiltersPortFilterRowStatus_Object = MibTableColumn
cmGwFiltersPortFilterRowStatus = _CmGwFiltersPortFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1005, 1, 3, 2, 1, 6),
    _CmGwFiltersPortFilterRowStatus_Type()
)
cmGwFiltersPortFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmGwFiltersPortFilterRowStatus.setStatus("current")
_CmGwFirewallMib_ObjectIdentity = ObjectIdentity
cmGwFirewallMib = _CmGwFirewallMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006)
)
_CmGwFirewallObjects_ObjectIdentity = ObjectIdentity
cmGwFirewallObjects = _CmGwFirewallObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1)
)
_CmGwFirewallProtectEnable_Type = TruthValue
_CmGwFirewallProtectEnable_Object = MibScalar
cmGwFirewallProtectEnable = _CmGwFirewallProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1, 1),
    _CmGwFirewallProtectEnable_Type()
)
cmGwFirewallProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFirewallProtectEnable.setStatus("current")
_CmGwFirewallIpFloodDetectEnable_Type = TruthValue
_CmGwFirewallIpFloodDetectEnable_Object = MibScalar
cmGwFirewallIpFloodDetectEnable = _CmGwFirewallIpFloodDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1, 2),
    _CmGwFirewallIpFloodDetectEnable_Type()
)
cmGwFirewallIpFloodDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFirewallIpFloodDetectEnable.setStatus("current")
_CmGwFirewallPortScanDetectEnable_Type = TruthValue
_CmGwFirewallPortScanDetectEnable_Object = MibScalar
cmGwFirewallPortScanDetectEnable = _CmGwFirewallPortScanDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1, 3),
    _CmGwFirewallPortScanDetectEnable_Type()
)
cmGwFirewallPortScanDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFirewallPortScanDetectEnable.setStatus("current")
_CmGwFirewallBlockFragIpEnable_Type = TruthValue
_CmGwFirewallBlockFragIpEnable_Object = MibScalar
cmGwFirewallBlockFragIpEnable = _CmGwFirewallBlockFragIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1, 4),
    _CmGwFirewallBlockFragIpEnable_Type()
)
cmGwFirewallBlockFragIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFirewallBlockFragIpEnable.setStatus("current")


class _CmGwFirewallProtectionLevel_Type(Integer32):
    """Custom type cmGwFirewallProtectionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_CmGwFirewallProtectionLevel_Type.__name__ = "Integer32"
_CmGwFirewallProtectionLevel_Object = MibScalar
cmGwFirewallProtectionLevel = _CmGwFirewallProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1, 5),
    _CmGwFirewallProtectionLevel_Type()
)
cmGwFirewallProtectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwFirewallProtectionLevel.setStatus("current")
_CmGwIPv6FirewallProtectEnable_Type = TruthValue
_CmGwIPv6FirewallProtectEnable_Object = MibScalar
cmGwIPv6FirewallProtectEnable = _CmGwIPv6FirewallProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1006, 1, 6),
    _CmGwIPv6FirewallProtectEnable_Type()
)
cmGwIPv6FirewallProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwIPv6FirewallProtectEnable.setStatus("current")
_CmGwProvisioningMib_ObjectIdentity = ObjectIdentity
cmGwProvisioningMib = _CmGwProvisioningMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007)
)
_CmGwProvisioningObjects_ObjectIdentity = ObjectIdentity
cmGwProvisioningObjects = _CmGwProvisioningObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007, 1)
)
_CmGwProvDeviceProvisioningMode_Type = Integer32
_CmGwProvDeviceProvisioningMode_Object = MibScalar
cmGwProvDeviceProvisioningMode = _CmGwProvDeviceProvisioningMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007, 1, 1),
    _CmGwProvDeviceProvisioningMode_Type()
)
cmGwProvDeviceProvisioningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwProvDeviceProvisioningMode.setStatus("current")


class _CmGwProvDeviceConfigStatus_Type(Integer32):
    """Custom type cmGwProvDeviceConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("inProgress", 2),
          ("success", 3),
          ("errorServerUnavailable", 4),
          ("errorFileNotFound", 5),
          ("errorBadFile", 6),
          ("download", 7))
    )


_CmGwProvDeviceConfigStatus_Type.__name__ = "Integer32"
_CmGwProvDeviceConfigStatus_Object = MibScalar
cmGwProvDeviceConfigStatus = _CmGwProvDeviceConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007, 1, 2),
    _CmGwProvDeviceConfigStatus_Type()
)
cmGwProvDeviceConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwProvDeviceConfigStatus.setStatus("current")
_CmGwProvDeviceConfigFilename_Type = SnmpAdminString
_CmGwProvDeviceConfigFilename_Object = MibScalar
cmGwProvDeviceConfigFilename = _CmGwProvDeviceConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007, 1, 3),
    _CmGwProvDeviceConfigFilename_Type()
)
cmGwProvDeviceConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwProvDeviceConfigFilename.setStatus("current")


class _CmGwProvErouterMode_Type(Integer32):
    """Custom type cmGwProvErouterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("ipv4", 2),
          ("ipv6", 3),
          ("dual", 4),
          ("ipv4RG", 5))
    )


_CmGwProvErouterMode_Type.__name__ = "Integer32"
_CmGwProvErouterMode_Object = MibScalar
cmGwProvErouterMode = _CmGwProvErouterMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007, 1, 4),
    _CmGwProvErouterMode_Type()
)
cmGwProvErouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwProvErouterMode.setStatus("current")


class _CmGwProvErouterIPv6PassthruMode_Type(Integer32):
    """Custom type cmGwProvErouterIPv6PassthruMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ipv6Only", 1),
          ("dualStack", 2))
    )


_CmGwProvErouterIPv6PassthruMode_Type.__name__ = "Integer32"
_CmGwProvErouterIPv6PassthruMode_Object = MibScalar
cmGwProvErouterIPv6PassthruMode = _CmGwProvErouterIPv6PassthruMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1007, 1, 5),
    _CmGwProvErouterIPv6PassthruMode_Type()
)
cmGwProvErouterIPv6PassthruMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwProvErouterIPv6PassthruMode.setStatus("current")
_CmGwDsliteMib_ObjectIdentity = ObjectIdentity
cmGwDsliteMib = _CmGwDsliteMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008)
)
_CmGwDsliteObjects_ObjectIdentity = ObjectIdentity
cmGwDsliteObjects = _CmGwDsliteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008, 1)
)
_CmGwDsliteEnabled_Type = TruthValue
_CmGwDsliteEnabled_Object = MibScalar
cmGwDsliteEnabled = _CmGwDsliteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008, 1, 1),
    _CmGwDsliteEnabled_Type()
)
cmGwDsliteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwDsliteEnabled.setStatus("current")
_CmGwDsliteAftrAddress_Type = InetAddressIPv6
_CmGwDsliteAftrAddress_Object = MibScalar
cmGwDsliteAftrAddress = _CmGwDsliteAftrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008, 1, 2),
    _CmGwDsliteAftrAddress_Type()
)
cmGwDsliteAftrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwDsliteAftrAddress.setStatus("current")


class _CmGwDslitePcpMode_Type(Integer32):
    """Custom type cmGwDslitePcpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plain", 1),
          ("encapsulation", 2))
    )


_CmGwDslitePcpMode_Type.__name__ = "Integer32"
_CmGwDslitePcpMode_Object = MibScalar
cmGwDslitePcpMode = _CmGwDslitePcpMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008, 1, 3),
    _CmGwDslitePcpMode_Type()
)
cmGwDslitePcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwDslitePcpMode.setStatus("current")


class _CmGwDsliteTcpMssClamping_Type(Integer32):
    """Custom type cmGwDsliteTcpMssClamping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1420),
    )


_CmGwDsliteTcpMssClamping_Type.__name__ = "Integer32"
_CmGwDsliteTcpMssClamping_Object = MibScalar
cmGwDsliteTcpMssClamping = _CmGwDsliteTcpMssClamping_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008, 1, 4),
    _CmGwDsliteTcpMssClamping_Type()
)
cmGwDsliteTcpMssClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwDsliteTcpMssClamping.setStatus("current")
_CmGwDsliteIPv4FragEnabled_Type = TruthValue
_CmGwDsliteIPv4FragEnabled_Object = MibScalar
cmGwDsliteIPv4FragEnabled = _CmGwDsliteIPv4FragEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 1, 1008, 1, 5),
    _CmGwDsliteIPv4FragEnabled_Type()
)
cmGwDsliteIPv4FragEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGwDsliteIPv4FragEnabled.setStatus("current")
_CmGwConformance_ObjectIdentity = ObjectIdentity
cmGwConformance = _CmGwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 2)
)
_CmGwCompliances_ObjectIdentity = ObjectIdentity
cmGwCompliances = _CmGwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 2, 1)
)
_CmGwGroups_ObjectIdentity = ObjectIdentity
cmGwGroups = _CmGwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 2, 2)
)

# Managed Objects groups

cmGwBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 2, 2, 1)
)
cmGwBaseGroup.setObjects(
      *(("CM-GATEWAY-MIB", "cmGwWanMacAddress"),
        ("CM-GATEWAY-MIB", "cmGwWanSetToFactory"),
        ("CM-GATEWAY-MIB", "cmGwWanDhcpcAdminStatus"),
        ("CM-GATEWAY-MIB", "cmGwWanInetAddressType"),
        ("CM-GATEWAY-MIB", "cmGwWanInetAddress"),
        ("CM-GATEWAY-MIB", "cmGwWanHostName"),
        ("CM-GATEWAY-MIB", "cmGwWanSubnetMaskType"),
        ("CM-GATEWAY-MIB", "cmGwWanSubnetMask"),
        ("CM-GATEWAY-MIB", "cmGwWanRouterType"),
        ("CM-GATEWAY-MIB", "cmGwWanRouter"),
        ("CM-GATEWAY-MIB", "cmGwWanAddrDnsRowStatus"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsSetToFactory"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsAddressPoolStartType"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsAddressPoolStart"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsNetworkNumberType"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsNetworkNumber"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsSubnetMaskType"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsSubnetMask"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsDomainName"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsTTL"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsInterfaceMTU"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsLeaseTime"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsInetAddressType"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsInetAddress"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsMaxAddressCount"),
        ("CM-GATEWAY-MIB", "cmGwLanDhcpsCurrentLeaseCount"),
        ("CM-GATEWAY-MIB", "cmGwLanAddrClientID"),
        ("CM-GATEWAY-MIB", "cmGwLanAddrLeaseCreateTime"),
        ("CM-GATEWAY-MIB", "cmGwLanAddrLeaseExpireTime"),
        ("CM-GATEWAY-MIB", "cmGwLanAddrMethod"),
        ("CM-GATEWAY-MIB", "cmGwLanAddrHostName"),
        ("CM-GATEWAY-MIB", "cmGwLanAddrRowStatus"),
        ("CM-GATEWAY-MIB", "cmGwNatSetToFactory"),
        ("CM-GATEWAY-MIB", "cmGwNatTcpTimeWait"),
        ("CM-GATEWAY-MIB", "cmGwNatUdpTimeWait"),
        ("CM-GATEWAY-MIB", "cmGwNatIcmpTimeWait"),
        ("CM-GATEWAY-MIB", "cmGwNatPrimaryMode"),
        ("CM-GATEWAY-MIB", "cmGwNatGamingDMZIpAddrType"),
        ("CM-GATEWAY-MIB", "cmGwNatGamingDMZIpAddr"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingWanAddrType"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingWanAddr"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingWanPort"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingLanAddrType"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingLanAddr"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingLanPort"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingMethod"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingProtocol"),
        ("CM-GATEWAY-MIB", "cmGwNatMappingRowStatus"),
        ("CM-GATEWAY-MIB", "cmGwNatPassthroughMACAddr"),
        ("CM-GATEWAY-MIB", "cmGwNatPassthroughDMZEnable"),
        ("CM-GATEWAY-MIB", "cmGwNatPassthroughRowStatus"),
        ("CM-GATEWAY-MIB", "cmGwDevEvControl"),
        ("CM-GATEWAY-MIB", "cmGwDevEvFirstTime"),
        ("CM-GATEWAY-MIB", "cmGwDevEvLastTime"),
        ("CM-GATEWAY-MIB", "cmGwDevEvCounts"),
        ("CM-GATEWAY-MIB", "cmGwDevEvLevel"),
        ("CM-GATEWAY-MIB", "cmGwDevEvId"),
        ("CM-GATEWAY-MIB", "cmGwDevEvText"),
        ("CM-GATEWAY-MIB", "cmGwAlgSetToFactory"),
        ("CM-GATEWAY-MIB", "cmGwAlgName"),
        ("CM-GATEWAY-MIB", "cmGwAlgProtocol"),
        ("CM-GATEWAY-MIB", "cmGwAlgPortFrom"),
        ("CM-GATEWAY-MIB", "cmGwAlgPortTo"),
        ("CM-GATEWAY-MIB", "cmGwAlgSessionChaining"),
        ("CM-GATEWAY-MIB", "cmGwAlgSessionInterval"),
        ("CM-GATEWAY-MIB", "cmGwAlgAddressReplacement"),
        ("CM-GATEWAY-MIB", "cmGwAlgMultipleHostEnable"),
        ("CM-GATEWAY-MIB", "cmGwAlgEnable"),
        ("CM-GATEWAY-MIB", "cmGwAlgStatus"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerSetToFactory"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerName"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerType"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerPort1"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerPort2"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerLanAddrType"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerLanAddr"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerEnable"),
        ("CM-GATEWAY-MIB", "cmGwVirtualServerRowStatus"))
)
if mibBuilder.loadTexts:
    cmGwBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmGwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19, 52, 2, 1, 1)
)
cmGwCompliance.setObjects(
    ("CM-GATEWAY-MIB", "cmGwBaseGroup")
)
if mibBuilder.loadTexts:
    cmGwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-GATEWAY-MIB",
    **{"CmGwLanClientId": CmGwLanClientId,
       "CmGwNatPacketMode": CmGwNatPacketMode,
       "gi": gi,
       "giproducts": giproducts,
       "cm": cm,
       "cmGw": cmGw,
       "cmGwObjects": cmGwObjects,
       "cmGwBaseMib": cmGwBaseMib,
       "cmGwWanMacAddress": cmGwWanMacAddress,
       "cmGwWanSetToFactory": cmGwWanSetToFactory,
       "cmGwWanDhcpcAdminStatus": cmGwWanDhcpcAdminStatus,
       "cmGwWanInetAddressType": cmGwWanInetAddressType,
       "cmGwWanInetAddress": cmGwWanInetAddress,
       "cmGwWanHostName": cmGwWanHostName,
       "cmGwWanSubnetMaskType": cmGwWanSubnetMaskType,
       "cmGwWanSubnetMask": cmGwWanSubnetMask,
       "cmGwWanRouterType": cmGwWanRouterType,
       "cmGwWanRouter": cmGwWanRouter,
       "cmGwWanDnsServerTable": cmGwWanDnsServerTable,
       "cmGwWanDnsServerEntry": cmGwWanDnsServerEntry,
       "cmGwWanAddrDnsServerOrder": cmGwWanAddrDnsServerOrder,
       "cmGwWanAddrDnsIpType": cmGwWanAddrDnsIpType,
       "cmGwWanAddrDnsIp": cmGwWanAddrDnsIp,
       "cmGwWanAddrDnsRowStatus": cmGwWanAddrDnsRowStatus,
       "cmGwDhcpMib": cmGwDhcpMib,
       "cmGwDhcpObjects": cmGwDhcpObjects,
       "cmGwDhcpBase": cmGwDhcpBase,
       "cmGwLanDhcpsSetToFactory": cmGwLanDhcpsSetToFactory,
       "cmGwDhcpServer": cmGwDhcpServer,
       "cmGwLanDhcpsAddressPoolStartType": cmGwLanDhcpsAddressPoolStartType,
       "cmGwLanDhcpsAddressPoolStart": cmGwLanDhcpsAddressPoolStart,
       "cmGwLanDhcpsNetworkNumberType": cmGwLanDhcpsNetworkNumberType,
       "cmGwLanDhcpsNetworkNumber": cmGwLanDhcpsNetworkNumber,
       "cmGwLanDhcpsSubnetMaskType": cmGwLanDhcpsSubnetMaskType,
       "cmGwLanDhcpsSubnetMask": cmGwLanDhcpsSubnetMask,
       "cmGwLanDhcpsDomainName": cmGwLanDhcpsDomainName,
       "cmGwLanDhcpsTTL": cmGwLanDhcpsTTL,
       "cmGwLanDhcpsInterfaceMTU": cmGwLanDhcpsInterfaceMTU,
       "cmGwLanDhcpsLeaseTime": cmGwLanDhcpsLeaseTime,
       "cmGwLanDhcpsInetAddressType": cmGwLanDhcpsInetAddressType,
       "cmGwLanDhcpsInetAddress": cmGwLanDhcpsInetAddress,
       "cmGwLanDhcpsMaxAddressCount": cmGwLanDhcpsMaxAddressCount,
       "cmGwLanDhcpsCurrentLeaseCount": cmGwLanDhcpsCurrentLeaseCount,
       "cmGwLanDhcpsControl": cmGwLanDhcpsControl,
       "cmGwLanDhcpsCommitStatus": cmGwLanDhcpsCommitStatus,
       "cmGwDhcpAddr": cmGwDhcpAddr,
       "cmGwLanAddrTable": cmGwLanAddrTable,
       "cmGwLanAddrEntry": cmGwLanAddrEntry,
       "cmGwLanAddrIpType": cmGwLanAddrIpType,
       "cmGwLanAddrIp": cmGwLanAddrIp,
       "cmGwLanAddrClientID": cmGwLanAddrClientID,
       "cmGwLanAddrLeaseCreateTime": cmGwLanAddrLeaseCreateTime,
       "cmGwLanAddrLeaseExpireTime": cmGwLanAddrLeaseExpireTime,
       "cmGwLanAddrMethod": cmGwLanAddrMethod,
       "cmGwLanAddrHostName": cmGwLanAddrHostName,
       "cmGwLanAddrRowStatus": cmGwLanAddrRowStatus,
       "cmGwNatMib": cmGwNatMib,
       "cmGwNatObjects": cmGwNatObjects,
       "cmGwNatBase": cmGwNatBase,
       "cmGwNatSetToFactory": cmGwNatSetToFactory,
       "cmGwNatTcpTimeWait": cmGwNatTcpTimeWait,
       "cmGwNatUdpTimeWait": cmGwNatUdpTimeWait,
       "cmGwNatIcmpTimeWait": cmGwNatIcmpTimeWait,
       "cmGwNatPrimaryMode": cmGwNatPrimaryMode,
       "cmGwNatGamingDMZIpAddrType": cmGwNatGamingDMZIpAddrType,
       "cmGwNatGamingDMZIpAddr": cmGwNatGamingDMZIpAddr,
       "cmGwNatMap": cmGwNatMap,
       "cmGwNatMappingTable": cmGwNatMappingTable,
       "cmGwNatMappingEntry": cmGwNatMappingEntry,
       "cmGwNatMappingIndex": cmGwNatMappingIndex,
       "cmGwNatMappingWanAddrType": cmGwNatMappingWanAddrType,
       "cmGwNatMappingWanAddr": cmGwNatMappingWanAddr,
       "cmGwNatMappingWanPort": cmGwNatMappingWanPort,
       "cmGwNatMappingLanAddrType": cmGwNatMappingLanAddrType,
       "cmGwNatMappingLanAddr": cmGwNatMappingLanAddr,
       "cmGwNatMappingLanPort": cmGwNatMappingLanPort,
       "cmGwNatMappingMethod": cmGwNatMappingMethod,
       "cmGwNatMappingProtocol": cmGwNatMappingProtocol,
       "cmGwNatMappingRowStatus": cmGwNatMappingRowStatus,
       "cmGwNatPassthroughTable": cmGwNatPassthroughTable,
       "cmGwNatPassthroughEntry": cmGwNatPassthroughEntry,
       "cmGwNatPassthroughIndex": cmGwNatPassthroughIndex,
       "cmGwNatPassthroughMACAddr": cmGwNatPassthroughMACAddr,
       "cmGwNatPassthroughDMZEnable": cmGwNatPassthroughDMZEnable,
       "cmGwNatPassthroughRowStatus": cmGwNatPassthroughRowStatus,
       "cmGwLogMib": cmGwLogMib,
       "cmGwDevEvent": cmGwDevEvent,
       "cmGwDevEvControl": cmGwDevEvControl,
       "cmGwDevEventTable": cmGwDevEventTable,
       "cmGwDevEventEntry": cmGwDevEventEntry,
       "cmGwDevEvIndex": cmGwDevEvIndex,
       "cmGwDevEvFirstTime": cmGwDevEvFirstTime,
       "cmGwDevEvLastTime": cmGwDevEvLastTime,
       "cmGwDevEvCounts": cmGwDevEvCounts,
       "cmGwDevEvLevel": cmGwDevEvLevel,
       "cmGwDevEvId": cmGwDevEvId,
       "cmGwDevEvText": cmGwDevEvText,
       "cmGwAlgMib": cmGwAlgMib,
       "cmGwAlgObjects": cmGwAlgObjects,
       "cmGwAlgSetToFactory": cmGwAlgSetToFactory,
       "cmGwAlgTable": cmGwAlgTable,
       "cmGwAlgEntry": cmGwAlgEntry,
       "cmGwAlgIndex": cmGwAlgIndex,
       "cmGwAlgName": cmGwAlgName,
       "cmGwAlgProtocol": cmGwAlgProtocol,
       "cmGwAlgPortFrom": cmGwAlgPortFrom,
       "cmGwAlgPortTo": cmGwAlgPortTo,
       "cmGwAlgSessionChaining": cmGwAlgSessionChaining,
       "cmGwAlgSessionInterval": cmGwAlgSessionInterval,
       "cmGwAlgAddressReplacement": cmGwAlgAddressReplacement,
       "cmGwAlgMultipleHostEnable": cmGwAlgMultipleHostEnable,
       "cmGwAlgEnable": cmGwAlgEnable,
       "cmGwAlgStatus": cmGwAlgStatus,
       "cmGwVirtualServerMib": cmGwVirtualServerMib,
       "cmGwVirtualServerObjects": cmGwVirtualServerObjects,
       "cmGwVirtualServerSetToFactory": cmGwVirtualServerSetToFactory,
       "cmGwVirtualServerTable": cmGwVirtualServerTable,
       "cmGwVirtualServerEntry": cmGwVirtualServerEntry,
       "cmGwVirtualServerIndex": cmGwVirtualServerIndex,
       "cmGwVirtualServerName": cmGwVirtualServerName,
       "cmGwVirtualServerType": cmGwVirtualServerType,
       "cmGwVirtualServerPort1": cmGwVirtualServerPort1,
       "cmGwVirtualServerPort2": cmGwVirtualServerPort2,
       "cmGwVirtualServerLanAddrType": cmGwVirtualServerLanAddrType,
       "cmGwVirtualServerLanAddr": cmGwVirtualServerLanAddr,
       "cmGwVirtualServerEnable": cmGwVirtualServerEnable,
       "cmGwVirtualServerRowStatus": cmGwVirtualServerRowStatus,
       "cmGwVirtualServerProtocol": cmGwVirtualServerProtocol,
       "cmGwVirtualServerUSBAppsPort": cmGwVirtualServerUSBAppsPort,
       "cmGwAlgPredefinedMib": cmGwAlgPredefinedMib,
       "cmGwAlgPredfinedObjects": cmGwAlgPredfinedObjects,
       "cmGwAlgPredefinedTable": cmGwAlgPredefinedTable,
       "cmGwAlgPredefinedEntry": cmGwAlgPredefinedEntry,
       "cmGwAlgPredefinedIndex": cmGwAlgPredefinedIndex,
       "cmGwAlgPredefinedName": cmGwAlgPredefinedName,
       "cmGwAlgPredefinedEnable": cmGwAlgPredefinedEnable,
       "cmGwAdvCfgMib": cmGwAdvCfgMib,
       "cmGwAdvCfgObjects": cmGwAdvCfgObjects,
       "cmGwAdvCfgUPnPEnable": cmGwAdvCfgUPnPEnable,
       "cmGwAdvCfgIpsecPassThroughEnable": cmGwAdvCfgIpsecPassThroughEnable,
       "cmGwAdvCfgPptpPassThroughEnable": cmGwAdvCfgPptpPassThroughEnable,
       "cmGwAdvCfgParentalControl": cmGwAdvCfgParentalControl,
       "cmGwPortTriggerMib": cmGwPortTriggerMib,
       "cmGwPortTriggerObjects": cmGwPortTriggerObjects,
       "cmGwPortTriggerSetToFactory": cmGwPortTriggerSetToFactory,
       "cmGwPortTriggerTable": cmGwPortTriggerTable,
       "cmGwPortTriggerEntry": cmGwPortTriggerEntry,
       "cmGwPortTriggerIndex": cmGwPortTriggerIndex,
       "cmGwPortTriggerStartPortTriggerRange": cmGwPortTriggerStartPortTriggerRange,
       "cmGwPortTriggerEndPortTriggerRange": cmGwPortTriggerEndPortTriggerRange,
       "cmGwPortTriggerStartPortTargetRange": cmGwPortTriggerStartPortTargetRange,
       "cmGwPortTriggerEndPortTargetRange": cmGwPortTriggerEndPortTargetRange,
       "cmGwPortTriggerProtocol": cmGwPortTriggerProtocol,
       "cmGwPortTriggerEnable": cmGwPortTriggerEnable,
       "cmGwPortTriggerRowStatus": cmGwPortTriggerRowStatus,
       "cmGwFiltersMib": cmGwFiltersMib,
       "cmGwFiltersObjects": cmGwFiltersObjects,
       "cmGwFiltersIpFilter": cmGwFiltersIpFilter,
       "cmGwFiltersIpFilterSetToFactory": cmGwFiltersIpFilterSetToFactory,
       "cmGwFiltersIpFilterTable": cmGwFiltersIpFilterTable,
       "cmGwFiltersIpFilterEntry": cmGwFiltersIpFilterEntry,
       "cmGwFiltersIpFilterIndex": cmGwFiltersIpFilterIndex,
       "cmGwFiltersIpFilterAddressType": cmGwFiltersIpFilterAddressType,
       "cmGwFiltersIpFilterStartAddress": cmGwFiltersIpFilterStartAddress,
       "cmGwFiltersIpFilterEndAddress": cmGwFiltersIpFilterEndAddress,
       "cmGwFiltersIpFilterEnable": cmGwFiltersIpFilterEnable,
       "cmGwFiltersIpFilterRowStatus": cmGwFiltersIpFilterRowStatus,
       "cmGwFiltersMacFilter": cmGwFiltersMacFilter,
       "cmGwFiltersMacFilterSetToFactory": cmGwFiltersMacFilterSetToFactory,
       "cmGwFiltersMacFilterTable": cmGwFiltersMacFilterTable,
       "cmGwFiltersMacFilterEntry": cmGwFiltersMacFilterEntry,
       "cmGwFiltersMacFilterIndex": cmGwFiltersMacFilterIndex,
       "cmGwFiltersMacFilterMacAddress": cmGwFiltersMacFilterMacAddress,
       "cmGwFiltersMacFilterRowStatus": cmGwFiltersMacFilterRowStatus,
       "cmGwFiltersPortFilter": cmGwFiltersPortFilter,
       "cmGwFiltersPortFilterSetToFactory": cmGwFiltersPortFilterSetToFactory,
       "cmGwFiltersPortFilterTable": cmGwFiltersPortFilterTable,
       "cmGwFiltersPortFilterEntry": cmGwFiltersPortFilterEntry,
       "cmGwFiltersPortFilterIndex": cmGwFiltersPortFilterIndex,
       "cmGwFiltersPortFilterStartPort": cmGwFiltersPortFilterStartPort,
       "cmGwFiltersPortFilterEndPort": cmGwFiltersPortFilterEndPort,
       "cmGwFiltersPortFilterProtocol": cmGwFiltersPortFilterProtocol,
       "cmGwFiltersPortFilterEnable": cmGwFiltersPortFilterEnable,
       "cmGwFiltersPortFilterRowStatus": cmGwFiltersPortFilterRowStatus,
       "cmGwFirewallMib": cmGwFirewallMib,
       "cmGwFirewallObjects": cmGwFirewallObjects,
       "cmGwFirewallProtectEnable": cmGwFirewallProtectEnable,
       "cmGwFirewallIpFloodDetectEnable": cmGwFirewallIpFloodDetectEnable,
       "cmGwFirewallPortScanDetectEnable": cmGwFirewallPortScanDetectEnable,
       "cmGwFirewallBlockFragIpEnable": cmGwFirewallBlockFragIpEnable,
       "cmGwFirewallProtectionLevel": cmGwFirewallProtectionLevel,
       "cmGwIPv6FirewallProtectEnable": cmGwIPv6FirewallProtectEnable,
       "cmGwProvisioningMib": cmGwProvisioningMib,
       "cmGwProvisioningObjects": cmGwProvisioningObjects,
       "cmGwProvDeviceProvisioningMode": cmGwProvDeviceProvisioningMode,
       "cmGwProvDeviceConfigStatus": cmGwProvDeviceConfigStatus,
       "cmGwProvDeviceConfigFilename": cmGwProvDeviceConfigFilename,
       "cmGwProvErouterMode": cmGwProvErouterMode,
       "cmGwProvErouterIPv6PassthruMode": cmGwProvErouterIPv6PassthruMode,
       "cmGwDsliteMib": cmGwDsliteMib,
       "cmGwDsliteObjects": cmGwDsliteObjects,
       "cmGwDsliteEnabled": cmGwDsliteEnabled,
       "cmGwDsliteAftrAddress": cmGwDsliteAftrAddress,
       "cmGwDslitePcpMode": cmGwDslitePcpMode,
       "cmGwDsliteTcpMssClamping": cmGwDsliteTcpMssClamping,
       "cmGwDsliteIPv4FragEnabled": cmGwDsliteIPv4FragEnabled,
       "cmGwConformance": cmGwConformance,
       "cmGwCompliances": cmGwCompliances,
       "cmGwCompliance": cmGwCompliance,
       "cmGwGroups": cmGwGroups,
       "cmGwBaseGroup": cmGwBaseGroup}
)
