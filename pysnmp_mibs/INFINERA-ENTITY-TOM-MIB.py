# SNMP MIB module (INFINERA-ENTITY-TOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-TOM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:52 2025
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

(InfnEqptType,
 InfnPhyMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType",
    "InfnPhyMode")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

tomMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TomTable_Object = MibTable
tomTable = _TomTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tomTable.setStatus("current")
_TomEntry_Object = MibTableRow
tomEntry = _TomEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1)
)
tomEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tomEntry.setStatus("current")
_TomMoId_Type = DisplayString
_TomMoId_Object = MibTableColumn
tomMoId = _TomMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 1),
    _TomMoId_Type()
)
tomMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tomMoId.setStatus("current")
_TomProvEqptType_Type = InfnEqptType
_TomProvEqptType_Object = MibTableColumn
tomProvEqptType = _TomProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 2),
    _TomProvEqptType_Type()
)
tomProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomProvEqptType.setStatus("current")


class _TomSFPState_Type(Integer32):
    """Custom type tomSFPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("maintenance", 2),
          ("unlocked", 3))
    )


_TomSFPState_Type.__name__ = "Integer32"
_TomSFPState_Object = MibTableColumn
tomSFPState = _TomSFPState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 3),
    _TomSFPState_Type()
)
tomSFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tomSFPState.setStatus("current")
_TomTxPowerThresholdPcentge_Type = Unsigned32
_TomTxPowerThresholdPcentge_Object = MibTableColumn
tomTxPowerThresholdPcentge = _TomTxPowerThresholdPcentge_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 4),
    _TomTxPowerThresholdPcentge_Type()
)
tomTxPowerThresholdPcentge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPowerThresholdPcentge.setStatus("current")
_TomRxPowerThresholdPcentge_Type = Unsigned32
_TomRxPowerThresholdPcentge_Object = MibTableColumn
tomRxPowerThresholdPcentge = _TomRxPowerThresholdPcentge_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 5),
    _TomRxPowerThresholdPcentge_Type()
)
tomRxPowerThresholdPcentge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRxPowerThresholdPcentge.setStatus("current")
_TomProvisionedFrequency_Type = Unsigned32
_TomProvisionedFrequency_Object = MibTableColumn
tomProvisionedFrequency = _TomProvisionedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 6),
    _TomProvisionedFrequency_Type()
)
tomProvisionedFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomProvisionedFrequency.setStatus("current")
_TomInstalledFrequency_Type = Unsigned32
_TomInstalledFrequency_Object = MibTableColumn
tomInstalledFrequency = _TomInstalledFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 7),
    _TomInstalledFrequency_Type()
)
tomInstalledFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tomInstalledFrequency.setStatus("current")
_TomProvisionedWavelength_Type = Unsigned32
_TomProvisionedWavelength_Object = MibTableColumn
tomProvisionedWavelength = _TomProvisionedWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 8),
    _TomProvisionedWavelength_Type()
)
tomProvisionedWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tomProvisionedWavelength.setStatus("current")
_TomInstalledWavelength_Type = Unsigned32
_TomInstalledWavelength_Object = MibTableColumn
tomInstalledWavelength = _TomInstalledWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 9),
    _TomInstalledWavelength_Type()
)
tomInstalledWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tomInstalledWavelength.setStatus("current")
_TomPhyMode_Type = InfnPhyMode
_TomPhyMode_Object = MibTableColumn
tomPhyMode = _TomPhyMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 10),
    _TomPhyMode_Type()
)
tomPhyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomPhyMode.setStatus("current")
_TomSerdesOverride_Type = TruthValue
_TomSerdesOverride_Object = MibTableColumn
tomSerdesOverride = _TomSerdesOverride_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 11),
    _TomSerdesOverride_Type()
)
tomSerdesOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomSerdesOverride.setStatus("current")
_TomTxAmplitude_Type = Integer32
_TomTxAmplitude_Object = MibTableColumn
tomTxAmplitude = _TomTxAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 12),
    _TomTxAmplitude_Type()
)
tomTxAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxAmplitude.setStatus("current")
_TomTxVod_Type = Integer32
_TomTxVod_Object = MibTableColumn
tomTxVod = _TomTxVod_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 13),
    _TomTxVod_Type()
)
tomTxVod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxVod.setStatus("current")
_TomTxPost1_Type = Integer32
_TomTxPost1_Object = MibTableColumn
tomTxPost1 = _TomTxPost1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 14),
    _TomTxPost1_Type()
)
tomTxPost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPost1.setStatus("current")
_TomTxPost2_Type = Integer32
_TomTxPost2_Object = MibTableColumn
tomTxPost2 = _TomTxPost2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 15),
    _TomTxPost2_Type()
)
tomTxPost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPost2.setStatus("current")
_TomTxPre_Type = Integer32
_TomTxPre_Object = MibTableColumn
tomTxPre = _TomTxPre_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 16),
    _TomTxPre_Type()
)
tomTxPre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPre.setStatus("current")
_TomTxIDrv_Type = Integer32
_TomTxIDrv_Object = MibTableColumn
tomTxIDrv = _TomTxIDrv_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 17),
    _TomTxIDrv_Type()
)
tomTxIDrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxIDrv.setStatus("current")
_TomTxIPreDrv_Type = Integer32
_TomTxIPreDrv_Object = MibTableColumn
tomTxIPreDrv = _TomTxIPreDrv_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 18),
    _TomTxIPreDrv_Type()
)
tomTxIPreDrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxIPreDrv.setStatus("current")
_TomTxPoshUp_Type = Integer32
_TomTxPoshUp_Object = MibTableColumn
tomTxPoshUp = _TomTxPoshUp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 19),
    _TomTxPoshUp_Type()
)
tomTxPoshUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPoshUp.setStatus("current")
_TomTxPoshDn_Type = Integer32
_TomTxPoshDn_Object = MibTableColumn
tomTxPoshDn = _TomTxPoshDn_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 20),
    _TomTxPoshDn_Type()
)
tomTxPoshDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPoshDn.setStatus("current")
_TomTxPost3_Type = Integer32
_TomTxPost3_Object = MibTableColumn
tomTxPost3 = _TomTxPost3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 21),
    _TomTxPost3_Type()
)
tomTxPost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxPost3.setStatus("current")
_TomTxEq_Type = Integer32
_TomTxEq_Object = MibTableColumn
tomTxEq = _TomTxEq_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 22),
    _TomTxEq_Type()
)
tomTxEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTxEq.setStatus("current")
_TomTx12Eq_Type = Integer32
_TomTx12Eq_Object = MibTableColumn
tomTx12Eq = _TomTx12Eq_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 23),
    _TomTx12Eq_Type()
)
tomTx12Eq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTx12Eq.setStatus("current")
_TomTx34Eq_Type = Integer32
_TomTx34Eq_Object = MibTableColumn
tomTx34Eq = _TomTx34Eq_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 24),
    _TomTx34Eq_Type()
)
tomTx34Eq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomTx34Eq.setStatus("current")
_TomRx12Emphasis_Type = Integer32
_TomRx12Emphasis_Object = MibTableColumn
tomRx12Emphasis = _TomRx12Emphasis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 25),
    _TomRx12Emphasis_Type()
)
tomRx12Emphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRx12Emphasis.setStatus("current")
_TomRx34Emphasis_Type = Integer32
_TomRx34Emphasis_Object = MibTableColumn
tomRx34Emphasis = _TomRx34Emphasis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 26),
    _TomRx34Emphasis_Type()
)
tomRx34Emphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRx34Emphasis.setStatus("current")
_TomRx12Amplitude_Type = Integer32
_TomRx12Amplitude_Object = MibTableColumn
tomRx12Amplitude = _TomRx12Amplitude_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 27),
    _TomRx12Amplitude_Type()
)
tomRx12Amplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRx12Amplitude.setStatus("current")
_TomRx34Amplitude_Type = Integer32
_TomRx34Amplitude_Object = MibTableColumn
tomRx34Amplitude = _TomRx34Amplitude_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 28),
    _TomRx34Amplitude_Type()
)
tomRx34Amplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRx34Amplitude.setStatus("current")
_TomHighPowerEnable_Type = TruthValue
_TomHighPowerEnable_Object = MibTableColumn
tomHighPowerEnable = _TomHighPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 29),
    _TomHighPowerEnable_Type()
)
tomHighPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomHighPowerEnable.setStatus("current")
_TomRxCtleOverride_Type = TruthValue
_TomRxCtleOverride_Object = MibTableColumn
tomRxCtleOverride = _TomRxCtleOverride_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 30),
    _TomRxCtleOverride_Type()
)
tomRxCtleOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRxCtleOverride.setStatus("current")
_TomRxCtleEqValue_Type = Integer32
_TomRxCtleEqValue_Object = MibTableColumn
tomRxCtleEqValue = _TomRxCtleEqValue_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 31),
    _TomRxCtleEqValue_Type()
)
tomRxCtleEqValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tomRxCtleEqValue.setStatus("current")
_TomIs3rdPartyTom_Type = TruthValue
_TomIs3rdPartyTom_Object = MibTableColumn
tomIs3rdPartyTom = _TomIs3rdPartyTom_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 1, 1, 32),
    _TomIs3rdPartyTom_Type()
)
tomIs3rdPartyTom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tomIs3rdPartyTom.setStatus("current")
_TomConformance_ObjectIdentity = ObjectIdentity
tomConformance = _TomConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 3)
)
_TomCompliances_ObjectIdentity = ObjectIdentity
tomCompliances = _TomCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 3, 1)
)
_TomGroups_ObjectIdentity = ObjectIdentity
tomGroups = _TomGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 3, 2)
)

# Managed Objects groups

tomGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 3, 2, 1)
)
tomGroup.setObjects(
      *(("INFINERA-ENTITY-TOM-MIB", "tomInstalledFrequency"),
        ("INFINERA-ENTITY-TOM-MIB", "tomMoId"),
        ("INFINERA-ENTITY-TOM-MIB", "tomProvEqptType"),
        ("INFINERA-ENTITY-TOM-MIB", "tomSFPState"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPowerThresholdPcentge"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRxPowerThresholdPcentge"),
        ("INFINERA-ENTITY-TOM-MIB", "tomProvisionedFrequency"),
        ("INFINERA-ENTITY-TOM-MIB", "tomProvisionedWavelength"),
        ("INFINERA-ENTITY-TOM-MIB", "tomInstalledWavelength"),
        ("INFINERA-ENTITY-TOM-MIB", "tomPhyMode"),
        ("INFINERA-ENTITY-TOM-MIB", "tomSerdesOverride"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxAmplitude"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxVod"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPost1"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPost2"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPre"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxIDrv"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxIPreDrv"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPoshUp"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPoshDn"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxPost3"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTxEq"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTx12Eq"),
        ("INFINERA-ENTITY-TOM-MIB", "tomTx34Eq"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRx12Emphasis"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRx34Emphasis"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRx12Amplitude"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRx34Amplitude"),
        ("INFINERA-ENTITY-TOM-MIB", "tomHighPowerEnable"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRxCtleOverride"),
        ("INFINERA-ENTITY-TOM-MIB", "tomRxCtleEqValue"),
        ("INFINERA-ENTITY-TOM-MIB", "tomIs3rdPartyTom"))
)
if mibBuilder.loadTexts:
    tomGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tomCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 9, 3, 1, 1)
)
tomCompliance.setObjects(
    ("INFINERA-ENTITY-TOM-MIB", "tomGroup")
)
if mibBuilder.loadTexts:
    tomCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-TOM-MIB",
    **{"tomMIB": tomMIB,
       "tomTable": tomTable,
       "tomEntry": tomEntry,
       "tomMoId": tomMoId,
       "tomProvEqptType": tomProvEqptType,
       "tomSFPState": tomSFPState,
       "tomTxPowerThresholdPcentge": tomTxPowerThresholdPcentge,
       "tomRxPowerThresholdPcentge": tomRxPowerThresholdPcentge,
       "tomProvisionedFrequency": tomProvisionedFrequency,
       "tomInstalledFrequency": tomInstalledFrequency,
       "tomProvisionedWavelength": tomProvisionedWavelength,
       "tomInstalledWavelength": tomInstalledWavelength,
       "tomPhyMode": tomPhyMode,
       "tomSerdesOverride": tomSerdesOverride,
       "tomTxAmplitude": tomTxAmplitude,
       "tomTxVod": tomTxVod,
       "tomTxPost1": tomTxPost1,
       "tomTxPost2": tomTxPost2,
       "tomTxPre": tomTxPre,
       "tomTxIDrv": tomTxIDrv,
       "tomTxIPreDrv": tomTxIPreDrv,
       "tomTxPoshUp": tomTxPoshUp,
       "tomTxPoshDn": tomTxPoshDn,
       "tomTxPost3": tomTxPost3,
       "tomTxEq": tomTxEq,
       "tomTx12Eq": tomTx12Eq,
       "tomTx34Eq": tomTx34Eq,
       "tomRx12Emphasis": tomRx12Emphasis,
       "tomRx34Emphasis": tomRx34Emphasis,
       "tomRx12Amplitude": tomRx12Amplitude,
       "tomRx34Amplitude": tomRx34Amplitude,
       "tomHighPowerEnable": tomHighPowerEnable,
       "tomRxCtleOverride": tomRxCtleOverride,
       "tomRxCtleEqValue": tomRxCtleEqValue,
       "tomIs3rdPartyTom": tomIs3rdPartyTom,
       "tomConformance": tomConformance,
       "tomCompliances": tomCompliances,
       "tomCompliance": tomCompliance,
       "tomGroups": tomGroups,
       "tomGroup": tomGroup}
)
