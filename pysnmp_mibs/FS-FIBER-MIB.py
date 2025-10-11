# SNMP MIB module (FS-FIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-FIBER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:35 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsFiberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105)
)
if mibBuilder.loadTexts:
    fsFiberMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsFiberMIBObjects_ObjectIdentity = ObjectIdentity
fsFiberMIBObjects = _FsFiberMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1)
)
_FsFiberTable_Object = MibTable
fsFiberTable = _FsFiberTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1)
)
if mibBuilder.loadTexts:
    fsFiberTable.setStatus("current")
_FsFiberEntry_Object = MibTableRow
fsFiberEntry = _FsFiberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1)
)
fsFiberEntry.setIndexNames(
    (0, "FS-FIBER-MIB", "fsFiberPortIndex"),
)
if mibBuilder.loadTexts:
    fsFiberEntry.setStatus("current")
_FsFiberPortIndex_Type = IfIndex
_FsFiberPortIndex_Object = MibTableColumn
fsFiberPortIndex = _FsFiberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 1),
    _FsFiberPortIndex_Type()
)
fsFiberPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsFiberPortIndex.setStatus("current")


class _FsFiberPortDescr_Type(DisplayString):
    """Custom type fsFiberPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsFiberPortDescr_Type.__name__ = "DisplayString"
_FsFiberPortDescr_Object = MibTableColumn
fsFiberPortDescr = _FsFiberPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 2),
    _FsFiberPortDescr_Type()
)
fsFiberPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberPortDescr.setStatus("current")


class _FsFiberTransceiverType_Type(Integer32):
    """Custom type fsFiberTransceiverType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fiber100BASEGTSFP", 2),
          ("fiber100BASESXSFP", 3),
          ("fiber100BASELXSFP", 4),
          ("fiber100BASELHSFP", 5),
          ("fiber100BASEZXSFP", 6),
          ("fiber100CopperSFP", 7),
          ("fiber1000BASEGTSFP", 8),
          ("fiber1000BASESXSFP", 9),
          ("fiber1000BASELXSFP", 10),
          ("fiber1000BASELHSFP", 11),
          ("fiber1000BASEZXSFP", 12),
          ("fiber1000CopperSFP", 13),
          ("fiber10GCopperSFPPlus", 14),
          ("fiber10GBASESRSFPPlus", 15),
          ("fiber10GBASELRSFPPlus", 16),
          ("fiber10GBASEERSFPPlus", 17),
          ("fiber10GBASEZRSFPPlus", 18),
          ("fiber10GCopperXFP", 19),
          ("fiber10GBASESRXFP", 20),
          ("fiber10GBASELRXFP", 21),
          ("fiber10GBASEERXFP", 22),
          ("fiber10GBASEZRXFP", 23),
          ("fiber40GActiveCableQSFPPlus", 24),
          ("fiber40GLR4QSFPPlus", 25),
          ("fiber40GCopperQSFPPlus", 26),
          ("fiber40GSR4QSFPPlus", 27),
          ("fiber2500CopperSFP", 28),
          ("fiberFC16G", 29),
          ("fiberFC8G", 30),
          ("fiberFC4G", 31),
          ("fiberFC2G", 32),
          ("fiber10GActiveCableSFPPlus", 33),
          ("fiber40GER4QSFPPlus", 34),
          ("fiber40GZR4QSFPPlus", 35),
          ("fiber100GCABLEQSFP28", 36),
          ("fiber100GLR4QSFP28", 37),
          ("fiber100GSR4QSFP28", 38),
          ("fiber100GER4QSFP28", 39),
          ("fiber100GZR4QSFP28", 40),
          ("fiber100GCR4QSFP28", 41),
          ("fiber100GPSM4QSFP28", 42),
          ("fiber25GSRSFP28", 43),
          ("fiber25GLRSFP28", 44),
          ("fiber25GERSFP28", 45),
          ("fiber25GZRSFP28", 46),
          ("fiber25GCOPPERSFP28", 47),
          ("fiber25GACTIVECABLESFP28", 48),
          ("fiber100GiLR4QSFP28", 49))
    )


_FsFiberTransceiverType_Type.__name__ = "Integer32"
_FsFiberTransceiverType_Object = MibTableColumn
fsFiberTransceiverType = _FsFiberTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 3),
    _FsFiberTransceiverType_Type()
)
fsFiberTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransceiverType.setStatus("current")


class _FsFiberConnectorType_Type(Integer32):
    """Custom type fsFiberConnectorType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("meaningless", 0),
          ("unknownorunspecified", 1),
          ("vendorspecific", 2),
          ("sc", 3),
          ("fiberChannelStyle1CopperConnector", 4),
          ("fiberChannelStyle2CopperConnector", 5),
          ("bncortnc", 6),
          ("fiberChannelCoaxialHeaders", 7),
          ("fiberJack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalPigtail", 13),
          ("hssdcII", 14),
          ("copperPigtail", 15),
          ("mpo", 16),
          ("rj45", 17),
          ("noSparableConnector", 18))
    )


_FsFiberConnectorType_Type.__name__ = "Integer32"
_FsFiberConnectorType_Object = MibTableColumn
fsFiberConnectorType = _FsFiberConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 4),
    _FsFiberConnectorType_Type()
)
fsFiberConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberConnectorType.setStatus("current")
_FsFiberWavelength_Type = Integer32
_FsFiberWavelength_Object = MibTableColumn
fsFiberWavelength = _FsFiberWavelength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 5),
    _FsFiberWavelength_Type()
)
fsFiberWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberWavelength.setStatus("current")
_FsFiberTransferDistanceSMF_Type = Integer32
_FsFiberTransferDistanceSMF_Object = MibTableColumn
fsFiberTransferDistanceSMF = _FsFiberTransferDistanceSMF_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 6),
    _FsFiberTransferDistanceSMF_Type()
)
fsFiberTransferDistanceSMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceSMF.setStatus("current")
_FsFiberTransferDistance62point5umOM1_Type = Integer32
_FsFiberTransferDistance62point5umOM1_Object = MibTableColumn
fsFiberTransferDistance62point5umOM1 = _FsFiberTransferDistance62point5umOM1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 7),
    _FsFiberTransferDistance62point5umOM1_Type()
)
fsFiberTransferDistance62point5umOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance62point5umOM1.setStatus("current")
_FsFiberTransferDistance62point5um_Type = Integer32
_FsFiberTransferDistance62point5um_Object = MibTableColumn
fsFiberTransferDistance62point5um = _FsFiberTransferDistance62point5um_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 8),
    _FsFiberTransferDistance62point5um_Type()
)
fsFiberTransferDistance62point5um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance62point5um.setStatus("current")
_FsFiberTransferDistance50umOM2_Type = Integer32
_FsFiberTransferDistance50umOM2_Object = MibTableColumn
fsFiberTransferDistance50umOM2 = _FsFiberTransferDistance50umOM2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 9),
    _FsFiberTransferDistance50umOM2_Type()
)
fsFiberTransferDistance50umOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50umOM2.setStatus("current")
_FsFiberTransferDistance50um_Type = Integer32
_FsFiberTransferDistance50um_Object = MibTableColumn
fsFiberTransferDistance50um = _FsFiberTransferDistance50um_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 10),
    _FsFiberTransferDistance50um_Type()
)
fsFiberTransferDistance50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50um.setStatus("current")
_FsFiberTransferDistance50umOM3_Type = Integer32
_FsFiberTransferDistance50umOM3_Object = MibTableColumn
fsFiberTransferDistance50umOM3 = _FsFiberTransferDistance50umOM3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 11),
    _FsFiberTransferDistance50umOM3_Type()
)
fsFiberTransferDistance50umOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistance50umOM3.setStatus("current")
_FsFiberTransferDistanceEBW50um_Type = Integer32
_FsFiberTransferDistanceEBW50um_Object = MibTableColumn
fsFiberTransferDistanceEBW50um = _FsFiberTransferDistanceEBW50um_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 12),
    _FsFiberTransferDistanceEBW50um_Type()
)
fsFiberTransferDistanceEBW50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceEBW50um.setStatus("current")
_FsFiberTransferDistanceCopper_Type = Integer32
_FsFiberTransferDistanceCopper_Object = MibTableColumn
fsFiberTransferDistanceCopper = _FsFiberTransferDistanceCopper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 13),
    _FsFiberTransferDistanceCopper_Type()
)
fsFiberTransferDistanceCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceCopper.setStatus("current")
_FsFiberTransferDistanceCableAssembly_Type = Integer32
_FsFiberTransferDistanceCableAssembly_Object = MibTableColumn
fsFiberTransferDistanceCableAssembly = _FsFiberTransferDistanceCableAssembly_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 14),
    _FsFiberTransferDistanceCableAssembly_Type()
)
fsFiberTransferDistanceCableAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTransferDistanceCableAssembly.setStatus("current")
_FsFiberDDMSupportStatus_Type = TruthValue
_FsFiberDDMSupportStatus_Object = MibTableColumn
fsFiberDDMSupportStatus = _FsFiberDDMSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 15),
    _FsFiberDDMSupportStatus_Type()
)
fsFiberDDMSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberDDMSupportStatus.setStatus("current")


class _FsFiberSerialNumber_Type(DisplayString):
    """Custom type fsFiberSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsFiberSerialNumber_Type.__name__ = "DisplayString"
_FsFiberSerialNumber_Object = MibTableColumn
fsFiberSerialNumber = _FsFiberSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 16),
    _FsFiberSerialNumber_Type()
)
fsFiberSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberSerialNumber.setStatus("current")
_FsFiberTemp_Type = Integer32
_FsFiberTemp_Object = MibTableColumn
fsFiberTemp = _FsFiberTemp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 17),
    _FsFiberTemp_Type()
)
fsFiberTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTemp.setStatus("current")


class _FsFiberTempStatus_Type(Integer32):
    """Custom type fsFiberTempStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberTempStatus_Type.__name__ = "Integer32"
_FsFiberTempStatus_Object = MibTableColumn
fsFiberTempStatus = _FsFiberTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 18),
    _FsFiberTempStatus_Type()
)
fsFiberTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTempStatus.setStatus("current")
_FsFiberVoltage_Type = Integer32
_FsFiberVoltage_Object = MibTableColumn
fsFiberVoltage = _FsFiberVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 19),
    _FsFiberVoltage_Type()
)
fsFiberVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltage.setStatus("current")


class _FsFiberVoltageStatus_Type(Integer32):
    """Custom type fsFiberVoltageStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberVoltageStatus_Type.__name__ = "Integer32"
_FsFiberVoltageStatus_Object = MibTableColumn
fsFiberVoltageStatus = _FsFiberVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 20),
    _FsFiberVoltageStatus_Type()
)
fsFiberVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVoltageStatus.setStatus("current")
_FsFiberBias_Type = Integer32
_FsFiberBias_Object = MibTableColumn
fsFiberBias = _FsFiberBias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 21),
    _FsFiberBias_Type()
)
fsFiberBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBias.setStatus("current")


class _FsFiberBiasStatus_Type(Integer32):
    """Custom type fsFiberBiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberBiasStatus_Type.__name__ = "Integer32"
_FsFiberBiasStatus_Object = MibTableColumn
fsFiberBiasStatus = _FsFiberBiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 22),
    _FsFiberBiasStatus_Type()
)
fsFiberBiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberBiasStatus.setStatus("current")
_FsFiberChannel1Bias_Type = Integer32
_FsFiberChannel1Bias_Object = MibTableColumn
fsFiberChannel1Bias = _FsFiberChannel1Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 23),
    _FsFiberChannel1Bias_Type()
)
fsFiberChannel1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1Bias.setStatus("current")


class _FsFiberChannel1BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel1BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel1BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel1BiasStatus_Object = MibTableColumn
fsFiberChannel1BiasStatus = _FsFiberChannel1BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 24),
    _FsFiberChannel1BiasStatus_Type()
)
fsFiberChannel1BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1BiasStatus.setStatus("current")
_FsFiberChannel2Bias_Type = Integer32
_FsFiberChannel2Bias_Object = MibTableColumn
fsFiberChannel2Bias = _FsFiberChannel2Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 25),
    _FsFiberChannel2Bias_Type()
)
fsFiberChannel2Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2Bias.setStatus("current")


class _FsFiberChannel2BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel2BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel2BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel2BiasStatus_Object = MibTableColumn
fsFiberChannel2BiasStatus = _FsFiberChannel2BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 26),
    _FsFiberChannel2BiasStatus_Type()
)
fsFiberChannel2BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2BiasStatus.setStatus("current")
_FsFiberChannel3Bias_Type = Integer32
_FsFiberChannel3Bias_Object = MibTableColumn
fsFiberChannel3Bias = _FsFiberChannel3Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 27),
    _FsFiberChannel3Bias_Type()
)
fsFiberChannel3Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3Bias.setStatus("current")


class _FsFiberChannel3BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel3BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel3BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel3BiasStatus_Object = MibTableColumn
fsFiberChannel3BiasStatus = _FsFiberChannel3BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 28),
    _FsFiberChannel3BiasStatus_Type()
)
fsFiberChannel3BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3BiasStatus.setStatus("current")
_FsFiberChannel4Bias_Type = Integer32
_FsFiberChannel4Bias_Object = MibTableColumn
fsFiberChannel4Bias = _FsFiberChannel4Bias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 29),
    _FsFiberChannel4Bias_Type()
)
fsFiberChannel4Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4Bias.setStatus("current")


class _FsFiberChannel4BiasStatus_Type(Integer32):
    """Custom type fsFiberChannel4BiasStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel4BiasStatus_Type.__name__ = "Integer32"
_FsFiberChannel4BiasStatus_Object = MibTableColumn
fsFiberChannel4BiasStatus = _FsFiberChannel4BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 30),
    _FsFiberChannel4BiasStatus_Type()
)
fsFiberChannel4BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4BiasStatus.setStatus("current")
_FsFiberRXpowerIntegerpart_Type = Integer32
_FsFiberRXpowerIntegerpart_Object = MibTableColumn
fsFiberRXpowerIntegerpart = _FsFiberRXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 31),
    _FsFiberRXpowerIntegerpart_Type()
)
fsFiberRXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerIntegerpart.setStatus("current")
_FsFiberRXpowerDecimalpart_Type = Integer32
_FsFiberRXpowerDecimalpart_Object = MibTableColumn
fsFiberRXpowerDecimalpart = _FsFiberRXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 32),
    _FsFiberRXpowerDecimalpart_Type()
)
fsFiberRXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerDecimalpart.setStatus("current")


class _FsFiberRXpowertype_Type(Integer32):
    """Custom type fsFiberRXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_FsFiberRXpowertype_Type.__name__ = "Integer32"
_FsFiberRXpowertype_Object = MibTableColumn
fsFiberRXpowertype = _FsFiberRXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 33),
    _FsFiberRXpowertype_Type()
)
fsFiberRXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowertype.setStatus("current")


class _FsFiberRXpowerStatus_Type(Integer32):
    """Custom type fsFiberRXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberRXpowerStatus_Type.__name__ = "Integer32"
_FsFiberRXpowerStatus_Object = MibTableColumn
fsFiberRXpowerStatus = _FsFiberRXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 34),
    _FsFiberRXpowerStatus_Type()
)
fsFiberRXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerStatus.setStatus("current")
_FsFiberChannel1RXpowerIntegerpart_Type = Integer32
_FsFiberChannel1RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel1RXpowerIntegerpart = _FsFiberChannel1RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 35),
    _FsFiberChannel1RXpowerIntegerpart_Type()
)
fsFiberChannel1RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerIntegerpart.setStatus("current")
_FsFiberChannel1RXpowerDecimalpart_Type = Integer32
_FsFiberChannel1RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel1RXpowerDecimalpart = _FsFiberChannel1RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 36),
    _FsFiberChannel1RXpowerDecimalpart_Type()
)
fsFiberChannel1RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel1RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel1RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_FsFiberChannel1RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel1RXpowertype_Object = MibTableColumn
fsFiberChannel1RXpowertype = _FsFiberChannel1RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 37),
    _FsFiberChannel1RXpowertype_Type()
)
fsFiberChannel1RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowertype.setStatus("current")


class _FsFiberChannel1RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel1RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel1RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel1RXpowerStatus_Object = MibTableColumn
fsFiberChannel1RXpowerStatus = _FsFiberChannel1RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 38),
    _FsFiberChannel1RXpowerStatus_Type()
)
fsFiberChannel1RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerStatus.setStatus("current")
_FsFiberChannel2RXpowerIntegerpart_Type = Integer32
_FsFiberChannel2RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel2RXpowerIntegerpart = _FsFiberChannel2RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 39),
    _FsFiberChannel2RXpowerIntegerpart_Type()
)
fsFiberChannel2RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerIntegerpart.setStatus("current")
_FsFiberChannel2RXpowerDecimalpart_Type = Integer32
_FsFiberChannel2RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel2RXpowerDecimalpart = _FsFiberChannel2RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 40),
    _FsFiberChannel2RXpowerDecimalpart_Type()
)
fsFiberChannel2RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel2RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel2RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_FsFiberChannel2RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel2RXpowertype_Object = MibTableColumn
fsFiberChannel2RXpowertype = _FsFiberChannel2RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 41),
    _FsFiberChannel2RXpowertype_Type()
)
fsFiberChannel2RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowertype.setStatus("current")


class _FsFiberChannel2RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel2RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel2RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel2RXpowerStatus_Object = MibTableColumn
fsFiberChannel2RXpowerStatus = _FsFiberChannel2RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 42),
    _FsFiberChannel2RXpowerStatus_Type()
)
fsFiberChannel2RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerStatus.setStatus("current")
_FsFiberChannel3RXpowerIntegerpart_Type = Integer32
_FsFiberChannel3RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel3RXpowerIntegerpart = _FsFiberChannel3RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 43),
    _FsFiberChannel3RXpowerIntegerpart_Type()
)
fsFiberChannel3RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerIntegerpart.setStatus("current")
_FsFiberChannel3RXpowerDecimalpart_Type = Integer32
_FsFiberChannel3RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel3RXpowerDecimalpart = _FsFiberChannel3RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 44),
    _FsFiberChannel3RXpowerDecimalpart_Type()
)
fsFiberChannel3RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel3RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel3RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_FsFiberChannel3RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel3RXpowertype_Object = MibTableColumn
fsFiberChannel3RXpowertype = _FsFiberChannel3RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 45),
    _FsFiberChannel3RXpowertype_Type()
)
fsFiberChannel3RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowertype.setStatus("current")


class _FsFiberChannel3RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel3RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel3RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel3RXpowerStatus_Object = MibTableColumn
fsFiberChannel3RXpowerStatus = _FsFiberChannel3RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 46),
    _FsFiberChannel3RXpowerStatus_Type()
)
fsFiberChannel3RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerStatus.setStatus("current")
_FsFiberChannel4RXpowerIntegerpart_Type = Integer32
_FsFiberChannel4RXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel4RXpowerIntegerpart = _FsFiberChannel4RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 47),
    _FsFiberChannel4RXpowerIntegerpart_Type()
)
fsFiberChannel4RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerIntegerpart.setStatus("current")
_FsFiberChannel4RXpowerDecimalpart_Type = Integer32
_FsFiberChannel4RXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel4RXpowerDecimalpart = _FsFiberChannel4RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 48),
    _FsFiberChannel4RXpowerDecimalpart_Type()
)
fsFiberChannel4RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerDecimalpart.setStatus("current")


class _FsFiberChannel4RXpowertype_Type(Integer32):
    """Custom type fsFiberChannel4RXpowertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_FsFiberChannel4RXpowertype_Type.__name__ = "Integer32"
_FsFiberChannel4RXpowertype_Object = MibTableColumn
fsFiberChannel4RXpowertype = _FsFiberChannel4RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 49),
    _FsFiberChannel4RXpowertype_Type()
)
fsFiberChannel4RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowertype.setStatus("current")


class _FsFiberChannel4RXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel4RXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel4RXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel4RXpowerStatus_Object = MibTableColumn
fsFiberChannel4RXpowerStatus = _FsFiberChannel4RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 50),
    _FsFiberChannel4RXpowerStatus_Type()
)
fsFiberChannel4RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerStatus.setStatus("current")
_FsFiberTXpowerIntegerpart_Type = Integer32
_FsFiberTXpowerIntegerpart_Object = MibTableColumn
fsFiberTXpowerIntegerpart = _FsFiberTXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 51),
    _FsFiberTXpowerIntegerpart_Type()
)
fsFiberTXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerIntegerpart.setStatus("current")
_FsFiberTXpowerDecimalpart_Type = Integer32
_FsFiberTXpowerDecimalpart_Object = MibTableColumn
fsFiberTXpowerDecimalpart = _FsFiberTXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 52),
    _FsFiberTXpowerDecimalpart_Type()
)
fsFiberTXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerDecimalpart.setStatus("current")


class _FsFiberTXpowerStatus_Type(Integer32):
    """Custom type fsFiberTXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberTXpowerStatus_Type.__name__ = "Integer32"
_FsFiberTXpowerStatus_Object = MibTableColumn
fsFiberTXpowerStatus = _FsFiberTXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 53),
    _FsFiberTXpowerStatus_Type()
)
fsFiberTXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerStatus.setStatus("current")
_FsFiberChannel1TXpowerIntegerpart_Type = Integer32
_FsFiberChannel1TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel1TXpowerIntegerpart = _FsFiberChannel1TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 54),
    _FsFiberChannel1TXpowerIntegerpart_Type()
)
fsFiberChannel1TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerIntegerpart.setStatus("current")
_FsFiberChannel1TXpowerDecimalpart_Type = Integer32
_FsFiberChannel1TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel1TXpowerDecimalpart = _FsFiberChannel1TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 55),
    _FsFiberChannel1TXpowerDecimalpart_Type()
)
fsFiberChannel1TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel1TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel1TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel1TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel1TXpowerStatus_Object = MibTableColumn
fsFiberChannel1TXpowerStatus = _FsFiberChannel1TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 56),
    _FsFiberChannel1TXpowerStatus_Type()
)
fsFiberChannel1TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerStatus.setStatus("current")
_FsFiberChannel2TXpowerIntegerpart_Type = Integer32
_FsFiberChannel2TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel2TXpowerIntegerpart = _FsFiberChannel2TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 57),
    _FsFiberChannel2TXpowerIntegerpart_Type()
)
fsFiberChannel2TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerIntegerpart.setStatus("current")
_FsFiberChannel2TXpowerDecimalpart_Type = Integer32
_FsFiberChannel2TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel2TXpowerDecimalpart = _FsFiberChannel2TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 58),
    _FsFiberChannel2TXpowerDecimalpart_Type()
)
fsFiberChannel2TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel2TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel2TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel2TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel2TXpowerStatus_Object = MibTableColumn
fsFiberChannel2TXpowerStatus = _FsFiberChannel2TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 59),
    _FsFiberChannel2TXpowerStatus_Type()
)
fsFiberChannel2TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerStatus.setStatus("current")
_FsFiberChannel3TXpowerIntegerpart_Type = Integer32
_FsFiberChannel3TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel3TXpowerIntegerpart = _FsFiberChannel3TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 60),
    _FsFiberChannel3TXpowerIntegerpart_Type()
)
fsFiberChannel3TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerIntegerpart.setStatus("current")
_FsFiberChannel3TXpowerDecimalpart_Type = Integer32
_FsFiberChannel3TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel3TXpowerDecimalpart = _FsFiberChannel3TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 61),
    _FsFiberChannel3TXpowerDecimalpart_Type()
)
fsFiberChannel3TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel3TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel3TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel3TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel3TXpowerStatus_Object = MibTableColumn
fsFiberChannel3TXpowerStatus = _FsFiberChannel3TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 62),
    _FsFiberChannel3TXpowerStatus_Type()
)
fsFiberChannel3TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerStatus.setStatus("current")
_FsFiberChannel4TXpowerIntegerpart_Type = Integer32
_FsFiberChannel4TXpowerIntegerpart_Object = MibTableColumn
fsFiberChannel4TXpowerIntegerpart = _FsFiberChannel4TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 63),
    _FsFiberChannel4TXpowerIntegerpart_Type()
)
fsFiberChannel4TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerIntegerpart.setStatus("current")
_FsFiberChannel4TXpowerDecimalpart_Type = Integer32
_FsFiberChannel4TXpowerDecimalpart_Object = MibTableColumn
fsFiberChannel4TXpowerDecimalpart = _FsFiberChannel4TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 64),
    _FsFiberChannel4TXpowerDecimalpart_Type()
)
fsFiberChannel4TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerDecimalpart.setStatus("current")


class _FsFiberChannel4TXpowerStatus_Type(Integer32):
    """Custom type fsFiberChannel4TXpowerStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_FsFiberChannel4TXpowerStatus_Type.__name__ = "Integer32"
_FsFiberChannel4TXpowerStatus_Object = MibTableColumn
fsFiberChannel4TXpowerStatus = _FsFiberChannel4TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 65),
    _FsFiberChannel4TXpowerStatus_Type()
)
fsFiberChannel4TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerStatus.setStatus("current")
_FsFiberRXpowerSign_Type = Integer32
_FsFiberRXpowerSign_Object = MibTableColumn
fsFiberRXpowerSign = _FsFiberRXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 66),
    _FsFiberRXpowerSign_Type()
)
fsFiberRXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerSign.setStatus("current")
_FsFiberChannel1RXpowerSign_Type = Integer32
_FsFiberChannel1RXpowerSign_Object = MibTableColumn
fsFiberChannel1RXpowerSign = _FsFiberChannel1RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 67),
    _FsFiberChannel1RXpowerSign_Type()
)
fsFiberChannel1RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerSign.setStatus("current")
_FsFiberChannel2RXpowerSign_Type = Integer32
_FsFiberChannel2RXpowerSign_Object = MibTableColumn
fsFiberChannel2RXpowerSign = _FsFiberChannel2RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 68),
    _FsFiberChannel2RXpowerSign_Type()
)
fsFiberChannel2RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerSign.setStatus("current")
_FsFiberChannel3RXpowerSign_Type = Integer32
_FsFiberChannel3RXpowerSign_Object = MibTableColumn
fsFiberChannel3RXpowerSign = _FsFiberChannel3RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 69),
    _FsFiberChannel3RXpowerSign_Type()
)
fsFiberChannel3RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerSign.setStatus("current")
_FsFiberChannel4RXpowerSign_Type = Integer32
_FsFiberChannel4RXpowerSign_Object = MibTableColumn
fsFiberChannel4RXpowerSign = _FsFiberChannel4RXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 70),
    _FsFiberChannel4RXpowerSign_Type()
)
fsFiberChannel4RXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerSign.setStatus("current")
_FsFiberTXpowerSign_Type = Integer32
_FsFiberTXpowerSign_Object = MibTableColumn
fsFiberTXpowerSign = _FsFiberTXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 71),
    _FsFiberTXpowerSign_Type()
)
fsFiberTXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerSign.setStatus("current")
_FsFiberChannel1TXpowerSign_Type = Integer32
_FsFiberChannel1TXpowerSign_Object = MibTableColumn
fsFiberChannel1TXpowerSign = _FsFiberChannel1TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 72),
    _FsFiberChannel1TXpowerSign_Type()
)
fsFiberChannel1TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerSign.setStatus("current")
_FsFiberChannel2TXpowerSign_Type = Integer32
_FsFiberChannel2TXpowerSign_Object = MibTableColumn
fsFiberChannel2TXpowerSign = _FsFiberChannel2TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 73),
    _FsFiberChannel2TXpowerSign_Type()
)
fsFiberChannel2TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerSign.setStatus("current")
_FsFiberChannel3TXpowerSign_Type = Integer32
_FsFiberChannel3TXpowerSign_Object = MibTableColumn
fsFiberChannel3TXpowerSign = _FsFiberChannel3TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 74),
    _FsFiberChannel3TXpowerSign_Type()
)
fsFiberChannel3TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerSign.setStatus("current")
_FsFiberChannel4TXpowerSign_Type = Integer32
_FsFiberChannel4TXpowerSign_Object = MibTableColumn
fsFiberChannel4TXpowerSign = _FsFiberChannel4TXpowerSign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 75),
    _FsFiberChannel4TXpowerSign_Type()
)
fsFiberChannel4TXpowerSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerSign.setStatus("current")
_FsFiberRXpowerInteger_Type = Integer32
_FsFiberRXpowerInteger_Object = MibTableColumn
fsFiberRXpowerInteger = _FsFiberRXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 76),
    _FsFiberRXpowerInteger_Type()
)
fsFiberRXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberRXpowerInteger.setStatus("current")
_FsFiberChannel1RXpowerInteger_Type = Integer32
_FsFiberChannel1RXpowerInteger_Object = MibTableColumn
fsFiberChannel1RXpowerInteger = _FsFiberChannel1RXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 77),
    _FsFiberChannel1RXpowerInteger_Type()
)
fsFiberChannel1RXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1RXpowerInteger.setStatus("current")
_FsFiberChannel2RXpowerInteger_Type = Integer32
_FsFiberChannel2RXpowerInteger_Object = MibTableColumn
fsFiberChannel2RXpowerInteger = _FsFiberChannel2RXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 78),
    _FsFiberChannel2RXpowerInteger_Type()
)
fsFiberChannel2RXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2RXpowerInteger.setStatus("current")
_FsFiberChannel3RXpowerInteger_Type = Integer32
_FsFiberChannel3RXpowerInteger_Object = MibTableColumn
fsFiberChannel3RXpowerInteger = _FsFiberChannel3RXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 79),
    _FsFiberChannel3RXpowerInteger_Type()
)
fsFiberChannel3RXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3RXpowerInteger.setStatus("current")
_FsFiberChannel4RXpowerInteger_Type = Integer32
_FsFiberChannel4RXpowerInteger_Object = MibTableColumn
fsFiberChannel4RXpowerInteger = _FsFiberChannel4RXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 80),
    _FsFiberChannel4RXpowerInteger_Type()
)
fsFiberChannel4RXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4RXpowerInteger.setStatus("current")
_FsFiberTXpowerInteger_Type = Integer32
_FsFiberTXpowerInteger_Object = MibTableColumn
fsFiberTXpowerInteger = _FsFiberTXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 81),
    _FsFiberTXpowerInteger_Type()
)
fsFiberTXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberTXpowerInteger.setStatus("current")
_FsFiberChannel1TXpowerInteger_Type = Integer32
_FsFiberChannel1TXpowerInteger_Object = MibTableColumn
fsFiberChannel1TXpowerInteger = _FsFiberChannel1TXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 82),
    _FsFiberChannel1TXpowerInteger_Type()
)
fsFiberChannel1TXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel1TXpowerInteger.setStatus("current")
_FsFiberChannel2TXpowerInteger_Type = Integer32
_FsFiberChannel2TXpowerInteger_Object = MibTableColumn
fsFiberChannel2TXpowerInteger = _FsFiberChannel2TXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 83),
    _FsFiberChannel2TXpowerInteger_Type()
)
fsFiberChannel2TXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel2TXpowerInteger.setStatus("current")
_FsFiberChannel3TXpowerInteger_Type = Integer32
_FsFiberChannel3TXpowerInteger_Object = MibTableColumn
fsFiberChannel3TXpowerInteger = _FsFiberChannel3TXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 84),
    _FsFiberChannel3TXpowerInteger_Type()
)
fsFiberChannel3TXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel3TXpowerInteger.setStatus("current")
_FsFiberChannel4TXpowerInteger_Type = Integer32
_FsFiberChannel4TXpowerInteger_Object = MibTableColumn
fsFiberChannel4TXpowerInteger = _FsFiberChannel4TXpowerInteger_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 1, 1, 85),
    _FsFiberChannel4TXpowerInteger_Type()
)
fsFiberChannel4TXpowerInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberChannel4TXpowerInteger.setStatus("current")
_FsFiberVendorTable_Object = MibTable
fsFiberVendorTable = _FsFiberVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    fsFiberVendorTable.setStatus("current")
_FsFiberVendorEntry_Object = MibTableRow
fsFiberVendorEntry = _FsFiberVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1)
)
fsFiberVendorEntry.setIndexNames(
    (0, "FS-FIBER-MIB", "fsFiberVendorPortIndex"),
)
if mibBuilder.loadTexts:
    fsFiberVendorEntry.setStatus("current")
_FsFiberVendorPortIndex_Type = IfIndex
_FsFiberVendorPortIndex_Object = MibTableColumn
fsFiberVendorPortIndex = _FsFiberVendorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 1),
    _FsFiberVendorPortIndex_Type()
)
fsFiberVendorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorPortIndex.setStatus("current")
_FsFiberVendorName_Type = DisplayString
_FsFiberVendorName_Object = MibTableColumn
fsFiberVendorName = _FsFiberVendorName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 2),
    _FsFiberVendorName_Type()
)
fsFiberVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorName.setStatus("current")
_FsFiberVendorOUI_Type = DisplayString
_FsFiberVendorOUI_Object = MibTableColumn
fsFiberVendorOUI = _FsFiberVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 3),
    _FsFiberVendorOUI_Type()
)
fsFiberVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorOUI.setStatus("current")
_FsFiberVendorPN_Type = DisplayString
_FsFiberVendorPN_Object = MibTableColumn
fsFiberVendorPN = _FsFiberVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 4),
    _FsFiberVendorPN_Type()
)
fsFiberVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorPN.setStatus("current")
_FsFiberVendorRev_Type = DisplayString
_FsFiberVendorRev_Object = MibTableColumn
fsFiberVendorRev = _FsFiberVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 5),
    _FsFiberVendorRev_Type()
)
fsFiberVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorRev.setStatus("current")
_FsFiberVendorDate_Type = DisplayString
_FsFiberVendorDate_Object = MibTableColumn
fsFiberVendorDate = _FsFiberVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 6),
    _FsFiberVendorDate_Type()
)
fsFiberVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorDate.setStatus("current")
_FsFiberVendorEncoding_Type = DisplayString
_FsFiberVendorEncoding_Object = MibTableColumn
fsFiberVendorEncoding = _FsFiberVendorEncoding_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 1, 2, 1, 7),
    _FsFiberVendorEncoding_Type()
)
fsFiberVendorEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFiberVendorEncoding.setStatus("current")
_FsFiberAntifakeMIBTraps_ObjectIdentity = ObjectIdentity
fsFiberAntifakeMIBTraps = _FsFiberAntifakeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2)
)


class _FsFiberAntifakeIntfNameDesc_Type(DisplayString):
    """Custom type fsFiberAntifakeIntfNameDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberAntifakeIntfNameDesc_Type.__name__ = "DisplayString"
_FsFiberAntifakeIntfNameDesc_Object = MibScalar
fsFiberAntifakeIntfNameDesc = _FsFiberAntifakeIntfNameDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2, 1),
    _FsFiberAntifakeIntfNameDesc_Type()
)
fsFiberAntifakeIntfNameDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberAntifakeIntfNameDesc.setStatus("current")


class _FsFiberAntifakeSerialNumberDesc_Type(DisplayString):
    """Custom type fsFiberAntifakeSerialNumberDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFiberAntifakeSerialNumberDesc_Type.__name__ = "DisplayString"
_FsFiberAntifakeSerialNumberDesc_Object = MibScalar
fsFiberAntifakeSerialNumberDesc = _FsFiberAntifakeSerialNumberDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2, 2),
    _FsFiberAntifakeSerialNumberDesc_Type()
)
fsFiberAntifakeSerialNumberDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsFiberAntifakeSerialNumberDesc.setStatus("current")
_FsFiberMIBConformance_ObjectIdentity = ObjectIdentity
fsFiberMIBConformance = _FsFiberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3)
)
_FsFiberMIBCompliances_ObjectIdentity = ObjectIdentity
fsFiberMIBCompliances = _FsFiberMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 1)
)
_FsFiberMIBGroups_ObjectIdentity = ObjectIdentity
fsFiberMIBGroups = _FsFiberMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2)
)

# Managed Objects groups

fsFiberMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2, 1)
)
fsFiberMIBGroup.setObjects(
      *(("FS-FIBER-MIB", "fsFiberPortDescr"),
        ("FS-FIBER-MIB", "fsFiberTransceiverType"),
        ("FS-FIBER-MIB", "fsFiberConnectorType"),
        ("FS-FIBER-MIB", "fsFiberWavelength"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceSMF"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance62point5umOM1"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance62point5um"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50umOM2"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50um"),
        ("FS-FIBER-MIB", "fsFiberTransferDistance50umOM3"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceEBW50um"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceCopper"),
        ("FS-FIBER-MIB", "fsFiberTransferDistanceCableAssembly"),
        ("FS-FIBER-MIB", "fsFiberDDMSupportStatus"),
        ("FS-FIBER-MIB", "fsFiberSerialNumber"),
        ("FS-FIBER-MIB", "fsFiberTemp"),
        ("FS-FIBER-MIB", "fsFiberTempStatus"),
        ("FS-FIBER-MIB", "fsFiberVoltage"),
        ("FS-FIBER-MIB", "fsFiberVoltageStatus"),
        ("FS-FIBER-MIB", "fsFiberBias"),
        ("FS-FIBER-MIB", "fsFiberBiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel1Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel1BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel2Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel2BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel3Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel3BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel4Bias"),
        ("FS-FIBER-MIB", "fsFiberChannel4BiasStatus"),
        ("FS-FIBER-MIB", "fsFiberRXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberRXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberRXpowertype"),
        ("FS-FIBER-MIB", "fsFiberRXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowertype"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberTXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberTXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberTXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerIntegerpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerDecimalpart"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerStatus"),
        ("FS-FIBER-MIB", "fsFiberRXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel1RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel2RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel3RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel4RXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberTXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel1TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel2TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel3TXpowerSign"),
        ("FS-FIBER-MIB", "fsFiberChannel4TXpowerSign"))
)
if mibBuilder.loadTexts:
    fsFiberMIBGroup.setStatus("current")

fsFiberAntifakeIntfNameDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2, 2)
)
fsFiberAntifakeIntfNameDescGroup.setObjects(
    ("FS-FIBER-MIB", "fsFiberAntifakeIntfNameDesc")
)
if mibBuilder.loadTexts:
    fsFiberAntifakeIntfNameDescGroup.setStatus("current")

fsFiberAntifakeSerialNumberDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 2, 3)
)
fsFiberAntifakeSerialNumberDescGroup.setObjects(
    ("FS-FIBER-MIB", "fsFiberAntifakeSerialNumberDesc")
)
if mibBuilder.loadTexts:
    fsFiberAntifakeSerialNumberDescGroup.setStatus("current")


# Notification objects

fsFiberAntifakeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 2, 3)
)
fsFiberAntifakeTrap.setObjects(
      *(("FS-FIBER-MIB", "fsFiberAntifakeIntfNameDesc"),
        ("FS-FIBER-MIB", "fsFiberAntifakeSerialNumberDesc"))
)
if mibBuilder.loadTexts:
    fsFiberAntifakeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsFiberMIBConpliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 105, 3, 1, 1)
)
fsFiberMIBConpliance.setObjects(
      *(("FS-FIBER-MIB", "fsFiberMIBGroup"),
        ("FS-FIBER-MIB", "fsFiberAntifakeIntfNameDescGroup"),
        ("FS-FIBER-MIB", "fsFiberAntifakeSerialNumberDescGroup"))
)
if mibBuilder.loadTexts:
    fsFiberMIBConpliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-FIBER-MIB",
    **{"fsFiberMIB": fsFiberMIB,
       "fsFiberMIBObjects": fsFiberMIBObjects,
       "fsFiberTable": fsFiberTable,
       "fsFiberEntry": fsFiberEntry,
       "fsFiberPortIndex": fsFiberPortIndex,
       "fsFiberPortDescr": fsFiberPortDescr,
       "fsFiberTransceiverType": fsFiberTransceiverType,
       "fsFiberConnectorType": fsFiberConnectorType,
       "fsFiberWavelength": fsFiberWavelength,
       "fsFiberTransferDistanceSMF": fsFiberTransferDistanceSMF,
       "fsFiberTransferDistance62point5umOM1": fsFiberTransferDistance62point5umOM1,
       "fsFiberTransferDistance62point5um": fsFiberTransferDistance62point5um,
       "fsFiberTransferDistance50umOM2": fsFiberTransferDistance50umOM2,
       "fsFiberTransferDistance50um": fsFiberTransferDistance50um,
       "fsFiberTransferDistance50umOM3": fsFiberTransferDistance50umOM3,
       "fsFiberTransferDistanceEBW50um": fsFiberTransferDistanceEBW50um,
       "fsFiberTransferDistanceCopper": fsFiberTransferDistanceCopper,
       "fsFiberTransferDistanceCableAssembly": fsFiberTransferDistanceCableAssembly,
       "fsFiberDDMSupportStatus": fsFiberDDMSupportStatus,
       "fsFiberSerialNumber": fsFiberSerialNumber,
       "fsFiberTemp": fsFiberTemp,
       "fsFiberTempStatus": fsFiberTempStatus,
       "fsFiberVoltage": fsFiberVoltage,
       "fsFiberVoltageStatus": fsFiberVoltageStatus,
       "fsFiberBias": fsFiberBias,
       "fsFiberBiasStatus": fsFiberBiasStatus,
       "fsFiberChannel1Bias": fsFiberChannel1Bias,
       "fsFiberChannel1BiasStatus": fsFiberChannel1BiasStatus,
       "fsFiberChannel2Bias": fsFiberChannel2Bias,
       "fsFiberChannel2BiasStatus": fsFiberChannel2BiasStatus,
       "fsFiberChannel3Bias": fsFiberChannel3Bias,
       "fsFiberChannel3BiasStatus": fsFiberChannel3BiasStatus,
       "fsFiberChannel4Bias": fsFiberChannel4Bias,
       "fsFiberChannel4BiasStatus": fsFiberChannel4BiasStatus,
       "fsFiberRXpowerIntegerpart": fsFiberRXpowerIntegerpart,
       "fsFiberRXpowerDecimalpart": fsFiberRXpowerDecimalpart,
       "fsFiberRXpowertype": fsFiberRXpowertype,
       "fsFiberRXpowerStatus": fsFiberRXpowerStatus,
       "fsFiberChannel1RXpowerIntegerpart": fsFiberChannel1RXpowerIntegerpart,
       "fsFiberChannel1RXpowerDecimalpart": fsFiberChannel1RXpowerDecimalpart,
       "fsFiberChannel1RXpowertype": fsFiberChannel1RXpowertype,
       "fsFiberChannel1RXpowerStatus": fsFiberChannel1RXpowerStatus,
       "fsFiberChannel2RXpowerIntegerpart": fsFiberChannel2RXpowerIntegerpart,
       "fsFiberChannel2RXpowerDecimalpart": fsFiberChannel2RXpowerDecimalpart,
       "fsFiberChannel2RXpowertype": fsFiberChannel2RXpowertype,
       "fsFiberChannel2RXpowerStatus": fsFiberChannel2RXpowerStatus,
       "fsFiberChannel3RXpowerIntegerpart": fsFiberChannel3RXpowerIntegerpart,
       "fsFiberChannel3RXpowerDecimalpart": fsFiberChannel3RXpowerDecimalpart,
       "fsFiberChannel3RXpowertype": fsFiberChannel3RXpowertype,
       "fsFiberChannel3RXpowerStatus": fsFiberChannel3RXpowerStatus,
       "fsFiberChannel4RXpowerIntegerpart": fsFiberChannel4RXpowerIntegerpart,
       "fsFiberChannel4RXpowerDecimalpart": fsFiberChannel4RXpowerDecimalpart,
       "fsFiberChannel4RXpowertype": fsFiberChannel4RXpowertype,
       "fsFiberChannel4RXpowerStatus": fsFiberChannel4RXpowerStatus,
       "fsFiberTXpowerIntegerpart": fsFiberTXpowerIntegerpart,
       "fsFiberTXpowerDecimalpart": fsFiberTXpowerDecimalpart,
       "fsFiberTXpowerStatus": fsFiberTXpowerStatus,
       "fsFiberChannel1TXpowerIntegerpart": fsFiberChannel1TXpowerIntegerpart,
       "fsFiberChannel1TXpowerDecimalpart": fsFiberChannel1TXpowerDecimalpart,
       "fsFiberChannel1TXpowerStatus": fsFiberChannel1TXpowerStatus,
       "fsFiberChannel2TXpowerIntegerpart": fsFiberChannel2TXpowerIntegerpart,
       "fsFiberChannel2TXpowerDecimalpart": fsFiberChannel2TXpowerDecimalpart,
       "fsFiberChannel2TXpowerStatus": fsFiberChannel2TXpowerStatus,
       "fsFiberChannel3TXpowerIntegerpart": fsFiberChannel3TXpowerIntegerpart,
       "fsFiberChannel3TXpowerDecimalpart": fsFiberChannel3TXpowerDecimalpart,
       "fsFiberChannel3TXpowerStatus": fsFiberChannel3TXpowerStatus,
       "fsFiberChannel4TXpowerIntegerpart": fsFiberChannel4TXpowerIntegerpart,
       "fsFiberChannel4TXpowerDecimalpart": fsFiberChannel4TXpowerDecimalpart,
       "fsFiberChannel4TXpowerStatus": fsFiberChannel4TXpowerStatus,
       "fsFiberRXpowerSign": fsFiberRXpowerSign,
       "fsFiberChannel1RXpowerSign": fsFiberChannel1RXpowerSign,
       "fsFiberChannel2RXpowerSign": fsFiberChannel2RXpowerSign,
       "fsFiberChannel3RXpowerSign": fsFiberChannel3RXpowerSign,
       "fsFiberChannel4RXpowerSign": fsFiberChannel4RXpowerSign,
       "fsFiberTXpowerSign": fsFiberTXpowerSign,
       "fsFiberChannel1TXpowerSign": fsFiberChannel1TXpowerSign,
       "fsFiberChannel2TXpowerSign": fsFiberChannel2TXpowerSign,
       "fsFiberChannel3TXpowerSign": fsFiberChannel3TXpowerSign,
       "fsFiberChannel4TXpowerSign": fsFiberChannel4TXpowerSign,
       "fsFiberRXpowerInteger": fsFiberRXpowerInteger,
       "fsFiberChannel1RXpowerInteger": fsFiberChannel1RXpowerInteger,
       "fsFiberChannel2RXpowerInteger": fsFiberChannel2RXpowerInteger,
       "fsFiberChannel3RXpowerInteger": fsFiberChannel3RXpowerInteger,
       "fsFiberChannel4RXpowerInteger": fsFiberChannel4RXpowerInteger,
       "fsFiberTXpowerInteger": fsFiberTXpowerInteger,
       "fsFiberChannel1TXpowerInteger": fsFiberChannel1TXpowerInteger,
       "fsFiberChannel2TXpowerInteger": fsFiberChannel2TXpowerInteger,
       "fsFiberChannel3TXpowerInteger": fsFiberChannel3TXpowerInteger,
       "fsFiberChannel4TXpowerInteger": fsFiberChannel4TXpowerInteger,
       "fsFiberVendorTable": fsFiberVendorTable,
       "fsFiberVendorEntry": fsFiberVendorEntry,
       "fsFiberVendorPortIndex": fsFiberVendorPortIndex,
       "fsFiberVendorName": fsFiberVendorName,
       "fsFiberVendorOUI": fsFiberVendorOUI,
       "fsFiberVendorPN": fsFiberVendorPN,
       "fsFiberVendorRev": fsFiberVendorRev,
       "fsFiberVendorDate": fsFiberVendorDate,
       "fsFiberVendorEncoding": fsFiberVendorEncoding,
       "fsFiberAntifakeMIBTraps": fsFiberAntifakeMIBTraps,
       "fsFiberAntifakeIntfNameDesc": fsFiberAntifakeIntfNameDesc,
       "fsFiberAntifakeSerialNumberDesc": fsFiberAntifakeSerialNumberDesc,
       "fsFiberAntifakeTrap": fsFiberAntifakeTrap,
       "fsFiberMIBConformance": fsFiberMIBConformance,
       "fsFiberMIBCompliances": fsFiberMIBCompliances,
       "fsFiberMIBConpliance": fsFiberMIBConpliance,
       "fsFiberMIBGroups": fsFiberMIBGroups,
       "fsFiberMIBGroup": fsFiberMIBGroup,
       "fsFiberAntifakeIntfNameDescGroup": fsFiberAntifakeIntfNameDescGroup,
       "fsFiberAntifakeSerialNumberDescGroup": fsFiberAntifakeSerialNumberDescGroup}
)
