# SNMP MIB module (INFINERA-ENTITY-OFIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OFIM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:56 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatTenths,
 InfnEnforcementMode,
 InfnEqptType,
 InfnOtnOtuType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEnforcementMode",
    "InfnEqptType",
    "InfnOtnOtuType")

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

ofimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfimTable_Object = MibTable
ofimTable = _OfimTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1)
)
if mibBuilder.loadTexts:
    ofimTable.setStatus("current")
_OfimEntry_Object = MibTableRow
ofimEntry = _OfimEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1)
)
ofimEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ofimEntry.setStatus("current")
_OfimMoId_Type = DisplayString
_OfimMoId_Object = MibTableColumn
ofimMoId = _OfimMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 1),
    _OfimMoId_Type()
)
ofimMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimMoId.setStatus("current")
_OfimProvEqptType_Type = InfnEqptType
_OfimProvEqptType_Object = MibTableColumn
ofimProvEqptType = _OfimProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 2),
    _OfimProvEqptType_Type()
)
ofimProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimProvEqptType.setStatus("current")
_OfimOTNContainerRepresentation_Type = InfnOtnOtuType
_OfimOTNContainerRepresentation_Object = MibTableColumn
ofimOTNContainerRepresentation = _OfimOTNContainerRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 3),
    _OfimOTNContainerRepresentation_Type()
)
ofimOTNContainerRepresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimOTNContainerRepresentation.setStatus("current")
_OfimPicDspVer_Type = DisplayString
_OfimPicDspVer_Object = MibTableColumn
ofimPicDspVer = _OfimPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 4),
    _OfimPicDspVer_Type()
)
ofimPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofimPicDspVer.setStatus("current")
_OfimMaxFruGain_Type = FloatTenths
_OfimMaxFruGain_Object = MibTableColumn
ofimMaxFruGain = _OfimMaxFruGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 5),
    _OfimMaxFruGain_Type()
)
ofimMaxFruGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofimMaxFruGain.setStatus("current")
_OfimRecommendedGain_Type = FloatTenths
_OfimRecommendedGain_Object = MibTableColumn
ofimRecommendedGain = _OfimRecommendedGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 6),
    _OfimRecommendedGain_Type()
)
ofimRecommendedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofimRecommendedGain.setStatus("current")
_OfimRxEdfaOutputPowerTarget_Type = FloatTenths
_OfimRxEdfaOutputPowerTarget_Object = MibTableColumn
ofimRxEdfaOutputPowerTarget = _OfimRxEdfaOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 7),
    _OfimRxEdfaOutputPowerTarget_Type()
)
ofimRxEdfaOutputPowerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofimRxEdfaOutputPowerTarget.setStatus("current")
_OfimRxEdfaGain_Type = FloatTenths
_OfimRxEdfaGain_Object = MibTableColumn
ofimRxEdfaGain = _OfimRxEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 8),
    _OfimRxEdfaGain_Type()
)
ofimRxEdfaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimRxEdfaGain.setStatus("current")
_OfimBwQmax_Type = FloatTenths
_OfimBwQmax_Object = MibTableColumn
ofimBwQmax = _OfimBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 9),
    _OfimBwQmax_Type()
)
ofimBwQmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimBwQmax.setStatus("current")
_OfimBwQused_Type = FloatTenths
_OfimBwQused_Object = MibTableColumn
ofimBwQused = _OfimBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 10),
    _OfimBwQused_Type()
)
ofimBwQused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimBwQused.setStatus("current")
_OfimBwBmax_Type = FloatTenths
_OfimBwBmax_Object = MibTableColumn
ofimBwBmax = _OfimBwBmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 11),
    _OfimBwBmax_Type()
)
ofimBwBmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimBwBmax.setStatus("current")
_OfimBwBused_Type = FloatTenths
_OfimBwBused_Object = MibTableColumn
ofimBwBused = _OfimBwBused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 12),
    _OfimBwBused_Type()
)
ofimBwBused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimBwBused.setStatus("current")
_OfimBwUsgWaterMarkGranularity_Type = FloatTenths
_OfimBwUsgWaterMarkGranularity_Object = MibTableColumn
ofimBwUsgWaterMarkGranularity = _OfimBwUsgWaterMarkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 13),
    _OfimBwUsgWaterMarkGranularity_Type()
)
ofimBwUsgWaterMarkGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofimBwUsgWaterMarkGranularity.setStatus("current")
_OfimAvailableTunableSuperChNumbers_Type = DisplayString
_OfimAvailableTunableSuperChNumbers_Object = MibTableColumn
ofimAvailableTunableSuperChNumbers = _OfimAvailableTunableSuperChNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 1, 1, 14),
    _OfimAvailableTunableSuperChNumbers_Type()
)
ofimAvailableTunableSuperChNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofimAvailableTunableSuperChNumbers.setStatus("current")
_OfimConformance_ObjectIdentity = ObjectIdentity
ofimConformance = _OfimConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 3)
)
_OfimCompliances_ObjectIdentity = ObjectIdentity
ofimCompliances = _OfimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 3, 1)
)
_OfimGroups_ObjectIdentity = ObjectIdentity
ofimGroups = _OfimGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 3, 2)
)

# Managed Objects groups

ofimGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 3, 2, 1)
)
ofimGroup.setObjects(
      *(("INFINERA-ENTITY-OFIM-MIB", "ofimMoId"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimProvEqptType"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimPicDspVer"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimMaxFruGain"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimRxEdfaOutputPowerTarget"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimRxEdfaGain"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimOTNContainerRepresentation"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimRecommendedGain"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimBwQmax"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimBwQused"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimBwBmax"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimBwBused"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimBwUsgWaterMarkGranularity"),
        ("INFINERA-ENTITY-OFIM-MIB", "ofimAvailableTunableSuperChNumbers"))
)
if mibBuilder.loadTexts:
    ofimGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ofimCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 44, 3, 1, 1)
)
ofimCompliance.setObjects(
    ("INFINERA-ENTITY-OFIM-MIB", "ofimGroup")
)
if mibBuilder.loadTexts:
    ofimCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OFIM-MIB",
    **{"ofimMIB": ofimMIB,
       "ofimTable": ofimTable,
       "ofimEntry": ofimEntry,
       "ofimMoId": ofimMoId,
       "ofimProvEqptType": ofimProvEqptType,
       "ofimOTNContainerRepresentation": ofimOTNContainerRepresentation,
       "ofimPicDspVer": ofimPicDspVer,
       "ofimMaxFruGain": ofimMaxFruGain,
       "ofimRecommendedGain": ofimRecommendedGain,
       "ofimRxEdfaOutputPowerTarget": ofimRxEdfaOutputPowerTarget,
       "ofimRxEdfaGain": ofimRxEdfaGain,
       "ofimBwQmax": ofimBwQmax,
       "ofimBwQused": ofimBwQused,
       "ofimBwBmax": ofimBwBmax,
       "ofimBwBused": ofimBwBused,
       "ofimBwUsgWaterMarkGranularity": ofimBwUsgWaterMarkGranularity,
       "ofimAvailableTunableSuperChNumbers": ofimAvailableTunableSuperChNumbers,
       "ofimConformance": ofimConformance,
       "ofimCompliances": ofimCompliances,
       "ofimCompliance": ofimCompliance,
       "ofimGroups": ofimGroups,
       "ofimGroup": ofimGroup}
)
