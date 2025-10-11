# SNMP MIB module (NSCRTV-HFCEMS-TVMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-TVMOD-MIB
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

(tvmodIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "tvmodIdent")

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

_TvmodVendorOID_Type = ObjectIdentifier
_TvmodVendorOID_Object = MibScalar
tvmodVendorOID = _TvmodVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 1),
    _TvmodVendorOID_Type()
)
tvmodVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodVendorOID.setStatus("optional")


class _TvmodOutputlevel_Type(Integer32):
    """Custom type tvmodOutputlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TvmodOutputlevel_Type.__name__ = "Integer32"
_TvmodOutputlevel_Object = MibScalar
tvmodOutputlevel = _TvmodOutputlevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 2),
    _TvmodOutputlevel_Type()
)
tvmodOutputlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodOutputlevel.setStatus("mandatory")


class _TvmodOutputlevelAtt_Type(Integer32):
    """Custom type tvmodOutputlevelAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TvmodOutputlevelAtt_Type.__name__ = "Integer32"
_TvmodOutputlevelAtt_Object = MibScalar
tvmodOutputlevelAtt = _TvmodOutputlevelAtt_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 3),
    _TvmodOutputlevelAtt_Type()
)
tvmodOutputlevelAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvmodOutputlevelAtt.setStatus("mandatory")


class _TvmodAVPower_ratio_Type(Integer32):
    """Custom type tvmodAVPower_ratio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TvmodAVPower_ratio_Type.__name__ = "Integer32"
_TvmodAVPower_ratio_Object = MibScalar
tvmodAVPower_ratio = _TvmodAVPower_ratio_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 4),
    _TvmodAVPower_ratio_Type()
)
tvmodAVPower_ratio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvmodAVPower_ratio.setStatus("mandatory")


class _Tvmodfreqdeviation_Type(Integer32):
    """Custom type tvmodfreqdeviation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tvmodfreqdeviation_Type.__name__ = "Integer32"
_Tvmodfreqdeviation_Object = MibScalar
tvmodfreqdeviation = _Tvmodfreqdeviation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 5),
    _Tvmodfreqdeviation_Type()
)
tvmodfreqdeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvmodfreqdeviation.setStatus("mandatory")
_TvmodOperatingFreq_Type = Integer32
_TvmodOperatingFreq_Object = MibScalar
tvmodOperatingFreq = _TvmodOperatingFreq_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 6),
    _TvmodOperatingFreq_Type()
)
tvmodOperatingFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodOperatingFreq.setStatus("mandatory")


class _TvmodModulatingDepth_Type(Integer32):
    """Custom type tvmodModulatingDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TvmodModulatingDepth_Type.__name__ = "Integer32"
_TvmodModulatingDepth_Object = MibScalar
tvmodModulatingDepth = _TvmodModulatingDepth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 7),
    _TvmodModulatingDepth_Type()
)
tvmodModulatingDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvmodModulatingDepth.setStatus("mandatory")


class _TvmodLockalarm_Type(Integer32):
    """Custom type tvmodLockalarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_TvmodLockalarm_Type.__name__ = "Integer32"
_TvmodLockalarm_Object = MibScalar
tvmodLockalarm = _TvmodLockalarm_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 8),
    _TvmodLockalarm_Type()
)
tvmodLockalarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodLockalarm.setStatus("mandatory")


class _TvmodNumberDCPowerSupply_Type(Integer32):
    """Custom type tvmodNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TvmodNumberDCPowerSupply_Type.__name__ = "Integer32"
_TvmodNumberDCPowerSupply_Object = MibScalar
tvmodNumberDCPowerSupply = _TvmodNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 9),
    _TvmodNumberDCPowerSupply_Type()
)
tvmodNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodNumberDCPowerSupply.setStatus("mandatory")


class _TvmodDCPowerSupplymode_Type(Integer32):
    """Custom type tvmodDCPowerSupplymode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadsharing", 1),
          ("switchedRedundant", 2))
    )


_TvmodDCPowerSupplymode_Type.__name__ = "Integer32"
_TvmodDCPowerSupplymode_Object = MibScalar
tvmodDCPowerSupplymode = _TvmodDCPowerSupplymode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 10),
    _TvmodDCPowerSupplymode_Type()
)
tvmodDCPowerSupplymode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodDCPowerSupplymode.setStatus("optional")
_TvmodDCPowerTable_Object = MibTable
tvmodDCPowerTable = _TvmodDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 11)
)
if mibBuilder.loadTexts:
    tvmodDCPowerTable.setStatus("mandatory")
_TvmodDCPowerEntry_Object = MibTableRow
tvmodDCPowerEntry = _TvmodDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 11, 1)
)
tvmodDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-TVMOD-MIB", "tvmodDCPowerIndex"),
)
if mibBuilder.loadTexts:
    tvmodDCPowerEntry.setStatus("mandatory")
_TvmodDCPowerIndex_Type = Integer32
_TvmodDCPowerIndex_Object = MibTableColumn
tvmodDCPowerIndex = _TvmodDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 11, 1, 1),
    _TvmodDCPowerIndex_Type()
)
tvmodDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodDCPowerIndex.setStatus("mandatory")


class _TvmodDCPowerVoltage_Type(Integer32):
    """Custom type tvmodDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_TvmodDCPowerVoltage_Type.__name__ = "Integer32"
_TvmodDCPowerVoltage_Object = MibTableColumn
tvmodDCPowerVoltage = _TvmodDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 11, 1, 2),
    _TvmodDCPowerVoltage_Type()
)
tvmodDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodDCPowerVoltage.setStatus("mandatory")


class _TvmodDCPowerCurrent_Type(Integer32):
    """Custom type tvmodDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TvmodDCPowerCurrent_Type.__name__ = "Integer32"
_TvmodDCPowerCurrent_Object = MibTableColumn
tvmodDCPowerCurrent = _TvmodDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 11, 1, 3),
    _TvmodDCPowerCurrent_Type()
)
tvmodDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodDCPowerCurrent.setStatus("optional")
_TvmodDCPowerName_Type = DisplayString
_TvmodDCPowerName_Object = MibTableColumn
tvmodDCPowerName = _TvmodDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4, 11, 1, 4),
    _TvmodDCPowerName_Type()
)
tvmodDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvmodDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-TVMOD-MIB",
    **{"tvmodVendorOID": tvmodVendorOID,
       "tvmodOutputlevel": tvmodOutputlevel,
       "tvmodOutputlevelAtt": tvmodOutputlevelAtt,
       "tvmodAVPower-ratio": tvmodAVPower_ratio,
       "tvmodfreqdeviation": tvmodfreqdeviation,
       "tvmodOperatingFreq": tvmodOperatingFreq,
       "tvmodModulatingDepth": tvmodModulatingDepth,
       "tvmodLockalarm": tvmodLockalarm,
       "tvmodNumberDCPowerSupply": tvmodNumberDCPowerSupply,
       "tvmodDCPowerSupplymode": tvmodDCPowerSupplymode,
       "tvmodDCPowerTable": tvmodDCPowerTable,
       "tvmodDCPowerEntry": tvmodDCPowerEntry,
       "tvmodDCPowerIndex": tvmodDCPowerIndex,
       "tvmodDCPowerVoltage": tvmodDCPowerVoltage,
       "tvmodDCPowerCurrent": tvmodDCPowerCurrent,
       "tvmodDCPowerName": tvmodDCPowerName}
)
