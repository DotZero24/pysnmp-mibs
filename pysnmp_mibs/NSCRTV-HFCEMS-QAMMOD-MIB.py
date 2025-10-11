# SNMP MIB module (NSCRTV-HFCEMS-QAMMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-QAMMOD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:41 2025
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

(qammodIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "qammodIdent")

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

_QamModVendorOID_Type = ObjectIdentifier
_QamModVendorOID_Object = MibScalar
qamModVendorOID = _QamModVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 1),
    _QamModVendorOID_Type()
)
qamModVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModVendorOID.setStatus("optional")


class _QamModmode_Type(Integer32):
    """Custom type qamModmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_QamModmode_Type.__name__ = "Integer32"
_QamModmode_Object = MibScalar
qamModmode = _QamModmode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 2),
    _QamModmode_Type()
)
qamModmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qamModmode.setStatus("mandatory")


class _QamModsymbolrate_Type(Integer32):
    """Custom type qamModsymbolrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QamModsymbolrate_Type.__name__ = "Integer32"
_QamModsymbolrate_Object = MibScalar
qamModsymbolrate = _QamModsymbolrate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 3),
    _QamModsymbolrate_Type()
)
qamModsymbolrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qamModsymbolrate.setStatus("mandatory")
_QamModRFfreq_Type = Integer32
_QamModRFfreq_Object = MibScalar
qamModRFfreq = _QamModRFfreq_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 4),
    _QamModRFfreq_Type()
)
qamModRFfreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qamModRFfreq.setStatus("mandatory")
_QamModRFLevel_Type = Integer32
_QamModRFLevel_Object = MibScalar
qamModRFLevel = _QamModRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 5),
    _QamModRFLevel_Type()
)
qamModRFLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qamModRFLevel.setStatus("optional")
_QamModRFLevelatt_Type = Integer32
_QamModRFLevelatt_Object = MibScalar
qamModRFLevelatt = _QamModRFLevelatt_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 6),
    _QamModRFLevelatt_Type()
)
qamModRFLevelatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qamModRFLevelatt.setStatus("optional")


class _QamModInputInterface_Type(Integer32):
    """Custom type qamModInputInterface based on Integer32"""
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
        *(("asi", 1),
          ("spi", 2),
          ("ds3", 3),
          ("other", 4))
    )


_QamModInputInterface_Type.__name__ = "Integer32"
_QamModInputInterface_Object = MibScalar
qamModInputInterface = _QamModInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 7),
    _QamModInputInterface_Type()
)
qamModInputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModInputInterface.setStatus("mandatory")


class _QamInputstatus_Type(Integer32):
    """Custom type qamInputstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync", 1),
          ("noSync", 2))
    )


_QamInputstatus_Type.__name__ = "Integer32"
_QamInputstatus_Object = MibScalar
qamInputstatus = _QamInputstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 8),
    _QamInputstatus_Type()
)
qamInputstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamInputstatus.setStatus("mandatory")


class _QamModTSpacketlen_Type(Integer32):
    """Custom type qamModTSpacketlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes188", 1),
          ("bytes204", 2))
    )


_QamModTSpacketlen_Type.__name__ = "Integer32"
_QamModTSpacketlen_Object = MibScalar
qamModTSpacketlen = _QamModTSpacketlen_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 9),
    _QamModTSpacketlen_Type()
)
qamModTSpacketlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qamModTSpacketlen.setStatus("mandatory")
_QamPidFilterTable_Object = MibTable
qamPidFilterTable = _QamPidFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 10)
)
if mibBuilder.loadTexts:
    qamPidFilterTable.setStatus("mandatory")
_QamPidFilterEntry_Object = MibTableRow
qamPidFilterEntry = _QamPidFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 10, 1)
)
qamPidFilterEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-QAMMOD-MIB", "qamPidFilterIndex"),
)
if mibBuilder.loadTexts:
    qamPidFilterEntry.setStatus("mandatory")
_QamPidFilterIndex_Type = Integer32
_QamPidFilterIndex_Object = MibTableColumn
qamPidFilterIndex = _QamPidFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 10, 1, 1),
    _QamPidFilterIndex_Type()
)
qamPidFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamPidFilterIndex.setStatus("mandatory")


class _QamInPid_Type(Integer32):
    """Custom type qamInPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QamInPid_Type.__name__ = "Integer32"
_QamInPid_Object = MibTableColumn
qamInPid = _QamInPid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 10, 1, 2),
    _QamInPid_Type()
)
qamInPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamInPid.setStatus("mandatory")


class _QamModNumberDCPowerSupply_Type(Integer32):
    """Custom type qamModNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QamModNumberDCPowerSupply_Type.__name__ = "Integer32"
_QamModNumberDCPowerSupply_Object = MibScalar
qamModNumberDCPowerSupply = _QamModNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 11),
    _QamModNumberDCPowerSupply_Type()
)
qamModNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModNumberDCPowerSupply.setStatus("mandatory")


class _QamModDCPowerSupplyMode_Type(Integer32):
    """Custom type qamModDCPowerSupplyMode based on Integer32"""
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


_QamModDCPowerSupplyMode_Type.__name__ = "Integer32"
_QamModDCPowerSupplyMode_Object = MibScalar
qamModDCPowerSupplyMode = _QamModDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 12),
    _QamModDCPowerSupplyMode_Type()
)
qamModDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModDCPowerSupplyMode.setStatus("optional")
_QamModDCPowerTable_Object = MibTable
qamModDCPowerTable = _QamModDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 13)
)
if mibBuilder.loadTexts:
    qamModDCPowerTable.setStatus("mandatory")
_QamModDCPowerEntry_Object = MibTableRow
qamModDCPowerEntry = _QamModDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 13, 1)
)
qamModDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-QAMMOD-MIB", "qamModDCPowerIndex"),
)
if mibBuilder.loadTexts:
    qamModDCPowerEntry.setStatus("mandatory")
_QamModDCPowerIndex_Type = Integer32
_QamModDCPowerIndex_Object = MibTableColumn
qamModDCPowerIndex = _QamModDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 13, 1, 1),
    _QamModDCPowerIndex_Type()
)
qamModDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModDCPowerIndex.setStatus("mandatory")


class _QamModDCPowerVoltage_Type(Integer32):
    """Custom type qamModDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_QamModDCPowerVoltage_Type.__name__ = "Integer32"
_QamModDCPowerVoltage_Object = MibTableColumn
qamModDCPowerVoltage = _QamModDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 13, 1, 2),
    _QamModDCPowerVoltage_Type()
)
qamModDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModDCPowerVoltage.setStatus("mandatory")


class _QamModDCPowerCurrent_Type(Integer32):
    """Custom type qamModDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QamModDCPowerCurrent_Type.__name__ = "Integer32"
_QamModDCPowerCurrent_Object = MibTableColumn
qamModDCPowerCurrent = _QamModDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 13, 1, 3),
    _QamModDCPowerCurrent_Type()
)
qamModDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModDCPowerCurrent.setStatus("optional")
_QamModDCPowerName_Type = DisplayString
_QamModDCPowerName_Object = MibTableColumn
qamModDCPowerName = _QamModDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5, 13, 1, 4),
    _QamModDCPowerName_Type()
)
qamModDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qamModDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-QAMMOD-MIB",
    **{"qamModVendorOID": qamModVendorOID,
       "qamModmode": qamModmode,
       "qamModsymbolrate": qamModsymbolrate,
       "qamModRFfreq": qamModRFfreq,
       "qamModRFLevel": qamModRFLevel,
       "qamModRFLevelatt": qamModRFLevelatt,
       "qamModInputInterface": qamModInputInterface,
       "qamInputstatus": qamInputstatus,
       "qamModTSpacketlen": qamModTSpacketlen,
       "qamPidFilterTable": qamPidFilterTable,
       "qamPidFilterEntry": qamPidFilterEntry,
       "qamPidFilterIndex": qamPidFilterIndex,
       "qamInPid": qamInPid,
       "qamModNumberDCPowerSupply": qamModNumberDCPowerSupply,
       "qamModDCPowerSupplyMode": qamModDCPowerSupplyMode,
       "qamModDCPowerTable": qamModDCPowerTable,
       "qamModDCPowerEntry": qamModDCPowerEntry,
       "qamModDCPowerIndex": qamModDCPowerIndex,
       "qamModDCPowerVoltage": qamModDCPowerVoltage,
       "qamModDCPowerCurrent": qamModDCPowerCurrent,
       "qamModDCPowerName": qamModDCPowerName}
)
