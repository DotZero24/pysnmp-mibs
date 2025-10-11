# SNMP MIB module (ADTRAN-GEN-OPTICAL-AMPLIFIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-OPTICAL-AMPLIFIER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:25 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenOpticalAmplifier,
 adGenOpticalAmplifierID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenOpticalAmplifier",
    "adGenOpticalAmplifierID")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenOpticalAmplifierMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 41, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMIB.setRevisions(
        ("2013-07-23 00:00",
         "2012-08-27 00:00",
         "2012-04-12 00:00",
         "2012-01-17 00:00",
         "2011-10-20 00:00",
         "2011-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenOpticalAmplifierProduct_ObjectIdentity = ObjectIdentity
adGenOpticalAmplifierProduct = _AdGenOpticalAmplifierProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1)
)
_AdGenOpticalAmplifierTable_Object = MibTable
adGenOpticalAmplifierTable = _AdGenOpticalAmplifierTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierTable.setStatus("current")
_AdGenOpticalAmplifierEntry_Object = MibTableRow
adGenOpticalAmplifierEntry = _AdGenOpticalAmplifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1)
)
adGenOpticalAmplifierEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierEntry.setStatus("current")


class _AdGenOpticalAmplifierProdType_Type(Integer32):
    """Custom type adGenOpticalAmplifierProdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preAmp", 1),
          ("boostAmp", 2),
          ("midStageAmp", 3))
    )


_AdGenOpticalAmplifierProdType_Type.__name__ = "Integer32"
_AdGenOpticalAmplifierProdType_Object = MibTableColumn
adGenOpticalAmplifierProdType = _AdGenOpticalAmplifierProdType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 1),
    _AdGenOpticalAmplifierProdType_Type()
)
adGenOpticalAmplifierProdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierProdType.setStatus("current")


class _AdGenOpticalAmplifierStatus_Type(Integer32):
    """Custom type adGenOpticalAmplifierStatus based on Integer32"""
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
        *(("moduleDisabled", 1),
          ("eyeSafeMode", 2),
          ("moduleOk", 3),
          ("powerOrGainLimited", 4))
    )


_AdGenOpticalAmplifierStatus_Type.__name__ = "Integer32"
_AdGenOpticalAmplifierStatus_Object = MibTableColumn
adGenOpticalAmplifierStatus = _AdGenOpticalAmplifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 2),
    _AdGenOpticalAmplifierStatus_Type()
)
adGenOpticalAmplifierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierStatus.setStatus("current")
_AdGenOpticalAmplifierInputPower_Type = Integer32
_AdGenOpticalAmplifierInputPower_Object = MibTableColumn
adGenOpticalAmplifierInputPower = _AdGenOpticalAmplifierInputPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 3),
    _AdGenOpticalAmplifierInputPower_Type()
)
adGenOpticalAmplifierInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPower.setStatus("current")
_AdGenOpticalAmplifierOutputPower_Type = Integer32
_AdGenOpticalAmplifierOutputPower_Object = MibTableColumn
adGenOpticalAmplifierOutputPower = _AdGenOpticalAmplifierOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 4),
    _AdGenOpticalAmplifierOutputPower_Type()
)
adGenOpticalAmplifierOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPower.setStatus("current")
_AdGenOpticalAmplifierGain_Type = Integer32
_AdGenOpticalAmplifierGain_Object = MibTableColumn
adGenOpticalAmplifierGain = _AdGenOpticalAmplifierGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 5),
    _AdGenOpticalAmplifierGain_Type()
)
adGenOpticalAmplifierGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierGain.setStatus("current")
_AdGenOpticalAmplifierCaseTemperature_Type = Integer32
_AdGenOpticalAmplifierCaseTemperature_Object = MibTableColumn
adGenOpticalAmplifierCaseTemperature = _AdGenOpticalAmplifierCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 6),
    _AdGenOpticalAmplifierCaseTemperature_Type()
)
adGenOpticalAmplifierCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierCaseTemperature.setStatus("current")
_AdGenOpticalAmplifierBoardTemperature_Type = Integer32
_AdGenOpticalAmplifierBoardTemperature_Object = MibTableColumn
adGenOpticalAmplifierBoardTemperature = _AdGenOpticalAmplifierBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 7),
    _AdGenOpticalAmplifierBoardTemperature_Type()
)
adGenOpticalAmplifierBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierBoardTemperature.setStatus("current")
_AdGenOpticalAmplifierPumpTemperature_Type = Integer32
_AdGenOpticalAmplifierPumpTemperature_Object = MibTableColumn
adGenOpticalAmplifierPumpTemperature = _AdGenOpticalAmplifierPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 8),
    _AdGenOpticalAmplifierPumpTemperature_Type()
)
adGenOpticalAmplifierPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierPumpTemperature.setStatus("current")
_AdGenOpticalAmplifierLaserPumpOperatingCurrent_Type = Integer32
_AdGenOpticalAmplifierLaserPumpOperatingCurrent_Object = MibTableColumn
adGenOpticalAmplifierLaserPumpOperatingCurrent = _AdGenOpticalAmplifierLaserPumpOperatingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 9),
    _AdGenOpticalAmplifierLaserPumpOperatingCurrent_Type()
)
adGenOpticalAmplifierLaserPumpOperatingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierLaserPumpOperatingCurrent.setStatus("current")
_AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Type = Integer32
_AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Object = MibTableColumn
adGenOpticalAmplifierLaserPumpEndOfLifeCurrent = _AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 10),
    _AdGenOpticalAmplifierLaserPumpEndOfLifeCurrent_Type()
)
adGenOpticalAmplifierLaserPumpEndOfLifeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierLaserPumpEndOfLifeCurrent.setStatus("current")
_AdGenOpticalAmplifierLaserPumpReflectedPower_Type = Integer32
_AdGenOpticalAmplifierLaserPumpReflectedPower_Object = MibTableColumn
adGenOpticalAmplifierLaserPumpReflectedPower = _AdGenOpticalAmplifierLaserPumpReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 11),
    _AdGenOpticalAmplifierLaserPumpReflectedPower_Type()
)
adGenOpticalAmplifierLaserPumpReflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierLaserPumpReflectedPower.setStatus("current")


class _AdGenOpticalAmplifierInputPowerThreshold_Type(Integer32):
    """Custom type adGenOpticalAmplifierInputPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 31),
        ValueRangeConstraint(32767, 32767),
    )


_AdGenOpticalAmplifierInputPowerThreshold_Type.__name__ = "Integer32"
_AdGenOpticalAmplifierInputPowerThreshold_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThreshold = _AdGenOpticalAmplifierInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 12),
    _AdGenOpticalAmplifierInputPowerThreshold_Type()
)
adGenOpticalAmplifierInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThreshold.setStatus("deprecated")
_AdGenOpticalAmplifierIfIndexReference_Type = InterfaceIndex
_AdGenOpticalAmplifierIfIndexReference_Object = MibTableColumn
adGenOpticalAmplifierIfIndexReference = _AdGenOpticalAmplifierIfIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 13),
    _AdGenOpticalAmplifierIfIndexReference_Type()
)
adGenOpticalAmplifierIfIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierIfIndexReference.setStatus("current")
_AdGenOpticalAmplifierInputPowerThresholdLow_Type = Integer32
_AdGenOpticalAmplifierInputPowerThresholdLow_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThresholdLow = _AdGenOpticalAmplifierInputPowerThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 14),
    _AdGenOpticalAmplifierInputPowerThresholdLow_Type()
)
adGenOpticalAmplifierInputPowerThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdLow.setStatus("current")
_AdGenOpticalAmplifierInputPowerThresholdHigh_Type = Integer32
_AdGenOpticalAmplifierInputPowerThresholdHigh_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThresholdHigh = _AdGenOpticalAmplifierInputPowerThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 15),
    _AdGenOpticalAmplifierInputPowerThresholdHigh_Type()
)
adGenOpticalAmplifierInputPowerThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdHigh.setStatus("current")
_AdGenOpticalAmplifierOutputPowerThresholdLow_Type = Integer32
_AdGenOpticalAmplifierOutputPowerThresholdLow_Object = MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdLow = _AdGenOpticalAmplifierOutputPowerThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 16),
    _AdGenOpticalAmplifierOutputPowerThresholdLow_Type()
)
adGenOpticalAmplifierOutputPowerThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdLow.setStatus("current")
_AdGenOpticalAmplifierOutputPowerThresholdHigh_Type = Integer32
_AdGenOpticalAmplifierOutputPowerThresholdHigh_Object = MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdHigh = _AdGenOpticalAmplifierOutputPowerThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 17),
    _AdGenOpticalAmplifierOutputPowerThresholdHigh_Type()
)
adGenOpticalAmplifierOutputPowerThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdHigh.setStatus("current")
_AdGenOpticalAmplifierMidStageAttenuation_Type = Integer32
_AdGenOpticalAmplifierMidStageAttenuation_Object = MibTableColumn
adGenOpticalAmplifierMidStageAttenuation = _AdGenOpticalAmplifierMidStageAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 18),
    _AdGenOpticalAmplifierMidStageAttenuation_Type()
)
adGenOpticalAmplifierMidStageAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMidStageAttenuation.setStatus("current")
_AdGenOpticalAmplifierVariableGain_Type = Integer32
_AdGenOpticalAmplifierVariableGain_Object = MibTableColumn
adGenOpticalAmplifierVariableGain = _AdGenOpticalAmplifierVariableGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 19),
    _AdGenOpticalAmplifierVariableGain_Type()
)
adGenOpticalAmplifierVariableGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierVariableGain.setStatus("current")


class _AdGenOpticalAmplifierMode_Type(Integer32):
    """Custom type adGenOpticalAmplifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preAmp", 1),
          ("boostAmp", 2))
    )


_AdGenOpticalAmplifierMode_Type.__name__ = "Integer32"
_AdGenOpticalAmplifierMode_Object = MibTableColumn
adGenOpticalAmplifierMode = _AdGenOpticalAmplifierMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 20),
    _AdGenOpticalAmplifierMode_Type()
)
adGenOpticalAmplifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMode.setStatus("current")


class _AdGenOpticalAmplifierAdminState_Type(Integer32):
    """Custom type adGenOpticalAmplifierAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenOpticalAmplifierAdminState_Type.__name__ = "Integer32"
_AdGenOpticalAmplifierAdminState_Object = MibTableColumn
adGenOpticalAmplifierAdminState = _AdGenOpticalAmplifierAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 21),
    _AdGenOpticalAmplifierAdminState_Type()
)
adGenOpticalAmplifierAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierAdminState.setStatus("current")


class _AdGenOpticalAmplifierOperState_Type(Integer32):
    """Custom type adGenOpticalAmplifierOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenOpticalAmplifierOperState_Type.__name__ = "Integer32"
_AdGenOpticalAmplifierOperState_Object = MibTableColumn
adGenOpticalAmplifierOperState = _AdGenOpticalAmplifierOperState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 1, 1, 22),
    _AdGenOpticalAmplifierOperState_Type()
)
adGenOpticalAmplifierOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOperState.setStatus("current")
_AdGenOpticalAmplifierSupplementTable_Object = MibTable
adGenOpticalAmplifierSupplementTable = _AdGenOpticalAmplifierSupplementTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2)
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierSupplementTable.setStatus("current")
_AdGenOpticalAmplifierSupplementEntry_Object = MibTableRow
adGenOpticalAmplifierSupplementEntry = _AdGenOpticalAmplifierSupplementEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1)
)
adGenOpticalAmplifierSupplementEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierSupplementEntry.setStatus("current")
_AdGenOpticalAmplifierInputPowerThresholdLowMax_Type = Integer32
_AdGenOpticalAmplifierInputPowerThresholdLowMax_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThresholdLowMax = _AdGenOpticalAmplifierInputPowerThresholdLowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 1),
    _AdGenOpticalAmplifierInputPowerThresholdLowMax_Type()
)
adGenOpticalAmplifierInputPowerThresholdLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdLowMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdLowMax.setUnits("dBm")
_AdGenOpticalAmplifierInputPowerThresholdLowMin_Type = Integer32
_AdGenOpticalAmplifierInputPowerThresholdLowMin_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThresholdLowMin = _AdGenOpticalAmplifierInputPowerThresholdLowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 2),
    _AdGenOpticalAmplifierInputPowerThresholdLowMin_Type()
)
adGenOpticalAmplifierInputPowerThresholdLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdLowMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdLowMin.setUnits("dBm")
_AdGenOpticalAmplifierInputPowerThresholdHighMax_Type = Integer32
_AdGenOpticalAmplifierInputPowerThresholdHighMax_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThresholdHighMax = _AdGenOpticalAmplifierInputPowerThresholdHighMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 3),
    _AdGenOpticalAmplifierInputPowerThresholdHighMax_Type()
)
adGenOpticalAmplifierInputPowerThresholdHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdHighMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdHighMax.setUnits("dBm")
_AdGenOpticalAmplifierInputPowerThresholdHighMin_Type = Integer32
_AdGenOpticalAmplifierInputPowerThresholdHighMin_Object = MibTableColumn
adGenOpticalAmplifierInputPowerThresholdHighMin = _AdGenOpticalAmplifierInputPowerThresholdHighMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 4),
    _AdGenOpticalAmplifierInputPowerThresholdHighMin_Type()
)
adGenOpticalAmplifierInputPowerThresholdHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdHighMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierInputPowerThresholdHighMin.setUnits("dBm")
_AdGenOpticalAmplifierOutputPowerThresholdLowMax_Type = Integer32
_AdGenOpticalAmplifierOutputPowerThresholdLowMax_Object = MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdLowMax = _AdGenOpticalAmplifierOutputPowerThresholdLowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 5),
    _AdGenOpticalAmplifierOutputPowerThresholdLowMax_Type()
)
adGenOpticalAmplifierOutputPowerThresholdLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdLowMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdLowMax.setUnits("dBm")
_AdGenOpticalAmplifierOutputPowerThresholdLowMin_Type = Integer32
_AdGenOpticalAmplifierOutputPowerThresholdLowMin_Object = MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdLowMin = _AdGenOpticalAmplifierOutputPowerThresholdLowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 6),
    _AdGenOpticalAmplifierOutputPowerThresholdLowMin_Type()
)
adGenOpticalAmplifierOutputPowerThresholdLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdLowMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdLowMin.setUnits("dBm")
_AdGenOpticalAmplifierOutputPowerThresholdHighMax_Type = Integer32
_AdGenOpticalAmplifierOutputPowerThresholdHighMax_Object = MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdHighMax = _AdGenOpticalAmplifierOutputPowerThresholdHighMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 7),
    _AdGenOpticalAmplifierOutputPowerThresholdHighMax_Type()
)
adGenOpticalAmplifierOutputPowerThresholdHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdHighMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdHighMax.setUnits("dBm")
_AdGenOpticalAmplifierOutputPowerThresholdHighMin_Type = Integer32
_AdGenOpticalAmplifierOutputPowerThresholdHighMin_Object = MibTableColumn
adGenOpticalAmplifierOutputPowerThresholdHighMin = _AdGenOpticalAmplifierOutputPowerThresholdHighMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 8),
    _AdGenOpticalAmplifierOutputPowerThresholdHighMin_Type()
)
adGenOpticalAmplifierOutputPowerThresholdHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdHighMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierOutputPowerThresholdHighMin.setUnits("dBm")
_AdGenOpticalAmplifierMidStageAttenuationMax_Type = Integer32
_AdGenOpticalAmplifierMidStageAttenuationMax_Object = MibTableColumn
adGenOpticalAmplifierMidStageAttenuationMax = _AdGenOpticalAmplifierMidStageAttenuationMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 9),
    _AdGenOpticalAmplifierMidStageAttenuationMax_Type()
)
adGenOpticalAmplifierMidStageAttenuationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMidStageAttenuationMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMidStageAttenuationMax.setUnits("dBm")
_AdGenOpticalAmplifierMidStageAttenuationMin_Type = Integer32
_AdGenOpticalAmplifierMidStageAttenuationMin_Object = MibTableColumn
adGenOpticalAmplifierMidStageAttenuationMin = _AdGenOpticalAmplifierMidStageAttenuationMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 10),
    _AdGenOpticalAmplifierMidStageAttenuationMin_Type()
)
adGenOpticalAmplifierMidStageAttenuationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMidStageAttenuationMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierMidStageAttenuationMin.setUnits("dBm")
_AdGenOpticalAmplifierVariableGainMin_Type = Integer32
_AdGenOpticalAmplifierVariableGainMin_Object = MibTableColumn
adGenOpticalAmplifierVariableGainMin = _AdGenOpticalAmplifierVariableGainMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 11),
    _AdGenOpticalAmplifierVariableGainMin_Type()
)
adGenOpticalAmplifierVariableGainMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierVariableGainMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierVariableGainMin.setUnits("dB")
_AdGenOpticalAmplifierVariableGainMax_Type = Integer32
_AdGenOpticalAmplifierVariableGainMax_Object = MibTableColumn
adGenOpticalAmplifierVariableGainMax = _AdGenOpticalAmplifierVariableGainMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 2, 1, 12),
    _AdGenOpticalAmplifierVariableGainMax_Type()
)
adGenOpticalAmplifierVariableGainMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierVariableGainMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalAmplifierVariableGainMax.setUnits("dB")
_AdGenOpticalAmplifierAlrms_ObjectIdentity = ObjectIdentity
adGenOpticalAmplifierAlrms = _AdGenOpticalAmplifierAlrms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100)
)
_AdGenOpticalAmplifierEvents_ObjectIdentity = ObjectIdentity
adGenOpticalAmplifierEvents = _AdGenOpticalAmplifierEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0)
)

# Managed Objects groups


# Notification objects

adGenInputPowerThrAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 1)
)
adGenInputPowerThrAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenInputPowerThrAlarmClear.setStatus(
        "current"
    )

adGenInputPowerThrAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 2)
)
adGenInputPowerThrAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenInputPowerThrAlrmSet.setStatus(
        "current"
    )

adGenOutputPowerLossClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 3)
)
adGenOutputPowerLossClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOutputPowerLossClear.setStatus(
        "current"
    )

adGenOutputPowerLossAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 4)
)
adGenOutputPowerLossAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOutputPowerLossAlrmSet.setStatus(
        "current"
    )

adGenBoardTempClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 5)
)
adGenBoardTempClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenBoardTempClear.setStatus(
        "current"
    )

adGenBoardTempAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 6)
)
adGenBoardTempAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenBoardTempAlrmSet.setStatus(
        "current"
    )

adGenModuleTempLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 7)
)
adGenModuleTempLowClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenModuleTempLowClear.setStatus(
        "current"
    )

adGenModuleTempLowAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 8)
)
adGenModuleTempLowAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenModuleTempLowAlrmSet.setStatus(
        "current"
    )

adGenModuleTempHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 9)
)
adGenModuleTempHighClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenModuleTempHighClear.setStatus(
        "current"
    )

adGenModuleTempHighAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 10)
)
adGenModuleTempHighAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenModuleTempHighAlrmSet.setStatus(
        "current"
    )

adGenLaserPumpTempClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 11)
)
adGenLaserPumpTempClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenLaserPumpTempClear.setStatus(
        "current"
    )

adGenLaserPumpTempAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 12)
)
adGenLaserPumpTempAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenLaserPumpTempAlrmSet.setStatus(
        "current"
    )

adGenLaserPumpEOLClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 13)
)
adGenLaserPumpEOLClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenLaserPumpEOLClear.setStatus(
        "current"
    )

adGenLaserPumpEOLAlrmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 14)
)
adGenLaserPumpEOLAlrmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenLaserPumpEOLAlrmSet.setStatus(
        "current"
    )

adGenInputPowerThLowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 15)
)
adGenInputPowerThLowAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenInputPowerThLowAlarmClear.setStatus(
        "current"
    )

adGenInputPowerThLowAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 16)
)
adGenInputPowerThLowAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenInputPowerThLowAlarmSet.setStatus(
        "current"
    )

adGenInputPowerThHighAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 17)
)
adGenInputPowerThHighAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenInputPowerThHighAlarmClear.setStatus(
        "current"
    )

adGenInputPowerThHighAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 18)
)
adGenInputPowerThHighAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenInputPowerThHighAlarmSet.setStatus(
        "current"
    )

adGenOutputPowerThLowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 19)
)
adGenOutputPowerThLowAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOutputPowerThLowAlarmClear.setStatus(
        "current"
    )

adGenOutputPowerThLowAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 20)
)
adGenOutputPowerThLowAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOutputPowerThLowAlarmSet.setStatus(
        "current"
    )

adGenOutputPowerThHighAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 21)
)
adGenOutputPowerThHighAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOutputPowerThHighAlarmClear.setStatus(
        "current"
    )

adGenOutputPowerThHighAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 22)
)
adGenOutputPowerThHighAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOutputPowerThHighAlarmSet.setStatus(
        "current"
    )

adGenAmplifierLOSAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 23)
)
adGenAmplifierLOSAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenAmplifierLOSAlarmClear.setStatus(
        "current"
    )

adGenAmplifierLOSAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 24)
)
adGenAmplifierLOSAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenAmplifierLOSAlarmSet.setStatus(
        "current"
    )

adGenOpticalAmplifierLossOfMidStageInActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 25)
)
adGenOpticalAmplifierLossOfMidStageInActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierLossOfMidStageInActiveClear.setStatus(
        "current"
    )

adGenOpticalAmplifierLossOfMidStageInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 41, 1, 100, 0, 26)
)
adGenOpticalAmplifierLossOfMidStageInActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalAmplifierLossOfMidStageInActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-OPTICAL-AMPLIFIER-MIB",
    **{"adGenOpticalAmplifierProduct": adGenOpticalAmplifierProduct,
       "adGenOpticalAmplifierTable": adGenOpticalAmplifierTable,
       "adGenOpticalAmplifierEntry": adGenOpticalAmplifierEntry,
       "adGenOpticalAmplifierProdType": adGenOpticalAmplifierProdType,
       "adGenOpticalAmplifierStatus": adGenOpticalAmplifierStatus,
       "adGenOpticalAmplifierInputPower": adGenOpticalAmplifierInputPower,
       "adGenOpticalAmplifierOutputPower": adGenOpticalAmplifierOutputPower,
       "adGenOpticalAmplifierGain": adGenOpticalAmplifierGain,
       "adGenOpticalAmplifierCaseTemperature": adGenOpticalAmplifierCaseTemperature,
       "adGenOpticalAmplifierBoardTemperature": adGenOpticalAmplifierBoardTemperature,
       "adGenOpticalAmplifierPumpTemperature": adGenOpticalAmplifierPumpTemperature,
       "adGenOpticalAmplifierLaserPumpOperatingCurrent": adGenOpticalAmplifierLaserPumpOperatingCurrent,
       "adGenOpticalAmplifierLaserPumpEndOfLifeCurrent": adGenOpticalAmplifierLaserPumpEndOfLifeCurrent,
       "adGenOpticalAmplifierLaserPumpReflectedPower": adGenOpticalAmplifierLaserPumpReflectedPower,
       "adGenOpticalAmplifierInputPowerThreshold": adGenOpticalAmplifierInputPowerThreshold,
       "adGenOpticalAmplifierIfIndexReference": adGenOpticalAmplifierIfIndexReference,
       "adGenOpticalAmplifierInputPowerThresholdLow": adGenOpticalAmplifierInputPowerThresholdLow,
       "adGenOpticalAmplifierInputPowerThresholdHigh": adGenOpticalAmplifierInputPowerThresholdHigh,
       "adGenOpticalAmplifierOutputPowerThresholdLow": adGenOpticalAmplifierOutputPowerThresholdLow,
       "adGenOpticalAmplifierOutputPowerThresholdHigh": adGenOpticalAmplifierOutputPowerThresholdHigh,
       "adGenOpticalAmplifierMidStageAttenuation": adGenOpticalAmplifierMidStageAttenuation,
       "adGenOpticalAmplifierVariableGain": adGenOpticalAmplifierVariableGain,
       "adGenOpticalAmplifierMode": adGenOpticalAmplifierMode,
       "adGenOpticalAmplifierAdminState": adGenOpticalAmplifierAdminState,
       "adGenOpticalAmplifierOperState": adGenOpticalAmplifierOperState,
       "adGenOpticalAmplifierSupplementTable": adGenOpticalAmplifierSupplementTable,
       "adGenOpticalAmplifierSupplementEntry": adGenOpticalAmplifierSupplementEntry,
       "adGenOpticalAmplifierInputPowerThresholdLowMax": adGenOpticalAmplifierInputPowerThresholdLowMax,
       "adGenOpticalAmplifierInputPowerThresholdLowMin": adGenOpticalAmplifierInputPowerThresholdLowMin,
       "adGenOpticalAmplifierInputPowerThresholdHighMax": adGenOpticalAmplifierInputPowerThresholdHighMax,
       "adGenOpticalAmplifierInputPowerThresholdHighMin": adGenOpticalAmplifierInputPowerThresholdHighMin,
       "adGenOpticalAmplifierOutputPowerThresholdLowMax": adGenOpticalAmplifierOutputPowerThresholdLowMax,
       "adGenOpticalAmplifierOutputPowerThresholdLowMin": adGenOpticalAmplifierOutputPowerThresholdLowMin,
       "adGenOpticalAmplifierOutputPowerThresholdHighMax": adGenOpticalAmplifierOutputPowerThresholdHighMax,
       "adGenOpticalAmplifierOutputPowerThresholdHighMin": adGenOpticalAmplifierOutputPowerThresholdHighMin,
       "adGenOpticalAmplifierMidStageAttenuationMax": adGenOpticalAmplifierMidStageAttenuationMax,
       "adGenOpticalAmplifierMidStageAttenuationMin": adGenOpticalAmplifierMidStageAttenuationMin,
       "adGenOpticalAmplifierVariableGainMin": adGenOpticalAmplifierVariableGainMin,
       "adGenOpticalAmplifierVariableGainMax": adGenOpticalAmplifierVariableGainMax,
       "adGenOpticalAmplifierAlrms": adGenOpticalAmplifierAlrms,
       "adGenOpticalAmplifierEvents": adGenOpticalAmplifierEvents,
       "adGenInputPowerThrAlarmClear": adGenInputPowerThrAlarmClear,
       "adGenInputPowerThrAlrmSet": adGenInputPowerThrAlrmSet,
       "adGenOutputPowerLossClear": adGenOutputPowerLossClear,
       "adGenOutputPowerLossAlrmSet": adGenOutputPowerLossAlrmSet,
       "adGenBoardTempClear": adGenBoardTempClear,
       "adGenBoardTempAlrmSet": adGenBoardTempAlrmSet,
       "adGenModuleTempLowClear": adGenModuleTempLowClear,
       "adGenModuleTempLowAlrmSet": adGenModuleTempLowAlrmSet,
       "adGenModuleTempHighClear": adGenModuleTempHighClear,
       "adGenModuleTempHighAlrmSet": adGenModuleTempHighAlrmSet,
       "adGenLaserPumpTempClear": adGenLaserPumpTempClear,
       "adGenLaserPumpTempAlrmSet": adGenLaserPumpTempAlrmSet,
       "adGenLaserPumpEOLClear": adGenLaserPumpEOLClear,
       "adGenLaserPumpEOLAlrmSet": adGenLaserPumpEOLAlrmSet,
       "adGenInputPowerThLowAlarmClear": adGenInputPowerThLowAlarmClear,
       "adGenInputPowerThLowAlarmSet": adGenInputPowerThLowAlarmSet,
       "adGenInputPowerThHighAlarmClear": adGenInputPowerThHighAlarmClear,
       "adGenInputPowerThHighAlarmSet": adGenInputPowerThHighAlarmSet,
       "adGenOutputPowerThLowAlarmClear": adGenOutputPowerThLowAlarmClear,
       "adGenOutputPowerThLowAlarmSet": adGenOutputPowerThLowAlarmSet,
       "adGenOutputPowerThHighAlarmClear": adGenOutputPowerThHighAlarmClear,
       "adGenOutputPowerThHighAlarmSet": adGenOutputPowerThHighAlarmSet,
       "adGenAmplifierLOSAlarmClear": adGenAmplifierLOSAlarmClear,
       "adGenAmplifierLOSAlarmSet": adGenAmplifierLOSAlarmSet,
       "adGenOpticalAmplifierLossOfMidStageInActiveClear": adGenOpticalAmplifierLossOfMidStageInActiveClear,
       "adGenOpticalAmplifierLossOfMidStageInActive": adGenOpticalAmplifierLossOfMidStageInActive,
       "adGenOpticalAmplifierMIB": adGenOpticalAmplifierMIB}
)
