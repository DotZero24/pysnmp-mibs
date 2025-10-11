# SNMP MIB module (NSCRTV-HFCEMS-UPSTREAMOPTICALRECEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-UPSTREAMOPTICALRECEIVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:39 2025
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

(uporIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "uporIdent")

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

_UporVendorOID_Type = ObjectIdentifier
_UporVendorOID_Object = MibScalar
uporVendorOID = _UporVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 1),
    _UporVendorOID_Type()
)
uporVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporVendorOID.setStatus("optional")


class _UporSlotNumber_Type(Integer32):
    """Custom type uporSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UporSlotNumber_Type.__name__ = "Integer32"
_UporSlotNumber_Object = MibScalar
uporSlotNumber = _UporSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 2),
    _UporSlotNumber_Type()
)
uporSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uporSlotNumber.setStatus("mandatory")
_UporDeviceTable_Object = MibTable
uporDeviceTable = _UporDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3)
)
if mibBuilder.loadTexts:
    uporDeviceTable.setStatus("mandatory")
_UporDeviceEntry_Object = MibTableRow
uporDeviceEntry = _UporDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3, 1)
)
uporDeviceEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-UPSTREAMOPTICALRECEIVER-MIB", "uporIndex"),
)
if mibBuilder.loadTexts:
    uporDeviceEntry.setStatus("mandatory")


class _UporIndex_Type(Integer32):
    """Custom type uporIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UporIndex_Type.__name__ = "Integer32"
_UporIndex_Object = MibTableColumn
uporIndex = _UporIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3, 1, 1),
    _UporIndex_Type()
)
uporIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporIndex.setStatus("mandatory")


class _UporOpicalInputPower_Type(Integer32):
    """Custom type uporOpicalInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_UporOpicalInputPower_Type.__name__ = "Integer32"
_UporOpicalInputPower_Object = MibTableColumn
uporOpicalInputPower = _UporOpicalInputPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3, 1, 2),
    _UporOpicalInputPower_Type()
)
uporOpicalInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporOpicalInputPower.setStatus("mandatory")


class _UporOutputRFAttenuationRange_Type(Integer32):
    """Custom type uporOutputRFAttenuationRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_UporOutputRFAttenuationRange_Type.__name__ = "Integer32"
_UporOutputRFAttenuationRange_Object = MibTableColumn
uporOutputRFAttenuationRange = _UporOutputRFAttenuationRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3, 1, 3),
    _UporOutputRFAttenuationRange_Type()
)
uporOutputRFAttenuationRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporOutputRFAttenuationRange.setStatus("optional")


class _UporOutputRFAttenuation_Type(Integer32):
    """Custom type uporOutputRFAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_UporOutputRFAttenuation_Type.__name__ = "Integer32"
_UporOutputRFAttenuation_Object = MibTableColumn
uporOutputRFAttenuation = _UporOutputRFAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3, 1, 4),
    _UporOutputRFAttenuation_Type()
)
uporOutputRFAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uporOutputRFAttenuation.setStatus("optional")


class _UporAGCControl_Type(Integer32):
    """Custom type uporAGCControl based on Integer32"""
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


_UporAGCControl_Type.__name__ = "Integer32"
_UporAGCControl_Object = MibTableColumn
uporAGCControl = _UporAGCControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 3, 1, 5),
    _UporAGCControl_Type()
)
uporAGCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uporAGCControl.setStatus("optional")


class _UporNumberDCPowerSupply_Type(Integer32):
    """Custom type uporNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_UporNumberDCPowerSupply_Type.__name__ = "Integer32"
_UporNumberDCPowerSupply_Object = MibScalar
uporNumberDCPowerSupply = _UporNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 4),
    _UporNumberDCPowerSupply_Type()
)
uporNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporNumberDCPowerSupply.setStatus("mandatory")


class _UporDCPowerSupplyMode_Type(Integer32):
    """Custom type uporDCPowerSupplyMode based on Integer32"""
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


_UporDCPowerSupplyMode_Type.__name__ = "Integer32"
_UporDCPowerSupplyMode_Object = MibScalar
uporDCPowerSupplyMode = _UporDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 5),
    _UporDCPowerSupplyMode_Type()
)
uporDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporDCPowerSupplyMode.setStatus("optional")
_UporDCPowerTable_Object = MibTable
uporDCPowerTable = _UporDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 6)
)
if mibBuilder.loadTexts:
    uporDCPowerTable.setStatus("mandatory")
_UporDCPowerEntry_Object = MibTableRow
uporDCPowerEntry = _UporDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 6, 1)
)
uporDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-UPSTREAMOPTICALRECEIVER-MIB", "uporDCPowerIndex"),
)
if mibBuilder.loadTexts:
    uporDCPowerEntry.setStatus("mandatory")
_UporDCPowerIndex_Type = Integer32
_UporDCPowerIndex_Object = MibTableColumn
uporDCPowerIndex = _UporDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 6, 1, 1),
    _UporDCPowerIndex_Type()
)
uporDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporDCPowerIndex.setStatus("mandatory")


class _UporDCPowerVoltage_Type(Integer32):
    """Custom type uporDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_UporDCPowerVoltage_Type.__name__ = "Integer32"
_UporDCPowerVoltage_Object = MibTableColumn
uporDCPowerVoltage = _UporDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 6, 1, 2),
    _UporDCPowerVoltage_Type()
)
uporDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporDCPowerVoltage.setStatus("mandatory")


class _UporDCPowerCurrent_Type(Integer32):
    """Custom type uporDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UporDCPowerCurrent_Type.__name__ = "Integer32"
_UporDCPowerCurrent_Object = MibTableColumn
uporDCPowerCurrent = _UporDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 6, 1, 3),
    _UporDCPowerCurrent_Type()
)
uporDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporDCPowerCurrent.setStatus("optional")
_UporDCPowerName_Type = DisplayString
_UporDCPowerName_Object = MibTableColumn
uporDCPowerName = _UporDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8, 6, 1, 4),
    _UporDCPowerName_Type()
)
uporDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uporDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-UPSTREAMOPTICALRECEIVER-MIB",
    **{"uporVendorOID": uporVendorOID,
       "uporSlotNumber": uporSlotNumber,
       "uporDeviceTable": uporDeviceTable,
       "uporDeviceEntry": uporDeviceEntry,
       "uporIndex": uporIndex,
       "uporOpicalInputPower": uporOpicalInputPower,
       "uporOutputRFAttenuationRange": uporOutputRFAttenuationRange,
       "uporOutputRFAttenuation": uporOutputRFAttenuation,
       "uporAGCControl": uporAGCControl,
       "uporNumberDCPowerSupply": uporNumberDCPowerSupply,
       "uporDCPowerSupplyMode": uporDCPowerSupplyMode,
       "uporDCPowerTable": uporDCPowerTable,
       "uporDCPowerEntry": uporDCPowerEntry,
       "uporDCPowerIndex": uporDCPowerIndex,
       "uporDCPowerVoltage": uporDCPowerVoltage,
       "uporDCPowerCurrent": uporDCPowerCurrent,
       "uporDCPowerName": uporDCPowerName}
)
