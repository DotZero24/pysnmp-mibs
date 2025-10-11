# SNMP MIB module (FS-IP-SET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IP-SET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:13 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsIPSetMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111)
)
if mibBuilder.loadTexts:
    fsIPSetMgmt.setRevisions(
        ("2012-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIPSetMIBObjects_ObjectIdentity = ObjectIdentity
fsIPSetMIBObjects = _FsIPSetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1)
)
_FsIPSetipAddressTable_Object = MibTable
fsIPSetipAddressTable = _FsIPSetipAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1)
)
if mibBuilder.loadTexts:
    fsIPSetipAddressTable.setStatus("current")
_FsIPSetIpAddressEntry_Object = MibTableRow
fsIPSetIpAddressEntry = _FsIPSetIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1)
)
fsIPSetIpAddressEntry.setIndexNames(
    (0, "FS-IP-SET-MIB", "fsIPSetipAddressIfIndex"),
)
if mibBuilder.loadTexts:
    fsIPSetIpAddressEntry.setStatus("current")
_FsIPSetipAddressIfIndex_Type = InterfaceIndex
_FsIPSetipAddressIfIndex_Object = MibTableColumn
fsIPSetipAddressIfIndex = _FsIPSetipAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 1),
    _FsIPSetipAddressIfIndex_Type()
)
fsIPSetipAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSetipAddressIfIndex.setStatus("current")
_FsIPSetipAddressAddr_Type = IpAddress
_FsIPSetipAddressAddr_Object = MibTableColumn
fsIPSetipAddressAddr = _FsIPSetipAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 2),
    _FsIPSetipAddressAddr_Type()
)
fsIPSetipAddressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIPSetipAddressAddr.setStatus("current")
_FsIPSetipAddressMask_Type = IpAddress
_FsIPSetipAddressMask_Object = MibTableColumn
fsIPSetipAddressMask = _FsIPSetipAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 3),
    _FsIPSetipAddressMask_Type()
)
fsIPSetipAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIPSetipAddressMask.setStatus("current")


class _FsIPSetipAddressStatus_Type(Integer32):
    """Custom type fsIPSetipAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1))
    )


_FsIPSetipAddressStatus_Type.__name__ = "Integer32"
_FsIPSetipAddressStatus_Object = MibTableColumn
fsIPSetipAddressStatus = _FsIPSetipAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 4),
    _FsIPSetipAddressStatus_Type()
)
fsIPSetipAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPSetipAddressStatus.setStatus("current")


class _FsIPSetipAddressType_Type(Integer32):
    """Custom type fsIPSetipAddressType based on Integer32"""
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
        *(("unicast", 1),
          ("anycast", 2),
          ("broadcast", 3))
    )


_FsIPSetipAddressType_Type.__name__ = "Integer32"
_FsIPSetipAddressType_Object = MibTableColumn
fsIPSetipAddressType = _FsIPSetipAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 1, 1, 1, 5),
    _FsIPSetipAddressType_Type()
)
fsIPSetipAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPSetipAddressType.setStatus("current")
_FsIpSetMIBConformance_ObjectIdentity = ObjectIdentity
fsIpSetMIBConformance = _FsIpSetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2)
)
_FsIpSetMIBCompliances_ObjectIdentity = ObjectIdentity
fsIpSetMIBCompliances = _FsIpSetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 1)
)
_FsIpSetMIBGroups_ObjectIdentity = ObjectIdentity
fsIpSetMIBGroups = _FsIpSetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 2)
)

# Managed Objects groups

fsIpSetMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 2, 1)
)
fsIpSetMIBGroup.setObjects(
      *(("FS-IP-SET-MIB", "fsIPSetipAddressIfIndex"),
        ("FS-IP-SET-MIB", "fsIPSetipAddressAddr"),
        ("FS-IP-SET-MIB", "fsIPSetipAddressMask"),
        ("FS-IP-SET-MIB", "fsIPSetipAddressStatus"),
        ("FS-IP-SET-MIB", "fsIPSetipAddressType"))
)
if mibBuilder.loadTexts:
    fsIpSetMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsIcmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 111, 2, 1, 1)
)
fsIcmpMIBCompliance.setObjects(
    ("FS-IP-SET-MIB", "fsIpSetMIBGroup")
)
if mibBuilder.loadTexts:
    fsIcmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IP-SET-MIB",
    **{"fsIPSetMgmt": fsIPSetMgmt,
       "fsIPSetMIBObjects": fsIPSetMIBObjects,
       "fsIPSetipAddressTable": fsIPSetipAddressTable,
       "fsIPSetIpAddressEntry": fsIPSetIpAddressEntry,
       "fsIPSetipAddressIfIndex": fsIPSetipAddressIfIndex,
       "fsIPSetipAddressAddr": fsIPSetipAddressAddr,
       "fsIPSetipAddressMask": fsIPSetipAddressMask,
       "fsIPSetipAddressStatus": fsIPSetipAddressStatus,
       "fsIPSetipAddressType": fsIPSetipAddressType,
       "fsIpSetMIBConformance": fsIpSetMIBConformance,
       "fsIpSetMIBCompliances": fsIpSetMIBCompliances,
       "fsIcmpMIBCompliance": fsIcmpMIBCompliance,
       "fsIpSetMIBGroups": fsIpSetMIBGroups,
       "fsIpSetMIBGroup": fsIpSetMIBGroup}
)
