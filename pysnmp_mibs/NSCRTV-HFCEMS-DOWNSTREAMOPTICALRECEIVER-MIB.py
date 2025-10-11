# SNMP MIB module (NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:34 2025
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

(dorIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "dorIdent")

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

_DorVendorOID_Type = ObjectIdentifier
_DorVendorOID_Object = MibScalar
dorVendorOID = _DorVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 1),
    _DorVendorOID_Type()
)
dorVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorVendorOID.setStatus("optional")
_DorRxInputNumber_Type = Integer32
_DorRxInputNumber_Object = MibScalar
dorRxInputNumber = _DorRxInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 2),
    _DorRxInputNumber_Type()
)
dorRxInputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorRxInputNumber.setStatus("mandatory")
_DorRxInputTable_Object = MibTable
dorRxInputTable = _DorRxInputTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 3)
)
if mibBuilder.loadTexts:
    dorRxInputTable.setStatus("mandatory")
_DorRxInputEntry_Object = MibTableRow
dorRxInputEntry = _DorRxInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 3, 1)
)
dorRxInputEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB", "dorInputIndex"),
)
if mibBuilder.loadTexts:
    dorRxInputEntry.setStatus("mandatory")
_DorInputIndex_Type = Integer32
_DorInputIndex_Object = MibTableColumn
dorInputIndex = _DorInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 3, 1, 1),
    _DorInputIndex_Type()
)
dorInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorInputIndex.setStatus("mandatory")
_DorInputPower_Type = Integer32
_DorInputPower_Object = MibTableColumn
dorInputPower = _DorInputPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 3, 1, 2),
    _DorInputPower_Type()
)
dorInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorInputPower.setStatus("mandatory")
_DorInputWavelengthControl_Type = Integer32
_DorInputWavelengthControl_Object = MibTableColumn
dorInputWavelengthControl = _DorInputWavelengthControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 3, 1, 3),
    _DorInputWavelengthControl_Type()
)
dorInputWavelengthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorInputWavelengthControl.setStatus("mandatory")


class _DorInputStatus_Type(Integer32):
    """Custom type dorInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2))
    )


_DorInputStatus_Type.__name__ = "Integer32"
_DorInputStatus_Object = MibTableColumn
dorInputStatus = _DorInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 3, 1, 4),
    _DorInputStatus_Type()
)
dorInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorInputStatus.setStatus("mandatory")
_DorRxOutputNumber_Type = Integer32
_DorRxOutputNumber_Object = MibScalar
dorRxOutputNumber = _DorRxOutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 4),
    _DorRxOutputNumber_Type()
)
dorRxOutputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorRxOutputNumber.setStatus("mandatory")
_DorRxOutputTable_Object = MibTable
dorRxOutputTable = _DorRxOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5)
)
if mibBuilder.loadTexts:
    dorRxOutputTable.setStatus("mandatory")
_DorRxOutputEntry_Object = MibTableRow
dorRxOutputEntry = _DorRxOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1)
)
dorRxOutputEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB", "dorOutputIndex"),
)
if mibBuilder.loadTexts:
    dorRxOutputEntry.setStatus("mandatory")
_DorOutputIndex_Type = Integer32
_DorOutputIndex_Object = MibTableColumn
dorOutputIndex = _DorOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 1),
    _DorOutputIndex_Type()
)
dorOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorOutputIndex.setStatus("mandatory")


class _DorOutputControl_Type(Integer32):
    """Custom type dorOutputControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DorOutputControl_Type.__name__ = "Integer32"
_DorOutputControl_Object = MibTableColumn
dorOutputControl = _DorOutputControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 2),
    _DorOutputControl_Type()
)
dorOutputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorOutputControl.setStatus("mandatory")


class _DorOutputGainType_Type(Integer32):
    """Custom type dorOutputGainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constantLevel", 1),
          ("constantGain", 2))
    )


_DorOutputGainType_Type.__name__ = "Integer32"
_DorOutputGainType_Object = MibTableColumn
dorOutputGainType = _DorOutputGainType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 3),
    _DorOutputGainType_Type()
)
dorOutputGainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorOutputGainType.setStatus("optional")
_DorOutputLevel_Type = Integer32
_DorOutputLevel_Object = MibTableColumn
dorOutputLevel = _DorOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 4),
    _DorOutputLevel_Type()
)
dorOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorOutputLevel.setStatus("mandatory")
_DorConfiguartionOutputLevel_Type = Integer32
_DorConfiguartionOutputLevel_Object = MibTableColumn
dorConfiguartionOutputLevel = _DorConfiguartionOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 5),
    _DorConfiguartionOutputLevel_Type()
)
dorConfiguartionOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorConfiguartionOutputLevel.setStatus("optional")
_DorOutputRFlevelatt_Type = Integer32
_DorOutputRFlevelatt_Object = MibTableColumn
dorOutputRFlevelatt = _DorOutputRFlevelatt_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 6),
    _DorOutputRFlevelatt_Type()
)
dorOutputRFlevelatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorOutputRFlevelatt.setStatus("mandatory")
_DorConfigurationOutputRFlevelatt_Type = Integer32
_DorConfigurationOutputRFlevelatt_Object = MibTableColumn
dorConfigurationOutputRFlevelatt = _DorConfigurationOutputRFlevelatt_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 7),
    _DorConfigurationOutputRFlevelatt_Type()
)
dorConfigurationOutputRFlevelatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorConfigurationOutputRFlevelatt.setStatus("optional")
_DorOutputRFName_Type = DisplayString
_DorOutputRFName_Object = MibTableColumn
dorOutputRFName = _DorOutputRFName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 5, 1, 8),
    _DorOutputRFName_Type()
)
dorOutputRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorOutputRFName.setStatus("mandatory")


class _DorNumberDCPowerSupply_Type(Integer32):
    """Custom type dorNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DorNumberDCPowerSupply_Type.__name__ = "Integer32"
_DorNumberDCPowerSupply_Object = MibScalar
dorNumberDCPowerSupply = _DorNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 6),
    _DorNumberDCPowerSupply_Type()
)
dorNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorNumberDCPowerSupply.setStatus("mandatory")


class _DorDCPowerSupplyMode_Type(Integer32):
    """Custom type dorDCPowerSupplyMode based on Integer32"""
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


_DorDCPowerSupplyMode_Type.__name__ = "Integer32"
_DorDCPowerSupplyMode_Object = MibScalar
dorDCPowerSupplyMode = _DorDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 7),
    _DorDCPowerSupplyMode_Type()
)
dorDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorDCPowerSupplyMode.setStatus("optional")
_DorDCPowerTable_Object = MibTable
dorDCPowerTable = _DorDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 8)
)
if mibBuilder.loadTexts:
    dorDCPowerTable.setStatus("mandatory")
_DorDCPowerEntry_Object = MibTableRow
dorDCPowerEntry = _DorDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 8, 1)
)
dorDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB", "dorDCPowerIndex"),
)
if mibBuilder.loadTexts:
    dorDCPowerEntry.setStatus("mandatory")
_DorDCPowerIndex_Type = Integer32
_DorDCPowerIndex_Object = MibTableColumn
dorDCPowerIndex = _DorDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 8, 1, 1),
    _DorDCPowerIndex_Type()
)
dorDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorDCPowerIndex.setStatus("mandatory")


class _DorDCPowerVoltage_Type(Integer32):
    """Custom type dorDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_DorDCPowerVoltage_Type.__name__ = "Integer32"
_DorDCPowerVoltage_Object = MibTableColumn
dorDCPowerVoltage = _DorDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 8, 1, 2),
    _DorDCPowerVoltage_Type()
)
dorDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorDCPowerVoltage.setStatus("mandatory")


class _DorDCPowerCurrent_Type(Integer32):
    """Custom type dorDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DorDCPowerCurrent_Type.__name__ = "Integer32"
_DorDCPowerCurrent_Object = MibTableColumn
dorDCPowerCurrent = _DorDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 8, 1, 3),
    _DorDCPowerCurrent_Type()
)
dorDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorDCPowerCurrent.setStatus("optional")
_DorDCPowerName_Type = DisplayString
_DorDCPowerName_Object = MibTableColumn
dorDCPowerName = _DorDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 8, 1, 4),
    _DorDCPowerName_Type()
)
dorDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorDCPowerName.setStatus("mandatory")


class _DorReverseOptPower_Type(Integer32):
    """Custom type dorReverseOptPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_DorReverseOptPower_Type.__name__ = "Integer32"
_DorReverseOptPower_Object = MibScalar
dorReverseOptPower = _DorReverseOptPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 9),
    _DorReverseOptPower_Type()
)
dorReverseOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorReverseOptPower.setStatus("mandatory")


class _DorReverseCurrent_Type(Integer32):
    """Custom type dorReverseCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DorReverseCurrent_Type.__name__ = "Integer32"
_DorReverseCurrent_Object = MibScalar
dorReverseCurrent = _DorReverseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 10),
    _DorReverseCurrent_Type()
)
dorReverseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dorReverseCurrent.setStatus("mandatory")


class _DorChannelNum_Type(Integer32):
    """Custom type dorChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DorChannelNum_Type.__name__ = "Integer32"
_DorChannelNum_Object = MibScalar
dorChannelNum = _DorChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9, 11),
    _DorChannelNum_Type()
)
dorChannelNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dorChannelNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-DOWNSTREAMOPTICALRECEIVER-MIB",
    **{"dorVendorOID": dorVendorOID,
       "dorRxInputNumber": dorRxInputNumber,
       "dorRxInputTable": dorRxInputTable,
       "dorRxInputEntry": dorRxInputEntry,
       "dorInputIndex": dorInputIndex,
       "dorInputPower": dorInputPower,
       "dorInputWavelengthControl": dorInputWavelengthControl,
       "dorInputStatus": dorInputStatus,
       "dorRxOutputNumber": dorRxOutputNumber,
       "dorRxOutputTable": dorRxOutputTable,
       "dorRxOutputEntry": dorRxOutputEntry,
       "dorOutputIndex": dorOutputIndex,
       "dorOutputControl": dorOutputControl,
       "dorOutputGainType": dorOutputGainType,
       "dorOutputLevel": dorOutputLevel,
       "dorConfiguartionOutputLevel": dorConfiguartionOutputLevel,
       "dorOutputRFlevelatt": dorOutputRFlevelatt,
       "dorConfigurationOutputRFlevelatt": dorConfigurationOutputRFlevelatt,
       "dorOutputRFName": dorOutputRFName,
       "dorNumberDCPowerSupply": dorNumberDCPowerSupply,
       "dorDCPowerSupplyMode": dorDCPowerSupplyMode,
       "dorDCPowerTable": dorDCPowerTable,
       "dorDCPowerEntry": dorDCPowerEntry,
       "dorDCPowerIndex": dorDCPowerIndex,
       "dorDCPowerVoltage": dorDCPowerVoltage,
       "dorDCPowerCurrent": dorDCPowerCurrent,
       "dorDCPowerName": dorDCPowerName,
       "dorReverseOptPower": dorReverseOptPower,
       "dorReverseCurrent": dorReverseCurrent,
       "dorChannelNum": dorChannelNum}
)
