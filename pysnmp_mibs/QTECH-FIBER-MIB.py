# SNMP MIB module (QTECH-FIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-FIBER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:23 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechFiberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105)
)
if mibBuilder.loadTexts:
    qtechFiberMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechFiberMIBObjects_ObjectIdentity = ObjectIdentity
qtechFiberMIBObjects = _QtechFiberMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1)
)
_QtechFiberTable_Object = MibTable
qtechFiberTable = _QtechFiberTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1)
)
if mibBuilder.loadTexts:
    qtechFiberTable.setStatus("current")
_QtechFiberEntry_Object = MibTableRow
qtechFiberEntry = _QtechFiberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1)
)
qtechFiberEntry.setIndexNames(
    (0, "QTECH-FIBER-MIB", "qtechFiberPortIndex"),
)
if mibBuilder.loadTexts:
    qtechFiberEntry.setStatus("current")
_QtechFiberPortIndex_Type = IfIndex
_QtechFiberPortIndex_Object = MibTableColumn
qtechFiberPortIndex = _QtechFiberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 1),
    _QtechFiberPortIndex_Type()
)
qtechFiberPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechFiberPortIndex.setStatus("current")


class _QtechFiberPortDescr_Type(DisplayString):
    """Custom type qtechFiberPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechFiberPortDescr_Type.__name__ = "DisplayString"
_QtechFiberPortDescr_Object = MibTableColumn
qtechFiberPortDescr = _QtechFiberPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 2),
    _QtechFiberPortDescr_Type()
)
qtechFiberPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberPortDescr.setStatus("current")


class _QtechFiberTransceiverType_Type(Integer32):
    """Custom type qtechFiberTransceiverType based on Integer32"""
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
              28)
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
          ("fiber2500CopperSFP", 28))
    )


_QtechFiberTransceiverType_Type.__name__ = "Integer32"
_QtechFiberTransceiverType_Object = MibTableColumn
qtechFiberTransceiverType = _QtechFiberTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 3),
    _QtechFiberTransceiverType_Type()
)
qtechFiberTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransceiverType.setStatus("current")


class _QtechFiberConnectorType_Type(Integer32):
    """Custom type qtechFiberConnectorType based on Integer32"""
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


_QtechFiberConnectorType_Type.__name__ = "Integer32"
_QtechFiberConnectorType_Object = MibTableColumn
qtechFiberConnectorType = _QtechFiberConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 4),
    _QtechFiberConnectorType_Type()
)
qtechFiberConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberConnectorType.setStatus("current")
_QtechFiberWavelength_Type = Integer32
_QtechFiberWavelength_Object = MibTableColumn
qtechFiberWavelength = _QtechFiberWavelength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 5),
    _QtechFiberWavelength_Type()
)
qtechFiberWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberWavelength.setStatus("current")
_QtechFiberTransferDistanceSMF_Type = Integer32
_QtechFiberTransferDistanceSMF_Object = MibTableColumn
qtechFiberTransferDistanceSMF = _QtechFiberTransferDistanceSMF_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 6),
    _QtechFiberTransferDistanceSMF_Type()
)
qtechFiberTransferDistanceSMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistanceSMF.setStatus("current")
_QtechFiberTransferDistance62point5umOM1_Type = Integer32
_QtechFiberTransferDistance62point5umOM1_Object = MibTableColumn
qtechFiberTransferDistance62point5umOM1 = _QtechFiberTransferDistance62point5umOM1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 7),
    _QtechFiberTransferDistance62point5umOM1_Type()
)
qtechFiberTransferDistance62point5umOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistance62point5umOM1.setStatus("current")
_QtechFiberTransferDistance62point5um_Type = Integer32
_QtechFiberTransferDistance62point5um_Object = MibTableColumn
qtechFiberTransferDistance62point5um = _QtechFiberTransferDistance62point5um_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 8),
    _QtechFiberTransferDistance62point5um_Type()
)
qtechFiberTransferDistance62point5um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistance62point5um.setStatus("current")
_QtechFiberTransferDistance50umOM2_Type = Integer32
_QtechFiberTransferDistance50umOM2_Object = MibTableColumn
qtechFiberTransferDistance50umOM2 = _QtechFiberTransferDistance50umOM2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 9),
    _QtechFiberTransferDistance50umOM2_Type()
)
qtechFiberTransferDistance50umOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistance50umOM2.setStatus("current")
_QtechFiberTransferDistance50um_Type = Integer32
_QtechFiberTransferDistance50um_Object = MibTableColumn
qtechFiberTransferDistance50um = _QtechFiberTransferDistance50um_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 10),
    _QtechFiberTransferDistance50um_Type()
)
qtechFiberTransferDistance50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistance50um.setStatus("current")
_QtechFiberTransferDistance50umOM3_Type = Integer32
_QtechFiberTransferDistance50umOM3_Object = MibTableColumn
qtechFiberTransferDistance50umOM3 = _QtechFiberTransferDistance50umOM3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 11),
    _QtechFiberTransferDistance50umOM3_Type()
)
qtechFiberTransferDistance50umOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistance50umOM3.setStatus("current")
_QtechFiberTransferDistanceEBW50um_Type = Integer32
_QtechFiberTransferDistanceEBW50um_Object = MibTableColumn
qtechFiberTransferDistanceEBW50um = _QtechFiberTransferDistanceEBW50um_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 12),
    _QtechFiberTransferDistanceEBW50um_Type()
)
qtechFiberTransferDistanceEBW50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistanceEBW50um.setStatus("current")
_QtechFiberTransferDistanceCopper_Type = Integer32
_QtechFiberTransferDistanceCopper_Object = MibTableColumn
qtechFiberTransferDistanceCopper = _QtechFiberTransferDistanceCopper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 13),
    _QtechFiberTransferDistanceCopper_Type()
)
qtechFiberTransferDistanceCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistanceCopper.setStatus("current")
_QtechFiberTransferDistanceCableAssembly_Type = Integer32
_QtechFiberTransferDistanceCableAssembly_Object = MibTableColumn
qtechFiberTransferDistanceCableAssembly = _QtechFiberTransferDistanceCableAssembly_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 14),
    _QtechFiberTransferDistanceCableAssembly_Type()
)
qtechFiberTransferDistanceCableAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTransferDistanceCableAssembly.setStatus("current")
_QtechFiberDDMSupportStatus_Type = TruthValue
_QtechFiberDDMSupportStatus_Object = MibTableColumn
qtechFiberDDMSupportStatus = _QtechFiberDDMSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 15),
    _QtechFiberDDMSupportStatus_Type()
)
qtechFiberDDMSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberDDMSupportStatus.setStatus("current")


class _QtechFiberSerialNumber_Type(DisplayString):
    """Custom type qtechFiberSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechFiberSerialNumber_Type.__name__ = "DisplayString"
_QtechFiberSerialNumber_Object = MibTableColumn
qtechFiberSerialNumber = _QtechFiberSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 16),
    _QtechFiberSerialNumber_Type()
)
qtechFiberSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberSerialNumber.setStatus("current")
_QtechFiberTemp_Type = Integer32
_QtechFiberTemp_Object = MibTableColumn
qtechFiberTemp = _QtechFiberTemp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 17),
    _QtechFiberTemp_Type()
)
qtechFiberTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTemp.setStatus("current")


class _QtechFiberTempStatus_Type(Integer32):
    """Custom type qtechFiberTempStatus based on Integer32"""
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


_QtechFiberTempStatus_Type.__name__ = "Integer32"
_QtechFiberTempStatus_Object = MibTableColumn
qtechFiberTempStatus = _QtechFiberTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 18),
    _QtechFiberTempStatus_Type()
)
qtechFiberTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTempStatus.setStatus("current")
_QtechFiberVoltage_Type = Integer32
_QtechFiberVoltage_Object = MibTableColumn
qtechFiberVoltage = _QtechFiberVoltage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 19),
    _QtechFiberVoltage_Type()
)
qtechFiberVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberVoltage.setStatus("current")


class _QtechFiberVoltageStatus_Type(Integer32):
    """Custom type qtechFiberVoltageStatus based on Integer32"""
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


_QtechFiberVoltageStatus_Type.__name__ = "Integer32"
_QtechFiberVoltageStatus_Object = MibTableColumn
qtechFiberVoltageStatus = _QtechFiberVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 20),
    _QtechFiberVoltageStatus_Type()
)
qtechFiberVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberVoltageStatus.setStatus("current")
_QtechFiberBias_Type = Integer32
_QtechFiberBias_Object = MibTableColumn
qtechFiberBias = _QtechFiberBias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 21),
    _QtechFiberBias_Type()
)
qtechFiberBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberBias.setStatus("current")


class _QtechFiberBiasStatus_Type(Integer32):
    """Custom type qtechFiberBiasStatus based on Integer32"""
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


_QtechFiberBiasStatus_Type.__name__ = "Integer32"
_QtechFiberBiasStatus_Object = MibTableColumn
qtechFiberBiasStatus = _QtechFiberBiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 22),
    _QtechFiberBiasStatus_Type()
)
qtechFiberBiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberBiasStatus.setStatus("current")
_QtechFiberChannel1Bias_Type = Integer32
_QtechFiberChannel1Bias_Object = MibTableColumn
qtechFiberChannel1Bias = _QtechFiberChannel1Bias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 23),
    _QtechFiberChannel1Bias_Type()
)
qtechFiberChannel1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1Bias.setStatus("current")


class _QtechFiberChannel1BiasStatus_Type(Integer32):
    """Custom type qtechFiberChannel1BiasStatus based on Integer32"""
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


_QtechFiberChannel1BiasStatus_Type.__name__ = "Integer32"
_QtechFiberChannel1BiasStatus_Object = MibTableColumn
qtechFiberChannel1BiasStatus = _QtechFiberChannel1BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 24),
    _QtechFiberChannel1BiasStatus_Type()
)
qtechFiberChannel1BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1BiasStatus.setStatus("current")
_QtechFiberChannel2Bias_Type = Integer32
_QtechFiberChannel2Bias_Object = MibTableColumn
qtechFiberChannel2Bias = _QtechFiberChannel2Bias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 25),
    _QtechFiberChannel2Bias_Type()
)
qtechFiberChannel2Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2Bias.setStatus("current")


class _QtechFiberChannel2BiasStatus_Type(Integer32):
    """Custom type qtechFiberChannel2BiasStatus based on Integer32"""
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


_QtechFiberChannel2BiasStatus_Type.__name__ = "Integer32"
_QtechFiberChannel2BiasStatus_Object = MibTableColumn
qtechFiberChannel2BiasStatus = _QtechFiberChannel2BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 26),
    _QtechFiberChannel2BiasStatus_Type()
)
qtechFiberChannel2BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2BiasStatus.setStatus("current")
_QtechFiberChannel3Bias_Type = Integer32
_QtechFiberChannel3Bias_Object = MibTableColumn
qtechFiberChannel3Bias = _QtechFiberChannel3Bias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 27),
    _QtechFiberChannel3Bias_Type()
)
qtechFiberChannel3Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3Bias.setStatus("current")


class _QtechFiberChannel3BiasStatus_Type(Integer32):
    """Custom type qtechFiberChannel3BiasStatus based on Integer32"""
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


_QtechFiberChannel3BiasStatus_Type.__name__ = "Integer32"
_QtechFiberChannel3BiasStatus_Object = MibTableColumn
qtechFiberChannel3BiasStatus = _QtechFiberChannel3BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 28),
    _QtechFiberChannel3BiasStatus_Type()
)
qtechFiberChannel3BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3BiasStatus.setStatus("current")
_QtechFiberChannel4Bias_Type = Integer32
_QtechFiberChannel4Bias_Object = MibTableColumn
qtechFiberChannel4Bias = _QtechFiberChannel4Bias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 29),
    _QtechFiberChannel4Bias_Type()
)
qtechFiberChannel4Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4Bias.setStatus("current")


class _QtechFiberChannel4BiasStatus_Type(Integer32):
    """Custom type qtechFiberChannel4BiasStatus based on Integer32"""
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


_QtechFiberChannel4BiasStatus_Type.__name__ = "Integer32"
_QtechFiberChannel4BiasStatus_Object = MibTableColumn
qtechFiberChannel4BiasStatus = _QtechFiberChannel4BiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 30),
    _QtechFiberChannel4BiasStatus_Type()
)
qtechFiberChannel4BiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4BiasStatus.setStatus("current")
_QtechFiberRXpowerIntegerpart_Type = Integer32
_QtechFiberRXpowerIntegerpart_Object = MibTableColumn
qtechFiberRXpowerIntegerpart = _QtechFiberRXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 31),
    _QtechFiberRXpowerIntegerpart_Type()
)
qtechFiberRXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberRXpowerIntegerpart.setStatus("current")
_QtechFiberRXpowerDecimalpart_Type = Integer32
_QtechFiberRXpowerDecimalpart_Object = MibTableColumn
qtechFiberRXpowerDecimalpart = _QtechFiberRXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 32),
    _QtechFiberRXpowerDecimalpart_Type()
)
qtechFiberRXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberRXpowerDecimalpart.setStatus("current")


class _QtechFiberRXpowertype_Type(Integer32):
    """Custom type qtechFiberRXpowertype based on Integer32"""
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


_QtechFiberRXpowertype_Type.__name__ = "Integer32"
_QtechFiberRXpowertype_Object = MibTableColumn
qtechFiberRXpowertype = _QtechFiberRXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 33),
    _QtechFiberRXpowertype_Type()
)
qtechFiberRXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberRXpowertype.setStatus("current")


class _QtechFiberRXpowerStatus_Type(Integer32):
    """Custom type qtechFiberRXpowerStatus based on Integer32"""
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


_QtechFiberRXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberRXpowerStatus_Object = MibTableColumn
qtechFiberRXpowerStatus = _QtechFiberRXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 34),
    _QtechFiberRXpowerStatus_Type()
)
qtechFiberRXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberRXpowerStatus.setStatus("current")
_QtechFiberChannel1RXpowerIntegerpart_Type = Integer32
_QtechFiberChannel1RXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel1RXpowerIntegerpart = _QtechFiberChannel1RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 35),
    _QtechFiberChannel1RXpowerIntegerpart_Type()
)
qtechFiberChannel1RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1RXpowerIntegerpart.setStatus("current")
_QtechFiberChannel1RXpowerDecimalpart_Type = Integer32
_QtechFiberChannel1RXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel1RXpowerDecimalpart = _QtechFiberChannel1RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 36),
    _QtechFiberChannel1RXpowerDecimalpart_Type()
)
qtechFiberChannel1RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1RXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel1RXpowertype_Type(Integer32):
    """Custom type qtechFiberChannel1RXpowertype based on Integer32"""
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


_QtechFiberChannel1RXpowertype_Type.__name__ = "Integer32"
_QtechFiberChannel1RXpowertype_Object = MibTableColumn
qtechFiberChannel1RXpowertype = _QtechFiberChannel1RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 37),
    _QtechFiberChannel1RXpowertype_Type()
)
qtechFiberChannel1RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1RXpowertype.setStatus("current")


class _QtechFiberChannel1RXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel1RXpowerStatus based on Integer32"""
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


_QtechFiberChannel1RXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel1RXpowerStatus_Object = MibTableColumn
qtechFiberChannel1RXpowerStatus = _QtechFiberChannel1RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 38),
    _QtechFiberChannel1RXpowerStatus_Type()
)
qtechFiberChannel1RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1RXpowerStatus.setStatus("current")
_QtechFiberChannel2RXpowerIntegerpart_Type = Integer32
_QtechFiberChannel2RXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel2RXpowerIntegerpart = _QtechFiberChannel2RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 39),
    _QtechFiberChannel2RXpowerIntegerpart_Type()
)
qtechFiberChannel2RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2RXpowerIntegerpart.setStatus("current")
_QtechFiberChannel2RXpowerDecimalpart_Type = Integer32
_QtechFiberChannel2RXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel2RXpowerDecimalpart = _QtechFiberChannel2RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 40),
    _QtechFiberChannel2RXpowerDecimalpart_Type()
)
qtechFiberChannel2RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2RXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel2RXpowertype_Type(Integer32):
    """Custom type qtechFiberChannel2RXpowertype based on Integer32"""
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


_QtechFiberChannel2RXpowertype_Type.__name__ = "Integer32"
_QtechFiberChannel2RXpowertype_Object = MibTableColumn
qtechFiberChannel2RXpowertype = _QtechFiberChannel2RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 41),
    _QtechFiberChannel2RXpowertype_Type()
)
qtechFiberChannel2RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2RXpowertype.setStatus("current")


class _QtechFiberChannel2RXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel2RXpowerStatus based on Integer32"""
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


_QtechFiberChannel2RXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel2RXpowerStatus_Object = MibTableColumn
qtechFiberChannel2RXpowerStatus = _QtechFiberChannel2RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 42),
    _QtechFiberChannel2RXpowerStatus_Type()
)
qtechFiberChannel2RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2RXpowerStatus.setStatus("current")
_QtechFiberChannel3RXpowerIntegerpart_Type = Integer32
_QtechFiberChannel3RXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel3RXpowerIntegerpart = _QtechFiberChannel3RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 43),
    _QtechFiberChannel3RXpowerIntegerpart_Type()
)
qtechFiberChannel3RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3RXpowerIntegerpart.setStatus("current")
_QtechFiberChannel3RXpowerDecimalpart_Type = Integer32
_QtechFiberChannel3RXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel3RXpowerDecimalpart = _QtechFiberChannel3RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 44),
    _QtechFiberChannel3RXpowerDecimalpart_Type()
)
qtechFiberChannel3RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3RXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel3RXpowertype_Type(Integer32):
    """Custom type qtechFiberChannel3RXpowertype based on Integer32"""
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


_QtechFiberChannel3RXpowertype_Type.__name__ = "Integer32"
_QtechFiberChannel3RXpowertype_Object = MibTableColumn
qtechFiberChannel3RXpowertype = _QtechFiberChannel3RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 45),
    _QtechFiberChannel3RXpowertype_Type()
)
qtechFiberChannel3RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3RXpowertype.setStatus("current")


class _QtechFiberChannel3RXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel3RXpowerStatus based on Integer32"""
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


_QtechFiberChannel3RXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel3RXpowerStatus_Object = MibTableColumn
qtechFiberChannel3RXpowerStatus = _QtechFiberChannel3RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 46),
    _QtechFiberChannel3RXpowerStatus_Type()
)
qtechFiberChannel3RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3RXpowerStatus.setStatus("current")
_QtechFiberChannel4RXpowerIntegerpart_Type = Integer32
_QtechFiberChannel4RXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel4RXpowerIntegerpart = _QtechFiberChannel4RXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 47),
    _QtechFiberChannel4RXpowerIntegerpart_Type()
)
qtechFiberChannel4RXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4RXpowerIntegerpart.setStatus("current")
_QtechFiberChannel4RXpowerDecimalpart_Type = Integer32
_QtechFiberChannel4RXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel4RXpowerDecimalpart = _QtechFiberChannel4RXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 48),
    _QtechFiberChannel4RXpowerDecimalpart_Type()
)
qtechFiberChannel4RXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4RXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel4RXpowertype_Type(Integer32):
    """Custom type qtechFiberChannel4RXpowertype based on Integer32"""
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


_QtechFiberChannel4RXpowertype_Type.__name__ = "Integer32"
_QtechFiberChannel4RXpowertype_Object = MibTableColumn
qtechFiberChannel4RXpowertype = _QtechFiberChannel4RXpowertype_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 49),
    _QtechFiberChannel4RXpowertype_Type()
)
qtechFiberChannel4RXpowertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4RXpowertype.setStatus("current")


class _QtechFiberChannel4RXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel4RXpowerStatus based on Integer32"""
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


_QtechFiberChannel4RXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel4RXpowerStatus_Object = MibTableColumn
qtechFiberChannel4RXpowerStatus = _QtechFiberChannel4RXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 50),
    _QtechFiberChannel4RXpowerStatus_Type()
)
qtechFiberChannel4RXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4RXpowerStatus.setStatus("current")
_QtechFiberTXpowerIntegerpart_Type = Integer32
_QtechFiberTXpowerIntegerpart_Object = MibTableColumn
qtechFiberTXpowerIntegerpart = _QtechFiberTXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 51),
    _QtechFiberTXpowerIntegerpart_Type()
)
qtechFiberTXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTXpowerIntegerpart.setStatus("current")
_QtechFiberTXpowerDecimalpart_Type = Integer32
_QtechFiberTXpowerDecimalpart_Object = MibTableColumn
qtechFiberTXpowerDecimalpart = _QtechFiberTXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 52),
    _QtechFiberTXpowerDecimalpart_Type()
)
qtechFiberTXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTXpowerDecimalpart.setStatus("current")


class _QtechFiberTXpowerStatus_Type(Integer32):
    """Custom type qtechFiberTXpowerStatus based on Integer32"""
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


_QtechFiberTXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberTXpowerStatus_Object = MibTableColumn
qtechFiberTXpowerStatus = _QtechFiberTXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 53),
    _QtechFiberTXpowerStatus_Type()
)
qtechFiberTXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberTXpowerStatus.setStatus("current")
_QtechFiberChannel1TXpowerIntegerpart_Type = Integer32
_QtechFiberChannel1TXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel1TXpowerIntegerpart = _QtechFiberChannel1TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 54),
    _QtechFiberChannel1TXpowerIntegerpart_Type()
)
qtechFiberChannel1TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1TXpowerIntegerpart.setStatus("current")
_QtechFiberChannel1TXpowerDecimalpart_Type = Integer32
_QtechFiberChannel1TXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel1TXpowerDecimalpart = _QtechFiberChannel1TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 55),
    _QtechFiberChannel1TXpowerDecimalpart_Type()
)
qtechFiberChannel1TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1TXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel1TXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel1TXpowerStatus based on Integer32"""
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


_QtechFiberChannel1TXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel1TXpowerStatus_Object = MibTableColumn
qtechFiberChannel1TXpowerStatus = _QtechFiberChannel1TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 56),
    _QtechFiberChannel1TXpowerStatus_Type()
)
qtechFiberChannel1TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel1TXpowerStatus.setStatus("current")
_QtechFiberChannel2TXpowerIntegerpart_Type = Integer32
_QtechFiberChannel2TXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel2TXpowerIntegerpart = _QtechFiberChannel2TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 57),
    _QtechFiberChannel2TXpowerIntegerpart_Type()
)
qtechFiberChannel2TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2TXpowerIntegerpart.setStatus("current")
_QtechFiberChannel2TXpowerDecimalpart_Type = Integer32
_QtechFiberChannel2TXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel2TXpowerDecimalpart = _QtechFiberChannel2TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 58),
    _QtechFiberChannel2TXpowerDecimalpart_Type()
)
qtechFiberChannel2TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2TXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel2TXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel2TXpowerStatus based on Integer32"""
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


_QtechFiberChannel2TXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel2TXpowerStatus_Object = MibTableColumn
qtechFiberChannel2TXpowerStatus = _QtechFiberChannel2TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 59),
    _QtechFiberChannel2TXpowerStatus_Type()
)
qtechFiberChannel2TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel2TXpowerStatus.setStatus("current")
_QtechFiberChannel3TXpowerIntegerpart_Type = Integer32
_QtechFiberChannel3TXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel3TXpowerIntegerpart = _QtechFiberChannel3TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 60),
    _QtechFiberChannel3TXpowerIntegerpart_Type()
)
qtechFiberChannel3TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3TXpowerIntegerpart.setStatus("current")
_QtechFiberChannel3TXpowerDecimalpart_Type = Integer32
_QtechFiberChannel3TXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel3TXpowerDecimalpart = _QtechFiberChannel3TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 61),
    _QtechFiberChannel3TXpowerDecimalpart_Type()
)
qtechFiberChannel3TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3TXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel3TXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel3TXpowerStatus based on Integer32"""
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


_QtechFiberChannel3TXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel3TXpowerStatus_Object = MibTableColumn
qtechFiberChannel3TXpowerStatus = _QtechFiberChannel3TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 62),
    _QtechFiberChannel3TXpowerStatus_Type()
)
qtechFiberChannel3TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel3TXpowerStatus.setStatus("current")
_QtechFiberChannel4TXpowerIntegerpart_Type = Integer32
_QtechFiberChannel4TXpowerIntegerpart_Object = MibTableColumn
qtechFiberChannel4TXpowerIntegerpart = _QtechFiberChannel4TXpowerIntegerpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 63),
    _QtechFiberChannel4TXpowerIntegerpart_Type()
)
qtechFiberChannel4TXpowerIntegerpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4TXpowerIntegerpart.setStatus("current")
_QtechFiberChannel4TXpowerDecimalpart_Type = Integer32
_QtechFiberChannel4TXpowerDecimalpart_Object = MibTableColumn
qtechFiberChannel4TXpowerDecimalpart = _QtechFiberChannel4TXpowerDecimalpart_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 64),
    _QtechFiberChannel4TXpowerDecimalpart_Type()
)
qtechFiberChannel4TXpowerDecimalpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4TXpowerDecimalpart.setStatus("current")


class _QtechFiberChannel4TXpowerStatus_Type(Integer32):
    """Custom type qtechFiberChannel4TXpowerStatus based on Integer32"""
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


_QtechFiberChannel4TXpowerStatus_Type.__name__ = "Integer32"
_QtechFiberChannel4TXpowerStatus_Object = MibTableColumn
qtechFiberChannel4TXpowerStatus = _QtechFiberChannel4TXpowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 1, 1, 1, 65),
    _QtechFiberChannel4TXpowerStatus_Type()
)
qtechFiberChannel4TXpowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFiberChannel4TXpowerStatus.setStatus("current")
_QtechFiberMIBConformance_ObjectIdentity = ObjectIdentity
qtechFiberMIBConformance = _QtechFiberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 2)
)
_QtechFiberMIBCompliances_ObjectIdentity = ObjectIdentity
qtechFiberMIBCompliances = _QtechFiberMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 2, 1)
)
_QtechFiberMIBGroups_ObjectIdentity = ObjectIdentity
qtechFiberMIBGroups = _QtechFiberMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 2, 2)
)

# Managed Objects groups

qtechFiberMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 2, 2, 1)
)
qtechFiberMIBGroup.setObjects(
      *(("QTECH-FIBER-MIB", "qtechFiberPortDescr"),
        ("QTECH-FIBER-MIB", "qtechFiberTransceiverType"),
        ("QTECH-FIBER-MIB", "qtechFiberConnectorType"),
        ("QTECH-FIBER-MIB", "qtechFiberWavelength"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistanceSMF"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistance62point5umOM1"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistance62point5um"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistance50umOM2"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistance50um"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistance50umOM3"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistanceEBW50um"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistanceCopper"),
        ("QTECH-FIBER-MIB", "qtechFiberTransferDistanceCableAssembly"),
        ("QTECH-FIBER-MIB", "qtechFiberDDMSupportStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberSerialNumber"),
        ("QTECH-FIBER-MIB", "qtechFiberTemp"),
        ("QTECH-FIBER-MIB", "qtechFiberTempStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberVoltage"),
        ("QTECH-FIBER-MIB", "qtechFiberVoltageStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberBias"),
        ("QTECH-FIBER-MIB", "qtechFiberBiasStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1Bias"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1BiasStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2Bias"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2BiasStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3Bias"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3BiasStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4Bias"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4BiasStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberRXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberRXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberRXpowertype"),
        ("QTECH-FIBER-MIB", "qtechFiberRXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1RXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1RXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1RXpowertype"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1RXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2RXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2RXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2RXpowertype"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2RXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3RXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3RXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3RXpowertype"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3RXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4RXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4RXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4RXpowertype"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4RXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberTXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberTXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberTXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1TXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1TXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel1TXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2TXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2TXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel2TXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3TXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3TXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel3TXpowerStatus"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4TXpowerIntegerpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4TXpowerDecimalpart"),
        ("QTECH-FIBER-MIB", "qtechFiberChannel4TXpowerStatus"))
)
if mibBuilder.loadTexts:
    qtechFiberMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechFiberMIBConpliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 105, 2, 1, 1)
)
qtechFiberMIBConpliance.setObjects(
    ("QTECH-FIBER-MIB", "qtechFiberMIBGroup")
)
if mibBuilder.loadTexts:
    qtechFiberMIBConpliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-FIBER-MIB",
    **{"qtechFiberMIB": qtechFiberMIB,
       "qtechFiberMIBObjects": qtechFiberMIBObjects,
       "qtechFiberTable": qtechFiberTable,
       "qtechFiberEntry": qtechFiberEntry,
       "qtechFiberPortIndex": qtechFiberPortIndex,
       "qtechFiberPortDescr": qtechFiberPortDescr,
       "qtechFiberTransceiverType": qtechFiberTransceiverType,
       "qtechFiberConnectorType": qtechFiberConnectorType,
       "qtechFiberWavelength": qtechFiberWavelength,
       "qtechFiberTransferDistanceSMF": qtechFiberTransferDistanceSMF,
       "qtechFiberTransferDistance62point5umOM1": qtechFiberTransferDistance62point5umOM1,
       "qtechFiberTransferDistance62point5um": qtechFiberTransferDistance62point5um,
       "qtechFiberTransferDistance50umOM2": qtechFiberTransferDistance50umOM2,
       "qtechFiberTransferDistance50um": qtechFiberTransferDistance50um,
       "qtechFiberTransferDistance50umOM3": qtechFiberTransferDistance50umOM3,
       "qtechFiberTransferDistanceEBW50um": qtechFiberTransferDistanceEBW50um,
       "qtechFiberTransferDistanceCopper": qtechFiberTransferDistanceCopper,
       "qtechFiberTransferDistanceCableAssembly": qtechFiberTransferDistanceCableAssembly,
       "qtechFiberDDMSupportStatus": qtechFiberDDMSupportStatus,
       "qtechFiberSerialNumber": qtechFiberSerialNumber,
       "qtechFiberTemp": qtechFiberTemp,
       "qtechFiberTempStatus": qtechFiberTempStatus,
       "qtechFiberVoltage": qtechFiberVoltage,
       "qtechFiberVoltageStatus": qtechFiberVoltageStatus,
       "qtechFiberBias": qtechFiberBias,
       "qtechFiberBiasStatus": qtechFiberBiasStatus,
       "qtechFiberChannel1Bias": qtechFiberChannel1Bias,
       "qtechFiberChannel1BiasStatus": qtechFiberChannel1BiasStatus,
       "qtechFiberChannel2Bias": qtechFiberChannel2Bias,
       "qtechFiberChannel2BiasStatus": qtechFiberChannel2BiasStatus,
       "qtechFiberChannel3Bias": qtechFiberChannel3Bias,
       "qtechFiberChannel3BiasStatus": qtechFiberChannel3BiasStatus,
       "qtechFiberChannel4Bias": qtechFiberChannel4Bias,
       "qtechFiberChannel4BiasStatus": qtechFiberChannel4BiasStatus,
       "qtechFiberRXpowerIntegerpart": qtechFiberRXpowerIntegerpart,
       "qtechFiberRXpowerDecimalpart": qtechFiberRXpowerDecimalpart,
       "qtechFiberRXpowertype": qtechFiberRXpowertype,
       "qtechFiberRXpowerStatus": qtechFiberRXpowerStatus,
       "qtechFiberChannel1RXpowerIntegerpart": qtechFiberChannel1RXpowerIntegerpart,
       "qtechFiberChannel1RXpowerDecimalpart": qtechFiberChannel1RXpowerDecimalpart,
       "qtechFiberChannel1RXpowertype": qtechFiberChannel1RXpowertype,
       "qtechFiberChannel1RXpowerStatus": qtechFiberChannel1RXpowerStatus,
       "qtechFiberChannel2RXpowerIntegerpart": qtechFiberChannel2RXpowerIntegerpart,
       "qtechFiberChannel2RXpowerDecimalpart": qtechFiberChannel2RXpowerDecimalpart,
       "qtechFiberChannel2RXpowertype": qtechFiberChannel2RXpowertype,
       "qtechFiberChannel2RXpowerStatus": qtechFiberChannel2RXpowerStatus,
       "qtechFiberChannel3RXpowerIntegerpart": qtechFiberChannel3RXpowerIntegerpart,
       "qtechFiberChannel3RXpowerDecimalpart": qtechFiberChannel3RXpowerDecimalpart,
       "qtechFiberChannel3RXpowertype": qtechFiberChannel3RXpowertype,
       "qtechFiberChannel3RXpowerStatus": qtechFiberChannel3RXpowerStatus,
       "qtechFiberChannel4RXpowerIntegerpart": qtechFiberChannel4RXpowerIntegerpart,
       "qtechFiberChannel4RXpowerDecimalpart": qtechFiberChannel4RXpowerDecimalpart,
       "qtechFiberChannel4RXpowertype": qtechFiberChannel4RXpowertype,
       "qtechFiberChannel4RXpowerStatus": qtechFiberChannel4RXpowerStatus,
       "qtechFiberTXpowerIntegerpart": qtechFiberTXpowerIntegerpart,
       "qtechFiberTXpowerDecimalpart": qtechFiberTXpowerDecimalpart,
       "qtechFiberTXpowerStatus": qtechFiberTXpowerStatus,
       "qtechFiberChannel1TXpowerIntegerpart": qtechFiberChannel1TXpowerIntegerpart,
       "qtechFiberChannel1TXpowerDecimalpart": qtechFiberChannel1TXpowerDecimalpart,
       "qtechFiberChannel1TXpowerStatus": qtechFiberChannel1TXpowerStatus,
       "qtechFiberChannel2TXpowerIntegerpart": qtechFiberChannel2TXpowerIntegerpart,
       "qtechFiberChannel2TXpowerDecimalpart": qtechFiberChannel2TXpowerDecimalpart,
       "qtechFiberChannel2TXpowerStatus": qtechFiberChannel2TXpowerStatus,
       "qtechFiberChannel3TXpowerIntegerpart": qtechFiberChannel3TXpowerIntegerpart,
       "qtechFiberChannel3TXpowerDecimalpart": qtechFiberChannel3TXpowerDecimalpart,
       "qtechFiberChannel3TXpowerStatus": qtechFiberChannel3TXpowerStatus,
       "qtechFiberChannel4TXpowerIntegerpart": qtechFiberChannel4TXpowerIntegerpart,
       "qtechFiberChannel4TXpowerDecimalpart": qtechFiberChannel4TXpowerDecimalpart,
       "qtechFiberChannel4TXpowerStatus": qtechFiberChannel4TXpowerStatus,
       "qtechFiberMIBConformance": qtechFiberMIBConformance,
       "qtechFiberMIBCompliances": qtechFiberMIBCompliances,
       "qtechFiberMIBConpliance": qtechFiberMIBConpliance,
       "qtechFiberMIBGroups": qtechFiberMIBGroups,
       "qtechFiberMIBGroup": qtechFiberMIBGroup}
)
