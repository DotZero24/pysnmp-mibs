# SNMP MIB module (HIRSCHMANN-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-ROUTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:45 2025
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_HmConfiguration_ObjectIdentity = ObjectIdentity
hmConfiguration = _HmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14)
)
_HmRouter_ObjectIdentity = ObjectIdentity
hmRouter = _HmRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6)
)
_HmRouterMisc_ObjectIdentity = ObjectIdentity
hmRouterMisc = _HmRouterMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1)
)
_HmRouterNumInterfaces_Type = Integer32
_HmRouterNumInterfaces_Object = MibScalar
hmRouterNumInterfaces = _HmRouterNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 1),
    _HmRouterNumInterfaces_Type()
)
hmRouterNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterNumInterfaces.setStatus("mandatory")
_HmRouterMaxHostRouteEntries_Type = Integer32
_HmRouterMaxHostRouteEntries_Object = MibScalar
hmRouterMaxHostRouteEntries = _HmRouterMaxHostRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 2),
    _HmRouterMaxHostRouteEntries_Type()
)
hmRouterMaxHostRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterMaxHostRouteEntries.setStatus("mandatory")
_HmRouterMaxSubnetRouteEntries_Type = Integer32
_HmRouterMaxSubnetRouteEntries_Object = MibScalar
hmRouterMaxSubnetRouteEntries = _HmRouterMaxSubnetRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 3),
    _HmRouterMaxSubnetRouteEntries_Type()
)
hmRouterMaxSubnetRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterMaxSubnetRouteEntries.setStatus("mandatory")


class _HmRouterRipEnable_Type(Integer32):
    """Custom type hmRouterRipEnable based on Integer32"""
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


_HmRouterRipEnable_Type.__name__ = "Integer32"
_HmRouterRipEnable_Object = MibScalar
hmRouterRipEnable = _HmRouterRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 4),
    _HmRouterRipEnable_Type()
)
hmRouterRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterRipEnable.setStatus("mandatory")


class _HmRouterOspfEnable_Type(Integer32):
    """Custom type hmRouterOspfEnable based on Integer32"""
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


_HmRouterOspfEnable_Type.__name__ = "Integer32"
_HmRouterOspfEnable_Object = MibScalar
hmRouterOspfEnable = _HmRouterOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 5),
    _HmRouterOspfEnable_Type()
)
hmRouterOspfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterOspfEnable.setStatus("mandatory")
_HmRouterDHCPServerIpAddr_Type = IpAddress
_HmRouterDHCPServerIpAddr_Object = MibScalar
hmRouterDHCPServerIpAddr = _HmRouterDHCPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 6),
    _HmRouterDHCPServerIpAddr_Type()
)
hmRouterDHCPServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterDHCPServerIpAddr.setStatus("mandatory")
_HmRouterDHCPServer2IpAddr_Type = IpAddress
_HmRouterDHCPServer2IpAddr_Object = MibScalar
hmRouterDHCPServer2IpAddr = _HmRouterDHCPServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 7),
    _HmRouterDHCPServer2IpAddr_Type()
)
hmRouterDHCPServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterDHCPServer2IpAddr.setStatus("mandatory")
_HmRouterDHCPServer3IpAddr_Type = IpAddress
_HmRouterDHCPServer3IpAddr_Object = MibScalar
hmRouterDHCPServer3IpAddr = _HmRouterDHCPServer3IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 8),
    _HmRouterDHCPServer3IpAddr_Type()
)
hmRouterDHCPServer3IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterDHCPServer3IpAddr.setStatus("mandatory")
_HmRouterDHCPServer4IpAddr_Type = IpAddress
_HmRouterDHCPServer4IpAddr_Object = MibScalar
hmRouterDHCPServer4IpAddr = _HmRouterDHCPServer4IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 1, 9),
    _HmRouterDHCPServer4IpAddr_Type()
)
hmRouterDHCPServer4IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterDHCPServer4IpAddr.setStatus("mandatory")
_HmRouterIfTable_Object = MibTable
hmRouterIfTable = _HmRouterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2)
)
if mibBuilder.loadTexts:
    hmRouterIfTable.setStatus("mandatory")
_HmRouterIfEntry_Object = MibTableRow
hmRouterIfEntry = _HmRouterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1)
)
hmRouterIfEntry.setIndexNames(
    (0, "HIRSCHMANN-ROUTER-MIB", "hmRouterIfIndex"),
)
if mibBuilder.loadTexts:
    hmRouterIfEntry.setStatus("mandatory")
_HmRouterIfIndex_Type = Integer32
_HmRouterIfIndex_Object = MibTableColumn
hmRouterIfIndex = _HmRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 1),
    _HmRouterIfIndex_Type()
)
hmRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterIfIndex.setStatus("mandatory")


class _HmRouterIfVlanID_Type(Integer32):
    """Custom type hmRouterIfVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HmRouterIfVlanID_Type.__name__ = "Integer32"
_HmRouterIfVlanID_Object = MibTableColumn
hmRouterIfVlanID = _HmRouterIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 2),
    _HmRouterIfVlanID_Type()
)
hmRouterIfVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIfVlanID.setStatus("mandatory")
_HmRouterIfIpAddr_Type = IpAddress
_HmRouterIfIpAddr_Object = MibTableColumn
hmRouterIfIpAddr = _HmRouterIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 3),
    _HmRouterIfIpAddr_Type()
)
hmRouterIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIfIpAddr.setStatus("mandatory")
_HmRouterIfSubnetMask_Type = IpAddress
_HmRouterIfSubnetMask_Object = MibTableColumn
hmRouterIfSubnetMask = _HmRouterIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 4),
    _HmRouterIfSubnetMask_Type()
)
hmRouterIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIfSubnetMask.setStatus("mandatory")


class _HmRouterIfName_Type(DisplayString):
    """Custom type hmRouterIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmRouterIfName_Type.__name__ = "DisplayString"
_HmRouterIfName_Object = MibTableColumn
hmRouterIfName = _HmRouterIfName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 5),
    _HmRouterIfName_Type()
)
hmRouterIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIfName.setStatus("mandatory")


class _HmRouterIfAdminStatus_Type(Integer32):
    """Custom type hmRouterIfAdminStatus based on Integer32"""
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


_HmRouterIfAdminStatus_Type.__name__ = "Integer32"
_HmRouterIfAdminStatus_Object = MibTableColumn
hmRouterIfAdminStatus = _HmRouterIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 6),
    _HmRouterIfAdminStatus_Type()
)
hmRouterIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIfAdminStatus.setStatus("mandatory")


class _HmRouterIfOperStatus_Type(Integer32):
    """Custom type hmRouterIfOperStatus based on Integer32"""
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


_HmRouterIfOperStatus_Type.__name__ = "Integer32"
_HmRouterIfOperStatus_Object = MibTableColumn
hmRouterIfOperStatus = _HmRouterIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 7),
    _HmRouterIfOperStatus_Type()
)
hmRouterIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterIfOperStatus.setStatus("mandatory")
_HmRouterIfRedundantIpAddr_Type = IpAddress
_HmRouterIfRedundantIpAddr_Object = MibTableColumn
hmRouterIfRedundantIpAddr = _HmRouterIfRedundantIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 2, 1, 8),
    _HmRouterIfRedundantIpAddr_Type()
)
hmRouterIfRedundantIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIfRedundantIpAddr.setStatus("mandatory")
_HmRouterStaticTable_Object = MibTable
hmRouterStaticTable = _HmRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4)
)
if mibBuilder.loadTexts:
    hmRouterStaticTable.setStatus("mandatory")
_HmRouterStaticEntry_Object = MibTableRow
hmRouterStaticEntry = _HmRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4, 1)
)
hmRouterStaticEntry.setIndexNames(
    (0, "HIRSCHMANN-ROUTER-MIB", "hmRouterStaticDestIpAddr"),
)
if mibBuilder.loadTexts:
    hmRouterStaticEntry.setStatus("mandatory")
_HmRouterStaticDestIpAddr_Type = IpAddress
_HmRouterStaticDestIpAddr_Object = MibTableColumn
hmRouterStaticDestIpAddr = _HmRouterStaticDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4, 1, 1),
    _HmRouterStaticDestIpAddr_Type()
)
hmRouterStaticDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterStaticDestIpAddr.setStatus("mandatory")
_HmRouterStaticMask_Type = IpAddress
_HmRouterStaticMask_Object = MibTableColumn
hmRouterStaticMask = _HmRouterStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4, 1, 2),
    _HmRouterStaticMask_Type()
)
hmRouterStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticMask.setStatus("mandatory")
_HmRouterStaticNextHop_Type = IpAddress
_HmRouterStaticNextHop_Object = MibTableColumn
hmRouterStaticNextHop = _HmRouterStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4, 1, 3),
    _HmRouterStaticNextHop_Type()
)
hmRouterStaticNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticNextHop.setStatus("mandatory")


class _HmRouterStaticRouteName_Type(DisplayString):
    """Custom type hmRouterStaticRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmRouterStaticRouteName_Type.__name__ = "DisplayString"
_HmRouterStaticRouteName_Object = MibTableColumn
hmRouterStaticRouteName = _HmRouterStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4, 1, 4),
    _HmRouterStaticRouteName_Type()
)
hmRouterStaticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticRouteName.setStatus("mandatory")


class _HmRouterStaticRouteType_Type(Integer32):
    """Custom type hmRouterStaticRouteType based on Integer32"""
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
          ("invalid", 2),
          ("direct", 3),
          ("indirect", 4))
    )


_HmRouterStaticRouteType_Type.__name__ = "Integer32"
_HmRouterStaticRouteType_Object = MibTableColumn
hmRouterStaticRouteType = _HmRouterStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 4, 1, 5),
    _HmRouterStaticRouteType_Type()
)
hmRouterStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticRouteType.setStatus("mandatory")
_HmRouterOptions_ObjectIdentity = ObjectIdentity
hmRouterOptions = _HmRouterOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 5)
)


class _HmRouterIcmpTimeExceededMessage_Type(Integer32):
    """Custom type hmRouterIcmpTimeExceededMessage based on Integer32"""
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


_HmRouterIcmpTimeExceededMessage_Type.__name__ = "Integer32"
_HmRouterIcmpTimeExceededMessage_Object = MibScalar
hmRouterIcmpTimeExceededMessage = _HmRouterIcmpTimeExceededMessage_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 5, 1),
    _HmRouterIcmpTimeExceededMessage_Type()
)
hmRouterIcmpTimeExceededMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterIcmpTimeExceededMessage.setStatus("mandatory")
_HmRouterStaticArpTable_Object = MibTable
hmRouterStaticArpTable = _HmRouterStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 6)
)
if mibBuilder.loadTexts:
    hmRouterStaticArpTable.setStatus("mandatory")
_HmRouterStaticArpEntry_Object = MibTableRow
hmRouterStaticArpEntry = _HmRouterStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 6, 1)
)
hmRouterStaticArpEntry.setIndexNames(
    (0, "HIRSCHMANN-ROUTER-MIB", "hmRouterStaticArpNetAddress"),
)
if mibBuilder.loadTexts:
    hmRouterStaticArpEntry.setStatus("mandatory")
_HmRouterStaticArpNetAddress_Type = IpAddress
_HmRouterStaticArpNetAddress_Object = MibTableColumn
hmRouterStaticArpNetAddress = _HmRouterStaticArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 6, 1, 1),
    _HmRouterStaticArpNetAddress_Type()
)
hmRouterStaticArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterStaticArpNetAddress.setStatus("mandatory")
_HmRouterStaticArpPhysAddress_Type = PhysAddress
_HmRouterStaticArpPhysAddress_Object = MibTableColumn
hmRouterStaticArpPhysAddress = _HmRouterStaticArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 6, 1, 2),
    _HmRouterStaticArpPhysAddress_Type()
)
hmRouterStaticArpPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticArpPhysAddress.setStatus("mandatory")


class _HmRouterStaticArpName_Type(DisplayString):
    """Custom type hmRouterStaticArpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmRouterStaticArpName_Type.__name__ = "DisplayString"
_HmRouterStaticArpName_Object = MibTableColumn
hmRouterStaticArpName = _HmRouterStaticArpName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 6, 1, 3),
    _HmRouterStaticArpName_Type()
)
hmRouterStaticArpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticArpName.setStatus("mandatory")


class _HmRouterStaticArpType_Type(Integer32):
    """Custom type hmRouterStaticArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("static", 3))
    )


_HmRouterStaticArpType_Type.__name__ = "Integer32"
_HmRouterStaticArpType_Object = MibTableColumn
hmRouterStaticArpType = _HmRouterStaticArpType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 6, 1, 4),
    _HmRouterStaticArpType_Type()
)
hmRouterStaticArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterStaticArpType.setStatus("mandatory")
_HmRouterRedundancy_ObjectIdentity = ObjectIdentity
hmRouterRedundancy = _HmRouterRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10)
)
_HmRouterRedConfiguration_ObjectIdentity = ObjectIdentity
hmRouterRedConfiguration = _HmRouterRedConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1)
)
_HmRouterRedPartnerIpAddress_Type = IpAddress
_HmRouterRedPartnerIpAddress_Object = MibScalar
hmRouterRedPartnerIpAddress = _HmRouterRedPartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 1),
    _HmRouterRedPartnerIpAddress_Type()
)
hmRouterRedPartnerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterRedPartnerIpAddress.setStatus("mandatory")


class _HmRouterRedPartnerInfo_Type(OctetString):
    """Custom type hmRouterRedPartnerInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_HmRouterRedPartnerInfo_Type.__name__ = "OctetString"
_HmRouterRedPartnerInfo_Object = MibScalar
hmRouterRedPartnerInfo = _HmRouterRedPartnerInfo_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 2),
    _HmRouterRedPartnerInfo_Type()
)
hmRouterRedPartnerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterRedPartnerInfo.setStatus("mandatory")


class _HmRouterRedMessageInterval_Type(Integer32):
    """Custom type hmRouterRedMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 5000),
    )


_HmRouterRedMessageInterval_Type.__name__ = "Integer32"
_HmRouterRedMessageInterval_Object = MibScalar
hmRouterRedMessageInterval = _HmRouterRedMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 3),
    _HmRouterRedMessageInterval_Type()
)
hmRouterRedMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterRedMessageInterval.setStatus("mandatory")


class _HmRouterRedMessageTimeout_Type(Integer32):
    """Custom type hmRouterRedMessageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_HmRouterRedMessageTimeout_Type.__name__ = "Integer32"
_HmRouterRedMessageTimeout_Object = MibScalar
hmRouterRedMessageTimeout = _HmRouterRedMessageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 4),
    _HmRouterRedMessageTimeout_Type()
)
hmRouterRedMessageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterRedMessageTimeout.setStatus("mandatory")


class _HmRouterRedAdminStatus_Type(Integer32):
    """Custom type hmRouterRedAdminStatus based on Integer32"""
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


_HmRouterRedAdminStatus_Type.__name__ = "Integer32"
_HmRouterRedAdminStatus_Object = MibScalar
hmRouterRedAdminStatus = _HmRouterRedAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 5),
    _HmRouterRedAdminStatus_Type()
)
hmRouterRedAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterRedAdminStatus.setStatus("mandatory")


class _HmRouterRedOperStatus_Type(Integer32):
    """Custom type hmRouterRedOperStatus based on Integer32"""
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
        *(("disable", 1),
          ("standby", 2),
          ("active", 3),
          ("other", 4))
    )


_HmRouterRedOperStatus_Type.__name__ = "Integer32"
_HmRouterRedOperStatus_Object = MibScalar
hmRouterRedOperStatus = _HmRouterRedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 6),
    _HmRouterRedOperStatus_Type()
)
hmRouterRedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterRedOperStatus.setStatus("mandatory")
_HmRouterRedLastErrorMessage_Type = DisplayString
_HmRouterRedLastErrorMessage_Object = MibScalar
hmRouterRedLastErrorMessage = _HmRouterRedLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 7),
    _HmRouterRedLastErrorMessage_Type()
)
hmRouterRedLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterRedLastErrorMessage.setStatus("mandatory")


class _HmRouterRedErrorStatus_Type(Integer32):
    """Custom type hmRouterRedErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("error", 2))
    )


_HmRouterRedErrorStatus_Type.__name__ = "Integer32"
_HmRouterRedErrorStatus_Object = MibScalar
hmRouterRedErrorStatus = _HmRouterRedErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 1, 8),
    _HmRouterRedErrorStatus_Type()
)
hmRouterRedErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterRedErrorStatus.setStatus("mandatory")
_HmRouterRedStats_ObjectIdentity = ObjectIdentity
hmRouterRedStats = _HmRouterRedStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 2)
)
_HmRouterRedStatsTakeoverCount_Type = Counter32
_HmRouterRedStatsTakeoverCount_Object = MibScalar
hmRouterRedStatsTakeoverCount = _HmRouterRedStatsTakeoverCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 2, 1),
    _HmRouterRedStatsTakeoverCount_Type()
)
hmRouterRedStatsTakeoverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterRedStatsTakeoverCount.setStatus("mandatory")
_HmRouterRedStatsLastChange_Type = TimeTicks
_HmRouterRedStatsLastChange_Object = MibScalar
hmRouterRedStatsLastChange = _HmRouterRedStatsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 2, 2),
    _HmRouterRedStatsLastChange_Type()
)
hmRouterRedStatsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterRedStatsLastChange.setStatus("mandatory")
_HmRouterForwardControl_ObjectIdentity = ObjectIdentity
hmRouterForwardControl = _HmRouterForwardControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11)
)


class _HmRouterForwardControlEnable_Type(Integer32):
    """Custom type hmRouterForwardControlEnable based on Integer32"""
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


_HmRouterForwardControlEnable_Type.__name__ = "Integer32"
_HmRouterForwardControlEnable_Object = MibScalar
hmRouterForwardControlEnable = _HmRouterForwardControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 1),
    _HmRouterForwardControlEnable_Type()
)
hmRouterForwardControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterForwardControlEnable.setStatus("mandatory")
_HmRouterForwardControlTable_Object = MibTable
hmRouterForwardControlTable = _HmRouterForwardControlTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 10)
)
if mibBuilder.loadTexts:
    hmRouterForwardControlTable.setStatus("mandatory")
_HmRouterForwardControlEntry_Object = MibTableRow
hmRouterForwardControlEntry = _HmRouterForwardControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 10, 1)
)
hmRouterForwardControlEntry.setIndexNames(
    (0, "HIRSCHMANN-ROUTER-MIB", "hmRouterForwardControlIndex"),
)
if mibBuilder.loadTexts:
    hmRouterForwardControlEntry.setStatus("mandatory")
_HmRouterForwardControlIndex_Type = Integer32
_HmRouterForwardControlIndex_Object = MibTableColumn
hmRouterForwardControlIndex = _HmRouterForwardControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 10, 1, 1),
    _HmRouterForwardControlIndex_Type()
)
hmRouterForwardControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmRouterForwardControlIndex.setStatus("mandatory")


class _HmRouterFCAllowedToGo_Type(OctetString):
    """Custom type hmRouterFCAllowedToGo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_HmRouterFCAllowedToGo_Type.__name__ = "OctetString"
_HmRouterFCAllowedToGo_Object = MibTableColumn
hmRouterFCAllowedToGo = _HmRouterFCAllowedToGo_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 10, 1, 2),
    _HmRouterFCAllowedToGo_Type()
)
hmRouterFCAllowedToGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRouterFCAllowedToGo.setStatus("mandatory")
_HmRouterFCIngressRejects_Type = Counter32
_HmRouterFCIngressRejects_Object = MibTableColumn
hmRouterFCIngressRejects = _HmRouterFCIngressRejects_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 10, 1, 3),
    _HmRouterFCIngressRejects_Type()
)
hmRouterFCIngressRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterFCIngressRejects.setStatus("mandatory")
_HmRouterFCEgressRejects_Type = Counter32
_HmRouterFCEgressRejects_Object = MibTableColumn
hmRouterFCEgressRejects = _HmRouterFCEgressRejects_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 11, 10, 1, 4),
    _HmRouterFCEgressRejects_Type()
)
hmRouterFCEgressRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRouterFCEgressRejects.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hmRouterRedTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 0, 1)
)
hmRouterRedTransition.setObjects(
    ("HIRSCHMANN-ROUTER-MIB", "hmRouterRedOperStatus")
)
if mibBuilder.loadTexts:
    hmRouterRedTransition.setStatus(
        ""
    )

hmRouterRedConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 6, 10, 0, 2)
)
hmRouterRedConfigError.setObjects(
      *(("HIRSCHMANN-ROUTER-MIB", "hmRouterRedErrorStatus"),
        ("HIRSCHMANN-ROUTER-MIB", "hmRouterRedLastErrorMessage"),
        ("HIRSCHMANN-ROUTER-MIB", "hmRouterRedOperStatus"))
)
if mibBuilder.loadTexts:
    hmRouterRedConfigError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-ROUTER-MIB",
    **{"enterprises": enterprises,
       "hirschmann": hirschmann,
       "hmConfiguration": hmConfiguration,
       "hmRouter": hmRouter,
       "hmRouterMisc": hmRouterMisc,
       "hmRouterNumInterfaces": hmRouterNumInterfaces,
       "hmRouterMaxHostRouteEntries": hmRouterMaxHostRouteEntries,
       "hmRouterMaxSubnetRouteEntries": hmRouterMaxSubnetRouteEntries,
       "hmRouterRipEnable": hmRouterRipEnable,
       "hmRouterOspfEnable": hmRouterOspfEnable,
       "hmRouterDHCPServerIpAddr": hmRouterDHCPServerIpAddr,
       "hmRouterDHCPServer2IpAddr": hmRouterDHCPServer2IpAddr,
       "hmRouterDHCPServer3IpAddr": hmRouterDHCPServer3IpAddr,
       "hmRouterDHCPServer4IpAddr": hmRouterDHCPServer4IpAddr,
       "hmRouterIfTable": hmRouterIfTable,
       "hmRouterIfEntry": hmRouterIfEntry,
       "hmRouterIfIndex": hmRouterIfIndex,
       "hmRouterIfVlanID": hmRouterIfVlanID,
       "hmRouterIfIpAddr": hmRouterIfIpAddr,
       "hmRouterIfSubnetMask": hmRouterIfSubnetMask,
       "hmRouterIfName": hmRouterIfName,
       "hmRouterIfAdminStatus": hmRouterIfAdminStatus,
       "hmRouterIfOperStatus": hmRouterIfOperStatus,
       "hmRouterIfRedundantIpAddr": hmRouterIfRedundantIpAddr,
       "hmRouterStaticTable": hmRouterStaticTable,
       "hmRouterStaticEntry": hmRouterStaticEntry,
       "hmRouterStaticDestIpAddr": hmRouterStaticDestIpAddr,
       "hmRouterStaticMask": hmRouterStaticMask,
       "hmRouterStaticNextHop": hmRouterStaticNextHop,
       "hmRouterStaticRouteName": hmRouterStaticRouteName,
       "hmRouterStaticRouteType": hmRouterStaticRouteType,
       "hmRouterOptions": hmRouterOptions,
       "hmRouterIcmpTimeExceededMessage": hmRouterIcmpTimeExceededMessage,
       "hmRouterStaticArpTable": hmRouterStaticArpTable,
       "hmRouterStaticArpEntry": hmRouterStaticArpEntry,
       "hmRouterStaticArpNetAddress": hmRouterStaticArpNetAddress,
       "hmRouterStaticArpPhysAddress": hmRouterStaticArpPhysAddress,
       "hmRouterStaticArpName": hmRouterStaticArpName,
       "hmRouterStaticArpType": hmRouterStaticArpType,
       "hmRouterRedundancy": hmRouterRedundancy,
       "hmRouterRedTransition": hmRouterRedTransition,
       "hmRouterRedConfigError": hmRouterRedConfigError,
       "hmRouterRedConfiguration": hmRouterRedConfiguration,
       "hmRouterRedPartnerIpAddress": hmRouterRedPartnerIpAddress,
       "hmRouterRedPartnerInfo": hmRouterRedPartnerInfo,
       "hmRouterRedMessageInterval": hmRouterRedMessageInterval,
       "hmRouterRedMessageTimeout": hmRouterRedMessageTimeout,
       "hmRouterRedAdminStatus": hmRouterRedAdminStatus,
       "hmRouterRedOperStatus": hmRouterRedOperStatus,
       "hmRouterRedLastErrorMessage": hmRouterRedLastErrorMessage,
       "hmRouterRedErrorStatus": hmRouterRedErrorStatus,
       "hmRouterRedStats": hmRouterRedStats,
       "hmRouterRedStatsTakeoverCount": hmRouterRedStatsTakeoverCount,
       "hmRouterRedStatsLastChange": hmRouterRedStatsLastChange,
       "hmRouterForwardControl": hmRouterForwardControl,
       "hmRouterForwardControlEnable": hmRouterForwardControlEnable,
       "hmRouterForwardControlTable": hmRouterForwardControlTable,
       "hmRouterForwardControlEntry": hmRouterForwardControlEntry,
       "hmRouterForwardControlIndex": hmRouterForwardControlIndex,
       "hmRouterFCAllowedToGo": hmRouterFCAllowedToGo,
       "hmRouterFCIngressRejects": hmRouterFCIngressRejects,
       "hmRouterFCEgressRejects": hmRouterFCEgressRejects}
)
