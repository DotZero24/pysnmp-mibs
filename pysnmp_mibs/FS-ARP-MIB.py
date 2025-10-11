# SNMP MIB module (FS-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:24 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
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

fsArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    fsArpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsArpMIBObjects_ObjectIdentity = ObjectIdentity
fsArpMIBObjects = _FsArpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1)
)
_FsArpTable_Object = MibTable
fsArpTable = _FsArpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsArpTable.setStatus("current")
_FsArpEntry_Object = MibTableRow
fsArpEntry = _FsArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1)
)
fsArpEntry.setIndexNames(
    (0, "FS-ARP-MIB", "fsArpIfIndex"),
    (0, "FS-ARP-MIB", "fsArpNetAddress"),
)
if mibBuilder.loadTexts:
    fsArpEntry.setStatus("current")
_FsArpIfIndex_Type = IfIndex
_FsArpIfIndex_Object = MibTableColumn
fsArpIfIndex = _FsArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 1),
    _FsArpIfIndex_Type()
)
fsArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpIfIndex.setStatus("current")
_FsArpPhysAddress_Type = PhysAddress
_FsArpPhysAddress_Object = MibTableColumn
fsArpPhysAddress = _FsArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 2),
    _FsArpPhysAddress_Type()
)
fsArpPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsArpPhysAddress.setStatus("current")
_FsArpNetAddress_Type = IpAddress
_FsArpNetAddress_Object = MibTableColumn
fsArpNetAddress = _FsArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 3),
    _FsArpNetAddress_Type()
)
fsArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpNetAddress.setStatus("current")
_FsArpRemainAge_Type = Integer32
_FsArpRemainAge_Object = MibTableColumn
fsArpRemainAge = _FsArpRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 4),
    _FsArpRemainAge_Type()
)
fsArpRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpRemainAge.setStatus("current")


class _FsArpType_Type(Integer32):
    """Custom type fsArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("arpa", 1)
    )


_FsArpType_Type.__name__ = "Integer32"
_FsArpType_Object = MibTableColumn
fsArpType = _FsArpType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 5),
    _FsArpType_Type()
)
fsArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsArpType.setStatus("current")


class _FsArpEntryType_Type(Integer32):
    """Custom type fsArpEntryType based on Integer32"""
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


_FsArpEntryType_Type.__name__ = "Integer32"
_FsArpEntryType_Object = MibTableColumn
fsArpEntryType = _FsArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 6),
    _FsArpEntryType_Type()
)
fsArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpEntryType.setStatus("current")
_FsArpStatus_Type = RowStatus
_FsArpStatus_Object = MibTableColumn
fsArpStatus = _FsArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 1, 1, 7),
    _FsArpStatus_Type()
)
fsArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsArpStatus.setStatus("current")
_FsArpIfTable_Object = MibTable
fsArpIfTable = _FsArpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fsArpIfTable.setStatus("current")
_FsArpIfEntry_Object = MibTableRow
fsArpIfEntry = _FsArpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 2, 1)
)
fsArpIfEntry.setIndexNames(
    (0, "FS-ARP-MIB", "fsArpIfIfIndex"),
)
if mibBuilder.loadTexts:
    fsArpIfEntry.setStatus("current")
_FsArpIfIfIndex_Type = IfIndex
_FsArpIfIfIndex_Object = MibTableColumn
fsArpIfIfIndex = _FsArpIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 2, 1, 1),
    _FsArpIfIfIndex_Type()
)
fsArpIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpIfIfIndex.setStatus("current")


class _FsArpIfCacheTimeOut_Type(Integer32):
    """Custom type fsArpIfCacheTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 18000),
    )


_FsArpIfCacheTimeOut_Type.__name__ = "Integer32"
_FsArpIfCacheTimeOut_Object = MibTableColumn
fsArpIfCacheTimeOut = _FsArpIfCacheTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 2, 1, 2),
    _FsArpIfCacheTimeOut_Type()
)
fsArpIfCacheTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsArpIfCacheTimeOut.setStatus("current")
_FsArpCurrentTotalNumber_Type = Counter32
_FsArpCurrentTotalNumber_Object = MibScalar
fsArpCurrentTotalNumber = _FsArpCurrentTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 3),
    _FsArpCurrentTotalNumber_Type()
)
fsArpCurrentTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpCurrentTotalNumber.setStatus("current")
_FsArpCurrentUnresolveNumber_Type = Counter32
_FsArpCurrentUnresolveNumber_Object = MibScalar
fsArpCurrentUnresolveNumber = _FsArpCurrentUnresolveNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 1, 4),
    _FsArpCurrentUnresolveNumber_Type()
)
fsArpCurrentUnresolveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpCurrentUnresolveNumber.setStatus("current")
_FsArpMIBConformance_ObjectIdentity = ObjectIdentity
fsArpMIBConformance = _FsArpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 2)
)
_FsArpMIBCompliances_ObjectIdentity = ObjectIdentity
fsArpMIBCompliances = _FsArpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 2, 1)
)
_FsArpMIBGroups_ObjectIdentity = ObjectIdentity
fsArpMIBGroups = _FsArpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 2, 2)
)

# Managed Objects groups

fsArpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 2, 2, 1)
)
fsArpMIBGroup.setObjects(
      *(("FS-ARP-MIB", "fsArpIfIndex"),
        ("FS-ARP-MIB", "fsArpPhysAddress"),
        ("FS-ARP-MIB", "fsArpNetAddress"),
        ("FS-ARP-MIB", "fsArpRemainAge"),
        ("FS-ARP-MIB", "fsArpType"),
        ("FS-ARP-MIB", "fsArpEntryType"),
        ("FS-ARP-MIB", "fsArpStatus"),
        ("FS-ARP-MIB", "fsArpIfIfIndex"),
        ("FS-ARP-MIB", "fsArpIfCacheTimeOut"),
        ("FS-ARP-MIB", "fsArpCurrentTotalNumber"),
        ("FS-ARP-MIB", "fsArpCurrentUnresolveNumber"))
)
if mibBuilder.loadTexts:
    fsArpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsArpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 2, 2, 1, 1)
)
fsArpMIBCompliance.setObjects(
    ("FS-ARP-MIB", "fsArpMIBGroup")
)
if mibBuilder.loadTexts:
    fsArpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ARP-MIB",
    **{"fsArpMIB": fsArpMIB,
       "fsArpMIBObjects": fsArpMIBObjects,
       "fsArpTable": fsArpTable,
       "fsArpEntry": fsArpEntry,
       "fsArpIfIndex": fsArpIfIndex,
       "fsArpPhysAddress": fsArpPhysAddress,
       "fsArpNetAddress": fsArpNetAddress,
       "fsArpRemainAge": fsArpRemainAge,
       "fsArpType": fsArpType,
       "fsArpEntryType": fsArpEntryType,
       "fsArpStatus": fsArpStatus,
       "fsArpIfTable": fsArpIfTable,
       "fsArpIfEntry": fsArpIfEntry,
       "fsArpIfIfIndex": fsArpIfIfIndex,
       "fsArpIfCacheTimeOut": fsArpIfCacheTimeOut,
       "fsArpCurrentTotalNumber": fsArpCurrentTotalNumber,
       "fsArpCurrentUnresolveNumber": fsArpCurrentUnresolveNumber,
       "fsArpMIBConformance": fsArpMIBConformance,
       "fsArpMIBCompliances": fsArpMIBCompliances,
       "fsArpMIBCompliance": fsArpMIBCompliance,
       "fsArpMIBGroups": fsArpMIBGroups,
       "fsArpMIBGroup": fsArpMIBGroup}
)
