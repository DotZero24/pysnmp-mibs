# SNMP MIB module (ZXPW-ENET-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXPW-ENET-STD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:13 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")

(zxAnCesMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnCesMib")

(zxPwIndex,) = mibBuilder.importSymbols(
    "ZXPW-STD-MIB",
    "zxPwIndex")


# MODULE-IDENTITY

zxPwEnetStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIdOrAnyOrNone(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_ZxPwEnetObjects_ObjectIdentity = ObjectIdentity
zxPwEnetObjects = _ZxPwEnetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1)
)
_ZxPwEnetTable_Object = MibTable
zxPwEnetTable = _ZxPwEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1)
)
if mibBuilder.loadTexts:
    zxPwEnetTable.setStatus("current")
_ZxPwEnetEntry_Object = MibTableRow
zxPwEnetEntry = _ZxPwEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1)
)
zxPwEnetEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
    (0, "ZXPW-ENET-STD-MIB", "zxPwEnetPwInstance"),
)
if mibBuilder.loadTexts:
    zxPwEnetEntry.setStatus("current")
_ZxPwEnetPwInstance_Type = Unsigned32
_ZxPwEnetPwInstance_Object = MibTableColumn
zxPwEnetPwInstance = _ZxPwEnetPwInstance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 1),
    _ZxPwEnetPwInstance_Type()
)
zxPwEnetPwInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxPwEnetPwInstance.setStatus("current")
_ZxPwEnetPwVlan_Type = VlanIdOrAnyOrNone
_ZxPwEnetPwVlan_Object = MibTableColumn
zxPwEnetPwVlan = _ZxPwEnetPwVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 2),
    _ZxPwEnetPwVlan_Type()
)
zxPwEnetPwVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetPwVlan.setStatus("current")


class _ZxPwEnetVlanMode_Type(Integer32):
    """Custom type zxPwEnetVlanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("portBased", 1),
          ("noChange", 2),
          ("changeVlan", 3),
          ("addVlan", 4),
          ("removeVlan", 5))
    )


_ZxPwEnetVlanMode_Type.__name__ = "Integer32"
_ZxPwEnetVlanMode_Object = MibTableColumn
zxPwEnetVlanMode = _ZxPwEnetVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 3),
    _ZxPwEnetVlanMode_Type()
)
zxPwEnetVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetVlanMode.setStatus("current")


class _ZxPwEnetPortVlan_Type(VlanIdOrAnyOrNone):
    """Custom type zxPwEnetPortVlan based on VlanIdOrAnyOrNone"""
    defaultValue = 4095


_ZxPwEnetPortVlan_Type.__name__ = "VlanIdOrAnyOrNone"
_ZxPwEnetPortVlan_Object = MibTableColumn
zxPwEnetPortVlan = _ZxPwEnetPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 4),
    _ZxPwEnetPortVlan_Type()
)
zxPwEnetPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetPortVlan.setStatus("current")
_ZxPwEnetPortIfIndex_Type = InterfaceIndexOrZero
_ZxPwEnetPortIfIndex_Object = MibTableColumn
zxPwEnetPortIfIndex = _ZxPwEnetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 5),
    _ZxPwEnetPortIfIndex_Type()
)
zxPwEnetPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetPortIfIndex.setStatus("current")


class _ZxPwEnetPwIfIndex_Type(InterfaceIndexOrZero):
    """Custom type zxPwEnetPwIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZxPwEnetPwIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_ZxPwEnetPwIfIndex_Object = MibTableColumn
zxPwEnetPwIfIndex = _ZxPwEnetPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 6),
    _ZxPwEnetPwIfIndex_Type()
)
zxPwEnetPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetPwIfIndex.setStatus("current")
_ZxPwEnetRowStatus_Type = RowStatus
_ZxPwEnetRowStatus_Object = MibTableColumn
zxPwEnetRowStatus = _ZxPwEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 7),
    _ZxPwEnetRowStatus_Type()
)
zxPwEnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetRowStatus.setStatus("current")


class _ZxPwEnetStorageType_Type(StorageType):
    """Custom type zxPwEnetStorageType based on StorageType"""
    defaultValue = 3


_ZxPwEnetStorageType_Type.__name__ = "StorageType"
_ZxPwEnetStorageType_Object = MibTableColumn
zxPwEnetStorageType = _ZxPwEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 8),
    _ZxPwEnetStorageType_Type()
)
zxPwEnetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwEnetStorageType.setStatus("current")
_ZxPwEnetConformance_ObjectIdentity = ObjectIdentity
zxPwEnetConformance = _ZxPwEnetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXPW-ENET-STD-MIB",
    **{"VlanIdOrAnyOrNone": VlanIdOrAnyOrNone,
       "zxPwEnetStdMIB": zxPwEnetStdMIB,
       "zxPwEnetObjects": zxPwEnetObjects,
       "zxPwEnetTable": zxPwEnetTable,
       "zxPwEnetEntry": zxPwEnetEntry,
       "zxPwEnetPwInstance": zxPwEnetPwInstance,
       "zxPwEnetPwVlan": zxPwEnetPwVlan,
       "zxPwEnetVlanMode": zxPwEnetVlanMode,
       "zxPwEnetPortVlan": zxPwEnetPortVlan,
       "zxPwEnetPortIfIndex": zxPwEnetPortIfIndex,
       "zxPwEnetPwIfIndex": zxPwEnetPwIfIndex,
       "zxPwEnetRowStatus": zxPwEnetRowStatus,
       "zxPwEnetStorageType": zxPwEnetStorageType,
       "zxPwEnetConformance": zxPwEnetConformance}
)
