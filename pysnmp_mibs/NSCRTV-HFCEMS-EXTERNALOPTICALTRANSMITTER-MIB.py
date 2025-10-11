# SNMP MIB module (NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:40 2025
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

(otxIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "otxIdent")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtxVendorOID_Type = ObjectIdentifier
_OtxVendorOID_Object = MibScalar
otxVendorOID = _OtxVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 1),
    _OtxVendorOID_Type()
)
otxVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxVendorOID.setStatus("optional")
_OtxSlotNumber_Type = Integer32
_OtxSlotNumber_Object = MibScalar
otxSlotNumber = _OtxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 2),
    _OtxSlotNumber_Type()
)
otxSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxSlotNumber.setStatus("mandatory")
_OtxModuleTable_Object = MibTable
otxModuleTable = _OtxModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3)
)
if mibBuilder.loadTexts:
    otxModuleTable.setStatus("mandatory")
_OtxModuleEntry_Object = MibTableRow
otxModuleEntry = _OtxModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1)
)
otxModuleEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB", "otxModuleIndex"),
)
if mibBuilder.loadTexts:
    otxModuleEntry.setStatus("mandatory")
_OtxModuleIndex_Type = Integer32
_OtxModuleIndex_Object = MibTableColumn
otxModuleIndex = _OtxModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 1),
    _OtxModuleIndex_Type()
)
otxModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxModuleIndex.setStatus("mandatory")


class _OtxLaserControl_Type(Integer32):
    """Custom type otxLaserControl based on Integer32"""
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


_OtxLaserControl_Type.__name__ = "Integer32"
_OtxLaserControl_Object = MibTableColumn
otxLaserControl = _OtxLaserControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 2),
    _OtxLaserControl_Type()
)
otxLaserControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxLaserControl.setStatus("mandatory")


class _OtxConfigurationAGCMode_Type(Integer32):
    """Custom type otxConfigurationAGCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeAgcOff", 1),
          ("modeCWUnmodulatedAgcOn", 2),
          ("modeVideoModulatedAgcOn", 3))
    )


_OtxConfigurationAGCMode_Type.__name__ = "Integer32"
_OtxConfigurationAGCMode_Object = MibTableColumn
otxConfigurationAGCMode = _OtxConfigurationAGCMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 3),
    _OtxConfigurationAGCMode_Type()
)
otxConfigurationAGCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxConfigurationAGCMode.setStatus("optional")
_OtxConfigurationOmi_Type = Integer32
_OtxConfigurationOmi_Object = MibTableColumn
otxConfigurationOmi = _OtxConfigurationOmi_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 4),
    _OtxConfigurationOmi_Type()
)
otxConfigurationOmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxConfigurationOmi.setStatus("optional")
_OtxConfigurationRfGain_Type = Integer32
_OtxConfigurationRfGain_Object = MibTableColumn
otxConfigurationRfGain = _OtxConfigurationRfGain_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 5),
    _OtxConfigurationRfGain_Type()
)
otxConfigurationRfGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxConfigurationRfGain.setStatus("optional")
_OtxConfigurationSbsSuppression_Type = Integer32
_OtxConfigurationSbsSuppression_Object = MibTableColumn
otxConfigurationSbsSuppression = _OtxConfigurationSbsSuppression_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 6),
    _OtxConfigurationSbsSuppression_Type()
)
otxConfigurationSbsSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxConfigurationSbsSuppression.setStatus("optional")
_OtxConfigurationChannelDistance_Type = Integer32
_OtxConfigurationChannelDistance_Object = MibTableColumn
otxConfigurationChannelDistance = _OtxConfigurationChannelDistance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 7),
    _OtxConfigurationChannelDistance_Type()
)
otxConfigurationChannelDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxConfigurationChannelDistance.setStatus("optional")
_OtxConfigurationItuFrequency_Type = Integer32
_OtxConfigurationItuFrequency_Object = MibTableColumn
otxConfigurationItuFrequency = _OtxConfigurationItuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 8),
    _OtxConfigurationItuFrequency_Type()
)
otxConfigurationItuFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxConfigurationItuFrequency.setStatus("optional")
_OtxItuFrequencyMin_Type = Integer32
_OtxItuFrequencyMin_Object = MibTableColumn
otxItuFrequencyMin = _OtxItuFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 9),
    _OtxItuFrequencyMin_Type()
)
otxItuFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxItuFrequencyMin.setStatus("optional")
_OtxItuFrequencyMax_Type = Integer32
_OtxItuFrequencyMax_Object = MibTableColumn
otxItuFrequencyMax = _OtxItuFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 10),
    _OtxItuFrequencyMax_Type()
)
otxItuFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxItuFrequencyMax.setStatus("optional")
_OtxItuFrequencyStep_Type = Integer32
_OtxItuFrequencyStep_Object = MibTableColumn
otxItuFrequencyStep = _OtxItuFrequencyStep_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 11),
    _OtxItuFrequencyStep_Type()
)
otxItuFrequencyStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxItuFrequencyStep.setStatus("optional")
_OtxInputRFLevel_Type = Integer32
_OtxInputRFLevel_Object = MibTableColumn
otxInputRFLevel = _OtxInputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 12),
    _OtxInputRFLevel_Type()
)
otxInputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxInputRFLevel.setStatus("optional")
_OtxRfGain_Type = Integer32
_OtxRfGain_Object = MibTableColumn
otxRfGain = _OtxRfGain_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 13),
    _OtxRfGain_Type()
)
otxRfGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxRfGain.setStatus("optional")
_OtxLaserCurrent_Type = Integer32
_OtxLaserCurrent_Object = MibTableColumn
otxLaserCurrent = _OtxLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 14),
    _OtxLaserCurrent_Type()
)
otxLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxLaserCurrent.setStatus("mandatory")
_OtxLaserOutputPower_Type = Integer32
_OtxLaserOutputPower_Object = MibTableColumn
otxLaserOutputPower = _OtxLaserOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 15),
    _OtxLaserOutputPower_Type()
)
otxLaserOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxLaserOutputPower.setStatus("mandatory")
_OtxLaserTemperature_Type = Integer32
_OtxLaserTemperature_Object = MibTableColumn
otxLaserTemperature = _OtxLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 16),
    _OtxLaserTemperature_Type()
)
otxLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxLaserTemperature.setStatus("mandatory")
_OtxLaserTecCurrent_Type = Integer32
_OtxLaserTecCurrent_Object = MibTableColumn
otxLaserTecCurrent = _OtxLaserTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 17),
    _OtxLaserTecCurrent_Type()
)
otxLaserTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxLaserTecCurrent.setStatus("mandatory")
_OtxOmi_Type = Integer32
_OtxOmi_Object = MibTableColumn
otxOmi = _OtxOmi_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 3, 1, 18),
    _OtxOmi_Type()
)
otxOmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxOmi.setStatus("optional")
_OtxFansNumber_Type = Integer32
_OtxFansNumber_Object = MibScalar
otxFansNumber = _OtxFansNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 4),
    _OtxFansNumber_Type()
)
otxFansNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxFansNumber.setStatus("mandatory")
_OtxFansTable_Object = MibTable
otxFansTable = _OtxFansTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5)
)
if mibBuilder.loadTexts:
    otxFansTable.setStatus("optional")
_OtxFansEntry_Object = MibTableRow
otxFansEntry = _OtxFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5, 1)
)
otxFansEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB", "otxFansIndex"),
)
if mibBuilder.loadTexts:
    otxFansEntry.setStatus("optional")
_OtxFansIndex_Type = Integer32
_OtxFansIndex_Object = MibTableColumn
otxFansIndex = _OtxFansIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5, 1, 1),
    _OtxFansIndex_Type()
)
otxFansIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxFansIndex.setStatus("optional")


class _OtxFansState_Type(Integer32):
    """Custom type otxFansState based on Integer32"""
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
          ("fault", 2),
          ("off", 3))
    )


_OtxFansState_Type.__name__ = "Integer32"
_OtxFansState_Object = MibTableColumn
otxFansState = _OtxFansState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5, 1, 2),
    _OtxFansState_Type()
)
otxFansState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxFansState.setStatus("optional")
_OtxFansSpeed_Type = Integer32
_OtxFansSpeed_Object = MibTableColumn
otxFansSpeed = _OtxFansSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5, 1, 3),
    _OtxFansSpeed_Type()
)
otxFansSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxFansSpeed.setStatus("optional")


class _OtxFansControl_Type(Integer32):
    """Custom type otxFansControl based on Integer32"""
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


_OtxFansControl_Type.__name__ = "Integer32"
_OtxFansControl_Object = MibTableColumn
otxFansControl = _OtxFansControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5, 1, 4),
    _OtxFansControl_Type()
)
otxFansControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otxFansControl.setStatus("optional")
_OtxFansName_Type = DisplayString
_OtxFansName_Object = MibTableColumn
otxFansName = _OtxFansName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 5, 1, 5),
    _OtxFansName_Type()
)
otxFansName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxFansName.setStatus("optional")


class _OtxNumberDCPowerSupply_Type(Integer32):
    """Custom type otxNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_OtxNumberDCPowerSupply_Type.__name__ = "Integer32"
_OtxNumberDCPowerSupply_Object = MibScalar
otxNumberDCPowerSupply = _OtxNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 6),
    _OtxNumberDCPowerSupply_Type()
)
otxNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxNumberDCPowerSupply.setStatus("mandatory")


class _OtxDCPowerSupplyMode_Type(Integer32):
    """Custom type otxDCPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadsharing", 1),
          ("switchedRedundant", 2),
          ("aloneSupply", 3))
    )


_OtxDCPowerSupplyMode_Type.__name__ = "Integer32"
_OtxDCPowerSupplyMode_Object = MibScalar
otxDCPowerSupplyMode = _OtxDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 7),
    _OtxDCPowerSupplyMode_Type()
)
otxDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxDCPowerSupplyMode.setStatus("optional")
_OtxDCPowerTable_Object = MibTable
otxDCPowerTable = _OtxDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 8)
)
if mibBuilder.loadTexts:
    otxDCPowerTable.setStatus("mandatory")
_OtxDCPowerEntry_Object = MibTableRow
otxDCPowerEntry = _OtxDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 8, 1)
)
otxDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB", "otxDCPowerIndex"),
)
if mibBuilder.loadTexts:
    otxDCPowerEntry.setStatus("mandatory")
_OtxDCPowerIndex_Type = Integer32
_OtxDCPowerIndex_Object = MibTableColumn
otxDCPowerIndex = _OtxDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 8, 1, 1),
    _OtxDCPowerIndex_Type()
)
otxDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxDCPowerIndex.setStatus("mandatory")


class _OtxDCPowerVoltage_Type(Integer32):
    """Custom type otxDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OtxDCPowerVoltage_Type.__name__ = "Integer32"
_OtxDCPowerVoltage_Object = MibTableColumn
otxDCPowerVoltage = _OtxDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 8, 1, 2),
    _OtxDCPowerVoltage_Type()
)
otxDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxDCPowerVoltage.setStatus("mandatory")


class _OtxDCPowerCurrent_Type(Integer32):
    """Custom type otxDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OtxDCPowerCurrent_Type.__name__ = "Integer32"
_OtxDCPowerCurrent_Object = MibTableColumn
otxDCPowerCurrent = _OtxDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 8, 1, 3),
    _OtxDCPowerCurrent_Type()
)
otxDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxDCPowerCurrent.setStatus("optional")
_OtxDCPowerName_Type = DisplayString
_OtxDCPowerName_Object = MibTableColumn
otxDCPowerName = _OtxDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7, 8, 1, 4),
    _OtxDCPowerName_Type()
)
otxDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-EXTERNALOPTICALTRANSMITTER-MIB",
    **{"otxVendorOID": otxVendorOID,
       "otxSlotNumber": otxSlotNumber,
       "otxModuleTable": otxModuleTable,
       "otxModuleEntry": otxModuleEntry,
       "otxModuleIndex": otxModuleIndex,
       "otxLaserControl": otxLaserControl,
       "otxConfigurationAGCMode": otxConfigurationAGCMode,
       "otxConfigurationOmi": otxConfigurationOmi,
       "otxConfigurationRfGain": otxConfigurationRfGain,
       "otxConfigurationSbsSuppression": otxConfigurationSbsSuppression,
       "otxConfigurationChannelDistance": otxConfigurationChannelDistance,
       "otxConfigurationItuFrequency": otxConfigurationItuFrequency,
       "otxItuFrequencyMin": otxItuFrequencyMin,
       "otxItuFrequencyMax": otxItuFrequencyMax,
       "otxItuFrequencyStep": otxItuFrequencyStep,
       "otxInputRFLevel": otxInputRFLevel,
       "otxRfGain": otxRfGain,
       "otxLaserCurrent": otxLaserCurrent,
       "otxLaserOutputPower": otxLaserOutputPower,
       "otxLaserTemperature": otxLaserTemperature,
       "otxLaserTecCurrent": otxLaserTecCurrent,
       "otxOmi": otxOmi,
       "otxFansNumber": otxFansNumber,
       "otxFansTable": otxFansTable,
       "otxFansEntry": otxFansEntry,
       "otxFansIndex": otxFansIndex,
       "otxFansState": otxFansState,
       "otxFansSpeed": otxFansSpeed,
       "otxFansControl": otxFansControl,
       "otxFansName": otxFansName,
       "otxNumberDCPowerSupply": otxNumberDCPowerSupply,
       "otxDCPowerSupplyMode": otxDCPowerSupplyMode,
       "otxDCPowerTable": otxDCPowerTable,
       "otxDCPowerEntry": otxDCPowerEntry,
       "otxDCPowerIndex": otxDCPowerIndex,
       "otxDCPowerVoltage": otxDCPowerVoltage,
       "otxDCPowerCurrent": otxDCPowerCurrent,
       "otxDCPowerName": otxDCPowerName}
)
