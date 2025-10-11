# SNMP MIB module (QTECH-IP-SET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IP-SET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:01 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechIPSetMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111)
)
if mibBuilder.loadTexts:
    qtechIPSetMgmt.setRevisions(
        ("2012-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechIPSetMIBObjects_ObjectIdentity = ObjectIdentity
qtechIPSetMIBObjects = _QtechIPSetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1)
)
_QtechIPSetipAddressTable_Object = MibTable
qtechIPSetipAddressTable = _QtechIPSetipAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIPSetipAddressTable.setStatus("current")
_QtechIPSetIpAddressEntry_Object = MibTableRow
qtechIPSetIpAddressEntry = _QtechIPSetIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1)
)
qtechIPSetIpAddressEntry.setIndexNames(
    (0, "QTECH-IP-SET-MIB", "qtechIPSetipAddressIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIPSetIpAddressEntry.setStatus("current")
_QtechIPSetipAddressIfIndex_Type = InterfaceIndex
_QtechIPSetipAddressIfIndex_Object = MibTableColumn
qtechIPSetipAddressIfIndex = _QtechIPSetipAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 1),
    _QtechIPSetipAddressIfIndex_Type()
)
qtechIPSetipAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSetipAddressIfIndex.setStatus("current")
_QtechIPSetipAddressAddr_Type = IpAddress
_QtechIPSetipAddressAddr_Object = MibTableColumn
qtechIPSetipAddressAddr = _QtechIPSetipAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 2),
    _QtechIPSetipAddressAddr_Type()
)
qtechIPSetipAddressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIPSetipAddressAddr.setStatus("current")
_QtechIPSetipAddressMask_Type = IpAddress
_QtechIPSetipAddressMask_Object = MibTableColumn
qtechIPSetipAddressMask = _QtechIPSetipAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 3),
    _QtechIPSetipAddressMask_Type()
)
qtechIPSetipAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIPSetipAddressMask.setStatus("current")


class _QtechIPSetipAddressStatus_Type(Integer32):
    """Custom type qtechIPSetipAddressStatus based on Integer32"""
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


_QtechIPSetipAddressStatus_Type.__name__ = "Integer32"
_QtechIPSetipAddressStatus_Object = MibTableColumn
qtechIPSetipAddressStatus = _QtechIPSetipAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 4),
    _QtechIPSetipAddressStatus_Type()
)
qtechIPSetipAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIPSetipAddressStatus.setStatus("current")


class _QtechIPSetipAddressType_Type(Integer32):
    """Custom type qtechIPSetipAddressType based on Integer32"""
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


_QtechIPSetipAddressType_Type.__name__ = "Integer32"
_QtechIPSetipAddressType_Object = MibTableColumn
qtechIPSetipAddressType = _QtechIPSetipAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 1, 1, 1, 5),
    _QtechIPSetipAddressType_Type()
)
qtechIPSetipAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIPSetipAddressType.setStatus("current")
_QtechIpSetMIBConformance_ObjectIdentity = ObjectIdentity
qtechIpSetMIBConformance = _QtechIpSetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2)
)
_QtechIpSetMIBCompliances_ObjectIdentity = ObjectIdentity
qtechIpSetMIBCompliances = _QtechIpSetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 1)
)
_QtechIpSetMIBGroups_ObjectIdentity = ObjectIdentity
qtechIpSetMIBGroups = _QtechIpSetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 2)
)

# Managed Objects groups

qtechIpSetMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 2, 1)
)
qtechIpSetMIBGroup.setObjects(
      *(("QTECH-IP-SET-MIB", "qtechIPSetipAddressIfIndex"),
        ("QTECH-IP-SET-MIB", "qtechIPSetipAddressAddr"),
        ("QTECH-IP-SET-MIB", "qtechIPSetipAddressMask"),
        ("QTECH-IP-SET-MIB", "qtechIPSetipAddressStatus"),
        ("QTECH-IP-SET-MIB", "qtechIPSetipAddressType"))
)
if mibBuilder.loadTexts:
    qtechIpSetMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechIcmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 111, 2, 1, 1)
)
qtechIcmpMIBCompliance.setObjects(
    ("QTECH-IP-SET-MIB", "qtechIpSetMIBGroup")
)
if mibBuilder.loadTexts:
    qtechIcmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IP-SET-MIB",
    **{"qtechIPSetMgmt": qtechIPSetMgmt,
       "qtechIPSetMIBObjects": qtechIPSetMIBObjects,
       "qtechIPSetipAddressTable": qtechIPSetipAddressTable,
       "qtechIPSetIpAddressEntry": qtechIPSetIpAddressEntry,
       "qtechIPSetipAddressIfIndex": qtechIPSetipAddressIfIndex,
       "qtechIPSetipAddressAddr": qtechIPSetipAddressAddr,
       "qtechIPSetipAddressMask": qtechIPSetipAddressMask,
       "qtechIPSetipAddressStatus": qtechIPSetipAddressStatus,
       "qtechIPSetipAddressType": qtechIPSetipAddressType,
       "qtechIpSetMIBConformance": qtechIpSetMIBConformance,
       "qtechIpSetMIBCompliances": qtechIpSetMIBCompliances,
       "qtechIcmpMIBCompliance": qtechIcmpMIBCompliance,
       "qtechIpSetMIBGroups": qtechIpSetMIBGroups,
       "qtechIpSetMIBGroup": qtechIpSetMIBGroup}
)
