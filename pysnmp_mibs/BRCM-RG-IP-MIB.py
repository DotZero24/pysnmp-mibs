# SNMP MIB module (BRCM-RG-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-RG-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:32 2025
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

(residentialGatewayMgmt,) = mibBuilder.importSymbols(
    "BRCM-RG-MGMT-MIB",
    "residentialGatewayMgmt")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rgIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    rgIpMib.setRevisions(
        ("2007-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RgIpNetworkSettingsCommit_Type = TruthValue
_RgIpNetworkSettingsCommit_Object = MibScalar
rgIpNetworkSettingsCommit = _RgIpNetworkSettingsCommit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 1),
    _RgIpNetworkSettingsCommit_Type()
)
rgIpNetworkSettingsCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpNetworkSettingsCommit.setStatus("current")
_RgIpRipSettings_ObjectIdentity = ObjectIdentity
rgIpRipSettings = _RgIpRipSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2)
)
_RgIpRipEnable_Type = TruthValue
_RgIpRipEnable_Object = MibScalar
rgIpRipEnable = _RgIpRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 1),
    _RgIpRipEnable_Type()
)
rgIpRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipEnable.setStatus("current")
_RgIpRipMd5AuthEnable_Type = TruthValue
_RgIpRipMd5AuthEnable_Object = MibScalar
rgIpRipMd5AuthEnable = _RgIpRipMd5AuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 2),
    _RgIpRipMd5AuthEnable_Type()
)
rgIpRipMd5AuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipMd5AuthEnable.setStatus("current")
_RgIpRipMd5KeyId_Type = Integer32
_RgIpRipMd5KeyId_Object = MibScalar
rgIpRipMd5KeyId = _RgIpRipMd5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 3),
    _RgIpRipMd5KeyId_Type()
)
rgIpRipMd5KeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipMd5KeyId.setStatus("current")


class _RgIpRipMd5KeyValue_Type(OctetString):
    """Custom type rgIpRipMd5KeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_RgIpRipMd5KeyValue_Type.__name__ = "OctetString"
_RgIpRipMd5KeyValue_Object = MibScalar
rgIpRipMd5KeyValue = _RgIpRipMd5KeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 4),
    _RgIpRipMd5KeyValue_Type()
)
rgIpRipMd5KeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipMd5KeyValue.setStatus("current")


class _RgIpRipInterval_Type(Integer32):
    """Custom type rgIpRipInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_RgIpRipInterval_Type.__name__ = "Integer32"
_RgIpRipInterval_Object = MibScalar
rgIpRipInterval = _RgIpRipInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 5),
    _RgIpRipInterval_Type()
)
rgIpRipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipInterval.setStatus("current")


class _RgIpRipDestIpAddressType_Type(InetAddressType):
    """Custom type rgIpRipDestIpAddressType based on InetAddressType"""
    defaultValue = 1


_RgIpRipDestIpAddressType_Type.__name__ = "InetAddressType"
_RgIpRipDestIpAddressType_Object = MibScalar
rgIpRipDestIpAddressType = _RgIpRipDestIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 6),
    _RgIpRipDestIpAddressType_Type()
)
rgIpRipDestIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipDestIpAddressType.setStatus("current")
_RgIpRipDestIpAddress_Type = InetAddress
_RgIpRipDestIpAddress_Object = MibScalar
rgIpRipDestIpAddress = _RgIpRipDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 2, 7),
    _RgIpRipDestIpAddress_Type()
)
rgIpRipDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgIpRipDestIpAddress.setStatus("current")
_RgIpLanAddr_ObjectIdentity = ObjectIdentity
rgIpLanAddr = _RgIpLanAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3)
)
_RgIpLanAddrTable_Object = MibTable
rgIpLanAddrTable = _RgIpLanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rgIpLanAddrTable.setStatus("current")
_RgIpLanAddrBaseEntry_Object = MibTableRow
rgIpLanAddrBaseEntry = _RgIpLanAddrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1)
)
rgIpLanAddrBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BRCM-RG-IP-MIB", "rgIpLanAddrIpType"),
    (0, "BRCM-RG-IP-MIB", "rgIpLanAddrIp"),
)
if mibBuilder.loadTexts:
    rgIpLanAddrBaseEntry.setStatus("current")
_RgIpLanAddrIpType_Type = InetAddressType
_RgIpLanAddrIpType_Object = MibTableColumn
rgIpLanAddrIpType = _RgIpLanAddrIpType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1, 1),
    _RgIpLanAddrIpType_Type()
)
rgIpLanAddrIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rgIpLanAddrIpType.setStatus("current")
_RgIpLanAddrIp_Type = InetAddress
_RgIpLanAddrIp_Object = MibTableColumn
rgIpLanAddrIp = _RgIpLanAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1, 2),
    _RgIpLanAddrIp_Type()
)
rgIpLanAddrIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rgIpLanAddrIp.setStatus("current")


class _RgIpLanAddrClientID_Type(OctetString):
    """Custom type rgIpLanAddrClientID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RgIpLanAddrClientID_Type.__name__ = "OctetString"
_RgIpLanAddrClientID_Object = MibTableColumn
rgIpLanAddrClientID = _RgIpLanAddrClientID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1, 3),
    _RgIpLanAddrClientID_Type()
)
rgIpLanAddrClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rgIpLanAddrClientID.setStatus("current")
_RgIpLanAddrLeaseCreateTime_Type = DateAndTime
_RgIpLanAddrLeaseCreateTime_Object = MibTableColumn
rgIpLanAddrLeaseCreateTime = _RgIpLanAddrLeaseCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1, 4),
    _RgIpLanAddrLeaseCreateTime_Type()
)
rgIpLanAddrLeaseCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rgIpLanAddrLeaseCreateTime.setStatus("current")
_RgIpLanAddrLeaseExpireTime_Type = DateAndTime
_RgIpLanAddrLeaseExpireTime_Object = MibTableColumn
rgIpLanAddrLeaseExpireTime = _RgIpLanAddrLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1, 5),
    _RgIpLanAddrLeaseExpireTime_Type()
)
rgIpLanAddrLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rgIpLanAddrLeaseExpireTime.setStatus("current")


class _RgIpLanAddrHostName_Type(SnmpAdminString):
    """Custom type rgIpLanAddrHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RgIpLanAddrHostName_Type.__name__ = "SnmpAdminString"
_RgIpLanAddrHostName_Object = MibTableColumn
rgIpLanAddrHostName = _RgIpLanAddrHostName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 3, 1, 1, 6),
    _RgIpLanAddrHostName_Type()
)
rgIpLanAddrHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rgIpLanAddrHostName.setStatus("current")
_RgIpDnsServer_ObjectIdentity = ObjectIdentity
rgIpDnsServer = _RgIpDnsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4)
)
_RgIpDnsServerTable_Object = MibTable
rgIpDnsServerTable = _RgIpDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4, 1)
)
if mibBuilder.loadTexts:
    rgIpDnsServerTable.setStatus("current")
_RgIpDnsServerEntry_Object = MibTableRow
rgIpDnsServerEntry = _RgIpDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4, 1, 1)
)
rgIpDnsServerEntry.setIndexNames(
    (0, "BRCM-RG-IP-MIB", "rgIpDnsServerOrder"),
)
if mibBuilder.loadTexts:
    rgIpDnsServerEntry.setStatus("current")


class _RgIpDnsServerOrder_Type(Integer32):
    """Custom type rgIpDnsServerOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RgIpDnsServerOrder_Type.__name__ = "Integer32"
_RgIpDnsServerOrder_Object = MibTableColumn
rgIpDnsServerOrder = _RgIpDnsServerOrder_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4, 1, 1, 1),
    _RgIpDnsServerOrder_Type()
)
rgIpDnsServerOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rgIpDnsServerOrder.setStatus("current")


class _RgIpDnsServerIpType_Type(InetAddressType):
    """Custom type rgIpDnsServerIpType based on InetAddressType"""
    defaultValue = 1


_RgIpDnsServerIpType_Type.__name__ = "InetAddressType"
_RgIpDnsServerIpType_Object = MibTableColumn
rgIpDnsServerIpType = _RgIpDnsServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4, 1, 1, 2),
    _RgIpDnsServerIpType_Type()
)
rgIpDnsServerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDnsServerIpType.setStatus("current")
_RgIpDnsServerIp_Type = InetAddress
_RgIpDnsServerIp_Object = MibTableColumn
rgIpDnsServerIp = _RgIpDnsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4, 1, 1, 3),
    _RgIpDnsServerIp_Type()
)
rgIpDnsServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDnsServerIp.setStatus("current")
_RgIpDnsServerRowStatus_Type = RowStatus
_RgIpDnsServerRowStatus_Object = MibTableColumn
rgIpDnsServerRowStatus = _RgIpDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 4, 1, 1, 4),
    _RgIpDnsServerRowStatus_Type()
)
rgIpDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDnsServerRowStatus.setStatus("current")
_RgIpDhcpServer_ObjectIdentity = ObjectIdentity
rgIpDhcpServer = _RgIpDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5)
)
_RgIpDhcpServerTable_Object = MibTable
rgIpDhcpServerTable = _RgIpDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rgIpDhcpServerTable.setStatus("current")
_RgIpDhcpServerEntry_Object = MibTableRow
rgIpDhcpServerEntry = _RgIpDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1)
)
rgIpDhcpServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rgIpDhcpServerEntry.setStatus("current")


class _RgIpDhcpServerLanPoolStartType_Type(InetAddressType):
    """Custom type rgIpDhcpServerLanPoolStartType based on InetAddressType"""
    defaultValue = 1


_RgIpDhcpServerLanPoolStartType_Type.__name__ = "InetAddressType"
_RgIpDhcpServerLanPoolStartType_Object = MibTableColumn
rgIpDhcpServerLanPoolStartType = _RgIpDhcpServerLanPoolStartType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1, 1),
    _RgIpDhcpServerLanPoolStartType_Type()
)
rgIpDhcpServerLanPoolStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDhcpServerLanPoolStartType.setStatus("current")
_RgIpDhcpServerLanPoolStart_Type = InetAddress
_RgIpDhcpServerLanPoolStart_Object = MibTableColumn
rgIpDhcpServerLanPoolStart = _RgIpDhcpServerLanPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1, 2),
    _RgIpDhcpServerLanPoolStart_Type()
)
rgIpDhcpServerLanPoolStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDhcpServerLanPoolStart.setStatus("current")


class _RgIpDhcpServerLanPoolEndType_Type(InetAddressType):
    """Custom type rgIpDhcpServerLanPoolEndType based on InetAddressType"""
    defaultValue = 1


_RgIpDhcpServerLanPoolEndType_Type.__name__ = "InetAddressType"
_RgIpDhcpServerLanPoolEndType_Object = MibTableColumn
rgIpDhcpServerLanPoolEndType = _RgIpDhcpServerLanPoolEndType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1, 3),
    _RgIpDhcpServerLanPoolEndType_Type()
)
rgIpDhcpServerLanPoolEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDhcpServerLanPoolEndType.setStatus("current")
_RgIpDhcpServerLanPoolEnd_Type = InetAddress
_RgIpDhcpServerLanPoolEnd_Object = MibTableColumn
rgIpDhcpServerLanPoolEnd = _RgIpDhcpServerLanPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1, 4),
    _RgIpDhcpServerLanPoolEnd_Type()
)
rgIpDhcpServerLanPoolEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDhcpServerLanPoolEnd.setStatus("current")


class _RgIpDhcpServerLeaseTime_Type(Unsigned32):
    """Custom type rgIpDhcpServerLeaseTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RgIpDhcpServerLeaseTime_Type.__name__ = "Unsigned32"
_RgIpDhcpServerLeaseTime_Object = MibTableColumn
rgIpDhcpServerLeaseTime = _RgIpDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1, 5),
    _RgIpDhcpServerLeaseTime_Type()
)
rgIpDhcpServerLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDhcpServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    rgIpDhcpServerLeaseTime.setUnits("seconds")
_RgIpDhcpServerRowStatus_Type = RowStatus
_RgIpDhcpServerRowStatus_Object = MibTableColumn
rgIpDhcpServerRowStatus = _RgIpDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 5, 1, 1, 6),
    _RgIpDhcpServerRowStatus_Type()
)
rgIpDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpDhcpServerRowStatus.setStatus("current")
_RgIpRoute_ObjectIdentity = ObjectIdentity
rgIpRoute = _RgIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6)
)
_RgIpRouteTable_Object = MibTable
rgIpRouteTable = _RgIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1)
)
if mibBuilder.loadTexts:
    rgIpRouteTable.setStatus("current")
_RgIpRouteEntry_Object = MibTableRow
rgIpRouteEntry = _RgIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1)
)
rgIpRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rgIpRouteEntry.setStatus("current")


class _RgIpRouteMode_Type(Integer32):
    """Custom type rgIpRouteMode based on Integer32"""
    defaultValue = 1

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
        *(("napt", 1),
          ("bridged", 2),
          ("routeddhcp", 3),
          ("routedstatic", 4))
    )


_RgIpRouteMode_Type.__name__ = "Integer32"
_RgIpRouteMode_Object = MibTableColumn
rgIpRouteMode = _RgIpRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 1),
    _RgIpRouteMode_Type()
)
rgIpRouteMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteMode.setStatus("current")


class _RgIpRouteNetworkNumberType_Type(InetAddressType):
    """Custom type rgIpRouteNetworkNumberType based on InetAddressType"""
    defaultValue = 1


_RgIpRouteNetworkNumberType_Type.__name__ = "InetAddressType"
_RgIpRouteNetworkNumberType_Object = MibTableColumn
rgIpRouteNetworkNumberType = _RgIpRouteNetworkNumberType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 2),
    _RgIpRouteNetworkNumberType_Type()
)
rgIpRouteNetworkNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteNetworkNumberType.setStatus("current")
_RgIpRouteNetworkNumber_Type = InetAddress
_RgIpRouteNetworkNumber_Object = MibTableColumn
rgIpRouteNetworkNumber = _RgIpRouteNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 3),
    _RgIpRouteNetworkNumber_Type()
)
rgIpRouteNetworkNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteNetworkNumber.setStatus("current")


class _RgIpRouteSubnetMaskType_Type(InetAddressType):
    """Custom type rgIpRouteSubnetMaskType based on InetAddressType"""
    defaultValue = 1


_RgIpRouteSubnetMaskType_Type.__name__ = "InetAddressType"
_RgIpRouteSubnetMaskType_Object = MibTableColumn
rgIpRouteSubnetMaskType = _RgIpRouteSubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 4),
    _RgIpRouteSubnetMaskType_Type()
)
rgIpRouteSubnetMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteSubnetMaskType.setStatus("current")
_RgIpRouteSubnetMask_Type = InetAddress
_RgIpRouteSubnetMask_Object = MibTableColumn
rgIpRouteSubnetMask = _RgIpRouteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 5),
    _RgIpRouteSubnetMask_Type()
)
rgIpRouteSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteSubnetMask.setStatus("current")


class _RgIpRouteGatewayIpType_Type(InetAddressType):
    """Custom type rgIpRouteGatewayIpType based on InetAddressType"""
    defaultValue = 1


_RgIpRouteGatewayIpType_Type.__name__ = "InetAddressType"
_RgIpRouteGatewayIpType_Object = MibTableColumn
rgIpRouteGatewayIpType = _RgIpRouteGatewayIpType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 6),
    _RgIpRouteGatewayIpType_Type()
)
rgIpRouteGatewayIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteGatewayIpType.setStatus("current")
_RgIpRouteGatewayIp_Type = InetAddress
_RgIpRouteGatewayIp_Object = MibTableColumn
rgIpRouteGatewayIp = _RgIpRouteGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 7),
    _RgIpRouteGatewayIp_Type()
)
rgIpRouteGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteGatewayIp.setStatus("current")


class _RgIpRouteTypeOfService_Type(Integer32):
    """Custom type rgIpRouteTypeOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RgIpRouteTypeOfService_Type.__name__ = "Integer32"
_RgIpRouteTypeOfService_Object = MibTableColumn
rgIpRouteTypeOfService = _RgIpRouteTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 8),
    _RgIpRouteTypeOfService_Type()
)
rgIpRouteTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteTypeOfService.setStatus("current")


class _RgIpRouteFirewallEnable_Type(TruthValue):
    """Custom type rgIpRouteFirewallEnable based on TruthValue"""
    defaultValue = 1


_RgIpRouteFirewallEnable_Type.__name__ = "TruthValue"
_RgIpRouteFirewallEnable_Object = MibTableColumn
rgIpRouteFirewallEnable = _RgIpRouteFirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 9),
    _RgIpRouteFirewallEnable_Type()
)
rgIpRouteFirewallEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteFirewallEnable.setStatus("current")
_RgIpRouteRowStatus_Type = RowStatus
_RgIpRouteRowStatus_Object = MibTableColumn
rgIpRouteRowStatus = _RgIpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 2, 6, 1, 1, 10),
    _RgIpRouteRowStatus_Type()
)
rgIpRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rgIpRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-RG-IP-MIB",
    **{"rgIpMib": rgIpMib,
       "rgIpNetworkSettingsCommit": rgIpNetworkSettingsCommit,
       "rgIpRipSettings": rgIpRipSettings,
       "rgIpRipEnable": rgIpRipEnable,
       "rgIpRipMd5AuthEnable": rgIpRipMd5AuthEnable,
       "rgIpRipMd5KeyId": rgIpRipMd5KeyId,
       "rgIpRipMd5KeyValue": rgIpRipMd5KeyValue,
       "rgIpRipInterval": rgIpRipInterval,
       "rgIpRipDestIpAddressType": rgIpRipDestIpAddressType,
       "rgIpRipDestIpAddress": rgIpRipDestIpAddress,
       "rgIpLanAddr": rgIpLanAddr,
       "rgIpLanAddrTable": rgIpLanAddrTable,
       "rgIpLanAddrBaseEntry": rgIpLanAddrBaseEntry,
       "rgIpLanAddrIpType": rgIpLanAddrIpType,
       "rgIpLanAddrIp": rgIpLanAddrIp,
       "rgIpLanAddrClientID": rgIpLanAddrClientID,
       "rgIpLanAddrLeaseCreateTime": rgIpLanAddrLeaseCreateTime,
       "rgIpLanAddrLeaseExpireTime": rgIpLanAddrLeaseExpireTime,
       "rgIpLanAddrHostName": rgIpLanAddrHostName,
       "rgIpDnsServer": rgIpDnsServer,
       "rgIpDnsServerTable": rgIpDnsServerTable,
       "rgIpDnsServerEntry": rgIpDnsServerEntry,
       "rgIpDnsServerOrder": rgIpDnsServerOrder,
       "rgIpDnsServerIpType": rgIpDnsServerIpType,
       "rgIpDnsServerIp": rgIpDnsServerIp,
       "rgIpDnsServerRowStatus": rgIpDnsServerRowStatus,
       "rgIpDhcpServer": rgIpDhcpServer,
       "rgIpDhcpServerTable": rgIpDhcpServerTable,
       "rgIpDhcpServerEntry": rgIpDhcpServerEntry,
       "rgIpDhcpServerLanPoolStartType": rgIpDhcpServerLanPoolStartType,
       "rgIpDhcpServerLanPoolStart": rgIpDhcpServerLanPoolStart,
       "rgIpDhcpServerLanPoolEndType": rgIpDhcpServerLanPoolEndType,
       "rgIpDhcpServerLanPoolEnd": rgIpDhcpServerLanPoolEnd,
       "rgIpDhcpServerLeaseTime": rgIpDhcpServerLeaseTime,
       "rgIpDhcpServerRowStatus": rgIpDhcpServerRowStatus,
       "rgIpRoute": rgIpRoute,
       "rgIpRouteTable": rgIpRouteTable,
       "rgIpRouteEntry": rgIpRouteEntry,
       "rgIpRouteMode": rgIpRouteMode,
       "rgIpRouteNetworkNumberType": rgIpRouteNetworkNumberType,
       "rgIpRouteNetworkNumber": rgIpRouteNetworkNumber,
       "rgIpRouteSubnetMaskType": rgIpRouteSubnetMaskType,
       "rgIpRouteSubnetMask": rgIpRouteSubnetMask,
       "rgIpRouteGatewayIpType": rgIpRouteGatewayIpType,
       "rgIpRouteGatewayIp": rgIpRouteGatewayIp,
       "rgIpRouteTypeOfService": rgIpRouteTypeOfService,
       "rgIpRouteFirewallEnable": rgIpRouteFirewallEnable,
       "rgIpRouteRowStatus": rgIpRouteRowStatus}
)
