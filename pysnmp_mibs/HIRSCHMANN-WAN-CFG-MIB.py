# SNMP MIB module (HIRSCHMANN-WAN-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-WAN-CFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:52 2025
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

(hmWanMgmt,) = mibBuilder.importSymbols(
    "HIRSCHMANN-WAN-MIB",
    "hmWanMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hmWanCfgMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8)
)
if mibBuilder.loadTexts:
    hmWanCfgMib.setRevisions(
        ("2015-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HmWanIfIndexTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class HmWanLeaseDhcpIndexTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class HmWanStaticDhcpIndexTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



# MIB Managed Objects in the order of their OIDs

_HmWanEth_ObjectIdentity = ObjectIdentity
hmWanEth = _HmWanEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1)
)
_HmWanIfNumber_Type = Integer32
_HmWanIfNumber_Object = MibScalar
hmWanIfNumber = _HmWanIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 1),
    _HmWanIfNumber_Type()
)
hmWanIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanIfNumber.setStatus("current")
_HmWanIfTable_Object = MibTable
hmWanIfTable = _HmWanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hmWanIfTable.setStatus("current")
_HmWanIfEntry_Object = MibTableRow
hmWanIfEntry = _HmWanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1)
)
hmWanIfEntry.setIndexNames(
    (0, "HIRSCHMANN-WAN-CFG-MIB", "hmWanIfIndex"),
)
if mibBuilder.loadTexts:
    hmWanIfEntry.setStatus("current")
_HmWanIfIndex_Type = HmWanIfIndexTc
_HmWanIfIndex_Object = MibTableColumn
hmWanIfIndex = _HmWanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 1),
    _HmWanIfIndex_Type()
)
hmWanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanIfIndex.setStatus("current")


class _HmWanIfDhcpClient_Type(Integer32):
    """Custom type hmWanIfDhcpClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HmWanIfDhcpClient_Type.__name__ = "Integer32"
_HmWanIfDhcpClient_Object = MibTableColumn
hmWanIfDhcpClient = _HmWanIfDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 2),
    _HmWanIfDhcpClient_Type()
)
hmWanIfDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfDhcpClient.setStatus("current")
_HmWanIfIpAddress_Type = IpAddress
_HmWanIfIpAddress_Object = MibTableColumn
hmWanIfIpAddress = _HmWanIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 3),
    _HmWanIfIpAddress_Type()
)
hmWanIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfIpAddress.setStatus("current")
_HmWanIfSubnetMask_Type = IpAddress
_HmWanIfSubnetMask_Object = MibTableColumn
hmWanIfSubnetMask = _HmWanIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 4),
    _HmWanIfSubnetMask_Type()
)
hmWanIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfSubnetMask.setStatus("current")


class _HmWanIfBridged_Type(Integer32):
    """Custom type hmWanIfBridged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_HmWanIfBridged_Type.__name__ = "Integer32"
_HmWanIfBridged_Object = MibTableColumn
hmWanIfBridged = _HmWanIfBridged_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 5),
    _HmWanIfBridged_Type()
)
hmWanIfBridged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfBridged.setStatus("current")


class _HmWanIfMediaType_Type(Integer32):
    """Custom type hmWanIfMediaType based on Integer32"""
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
        *(("auto-negotiation", 1),
          ("full-duplex-100-Mbps", 2),
          ("half-duplex-100-Mbps", 3),
          ("full-duplex-10-Mbps", 4),
          ("half-duplex-10-Mbps", 5))
    )


_HmWanIfMediaType_Type.__name__ = "Integer32"
_HmWanIfMediaType_Object = MibTableColumn
hmWanIfMediaType = _HmWanIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 6),
    _HmWanIfMediaType_Type()
)
hmWanIfMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfMediaType.setStatus("current")
_HmWanIfDefaultGateway_Type = IpAddress
_HmWanIfDefaultGateway_Object = MibTableColumn
hmWanIfDefaultGateway = _HmWanIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 7),
    _HmWanIfDefaultGateway_Type()
)
hmWanIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfDefaultGateway.setStatus("current")
_HmWanIfDnsServer_Type = IpAddress
_HmWanIfDnsServer_Object = MibTableColumn
hmWanIfDnsServer = _HmWanIfDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 2, 1, 8),
    _HmWanIfDnsServer_Type()
)
hmWanIfDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIfDnsServer.setStatus("current")
_HmWanLeaseDhcpNumber_Type = Integer32
_HmWanLeaseDhcpNumber_Object = MibScalar
hmWanLeaseDhcpNumber = _HmWanLeaseDhcpNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 3),
    _HmWanLeaseDhcpNumber_Type()
)
hmWanLeaseDhcpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpNumber.setStatus("current")
_HmWanLeaseDhcpTable_Object = MibTable
hmWanLeaseDhcpTable = _HmWanLeaseDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hmWanLeaseDhcpTable.setStatus("current")
_HmWanLeaseDhcpEntry_Object = MibTableRow
hmWanLeaseDhcpEntry = _HmWanLeaseDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4, 1)
)
hmWanLeaseDhcpEntry.setIndexNames(
    (0, "HIRSCHMANN-WAN-CFG-MIB", "hmWanLeaseDhcpIndex"),
)
if mibBuilder.loadTexts:
    hmWanLeaseDhcpEntry.setStatus("current")
_HmWanLeaseDhcpIndex_Type = HmWanLeaseDhcpIndexTc
_HmWanLeaseDhcpIndex_Object = MibTableColumn
hmWanLeaseDhcpIndex = _HmWanLeaseDhcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4, 1, 1),
    _HmWanLeaseDhcpIndex_Type()
)
hmWanLeaseDhcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpIndex.setStatus("current")


class _HmWanLeaseDhcpServer_Type(Integer32):
    """Custom type hmWanLeaseDhcpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HmWanLeaseDhcpServer_Type.__name__ = "Integer32"
_HmWanLeaseDhcpServer_Object = MibTableColumn
hmWanLeaseDhcpServer = _HmWanLeaseDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4, 1, 2),
    _HmWanLeaseDhcpServer_Type()
)
hmWanLeaseDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpServer.setStatus("current")
_HmWanLeaseDhcpIpPoolStart_Type = IpAddress
_HmWanLeaseDhcpIpPoolStart_Object = MibTableColumn
hmWanLeaseDhcpIpPoolStart = _HmWanLeaseDhcpIpPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4, 1, 3),
    _HmWanLeaseDhcpIpPoolStart_Type()
)
hmWanLeaseDhcpIpPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpIpPoolStart.setStatus("current")
_HmWanLeaseDhcpIpPoolEnd_Type = IpAddress
_HmWanLeaseDhcpIpPoolEnd_Object = MibTableColumn
hmWanLeaseDhcpIpPoolEnd = _HmWanLeaseDhcpIpPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4, 1, 4),
    _HmWanLeaseDhcpIpPoolEnd_Type()
)
hmWanLeaseDhcpIpPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpIpPoolEnd.setStatus("current")


class _HmWanLeaseDhcpTime_Type(Integer32):
    """Custom type hmWanLeaseDhcpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_HmWanLeaseDhcpTime_Type.__name__ = "Integer32"
_HmWanLeaseDhcpTime_Object = MibTableColumn
hmWanLeaseDhcpTime = _HmWanLeaseDhcpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 4, 1, 5),
    _HmWanLeaseDhcpTime_Type()
)
hmWanLeaseDhcpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpTime.setStatus("current")
if mibBuilder.loadTexts:
    hmWanLeaseDhcpTime.setUnits("sec")


class _HmWanStaticDhcp_Type(Integer32):
    """Custom type hmWanStaticDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HmWanStaticDhcp_Type.__name__ = "Integer32"
_HmWanStaticDhcp_Object = MibScalar
hmWanStaticDhcp = _HmWanStaticDhcp_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 5),
    _HmWanStaticDhcp_Type()
)
hmWanStaticDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanStaticDhcp.setStatus("current")
_HmWanStaticDhcpNumber_Type = Integer32
_HmWanStaticDhcpNumber_Object = MibScalar
hmWanStaticDhcpNumber = _HmWanStaticDhcpNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 6),
    _HmWanStaticDhcpNumber_Type()
)
hmWanStaticDhcpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanStaticDhcpNumber.setStatus("current")
_HmWanStaticDhcpTable_Object = MibTable
hmWanStaticDhcpTable = _HmWanStaticDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 7)
)
if mibBuilder.loadTexts:
    hmWanStaticDhcpTable.setStatus("current")
_HmWanStaticDhcpEntry_Object = MibTableRow
hmWanStaticDhcpEntry = _HmWanStaticDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 7, 1)
)
hmWanStaticDhcpEntry.setIndexNames(
    (0, "HIRSCHMANN-WAN-CFG-MIB", "hmWanStaticDhcpIndex"),
)
if mibBuilder.loadTexts:
    hmWanStaticDhcpEntry.setStatus("current")
_HmWanStaticDhcpIndex_Type = HmWanStaticDhcpIndexTc
_HmWanStaticDhcpIndex_Object = MibTableColumn
hmWanStaticDhcpIndex = _HmWanStaticDhcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 7, 1, 1),
    _HmWanStaticDhcpIndex_Type()
)
hmWanStaticDhcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanStaticDhcpIndex.setStatus("current")
_HmWanStaticDhcpMacAddress_Type = MacAddress
_HmWanStaticDhcpMacAddress_Object = MibTableColumn
hmWanStaticDhcpMacAddress = _HmWanStaticDhcpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 7, 1, 2),
    _HmWanStaticDhcpMacAddress_Type()
)
hmWanStaticDhcpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanStaticDhcpMacAddress.setStatus("current")
_HmWanStaticDhcpIpAddress_Type = IpAddress
_HmWanStaticDhcpIpAddress_Object = MibTableColumn
hmWanStaticDhcpIpAddress = _HmWanStaticDhcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 1, 7, 1, 3),
    _HmWanStaticDhcpIpAddress_Type()
)
hmWanStaticDhcpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanStaticDhcpIpAddress.setStatus("current")
_HmWanSnmpCfg_ObjectIdentity = ObjectIdentity
hmWanSnmpCfg = _HmWanSnmpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17)
)


class _HmWanSnmpAdminStatus_Type(Integer32):
    """Custom type hmWanSnmpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanSnmpAdminStatus_Type.__name__ = "Integer32"
_HmWanSnmpAdminStatus_Object = MibScalar
hmWanSnmpAdminStatus = _HmWanSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 1),
    _HmWanSnmpAdminStatus_Type()
)
hmWanSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpAdminStatus.setStatus("current")


class _HmWanSnmpSysName_Type(DisplayString):
    """Custom type hmWanSnmpSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpSysName_Type.__name__ = "DisplayString"
_HmWanSnmpSysName_Object = MibScalar
hmWanSnmpSysName = _HmWanSnmpSysName_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 2),
    _HmWanSnmpSysName_Type()
)
hmWanSnmpSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpSysName.setStatus("current")


class _HmWanSnmpSysLocation_Type(DisplayString):
    """Custom type hmWanSnmpSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpSysLocation_Type.__name__ = "DisplayString"
_HmWanSnmpSysLocation_Object = MibScalar
hmWanSnmpSysLocation = _HmWanSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 3),
    _HmWanSnmpSysLocation_Type()
)
hmWanSnmpSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpSysLocation.setStatus("current")


class _HmWanSnmpSysContact_Type(DisplayString):
    """Custom type hmWanSnmpSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpSysContact_Type.__name__ = "DisplayString"
_HmWanSnmpSysContact_Object = MibScalar
hmWanSnmpSysContact = _HmWanSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 4),
    _HmWanSnmpSysContact_Type()
)
hmWanSnmpSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpSysContact.setStatus("current")


class _HmWanSnmpV1AccessAdminStatus_Type(Integer32):
    """Custom type hmWanSnmpV1AccessAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanSnmpV1AccessAdminStatus_Type.__name__ = "Integer32"
_HmWanSnmpV1AccessAdminStatus_Object = MibScalar
hmWanSnmpV1AccessAdminStatus = _HmWanSnmpV1AccessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 5),
    _HmWanSnmpV1AccessAdminStatus_Type()
)
hmWanSnmpV1AccessAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV1AccessAdminStatus.setStatus("current")


class _HmWanSnmpV1ReadCommunity_Type(DisplayString):
    """Custom type hmWanSnmpV1ReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpV1ReadCommunity_Type.__name__ = "DisplayString"
_HmWanSnmpV1ReadCommunity_Object = MibScalar
hmWanSnmpV1ReadCommunity = _HmWanSnmpV1ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 6),
    _HmWanSnmpV1ReadCommunity_Type()
)
hmWanSnmpV1ReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV1ReadCommunity.setStatus("current")


class _HmWanSnmpV1WriteCommunity_Type(DisplayString):
    """Custom type hmWanSnmpV1WriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpV1WriteCommunity_Type.__name__ = "DisplayString"
_HmWanSnmpV1WriteCommunity_Object = MibScalar
hmWanSnmpV1WriteCommunity = _HmWanSnmpV1WriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 7),
    _HmWanSnmpV1WriteCommunity_Type()
)
hmWanSnmpV1WriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV1WriteCommunity.setStatus("current")


class _HmWanSnmpV3AccessAdminStatus_Type(Integer32):
    """Custom type hmWanSnmpV3AccessAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanSnmpV3AccessAdminStatus_Type.__name__ = "Integer32"
_HmWanSnmpV3AccessAdminStatus_Object = MibScalar
hmWanSnmpV3AccessAdminStatus = _HmWanSnmpV3AccessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 8),
    _HmWanSnmpV3AccessAdminStatus_Type()
)
hmWanSnmpV3AccessAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3AccessAdminStatus.setStatus("current")


class _HmWanSnmpV33ReadUsername_Type(DisplayString):
    """Custom type hmWanSnmpV33ReadUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpV33ReadUsername_Type.__name__ = "DisplayString"
_HmWanSnmpV33ReadUsername_Object = MibScalar
hmWanSnmpV33ReadUsername = _HmWanSnmpV33ReadUsername_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 9),
    _HmWanSnmpV33ReadUsername_Type()
)
hmWanSnmpV33ReadUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV33ReadUsername.setStatus("current")


class _HmWanSnmpV3ReadAuth_Type(Integer32):
    """Custom type hmWanSnmpV3ReadAuth based on Integer32"""
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
          ("md5", 2),
          ("sha1", 3))
    )


_HmWanSnmpV3ReadAuth_Type.__name__ = "Integer32"
_HmWanSnmpV3ReadAuth_Object = MibScalar
hmWanSnmpV3ReadAuth = _HmWanSnmpV3ReadAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 10),
    _HmWanSnmpV3ReadAuth_Type()
)
hmWanSnmpV3ReadAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3ReadAuth.setStatus("current")


class _HmWanSnmpV3ReadAuthPwd_Type(DisplayString):
    """Custom type hmWanSnmpV3ReadAuthPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_HmWanSnmpV3ReadAuthPwd_Type.__name__ = "DisplayString"
_HmWanSnmpV3ReadAuthPwd_Object = MibScalar
hmWanSnmpV3ReadAuthPwd = _HmWanSnmpV3ReadAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 11),
    _HmWanSnmpV3ReadAuthPwd_Type()
)
hmWanSnmpV3ReadAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3ReadAuthPwd.setStatus("current")


class _HmWanSnmpV3ReadPrivProt_Type(Integer32):
    """Custom type hmWanSnmpV3ReadPrivProt based on Integer32"""
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
          ("des", 2),
          ("aes", 3))
    )


_HmWanSnmpV3ReadPrivProt_Type.__name__ = "Integer32"
_HmWanSnmpV3ReadPrivProt_Object = MibScalar
hmWanSnmpV3ReadPrivProt = _HmWanSnmpV3ReadPrivProt_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 12),
    _HmWanSnmpV3ReadPrivProt_Type()
)
hmWanSnmpV3ReadPrivProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3ReadPrivProt.setStatus("current")


class _HmWanSnmpV3ReadPrivPwd_Type(DisplayString):
    """Custom type hmWanSnmpV3ReadPrivPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_HmWanSnmpV3ReadPrivPwd_Type.__name__ = "DisplayString"
_HmWanSnmpV3ReadPrivPwd_Object = MibScalar
hmWanSnmpV3ReadPrivPwd = _HmWanSnmpV3ReadPrivPwd_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 13),
    _HmWanSnmpV3ReadPrivPwd_Type()
)
hmWanSnmpV3ReadPrivPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3ReadPrivPwd.setStatus("current")


class _HmWanSnmpV3WriteUsername_Type(DisplayString):
    """Custom type hmWanSnmpV3WriteUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanSnmpV3WriteUsername_Type.__name__ = "DisplayString"
_HmWanSnmpV3WriteUsername_Object = MibScalar
hmWanSnmpV3WriteUsername = _HmWanSnmpV3WriteUsername_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 14),
    _HmWanSnmpV3WriteUsername_Type()
)
hmWanSnmpV3WriteUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3WriteUsername.setStatus("current")


class _HmWanSnmpV3WriteAuth_Type(Integer32):
    """Custom type hmWanSnmpV3WriteAuth based on Integer32"""
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
          ("md5", 2),
          ("sha1", 3))
    )


_HmWanSnmpV3WriteAuth_Type.__name__ = "Integer32"
_HmWanSnmpV3WriteAuth_Object = MibScalar
hmWanSnmpV3WriteAuth = _HmWanSnmpV3WriteAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 15),
    _HmWanSnmpV3WriteAuth_Type()
)
hmWanSnmpV3WriteAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3WriteAuth.setStatus("current")


class _HmWanSnmpV3WriteAuthPwd_Type(DisplayString):
    """Custom type hmWanSnmpV3WriteAuthPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_HmWanSnmpV3WriteAuthPwd_Type.__name__ = "DisplayString"
_HmWanSnmpV3WriteAuthPwd_Object = MibScalar
hmWanSnmpV3WriteAuthPwd = _HmWanSnmpV3WriteAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 16),
    _HmWanSnmpV3WriteAuthPwd_Type()
)
hmWanSnmpV3WriteAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3WriteAuthPwd.setStatus("current")


class _HmWanSnmpV3WritePrivProt_Type(Integer32):
    """Custom type hmWanSnmpV3WritePrivProt based on Integer32"""
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
          ("des", 2),
          ("aes", 3))
    )


_HmWanSnmpV3WritePrivProt_Type.__name__ = "Integer32"
_HmWanSnmpV3WritePrivProt_Object = MibScalar
hmWanSnmpV3WritePrivProt = _HmWanSnmpV3WritePrivProt_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 17),
    _HmWanSnmpV3WritePrivProt_Type()
)
hmWanSnmpV3WritePrivProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3WritePrivProt.setStatus("current")


class _HmWanSnmpV3WritePrivPwd_Type(DisplayString):
    """Custom type hmWanSnmpV3WritePrivPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_HmWanSnmpV3WritePrivPwd_Type.__name__ = "DisplayString"
_HmWanSnmpV3WritePrivPwd_Object = MibScalar
hmWanSnmpV3WritePrivPwd = _HmWanSnmpV3WritePrivPwd_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 18),
    _HmWanSnmpV3WritePrivPwd_Type()
)
hmWanSnmpV3WritePrivPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanSnmpV3WritePrivPwd.setStatus("current")


class _HmWanIoExtensionAdminStatus_Type(Integer32):
    """Custom type hmWanIoExtensionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanIoExtensionAdminStatus_Type.__name__ = "Integer32"
_HmWanIoExtensionAdminStatus_Object = MibScalar
hmWanIoExtensionAdminStatus = _HmWanIoExtensionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 19),
    _HmWanIoExtensionAdminStatus_Type()
)
hmWanIoExtensionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanIoExtensionAdminStatus.setStatus("current")


class _HmWanXccntExtensionAdminStatus_Type(Integer32):
    """Custom type hmWanXccntExtensionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanXccntExtensionAdminStatus_Type.__name__ = "Integer32"
_HmWanXccntExtensionAdminStatus_Object = MibScalar
hmWanXccntExtensionAdminStatus = _HmWanXccntExtensionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 20),
    _HmWanXccntExtensionAdminStatus_Type()
)
hmWanXccntExtensionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanXccntExtensionAdminStatus.setStatus("current")


class _HmWanMbusExtensionAdminStatus_Type(Integer32):
    """Custom type hmWanMbusExtensionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanMbusExtensionAdminStatus_Type.__name__ = "Integer32"
_HmWanMbusExtensionAdminStatus_Object = MibScalar
hmWanMbusExtensionAdminStatus = _HmWanMbusExtensionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 21),
    _HmWanMbusExtensionAdminStatus_Type()
)
hmWanMbusExtensionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanMbusExtensionAdminStatus.setStatus("current")


class _HmWanMbusBaudrate_Type(Integer32):
    """Custom type hmWanMbusBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
    )


_HmWanMbusBaudrate_Type.__name__ = "Integer32"
_HmWanMbusBaudrate_Object = MibScalar
hmWanMbusBaudrate = _HmWanMbusBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 22),
    _HmWanMbusBaudrate_Type()
)
hmWanMbusBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanMbusBaudrate.setStatus("current")


class _HmWanMbusParity_Type(Integer32):
    """Custom type hmWanMbusParity based on Integer32"""
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
          ("even", 2),
          ("odd", 3))
    )


_HmWanMbusParity_Type.__name__ = "Integer32"
_HmWanMbusParity_Object = MibScalar
hmWanMbusParity = _HmWanMbusParity_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 23),
    _HmWanMbusParity_Type()
)
hmWanMbusParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanMbusParity.setStatus("current")


class _HmWanMbusStopbits_Type(Integer32):
    """Custom type hmWanMbusStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_HmWanMbusStopbits_Type.__name__ = "Integer32"
_HmWanMbusStopbits_Object = MibScalar
hmWanMbusStopbits = _HmWanMbusStopbits_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 24),
    _HmWanMbusStopbits_Type()
)
hmWanMbusStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanMbusStopbits.setStatus("current")


class _HmWanReportAdminStatus_Type(Integer32):
    """Custom type hmWanReportAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HmWanReportAdminStatus_Type.__name__ = "Integer32"
_HmWanReportAdminStatus_Object = MibScalar
hmWanReportAdminStatus = _HmWanReportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 25),
    _HmWanReportAdminStatus_Type()
)
hmWanReportAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanReportAdminStatus.setStatus("current")


class _HmWanReportIPAddress_Type(DisplayString):
    """Custom type hmWanReportIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmWanReportIPAddress_Type.__name__ = "DisplayString"
_HmWanReportIPAddress_Object = MibScalar
hmWanReportIPAddress = _HmWanReportIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 26),
    _HmWanReportIPAddress_Type()
)
hmWanReportIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanReportIPAddress.setStatus("current")


class _HmWanReportPeriod_Type(Integer32):
    """Custom type hmWanReportPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_HmWanReportPeriod_Type.__name__ = "Integer32"
_HmWanReportPeriod_Object = MibScalar
hmWanReportPeriod = _HmWanReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 8, 17, 27),
    _HmWanReportPeriod_Type()
)
hmWanReportPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWanReportPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hmWanReportPeriod.setUnits("min")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-WAN-CFG-MIB",
    **{"HmWanIfIndexTc": HmWanIfIndexTc,
       "HmWanLeaseDhcpIndexTc": HmWanLeaseDhcpIndexTc,
       "HmWanStaticDhcpIndexTc": HmWanStaticDhcpIndexTc,
       "hmWanCfgMib": hmWanCfgMib,
       "hmWanEth": hmWanEth,
       "hmWanIfNumber": hmWanIfNumber,
       "hmWanIfTable": hmWanIfTable,
       "hmWanIfEntry": hmWanIfEntry,
       "hmWanIfIndex": hmWanIfIndex,
       "hmWanIfDhcpClient": hmWanIfDhcpClient,
       "hmWanIfIpAddress": hmWanIfIpAddress,
       "hmWanIfSubnetMask": hmWanIfSubnetMask,
       "hmWanIfBridged": hmWanIfBridged,
       "hmWanIfMediaType": hmWanIfMediaType,
       "hmWanIfDefaultGateway": hmWanIfDefaultGateway,
       "hmWanIfDnsServer": hmWanIfDnsServer,
       "hmWanLeaseDhcpNumber": hmWanLeaseDhcpNumber,
       "hmWanLeaseDhcpTable": hmWanLeaseDhcpTable,
       "hmWanLeaseDhcpEntry": hmWanLeaseDhcpEntry,
       "hmWanLeaseDhcpIndex": hmWanLeaseDhcpIndex,
       "hmWanLeaseDhcpServer": hmWanLeaseDhcpServer,
       "hmWanLeaseDhcpIpPoolStart": hmWanLeaseDhcpIpPoolStart,
       "hmWanLeaseDhcpIpPoolEnd": hmWanLeaseDhcpIpPoolEnd,
       "hmWanLeaseDhcpTime": hmWanLeaseDhcpTime,
       "hmWanStaticDhcp": hmWanStaticDhcp,
       "hmWanStaticDhcpNumber": hmWanStaticDhcpNumber,
       "hmWanStaticDhcpTable": hmWanStaticDhcpTable,
       "hmWanStaticDhcpEntry": hmWanStaticDhcpEntry,
       "hmWanStaticDhcpIndex": hmWanStaticDhcpIndex,
       "hmWanStaticDhcpMacAddress": hmWanStaticDhcpMacAddress,
       "hmWanStaticDhcpIpAddress": hmWanStaticDhcpIpAddress,
       "hmWanSnmpCfg": hmWanSnmpCfg,
       "hmWanSnmpAdminStatus": hmWanSnmpAdminStatus,
       "hmWanSnmpSysName": hmWanSnmpSysName,
       "hmWanSnmpSysLocation": hmWanSnmpSysLocation,
       "hmWanSnmpSysContact": hmWanSnmpSysContact,
       "hmWanSnmpV1AccessAdminStatus": hmWanSnmpV1AccessAdminStatus,
       "hmWanSnmpV1ReadCommunity": hmWanSnmpV1ReadCommunity,
       "hmWanSnmpV1WriteCommunity": hmWanSnmpV1WriteCommunity,
       "hmWanSnmpV3AccessAdminStatus": hmWanSnmpV3AccessAdminStatus,
       "hmWanSnmpV33ReadUsername": hmWanSnmpV33ReadUsername,
       "hmWanSnmpV3ReadAuth": hmWanSnmpV3ReadAuth,
       "hmWanSnmpV3ReadAuthPwd": hmWanSnmpV3ReadAuthPwd,
       "hmWanSnmpV3ReadPrivProt": hmWanSnmpV3ReadPrivProt,
       "hmWanSnmpV3ReadPrivPwd": hmWanSnmpV3ReadPrivPwd,
       "hmWanSnmpV3WriteUsername": hmWanSnmpV3WriteUsername,
       "hmWanSnmpV3WriteAuth": hmWanSnmpV3WriteAuth,
       "hmWanSnmpV3WriteAuthPwd": hmWanSnmpV3WriteAuthPwd,
       "hmWanSnmpV3WritePrivProt": hmWanSnmpV3WritePrivProt,
       "hmWanSnmpV3WritePrivPwd": hmWanSnmpV3WritePrivPwd,
       "hmWanIoExtensionAdminStatus": hmWanIoExtensionAdminStatus,
       "hmWanXccntExtensionAdminStatus": hmWanXccntExtensionAdminStatus,
       "hmWanMbusExtensionAdminStatus": hmWanMbusExtensionAdminStatus,
       "hmWanMbusBaudrate": hmWanMbusBaudrate,
       "hmWanMbusParity": hmWanMbusParity,
       "hmWanMbusStopbits": hmWanMbusStopbits,
       "hmWanReportAdminStatus": hmWanReportAdminStatus,
       "hmWanReportIPAddress": hmWanReportIPAddress,
       "hmWanReportPeriod": hmWanReportPeriod}
)
