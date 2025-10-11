# SNMP MIB module (NSCRTV-HFCEMS-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-LINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:33 2025
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

(lineIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "lineIdent")

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

_LineVendorOID_Type = ObjectIdentifier
_LineVendorOID_Object = MibScalar
lineVendorOID = _LineVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 1),
    _LineVendorOID_Type()
)
lineVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVendorOID.setStatus("optional")


class _LineRFLevel_Type(Integer32):
    """Custom type lineRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LineRFLevel_Type.__name__ = "Integer32"
_LineRFLevel_Object = MibScalar
lineRFLevel = _LineRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 2),
    _LineRFLevel_Type()
)
lineRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineRFLevel.setStatus("mandatory")


class _LineLinePowerVoltage_Type(Integer32):
    """Custom type lineLinePowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LineLinePowerVoltage_Type.__name__ = "Integer32"
_LineLinePowerVoltage_Object = MibScalar
lineLinePowerVoltage = _LineLinePowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 3),
    _LineLinePowerVoltage_Type()
)
lineLinePowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineLinePowerVoltage.setStatus("optional")


class _LineLinePowerCurrent_Type(Integer32):
    """Custom type lineLinePowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LineLinePowerCurrent_Type.__name__ = "Integer32"
_LineLinePowerCurrent_Object = MibScalar
lineLinePowerCurrent = _LineLinePowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 4),
    _LineLinePowerCurrent_Type()
)
lineLinePowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineLinePowerCurrent.setStatus("optional")


class _LineNumberDCPowerSupply_Type(Integer32):
    """Custom type lineNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LineNumberDCPowerSupply_Type.__name__ = "Integer32"
_LineNumberDCPowerSupply_Object = MibScalar
lineNumberDCPowerSupply = _LineNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 5),
    _LineNumberDCPowerSupply_Type()
)
lineNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineNumberDCPowerSupply.setStatus("mandatory")
_LineDCPowerTable_Object = MibTable
lineDCPowerTable = _LineDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 6)
)
if mibBuilder.loadTexts:
    lineDCPowerTable.setStatus("mandatory")
_LineDCPowerEntry_Object = MibTableRow
lineDCPowerEntry = _LineDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 6, 1)
)
lineDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-LINE-MIB", "lineDCPowerIndex"),
)
if mibBuilder.loadTexts:
    lineDCPowerEntry.setStatus("mandatory")
_LineDCPowerIndex_Type = Integer32
_LineDCPowerIndex_Object = MibTableColumn
lineDCPowerIndex = _LineDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 6, 1, 1),
    _LineDCPowerIndex_Type()
)
lineDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDCPowerIndex.setStatus("mandatory")


class _LineDCPowerVoltage_Type(Integer32):
    """Custom type lineDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LineDCPowerVoltage_Type.__name__ = "Integer32"
_LineDCPowerVoltage_Object = MibTableColumn
lineDCPowerVoltage = _LineDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 6, 1, 2),
    _LineDCPowerVoltage_Type()
)
lineDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDCPowerVoltage.setStatus("mandatory")


class _LineDCPowerCurrent_Type(Integer32):
    """Custom type lineDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LineDCPowerCurrent_Type.__name__ = "Integer32"
_LineDCPowerCurrent_Object = MibTableColumn
lineDCPowerCurrent = _LineDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 6, 1, 3),
    _LineDCPowerCurrent_Type()
)
lineDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDCPowerCurrent.setStatus("optional")
_LineDCPowerName_Type = DisplayString
_LineDCPowerName_Object = MibTableColumn
lineDCPowerName = _LineDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14, 6, 1, 4),
    _LineDCPowerName_Type()
)
lineDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-LINE-MIB",
    **{"lineVendorOID": lineVendorOID,
       "lineRFLevel": lineRFLevel,
       "lineLinePowerVoltage": lineLinePowerVoltage,
       "lineLinePowerCurrent": lineLinePowerCurrent,
       "lineNumberDCPowerSupply": lineNumberDCPowerSupply,
       "lineDCPowerTable": lineDCPowerTable,
       "lineDCPowerEntry": lineDCPowerEntry,
       "lineDCPowerIndex": lineDCPowerIndex,
       "lineDCPowerVoltage": lineDCPowerVoltage,
       "lineDCPowerCurrent": lineDCPowerCurrent,
       "lineDCPowerName": lineDCPowerName}
)
