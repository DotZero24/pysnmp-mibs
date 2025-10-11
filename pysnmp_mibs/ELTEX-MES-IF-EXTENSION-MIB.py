# SNMP MIB module (ELTEX-MES-IF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-IF-EXTENSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:08 2025
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

(eltMesIfExtensionMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesIfExtensionMIB")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIfExtensionMIBObjects_ObjectIdentity = ObjectIdentity
eltMesIfExtensionMIBObjects = _EltMesIfExtensionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1)
)
_EltMesIfExtDot1qCustomEtherType_ObjectIdentity = ObjectIdentity
eltMesIfExtDot1qCustomEtherType = _EltMesIfExtDot1qCustomEtherType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3)
)
_EltIfDot1qCustomEgressEtherTypeTable_Object = MibTable
eltIfDot1qCustomEgressEtherTypeTable = _EltIfDot1qCustomEgressEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomEgressEtherTypeTable.setStatus("current")
_EltIfDot1qCustomEgressEtherTypeEntry_Object = MibTableRow
eltIfDot1qCustomEgressEtherTypeEntry = _EltIfDot1qCustomEgressEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 1, 1)
)
eltIfDot1qCustomEgressEtherTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomEgressEtherTypeEntry.setStatus("current")


class _EltIfDot1qCustomEgressEtherType_Type(Integer32):
    """Custom type eltIfDot1qCustomEgressEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltIfDot1qCustomEgressEtherType_Type.__name__ = "Integer32"
_EltIfDot1qCustomEgressEtherType_Object = MibTableColumn
eltIfDot1qCustomEgressEtherType = _EltIfDot1qCustomEgressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 1, 1, 1),
    _EltIfDot1qCustomEgressEtherType_Type()
)
eltIfDot1qCustomEgressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomEgressEtherType.setStatus("current")
_EltIfDot1qCustomIngressEtherTypeTable_Object = MibTable
eltIfDot1qCustomIngressEtherTypeTable = _EltIfDot1qCustomIngressEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherTypeTable.setStatus("current")
_EltIfDot1qCustomIngressEtherTypeEntry_Object = MibTableRow
eltIfDot1qCustomIngressEtherTypeEntry = _EltIfDot1qCustomIngressEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1)
)
eltIfDot1qCustomIngressEtherTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherTypeEntry.setStatus("current")


class _EltIfDot1qCustomIngressEtherType1_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType1 based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(33024, 33024),
    )


_EltIfDot1qCustomIngressEtherType1_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType1_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType1 = _EltIfDot1qCustomIngressEtherType1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 1),
    _EltIfDot1qCustomIngressEtherType1_Type()
)
eltIfDot1qCustomIngressEtherType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType1.setStatus("current")


class _EltIfDot1qCustomIngressEtherType2_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType2_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType2_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType2 = _EltIfDot1qCustomIngressEtherType2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 2),
    _EltIfDot1qCustomIngressEtherType2_Type()
)
eltIfDot1qCustomIngressEtherType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType2.setStatus("current")


class _EltIfDot1qCustomIngressEtherType3_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType3_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType3_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType3 = _EltIfDot1qCustomIngressEtherType3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 3),
    _EltIfDot1qCustomIngressEtherType3_Type()
)
eltIfDot1qCustomIngressEtherType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType3.setStatus("current")


class _EltIfDot1qCustomIngressEtherType4_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType4_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType4_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType4 = _EltIfDot1qCustomIngressEtherType4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 4),
    _EltIfDot1qCustomIngressEtherType4_Type()
)
eltIfDot1qCustomIngressEtherType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType4.setStatus("current")


class _EltIfDot1qCustomIngressEtherType5_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType5_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType5_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType5 = _EltIfDot1qCustomIngressEtherType5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 5),
    _EltIfDot1qCustomIngressEtherType5_Type()
)
eltIfDot1qCustomIngressEtherType5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType5.setStatus("current")


class _EltIfDot1qCustomIngressEtherType6_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType6_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType6_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType6 = _EltIfDot1qCustomIngressEtherType6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 6),
    _EltIfDot1qCustomIngressEtherType6_Type()
)
eltIfDot1qCustomIngressEtherType6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType6.setStatus("current")


class _EltIfDot1qCustomIngressEtherType7_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType7_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType7_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType7 = _EltIfDot1qCustomIngressEtherType7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 7),
    _EltIfDot1qCustomIngressEtherType7_Type()
)
eltIfDot1qCustomIngressEtherType7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType7.setStatus("current")
_EltMesIfExtDot1q_ObjectIdentity = ObjectIdentity
eltMesIfExtDot1q = _EltMesIfExtDot1q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4)
)
_EltIfDot1qIngressCvlanTable_Object = MibTable
eltIfDot1qIngressCvlanTable = _EltIfDot1qIngressCvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltIfDot1qIngressCvlanTable.setStatus("current")
_EltIfDot1qIngressCvlanEntry_Object = MibTableRow
eltIfDot1qIngressCvlanEntry = _EltIfDot1qIngressCvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 1, 1)
)
eltIfDot1qIngressCvlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIfDot1qIngressCvlanEntry.setStatus("current")


class _EltIfDot1qIngressCvlanTag_Type(Integer32):
    """Custom type eltIfDot1qIngressCvlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_EltIfDot1qIngressCvlanTag_Type.__name__ = "Integer32"
_EltIfDot1qIngressCvlanTag_Object = MibTableColumn
eltIfDot1qIngressCvlanTag = _EltIfDot1qIngressCvlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 1, 1, 1),
    _EltIfDot1qIngressCvlanTag_Type()
)
eltIfDot1qIngressCvlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qIngressCvlanTag.setStatus("current")
_EltIfDot1qTr101CVlanMapTable_Object = MibTable
eltIfDot1qTr101CVlanMapTable = _EltIfDot1qTr101CVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 2)
)
if mibBuilder.loadTexts:
    eltIfDot1qTr101CVlanMapTable.setStatus("current")
_EltIfDot1qTr101CVlanMapEntry_Object = MibTableRow
eltIfDot1qTr101CVlanMapEntry = _EltIfDot1qTr101CVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 2, 1)
)
eltIfDot1qTr101CVlanMapEntry.setIndexNames(
    (0, "ELTEX-MES-IF-EXTENSION-MIB", "eltIfDot1qIngressCvlanTag"),
)
if mibBuilder.loadTexts:
    eltIfDot1qTr101CVlanMapEntry.setStatus("current")
_EltIfDot1qTr101CVlanMapRowStatus_Type = RowStatus
_EltIfDot1qTr101CVlanMapRowStatus_Object = MibTableColumn
eltIfDot1qTr101CVlanMapRowStatus = _EltIfDot1qTr101CVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 2, 1, 1),
    _EltIfDot1qTr101CVlanMapRowStatus_Type()
)
eltIfDot1qTr101CVlanMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qTr101CVlanMapRowStatus.setStatus("current")
_EltIfDot1qTr101CVlanMapPortList_Type = PortList
_EltIfDot1qTr101CVlanMapPortList_Object = MibTableColumn
eltIfDot1qTr101CVlanMapPortList = _EltIfDot1qTr101CVlanMapPortList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 2, 1, 2),
    _EltIfDot1qTr101CVlanMapPortList_Type()
)
eltIfDot1qTr101CVlanMapPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qTr101CVlanMapPortList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IF-EXTENSION-MIB",
    **{"eltMesIfExtensionMIBObjects": eltMesIfExtensionMIBObjects,
       "eltMesIfExtDot1qCustomEtherType": eltMesIfExtDot1qCustomEtherType,
       "eltIfDot1qCustomEgressEtherTypeTable": eltIfDot1qCustomEgressEtherTypeTable,
       "eltIfDot1qCustomEgressEtherTypeEntry": eltIfDot1qCustomEgressEtherTypeEntry,
       "eltIfDot1qCustomEgressEtherType": eltIfDot1qCustomEgressEtherType,
       "eltIfDot1qCustomIngressEtherTypeTable": eltIfDot1qCustomIngressEtherTypeTable,
       "eltIfDot1qCustomIngressEtherTypeEntry": eltIfDot1qCustomIngressEtherTypeEntry,
       "eltIfDot1qCustomIngressEtherType1": eltIfDot1qCustomIngressEtherType1,
       "eltIfDot1qCustomIngressEtherType2": eltIfDot1qCustomIngressEtherType2,
       "eltIfDot1qCustomIngressEtherType3": eltIfDot1qCustomIngressEtherType3,
       "eltIfDot1qCustomIngressEtherType4": eltIfDot1qCustomIngressEtherType4,
       "eltIfDot1qCustomIngressEtherType5": eltIfDot1qCustomIngressEtherType5,
       "eltIfDot1qCustomIngressEtherType6": eltIfDot1qCustomIngressEtherType6,
       "eltIfDot1qCustomIngressEtherType7": eltIfDot1qCustomIngressEtherType7,
       "eltMesIfExtDot1q": eltMesIfExtDot1q,
       "eltIfDot1qIngressCvlanTable": eltIfDot1qIngressCvlanTable,
       "eltIfDot1qIngressCvlanEntry": eltIfDot1qIngressCvlanEntry,
       "eltIfDot1qIngressCvlanTag": eltIfDot1qIngressCvlanTag,
       "eltIfDot1qTr101CVlanMapTable": eltIfDot1qTr101CVlanMapTable,
       "eltIfDot1qTr101CVlanMapEntry": eltIfDot1qTr101CVlanMapEntry,
       "eltIfDot1qTr101CVlanMapRowStatus": eltIfDot1qTr101CVlanMapRowStatus,
       "eltIfDot1qTr101CVlanMapPortList": eltIfDot1qTr101CVlanMapPortList}
)
