# SNMP MIB module (DHCPv6-Server-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DHCPv6-Server-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:45 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swDHCPv6ServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 90)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDHCPv6ServerMIBObjects_ObjectIdentity = ObjectIdentity
swDHCPv6ServerMIBObjects = _SwDHCPv6ServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1)
)
_SwDHCPv6ServerStateCtrl_ObjectIdentity = ObjectIdentity
swDHCPv6ServerStateCtrl = _SwDHCPv6ServerStateCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 1)
)


class _SwDHCPv6ServerState_Type(Integer32):
    """Custom type swDHCPv6ServerState based on Integer32"""
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


_SwDHCPv6ServerState_Type.__name__ = "Integer32"
_SwDHCPv6ServerState_Object = MibScalar
swDHCPv6ServerState = _SwDHCPv6ServerState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 1, 1),
    _SwDHCPv6ServerState_Type()
)
swDHCPv6ServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerState.setStatus("current")
_SwDHCPv6ServerCtrlTable_Object = MibTable
swDHCPv6ServerCtrlTable = _SwDHCPv6ServerCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 1, 2)
)
if mibBuilder.loadTexts:
    swDHCPv6ServerCtrlTable.setStatus("current")
_SwDHCPv6ServerCtrlEntry_Object = MibTableRow
swDHCPv6ServerCtrlEntry = _SwDHCPv6ServerCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 1, 2, 1)
)
swDHCPv6ServerCtrlEntry.setIndexNames(
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerIfName"),
)
if mibBuilder.loadTexts:
    swDHCPv6ServerCtrlEntry.setStatus("current")


class _SwDHCPv6ServerIfName_Type(DisplayString):
    """Custom type swDHCPv6ServerIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwDHCPv6ServerIfName_Type.__name__ = "DisplayString"
_SwDHCPv6ServerIfName_Object = MibTableColumn
swDHCPv6ServerIfName = _SwDHCPv6ServerIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 1, 2, 1, 1),
    _SwDHCPv6ServerIfName_Type()
)
swDHCPv6ServerIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerIfName.setStatus("current")


class _SwDHCPv6ServerCtrlState_Type(Integer32):
    """Custom type swDHCPv6ServerCtrlState based on Integer32"""
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


_SwDHCPv6ServerCtrlState_Type.__name__ = "Integer32"
_SwDHCPv6ServerCtrlState_Object = MibTableColumn
swDHCPv6ServerCtrlState = _SwDHCPv6ServerCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 1, 2, 1, 2),
    _SwDHCPv6ServerCtrlState_Type()
)
swDHCPv6ServerCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerCtrlState.setStatus("current")
_SwDHCPv6ServerPoolMgmt_ObjectIdentity = ObjectIdentity
swDHCPv6ServerPoolMgmt = _SwDHCPv6ServerPoolMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2)
)
_SwDHCPv6ServerPoolTable_Object = MibTable
swDHCPv6ServerPoolTable = _SwDHCPv6ServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolTable.setStatus("current")
_SwDHCPv6ServerPoolEntry_Object = MibTableRow
swDHCPv6ServerPoolEntry = _SwDHCPv6ServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1)
)
swDHCPv6ServerPoolEntry.setIndexNames(
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerPoolName"),
)
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolEntry.setStatus("current")


class _SwDHCPv6ServerPoolName_Type(DisplayString):
    """Custom type swDHCPv6ServerPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwDHCPv6ServerPoolName_Type.__name__ = "DisplayString"
_SwDHCPv6ServerPoolName_Object = MibTableColumn
swDHCPv6ServerPoolName = _SwDHCPv6ServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 1),
    _SwDHCPv6ServerPoolName_Type()
)
swDHCPv6ServerPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolName.setStatus("current")
_SwDHCPv6ServerPoolBeginAddress_Type = Ipv6Address
_SwDHCPv6ServerPoolBeginAddress_Object = MibTableColumn
swDHCPv6ServerPoolBeginAddress = _SwDHCPv6ServerPoolBeginAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 2),
    _SwDHCPv6ServerPoolBeginAddress_Type()
)
swDHCPv6ServerPoolBeginAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolBeginAddress.setStatus("current")
_SwDHCPv6ServerPoolEndAddress_Type = Ipv6Address
_SwDHCPv6ServerPoolEndAddress_Object = MibTableColumn
swDHCPv6ServerPoolEndAddress = _SwDHCPv6ServerPoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 3),
    _SwDHCPv6ServerPoolEndAddress_Type()
)
swDHCPv6ServerPoolEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolEndAddress.setStatus("current")
_SwDHCPv6ServerPoolAddressPrefixLen_Type = Integer32
_SwDHCPv6ServerPoolAddressPrefixLen_Object = MibTableColumn
swDHCPv6ServerPoolAddressPrefixLen = _SwDHCPv6ServerPoolAddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 4),
    _SwDHCPv6ServerPoolAddressPrefixLen_Type()
)
swDHCPv6ServerPoolAddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolAddressPrefixLen.setStatus("current")


class _SwDHCPv6ServerPoolDomainName_Type(DisplayString):
    """Custom type swDHCPv6ServerPoolDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDHCPv6ServerPoolDomainName_Type.__name__ = "DisplayString"
_SwDHCPv6ServerPoolDomainName_Object = MibTableColumn
swDHCPv6ServerPoolDomainName = _SwDHCPv6ServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 5),
    _SwDHCPv6ServerPoolDomainName_Type()
)
swDHCPv6ServerPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolDomainName.setStatus("current")


class _SwDHCPv6ServerPoolPreferredLifetime_Type(Unsigned32):
    """Custom type swDHCPv6ServerPoolPreferredLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_SwDHCPv6ServerPoolPreferredLifetime_Type.__name__ = "Unsigned32"
_SwDHCPv6ServerPoolPreferredLifetime_Object = MibTableColumn
swDHCPv6ServerPoolPreferredLifetime = _SwDHCPv6ServerPoolPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 6),
    _SwDHCPv6ServerPoolPreferredLifetime_Type()
)
swDHCPv6ServerPoolPreferredLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolPreferredLifetime.setStatus("current")


class _SwDHCPv6ServerPoolValidLifetime_Type(Unsigned32):
    """Custom type swDHCPv6ServerPoolValidLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_SwDHCPv6ServerPoolValidLifetime_Type.__name__ = "Unsigned32"
_SwDHCPv6ServerPoolValidLifetime_Object = MibTableColumn
swDHCPv6ServerPoolValidLifetime = _SwDHCPv6ServerPoolValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 7),
    _SwDHCPv6ServerPoolValidLifetime_Type()
)
swDHCPv6ServerPoolValidLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolValidLifetime.setStatus("current")
_SwDHCPv6ServerPoolRowStatus_Type = RowStatus
_SwDHCPv6ServerPoolRowStatus_Object = MibTableColumn
swDHCPv6ServerPoolRowStatus = _SwDHCPv6ServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 1, 1, 100),
    _SwDHCPv6ServerPoolRowStatus_Type()
)
swDHCPv6ServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPv6ServerPoolRowStatus.setStatus("current")
_SwDHCPv6ServerDNSServerAddressTable_Object = MibTable
swDHCPv6ServerDNSServerAddressTable = _SwDHCPv6ServerDNSServerAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 2)
)
if mibBuilder.loadTexts:
    swDHCPv6ServerDNSServerAddressTable.setStatus("current")
_SwDHCPv6ServerDNSServerAddressEntry_Object = MibTableRow
swDHCPv6ServerDNSServerAddressEntry = _SwDHCPv6ServerDNSServerAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 2, 1)
)
swDHCPv6ServerDNSServerAddressEntry.setIndexNames(
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerPoolName"),
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerDNSServerAddressIndex"),
)
if mibBuilder.loadTexts:
    swDHCPv6ServerDNSServerAddressEntry.setStatus("current")
_SwDHCPv6ServerDNSServerAddressIndex_Type = Integer32
_SwDHCPv6ServerDNSServerAddressIndex_Object = MibTableColumn
swDHCPv6ServerDNSServerAddressIndex = _SwDHCPv6ServerDNSServerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 2, 1, 1),
    _SwDHCPv6ServerDNSServerAddressIndex_Type()
)
swDHCPv6ServerDNSServerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerDNSServerAddressIndex.setStatus("current")
_SwDHCPv6ServerDNSServerAddress_Type = Ipv6Address
_SwDHCPv6ServerDNSServerAddress_Object = MibTableColumn
swDHCPv6ServerDNSServerAddress = _SwDHCPv6ServerDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 2, 1, 2),
    _SwDHCPv6ServerDNSServerAddress_Type()
)
swDHCPv6ServerDNSServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerDNSServerAddress.setStatus("current")
_SwDHCPv6ServerDNSServerAddressRowStatus_Type = RowStatus
_SwDHCPv6ServerDNSServerAddressRowStatus_Object = MibTableColumn
swDHCPv6ServerDNSServerAddressRowStatus = _SwDHCPv6ServerDNSServerAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 2, 2, 1, 100),
    _SwDHCPv6ServerDNSServerAddressRowStatus_Type()
)
swDHCPv6ServerDNSServerAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPv6ServerDNSServerAddressRowStatus.setStatus("current")
_SwDHCPv6ServerManualBindingTable_Object = MibTable
swDHCPv6ServerManualBindingTable = _SwDHCPv6ServerManualBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 3)
)
if mibBuilder.loadTexts:
    swDHCPv6ServerManualBindingTable.setStatus("current")
_SwDHCPv6ServerManualBindingEntry_Object = MibTableRow
swDHCPv6ServerManualBindingEntry = _SwDHCPv6ServerManualBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 3, 1)
)
swDHCPv6ServerManualBindingEntry.setIndexNames(
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerPoolName"),
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerManualBindingIpv6Address"),
)
if mibBuilder.loadTexts:
    swDHCPv6ServerManualBindingEntry.setStatus("current")
_SwDHCPv6ServerManualBindingIpv6Address_Type = Ipv6Address
_SwDHCPv6ServerManualBindingIpv6Address_Object = MibTableColumn
swDHCPv6ServerManualBindingIpv6Address = _SwDHCPv6ServerManualBindingIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 3, 1, 1),
    _SwDHCPv6ServerManualBindingIpv6Address_Type()
)
swDHCPv6ServerManualBindingIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerManualBindingIpv6Address.setStatus("current")


class _SwDHCPv6ServerManualBindingDUID_Type(DisplayString):
    """Custom type swDHCPv6ServerManualBindingDUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_SwDHCPv6ServerManualBindingDUID_Type.__name__ = "DisplayString"
_SwDHCPv6ServerManualBindingDUID_Object = MibTableColumn
swDHCPv6ServerManualBindingDUID = _SwDHCPv6ServerManualBindingDUID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 3, 1, 2),
    _SwDHCPv6ServerManualBindingDUID_Type()
)
swDHCPv6ServerManualBindingDUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPv6ServerManualBindingDUID.setStatus("current")
_SwDHCPv6ServerManualBindingRowStatus_Type = RowStatus
_SwDHCPv6ServerManualBindingRowStatus_Object = MibTableColumn
swDHCPv6ServerManualBindingRowStatus = _SwDHCPv6ServerManualBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 3, 1, 100),
    _SwDHCPv6ServerManualBindingRowStatus_Type()
)
swDHCPv6ServerManualBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPv6ServerManualBindingRowStatus.setStatus("current")
_SwDHCPv6ServerExcludedAddressTable_Object = MibTable
swDHCPv6ServerExcludedAddressTable = _SwDHCPv6ServerExcludedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 4)
)
if mibBuilder.loadTexts:
    swDHCPv6ServerExcludedAddressTable.setStatus("current")
_SwDHCPv6ServerExcludedAddressEntry_Object = MibTableRow
swDHCPv6ServerExcludedAddressEntry = _SwDHCPv6ServerExcludedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 4, 1)
)
swDHCPv6ServerExcludedAddressEntry.setIndexNames(
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerPoolName"),
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerExcludedAddressBegin"),
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerExcludedAddressEnd"),
)
if mibBuilder.loadTexts:
    swDHCPv6ServerExcludedAddressEntry.setStatus("current")
_SwDHCPv6ServerExcludedAddressBegin_Type = Ipv6Address
_SwDHCPv6ServerExcludedAddressBegin_Object = MibTableColumn
swDHCPv6ServerExcludedAddressBegin = _SwDHCPv6ServerExcludedAddressBegin_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 4, 1, 1),
    _SwDHCPv6ServerExcludedAddressBegin_Type()
)
swDHCPv6ServerExcludedAddressBegin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerExcludedAddressBegin.setStatus("current")
_SwDHCPv6ServerExcludedAddressEnd_Type = Ipv6Address
_SwDHCPv6ServerExcludedAddressEnd_Object = MibTableColumn
swDHCPv6ServerExcludedAddressEnd = _SwDHCPv6ServerExcludedAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 4, 1, 2),
    _SwDHCPv6ServerExcludedAddressEnd_Type()
)
swDHCPv6ServerExcludedAddressEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerExcludedAddressEnd.setStatus("current")
_SwDHCPv6ServerExcludedAddressRowStatus_Type = RowStatus
_SwDHCPv6ServerExcludedAddressRowStatus_Object = MibTableColumn
swDHCPv6ServerExcludedAddressRowStatus = _SwDHCPv6ServerExcludedAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 4, 1, 100),
    _SwDHCPv6ServerExcludedAddressRowStatus_Type()
)
swDHCPv6ServerExcludedAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPv6ServerExcludedAddressRowStatus.setStatus("current")
_SwDHCPv6ServerBindingTable_Object = MibTable
swDHCPv6ServerBindingTable = _SwDHCPv6ServerBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5)
)
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingTable.setStatus("current")
_SwDHCPv6ServerBindingEntry_Object = MibTableRow
swDHCPv6ServerBindingEntry = _SwDHCPv6ServerBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5, 1)
)
swDHCPv6ServerBindingEntry.setIndexNames(
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerPoolName"),
    (0, "DHCPv6-Server-MIB", "swDHCPv6ServerBindingIpv6Address"),
)
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingEntry.setStatus("current")
_SwDHCPv6ServerBindingIpv6Address_Type = Ipv6Address
_SwDHCPv6ServerBindingIpv6Address_Object = MibTableColumn
swDHCPv6ServerBindingIpv6Address = _SwDHCPv6ServerBindingIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5, 1, 1),
    _SwDHCPv6ServerBindingIpv6Address_Type()
)
swDHCPv6ServerBindingIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingIpv6Address.setStatus("current")


class _SwDHCPv6ServerBindingDUID_Type(DisplayString):
    """Custom type swDHCPv6ServerBindingDUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_SwDHCPv6ServerBindingDUID_Type.__name__ = "DisplayString"
_SwDHCPv6ServerBindingDUID_Object = MibTableColumn
swDHCPv6ServerBindingDUID = _SwDHCPv6ServerBindingDUID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5, 1, 2),
    _SwDHCPv6ServerBindingDUID_Type()
)
swDHCPv6ServerBindingDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingDUID.setStatus("current")


class _SwDHCPv6ServerBindingPreferredLifetime_Type(Unsigned32):
    """Custom type swDHCPv6ServerBindingPreferredLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_SwDHCPv6ServerBindingPreferredLifetime_Type.__name__ = "Unsigned32"
_SwDHCPv6ServerBindingPreferredLifetime_Object = MibTableColumn
swDHCPv6ServerBindingPreferredLifetime = _SwDHCPv6ServerBindingPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5, 1, 3),
    _SwDHCPv6ServerBindingPreferredLifetime_Type()
)
swDHCPv6ServerBindingPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingPreferredLifetime.setStatus("current")


class _SwDHCPv6ServerBindingValidLifetime_Type(Unsigned32):
    """Custom type swDHCPv6ServerBindingValidLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_SwDHCPv6ServerBindingValidLifetime_Type.__name__ = "Unsigned32"
_SwDHCPv6ServerBindingValidLifetime_Object = MibTableColumn
swDHCPv6ServerBindingValidLifetime = _SwDHCPv6ServerBindingValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5, 1, 4),
    _SwDHCPv6ServerBindingValidLifetime_Type()
)
swDHCPv6ServerBindingValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingValidLifetime.setStatus("current")


class _SwDHCPv6ServerBindingClearState_Type(Integer32):
    """Custom type swDHCPv6ServerBindingClearState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwDHCPv6ServerBindingClearState_Type.__name__ = "Integer32"
_SwDHCPv6ServerBindingClearState_Object = MibTableColumn
swDHCPv6ServerBindingClearState = _SwDHCPv6ServerBindingClearState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 90, 1, 5, 1, 5),
    _SwDHCPv6ServerBindingClearState_Type()
)
swDHCPv6ServerBindingClearState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6ServerBindingClearState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCPv6-Server-MIB",
    **{"swDHCPv6ServerMIB": swDHCPv6ServerMIB,
       "swDHCPv6ServerMIBObjects": swDHCPv6ServerMIBObjects,
       "swDHCPv6ServerStateCtrl": swDHCPv6ServerStateCtrl,
       "swDHCPv6ServerState": swDHCPv6ServerState,
       "swDHCPv6ServerCtrlTable": swDHCPv6ServerCtrlTable,
       "swDHCPv6ServerCtrlEntry": swDHCPv6ServerCtrlEntry,
       "swDHCPv6ServerIfName": swDHCPv6ServerIfName,
       "swDHCPv6ServerCtrlState": swDHCPv6ServerCtrlState,
       "swDHCPv6ServerPoolMgmt": swDHCPv6ServerPoolMgmt,
       "swDHCPv6ServerPoolTable": swDHCPv6ServerPoolTable,
       "swDHCPv6ServerPoolEntry": swDHCPv6ServerPoolEntry,
       "swDHCPv6ServerPoolName": swDHCPv6ServerPoolName,
       "swDHCPv6ServerPoolBeginAddress": swDHCPv6ServerPoolBeginAddress,
       "swDHCPv6ServerPoolEndAddress": swDHCPv6ServerPoolEndAddress,
       "swDHCPv6ServerPoolAddressPrefixLen": swDHCPv6ServerPoolAddressPrefixLen,
       "swDHCPv6ServerPoolDomainName": swDHCPv6ServerPoolDomainName,
       "swDHCPv6ServerPoolPreferredLifetime": swDHCPv6ServerPoolPreferredLifetime,
       "swDHCPv6ServerPoolValidLifetime": swDHCPv6ServerPoolValidLifetime,
       "swDHCPv6ServerPoolRowStatus": swDHCPv6ServerPoolRowStatus,
       "swDHCPv6ServerDNSServerAddressTable": swDHCPv6ServerDNSServerAddressTable,
       "swDHCPv6ServerDNSServerAddressEntry": swDHCPv6ServerDNSServerAddressEntry,
       "swDHCPv6ServerDNSServerAddressIndex": swDHCPv6ServerDNSServerAddressIndex,
       "swDHCPv6ServerDNSServerAddress": swDHCPv6ServerDNSServerAddress,
       "swDHCPv6ServerDNSServerAddressRowStatus": swDHCPv6ServerDNSServerAddressRowStatus,
       "swDHCPv6ServerManualBindingTable": swDHCPv6ServerManualBindingTable,
       "swDHCPv6ServerManualBindingEntry": swDHCPv6ServerManualBindingEntry,
       "swDHCPv6ServerManualBindingIpv6Address": swDHCPv6ServerManualBindingIpv6Address,
       "swDHCPv6ServerManualBindingDUID": swDHCPv6ServerManualBindingDUID,
       "swDHCPv6ServerManualBindingRowStatus": swDHCPv6ServerManualBindingRowStatus,
       "swDHCPv6ServerExcludedAddressTable": swDHCPv6ServerExcludedAddressTable,
       "swDHCPv6ServerExcludedAddressEntry": swDHCPv6ServerExcludedAddressEntry,
       "swDHCPv6ServerExcludedAddressBegin": swDHCPv6ServerExcludedAddressBegin,
       "swDHCPv6ServerExcludedAddressEnd": swDHCPv6ServerExcludedAddressEnd,
       "swDHCPv6ServerExcludedAddressRowStatus": swDHCPv6ServerExcludedAddressRowStatus,
       "swDHCPv6ServerBindingTable": swDHCPv6ServerBindingTable,
       "swDHCPv6ServerBindingEntry": swDHCPv6ServerBindingEntry,
       "swDHCPv6ServerBindingIpv6Address": swDHCPv6ServerBindingIpv6Address,
       "swDHCPv6ServerBindingDUID": swDHCPv6ServerBindingDUID,
       "swDHCPv6ServerBindingPreferredLifetime": swDHCPv6ServerBindingPreferredLifetime,
       "swDHCPv6ServerBindingValidLifetime": swDHCPv6ServerBindingValidLifetime,
       "swDHCPv6ServerBindingClearState": swDHCPv6ServerBindingClearState}
)
