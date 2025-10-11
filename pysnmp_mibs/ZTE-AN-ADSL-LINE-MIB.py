# SNMP MIB module (ZTE-AN-ADSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ADSL-LINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:24 2025
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

(adslAtucChanConfInterleaveMaxTxRate,
 adslAtucChanCurrTxRate,
 adslAtucChanIntervalEntry,
 adslAturChanConfInterleaveMaxTxRate,
 adslAturChanCurrTxRate,
 adslAturChanIntervalEntry,
 adslLineAlarmConfProfileEntry,
 adslLineConfProfileEntry,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslAtucChanConfInterleaveMaxTxRate",
    "adslAtucChanCurrTxRate",
    "adslAtucChanIntervalEntry",
    "adslAturChanConfInterleaveMaxTxRate",
    "adslAturChanCurrTxRate",
    "adslAturChanIntervalEntry",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnAdslMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnAdslMibObjects_ObjectIdentity = ObjectIdentity
zxAnAdslMibObjects = _ZxAnAdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1)
)
_ZxAnAdslLineTable_Object = MibTable
zxAnAdslLineTable = _ZxAnAdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnAdslLineTable.setStatus("current")
_ZxAnAdslLineEntry_Object = MibTableRow
zxAnAdslLineEntry = _ZxAnAdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1, 1)
)
zxAnAdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslLineEntry.setStatus("current")
_ZxAnAdslLineTxDataRate_Type = Gauge32
_ZxAnAdslLineTxDataRate_Object = MibTableColumn
zxAnAdslLineTxDataRate = _ZxAnAdslLineTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1, 1, 1),
    _ZxAnAdslLineTxDataRate_Type()
)
zxAnAdslLineTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslLineTxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslLineTxDataRate.setUnits("kbps")
_ZxAnAdslLineRxDataRate_Type = Gauge32
_ZxAnAdslLineRxDataRate_Object = MibTableColumn
zxAnAdslLineRxDataRate = _ZxAnAdslLineRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1, 1, 2),
    _ZxAnAdslLineRxDataRate_Type()
)
zxAnAdslLineRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslLineRxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslLineRxDataRate.setUnits("kbps")


class _ZxAnAdslAtucActInp_Type(Integer32):
    """Custom type zxAnAdslAtucActInp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAdslAtucActInp_Type.__name__ = "Integer32"
_ZxAnAdslAtucActInp_Object = MibTableColumn
zxAnAdslAtucActInp = _ZxAnAdslAtucActInp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1, 1, 3),
    _ZxAnAdslAtucActInp_Type()
)
zxAnAdslAtucActInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucActInp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucActInp.setUnits("0.1 symbols")


class _ZxAnAdslAturActInp_Type(Integer32):
    """Custom type zxAnAdslAturActInp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAdslAturActInp_Type.__name__ = "Integer32"
_ZxAnAdslAturActInp_Object = MibTableColumn
zxAnAdslAturActInp = _ZxAnAdslAturActInp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1, 1, 4),
    _ZxAnAdslAturActInp_Type()
)
zxAnAdslAturActInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturActInp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturActInp.setUnits("0.1 symbols")


class _ZxAnAdslLineExtConfPrf_Type(SnmpAdminString):
    """Custom type zxAnAdslLineExtConfPrf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnAdslLineExtConfPrf_Type.__name__ = "SnmpAdminString"
_ZxAnAdslLineExtConfPrf_Object = MibTableColumn
zxAnAdslLineExtConfPrf = _ZxAnAdslLineExtConfPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 1, 1, 5),
    _ZxAnAdslLineExtConfPrf_Type()
)
zxAnAdslLineExtConfPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAdslLineExtConfPrf.setStatus("current")
_ZxAnAdslLineConfProfileExtTable_Object = MibTable
zxAnAdslLineConfProfileExtTable = _ZxAnAdslLineConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnAdslLineConfProfileExtTable.setStatus("current")
_ZxAnAdslLineConfProfileExtEntry_Object = MibTableRow
zxAnAdslLineConfProfileExtEntry = _ZxAnAdslLineConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnAdslLineConfProfileExtEntry.setStatus("current")
_ZxAnAdslLineConfTxStartBin_Type = Integer32
_ZxAnAdslLineConfTxStartBin_Object = MibTableColumn
zxAnAdslLineConfTxStartBin = _ZxAnAdslLineConfTxStartBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 1),
    _ZxAnAdslLineConfTxStartBin_Type()
)
zxAnAdslLineConfTxStartBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfTxStartBin.setStatus("current")


class _ZxAnAdslLineConfTxEndBin_Type(Integer32):
    """Custom type zxAnAdslLineConfTxEndBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ZxAnAdslLineConfTxEndBin_Type.__name__ = "Integer32"
_ZxAnAdslLineConfTxEndBin_Object = MibTableColumn
zxAnAdslLineConfTxEndBin = _ZxAnAdslLineConfTxEndBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 2),
    _ZxAnAdslLineConfTxEndBin_Type()
)
zxAnAdslLineConfTxEndBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfTxEndBin.setStatus("current")
_ZxAnAdslLineConfRxStartBin_Type = Integer32
_ZxAnAdslLineConfRxStartBin_Object = MibTableColumn
zxAnAdslLineConfRxStartBin = _ZxAnAdslLineConfRxStartBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 3),
    _ZxAnAdslLineConfRxStartBin_Type()
)
zxAnAdslLineConfRxStartBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfRxStartBin.setStatus("current")


class _ZxAnAdslLineConfRxEndBin_Type(Integer32):
    """Custom type zxAnAdslLineConfRxEndBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ZxAnAdslLineConfRxEndBin_Type.__name__ = "Integer32"
_ZxAnAdslLineConfRxEndBin_Object = MibTableColumn
zxAnAdslLineConfRxEndBin = _ZxAnAdslLineConfRxEndBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 4),
    _ZxAnAdslLineConfRxEndBin_Type()
)
zxAnAdslLineConfRxEndBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfRxEndBin.setStatus("current")


class _ZxAnAdslLineConfUseCustomBins_Type(Integer32):
    """Custom type zxAnAdslLineConfUseCustomBins based on Integer32"""
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


_ZxAnAdslLineConfUseCustomBins_Type.__name__ = "Integer32"
_ZxAnAdslLineConfUseCustomBins_Object = MibTableColumn
zxAnAdslLineConfUseCustomBins = _ZxAnAdslLineConfUseCustomBins_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 5),
    _ZxAnAdslLineConfUseCustomBins_Type()
)
zxAnAdslLineConfUseCustomBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfUseCustomBins.setStatus("current")
_ZxAnAdslAtucConfPsdMaskType_Type = Integer32
_ZxAnAdslAtucConfPsdMaskType_Object = MibTableColumn
zxAnAdslAtucConfPsdMaskType = _ZxAnAdslAtucConfPsdMaskType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 6),
    _ZxAnAdslAtucConfPsdMaskType_Type()
)
zxAnAdslAtucConfPsdMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPsdMaskType.setStatus("current")


class _ZxAnAdslLineConfPMMode_Type(Bits):
    """Custom type zxAnAdslLineConfPMMode based on Bits"""
    namedValues = NamedValues(
        *(("idle", 0),
          ("lowPower", 1))
    )

_ZxAnAdslLineConfPMMode_Type.__name__ = "Bits"
_ZxAnAdslLineConfPMMode_Object = MibTableColumn
zxAnAdslLineConfPMMode = _ZxAnAdslLineConfPMMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 7),
    _ZxAnAdslLineConfPMMode_Type()
)
zxAnAdslLineConfPMMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfPMMode.setStatus("current")


class _ZxAnAdslLineConfPML2Rate_Type(Integer32):
    """Custom type zxAnAdslLineConfPML2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1024),
    )


_ZxAnAdslLineConfPML2Rate_Type.__name__ = "Integer32"
_ZxAnAdslLineConfPML2Rate_Object = MibTableColumn
zxAnAdslLineConfPML2Rate = _ZxAnAdslLineConfPML2Rate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 8),
    _ZxAnAdslLineConfPML2Rate_Type()
)
zxAnAdslLineConfPML2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfPML2Rate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslLineConfPML2Rate.setUnits("kbps")


class _ZxAnAdsl2ConfMinProtectionDs_Type(Integer32):
    """Custom type zxAnAdsl2ConfMinProtectionDs based on Integer32"""
    defaultValue = 2

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoAdaption", 0),
          ("noProtection", 1),
          ("halfSymbol", 2),
          ("singleSymbol", 3),
          ("twoSymbols", 4),
          ("fourSymbols", 5),
          ("eightSymbols", 6),
          ("sixteenSymbols", 7))
    )


_ZxAnAdsl2ConfMinProtectionDs_Type.__name__ = "Integer32"
_ZxAnAdsl2ConfMinProtectionDs_Object = MibTableColumn
zxAnAdsl2ConfMinProtectionDs = _ZxAnAdsl2ConfMinProtectionDs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 9),
    _ZxAnAdsl2ConfMinProtectionDs_Type()
)
zxAnAdsl2ConfMinProtectionDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdsl2ConfMinProtectionDs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdsl2ConfMinProtectionDs.setUnits("symbols")


class _ZxAnAdslLineConfMinProtectionUs_Type(Integer32):
    """Custom type zxAnAdslLineConfMinProtectionUs based on Integer32"""
    defaultValue = 2

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoAdaption", 0),
          ("noProtection", 1),
          ("halfSymbol", 2),
          ("singleSymbol", 3),
          ("twoSymbols", 4),
          ("fourSymbols", 5),
          ("eightSymbols", 6),
          ("sixteenSymbols", 7))
    )


_ZxAnAdslLineConfMinProtectionUs_Type.__name__ = "Integer32"
_ZxAnAdslLineConfMinProtectionUs_Object = MibTableColumn
zxAnAdslLineConfMinProtectionUs = _ZxAnAdslLineConfMinProtectionUs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 10),
    _ZxAnAdslLineConfMinProtectionUs_Type()
)
zxAnAdslLineConfMinProtectionUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslLineConfMinProtectionUs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslLineConfMinProtectionUs.setUnits("symbols")


class _ZxAnAdslConfDMTConfTrellis_Type(Integer32):
    """Custom type zxAnAdslConfDMTConfTrellis based on Integer32"""
    defaultValue = 1

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


_ZxAnAdslConfDMTConfTrellis_Type.__name__ = "Integer32"
_ZxAnAdslConfDMTConfTrellis_Object = MibTableColumn
zxAnAdslConfDMTConfTrellis = _ZxAnAdslConfDMTConfTrellis_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 11),
    _ZxAnAdslConfDMTConfTrellis_Type()
)
zxAnAdslConfDMTConfTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslConfDMTConfTrellis.setStatus("current")


class _ZxAnAdslAtucConfMaxBitsPerBin_Type(Integer32):
    """Custom type zxAnAdslAtucConfMaxBitsPerBin based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZxAnAdslAtucConfMaxBitsPerBin_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfMaxBitsPerBin_Object = MibTableColumn
zxAnAdslAtucConfMaxBitsPerBin = _ZxAnAdslAtucConfMaxBitsPerBin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 12),
    _ZxAnAdslAtucConfMaxBitsPerBin_Type()
)
zxAnAdslAtucConfMaxBitsPerBin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfMaxBitsPerBin.setStatus("current")


class _ZxAnAdslAtucConfBitSwapDs_Type(Integer32):
    """Custom type zxAnAdslAtucConfBitSwapDs based on Integer32"""
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


_ZxAnAdslAtucConfBitSwapDs_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfBitSwapDs_Object = MibTableColumn
zxAnAdslAtucConfBitSwapDs = _ZxAnAdslAtucConfBitSwapDs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 13),
    _ZxAnAdslAtucConfBitSwapDs_Type()
)
zxAnAdslAtucConfBitSwapDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfBitSwapDs.setStatus("current")


class _ZxAnAdslAtucConfBitSwapUs_Type(Integer32):
    """Custom type zxAnAdslAtucConfBitSwapUs based on Integer32"""
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


_ZxAnAdslAtucConfBitSwapUs_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfBitSwapUs_Object = MibTableColumn
zxAnAdslAtucConfBitSwapUs = _ZxAnAdslAtucConfBitSwapUs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 14),
    _ZxAnAdslAtucConfBitSwapUs_Type()
)
zxAnAdslAtucConfBitSwapUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfBitSwapUs.setStatus("current")


class _ZxAnAdslAtucConfReAdsl2Enable_Type(Integer32):
    """Custom type zxAnAdslAtucConfReAdsl2Enable based on Integer32"""
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


_ZxAnAdslAtucConfReAdsl2Enable_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfReAdsl2Enable_Object = MibTableColumn
zxAnAdslAtucConfReAdsl2Enable = _ZxAnAdslAtucConfReAdsl2Enable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 15),
    _ZxAnAdslAtucConfReAdsl2Enable_Type()
)
zxAnAdslAtucConfReAdsl2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfReAdsl2Enable.setStatus("current")


class _ZxAnAdslAtucConfPmL0Time_Type(Integer32):
    """Custom type zxAnAdslAtucConfPmL0Time based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAdslAtucConfPmL0Time_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfPmL0Time_Object = MibTableColumn
zxAnAdslAtucConfPmL0Time = _ZxAnAdslAtucConfPmL0Time_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 16),
    _ZxAnAdslAtucConfPmL0Time_Type()
)
zxAnAdslAtucConfPmL0Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPmL0Time.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPmL0Time.setUnits("seconds")


class _ZxAnAdslAtucConfPmL2Time_Type(Integer32):
    """Custom type zxAnAdslAtucConfPmL2Time based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAdslAtucConfPmL2Time_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfPmL2Time_Object = MibTableColumn
zxAnAdslAtucConfPmL2Time = _ZxAnAdslAtucConfPmL2Time_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 17),
    _ZxAnAdslAtucConfPmL2Time_Type()
)
zxAnAdslAtucConfPmL2Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPmL2Time.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPmL2Time.setUnits("seconds")


class _ZxAnAdslAtucConfPmL2Atpr_Type(Integer32):
    """Custom type zxAnAdslAtucConfPmL2Atpr based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ZxAnAdslAtucConfPmL2Atpr_Type.__name__ = "Integer32"
_ZxAnAdslAtucConfPmL2Atpr_Object = MibTableColumn
zxAnAdslAtucConfPmL2Atpr = _ZxAnAdslAtucConfPmL2Atpr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 18),
    _ZxAnAdslAtucConfPmL2Atpr_Type()
)
zxAnAdslAtucConfPmL2Atpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPmL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucConfPmL2Atpr.setUnits("dB")


class _ZxAdsl2ConfPsdMaskSelectUs_Type(Integer32):
    """Custom type zxAdsl2ConfPsdMaskSelectUs based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("adlu32Eu32", 1),
          ("adlu36Eu36", 2),
          ("adlu40Eu40", 3),
          ("adlu44Eu44", 4),
          ("adlu48Eu48", 5),
          ("adlu52Eu52", 6),
          ("adlu56Eu56", 7),
          ("adlu60Eu60", 8),
          ("adlu64Eu64", 9))
    )


_ZxAdsl2ConfPsdMaskSelectUs_Type.__name__ = "Integer32"
_ZxAdsl2ConfPsdMaskSelectUs_Object = MibTableColumn
zxAdsl2ConfPsdMaskSelectUs = _ZxAdsl2ConfPsdMaskSelectUs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 2, 1, 19),
    _ZxAdsl2ConfPsdMaskSelectUs_Type()
)
zxAdsl2ConfPsdMaskSelectUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAdsl2ConfPsdMaskSelectUs.setStatus("current")
_ZxAnAdslAtucChanTable_Object = MibTable
zxAnAdslAtucChanTable = _ZxAnAdslAtucChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanTable.setStatus("current")
_ZxAnAdslAtucChanEntry_Object = MibTableRow
zxAnAdslAtucChanEntry = _ZxAnAdslAtucChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 3, 1)
)
zxAnAdslAtucChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanEntry.setStatus("current")


class _ZxAnAdslAtucChanInpEtr_Type(Unsigned32):
    """Custom type zxAnAdslAtucChanInpEtr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000),
    )


_ZxAnAdslAtucChanInpEtr_Type.__name__ = "Unsigned32"
_ZxAnAdslAtucChanInpEtr_Object = MibTableColumn
zxAnAdslAtucChanInpEtr = _ZxAnAdslAtucChanInpEtr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 3, 1, 1),
    _ZxAnAdslAtucChanInpEtr_Type()
)
zxAnAdslAtucChanInpEtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpEtr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpEtr.setUnits("kbps")


class _ZxAnAdslAtucChanInpEftr_Type(Unsigned32):
    """Custom type zxAnAdslAtucChanInpEftr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000),
    )


_ZxAnAdslAtucChanInpEftr_Type.__name__ = "Unsigned32"
_ZxAnAdslAtucChanInpEftr_Object = MibTableColumn
zxAnAdslAtucChanInpEftr = _ZxAnAdslAtucChanInpEftr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 3, 1, 2),
    _ZxAnAdslAtucChanInpEftr_Type()
)
zxAnAdslAtucChanInpEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpEftr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpEftr.setUnits("kbps")


class _ZxAnAdslAtucChanInpMinEftr_Type(Unsigned32):
    """Custom type zxAnAdslAtucChanInpMinEftr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000),
    )


_ZxAnAdslAtucChanInpMinEftr_Type.__name__ = "Unsigned32"
_ZxAnAdslAtucChanInpMinEftr_Object = MibTableColumn
zxAnAdslAtucChanInpMinEftr = _ZxAnAdslAtucChanInpMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 3, 1, 3),
    _ZxAnAdslAtucChanInpMinEftr_Type()
)
zxAnAdslAtucChanInpMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpMinEftr.setUnits("kbps")


class _ZxAnAdslAtucChanInpActDelay_Type(Integer32):
    """Custom type zxAnAdslAtucChanInpActDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnAdslAtucChanInpActDelay_Type.__name__ = "Integer32"
_ZxAnAdslAtucChanInpActDelay_Object = MibTableColumn
zxAnAdslAtucChanInpActDelay = _ZxAnAdslAtucChanInpActDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 3, 1, 4),
    _ZxAnAdslAtucChanInpActDelay_Type()
)
zxAnAdslAtucChanInpActDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpActDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanInpActDelay.setUnits("ms")
_ZxAnAdslAturChanTable_Object = MibTable
zxAnAdslAturChanTable = _ZxAnAdslAturChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanTable.setStatus("current")
_ZxAnAdslAturChanEntry_Object = MibTableRow
zxAnAdslAturChanEntry = _ZxAnAdslAturChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 4, 1)
)
zxAnAdslAturChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanEntry.setStatus("current")


class _ZxAnAdslAturChanInpEtr_Type(Unsigned32):
    """Custom type zxAnAdslAturChanInpEtr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000),
    )


_ZxAnAdslAturChanInpEtr_Type.__name__ = "Unsigned32"
_ZxAnAdslAturChanInpEtr_Object = MibTableColumn
zxAnAdslAturChanInpEtr = _ZxAnAdslAturChanInpEtr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 4, 1, 1),
    _ZxAnAdslAturChanInpEtr_Type()
)
zxAnAdslAturChanInpEtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpEtr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpEtr.setUnits("kbps")


class _ZxAnAdslAturChanInpEftr_Type(Unsigned32):
    """Custom type zxAnAdslAturChanInpEftr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000),
    )


_ZxAnAdslAturChanInpEftr_Type.__name__ = "Unsigned32"
_ZxAnAdslAturChanInpEftr_Object = MibTableColumn
zxAnAdslAturChanInpEftr = _ZxAnAdslAturChanInpEftr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 4, 1, 2),
    _ZxAnAdslAturChanInpEftr_Type()
)
zxAnAdslAturChanInpEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpEftr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpEftr.setUnits("kbps")


class _ZxAnAdslAturChanInpMinEftr_Type(Unsigned32):
    """Custom type zxAnAdslAturChanInpMinEftr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000),
    )


_ZxAnAdslAturChanInpMinEftr_Type.__name__ = "Unsigned32"
_ZxAnAdslAturChanInpMinEftr_Object = MibTableColumn
zxAnAdslAturChanInpMinEftr = _ZxAnAdslAturChanInpMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 4, 1, 3),
    _ZxAnAdslAturChanInpMinEftr_Type()
)
zxAnAdslAturChanInpMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpMinEftr.setUnits("kbps")


class _ZxAnAdslAturChanInpActDelay_Type(Integer32):
    """Custom type zxAnAdslAturChanInpActDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnAdslAturChanInpActDelay_Type.__name__ = "Integer32"
_ZxAnAdslAturChanInpActDelay_Object = MibTableColumn
zxAnAdslAturChanInpActDelay = _ZxAnAdslAturChanInpActDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 4, 1, 4),
    _ZxAnAdslAturChanInpActDelay_Type()
)
zxAnAdslAturChanInpActDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpActDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturChanInpActDelay.setUnits("ms")
_ZxAnAdslLineAlarmConfProfileExtTable_Object = MibTable
zxAnAdslLineAlarmConfProfileExtTable = _ZxAnAdslLineAlarmConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20)
)
if mibBuilder.loadTexts:
    zxAnAdslLineAlarmConfProfileExtTable.setStatus("current")
_ZxAnAdslLineAlarmConfProfileExtEntry_Object = MibTableRow
zxAnAdslLineAlarmConfProfileExtEntry = _ZxAnAdslLineAlarmConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1)
)
if mibBuilder.loadTexts:
    zxAnAdslLineAlarmConfProfileExtEntry.setStatus("current")


class _ZxAnAdslAtucConnRateTolerance_Type(Integer32):
    """Custom type zxAnAdslAtucConnRateTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnAdslAtucConnRateTolerance_Type.__name__ = "Integer32"
_ZxAnAdslAtucConnRateTolerance_Object = MibTableColumn
zxAnAdslAtucConnRateTolerance = _ZxAnAdslAtucConnRateTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 1),
    _ZxAnAdslAtucConnRateTolerance_Type()
)
zxAnAdslAtucConnRateTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucConnRateTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucConnRateTolerance.setUnits("%")


class _ZxAnAdslAturConnRateTolerance_Type(Integer32):
    """Custom type zxAnAdslAturConnRateTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnAdslAturConnRateTolerance_Type.__name__ = "Integer32"
_ZxAnAdslAturConnRateTolerance_Object = MibTableColumn
zxAnAdslAturConnRateTolerance = _ZxAnAdslAturConnRateTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 2),
    _ZxAnAdslAturConnRateTolerance_Type()
)
zxAnAdslAturConnRateTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAturConnRateTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturConnRateTolerance.setUnits("%")


class _ZxAnAdslAtucThreshConnRate_Type(Integer32):
    """Custom type zxAnAdslAtucThreshConnRate based on Integer32"""
    defaultValue = 0


_ZxAnAdslAtucThreshConnRate_Type.__name__ = "Integer32"
_ZxAnAdslAtucThreshConnRate_Object = MibTableColumn
zxAnAdslAtucThreshConnRate = _ZxAnAdslAtucThreshConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 3),
    _ZxAnAdslAtucThreshConnRate_Type()
)
zxAnAdslAtucThreshConnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAtucThreshConnRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucThreshConnRate.setUnits("kbps")


class _ZxAnAdslAturThreshConnRate_Type(Integer32):
    """Custom type zxAnAdslAturThreshConnRate based on Integer32"""
    defaultValue = 0


_ZxAnAdslAturThreshConnRate_Type.__name__ = "Integer32"
_ZxAnAdslAturThreshConnRate_Object = MibTableColumn
zxAnAdslAturThreshConnRate = _ZxAnAdslAturThreshConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 4),
    _ZxAnAdslAturThreshConnRate_Type()
)
zxAnAdslAturThreshConnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAturThreshConnRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturThreshConnRate.setUnits("kbps")


class _ZxAnAdslMaxAtucConnRateTolerance_Type(Integer32):
    """Custom type zxAnAdslMaxAtucConnRateTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnAdslMaxAtucConnRateTolerance_Type.__name__ = "Integer32"
_ZxAnAdslMaxAtucConnRateTolerance_Object = MibTableColumn
zxAnAdslMaxAtucConnRateTolerance = _ZxAnAdslMaxAtucConnRateTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 5),
    _ZxAnAdslMaxAtucConnRateTolerance_Type()
)
zxAnAdslMaxAtucConnRateTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslMaxAtucConnRateTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslMaxAtucConnRateTolerance.setUnits("%")


class _ZxAnAdslMaxAturConnRateTolerance_Type(Integer32):
    """Custom type zxAnAdslMaxAturConnRateTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnAdslMaxAturConnRateTolerance_Type.__name__ = "Integer32"
_ZxAnAdslMaxAturConnRateTolerance_Object = MibTableColumn
zxAnAdslMaxAturConnRateTolerance = _ZxAnAdslMaxAturConnRateTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 6),
    _ZxAnAdslMaxAturConnRateTolerance_Type()
)
zxAnAdslMaxAturConnRateTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslMaxAturConnRateTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslMaxAturConnRateTolerance.setUnits("%")


class _ZxAnAdslMaxThreshAtucConnRate_Type(Integer32):
    """Custom type zxAnAdslMaxThreshAtucConnRate based on Integer32"""
    defaultValue = 0


_ZxAnAdslMaxThreshAtucConnRate_Type.__name__ = "Integer32"
_ZxAnAdslMaxThreshAtucConnRate_Object = MibTableColumn
zxAnAdslMaxThreshAtucConnRate = _ZxAnAdslMaxThreshAtucConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 7),
    _ZxAnAdslMaxThreshAtucConnRate_Type()
)
zxAnAdslMaxThreshAtucConnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslMaxThreshAtucConnRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslMaxThreshAtucConnRate.setUnits("kbps")


class _ZxAnAdslMaxThreshAturConnRate_Type(Integer32):
    """Custom type zxAnAdslMaxThreshAturConnRate based on Integer32"""
    defaultValue = 0


_ZxAnAdslMaxThreshAturConnRate_Type.__name__ = "Integer32"
_ZxAnAdslMaxThreshAturConnRate_Object = MibTableColumn
zxAnAdslMaxThreshAturConnRate = _ZxAnAdslMaxThreshAturConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 8),
    _ZxAnAdslMaxThreshAturConnRate_Type()
)
zxAnAdslMaxThreshAturConnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslMaxThreshAturConnRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslMaxThreshAturConnRate.setUnits("kbps")


class _ZxAnAdslAturInitFailTrapEnable_Type(Bits):
    """Custom type zxAnAdslAturInitFailTrapEnable based on Bits"""
    namedValues = NamedValues(
        *(("unused1", 0),
          ("lossOfFraming", 1),
          ("lossOfSignal", 2),
          ("lossOfPower", 3),
          ("unused2", 4),
          ("lossOfSignalQuality", 5))
    )

_ZxAnAdslAturInitFailTrapEnable_Type.__name__ = "Bits"
_ZxAnAdslAturInitFailTrapEnable_Object = MibTableColumn
zxAnAdslAturInitFailTrapEnable = _ZxAnAdslAturInitFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 9),
    _ZxAnAdslAturInitFailTrapEnable_Type()
)
zxAnAdslAturInitFailTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslAturInitFailTrapEnable.setStatus("current")


class _ZxAnAdslThreshAtucInpLeftr_Type(Integer32):
    """Custom type zxAnAdslThreshAtucInpLeftr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnAdslThreshAtucInpLeftr_Type.__name__ = "Integer32"
_ZxAnAdslThreshAtucInpLeftr_Object = MibTableColumn
zxAnAdslThreshAtucInpLeftr = _ZxAnAdslThreshAtucInpLeftr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 10),
    _ZxAnAdslThreshAtucInpLeftr_Type()
)
zxAnAdslThreshAtucInpLeftr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslThreshAtucInpLeftr.setStatus("current")


class _ZxAnAdslThreshAturInpLeftr_Type(Integer32):
    """Custom type zxAnAdslThreshAturInpLeftr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnAdslThreshAturInpLeftr_Type.__name__ = "Integer32"
_ZxAnAdslThreshAturInpLeftr_Object = MibTableColumn
zxAnAdslThreshAturInpLeftr = _ZxAnAdslThreshAturInpLeftr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 20, 1, 11),
    _ZxAnAdslThreshAturInpLeftr_Type()
)
zxAnAdslThreshAturInpLeftr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAdslThreshAturInpLeftr.setStatus("current")
_ZxAnAdslAtucPerfDataTable_Object = MibTable
zxAnAdslAtucPerfDataTable = _ZxAnAdslAtucPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 21)
)
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataTable.setStatus("current")
_ZxAnAdslAtucPerfDataEntry_Object = MibTableRow
zxAnAdslAtucPerfDataEntry = _ZxAnAdslAtucPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 21, 1)
)
zxAnAdslAtucPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataEntry.setStatus("current")
_ZxAnAdslAtucPerfDataFecs_Type = Counter32
_ZxAnAdslAtucPerfDataFecs_Object = MibTableColumn
zxAnAdslAtucPerfDataFecs = _ZxAnAdslAtucPerfDataFecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 21, 1, 1),
    _ZxAnAdslAtucPerfDataFecs_Type()
)
zxAnAdslAtucPerfDataFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataFecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataFecs.setUnits("seconds")
_ZxAnAdslAtucPerfDataCurr15Fecs_Type = Counter32
_ZxAnAdslAtucPerfDataCurr15Fecs_Object = MibTableColumn
zxAnAdslAtucPerfDataCurr15Fecs = _ZxAnAdslAtucPerfDataCurr15Fecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 21, 1, 2),
    _ZxAnAdslAtucPerfDataCurr15Fecs_Type()
)
zxAnAdslAtucPerfDataCurr15Fecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataCurr15Fecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataCurr15Fecs.setUnits("seconds")
_ZxAnAdslAtucPerfDataCurr1DayFecs_Type = Counter32
_ZxAnAdslAtucPerfDataCurr1DayFecs_Object = MibTableColumn
zxAnAdslAtucPerfDataCurr1DayFecs = _ZxAnAdslAtucPerfDataCurr1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 21, 1, 3),
    _ZxAnAdslAtucPerfDataCurr1DayFecs_Type()
)
zxAnAdslAtucPerfDataCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataCurr1DayFecs.setUnits("seconds")
_ZxAnAdslAtucPerfDataPrev1DayFecs_Type = Counter32
_ZxAnAdslAtucPerfDataPrev1DayFecs_Object = MibTableColumn
zxAnAdslAtucPerfDataPrev1DayFecs = _ZxAnAdslAtucPerfDataPrev1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 21, 1, 4),
    _ZxAnAdslAtucPerfDataPrev1DayFecs_Type()
)
zxAnAdslAtucPerfDataPrev1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataPrev1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAtucPerfDataPrev1DayFecs.setUnits("seconds")
_ZxAnAdslAturPerfDataTable_Object = MibTable
zxAnAdslAturPerfDataTable = _ZxAnAdslAturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 22)
)
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataTable.setStatus("current")
_ZxAnAdslAturPerfDataEntry_Object = MibTableRow
zxAnAdslAturPerfDataEntry = _ZxAnAdslAturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 22, 1)
)
zxAnAdslAturPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataEntry.setStatus("current")
_ZxAnAdslAturPerfDataFecs_Type = Counter32
_ZxAnAdslAturPerfDataFecs_Object = MibTableColumn
zxAnAdslAturPerfDataFecs = _ZxAnAdslAturPerfDataFecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 22, 1, 1),
    _ZxAnAdslAturPerfDataFecs_Type()
)
zxAnAdslAturPerfDataFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataFecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataFecs.setUnits("seconds")
_ZxAnAdslAturPerfDataCurr15Fecs_Type = Counter32
_ZxAnAdslAturPerfDataCurr15Fecs_Object = MibTableColumn
zxAnAdslAturPerfDataCurr15Fecs = _ZxAnAdslAturPerfDataCurr15Fecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 22, 1, 2),
    _ZxAnAdslAturPerfDataCurr15Fecs_Type()
)
zxAnAdslAturPerfDataCurr15Fecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataCurr15Fecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataCurr15Fecs.setUnits("seconds")
_ZxAnAdslAturPerfDataCurr1DayFecs_Type = Counter32
_ZxAnAdslAturPerfDataCurr1DayFecs_Object = MibTableColumn
zxAnAdslAturPerfDataCurr1DayFecs = _ZxAnAdslAturPerfDataCurr1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 22, 1, 3),
    _ZxAnAdslAturPerfDataCurr1DayFecs_Type()
)
zxAnAdslAturPerfDataCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataCurr1DayFecs.setUnits("seconds")
_ZxAnAdslAturPerfDataPrev1DayFecs_Type = Counter32
_ZxAnAdslAturPerfDataPrev1DayFecs_Object = MibTableColumn
zxAnAdslAturPerfDataPrev1DayFecs = _ZxAnAdslAturPerfDataPrev1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 22, 1, 4),
    _ZxAnAdslAturPerfDataPrev1DayFecs_Type()
)
zxAnAdslAturPerfDataPrev1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataPrev1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnAdslAturPerfDataPrev1DayFecs.setUnits("seconds")
_ZxAnAdslAtucChanPerfDataTable_Object = MibTable
zxAnAdslAtucChanPerfDataTable = _ZxAnAdslAtucChanPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23)
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanPerfDataTable.setStatus("current")
_ZxAnAdslAtucChanPerfDataEntry_Object = MibTableRow
zxAnAdslAtucChanPerfDataEntry = _ZxAnAdslAtucChanPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1)
)
zxAnAdslAtucChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanPerfDataEntry.setStatus("current")
_ZxAnAtucChanPerfCurr15RtxDtu_Type = Counter32
_ZxAnAtucChanPerfCurr15RtxDtu_Object = MibTableColumn
zxAnAtucChanPerfCurr15RtxDtu = _ZxAnAtucChanPerfCurr15RtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1, 1),
    _ZxAnAtucChanPerfCurr15RtxDtu_Type()
)
zxAnAtucChanPerfCurr15RtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtucChanPerfCurr15RtxDtu.setStatus("current")
_ZxAnAtucChanPerfCurr15RtxCDtu_Type = Counter32
_ZxAnAtucChanPerfCurr15RtxCDtu_Object = MibTableColumn
zxAnAtucChanPerfCurr15RtxCDtu = _ZxAnAtucChanPerfCurr15RtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1, 2),
    _ZxAnAtucChanPerfCurr15RtxCDtu_Type()
)
zxAnAtucChanPerfCurr15RtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtucChanPerfCurr15RtxCDtu.setStatus("current")
_ZxAnAtucChanPerfCurr15RtxUcDtu_Type = Counter32
_ZxAnAtucChanPerfCurr15RtxUcDtu_Object = MibTableColumn
zxAnAtucChanPerfCurr15RtxUcDtu = _ZxAnAtucChanPerfCurr15RtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1, 3),
    _ZxAnAtucChanPerfCurr15RtxUcDtu_Type()
)
zxAnAtucChanPerfCurr15RtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtucChanPerfCurr15RtxUcDtu.setStatus("current")
_ZxAnAtucChanPerfCurr1DRtxDtu_Type = Counter32
_ZxAnAtucChanPerfCurr1DRtxDtu_Object = MibTableColumn
zxAnAtucChanPerfCurr1DRtxDtu = _ZxAnAtucChanPerfCurr1DRtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1, 4),
    _ZxAnAtucChanPerfCurr1DRtxDtu_Type()
)
zxAnAtucChanPerfCurr1DRtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtucChanPerfCurr1DRtxDtu.setStatus("current")
_ZxAnAtucChanPerfCurr1DRtxCDtu_Type = Counter32
_ZxAnAtucChanPerfCurr1DRtxCDtu_Object = MibTableColumn
zxAnAtucChanPerfCurr1DRtxCDtu = _ZxAnAtucChanPerfCurr1DRtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1, 5),
    _ZxAnAtucChanPerfCurr1DRtxCDtu_Type()
)
zxAnAtucChanPerfCurr1DRtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtucChanPerfCurr1DRtxCDtu.setStatus("current")
_ZxAnAtucChanPerfCurr1DRtxUcDtu_Type = Counter32
_ZxAnAtucChanPerfCurr1DRtxUcDtu_Object = MibTableColumn
zxAnAtucChanPerfCurr1DRtxUcDtu = _ZxAnAtucChanPerfCurr1DRtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 23, 1, 6),
    _ZxAnAtucChanPerfCurr1DRtxUcDtu_Type()
)
zxAnAtucChanPerfCurr1DRtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtucChanPerfCurr1DRtxUcDtu.setStatus("current")
_ZxAnAdslAturChanPerfDataTable_Object = MibTable
zxAnAdslAturChanPerfDataTable = _ZxAnAdslAturChanPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24)
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanPerfDataTable.setStatus("current")
_ZxAnAdslAturChanPerfDataEntry_Object = MibTableRow
zxAnAdslAturChanPerfDataEntry = _ZxAnAdslAturChanPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1)
)
zxAnAdslAturChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanPerfDataEntry.setStatus("current")
_ZxAnAturChanPerfCurr15RtxDtu_Type = Counter32
_ZxAnAturChanPerfCurr15RtxDtu_Object = MibTableColumn
zxAnAturChanPerfCurr15RtxDtu = _ZxAnAturChanPerfCurr15RtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1, 1),
    _ZxAnAturChanPerfCurr15RtxDtu_Type()
)
zxAnAturChanPerfCurr15RtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAturChanPerfCurr15RtxDtu.setStatus("current")
_ZxAnAturChanPerfCurr15RtxCDtu_Type = Counter32
_ZxAnAturChanPerfCurr15RtxCDtu_Object = MibTableColumn
zxAnAturChanPerfCurr15RtxCDtu = _ZxAnAturChanPerfCurr15RtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1, 2),
    _ZxAnAturChanPerfCurr15RtxCDtu_Type()
)
zxAnAturChanPerfCurr15RtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAturChanPerfCurr15RtxCDtu.setStatus("current")
_ZxAnAturChanPerfCurr15RtxUcDtu_Type = Counter32
_ZxAnAturChanPerfCurr15RtxUcDtu_Object = MibTableColumn
zxAnAturChanPerfCurr15RtxUcDtu = _ZxAnAturChanPerfCurr15RtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1, 3),
    _ZxAnAturChanPerfCurr15RtxUcDtu_Type()
)
zxAnAturChanPerfCurr15RtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAturChanPerfCurr15RtxUcDtu.setStatus("current")
_ZxAnAturChanPerfCurr1DRtxDtu_Type = Counter32
_ZxAnAturChanPerfCurr1DRtxDtu_Object = MibTableColumn
zxAnAturChanPerfCurr1DRtxDtu = _ZxAnAturChanPerfCurr1DRtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1, 4),
    _ZxAnAturChanPerfCurr1DRtxDtu_Type()
)
zxAnAturChanPerfCurr1DRtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAturChanPerfCurr1DRtxDtu.setStatus("current")
_ZxAnAturChanPerfCurr1DRtxCDtu_Type = Counter32
_ZxAnAturChanPerfCurr1DRtxCDtu_Object = MibTableColumn
zxAnAturChanPerfCurr1DRtxCDtu = _ZxAnAturChanPerfCurr1DRtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1, 5),
    _ZxAnAturChanPerfCurr1DRtxCDtu_Type()
)
zxAnAturChanPerfCurr1DRtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAturChanPerfCurr1DRtxCDtu.setStatus("current")
_ZxAnAturChanPerfCurr1DRtxUcDtu_Type = Counter32
_ZxAnAturChanPerfCurr1DRtxUcDtu_Object = MibTableColumn
zxAnAturChanPerfCurr1DRtxUcDtu = _ZxAnAturChanPerfCurr1DRtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 24, 1, 6),
    _ZxAnAturChanPerfCurr1DRtxUcDtu_Type()
)
zxAnAturChanPerfCurr1DRtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAturChanPerfCurr1DRtxUcDtu.setStatus("current")
_ZxAnAdslAtucChanIntervalTable_Object = MibTable
zxAnAdslAtucChanIntervalTable = _ZxAnAdslAtucChanIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 25)
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanIntervalTable.setStatus("current")
_ZxAnAdslAtucChanIntervalEntry_Object = MibTableRow
zxAnAdslAtucChanIntervalEntry = _ZxAnAdslAtucChanIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 25, 1)
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanIntervalEntry.setStatus("current")
_ZxAnAdslAtucChanIntervalRtxDtu_Type = Counter32
_ZxAnAdslAtucChanIntervalRtxDtu_Object = MibTableColumn
zxAnAdslAtucChanIntervalRtxDtu = _ZxAnAdslAtucChanIntervalRtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 25, 1, 1),
    _ZxAnAdslAtucChanIntervalRtxDtu_Type()
)
zxAnAdslAtucChanIntervalRtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanIntervalRtxDtu.setStatus("current")
_ZxAnAdslAtucChanIntervalRtxCDtu_Type = Counter32
_ZxAnAdslAtucChanIntervalRtxCDtu_Object = MibTableColumn
zxAnAdslAtucChanIntervalRtxCDtu = _ZxAnAdslAtucChanIntervalRtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 25, 1, 2),
    _ZxAnAdslAtucChanIntervalRtxCDtu_Type()
)
zxAnAdslAtucChanIntervalRtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanIntervalRtxCDtu.setStatus("current")
_ZxAnAdslAtucChanIntervalRtxUcDtu_Type = Counter32
_ZxAnAdslAtucChanIntervalRtxUcDtu_Object = MibTableColumn
zxAnAdslAtucChanIntervalRtxUcDtu = _ZxAnAdslAtucChanIntervalRtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 25, 1, 3),
    _ZxAnAdslAtucChanIntervalRtxUcDtu_Type()
)
zxAnAdslAtucChanIntervalRtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanIntervalRtxUcDtu.setStatus("current")
_ZxAnAdslAturChanIntervalTable_Object = MibTable
zxAnAdslAturChanIntervalTable = _ZxAnAdslAturChanIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 26)
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanIntervalTable.setStatus("current")
_ZxAnAdslAturChanIntervalEntry_Object = MibTableRow
zxAnAdslAturChanIntervalEntry = _ZxAnAdslAturChanIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 26, 1)
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanIntervalEntry.setStatus("current")
_ZxAnAdslAturChanIntervalRtxDtu_Type = Counter32
_ZxAnAdslAturChanIntervalRtxDtu_Object = MibTableColumn
zxAnAdslAturChanIntervalRtxDtu = _ZxAnAdslAturChanIntervalRtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 26, 1, 1),
    _ZxAnAdslAturChanIntervalRtxDtu_Type()
)
zxAnAdslAturChanIntervalRtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanIntervalRtxDtu.setStatus("current")
_ZxAnAdslAturChanIntervalRtxCDtu_Type = Counter32
_ZxAnAdslAturChanIntervalRtxCDtu_Object = MibTableColumn
zxAnAdslAturChanIntervalRtxCDtu = _ZxAnAdslAturChanIntervalRtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 26, 1, 2),
    _ZxAnAdslAturChanIntervalRtxCDtu_Type()
)
zxAnAdslAturChanIntervalRtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanIntervalRtxCDtu.setStatus("current")
_ZxAnAdslAturChanIntervalRtxUcDtu_Type = Counter32
_ZxAnAdslAturChanIntervalRtxUcDtu_Object = MibTableColumn
zxAnAdslAturChanIntervalRtxUcDtu = _ZxAnAdslAturChanIntervalRtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 26, 1, 3),
    _ZxAnAdslAturChanIntervalRtxUcDtu_Type()
)
zxAnAdslAturChanIntervalRtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanIntervalRtxUcDtu.setStatus("current")
_ZxAnAdslAtucChanHist1DayTable_Object = MibTable
zxAnAdslAtucChanHist1DayTable = _ZxAnAdslAtucChanHist1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 27)
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanHist1DayTable.setStatus("current")
_ZxAnAdslAtucChanHist1DayEntry_Object = MibTableRow
zxAnAdslAtucChanHist1DayEntry = _ZxAnAdslAtucChanHist1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 27, 1)
)
zxAnAdslAtucChanHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAtucChanHist1DayNumber"),
)
if mibBuilder.loadTexts:
    zxAnAdslAtucChanHist1DayEntry.setStatus("current")


class _ZxAnAdslAtucChanHist1DayNumber_Type(Integer32):
    """Custom type zxAnAdslAtucChanHist1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ZxAnAdslAtucChanHist1DayNumber_Type.__name__ = "Integer32"
_ZxAnAdslAtucChanHist1DayNumber_Object = MibTableColumn
zxAnAdslAtucChanHist1DayNumber = _ZxAnAdslAtucChanHist1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 27, 1, 1),
    _ZxAnAdslAtucChanHist1DayNumber_Type()
)
zxAnAdslAtucChanHist1DayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanHist1DayNumber.setStatus("current")
_ZxAnAdslAtucChanHist1DayRtxDtu_Type = Counter32
_ZxAnAdslAtucChanHist1DayRtxDtu_Object = MibTableColumn
zxAnAdslAtucChanHist1DayRtxDtu = _ZxAnAdslAtucChanHist1DayRtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 27, 1, 2),
    _ZxAnAdslAtucChanHist1DayRtxDtu_Type()
)
zxAnAdslAtucChanHist1DayRtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanHist1DayRtxDtu.setStatus("current")
_ZxAnAdslAtucChanHist1DayRtxCDtu_Type = Counter32
_ZxAnAdslAtucChanHist1DayRtxCDtu_Object = MibTableColumn
zxAnAdslAtucChanHist1DayRtxCDtu = _ZxAnAdslAtucChanHist1DayRtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 27, 1, 3),
    _ZxAnAdslAtucChanHist1DayRtxCDtu_Type()
)
zxAnAdslAtucChanHist1DayRtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanHist1DayRtxCDtu.setStatus("current")
_ZxAnAdslAtucChanHist1DayRtxUcDtu_Type = Counter32
_ZxAnAdslAtucChanHist1DayRtxUcDtu_Object = MibTableColumn
zxAnAdslAtucChanHist1DayRtxUcDtu = _ZxAnAdslAtucChanHist1DayRtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 27, 1, 4),
    _ZxAnAdslAtucChanHist1DayRtxUcDtu_Type()
)
zxAnAdslAtucChanHist1DayRtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAtucChanHist1DayRtxUcDtu.setStatus("current")
_ZxAnAdslAturChanHist1DayTable_Object = MibTable
zxAnAdslAturChanHist1DayTable = _ZxAnAdslAturChanHist1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 28)
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanHist1DayTable.setStatus("current")
_ZxAnAdslAturChanHist1DayEntry_Object = MibTableRow
zxAnAdslAturChanHist1DayEntry = _ZxAnAdslAturChanHist1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 28, 1)
)
zxAnAdslAturChanHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAturChanHist1DayNumber"),
)
if mibBuilder.loadTexts:
    zxAnAdslAturChanHist1DayEntry.setStatus("current")


class _ZxAnAdslAturChanHist1DayNumber_Type(Integer32):
    """Custom type zxAnAdslAturChanHist1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ZxAnAdslAturChanHist1DayNumber_Type.__name__ = "Integer32"
_ZxAnAdslAturChanHist1DayNumber_Object = MibTableColumn
zxAnAdslAturChanHist1DayNumber = _ZxAnAdslAturChanHist1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 28, 1, 1),
    _ZxAnAdslAturChanHist1DayNumber_Type()
)
zxAnAdslAturChanHist1DayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAdslAturChanHist1DayNumber.setStatus("current")
_ZxAnAdslAturChanHist1DayRtxDtu_Type = Counter32
_ZxAnAdslAturChanHist1DayRtxDtu_Object = MibTableColumn
zxAnAdslAturChanHist1DayRtxDtu = _ZxAnAdslAturChanHist1DayRtxDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 28, 1, 2),
    _ZxAnAdslAturChanHist1DayRtxDtu_Type()
)
zxAnAdslAturChanHist1DayRtxDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanHist1DayRtxDtu.setStatus("current")
_ZxAnAdslAturChanHist1DayRtxCDtu_Type = Counter32
_ZxAnAdslAturChanHist1DayRtxCDtu_Object = MibTableColumn
zxAnAdslAturChanHist1DayRtxCDtu = _ZxAnAdslAturChanHist1DayRtxCDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 28, 1, 3),
    _ZxAnAdslAturChanHist1DayRtxCDtu_Type()
)
zxAnAdslAturChanHist1DayRtxCDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanHist1DayRtxCDtu.setStatus("current")
_ZxAnAdslAturChanHist1DayRtxUcDtu_Type = Counter32
_ZxAnAdslAturChanHist1DayRtxUcDtu_Object = MibTableColumn
zxAnAdslAturChanHist1DayRtxUcDtu = _ZxAnAdslAturChanHist1DayRtxUcDtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 28, 1, 4),
    _ZxAnAdslAturChanHist1DayRtxUcDtu_Type()
)
zxAnAdslAturChanHist1DayRtxUcDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAdslAturChanHist1DayRtxUcDtu.setStatus("current")
_ZxAnDslLoopBackTestTable_Object = MibTable
zxAnDslLoopBackTestTable = _ZxAnDslLoopBackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30)
)
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestTable.setStatus("current")
_ZxAnDslLoopBackTestEntry_Object = MibTableRow
zxAnDslLoopBackTestEntry = _ZxAnDslLoopBackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1)
)
zxAnDslLoopBackTestEntry.setIndexNames(
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnDslLoopBackTestRack"),
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnDslLoopBackTestShelf"),
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnDslLoopBackTestSlot"),
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnDslLoopBackTestPort"),
    (0, "ZTE-AN-ADSL-LINE-MIB", "zxAnDslLoopBackTestBridgePort"),
)
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestEntry.setStatus("current")
_ZxAnDslLoopBackTestRack_Type = Integer32
_ZxAnDslLoopBackTestRack_Object = MibTableColumn
zxAnDslLoopBackTestRack = _ZxAnDslLoopBackTestRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 1),
    _ZxAnDslLoopBackTestRack_Type()
)
zxAnDslLoopBackTestRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestRack.setStatus("current")
_ZxAnDslLoopBackTestShelf_Type = Integer32
_ZxAnDslLoopBackTestShelf_Object = MibTableColumn
zxAnDslLoopBackTestShelf = _ZxAnDslLoopBackTestShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 2),
    _ZxAnDslLoopBackTestShelf_Type()
)
zxAnDslLoopBackTestShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestShelf.setStatus("current")
_ZxAnDslLoopBackTestSlot_Type = Integer32
_ZxAnDslLoopBackTestSlot_Object = MibTableColumn
zxAnDslLoopBackTestSlot = _ZxAnDslLoopBackTestSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 3),
    _ZxAnDslLoopBackTestSlot_Type()
)
zxAnDslLoopBackTestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestSlot.setStatus("current")
_ZxAnDslLoopBackTestPort_Type = Integer32
_ZxAnDslLoopBackTestPort_Object = MibTableColumn
zxAnDslLoopBackTestPort = _ZxAnDslLoopBackTestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 4),
    _ZxAnDslLoopBackTestPort_Type()
)
zxAnDslLoopBackTestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestPort.setStatus("current")
_ZxAnDslLoopBackTestBridgePort_Type = Integer32
_ZxAnDslLoopBackTestBridgePort_Object = MibTableColumn
zxAnDslLoopBackTestBridgePort = _ZxAnDslLoopBackTestBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 5),
    _ZxAnDslLoopBackTestBridgePort_Type()
)
zxAnDslLoopBackTestBridgePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestBridgePort.setStatus("current")


class _ZxAnDslLoopBackTestType_Type(Integer32):
    """Custom type zxAnDslLoopBackTestType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 0),
          ("cancle", 1),
          ("utopia", 2),
          ("afe", 3),
          ("hybrid", 4),
          ("xTUC_OAM", 5),
          ("xTUR_OAM", 6),
          ("xTUR_CC", 7),
          ("digital", 8))
    )


_ZxAnDslLoopBackTestType_Type.__name__ = "Integer32"
_ZxAnDslLoopBackTestType_Object = MibTableColumn
zxAnDslLoopBackTestType = _ZxAnDslLoopBackTestType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 6),
    _ZxAnDslLoopBackTestType_Type()
)
zxAnDslLoopBackTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestType.setStatus("current")


class _ZxAnDslLoopBackTestOperStatus_Type(Integer32):
    """Custom type zxAnDslLoopBackTestOperStatus based on Integer32"""
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


_ZxAnDslLoopBackTestOperStatus_Type.__name__ = "Integer32"
_ZxAnDslLoopBackTestOperStatus_Object = MibTableColumn
zxAnDslLoopBackTestOperStatus = _ZxAnDslLoopBackTestOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 7),
    _ZxAnDslLoopBackTestOperStatus_Type()
)
zxAnDslLoopBackTestOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestOperStatus.setStatus("current")


class _ZxAnDslLoopBackTestResult_Type(Integer32):
    """Custom type zxAnDslLoopBackTestResult based on Integer32"""
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
        *(("noResult", 0),
          ("success", 1),
          ("generalFailed", 2),
          ("noSupport", 3),
          ("unkown", 4),
          ("noSuchPort", 5),
          ("loopBackFailed", 6),
          ("portNotActive", 7),
          ("portInTesting", 8),
          ("portInService", 9),
          ("portFailures", 10),
          ("cardFailures", 11),
          ("noPvcFound", 12),
          ("unknownTestType", 13))
    )


_ZxAnDslLoopBackTestResult_Type.__name__ = "Integer32"
_ZxAnDslLoopBackTestResult_Object = MibTableColumn
zxAnDslLoopBackTestResult = _ZxAnDslLoopBackTestResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 8),
    _ZxAnDslLoopBackTestResult_Type()
)
zxAnDslLoopBackTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestResult.setStatus("current")
_ZxAnDslLoopBackTestConfSendCells_Type = Integer32
_ZxAnDslLoopBackTestConfSendCells_Object = MibTableColumn
zxAnDslLoopBackTestConfSendCells = _ZxAnDslLoopBackTestConfSendCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 9),
    _ZxAnDslLoopBackTestConfSendCells_Type()
)
zxAnDslLoopBackTestConfSendCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestConfSendCells.setStatus("current")
_ZxAnDslLoopBackTestResultRecivedCells_Type = Integer32
_ZxAnDslLoopBackTestResultRecivedCells_Object = MibTableColumn
zxAnDslLoopBackTestResultRecivedCells = _ZxAnDslLoopBackTestResultRecivedCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 10),
    _ZxAnDslLoopBackTestResultRecivedCells_Type()
)
zxAnDslLoopBackTestResultRecivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestResultRecivedCells.setStatus("current")
_ZxAnDslLoopBackTestRowStatus_Type = RowStatus
_ZxAnDslLoopBackTestRowStatus_Object = MibTableColumn
zxAnDslLoopBackTestRowStatus = _ZxAnDslLoopBackTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 1, 30, 1, 15),
    _ZxAnDslLoopBackTestRowStatus_Type()
)
zxAnDslLoopBackTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDslLoopBackTestRowStatus.setStatus("current")
_ZxAnAdslTraps_ObjectIdentity = ObjectIdentity
zxAnAdslTraps = _ZxAnAdslTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2)
)
adslLineConfProfileEntry.registerAugmentions(
    ("ZTE-AN-ADSL-LINE-MIB",
     "zxAnAdslLineConfProfileExtEntry")
)
zxAnAdslLineConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineAlarmConfProfileEntry.registerAugmentions(
    ("ZTE-AN-ADSL-LINE-MIB",
     "zxAnAdslLineAlarmConfProfileExtEntry")
)
zxAnAdslLineAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())
adslAtucChanIntervalEntry.registerAugmentions(
    ("ZTE-AN-ADSL-LINE-MIB",
     "zxAnAdslAtucChanIntervalEntry")
)
zxAnAdslAtucChanIntervalEntry.setIndexNames(*adslAtucChanIntervalEntry.getIndexNames())
adslAturChanIntervalEntry.registerAugmentions(
    ("ZTE-AN-ADSL-LINE-MIB",
     "zxAnAdslAturChanIntervalEntry")
)
zxAnAdslAturChanIntervalEntry.setIndexNames(*adslAturChanIntervalEntry.getIndexNames())

# Managed Objects groups


# Notification objects

zxAnAdslAtuxConnRateOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 1)
)
zxAnAdslAtuxConnRateOverThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"))
)
if mibBuilder.loadTexts:
    zxAnAdslAtuxConnRateOverThreshTrap.setStatus(
        "current"
    )

zxAnAdslAtuxConnRateUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 2)
)
zxAnAdslAtuxConnRateUnderThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"))
)
if mibBuilder.loadTexts:
    zxAnAdslAtuxConnRateUnderThreshTrap.setStatus(
        "current"
    )

zxAnAdslAtucHighConnRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 3)
)
zxAnAdslAtucHighConnRateTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxThreshAtucConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxAtucConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAtucHighConnRateTrap.setStatus(
        "current"
    )

zxAnAdslAtucHighConnRateClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 4)
)
zxAnAdslAtucHighConnRateClearTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxThreshAtucConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxAtucConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAtucHighConnRateClearTrap.setStatus(
        "current"
    )

zxAnAdslAtucLowConnRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 5)
)
zxAnAdslAtucLowConnRateTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAtucThreshConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAtucConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAtucLowConnRateTrap.setStatus(
        "current"
    )

zxAnAdslAtucLowConnRateClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 6)
)
zxAnAdslAtucLowConnRateClearTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAtucThreshConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAtucConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAtucLowConnRateClearTrap.setStatus(
        "current"
    )

zxAnAdslAturHighConnRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 7)
)
zxAnAdslAturHighConnRateTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxThreshAturConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxAturConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAturHighConnRateTrap.setStatus(
        "current"
    )

zxAnAdslAturHighConnRateClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 8)
)
zxAnAdslAturHighConnRateClearTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxThreshAturConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslMaxAturConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAturHighConnRateClearTrap.setStatus(
        "current"
    )

zxAnAdslAturLowConnRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 9)
)
zxAnAdslAturLowConnRateTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAturThreshConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAturConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAturLowConnRateTrap.setStatus(
        "current"
    )

zxAnAdslAturLowConnRateClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1000, 2, 10)
)
zxAnAdslAturLowConnRateClearTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAturThreshConnRate"),
        ("ZTE-AN-ADSL-LINE-MIB", "zxAnAdslAturConnRateTolerance"))
)
if mibBuilder.loadTexts:
    zxAnAdslAturLowConnRateClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ADSL-LINE-MIB",
    **{"zxAnAdslMib": zxAnAdslMib,
       "zxAnAdslMibObjects": zxAnAdslMibObjects,
       "zxAnAdslLineTable": zxAnAdslLineTable,
       "zxAnAdslLineEntry": zxAnAdslLineEntry,
       "zxAnAdslLineTxDataRate": zxAnAdslLineTxDataRate,
       "zxAnAdslLineRxDataRate": zxAnAdslLineRxDataRate,
       "zxAnAdslAtucActInp": zxAnAdslAtucActInp,
       "zxAnAdslAturActInp": zxAnAdslAturActInp,
       "zxAnAdslLineExtConfPrf": zxAnAdslLineExtConfPrf,
       "zxAnAdslLineConfProfileExtTable": zxAnAdslLineConfProfileExtTable,
       "zxAnAdslLineConfProfileExtEntry": zxAnAdslLineConfProfileExtEntry,
       "zxAnAdslLineConfTxStartBin": zxAnAdslLineConfTxStartBin,
       "zxAnAdslLineConfTxEndBin": zxAnAdslLineConfTxEndBin,
       "zxAnAdslLineConfRxStartBin": zxAnAdslLineConfRxStartBin,
       "zxAnAdslLineConfRxEndBin": zxAnAdslLineConfRxEndBin,
       "zxAnAdslLineConfUseCustomBins": zxAnAdslLineConfUseCustomBins,
       "zxAnAdslAtucConfPsdMaskType": zxAnAdslAtucConfPsdMaskType,
       "zxAnAdslLineConfPMMode": zxAnAdslLineConfPMMode,
       "zxAnAdslLineConfPML2Rate": zxAnAdslLineConfPML2Rate,
       "zxAnAdsl2ConfMinProtectionDs": zxAnAdsl2ConfMinProtectionDs,
       "zxAnAdslLineConfMinProtectionUs": zxAnAdslLineConfMinProtectionUs,
       "zxAnAdslConfDMTConfTrellis": zxAnAdslConfDMTConfTrellis,
       "zxAnAdslAtucConfMaxBitsPerBin": zxAnAdslAtucConfMaxBitsPerBin,
       "zxAnAdslAtucConfBitSwapDs": zxAnAdslAtucConfBitSwapDs,
       "zxAnAdslAtucConfBitSwapUs": zxAnAdslAtucConfBitSwapUs,
       "zxAnAdslAtucConfReAdsl2Enable": zxAnAdslAtucConfReAdsl2Enable,
       "zxAnAdslAtucConfPmL0Time": zxAnAdslAtucConfPmL0Time,
       "zxAnAdslAtucConfPmL2Time": zxAnAdslAtucConfPmL2Time,
       "zxAnAdslAtucConfPmL2Atpr": zxAnAdslAtucConfPmL2Atpr,
       "zxAdsl2ConfPsdMaskSelectUs": zxAdsl2ConfPsdMaskSelectUs,
       "zxAnAdslAtucChanTable": zxAnAdslAtucChanTable,
       "zxAnAdslAtucChanEntry": zxAnAdslAtucChanEntry,
       "zxAnAdslAtucChanInpEtr": zxAnAdslAtucChanInpEtr,
       "zxAnAdslAtucChanInpEftr": zxAnAdslAtucChanInpEftr,
       "zxAnAdslAtucChanInpMinEftr": zxAnAdslAtucChanInpMinEftr,
       "zxAnAdslAtucChanInpActDelay": zxAnAdslAtucChanInpActDelay,
       "zxAnAdslAturChanTable": zxAnAdslAturChanTable,
       "zxAnAdslAturChanEntry": zxAnAdslAturChanEntry,
       "zxAnAdslAturChanInpEtr": zxAnAdslAturChanInpEtr,
       "zxAnAdslAturChanInpEftr": zxAnAdslAturChanInpEftr,
       "zxAnAdslAturChanInpMinEftr": zxAnAdslAturChanInpMinEftr,
       "zxAnAdslAturChanInpActDelay": zxAnAdslAturChanInpActDelay,
       "zxAnAdslLineAlarmConfProfileExtTable": zxAnAdslLineAlarmConfProfileExtTable,
       "zxAnAdslLineAlarmConfProfileExtEntry": zxAnAdslLineAlarmConfProfileExtEntry,
       "zxAnAdslAtucConnRateTolerance": zxAnAdslAtucConnRateTolerance,
       "zxAnAdslAturConnRateTolerance": zxAnAdslAturConnRateTolerance,
       "zxAnAdslAtucThreshConnRate": zxAnAdslAtucThreshConnRate,
       "zxAnAdslAturThreshConnRate": zxAnAdslAturThreshConnRate,
       "zxAnAdslMaxAtucConnRateTolerance": zxAnAdslMaxAtucConnRateTolerance,
       "zxAnAdslMaxAturConnRateTolerance": zxAnAdslMaxAturConnRateTolerance,
       "zxAnAdslMaxThreshAtucConnRate": zxAnAdslMaxThreshAtucConnRate,
       "zxAnAdslMaxThreshAturConnRate": zxAnAdslMaxThreshAturConnRate,
       "zxAnAdslAturInitFailTrapEnable": zxAnAdslAturInitFailTrapEnable,
       "zxAnAdslThreshAtucInpLeftr": zxAnAdslThreshAtucInpLeftr,
       "zxAnAdslThreshAturInpLeftr": zxAnAdslThreshAturInpLeftr,
       "zxAnAdslAtucPerfDataTable": zxAnAdslAtucPerfDataTable,
       "zxAnAdslAtucPerfDataEntry": zxAnAdslAtucPerfDataEntry,
       "zxAnAdslAtucPerfDataFecs": zxAnAdslAtucPerfDataFecs,
       "zxAnAdslAtucPerfDataCurr15Fecs": zxAnAdslAtucPerfDataCurr15Fecs,
       "zxAnAdslAtucPerfDataCurr1DayFecs": zxAnAdslAtucPerfDataCurr1DayFecs,
       "zxAnAdslAtucPerfDataPrev1DayFecs": zxAnAdslAtucPerfDataPrev1DayFecs,
       "zxAnAdslAturPerfDataTable": zxAnAdslAturPerfDataTable,
       "zxAnAdslAturPerfDataEntry": zxAnAdslAturPerfDataEntry,
       "zxAnAdslAturPerfDataFecs": zxAnAdslAturPerfDataFecs,
       "zxAnAdslAturPerfDataCurr15Fecs": zxAnAdslAturPerfDataCurr15Fecs,
       "zxAnAdslAturPerfDataCurr1DayFecs": zxAnAdslAturPerfDataCurr1DayFecs,
       "zxAnAdslAturPerfDataPrev1DayFecs": zxAnAdslAturPerfDataPrev1DayFecs,
       "zxAnAdslAtucChanPerfDataTable": zxAnAdslAtucChanPerfDataTable,
       "zxAnAdslAtucChanPerfDataEntry": zxAnAdslAtucChanPerfDataEntry,
       "zxAnAtucChanPerfCurr15RtxDtu": zxAnAtucChanPerfCurr15RtxDtu,
       "zxAnAtucChanPerfCurr15RtxCDtu": zxAnAtucChanPerfCurr15RtxCDtu,
       "zxAnAtucChanPerfCurr15RtxUcDtu": zxAnAtucChanPerfCurr15RtxUcDtu,
       "zxAnAtucChanPerfCurr1DRtxDtu": zxAnAtucChanPerfCurr1DRtxDtu,
       "zxAnAtucChanPerfCurr1DRtxCDtu": zxAnAtucChanPerfCurr1DRtxCDtu,
       "zxAnAtucChanPerfCurr1DRtxUcDtu": zxAnAtucChanPerfCurr1DRtxUcDtu,
       "zxAnAdslAturChanPerfDataTable": zxAnAdslAturChanPerfDataTable,
       "zxAnAdslAturChanPerfDataEntry": zxAnAdslAturChanPerfDataEntry,
       "zxAnAturChanPerfCurr15RtxDtu": zxAnAturChanPerfCurr15RtxDtu,
       "zxAnAturChanPerfCurr15RtxCDtu": zxAnAturChanPerfCurr15RtxCDtu,
       "zxAnAturChanPerfCurr15RtxUcDtu": zxAnAturChanPerfCurr15RtxUcDtu,
       "zxAnAturChanPerfCurr1DRtxDtu": zxAnAturChanPerfCurr1DRtxDtu,
       "zxAnAturChanPerfCurr1DRtxCDtu": zxAnAturChanPerfCurr1DRtxCDtu,
       "zxAnAturChanPerfCurr1DRtxUcDtu": zxAnAturChanPerfCurr1DRtxUcDtu,
       "zxAnAdslAtucChanIntervalTable": zxAnAdslAtucChanIntervalTable,
       "zxAnAdslAtucChanIntervalEntry": zxAnAdslAtucChanIntervalEntry,
       "zxAnAdslAtucChanIntervalRtxDtu": zxAnAdslAtucChanIntervalRtxDtu,
       "zxAnAdslAtucChanIntervalRtxCDtu": zxAnAdslAtucChanIntervalRtxCDtu,
       "zxAnAdslAtucChanIntervalRtxUcDtu": zxAnAdslAtucChanIntervalRtxUcDtu,
       "zxAnAdslAturChanIntervalTable": zxAnAdslAturChanIntervalTable,
       "zxAnAdslAturChanIntervalEntry": zxAnAdslAturChanIntervalEntry,
       "zxAnAdslAturChanIntervalRtxDtu": zxAnAdslAturChanIntervalRtxDtu,
       "zxAnAdslAturChanIntervalRtxCDtu": zxAnAdslAturChanIntervalRtxCDtu,
       "zxAnAdslAturChanIntervalRtxUcDtu": zxAnAdslAturChanIntervalRtxUcDtu,
       "zxAnAdslAtucChanHist1DayTable": zxAnAdslAtucChanHist1DayTable,
       "zxAnAdslAtucChanHist1DayEntry": zxAnAdslAtucChanHist1DayEntry,
       "zxAnAdslAtucChanHist1DayNumber": zxAnAdslAtucChanHist1DayNumber,
       "zxAnAdslAtucChanHist1DayRtxDtu": zxAnAdslAtucChanHist1DayRtxDtu,
       "zxAnAdslAtucChanHist1DayRtxCDtu": zxAnAdslAtucChanHist1DayRtxCDtu,
       "zxAnAdslAtucChanHist1DayRtxUcDtu": zxAnAdslAtucChanHist1DayRtxUcDtu,
       "zxAnAdslAturChanHist1DayTable": zxAnAdslAturChanHist1DayTable,
       "zxAnAdslAturChanHist1DayEntry": zxAnAdslAturChanHist1DayEntry,
       "zxAnAdslAturChanHist1DayNumber": zxAnAdslAturChanHist1DayNumber,
       "zxAnAdslAturChanHist1DayRtxDtu": zxAnAdslAturChanHist1DayRtxDtu,
       "zxAnAdslAturChanHist1DayRtxCDtu": zxAnAdslAturChanHist1DayRtxCDtu,
       "zxAnAdslAturChanHist1DayRtxUcDtu": zxAnAdslAturChanHist1DayRtxUcDtu,
       "zxAnDslLoopBackTestTable": zxAnDslLoopBackTestTable,
       "zxAnDslLoopBackTestEntry": zxAnDslLoopBackTestEntry,
       "zxAnDslLoopBackTestRack": zxAnDslLoopBackTestRack,
       "zxAnDslLoopBackTestShelf": zxAnDslLoopBackTestShelf,
       "zxAnDslLoopBackTestSlot": zxAnDslLoopBackTestSlot,
       "zxAnDslLoopBackTestPort": zxAnDslLoopBackTestPort,
       "zxAnDslLoopBackTestBridgePort": zxAnDslLoopBackTestBridgePort,
       "zxAnDslLoopBackTestType": zxAnDslLoopBackTestType,
       "zxAnDslLoopBackTestOperStatus": zxAnDslLoopBackTestOperStatus,
       "zxAnDslLoopBackTestResult": zxAnDslLoopBackTestResult,
       "zxAnDslLoopBackTestConfSendCells": zxAnDslLoopBackTestConfSendCells,
       "zxAnDslLoopBackTestResultRecivedCells": zxAnDslLoopBackTestResultRecivedCells,
       "zxAnDslLoopBackTestRowStatus": zxAnDslLoopBackTestRowStatus,
       "zxAnAdslTraps": zxAnAdslTraps,
       "zxAnAdslAtuxConnRateOverThreshTrap": zxAnAdslAtuxConnRateOverThreshTrap,
       "zxAnAdslAtuxConnRateUnderThreshTrap": zxAnAdslAtuxConnRateUnderThreshTrap,
       "zxAnAdslAtucHighConnRateTrap": zxAnAdslAtucHighConnRateTrap,
       "zxAnAdslAtucHighConnRateClearTrap": zxAnAdslAtucHighConnRateClearTrap,
       "zxAnAdslAtucLowConnRateTrap": zxAnAdslAtucLowConnRateTrap,
       "zxAnAdslAtucLowConnRateClearTrap": zxAnAdslAtucLowConnRateClearTrap,
       "zxAnAdslAturHighConnRateTrap": zxAnAdslAturHighConnRateTrap,
       "zxAnAdslAturHighConnRateClearTrap": zxAnAdslAturHighConnRateClearTrap,
       "zxAnAdslAturLowConnRateTrap": zxAnAdslAturLowConnRateTrap,
       "zxAnAdslAturLowConnRateClearTrap": zxAnAdslAturLowConnRateClearTrap}
)
