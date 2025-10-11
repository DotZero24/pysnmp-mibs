# SNMP MIB module (INFINERA-ENTITY-OLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OLM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:17 2025
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
 FloatThousandths,
 InfnAutoTunable,
 InfnChannelPlan,
 InfnEqptType,
 InfnOcgType,
 InfnOlmDefFlexLicModformat,
 InfnOperatingMode,
 InfnOtnOtuType,
 InfnSlteOpMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "FloatThousandths",
    "InfnAutoTunable",
    "InfnChannelPlan",
    "InfnEqptType",
    "InfnOcgType",
    "InfnOlmDefFlexLicModformat",
    "InfnOperatingMode",
    "InfnOtnOtuType",
    "InfnSlteOpMode")

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

olmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OlmTable_Object = MibTable
olmTable = _OlmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1)
)
if mibBuilder.loadTexts:
    olmTable.setStatus("current")
_OlmEntry_Object = MibTableRow
olmEntry = _OlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1)
)
olmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    olmEntry.setStatus("current")
_OlmMoId_Type = DisplayString
_OlmMoId_Object = MibTableColumn
olmMoId = _OlmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 1),
    _OlmMoId_Type()
)
olmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olmMoId.setStatus("current")
_OlmProvEqptType_Type = InfnEqptType
_OlmProvEqptType_Object = MibTableColumn
olmProvEqptType = _OlmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 2),
    _OlmProvEqptType_Type()
)
olmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olmProvEqptType.setStatus("current")


class _OlmOperatingMode_Type(InfnOperatingMode):
    """Custom type olmOperatingMode based on InfnOperatingMode"""
    defaultValue = 2


_OlmOperatingMode_Type.__name__ = "InfnOperatingMode"
_OlmOperatingMode_Object = MibTableColumn
olmOperatingMode = _OlmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 3),
    _OlmOperatingMode_Type()
)
olmOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmOperatingMode.setStatus("current")
_OlmAvailableTunableOcgNumbers_Type = Integer32
_OlmAvailableTunableOcgNumbers_Object = MibTableColumn
olmAvailableTunableOcgNumbers = _OlmAvailableTunableOcgNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 4),
    _OlmAvailableTunableOcgNumbers_Type()
)
olmAvailableTunableOcgNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmAvailableTunableOcgNumbers.setStatus("current")
_OlmTunableOcgNumber_Type = Integer32
_OlmTunableOcgNumber_Object = MibTableColumn
olmTunableOcgNumber = _OlmTunableOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 5),
    _OlmTunableOcgNumber_Type()
)
olmTunableOcgNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmTunableOcgNumber.setStatus("current")
_OlmCurOcgNumber_Type = Integer32
_OlmCurOcgNumber_Object = MibTableColumn
olmCurOcgNumber = _OlmCurOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 6),
    _OlmCurOcgNumber_Type()
)
olmCurOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmCurOcgNumber.setStatus("current")
_OlmPicDspVer_Type = DisplayString
_OlmPicDspVer_Object = MibTableColumn
olmPicDspVer = _OlmPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 7),
    _OlmPicDspVer_Type()
)
olmPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmPicDspVer.setStatus("current")
_OlmOcgNumber_Type = Integer32
_OlmOcgNumber_Object = MibTableColumn
olmOcgNumber = _OlmOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 8),
    _OlmOcgNumber_Type()
)
olmOcgNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olmOcgNumber.setStatus("current")
_OlmRowStatus_Type = RowStatus
_OlmRowStatus_Object = MibTableColumn
olmRowStatus = _OlmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 9),
    _OlmRowStatus_Type()
)
olmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olmRowStatus.setStatus("current")
_ActvTimingSource_Type = DisplayString
_ActvTimingSource_Object = MibTableColumn
actvTimingSource = _ActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 10),
    _ActvTimingSource_Type()
)
actvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvTimingSource.setStatus("current")
_OlmRxEdfaGain_Type = FloatTenths
_OlmRxEdfaGain_Object = MibTableColumn
olmRxEdfaGain = _OlmRxEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 11),
    _OlmRxEdfaGain_Type()
)
olmRxEdfaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmRxEdfaGain.setStatus("current")
_OlmRxEdfaOutputTargetPower_Type = FloatTenths
_OlmRxEdfaOutputTargetPower_Object = MibTableColumn
olmRxEdfaOutputTargetPower = _OlmRxEdfaOutputTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 12),
    _OlmRxEdfaOutputTargetPower_Type()
)
olmRxEdfaOutputTargetPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmRxEdfaOutputTargetPower.setStatus("current")
_OlmDefFlexLicModformat_Type = InfnOlmDefFlexLicModformat
_OlmDefFlexLicModformat_Object = MibTableColumn
olmDefFlexLicModformat = _OlmDefFlexLicModformat_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 13),
    _OlmDefFlexLicModformat_Type()
)
olmDefFlexLicModformat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmDefFlexLicModformat.setStatus("current")
_OlmBwQmax_Type = FloatThousandths
_OlmBwQmax_Object = MibTableColumn
olmBwQmax = _OlmBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 14),
    _OlmBwQmax_Type()
)
olmBwQmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmBwQmax.setStatus("current")
_OlmBwQused_Type = FloatThousandths
_OlmBwQused_Object = MibTableColumn
olmBwQused = _OlmBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 15),
    _OlmBwQused_Type()
)
olmBwQused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmBwQused.setStatus("current")
_OlmBwQlicensed_Type = FloatThousandths
_OlmBwQlicensed_Object = MibTableColumn
olmBwQlicensed = _OlmBwQlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 16),
    _OlmBwQlicensed_Type()
)
olmBwQlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmBwQlicensed.setStatus("current")
_OlmBwBmax_Type = FloatThousandths
_OlmBwBmax_Object = MibTableColumn
olmBwBmax = _OlmBwBmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 17),
    _OlmBwBmax_Type()
)
olmBwBmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmBwBmax.setStatus("current")
_OlmBwBused_Type = FloatThousandths
_OlmBwBused_Object = MibTableColumn
olmBwBused = _OlmBwBused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 18),
    _OlmBwBused_Type()
)
olmBwBused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmBwBused.setStatus("current")
_OlmBwBlicensed_Type = FloatThousandths
_OlmBwBlicensed_Object = MibTableColumn
olmBwBlicensed = _OlmBwBlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 19),
    _OlmBwBlicensed_Type()
)
olmBwBlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmBwBlicensed.setStatus("current")
_OlmOTNContainerRepresentation_Type = InfnOtnOtuType
_OlmOTNContainerRepresentation_Object = MibTableColumn
olmOTNContainerRepresentation = _OlmOTNContainerRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 20),
    _OlmOTNContainerRepresentation_Type()
)
olmOTNContainerRepresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmOTNContainerRepresentation.setStatus("current")
_OlmInstalledOTNContainerRepresentation_Type = InfnOtnOtuType
_OlmInstalledOTNContainerRepresentation_Object = MibTableColumn
olmInstalledOTNContainerRepresentation = _OlmInstalledOTNContainerRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 1, 1, 21),
    _OlmInstalledOTNContainerRepresentation_Type()
)
olmInstalledOTNContainerRepresentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmInstalledOTNContainerRepresentation.setStatus("current")
_OlmConformance_ObjectIdentity = ObjectIdentity
olmConformance = _OlmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 3)
)
_OlmCompliances_ObjectIdentity = ObjectIdentity
olmCompliances = _OlmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 3, 1)
)
_OlmGroups_ObjectIdentity = ObjectIdentity
olmGroups = _OlmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 3, 2)
)

# Managed Objects groups

olmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 3, 2, 1)
)
olmGroup.setObjects(
      *(("INFINERA-ENTITY-OLM-MIB", "olmMoId"),
        ("INFINERA-ENTITY-OLM-MIB", "olmProvEqptType"),
        ("INFINERA-ENTITY-OLM-MIB", "olmOperatingMode"),
        ("INFINERA-ENTITY-OLM-MIB", "olmAvailableTunableOcgNumbers"),
        ("INFINERA-ENTITY-OLM-MIB", "olmTunableOcgNumber"),
        ("INFINERA-ENTITY-OLM-MIB", "olmCurOcgNumber"),
        ("INFINERA-ENTITY-OLM-MIB", "olmPicDspVer"),
        ("INFINERA-ENTITY-OLM-MIB", "olmOcgNumber"),
        ("INFINERA-ENTITY-OLM-MIB", "olmRowStatus"),
        ("INFINERA-ENTITY-OLM-MIB", "actvTimingSource"),
        ("INFINERA-ENTITY-OLM-MIB", "olmRxEdfaGain"),
        ("INFINERA-ENTITY-OLM-MIB", "olmRxEdfaOutputTargetPower"),
        ("INFINERA-ENTITY-OLM-MIB", "olmDefFlexLicModformat"),
        ("INFINERA-ENTITY-OLM-MIB", "olmBwQmax"),
        ("INFINERA-ENTITY-OLM-MIB", "olmBwQused"),
        ("INFINERA-ENTITY-OLM-MIB", "olmBwQlicensed"),
        ("INFINERA-ENTITY-OLM-MIB", "olmBwBmax"),
        ("INFINERA-ENTITY-OLM-MIB", "olmBwBused"),
        ("INFINERA-ENTITY-OLM-MIB", "olmBwBlicensed"),
        ("INFINERA-ENTITY-OLM-MIB", "olmOTNContainerRepresentation"),
        ("INFINERA-ENTITY-OLM-MIB", "olmInstalledOTNContainerRepresentation"))
)
if mibBuilder.loadTexts:
    olmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

olmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 25, 3, 1, 1)
)
olmCompliance.setObjects(
    ("INFINERA-ENTITY-OLM-MIB", "olmGroup")
)
if mibBuilder.loadTexts:
    olmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OLM-MIB",
    **{"olmMIB": olmMIB,
       "olmTable": olmTable,
       "olmEntry": olmEntry,
       "olmMoId": olmMoId,
       "olmProvEqptType": olmProvEqptType,
       "olmOperatingMode": olmOperatingMode,
       "olmAvailableTunableOcgNumbers": olmAvailableTunableOcgNumbers,
       "olmTunableOcgNumber": olmTunableOcgNumber,
       "olmCurOcgNumber": olmCurOcgNumber,
       "olmPicDspVer": olmPicDspVer,
       "olmOcgNumber": olmOcgNumber,
       "olmRowStatus": olmRowStatus,
       "actvTimingSource": actvTimingSource,
       "olmRxEdfaGain": olmRxEdfaGain,
       "olmRxEdfaOutputTargetPower": olmRxEdfaOutputTargetPower,
       "olmDefFlexLicModformat": olmDefFlexLicModformat,
       "olmBwQmax": olmBwQmax,
       "olmBwQused": olmBwQused,
       "olmBwQlicensed": olmBwQlicensed,
       "olmBwBmax": olmBwBmax,
       "olmBwBused": olmBwBused,
       "olmBwBlicensed": olmBwBlicensed,
       "olmOTNContainerRepresentation": olmOTNContainerRepresentation,
       "olmInstalledOTNContainerRepresentation": olmInstalledOTNContainerRepresentation,
       "olmConformance": olmConformance,
       "olmCompliances": olmCompliances,
       "olmCompliance": olmCompliance,
       "olmGroups": olmGroups,
       "olmGroup": olmGroup}
)
