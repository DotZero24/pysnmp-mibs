# SNMP MIB module (DeltaUPSv5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/delta/DeltaUPSv5-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:56:40 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2)
)
_Upsv5_ObjectIdentity = ObjectIdentity
upsv5 = _Upsv5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5)
)
_DupsIdent_ObjectIdentity = ObjectIdentity
dupsIdent = _DupsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1)
)


class _DupsIdentManufacturer_Type(DisplayString):
    """Custom type dupsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DupsIdentManufacturer_Type.__name__ = "DisplayString"
_DupsIdentManufacturer_Object = MibScalar
dupsIdentManufacturer = _DupsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 1),
    _DupsIdentManufacturer_Type()
)
dupsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentManufacturer.setStatus("mandatory")


class _DupsIdentModel_Type(DisplayString):
    """Custom type dupsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DupsIdentModel_Type.__name__ = "DisplayString"
_DupsIdentModel_Object = MibScalar
dupsIdentModel = _DupsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 2),
    _DupsIdentModel_Type()
)
dupsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentModel.setStatus("mandatory")


class _DupsIdentUPSSoftwareVersion_Type(DisplayString):
    """Custom type dupsIdentUPSSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DupsIdentUPSSoftwareVersion_Type.__name__ = "DisplayString"
_DupsIdentUPSSoftwareVersion_Object = MibScalar
dupsIdentUPSSoftwareVersion = _DupsIdentUPSSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 3),
    _DupsIdentUPSSoftwareVersion_Type()
)
dupsIdentUPSSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentUPSSoftwareVersion.setStatus("mandatory")


class _DupsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type dupsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DupsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_DupsIdentAgentSoftwareVersion_Object = MibScalar
dupsIdentAgentSoftwareVersion = _DupsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 4),
    _DupsIdentAgentSoftwareVersion_Type()
)
dupsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentAgentSoftwareVersion.setStatus("mandatory")


class _DupsIdentName_Type(DisplayString):
    """Custom type dupsIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DupsIdentName_Type.__name__ = "DisplayString"
_DupsIdentName_Object = MibScalar
dupsIdentName = _DupsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 5),
    _DupsIdentName_Type()
)
dupsIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsIdentName.setStatus("mandatory")


class _DupsAttachedDevices_Type(DisplayString):
    """Custom type dupsAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DupsAttachedDevices_Type.__name__ = "DisplayString"
_DupsAttachedDevices_Object = MibScalar
dupsAttachedDevices = _DupsAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 6),
    _DupsAttachedDevices_Type()
)
dupsAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsAttachedDevices.setStatus("mandatory")
_DupsRatingOutputVA_Type = Integer32
_DupsRatingOutputVA_Object = MibScalar
dupsRatingOutputVA = _DupsRatingOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 7),
    _DupsRatingOutputVA_Type()
)
dupsRatingOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingOutputVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsRatingOutputVA.setUnits("VA")
_DupsRatingOutputVoltage_Type = Integer32
_DupsRatingOutputVoltage_Object = MibScalar
dupsRatingOutputVoltage = _DupsRatingOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 8),
    _DupsRatingOutputVoltage_Type()
)
dupsRatingOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingOutputVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsRatingOutputVoltage.setUnits("Volt")
_DupsRatingOutputFrequency_Type = Integer32
_DupsRatingOutputFrequency_Object = MibScalar
dupsRatingOutputFrequency = _DupsRatingOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 9),
    _DupsRatingOutputFrequency_Type()
)
dupsRatingOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsRatingOutputFrequency.setUnits("Hz")
_DupsRatingInputVoltage_Type = Integer32
_DupsRatingInputVoltage_Object = MibScalar
dupsRatingInputVoltage = _DupsRatingInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 10),
    _DupsRatingInputVoltage_Type()
)
dupsRatingInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingInputVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsRatingInputVoltage.setUnits("Volt")
_DupsRatingInputFrequency_Type = Integer32
_DupsRatingInputFrequency_Object = MibScalar
dupsRatingInputFrequency = _DupsRatingInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 11),
    _DupsRatingInputFrequency_Type()
)
dupsRatingInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingInputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsRatingInputFrequency.setUnits("Hz")
_DupsRatingBatteryVoltage_Type = Integer32
_DupsRatingBatteryVoltage_Object = MibScalar
dupsRatingBatteryVoltage = _DupsRatingBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 12),
    _DupsRatingBatteryVoltage_Type()
)
dupsRatingBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingBatteryVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsRatingBatteryVoltage.setUnits("Volt")
_DupsLowTransferVoltUpBound_Type = Integer32
_DupsLowTransferVoltUpBound_Object = MibScalar
dupsLowTransferVoltUpBound = _DupsLowTransferVoltUpBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 13),
    _DupsLowTransferVoltUpBound_Type()
)
dupsLowTransferVoltUpBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLowTransferVoltUpBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsLowTransferVoltUpBound.setUnits("Volt")
_DupsLowTransferVoltLowBound_Type = Integer32
_DupsLowTransferVoltLowBound_Object = MibScalar
dupsLowTransferVoltLowBound = _DupsLowTransferVoltLowBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 14),
    _DupsLowTransferVoltLowBound_Type()
)
dupsLowTransferVoltLowBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLowTransferVoltLowBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsLowTransferVoltLowBound.setUnits("Volt")
_DupsHighTransferVoltUpBound_Type = Integer32
_DupsHighTransferVoltUpBound_Object = MibScalar
dupsHighTransferVoltUpBound = _DupsHighTransferVoltUpBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 15),
    _DupsHighTransferVoltUpBound_Type()
)
dupsHighTransferVoltUpBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsHighTransferVoltUpBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsHighTransferVoltUpBound.setUnits("Volt")
_DupsHighTransferVoltLowBound_Type = Integer32
_DupsHighTransferVoltLowBound_Object = MibScalar
dupsHighTransferVoltLowBound = _DupsHighTransferVoltLowBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 16),
    _DupsHighTransferVoltLowBound_Type()
)
dupsHighTransferVoltLowBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsHighTransferVoltLowBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsHighTransferVoltLowBound.setUnits("Volt")
_DupsLowBattTime_Type = Integer32
_DupsLowBattTime_Object = MibScalar
dupsLowBattTime = _DupsLowBattTime_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 17),
    _DupsLowBattTime_Type()
)
dupsLowBattTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLowBattTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsLowBattTime.setUnits("Second")
_DupsOutletRelays_Type = Integer32
_DupsOutletRelays_Object = MibScalar
dupsOutletRelays = _DupsOutletRelays_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 18),
    _DupsOutletRelays_Type()
)
dupsOutletRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutletRelays.setStatus("mandatory")


class _DupsType_Type(Integer32):
    """Custom type dupsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("on-line", 1),
          ("off-line", 2),
          ("line-interactive", 3),
          ("three-phase", 4),
          ("splite-phase", 5))
    )


_DupsType_Type.__name__ = "Integer32"
_DupsType_Object = MibScalar
dupsType = _DupsType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 1, 19),
    _DupsType_Type()
)
dupsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsType.setStatus("mandatory")
_DupsControl_ObjectIdentity = ObjectIdentity
dupsControl = _DupsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2)
)


class _DupsShutdownType_Type(Integer32):
    """Custom type dupsShutdownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("output", 1),
          ("system", 2))
    )


_DupsShutdownType_Type.__name__ = "Integer32"
_DupsShutdownType_Object = MibScalar
dupsShutdownType = _DupsShutdownType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 1),
    _DupsShutdownType_Type()
)
dupsShutdownType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsShutdownType.setStatus("mandatory")


class _DupsAutoReboot_Type(Integer32):
    """Custom type dupsAutoReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAutoReboot_Type.__name__ = "Integer32"
_DupsAutoReboot_Object = MibScalar
dupsAutoReboot = _DupsAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 2),
    _DupsAutoReboot_Type()
)
dupsAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsAutoReboot.setStatus("mandatory")
_DupsShutdownAction_Type = Integer32
_DupsShutdownAction_Object = MibScalar
dupsShutdownAction = _DupsShutdownAction_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 3),
    _DupsShutdownAction_Type()
)
dupsShutdownAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsShutdownAction.setStatus("mandatory")
_DupsRestartAction_Type = Integer32
_DupsRestartAction_Object = MibScalar
dupsRestartAction = _DupsRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 4),
    _DupsRestartAction_Type()
)
dupsRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsRestartAction.setStatus("mandatory")
_DupsSetOutletRelay_Type = Integer32
_DupsSetOutletRelay_Object = MibScalar
dupsSetOutletRelay = _DupsSetOutletRelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 5),
    _DupsSetOutletRelay_Type()
)
dupsSetOutletRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsSetOutletRelay.setStatus("mandatory")
_DupsRelayOffDelay_Type = Integer32
_DupsRelayOffDelay_Object = MibScalar
dupsRelayOffDelay = _DupsRelayOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 6),
    _DupsRelayOffDelay_Type()
)
dupsRelayOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsRelayOffDelay.setStatus("mandatory")
_DupsRelayOnDelay_Type = Integer32
_DupsRelayOnDelay_Object = MibScalar
dupsRelayOnDelay = _DupsRelayOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 7),
    _DupsRelayOnDelay_Type()
)
dupsRelayOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsRelayOnDelay.setStatus("mandatory")
_DupsSmartShutdown_Type = Integer32
_DupsSmartShutdown_Object = MibScalar
dupsSmartShutdown = _DupsSmartShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 8),
    _DupsSmartShutdown_Type()
)
dupsSmartShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsSmartShutdown.setStatus("mandatory")
_DupsClearEnergy_Type = Integer32
_DupsClearEnergy_Object = MibScalar
dupsClearEnergy = _DupsClearEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 2, 9),
    _DupsClearEnergy_Type()
)
dupsClearEnergy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsClearEnergy.setStatus("mandatory")
_DupsConfig_ObjectIdentity = ObjectIdentity
dupsConfig = _DupsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3)
)


class _DupsConfigBuzzerAlarm_Type(Integer32):
    """Custom type dupsConfigBuzzerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("silence", 2))
    )


_DupsConfigBuzzerAlarm_Type.__name__ = "Integer32"
_DupsConfigBuzzerAlarm_Object = MibScalar
dupsConfigBuzzerAlarm = _DupsConfigBuzzerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 1),
    _DupsConfigBuzzerAlarm_Type()
)
dupsConfigBuzzerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigBuzzerAlarm.setStatus("mandatory")


class _DupsConfigBuzzerState_Type(Integer32):
    """Custom type dupsConfigBuzzerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DupsConfigBuzzerState_Type.__name__ = "Integer32"
_DupsConfigBuzzerState_Object = MibScalar
dupsConfigBuzzerState = _DupsConfigBuzzerState_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 2),
    _DupsConfigBuzzerState_Type()
)
dupsConfigBuzzerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigBuzzerState.setStatus("mandatory")


class _DupsConfigSensitivity_Type(Integer32):
    """Custom type dupsConfigSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reduced", 2),
          ("low", 3))
    )


_DupsConfigSensitivity_Type.__name__ = "Integer32"
_DupsConfigSensitivity_Object = MibScalar
dupsConfigSensitivity = _DupsConfigSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 3),
    _DupsConfigSensitivity_Type()
)
dupsConfigSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigSensitivity.setStatus("mandatory")
_DupsConfigLowVoltageTransferPoint_Type = Integer32
_DupsConfigLowVoltageTransferPoint_Object = MibScalar
dupsConfigLowVoltageTransferPoint = _DupsConfigLowVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 4),
    _DupsConfigLowVoltageTransferPoint_Type()
)
dupsConfigLowVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigLowVoltageTransferPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigLowVoltageTransferPoint.setUnits("Volt")
_DupsConfigHighVoltageTransferPoint_Type = Integer32
_DupsConfigHighVoltageTransferPoint_Object = MibScalar
dupsConfigHighVoltageTransferPoint = _DupsConfigHighVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 5),
    _DupsConfigHighVoltageTransferPoint_Type()
)
dupsConfigHighVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigHighVoltageTransferPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigHighVoltageTransferPoint.setUnits("Volt")
_DupsConfigUPSBootDelay_Type = Integer32
_DupsConfigUPSBootDelay_Object = MibScalar
dupsConfigUPSBootDelay = _DupsConfigUPSBootDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 6),
    _DupsConfigUPSBootDelay_Type()
)
dupsConfigUPSBootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigUPSBootDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigUPSBootDelay.setUnits("Second")
_DupsConfigExternalBatteryPack_Type = Integer32
_DupsConfigExternalBatteryPack_Object = MibScalar
dupsConfigExternalBatteryPack = _DupsConfigExternalBatteryPack_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 7),
    _DupsConfigExternalBatteryPack_Type()
)
dupsConfigExternalBatteryPack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigExternalBatteryPack.setStatus("mandatory")
_DupsConfigSmartShutdownOSDelay_Type = Integer32
_DupsConfigSmartShutdownOSDelay_Object = MibScalar
dupsConfigSmartShutdownOSDelay = _DupsConfigSmartShutdownOSDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 8),
    _DupsConfigSmartShutdownOSDelay_Type()
)
dupsConfigSmartShutdownOSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigSmartShutdownOSDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigSmartShutdownOSDelay.setUnits("Second")
_DupsConfigSmartShutdownUPSDelay_Type = Integer32
_DupsConfigSmartShutdownUPSDelay_Object = MibScalar
dupsConfigSmartShutdownUPSDelay = _DupsConfigSmartShutdownUPSDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 9),
    _DupsConfigSmartShutdownUPSDelay_Type()
)
dupsConfigSmartShutdownUPSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigSmartShutdownUPSDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigSmartShutdownUPSDelay.setUnits("Second")


class _DupsConfigEconomicMode_Type(Integer32):
    """Custom type dupsConfigEconomicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DupsConfigEconomicMode_Type.__name__ = "Integer32"
_DupsConfigEconomicMode_Object = MibScalar
dupsConfigEconomicMode = _DupsConfigEconomicMode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 3, 10),
    _DupsConfigEconomicMode_Type()
)
dupsConfigEconomicMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigEconomicMode.setStatus("mandatory")
_DupsInput_ObjectIdentity = ObjectIdentity
dupsInput = _DupsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4)
)
_DupsInputNumLines_Type = Integer32
_DupsInputNumLines_Object = MibScalar
dupsInputNumLines = _DupsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 1),
    _DupsInputNumLines_Type()
)
dupsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputNumLines.setStatus("mandatory")
_DupsInputFrequency1_Type = Integer32
_DupsInputFrequency1_Object = MibScalar
dupsInputFrequency1 = _DupsInputFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 2),
    _DupsInputFrequency1_Type()
)
dupsInputFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputFrequency1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputFrequency1.setUnits("0.1 Hertz")
_DupsInputVoltage1_Type = Integer32
_DupsInputVoltage1_Object = MibScalar
dupsInputVoltage1 = _DupsInputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 3),
    _DupsInputVoltage1_Type()
)
dupsInputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputVoltage1.setUnits("0.1 Volt")
_DupsInputVoltage12_Type = Integer32
_DupsInputVoltage12_Object = MibScalar
dupsInputVoltage12 = _DupsInputVoltage12_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 4),
    _DupsInputVoltage12_Type()
)
dupsInputVoltage12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage12.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputVoltage12.setUnits("0.1 Volt")
_DupsInputCurrent1_Type = Integer32
_DupsInputCurrent1_Object = MibScalar
dupsInputCurrent1 = _DupsInputCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 5),
    _DupsInputCurrent1_Type()
)
dupsInputCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputCurrent1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputCurrent1.setUnits("0.1 Amp")
_DupsInputPower1_Type = Integer32
_DupsInputPower1_Object = MibScalar
dupsInputPower1 = _DupsInputPower1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 6),
    _DupsInputPower1_Type()
)
dupsInputPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputPower1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputPower1.setUnits("1 Watt")
_DupsInputFrequency2_Type = Integer32
_DupsInputFrequency2_Object = MibScalar
dupsInputFrequency2 = _DupsInputFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 7),
    _DupsInputFrequency2_Type()
)
dupsInputFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputFrequency2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputFrequency2.setUnits("0.1 Hertz")
_DupsInputVoltage2_Type = Integer32
_DupsInputVoltage2_Object = MibScalar
dupsInputVoltage2 = _DupsInputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 8),
    _DupsInputVoltage2_Type()
)
dupsInputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputVoltage2.setUnits("0.1 Volt")
_DupsInputVoltage23_Type = Integer32
_DupsInputVoltage23_Object = MibScalar
dupsInputVoltage23 = _DupsInputVoltage23_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 9),
    _DupsInputVoltage23_Type()
)
dupsInputVoltage23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage23.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputVoltage23.setUnits("0.1 Volt")
_DupsInputCurrent2_Type = Integer32
_DupsInputCurrent2_Object = MibScalar
dupsInputCurrent2 = _DupsInputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 10),
    _DupsInputCurrent2_Type()
)
dupsInputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputCurrent2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputCurrent2.setUnits("0.1 Amp")
_DupsInputPower2_Type = Integer32
_DupsInputPower2_Object = MibScalar
dupsInputPower2 = _DupsInputPower2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 11),
    _DupsInputPower2_Type()
)
dupsInputPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputPower2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputPower2.setUnits("1 Watt")
_DupsInputFrequency3_Type = Integer32
_DupsInputFrequency3_Object = MibScalar
dupsInputFrequency3 = _DupsInputFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 12),
    _DupsInputFrequency3_Type()
)
dupsInputFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputFrequency3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputFrequency3.setUnits("0.1 Hertz")
_DupsInputVoltage3_Type = Integer32
_DupsInputVoltage3_Object = MibScalar
dupsInputVoltage3 = _DupsInputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 13),
    _DupsInputVoltage3_Type()
)
dupsInputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputVoltage3.setUnits("0.1 Volt")
_DupsInputVoltage31_Type = Integer32
_DupsInputVoltage31_Object = MibScalar
dupsInputVoltage31 = _DupsInputVoltage31_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 14),
    _DupsInputVoltage31_Type()
)
dupsInputVoltage31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage31.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputVoltage31.setUnits("0.1 Volt")
_DupsInputCurrent3_Type = Integer32
_DupsInputCurrent3_Object = MibScalar
dupsInputCurrent3 = _DupsInputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 15),
    _DupsInputCurrent3_Type()
)
dupsInputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputCurrent3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputCurrent3.setUnits("0.1 Amp")
_DupsInputPower3_Type = Integer32
_DupsInputPower3_Object = MibScalar
dupsInputPower3 = _DupsInputPower3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 16),
    _DupsInputPower3_Type()
)
dupsInputPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputPower3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputPower3.setUnits("1 Watt")
_DupsInputEnergy1_Type = Integer32
_DupsInputEnergy1_Object = MibScalar
dupsInputEnergy1 = _DupsInputEnergy1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 17),
    _DupsInputEnergy1_Type()
)
dupsInputEnergy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputEnergy1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputEnergy1.setUnits("1 kWh")
_DupsInputEnergy2_Type = Integer32
_DupsInputEnergy2_Object = MibScalar
dupsInputEnergy2 = _DupsInputEnergy2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 18),
    _DupsInputEnergy2_Type()
)
dupsInputEnergy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputEnergy2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputEnergy2.setUnits("1 kWh")
_DupsInputEnergy3_Type = Integer32
_DupsInputEnergy3_Object = MibScalar
dupsInputEnergy3 = _DupsInputEnergy3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 19),
    _DupsInputEnergy3_Type()
)
dupsInputEnergy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputEnergy3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputEnergy3.setUnits("1 kWh")
_DupsInputEnergyTotal_Type = Integer32
_DupsInputEnergyTotal_Object = MibScalar
dupsInputEnergyTotal = _DupsInputEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 20),
    _DupsInputEnergyTotal_Type()
)
dupsInputEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputEnergyTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsInputEnergyTotal.setUnits("1 kWh")


class _DupsInputLineFailCause_Type(Integer32):
    """Custom type dupsInputLineFailCause based on Integer32"""
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
        *(("no", 1),
          ("outoftolvolt", 2),
          ("outoftolfreq", 3),
          ("utilityoff", 4))
    )


_DupsInputLineFailCause_Type.__name__ = "Integer32"
_DupsInputLineFailCause_Object = MibScalar
dupsInputLineFailCause = _DupsInputLineFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 21),
    _DupsInputLineFailCause_Type()
)
dupsInputLineFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputLineFailCause.setStatus("mandatory")


class _DupsInputBadStatus_Type(Integer32):
    """Custom type dupsInputBadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_DupsInputBadStatus_Type.__name__ = "Integer32"
_DupsInputBadStatus_Object = MibScalar
dupsInputBadStatus = _DupsInputBadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 4, 22),
    _DupsInputBadStatus_Type()
)
dupsInputBadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputBadStatus.setStatus("mandatory")
_DupsOutput_ObjectIdentity = ObjectIdentity
dupsOutput = _DupsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5)
)


class _DupsOutputSource_Type(Integer32):
    """Custom type dupsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("battery", 2),
          ("bypass", 3),
          ("reducing", 4),
          ("boosting", 5),
          ("manualBypass", 6),
          ("other", 7),
          ("noOutput", 8),
          ("onEco", 9))
    )


_DupsOutputSource_Type.__name__ = "Integer32"
_DupsOutputSource_Object = MibScalar
dupsOutputSource = _DupsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 1),
    _DupsOutputSource_Type()
)
dupsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputSource.setStatus("mandatory")
_DupsOutputFrequency_Type = Integer32
_DupsOutputFrequency_Object = MibScalar
dupsOutputFrequency = _DupsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 2),
    _DupsOutputFrequency_Type()
)
dupsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputFrequency.setUnits("0.1 Hertz")
_DupsOutputNumLines_Type = Integer32
_DupsOutputNumLines_Object = MibScalar
dupsOutputNumLines = _DupsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 3),
    _DupsOutputNumLines_Type()
)
dupsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputNumLines.setStatus("mandatory")
_DupsOutputVoltage1_Type = Integer32
_DupsOutputVoltage1_Object = MibScalar
dupsOutputVoltage1 = _DupsOutputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 4),
    _DupsOutputVoltage1_Type()
)
dupsOutputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputVoltage1.setUnits("0.1 Volt")
_DupsOutputVoltage12_Type = Integer32
_DupsOutputVoltage12_Object = MibScalar
dupsOutputVoltage12 = _DupsOutputVoltage12_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 5),
    _DupsOutputVoltage12_Type()
)
dupsOutputVoltage12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage12.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputVoltage12.setUnits("0.1 Volt")
_DupsOutputCurrent1_Type = Integer32
_DupsOutputCurrent1_Object = MibScalar
dupsOutputCurrent1 = _DupsOutputCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 6),
    _DupsOutputCurrent1_Type()
)
dupsOutputCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputCurrent1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputCurrent1.setUnits("0.1 Amp")
_DupsOutputPower1_Type = Integer32
_DupsOutputPower1_Object = MibScalar
dupsOutputPower1 = _DupsOutputPower1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 7),
    _DupsOutputPower1_Type()
)
dupsOutputPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputPower1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputPower1.setUnits("1 Watt")
_DupsOutputLoad1_Type = Integer32
_DupsOutputLoad1_Object = MibScalar
dupsOutputLoad1 = _DupsOutputLoad1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 8),
    _DupsOutputLoad1_Type()
)
dupsOutputLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputLoad1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputLoad1.setUnits("1 Percent")
_DupsOutputVoltage2_Type = Integer32
_DupsOutputVoltage2_Object = MibScalar
dupsOutputVoltage2 = _DupsOutputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 9),
    _DupsOutputVoltage2_Type()
)
dupsOutputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputVoltage2.setUnits("0.1 Volt")
_DupsOutputVoltage23_Type = Integer32
_DupsOutputVoltage23_Object = MibScalar
dupsOutputVoltage23 = _DupsOutputVoltage23_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 10),
    _DupsOutputVoltage23_Type()
)
dupsOutputVoltage23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage23.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputVoltage23.setUnits("0.1 Volt")
_DupsOutputCurrent2_Type = Integer32
_DupsOutputCurrent2_Object = MibScalar
dupsOutputCurrent2 = _DupsOutputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 11),
    _DupsOutputCurrent2_Type()
)
dupsOutputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputCurrent2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputCurrent2.setUnits("0.1 Amp")
_DupsOutputPower2_Type = Integer32
_DupsOutputPower2_Object = MibScalar
dupsOutputPower2 = _DupsOutputPower2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 12),
    _DupsOutputPower2_Type()
)
dupsOutputPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputPower2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputPower2.setUnits("1 Watt")
_DupsOutputLoad2_Type = Integer32
_DupsOutputLoad2_Object = MibScalar
dupsOutputLoad2 = _DupsOutputLoad2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 13),
    _DupsOutputLoad2_Type()
)
dupsOutputLoad2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputLoad2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputLoad2.setUnits("1 Percent")
_DupsOutputVoltage3_Type = Integer32
_DupsOutputVoltage3_Object = MibScalar
dupsOutputVoltage3 = _DupsOutputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 14),
    _DupsOutputVoltage3_Type()
)
dupsOutputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputVoltage3.setUnits("0.1 Volt")
_DupsOutputVoltage31_Type = Integer32
_DupsOutputVoltage31_Object = MibScalar
dupsOutputVoltage31 = _DupsOutputVoltage31_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 15),
    _DupsOutputVoltage31_Type()
)
dupsOutputVoltage31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage31.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputVoltage31.setUnits("0.1 Volt")
_DupsOutputCurrent3_Type = Integer32
_DupsOutputCurrent3_Object = MibScalar
dupsOutputCurrent3 = _DupsOutputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 16),
    _DupsOutputCurrent3_Type()
)
dupsOutputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputCurrent3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputCurrent3.setUnits("0.1 Amp")
_DupsOutputPower3_Type = Integer32
_DupsOutputPower3_Object = MibScalar
dupsOutputPower3 = _DupsOutputPower3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 17),
    _DupsOutputPower3_Type()
)
dupsOutputPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputPower3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputPower3.setUnits("1 Watt")
_DupsOutputLoad3_Type = Integer32
_DupsOutputLoad3_Object = MibScalar
dupsOutputLoad3 = _DupsOutputLoad3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 18),
    _DupsOutputLoad3_Type()
)
dupsOutputLoad3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputLoad3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputLoad3.setUnits("1 Percent")
_DupsOutputTotalActivePower_Type = Integer32
_DupsOutputTotalActivePower_Object = MibScalar
dupsOutputTotalActivePower = _DupsOutputTotalActivePower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 19),
    _DupsOutputTotalActivePower_Type()
)
dupsOutputTotalActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputTotalActivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputTotalActivePower.setUnits("0.1 kW")
_DupsOutputTotalApparentPower_Type = Integer32
_DupsOutputTotalApparentPower_Object = MibScalar
dupsOutputTotalApparentPower = _DupsOutputTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 20),
    _DupsOutputTotalApparentPower_Type()
)
dupsOutputTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputTotalApparentPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputTotalApparentPower.setUnits("0.1 kVA")
_DupsOutputTotalPowerFactor_Type = Integer32
_DupsOutputTotalPowerFactor_Object = MibScalar
dupsOutputTotalPowerFactor = _DupsOutputTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 21),
    _DupsOutputTotalPowerFactor_Type()
)
dupsOutputTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputTotalPowerFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputTotalPowerFactor.setUnits("1 Percent")
_DupsOutputEnergy1_Type = Integer32
_DupsOutputEnergy1_Object = MibScalar
dupsOutputEnergy1 = _DupsOutputEnergy1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 22),
    _DupsOutputEnergy1_Type()
)
dupsOutputEnergy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputEnergy1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputEnergy1.setUnits("1 kWh")
_DupsOutputEnergy2_Type = Integer32
_DupsOutputEnergy2_Object = MibScalar
dupsOutputEnergy2 = _DupsOutputEnergy2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 23),
    _DupsOutputEnergy2_Type()
)
dupsOutputEnergy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputEnergy2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputEnergy2.setUnits("1 kWh")
_DupsOutputEnergy3_Type = Integer32
_DupsOutputEnergy3_Object = MibScalar
dupsOutputEnergy3 = _DupsOutputEnergy3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 24),
    _DupsOutputEnergy3_Type()
)
dupsOutputEnergy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputEnergy3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputEnergy3.setUnits("1 kWh")
_DupsOutputEnergyTotal_Type = Integer32
_DupsOutputEnergyTotal_Object = MibScalar
dupsOutputEnergyTotal = _DupsOutputEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 5, 25),
    _DupsOutputEnergyTotal_Type()
)
dupsOutputEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputEnergyTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputEnergyTotal.setUnits("1 kWh")
_DupsBypass_ObjectIdentity = ObjectIdentity
dupsBypass = _DupsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6)
)
_DupsBypassFrequency_Type = Integer32
_DupsBypassFrequency_Object = MibScalar
dupsBypassFrequency = _DupsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 1),
    _DupsBypassFrequency_Type()
)
dupsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassFrequency.setUnits("0.1 Hertz")
_DupsBypassNumLines_Type = Integer32
_DupsBypassNumLines_Object = MibScalar
dupsBypassNumLines = _DupsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 2),
    _DupsBypassNumLines_Type()
)
dupsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassNumLines.setStatus("mandatory")
_DupsBypassVoltage1_Type = Integer32
_DupsBypassVoltage1_Object = MibScalar
dupsBypassVoltage1 = _DupsBypassVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 3),
    _DupsBypassVoltage1_Type()
)
dupsBypassVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassVoltage1.setUnits("0.1 Volt")
_DupsBypassVoltage12_Type = Integer32
_DupsBypassVoltage12_Object = MibScalar
dupsBypassVoltage12 = _DupsBypassVoltage12_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 4),
    _DupsBypassVoltage12_Type()
)
dupsBypassVoltage12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage12.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassVoltage12.setUnits("0.1 Volt")
_DupsBypassCurrent1_Type = Integer32
_DupsBypassCurrent1_Object = MibScalar
dupsBypassCurrent1 = _DupsBypassCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 5),
    _DupsBypassCurrent1_Type()
)
dupsBypassCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassCurrent1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassCurrent1.setUnits("0.1 Amp")
_DupsBypassPower1_Type = Integer32
_DupsBypassPower1_Object = MibScalar
dupsBypassPower1 = _DupsBypassPower1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 6),
    _DupsBypassPower1_Type()
)
dupsBypassPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassPower1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassPower1.setUnits("1 Watt")
_DupsBypassVoltage2_Type = Integer32
_DupsBypassVoltage2_Object = MibScalar
dupsBypassVoltage2 = _DupsBypassVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 7),
    _DupsBypassVoltage2_Type()
)
dupsBypassVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassVoltage2.setUnits("0.1 Volt")
_DupsBypassVoltage23_Type = Integer32
_DupsBypassVoltage23_Object = MibScalar
dupsBypassVoltage23 = _DupsBypassVoltage23_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 8),
    _DupsBypassVoltage23_Type()
)
dupsBypassVoltage23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage23.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassVoltage23.setUnits("0.1 Volt")
_DupsBypassCurrent2_Type = Integer32
_DupsBypassCurrent2_Object = MibScalar
dupsBypassCurrent2 = _DupsBypassCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 9),
    _DupsBypassCurrent2_Type()
)
dupsBypassCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassCurrent2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassCurrent2.setUnits("0.1 Amp")
_DupsBypassPower2_Type = Integer32
_DupsBypassPower2_Object = MibScalar
dupsBypassPower2 = _DupsBypassPower2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 10),
    _DupsBypassPower2_Type()
)
dupsBypassPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassPower2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassPower2.setUnits("1 Watt")
_DupsBypassVoltage3_Type = Integer32
_DupsBypassVoltage3_Object = MibScalar
dupsBypassVoltage3 = _DupsBypassVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 11),
    _DupsBypassVoltage3_Type()
)
dupsBypassVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassVoltage3.setUnits("0.1 Volt")
_DupsBypassVoltage31_Type = Integer32
_DupsBypassVoltage31_Object = MibScalar
dupsBypassVoltage31 = _DupsBypassVoltage31_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 12),
    _DupsBypassVoltage31_Type()
)
dupsBypassVoltage31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage31.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassVoltage31.setUnits("0.1 Volt")
_DupsBypassCurrent3_Type = Integer32
_DupsBypassCurrent3_Object = MibScalar
dupsBypassCurrent3 = _DupsBypassCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 13),
    _DupsBypassCurrent3_Type()
)
dupsBypassCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassCurrent3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassCurrent3.setUnits("0.1 Amp")
_DupsBypassPower3_Type = Integer32
_DupsBypassPower3_Object = MibScalar
dupsBypassPower3 = _DupsBypassPower3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 14),
    _DupsBypassPower3_Type()
)
dupsBypassPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassPower3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassPower3.setUnits("1 Watt")
_DupsBypassSTSTemperature_Type = Integer32
_DupsBypassSTSTemperature_Object = MibScalar
dupsBypassSTSTemperature = _DupsBypassSTSTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 6, 15),
    _DupsBypassSTSTemperature_Type()
)
dupsBypassSTSTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassSTSTemperature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassSTSTemperature.setUnits("1 Degree Celsius")
_DupsBattery_ObjectIdentity = ObjectIdentity
dupsBattery = _DupsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7)
)


class _DupsBatteryCondition_Type(Integer32):
    """Custom type dupsBatteryCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("weak", 2),
          ("replace", 3))
    )


_DupsBatteryCondition_Type.__name__ = "Integer32"
_DupsBatteryCondition_Object = MibScalar
dupsBatteryCondition = _DupsBatteryCondition_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 1),
    _DupsBatteryCondition_Type()
)
dupsBatteryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCondition.setStatus("mandatory")


class _DupsBatteryStatus_Type(Integer32):
    """Custom type dupsBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("low", 2),
          ("depleted", 3))
    )


_DupsBatteryStatus_Type.__name__ = "Integer32"
_DupsBatteryStatus_Object = MibScalar
dupsBatteryStatus = _DupsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 2),
    _DupsBatteryStatus_Type()
)
dupsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryStatus.setStatus("mandatory")


class _DupsBatteryCharge_Type(Integer32):
    """Custom type dupsBatteryCharge based on Integer32"""
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
        *(("floating", 1),
          ("charging", 2),
          ("resting", 3),
          ("discharging", 4))
    )


_DupsBatteryCharge_Type.__name__ = "Integer32"
_DupsBatteryCharge_Object = MibScalar
dupsBatteryCharge = _DupsBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 3),
    _DupsBatteryCharge_Type()
)
dupsBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCharge.setStatus("mandatory")
_DupsSecondsOnBattery_Type = Integer32
_DupsSecondsOnBattery_Object = MibScalar
dupsSecondsOnBattery = _DupsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 4),
    _DupsSecondsOnBattery_Type()
)
dupsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsSecondsOnBattery.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsSecondsOnBattery.setUnits("1 Second")
_DupsBatteryEstimatedTime_Type = Integer32
_DupsBatteryEstimatedTime_Object = MibScalar
dupsBatteryEstimatedTime = _DupsBatteryEstimatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 5),
    _DupsBatteryEstimatedTime_Type()
)
dupsBatteryEstimatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryEstimatedTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryEstimatedTime.setUnits("1 Minute")
_DupsBatteryPosVoltage_Type = Integer32
_DupsBatteryPosVoltage_Object = MibScalar
dupsBatteryPosVoltage = _DupsBatteryPosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 6),
    _DupsBatteryPosVoltage_Type()
)
dupsBatteryPosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryPosVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryPosVoltage.setUnits("0.1 Volt DC")
_DupsBatteryNegVoltage_Type = Integer32
_DupsBatteryNegVoltage_Object = MibScalar
dupsBatteryNegVoltage = _DupsBatteryNegVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 7),
    _DupsBatteryNegVoltage_Type()
)
dupsBatteryNegVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryNegVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryNegVoltage.setUnits("-0.1 Volt DC")
_DupsBatteryPosCurrent_Type = Integer32
_DupsBatteryPosCurrent_Object = MibScalar
dupsBatteryPosCurrent = _DupsBatteryPosCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 8),
    _DupsBatteryPosCurrent_Type()
)
dupsBatteryPosCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryPosCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryPosCurrent.setUnits("0.1 Amp DC")
_DupsBatteryNegCurrent_Type = Integer32
_DupsBatteryNegCurrent_Object = MibScalar
dupsBatteryNegCurrent = _DupsBatteryNegCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 9),
    _DupsBatteryNegCurrent_Type()
)
dupsBatteryNegCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryNegCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryNegCurrent.setUnits("0.1 Amp DC")


class _DupsBatteryPosCapacity_Type(Integer32):
    """Custom type dupsBatteryPosCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DupsBatteryPosCapacity_Type.__name__ = "Integer32"
_DupsBatteryPosCapacity_Object = MibScalar
dupsBatteryPosCapacity = _DupsBatteryPosCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 10),
    _DupsBatteryPosCapacity_Type()
)
dupsBatteryPosCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryPosCapacity.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryPosCapacity.setUnits("1 Percent")


class _DupsBatteryNegCapacity_Type(Integer32):
    """Custom type dupsBatteryNegCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DupsBatteryNegCapacity_Type.__name__ = "Integer32"
_DupsBatteryNegCapacity_Object = MibScalar
dupsBatteryNegCapacity = _DupsBatteryNegCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 11),
    _DupsBatteryNegCapacity_Type()
)
dupsBatteryNegCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryNegCapacity.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryNegCapacity.setUnits("1 Percent")
_DupsTemperature_Type = Integer32
_DupsTemperature_Object = MibScalar
dupsTemperature = _DupsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 12),
    _DupsTemperature_Type()
)
dupsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTemperature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsTemperature.setUnits("1 Degrees Centigrade")


class _DupsLastReplaceDate_Type(DisplayString):
    """Custom type dupsLastReplaceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DupsLastReplaceDate_Type.__name__ = "DisplayString"
_DupsLastReplaceDate_Object = MibScalar
dupsLastReplaceDate = _DupsLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 13),
    _DupsLastReplaceDate_Type()
)
dupsLastReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLastReplaceDate.setStatus("mandatory")


class _DupsNextReplaceDate_Type(DisplayString):
    """Custom type dupsNextReplaceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DupsNextReplaceDate_Type.__name__ = "DisplayString"
_DupsNextReplaceDate_Object = MibScalar
dupsNextReplaceDate = _DupsNextReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 14),
    _DupsNextReplaceDate_Type()
)
dupsNextReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsNextReplaceDate.setStatus("mandatory")


class _DupsBatteryBreaker_Type(Integer32):
    """Custom type dupsBatteryBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsBatteryBreaker_Type.__name__ = "Integer32"
_DupsBatteryBreaker_Object = MibScalar
dupsBatteryBreaker = _DupsBatteryBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 15),
    _DupsBatteryBreaker_Type()
)
dupsBatteryBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryBreaker.setStatus("mandatory")
_DupsBatteryCab1Tempurature_Type = Integer32
_DupsBatteryCab1Tempurature_Object = MibScalar
dupsBatteryCab1Tempurature = _DupsBatteryCab1Tempurature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 16),
    _DupsBatteryCab1Tempurature_Type()
)
dupsBatteryCab1Tempurature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCab1Tempurature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryCab1Tempurature.setUnits("1 Degrees Centigrade")
_DupsBatteryCab2Tempurature_Type = Integer32
_DupsBatteryCab2Tempurature_Object = MibScalar
dupsBatteryCab2Tempurature = _DupsBatteryCab2Tempurature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 17),
    _DupsBatteryCab2Tempurature_Type()
)
dupsBatteryCab2Tempurature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCab2Tempurature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryCab2Tempurature.setUnits("1 Degrees Centigrade")
_DupsBatteryCab3Tempurature_Type = Integer32
_DupsBatteryCab3Tempurature_Object = MibScalar
dupsBatteryCab3Tempurature = _DupsBatteryCab3Tempurature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 18),
    _DupsBatteryCab3Tempurature_Type()
)
dupsBatteryCab3Tempurature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCab3Tempurature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryCab3Tempurature.setUnits("1 Degrees Centigrade")
_DupsBatteryCab4Tempurature_Type = Integer32
_DupsBatteryCab4Tempurature_Object = MibScalar
dupsBatteryCab4Tempurature = _DupsBatteryCab4Tempurature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 7, 19),
    _DupsBatteryCab4Tempurature_Type()
)
dupsBatteryCab4Tempurature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCab4Tempurature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryCab4Tempurature.setUnits("1 Degrees Centigrade")
_DupsTest_ObjectIdentity = ObjectIdentity
dupsTest = _DupsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 8)
)


class _DupsTestType_Type(Integer32):
    """Custom type dupsTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("generalTest", 2),
          ("batteryTest", 3),
          ("testFor10sec", 4),
          ("testUntilBattlow", 5))
    )


_DupsTestType_Type.__name__ = "Integer32"
_DupsTestType_Object = MibScalar
dupsTestType = _DupsTestType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 8, 1),
    _DupsTestType_Type()
)
dupsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsTestType.setStatus("mandatory")


class _DupsTestResultsSummary_Type(Integer32):
    """Custom type dupsTestResultsSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noTestsInitiated", 1),
          ("donePass", 2),
          ("inProgress", 3),
          ("generalTestFail", 4),
          ("batteryTestFail", 5),
          ("deepBatteryTestFail", 6))
    )


_DupsTestResultsSummary_Type.__name__ = "Integer32"
_DupsTestResultsSummary_Object = MibScalar
dupsTestResultsSummary = _DupsTestResultsSummary_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 8, 2),
    _DupsTestResultsSummary_Type()
)
dupsTestResultsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTestResultsSummary.setStatus("mandatory")


class _DupsTestResultsDetail_Type(DisplayString):
    """Custom type dupsTestResultsDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DupsTestResultsDetail_Type.__name__ = "DisplayString"
_DupsTestResultsDetail_Object = MibScalar
dupsTestResultsDetail = _DupsTestResultsDetail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 8, 3),
    _DupsTestResultsDetail_Type()
)
dupsTestResultsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTestResultsDetail.setStatus("mandatory")


class _DupsGeneratorTest_Type(Integer32):
    """Custom type dupsGeneratorTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("start", 2))
    )


_DupsGeneratorTest_Type.__name__ = "Integer32"
_DupsGeneratorTest_Object = MibScalar
dupsGeneratorTest = _DupsGeneratorTest_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 8, 4),
    _DupsGeneratorTest_Type()
)
dupsGeneratorTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsGeneratorTest.setStatus("mandatory")


class _DupsGeneratorTestStatus_Type(Integer32):
    """Custom type dupsGeneratorTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("none", 2),
          ("inhibitTest", 3),
          ("abnormallyTerminate", 4),
          ("byInstruction", 5),
          ("byTimeout", 6))
    )


_DupsGeneratorTestStatus_Type.__name__ = "Integer32"
_DupsGeneratorTestStatus_Object = MibScalar
dupsGeneratorTestStatus = _DupsGeneratorTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 8, 5),
    _DupsGeneratorTestStatus_Type()
)
dupsGeneratorTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsGeneratorTestStatus.setStatus("mandatory")
_DupsAlarm_ObjectIdentity = ObjectIdentity
dupsAlarm = _DupsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9)
)


class _DupsAlarmDisconnect_Type(Integer32):
    """Custom type dupsAlarmDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmDisconnect_Type.__name__ = "Integer32"
_DupsAlarmDisconnect_Object = MibScalar
dupsAlarmDisconnect = _DupsAlarmDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 1),
    _DupsAlarmDisconnect_Type()
)
dupsAlarmDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmDisconnect.setStatus("mandatory")


class _DupsAlarmInputOutOfRange_Type(Integer32):
    """Custom type dupsAlarmInputOutOfRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmInputOutOfRange_Type.__name__ = "Integer32"
_DupsAlarmInputOutOfRange_Object = MibScalar
dupsAlarmInputOutOfRange = _DupsAlarmInputOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 2),
    _DupsAlarmInputOutOfRange_Type()
)
dupsAlarmInputOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmInputOutOfRange.setStatus("mandatory")


class _DupsAlarmBatteryLow_Type(Integer32):
    """Custom type dupsAlarmBatteryLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmBatteryLow_Type.__name__ = "Integer32"
_DupsAlarmBatteryLow_Object = MibScalar
dupsAlarmBatteryLow = _DupsAlarmBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 3),
    _DupsAlarmBatteryLow_Type()
)
dupsAlarmBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBatteryLow.setStatus("mandatory")


class _DupsAlarmLoadOnBypass_Type(Integer32):
    """Custom type dupsAlarmLoadOnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmLoadOnBypass_Type.__name__ = "Integer32"
_DupsAlarmLoadOnBypass_Object = MibScalar
dupsAlarmLoadOnBypass = _DupsAlarmLoadOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 4),
    _DupsAlarmLoadOnBypass_Type()
)
dupsAlarmLoadOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmLoadOnBypass.setStatus("mandatory")


class _DupsAlarmOther_Type(Integer32):
    """Custom type dupsAlarmOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmOther_Type.__name__ = "Integer32"
_DupsAlarmOther_Object = MibScalar
dupsAlarmOther = _DupsAlarmOther_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 5),
    _DupsAlarmOther_Type()
)
dupsAlarmOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOther.setStatus("mandatory")


class _DupsAlarmBatteryGroundFault_Type(Integer32):
    """Custom type dupsAlarmBatteryGroundFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmBatteryGroundFault_Type.__name__ = "Integer32"
_DupsAlarmBatteryGroundFault_Object = MibScalar
dupsAlarmBatteryGroundFault = _DupsAlarmBatteryGroundFault_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 6),
    _DupsAlarmBatteryGroundFault_Type()
)
dupsAlarmBatteryGroundFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBatteryGroundFault.setStatus("mandatory")


class _DupsAlarmTestInProgress_Type(Integer32):
    """Custom type dupsAlarmTestInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmTestInProgress_Type.__name__ = "Integer32"
_DupsAlarmTestInProgress_Object = MibScalar
dupsAlarmTestInProgress = _DupsAlarmTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 7),
    _DupsAlarmTestInProgress_Type()
)
dupsAlarmTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmTestInProgress.setStatus("mandatory")


class _DupsAlarmBatteryTestFail_Type(Integer32):
    """Custom type dupsAlarmBatteryTestFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmBatteryTestFail_Type.__name__ = "Integer32"
_DupsAlarmBatteryTestFail_Object = MibScalar
dupsAlarmBatteryTestFail = _DupsAlarmBatteryTestFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 8),
    _DupsAlarmBatteryTestFail_Type()
)
dupsAlarmBatteryTestFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBatteryTestFail.setStatus("mandatory")


class _DupsAlarmFuseFailure_Type(Integer32):
    """Custom type dupsAlarmFuseFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmFuseFailure_Type.__name__ = "Integer32"
_DupsAlarmFuseFailure_Object = MibScalar
dupsAlarmFuseFailure = _DupsAlarmFuseFailure_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 9),
    _DupsAlarmFuseFailure_Type()
)
dupsAlarmFuseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmFuseFailure.setStatus("mandatory")


class _DupsAlarmOutputOverload_Type(Integer32):
    """Custom type dupsAlarmOutputOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmOutputOverload_Type.__name__ = "Integer32"
_DupsAlarmOutputOverload_Object = MibScalar
dupsAlarmOutputOverload = _DupsAlarmOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 10),
    _DupsAlarmOutputOverload_Type()
)
dupsAlarmOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputOverload.setStatus("mandatory")


class _DupsAlarmInverterAbnormal_Type(Integer32):
    """Custom type dupsAlarmInverterAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmInverterAbnormal_Type.__name__ = "Integer32"
_DupsAlarmInverterAbnormal_Object = MibScalar
dupsAlarmInverterAbnormal = _DupsAlarmInverterAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 11),
    _DupsAlarmInverterAbnormal_Type()
)
dupsAlarmInverterAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmInverterAbnormal.setStatus("mandatory")


class _DupsAlarmLoadOnReserve_Type(Integer32):
    """Custom type dupsAlarmLoadOnReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmLoadOnReserve_Type.__name__ = "Integer32"
_DupsAlarmLoadOnReserve_Object = MibScalar
dupsAlarmLoadOnReserve = _DupsAlarmLoadOnReserve_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 12),
    _DupsAlarmLoadOnReserve_Type()
)
dupsAlarmLoadOnReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmLoadOnReserve.setStatus("mandatory")


class _DupsAlarmTemperature_Type(Integer32):
    """Custom type dupsAlarmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmTemperature_Type.__name__ = "Integer32"
_DupsAlarmTemperature_Object = MibScalar
dupsAlarmTemperature = _DupsAlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 13),
    _DupsAlarmTemperature_Type()
)
dupsAlarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmTemperature.setStatus("mandatory")


class _DupsAlarmBypassOutOfRange_Type(Integer32):
    """Custom type dupsAlarmBypassOutOfRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmBypassOutOfRange_Type.__name__ = "Integer32"
_DupsAlarmBypassOutOfRange_Object = MibScalar
dupsAlarmBypassOutOfRange = _DupsAlarmBypassOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 14),
    _DupsAlarmBypassOutOfRange_Type()
)
dupsAlarmBypassOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBypassOutOfRange.setStatus("mandatory")


class _DupsAlarmStandby_Type(Integer32):
    """Custom type dupsAlarmStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmStandby_Type.__name__ = "Integer32"
_DupsAlarmStandby_Object = MibScalar
dupsAlarmStandby = _DupsAlarmStandby_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 15),
    _DupsAlarmStandby_Type()
)
dupsAlarmStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmStandby.setStatus("mandatory")


class _DupsAlarmChargerFail_Type(Integer32):
    """Custom type dupsAlarmChargerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmChargerFail_Type.__name__ = "Integer32"
_DupsAlarmChargerFail_Object = MibScalar
dupsAlarmChargerFail = _DupsAlarmChargerFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 16),
    _DupsAlarmChargerFail_Type()
)
dupsAlarmChargerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmChargerFail.setStatus("mandatory")


class _DupsAlarmFanFail_Type(Integer32):
    """Custom type dupsAlarmFanFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmFanFail_Type.__name__ = "Integer32"
_DupsAlarmFanFail_Object = MibScalar
dupsAlarmFanFail = _DupsAlarmFanFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 17),
    _DupsAlarmFanFail_Type()
)
dupsAlarmFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmFanFail.setStatus("mandatory")


class _DupsAlarmEconomicMode_Type(Integer32):
    """Custom type dupsAlarmEconomicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmEconomicMode_Type.__name__ = "Integer32"
_DupsAlarmEconomicMode_Object = MibScalar
dupsAlarmEconomicMode = _DupsAlarmEconomicMode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 18),
    _DupsAlarmEconomicMode_Type()
)
dupsAlarmEconomicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEconomicMode.setStatus("mandatory")


class _DupsAlarmOutputOff_Type(Integer32):
    """Custom type dupsAlarmOutputOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmOutputOff_Type.__name__ = "Integer32"
_DupsAlarmOutputOff_Object = MibScalar
dupsAlarmOutputOff = _DupsAlarmOutputOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 19),
    _DupsAlarmOutputOff_Type()
)
dupsAlarmOutputOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputOff.setStatus("mandatory")


class _DupsAlarmSmartShutdown_Type(Integer32):
    """Custom type dupsAlarmSmartShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmSmartShutdown_Type.__name__ = "Integer32"
_DupsAlarmSmartShutdown_Object = MibScalar
dupsAlarmSmartShutdown = _DupsAlarmSmartShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 20),
    _DupsAlarmSmartShutdown_Type()
)
dupsAlarmSmartShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmSmartShutdown.setStatus("mandatory")


class _DupsAlarmEmergencyPowerOff_Type(Integer32):
    """Custom type dupsAlarmEmergencyPowerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmEmergencyPowerOff_Type.__name__ = "Integer32"
_DupsAlarmEmergencyPowerOff_Object = MibScalar
dupsAlarmEmergencyPowerOff = _DupsAlarmEmergencyPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 21),
    _DupsAlarmEmergencyPowerOff_Type()
)
dupsAlarmEmergencyPowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEmergencyPowerOff.setStatus("mandatory")


class _DupsAlarmUPSShutdown_Type(Integer32):
    """Custom type dupsAlarmUPSShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmUPSShutdown_Type.__name__ = "Integer32"
_DupsAlarmUPSShutdown_Object = MibScalar
dupsAlarmUPSShutdown = _DupsAlarmUPSShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 22),
    _DupsAlarmUPSShutdown_Type()
)
dupsAlarmUPSShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmUPSShutdown.setStatus("mandatory")


class _DupsAlarmEPO_Type(Integer32):
    """Custom type dupsAlarmEPO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmEPO_Type.__name__ = "Integer32"
_DupsAlarmEPO_Object = MibScalar
dupsAlarmEPO = _DupsAlarmEPO_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 23),
    _DupsAlarmEPO_Type()
)
dupsAlarmEPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEPO.setStatus("mandatory")


class _DupsAlarmOutVoltOverLimit_Type(Integer32):
    """Custom type dupsAlarmOutVoltOverLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmOutVoltOverLimit_Type.__name__ = "Integer32"
_DupsAlarmOutVoltOverLimit_Object = MibScalar
dupsAlarmOutVoltOverLimit = _DupsAlarmOutVoltOverLimit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 24),
    _DupsAlarmOutVoltOverLimit_Type()
)
dupsAlarmOutVoltOverLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutVoltOverLimit.setStatus("mandatory")


class _DupsAlarmOutVoltUnderLimit_Type(Integer32):
    """Custom type dupsAlarmOutVoltUnderLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmOutVoltUnderLimit_Type.__name__ = "Integer32"
_DupsAlarmOutVoltUnderLimit_Object = MibScalar
dupsAlarmOutVoltUnderLimit = _DupsAlarmOutVoltUnderLimit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 25),
    _DupsAlarmOutVoltUnderLimit_Type()
)
dupsAlarmOutVoltUnderLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutVoltUnderLimit.setStatus("mandatory")


class _DupsAlarmPowerModule_Type(Integer32):
    """Custom type dupsAlarmPowerModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmPowerModule_Type.__name__ = "Integer32"
_DupsAlarmPowerModule_Object = MibScalar
dupsAlarmPowerModule = _DupsAlarmPowerModule_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 26),
    _DupsAlarmPowerModule_Type()
)
dupsAlarmPowerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmPowerModule.setStatus("mandatory")


class _DupsAlarmOutputBreaker_Type(Integer32):
    """Custom type dupsAlarmOutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmOutputBreaker_Type.__name__ = "Integer32"
_DupsAlarmOutputBreaker_Object = MibScalar
dupsAlarmOutputBreaker = _DupsAlarmOutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 27),
    _DupsAlarmOutputBreaker_Type()
)
dupsAlarmOutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputBreaker.setStatus("mandatory")


class _DupsAlarmOutletBank1Breaker_Type(Integer32):
    """Custom type dupsAlarmOutletBank1Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmOutletBank1Breaker_Type.__name__ = "Integer32"
_DupsAlarmOutletBank1Breaker_Object = MibScalar
dupsAlarmOutletBank1Breaker = _DupsAlarmOutletBank1Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 28),
    _DupsAlarmOutletBank1Breaker_Type()
)
dupsAlarmOutletBank1Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutletBank1Breaker.setStatus("mandatory")


class _DupsAlarmOutletBank2Breaker_Type(Integer32):
    """Custom type dupsAlarmOutletBank2Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmOutletBank2Breaker_Type.__name__ = "Integer32"
_DupsAlarmOutletBank2Breaker_Object = MibScalar
dupsAlarmOutletBank2Breaker = _DupsAlarmOutletBank2Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 29),
    _DupsAlarmOutletBank2Breaker_Type()
)
dupsAlarmOutletBank2Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutletBank2Breaker.setStatus("mandatory")


class _DupsAlarmOutletBank3Breaker_Type(Integer32):
    """Custom type dupsAlarmOutletBank3Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmOutletBank3Breaker_Type.__name__ = "Integer32"
_DupsAlarmOutletBank3Breaker_Object = MibScalar
dupsAlarmOutletBank3Breaker = _DupsAlarmOutletBank3Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 30),
    _DupsAlarmOutletBank3Breaker_Type()
)
dupsAlarmOutletBank3Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutletBank3Breaker.setStatus("mandatory")


class _DupsAlarmOutletBank4Breaker_Type(Integer32):
    """Custom type dupsAlarmOutletBank4Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmOutletBank4Breaker_Type.__name__ = "Integer32"
_DupsAlarmOutletBank4Breaker_Object = MibScalar
dupsAlarmOutletBank4Breaker = _DupsAlarmOutletBank4Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 31),
    _DupsAlarmOutletBank4Breaker_Type()
)
dupsAlarmOutletBank4Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutletBank4Breaker.setStatus("mandatory")


class _DupsAlarmSummary_Type(Integer32):
    """Custom type dupsAlarmSummary based on Integer32"""
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
        *(("none", 1),
          ("informational", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_DupsAlarmSummary_Type.__name__ = "Integer32"
_DupsAlarmSummary_Object = MibScalar
dupsAlarmSummary = _DupsAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 32),
    _DupsAlarmSummary_Type()
)
dupsAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmSummary.setStatus("mandatory")


class _DupsAlarmRedundancyLoss_Type(Integer32):
    """Custom type dupsAlarmRedundancyLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsAlarmRedundancyLoss_Type.__name__ = "Integer32"
_DupsAlarmRedundancyLoss_Object = MibScalar
dupsAlarmRedundancyLoss = _DupsAlarmRedundancyLoss_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 33),
    _DupsAlarmRedundancyLoss_Type()
)
dupsAlarmRedundancyLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmRedundancyLoss.setStatus("mandatory")


class _DupsAlarmPhaseAsynchronous_Type(Integer32):
    """Custom type dupsAlarmPhaseAsynchronous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("synchronous", 2))
    )


_DupsAlarmPhaseAsynchronous_Type.__name__ = "Integer32"
_DupsAlarmPhaseAsynchronous_Object = MibScalar
dupsAlarmPhaseAsynchronous = _DupsAlarmPhaseAsynchronous_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 34),
    _DupsAlarmPhaseAsynchronous_Type()
)
dupsAlarmPhaseAsynchronous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmPhaseAsynchronous.setStatus("mandatory")


class _DupsAlarmRectifierAbnormal_Type(Integer32):
    """Custom type dupsAlarmRectifierAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsAlarmRectifierAbnormal_Type.__name__ = "Integer32"
_DupsAlarmRectifierAbnormal_Object = MibScalar
dupsAlarmRectifierAbnormal = _DupsAlarmRectifierAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 35),
    _DupsAlarmRectifierAbnormal_Type()
)
dupsAlarmRectifierAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmRectifierAbnormal.setStatus("mandatory")


class _DupsAlarmBypassBreakerOpen_Type(Integer32):
    """Custom type dupsAlarmBypassBreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmBypassBreakerOpen_Type.__name__ = "Integer32"
_DupsAlarmBypassBreakerOpen_Object = MibScalar
dupsAlarmBypassBreakerOpen = _DupsAlarmBypassBreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 36),
    _DupsAlarmBypassBreakerOpen_Type()
)
dupsAlarmBypassBreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBypassBreakerOpen.setStatus("mandatory")


class _DupsAlarmMainInputBreakerOpen_Type(Integer32):
    """Custom type dupsAlarmMainInputBreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmMainInputBreakerOpen_Type.__name__ = "Integer32"
_DupsAlarmMainInputBreakerOpen_Object = MibScalar
dupsAlarmMainInputBreakerOpen = _DupsAlarmMainInputBreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 37),
    _DupsAlarmMainInputBreakerOpen_Type()
)
dupsAlarmMainInputBreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmMainInputBreakerOpen.setStatus("mandatory")


class _DupsAlarmManualBypassBreaker_Type(Integer32):
    """Custom type dupsAlarmManualBypassBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsAlarmManualBypassBreaker_Type.__name__ = "Integer32"
_DupsAlarmManualBypassBreaker_Object = MibScalar
dupsAlarmManualBypassBreaker = _DupsAlarmManualBypassBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 9, 38),
    _DupsAlarmManualBypassBreaker_Type()
)
dupsAlarmManualBypassBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmManualBypassBreaker.setStatus("mandatory")
_DupsPowerModule_ObjectIdentity = ObjectIdentity
dupsPowerModule = _DupsPowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10)
)


class _DupsPMBypassInputAlarm_Type(Integer32):
    """Custom type dupsPMBypassInputAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsPMBypassInputAlarm_Type.__name__ = "Integer32"
_DupsPMBypassInputAlarm_Object = MibScalar
dupsPMBypassInputAlarm = _DupsPMBypassInputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 1),
    _DupsPMBypassInputAlarm_Type()
)
dupsPMBypassInputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMBypassInputAlarm.setStatus("mandatory")


class _DupsPMBypassPhaseAlarm_Type(Integer32):
    """Custom type dupsPMBypassPhaseAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsPMBypassPhaseAlarm_Type.__name__ = "Integer32"
_DupsPMBypassPhaseAlarm_Object = MibScalar
dupsPMBypassPhaseAlarm = _DupsPMBypassPhaseAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 2),
    _DupsPMBypassPhaseAlarm_Type()
)
dupsPMBypassPhaseAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMBypassPhaseAlarm.setStatus("mandatory")


class _DupsPMBypassSTSOverloadAlarm_Type(Integer32):
    """Custom type dupsPMBypassSTSOverloadAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsPMBypassSTSOverloadAlarm_Type.__name__ = "Integer32"
_DupsPMBypassSTSOverloadAlarm_Object = MibScalar
dupsPMBypassSTSOverloadAlarm = _DupsPMBypassSTSOverloadAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 3),
    _DupsPMBypassSTSOverloadAlarm_Type()
)
dupsPMBypassSTSOverloadAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMBypassSTSOverloadAlarm.setStatus("mandatory")


class _DupsPMBypassSTSOverTempAlarm_Type(Integer32):
    """Custom type dupsPMBypassSTSOverTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsPMBypassSTSOverTempAlarm_Type.__name__ = "Integer32"
_DupsPMBypassSTSOverTempAlarm_Object = MibScalar
dupsPMBypassSTSOverTempAlarm = _DupsPMBypassSTSOverTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 4),
    _DupsPMBypassSTSOverTempAlarm_Type()
)
dupsPMBypassSTSOverTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMBypassSTSOverTempAlarm.setStatus("mandatory")


class _DupsPMBypassSTSFailAlarm_Type(Integer32):
    """Custom type dupsPMBypassSTSFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsPMBypassSTSFailAlarm_Type.__name__ = "Integer32"
_DupsPMBypassSTSFailAlarm_Object = MibScalar
dupsPMBypassSTSFailAlarm = _DupsPMBypassSTSFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 5),
    _DupsPMBypassSTSFailAlarm_Type()
)
dupsPMBypassSTSFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMBypassSTSFailAlarm.setStatus("mandatory")
_DupsPMTable_Object = MibTable
dupsPMTable = _DupsPMTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6)
)
if mibBuilder.loadTexts:
    dupsPMTable.setStatus("mandatory")
_DupsPMEntry_Object = MibTableRow
dupsPMEntry = _DupsPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1)
)
dupsPMEntry.setIndexNames(
    (0, "DeltaUPSv5-MIB", "dupsPMID"),
)
if mibBuilder.loadTexts:
    dupsPMEntry.setStatus("mandatory")
_DupsPMID_Type = Integer32
_DupsPMID_Object = MibTableColumn
dupsPMID = _DupsPMID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 1),
    _DupsPMID_Type()
)
dupsPMID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dupsPMID.setStatus("mandatory")
_DupsPMPFCTemp_Type = Integer32
_DupsPMPFCTemp_Object = MibTableColumn
dupsPMPFCTemp = _DupsPMPFCTemp_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 2),
    _DupsPMPFCTemp_Type()
)
dupsPMPFCTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMPFCTemp.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMPFCTemp.setUnits("1 Degree Celsius")
_DupsPMINVTemp_Type = Integer32
_DupsPMINVTemp_Object = MibTableColumn
dupsPMINVTemp = _DupsPMINVTemp_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 3),
    _DupsPMINVTemp_Type()
)
dupsPMINVTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVTemp.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVTemp.setUnits("1 Degree Celsius")
_DupsPMINVTempR_Type = Integer32
_DupsPMINVTempR_Object = MibTableColumn
dupsPMINVTempR = _DupsPMINVTempR_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 4),
    _DupsPMINVTempR_Type()
)
dupsPMINVTempR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVTempR.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVTempR.setUnits("1 Degree Celsius")
_DupsPMINVTempS_Type = Integer32
_DupsPMINVTempS_Object = MibTableColumn
dupsPMINVTempS = _DupsPMINVTempS_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 5),
    _DupsPMINVTempS_Type()
)
dupsPMINVTempS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVTempS.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVTempS.setUnits("1 Degree Celsius")
_DupsPMINVTempT_Type = Integer32
_DupsPMINVTempT_Object = MibTableColumn
dupsPMINVTempT = _DupsPMINVTempT_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 6),
    _DupsPMINVTempT_Type()
)
dupsPMINVTempT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVTempT.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVTempT.setUnits("1 Degree Celsius")
_DupsPMINVVolt1_Type = Integer32
_DupsPMINVVolt1_Object = MibTableColumn
dupsPMINVVolt1 = _DupsPMINVVolt1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 7),
    _DupsPMINVVolt1_Type()
)
dupsPMINVVolt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVVolt1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVVolt1.setUnits("0.1 Volt")
_DupsPMINVVolt2_Type = Integer32
_DupsPMINVVolt2_Object = MibTableColumn
dupsPMINVVolt2 = _DupsPMINVVolt2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 8),
    _DupsPMINVVolt2_Type()
)
dupsPMINVVolt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVVolt2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVVolt2.setUnits("0.1 Volt")
_DupsPMINVVolt3_Type = Integer32
_DupsPMINVVolt3_Object = MibTableColumn
dupsPMINVVolt3 = _DupsPMINVVolt3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 9),
    _DupsPMINVVolt3_Type()
)
dupsPMINVVolt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMINVVolt3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMINVVolt3.setUnits("0.1 Volt")


class _DupsPMStsNotExist_Type(Integer32):
    """Custom type dupsPMStsNotExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notExist", 1),
          ("existed", 2))
    )


_DupsPMStsNotExist_Type.__name__ = "Integer32"
_DupsPMStsNotExist_Object = MibTableColumn
dupsPMStsNotExist = _DupsPMStsNotExist_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 10),
    _DupsPMStsNotExist_Type()
)
dupsPMStsNotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsNotExist.setStatus("mandatory")


class _DupsPMStsOff_Type(Integer32):
    """Custom type dupsPMStsOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pmOff", 1),
          ("pmOn", 2))
    )


_DupsPMStsOff_Type.__name__ = "Integer32"
_DupsPMStsOff_Object = MibTableColumn
dupsPMStsOff = _DupsPMStsOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 11),
    _DupsPMStsOff_Type()
)
dupsPMStsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsOff.setStatus("mandatory")


class _DupsPMStsRepair_Type(Integer32):
    """Custom type dupsPMStsRepair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("repair", 1),
          ("notRepair", 2))
    )


_DupsPMStsRepair_Type.__name__ = "Integer32"
_DupsPMStsRepair_Object = MibTableColumn
dupsPMStsRepair = _DupsPMStsRepair_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 12),
    _DupsPMStsRepair_Type()
)
dupsPMStsRepair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsRepair.setStatus("mandatory")


class _DupsPMStsFaultShutdown_Type(Integer32):
    """Custom type dupsPMStsFaultShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsFaultShutdown_Type.__name__ = "Integer32"
_DupsPMStsFaultShutdown_Object = MibTableColumn
dupsPMStsFaultShutdown = _DupsPMStsFaultShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 13),
    _DupsPMStsFaultShutdown_Type()
)
dupsPMStsFaultShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsFaultShutdown.setStatus("mandatory")


class _DupsPMStsPFCFuseFail_Type(Integer32):
    """Custom type dupsPMStsPFCFuseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCFuseFail_Type.__name__ = "Integer32"
_DupsPMStsPFCFuseFail_Object = MibTableColumn
dupsPMStsPFCFuseFail = _DupsPMStsPFCFuseFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 14),
    _DupsPMStsPFCFuseFail_Type()
)
dupsPMStsPFCFuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCFuseFail.setStatus("mandatory")


class _DupsPMStsPFCOverTempWarning_Type(Integer32):
    """Custom type dupsPMStsPFCOverTempWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("normal", 2))
    )


_DupsPMStsPFCOverTempWarning_Type.__name__ = "Integer32"
_DupsPMStsPFCOverTempWarning_Object = MibTableColumn
dupsPMStsPFCOverTempWarning = _DupsPMStsPFCOverTempWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 15),
    _DupsPMStsPFCOverTempWarning_Type()
)
dupsPMStsPFCOverTempWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCOverTempWarning.setStatus("mandatory")


class _DupsPMStsPFCOverTempShutdown_Type(Integer32):
    """Custom type dupsPMStsPFCOverTempShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCOverTempShutdown_Type.__name__ = "Integer32"
_DupsPMStsPFCOverTempShutdown_Object = MibTableColumn
dupsPMStsPFCOverTempShutdown = _DupsPMStsPFCOverTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 16),
    _DupsPMStsPFCOverTempShutdown_Type()
)
dupsPMStsPFCOverTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCOverTempShutdown.setStatus("mandatory")


class _DupsPMStsPFCOverVoltWarning_Type(Integer32):
    """Custom type dupsPMStsPFCOverVoltWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("normal", 2))
    )


_DupsPMStsPFCOverVoltWarning_Type.__name__ = "Integer32"
_DupsPMStsPFCOverVoltWarning_Object = MibTableColumn
dupsPMStsPFCOverVoltWarning = _DupsPMStsPFCOverVoltWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 17),
    _DupsPMStsPFCOverVoltWarning_Type()
)
dupsPMStsPFCOverVoltWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCOverVoltWarning.setStatus("mandatory")


class _DupsPMStsPFCOverVoltShutdown_Type(Integer32):
    """Custom type dupsPMStsPFCOverVoltShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCOverVoltShutdown_Type.__name__ = "Integer32"
_DupsPMStsPFCOverVoltShutdown_Object = MibTableColumn
dupsPMStsPFCOverVoltShutdown = _DupsPMStsPFCOverVoltShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 18),
    _DupsPMStsPFCOverVoltShutdown_Type()
)
dupsPMStsPFCOverVoltShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCOverVoltShutdown.setStatus("mandatory")


class _DupsPMStsPFCUnderVoltWarning_Type(Integer32):
    """Custom type dupsPMStsPFCUnderVoltWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("normal", 2))
    )


_DupsPMStsPFCUnderVoltWarning_Type.__name__ = "Integer32"
_DupsPMStsPFCUnderVoltWarning_Object = MibTableColumn
dupsPMStsPFCUnderVoltWarning = _DupsPMStsPFCUnderVoltWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 19),
    _DupsPMStsPFCUnderVoltWarning_Type()
)
dupsPMStsPFCUnderVoltWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCUnderVoltWarning.setStatus("mandatory")


class _DupsPMStsPFCUnderVoltShutdown_Type(Integer32):
    """Custom type dupsPMStsPFCUnderVoltShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCUnderVoltShutdown_Type.__name__ = "Integer32"
_DupsPMStsPFCUnderVoltShutdown_Object = MibTableColumn
dupsPMStsPFCUnderVoltShutdown = _DupsPMStsPFCUnderVoltShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 20),
    _DupsPMStsPFCUnderVoltShutdown_Type()
)
dupsPMStsPFCUnderVoltShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCUnderVoltShutdown.setStatus("mandatory")


class _DupsPMStsPFCGeneralFault_Type(Integer32):
    """Custom type dupsPMStsPFCGeneralFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCGeneralFault_Type.__name__ = "Integer32"
_DupsPMStsPFCGeneralFault_Object = MibTableColumn
dupsPMStsPFCGeneralFault = _DupsPMStsPFCGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 21),
    _DupsPMStsPFCGeneralFault_Type()
)
dupsPMStsPFCGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCGeneralFault.setStatus("mandatory")


class _DupsPMStsPFCFanFail_Type(Integer32):
    """Custom type dupsPMStsPFCFanFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCFanFail_Type.__name__ = "Integer32"
_DupsPMStsPFCFanFail_Object = MibTableColumn
dupsPMStsPFCFanFail = _DupsPMStsPFCFanFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 22),
    _DupsPMStsPFCFanFail_Type()
)
dupsPMStsPFCFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCFanFail.setStatus("mandatory")


class _DupsPMStsPFCCurrentLimit_Type(Integer32):
    """Custom type dupsPMStsPFCCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCCurrentLimit_Type.__name__ = "Integer32"
_DupsPMStsPFCCurrentLimit_Object = MibTableColumn
dupsPMStsPFCCurrentLimit = _DupsPMStsPFCCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 23),
    _DupsPMStsPFCCurrentLimit_Type()
)
dupsPMStsPFCCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCCurrentLimit.setStatus("mandatory")


class _DupsPMStsPFCOff_Type(Integer32):
    """Custom type dupsPMStsPFCOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCOff_Type.__name__ = "Integer32"
_DupsPMStsPFCOff_Object = MibTableColumn
dupsPMStsPFCOff = _DupsPMStsPFCOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 24),
    _DupsPMStsPFCOff_Type()
)
dupsPMStsPFCOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCOff.setStatus("mandatory")


class _DupsPMStsPFCInnerCommFail_Type(Integer32):
    """Custom type dupsPMStsPFCInnerCommFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCInnerCommFail_Type.__name__ = "Integer32"
_DupsPMStsPFCInnerCommFail_Object = MibTableColumn
dupsPMStsPFCInnerCommFail = _DupsPMStsPFCInnerCommFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 25),
    _DupsPMStsPFCInnerCommFail_Type()
)
dupsPMStsPFCInnerCommFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCInnerCommFail.setStatus("mandatory")


class _DupsPMStsPFCNotCalibrated_Type(Integer32):
    """Custom type dupsPMStsPFCNotCalibrated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsPFCNotCalibrated_Type.__name__ = "Integer32"
_DupsPMStsPFCNotCalibrated_Object = MibTableColumn
dupsPMStsPFCNotCalibrated = _DupsPMStsPFCNotCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 26),
    _DupsPMStsPFCNotCalibrated_Type()
)
dupsPMStsPFCNotCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsPFCNotCalibrated.setStatus("mandatory")


class _DupsPMStsINVFuseFail_Type(Integer32):
    """Custom type dupsPMStsINVFuseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DupsPMStsINVFuseFail_Type.__name__ = "Integer32"
_DupsPMStsINVFuseFail_Object = MibTableColumn
dupsPMStsINVFuseFail = _DupsPMStsINVFuseFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 27),
    _DupsPMStsINVFuseFail_Type()
)
dupsPMStsINVFuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVFuseFail.setStatus("mandatory")


class _DupsPMStsINVOverTempWarning_Type(Integer32):
    """Custom type dupsPMStsINVOverTempWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("normal", 2))
    )


_DupsPMStsINVOverTempWarning_Type.__name__ = "Integer32"
_DupsPMStsINVOverTempWarning_Object = MibTableColumn
dupsPMStsINVOverTempWarning = _DupsPMStsINVOverTempWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 28),
    _DupsPMStsINVOverTempWarning_Type()
)
dupsPMStsINVOverTempWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVOverTempWarning.setStatus("mandatory")


class _DupsPMStsINVOverTempShutdown_Type(Integer32):
    """Custom type dupsPMStsINVOverTempShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVOverTempShutdown_Type.__name__ = "Integer32"
_DupsPMStsINVOverTempShutdown_Object = MibTableColumn
dupsPMStsINVOverTempShutdown = _DupsPMStsINVOverTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 29),
    _DupsPMStsINVOverTempShutdown_Type()
)
dupsPMStsINVOverTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVOverTempShutdown.setStatus("mandatory")


class _DupsPMStsINVFanFail_Type(Integer32):
    """Custom type dupsPMStsINVFanFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVFanFail_Type.__name__ = "Integer32"
_DupsPMStsINVFanFail_Object = MibTableColumn
dupsPMStsINVFanFail = _DupsPMStsINVFanFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 30),
    _DupsPMStsINVFanFail_Type()
)
dupsPMStsINVFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVFanFail.setStatus("mandatory")


class _DupsPMStsINVShortCircuit_Type(Integer32):
    """Custom type dupsPMStsINVShortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVShortCircuit_Type.__name__ = "Integer32"
_DupsPMStsINVShortCircuit_Object = MibTableColumn
dupsPMStsINVShortCircuit = _DupsPMStsINVShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 31),
    _DupsPMStsINVShortCircuit_Type()
)
dupsPMStsINVShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVShortCircuit.setStatus("mandatory")


class _DupsPMStsINVSTSFail_Type(Integer32):
    """Custom type dupsPMStsINVSTSFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVSTSFail_Type.__name__ = "Integer32"
_DupsPMStsINVSTSFail_Object = MibTableColumn
dupsPMStsINVSTSFail = _DupsPMStsINVSTSFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 32),
    _DupsPMStsINVSTSFail_Type()
)
dupsPMStsINVSTSFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVSTSFail.setStatus("mandatory")


class _DupsPMStsINVCircuitFail_Type(Integer32):
    """Custom type dupsPMStsINVCircuitFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVCircuitFail_Type.__name__ = "Integer32"
_DupsPMStsINVCircuitFail_Object = MibTableColumn
dupsPMStsINVCircuitFail = _DupsPMStsINVCircuitFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 33),
    _DupsPMStsINVCircuitFail_Type()
)
dupsPMStsINVCircuitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVCircuitFail.setStatus("mandatory")


class _DupsPMStsINVOverVolt_Type(Integer32):
    """Custom type dupsPMStsINVOverVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVOverVolt_Type.__name__ = "Integer32"
_DupsPMStsINVOverVolt_Object = MibTableColumn
dupsPMStsINVOverVolt = _DupsPMStsINVOverVolt_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 34),
    _DupsPMStsINVOverVolt_Type()
)
dupsPMStsINVOverVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVOverVolt.setStatus("mandatory")


class _DupsPMStsINVOverload_Type(Integer32):
    """Custom type dupsPMStsINVOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVOverload_Type.__name__ = "Integer32"
_DupsPMStsINVOverload_Object = MibTableColumn
dupsPMStsINVOverload = _DupsPMStsINVOverload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 35),
    _DupsPMStsINVOverload_Type()
)
dupsPMStsINVOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVOverload.setStatus("mandatory")


class _DupsPMStsINVInnerCommFail_Type(Integer32):
    """Custom type dupsPMStsINVInnerCommFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVInnerCommFail_Type.__name__ = "Integer32"
_DupsPMStsINVInnerCommFail_Object = MibTableColumn
dupsPMStsINVInnerCommFail = _DupsPMStsINVInnerCommFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 36),
    _DupsPMStsINVInnerCommFail_Type()
)
dupsPMStsINVInnerCommFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVInnerCommFail.setStatus("mandatory")


class _DupsPMStsINVEPO_Type(Integer32):
    """Custom type dupsPMStsINVEPO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVEPO_Type.__name__ = "Integer32"
_DupsPMStsINVEPO_Object = MibTableColumn
dupsPMStsINVEPO = _DupsPMStsINVEPO_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 37),
    _DupsPMStsINVEPO_Type()
)
dupsPMStsINVEPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVEPO.setStatus("mandatory")


class _DupsPMStsINVParallelCommFail_Type(Integer32):
    """Custom type dupsPMStsINVParallelCommFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVParallelCommFail_Type.__name__ = "Integer32"
_DupsPMStsINVParallelCommFail_Object = MibTableColumn
dupsPMStsINVParallelCommFail = _DupsPMStsINVParallelCommFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 38),
    _DupsPMStsINVParallelCommFail_Type()
)
dupsPMStsINVParallelCommFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVParallelCommFail.setStatus("mandatory")


class _DupsPMStsINVParallelFail_Type(Integer32):
    """Custom type dupsPMStsINVParallelFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVParallelFail_Type.__name__ = "Integer32"
_DupsPMStsINVParallelFail_Object = MibTableColumn
dupsPMStsINVParallelFail = _DupsPMStsINVParallelFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 39),
    _DupsPMStsINVParallelFail_Type()
)
dupsPMStsINVParallelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVParallelFail.setStatus("mandatory")


class _DupsPMStsINVSTSOn_Type(Integer32):
    """Custom type dupsPMStsINVSTSOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DupsPMStsINVSTSOn_Type.__name__ = "Integer32"
_DupsPMStsINVSTSOn_Object = MibTableColumn
dupsPMStsINVSTSOn = _DupsPMStsINVSTSOn_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 40),
    _DupsPMStsINVSTSOn_Type()
)
dupsPMStsINVSTSOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVSTSOn.setStatus("mandatory")


class _DupsPMStsINVNotCalibrated_Type(Integer32):
    """Custom type dupsPMStsINVNotCalibrated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsINVNotCalibrated_Type.__name__ = "Integer32"
_DupsPMStsINVNotCalibrated_Object = MibTableColumn
dupsPMStsINVNotCalibrated = _DupsPMStsINVNotCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 41),
    _DupsPMStsINVNotCalibrated_Type()
)
dupsPMStsINVNotCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsINVNotCalibrated.setStatus("mandatory")


class _DupsPMStsChargerFail_Type(Integer32):
    """Custom type dupsPMStsChargerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DupsPMStsChargerFail_Type.__name__ = "Integer32"
_DupsPMStsChargerFail_Object = MibTableColumn
dupsPMStsChargerFail = _DupsPMStsChargerFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 42),
    _DupsPMStsChargerFail_Type()
)
dupsPMStsChargerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMStsChargerFail.setStatus("mandatory")


class _DupsPMSummaryStatus_Type(Integer32):
    """Custom type dupsPMSummaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_DupsPMSummaryStatus_Type.__name__ = "Integer32"
_DupsPMSummaryStatus_Object = MibTableColumn
dupsPMSummaryStatus = _DupsPMSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 43),
    _DupsPMSummaryStatus_Type()
)
dupsPMSummaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMSummaryStatus.setStatus("mandatory")
_DupsPMPFCTempR_Type = Integer32
_DupsPMPFCTempR_Object = MibTableColumn
dupsPMPFCTempR = _DupsPMPFCTempR_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 44),
    _DupsPMPFCTempR_Type()
)
dupsPMPFCTempR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMPFCTempR.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMPFCTempR.setUnits("1 Degree Celsius")
_DupsPMPFCTempS_Type = Integer32
_DupsPMPFCTempS_Object = MibTableColumn
dupsPMPFCTempS = _DupsPMPFCTempS_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 45),
    _DupsPMPFCTempS_Type()
)
dupsPMPFCTempS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMPFCTempS.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMPFCTempS.setUnits("1 Degree Celsius")
_DupsPMPFCTempT_Type = Integer32
_DupsPMPFCTempT_Object = MibTableColumn
dupsPMPFCTempT = _DupsPMPFCTempT_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 10, 6, 1, 46),
    _DupsPMPFCTempT_Type()
)
dupsPMPFCTempT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsPMPFCTempT.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsPMPFCTempT.setUnits("1 Degree Celsius")
_DupsTrapArgs_ObjectIdentity = ObjectIdentity
dupsTrapArgs = _DupsTrapArgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 11)
)
_DupsDescription_Type = DisplayString
_DupsDescription_Object = MibScalar
dupsDescription = _DupsDescription_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 11, 1),
    _DupsDescription_Type()
)
dupsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsDescription.setStatus("mandatory")
_DupsTimeTicks_Type = TimeTicks
_DupsTimeTicks_Object = MibScalar
dupsTimeTicks = _DupsTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 11, 2),
    _DupsTimeTicks_Type()
)
dupsTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTimeTicks.setStatus("mandatory")
_DupsParallel_ObjectIdentity = ObjectIdentity
dupsParallel = _DupsParallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12)
)
_DupsParallelRatingVA_Type = Integer32
_DupsParallelRatingVA_Object = MibScalar
dupsParallelRatingVA = _DupsParallelRatingVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 1),
    _DupsParallelRatingVA_Type()
)
dupsParallelRatingVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelRatingVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelRatingVA.setUnits("1 VA")
_DupsParallelRatingPower_Type = Integer32
_DupsParallelRatingPower_Object = MibScalar
dupsParallelRatingPower = _DupsParallelRatingPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 2),
    _DupsParallelRatingPower_Type()
)
dupsParallelRatingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelRatingPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelRatingPower.setUnits("1 Watt")
_DupsParallelInCurrent1_Type = Integer32
_DupsParallelInCurrent1_Object = MibScalar
dupsParallelInCurrent1 = _DupsParallelInCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 3),
    _DupsParallelInCurrent1_Type()
)
dupsParallelInCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInCurrent1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInCurrent1.setUnits("0.1 Amp")
_DupsParallelInCurrent2_Type = Integer32
_DupsParallelInCurrent2_Object = MibScalar
dupsParallelInCurrent2 = _DupsParallelInCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 4),
    _DupsParallelInCurrent2_Type()
)
dupsParallelInCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInCurrent2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInCurrent2.setUnits("0.1 Amp")
_DupsParallelInCurrent3_Type = Integer32
_DupsParallelInCurrent3_Object = MibScalar
dupsParallelInCurrent3 = _DupsParallelInCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 5),
    _DupsParallelInCurrent3_Type()
)
dupsParallelInCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInCurrent3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInCurrent3.setUnits("0.1 Amp")
_DupsParallelOutCurrent1_Type = Integer32
_DupsParallelOutCurrent1_Object = MibScalar
dupsParallelOutCurrent1 = _DupsParallelOutCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 6),
    _DupsParallelOutCurrent1_Type()
)
dupsParallelOutCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutCurrent1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutCurrent1.setUnits("0.1 Amp")
_DupsParallelOutCurrent2_Type = Integer32
_DupsParallelOutCurrent2_Object = MibScalar
dupsParallelOutCurrent2 = _DupsParallelOutCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 7),
    _DupsParallelOutCurrent2_Type()
)
dupsParallelOutCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutCurrent2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutCurrent2.setUnits("0.1 Amp")
_DupsParallelOutCurrent3_Type = Integer32
_DupsParallelOutCurrent3_Object = MibScalar
dupsParallelOutCurrent3 = _DupsParallelOutCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 8),
    _DupsParallelOutCurrent3_Type()
)
dupsParallelOutCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutCurrent3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutCurrent3.setUnits("0.1 Amp")
_DupsParallelOutPower1_Type = Integer32
_DupsParallelOutPower1_Object = MibScalar
dupsParallelOutPower1 = _DupsParallelOutPower1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 9),
    _DupsParallelOutPower1_Type()
)
dupsParallelOutPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutPower1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutPower1.setUnits("1 Watt")
_DupsParallelOutPower2_Type = Integer32
_DupsParallelOutPower2_Object = MibScalar
dupsParallelOutPower2 = _DupsParallelOutPower2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 10),
    _DupsParallelOutPower2_Type()
)
dupsParallelOutPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutPower2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutPower2.setUnits("1 Watt")
_DupsParallelOutPower3_Type = Integer32
_DupsParallelOutPower3_Object = MibScalar
dupsParallelOutPower3 = _DupsParallelOutPower3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 11),
    _DupsParallelOutPower3_Type()
)
dupsParallelOutPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutPower3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutPower3.setUnits("1 Watt")
_DupsParallelInEnergy1_Type = Integer32
_DupsParallelInEnergy1_Object = MibScalar
dupsParallelInEnergy1 = _DupsParallelInEnergy1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 12),
    _DupsParallelInEnergy1_Type()
)
dupsParallelInEnergy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInEnergy1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInEnergy1.setUnits("1 kWh")
_DupsParallelInEnergy2_Type = Integer32
_DupsParallelInEnergy2_Object = MibScalar
dupsParallelInEnergy2 = _DupsParallelInEnergy2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 13),
    _DupsParallelInEnergy2_Type()
)
dupsParallelInEnergy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInEnergy2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInEnergy2.setUnits("1 kWh")
_DupsParallelInEnergy3_Type = Integer32
_DupsParallelInEnergy3_Object = MibScalar
dupsParallelInEnergy3 = _DupsParallelInEnergy3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 14),
    _DupsParallelInEnergy3_Type()
)
dupsParallelInEnergy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInEnergy3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInEnergy3.setUnits("1 kWh")
_DupsParallelInEnergyTotal_Type = Integer32
_DupsParallelInEnergyTotal_Object = MibScalar
dupsParallelInEnergyTotal = _DupsParallelInEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 15),
    _DupsParallelInEnergyTotal_Type()
)
dupsParallelInEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelInEnergyTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelInEnergyTotal.setUnits("1 kWh")
_DupsParallelOutEnergy1_Type = Integer32
_DupsParallelOutEnergy1_Object = MibScalar
dupsParallelOutEnergy1 = _DupsParallelOutEnergy1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 16),
    _DupsParallelOutEnergy1_Type()
)
dupsParallelOutEnergy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutEnergy1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutEnergy1.setUnits("1 kWh")
_DupsParallelOutEnergy2_Type = Integer32
_DupsParallelOutEnergy2_Object = MibScalar
dupsParallelOutEnergy2 = _DupsParallelOutEnergy2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 17),
    _DupsParallelOutEnergy2_Type()
)
dupsParallelOutEnergy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutEnergy2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutEnergy2.setUnits("1 kWh")
_DupsParallelOutEnergy3_Type = Integer32
_DupsParallelOutEnergy3_Object = MibScalar
dupsParallelOutEnergy3 = _DupsParallelOutEnergy3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 18),
    _DupsParallelOutEnergy3_Type()
)
dupsParallelOutEnergy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutEnergy3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutEnergy3.setUnits("1 kWh")
_DupsParallelOutEnergyTotal_Type = Integer32
_DupsParallelOutEnergyTotal_Object = MibScalar
dupsParallelOutEnergyTotal = _DupsParallelOutEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 12, 19),
    _DupsParallelOutEnergyTotal_Type()
)
dupsParallelOutEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsParallelOutEnergyTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsParallelOutEnergyTotal.setUnits("1 kWh")
_DupsIntegrated_ObjectIdentity = ObjectIdentity
dupsIntegrated = _DupsIntegrated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 13)
)


class _DupsIntegratedParallel_Type(Integer32):
    """Custom type dupsIntegratedParallel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("parallel", 1),
          ("noParallel", 2))
    )


_DupsIntegratedParallel_Type.__name__ = "Integer32"
_DupsIntegratedParallel_Object = MibScalar
dupsIntegratedParallel = _DupsIntegratedParallel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 13, 1),
    _DupsIntegratedParallel_Type()
)
dupsIntegratedParallel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIntegratedParallel.setStatus("mandatory")


class _DupsIntegratedDryInput1_Type(Integer32):
    """Custom type dupsIntegratedDryInput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DupsIntegratedDryInput1_Type.__name__ = "Integer32"
_DupsIntegratedDryInput1_Object = MibScalar
dupsIntegratedDryInput1 = _DupsIntegratedDryInput1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 13, 2),
    _DupsIntegratedDryInput1_Type()
)
dupsIntegratedDryInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIntegratedDryInput1.setStatus("mandatory")


class _DupsIntegratedDryInput2_Type(Integer32):
    """Custom type dupsIntegratedDryInput2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DupsIntegratedDryInput2_Type.__name__ = "Integer32"
_DupsIntegratedDryInput2_Object = MibScalar
dupsIntegratedDryInput2 = _DupsIntegratedDryInput2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 13, 3),
    _DupsIntegratedDryInput2_Type()
)
dupsIntegratedDryInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIntegratedDryInput2.setStatus("mandatory")


class _DupsIntegratedDryInput3_Type(Integer32):
    """Custom type dupsIntegratedDryInput3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DupsIntegratedDryInput3_Type.__name__ = "Integer32"
_DupsIntegratedDryInput3_Object = MibScalar
dupsIntegratedDryInput3 = _DupsIntegratedDryInput3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 13, 4),
    _DupsIntegratedDryInput3_Type()
)
dupsIntegratedDryInput3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIntegratedDryInput3.setStatus("mandatory")


class _DupsIntegratedDryInput4_Type(Integer32):
    """Custom type dupsIntegratedDryInput4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DupsIntegratedDryInput4_Type.__name__ = "Integer32"
_DupsIntegratedDryInput4_Object = MibScalar
dupsIntegratedDryInput4 = _DupsIntegratedDryInput4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 13, 5),
    _DupsIntegratedDryInput4_Type()
)
dupsIntegratedDryInput4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIntegratedDryInput4.setStatus("mandatory")
_DupsTraps_ObjectIdentity = ObjectIdentity
dupsTraps = _DupsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20)
)

# Managed Objects groups


# Notification objects

dupsCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 1)
)
dupsCommunicationLost.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsCommunicationLost.setStatus(
        ""
    )

dupsCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 2)
)
dupsCommunicationEstablished.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsCommunicationEstablished.setStatus(
        ""
    )

dupsPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 3)
)
dupsPowerFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsPowerFail.setStatus(
        ""
    )

dupsPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 4)
)
dupsPowerRestored.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsPowerRestored.setStatus(
        ""
    )

dupsLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 5)
)
dupsLowBattery.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsLowBattery.setStatus(
        ""
    )

dupsReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 6)
)
dupsReturnFromLowBattery.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromLowBattery.setStatus(
        ""
    )

dupsLoadOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 7)
)
dupsLoadOnBypass.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsLoadOnBypass.setStatus(
        ""
    )

dupsNoLongerLoadOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 8)
)
dupsNoLongerLoadOnBypass.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsNoLongerLoadOnBypass.setStatus(
        ""
    )

dupsUPSFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 9)
)
dupsUPSFault.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsUPSFault.setStatus(
        ""
    )

dupsReturnFromUPSFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 10)
)
dupsReturnFromUPSFault.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromUPSFault.setStatus(
        ""
    )

dupsBatteryGroundFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 11)
)
dupsBatteryGroundFault.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsBatteryGroundFault.setStatus(
        ""
    )

dupsNoLongerBatteryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 12)
)
dupsNoLongerBatteryFault.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsNoLongerBatteryFault.setStatus(
        ""
    )

dupsTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 13)
)
dupsTestInProgress.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsTestInProgress.setStatus(
        ""
    )

dupsBatteryTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 14)
)
dupsBatteryTestFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsBatteryTestFail.setStatus(
        ""
    )

dupsFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 15)
)
dupsFuseFailure.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsFuseFailure.setStatus(
        ""
    )

dupsFuseRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 16)
)
dupsFuseRecovered.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsFuseRecovered.setStatus(
        ""
    )

dupsOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 17)
)
dupsOutputOverload.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOutputOverload.setStatus(
        ""
    )

dupsNoLongerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 18)
)
dupsNoLongerOverload.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsNoLongerOverload.setStatus(
        ""
    )

dupsInverterAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 19)
)
dupsInverterAbnormal.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsInverterAbnormal.setStatus(
        ""
    )

dupsInverterRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 20)
)
dupsInverterRecovered.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsInverterRecovered.setStatus(
        ""
    )

dupsSmartShutdownInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 21)
)
dupsSmartShutdownInit.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsSmartShutdownInit.setStatus(
        ""
    )

dupsCancelShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 22)
)
dupsCancelShutdown.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsCancelShutdown.setStatus(
        ""
    )

dupsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 23)
)
dupsTestCompleted.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsTestCompleted.setStatus(
        ""
    )

dupsEPOON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 24)
)
dupsEPOON.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsEPOON.setStatus(
        ""
    )

dupsEPOOFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 25)
)
dupsEPOOFF.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsEPOOFF.setStatus(
        ""
    )

dupsTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 26)
)
dupsTemperatureAlarm.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsTemperatureAlarm.setStatus(
        ""
    )

dupsTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 27)
)
dupsTemperatureNormal.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsTemperatureNormal.setStatus(
        ""
    )

dupsBattReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 28)
)
dupsBattReplace.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsBattReplace.setStatus(
        ""
    )

dupsReturnFromBattReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 29)
)
dupsReturnFromBattReplace.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromBattReplace.setStatus(
        ""
    )

dupsOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 30)
)
dupsOutputOff.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOutputOff.setStatus(
        ""
    )

dupsReturnFromOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 31)
)
dupsReturnFromOutputOff.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromOutputOff.setStatus(
        ""
    )

dupsShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 32)
)
dupsShutdown.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsShutdown.setStatus(
        ""
    )

dupsReturnFromShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 33)
)
dupsReturnFromShutdown.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromShutdown.setStatus(
        ""
    )

dupsChargerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 34)
)
dupsChargerFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsChargerFail.setStatus(
        ""
    )

dupsReturnFromChargerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 35)
)
dupsReturnFromChargerFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromChargerFail.setStatus(
        ""
    )

dupsOnStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 36)
)
dupsOnStandby.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOnStandby.setStatus(
        ""
    )

dupsReturnFromStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 37)
)
dupsReturnFromStandby.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromStandby.setStatus(
        ""
    )

dupsFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 38)
)
dupsFanFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsFanFail.setStatus(
        ""
    )

dupsReturnFromFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 39)
)
dupsReturnFromFanFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromFanFail.setStatus(
        ""
    )

dupsOnEconomic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 40)
)
dupsOnEconomic.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOnEconomic.setStatus(
        ""
    )

dupsReturnFromEconomic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 41)
)
dupsReturnFromEconomic.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromEconomic.setStatus(
        ""
    )

dupsPowerModuleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 42)
)
dupsPowerModuleFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsPowerModuleFail.setStatus(
        ""
    )

dupsReturnFromPowerModuleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 43)
)
dupsReturnFromPowerModuleFail.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromPowerModuleFail.setStatus(
        ""
    )

dupsOutputBreakerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 44)
)
dupsOutputBreakerOff.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOutputBreakerOff.setStatus(
        ""
    )

dupsReturnFromOutputBreakerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 45)
)
dupsReturnFromOutputBreakerOff.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromOutputBreakerOff.setStatus(
        ""
    )

dupsBatteryDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 46)
)
dupsBatteryDepleted.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsBatteryDepleted.setStatus(
        ""
    )

dupsReturnFromBatteryDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 47)
)
dupsReturnFromBatteryDepleted.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromBatteryDepleted.setStatus(
        ""
    )

dupsLoadOnManualBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 48)
)
dupsLoadOnManualBypass.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsLoadOnManualBypass.setStatus(
        ""
    )

dupsNoLongerLoadOnManualBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 49)
)
dupsNoLongerLoadOnManualBypass.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsNoLongerLoadOnManualBypass.setStatus(
        ""
    )

dupsBatteryBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 50)
)
dupsBatteryBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsBatteryBreakerOpen.setStatus(
        ""
    )

dupsReturnFromBatteryBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 51)
)
dupsReturnFromBatteryBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromBatteryBreakerOpen.setStatus(
        ""
    )

dupsOutletBankOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 52)
)
dupsOutletBankOn.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOutletBankOn.setStatus(
        ""
    )

dupsOutletBankOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 53)
)
dupsOutletBankOff.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsOutletBankOff.setStatus(
        ""
    )

dupsRedundancyLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 54)
)
dupsRedundancyLoss.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsRedundancyLoss.setStatus(
        ""
    )

dupsReturnFromRedundancyLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 55)
)
dupsReturnFromRedundancyLoss.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromRedundancyLoss.setStatus(
        ""
    )

dupsPhaseAsynchronous = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 56)
)
dupsPhaseAsynchronous.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsPhaseAsynchronous.setStatus(
        ""
    )

dupsReturnFromPhaseAsynchronous = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 57)
)
dupsReturnFromPhaseAsynchronous.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromPhaseAsynchronous.setStatus(
        ""
    )

dupsRectifierAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 58)
)
dupsRectifierAbnormal.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsRectifierAbnormal.setStatus(
        ""
    )

dupsReturnFromRectifierAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 59)
)
dupsReturnFromRectifierAbnormal.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromRectifierAbnormal.setStatus(
        ""
    )

dupsBypassBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 60)
)
dupsBypassBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsBypassBreakerOpen.setStatus(
        ""
    )

dupsReturnFromBypassBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 61)
)
dupsReturnFromBypassBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromBypassBreakerOpen.setStatus(
        ""
    )

dupsMainInputBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 62)
)
dupsMainInputBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsMainInputBreakerOpen.setStatus(
        ""
    )

dupsReturnFromMainInputBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 63)
)
dupsReturnFromMainInputBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromMainInputBreakerOpen.setStatus(
        ""
    )

dupsManualBypassBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 64)
)
dupsManualBypassBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsManualBypassBreakerOpen.setStatus(
        ""
    )

dupsReturnFromManualBypassBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 5, 20, 0, 65)
)
dupsReturnFromManualBypassBreakerOpen.setObjects(
      *(("DeltaUPSv5-MIB", "dupsTimeTicks"),
        ("DeltaUPSv5-MIB", "dupsDescription"))
)
if mibBuilder.loadTexts:
    dupsReturnFromManualBypassBreakerOpen.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaUPSv5-MIB",
    **{"delta": delta,
       "ups": ups,
       "upsv5": upsv5,
       "dupsIdent": dupsIdent,
       "dupsIdentManufacturer": dupsIdentManufacturer,
       "dupsIdentModel": dupsIdentModel,
       "dupsIdentUPSSoftwareVersion": dupsIdentUPSSoftwareVersion,
       "dupsIdentAgentSoftwareVersion": dupsIdentAgentSoftwareVersion,
       "dupsIdentName": dupsIdentName,
       "dupsAttachedDevices": dupsAttachedDevices,
       "dupsRatingOutputVA": dupsRatingOutputVA,
       "dupsRatingOutputVoltage": dupsRatingOutputVoltage,
       "dupsRatingOutputFrequency": dupsRatingOutputFrequency,
       "dupsRatingInputVoltage": dupsRatingInputVoltage,
       "dupsRatingInputFrequency": dupsRatingInputFrequency,
       "dupsRatingBatteryVoltage": dupsRatingBatteryVoltage,
       "dupsLowTransferVoltUpBound": dupsLowTransferVoltUpBound,
       "dupsLowTransferVoltLowBound": dupsLowTransferVoltLowBound,
       "dupsHighTransferVoltUpBound": dupsHighTransferVoltUpBound,
       "dupsHighTransferVoltLowBound": dupsHighTransferVoltLowBound,
       "dupsLowBattTime": dupsLowBattTime,
       "dupsOutletRelays": dupsOutletRelays,
       "dupsType": dupsType,
       "dupsControl": dupsControl,
       "dupsShutdownType": dupsShutdownType,
       "dupsAutoReboot": dupsAutoReboot,
       "dupsShutdownAction": dupsShutdownAction,
       "dupsRestartAction": dupsRestartAction,
       "dupsSetOutletRelay": dupsSetOutletRelay,
       "dupsRelayOffDelay": dupsRelayOffDelay,
       "dupsRelayOnDelay": dupsRelayOnDelay,
       "dupsSmartShutdown": dupsSmartShutdown,
       "dupsClearEnergy": dupsClearEnergy,
       "dupsConfig": dupsConfig,
       "dupsConfigBuzzerAlarm": dupsConfigBuzzerAlarm,
       "dupsConfigBuzzerState": dupsConfigBuzzerState,
       "dupsConfigSensitivity": dupsConfigSensitivity,
       "dupsConfigLowVoltageTransferPoint": dupsConfigLowVoltageTransferPoint,
       "dupsConfigHighVoltageTransferPoint": dupsConfigHighVoltageTransferPoint,
       "dupsConfigUPSBootDelay": dupsConfigUPSBootDelay,
       "dupsConfigExternalBatteryPack": dupsConfigExternalBatteryPack,
       "dupsConfigSmartShutdownOSDelay": dupsConfigSmartShutdownOSDelay,
       "dupsConfigSmartShutdownUPSDelay": dupsConfigSmartShutdownUPSDelay,
       "dupsConfigEconomicMode": dupsConfigEconomicMode,
       "dupsInput": dupsInput,
       "dupsInputNumLines": dupsInputNumLines,
       "dupsInputFrequency1": dupsInputFrequency1,
       "dupsInputVoltage1": dupsInputVoltage1,
       "dupsInputVoltage12": dupsInputVoltage12,
       "dupsInputCurrent1": dupsInputCurrent1,
       "dupsInputPower1": dupsInputPower1,
       "dupsInputFrequency2": dupsInputFrequency2,
       "dupsInputVoltage2": dupsInputVoltage2,
       "dupsInputVoltage23": dupsInputVoltage23,
       "dupsInputCurrent2": dupsInputCurrent2,
       "dupsInputPower2": dupsInputPower2,
       "dupsInputFrequency3": dupsInputFrequency3,
       "dupsInputVoltage3": dupsInputVoltage3,
       "dupsInputVoltage31": dupsInputVoltage31,
       "dupsInputCurrent3": dupsInputCurrent3,
       "dupsInputPower3": dupsInputPower3,
       "dupsInputEnergy1": dupsInputEnergy1,
       "dupsInputEnergy2": dupsInputEnergy2,
       "dupsInputEnergy3": dupsInputEnergy3,
       "dupsInputEnergyTotal": dupsInputEnergyTotal,
       "dupsInputLineFailCause": dupsInputLineFailCause,
       "dupsInputBadStatus": dupsInputBadStatus,
       "dupsOutput": dupsOutput,
       "dupsOutputSource": dupsOutputSource,
       "dupsOutputFrequency": dupsOutputFrequency,
       "dupsOutputNumLines": dupsOutputNumLines,
       "dupsOutputVoltage1": dupsOutputVoltage1,
       "dupsOutputVoltage12": dupsOutputVoltage12,
       "dupsOutputCurrent1": dupsOutputCurrent1,
       "dupsOutputPower1": dupsOutputPower1,
       "dupsOutputLoad1": dupsOutputLoad1,
       "dupsOutputVoltage2": dupsOutputVoltage2,
       "dupsOutputVoltage23": dupsOutputVoltage23,
       "dupsOutputCurrent2": dupsOutputCurrent2,
       "dupsOutputPower2": dupsOutputPower2,
       "dupsOutputLoad2": dupsOutputLoad2,
       "dupsOutputVoltage3": dupsOutputVoltage3,
       "dupsOutputVoltage31": dupsOutputVoltage31,
       "dupsOutputCurrent3": dupsOutputCurrent3,
       "dupsOutputPower3": dupsOutputPower3,
       "dupsOutputLoad3": dupsOutputLoad3,
       "dupsOutputTotalActivePower": dupsOutputTotalActivePower,
       "dupsOutputTotalApparentPower": dupsOutputTotalApparentPower,
       "dupsOutputTotalPowerFactor": dupsOutputTotalPowerFactor,
       "dupsOutputEnergy1": dupsOutputEnergy1,
       "dupsOutputEnergy2": dupsOutputEnergy2,
       "dupsOutputEnergy3": dupsOutputEnergy3,
       "dupsOutputEnergyTotal": dupsOutputEnergyTotal,
       "dupsBypass": dupsBypass,
       "dupsBypassFrequency": dupsBypassFrequency,
       "dupsBypassNumLines": dupsBypassNumLines,
       "dupsBypassVoltage1": dupsBypassVoltage1,
       "dupsBypassVoltage12": dupsBypassVoltage12,
       "dupsBypassCurrent1": dupsBypassCurrent1,
       "dupsBypassPower1": dupsBypassPower1,
       "dupsBypassVoltage2": dupsBypassVoltage2,
       "dupsBypassVoltage23": dupsBypassVoltage23,
       "dupsBypassCurrent2": dupsBypassCurrent2,
       "dupsBypassPower2": dupsBypassPower2,
       "dupsBypassVoltage3": dupsBypassVoltage3,
       "dupsBypassVoltage31": dupsBypassVoltage31,
       "dupsBypassCurrent3": dupsBypassCurrent3,
       "dupsBypassPower3": dupsBypassPower3,
       "dupsBypassSTSTemperature": dupsBypassSTSTemperature,
       "dupsBattery": dupsBattery,
       "dupsBatteryCondition": dupsBatteryCondition,
       "dupsBatteryStatus": dupsBatteryStatus,
       "dupsBatteryCharge": dupsBatteryCharge,
       "dupsSecondsOnBattery": dupsSecondsOnBattery,
       "dupsBatteryEstimatedTime": dupsBatteryEstimatedTime,
       "dupsBatteryPosVoltage": dupsBatteryPosVoltage,
       "dupsBatteryNegVoltage": dupsBatteryNegVoltage,
       "dupsBatteryPosCurrent": dupsBatteryPosCurrent,
       "dupsBatteryNegCurrent": dupsBatteryNegCurrent,
       "dupsBatteryPosCapacity": dupsBatteryPosCapacity,
       "dupsBatteryNegCapacity": dupsBatteryNegCapacity,
       "dupsTemperature": dupsTemperature,
       "dupsLastReplaceDate": dupsLastReplaceDate,
       "dupsNextReplaceDate": dupsNextReplaceDate,
       "dupsBatteryBreaker": dupsBatteryBreaker,
       "dupsBatteryCab1Tempurature": dupsBatteryCab1Tempurature,
       "dupsBatteryCab2Tempurature": dupsBatteryCab2Tempurature,
       "dupsBatteryCab3Tempurature": dupsBatteryCab3Tempurature,
       "dupsBatteryCab4Tempurature": dupsBatteryCab4Tempurature,
       "dupsTest": dupsTest,
       "dupsTestType": dupsTestType,
       "dupsTestResultsSummary": dupsTestResultsSummary,
       "dupsTestResultsDetail": dupsTestResultsDetail,
       "dupsGeneratorTest": dupsGeneratorTest,
       "dupsGeneratorTestStatus": dupsGeneratorTestStatus,
       "dupsAlarm": dupsAlarm,
       "dupsAlarmDisconnect": dupsAlarmDisconnect,
       "dupsAlarmInputOutOfRange": dupsAlarmInputOutOfRange,
       "dupsAlarmBatteryLow": dupsAlarmBatteryLow,
       "dupsAlarmLoadOnBypass": dupsAlarmLoadOnBypass,
       "dupsAlarmOther": dupsAlarmOther,
       "dupsAlarmBatteryGroundFault": dupsAlarmBatteryGroundFault,
       "dupsAlarmTestInProgress": dupsAlarmTestInProgress,
       "dupsAlarmBatteryTestFail": dupsAlarmBatteryTestFail,
       "dupsAlarmFuseFailure": dupsAlarmFuseFailure,
       "dupsAlarmOutputOverload": dupsAlarmOutputOverload,
       "dupsAlarmInverterAbnormal": dupsAlarmInverterAbnormal,
       "dupsAlarmLoadOnReserve": dupsAlarmLoadOnReserve,
       "dupsAlarmTemperature": dupsAlarmTemperature,
       "dupsAlarmBypassOutOfRange": dupsAlarmBypassOutOfRange,
       "dupsAlarmStandby": dupsAlarmStandby,
       "dupsAlarmChargerFail": dupsAlarmChargerFail,
       "dupsAlarmFanFail": dupsAlarmFanFail,
       "dupsAlarmEconomicMode": dupsAlarmEconomicMode,
       "dupsAlarmOutputOff": dupsAlarmOutputOff,
       "dupsAlarmSmartShutdown": dupsAlarmSmartShutdown,
       "dupsAlarmEmergencyPowerOff": dupsAlarmEmergencyPowerOff,
       "dupsAlarmUPSShutdown": dupsAlarmUPSShutdown,
       "dupsAlarmEPO": dupsAlarmEPO,
       "dupsAlarmOutVoltOverLimit": dupsAlarmOutVoltOverLimit,
       "dupsAlarmOutVoltUnderLimit": dupsAlarmOutVoltUnderLimit,
       "dupsAlarmPowerModule": dupsAlarmPowerModule,
       "dupsAlarmOutputBreaker": dupsAlarmOutputBreaker,
       "dupsAlarmOutletBank1Breaker": dupsAlarmOutletBank1Breaker,
       "dupsAlarmOutletBank2Breaker": dupsAlarmOutletBank2Breaker,
       "dupsAlarmOutletBank3Breaker": dupsAlarmOutletBank3Breaker,
       "dupsAlarmOutletBank4Breaker": dupsAlarmOutletBank4Breaker,
       "dupsAlarmSummary": dupsAlarmSummary,
       "dupsAlarmRedundancyLoss": dupsAlarmRedundancyLoss,
       "dupsAlarmPhaseAsynchronous": dupsAlarmPhaseAsynchronous,
       "dupsAlarmRectifierAbnormal": dupsAlarmRectifierAbnormal,
       "dupsAlarmBypassBreakerOpen": dupsAlarmBypassBreakerOpen,
       "dupsAlarmMainInputBreakerOpen": dupsAlarmMainInputBreakerOpen,
       "dupsAlarmManualBypassBreaker": dupsAlarmManualBypassBreaker,
       "dupsPowerModule": dupsPowerModule,
       "dupsPMBypassInputAlarm": dupsPMBypassInputAlarm,
       "dupsPMBypassPhaseAlarm": dupsPMBypassPhaseAlarm,
       "dupsPMBypassSTSOverloadAlarm": dupsPMBypassSTSOverloadAlarm,
       "dupsPMBypassSTSOverTempAlarm": dupsPMBypassSTSOverTempAlarm,
       "dupsPMBypassSTSFailAlarm": dupsPMBypassSTSFailAlarm,
       "dupsPMTable": dupsPMTable,
       "dupsPMEntry": dupsPMEntry,
       "dupsPMID": dupsPMID,
       "dupsPMPFCTemp": dupsPMPFCTemp,
       "dupsPMINVTemp": dupsPMINVTemp,
       "dupsPMINVTempR": dupsPMINVTempR,
       "dupsPMINVTempS": dupsPMINVTempS,
       "dupsPMINVTempT": dupsPMINVTempT,
       "dupsPMINVVolt1": dupsPMINVVolt1,
       "dupsPMINVVolt2": dupsPMINVVolt2,
       "dupsPMINVVolt3": dupsPMINVVolt3,
       "dupsPMStsNotExist": dupsPMStsNotExist,
       "dupsPMStsOff": dupsPMStsOff,
       "dupsPMStsRepair": dupsPMStsRepair,
       "dupsPMStsFaultShutdown": dupsPMStsFaultShutdown,
       "dupsPMStsPFCFuseFail": dupsPMStsPFCFuseFail,
       "dupsPMStsPFCOverTempWarning": dupsPMStsPFCOverTempWarning,
       "dupsPMStsPFCOverTempShutdown": dupsPMStsPFCOverTempShutdown,
       "dupsPMStsPFCOverVoltWarning": dupsPMStsPFCOverVoltWarning,
       "dupsPMStsPFCOverVoltShutdown": dupsPMStsPFCOverVoltShutdown,
       "dupsPMStsPFCUnderVoltWarning": dupsPMStsPFCUnderVoltWarning,
       "dupsPMStsPFCUnderVoltShutdown": dupsPMStsPFCUnderVoltShutdown,
       "dupsPMStsPFCGeneralFault": dupsPMStsPFCGeneralFault,
       "dupsPMStsPFCFanFail": dupsPMStsPFCFanFail,
       "dupsPMStsPFCCurrentLimit": dupsPMStsPFCCurrentLimit,
       "dupsPMStsPFCOff": dupsPMStsPFCOff,
       "dupsPMStsPFCInnerCommFail": dupsPMStsPFCInnerCommFail,
       "dupsPMStsPFCNotCalibrated": dupsPMStsPFCNotCalibrated,
       "dupsPMStsINVFuseFail": dupsPMStsINVFuseFail,
       "dupsPMStsINVOverTempWarning": dupsPMStsINVOverTempWarning,
       "dupsPMStsINVOverTempShutdown": dupsPMStsINVOverTempShutdown,
       "dupsPMStsINVFanFail": dupsPMStsINVFanFail,
       "dupsPMStsINVShortCircuit": dupsPMStsINVShortCircuit,
       "dupsPMStsINVSTSFail": dupsPMStsINVSTSFail,
       "dupsPMStsINVCircuitFail": dupsPMStsINVCircuitFail,
       "dupsPMStsINVOverVolt": dupsPMStsINVOverVolt,
       "dupsPMStsINVOverload": dupsPMStsINVOverload,
       "dupsPMStsINVInnerCommFail": dupsPMStsINVInnerCommFail,
       "dupsPMStsINVEPO": dupsPMStsINVEPO,
       "dupsPMStsINVParallelCommFail": dupsPMStsINVParallelCommFail,
       "dupsPMStsINVParallelFail": dupsPMStsINVParallelFail,
       "dupsPMStsINVSTSOn": dupsPMStsINVSTSOn,
       "dupsPMStsINVNotCalibrated": dupsPMStsINVNotCalibrated,
       "dupsPMStsChargerFail": dupsPMStsChargerFail,
       "dupsPMSummaryStatus": dupsPMSummaryStatus,
       "dupsPMPFCTempR": dupsPMPFCTempR,
       "dupsPMPFCTempS": dupsPMPFCTempS,
       "dupsPMPFCTempT": dupsPMPFCTempT,
       "dupsTrapArgs": dupsTrapArgs,
       "dupsDescription": dupsDescription,
       "dupsTimeTicks": dupsTimeTicks,
       "dupsParallel": dupsParallel,
       "dupsParallelRatingVA": dupsParallelRatingVA,
       "dupsParallelRatingPower": dupsParallelRatingPower,
       "dupsParallelInCurrent1": dupsParallelInCurrent1,
       "dupsParallelInCurrent2": dupsParallelInCurrent2,
       "dupsParallelInCurrent3": dupsParallelInCurrent3,
       "dupsParallelOutCurrent1": dupsParallelOutCurrent1,
       "dupsParallelOutCurrent2": dupsParallelOutCurrent2,
       "dupsParallelOutCurrent3": dupsParallelOutCurrent3,
       "dupsParallelOutPower1": dupsParallelOutPower1,
       "dupsParallelOutPower2": dupsParallelOutPower2,
       "dupsParallelOutPower3": dupsParallelOutPower3,
       "dupsParallelInEnergy1": dupsParallelInEnergy1,
       "dupsParallelInEnergy2": dupsParallelInEnergy2,
       "dupsParallelInEnergy3": dupsParallelInEnergy3,
       "dupsParallelInEnergyTotal": dupsParallelInEnergyTotal,
       "dupsParallelOutEnergy1": dupsParallelOutEnergy1,
       "dupsParallelOutEnergy2": dupsParallelOutEnergy2,
       "dupsParallelOutEnergy3": dupsParallelOutEnergy3,
       "dupsParallelOutEnergyTotal": dupsParallelOutEnergyTotal,
       "dupsIntegrated": dupsIntegrated,
       "dupsIntegratedParallel": dupsIntegratedParallel,
       "dupsIntegratedDryInput1": dupsIntegratedDryInput1,
       "dupsIntegratedDryInput2": dupsIntegratedDryInput2,
       "dupsIntegratedDryInput3": dupsIntegratedDryInput3,
       "dupsIntegratedDryInput4": dupsIntegratedDryInput4,
       "dupsTraps": dupsTraps,
       "dupsCommunicationLost": dupsCommunicationLost,
       "dupsCommunicationEstablished": dupsCommunicationEstablished,
       "dupsPowerFail": dupsPowerFail,
       "dupsPowerRestored": dupsPowerRestored,
       "dupsLowBattery": dupsLowBattery,
       "dupsReturnFromLowBattery": dupsReturnFromLowBattery,
       "dupsLoadOnBypass": dupsLoadOnBypass,
       "dupsNoLongerLoadOnBypass": dupsNoLongerLoadOnBypass,
       "dupsUPSFault": dupsUPSFault,
       "dupsReturnFromUPSFault": dupsReturnFromUPSFault,
       "dupsBatteryGroundFault": dupsBatteryGroundFault,
       "dupsNoLongerBatteryFault": dupsNoLongerBatteryFault,
       "dupsTestInProgress": dupsTestInProgress,
       "dupsBatteryTestFail": dupsBatteryTestFail,
       "dupsFuseFailure": dupsFuseFailure,
       "dupsFuseRecovered": dupsFuseRecovered,
       "dupsOutputOverload": dupsOutputOverload,
       "dupsNoLongerOverload": dupsNoLongerOverload,
       "dupsInverterAbnormal": dupsInverterAbnormal,
       "dupsInverterRecovered": dupsInverterRecovered,
       "dupsSmartShutdownInit": dupsSmartShutdownInit,
       "dupsCancelShutdown": dupsCancelShutdown,
       "dupsTestCompleted": dupsTestCompleted,
       "dupsEPOON": dupsEPOON,
       "dupsEPOOFF": dupsEPOOFF,
       "dupsTemperatureAlarm": dupsTemperatureAlarm,
       "dupsTemperatureNormal": dupsTemperatureNormal,
       "dupsBattReplace": dupsBattReplace,
       "dupsReturnFromBattReplace": dupsReturnFromBattReplace,
       "dupsOutputOff": dupsOutputOff,
       "dupsReturnFromOutputOff": dupsReturnFromOutputOff,
       "dupsShutdown": dupsShutdown,
       "dupsReturnFromShutdown": dupsReturnFromShutdown,
       "dupsChargerFail": dupsChargerFail,
       "dupsReturnFromChargerFail": dupsReturnFromChargerFail,
       "dupsOnStandby": dupsOnStandby,
       "dupsReturnFromStandby": dupsReturnFromStandby,
       "dupsFanFail": dupsFanFail,
       "dupsReturnFromFanFail": dupsReturnFromFanFail,
       "dupsOnEconomic": dupsOnEconomic,
       "dupsReturnFromEconomic": dupsReturnFromEconomic,
       "dupsPowerModuleFail": dupsPowerModuleFail,
       "dupsReturnFromPowerModuleFail": dupsReturnFromPowerModuleFail,
       "dupsOutputBreakerOff": dupsOutputBreakerOff,
       "dupsReturnFromOutputBreakerOff": dupsReturnFromOutputBreakerOff,
       "dupsBatteryDepleted": dupsBatteryDepleted,
       "dupsReturnFromBatteryDepleted": dupsReturnFromBatteryDepleted,
       "dupsLoadOnManualBypass": dupsLoadOnManualBypass,
       "dupsNoLongerLoadOnManualBypass": dupsNoLongerLoadOnManualBypass,
       "dupsBatteryBreakerOpen": dupsBatteryBreakerOpen,
       "dupsReturnFromBatteryBreakerOpen": dupsReturnFromBatteryBreakerOpen,
       "dupsOutletBankOn": dupsOutletBankOn,
       "dupsOutletBankOff": dupsOutletBankOff,
       "dupsRedundancyLoss": dupsRedundancyLoss,
       "dupsReturnFromRedundancyLoss": dupsReturnFromRedundancyLoss,
       "dupsPhaseAsynchronous": dupsPhaseAsynchronous,
       "dupsReturnFromPhaseAsynchronous": dupsReturnFromPhaseAsynchronous,
       "dupsRectifierAbnormal": dupsRectifierAbnormal,
       "dupsReturnFromRectifierAbnormal": dupsReturnFromRectifierAbnormal,
       "dupsBypassBreakerOpen": dupsBypassBreakerOpen,
       "dupsReturnFromBypassBreakerOpen": dupsReturnFromBypassBreakerOpen,
       "dupsMainInputBreakerOpen": dupsMainInputBreakerOpen,
       "dupsReturnFromMainInputBreakerOpen": dupsReturnFromMainInputBreakerOpen,
       "dupsManualBypassBreakerOpen": dupsManualBypassBreakerOpen,
       "dupsReturnFromManualBypassBreakerOpen": dupsReturnFromManualBypassBreakerOpen}
)
