# SNMP MIB module (HPN-ICF-IPV6-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-IPV6-ADDRESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:51 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hpnicfIpv6AddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71)
)
if mibBuilder.loadTexts:
    hpnicfIpv6AddrMIB.setRevisions(
        ("2006-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfIpv6AddressObjects_ObjectIdentity = ObjectIdentity
hpnicfIpv6AddressObjects = _HpnicfIpv6AddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1)
)
_HpnicfIpv6AddressConfig_ObjectIdentity = ObjectIdentity
hpnicfIpv6AddressConfig = _HpnicfIpv6AddressConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1)
)
_HpnicfIpv6AddrSetTable_Object = MibTable
hpnicfIpv6AddrSetTable = _HpnicfIpv6AddrSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetTable.setStatus("current")
_HpnicfIpv6AddrSetEntry_Object = MibTableRow
hpnicfIpv6AddrSetEntry = _HpnicfIpv6AddrSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1)
)
hpnicfIpv6AddrSetEntry.setIndexNames(
    (0, "HPN-ICF-IPV6-ADDRESS-MIB", "hpnicfIpv6AddrSetIfIndex"),
    (0, "HPN-ICF-IPV6-ADDRESS-MIB", "hpnicfIpv6AddrSetAddrType"),
    (0, "HPN-ICF-IPV6-ADDRESS-MIB", "hpnicfIpv6AddrSetAddr"),
)
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetEntry.setStatus("current")


class _HpnicfIpv6AddrSetIfIndex_Type(Integer32):
    """Custom type hpnicfIpv6AddrSetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpv6AddrSetIfIndex_Type.__name__ = "Integer32"
_HpnicfIpv6AddrSetIfIndex_Object = MibTableColumn
hpnicfIpv6AddrSetIfIndex = _HpnicfIpv6AddrSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1, 1),
    _HpnicfIpv6AddrSetIfIndex_Type()
)
hpnicfIpv6AddrSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetIfIndex.setStatus("current")
_HpnicfIpv6AddrSetAddrType_Type = InetAddressType
_HpnicfIpv6AddrSetAddrType_Object = MibTableColumn
hpnicfIpv6AddrSetAddrType = _HpnicfIpv6AddrSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1, 2),
    _HpnicfIpv6AddrSetAddrType_Type()
)
hpnicfIpv6AddrSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetAddrType.setStatus("current")
_HpnicfIpv6AddrSetAddr_Type = InetAddress
_HpnicfIpv6AddrSetAddr_Object = MibTableColumn
hpnicfIpv6AddrSetAddr = _HpnicfIpv6AddrSetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1, 3),
    _HpnicfIpv6AddrSetAddr_Type()
)
hpnicfIpv6AddrSetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetAddr.setStatus("current")


class _HpnicfIpv6AddrSetPfxLength_Type(Integer32):
    """Custom type hpnicfIpv6AddrSetPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HpnicfIpv6AddrSetPfxLength_Type.__name__ = "Integer32"
_HpnicfIpv6AddrSetPfxLength_Object = MibTableColumn
hpnicfIpv6AddrSetPfxLength = _HpnicfIpv6AddrSetPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1, 4),
    _HpnicfIpv6AddrSetPfxLength_Type()
)
hpnicfIpv6AddrSetPfxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetPfxLength.setStatus("current")


class _HpnicfIpv6AddrSetSourceType_Type(Integer32):
    """Custom type hpnicfIpv6AddrSetSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assignedIp", 1),
          ("assignedEUI64Ip", 2),
          ("assignedLinklocalIp", 3))
    )


_HpnicfIpv6AddrSetSourceType_Type.__name__ = "Integer32"
_HpnicfIpv6AddrSetSourceType_Object = MibTableColumn
hpnicfIpv6AddrSetSourceType = _HpnicfIpv6AddrSetSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1, 5),
    _HpnicfIpv6AddrSetSourceType_Type()
)
hpnicfIpv6AddrSetSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetSourceType.setStatus("current")
_HpnicfIpv6AddrSetRowStatus_Type = RowStatus
_HpnicfIpv6AddrSetRowStatus_Object = MibTableColumn
hpnicfIpv6AddrSetRowStatus = _HpnicfIpv6AddrSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 1, 1, 6),
    _HpnicfIpv6AddrSetRowStatus_Type()
)
hpnicfIpv6AddrSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrSetRowStatus.setStatus("current")
_HpnicfIpv6AddrReadTable_Object = MibTable
hpnicfIpv6AddrReadTable = _HpnicfIpv6AddrReadTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadTable.setStatus("current")
_HpnicfIpv6AddrReadEntry_Object = MibTableRow
hpnicfIpv6AddrReadEntry = _HpnicfIpv6AddrReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1)
)
hpnicfIpv6AddrReadEntry.setIndexNames(
    (0, "HPN-ICF-IPV6-ADDRESS-MIB", "hpnicfIpv6AddrReadIfIndex"),
    (0, "HPN-ICF-IPV6-ADDRESS-MIB", "hpnicfIpv6AddrReadAddrType"),
    (0, "HPN-ICF-IPV6-ADDRESS-MIB", "hpnicfIpv6AddrReadAddr"),
)
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadEntry.setStatus("current")


class _HpnicfIpv6AddrReadIfIndex_Type(Integer32):
    """Custom type hpnicfIpv6AddrReadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpv6AddrReadIfIndex_Type.__name__ = "Integer32"
_HpnicfIpv6AddrReadIfIndex_Object = MibTableColumn
hpnicfIpv6AddrReadIfIndex = _HpnicfIpv6AddrReadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1, 1),
    _HpnicfIpv6AddrReadIfIndex_Type()
)
hpnicfIpv6AddrReadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadIfIndex.setStatus("current")
_HpnicfIpv6AddrReadAddrType_Type = InetAddressType
_HpnicfIpv6AddrReadAddrType_Object = MibTableColumn
hpnicfIpv6AddrReadAddrType = _HpnicfIpv6AddrReadAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1, 2),
    _HpnicfIpv6AddrReadAddrType_Type()
)
hpnicfIpv6AddrReadAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadAddrType.setStatus("current")
_HpnicfIpv6AddrReadAddr_Type = InetAddress
_HpnicfIpv6AddrReadAddr_Object = MibTableColumn
hpnicfIpv6AddrReadAddr = _HpnicfIpv6AddrReadAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1, 3),
    _HpnicfIpv6AddrReadAddr_Type()
)
hpnicfIpv6AddrReadAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadAddr.setStatus("current")


class _HpnicfIpv6AddrReadPfxLength_Type(Integer32):
    """Custom type hpnicfIpv6AddrReadPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HpnicfIpv6AddrReadPfxLength_Type.__name__ = "Integer32"
_HpnicfIpv6AddrReadPfxLength_Object = MibTableColumn
hpnicfIpv6AddrReadPfxLength = _HpnicfIpv6AddrReadPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1, 4),
    _HpnicfIpv6AddrReadPfxLength_Type()
)
hpnicfIpv6AddrReadPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadPfxLength.setStatus("current")


class _HpnicfIpv6AddrReadSourceType_Type(Integer32):
    """Custom type hpnicfIpv6AddrReadSourceType based on Integer32"""
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
        *(("assignedIp", 1),
          ("assignedEUI64Ip", 2),
          ("assignedAutoIp", 3),
          ("autoIp", 4),
          ("dhcpv6", 5),
          ("negotiate", 6),
          ("cluster", 7))
    )


_HpnicfIpv6AddrReadSourceType_Type.__name__ = "Integer32"
_HpnicfIpv6AddrReadSourceType_Object = MibTableColumn
hpnicfIpv6AddrReadSourceType = _HpnicfIpv6AddrReadSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1, 5),
    _HpnicfIpv6AddrReadSourceType_Type()
)
hpnicfIpv6AddrReadSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadSourceType.setStatus("current")


class _HpnicfIpv6AddrReadCatalog_Type(Integer32):
    """Custom type hpnicfIpv6AddrReadCatalog based on Integer32"""
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
        *(("nodelocal", 1),
          ("linklocal", 2),
          ("sitelocal", 3),
          ("orglocal", 4),
          ("global", 5))
    )


_HpnicfIpv6AddrReadCatalog_Type.__name__ = "Integer32"
_HpnicfIpv6AddrReadCatalog_Object = MibTableColumn
hpnicfIpv6AddrReadCatalog = _HpnicfIpv6AddrReadCatalog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71, 1, 1, 2, 1, 6),
    _HpnicfIpv6AddrReadCatalog_Type()
)
hpnicfIpv6AddrReadCatalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpv6AddrReadCatalog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IPV6-ADDRESS-MIB",
    **{"hpnicfIpv6AddrMIB": hpnicfIpv6AddrMIB,
       "hpnicfIpv6AddressObjects": hpnicfIpv6AddressObjects,
       "hpnicfIpv6AddressConfig": hpnicfIpv6AddressConfig,
       "hpnicfIpv6AddrSetTable": hpnicfIpv6AddrSetTable,
       "hpnicfIpv6AddrSetEntry": hpnicfIpv6AddrSetEntry,
       "hpnicfIpv6AddrSetIfIndex": hpnicfIpv6AddrSetIfIndex,
       "hpnicfIpv6AddrSetAddrType": hpnicfIpv6AddrSetAddrType,
       "hpnicfIpv6AddrSetAddr": hpnicfIpv6AddrSetAddr,
       "hpnicfIpv6AddrSetPfxLength": hpnicfIpv6AddrSetPfxLength,
       "hpnicfIpv6AddrSetSourceType": hpnicfIpv6AddrSetSourceType,
       "hpnicfIpv6AddrSetRowStatus": hpnicfIpv6AddrSetRowStatus,
       "hpnicfIpv6AddrReadTable": hpnicfIpv6AddrReadTable,
       "hpnicfIpv6AddrReadEntry": hpnicfIpv6AddrReadEntry,
       "hpnicfIpv6AddrReadIfIndex": hpnicfIpv6AddrReadIfIndex,
       "hpnicfIpv6AddrReadAddrType": hpnicfIpv6AddrReadAddrType,
       "hpnicfIpv6AddrReadAddr": hpnicfIpv6AddrReadAddr,
       "hpnicfIpv6AddrReadPfxLength": hpnicfIpv6AddrReadPfxLength,
       "hpnicfIpv6AddrReadSourceType": hpnicfIpv6AddrReadSourceType,
       "hpnicfIpv6AddrReadCatalog": hpnicfIpv6AddrReadCatalog}
)
