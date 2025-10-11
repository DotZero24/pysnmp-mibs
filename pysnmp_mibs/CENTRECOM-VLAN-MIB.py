# SNMP MIB module (CENTRECOM-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/CENTRECOM-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:33 2025
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

(extSwitchMIB,) = mibBuilder.importSymbols(
    "CENTRECOM-MIB",
    "extSwitchMIB")

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

atiVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4)
)


# Types definitions



class AtiSwitchVlanType(Integer32):
    """Custom type AtiSwitchVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlanLayer2", 1)
    )





class AtiSwitchVlanEncapsType(Integer32):
    """Custom type AtiSwitchVlanEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("vlanEncaps8021q", 2)
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtiVlanGroup_ObjectIdentity = ObjectIdentity
atiVlanGroup = _AtiVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1)
)
_AtiVlanIfTable_Object = MibTable
atiVlanIfTable = _AtiVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    atiVlanIfTable.setStatus("mandatory")
_AtiVlanIfEntry_Object = MibTableRow
atiVlanIfEntry = _AtiVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2, 1)
)
atiVlanIfEntry.setIndexNames(
    (0, "CENTRECOM-VLAN-MIB", "atiVlanIfIndex"),
)
if mibBuilder.loadTexts:
    atiVlanIfEntry.setStatus("mandatory")
_AtiVlanIfIndex_Type = Integer32
_AtiVlanIfIndex_Object = MibTableColumn
atiVlanIfIndex = _AtiVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2, 1, 1),
    _AtiVlanIfIndex_Type()
)
atiVlanIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanIfIndex.setStatus("mandatory")


class _AtiVlanIfDescr_Type(DisplayString):
    """Custom type atiVlanIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtiVlanIfDescr_Type.__name__ = "DisplayString"
_AtiVlanIfDescr_Object = MibTableColumn
atiVlanIfDescr = _AtiVlanIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2, 1, 2),
    _AtiVlanIfDescr_Type()
)
atiVlanIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanIfDescr.setStatus("mandatory")
_AtiVlanIfType_Type = AtiSwitchVlanType
_AtiVlanIfType_Object = MibTableColumn
atiVlanIfType = _AtiVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2, 1, 3),
    _AtiVlanIfType_Type()
)
atiVlanIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanIfType.setStatus("mandatory")


class _AtiVlanIfGlobalIdentifier_Type(Integer32):
    """Custom type atiVlanIfGlobalIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtiVlanIfGlobalIdentifier_Type.__name__ = "Integer32"
_AtiVlanIfGlobalIdentifier_Object = MibTableColumn
atiVlanIfGlobalIdentifier = _AtiVlanIfGlobalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2, 1, 4),
    _AtiVlanIfGlobalIdentifier_Type()
)
atiVlanIfGlobalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanIfGlobalIdentifier.setStatus("mandatory")
_AtiVlanIfStatus_Type = RowStatus
_AtiVlanIfStatus_Object = MibTableColumn
atiVlanIfStatus = _AtiVlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 1, 2, 1, 6),
    _AtiVlanIfStatus_Type()
)
atiVlanIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanIfStatus.setStatus("mandatory")
_AtiVirtualGroup_ObjectIdentity = ObjectIdentity
atiVirtualGroup = _AtiVirtualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 2)
)
_AtiNextAvailableVirtIfIndex_Type = Integer32
_AtiNextAvailableVirtIfIndex_Object = MibScalar
atiNextAvailableVirtIfIndex = _AtiNextAvailableVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 2, 1),
    _AtiNextAvailableVirtIfIndex_Type()
)
atiNextAvailableVirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiNextAvailableVirtIfIndex.setStatus("mandatory")
_AtiEncapsulationGroup_ObjectIdentity = ObjectIdentity
atiEncapsulationGroup = _AtiEncapsulationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3)
)
_AtiVlanEncapsIfTable_Object = MibTable
atiVlanEncapsIfTable = _AtiVlanEncapsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atiVlanEncapsIfTable.setStatus("mandatory")
_AtiVlanEncapsIfEntry_Object = MibTableRow
atiVlanEncapsIfEntry = _AtiVlanEncapsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3, 1, 1)
)
atiVlanEncapsIfEntry.setIndexNames(
    (0, "CENTRECOM-VLAN-MIB", "atiVlanEncapsIfIndex"),
)
if mibBuilder.loadTexts:
    atiVlanEncapsIfEntry.setStatus("mandatory")
_AtiVlanEncapsIfIndex_Type = Integer32
_AtiVlanEncapsIfIndex_Object = MibTableColumn
atiVlanEncapsIfIndex = _AtiVlanEncapsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3, 1, 1, 1),
    _AtiVlanEncapsIfIndex_Type()
)
atiVlanEncapsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanEncapsIfIndex.setStatus("mandatory")
_AtiVlanEncapsIfType_Type = AtiSwitchVlanEncapsType
_AtiVlanEncapsIfType_Object = MibTableColumn
atiVlanEncapsIfType = _AtiVlanEncapsIfType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3, 1, 1, 2),
    _AtiVlanEncapsIfType_Type()
)
atiVlanEncapsIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanEncapsIfType.setStatus("mandatory")
_AtiVlanEncapsIfTag_Type = Integer32
_AtiVlanEncapsIfTag_Object = MibTableColumn
atiVlanEncapsIfTag = _AtiVlanEncapsIfTag_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3, 1, 1, 3),
    _AtiVlanEncapsIfTag_Type()
)
atiVlanEncapsIfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanEncapsIfTag.setStatus("mandatory")
_AtiVlanEncapsIfStatus_Type = RowStatus
_AtiVlanEncapsIfStatus_Object = MibTableColumn
atiVlanEncapsIfStatus = _AtiVlanEncapsIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 3, 1, 1, 4),
    _AtiVlanEncapsIfStatus_Type()
)
atiVlanEncapsIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanEncapsIfStatus.setStatus("mandatory")
_AtiProtocolGroup_ObjectIdentity = ObjectIdentity
atiProtocolGroup = _AtiProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5)
)
_AtiVlanProtocolTable_Object = MibTable
atiVlanProtocolTable = _AtiVlanProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    atiVlanProtocolTable.setStatus("mandatory")
_AtiVlanProtocolEntry_Object = MibTableRow
atiVlanProtocolEntry = _AtiVlanProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1)
)
atiVlanProtocolEntry.setIndexNames(
    (0, "CENTRECOM-VLAN-MIB", "atiVlanProtocolIndex"),
    (0, "CENTRECOM-VLAN-MIB", "atiVlanProtocolIdIndex"),
)
if mibBuilder.loadTexts:
    atiVlanProtocolEntry.setStatus("mandatory")


class _AtiVlanProtocolIndex_Type(Integer32):
    """Custom type atiVlanProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtiVlanProtocolIndex_Type.__name__ = "Integer32"
_AtiVlanProtocolIndex_Object = MibTableColumn
atiVlanProtocolIndex = _AtiVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1, 1),
    _AtiVlanProtocolIndex_Type()
)
atiVlanProtocolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolIndex.setStatus("mandatory")


class _AtiVlanProtocolIdIndex_Type(Integer32):
    """Custom type atiVlanProtocolIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AtiVlanProtocolIdIndex_Type.__name__ = "Integer32"
_AtiVlanProtocolIdIndex_Object = MibTableColumn
atiVlanProtocolIdIndex = _AtiVlanProtocolIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1, 2),
    _AtiVlanProtocolIdIndex_Type()
)
atiVlanProtocolIdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolIdIndex.setStatus("mandatory")


class _AtiVlanProtocolName_Type(DisplayString):
    """Custom type atiVlanProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtiVlanProtocolName_Type.__name__ = "DisplayString"
_AtiVlanProtocolName_Object = MibTableColumn
atiVlanProtocolName = _AtiVlanProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1, 3),
    _AtiVlanProtocolName_Type()
)
atiVlanProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolName.setStatus("mandatory")


class _AtiVlanProtocolDllEncapsType_Type(Integer32):
    """Custom type atiVlanProtocolDllEncapsType based on Integer32"""
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
        *(("any", 1),
          ("ethertype", 2),
          ("llc", 3),
          ("llcSnapEthertype", 4))
    )


_AtiVlanProtocolDllEncapsType_Type.__name__ = "Integer32"
_AtiVlanProtocolDllEncapsType_Object = MibTableColumn
atiVlanProtocolDllEncapsType = _AtiVlanProtocolDllEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1, 4),
    _AtiVlanProtocolDllEncapsType_Type()
)
atiVlanProtocolDllEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolDllEncapsType.setStatus("mandatory")


class _AtiVlanProtocolId_Type(Integer32):
    """Custom type atiVlanProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtiVlanProtocolId_Type.__name__ = "Integer32"
_AtiVlanProtocolId_Object = MibTableColumn
atiVlanProtocolId = _AtiVlanProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1, 5),
    _AtiVlanProtocolId_Type()
)
atiVlanProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolId.setStatus("mandatory")
_AtiVlanProtocolStatus_Type = RowStatus
_AtiVlanProtocolStatus_Object = MibTableColumn
atiVlanProtocolStatus = _AtiVlanProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 1, 1, 6),
    _AtiVlanProtocolStatus_Type()
)
atiVlanProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolStatus.setStatus("mandatory")
_AtiVlanProtocolVlanTable_Object = MibTable
atiVlanProtocolVlanTable = _AtiVlanProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    atiVlanProtocolVlanTable.setStatus("mandatory")
_AtiVlanProtocolVlanEntry_Object = MibTableRow
atiVlanProtocolVlanEntry = _AtiVlanProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 2, 1)
)
atiVlanProtocolVlanEntry.setIndexNames(
    (0, "CENTRECOM-VLAN-MIB", "atiVlanProtocolVlanIfIndex"),
    (0, "CENTRECOM-VLAN-MIB", "atiVlanProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    atiVlanProtocolVlanEntry.setStatus("mandatory")
_AtiVlanProtocolVlanIfIndex_Type = Integer32
_AtiVlanProtocolVlanIfIndex_Object = MibTableColumn
atiVlanProtocolVlanIfIndex = _AtiVlanProtocolVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 2, 1, 1),
    _AtiVlanProtocolVlanIfIndex_Type()
)
atiVlanProtocolVlanIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolVlanIfIndex.setStatus("mandatory")
_AtiVlanProtocolVlanProtocolIndex_Type = Integer32
_AtiVlanProtocolVlanProtocolIndex_Object = MibTableColumn
atiVlanProtocolVlanProtocolIndex = _AtiVlanProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 2, 1, 2),
    _AtiVlanProtocolVlanProtocolIndex_Type()
)
atiVlanProtocolVlanProtocolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolVlanProtocolIndex.setStatus("mandatory")
_AtiVlanProtocolVlanStatus_Type = RowStatus
_AtiVlanProtocolVlanStatus_Object = MibTableColumn
atiVlanProtocolVlanStatus = _AtiVlanProtocolVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 4, 5, 2, 1, 3),
    _AtiVlanProtocolVlanStatus_Type()
)
atiVlanProtocolVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiVlanProtocolVlanStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTRECOM-VLAN-MIB",
    **{"AtiSwitchVlanType": AtiSwitchVlanType,
       "AtiSwitchVlanEncapsType": AtiSwitchVlanEncapsType,
       "atiVlan": atiVlan,
       "atiVlanGroup": atiVlanGroup,
       "atiVlanIfTable": atiVlanIfTable,
       "atiVlanIfEntry": atiVlanIfEntry,
       "atiVlanIfIndex": atiVlanIfIndex,
       "atiVlanIfDescr": atiVlanIfDescr,
       "atiVlanIfType": atiVlanIfType,
       "atiVlanIfGlobalIdentifier": atiVlanIfGlobalIdentifier,
       "atiVlanIfStatus": atiVlanIfStatus,
       "atiVirtualGroup": atiVirtualGroup,
       "atiNextAvailableVirtIfIndex": atiNextAvailableVirtIfIndex,
       "atiEncapsulationGroup": atiEncapsulationGroup,
       "atiVlanEncapsIfTable": atiVlanEncapsIfTable,
       "atiVlanEncapsIfEntry": atiVlanEncapsIfEntry,
       "atiVlanEncapsIfIndex": atiVlanEncapsIfIndex,
       "atiVlanEncapsIfType": atiVlanEncapsIfType,
       "atiVlanEncapsIfTag": atiVlanEncapsIfTag,
       "atiVlanEncapsIfStatus": atiVlanEncapsIfStatus,
       "atiProtocolGroup": atiProtocolGroup,
       "atiVlanProtocolTable": atiVlanProtocolTable,
       "atiVlanProtocolEntry": atiVlanProtocolEntry,
       "atiVlanProtocolIndex": atiVlanProtocolIndex,
       "atiVlanProtocolIdIndex": atiVlanProtocolIdIndex,
       "atiVlanProtocolName": atiVlanProtocolName,
       "atiVlanProtocolDllEncapsType": atiVlanProtocolDllEncapsType,
       "atiVlanProtocolId": atiVlanProtocolId,
       "atiVlanProtocolStatus": atiVlanProtocolStatus,
       "atiVlanProtocolVlanTable": atiVlanProtocolVlanTable,
       "atiVlanProtocolVlanEntry": atiVlanProtocolVlanEntry,
       "atiVlanProtocolVlanIfIndex": atiVlanProtocolVlanIfIndex,
       "atiVlanProtocolVlanProtocolIndex": atiVlanProtocolVlanProtocolIndex,
       "atiVlanProtocolVlanStatus": atiVlanProtocolVlanStatus}
)
