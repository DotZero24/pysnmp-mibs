# SNMP MIB module (QTECH-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:55 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    qtechArpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechArpMIBObjects_ObjectIdentity = ObjectIdentity
qtechArpMIBObjects = _QtechArpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1)
)
_QtechArpTable_Object = MibTable
qtechArpTable = _QtechArpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qtechArpTable.setStatus("current")
_QtechArpEntry_Object = MibTableRow
qtechArpEntry = _QtechArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1)
)
qtechArpEntry.setIndexNames(
    (0, "QTECH-ARP-MIB", "qtechArpIfIndex"),
    (0, "QTECH-ARP-MIB", "qtechArpNetAddress"),
)
if mibBuilder.loadTexts:
    qtechArpEntry.setStatus("current")
_QtechArpIfIndex_Type = IfIndex
_QtechArpIfIndex_Object = MibTableColumn
qtechArpIfIndex = _QtechArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 1),
    _QtechArpIfIndex_Type()
)
qtechArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpIfIndex.setStatus("current")
_QtechArpPhysAddress_Type = PhysAddress
_QtechArpPhysAddress_Object = MibTableColumn
qtechArpPhysAddress = _QtechArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 2),
    _QtechArpPhysAddress_Type()
)
qtechArpPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechArpPhysAddress.setStatus("current")
_QtechArpNetAddress_Type = IpAddress
_QtechArpNetAddress_Object = MibTableColumn
qtechArpNetAddress = _QtechArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 3),
    _QtechArpNetAddress_Type()
)
qtechArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpNetAddress.setStatus("current")
_QtechArpRemainAge_Type = Integer32
_QtechArpRemainAge_Object = MibTableColumn
qtechArpRemainAge = _QtechArpRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 4),
    _QtechArpRemainAge_Type()
)
qtechArpRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpRemainAge.setStatus("current")


class _QtechArpType_Type(Integer32):
    """Custom type qtechArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("arpa", 1)
    )


_QtechArpType_Type.__name__ = "Integer32"
_QtechArpType_Object = MibTableColumn
qtechArpType = _QtechArpType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 5),
    _QtechArpType_Type()
)
qtechArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechArpType.setStatus("current")


class _QtechArpEntryType_Type(Integer32):
    """Custom type qtechArpEntryType based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("interface", 3),
          ("vrrp", 4),
          ("trusted", 5))
    )


_QtechArpEntryType_Type.__name__ = "Integer32"
_QtechArpEntryType_Object = MibTableColumn
qtechArpEntryType = _QtechArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 6),
    _QtechArpEntryType_Type()
)
qtechArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpEntryType.setStatus("current")
_QtechArpStatus_Type = RowStatus
_QtechArpStatus_Object = MibTableColumn
qtechArpStatus = _QtechArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 1, 1, 7),
    _QtechArpStatus_Type()
)
qtechArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechArpStatus.setStatus("current")
_QtechArpIfTable_Object = MibTable
qtechArpIfTable = _QtechArpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    qtechArpIfTable.setStatus("current")
_QtechArpIfEntry_Object = MibTableRow
qtechArpIfEntry = _QtechArpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 2, 1)
)
qtechArpIfEntry.setIndexNames(
    (0, "QTECH-ARP-MIB", "qtechArpIfIfIndex"),
)
if mibBuilder.loadTexts:
    qtechArpIfEntry.setStatus("current")
_QtechArpIfIfIndex_Type = IfIndex
_QtechArpIfIfIndex_Object = MibTableColumn
qtechArpIfIfIndex = _QtechArpIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 2, 1, 1),
    _QtechArpIfIfIndex_Type()
)
qtechArpIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpIfIfIndex.setStatus("current")


class _QtechArpIfCacheTimeOut_Type(Integer32):
    """Custom type qtechArpIfCacheTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 18000),
    )


_QtechArpIfCacheTimeOut_Type.__name__ = "Integer32"
_QtechArpIfCacheTimeOut_Object = MibTableColumn
qtechArpIfCacheTimeOut = _QtechArpIfCacheTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 2, 1, 2),
    _QtechArpIfCacheTimeOut_Type()
)
qtechArpIfCacheTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechArpIfCacheTimeOut.setStatus("current")
_QtechArpCurrentTotalNumber_Type = Counter32
_QtechArpCurrentTotalNumber_Object = MibScalar
qtechArpCurrentTotalNumber = _QtechArpCurrentTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 3),
    _QtechArpCurrentTotalNumber_Type()
)
qtechArpCurrentTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpCurrentTotalNumber.setStatus("current")
_QtechArpCurrentUnresolveNumber_Type = Counter32
_QtechArpCurrentUnresolveNumber_Object = MibScalar
qtechArpCurrentUnresolveNumber = _QtechArpCurrentUnresolveNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 1, 4),
    _QtechArpCurrentUnresolveNumber_Type()
)
qtechArpCurrentUnresolveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpCurrentUnresolveNumber.setStatus("current")
_QtechArpMIBConformance_ObjectIdentity = ObjectIdentity
qtechArpMIBConformance = _QtechArpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 2)
)
_QtechArpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechArpMIBCompliances = _QtechArpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 2, 1)
)
_QtechArpMIBGroups_ObjectIdentity = ObjectIdentity
qtechArpMIBGroups = _QtechArpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 2, 2)
)

# Managed Objects groups

qtechArpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 2, 2, 1)
)
qtechArpMIBGroup.setObjects(
      *(("QTECH-ARP-MIB", "qtechArpIfIndex"),
        ("QTECH-ARP-MIB", "qtechArpPhysAddress"),
        ("QTECH-ARP-MIB", "qtechArpNetAddress"),
        ("QTECH-ARP-MIB", "qtechArpRemainAge"),
        ("QTECH-ARP-MIB", "qtechArpType"),
        ("QTECH-ARP-MIB", "qtechArpEntryType"),
        ("QTECH-ARP-MIB", "qtechArpStatus"),
        ("QTECH-ARP-MIB", "qtechArpIfIfIndex"),
        ("QTECH-ARP-MIB", "qtechArpIfCacheTimeOut"),
        ("QTECH-ARP-MIB", "qtechArpCurrentTotalNumber"),
        ("QTECH-ARP-MIB", "qtechArpCurrentUnresolveNumber"))
)
if mibBuilder.loadTexts:
    qtechArpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechArpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 2, 2, 1, 1)
)
qtechArpMIBCompliance.setObjects(
    ("QTECH-ARP-MIB", "qtechArpMIBGroup")
)
if mibBuilder.loadTexts:
    qtechArpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ARP-MIB",
    **{"qtechArpMIB": qtechArpMIB,
       "qtechArpMIBObjects": qtechArpMIBObjects,
       "qtechArpTable": qtechArpTable,
       "qtechArpEntry": qtechArpEntry,
       "qtechArpIfIndex": qtechArpIfIndex,
       "qtechArpPhysAddress": qtechArpPhysAddress,
       "qtechArpNetAddress": qtechArpNetAddress,
       "qtechArpRemainAge": qtechArpRemainAge,
       "qtechArpType": qtechArpType,
       "qtechArpEntryType": qtechArpEntryType,
       "qtechArpStatus": qtechArpStatus,
       "qtechArpIfTable": qtechArpIfTable,
       "qtechArpIfEntry": qtechArpIfEntry,
       "qtechArpIfIfIndex": qtechArpIfIfIndex,
       "qtechArpIfCacheTimeOut": qtechArpIfCacheTimeOut,
       "qtechArpCurrentTotalNumber": qtechArpCurrentTotalNumber,
       "qtechArpCurrentUnresolveNumber": qtechArpCurrentUnresolveNumber,
       "qtechArpMIBConformance": qtechArpMIBConformance,
       "qtechArpMIBCompliances": qtechArpMIBCompliances,
       "qtechArpMIBCompliance": qtechArpMIBCompliance,
       "qtechArpMIBGroups": qtechArpMIBGroups,
       "qtechArpMIBGroup": qtechArpMIBGroup}
)
