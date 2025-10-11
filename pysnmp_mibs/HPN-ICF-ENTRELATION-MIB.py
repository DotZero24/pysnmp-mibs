# SNMP MIB module (HPN-ICF-ENTRELATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-ENTRELATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:21 2025
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfEntityRelation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfEntRelationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stackport", 1),
          ("comboport", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfEntRelationObjects_ObjectIdentity = ObjectIdentity
hpnicfEntRelationObjects = _HpnicfEntRelationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1)
)
_HpnicfEntRelation_ObjectIdentity = ObjectIdentity
hpnicfEntRelation = _HpnicfEntRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1)
)
_HpnicfEntRelationTable_Object = MibTable
hpnicfEntRelationTable = _HpnicfEntRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntRelationTable.setStatus("current")
_HpnicfEntRelationEntry_Object = MibTableRow
hpnicfEntRelationEntry = _HpnicfEntRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1)
)
hpnicfEntRelationEntry.setIndexNames(
    (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationType"),
    (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntityIndex"),
    (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEntRelationEntry.setStatus("current")
_HpnicfEntRelationType_Type = HpnicfEntRelationType
_HpnicfEntRelationType_Object = MibTableColumn
hpnicfEntRelationType = _HpnicfEntRelationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 1),
    _HpnicfEntRelationType_Type()
)
hpnicfEntRelationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEntRelationType.setStatus("current")
_HpnicfEntityIndex_Type = PhysicalIndex
_HpnicfEntityIndex_Object = MibTableColumn
hpnicfEntityIndex = _HpnicfEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 2),
    _HpnicfEntityIndex_Type()
)
hpnicfEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEntityIndex.setStatus("current")
_HpnicfRelatedEntityIndex_Type = PhysicalIndex
_HpnicfRelatedEntityIndex_Object = MibTableColumn
hpnicfRelatedEntityIndex = _HpnicfRelatedEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 3),
    _HpnicfRelatedEntityIndex_Type()
)
hpnicfRelatedEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRelatedEntityIndex.setStatus("current")
_HpnicfEntRelationConformance_ObjectIdentity = ObjectIdentity
hpnicfEntRelationConformance = _HpnicfEntRelationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2)
)
_HpnicfEntRelationCompliances_ObjectIdentity = ObjectIdentity
hpnicfEntRelationCompliances = _HpnicfEntRelationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1)
)
_HpnicfEntRelationGroups_ObjectIdentity = ObjectIdentity
hpnicfEntRelationGroups = _HpnicfEntRelationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2)
)

# Managed Objects groups

hpnicfEntRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2, 1)
)
hpnicfEntRelationGroup.setObjects(
    ("HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex")
)
if mibBuilder.loadTexts:
    hpnicfEntRelationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfEntRelationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1, 1)
)
hpnicfEntRelationCompliance.setObjects(
    ("HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationGroup")
)
if mibBuilder.loadTexts:
    hpnicfEntRelationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ENTRELATION-MIB",
    **{"HpnicfEntRelationType": HpnicfEntRelationType,
       "hpnicfEntityRelation": hpnicfEntityRelation,
       "hpnicfEntRelationObjects": hpnicfEntRelationObjects,
       "hpnicfEntRelation": hpnicfEntRelation,
       "hpnicfEntRelationTable": hpnicfEntRelationTable,
       "hpnicfEntRelationEntry": hpnicfEntRelationEntry,
       "hpnicfEntRelationType": hpnicfEntRelationType,
       "hpnicfEntityIndex": hpnicfEntityIndex,
       "hpnicfRelatedEntityIndex": hpnicfRelatedEntityIndex,
       "hpnicfEntRelationConformance": hpnicfEntRelationConformance,
       "hpnicfEntRelationCompliances": hpnicfEntRelationCompliances,
       "hpnicfEntRelationCompliance": hpnicfEntRelationCompliance,
       "hpnicfEntRelationGroups": hpnicfEntRelationGroups,
       "hpnicfEntRelationGroup": hpnicfEntRelationGroup}
)
