# SNMP MIB module (H3C-QOS-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-QOS-CAPABILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:31 2025
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

(h3cSNMPAgCpb,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cSNMPAgCpb")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1)
)
if mibBuilder.loadTexts:
    h3cQosCapability.setRevisions(
        ("2016-10-25 00:00",
         "2014-10-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CapabilityPhysicalType(TextualConvention, Integer32):
    status = "current"
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
        *(("stack", 1),
          ("chassis", 2),
          ("module", 3),
          ("port", 4))
    )



# MIB Managed Objects in the order of their OIDs

_H3cQoSCapabilityMibObjects_ObjectIdentity = ObjectIdentity
h3cQoSCapabilityMibObjects = _H3cQoSCapabilityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1)
)
_H3cQoSCapabilityGroup_ObjectIdentity = ObjectIdentity
h3cQoSCapabilityGroup = _H3cQoSCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1)
)
_H3cQoSCapabilityTable_Object = MibTable
h3cQoSCapabilityTable = _H3cQoSCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cQoSCapabilityTable.setStatus("current")
_H3cQoSCapabilityEntry_Object = MibTableRow
h3cQoSCapabilityEntry = _H3cQoSCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1)
)
h3cQoSCapabilityEntry.setIndexNames(
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalType"),
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalIndex"),
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSModuleIndex"),
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSCapabilityEntry.setStatus("current")
_H3cQoSCapabilityPhysicalType_Type = CapabilityPhysicalType
_H3cQoSCapabilityPhysicalType_Object = MibTableColumn
h3cQoSCapabilityPhysicalType = _H3cQoSCapabilityPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 1),
    _H3cQoSCapabilityPhysicalType_Type()
)
h3cQoSCapabilityPhysicalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSCapabilityPhysicalType.setStatus("current")
_H3cQoSCapabilityPhysicalIndex_Type = Integer32
_H3cQoSCapabilityPhysicalIndex_Object = MibTableColumn
h3cQoSCapabilityPhysicalIndex = _H3cQoSCapabilityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 2),
    _H3cQoSCapabilityPhysicalIndex_Type()
)
h3cQoSCapabilityPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSCapabilityPhysicalIndex.setStatus("current")
_H3cQoSModuleIndex_Type = Integer32
_H3cQoSModuleIndex_Object = MibTableColumn
h3cQoSModuleIndex = _H3cQoSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 3),
    _H3cQoSModuleIndex_Type()
)
h3cQoSModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSModuleIndex.setStatus("current")
_H3cQoSCharacteristicsIndex_Type = Integer32
_H3cQoSCharacteristicsIndex_Object = MibTableColumn
h3cQoSCharacteristicsIndex = _H3cQoSCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 4),
    _H3cQoSCharacteristicsIndex_Type()
)
h3cQoSCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSCharacteristicsIndex.setStatus("current")
_H3cQoSCharacteristicsValue_Type = Unsigned32
_H3cQoSCharacteristicsValue_Object = MibTableColumn
h3cQoSCharacteristicsValue = _H3cQoSCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 5),
    _H3cQoSCharacteristicsValue_Type()
)
h3cQoSCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSCharacteristicsValue.setStatus("current")
_H3cQoSSysCapabilityTable_Object = MibTable
h3cQoSSysCapabilityTable = _H3cQoSSysCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cQoSSysCapabilityTable.setStatus("current")
_H3cQoSSysCapabilityEntry_Object = MibTableRow
h3cQoSSysCapabilityEntry = _H3cQoSSysCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 2, 1)
)
h3cQoSSysCapabilityEntry.setIndexNames(
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSSysCapModuleIndex"),
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSSysCapCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSSysCapabilityEntry.setStatus("current")


class _H3cQoSSysCapModuleIndex_Type(Integer32):
    """Custom type h3cQoSSysCapModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSSysCapModuleIndex_Type.__name__ = "Integer32"
_H3cQoSSysCapModuleIndex_Object = MibTableColumn
h3cQoSSysCapModuleIndex = _H3cQoSSysCapModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 2, 1, 1),
    _H3cQoSSysCapModuleIndex_Type()
)
h3cQoSSysCapModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSSysCapModuleIndex.setStatus("current")


class _H3cQoSSysCapCharacteristicsIndex_Type(Integer32):
    """Custom type h3cQoSSysCapCharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSSysCapCharacteristicsIndex_Type.__name__ = "Integer32"
_H3cQoSSysCapCharacteristicsIndex_Object = MibTableColumn
h3cQoSSysCapCharacteristicsIndex = _H3cQoSSysCapCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 2, 1, 2),
    _H3cQoSSysCapCharacteristicsIndex_Type()
)
h3cQoSSysCapCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSSysCapCharacteristicsIndex.setStatus("current")
_H3cQoSSysCapCharacteristicsValue_Type = Unsigned32
_H3cQoSSysCapCharacteristicsValue_Object = MibTableColumn
h3cQoSSysCapCharacteristicsValue = _H3cQoSSysCapCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 2, 1, 3),
    _H3cQoSSysCapCharacteristicsValue_Type()
)
h3cQoSSysCapCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSSysCapCharacteristicsValue.setStatus("current")
_H3cQoSIfCapabilityTable_Object = MibTable
h3cQoSIfCapabilityTable = _H3cQoSIfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cQoSIfCapabilityTable.setStatus("current")
_H3cQoSIfCapabilityEntry_Object = MibTableRow
h3cQoSIfCapabilityEntry = _H3cQoSIfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 3, 1)
)
h3cQoSIfCapabilityEntry.setIndexNames(
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSIfCapIfIndex"),
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSIfCapModuleIndex"),
    (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSIfCapCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSIfCapabilityEntry.setStatus("current")


class _H3cQoSIfCapIfIndex_Type(Integer32):
    """Custom type h3cQoSIfCapIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cQoSIfCapIfIndex_Type.__name__ = "Integer32"
_H3cQoSIfCapIfIndex_Object = MibTableColumn
h3cQoSIfCapIfIndex = _H3cQoSIfCapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 3, 1, 1),
    _H3cQoSIfCapIfIndex_Type()
)
h3cQoSIfCapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfCapIfIndex.setStatus("current")


class _H3cQoSIfCapModuleIndex_Type(Integer32):
    """Custom type h3cQoSIfCapModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSIfCapModuleIndex_Type.__name__ = "Integer32"
_H3cQoSIfCapModuleIndex_Object = MibTableColumn
h3cQoSIfCapModuleIndex = _H3cQoSIfCapModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 3, 1, 2),
    _H3cQoSIfCapModuleIndex_Type()
)
h3cQoSIfCapModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfCapModuleIndex.setStatus("current")


class _H3cQoSIfCapCharacteristicsIndex_Type(Integer32):
    """Custom type h3cQoSIfCapCharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSIfCapCharacteristicsIndex_Type.__name__ = "Integer32"
_H3cQoSIfCapCharacteristicsIndex_Object = MibTableColumn
h3cQoSIfCapCharacteristicsIndex = _H3cQoSIfCapCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 3, 1, 3),
    _H3cQoSIfCapCharacteristicsIndex_Type()
)
h3cQoSIfCapCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfCapCharacteristicsIndex.setStatus("current")
_H3cQoSIfCapCharacteristicsValue_Type = Unsigned32
_H3cQoSIfCapCharacteristicsValue_Object = MibTableColumn
h3cQoSIfCapCharacteristicsValue = _H3cQoSIfCapCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 3, 1, 4),
    _H3cQoSIfCapCharacteristicsValue_Type()
)
h3cQoSIfCapCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfCapCharacteristicsValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-QOS-CAPABILITY-MIB",
    **{"CapabilityPhysicalType": CapabilityPhysicalType,
       "h3cQosCapability": h3cQosCapability,
       "h3cQoSCapabilityMibObjects": h3cQoSCapabilityMibObjects,
       "h3cQoSCapabilityGroup": h3cQoSCapabilityGroup,
       "h3cQoSCapabilityTable": h3cQoSCapabilityTable,
       "h3cQoSCapabilityEntry": h3cQoSCapabilityEntry,
       "h3cQoSCapabilityPhysicalType": h3cQoSCapabilityPhysicalType,
       "h3cQoSCapabilityPhysicalIndex": h3cQoSCapabilityPhysicalIndex,
       "h3cQoSModuleIndex": h3cQoSModuleIndex,
       "h3cQoSCharacteristicsIndex": h3cQoSCharacteristicsIndex,
       "h3cQoSCharacteristicsValue": h3cQoSCharacteristicsValue,
       "h3cQoSSysCapabilityTable": h3cQoSSysCapabilityTable,
       "h3cQoSSysCapabilityEntry": h3cQoSSysCapabilityEntry,
       "h3cQoSSysCapModuleIndex": h3cQoSSysCapModuleIndex,
       "h3cQoSSysCapCharacteristicsIndex": h3cQoSSysCapCharacteristicsIndex,
       "h3cQoSSysCapCharacteristicsValue": h3cQoSSysCapCharacteristicsValue,
       "h3cQoSIfCapabilityTable": h3cQoSIfCapabilityTable,
       "h3cQoSIfCapabilityEntry": h3cQoSIfCapabilityEntry,
       "h3cQoSIfCapIfIndex": h3cQoSIfCapIfIndex,
       "h3cQoSIfCapModuleIndex": h3cQoSIfCapModuleIndex,
       "h3cQoSIfCapCharacteristicsIndex": h3cQoSIfCapCharacteristicsIndex,
       "h3cQoSIfCapCharacteristicsValue": h3cQoSIfCapCharacteristicsValue}
)
