# SNMP MIB module (INFINERA-ENTITY-OFX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OFX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:36 2025
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
 InfnLicenseModulationType,
 InfnOtnOtuType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEnforcementMode",
    "InfnEqptType",
    "InfnLicenseModulationType",
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

ofxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfxTable_Object = MibTable
ofxTable = _OfxTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1)
)
if mibBuilder.loadTexts:
    ofxTable.setStatus("current")
_OfxEntry_Object = MibTableRow
ofxEntry = _OfxEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1)
)
ofxEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ofxEntry.setStatus("current")
_OfxMoId_Type = DisplayString
_OfxMoId_Object = MibTableColumn
ofxMoId = _OfxMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 1),
    _OfxMoId_Type()
)
ofxMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxMoId.setStatus("current")
_OfxProvEqptType_Type = InfnEqptType
_OfxProvEqptType_Object = MibTableColumn
ofxProvEqptType = _OfxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 2),
    _OfxProvEqptType_Type()
)
ofxProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxProvEqptType.setStatus("current")
_OfxOTNContainerRepresentation_Type = InfnOtnOtuType
_OfxOTNContainerRepresentation_Object = MibTableColumn
ofxOTNContainerRepresentation = _OfxOTNContainerRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 3),
    _OfxOTNContainerRepresentation_Type()
)
ofxOTNContainerRepresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxOTNContainerRepresentation.setStatus("current")
_OfxActvTimingSource_Type = DisplayString
_OfxActvTimingSource_Object = MibTableColumn
ofxActvTimingSource = _OfxActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 4),
    _OfxActvTimingSource_Type()
)
ofxActvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxActvTimingSource.setStatus("current")
_OfxPicDspVer_Type = DisplayString
_OfxPicDspVer_Object = MibTableColumn
ofxPicDspVer = _OfxPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 5),
    _OfxPicDspVer_Type()
)
ofxPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxPicDspVer.setStatus("current")
_OfxMaxFruGain_Type = FloatTenths
_OfxMaxFruGain_Object = MibTableColumn
ofxMaxFruGain = _OfxMaxFruGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 6),
    _OfxMaxFruGain_Type()
)
ofxMaxFruGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxMaxFruGain.setStatus("current")
_OfxRecommendedGain_Type = FloatTenths
_OfxRecommendedGain_Object = MibTableColumn
ofxRecommendedGain = _OfxRecommendedGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 7),
    _OfxRecommendedGain_Type()
)
ofxRecommendedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxRecommendedGain.setStatus("current")
_OfxRxEdfaOutputPowerTarget_Type = FloatTenths
_OfxRxEdfaOutputPowerTarget_Object = MibTableColumn
ofxRxEdfaOutputPowerTarget = _OfxRxEdfaOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 8),
    _OfxRxEdfaOutputPowerTarget_Type()
)
ofxRxEdfaOutputPowerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxRxEdfaOutputPowerTarget.setStatus("current")
_OfxRxEdfaGain_Type = FloatTenths
_OfxRxEdfaGain_Object = MibTableColumn
ofxRxEdfaGain = _OfxRxEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 9),
    _OfxRxEdfaGain_Type()
)
ofxRxEdfaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxRxEdfaGain.setStatus("current")
_OfxBwQmax_Type = FloatTenths
_OfxBwQmax_Object = MibTableColumn
ofxBwQmax = _OfxBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 10),
    _OfxBwQmax_Type()
)
ofxBwQmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxBwQmax.setStatus("current")
_OfxBwQused_Type = FloatTenths
_OfxBwQused_Object = MibTableColumn
ofxBwQused = _OfxBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 11),
    _OfxBwQused_Type()
)
ofxBwQused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxBwQused.setStatus("current")
_OfxBwQlicensed_Type = FloatTenths
_OfxBwQlicensed_Object = MibTableColumn
ofxBwQlicensed = _OfxBwQlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 12),
    _OfxBwQlicensed_Type()
)
ofxBwQlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxBwQlicensed.setStatus("current")
_OfxBwBmax_Type = FloatTenths
_OfxBwBmax_Object = MibTableColumn
ofxBwBmax = _OfxBwBmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 13),
    _OfxBwBmax_Type()
)
ofxBwBmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxBwBmax.setStatus("current")
_OfxBwBused_Type = FloatTenths
_OfxBwBused_Object = MibTableColumn
ofxBwBused = _OfxBwBused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 14),
    _OfxBwBused_Type()
)
ofxBwBused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxBwBused.setStatus("current")
_OfxBwBlicensed_Type = FloatTenths
_OfxBwBlicensed_Object = MibTableColumn
ofxBwBlicensed = _OfxBwBlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 15),
    _OfxBwBlicensed_Type()
)
ofxBwBlicensed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxBwBlicensed.setStatus("current")
_OfxLicensedServicesDisabled_Type = Integer32
_OfxLicensedServicesDisabled_Object = MibTableColumn
ofxLicensedServicesDisabled = _OfxLicensedServicesDisabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 16),
    _OfxLicensedServicesDisabled_Type()
)
ofxLicensedServicesDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxLicensedServicesDisabled.setStatus("current")
_OfxLicenseEnforced_Type = InfnEnforcementMode
_OfxLicenseEnforced_Object = MibTableColumn
ofxLicenseEnforced = _OfxLicenseEnforced_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 17),
    _OfxLicenseEnforced_Type()
)
ofxLicenseEnforced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxLicenseEnforced.setStatus("current")
_OfxDefFlexLicModFormat_Type = InfnLicenseModulationType
_OfxDefFlexLicModFormat_Object = MibTableColumn
ofxDefFlexLicModFormat = _OfxDefFlexLicModFormat_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 18),
    _OfxDefFlexLicModFormat_Type()
)
ofxDefFlexLicModFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxDefFlexLicModFormat.setStatus("current")
_OfxBwUsgWaterMarkGranularity_Type = FloatTenths
_OfxBwUsgWaterMarkGranularity_Object = MibTableColumn
ofxBwUsgWaterMarkGranularity = _OfxBwUsgWaterMarkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 19),
    _OfxBwUsgWaterMarkGranularity_Type()
)
ofxBwUsgWaterMarkGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxBwUsgWaterMarkGranularity.setStatus("current")
_OfxAvailableTunableSuperChNumbers_Type = DisplayString
_OfxAvailableTunableSuperChNumbers_Object = MibTableColumn
ofxAvailableTunableSuperChNumbers = _OfxAvailableTunableSuperChNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 20),
    _OfxAvailableTunableSuperChNumbers_Type()
)
ofxAvailableTunableSuperChNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxAvailableTunableSuperChNumbers.setStatus("current")
_OfxBw3Qmax_Type = FloatTenths
_OfxBw3Qmax_Object = MibTableColumn
ofxBw3Qmax = _OfxBw3Qmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 21),
    _OfxBw3Qmax_Type()
)
ofxBw3Qmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxBw3Qmax.setStatus("current")
_OfxBw3Qused_Type = FloatTenths
_OfxBw3Qused_Object = MibTableColumn
ofxBw3Qused = _OfxBw3Qused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 22),
    _OfxBw3Qused_Type()
)
ofxBw3Qused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxBw3Qused.setStatus("current")
_OfxBw3Qlicensed_Type = FloatTenths
_OfxBw3Qlicensed_Object = MibTableColumn
ofxBw3Qlicensed = _OfxBw3Qlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 1, 1, 23),
    _OfxBw3Qlicensed_Type()
)
ofxBw3Qlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxBw3Qlicensed.setStatus("current")
_OfxConformance_ObjectIdentity = ObjectIdentity
ofxConformance = _OfxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 3)
)
_OfxCompliances_ObjectIdentity = ObjectIdentity
ofxCompliances = _OfxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 3, 1)
)
_OfxGroups_ObjectIdentity = ObjectIdentity
ofxGroups = _OfxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 3, 2)
)

# Managed Objects groups

ofxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 3, 2, 1)
)
ofxGroup.setObjects(
      *(("INFINERA-ENTITY-OFX-MIB", "ofxMoId"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxProvEqptType"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxActvTimingSource"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxPicDspVer"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxMaxFruGain"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxRxEdfaOutputPowerTarget"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxRxEdfaGain"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxOTNContainerRepresentation"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxRecommendedGain"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwQmax"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwQused"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwQlicensed"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwBmax"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwBused"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwBlicensed"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxLicensedServicesDisabled"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxLicenseEnforced"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxDefFlexLicModFormat"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBwUsgWaterMarkGranularity"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxAvailableTunableSuperChNumbers"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBw3Qmax"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBw3Qused"),
        ("INFINERA-ENTITY-OFX-MIB", "ofxBw3Qlicensed"))
)
if mibBuilder.loadTexts:
    ofxGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ofxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 34, 3, 1, 1)
)
ofxCompliance.setObjects(
    ("INFINERA-ENTITY-OFX-MIB", "ofxGroup")
)
if mibBuilder.loadTexts:
    ofxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OFX-MIB",
    **{"ofxMIB": ofxMIB,
       "ofxTable": ofxTable,
       "ofxEntry": ofxEntry,
       "ofxMoId": ofxMoId,
       "ofxProvEqptType": ofxProvEqptType,
       "ofxOTNContainerRepresentation": ofxOTNContainerRepresentation,
       "ofxActvTimingSource": ofxActvTimingSource,
       "ofxPicDspVer": ofxPicDspVer,
       "ofxMaxFruGain": ofxMaxFruGain,
       "ofxRecommendedGain": ofxRecommendedGain,
       "ofxRxEdfaOutputPowerTarget": ofxRxEdfaOutputPowerTarget,
       "ofxRxEdfaGain": ofxRxEdfaGain,
       "ofxBwQmax": ofxBwQmax,
       "ofxBwQused": ofxBwQused,
       "ofxBwQlicensed": ofxBwQlicensed,
       "ofxBwBmax": ofxBwBmax,
       "ofxBwBused": ofxBwBused,
       "ofxBwBlicensed": ofxBwBlicensed,
       "ofxLicensedServicesDisabled": ofxLicensedServicesDisabled,
       "ofxLicenseEnforced": ofxLicenseEnforced,
       "ofxDefFlexLicModFormat": ofxDefFlexLicModFormat,
       "ofxBwUsgWaterMarkGranularity": ofxBwUsgWaterMarkGranularity,
       "ofxAvailableTunableSuperChNumbers": ofxAvailableTunableSuperChNumbers,
       "ofxBw3Qmax": ofxBw3Qmax,
       "ofxBw3Qused": ofxBw3Qused,
       "ofxBw3Qlicensed": ofxBw3Qlicensed,
       "ofxConformance": ofxConformance,
       "ofxCompliances": ofxCompliances,
       "ofxCompliance": ofxCompliance,
       "ofxGroups": ofxGroups,
       "ofxGroup": ofxGroup}
)
