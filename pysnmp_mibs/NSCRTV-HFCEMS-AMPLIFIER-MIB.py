# SNMP MIB module (NSCRTV-HFCEMS-AMPLIFIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-AMPLIFIER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:37 2025
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

(addIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "addIdent")

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

_AddVendorOID_Type = ObjectIdentifier
_AddVendorOID_Object = MibScalar
addVendorOID = _AddVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 1),
    _AddVendorOID_Type()
)
addVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addVendorOID.setStatus("optional")


class _AddNumberRFPort_Type(Integer32):
    """Custom type addNumberRFPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AddNumberRFPort_Type.__name__ = "Integer32"
_AddNumberRFPort_Object = MibScalar
addNumberRFPort = _AddNumberRFPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 2),
    _AddNumberRFPort_Type()
)
addNumberRFPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addNumberRFPort.setStatus("mandatory")


class _AddPortMasterAttenuationControl_Type(Integer32):
    """Custom type addPortMasterAttenuationControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("low", 2),
          ("high", 3))
    )


_AddPortMasterAttenuationControl_Type.__name__ = "Integer32"
_AddPortMasterAttenuationControl_Object = MibScalar
addPortMasterAttenuationControl = _AddPortMasterAttenuationControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 3),
    _AddPortMasterAttenuationControl_Type()
)
addPortMasterAttenuationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addPortMasterAttenuationControl.setStatus("optional")
_AddRFPortTable_Object = MibTable
addRFPortTable = _AddRFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4)
)
if mibBuilder.loadTexts:
    addRFPortTable.setStatus("mandatory")
_AddRFPortEntry_Object = MibTableRow
addRFPortEntry = _AddRFPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1)
)
addRFPortEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-AMPLIFIER-MIB", "addRFPortIndex"),
)
if mibBuilder.loadTexts:
    addRFPortEntry.setStatus("mandatory")
_AddRFPortIndex_Type = Integer32
_AddRFPortIndex_Object = MibTableColumn
addRFPortIndex = _AddRFPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 1),
    _AddRFPortIndex_Type()
)
addRFPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortIndex.setStatus("mandatory")


class _AddRFPortControlType_Type(Integer32):
    """Custom type addRFPortControlType based on Integer32"""
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
        *(("alc", 1),
          ("asc", 2),
          ("agc", 3),
          ("none", 4))
    )


_AddRFPortControlType_Type.__name__ = "Integer32"
_AddRFPortControlType_Object = MibTableColumn
addRFPortControlType = _AddRFPortControlType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 2),
    _AddRFPortControlType_Type()
)
addRFPortControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortControlType.setStatus("optional")
_AddRFPortControlLevel_Type = Integer32
_AddRFPortControlLevel_Object = MibTableColumn
addRFPortControlLevel = _AddRFPortControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 3),
    _AddRFPortControlLevel_Type()
)
addRFPortControlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortControlLevel.setStatus("optional")


class _AddRFPortOutputRFLevel_Type(Integer32):
    """Custom type addRFPortOutputRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AddRFPortOutputRFLevel_Type.__name__ = "Integer32"
_AddRFPortOutputRFLevel_Object = MibTableColumn
addRFPortOutputRFLevel = _AddRFPortOutputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 4),
    _AddRFPortOutputRFLevel_Type()
)
addRFPortOutputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortOutputRFLevel.setStatus("optional")
_AddRFPortName_Type = DisplayString
_AddRFPortName_Object = MibTableColumn
addRFPortName = _AddRFPortName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 5),
    _AddRFPortName_Type()
)
addRFPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortName.setStatus("mandatory")


class _AddRFPortReverseAttenuationControl_Type(Integer32):
    """Custom type addRFPortReverseAttenuationControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("low", 2),
          ("high", 3))
    )


_AddRFPortReverseAttenuationControl_Type.__name__ = "Integer32"
_AddRFPortReverseAttenuationControl_Object = MibTableColumn
addRFPortReverseAttenuationControl = _AddRFPortReverseAttenuationControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 6),
    _AddRFPortReverseAttenuationControl_Type()
)
addRFPortReverseAttenuationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addRFPortReverseAttenuationControl.setStatus("optional")


class _AddRFPortPowerFeedStatus_Type(Integer32):
    """Custom type addRFPortPowerFeedStatus based on Integer32"""
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


_AddRFPortPowerFeedStatus_Type.__name__ = "Integer32"
_AddRFPortPowerFeedStatus_Object = MibTableColumn
addRFPortPowerFeedStatus = _AddRFPortPowerFeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 7),
    _AddRFPortPowerFeedStatus_Type()
)
addRFPortPowerFeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortPowerFeedStatus.setStatus("optional")


class _AddRFPortInputRFLevel_Type(Integer32):
    """Custom type addRFPortInputRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AddRFPortInputRFLevel_Type.__name__ = "Integer32"
_AddRFPortInputRFLevel_Object = MibTableColumn
addRFPortInputRFLevel = _AddRFPortInputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 8),
    _AddRFPortInputRFLevel_Type()
)
addRFPortInputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addRFPortInputRFLevel.setStatus("optional")


class _AddRFPortattenuation1_Type(Integer32):
    """Custom type addRFPortattenuation1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AddRFPortattenuation1_Type.__name__ = "Integer32"
_AddRFPortattenuation1_Object = MibTableColumn
addRFPortattenuation1 = _AddRFPortattenuation1_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 9),
    _AddRFPortattenuation1_Type()
)
addRFPortattenuation1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addRFPortattenuation1.setStatus("optional")


class _AddRFPortattenuation2_Type(Integer32):
    """Custom type addRFPortattenuation2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AddRFPortattenuation2_Type.__name__ = "Integer32"
_AddRFPortattenuation2_Object = MibTableColumn
addRFPortattenuation2 = _AddRFPortattenuation2_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 10),
    _AddRFPortattenuation2_Type()
)
addRFPortattenuation2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addRFPortattenuation2.setStatus("optional")


class _AddRFPorteq_Type(Integer32):
    """Custom type addRFPorteq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AddRFPorteq_Type.__name__ = "Integer32"
_AddRFPorteq_Object = MibTableColumn
addRFPorteq = _AddRFPorteq_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 4, 1, 11),
    _AddRFPorteq_Type()
)
addRFPorteq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addRFPorteq.setStatus("optional")


class _AddLinePowerVoltage1_Type(Integer32):
    """Custom type addLinePowerVoltage1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AddLinePowerVoltage1_Type.__name__ = "Integer32"
_AddLinePowerVoltage1_Object = MibScalar
addLinePowerVoltage1 = _AddLinePowerVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 5),
    _AddLinePowerVoltage1_Type()
)
addLinePowerVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addLinePowerVoltage1.setStatus("optional")


class _AddLinePowerVoltage2_Type(Integer32):
    """Custom type addLinePowerVoltage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AddLinePowerVoltage2_Type.__name__ = "Integer32"
_AddLinePowerVoltage2_Object = MibScalar
addLinePowerVoltage2 = _AddLinePowerVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 6),
    _AddLinePowerVoltage2_Type()
)
addLinePowerVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addLinePowerVoltage2.setStatus("optional")


class _AddLinePowerCurrent_Type(Integer32):
    """Custom type addLinePowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AddLinePowerCurrent_Type.__name__ = "Integer32"
_AddLinePowerCurrent_Object = MibScalar
addLinePowerCurrent = _AddLinePowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 7),
    _AddLinePowerCurrent_Type()
)
addLinePowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addLinePowerCurrent.setStatus("optional")


class _AddNumberDCPowerSupply_Type(Integer32):
    """Custom type addNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AddNumberDCPowerSupply_Type.__name__ = "Integer32"
_AddNumberDCPowerSupply_Object = MibScalar
addNumberDCPowerSupply = _AddNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 8),
    _AddNumberDCPowerSupply_Type()
)
addNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addNumberDCPowerSupply.setStatus("mandatory")


class _AddDCPowerSupplyMode_Type(Integer32):
    """Custom type addDCPowerSupplyMode based on Integer32"""
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


_AddDCPowerSupplyMode_Type.__name__ = "Integer32"
_AddDCPowerSupplyMode_Object = MibScalar
addDCPowerSupplyMode = _AddDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 9),
    _AddDCPowerSupplyMode_Type()
)
addDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addDCPowerSupplyMode.setStatus("optional")
_AddDCPowerTable_Object = MibTable
addDCPowerTable = _AddDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 10)
)
if mibBuilder.loadTexts:
    addDCPowerTable.setStatus("mandatory")
_AddDCPowerEntry_Object = MibTableRow
addDCPowerEntry = _AddDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 10, 1)
)
addDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-AMPLIFIER-MIB", "addDCPowerIndex"),
)
if mibBuilder.loadTexts:
    addDCPowerEntry.setStatus("mandatory")
_AddDCPowerIndex_Type = Integer32
_AddDCPowerIndex_Object = MibTableColumn
addDCPowerIndex = _AddDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 10, 1, 1),
    _AddDCPowerIndex_Type()
)
addDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addDCPowerIndex.setStatus("mandatory")


class _AddDCPowerVoltage_Type(Integer32):
    """Custom type addDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AddDCPowerVoltage_Type.__name__ = "Integer32"
_AddDCPowerVoltage_Object = MibTableColumn
addDCPowerVoltage = _AddDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 10, 1, 2),
    _AddDCPowerVoltage_Type()
)
addDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addDCPowerVoltage.setStatus("mandatory")


class _AddDCPowerCurrent_Type(Integer32):
    """Custom type addDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AddDCPowerCurrent_Type.__name__ = "Integer32"
_AddDCPowerCurrent_Object = MibTableColumn
addDCPowerCurrent = _AddDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 10, 1, 3),
    _AddDCPowerCurrent_Type()
)
addDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addDCPowerCurrent.setStatus("optional")
_AddDCPowerName_Type = DisplayString
_AddDCPowerName_Object = MibTableColumn
addDCPowerName = _AddDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 10, 1, 4),
    _AddDCPowerName_Type()
)
addDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addDCPowerName.setStatus("mandatory")


class _AddChannelNumber_Type(Integer32):
    """Custom type addChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AddChannelNumber_Type.__name__ = "Integer32"
_AddChannelNumber_Object = MibScalar
addChannelNumber = _AddChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 11),
    _AddChannelNumber_Type()
)
addChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addChannelNumber.setStatus("mandatory")


class _AddFanControl_Type(Integer32):
    """Custom type addFanControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AddFanControl_Type.__name__ = "Integer32"
_AddFanControl_Object = MibScalar
addFanControl = _AddFanControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12, 12),
    _AddFanControl_Type()
)
addFanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addFanControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-AMPLIFIER-MIB",
    **{"addVendorOID": addVendorOID,
       "addNumberRFPort": addNumberRFPort,
       "addPortMasterAttenuationControl": addPortMasterAttenuationControl,
       "addRFPortTable": addRFPortTable,
       "addRFPortEntry": addRFPortEntry,
       "addRFPortIndex": addRFPortIndex,
       "addRFPortControlType": addRFPortControlType,
       "addRFPortControlLevel": addRFPortControlLevel,
       "addRFPortOutputRFLevel": addRFPortOutputRFLevel,
       "addRFPortName": addRFPortName,
       "addRFPortReverseAttenuationControl": addRFPortReverseAttenuationControl,
       "addRFPortPowerFeedStatus": addRFPortPowerFeedStatus,
       "addRFPortInputRFLevel": addRFPortInputRFLevel,
       "addRFPortattenuation1": addRFPortattenuation1,
       "addRFPortattenuation2": addRFPortattenuation2,
       "addRFPorteq": addRFPorteq,
       "addLinePowerVoltage1": addLinePowerVoltage1,
       "addLinePowerVoltage2": addLinePowerVoltage2,
       "addLinePowerCurrent": addLinePowerCurrent,
       "addNumberDCPowerSupply": addNumberDCPowerSupply,
       "addDCPowerSupplyMode": addDCPowerSupplyMode,
       "addDCPowerTable": addDCPowerTable,
       "addDCPowerEntry": addDCPowerEntry,
       "addDCPowerIndex": addDCPowerIndex,
       "addDCPowerVoltage": addDCPowerVoltage,
       "addDCPowerCurrent": addDCPowerCurrent,
       "addDCPowerName": addDCPowerName,
       "addChannelNumber": addChannelNumber,
       "addFanControl": addFanControl}
)
