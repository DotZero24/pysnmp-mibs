# SNMP MIB module (SYNLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synaccess/SYNLINK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:14:21 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

synlink = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4)
)
if mibBuilder.loadTexts:
    synlink.setRevisions(
        ("2020-03-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RelayEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Synaccess_ObjectIdentity = ObjectIdentity
synaccess = _Synaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1)
)


class _SynLinkModel_Type(DisplayString):
    """Custom type synLinkModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SynLinkModel_Type.__name__ = "DisplayString"
_SynLinkModel_Object = MibScalar
synLinkModel = _SynLinkModel_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 1),
    _SynLinkModel_Type()
)
synLinkModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synLinkModel.setStatus("current")


class _EnclosureSerialNumber_Type(DisplayString):
    """Custom type enclosureSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_EnclosureSerialNumber_Type.__name__ = "DisplayString"
_EnclosureSerialNumber_Object = MibScalar
enclosureSerialNumber = _EnclosureSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 2),
    _EnclosureSerialNumber_Type()
)
enclosureSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSerialNumber.setStatus("current")


class _ControllerSerialNumber_Type(DisplayString):
    """Custom type controllerSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControllerSerialNumber_Type.__name__ = "DisplayString"
_ControllerSerialNumber_Object = MibScalar
controllerSerialNumber = _ControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 3),
    _ControllerSerialNumber_Type()
)
controllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSerialNumber.setStatus("current")


class _InletConfiguration_Type(DisplayString):
    """Custom type inletConfiguration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InletConfiguration_Type.__name__ = "DisplayString"
_InletConfiguration_Object = MibScalar
inletConfiguration = _InletConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 4),
    _InletConfiguration_Type()
)
inletConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletConfiguration.setStatus("current")


class _NumOutlets_Type(Integer32):
    """Custom type numOutlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NumOutlets_Type.__name__ = "Integer32"
_NumOutlets_Object = MibScalar
numOutlets = _NumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 5),
    _NumOutlets_Type()
)
numOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOutlets.setStatus("current")


class _NumBanks_Type(Integer32):
    """Custom type numBanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NumBanks_Type.__name__ = "Integer32"
_NumBanks_Object = MibScalar
numBanks = _NumBanks_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 6),
    _NumBanks_Type()
)
numBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBanks.setStatus("current")


class _Phase_Type(Integer32):
    """Custom type phase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Phase_Type.__name__ = "Integer32"
_Phase_Object = MibScalar
phase = _Phase_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 7),
    _Phase_Type()
)
phase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phase.setStatus("current")


class _NumInlets_Type(Integer32):
    """Custom type numInlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NumInlets_Type.__name__ = "Integer32"
_NumInlets_Object = MibScalar
numInlets = _NumInlets_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 8),
    _NumInlets_Type()
)
numInlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numInlets.setStatus("current")
_OutletPwrMeasurementsSupported_Type = TruthValue
_OutletPwrMeasurementsSupported_Object = MibScalar
outletPwrMeasurementsSupported = _OutletPwrMeasurementsSupported_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 9),
    _OutletPwrMeasurementsSupported_Type()
)
outletPwrMeasurementsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPwrMeasurementsSupported.setStatus("current")
_OutletSwitchingSupported_Type = TruthValue
_OutletSwitchingSupported_Object = MibScalar
outletSwitchingSupported = _OutletSwitchingSupported_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 10),
    _OutletSwitchingSupported_Type()
)
outletSwitchingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSwitchingSupported.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 11),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceIpAddress_Type = IpAddress
_DeviceIpAddress_Object = MibScalar
deviceIpAddress = _DeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 1, 12),
    _DeviceIpAddress_Type()
)
deviceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIpAddress.setStatus("current")
_Inlets_ObjectIdentity = ObjectIdentity
inlets = _Inlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2)
)
_InletTable_Object = MibTable
inletTable = _InletTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1)
)
if mibBuilder.loadTexts:
    inletTable.setStatus("current")
_InletEntry_Object = MibTableRow
inletEntry = _InletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1)
)
inletEntry.setIndexNames(
    (0, "SYNLINK-MIB", "inletIndex"),
)
if mibBuilder.loadTexts:
    inletEntry.setStatus("current")


class _InletIndex_Type(Integer32):
    """Custom type inletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletIndex_Type.__name__ = "Integer32"
_InletIndex_Object = MibTableColumn
inletIndex = _InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 1),
    _InletIndex_Type()
)
inletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inletIndex.setStatus("current")
_InletType_Type = DisplayString
_InletType_Object = MibTableColumn
inletType = _InletType_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 2),
    _InletType_Type()
)
inletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletType.setStatus("current")
_InletPlug_Type = DisplayString
_InletPlug_Object = MibTableColumn
inletPlug = _InletPlug_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 3),
    _InletPlug_Type()
)
inletPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPlug.setStatus("current")
_InletName_Type = DisplayString
_InletName_Object = MibTableColumn
inletName = _InletName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 4),
    _InletName_Type()
)
inletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletName.setStatus("current")
_InletEnergyAccumulation_Type = Integer32
_InletEnergyAccumulation_Object = MibTableColumn
inletEnergyAccumulation = _InletEnergyAccumulation_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 5),
    _InletEnergyAccumulation_Type()
)
inletEnergyAccumulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletEnergyAccumulation.setStatus("current")
_InletPowerFactor_Type = Integer32
_InletPowerFactor_Object = MibTableColumn
inletPowerFactor = _InletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 6),
    _InletPowerFactor_Type()
)
inletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerFactor.setStatus("current")
_InletPhase_Type = DisplayString
_InletPhase_Object = MibTableColumn
inletPhase = _InletPhase_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 7),
    _InletPhase_Type()
)
inletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPhase.setStatus("current")
_InletUuid_Type = DisplayString
_InletUuid_Object = MibTableColumn
inletUuid = _InletUuid_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 8),
    _InletUuid_Type()
)
inletUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletUuid.setStatus("current")
_Inlet3PhaseBalance_Type = Integer32
_Inlet3PhaseBalance_Object = MibTableColumn
inlet3PhaseBalance = _Inlet3PhaseBalance_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 9),
    _Inlet3PhaseBalance_Type()
)
inlet3PhaseBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlet3PhaseBalance.setStatus("current")
_InletLine1CurrentRms_Type = Integer32
_InletLine1CurrentRms_Object = MibTableColumn
inletLine1CurrentRms = _InletLine1CurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 10),
    _InletLine1CurrentRms_Type()
)
inletLine1CurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLine1CurrentRms.setStatus("current")
_InletLine2CurrentRms_Type = Integer32
_InletLine2CurrentRms_Object = MibTableColumn
inletLine2CurrentRms = _InletLine2CurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 11),
    _InletLine2CurrentRms_Type()
)
inletLine2CurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLine2CurrentRms.setStatus("current")
_InletLine3CurrentRms_Type = Integer32
_InletLine3CurrentRms_Object = MibTableColumn
inletLine3CurrentRms = _InletLine3CurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 12),
    _InletLine3CurrentRms_Type()
)
inletLine3CurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLine3CurrentRms.setStatus("current")
_InletLineConfiguration_Type = DisplayString
_InletLineConfiguration_Object = MibTableColumn
inletLineConfiguration = _InletLineConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 13),
    _InletLineConfiguration_Type()
)
inletLineConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLineConfiguration.setStatus("current")
_InletActivePower_Type = Integer32
_InletActivePower_Object = MibTableColumn
inletActivePower = _InletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 14),
    _InletActivePower_Type()
)
inletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletActivePower.setStatus("current")
_InletApparentPower_Type = Integer32
_InletApparentPower_Object = MibTableColumn
inletApparentPower = _InletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 15),
    _InletApparentPower_Type()
)
inletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletApparentPower.setStatus("current")
_InletReactivePower_Type = Integer32
_InletReactivePower_Object = MibTableColumn
inletReactivePower = _InletReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 16),
    _InletReactivePower_Type()
)
inletReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactivePower.setStatus("current")
_InletCurrentRms_Type = Integer32
_InletCurrentRms_Object = MibTableColumn
inletCurrentRms = _InletCurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 17),
    _InletCurrentRms_Type()
)
inletCurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrentRms.setStatus("current")
_InletLineFrequency_Type = Integer32
_InletLineFrequency_Object = MibTableColumn
inletLineFrequency = _InletLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 18),
    _InletLineFrequency_Type()
)
inletLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLineFrequency.setStatus("current")
_InletVoltageRms_Type = Integer32
_InletVoltageRms_Object = MibTableColumn
inletVoltageRms = _InletVoltageRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 19),
    _InletVoltageRms_Type()
)
inletVoltageRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltageRms.setStatus("current")
_AtsActiveInlet_Type = TruthValue
_AtsActiveInlet_Object = MibTableColumn
atsActiveInlet = _AtsActiveInlet_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 20),
    _AtsActiveInlet_Type()
)
atsActiveInlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsActiveInlet.setStatus("current")
_AtsInletId_Type = DisplayString
_AtsInletId_Object = MibTableColumn
atsInletId = _AtsInletId_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 21),
    _AtsInletId_Type()
)
atsInletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInletId.setStatus("current")
_AtsInletReady_Type = TruthValue
_AtsInletReady_Object = MibTableColumn
atsInletReady = _AtsInletReady_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 2, 1, 1, 22),
    _AtsInletReady_Type()
)
atsInletReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInletReady.setStatus("current")
_Banks_ObjectIdentity = ObjectIdentity
banks = _Banks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4)
)
_BankTable_Object = MibTable
bankTable = _BankTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1)
)
if mibBuilder.loadTexts:
    bankTable.setStatus("current")
_BankEntry_Object = MibTableRow
bankEntry = _BankEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1)
)
bankEntry.setIndexNames(
    (0, "SYNLINK-MIB", "bankIndex"),
)
if mibBuilder.loadTexts:
    bankEntry.setStatus("current")


class _BankIndex_Type(Integer32):
    """Custom type bankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BankIndex_Type.__name__ = "Integer32"
_BankIndex_Object = MibTableColumn
bankIndex = _BankIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 1),
    _BankIndex_Type()
)
bankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bankIndex.setStatus("current")
_BankUuid_Type = DisplayString
_BankUuid_Object = MibTableColumn
bankUuid = _BankUuid_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 2),
    _BankUuid_Type()
)
bankUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankUuid.setStatus("current")
_BankOutletSwitchingSupported_Type = TruthValue
_BankOutletSwitchingSupported_Object = MibTableColumn
bankOutletSwitchingSupported = _BankOutletSwitchingSupported_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 3),
    _BankOutletSwitchingSupported_Type()
)
bankOutletSwitchingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankOutletSwitchingSupported.setStatus("current")
_BankOutletMeteringSupported_Type = TruthValue
_BankOutletMeteringSupported_Object = MibTableColumn
bankOutletMeteringSupported = _BankOutletMeteringSupported_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 4),
    _BankOutletMeteringSupported_Type()
)
bankOutletMeteringSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankOutletMeteringSupported.setStatus("current")
_BankCurrentRms_Type = Integer32
_BankCurrentRms_Object = MibTableColumn
bankCurrentRms = _BankCurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 5),
    _BankCurrentRms_Type()
)
bankCurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankCurrentRms.setStatus("current")
_BankVoltage_Type = Integer32
_BankVoltage_Object = MibTableColumn
bankVoltage = _BankVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 6),
    _BankVoltage_Type()
)
bankVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankVoltage.setStatus("current")
_BankLineFrequency_Type = Integer32
_BankLineFrequency_Object = MibTableColumn
bankLineFrequency = _BankLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 7),
    _BankLineFrequency_Type()
)
bankLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankLineFrequency.setStatus("current")
_BankPowerFactor_Type = Integer32
_BankPowerFactor_Object = MibTableColumn
bankPowerFactor = _BankPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 8),
    _BankPowerFactor_Type()
)
bankPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankPowerFactor.setStatus("current")
_BankLines_Type = DisplayString
_BankLines_Object = MibTableColumn
bankLines = _BankLines_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 9),
    _BankLines_Type()
)
bankLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankLines.setStatus("current")
_BankActivePower_Type = Integer32
_BankActivePower_Object = MibTableColumn
bankActivePower = _BankActivePower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 10),
    _BankActivePower_Type()
)
bankActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankActivePower.setStatus("current")
_BankReactivePower_Type = Integer32
_BankReactivePower_Object = MibTableColumn
bankReactivePower = _BankReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 11),
    _BankReactivePower_Type()
)
bankReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankReactivePower.setStatus("current")
_BankApparentPower_Type = Integer32
_BankApparentPower_Object = MibTableColumn
bankApparentPower = _BankApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 12),
    _BankApparentPower_Type()
)
bankApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankApparentPower.setStatus("current")
_BankName_Type = DisplayString
_BankName_Object = MibTableColumn
bankName = _BankName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 13),
    _BankName_Type()
)
bankName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bankName.setStatus("current")
_BankBreakerSupported_Type = TruthValue
_BankBreakerSupported_Object = MibTableColumn
bankBreakerSupported = _BankBreakerSupported_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 14),
    _BankBreakerSupported_Type()
)
bankBreakerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankBreakerSupported.setStatus("current")
_BankBreakerState_Type = TruthValue
_BankBreakerState_Object = MibTableColumn
bankBreakerState = _BankBreakerState_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 4, 1, 1, 15),
    _BankBreakerState_Type()
)
bankBreakerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankBreakerState.setStatus("current")
_Outlets_ObjectIdentity = ObjectIdentity
outlets = _Outlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5)
)
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1)
)
outletEntry.setIndexNames(
    (0, "SYNLINK-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")
_OutletUuid_Type = DisplayString
_OutletUuid_Object = MibTableColumn
outletUuid = _OutletUuid_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1, 2),
    _OutletUuid_Type()
)
outletUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletUuid.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1, 3),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_OutletCurrentRms_Type = Integer32
_OutletCurrentRms_Object = MibTableColumn
outletCurrentRms = _OutletCurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1, 6),
    _OutletCurrentRms_Type()
)
outletCurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentRms.setStatus("current")
_OutletState_Type = RelayEnumeration
_OutletState_Object = MibTableColumn
outletState = _OutletState_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1, 7),
    _OutletState_Type()
)
outletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletState.setStatus("current")
_OutletConnector_Type = DisplayString
_OutletConnector_Object = MibTableColumn
outletConnector = _OutletConnector_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 5, 1, 1, 8),
    _OutletConnector_Type()
)
outletConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletConnector.setStatus("current")
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6)
)
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1)
)
groupEntry.setIndexNames(
    (0, "SYNLINK-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")


class _GroupIndex_Type(Integer32):
    """Custom type groupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_GroupIndex_Type.__name__ = "Integer32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1, 2),
    _GroupName_Type()
)
groupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_GroupUuid_Type = DisplayString
_GroupUuid_Object = MibTableColumn
groupUuid = _GroupUuid_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1, 3),
    _GroupUuid_Type()
)
groupUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUuid.setStatus("current")
_GroupSetState_Type = TruthValue
_GroupSetState_Object = MibTableColumn
groupSetState = _GroupSetState_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1, 4),
    _GroupSetState_Type()
)
groupSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupSetState.setStatus("current")
_GroupReboot_Type = TruthValue
_GroupReboot_Object = MibTableColumn
groupReboot = _GroupReboot_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1, 5),
    _GroupReboot_Type()
)
groupReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupReboot.setStatus("current")
_GroupCurrentRms_Type = Integer32
_GroupCurrentRms_Object = MibTableColumn
groupCurrentRms = _GroupCurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 6, 1, 1, 6),
    _GroupCurrentRms_Type()
)
groupCurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrentRms.setStatus("current")
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7)
)
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1)
)
sensorEntry.setIndexNames(
    (0, "SYNLINK-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorIndex_Type(Integer32):
    """Custom type sensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SensorIndex_Type.__name__ = "Integer32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")
_SensorType_Type = DisplayString
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 2),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SensorTemp_Type = Integer32
_SensorTemp_Object = MibTableColumn
sensorTemp = _SensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 3),
    _SensorTemp_Type()
)
sensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTemp.setStatus("current")
_SensorHumidity_Type = Integer32
_SensorHumidity_Object = MibTableColumn
sensorHumidity = _SensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 4),
    _SensorHumidity_Type()
)
sensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorHumidity.setStatus("current")
_SensorTempOffset_Type = Integer32
_SensorTempOffset_Object = MibTableColumn
sensorTempOffset = _SensorTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 5),
    _SensorTempOffset_Type()
)
sensorTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorTempOffset.setStatus("current")
_SensorHumidityOffset_Type = Integer32
_SensorHumidityOffset_Object = MibTableColumn
sensorHumidityOffset = _SensorHumidityOffset_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 6),
    _SensorHumidityOffset_Type()
)
sensorHumidityOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorHumidityOffset.setStatus("current")
_SensorName_Type = DisplayString
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 7, 1, 1, 7),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8)
)
_PowerLogTable_Object = MibTable
powerLogTable = _PowerLogTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 1)
)
if mibBuilder.loadTexts:
    powerLogTable.setStatus("current")
_PowerLogEntry_Object = MibTableRow
powerLogEntry = _PowerLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 1, 1)
)
powerLogEntry.setIndexNames(
    (0, "SYNLINK-MIB", "pwrLogIndex"),
)
if mibBuilder.loadTexts:
    powerLogEntry.setStatus("current")


class _PwrLogIndex_Type(Integer32):
    """Custom type pwrLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PwrLogIndex_Type.__name__ = "Integer32"
_PwrLogIndex_Object = MibTableColumn
pwrLogIndex = _PwrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 1, 1, 1),
    _PwrLogIndex_Type()
)
pwrLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwrLogIndex.setStatus("current")
_PwrLogType_Type = DisplayString
_PwrLogType_Object = MibTableColumn
pwrLogType = _PwrLogType_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 1, 1, 2),
    _PwrLogType_Type()
)
pwrLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrLogType.setStatus("current")
_PwrLogValue_Type = Integer32
_PwrLogValue_Object = MibTableColumn
pwrLogValue = _PwrLogValue_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 1, 1, 3),
    _PwrLogValue_Type()
)
pwrLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrLogValue.setStatus("current")
_EnvironmentLogTable_Object = MibTable
environmentLogTable = _EnvironmentLogTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 2)
)
if mibBuilder.loadTexts:
    environmentLogTable.setStatus("current")
_EnvironmentLogEntry_Object = MibTableRow
environmentLogEntry = _EnvironmentLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 2, 1)
)
environmentLogEntry.setIndexNames(
    (0, "SYNLINK-MIB", "envLogIndex"),
)
if mibBuilder.loadTexts:
    environmentLogEntry.setStatus("current")


class _EnvLogIndex_Type(Integer32):
    """Custom type envLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EnvLogIndex_Type.__name__ = "Integer32"
_EnvLogIndex_Object = MibTableColumn
envLogIndex = _EnvLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 2, 1, 1),
    _EnvLogIndex_Type()
)
envLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envLogIndex.setStatus("current")
_EnvLogType_Type = DisplayString
_EnvLogType_Object = MibTableColumn
envLogType = _EnvLogType_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 2, 1, 2),
    _EnvLogType_Type()
)
envLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envLogType.setStatus("current")
_EnvLogValue_Type = Integer32
_EnvLogValue_Object = MibTableColumn
envLogValue = _EnvLogValue_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 8, 2, 1, 3),
    _EnvLogValue_Type()
)
envLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envLogValue.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9)
)
_EventTraps_ObjectIdentity = ObjectIdentity
eventTraps = _EventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0)
)
_EventTriggers_ObjectIdentity = ObjectIdentity
eventTriggers = _EventTriggers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2)
)
_EventTriggerTable_Object = MibTable
eventTriggerTable = _EventTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1)
)
if mibBuilder.loadTexts:
    eventTriggerTable.setStatus("current")
_EventTriggerEntry_Object = MibTableRow
eventTriggerEntry = _EventTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1)
)
eventTriggerEntry.setIndexNames(
    (0, "SYNLINK-MIB", "eventTriggerIndex"),
)
if mibBuilder.loadTexts:
    eventTriggerEntry.setStatus("current")


class _EventTriggerIndex_Type(Integer32):
    """Custom type eventTriggerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EventTriggerIndex_Type.__name__ = "Integer32"
_EventTriggerIndex_Object = MibTableColumn
eventTriggerIndex = _EventTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 1),
    _EventTriggerIndex_Type()
)
eventTriggerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTriggerIndex.setStatus("current")
_EventType_Type = DisplayString
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 2),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventCode_Type = Integer32
_EventCode_Object = MibTableColumn
eventCode = _EventCode_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 3),
    _EventCode_Type()
)
eventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCode.setStatus("current")
_EventName_Type = DisplayString
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 4),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventTriggerAttr1_Type = DisplayString
_EventTriggerAttr1_Object = MibTableColumn
eventTriggerAttr1 = _EventTriggerAttr1_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 5),
    _EventTriggerAttr1_Type()
)
eventTriggerAttr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTriggerAttr1.setStatus("current")
_EventTriggerAttr2_Type = DisplayString
_EventTriggerAttr2_Object = MibTableColumn
eventTriggerAttr2 = _EventTriggerAttr2_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 6),
    _EventTriggerAttr2_Type()
)
eventTriggerAttr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTriggerAttr2.setStatus("current")
_EventTriggerAttr3_Type = DisplayString
_EventTriggerAttr3_Object = MibTableColumn
eventTriggerAttr3 = _EventTriggerAttr3_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 7),
    _EventTriggerAttr3_Type()
)
eventTriggerAttr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTriggerAttr3.setStatus("current")
_EventIsTriggered_Type = TruthValue
_EventIsTriggered_Object = MibTableColumn
eventIsTriggered = _EventIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 8),
    _EventIsTriggered_Type()
)
eventIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIsTriggered.setStatus("current")
_EventTriggeredTime_Type = Integer32
_EventTriggeredTime_Object = MibTableColumn
eventTriggeredTime = _EventTriggeredTime_Object(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 2, 1, 1, 9),
    _EventTriggeredTime_Type()
)
eventTriggeredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTriggeredTime.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10)
)
_SynLinkGroups_ObjectIdentity = ObjectIdentity
synLinkGroups = _SynLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1)
)
_SynLinkCompliances_ObjectIdentity = ObjectIdentity
synLinkCompliances = _SynLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 2)
)

# Managed Objects groups

synLinkDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 1)
)
synLinkDeviceGroup.setObjects(
      *(("SYNLINK-MIB", "synLinkModel"),
        ("SYNLINK-MIB", "enclosureSerialNumber"),
        ("SYNLINK-MIB", "controllerSerialNumber"),
        ("SYNLINK-MIB", "inletConfiguration"),
        ("SYNLINK-MIB", "numOutlets"),
        ("SYNLINK-MIB", "numBanks"),
        ("SYNLINK-MIB", "phase"),
        ("SYNLINK-MIB", "numInlets"),
        ("SYNLINK-MIB", "outletPwrMeasurementsSupported"),
        ("SYNLINK-MIB", "outletSwitchingSupported"),
        ("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"))
)
if mibBuilder.loadTexts:
    synLinkDeviceGroup.setStatus("current")

synLinkInletGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 2)
)
synLinkInletGroup.setObjects(
      *(("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletEnergyAccumulation"),
        ("SYNLINK-MIB", "inletPowerFactor"),
        ("SYNLINK-MIB", "inletPhase"),
        ("SYNLINK-MIB", "inletUuid"),
        ("SYNLINK-MIB", "inlet3PhaseBalance"),
        ("SYNLINK-MIB", "inletLine1CurrentRms"),
        ("SYNLINK-MIB", "inletLine2CurrentRms"),
        ("SYNLINK-MIB", "inletLine3CurrentRms"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "inletActivePower"),
        ("SYNLINK-MIB", "inletApparentPower"),
        ("SYNLINK-MIB", "inletReactivePower"),
        ("SYNLINK-MIB", "inletCurrentRms"),
        ("SYNLINK-MIB", "inletLineFrequency"),
        ("SYNLINK-MIB", "inletVoltageRms"),
        ("SYNLINK-MIB", "atsActiveInlet"),
        ("SYNLINK-MIB", "atsInletId"),
        ("SYNLINK-MIB", "atsInletReady"))
)
if mibBuilder.loadTexts:
    synLinkInletGroup.setStatus("current")

synLinkBankGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 4)
)
synLinkBankGroup.setObjects(
      *(("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "bankOutletSwitchingSupported"),
        ("SYNLINK-MIB", "bankOutletMeteringSupported"),
        ("SYNLINK-MIB", "bankCurrentRms"),
        ("SYNLINK-MIB", "bankVoltage"),
        ("SYNLINK-MIB", "bankLineFrequency"),
        ("SYNLINK-MIB", "bankPowerFactor"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankActivePower"),
        ("SYNLINK-MIB", "bankReactivePower"),
        ("SYNLINK-MIB", "bankApparentPower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankBreakerSupported"),
        ("SYNLINK-MIB", "bankBreakerState"))
)
if mibBuilder.loadTexts:
    synLinkBankGroup.setStatus("current")

synLinkOutletGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 5)
)
synLinkOutletGroup.setObjects(
      *(("SYNLINK-MIB", "outletUuid"),
        ("SYNLINK-MIB", "outletName"),
        ("SYNLINK-MIB", "outletCurrentRms"),
        ("SYNLINK-MIB", "outletState"),
        ("SYNLINK-MIB", "outletConnector"))
)
if mibBuilder.loadTexts:
    synLinkOutletGroup.setStatus("current")

synLinkGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 6)
)
synLinkGroupGroup.setObjects(
      *(("SYNLINK-MIB", "groupName"),
        ("SYNLINK-MIB", "groupUuid"),
        ("SYNLINK-MIB", "groupSetState"),
        ("SYNLINK-MIB", "groupReboot"),
        ("SYNLINK-MIB", "groupCurrentRms"))
)
if mibBuilder.loadTexts:
    synLinkGroupGroup.setStatus("current")

synLinkSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 7)
)
synLinkSensorGroup.setObjects(
      *(("SYNLINK-MIB", "sensorType"),
        ("SYNLINK-MIB", "sensorTemp"),
        ("SYNLINK-MIB", "sensorHumidity"),
        ("SYNLINK-MIB", "sensorTempOffset"),
        ("SYNLINK-MIB", "sensorHumidityOffset"),
        ("SYNLINK-MIB", "sensorName"))
)
if mibBuilder.loadTexts:
    synLinkSensorGroup.setStatus("current")

synLinkLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 8)
)
synLinkLogGroup.setObjects(
      *(("SYNLINK-MIB", "pwrLogType"),
        ("SYNLINK-MIB", "pwrLogValue"),
        ("SYNLINK-MIB", "envLogType"),
        ("SYNLINK-MIB", "envLogValue"))
)
if mibBuilder.loadTexts:
    synLinkLogGroup.setStatus("current")

synLinkEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 9)
)
synLinkEventGroup.setObjects(
      *(("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"),
        ("SYNLINK-MIB", "eventIsTriggered"),
        ("SYNLINK-MIB", "eventTriggeredTime"))
)
if mibBuilder.loadTexts:
    synLinkEventGroup.setStatus("current")


# Notification objects

autopingTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 1)
)
autopingTimeout.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"))
)
if mibBuilder.loadTexts:
    autopingTimeout.setStatus(
        "current"
    )

line1CurrentMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 2)
)
line1CurrentMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLine1CurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    line1CurrentMaxThreshold.setStatus(
        "current"
    )

line2CurrentMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 3)
)
line2CurrentMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLine2CurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    line2CurrentMaxThreshold.setStatus(
        "current"
    )

line3CurrentMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 4)
)
line3CurrentMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLine3CurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    line3CurrentMaxThreshold.setStatus(
        "current"
    )

line1CurrentMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 5)
)
line1CurrentMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLine1CurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    line1CurrentMinThreshold.setStatus(
        "current"
    )

line2CurrentMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 6)
)
line2CurrentMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLine2CurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    line2CurrentMinThreshold.setStatus(
        "current"
    )

line3CurrentMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 7)
)
line3CurrentMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLine3CurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    line3CurrentMinThreshold.setStatus(
        "current"
    )

inletCurrentMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 8)
)
inletCurrentMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletCurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletCurrentMaxThreshold.setStatus(
        "current"
    )

inletCurrentMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 9)
)
inletCurrentMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletCurrentRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletCurrentMinThreshold.setStatus(
        "current"
    )

inletVoltageMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 10)
)
inletVoltageMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletVoltageRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletVoltageMaxThreshold.setStatus(
        "current"
    )

inletVoltageMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 11)
)
inletVoltageMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletVoltageRms"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletVoltageMinThreshold.setStatus(
        "current"
    )

inletLineFrequencyMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 12)
)
inletLineFrequencyMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLineFrequency"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletLineFrequencyMaxThreshold.setStatus(
        "current"
    )

inletLineFrequencyMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 13)
)
inletLineFrequencyMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletLineFrequency"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletLineFrequencyMinThreshold.setStatus(
        "current"
    )

inletPowerFactorMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 14)
)
inletPowerFactorMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletPowerFactor"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletPowerFactorMinThreshold.setStatus(
        "current"
    )

inletActiveEnergyMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 15)
)
inletActiveEnergyMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletEnergyAccumulation"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletActiveEnergyMaxThreshold.setStatus(
        "current"
    )

inletActivePowerMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 16)
)
inletActivePowerMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletActivePower"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletActivePowerMaxThreshold.setStatus(
        "current"
    )

inletActivePowerMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 17)
)
inletActivePowerMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletActivePower"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletActivePowerMinThreshold.setStatus(
        "current"
    )

inletApparentPowerMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 18)
)
inletApparentPowerMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletApparentPower"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletApparentPowerMaxThreshold.setStatus(
        "current"
    )

inletApparentPowerMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 19)
)
inletApparentPowerMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletApparentPower"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletApparentPowerMinThreshold.setStatus(
        "current"
    )

inletReactivePowerMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 20)
)
inletReactivePowerMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletReactivePower"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletReactivePowerMaxThreshold.setStatus(
        "current"
    )

inletReactivePowerMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 21)
)
inletReactivePowerMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inletReactivePower"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inletReactivePowerMinThreshold.setStatus(
        "current"
    )

inlet3phaseImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 22)
)
inlet3phaseImbalance.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "inlet3PhaseBalance"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    inlet3phaseImbalance.setStatus(
        "current"
    )

bankBreakerTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 23)
)
bankBreakerTrip.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankCurrentRms"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "bankBreakerState"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"))
)
if mibBuilder.loadTexts:
    bankBreakerTrip.setStatus(
        "current"
    )

bankCurrentMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 24)
)
bankCurrentMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankCurrentRms"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankCurrentMaxThreshold.setStatus(
        "current"
    )

bankCurrentMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 25)
)
bankCurrentMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankCurrentRms"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankCurrentMinThreshold.setStatus(
        "current"
    )

bankVoltageMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 26)
)
bankVoltageMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankVoltage"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankVoltageMaxThreshold.setStatus(
        "current"
    )

bankVoltageMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 27)
)
bankVoltageMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankVoltage"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankVoltageMinThreshold.setStatus(
        "current"
    )

bankLineFrequencyMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 28)
)
bankLineFrequencyMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankLineFrequency"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankLineFrequencyMaxThreshold.setStatus(
        "current"
    )

bankLineFrequencyMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 29)
)
bankLineFrequencyMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankLineFrequency"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankLineFrequencyMinThreshold.setStatus(
        "current"
    )

bankPowerfactorMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 30)
)
bankPowerfactorMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankPowerFactor"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankPowerfactorMinThreshold.setStatus(
        "current"
    )

bankActivePowerMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 32)
)
bankActivePowerMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankActivePower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankActivePowerMaxThreshold.setStatus(
        "current"
    )

bankActivePowerMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 33)
)
bankActivePowerMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankActivePower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankActivePowerMinThreshold.setStatus(
        "current"
    )

bankApparentPowerMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 34)
)
bankApparentPowerMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankApparentPower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankApparentPowerMaxThreshold.setStatus(
        "current"
    )

bankApparentPowerMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 35)
)
bankApparentPowerMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankApparentPower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankApparentPowerMinThreshold.setStatus(
        "current"
    )

bankReactivePowerMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 36)
)
bankReactivePowerMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankReactivePower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankReactivePowerMaxThreshold.setStatus(
        "current"
    )

bankReactivePowerMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 37)
)
bankReactivePowerMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "bankReactivePower"),
        ("SYNLINK-MIB", "bankName"),
        ("SYNLINK-MIB", "bankLines"),
        ("SYNLINK-MIB", "bankUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    bankReactivePowerMinThreshold.setStatus(
        "current"
    )

outletCurrentMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 38)
)
outletCurrentMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "outletCurrentRms"),
        ("SYNLINK-MIB", "outletName"),
        ("SYNLINK-MIB", "outletState"),
        ("SYNLINK-MIB", "outletConnector"),
        ("SYNLINK-MIB", "outletUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    outletCurrentMaxThreshold.setStatus(
        "current"
    )

outletCurrentMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 39)
)
outletCurrentMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "outletCurrentRms"),
        ("SYNLINK-MIB", "outletName"),
        ("SYNLINK-MIB", "outletState"),
        ("SYNLINK-MIB", "outletConnector"),
        ("SYNLINK-MIB", "outletUuid"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    outletCurrentMinThreshold.setStatus(
        "current"
    )

temperatureMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 42)
)
temperatureMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "sensorTemp"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    temperatureMaxThreshold.setStatus(
        "current"
    )

temperatureMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 43)
)
temperatureMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "sensorTemp"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    temperatureMinThreshold.setStatus(
        "current"
    )

humidityMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 44)
)
humidityMaxThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "sensorHumidity"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    humidityMaxThreshold.setStatus(
        "current"
    )

humidityMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 45)
)
humidityMinThreshold.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "sensorHumidity"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"),
        ("SYNLINK-MIB", "eventTriggerAttr2"),
        ("SYNLINK-MIB", "eventTriggerAttr3"))
)
if mibBuilder.loadTexts:
    humidityMinThreshold.setStatus(
        "current"
    )

scheduledTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 46)
)
scheduledTime.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"))
)
if mibBuilder.loadTexts:
    scheduledTime.setStatus(
        "current"
    )

scheduledInterval = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 47)
)
scheduledInterval.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"),
        ("SYNLINK-MIB", "eventTriggerAttr1"))
)
if mibBuilder.loadTexts:
    scheduledInterval.setStatus(
        "current"
    )

atsInletSwitchedToSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 48)
)
atsInletSwitchedToSecondary.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "atsActiveInlet"),
        ("SYNLINK-MIB", "atsInletId"),
        ("SYNLINK-MIB", "atsInletReady"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"))
)
if mibBuilder.loadTexts:
    atsInletSwitchedToSecondary.setStatus(
        "current"
    )

atsInletSwitchedToPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 49)
)
atsInletSwitchedToPrimary.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "atsActiveInlet"),
        ("SYNLINK-MIB", "atsInletId"),
        ("SYNLINK-MIB", "atsInletReady"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"))
)
if mibBuilder.loadTexts:
    atsInletSwitchedToPrimary.setStatus(
        "current"
    )

atsInletSecondaryPowerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 50)
)
atsInletSecondaryPowerLoss.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "atsActiveInlet"),
        ("SYNLINK-MIB", "atsInletId"),
        ("SYNLINK-MIB", "atsInletReady"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"))
)
if mibBuilder.loadTexts:
    atsInletSecondaryPowerLoss.setStatus(
        "current"
    )

atsInletSecondaryPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 4, 9, 0, 51)
)
atsInletSecondaryPowerRestored.setObjects(
      *(("SYNLINK-MIB", "deviceName"),
        ("SYNLINK-MIB", "deviceIpAddress"),
        ("SYNLINK-MIB", "atsActiveInlet"),
        ("SYNLINK-MIB", "atsInletId"),
        ("SYNLINK-MIB", "atsInletReady"),
        ("SYNLINK-MIB", "inletName"),
        ("SYNLINK-MIB", "inletPlug"),
        ("SYNLINK-MIB", "inletType"),
        ("SYNLINK-MIB", "inletLineConfiguration"),
        ("SYNLINK-MIB", "eventType"),
        ("SYNLINK-MIB", "eventCode"),
        ("SYNLINK-MIB", "eventName"))
)
if mibBuilder.loadTexts:
    atsInletSecondaryPowerRestored.setStatus(
        "current"
    )


# Notifications groups

synLinkTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 1, 10)
)
synLinkTrapGroup.setObjects(
      *(("SYNLINK-MIB", "autopingTimeout"),
        ("SYNLINK-MIB", "line1CurrentMaxThreshold"),
        ("SYNLINK-MIB", "line2CurrentMaxThreshold"),
        ("SYNLINK-MIB", "line3CurrentMaxThreshold"),
        ("SYNLINK-MIB", "line1CurrentMinThreshold"),
        ("SYNLINK-MIB", "line2CurrentMinThreshold"),
        ("SYNLINK-MIB", "line3CurrentMinThreshold"),
        ("SYNLINK-MIB", "inletCurrentMaxThreshold"),
        ("SYNLINK-MIB", "inletCurrentMinThreshold"),
        ("SYNLINK-MIB", "inletVoltageMaxThreshold"),
        ("SYNLINK-MIB", "inletVoltageMinThreshold"),
        ("SYNLINK-MIB", "inletLineFrequencyMaxThreshold"),
        ("SYNLINK-MIB", "inletLineFrequencyMinThreshold"),
        ("SYNLINK-MIB", "inletPowerFactorMinThreshold"),
        ("SYNLINK-MIB", "inletActiveEnergyMaxThreshold"),
        ("SYNLINK-MIB", "inletActivePowerMaxThreshold"),
        ("SYNLINK-MIB", "inletActivePowerMinThreshold"),
        ("SYNLINK-MIB", "inletApparentPowerMaxThreshold"),
        ("SYNLINK-MIB", "inletApparentPowerMinThreshold"),
        ("SYNLINK-MIB", "inletReactivePowerMaxThreshold"),
        ("SYNLINK-MIB", "inletReactivePowerMinThreshold"),
        ("SYNLINK-MIB", "inlet3phaseImbalance"),
        ("SYNLINK-MIB", "bankBreakerTrip"),
        ("SYNLINK-MIB", "bankCurrentMaxThreshold"),
        ("SYNLINK-MIB", "bankCurrentMinThreshold"),
        ("SYNLINK-MIB", "bankVoltageMaxThreshold"),
        ("SYNLINK-MIB", "bankVoltageMinThreshold"),
        ("SYNLINK-MIB", "bankLineFrequencyMaxThreshold"),
        ("SYNLINK-MIB", "bankLineFrequencyMinThreshold"),
        ("SYNLINK-MIB", "bankPowerfactorMinThreshold"),
        ("SYNLINK-MIB", "bankActivePowerMaxThreshold"),
        ("SYNLINK-MIB", "bankActivePowerMinThreshold"),
        ("SYNLINK-MIB", "bankApparentPowerMaxThreshold"),
        ("SYNLINK-MIB", "bankApparentPowerMinThreshold"),
        ("SYNLINK-MIB", "bankReactivePowerMaxThreshold"),
        ("SYNLINK-MIB", "bankReactivePowerMinThreshold"),
        ("SYNLINK-MIB", "outletCurrentMaxThreshold"),
        ("SYNLINK-MIB", "outletCurrentMinThreshold"),
        ("SYNLINK-MIB", "temperatureMaxThreshold"),
        ("SYNLINK-MIB", "temperatureMinThreshold"),
        ("SYNLINK-MIB", "scheduledTime"),
        ("SYNLINK-MIB", "scheduledInterval"),
        ("SYNLINK-MIB", "atsInletSwitchedToSecondary"),
        ("SYNLINK-MIB", "atsInletSwitchedToPrimary"),
        ("SYNLINK-MIB", "atsInletSecondaryPowerLoss"),
        ("SYNLINK-MIB", "atsInletSecondaryPowerRestored"))
)
if mibBuilder.loadTexts:
    synLinkTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

synLinkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21728, 4, 10, 2, 1)
)
synLinkCompliance.setObjects(
      *(("SYNLINK-MIB", "synLinkDeviceGroup"),
        ("SYNLINK-MIB", "synLinkInletGroup"),
        ("SYNLINK-MIB", "synLinkBankGroup"),
        ("SYNLINK-MIB", "synLinkOutletGroup"),
        ("SYNLINK-MIB", "synLinkGroupGroup"),
        ("SYNLINK-MIB", "synLinkSensorGroup"),
        ("SYNLINK-MIB", "synLinkLogGroup"),
        ("SYNLINK-MIB", "synLinkEventGroup"),
        ("SYNLINK-MIB", "synLinkTrapGroup"))
)
if mibBuilder.loadTexts:
    synLinkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNLINK-MIB",
    **{"RelayEnumeration": RelayEnumeration,
       "synaccess": synaccess,
       "synlink": synlink,
       "device": device,
       "synLinkModel": synLinkModel,
       "enclosureSerialNumber": enclosureSerialNumber,
       "controllerSerialNumber": controllerSerialNumber,
       "inletConfiguration": inletConfiguration,
       "numOutlets": numOutlets,
       "numBanks": numBanks,
       "phase": phase,
       "numInlets": numInlets,
       "outletPwrMeasurementsSupported": outletPwrMeasurementsSupported,
       "outletSwitchingSupported": outletSwitchingSupported,
       "deviceName": deviceName,
       "deviceIpAddress": deviceIpAddress,
       "inlets": inlets,
       "inletTable": inletTable,
       "inletEntry": inletEntry,
       "inletIndex": inletIndex,
       "inletType": inletType,
       "inletPlug": inletPlug,
       "inletName": inletName,
       "inletEnergyAccumulation": inletEnergyAccumulation,
       "inletPowerFactor": inletPowerFactor,
       "inletPhase": inletPhase,
       "inletUuid": inletUuid,
       "inlet3PhaseBalance": inlet3PhaseBalance,
       "inletLine1CurrentRms": inletLine1CurrentRms,
       "inletLine2CurrentRms": inletLine2CurrentRms,
       "inletLine3CurrentRms": inletLine3CurrentRms,
       "inletLineConfiguration": inletLineConfiguration,
       "inletActivePower": inletActivePower,
       "inletApparentPower": inletApparentPower,
       "inletReactivePower": inletReactivePower,
       "inletCurrentRms": inletCurrentRms,
       "inletLineFrequency": inletLineFrequency,
       "inletVoltageRms": inletVoltageRms,
       "atsActiveInlet": atsActiveInlet,
       "atsInletId": atsInletId,
       "atsInletReady": atsInletReady,
       "banks": banks,
       "bankTable": bankTable,
       "bankEntry": bankEntry,
       "bankIndex": bankIndex,
       "bankUuid": bankUuid,
       "bankOutletSwitchingSupported": bankOutletSwitchingSupported,
       "bankOutletMeteringSupported": bankOutletMeteringSupported,
       "bankCurrentRms": bankCurrentRms,
       "bankVoltage": bankVoltage,
       "bankLineFrequency": bankLineFrequency,
       "bankPowerFactor": bankPowerFactor,
       "bankLines": bankLines,
       "bankActivePower": bankActivePower,
       "bankReactivePower": bankReactivePower,
       "bankApparentPower": bankApparentPower,
       "bankName": bankName,
       "bankBreakerSupported": bankBreakerSupported,
       "bankBreakerState": bankBreakerState,
       "outlets": outlets,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletUuid": outletUuid,
       "outletName": outletName,
       "outletCurrentRms": outletCurrentRms,
       "outletState": outletState,
       "outletConnector": outletConnector,
       "groups": groups,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupName": groupName,
       "groupUuid": groupUuid,
       "groupSetState": groupSetState,
       "groupReboot": groupReboot,
       "groupCurrentRms": groupCurrentRms,
       "sensors": sensors,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorType": sensorType,
       "sensorTemp": sensorTemp,
       "sensorHumidity": sensorHumidity,
       "sensorTempOffset": sensorTempOffset,
       "sensorHumidityOffset": sensorHumidityOffset,
       "sensorName": sensorName,
       "logs": logs,
       "powerLogTable": powerLogTable,
       "powerLogEntry": powerLogEntry,
       "pwrLogIndex": pwrLogIndex,
       "pwrLogType": pwrLogType,
       "pwrLogValue": pwrLogValue,
       "environmentLogTable": environmentLogTable,
       "environmentLogEntry": environmentLogEntry,
       "envLogIndex": envLogIndex,
       "envLogType": envLogType,
       "envLogValue": envLogValue,
       "events": events,
       "eventTraps": eventTraps,
       "autopingTimeout": autopingTimeout,
       "line1CurrentMaxThreshold": line1CurrentMaxThreshold,
       "line2CurrentMaxThreshold": line2CurrentMaxThreshold,
       "line3CurrentMaxThreshold": line3CurrentMaxThreshold,
       "line1CurrentMinThreshold": line1CurrentMinThreshold,
       "line2CurrentMinThreshold": line2CurrentMinThreshold,
       "line3CurrentMinThreshold": line3CurrentMinThreshold,
       "inletCurrentMaxThreshold": inletCurrentMaxThreshold,
       "inletCurrentMinThreshold": inletCurrentMinThreshold,
       "inletVoltageMaxThreshold": inletVoltageMaxThreshold,
       "inletVoltageMinThreshold": inletVoltageMinThreshold,
       "inletLineFrequencyMaxThreshold": inletLineFrequencyMaxThreshold,
       "inletLineFrequencyMinThreshold": inletLineFrequencyMinThreshold,
       "inletPowerFactorMinThreshold": inletPowerFactorMinThreshold,
       "inletActiveEnergyMaxThreshold": inletActiveEnergyMaxThreshold,
       "inletActivePowerMaxThreshold": inletActivePowerMaxThreshold,
       "inletActivePowerMinThreshold": inletActivePowerMinThreshold,
       "inletApparentPowerMaxThreshold": inletApparentPowerMaxThreshold,
       "inletApparentPowerMinThreshold": inletApparentPowerMinThreshold,
       "inletReactivePowerMaxThreshold": inletReactivePowerMaxThreshold,
       "inletReactivePowerMinThreshold": inletReactivePowerMinThreshold,
       "inlet3phaseImbalance": inlet3phaseImbalance,
       "bankBreakerTrip": bankBreakerTrip,
       "bankCurrentMaxThreshold": bankCurrentMaxThreshold,
       "bankCurrentMinThreshold": bankCurrentMinThreshold,
       "bankVoltageMaxThreshold": bankVoltageMaxThreshold,
       "bankVoltageMinThreshold": bankVoltageMinThreshold,
       "bankLineFrequencyMaxThreshold": bankLineFrequencyMaxThreshold,
       "bankLineFrequencyMinThreshold": bankLineFrequencyMinThreshold,
       "bankPowerfactorMinThreshold": bankPowerfactorMinThreshold,
       "bankActivePowerMaxThreshold": bankActivePowerMaxThreshold,
       "bankActivePowerMinThreshold": bankActivePowerMinThreshold,
       "bankApparentPowerMaxThreshold": bankApparentPowerMaxThreshold,
       "bankApparentPowerMinThreshold": bankApparentPowerMinThreshold,
       "bankReactivePowerMaxThreshold": bankReactivePowerMaxThreshold,
       "bankReactivePowerMinThreshold": bankReactivePowerMinThreshold,
       "outletCurrentMaxThreshold": outletCurrentMaxThreshold,
       "outletCurrentMinThreshold": outletCurrentMinThreshold,
       "temperatureMaxThreshold": temperatureMaxThreshold,
       "temperatureMinThreshold": temperatureMinThreshold,
       "humidityMaxThreshold": humidityMaxThreshold,
       "humidityMinThreshold": humidityMinThreshold,
       "scheduledTime": scheduledTime,
       "scheduledInterval": scheduledInterval,
       "atsInletSwitchedToSecondary": atsInletSwitchedToSecondary,
       "atsInletSwitchedToPrimary": atsInletSwitchedToPrimary,
       "atsInletSecondaryPowerLoss": atsInletSecondaryPowerLoss,
       "atsInletSecondaryPowerRestored": atsInletSecondaryPowerRestored,
       "eventTriggers": eventTriggers,
       "eventTriggerTable": eventTriggerTable,
       "eventTriggerEntry": eventTriggerEntry,
       "eventTriggerIndex": eventTriggerIndex,
       "eventType": eventType,
       "eventCode": eventCode,
       "eventName": eventName,
       "eventTriggerAttr1": eventTriggerAttr1,
       "eventTriggerAttr2": eventTriggerAttr2,
       "eventTriggerAttr3": eventTriggerAttr3,
       "eventIsTriggered": eventIsTriggered,
       "eventTriggeredTime": eventTriggeredTime,
       "conformance": conformance,
       "synLinkGroups": synLinkGroups,
       "synLinkDeviceGroup": synLinkDeviceGroup,
       "synLinkInletGroup": synLinkInletGroup,
       "synLinkBankGroup": synLinkBankGroup,
       "synLinkOutletGroup": synLinkOutletGroup,
       "synLinkGroupGroup": synLinkGroupGroup,
       "synLinkSensorGroup": synLinkSensorGroup,
       "synLinkLogGroup": synLinkLogGroup,
       "synLinkEventGroup": synLinkEventGroup,
       "synLinkTrapGroup": synLinkTrapGroup,
       "synLinkCompliances": synLinkCompliances,
       "synLinkCompliance": synLinkCompliance}
)
