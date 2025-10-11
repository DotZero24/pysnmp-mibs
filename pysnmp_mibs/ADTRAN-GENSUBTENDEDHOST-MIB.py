# SNMP MIB module (ADTRAN-GENSUBTENDEDHOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENSUBTENDEDHOST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:15 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenSubtendedHost,
 adGenSubtendedHostID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenSubtendedHost",
    "adGenSubtendedHostID")

(AdGenTrapVersion,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "AdGenTrapVersion")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenSubtendedHostMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 12, 1)
)
if mibBuilder.loadTexts:
    adGenSubtendedHostMIB.setRevisions(
        ("2015-08-21 00:00",
         "2015-05-27 00:00",
         "2015-03-06 00:00",
         "2014-05-16 00:00",
         "2009-03-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenSubtendedHostProvisioning_ObjectIdentity = ObjectIdentity
adGenSubtendedHostProvisioning = _AdGenSubtendedHostProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1)
)
_AdGenSubHostProvMgmtTable_Object = MibTable
adGenSubHostProvMgmtTable = _AdGenSubHostProvMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtTable.setStatus("current")
_AdGenSubHostProvMgmtEntry_Object = MibTableRow
adGenSubHostProvMgmtEntry = _AdGenSubHostProvMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1)
)
adGenSubHostProvMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtEntry.setStatus("current")
_AdGenSubHostProvMgmtIpAddress_Type = IpAddress
_AdGenSubHostProvMgmtIpAddress_Object = MibTableColumn
adGenSubHostProvMgmtIpAddress = _AdGenSubHostProvMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 1),
    _AdGenSubHostProvMgmtIpAddress_Type()
)
adGenSubHostProvMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpAddress.setStatus("current")
_AdGenSubHostProvMgmtIpSubnetMask_Type = IpAddress
_AdGenSubHostProvMgmtIpSubnetMask_Object = MibTableColumn
adGenSubHostProvMgmtIpSubnetMask = _AdGenSubHostProvMgmtIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 2),
    _AdGenSubHostProvMgmtIpSubnetMask_Type()
)
adGenSubHostProvMgmtIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpSubnetMask.setStatus("current")
_AdGenSubHostProvMgmtIpGateway_Type = IpAddress
_AdGenSubHostProvMgmtIpGateway_Object = MibTableColumn
adGenSubHostProvMgmtIpGateway = _AdGenSubHostProvMgmtIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 3),
    _AdGenSubHostProvMgmtIpGateway_Type()
)
adGenSubHostProvMgmtIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpGateway.setStatus("current")
_AdGenSubHostProvMgmtIpVlan_Type = Integer32
_AdGenSubHostProvMgmtIpVlan_Object = MibTableColumn
adGenSubHostProvMgmtIpVlan = _AdGenSubHostProvMgmtIpVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 4),
    _AdGenSubHostProvMgmtIpVlan_Type()
)
adGenSubHostProvMgmtIpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpVlan.setStatus("current")
_AdGenSubHostProvMgmtTftpServer_Type = IpAddress
_AdGenSubHostProvMgmtTftpServer_Object = MibTableColumn
adGenSubHostProvMgmtTftpServer = _AdGenSubHostProvMgmtTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 5),
    _AdGenSubHostProvMgmtTftpServer_Type()
)
adGenSubHostProvMgmtTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtTftpServer.setStatus("current")
_AdGenSubHostProvMgmtSnmpWriteCommunity_Type = DisplayString
_AdGenSubHostProvMgmtSnmpWriteCommunity_Object = MibTableColumn
adGenSubHostProvMgmtSnmpWriteCommunity = _AdGenSubHostProvMgmtSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 6),
    _AdGenSubHostProvMgmtSnmpWriteCommunity_Type()
)
adGenSubHostProvMgmtSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtSnmpWriteCommunity.setStatus("current")
_AdGenSubHostProvMgmtSnmpReadCommunity_Type = DisplayString
_AdGenSubHostProvMgmtSnmpReadCommunity_Object = MibTableColumn
adGenSubHostProvMgmtSnmpReadCommunity = _AdGenSubHostProvMgmtSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 7),
    _AdGenSubHostProvMgmtSnmpReadCommunity_Type()
)
adGenSubHostProvMgmtSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtSnmpReadCommunity.setStatus("current")
_AdGenSubHostProvMgmtSysName_Type = DisplayString
_AdGenSubHostProvMgmtSysName_Object = MibTableColumn
adGenSubHostProvMgmtSysName = _AdGenSubHostProvMgmtSysName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 8),
    _AdGenSubHostProvMgmtSysName_Type()
)
adGenSubHostProvMgmtSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtSysName.setStatus("current")
_AdGenSubHostProvMgmtPriority_Type = Integer32
_AdGenSubHostProvMgmtPriority_Object = MibTableColumn
adGenSubHostProvMgmtPriority = _AdGenSubHostProvMgmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 9),
    _AdGenSubHostProvMgmtPriority_Type()
)
adGenSubHostProvMgmtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtPriority.setStatus("current")


class _AdGenSubHostProvMgmtIpAssignMode_Type(Integer32):
    """Custom type adGenSubHostProvMgmtIpAssignMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_AdGenSubHostProvMgmtIpAssignMode_Type.__name__ = "Integer32"
_AdGenSubHostProvMgmtIpAssignMode_Object = MibTableColumn
adGenSubHostProvMgmtIpAssignMode = _AdGenSubHostProvMgmtIpAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 10),
    _AdGenSubHostProvMgmtIpAssignMode_Type()
)
adGenSubHostProvMgmtIpAssignMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpAssignMode.setStatus("current")


class _AdGenSubHostProvMgmtSync_Type(Integer32):
    """Custom type adGenSubHostProvMgmtSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resync", 1),
          ("reset", 2))
    )


_AdGenSubHostProvMgmtSync_Type.__name__ = "Integer32"
_AdGenSubHostProvMgmtSync_Object = MibTableColumn
adGenSubHostProvMgmtSync = _AdGenSubHostProvMgmtSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 11),
    _AdGenSubHostProvMgmtSync_Type()
)
adGenSubHostProvMgmtSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtSync.setStatus("current")
_AdGenSubHostProvMgmtSnmpSysLocation_Type = DisplayString
_AdGenSubHostProvMgmtSnmpSysLocation_Object = MibTableColumn
adGenSubHostProvMgmtSnmpSysLocation = _AdGenSubHostProvMgmtSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 12),
    _AdGenSubHostProvMgmtSnmpSysLocation_Type()
)
adGenSubHostProvMgmtSnmpSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtSnmpSysLocation.setStatus("current")
_AdGenSubHostProvMgmtEzProvHostOneIpAddress_Type = IpAddress
_AdGenSubHostProvMgmtEzProvHostOneIpAddress_Object = MibTableColumn
adGenSubHostProvMgmtEzProvHostOneIpAddress = _AdGenSubHostProvMgmtEzProvHostOneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 13),
    _AdGenSubHostProvMgmtEzProvHostOneIpAddress_Type()
)
adGenSubHostProvMgmtEzProvHostOneIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtEzProvHostOneIpAddress.setStatus("current")
_AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Type = AdGenTrapVersion
_AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Object = MibTableColumn
adGenSubHostProvMgmtEzProvHostOneTrapVersion = _AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 14),
    _AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Type()
)
adGenSubHostProvMgmtEzProvHostOneTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtEzProvHostOneTrapVersion.setStatus("current")
_AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Type = IpAddress
_AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Object = MibTableColumn
adGenSubHostProvMgmtEzProvHostTwoIpAddress = _AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 15),
    _AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Type()
)
adGenSubHostProvMgmtEzProvHostTwoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtEzProvHostTwoIpAddress.setStatus("current")
_AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Type = AdGenTrapVersion
_AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Object = MibTableColumn
adGenSubHostProvMgmtEzProvHostTwoTrapVersion = _AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 16),
    _AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Type()
)
adGenSubHostProvMgmtEzProvHostTwoTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtEzProvHostTwoTrapVersion.setStatus("current")
_AdGenSubHostProvMgmtEzProvEnabled_Type = TruthValue
_AdGenSubHostProvMgmtEzProvEnabled_Object = MibTableColumn
adGenSubHostProvMgmtEzProvEnabled = _AdGenSubHostProvMgmtEzProvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 17),
    _AdGenSubHostProvMgmtEzProvEnabled_Type()
)
adGenSubHostProvMgmtEzProvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtEzProvEnabled.setStatus("current")
_AdGenSubHostProvMgmtIpv6AddressPrefixLength_Type = InetAddressPrefixLength
_AdGenSubHostProvMgmtIpv6AddressPrefixLength_Object = MibTableColumn
adGenSubHostProvMgmtIpv6AddressPrefixLength = _AdGenSubHostProvMgmtIpv6AddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 18),
    _AdGenSubHostProvMgmtIpv6AddressPrefixLength_Type()
)
adGenSubHostProvMgmtIpv6AddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpv6AddressPrefixLength.setStatus("current")
_AdGenSubHostProvMgmtIpv6AddressEui64_Type = TruthValue
_AdGenSubHostProvMgmtIpv6AddressEui64_Object = MibTableColumn
adGenSubHostProvMgmtIpv6AddressEui64 = _AdGenSubHostProvMgmtIpv6AddressEui64_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 19),
    _AdGenSubHostProvMgmtIpv6AddressEui64_Type()
)
adGenSubHostProvMgmtIpv6AddressEui64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpv6AddressEui64.setStatus("current")
_AdGenSubHostProvMgmtIpv6Address_Type = InetAddressIPv6
_AdGenSubHostProvMgmtIpv6Address_Object = MibTableColumn
adGenSubHostProvMgmtIpv6Address = _AdGenSubHostProvMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 20),
    _AdGenSubHostProvMgmtIpv6Address_Type()
)
adGenSubHostProvMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpv6Address.setStatus("current")
_AdGenSubHostProvMgmtIpv6AddressLinkLocal_Type = InetAddressIPv6
_AdGenSubHostProvMgmtIpv6AddressLinkLocal_Object = MibTableColumn
adGenSubHostProvMgmtIpv6AddressLinkLocal = _AdGenSubHostProvMgmtIpv6AddressLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 21),
    _AdGenSubHostProvMgmtIpv6AddressLinkLocal_Type()
)
adGenSubHostProvMgmtIpv6AddressLinkLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtIpv6AddressLinkLocal.setStatus("current")


class _AdGenSubHostProvMgmtAutoConfigMode_Type(TruthValue):
    """Custom type adGenSubHostProvMgmtAutoConfigMode based on TruthValue"""
    defaultValue = 2


_AdGenSubHostProvMgmtAutoConfigMode_Type.__name__ = "TruthValue"
_AdGenSubHostProvMgmtAutoConfigMode_Object = MibTableColumn
adGenSubHostProvMgmtAutoConfigMode = _AdGenSubHostProvMgmtAutoConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 22),
    _AdGenSubHostProvMgmtAutoConfigMode_Type()
)
adGenSubHostProvMgmtAutoConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtAutoConfigMode.setStatus("current")


class _AdGenSubHostProvMgmtAutoConfigFilename_Type(DisplayString):
    """Custom type adGenSubHostProvMgmtAutoConfigFilename based on DisplayString"""
    defaultValue = OctetString("")


_AdGenSubHostProvMgmtAutoConfigFilename_Type.__name__ = "DisplayString"
_AdGenSubHostProvMgmtAutoConfigFilename_Object = MibTableColumn
adGenSubHostProvMgmtAutoConfigFilename = _AdGenSubHostProvMgmtAutoConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 23),
    _AdGenSubHostProvMgmtAutoConfigFilename_Type()
)
adGenSubHostProvMgmtAutoConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtAutoConfigFilename.setStatus("current")


class _AdGenSubHostProvMgmtAutoConfigGroupName_Type(DisplayString):
    """Custom type adGenSubHostProvMgmtAutoConfigGroupName based on DisplayString"""
    defaultValue = OctetString("")


_AdGenSubHostProvMgmtAutoConfigGroupName_Type.__name__ = "DisplayString"
_AdGenSubHostProvMgmtAutoConfigGroupName_Object = MibTableColumn
adGenSubHostProvMgmtAutoConfigGroupName = _AdGenSubHostProvMgmtAutoConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 24),
    _AdGenSubHostProvMgmtAutoConfigGroupName_Type()
)
adGenSubHostProvMgmtAutoConfigGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtAutoConfigGroupName.setStatus("current")
_AdGenSubHostProvMgmtAutoConfigHostIpv4_Type = InetAddressIPv4
_AdGenSubHostProvMgmtAutoConfigHostIpv4_Object = MibTableColumn
adGenSubHostProvMgmtAutoConfigHostIpv4 = _AdGenSubHostProvMgmtAutoConfigHostIpv4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 25),
    _AdGenSubHostProvMgmtAutoConfigHostIpv4_Type()
)
adGenSubHostProvMgmtAutoConfigHostIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtAutoConfigHostIpv4.setStatus("current")
_AdGenSubHostProvMgmtAutoConfigHostIpv6_Type = InetAddressIPv6
_AdGenSubHostProvMgmtAutoConfigHostIpv6_Object = MibTableColumn
adGenSubHostProvMgmtAutoConfigHostIpv6 = _AdGenSubHostProvMgmtAutoConfigHostIpv6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 26),
    _AdGenSubHostProvMgmtAutoConfigHostIpv6_Type()
)
adGenSubHostProvMgmtAutoConfigHostIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtAutoConfigHostIpv6.setStatus("current")


class _AdGenSubHostProvMgmtLastErrorString_Type(DisplayString):
    """Custom type adGenSubHostProvMgmtLastErrorString based on DisplayString"""
    defaultValue = OctetString("")


_AdGenSubHostProvMgmtLastErrorString_Type.__name__ = "DisplayString"
_AdGenSubHostProvMgmtLastErrorString_Object = MibTableColumn
adGenSubHostProvMgmtLastErrorString = _AdGenSubHostProvMgmtLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 1, 1, 27),
    _AdGenSubHostProvMgmtLastErrorString_Type()
)
adGenSubHostProvMgmtLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostProvMgmtLastErrorString.setStatus("current")
_AdGenSubHostProvIfTable_Object = MibTable
adGenSubHostProvIfTable = _AdGenSubHostProvIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 2)
)
if mibBuilder.loadTexts:
    adGenSubHostProvIfTable.setStatus("current")
_AdGenSubHostProvIfEntry_Object = MibTableRow
adGenSubHostProvIfEntry = _AdGenSubHostProvIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 2, 1)
)
adGenSubHostProvIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenSubHostProvIfEntry.setStatus("current")


class _AdGenSubHostProvIfMode_Type(Integer32):
    """Custom type adGenSubHostProvIfMode based on Integer32"""
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
          ("listener", 2),
          ("sender", 3))
    )


_AdGenSubHostProvIfMode_Type.__name__ = "Integer32"
_AdGenSubHostProvIfMode_Object = MibTableColumn
adGenSubHostProvIfMode = _AdGenSubHostProvIfMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 2, 1, 1),
    _AdGenSubHostProvIfMode_Type()
)
adGenSubHostProvIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvIfMode.setStatus("current")


class _AdGenSubHostProvIfAutoDiscoveryMode_Type(TruthValue):
    """Custom type adGenSubHostProvIfAutoDiscoveryMode based on TruthValue"""
    defaultValue = 2


_AdGenSubHostProvIfAutoDiscoveryMode_Type.__name__ = "TruthValue"
_AdGenSubHostProvIfAutoDiscoveryMode_Object = MibTableColumn
adGenSubHostProvIfAutoDiscoveryMode = _AdGenSubHostProvIfAutoDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 2, 1, 2),
    _AdGenSubHostProvIfAutoDiscoveryMode_Type()
)
adGenSubHostProvIfAutoDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvIfAutoDiscoveryMode.setStatus("current")


class _AdGenSubHostProvIfAutoDiscoveryAck_Type(TruthValue):
    """Custom type adGenSubHostProvIfAutoDiscoveryAck based on TruthValue"""
    defaultValue = 2


_AdGenSubHostProvIfAutoDiscoveryAck_Type.__name__ = "TruthValue"
_AdGenSubHostProvIfAutoDiscoveryAck_Object = MibTableColumn
adGenSubHostProvIfAutoDiscoveryAck = _AdGenSubHostProvIfAutoDiscoveryAck_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 1, 2, 1, 3),
    _AdGenSubHostProvIfAutoDiscoveryAck_Type()
)
adGenSubHostProvIfAutoDiscoveryAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSubHostProvIfAutoDiscoveryAck.setStatus("current")
_AdGenSubtendedHostStatus_ObjectIdentity = ObjectIdentity
adGenSubtendedHostStatus = _AdGenSubtendedHostStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2)
)
_AdGenSubHostStatTable_Object = MibTable
adGenSubHostStatTable = _AdGenSubHostStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1)
)
if mibBuilder.loadTexts:
    adGenSubHostStatTable.setStatus("current")
_AdGenSubHostStatEntry_Object = MibTableRow
adGenSubHostStatEntry = _AdGenSubHostStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1)
)
adGenSubHostStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenSubHostStatEntry.setStatus("current")
_AdGenSubHostStatMacAddress_Type = MacAddress
_AdGenSubHostStatMacAddress_Object = MibTableColumn
adGenSubHostStatMacAddress = _AdGenSubHostStatMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 1),
    _AdGenSubHostStatMacAddress_Type()
)
adGenSubHostStatMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatMacAddress.setStatus("current")
_AdGenSubHostStatIpAddress_Type = IpAddress
_AdGenSubHostStatIpAddress_Object = MibTableColumn
adGenSubHostStatIpAddress = _AdGenSubHostStatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 2),
    _AdGenSubHostStatIpAddress_Type()
)
adGenSubHostStatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatIpAddress.setStatus("current")
_AdGenSubHostStatGateway_Type = IpAddress
_AdGenSubHostStatGateway_Object = MibTableColumn
adGenSubHostStatGateway = _AdGenSubHostStatGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 3),
    _AdGenSubHostStatGateway_Type()
)
adGenSubHostStatGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatGateway.setStatus("current")
_AdGenSubHostStatProvSync_Type = DisplayString
_AdGenSubHostStatProvSync_Object = MibTableColumn
adGenSubHostStatProvSync = _AdGenSubHostStatProvSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 4),
    _AdGenSubHostStatProvSync_Type()
)
adGenSubHostStatProvSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatProvSync.setStatus("current")
_AdGenSubHostStatIpSubnetMask_Type = IpAddress
_AdGenSubHostStatIpSubnetMask_Object = MibTableColumn
adGenSubHostStatIpSubnetMask = _AdGenSubHostStatIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 5),
    _AdGenSubHostStatIpSubnetMask_Type()
)
adGenSubHostStatIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatIpSubnetMask.setStatus("current")
_AdGenSubHostStatIpv6AddressPrefixLength_Type = InetAddressPrefixLength
_AdGenSubHostStatIpv6AddressPrefixLength_Object = MibTableColumn
adGenSubHostStatIpv6AddressPrefixLength = _AdGenSubHostStatIpv6AddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 6),
    _AdGenSubHostStatIpv6AddressPrefixLength_Type()
)
adGenSubHostStatIpv6AddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatIpv6AddressPrefixLength.setStatus("current")
_AdGenSubHostStatIpv6AddressEui64_Type = TruthValue
_AdGenSubHostStatIpv6AddressEui64_Object = MibTableColumn
adGenSubHostStatIpv6AddressEui64 = _AdGenSubHostStatIpv6AddressEui64_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 7),
    _AdGenSubHostStatIpv6AddressEui64_Type()
)
adGenSubHostStatIpv6AddressEui64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatIpv6AddressEui64.setStatus("current")
_AdGenSubHostStatIpv6Address_Type = InetAddressIPv6
_AdGenSubHostStatIpv6Address_Object = MibTableColumn
adGenSubHostStatIpv6Address = _AdGenSubHostStatIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 8),
    _AdGenSubHostStatIpv6Address_Type()
)
adGenSubHostStatIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatIpv6Address.setStatus("current")
_AdGenSubHostStatIpv6AddressLinkLocal_Type = InetAddressIPv6
_AdGenSubHostStatIpv6AddressLinkLocal_Object = MibTableColumn
adGenSubHostStatIpv6AddressLinkLocal = _AdGenSubHostStatIpv6AddressLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 9),
    _AdGenSubHostStatIpv6AddressLinkLocal_Type()
)
adGenSubHostStatIpv6AddressLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatIpv6AddressLinkLocal.setStatus("current")
_AdGenSubHostStatAutoConfigMode_Type = TruthValue
_AdGenSubHostStatAutoConfigMode_Object = MibTableColumn
adGenSubHostStatAutoConfigMode = _AdGenSubHostStatAutoConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 10),
    _AdGenSubHostStatAutoConfigMode_Type()
)
adGenSubHostStatAutoConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatAutoConfigMode.setStatus("current")
_AdGenSubHostStatAutoConfigFilename_Type = DisplayString
_AdGenSubHostStatAutoConfigFilename_Object = MibTableColumn
adGenSubHostStatAutoConfigFilename = _AdGenSubHostStatAutoConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 11),
    _AdGenSubHostStatAutoConfigFilename_Type()
)
adGenSubHostStatAutoConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatAutoConfigFilename.setStatus("current")
_AdGenSubHostStatAutoConfigGroupName_Type = DisplayString
_AdGenSubHostStatAutoConfigGroupName_Object = MibTableColumn
adGenSubHostStatAutoConfigGroupName = _AdGenSubHostStatAutoConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 12),
    _AdGenSubHostStatAutoConfigGroupName_Type()
)
adGenSubHostStatAutoConfigGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatAutoConfigGroupName.setStatus("current")
_AdGenSubHostStatAutoConfigHostIpv4_Type = InetAddressIPv4
_AdGenSubHostStatAutoConfigHostIpv4_Object = MibTableColumn
adGenSubHostStatAutoConfigHostIpv4 = _AdGenSubHostStatAutoConfigHostIpv4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 13),
    _AdGenSubHostStatAutoConfigHostIpv4_Type()
)
adGenSubHostStatAutoConfigHostIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatAutoConfigHostIpv4.setStatus("current")
_AdGenSubHostStatAutoConfigHostIpv6_Type = InetAddressIPv6
_AdGenSubHostStatAutoConfigHostIpv6_Object = MibTableColumn
adGenSubHostStatAutoConfigHostIpv6 = _AdGenSubHostStatAutoConfigHostIpv6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 1, 1, 14),
    _AdGenSubHostStatAutoConfigHostIpv6_Type()
)
adGenSubHostStatAutoConfigHostIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatAutoConfigHostIpv6.setStatus("current")
_AdGenSubHostStatFarEndTable_Object = MibTable
adGenSubHostStatFarEndTable = _AdGenSubHostStatFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 2)
)
if mibBuilder.loadTexts:
    adGenSubHostStatFarEndTable.setStatus("current")
_AdGenSubHostStatFarEndEntry_Object = MibTableRow
adGenSubHostStatFarEndEntry = _AdGenSubHostStatFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 2, 1)
)
adGenSubHostStatFarEndEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenSubHostStatFarEndEntry.setStatus("current")
_AdGenSubHostStatFarEndIfIndex_Type = InterfaceIndex
_AdGenSubHostStatFarEndIfIndex_Object = MibTableColumn
adGenSubHostStatFarEndIfIndex = _AdGenSubHostStatFarEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 2, 1, 1),
    _AdGenSubHostStatFarEndIfIndex_Type()
)
adGenSubHostStatFarEndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatFarEndIfIndex.setStatus("current")
_AdGenSubHostStatFarEndIpAddress_Type = IpAddress
_AdGenSubHostStatFarEndIpAddress_Object = MibTableColumn
adGenSubHostStatFarEndIpAddress = _AdGenSubHostStatFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 2, 1, 2),
    _AdGenSubHostStatFarEndIpAddress_Type()
)
adGenSubHostStatFarEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatFarEndIpAddress.setStatus("current")
_AdGenSubHostStatFarEndSysName_Type = DisplayString
_AdGenSubHostStatFarEndSysName_Object = MibTableColumn
adGenSubHostStatFarEndSysName = _AdGenSubHostStatFarEndSysName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 2, 2, 1, 3),
    _AdGenSubHostStatFarEndSysName_Type()
)
adGenSubHostStatFarEndSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubHostStatFarEndSysName.setStatus("current")
_AdGenSubtendedHostNotificationsPrefix_ObjectIdentity = ObjectIdentity
adGenSubtendedHostNotificationsPrefix = _AdGenSubtendedHostNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 3)
)
_AdGenSubtendedHostNotifications_ObjectIdentity = ObjectIdentity
adGenSubtendedHostNotifications = _AdGenSubtendedHostNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 3, 0)
)

# Managed Objects groups


# Notification objects

adGenSubHostProvIfAutoDiscoveryAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 12, 3, 0, 1)
)
adGenSubHostProvIfAutoDiscoveryAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenSubHostProvIfAutoDiscoveryAlm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENSUBTENDEDHOST-MIB",
    **{"adGenSubtendedHostProvisioning": adGenSubtendedHostProvisioning,
       "adGenSubHostProvMgmtTable": adGenSubHostProvMgmtTable,
       "adGenSubHostProvMgmtEntry": adGenSubHostProvMgmtEntry,
       "adGenSubHostProvMgmtIpAddress": adGenSubHostProvMgmtIpAddress,
       "adGenSubHostProvMgmtIpSubnetMask": adGenSubHostProvMgmtIpSubnetMask,
       "adGenSubHostProvMgmtIpGateway": adGenSubHostProvMgmtIpGateway,
       "adGenSubHostProvMgmtIpVlan": adGenSubHostProvMgmtIpVlan,
       "adGenSubHostProvMgmtTftpServer": adGenSubHostProvMgmtTftpServer,
       "adGenSubHostProvMgmtSnmpWriteCommunity": adGenSubHostProvMgmtSnmpWriteCommunity,
       "adGenSubHostProvMgmtSnmpReadCommunity": adGenSubHostProvMgmtSnmpReadCommunity,
       "adGenSubHostProvMgmtSysName": adGenSubHostProvMgmtSysName,
       "adGenSubHostProvMgmtPriority": adGenSubHostProvMgmtPriority,
       "adGenSubHostProvMgmtIpAssignMode": adGenSubHostProvMgmtIpAssignMode,
       "adGenSubHostProvMgmtSync": adGenSubHostProvMgmtSync,
       "adGenSubHostProvMgmtSnmpSysLocation": adGenSubHostProvMgmtSnmpSysLocation,
       "adGenSubHostProvMgmtEzProvHostOneIpAddress": adGenSubHostProvMgmtEzProvHostOneIpAddress,
       "adGenSubHostProvMgmtEzProvHostOneTrapVersion": adGenSubHostProvMgmtEzProvHostOneTrapVersion,
       "adGenSubHostProvMgmtEzProvHostTwoIpAddress": adGenSubHostProvMgmtEzProvHostTwoIpAddress,
       "adGenSubHostProvMgmtEzProvHostTwoTrapVersion": adGenSubHostProvMgmtEzProvHostTwoTrapVersion,
       "adGenSubHostProvMgmtEzProvEnabled": adGenSubHostProvMgmtEzProvEnabled,
       "adGenSubHostProvMgmtIpv6AddressPrefixLength": adGenSubHostProvMgmtIpv6AddressPrefixLength,
       "adGenSubHostProvMgmtIpv6AddressEui64": adGenSubHostProvMgmtIpv6AddressEui64,
       "adGenSubHostProvMgmtIpv6Address": adGenSubHostProvMgmtIpv6Address,
       "adGenSubHostProvMgmtIpv6AddressLinkLocal": adGenSubHostProvMgmtIpv6AddressLinkLocal,
       "adGenSubHostProvMgmtAutoConfigMode": adGenSubHostProvMgmtAutoConfigMode,
       "adGenSubHostProvMgmtAutoConfigFilename": adGenSubHostProvMgmtAutoConfigFilename,
       "adGenSubHostProvMgmtAutoConfigGroupName": adGenSubHostProvMgmtAutoConfigGroupName,
       "adGenSubHostProvMgmtAutoConfigHostIpv4": adGenSubHostProvMgmtAutoConfigHostIpv4,
       "adGenSubHostProvMgmtAutoConfigHostIpv6": adGenSubHostProvMgmtAutoConfigHostIpv6,
       "adGenSubHostProvMgmtLastErrorString": adGenSubHostProvMgmtLastErrorString,
       "adGenSubHostProvIfTable": adGenSubHostProvIfTable,
       "adGenSubHostProvIfEntry": adGenSubHostProvIfEntry,
       "adGenSubHostProvIfMode": adGenSubHostProvIfMode,
       "adGenSubHostProvIfAutoDiscoveryMode": adGenSubHostProvIfAutoDiscoveryMode,
       "adGenSubHostProvIfAutoDiscoveryAck": adGenSubHostProvIfAutoDiscoveryAck,
       "adGenSubtendedHostStatus": adGenSubtendedHostStatus,
       "adGenSubHostStatTable": adGenSubHostStatTable,
       "adGenSubHostStatEntry": adGenSubHostStatEntry,
       "adGenSubHostStatMacAddress": adGenSubHostStatMacAddress,
       "adGenSubHostStatIpAddress": adGenSubHostStatIpAddress,
       "adGenSubHostStatGateway": adGenSubHostStatGateway,
       "adGenSubHostStatProvSync": adGenSubHostStatProvSync,
       "adGenSubHostStatIpSubnetMask": adGenSubHostStatIpSubnetMask,
       "adGenSubHostStatIpv6AddressPrefixLength": adGenSubHostStatIpv6AddressPrefixLength,
       "adGenSubHostStatIpv6AddressEui64": adGenSubHostStatIpv6AddressEui64,
       "adGenSubHostStatIpv6Address": adGenSubHostStatIpv6Address,
       "adGenSubHostStatIpv6AddressLinkLocal": adGenSubHostStatIpv6AddressLinkLocal,
       "adGenSubHostStatAutoConfigMode": adGenSubHostStatAutoConfigMode,
       "adGenSubHostStatAutoConfigFilename": adGenSubHostStatAutoConfigFilename,
       "adGenSubHostStatAutoConfigGroupName": adGenSubHostStatAutoConfigGroupName,
       "adGenSubHostStatAutoConfigHostIpv4": adGenSubHostStatAutoConfigHostIpv4,
       "adGenSubHostStatAutoConfigHostIpv6": adGenSubHostStatAutoConfigHostIpv6,
       "adGenSubHostStatFarEndTable": adGenSubHostStatFarEndTable,
       "adGenSubHostStatFarEndEntry": adGenSubHostStatFarEndEntry,
       "adGenSubHostStatFarEndIfIndex": adGenSubHostStatFarEndIfIndex,
       "adGenSubHostStatFarEndIpAddress": adGenSubHostStatFarEndIpAddress,
       "adGenSubHostStatFarEndSysName": adGenSubHostStatFarEndSysName,
       "adGenSubtendedHostNotificationsPrefix": adGenSubtendedHostNotificationsPrefix,
       "adGenSubtendedHostNotifications": adGenSubtendedHostNotifications,
       "adGenSubHostProvIfAutoDiscoveryAlm": adGenSubHostProvIfAutoDiscoveryAlm,
       "adGenSubtendedHostMIB": adGenSubtendedHostMIB}
)
