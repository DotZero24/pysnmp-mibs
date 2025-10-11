# SNMP MIB module (ZTE-DSL-LINE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-LINE-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:18 2025
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

(adslLineAlarmConfProfileEntry,
 adslLineConfProfileEntry,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLineAlarmConfProfileEntry",
    "adslLineConfProfileEntry",
    "adslLineConfProfileName")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

zxAdslExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxAdslExtMibObjects_ObjectIdentity = ObjectIdentity
zxAdslExtMibObjects = _ZxAdslExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1)
)
_ZxAdslLineTable_Object = MibTable
zxAdslLineTable = _ZxAdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1)
)
if mibBuilder.loadTexts:
    zxAdslLineTable.setStatus("current")
_ZxAdslLineEntry_Object = MibTableRow
zxAdslLineEntry = _ZxAdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1)
)
zxAdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslLineEntry.setStatus("current")


class _ZxAdslLinePMConfPMSF_Type(Integer32):
    """Custom type zxAdslLinePMConfPMSF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l0_FullOn", 1),
          ("l2_LowPower", 3),
          ("l3_Idle", 4))
    )


_ZxAdslLinePMConfPMSF_Type.__name__ = "Integer32"
_ZxAdslLinePMConfPMSF_Object = MibTableColumn
zxAdslLinePMConfPMSF = _ZxAdslLinePMConfPMSF_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 1),
    _ZxAdslLinePMConfPMSF_Type()
)
zxAdslLinePMConfPMSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslLinePMConfPMSF.setStatus("current")


class _ZxAdslLinePMState_Type(Integer32):
    """Custom type zxAdslLinePMState based on Integer32"""
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
        *(("l0_FullOn", 1),
          ("l1_LowPower", 2),
          ("l2_LowPower", 3),
          ("l3_Idle", 4))
    )


_ZxAdslLinePMState_Type.__name__ = "Integer32"
_ZxAdslLinePMState_Object = MibTableColumn
zxAdslLinePMState = _ZxAdslLinePMState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 2),
    _ZxAdslLinePMState_Type()
)
zxAdslLinePMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLinePMState.setStatus("current")


class _ZxAdslLineDMTTrellis_Type(Integer32):
    """Custom type zxAdslLineDMTTrellis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("on", 1),
          ("off", 2))
    )


_ZxAdslLineDMTTrellis_Type.__name__ = "Integer32"
_ZxAdslLineDMTTrellis_Object = MibTableColumn
zxAdslLineDMTTrellis = _ZxAdslLineDMTTrellis_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 3),
    _ZxAdslLineDMTTrellis_Type()
)
zxAdslLineDMTTrellis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLineDMTTrellis.setStatus("deprecated")
_ZxAdslLineTxAtmCells_Type = Counter32
_ZxAdslLineTxAtmCells_Object = MibTableColumn
zxAdslLineTxAtmCells = _ZxAdslLineTxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 4),
    _ZxAdslLineTxAtmCells_Type()
)
zxAdslLineTxAtmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLineTxAtmCells.setStatus("current")
_ZxAdslLineRxAtmCells_Type = Counter32
_ZxAdslLineRxAtmCells_Object = MibTableColumn
zxAdslLineRxAtmCells = _ZxAdslLineRxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 5),
    _ZxAdslLineRxAtmCells_Type()
)
zxAdslLineRxAtmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLineRxAtmCells.setStatus("current")
_ZxAdslLineIdleCells_Type = Counter32
_ZxAdslLineIdleCells_Object = MibTableColumn
zxAdslLineIdleCells = _ZxAdslLineIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 6),
    _ZxAdslLineIdleCells_Type()
)
zxAdslLineIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLineIdleCells.setStatus("current")
_ZxAdslLineTxDataRate_Type = Gauge32
_ZxAdslLineTxDataRate_Object = MibTableColumn
zxAdslLineTxDataRate = _ZxAdslLineTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 7),
    _ZxAdslLineTxDataRate_Type()
)
zxAdslLineTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLineTxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslLineTxDataRate.setUnits("kbps")
_ZxAdslLineRxDataRate_Type = Gauge32
_ZxAdslLineRxDataRate_Object = MibTableColumn
zxAdslLineRxDataRate = _ZxAdslLineRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 1, 1, 8),
    _ZxAdslLineRxDataRate_Type()
)
zxAdslLineRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslLineRxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslLineRxDataRate.setUnits("kbps")
_ZxAdslLineConfProfileExtTable_Object = MibTable
zxAdslLineConfProfileExtTable = _ZxAdslLineConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2)
)
if mibBuilder.loadTexts:
    zxAdslLineConfProfileExtTable.setStatus("current")
_ZxAdslLineConfProfileExtEntry_Object = MibTableRow
zxAdslLineConfProfileExtEntry = _ZxAdslLineConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAdslLineConfProfileExtEntry.setStatus("current")


class _ZxAdslLineDMTConfTrellis_Type(Integer32):
    """Custom type zxAdslLineDMTConfTrellis based on Integer32"""
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


_ZxAdslLineDMTConfTrellis_Type.__name__ = "Integer32"
_ZxAdslLineDMTConfTrellis_Object = MibTableColumn
zxAdslLineDMTConfTrellis = _ZxAdslLineDMTConfTrellis_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 1),
    _ZxAdslLineDMTConfTrellis_Type()
)
zxAdslLineDMTConfTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslLineDMTConfTrellis.setStatus("deprecated")


class _ZxAdslAtucConfMaxBitsPerBin_Type(Integer32):
    """Custom type zxAdslAtucConfMaxBitsPerBin based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZxAdslAtucConfMaxBitsPerBin_Type.__name__ = "Integer32"
_ZxAdslAtucConfMaxBitsPerBin_Object = MibTableColumn
zxAdslAtucConfMaxBitsPerBin = _ZxAdslAtucConfMaxBitsPerBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 2),
    _ZxAdslAtucConfMaxBitsPerBin_Type()
)
zxAdslAtucConfMaxBitsPerBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfMaxBitsPerBin.setStatus("current")
_ZxAdslAtucConfTxStartBin_Type = Integer32
_ZxAdslAtucConfTxStartBin_Object = MibTableColumn
zxAdslAtucConfTxStartBin = _ZxAdslAtucConfTxStartBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 3),
    _ZxAdslAtucConfTxStartBin_Type()
)
zxAdslAtucConfTxStartBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfTxStartBin.setStatus("current")


class _ZxAdslAtucConfTxEndBin_Type(Integer32):
    """Custom type zxAdslAtucConfTxEndBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ZxAdslAtucConfTxEndBin_Type.__name__ = "Integer32"
_ZxAdslAtucConfTxEndBin_Object = MibTableColumn
zxAdslAtucConfTxEndBin = _ZxAdslAtucConfTxEndBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 4),
    _ZxAdslAtucConfTxEndBin_Type()
)
zxAdslAtucConfTxEndBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfTxEndBin.setStatus("current")
_ZxAdslAtucConfRxStartBin_Type = Integer32
_ZxAdslAtucConfRxStartBin_Object = MibTableColumn
zxAdslAtucConfRxStartBin = _ZxAdslAtucConfRxStartBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 5),
    _ZxAdslAtucConfRxStartBin_Type()
)
zxAdslAtucConfRxStartBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfRxStartBin.setStatus("current")


class _ZxAdslAtucConfRxEndBin_Type(Integer32):
    """Custom type zxAdslAtucConfRxEndBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ZxAdslAtucConfRxEndBin_Type.__name__ = "Integer32"
_ZxAdslAtucConfRxEndBin_Object = MibTableColumn
zxAdslAtucConfRxEndBin = _ZxAdslAtucConfRxEndBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 6),
    _ZxAdslAtucConfRxEndBin_Type()
)
zxAdslAtucConfRxEndBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfRxEndBin.setStatus("current")


class _ZxAdslAtucConfUseCustomBins_Type(Integer32):
    """Custom type zxAdslAtucConfUseCustomBins based on Integer32"""
    defaultValue = 2

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


_ZxAdslAtucConfUseCustomBins_Type.__name__ = "Integer32"
_ZxAdslAtucConfUseCustomBins_Object = MibTableColumn
zxAdslAtucConfUseCustomBins = _ZxAdslAtucConfUseCustomBins_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 7),
    _ZxAdslAtucConfUseCustomBins_Type()
)
zxAdslAtucConfUseCustomBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfUseCustomBins.setStatus("current")


class _ZxAdslAtucConfDnBitSwap_Type(Integer32):
    """Custom type zxAdslAtucConfDnBitSwap based on Integer32"""
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


_ZxAdslAtucConfDnBitSwap_Type.__name__ = "Integer32"
_ZxAdslAtucConfDnBitSwap_Object = MibTableColumn
zxAdslAtucConfDnBitSwap = _ZxAdslAtucConfDnBitSwap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 8),
    _ZxAdslAtucConfDnBitSwap_Type()
)
zxAdslAtucConfDnBitSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfDnBitSwap.setStatus("current")


class _ZxAdslAtucConfUpBitSwap_Type(Integer32):
    """Custom type zxAdslAtucConfUpBitSwap based on Integer32"""
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


_ZxAdslAtucConfUpBitSwap_Type.__name__ = "Integer32"
_ZxAdslAtucConfUpBitSwap_Object = MibTableColumn
zxAdslAtucConfUpBitSwap = _ZxAdslAtucConfUpBitSwap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 9),
    _ZxAdslAtucConfUpBitSwap_Type()
)
zxAdslAtucConfUpBitSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfUpBitSwap.setStatus("current")


class _ZxAdslAtucConfREADSL2Enable_Type(Integer32):
    """Custom type zxAdslAtucConfREADSL2Enable based on Integer32"""
    defaultValue = 2

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


_ZxAdslAtucConfREADSL2Enable_Type.__name__ = "Integer32"
_ZxAdslAtucConfREADSL2Enable_Object = MibTableColumn
zxAdslAtucConfREADSL2Enable = _ZxAdslAtucConfREADSL2Enable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 10),
    _ZxAdslAtucConfREADSL2Enable_Type()
)
zxAdslAtucConfREADSL2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfREADSL2Enable.setStatus("deprecated")
_ZxAdslAtucConfPsdMaskType_Type = Integer32
_ZxAdslAtucConfPsdMaskType_Object = MibTableColumn
zxAdslAtucConfPsdMaskType = _ZxAdslAtucConfPsdMaskType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 11),
    _ZxAdslAtucConfPsdMaskType_Type()
)
zxAdslAtucConfPsdMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfPsdMaskType.setStatus("current")


class _ZxAdslAtucConfPMMode_Type(Bits):
    """Custom type zxAdslAtucConfPMMode based on Bits"""
    namedValues = NamedValues(
        *(("idle", 0),
          ("lowPower", 1))
    )

_ZxAdslAtucConfPMMode_Type.__name__ = "Bits"
_ZxAdslAtucConfPMMode_Object = MibTableColumn
zxAdslAtucConfPMMode = _ZxAdslAtucConfPMMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 12),
    _ZxAdslAtucConfPMMode_Type()
)
zxAdslAtucConfPMMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfPMMode.setStatus("current")


class _ZxAdslAtucConfPML0Time_Type(Integer32):
    """Custom type zxAdslAtucConfPML0Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAdslAtucConfPML0Time_Type.__name__ = "Integer32"
_ZxAdslAtucConfPML0Time_Object = MibTableColumn
zxAdslAtucConfPML0Time = _ZxAdslAtucConfPML0Time_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 13),
    _ZxAdslAtucConfPML0Time_Type()
)
zxAdslAtucConfPML0Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML0Time.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML0Time.setUnits("seconds")


class _ZxAdslAtucConfPML2Time_Type(Integer32):
    """Custom type zxAdslAtucConfPML2Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAdslAtucConfPML2Time_Type.__name__ = "Integer32"
_ZxAdslAtucConfPML2Time_Object = MibTableColumn
zxAdslAtucConfPML2Time = _ZxAdslAtucConfPML2Time_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 14),
    _ZxAdslAtucConfPML2Time_Type()
)
zxAdslAtucConfPML2Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML2Time.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML2Time.setUnits("seconds")


class _ZxAdslAtucConfPML2ATPR_Type(Integer32):
    """Custom type zxAdslAtucConfPML2ATPR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ZxAdslAtucConfPML2ATPR_Type.__name__ = "Integer32"
_ZxAdslAtucConfPML2ATPR_Object = MibTableColumn
zxAdslAtucConfPML2ATPR = _ZxAdslAtucConfPML2ATPR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 15),
    _ZxAdslAtucConfPML2ATPR_Type()
)
zxAdslAtucConfPML2ATPR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML2ATPR.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML2ATPR.setUnits("dB")


class _ZxAdslAtucConfPML2Rate_Type(Integer32):
    """Custom type zxAdslAtucConfPML2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1024),
    )


_ZxAdslAtucConfPML2Rate_Type.__name__ = "Integer32"
_ZxAdslAtucConfPML2Rate_Object = MibTableColumn
zxAdslAtucConfPML2Rate = _ZxAdslAtucConfPML2Rate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 16),
    _ZxAdslAtucConfPML2Rate_Type()
)
zxAdslAtucConfPML2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML2Rate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucConfPML2Rate.setUnits("kbps")


class _ZxAdsl2ConfMinProtectionDs_Type(Integer32):
    """Custom type zxAdsl2ConfMinProtectionDs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noProtection", 1),
          ("halfSymbol", 2),
          ("singleSymbol", 3),
          ("twoSymbols", 4),
          ("fourSymbols", 5),
          ("eightSymbols", 6),
          ("sixteenSymbols", 7))
    )


_ZxAdsl2ConfMinProtectionDs_Type.__name__ = "Integer32"
_ZxAdsl2ConfMinProtectionDs_Object = MibTableColumn
zxAdsl2ConfMinProtectionDs = _ZxAdsl2ConfMinProtectionDs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 20),
    _ZxAdsl2ConfMinProtectionDs_Type()
)
zxAdsl2ConfMinProtectionDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdsl2ConfMinProtectionDs.setStatus("current")
if mibBuilder.loadTexts:
    zxAdsl2ConfMinProtectionDs.setUnits("symbols")


class _ZxAdsl2ConfMinProtectionUs_Type(Integer32):
    """Custom type zxAdsl2ConfMinProtectionUs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noProtection", 1),
          ("halfSymbol", 2),
          ("singleSymbol", 3),
          ("twoSymbols", 4),
          ("fourSymbols", 5),
          ("eightSymbols", 6),
          ("sixteenSymbols", 7))
    )


_ZxAdsl2ConfMinProtectionUs_Type.__name__ = "Integer32"
_ZxAdsl2ConfMinProtectionUs_Object = MibTableColumn
zxAdsl2ConfMinProtectionUs = _ZxAdsl2ConfMinProtectionUs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 2, 1, 21),
    _ZxAdsl2ConfMinProtectionUs_Type()
)
zxAdsl2ConfMinProtectionUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdsl2ConfMinProtectionUs.setStatus("current")
if mibBuilder.loadTexts:
    zxAdsl2ConfMinProtectionUs.setUnits("symbols")
_ZxAdslAtucPhysTable_Object = MibTable
zxAdslAtucPhysTable = _ZxAdslAtucPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 3)
)
if mibBuilder.loadTexts:
    zxAdslAtucPhysTable.setStatus("current")
_ZxAdslAtucPhysEntry_Object = MibTableRow
zxAdslAtucPhysEntry = _ZxAdslAtucPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 3, 1)
)
zxAdslAtucPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslAtucPhysEntry.setStatus("current")


class _ZxAdslAtucPrevSnrMgn_Type(Integer32):
    """Custom type zxAdslAtucPrevSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_ZxAdslAtucPrevSnrMgn_Type.__name__ = "Integer32"
_ZxAdslAtucPrevSnrMgn_Object = MibTableColumn
zxAdslAtucPrevSnrMgn = _ZxAdslAtucPrevSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 3, 1, 1),
    _ZxAdslAtucPrevSnrMgn_Type()
)
zxAdslAtucPrevSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucPrevSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucPrevSnrMgn.setUnits("tenth dB")


class _ZxAdslAtucPrevAtn_Type(Gauge32):
    """Custom type zxAdslAtucPrevAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_ZxAdslAtucPrevAtn_Type.__name__ = "Gauge32"
_ZxAdslAtucPrevAtn_Object = MibTableColumn
zxAdslAtucPrevAtn = _ZxAdslAtucPrevAtn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 3, 1, 2),
    _ZxAdslAtucPrevAtn_Type()
)
zxAdslAtucPrevAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucPrevAtn.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucPrevAtn.setUnits("tenth dB")
_ZxAdslAtucPrevAttainableRate_Type = Gauge32
_ZxAdslAtucPrevAttainableRate_Object = MibTableColumn
zxAdslAtucPrevAttainableRate = _ZxAdslAtucPrevAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 3, 1, 3),
    _ZxAdslAtucPrevAttainableRate_Type()
)
zxAdslAtucPrevAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucPrevAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucPrevAttainableRate.setUnits("kbps")


class _ZxAdslAtucChipVersion_Type(SnmpAdminString):
    """Custom type zxAdslAtucChipVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAdslAtucChipVersion_Type.__name__ = "SnmpAdminString"
_ZxAdslAtucChipVersion_Object = MibTableColumn
zxAdslAtucChipVersion = _ZxAdslAtucChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 3, 1, 4),
    _ZxAdslAtucChipVersion_Type()
)
zxAdslAtucChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChipVersion.setStatus("deprecated")
_ZxAdslAturPhysTable_Object = MibTable
zxAdslAturPhysTable = _ZxAdslAturPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 4)
)
if mibBuilder.loadTexts:
    zxAdslAturPhysTable.setStatus("current")
_ZxAdslAturPhysEntry_Object = MibTableRow
zxAdslAturPhysEntry = _ZxAdslAturPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 4, 1)
)
zxAdslAturPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslAturPhysEntry.setStatus("current")


class _ZxAdslAturPrevSnrMgn_Type(Integer32):
    """Custom type zxAdslAturPrevSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_ZxAdslAturPrevSnrMgn_Type.__name__ = "Integer32"
_ZxAdslAturPrevSnrMgn_Object = MibTableColumn
zxAdslAturPrevSnrMgn = _ZxAdslAturPrevSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 4, 1, 1),
    _ZxAdslAturPrevSnrMgn_Type()
)
zxAdslAturPrevSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturPrevSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAturPrevSnrMgn.setUnits("tenth dB")


class _ZxAdslAturPrevAtn_Type(Gauge32):
    """Custom type zxAdslAturPrevAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_ZxAdslAturPrevAtn_Type.__name__ = "Gauge32"
_ZxAdslAturPrevAtn_Object = MibTableColumn
zxAdslAturPrevAtn = _ZxAdslAturPrevAtn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 4, 1, 2),
    _ZxAdslAturPrevAtn_Type()
)
zxAdslAturPrevAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturPrevAtn.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAturPrevAtn.setUnits("tenth dB")
_ZxAdslAturPrevAttainableRate_Type = Gauge32
_ZxAdslAturPrevAttainableRate_Object = MibTableColumn
zxAdslAturPrevAttainableRate = _ZxAdslAturPrevAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 4, 1, 3),
    _ZxAdslAturPrevAttainableRate_Type()
)
zxAdslAturPrevAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturPrevAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAturPrevAttainableRate.setUnits("kbps")
_ZxAdslAtucChanTable_Object = MibTable
zxAdslAtucChanTable = _ZxAdslAtucChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 5)
)
if mibBuilder.loadTexts:
    zxAdslAtucChanTable.setStatus("current")
_ZxAdslAtucChanEntry_Object = MibTableRow
zxAdslAtucChanEntry = _ZxAdslAtucChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 5, 1)
)
zxAdslAtucChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslAtucChanEntry.setStatus("current")
_ZxAdslAtucChanRsSymbols_Type = Integer32
_ZxAdslAtucChanRsSymbols_Object = MibTableColumn
zxAdslAtucChanRsSymbols = _ZxAdslAtucChanRsSymbols_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 5, 1, 1),
    _ZxAdslAtucChanRsSymbols_Type()
)
zxAdslAtucChanRsSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanRsSymbols.setStatus("current")
_ZxAdslAtucChanRsDepth_Type = Integer32
_ZxAdslAtucChanRsDepth_Object = MibTableColumn
zxAdslAtucChanRsDepth = _ZxAdslAtucChanRsDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 5, 1, 2),
    _ZxAdslAtucChanRsDepth_Type()
)
zxAdslAtucChanRsDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanRsDepth.setStatus("current")
_ZxAdslAtucChanRsRedundancy_Type = Integer32
_ZxAdslAtucChanRsRedundancy_Object = MibTableColumn
zxAdslAtucChanRsRedundancy = _ZxAdslAtucChanRsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 5, 1, 3),
    _ZxAdslAtucChanRsRedundancy_Type()
)
zxAdslAtucChanRsRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanRsRedundancy.setStatus("current")
_ZxAdslAturChanTable_Object = MibTable
zxAdslAturChanTable = _ZxAdslAturChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 6)
)
if mibBuilder.loadTexts:
    zxAdslAturChanTable.setStatus("current")
_ZxAdslAturChanEntry_Object = MibTableRow
zxAdslAturChanEntry = _ZxAdslAturChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 6, 1)
)
zxAdslAturChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslAturChanEntry.setStatus("current")
_ZxAdslAturChanRsSymbols_Type = Integer32
_ZxAdslAturChanRsSymbols_Object = MibTableColumn
zxAdslAturChanRsSymbols = _ZxAdslAturChanRsSymbols_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 6, 1, 1),
    _ZxAdslAturChanRsSymbols_Type()
)
zxAdslAturChanRsSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanRsSymbols.setStatus("current")
_ZxAdslAturChanRsDepth_Type = Integer32
_ZxAdslAturChanRsDepth_Object = MibTableColumn
zxAdslAturChanRsDepth = _ZxAdslAturChanRsDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 6, 1, 2),
    _ZxAdslAturChanRsDepth_Type()
)
zxAdslAturChanRsDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanRsDepth.setStatus("current")
_ZxAdslAturChanRsRedundancy_Type = Integer32
_ZxAdslAturChanRsRedundancy_Object = MibTableColumn
zxAdslAturChanRsRedundancy = _ZxAdslAturChanRsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 6, 1, 3),
    _ZxAdslAturChanRsRedundancy_Type()
)
zxAdslAturChanRsRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanRsRedundancy.setStatus("current")
_ZxAdslAtucChanPerfTable_Object = MibTable
zxAdslAtucChanPerfTable = _ZxAdslAtucChanPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7)
)
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfTable.setStatus("current")
_ZxAdslAtucChanPerfEntry_Object = MibTableRow
zxAdslAtucChanPerfEntry = _ZxAdslAtucChanPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1)
)
zxAdslAtucChanPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfEntry.setStatus("current")
_ZxAdslAtucChanPerfNcd_Type = Counter32
_ZxAdslAtucChanPerfNcd_Object = MibTableColumn
zxAdslAtucChanPerfNcd = _ZxAdslAtucChanPerfNcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 1),
    _ZxAdslAtucChanPerfNcd_Type()
)
zxAdslAtucChanPerfNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfNcd.setStatus("current")
_ZxAdslAtucChanPerfOcd_Type = Counter32
_ZxAdslAtucChanPerfOcd_Object = MibTableColumn
zxAdslAtucChanPerfOcd = _ZxAdslAtucChanPerfOcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 2),
    _ZxAdslAtucChanPerfOcd_Type()
)
zxAdslAtucChanPerfOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfOcd.setStatus("current")
_ZxAdslAtucChanPerfHec_Type = Counter32
_ZxAdslAtucChanPerfHec_Object = MibTableColumn
zxAdslAtucChanPerfHec = _ZxAdslAtucChanPerfHec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 3),
    _ZxAdslAtucChanPerfHec_Type()
)
zxAdslAtucChanPerfHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfHec.setStatus("current")
_ZxAdslAtucChanPerfCurr15Ncd_Type = Counter32
_ZxAdslAtucChanPerfCurr15Ncd_Object = MibTableColumn
zxAdslAtucChanPerfCurr15Ncd = _ZxAdslAtucChanPerfCurr15Ncd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 4),
    _ZxAdslAtucChanPerfCurr15Ncd_Type()
)
zxAdslAtucChanPerfCurr15Ncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfCurr15Ncd.setStatus("current")
_ZxAdslAtucChanPerfCurr15Ocd_Type = Counter32
_ZxAdslAtucChanPerfCurr15Ocd_Object = MibTableColumn
zxAdslAtucChanPerfCurr15Ocd = _ZxAdslAtucChanPerfCurr15Ocd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 5),
    _ZxAdslAtucChanPerfCurr15Ocd_Type()
)
zxAdslAtucChanPerfCurr15Ocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfCurr15Ocd.setStatus("current")
_ZxAdslAtucChanPerfCurr15Hec_Type = Counter32
_ZxAdslAtucChanPerfCurr15Hec_Object = MibTableColumn
zxAdslAtucChanPerfCurr15Hec = _ZxAdslAtucChanPerfCurr15Hec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 6),
    _ZxAdslAtucChanPerfCurr15Hec_Type()
)
zxAdslAtucChanPerfCurr15Hec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfCurr15Hec.setStatus("current")
_ZxAdslAtucChanPerfCurr1DayNcd_Type = Counter32
_ZxAdslAtucChanPerfCurr1DayNcd_Object = MibTableColumn
zxAdslAtucChanPerfCurr1DayNcd = _ZxAdslAtucChanPerfCurr1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 7),
    _ZxAdslAtucChanPerfCurr1DayNcd_Type()
)
zxAdslAtucChanPerfCurr1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfCurr1DayNcd.setStatus("current")
_ZxAdslAtucChanPerfCurr1DayOcd_Type = Counter32
_ZxAdslAtucChanPerfCurr1DayOcd_Object = MibTableColumn
zxAdslAtucChanPerfCurr1DayOcd = _ZxAdslAtucChanPerfCurr1DayOcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 8),
    _ZxAdslAtucChanPerfCurr1DayOcd_Type()
)
zxAdslAtucChanPerfCurr1DayOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfCurr1DayOcd.setStatus("current")
_ZxAdslAtucChanPerfCurr1DayHec_Type = Counter32
_ZxAdslAtucChanPerfCurr1DayHec_Object = MibTableColumn
zxAdslAtucChanPerfCurr1DayHec = _ZxAdslAtucChanPerfCurr1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 9),
    _ZxAdslAtucChanPerfCurr1DayHec_Type()
)
zxAdslAtucChanPerfCurr1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfCurr1DayHec.setStatus("current")
_ZxAdslAtucChanPerfPrev1DayNcd_Type = Counter32
_ZxAdslAtucChanPerfPrev1DayNcd_Object = MibTableColumn
zxAdslAtucChanPerfPrev1DayNcd = _ZxAdslAtucChanPerfPrev1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 10),
    _ZxAdslAtucChanPerfPrev1DayNcd_Type()
)
zxAdslAtucChanPerfPrev1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfPrev1DayNcd.setStatus("current")
_ZxAdslAtucChanPerfPrev1DayOcd_Type = Counter32
_ZxAdslAtucChanPerfPrev1DayOcd_Object = MibTableColumn
zxAdslAtucChanPerfPrev1DayOcd = _ZxAdslAtucChanPerfPrev1DayOcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 11),
    _ZxAdslAtucChanPerfPrev1DayOcd_Type()
)
zxAdslAtucChanPerfPrev1DayOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfPrev1DayOcd.setStatus("current")
_ZxAdslAtucChanPerfPrev1DayHec_Type = Counter32
_ZxAdslAtucChanPerfPrev1DayHec_Object = MibTableColumn
zxAdslAtucChanPerfPrev1DayHec = _ZxAdslAtucChanPerfPrev1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 7, 1, 12),
    _ZxAdslAtucChanPerfPrev1DayHec_Type()
)
zxAdslAtucChanPerfPrev1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAtucChanPerfPrev1DayHec.setStatus("current")
_ZxAdslAturChanPerfTable_Object = MibTable
zxAdslAturChanPerfTable = _ZxAdslAturChanPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8)
)
if mibBuilder.loadTexts:
    zxAdslAturChanPerfTable.setStatus("current")
_ZxAdslAturChanPerfEntry_Object = MibTableRow
zxAdslAturChanPerfEntry = _ZxAdslAturChanPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1)
)
zxAdslAturChanPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAdslAturChanPerfEntry.setStatus("current")
_ZxAdslAturChanPerfNcd_Type = Counter32
_ZxAdslAturChanPerfNcd_Object = MibTableColumn
zxAdslAturChanPerfNcd = _ZxAdslAturChanPerfNcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 1),
    _ZxAdslAturChanPerfNcd_Type()
)
zxAdslAturChanPerfNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfNcd.setStatus("current")
_ZxAdslAturChanPerfHec_Type = Counter32
_ZxAdslAturChanPerfHec_Object = MibTableColumn
zxAdslAturChanPerfHec = _ZxAdslAturChanPerfHec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 2),
    _ZxAdslAturChanPerfHec_Type()
)
zxAdslAturChanPerfHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfHec.setStatus("current")
_ZxAdslAturChanPerfCurr15Ncd_Type = Counter32
_ZxAdslAturChanPerfCurr15Ncd_Object = MibTableColumn
zxAdslAturChanPerfCurr15Ncd = _ZxAdslAturChanPerfCurr15Ncd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 3),
    _ZxAdslAturChanPerfCurr15Ncd_Type()
)
zxAdslAturChanPerfCurr15Ncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfCurr15Ncd.setStatus("current")
_ZxAdslAturChanPerfCurr15Hec_Type = Counter32
_ZxAdslAturChanPerfCurr15Hec_Object = MibTableColumn
zxAdslAturChanPerfCurr15Hec = _ZxAdslAturChanPerfCurr15Hec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 4),
    _ZxAdslAturChanPerfCurr15Hec_Type()
)
zxAdslAturChanPerfCurr15Hec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfCurr15Hec.setStatus("current")
_ZxAdslAturChanPerfCurr1DayNcd_Type = Counter32
_ZxAdslAturChanPerfCurr1DayNcd_Object = MibTableColumn
zxAdslAturChanPerfCurr1DayNcd = _ZxAdslAturChanPerfCurr1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 5),
    _ZxAdslAturChanPerfCurr1DayNcd_Type()
)
zxAdslAturChanPerfCurr1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfCurr1DayNcd.setStatus("current")
_ZxAdslAturChanPerfCurr1DayHec_Type = Counter32
_ZxAdslAturChanPerfCurr1DayHec_Object = MibTableColumn
zxAdslAturChanPerfCurr1DayHec = _ZxAdslAturChanPerfCurr1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 6),
    _ZxAdslAturChanPerfCurr1DayHec_Type()
)
zxAdslAturChanPerfCurr1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfCurr1DayHec.setStatus("current")
_ZxAdslAturChanPerfPrev1DayNcd_Type = Counter32
_ZxAdslAturChanPerfPrev1DayNcd_Object = MibTableColumn
zxAdslAturChanPerfPrev1DayNcd = _ZxAdslAturChanPerfPrev1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 7),
    _ZxAdslAturChanPerfPrev1DayNcd_Type()
)
zxAdslAturChanPerfPrev1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfPrev1DayNcd.setStatus("current")
_ZxAdslAturChanPerfPrev1DayHec_Type = Counter32
_ZxAdslAturChanPerfPrev1DayHec_Object = MibTableColumn
zxAdslAturChanPerfPrev1DayHec = _ZxAdslAturChanPerfPrev1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 8, 1, 8),
    _ZxAdslAturChanPerfPrev1DayHec_Type()
)
zxAdslAturChanPerfPrev1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslAturChanPerfPrev1DayHec.setStatus("current")
_ZxDslLoopTestTable_Object = MibTable
zxDslLoopTestTable = _ZxDslLoopTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9)
)
if mibBuilder.loadTexts:
    zxDslLoopTestTable.setStatus("current")
_ZxDslLoopTestEntry_Object = MibTableRow
zxDslLoopTestEntry = _ZxDslLoopTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1)
)
zxDslLoopTestEntry.setIndexNames(
    (0, "ZTE-DSL-LINE-EXT-MIB", "zxDslLoopTestPort"),
)
if mibBuilder.loadTexts:
    zxDslLoopTestEntry.setStatus("current")
_ZxDslLoopTestPort_Type = Integer32
_ZxDslLoopTestPort_Object = MibTableColumn
zxDslLoopTestPort = _ZxDslLoopTestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 1),
    _ZxDslLoopTestPort_Type()
)
zxDslLoopTestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslLoopTestPort.setStatus("current")


class _ZxDslLoopTestType_Type(Integer32):
    """Custom type zxDslLoopTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 0),
          ("cancle", 1),
          ("utopia", 2),
          ("afe", 3),
          ("hybrid", 4),
          ("atuc_OAM", 5),
          ("atur_OAM", 6))
    )


_ZxDslLoopTestType_Type.__name__ = "Integer32"
_ZxDslLoopTestType_Object = MibTableColumn
zxDslLoopTestType = _ZxDslLoopTestType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 2),
    _ZxDslLoopTestType_Type()
)
zxDslLoopTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestType.setStatus("current")


class _ZxDslLoopTestOperStatus_Type(Integer32):
    """Custom type zxDslLoopTestOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neverExcute", 0),
          ("excuting", 1),
          ("excuted", 2),
          ("faliedToCommit", 3))
    )


_ZxDslLoopTestOperStatus_Type.__name__ = "Integer32"
_ZxDslLoopTestOperStatus_Object = MibTableColumn
zxDslLoopTestOperStatus = _ZxDslLoopTestOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 3),
    _ZxDslLoopTestOperStatus_Type()
)
zxDslLoopTestOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestOperStatus.setStatus("current")


class _ZxDslLoopTestResult_Type(Integer32):
    """Custom type zxDslLoopTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("NoResult", 0),
          ("Success", 1),
          ("GeneralFailed", 2),
          ("NoSupport", 3),
          ("Unkown", 4),
          ("NoSuchPort", 5),
          ("LoopBackFailed", 6),
          ("PortNotActive", 7),
          ("PortInTesting", 8),
          ("PortInService", 9),
          ("PortFailures", 10),
          ("CardFailures", 11),
          ("NoPvcFound", 12),
          ("UnknownTestType", 13))
    )


_ZxDslLoopTestResult_Type.__name__ = "Integer32"
_ZxDslLoopTestResult_Object = MibTableColumn
zxDslLoopTestResult = _ZxDslLoopTestResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 4),
    _ZxDslLoopTestResult_Type()
)
zxDslLoopTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestResult.setStatus("current")
_ZxDslLoopTestConfParam1_Type = Integer32
_ZxDslLoopTestConfParam1_Object = MibTableColumn
zxDslLoopTestConfParam1 = _ZxDslLoopTestConfParam1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 5),
    _ZxDslLoopTestConfParam1_Type()
)
zxDslLoopTestConfParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestConfParam1.setStatus("current")
_ZxDslLoopTestConfParam2_Type = Integer32
_ZxDslLoopTestConfParam2_Object = MibTableColumn
zxDslLoopTestConfParam2 = _ZxDslLoopTestConfParam2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 6),
    _ZxDslLoopTestConfParam2_Type()
)
zxDslLoopTestConfParam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestConfParam2.setStatus("current")
_ZxDslLoopTestConfParam3_Type = Integer32
_ZxDslLoopTestConfParam3_Object = MibTableColumn
zxDslLoopTestConfParam3 = _ZxDslLoopTestConfParam3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 7),
    _ZxDslLoopTestConfParam3_Type()
)
zxDslLoopTestConfParam3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestConfParam3.setStatus("current")
_ZxDslLoopTestConfParam4_Type = Integer32
_ZxDslLoopTestConfParam4_Object = MibTableColumn
zxDslLoopTestConfParam4 = _ZxDslLoopTestConfParam4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 8),
    _ZxDslLoopTestConfParam4_Type()
)
zxDslLoopTestConfParam4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestConfParam4.setStatus("current")
_ZxDslLoopTestConfParam5_Type = Integer32
_ZxDslLoopTestConfParam5_Object = MibTableColumn
zxDslLoopTestConfParam5 = _ZxDslLoopTestConfParam5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 9),
    _ZxDslLoopTestConfParam5_Type()
)
zxDslLoopTestConfParam5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestConfParam5.setStatus("current")
_ZxDslLoopTestResultParam1_Type = Integer32
_ZxDslLoopTestResultParam1_Object = MibTableColumn
zxDslLoopTestResultParam1 = _ZxDslLoopTestResultParam1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 10),
    _ZxDslLoopTestResultParam1_Type()
)
zxDslLoopTestResultParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestResultParam1.setStatus("current")
_ZxDslLoopTestResultParam2_Type = Integer32
_ZxDslLoopTestResultParam2_Object = MibTableColumn
zxDslLoopTestResultParam2 = _ZxDslLoopTestResultParam2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 11),
    _ZxDslLoopTestResultParam2_Type()
)
zxDslLoopTestResultParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestResultParam2.setStatus("current")
_ZxDslLoopTestResultParam3_Type = Integer32
_ZxDslLoopTestResultParam3_Object = MibTableColumn
zxDslLoopTestResultParam3 = _ZxDslLoopTestResultParam3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 12),
    _ZxDslLoopTestResultParam3_Type()
)
zxDslLoopTestResultParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestResultParam3.setStatus("current")
_ZxDslLoopTestResultParam4_Type = Integer32
_ZxDslLoopTestResultParam4_Object = MibTableColumn
zxDslLoopTestResultParam4 = _ZxDslLoopTestResultParam4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 13),
    _ZxDslLoopTestResultParam4_Type()
)
zxDslLoopTestResultParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestResultParam4.setStatus("current")
_ZxDslLoopTestResultParam5_Type = Integer32
_ZxDslLoopTestResultParam5_Object = MibTableColumn
zxDslLoopTestResultParam5 = _ZxDslLoopTestResultParam5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 14),
    _ZxDslLoopTestResultParam5_Type()
)
zxDslLoopTestResultParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslLoopTestResultParam5.setStatus("current")
_ZxDslLoopTestRowStatus_Type = RowStatus
_ZxDslLoopTestRowStatus_Object = MibTableColumn
zxDslLoopTestRowStatus = _ZxDslLoopTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 9, 1, 15),
    _ZxDslLoopTestRowStatus_Type()
)
zxDslLoopTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLoopTestRowStatus.setStatus("current")


class _ZxAdslIsSupportAdsl2Plus_Type(Integer32):
    """Custom type zxAdslIsSupportAdsl2Plus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("noSupport", 2))
    )


_ZxAdslIsSupportAdsl2Plus_Type.__name__ = "Integer32"
_ZxAdslIsSupportAdsl2Plus_Object = MibScalar
zxAdslIsSupportAdsl2Plus = _ZxAdslIsSupportAdsl2Plus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 11),
    _ZxAdslIsSupportAdsl2Plus_Type()
)
zxAdslIsSupportAdsl2Plus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslIsSupportAdsl2Plus.setStatus("current")


class _ZxAdslIsSupportAdslRateThresh_Type(Integer32):
    """Custom type zxAdslIsSupportAdslRateThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Support", 1),
          ("noSupport", 2))
    )


_ZxAdslIsSupportAdslRateThresh_Type.__name__ = "Integer32"
_ZxAdslIsSupportAdslRateThresh_Object = MibScalar
zxAdslIsSupportAdslRateThresh = _ZxAdslIsSupportAdslRateThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 14),
    _ZxAdslIsSupportAdslRateThresh_Type()
)
zxAdslIsSupportAdslRateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAdslIsSupportAdslRateThresh.setStatus("current")
_ZxAdslLineAlarmConfProfileExtTable_Object = MibTable
zxAdslLineAlarmConfProfileExtTable = _ZxAdslLineAlarmConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20)
)
if mibBuilder.loadTexts:
    zxAdslLineAlarmConfProfileExtTable.setStatus("current")
_ZxAdslLineAlarmConfProfileExtEntry_Object = MibTableRow
zxAdslLineAlarmConfProfileExtEntry = _ZxAdslLineAlarmConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1)
)
if mibBuilder.loadTexts:
    zxAdslLineAlarmConfProfileExtEntry.setStatus("current")


class _ZxAdslAtucConnRateTolerance_Type(Integer32):
    """Custom type zxAdslAtucConnRateTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslAtucConnRateTolerance_Type.__name__ = "Integer32"
_ZxAdslAtucConnRateTolerance_Object = MibTableColumn
zxAdslAtucConnRateTolerance = _ZxAdslAtucConnRateTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 1),
    _ZxAdslAtucConnRateTolerance_Type()
)
zxAdslAtucConnRateTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAtucConnRateTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAtucConnRateTolerance.setUnits("%")


class _ZxAdslAturConnRateTolerance_Type(Integer32):
    """Custom type zxAdslAturConnRateTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslAturConnRateTolerance_Type.__name__ = "Integer32"
_ZxAdslAturConnRateTolerance_Object = MibTableColumn
zxAdslAturConnRateTolerance = _ZxAdslAturConnRateTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 2),
    _ZxAdslAturConnRateTolerance_Type()
)
zxAdslAturConnRateTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslAturConnRateTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslAturConnRateTolerance.setUnits("%")


class _ZxAdslThreshAtucConnRate_Type(Integer32):
    """Custom type zxAdslThreshAtucConnRate based on Integer32"""
    defaultValue = 0


_ZxAdslThreshAtucConnRate_Type.__name__ = "Integer32"
_ZxAdslThreshAtucConnRate_Object = MibTableColumn
zxAdslThreshAtucConnRate = _ZxAdslThreshAtucConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 3),
    _ZxAdslThreshAtucConnRate_Type()
)
zxAdslThreshAtucConnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAtucConnRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAtucConnRate.setUnits("kbps")


class _ZxAdslThreshAturConnRate_Type(Integer32):
    """Custom type zxAdslThreshAturConnRate based on Integer32"""
    defaultValue = 0


_ZxAdslThreshAturConnRate_Type.__name__ = "Integer32"
_ZxAdslThreshAturConnRate_Object = MibTableColumn
zxAdslThreshAturConnRate = _ZxAdslThreshAturConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 4),
    _ZxAdslThreshAturConnRate_Type()
)
zxAdslThreshAturConnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAturConnRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAturConnRate.setUnits("kbps")


class _ZxAdslThreshAtucBandwidthUtil_Type(Integer32):
    """Custom type zxAdslThreshAtucBandwidthUtil based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshAtucBandwidthUtil_Type.__name__ = "Integer32"
_ZxAdslThreshAtucBandwidthUtil_Object = MibTableColumn
zxAdslThreshAtucBandwidthUtil = _ZxAdslThreshAtucBandwidthUtil_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 5),
    _ZxAdslThreshAtucBandwidthUtil_Type()
)
zxAdslThreshAtucBandwidthUtil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAtucBandwidthUtil.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAtucBandwidthUtil.setUnits("%")


class _ZxAdslThreshAturBandwidthUtil_Type(Integer32):
    """Custom type zxAdslThreshAturBandwidthUtil based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshAturBandwidthUtil_Type.__name__ = "Integer32"
_ZxAdslThreshAturBandwidthUtil_Object = MibTableColumn
zxAdslThreshAturBandwidthUtil = _ZxAdslThreshAturBandwidthUtil_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 6),
    _ZxAdslThreshAturBandwidthUtil_Type()
)
zxAdslThreshAturBandwidthUtil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAturBandwidthUtil.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAturBandwidthUtil.setUnits("%")


class _ZxAdslThreshAtucPacketLossRate_Type(Integer32):
    """Custom type zxAdslThreshAtucPacketLossRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshAtucPacketLossRate_Type.__name__ = "Integer32"
_ZxAdslThreshAtucPacketLossRate_Object = MibTableColumn
zxAdslThreshAtucPacketLossRate = _ZxAdslThreshAtucPacketLossRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 7),
    _ZxAdslThreshAtucPacketLossRate_Type()
)
zxAdslThreshAtucPacketLossRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAtucPacketLossRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAtucPacketLossRate.setUnits("%")


class _ZxAdslThreshAturPacketLossRate_Type(Integer32):
    """Custom type zxAdslThreshAturPacketLossRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshAturPacketLossRate_Type.__name__ = "Integer32"
_ZxAdslThreshAturPacketLossRate_Object = MibTableColumn
zxAdslThreshAturPacketLossRate = _ZxAdslThreshAturPacketLossRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 8),
    _ZxAdslThreshAturPacketLossRate_Type()
)
zxAdslThreshAturPacketLossRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAturPacketLossRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAturPacketLossRate.setUnits("%")


class _ZxAdslThreshAtucBlockErrorRate_Type(Integer32):
    """Custom type zxAdslThreshAtucBlockErrorRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshAtucBlockErrorRate_Type.__name__ = "Integer32"
_ZxAdslThreshAtucBlockErrorRate_Object = MibTableColumn
zxAdslThreshAtucBlockErrorRate = _ZxAdslThreshAtucBlockErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 9),
    _ZxAdslThreshAtucBlockErrorRate_Type()
)
zxAdslThreshAtucBlockErrorRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAtucBlockErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAtucBlockErrorRate.setUnits("%")


class _ZxAdslThreshAturBlockErrorRate_Type(Integer32):
    """Custom type zxAdslThreshAturBlockErrorRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshAturBlockErrorRate_Type.__name__ = "Integer32"
_ZxAdslThreshAturBlockErrorRate_Object = MibTableColumn
zxAdslThreshAturBlockErrorRate = _ZxAdslThreshAturBlockErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 10),
    _ZxAdslThreshAturBlockErrorRate_Type()
)
zxAdslThreshAturBlockErrorRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshAturBlockErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAdslThreshAturBlockErrorRate.setUnits("%")


class _ZxAdslThreshReservedMetric1_Type(Integer32):
    """Custom type zxAdslThreshReservedMetric1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshReservedMetric1_Type.__name__ = "Integer32"
_ZxAdslThreshReservedMetric1_Object = MibTableColumn
zxAdslThreshReservedMetric1 = _ZxAdslThreshReservedMetric1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 11),
    _ZxAdslThreshReservedMetric1_Type()
)
zxAdslThreshReservedMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshReservedMetric1.setStatus("current")


class _ZxAdslThreshReservedMetric2_Type(Integer32):
    """Custom type zxAdslThreshReservedMetric2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshReservedMetric2_Type.__name__ = "Integer32"
_ZxAdslThreshReservedMetric2_Object = MibTableColumn
zxAdslThreshReservedMetric2 = _ZxAdslThreshReservedMetric2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 12),
    _ZxAdslThreshReservedMetric2_Type()
)
zxAdslThreshReservedMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshReservedMetric2.setStatus("current")


class _ZxAdslThreshReservedMetric3_Type(Integer32):
    """Custom type zxAdslThreshReservedMetric3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAdslThreshReservedMetric3_Type.__name__ = "Integer32"
_ZxAdslThreshReservedMetric3_Object = MibTableColumn
zxAdslThreshReservedMetric3 = _ZxAdslThreshReservedMetric3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 1, 20, 1, 13),
    _ZxAdslThreshReservedMetric3_Type()
)
zxAdslThreshReservedMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdslThreshReservedMetric3.setStatus("current")
_ZxAdslExtTraps_ObjectIdentity = ObjectIdentity
zxAdslExtTraps = _ZxAdslExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2)
)
adslLineConfProfileEntry.registerAugmentions(
    ("ZTE-DSL-LINE-EXT-MIB",
     "zxAdslLineConfProfileExtEntry")
)
zxAdslLineConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineAlarmConfProfileEntry.registerAugmentions(
    ("ZTE-DSL-LINE-EXT-MIB",
     "zxAdslLineAlarmConfProfileExtEntry")
)
zxAdslLineAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())

# Managed Objects groups


# Notification objects

zxAdslAtuxConnRateOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 1)
)
zxAdslAtuxConnRateOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanCurrTxRate"))
)
if mibBuilder.loadTexts:
    zxAdslAtuxConnRateOverThreshTrap.setStatus(
        "current"
    )

zxAdslAtuxConnRateUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 2)
)
zxAdslAtuxConnRateUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanCurrTxRate"))
)
if mibBuilder.loadTexts:
    zxAdslAtuxConnRateUnderThreshTrap.setStatus(
        "current"
    )

zxAdslAtucBandwidthUtilOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 5)
)
zxAdslAtucBandwidthUtilOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ZTE-DSL-LINE-EXT-MIB", "zxAdslLineTxDataRate"))
)
if mibBuilder.loadTexts:
    zxAdslAtucBandwidthUtilOverThreshTrap.setStatus(
        "current"
    )

zxAdslAtucBandwidthUtilUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 6)
)
zxAdslAtucBandwidthUtilUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ZTE-DSL-LINE-EXT-MIB", "zxAdslLineTxDataRate"))
)
if mibBuilder.loadTexts:
    zxAdslAtucBandwidthUtilUnderThreshTrap.setStatus(
        "current"
    )

zxAdslAturBandwidthUtilOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 7)
)
zxAdslAturBandwidthUtilOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ZTE-DSL-LINE-EXT-MIB", "zxAdslLineRxDataRate"))
)
if mibBuilder.loadTexts:
    zxAdslAturBandwidthUtilOverThreshTrap.setStatus(
        "current"
    )

zxAdslAturBandwidthUtilUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 8)
)
zxAdslAturBandwidthUtilUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ZTE-DSL-LINE-EXT-MIB", "zxAdslLineRxDataRate"))
)
if mibBuilder.loadTexts:
    zxAdslAturBandwidthUtilUnderThreshTrap.setStatus(
        "current"
    )

zxAdslAtucPacketLossRateOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 9)
)
zxAdslAtucPacketLossRateOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "ifOutDiscards"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifOutUcastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifOutMulticastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifOutBroadcastPkts"))
)
if mibBuilder.loadTexts:
    zxAdslAtucPacketLossRateOverThreshTrap.setStatus(
        "current"
    )

zxAdslAtucPacketLossRateUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 10)
)
zxAdslAtucPacketLossRateUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "ifOutDiscards"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifOutUcastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifOutMulticastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifOutBroadcastPkts"))
)
if mibBuilder.loadTexts:
    zxAdslAtucPacketLossRateUnderThreshTrap.setStatus(
        "current"
    )

zxAdslAturPacketLossRateOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 11)
)
zxAdslAturPacketLossRateOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "ifInDiscards"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifInUcastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifInMulticastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifInBroadcastPkts"))
)
if mibBuilder.loadTexts:
    zxAdslAturPacketLossRateOverThreshTrap.setStatus(
        "current"
    )

zxAdslAturPacketLossRateUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 12)
)
zxAdslAturPacketLossRateUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "ifInDiscards"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifInUcastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifInMulticastPkts"),
        ("ZTE-DSL-LINE-EXT-MIB", "ifInBroadcastPkts"))
)
if mibBuilder.loadTexts:
    zxAdslAturPacketLossRateUnderThreshTrap.setStatus(
        "current"
    )

zxAdslAtucBlockErrorRateOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 13)
)
zxAdslAtucBlockErrorRateOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanUncorrectBlks"),
        ("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanReceivedBlks"))
)
if mibBuilder.loadTexts:
    zxAdslAtucBlockErrorRateOverThreshTrap.setStatus(
        "current"
    )

zxAdslAtucBlockErrorRateUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 14)
)
zxAdslAtucBlockErrorRateUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanUncorrectBlks"),
        ("ZTE-DSL-LINE-EXT-MIB", "adslAtucChanReceivedBlks"))
)
if mibBuilder.loadTexts:
    zxAdslAtucBlockErrorRateUnderThreshTrap.setStatus(
        "current"
    )

zxAdslAturBlockErrorRateOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 15)
)
zxAdslAturBlockErrorRateOverThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAturChanUncorrectBlks"),
        ("ZTE-DSL-LINE-EXT-MIB", "adslAturChanReceivedBlks"))
)
if mibBuilder.loadTexts:
    zxAdslAturBlockErrorRateOverThreshTrap.setStatus(
        "current"
    )

zxAdslAturBlockErrorRateUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 4, 2, 16)
)
zxAdslAturBlockErrorRateUnderThreshTrap.setObjects(
      *(("ZTE-DSL-LINE-EXT-MIB", "adslAturChanUncorrectBlks"),
        ("ZTE-DSL-LINE-EXT-MIB", "adslAturChanReceivedBlks"))
)
if mibBuilder.loadTexts:
    zxAdslAturBlockErrorRateUnderThreshTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-LINE-EXT-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxAdslExtMib": zxAdslExtMib,
       "zxAdslExtMibObjects": zxAdslExtMibObjects,
       "zxAdslLineTable": zxAdslLineTable,
       "zxAdslLineEntry": zxAdslLineEntry,
       "zxAdslLinePMConfPMSF": zxAdslLinePMConfPMSF,
       "zxAdslLinePMState": zxAdslLinePMState,
       "zxAdslLineDMTTrellis": zxAdslLineDMTTrellis,
       "zxAdslLineTxAtmCells": zxAdslLineTxAtmCells,
       "zxAdslLineRxAtmCells": zxAdslLineRxAtmCells,
       "zxAdslLineIdleCells": zxAdslLineIdleCells,
       "zxAdslLineTxDataRate": zxAdslLineTxDataRate,
       "zxAdslLineRxDataRate": zxAdslLineRxDataRate,
       "zxAdslLineConfProfileExtTable": zxAdslLineConfProfileExtTable,
       "zxAdslLineConfProfileExtEntry": zxAdslLineConfProfileExtEntry,
       "zxAdslLineDMTConfTrellis": zxAdslLineDMTConfTrellis,
       "zxAdslAtucConfMaxBitsPerBin": zxAdslAtucConfMaxBitsPerBin,
       "zxAdslAtucConfTxStartBin": zxAdslAtucConfTxStartBin,
       "zxAdslAtucConfTxEndBin": zxAdslAtucConfTxEndBin,
       "zxAdslAtucConfRxStartBin": zxAdslAtucConfRxStartBin,
       "zxAdslAtucConfRxEndBin": zxAdslAtucConfRxEndBin,
       "zxAdslAtucConfUseCustomBins": zxAdslAtucConfUseCustomBins,
       "zxAdslAtucConfDnBitSwap": zxAdslAtucConfDnBitSwap,
       "zxAdslAtucConfUpBitSwap": zxAdslAtucConfUpBitSwap,
       "zxAdslAtucConfREADSL2Enable": zxAdslAtucConfREADSL2Enable,
       "zxAdslAtucConfPsdMaskType": zxAdslAtucConfPsdMaskType,
       "zxAdslAtucConfPMMode": zxAdslAtucConfPMMode,
       "zxAdslAtucConfPML0Time": zxAdslAtucConfPML0Time,
       "zxAdslAtucConfPML2Time": zxAdslAtucConfPML2Time,
       "zxAdslAtucConfPML2ATPR": zxAdslAtucConfPML2ATPR,
       "zxAdslAtucConfPML2Rate": zxAdslAtucConfPML2Rate,
       "zxAdsl2ConfMinProtectionDs": zxAdsl2ConfMinProtectionDs,
       "zxAdsl2ConfMinProtectionUs": zxAdsl2ConfMinProtectionUs,
       "zxAdslAtucPhysTable": zxAdslAtucPhysTable,
       "zxAdslAtucPhysEntry": zxAdslAtucPhysEntry,
       "zxAdslAtucPrevSnrMgn": zxAdslAtucPrevSnrMgn,
       "zxAdslAtucPrevAtn": zxAdslAtucPrevAtn,
       "zxAdslAtucPrevAttainableRate": zxAdslAtucPrevAttainableRate,
       "zxAdslAtucChipVersion": zxAdslAtucChipVersion,
       "zxAdslAturPhysTable": zxAdslAturPhysTable,
       "zxAdslAturPhysEntry": zxAdslAturPhysEntry,
       "zxAdslAturPrevSnrMgn": zxAdslAturPrevSnrMgn,
       "zxAdslAturPrevAtn": zxAdslAturPrevAtn,
       "zxAdslAturPrevAttainableRate": zxAdslAturPrevAttainableRate,
       "zxAdslAtucChanTable": zxAdslAtucChanTable,
       "zxAdslAtucChanEntry": zxAdslAtucChanEntry,
       "zxAdslAtucChanRsSymbols": zxAdslAtucChanRsSymbols,
       "zxAdslAtucChanRsDepth": zxAdslAtucChanRsDepth,
       "zxAdslAtucChanRsRedundancy": zxAdslAtucChanRsRedundancy,
       "zxAdslAturChanTable": zxAdslAturChanTable,
       "zxAdslAturChanEntry": zxAdslAturChanEntry,
       "zxAdslAturChanRsSymbols": zxAdslAturChanRsSymbols,
       "zxAdslAturChanRsDepth": zxAdslAturChanRsDepth,
       "zxAdslAturChanRsRedundancy": zxAdslAturChanRsRedundancy,
       "zxAdslAtucChanPerfTable": zxAdslAtucChanPerfTable,
       "zxAdslAtucChanPerfEntry": zxAdslAtucChanPerfEntry,
       "zxAdslAtucChanPerfNcd": zxAdslAtucChanPerfNcd,
       "zxAdslAtucChanPerfOcd": zxAdslAtucChanPerfOcd,
       "zxAdslAtucChanPerfHec": zxAdslAtucChanPerfHec,
       "zxAdslAtucChanPerfCurr15Ncd": zxAdslAtucChanPerfCurr15Ncd,
       "zxAdslAtucChanPerfCurr15Ocd": zxAdslAtucChanPerfCurr15Ocd,
       "zxAdslAtucChanPerfCurr15Hec": zxAdslAtucChanPerfCurr15Hec,
       "zxAdslAtucChanPerfCurr1DayNcd": zxAdslAtucChanPerfCurr1DayNcd,
       "zxAdslAtucChanPerfCurr1DayOcd": zxAdslAtucChanPerfCurr1DayOcd,
       "zxAdslAtucChanPerfCurr1DayHec": zxAdslAtucChanPerfCurr1DayHec,
       "zxAdslAtucChanPerfPrev1DayNcd": zxAdslAtucChanPerfPrev1DayNcd,
       "zxAdslAtucChanPerfPrev1DayOcd": zxAdslAtucChanPerfPrev1DayOcd,
       "zxAdslAtucChanPerfPrev1DayHec": zxAdslAtucChanPerfPrev1DayHec,
       "zxAdslAturChanPerfTable": zxAdslAturChanPerfTable,
       "zxAdslAturChanPerfEntry": zxAdslAturChanPerfEntry,
       "zxAdslAturChanPerfNcd": zxAdslAturChanPerfNcd,
       "zxAdslAturChanPerfHec": zxAdslAturChanPerfHec,
       "zxAdslAturChanPerfCurr15Ncd": zxAdslAturChanPerfCurr15Ncd,
       "zxAdslAturChanPerfCurr15Hec": zxAdslAturChanPerfCurr15Hec,
       "zxAdslAturChanPerfCurr1DayNcd": zxAdslAturChanPerfCurr1DayNcd,
       "zxAdslAturChanPerfCurr1DayHec": zxAdslAturChanPerfCurr1DayHec,
       "zxAdslAturChanPerfPrev1DayNcd": zxAdslAturChanPerfPrev1DayNcd,
       "zxAdslAturChanPerfPrev1DayHec": zxAdslAturChanPerfPrev1DayHec,
       "zxDslLoopTestTable": zxDslLoopTestTable,
       "zxDslLoopTestEntry": zxDslLoopTestEntry,
       "zxDslLoopTestPort": zxDslLoopTestPort,
       "zxDslLoopTestType": zxDslLoopTestType,
       "zxDslLoopTestOperStatus": zxDslLoopTestOperStatus,
       "zxDslLoopTestResult": zxDslLoopTestResult,
       "zxDslLoopTestConfParam1": zxDslLoopTestConfParam1,
       "zxDslLoopTestConfParam2": zxDslLoopTestConfParam2,
       "zxDslLoopTestConfParam3": zxDslLoopTestConfParam3,
       "zxDslLoopTestConfParam4": zxDslLoopTestConfParam4,
       "zxDslLoopTestConfParam5": zxDslLoopTestConfParam5,
       "zxDslLoopTestResultParam1": zxDslLoopTestResultParam1,
       "zxDslLoopTestResultParam2": zxDslLoopTestResultParam2,
       "zxDslLoopTestResultParam3": zxDslLoopTestResultParam3,
       "zxDslLoopTestResultParam4": zxDslLoopTestResultParam4,
       "zxDslLoopTestResultParam5": zxDslLoopTestResultParam5,
       "zxDslLoopTestRowStatus": zxDslLoopTestRowStatus,
       "zxAdslIsSupportAdsl2Plus": zxAdslIsSupportAdsl2Plus,
       "zxAdslIsSupportAdslRateThresh": zxAdslIsSupportAdslRateThresh,
       "zxAdslLineAlarmConfProfileExtTable": zxAdslLineAlarmConfProfileExtTable,
       "zxAdslLineAlarmConfProfileExtEntry": zxAdslLineAlarmConfProfileExtEntry,
       "zxAdslAtucConnRateTolerance": zxAdslAtucConnRateTolerance,
       "zxAdslAturConnRateTolerance": zxAdslAturConnRateTolerance,
       "zxAdslThreshAtucConnRate": zxAdslThreshAtucConnRate,
       "zxAdslThreshAturConnRate": zxAdslThreshAturConnRate,
       "zxAdslThreshAtucBandwidthUtil": zxAdslThreshAtucBandwidthUtil,
       "zxAdslThreshAturBandwidthUtil": zxAdslThreshAturBandwidthUtil,
       "zxAdslThreshAtucPacketLossRate": zxAdslThreshAtucPacketLossRate,
       "zxAdslThreshAturPacketLossRate": zxAdslThreshAturPacketLossRate,
       "zxAdslThreshAtucBlockErrorRate": zxAdslThreshAtucBlockErrorRate,
       "zxAdslThreshAturBlockErrorRate": zxAdslThreshAturBlockErrorRate,
       "zxAdslThreshReservedMetric1": zxAdslThreshReservedMetric1,
       "zxAdslThreshReservedMetric2": zxAdslThreshReservedMetric2,
       "zxAdslThreshReservedMetric3": zxAdslThreshReservedMetric3,
       "zxAdslExtTraps": zxAdslExtTraps,
       "zxAdslAtuxConnRateOverThreshTrap": zxAdslAtuxConnRateOverThreshTrap,
       "zxAdslAtuxConnRateUnderThreshTrap": zxAdslAtuxConnRateUnderThreshTrap,
       "zxAdslAtucBandwidthUtilOverThreshTrap": zxAdslAtucBandwidthUtilOverThreshTrap,
       "zxAdslAtucBandwidthUtilUnderThreshTrap": zxAdslAtucBandwidthUtilUnderThreshTrap,
       "zxAdslAturBandwidthUtilOverThreshTrap": zxAdslAturBandwidthUtilOverThreshTrap,
       "zxAdslAturBandwidthUtilUnderThreshTrap": zxAdslAturBandwidthUtilUnderThreshTrap,
       "zxAdslAtucPacketLossRateOverThreshTrap": zxAdslAtucPacketLossRateOverThreshTrap,
       "zxAdslAtucPacketLossRateUnderThreshTrap": zxAdslAtucPacketLossRateUnderThreshTrap,
       "zxAdslAturPacketLossRateOverThreshTrap": zxAdslAturPacketLossRateOverThreshTrap,
       "zxAdslAturPacketLossRateUnderThreshTrap": zxAdslAturPacketLossRateUnderThreshTrap,
       "zxAdslAtucBlockErrorRateOverThreshTrap": zxAdslAtucBlockErrorRateOverThreshTrap,
       "zxAdslAtucBlockErrorRateUnderThreshTrap": zxAdslAtucBlockErrorRateUnderThreshTrap,
       "zxAdslAturBlockErrorRateOverThreshTrap": zxAdslAturBlockErrorRateOverThreshTrap,
       "zxAdslAturBlockErrorRateUnderThreshTrap": zxAdslAturBlockErrorRateUnderThreshTrap}
)
