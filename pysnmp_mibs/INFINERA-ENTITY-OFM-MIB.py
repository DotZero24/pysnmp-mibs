# SNMP MIB module (INFINERA-ENTITY-OFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:32 2025
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
 InfnEqptType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEqptType")

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

ofmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfmTable_Object = MibTable
ofmTable = _OfmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1)
)
if mibBuilder.loadTexts:
    ofmTable.setStatus("current")
_OfmEntry_Object = MibTableRow
ofmEntry = _OfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1)
)
ofmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ofmEntry.setStatus("current")
_OfmMoId_Type = DisplayString
_OfmMoId_Object = MibTableColumn
ofmMoId = _OfmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 1),
    _OfmMoId_Type()
)
ofmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmMoId.setStatus("current")
_OfmProvEqptType_Type = InfnEqptType
_OfmProvEqptType_Object = MibTableColumn
ofmProvEqptType = _OfmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 2),
    _OfmProvEqptType_Type()
)
ofmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmProvEqptType.setStatus("current")


class _OfmOTNContainerRepresentation_Type(Integer32):
    """Custom type ofmOTNContainerRepresentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("otuKi", 1),
          ("otuAdapti", 2))
    )


_OfmOTNContainerRepresentation_Type.__name__ = "Integer32"
_OfmOTNContainerRepresentation_Object = MibTableColumn
ofmOTNContainerRepresentation = _OfmOTNContainerRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 3),
    _OfmOTNContainerRepresentation_Type()
)
ofmOTNContainerRepresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmOTNContainerRepresentation.setStatus("current")
_OfmActvTimingSource_Type = DisplayString
_OfmActvTimingSource_Object = MibTableColumn
ofmActvTimingSource = _OfmActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 4),
    _OfmActvTimingSource_Type()
)
ofmActvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmActvTimingSource.setStatus("current")
_OfmPicDspVer_Type = DisplayString
_OfmPicDspVer_Object = MibTableColumn
ofmPicDspVer = _OfmPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 5),
    _OfmPicDspVer_Type()
)
ofmPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmPicDspVer.setStatus("current")
_OfmMaxFruGain_Type = FloatTenths
_OfmMaxFruGain_Object = MibTableColumn
ofmMaxFruGain = _OfmMaxFruGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 6),
    _OfmMaxFruGain_Type()
)
ofmMaxFruGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmMaxFruGain.setStatus("current")
_OfmRecommendedGain_Type = FloatTenths
_OfmRecommendedGain_Object = MibTableColumn
ofmRecommendedGain = _OfmRecommendedGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 7),
    _OfmRecommendedGain_Type()
)
ofmRecommendedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmRecommendedGain.setStatus("current")
_OfmRxEdfaOutputPowerTarget_Type = FloatTenths
_OfmRxEdfaOutputPowerTarget_Object = MibTableColumn
ofmRxEdfaOutputPowerTarget = _OfmRxEdfaOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 8),
    _OfmRxEdfaOutputPowerTarget_Type()
)
ofmRxEdfaOutputPowerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmRxEdfaOutputPowerTarget.setStatus("current")
_OfmRxEdfaGain_Type = FloatTenths
_OfmRxEdfaGain_Object = MibTableColumn
ofmRxEdfaGain = _OfmRxEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 9),
    _OfmRxEdfaGain_Type()
)
ofmRxEdfaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmRxEdfaGain.setStatus("current")
_OfmBwQmax_Type = FloatTenths
_OfmBwQmax_Object = MibTableColumn
ofmBwQmax = _OfmBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 10),
    _OfmBwQmax_Type()
)
ofmBwQmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwQmax.setStatus("current")
_OfmBwQused_Type = FloatTenths
_OfmBwQused_Object = MibTableColumn
ofmBwQused = _OfmBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 11),
    _OfmBwQused_Type()
)
ofmBwQused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwQused.setStatus("current")
_OfmBwQlicensed_Type = FloatTenths
_OfmBwQlicensed_Object = MibTableColumn
ofmBwQlicensed = _OfmBwQlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 12),
    _OfmBwQlicensed_Type()
)
ofmBwQlicensed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwQlicensed.setStatus("current")
_OfmBwBmax_Type = FloatTenths
_OfmBwBmax_Object = MibTableColumn
ofmBwBmax = _OfmBwBmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 13),
    _OfmBwBmax_Type()
)
ofmBwBmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwBmax.setStatus("current")
_OfmBwBused_Type = FloatTenths
_OfmBwBused_Object = MibTableColumn
ofmBwBused = _OfmBwBused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 14),
    _OfmBwBused_Type()
)
ofmBwBused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwBused.setStatus("current")
_OfmBwBlicensed_Type = FloatTenths
_OfmBwBlicensed_Object = MibTableColumn
ofmBwBlicensed = _OfmBwBlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 15),
    _OfmBwBlicensed_Type()
)
ofmBwBlicensed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwBlicensed.setStatus("current")
_OfmLicensedServicesDisabled_Type = Integer32
_OfmLicensedServicesDisabled_Object = MibTableColumn
ofmLicensedServicesDisabled = _OfmLicensedServicesDisabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 16),
    _OfmLicensedServicesDisabled_Type()
)
ofmLicensedServicesDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmLicensedServicesDisabled.setStatus("current")


class _OfmLicenseEnforced_Type(Integer32):
    """Custom type ofmLicenseEnforced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notEnforced", 2),
          ("enforced", 3))
    )


_OfmLicenseEnforced_Type.__name__ = "Integer32"
_OfmLicenseEnforced_Object = MibTableColumn
ofmLicenseEnforced = _OfmLicenseEnforced_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 17),
    _OfmLicenseEnforced_Type()
)
ofmLicenseEnforced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmLicenseEnforced.setStatus("current")


class _OfmDefFlexLicModFormat_Type(Integer32):
    """Custom type ofmDefFlexLicModFormat based on Integer32"""
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
        *(("unknown", 1),
          ("qpsk", 2),
          ("bpsk", 3),
          ("pm3qam", 4))
    )


_OfmDefFlexLicModFormat_Type.__name__ = "Integer32"
_OfmDefFlexLicModFormat_Object = MibTableColumn
ofmDefFlexLicModFormat = _OfmDefFlexLicModFormat_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 18),
    _OfmDefFlexLicModFormat_Type()
)
ofmDefFlexLicModFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmDefFlexLicModFormat.setStatus("current")
_OfmBwUsgWaterMarkGranularity_Type = FloatTenths
_OfmBwUsgWaterMarkGranularity_Object = MibTableColumn
ofmBwUsgWaterMarkGranularity = _OfmBwUsgWaterMarkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 19),
    _OfmBwUsgWaterMarkGranularity_Type()
)
ofmBwUsgWaterMarkGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofmBwUsgWaterMarkGranularity.setStatus("current")
_OfmAvailableTunableSuperChNumbers_Type = DisplayString
_OfmAvailableTunableSuperChNumbers_Object = MibTableColumn
ofmAvailableTunableSuperChNumbers = _OfmAvailableTunableSuperChNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 1, 1, 20),
    _OfmAvailableTunableSuperChNumbers_Type()
)
ofmAvailableTunableSuperChNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofmAvailableTunableSuperChNumbers.setStatus("current")
_OfmConformance_ObjectIdentity = ObjectIdentity
ofmConformance = _OfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 3)
)
_OfmCompliances_ObjectIdentity = ObjectIdentity
ofmCompliances = _OfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 3, 1)
)
_OfmGroups_ObjectIdentity = ObjectIdentity
ofmGroups = _OfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 3, 2)
)

# Managed Objects groups

ofmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 3, 2, 1)
)
ofmGroup.setObjects(
      *(("INFINERA-ENTITY-OFM-MIB", "ofmMoId"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmProvEqptType"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmActvTimingSource"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmPicDspVer"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmMaxFruGain"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmRxEdfaOutputPowerTarget"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmRxEdfaGain"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmOTNContainerRepresentation"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmRecommendedGain"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwQmax"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwQused"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwQlicensed"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwBmax"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwBused"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwBlicensed"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmLicensedServicesDisabled"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmLicenseEnforced"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmDefFlexLicModFormat"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmBwUsgWaterMarkGranularity"),
        ("INFINERA-ENTITY-OFM-MIB", "ofmAvailableTunableSuperChNumbers"))
)
if mibBuilder.loadTexts:
    ofmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ofmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 40, 3, 1, 1)
)
ofmCompliance.setObjects(
    ("INFINERA-ENTITY-OFM-MIB", "ofmGroup")
)
if mibBuilder.loadTexts:
    ofmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OFM-MIB",
    **{"ofmMIB": ofmMIB,
       "ofmTable": ofmTable,
       "ofmEntry": ofmEntry,
       "ofmMoId": ofmMoId,
       "ofmProvEqptType": ofmProvEqptType,
       "ofmOTNContainerRepresentation": ofmOTNContainerRepresentation,
       "ofmActvTimingSource": ofmActvTimingSource,
       "ofmPicDspVer": ofmPicDspVer,
       "ofmMaxFruGain": ofmMaxFruGain,
       "ofmRecommendedGain": ofmRecommendedGain,
       "ofmRxEdfaOutputPowerTarget": ofmRxEdfaOutputPowerTarget,
       "ofmRxEdfaGain": ofmRxEdfaGain,
       "ofmBwQmax": ofmBwQmax,
       "ofmBwQused": ofmBwQused,
       "ofmBwQlicensed": ofmBwQlicensed,
       "ofmBwBmax": ofmBwBmax,
       "ofmBwBused": ofmBwBused,
       "ofmBwBlicensed": ofmBwBlicensed,
       "ofmLicensedServicesDisabled": ofmLicensedServicesDisabled,
       "ofmLicenseEnforced": ofmLicenseEnforced,
       "ofmDefFlexLicModFormat": ofmDefFlexLicModFormat,
       "ofmBwUsgWaterMarkGranularity": ofmBwUsgWaterMarkGranularity,
       "ofmAvailableTunableSuperChNumbers": ofmAvailableTunableSuperChNumbers,
       "ofmConformance": ofmConformance,
       "ofmCompliances": ofmCompliances,
       "ofmCompliance": ofmCompliance,
       "ofmGroups": ofmGroups,
       "ofmGroup": ofmGroup}
)
