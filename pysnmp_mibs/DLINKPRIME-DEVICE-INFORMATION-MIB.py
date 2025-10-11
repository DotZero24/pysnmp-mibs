# SNMP MIB module (DLINKPRIME-DEVICE-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-DEVICE-INFORMATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:34 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeDeviceInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 3)
)
if mibBuilder.loadTexts:
    dlinkPrimeDeviceInfoMIB.setRevisions(
        ("2014-05-30 00:00",)
    )


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



class Ipv6Address(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_DpDeviceInfoMIBObjects_ObjectIdentity = ObjectIdentity
dpDeviceInfoMIBObjects = _DpDeviceInfoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1)
)
_DpDeviceInfoSysConfiguration_ObjectIdentity = ObjectIdentity
dpDeviceInfoSysConfiguration = _DpDeviceInfoSysConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1)
)


class _DpDeviceInfoIpV4AddrCfgMode_Type(Integer32):
    """Custom type dpDeviceInfoIpV4AddrCfgMode based on Integer32"""
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
        *(("manual", 1),
          ("dhcp", 2),
          ("bootp", 3))
    )


_DpDeviceInfoIpV4AddrCfgMode_Type.__name__ = "Integer32"
_DpDeviceInfoIpV4AddrCfgMode_Object = MibScalar
dpDeviceInfoIpV4AddrCfgMode = _DpDeviceInfoIpV4AddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 1),
    _DpDeviceInfoIpV4AddrCfgMode_Type()
)
dpDeviceInfoIpV4AddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoIpV4AddrCfgMode.setStatus("current")
_DpDeviceInfoIpV4Addr_Type = IpAddress
_DpDeviceInfoIpV4Addr_Object = MibScalar
dpDeviceInfoIpV4Addr = _DpDeviceInfoIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 2),
    _DpDeviceInfoIpV4Addr_Type()
)
dpDeviceInfoIpV4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoIpV4Addr.setStatus("current")
_DpDeviceInfoIpV4SubnetMask_Type = IpAddress
_DpDeviceInfoIpV4SubnetMask_Object = MibScalar
dpDeviceInfoIpV4SubnetMask = _DpDeviceInfoIpV4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 3),
    _DpDeviceInfoIpV4SubnetMask_Type()
)
dpDeviceInfoIpV4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoIpV4SubnetMask.setStatus("current")
_DpDeviceInfoGateway_Type = IpAddress
_DpDeviceInfoGateway_Object = MibScalar
dpDeviceInfoGateway = _DpDeviceInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 4),
    _DpDeviceInfoGateway_Type()
)
dpDeviceInfoGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoGateway.setStatus("current")


class _DpDeviceInfoDhcpRetry_Type(Unsigned32):
    """Custom type dpDeviceInfoDhcpRetry based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 128),
    )


_DpDeviceInfoDhcpRetry_Type.__name__ = "Unsigned32"
_DpDeviceInfoDhcpRetry_Object = MibScalar
dpDeviceInfoDhcpRetry = _DpDeviceInfoDhcpRetry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 5),
    _DpDeviceInfoDhcpRetry_Type()
)
dpDeviceInfoDhcpRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoDhcpRetry.setStatus("current")


class _DpDeviceInfoIpV6GlobalState_Type(Integer32):
    """Custom type dpDeviceInfoIpV6GlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DpDeviceInfoIpV6GlobalState_Type.__name__ = "Integer32"
_DpDeviceInfoIpV6GlobalState_Object = MibScalar
dpDeviceInfoIpV6GlobalState = _DpDeviceInfoIpV6GlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 6),
    _DpDeviceInfoIpV6GlobalState_Type()
)
dpDeviceInfoIpV6GlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoIpV6GlobalState.setStatus("current")
_DpDeviceInfoIpV6AddressIpAddr_Type = Ipv6Address
_DpDeviceInfoIpV6AddressIpAddr_Object = MibScalar
dpDeviceInfoIpV6AddressIpAddr = _DpDeviceInfoIpV6AddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 7),
    _DpDeviceInfoIpV6AddressIpAddr_Type()
)
dpDeviceInfoIpV6AddressIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDeviceInfoIpV6AddressIpAddr.setStatus("current")
_DpDeviceInfoMacAddr_Type = MacAddress
_DpDeviceInfoMacAddr_Object = MibScalar
dpDeviceInfoMacAddr = _DpDeviceInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 2),
    _DpDeviceInfoMacAddr_Type()
)
dpDeviceInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpDeviceInfoMacAddr.setStatus("current")


class _DpDeviceInfoBootPromVersion_Type(DisplayString):
    """Custom type dpDeviceInfoBootPromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DpDeviceInfoBootPromVersion_Type.__name__ = "DisplayString"
_DpDeviceInfoBootPromVersion_Object = MibScalar
dpDeviceInfoBootPromVersion = _DpDeviceInfoBootPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 3),
    _DpDeviceInfoBootPromVersion_Type()
)
dpDeviceInfoBootPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpDeviceInfoBootPromVersion.setStatus("current")


class _DpDeviceInfoFirmwareVersion_Type(DisplayString):
    """Custom type dpDeviceInfoFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DpDeviceInfoFirmwareVersion_Type.__name__ = "DisplayString"
_DpDeviceInfoFirmwareVersion_Object = MibScalar
dpDeviceInfoFirmwareVersion = _DpDeviceInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 4),
    _DpDeviceInfoFirmwareVersion_Type()
)
dpDeviceInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpDeviceInfoFirmwareVersion.setStatus("current")


class _DpDeviceInfoHardwareVersion_Type(DisplayString):
    """Custom type dpDeviceInfoHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DpDeviceInfoHardwareVersion_Type.__name__ = "DisplayString"
_DpDeviceInfoHardwareVersion_Object = MibScalar
dpDeviceInfoHardwareVersion = _DpDeviceInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 5),
    _DpDeviceInfoHardwareVersion_Type()
)
dpDeviceInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpDeviceInfoHardwareVersion.setStatus("current")
_DpDeviceInfoSerialNumber_Type = DisplayString
_DpDeviceInfoSerialNumber_Object = MibScalar
dpDeviceInfoSerialNumber = _DpDeviceInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 6),
    _DpDeviceInfoSerialNumber_Type()
)
dpDeviceInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpDeviceInfoSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-DEVICE-INFORMATION-MIB",
    **{"MacAddress": MacAddress,
       "Ipv6Address": Ipv6Address,
       "dlinkPrimeDeviceInfoMIB": dlinkPrimeDeviceInfoMIB,
       "dpDeviceInfoMIBObjects": dpDeviceInfoMIBObjects,
       "dpDeviceInfoSysConfiguration": dpDeviceInfoSysConfiguration,
       "dpDeviceInfoIpV4AddrCfgMode": dpDeviceInfoIpV4AddrCfgMode,
       "dpDeviceInfoIpV4Addr": dpDeviceInfoIpV4Addr,
       "dpDeviceInfoIpV4SubnetMask": dpDeviceInfoIpV4SubnetMask,
       "dpDeviceInfoGateway": dpDeviceInfoGateway,
       "dpDeviceInfoDhcpRetry": dpDeviceInfoDhcpRetry,
       "dpDeviceInfoIpV6GlobalState": dpDeviceInfoIpV6GlobalState,
       "dpDeviceInfoIpV6AddressIpAddr": dpDeviceInfoIpV6AddressIpAddr,
       "dpDeviceInfoMacAddr": dpDeviceInfoMacAddr,
       "dpDeviceInfoBootPromVersion": dpDeviceInfoBootPromVersion,
       "dpDeviceInfoFirmwareVersion": dpDeviceInfoFirmwareVersion,
       "dpDeviceInfoHardwareVersion": dpDeviceInfoHardwareVersion,
       "dpDeviceInfoSerialNumber": dpDeviceInfoSerialNumber}
)
