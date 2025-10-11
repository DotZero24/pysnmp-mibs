# SNMP MIB module (INFINERA-ENTITY-OFIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OFIX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:36 2025
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

ofixMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfixTable_Object = MibTable
ofixTable = _OfixTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1)
)
if mibBuilder.loadTexts:
    ofixTable.setStatus("current")
_OfixEntry_Object = MibTableRow
ofixEntry = _OfixEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1)
)
ofixEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ofixEntry.setStatus("current")
_OfixMoId_Type = DisplayString
_OfixMoId_Object = MibTableColumn
ofixMoId = _OfixMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 1),
    _OfixMoId_Type()
)
ofixMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixMoId.setStatus("current")
_OfixProvEqptType_Type = InfnEqptType
_OfixProvEqptType_Object = MibTableColumn
ofixProvEqptType = _OfixProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 2),
    _OfixProvEqptType_Type()
)
ofixProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixProvEqptType.setStatus("current")
_OfixOTNContainerRepresentation_Type = InfnOtnOtuType
_OfixOTNContainerRepresentation_Object = MibTableColumn
ofixOTNContainerRepresentation = _OfixOTNContainerRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 3),
    _OfixOTNContainerRepresentation_Type()
)
ofixOTNContainerRepresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixOTNContainerRepresentation.setStatus("current")
_OfixPicDspVer_Type = DisplayString
_OfixPicDspVer_Object = MibTableColumn
ofixPicDspVer = _OfixPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 4),
    _OfixPicDspVer_Type()
)
ofixPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofixPicDspVer.setStatus("current")
_OfixMaxFruGain_Type = FloatTenths
_OfixMaxFruGain_Object = MibTableColumn
ofixMaxFruGain = _OfixMaxFruGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 5),
    _OfixMaxFruGain_Type()
)
ofixMaxFruGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofixMaxFruGain.setStatus("current")
_OfixRecommendedGain_Type = FloatTenths
_OfixRecommendedGain_Object = MibTableColumn
ofixRecommendedGain = _OfixRecommendedGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 6),
    _OfixRecommendedGain_Type()
)
ofixRecommendedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofixRecommendedGain.setStatus("current")
_OfixRxEdfaOutputPowerTarget_Type = FloatTenths
_OfixRxEdfaOutputPowerTarget_Object = MibTableColumn
ofixRxEdfaOutputPowerTarget = _OfixRxEdfaOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 7),
    _OfixRxEdfaOutputPowerTarget_Type()
)
ofixRxEdfaOutputPowerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofixRxEdfaOutputPowerTarget.setStatus("current")
_OfixRxEdfaGain_Type = FloatTenths
_OfixRxEdfaGain_Object = MibTableColumn
ofixRxEdfaGain = _OfixRxEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 8),
    _OfixRxEdfaGain_Type()
)
ofixRxEdfaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixRxEdfaGain.setStatus("current")
_OfixBwQmax_Type = FloatTenths
_OfixBwQmax_Object = MibTableColumn
ofixBwQmax = _OfixBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 9),
    _OfixBwQmax_Type()
)
ofixBwQmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixBwQmax.setStatus("current")
_OfixBwQused_Type = FloatTenths
_OfixBwQused_Object = MibTableColumn
ofixBwQused = _OfixBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 10),
    _OfixBwQused_Type()
)
ofixBwQused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixBwQused.setStatus("current")
_OfixBwBmax_Type = FloatTenths
_OfixBwBmax_Object = MibTableColumn
ofixBwBmax = _OfixBwBmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 11),
    _OfixBwBmax_Type()
)
ofixBwBmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixBwBmax.setStatus("current")
_OfixBwBused_Type = FloatTenths
_OfixBwBused_Object = MibTableColumn
ofixBwBused = _OfixBwBused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 12),
    _OfixBwBused_Type()
)
ofixBwBused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixBwBused.setStatus("current")
_OfixBwUsgWaterMarkGranularity_Type = FloatTenths
_OfixBwUsgWaterMarkGranularity_Object = MibTableColumn
ofixBwUsgWaterMarkGranularity = _OfixBwUsgWaterMarkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 13),
    _OfixBwUsgWaterMarkGranularity_Type()
)
ofixBwUsgWaterMarkGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofixBwUsgWaterMarkGranularity.setStatus("current")
_OfixAvailableTunableSuperChNumbers_Type = DisplayString
_OfixAvailableTunableSuperChNumbers_Object = MibTableColumn
ofixAvailableTunableSuperChNumbers = _OfixAvailableTunableSuperChNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 1, 1, 14),
    _OfixAvailableTunableSuperChNumbers_Type()
)
ofixAvailableTunableSuperChNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofixAvailableTunableSuperChNumbers.setStatus("current")
_OfixConformance_ObjectIdentity = ObjectIdentity
ofixConformance = _OfixConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 3)
)
_OfixCompliances_ObjectIdentity = ObjectIdentity
ofixCompliances = _OfixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 3, 1)
)
_OfixGroups_ObjectIdentity = ObjectIdentity
ofixGroups = _OfixGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 3, 2)
)

# Managed Objects groups

ofixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 3, 2, 1)
)
ofixGroup.setObjects(
      *(("INFINERA-ENTITY-OFIX-MIB", "ofixMoId"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixProvEqptType"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixPicDspVer"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixMaxFruGain"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixRxEdfaOutputPowerTarget"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixRxEdfaGain"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixOTNContainerRepresentation"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixRecommendedGain"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixBwQmax"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixBwQused"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixBwBmax"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixBwBused"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixBwUsgWaterMarkGranularity"),
        ("INFINERA-ENTITY-OFIX-MIB", "ofixAvailableTunableSuperChNumbers"))
)
if mibBuilder.loadTexts:
    ofixGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ofixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 45, 3, 1, 1)
)
ofixCompliance.setObjects(
    ("INFINERA-ENTITY-OFIX-MIB", "ofixGroup")
)
if mibBuilder.loadTexts:
    ofixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OFIX-MIB",
    **{"ofixMIB": ofixMIB,
       "ofixTable": ofixTable,
       "ofixEntry": ofixEntry,
       "ofixMoId": ofixMoId,
       "ofixProvEqptType": ofixProvEqptType,
       "ofixOTNContainerRepresentation": ofixOTNContainerRepresentation,
       "ofixPicDspVer": ofixPicDspVer,
       "ofixMaxFruGain": ofixMaxFruGain,
       "ofixRecommendedGain": ofixRecommendedGain,
       "ofixRxEdfaOutputPowerTarget": ofixRxEdfaOutputPowerTarget,
       "ofixRxEdfaGain": ofixRxEdfaGain,
       "ofixBwQmax": ofixBwQmax,
       "ofixBwQused": ofixBwQused,
       "ofixBwBmax": ofixBwBmax,
       "ofixBwBused": ofixBwBused,
       "ofixBwUsgWaterMarkGranularity": ofixBwUsgWaterMarkGranularity,
       "ofixAvailableTunableSuperChNumbers": ofixAvailableTunableSuperChNumbers,
       "ofixConformance": ofixConformance,
       "ofixCompliances": ofixCompliances,
       "ofixCompliance": ofixCompliance,
       "ofixGroups": ofixGroups,
       "ofixGroup": ofixGroup}
)
