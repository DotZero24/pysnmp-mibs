# SNMP MIB module (TROPIC-ABSNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-ABSNODE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:54:16 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TnGmreOptLineImpCompModule,
 TnGmreOptLineImpEncoding) = mibBuilder.importSymbols(
    "TROPIC-ASON-MIB",
    "TnGmreOptLineImpCompModule",
    "TnGmreOptLineImpEncoding")

(tnAbsNodeMIB,
 tnAbsNodeMIBModules,
 tnAbsNodeObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAbsNodeMIB",
    "tnAbsNodeMIBModules",
    "tnAbsNodeObjs")


# MODULE-IDENTITY

tnAbsNodeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tnAbsNodeMibModule.setRevisions(
        ("2021-09-17 02:00",
         "2021-02-26 02:00",
         "2020-09-25 02:00",
         "2020-05-22 02:00",
         "2019-11-08 02:00",
         "2019-07-05 02:00",
         "2018-11-22 02:00",
         "2018-05-02 02:00",
         "2018-04-13 12:00",
         "2018-02-23 12:00",
         "2018-02-02 12:00",
         "2017-01-18 12:00",
         "2016-12-07 12:00",
         "2016-11-22 12:00",
         "2016-11-16 12:00",
         "2016-10-27 12:00",
         "2016-10-04 12:00",
         "2016-04-28 12:00",
         "2016-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnAbsNodeOpState(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("up", 1),
          ("down", 2),
          ("deg", 3))
    )



class TnAbsNodeAnalogBandwidth(TextualConvention, Integer32):
    status = "current"
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("otm-2p666", 1),
          ("otm-9p95328", 2),
          ("otm-10p3125", 3),
          ("otm-10p519", 4),
          ("otm-10p709", 5),
          ("otm-11p049", 6),
          ("otm-11p096", 7),
          ("otm-11p317", 8),
          ("otm-39p813", 9),
          ("otm-43p018", 10),
          ("otm-44p583", 11),
          ("otm-103p125", 12),
          ("otm-111p810", 13),
          ("otm-129p280", 14),
          ("otm-258p560", 15),
          ("otm-268p925", 16),
          ("otm-11p270", 17),
          ("otm-134p463", 18),
          ("otm-131p679", 19),
          ("otm-229p280", 20),
          ("otm-50", 21),
          ("otm-100", 22),
          ("otm-200", 23),
          ("otm-250", 24),
          ("otm-300", 25),
          ("otm-400", 26),
          ("otm-500", 27),
          ("otm-600", 28),
          ("otm-alien", 29))
    )



class TnAbsNodeChannelSpacing(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("cs-50-GHz", 1),
          ("cs-100-GHz", 2),
          ("cs-6p25-GHz", 3),
          ("cs-12p5-GHz", 4),
          ("cs-25-GHz", 5))
    )



class TnAbsNodeSlotWidth(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("sw-12p5-GHz", 1),
          ("sw-25-GHz", 2),
          ("sw-37p5-GHz", 3),
          ("sw-50-GHz", 4),
          ("sw-62p5-GHz", 5),
          ("sw-75-GHz", 6),
          ("sw-87p5-GHz", 7),
          ("sw-100-GHz", 8),
          ("sw-112p5-GHz", 9),
          ("sw-125-GHz", 10))
    )



class TnAbsNode3RType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("uni3r", 1),
          ("cross-regen", 2),
          ("b2b-regen", 3),
          ("lo-regen", 4),
          ("none", 5))
    )



class TnAbsNode3RConnType(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("uni", 1),
          ("bidi", 2),
          ("uni-no-recoloring", 3))
    )



class TnAbsNodeEndPointType(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("roadm", 1),
          ("ila", 2),
          ("roadm-wr20", 3),
          ("roadm-wr8-88AF", 4),
          ("single-wr20-DGE", 5),
          ("irdm32", 6),
          ("ir9", 7))
    )



class TnAbsNodeAddDropType(TextualConvention, Integer32):
    status = "current"
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("local", 1),
          ("configD", 2),
          ("configDprime", 3),
          ("configDdoublePrime", 4),
          ("mCS", 5),
          ("opsConfigD", 6),
          ("opsConfigDprime", 7),
          ("opsConfigDdoublePrime", 8),
          ("pscLocal", 9),
          ("pscCF", 10),
          ("mCS-AAR2X", 11),
          ("mCS-AAR2X-L", 12),
          ("sfd-iroadm", 13),
          ("opsMCS", 14),
          ("opsMCS-AAR2X", 15),
          ("mCS-HIGH", 16),
          ("mCS-AAR2X-HIGH", 17),
          ("mCS-AAR2X-L-HIGH", 18),
          ("cF-MLFSB", 19),
          ("mXN-ASC", 20),
          ("opsMXN-ASC", 21),
          ("mXN-ASC-L", 22),
          ("opsMXN-ASC-L", 23),
          ("mXN", 24),
          ("mXN-L", 25))
    )



class TnAbsNodeOtAseConstraint(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("standard", 1),
          ("low", 2),
          ("no-noise", 3),
          ("useNetworkConstraint", 4))
    )



class TnAbsNodeWaveTrackerCapability(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("keyedOnly", 1),
          ("unkeyedOnly", 2),
          ("keyedAndUnkeyed", 3))
    )



class TnAbsNodeTransponderType(TextualConvention, Integer32):
    status = "current"
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
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tt-4DPA4", 1),
          ("tt-11STAR1", 2),
          ("tt-11STGE12", 3),
          ("tt-11DPE12", 4),
          ("tt-11DPE12E", 5),
          ("tt-11QPA4", 6),
          ("tt-11STMM10", 7),
          ("tt-11DPM12", 8),
          ("tt-43STA1P", 9),
          ("tt-43STX4P", 10),
          ("tt-43STX4", 11),
          ("tt-43SCX4", 12),
          ("tt-112SCA1", 13),
          ("tt-112SCX10", 14),
          ("tt-11QTA4", 15),
          ("tt-43SCA1", 16),
          ("tt-112SNX10", 17),
          ("tt-112SNA1", 18),
          ("tt-11QCUP", 19),
          ("tt-43SCUP", 20),
          ("tt-11QPEN4", 21),
          ("tt-11QPE24", 22),
          ("tt-11DPE12A", 23),
          ("tt-11STAR1A", 24),
          ("tt-43SCX4E", 25),
          ("tt-43SCGE1", 26),
          ("tt-11QCUPC", 27),
          ("tt-130SCX10", 28),
          ("tt-130SCUP", 29),
          ("tt-130SNX10", 30),
          ("tt-130SCUPB", 31),
          ("tt-260SCX2", 32),
          ("tt-130SCUPC", 33),
          ("tt-11OPE8", 34),
          ("tt-11QCE12X", 35),
          ("tt-130SCA1", 36),
          ("tt-4UC400", 37),
          ("tt-2UC400", 38),
          ("tt-20UC200", 39),
          ("tt-11DPM8", 40),
          ("tt-130SNQ10", 41),
          ("tt-D5X500", 42),
          ("tt-1UD200", 43),
          ("tt-12P120", 44),
          ("tt-130SCUPH", 45),
          ("tt-S13X100R", 46),
          ("tt-S13X100E", 47),
          ("tt-11OCUP", 48),
          ("tt-D5X500L", 49),
          ("tt-1UX100", 50),
          ("tt-20AX200", 51),
          ("tt-20MX80", 52),
          ("tt-D5X500Q", 53),
          ("tt-130SLX10", 54),
          ("tt-130SLA1", 55),
          ("tt-S2AD200H", 56),
          ("tt-20AN80", 57),
          ("tt-DA2C4", 58),
          ("tt-LCI2000", 59),
          ("tt-LCI2000L", 60),
          ("tt-2UX200", 61),
          ("tt-S13X100L", 62),
          ("tt-4MX200", 63),
          ("tt-DA2C4E", 64),
          ("tt-S4X400H", 65),
          ("tt-S4X400E", 66),
          ("tt-S4X400L", 67),
          ("tt-DFC12", 68),
          ("tt-DFC12E", 69),
          ("tt-8UC1T", 70),
          ("tt-10AN1T", 71),
          ("tt-2UC400E", 72),
          ("tt-8P20", 73),
          ("tt-DFM6", 74),
          ("tt-DFM6E", 75),
          ("tt-4UC1T", 76),
          ("tt-S5AD400", 77),
          ("tt-S5AD400H", 78),
          ("tt-SFM6", 79),
          ("tt-DD2M4", 80),
          ("tt-STRING", 81))
    )



class TnAbsNodeIsPreparedForOps(TextualConvention, Integer32):
    status = "current"
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
        *(("invalid", 0),
          ("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnAbsNodeAttributeTotal_Type = Integer32
_TnAbsNodeAttributeTotal_Object = MibScalar
tnAbsNodeAttributeTotal = _TnAbsNodeAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 1),
    _TnAbsNodeAttributeTotal_Type()
)
tnAbsNodeAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeAttributeTotal.setStatus("current")
_TnAbsNodeSubnodeTable_Object = MibTable
tnAbsNodeSubnodeTable = _TnAbsNodeSubnodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeTable.setStatus("current")
_TnAbsNodeSubnodeEntry_Object = MibTableRow
tnAbsNodeSubnodeEntry = _TnAbsNodeSubnodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 2, 1)
)
tnAbsNodeSubnodeEntry.setIndexNames(
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeSubnodeLocalShelfId"),
)
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeEntry.setStatus("current")
_TnAbsNodeSubnodeLocalShelfId_Type = Unsigned32
_TnAbsNodeSubnodeLocalShelfId_Object = MibTableColumn
tnAbsNodeSubnodeLocalShelfId = _TnAbsNodeSubnodeLocalShelfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 2, 1, 1),
    _TnAbsNodeSubnodeLocalShelfId_Type()
)
tnAbsNodeSubnodeLocalShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeLocalShelfId.setStatus("current")
_TnAbsNodeSubnodeLocalDPNodeId_Type = Unsigned32
_TnAbsNodeSubnodeLocalDPNodeId_Object = MibTableColumn
tnAbsNodeSubnodeLocalDPNodeId = _TnAbsNodeSubnodeLocalDPNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 2, 1, 2),
    _TnAbsNodeSubnodeLocalDPNodeId_Type()
)
tnAbsNodeSubnodeLocalDPNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeLocalDPNodeId.setStatus("current")
_TnAbsNodeSubnodeNodalSrg_Type = Unsigned32
_TnAbsNodeSubnodeNodalSrg_Object = MibTableColumn
tnAbsNodeSubnodeNodalSrg = _TnAbsNodeSubnodeNodalSrg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 2, 1, 3),
    _TnAbsNodeSubnodeNodalSrg_Type()
)
tnAbsNodeSubnodeNodalSrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeNodalSrg.setStatus("current")
_TnAbsNodeSubnodeOpState_Type = TnAbsNodeOpState
_TnAbsNodeSubnodeOpState_Object = MibTableColumn
tnAbsNodeSubnodeOpState = _TnAbsNodeSubnodeOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 2, 1, 4),
    _TnAbsNodeSubnodeOpState_Type()
)
tnAbsNodeSubnodeOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeOpState.setStatus("current")
_TnAbsNodeTeLinkTable_Object = MibTable
tnAbsNodeTeLinkTable = _TnAbsNodeTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkTable.setStatus("current")
_TnAbsNodeTeLinkEntry_Object = MibTableRow
tnAbsNodeTeLinkEntry = _TnAbsNodeTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1)
)
tnAbsNodeTeLinkEntry.setIndexNames(
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkIfId"),
)
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkEntry.setStatus("current")
_TnAbsNodeTeLinkIfId_Type = Unsigned32
_TnAbsNodeTeLinkIfId_Object = MibTableColumn
tnAbsNodeTeLinkIfId = _TnAbsNodeTeLinkIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 1),
    _TnAbsNodeTeLinkIfId_Type()
)
tnAbsNodeTeLinkIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkIfId.setStatus("current")
_TnAbsNodeTeLinkRemoteIfId_Type = Unsigned32
_TnAbsNodeTeLinkRemoteIfId_Object = MibTableColumn
tnAbsNodeTeLinkRemoteIfId = _TnAbsNodeTeLinkRemoteIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 2),
    _TnAbsNodeTeLinkRemoteIfId_Type()
)
tnAbsNodeTeLinkRemoteIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkRemoteIfId.setStatus("current")
_TnAbsNodeTeLinkRemoteNodeAddress_Type = InetAddressIPv4
_TnAbsNodeTeLinkRemoteNodeAddress_Object = MibTableColumn
tnAbsNodeTeLinkRemoteNodeAddress = _TnAbsNodeTeLinkRemoteNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 3),
    _TnAbsNodeTeLinkRemoteNodeAddress_Type()
)
tnAbsNodeTeLinkRemoteNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkRemoteNodeAddress.setStatus("current")
_TnAbsNodeTeLinkUserLabel_Type = DisplayString
_TnAbsNodeTeLinkUserLabel_Object = MibTableColumn
tnAbsNodeTeLinkUserLabel = _TnAbsNodeTeLinkUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 4),
    _TnAbsNodeTeLinkUserLabel_Type()
)
tnAbsNodeTeLinkUserLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkUserLabel.setStatus("current")
_TnAbsNodeTeLinkMetric_Type = Unsigned32
_TnAbsNodeTeLinkMetric_Object = MibTableColumn
tnAbsNodeTeLinkMetric = _TnAbsNodeTeLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 5),
    _TnAbsNodeTeLinkMetric_Type()
)
tnAbsNodeTeLinkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkMetric.setStatus("current")
_TnAbsNodeTeLinkSrgIds_Type = DisplayString
_TnAbsNodeTeLinkSrgIds_Object = MibTableColumn
tnAbsNodeTeLinkSrgIds = _TnAbsNodeTeLinkSrgIds_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 6),
    _TnAbsNodeTeLinkSrgIds_Type()
)
tnAbsNodeTeLinkSrgIds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkSrgIds.setStatus("current")
_TnAbsNodeTeLinkColors_Type = Unsigned32
_TnAbsNodeTeLinkColors_Object = MibTableColumn
tnAbsNodeTeLinkColors = _TnAbsNodeTeLinkColors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 7),
    _TnAbsNodeTeLinkColors_Type()
)
tnAbsNodeTeLinkColors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkColors.setStatus("current")


class _TnAbsNodeTeLinkLatency_Type(Unsigned32):
    """Custom type tnAbsNodeTeLinkLatency based on Unsigned32"""
    defaultValue = 0


_TnAbsNodeTeLinkLatency_Type.__name__ = "Unsigned32"
_TnAbsNodeTeLinkLatency_Object = MibTableColumn
tnAbsNodeTeLinkLatency = _TnAbsNodeTeLinkLatency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 8),
    _TnAbsNodeTeLinkLatency_Type()
)
tnAbsNodeTeLinkLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkLatency.setStatus("current")
_TnAbsNodeTeLinkComponentIfIdList_Type = DisplayString
_TnAbsNodeTeLinkComponentIfIdList_Object = MibTableColumn
tnAbsNodeTeLinkComponentIfIdList = _TnAbsNodeTeLinkComponentIfIdList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 9),
    _TnAbsNodeTeLinkComponentIfIdList_Type()
)
tnAbsNodeTeLinkComponentIfIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkComponentIfIdList.setStatus("current")
_TnAbsNodeTeLinkRowStatus_Type = RowStatus
_TnAbsNodeTeLinkRowStatus_Object = MibTableColumn
tnAbsNodeTeLinkRowStatus = _TnAbsNodeTeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 3, 1, 10),
    _TnAbsNodeTeLinkRowStatus_Type()
)
tnAbsNodeTeLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkRowStatus.setStatus("current")
_TnAbsNodeOtsPortTable_Object = MibTable
tnAbsNodeOtsPortTable = _TnAbsNodeOtsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4)
)
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortTable.setStatus("current")
_TnAbsNodeOtsPortEntry_Object = MibTableRow
tnAbsNodeOtsPortEntry = _TnAbsNodeOtsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1)
)
tnAbsNodeOtsPortEntry.setIndexNames(
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortIfId"),
)
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortEntry.setStatus("current")
_TnAbsNodeOtsPortIfId_Type = Unsigned32
_TnAbsNodeOtsPortIfId_Object = MibTableColumn
tnAbsNodeOtsPortIfId = _TnAbsNodeOtsPortIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 1),
    _TnAbsNodeOtsPortIfId_Type()
)
tnAbsNodeOtsPortIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortIfId.setStatus("current")
_TnAbsNodeOtsPortNeIfIndex_Type = InterfaceIndex
_TnAbsNodeOtsPortNeIfIndex_Object = MibTableColumn
tnAbsNodeOtsPortNeIfIndex = _TnAbsNodeOtsPortNeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 2),
    _TnAbsNodeOtsPortNeIfIndex_Type()
)
tnAbsNodeOtsPortNeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortNeIfIndex.setStatus("current")
_TnAbsNodeOtsPortLocalShelfId_Type = Unsigned32
_TnAbsNodeOtsPortLocalShelfId_Object = MibTableColumn
tnAbsNodeOtsPortLocalShelfId = _TnAbsNodeOtsPortLocalShelfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 3),
    _TnAbsNodeOtsPortLocalShelfId_Type()
)
tnAbsNodeOtsPortLocalShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortLocalShelfId.setStatus("current")
_TnAbsNodeOtsPortRemoteIfId_Type = Unsigned32
_TnAbsNodeOtsPortRemoteIfId_Object = MibTableColumn
tnAbsNodeOtsPortRemoteIfId = _TnAbsNodeOtsPortRemoteIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 4),
    _TnAbsNodeOtsPortRemoteIfId_Type()
)
tnAbsNodeOtsPortRemoteIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortRemoteIfId.setStatus("current")
_TnAbsNodeOtsPortRemoteNodeAddress_Type = InetAddressIPv4
_TnAbsNodeOtsPortRemoteNodeAddress_Object = MibTableColumn
tnAbsNodeOtsPortRemoteNodeAddress = _TnAbsNodeOtsPortRemoteNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 5),
    _TnAbsNodeOtsPortRemoteNodeAddress_Type()
)
tnAbsNodeOtsPortRemoteNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortRemoteNodeAddress.setStatus("current")
_TnAbsNodeOtsPortRemoteOtsPortIfId_Type = Unsigned32
_TnAbsNodeOtsPortRemoteOtsPortIfId_Object = MibTableColumn
tnAbsNodeOtsPortRemoteOtsPortIfId = _TnAbsNodeOtsPortRemoteOtsPortIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 6),
    _TnAbsNodeOtsPortRemoteOtsPortIfId_Type()
)
tnAbsNodeOtsPortRemoteOtsPortIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortRemoteOtsPortIfId.setStatus("current")
_TnAbsNodeOtsPortUserLabel_Type = DisplayString
_TnAbsNodeOtsPortUserLabel_Object = MibTableColumn
tnAbsNodeOtsPortUserLabel = _TnAbsNodeOtsPortUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 7),
    _TnAbsNodeOtsPortUserLabel_Type()
)
tnAbsNodeOtsPortUserLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortUserLabel.setStatus("current")
_TnAbsNodeOtsPortCentralFrequencyGranularity_Type = TnAbsNodeChannelSpacing
_TnAbsNodeOtsPortCentralFrequencyGranularity_Object = MibTableColumn
tnAbsNodeOtsPortCentralFrequencyGranularity = _TnAbsNodeOtsPortCentralFrequencyGranularity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 8),
    _TnAbsNodeOtsPortCentralFrequencyGranularity_Type()
)
tnAbsNodeOtsPortCentralFrequencyGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortCentralFrequencyGranularity.setStatus("current")
_TnAbsNodeOtsPortSlotWidthGranularity_Type = TnAbsNodeSlotWidth
_TnAbsNodeOtsPortSlotWidthGranularity_Object = MibTableColumn
tnAbsNodeOtsPortSlotWidthGranularity = _TnAbsNodeOtsPortSlotWidthGranularity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 9),
    _TnAbsNodeOtsPortSlotWidthGranularity_Type()
)
tnAbsNodeOtsPortSlotWidthGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortSlotWidthGranularity.setStatus("current")
_TnAbsNodeOtsPortMinSlotWidth_Type = TnAbsNodeSlotWidth
_TnAbsNodeOtsPortMinSlotWidth_Object = MibTableColumn
tnAbsNodeOtsPortMinSlotWidth = _TnAbsNodeOtsPortMinSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 10),
    _TnAbsNodeOtsPortMinSlotWidth_Type()
)
tnAbsNodeOtsPortMinSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortMinSlotWidth.setStatus("current")
_TnAbsNodeOtsPortMaxSlotWidth_Type = TnAbsNodeSlotWidth
_TnAbsNodeOtsPortMaxSlotWidth_Object = MibTableColumn
tnAbsNodeOtsPortMaxSlotWidth = _TnAbsNodeOtsPortMaxSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 11),
    _TnAbsNodeOtsPortMaxSlotWidth_Type()
)
tnAbsNodeOtsPortMaxSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortMaxSlotWidth.setStatus("current")
_TnAbsNodeOtsPortMinChannel_Type = Integer32
_TnAbsNodeOtsPortMinChannel_Object = MibTableColumn
tnAbsNodeOtsPortMinChannel = _TnAbsNodeOtsPortMinChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 12),
    _TnAbsNodeOtsPortMinChannel_Type()
)
tnAbsNodeOtsPortMinChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortMinChannel.setStatus("current")
_TnAbsNodeOtsPortMaxChannel_Type = Integer32
_TnAbsNodeOtsPortMaxChannel_Object = MibTableColumn
tnAbsNodeOtsPortMaxChannel = _TnAbsNodeOtsPortMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 13),
    _TnAbsNodeOtsPortMaxChannel_Type()
)
tnAbsNodeOtsPortMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortMaxChannel.setStatus("current")
_TnAbsNodeOtsPortWssGranularity_Type = TnAbsNodeChannelSpacing
_TnAbsNodeOtsPortWssGranularity_Object = MibTableColumn
tnAbsNodeOtsPortWssGranularity = _TnAbsNodeOtsPortWssGranularity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 14),
    _TnAbsNodeOtsPortWssGranularity_Type()
)
tnAbsNodeOtsPortWssGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortWssGranularity.setStatus("current")
_TnAbsNodeOtsPortEndPointType_Type = TnAbsNodeEndPointType
_TnAbsNodeOtsPortEndPointType_Object = MibTableColumn
tnAbsNodeOtsPortEndPointType = _TnAbsNodeOtsPortEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 15),
    _TnAbsNodeOtsPortEndPointType_Type()
)
tnAbsNodeOtsPortEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortEndPointType.setStatus("current")
_TnAbsNodeOtsPortOpState_Type = TnAbsNodeOpState
_TnAbsNodeOtsPortOpState_Object = MibTableColumn
tnAbsNodeOtsPortOpState = _TnAbsNodeOtsPortOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 16),
    _TnAbsNodeOtsPortOpState_Type()
)
tnAbsNodeOtsPortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortOpState.setStatus("current")
_TnAbsNodeOtsPortIsPreparedForOps_Type = TnAbsNodeIsPreparedForOps
_TnAbsNodeOtsPortIsPreparedForOps_Object = MibTableColumn
tnAbsNodeOtsPortIsPreparedForOps = _TnAbsNodeOtsPortIsPreparedForOps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 4, 1, 17),
    _TnAbsNodeOtsPortIsPreparedForOps_Type()
)
tnAbsNodeOtsPortIsPreparedForOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortIsPreparedForOps.setStatus("current")
_TnAbsNodeIfGroupTable_Object = MibTable
tnAbsNodeIfGroupTable = _TnAbsNodeIfGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5)
)
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupTable.setStatus("current")
_TnAbsNodeIfGroupEntry_Object = MibTableRow
tnAbsNodeIfGroupEntry = _TnAbsNodeIfGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1)
)
tnAbsNodeIfGroupEntry.setIndexNames(
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupIfId"),
)
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupEntry.setStatus("current")
_TnAbsNodeIfGroupIfId_Type = Unsigned32
_TnAbsNodeIfGroupIfId_Object = MibTableColumn
tnAbsNodeIfGroupIfId = _TnAbsNodeIfGroupIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 1),
    _TnAbsNodeIfGroupIfId_Type()
)
tnAbsNodeIfGroupIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupIfId.setStatus("current")
_TnAbsNodeIfGroupCentralFrequencyGranularity_Type = TnAbsNodeChannelSpacing
_TnAbsNodeIfGroupCentralFrequencyGranularity_Object = MibTableColumn
tnAbsNodeIfGroupCentralFrequencyGranularity = _TnAbsNodeIfGroupCentralFrequencyGranularity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 2),
    _TnAbsNodeIfGroupCentralFrequencyGranularity_Type()
)
tnAbsNodeIfGroupCentralFrequencyGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupCentralFrequencyGranularity.setStatus("current")
_TnAbsNodeIfGroupSlotWidthGranularity_Type = TnAbsNodeSlotWidth
_TnAbsNodeIfGroupSlotWidthGranularity_Object = MibTableColumn
tnAbsNodeIfGroupSlotWidthGranularity = _TnAbsNodeIfGroupSlotWidthGranularity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 3),
    _TnAbsNodeIfGroupSlotWidthGranularity_Type()
)
tnAbsNodeIfGroupSlotWidthGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupSlotWidthGranularity.setStatus("current")
_TnAbsNodeIfGroupMinSlotWidth_Type = TnAbsNodeSlotWidth
_TnAbsNodeIfGroupMinSlotWidth_Object = MibTableColumn
tnAbsNodeIfGroupMinSlotWidth = _TnAbsNodeIfGroupMinSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 4),
    _TnAbsNodeIfGroupMinSlotWidth_Type()
)
tnAbsNodeIfGroupMinSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupMinSlotWidth.setStatus("current")
_TnAbsNodeIfGroupMaxSlotWidth_Type = TnAbsNodeSlotWidth
_TnAbsNodeIfGroupMaxSlotWidth_Object = MibTableColumn
tnAbsNodeIfGroupMaxSlotWidth = _TnAbsNodeIfGroupMaxSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 5),
    _TnAbsNodeIfGroupMaxSlotWidth_Type()
)
tnAbsNodeIfGroupMaxSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupMaxSlotWidth.setStatus("current")
_TnAbsNodeIfGroupMinChannel_Type = Integer32
_TnAbsNodeIfGroupMinChannel_Object = MibTableColumn
tnAbsNodeIfGroupMinChannel = _TnAbsNodeIfGroupMinChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 6),
    _TnAbsNodeIfGroupMinChannel_Type()
)
tnAbsNodeIfGroupMinChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupMinChannel.setStatus("current")
_TnAbsNodeIfGroupMaxChannel_Type = Integer32
_TnAbsNodeIfGroupMaxChannel_Object = MibTableColumn
tnAbsNodeIfGroupMaxChannel = _TnAbsNodeIfGroupMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 7),
    _TnAbsNodeIfGroupMaxChannel_Type()
)
tnAbsNodeIfGroupMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupMaxChannel.setStatus("current")
_TnAbsNodeIfGroupWssGranularity_Type = TnAbsNodeChannelSpacing
_TnAbsNodeIfGroupWssGranularity_Object = MibTableColumn
tnAbsNodeIfGroupWssGranularity = _TnAbsNodeIfGroupWssGranularity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 8),
    _TnAbsNodeIfGroupWssGranularity_Type()
)
tnAbsNodeIfGroupWssGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupWssGranularity.setStatus("current")
_TnAbsNodeIfGroupAdType_Type = TnAbsNodeAddDropType
_TnAbsNodeIfGroupAdType_Object = MibTableColumn
tnAbsNodeIfGroupAdType = _TnAbsNodeIfGroupAdType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 9),
    _TnAbsNodeIfGroupAdType_Type()
)
tnAbsNodeIfGroupAdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupAdType.setStatus("current")
_TnAbsNodeIfGroupOtAseConst_Type = TnAbsNodeOtAseConstraint
_TnAbsNodeIfGroupOtAseConst_Object = MibTableColumn
tnAbsNodeIfGroupOtAseConst = _TnAbsNodeIfGroupOtAseConst_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 5, 1, 10),
    _TnAbsNodeIfGroupOtAseConst_Type()
)
tnAbsNodeIfGroupOtAseConst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupOtAseConst.setStatus("current")
_TnAbsNodeOtLinePortTable_Object = MibTable
tnAbsNodeOtLinePortTable = _TnAbsNodeOtLinePortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6)
)
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortTable.setStatus("current")
_TnAbsNodeOtLinePortEntry_Object = MibTableRow
tnAbsNodeOtLinePortEntry = _TnAbsNodeOtLinePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1)
)
tnAbsNodeOtLinePortEntry.setIndexNames(
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortIfId"),
)
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortEntry.setStatus("current")
_TnAbsNodeOtLinePortIfId_Type = Unsigned32
_TnAbsNodeOtLinePortIfId_Object = MibTableColumn
tnAbsNodeOtLinePortIfId = _TnAbsNodeOtLinePortIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 1),
    _TnAbsNodeOtLinePortIfId_Type()
)
tnAbsNodeOtLinePortIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortIfId.setStatus("current")
_TnAbsNodeOtLinePortRemoteUplinkNodeAddress_Type = InetAddressIPv4
_TnAbsNodeOtLinePortRemoteUplinkNodeAddress_Object = MibTableColumn
tnAbsNodeOtLinePortRemoteUplinkNodeAddress = _TnAbsNodeOtLinePortRemoteUplinkNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 2),
    _TnAbsNodeOtLinePortRemoteUplinkNodeAddress_Type()
)
tnAbsNodeOtLinePortRemoteUplinkNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortRemoteUplinkNodeAddress.setStatus("current")
_TnAbsNodeOtLinePortRemoteUplinkPortIfId_Type = Unsigned32
_TnAbsNodeOtLinePortRemoteUplinkPortIfId_Object = MibTableColumn
tnAbsNodeOtLinePortRemoteUplinkPortIfId = _TnAbsNodeOtLinePortRemoteUplinkPortIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 3),
    _TnAbsNodeOtLinePortRemoteUplinkPortIfId_Type()
)
tnAbsNodeOtLinePortRemoteUplinkPortIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortRemoteUplinkPortIfId.setStatus("current")
_TnAbsNodeOtLinePortPhysicalClientPortIfIds_Type = DisplayString
_TnAbsNodeOtLinePortPhysicalClientPortIfIds_Object = MibTableColumn
tnAbsNodeOtLinePortPhysicalClientPortIfIds = _TnAbsNodeOtLinePortPhysicalClientPortIfIds_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 4),
    _TnAbsNodeOtLinePortPhysicalClientPortIfIds_Type()
)
tnAbsNodeOtLinePortPhysicalClientPortIfIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortPhysicalClientPortIfIds.setStatus("current")
_TnAbsNodeOtLinePortLocalShelfId_Type = Unsigned32
_TnAbsNodeOtLinePortLocalShelfId_Object = MibTableColumn
tnAbsNodeOtLinePortLocalShelfId = _TnAbsNodeOtLinePortLocalShelfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 5),
    _TnAbsNodeOtLinePortLocalShelfId_Type()
)
tnAbsNodeOtLinePortLocalShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortLocalShelfId.setStatus("current")
_TnAbsNodeOtLinePortIfGroupIfId_Type = Unsigned32
_TnAbsNodeOtLinePortIfGroupIfId_Object = MibTableColumn
tnAbsNodeOtLinePortIfGroupIfId = _TnAbsNodeOtLinePortIfGroupIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 6),
    _TnAbsNodeOtLinePortIfGroupIfId_Type()
)
tnAbsNodeOtLinePortIfGroupIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortIfGroupIfId.setStatus("current")
_TnAbsNodeOtLinePortSubGroupIfId_Type = Unsigned32
_TnAbsNodeOtLinePortSubGroupIfId_Object = MibTableColumn
tnAbsNodeOtLinePortSubGroupIfId = _TnAbsNodeOtLinePortSubGroupIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 7),
    _TnAbsNodeOtLinePortSubGroupIfId_Type()
)
tnAbsNodeOtLinePortSubGroupIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSubGroupIfId.setStatus("current")
_TnAbsNodeOtLinePortIsOpsProtected_Type = TruthValue
_TnAbsNodeOtLinePortIsOpsProtected_Object = MibTableColumn
tnAbsNodeOtLinePortIsOpsProtected = _TnAbsNodeOtLinePortIsOpsProtected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 8),
    _TnAbsNodeOtLinePortIsOpsProtected_Type()
)
tnAbsNodeOtLinePortIsOpsProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortIsOpsProtected.setStatus("current")
_TnAbsNodeOtLinePortSpareIfGroupIfId_Type = Unsigned32
_TnAbsNodeOtLinePortSpareIfGroupIfId_Object = MibTableColumn
tnAbsNodeOtLinePortSpareIfGroupIfId = _TnAbsNodeOtLinePortSpareIfGroupIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 9),
    _TnAbsNodeOtLinePortSpareIfGroupIfId_Type()
)
tnAbsNodeOtLinePortSpareIfGroupIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSpareIfGroupIfId.setStatus("current")
_TnAbsNodeOtLinePortSpareSubGroupIfId_Type = Unsigned32
_TnAbsNodeOtLinePortSpareSubGroupIfId_Object = MibTableColumn
tnAbsNodeOtLinePortSpareSubGroupIfId = _TnAbsNodeOtLinePortSpareSubGroupIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 10),
    _TnAbsNodeOtLinePortSpareSubGroupIfId_Type()
)
tnAbsNodeOtLinePortSpareSubGroupIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSpareSubGroupIfId.setStatus("current")
_TnAbsNodeOtLinePortModType_Type = TnGmreOptLineImpEncoding
_TnAbsNodeOtLinePortModType_Object = MibTableColumn
tnAbsNodeOtLinePortModType = _TnAbsNodeOtLinePortModType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 11),
    _TnAbsNodeOtLinePortModType_Type()
)
tnAbsNodeOtLinePortModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortModType.setStatus("current")
_TnAbsNodeOtLinePortAnalogBw_Type = TnAbsNodeAnalogBandwidth
_TnAbsNodeOtLinePortAnalogBw_Object = MibTableColumn
tnAbsNodeOtLinePortAnalogBw = _TnAbsNodeOtLinePortAnalogBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 12),
    _TnAbsNodeOtLinePortAnalogBw_Type()
)
tnAbsNodeOtLinePortAnalogBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortAnalogBw.setStatus("current")
_TnAbsNodeOtLinePortCompMode_Type = TnGmreOptLineImpCompModule
_TnAbsNodeOtLinePortCompMode_Object = MibTableColumn
tnAbsNodeOtLinePortCompMode = _TnAbsNodeOtLinePortCompMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 13),
    _TnAbsNodeOtLinePortCompMode_Type()
)
tnAbsNodeOtLinePortCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortCompMode.setStatus("current")
_TnAbsNodeOtLinePortFecTypes_Type = DisplayString
_TnAbsNodeOtLinePortFecTypes_Object = MibTableColumn
tnAbsNodeOtLinePortFecTypes = _TnAbsNodeOtLinePortFecTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 14),
    _TnAbsNodeOtLinePortFecTypes_Type()
)
tnAbsNodeOtLinePortFecTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortFecTypes.setStatus("current")
_TnAbsNodeOtLinePortServiceWidth_Type = TnAbsNodeSlotWidth
_TnAbsNodeOtLinePortServiceWidth_Object = MibTableColumn
tnAbsNodeOtLinePortServiceWidth = _TnAbsNodeOtLinePortServiceWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 15),
    _TnAbsNodeOtLinePortServiceWidth_Type()
)
tnAbsNodeOtLinePortServiceWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortServiceWidth.setStatus("current")
_TnAbsNodeOtLinePortMinChannel_Type = Integer32
_TnAbsNodeOtLinePortMinChannel_Object = MibTableColumn
tnAbsNodeOtLinePortMinChannel = _TnAbsNodeOtLinePortMinChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 16),
    _TnAbsNodeOtLinePortMinChannel_Type()
)
tnAbsNodeOtLinePortMinChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortMinChannel.setStatus("current")
_TnAbsNodeOtLinePortMaxChannel_Type = Integer32
_TnAbsNodeOtLinePortMaxChannel_Object = MibTableColumn
tnAbsNodeOtLinePortMaxChannel = _TnAbsNodeOtLinePortMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 17),
    _TnAbsNodeOtLinePortMaxChannel_Type()
)
tnAbsNodeOtLinePortMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortMaxChannel.setStatus("current")
_TnAbsNodeOtLinePortChanStep_Type = Unsigned32
_TnAbsNodeOtLinePortChanStep_Object = MibTableColumn
tnAbsNodeOtLinePortChanStep = _TnAbsNodeOtLinePortChanStep_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 18),
    _TnAbsNodeOtLinePortChanStep_Type()
)
tnAbsNodeOtLinePortChanStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortChanStep.setStatus("current")
_TnAbsNodeOtLinePortHas100GHzSubGroupWidth_Type = TruthValue
_TnAbsNodeOtLinePortHas100GHzSubGroupWidth_Object = MibTableColumn
tnAbsNodeOtLinePortHas100GHzSubGroupWidth = _TnAbsNodeOtLinePortHas100GHzSubGroupWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 19),
    _TnAbsNodeOtLinePortHas100GHzSubGroupWidth_Type()
)
tnAbsNodeOtLinePortHas100GHzSubGroupWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortHas100GHzSubGroupWidth.setStatus("current")
_TnAbsNodeOtLinePort3RType_Type = TnAbsNode3RType
_TnAbsNodeOtLinePort3RType_Object = MibTableColumn
tnAbsNodeOtLinePort3RType = _TnAbsNodeOtLinePort3RType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 21),
    _TnAbsNodeOtLinePort3RType_Type()
)
tnAbsNodeOtLinePort3RType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePort3RType.setStatus("current")
_TnAbsNodeOtLinePortConnectedIfId_Type = Unsigned32
_TnAbsNodeOtLinePortConnectedIfId_Object = MibTableColumn
tnAbsNodeOtLinePortConnectedIfId = _TnAbsNodeOtLinePortConnectedIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 22),
    _TnAbsNodeOtLinePortConnectedIfId_Type()
)
tnAbsNodeOtLinePortConnectedIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortConnectedIfId.setStatus("current")
_TnAbsNodeOtLinePort3RConnType_Type = TnAbsNode3RConnType
_TnAbsNodeOtLinePort3RConnType_Object = MibTableColumn
tnAbsNodeOtLinePort3RConnType = _TnAbsNodeOtLinePort3RConnType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 23),
    _TnAbsNodeOtLinePort3RConnType_Type()
)
tnAbsNodeOtLinePort3RConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePort3RConnType.setStatus("current")
_TnAbsNodeOtLinePortOpState_Type = TnAbsNodeOpState
_TnAbsNodeOtLinePortOpState_Object = MibTableColumn
tnAbsNodeOtLinePortOpState = _TnAbsNodeOtLinePortOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 24),
    _TnAbsNodeOtLinePortOpState_Type()
)
tnAbsNodeOtLinePortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortOpState.setStatus("current")
_TnAbsNodeOtLinePortAddDropPort_Type = DisplayString
_TnAbsNodeOtLinePortAddDropPort_Object = MibTableColumn
tnAbsNodeOtLinePortAddDropPort = _TnAbsNodeOtLinePortAddDropPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 25),
    _TnAbsNodeOtLinePortAddDropPort_Type()
)
tnAbsNodeOtLinePortAddDropPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortAddDropPort.setStatus("current")
_TnAbsNodeOtLinePortAddDropSparePort_Type = DisplayString
_TnAbsNodeOtLinePortAddDropSparePort_Object = MibTableColumn
tnAbsNodeOtLinePortAddDropSparePort = _TnAbsNodeOtLinePortAddDropSparePort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 26),
    _TnAbsNodeOtLinePortAddDropSparePort_Type()
)
tnAbsNodeOtLinePortAddDropSparePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortAddDropSparePort.setStatus("current")
_TnAbsNodeOtLinePortAddDropOpsPort_Type = DisplayString
_TnAbsNodeOtLinePortAddDropOpsPort_Object = MibTableColumn
tnAbsNodeOtLinePortAddDropOpsPort = _TnAbsNodeOtLinePortAddDropOpsPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 27),
    _TnAbsNodeOtLinePortAddDropOpsPort_Type()
)
tnAbsNodeOtLinePortAddDropOpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortAddDropOpsPort.setStatus("current")
_TnAbsNodeOtLinePortTransponderType_Type = TnAbsNodeTransponderType
_TnAbsNodeOtLinePortTransponderType_Object = MibTableColumn
tnAbsNodeOtLinePortTransponderType = _TnAbsNodeOtLinePortTransponderType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 28),
    _TnAbsNodeOtLinePortTransponderType_Type()
)
tnAbsNodeOtLinePortTransponderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortTransponderType.setStatus("current")
_TnAbsNodeOtLinePortMinDropPower_Type = Integer32
_TnAbsNodeOtLinePortMinDropPower_Object = MibTableColumn
tnAbsNodeOtLinePortMinDropPower = _TnAbsNodeOtLinePortMinDropPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 29),
    _TnAbsNodeOtLinePortMinDropPower_Type()
)
tnAbsNodeOtLinePortMinDropPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortMinDropPower.setStatus("current")
_TnAbsNodeOtLinePortSpareMinDropPower_Type = Integer32
_TnAbsNodeOtLinePortSpareMinDropPower_Object = MibTableColumn
tnAbsNodeOtLinePortSpareMinDropPower = _TnAbsNodeOtLinePortSpareMinDropPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 30),
    _TnAbsNodeOtLinePortSpareMinDropPower_Type()
)
tnAbsNodeOtLinePortSpareMinDropPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSpareMinDropPower.setStatus("current")
_TnAbsNodeOtLinePortIsr_Type = Integer32
_TnAbsNodeOtLinePortIsr_Object = MibTableColumn
tnAbsNodeOtLinePortIsr = _TnAbsNodeOtLinePortIsr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 31),
    _TnAbsNodeOtLinePortIsr_Type()
)
tnAbsNodeOtLinePortIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortIsr.setStatus("current")
_TnAbsNodeOtLinePortSpareIsr_Type = Integer32
_TnAbsNodeOtLinePortSpareIsr_Object = MibTableColumn
tnAbsNodeOtLinePortSpareIsr = _TnAbsNodeOtLinePortSpareIsr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 32),
    _TnAbsNodeOtLinePortSpareIsr_Type()
)
tnAbsNodeOtLinePortSpareIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSpareIsr.setStatus("current")
_TnAbsNodeOtLinePortPhaseEncodeTypes_Type = DisplayString
_TnAbsNodeOtLinePortPhaseEncodeTypes_Object = MibTableColumn
tnAbsNodeOtLinePortPhaseEncodeTypes = _TnAbsNodeOtLinePortPhaseEncodeTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 33),
    _TnAbsNodeOtLinePortPhaseEncodeTypes_Type()
)
tnAbsNodeOtLinePortPhaseEncodeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortPhaseEncodeTypes.setStatus("current")
_TnAbsNodeOtLinePortHasPhaseEncodeDep_Type = TruthValue
_TnAbsNodeOtLinePortHasPhaseEncodeDep_Object = MibTableColumn
tnAbsNodeOtLinePortHasPhaseEncodeDep = _TnAbsNodeOtLinePortHasPhaseEncodeDep_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 34),
    _TnAbsNodeOtLinePortHasPhaseEncodeDep_Type()
)
tnAbsNodeOtLinePortHasPhaseEncodeDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortHasPhaseEncodeDep.setStatus("current")
_TnAbsNodeOtLinePortSamePhaseEncodePortId_Type = Unsigned32
_TnAbsNodeOtLinePortSamePhaseEncodePortId_Object = MibTableColumn
tnAbsNodeOtLinePortSamePhaseEncodePortId = _TnAbsNodeOtLinePortSamePhaseEncodePortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 35),
    _TnAbsNodeOtLinePortSamePhaseEncodePortId_Type()
)
tnAbsNodeOtLinePortSamePhaseEncodePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSamePhaseEncodePortId.setStatus("current")
_TnAbsNodeOtLinePortMinDropPowerP2_Type = Integer32
_TnAbsNodeOtLinePortMinDropPowerP2_Object = MibTableColumn
tnAbsNodeOtLinePortMinDropPowerP2 = _TnAbsNodeOtLinePortMinDropPowerP2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 36),
    _TnAbsNodeOtLinePortMinDropPowerP2_Type()
)
tnAbsNodeOtLinePortMinDropPowerP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortMinDropPowerP2.setStatus("current")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortMinDropPowerP2.setUnits("mBm")
_TnAbsNodeOtLinePortWaveTrackerCap_Type = TnAbsNodeWaveTrackerCapability
_TnAbsNodeOtLinePortWaveTrackerCap_Object = MibTableColumn
tnAbsNodeOtLinePortWaveTrackerCap = _TnAbsNodeOtLinePortWaveTrackerCap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 38),
    _TnAbsNodeOtLinePortWaveTrackerCap_Type()
)
tnAbsNodeOtLinePortWaveTrackerCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortWaveTrackerCap.setStatus("current")
_TnAbsNodeOtLinePortSpareMinDropPowerP2_Type = Integer32
_TnAbsNodeOtLinePortSpareMinDropPowerP2_Object = MibTableColumn
tnAbsNodeOtLinePortSpareMinDropPowerP2 = _TnAbsNodeOtLinePortSpareMinDropPowerP2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 39),
    _TnAbsNodeOtLinePortSpareMinDropPowerP2_Type()
)
tnAbsNodeOtLinePortSpareMinDropPowerP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSpareMinDropPowerP2.setStatus("current")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSpareMinDropPowerP2.setUnits("mBm")
_TnAbsNodeOtLinePortOtuSignalTypes_Type = DisplayString
_TnAbsNodeOtLinePortOtuSignalTypes_Object = MibTableColumn
tnAbsNodeOtLinePortOtuSignalTypes = _TnAbsNodeOtLinePortOtuSignalTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 40),
    _TnAbsNodeOtLinePortOtuSignalTypes_Type()
)
tnAbsNodeOtLinePortOtuSignalTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortOtuSignalTypes.setStatus("current")
_TnAbsNodeOtLinePortTransponderString_Type = DisplayString
_TnAbsNodeOtLinePortTransponderString_Object = MibTableColumn
tnAbsNodeOtLinePortTransponderString = _TnAbsNodeOtLinePortTransponderString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 41),
    _TnAbsNodeOtLinePortTransponderString_Type()
)
tnAbsNodeOtLinePortTransponderString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortTransponderString.setStatus("current")
_TnAbsNodeOtLinePortSupportedServiceWidths_Type = DisplayString
_TnAbsNodeOtLinePortSupportedServiceWidths_Object = MibTableColumn
tnAbsNodeOtLinePortSupportedServiceWidths = _TnAbsNodeOtLinePortSupportedServiceWidths_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 6, 1, 42),
    _TnAbsNodeOtLinePortSupportedServiceWidths_Type()
)
tnAbsNodeOtLinePortSupportedServiceWidths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortSupportedServiceWidths.setStatus("current")
_TnAbsNodeConnectivityTable_Object = MibTable
tnAbsNodeConnectivityTable = _TnAbsNodeConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 7)
)
if mibBuilder.loadTexts:
    tnAbsNodeConnectivityTable.setStatus("current")
_TnAbsNodeConnectivityEntry_Object = MibTableRow
tnAbsNodeConnectivityEntry = _TnAbsNodeConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 7, 1)
)
tnAbsNodeConnectivityEntry.setIndexNames(
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeConnectivityFromIfId"),
    (0, "TROPIC-ABSNODE-MIB", "tnAbsNodeConnectivityToIfId"),
)
if mibBuilder.loadTexts:
    tnAbsNodeConnectivityEntry.setStatus("current")
_TnAbsNodeConnectivityFromIfId_Type = Unsigned32
_TnAbsNodeConnectivityFromIfId_Object = MibTableColumn
tnAbsNodeConnectivityFromIfId = _TnAbsNodeConnectivityFromIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 7, 1, 1),
    _TnAbsNodeConnectivityFromIfId_Type()
)
tnAbsNodeConnectivityFromIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeConnectivityFromIfId.setStatus("current")
_TnAbsNodeConnectivityToIfId_Type = Unsigned32
_TnAbsNodeConnectivityToIfId_Object = MibTableColumn
tnAbsNodeConnectivityToIfId = _TnAbsNodeConnectivityToIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 7, 1, 2),
    _TnAbsNodeConnectivityToIfId_Type()
)
tnAbsNodeConnectivityToIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAbsNodeConnectivityToIfId.setStatus("current")
_TnAbsNodeConnectivityOpState_Type = TnAbsNodeOpState
_TnAbsNodeConnectivityOpState_Object = MibTableColumn
tnAbsNodeConnectivityOpState = _TnAbsNodeConnectivityOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1, 7, 1, 3),
    _TnAbsNodeConnectivityOpState_Type()
)
tnAbsNodeConnectivityOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAbsNodeConnectivityOpState.setStatus("current")
_TnAbsNodeConf_ObjectIdentity = ObjectIdentity
tnAbsNodeConf = _TnAbsNodeConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3)
)
_TnAbsNodeGroups_ObjectIdentity = ObjectIdentity
tnAbsNodeGroups = _TnAbsNodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1)
)
_TnAbsNodeCompliances_ObjectIdentity = ObjectIdentity
tnAbsNodeCompliances = _TnAbsNodeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 2)
)

# Managed Objects groups

tnAbsNodeObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 1)
)
tnAbsNodeObjsGroup.setObjects(
    ("TROPIC-ABSNODE-MIB", "tnAbsNodeAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAbsNodeObjsGroup.setStatus("current")

tnAbsNodeSubnodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 2)
)
tnAbsNodeSubnodeGroup.setObjects(
      *(("TROPIC-ABSNODE-MIB", "tnAbsNodeSubnodeLocalDPNodeId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeSubnodeNodalSrg"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeSubnodeOpState"))
)
if mibBuilder.loadTexts:
    tnAbsNodeSubnodeGroup.setStatus("current")

tnAbsNodeTeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 3)
)
tnAbsNodeTeLinkGroup.setObjects(
      *(("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkRemoteIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkRemoteNodeAddress"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkUserLabel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkMetric"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkSrgIds"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkColors"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkLatency"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkComponentIfIdList"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkRowStatus"))
)
if mibBuilder.loadTexts:
    tnAbsNodeTeLinkGroup.setStatus("current")

tnAbsNodeOtsPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 4)
)
tnAbsNodeOtsPortGroup.setObjects(
      *(("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortNeIfIndex"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortLocalShelfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortRemoteIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortRemoteNodeAddress"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortRemoteOtsPortIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortUserLabel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortCentralFrequencyGranularity"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortSlotWidthGranularity"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortMinSlotWidth"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortMaxSlotWidth"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortMinChannel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortMaxChannel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortWssGranularity"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortEndPointType"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortOpState"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortIsPreparedForOps"))
)
if mibBuilder.loadTexts:
    tnAbsNodeOtsPortGroup.setStatus("current")

tnAbsNodeIfGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 5)
)
tnAbsNodeIfGroupGroup.setObjects(
      *(("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupCentralFrequencyGranularity"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupSlotWidthGranularity"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupMinSlotWidth"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupMaxSlotWidth"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupMinChannel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupMaxChannel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupWssGranularity"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupAdType"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupOtAseConst"))
)
if mibBuilder.loadTexts:
    tnAbsNodeIfGroupGroup.setStatus("current")

tnAbsNodeOtLinePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 6)
)
tnAbsNodeOtLinePortGroup.setObjects(
      *(("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortRemoteUplinkNodeAddress"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortRemoteUplinkPortIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortPhysicalClientPortIfIds"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortLocalShelfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortIfGroupIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSubGroupIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortIsOpsProtected"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSpareIfGroupIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSpareSubGroupIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortModType"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortAnalogBw"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortCompMode"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortFecTypes"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortServiceWidth"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortMinChannel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortMaxChannel"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortChanStep"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortHas100GHzSubGroupWidth"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePort3RType"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortConnectedIfId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePort3RConnType"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortOpState"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortAddDropPort"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortAddDropSparePort"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortAddDropOpsPort"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortTransponderType"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortMinDropPower"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSpareMinDropPower"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortIsr"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSpareIsr"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortPhaseEncodeTypes"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortHasPhaseEncodeDep"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSamePhaseEncodePortId"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortMinDropPowerP2"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortWaveTrackerCap"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSpareMinDropPowerP2"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortOtuSignalTypes"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortTransponderString"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortSupportedServiceWidths"))
)
if mibBuilder.loadTexts:
    tnAbsNodeOtLinePortGroup.setStatus("current")

tnAbsNodeConnectivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 1, 7)
)
tnAbsNodeConnectivityGroup.setObjects(
    ("TROPIC-ABSNODE-MIB", "tnAbsNodeConnectivityOpState")
)
if mibBuilder.loadTexts:
    tnAbsNodeConnectivityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAbsNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 3, 2, 1)
)
tnAbsNodeCompliance.setObjects(
      *(("TROPIC-ABSNODE-MIB", "tnAbsNodeObjsGroup"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeSubnodeGroup"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeTeLinkGroup"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtsPortGroup"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeIfGroupGroup"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeOtLinePortGroup"),
        ("TROPIC-ABSNODE-MIB", "tnAbsNodeConnectivityGroup"))
)
if mibBuilder.loadTexts:
    tnAbsNodeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ABSNODE-MIB",
    **{"TnAbsNodeOpState": TnAbsNodeOpState,
       "TnAbsNodeAnalogBandwidth": TnAbsNodeAnalogBandwidth,
       "TnAbsNodeChannelSpacing": TnAbsNodeChannelSpacing,
       "TnAbsNodeSlotWidth": TnAbsNodeSlotWidth,
       "TnAbsNode3RType": TnAbsNode3RType,
       "TnAbsNode3RConnType": TnAbsNode3RConnType,
       "TnAbsNodeEndPointType": TnAbsNodeEndPointType,
       "TnAbsNodeAddDropType": TnAbsNodeAddDropType,
       "TnAbsNodeOtAseConstraint": TnAbsNodeOtAseConstraint,
       "TnAbsNodeWaveTrackerCapability": TnAbsNodeWaveTrackerCapability,
       "TnAbsNodeTransponderType": TnAbsNodeTransponderType,
       "TnAbsNodeIsPreparedForOps": TnAbsNodeIsPreparedForOps,
       "tnAbsNodeMibModule": tnAbsNodeMibModule,
       "tnAbsNodeAttributeTotal": tnAbsNodeAttributeTotal,
       "tnAbsNodeSubnodeTable": tnAbsNodeSubnodeTable,
       "tnAbsNodeSubnodeEntry": tnAbsNodeSubnodeEntry,
       "tnAbsNodeSubnodeLocalShelfId": tnAbsNodeSubnodeLocalShelfId,
       "tnAbsNodeSubnodeLocalDPNodeId": tnAbsNodeSubnodeLocalDPNodeId,
       "tnAbsNodeSubnodeNodalSrg": tnAbsNodeSubnodeNodalSrg,
       "tnAbsNodeSubnodeOpState": tnAbsNodeSubnodeOpState,
       "tnAbsNodeTeLinkTable": tnAbsNodeTeLinkTable,
       "tnAbsNodeTeLinkEntry": tnAbsNodeTeLinkEntry,
       "tnAbsNodeTeLinkIfId": tnAbsNodeTeLinkIfId,
       "tnAbsNodeTeLinkRemoteIfId": tnAbsNodeTeLinkRemoteIfId,
       "tnAbsNodeTeLinkRemoteNodeAddress": tnAbsNodeTeLinkRemoteNodeAddress,
       "tnAbsNodeTeLinkUserLabel": tnAbsNodeTeLinkUserLabel,
       "tnAbsNodeTeLinkMetric": tnAbsNodeTeLinkMetric,
       "tnAbsNodeTeLinkSrgIds": tnAbsNodeTeLinkSrgIds,
       "tnAbsNodeTeLinkColors": tnAbsNodeTeLinkColors,
       "tnAbsNodeTeLinkLatency": tnAbsNodeTeLinkLatency,
       "tnAbsNodeTeLinkComponentIfIdList": tnAbsNodeTeLinkComponentIfIdList,
       "tnAbsNodeTeLinkRowStatus": tnAbsNodeTeLinkRowStatus,
       "tnAbsNodeOtsPortTable": tnAbsNodeOtsPortTable,
       "tnAbsNodeOtsPortEntry": tnAbsNodeOtsPortEntry,
       "tnAbsNodeOtsPortIfId": tnAbsNodeOtsPortIfId,
       "tnAbsNodeOtsPortNeIfIndex": tnAbsNodeOtsPortNeIfIndex,
       "tnAbsNodeOtsPortLocalShelfId": tnAbsNodeOtsPortLocalShelfId,
       "tnAbsNodeOtsPortRemoteIfId": tnAbsNodeOtsPortRemoteIfId,
       "tnAbsNodeOtsPortRemoteNodeAddress": tnAbsNodeOtsPortRemoteNodeAddress,
       "tnAbsNodeOtsPortRemoteOtsPortIfId": tnAbsNodeOtsPortRemoteOtsPortIfId,
       "tnAbsNodeOtsPortUserLabel": tnAbsNodeOtsPortUserLabel,
       "tnAbsNodeOtsPortCentralFrequencyGranularity": tnAbsNodeOtsPortCentralFrequencyGranularity,
       "tnAbsNodeOtsPortSlotWidthGranularity": tnAbsNodeOtsPortSlotWidthGranularity,
       "tnAbsNodeOtsPortMinSlotWidth": tnAbsNodeOtsPortMinSlotWidth,
       "tnAbsNodeOtsPortMaxSlotWidth": tnAbsNodeOtsPortMaxSlotWidth,
       "tnAbsNodeOtsPortMinChannel": tnAbsNodeOtsPortMinChannel,
       "tnAbsNodeOtsPortMaxChannel": tnAbsNodeOtsPortMaxChannel,
       "tnAbsNodeOtsPortWssGranularity": tnAbsNodeOtsPortWssGranularity,
       "tnAbsNodeOtsPortEndPointType": tnAbsNodeOtsPortEndPointType,
       "tnAbsNodeOtsPortOpState": tnAbsNodeOtsPortOpState,
       "tnAbsNodeOtsPortIsPreparedForOps": tnAbsNodeOtsPortIsPreparedForOps,
       "tnAbsNodeIfGroupTable": tnAbsNodeIfGroupTable,
       "tnAbsNodeIfGroupEntry": tnAbsNodeIfGroupEntry,
       "tnAbsNodeIfGroupIfId": tnAbsNodeIfGroupIfId,
       "tnAbsNodeIfGroupCentralFrequencyGranularity": tnAbsNodeIfGroupCentralFrequencyGranularity,
       "tnAbsNodeIfGroupSlotWidthGranularity": tnAbsNodeIfGroupSlotWidthGranularity,
       "tnAbsNodeIfGroupMinSlotWidth": tnAbsNodeIfGroupMinSlotWidth,
       "tnAbsNodeIfGroupMaxSlotWidth": tnAbsNodeIfGroupMaxSlotWidth,
       "tnAbsNodeIfGroupMinChannel": tnAbsNodeIfGroupMinChannel,
       "tnAbsNodeIfGroupMaxChannel": tnAbsNodeIfGroupMaxChannel,
       "tnAbsNodeIfGroupWssGranularity": tnAbsNodeIfGroupWssGranularity,
       "tnAbsNodeIfGroupAdType": tnAbsNodeIfGroupAdType,
       "tnAbsNodeIfGroupOtAseConst": tnAbsNodeIfGroupOtAseConst,
       "tnAbsNodeOtLinePortTable": tnAbsNodeOtLinePortTable,
       "tnAbsNodeOtLinePortEntry": tnAbsNodeOtLinePortEntry,
       "tnAbsNodeOtLinePortIfId": tnAbsNodeOtLinePortIfId,
       "tnAbsNodeOtLinePortRemoteUplinkNodeAddress": tnAbsNodeOtLinePortRemoteUplinkNodeAddress,
       "tnAbsNodeOtLinePortRemoteUplinkPortIfId": tnAbsNodeOtLinePortRemoteUplinkPortIfId,
       "tnAbsNodeOtLinePortPhysicalClientPortIfIds": tnAbsNodeOtLinePortPhysicalClientPortIfIds,
       "tnAbsNodeOtLinePortLocalShelfId": tnAbsNodeOtLinePortLocalShelfId,
       "tnAbsNodeOtLinePortIfGroupIfId": tnAbsNodeOtLinePortIfGroupIfId,
       "tnAbsNodeOtLinePortSubGroupIfId": tnAbsNodeOtLinePortSubGroupIfId,
       "tnAbsNodeOtLinePortIsOpsProtected": tnAbsNodeOtLinePortIsOpsProtected,
       "tnAbsNodeOtLinePortSpareIfGroupIfId": tnAbsNodeOtLinePortSpareIfGroupIfId,
       "tnAbsNodeOtLinePortSpareSubGroupIfId": tnAbsNodeOtLinePortSpareSubGroupIfId,
       "tnAbsNodeOtLinePortModType": tnAbsNodeOtLinePortModType,
       "tnAbsNodeOtLinePortAnalogBw": tnAbsNodeOtLinePortAnalogBw,
       "tnAbsNodeOtLinePortCompMode": tnAbsNodeOtLinePortCompMode,
       "tnAbsNodeOtLinePortFecTypes": tnAbsNodeOtLinePortFecTypes,
       "tnAbsNodeOtLinePortServiceWidth": tnAbsNodeOtLinePortServiceWidth,
       "tnAbsNodeOtLinePortMinChannel": tnAbsNodeOtLinePortMinChannel,
       "tnAbsNodeOtLinePortMaxChannel": tnAbsNodeOtLinePortMaxChannel,
       "tnAbsNodeOtLinePortChanStep": tnAbsNodeOtLinePortChanStep,
       "tnAbsNodeOtLinePortHas100GHzSubGroupWidth": tnAbsNodeOtLinePortHas100GHzSubGroupWidth,
       "tnAbsNodeOtLinePort3RType": tnAbsNodeOtLinePort3RType,
       "tnAbsNodeOtLinePortConnectedIfId": tnAbsNodeOtLinePortConnectedIfId,
       "tnAbsNodeOtLinePort3RConnType": tnAbsNodeOtLinePort3RConnType,
       "tnAbsNodeOtLinePortOpState": tnAbsNodeOtLinePortOpState,
       "tnAbsNodeOtLinePortAddDropPort": tnAbsNodeOtLinePortAddDropPort,
       "tnAbsNodeOtLinePortAddDropSparePort": tnAbsNodeOtLinePortAddDropSparePort,
       "tnAbsNodeOtLinePortAddDropOpsPort": tnAbsNodeOtLinePortAddDropOpsPort,
       "tnAbsNodeOtLinePortTransponderType": tnAbsNodeOtLinePortTransponderType,
       "tnAbsNodeOtLinePortMinDropPower": tnAbsNodeOtLinePortMinDropPower,
       "tnAbsNodeOtLinePortSpareMinDropPower": tnAbsNodeOtLinePortSpareMinDropPower,
       "tnAbsNodeOtLinePortIsr": tnAbsNodeOtLinePortIsr,
       "tnAbsNodeOtLinePortSpareIsr": tnAbsNodeOtLinePortSpareIsr,
       "tnAbsNodeOtLinePortPhaseEncodeTypes": tnAbsNodeOtLinePortPhaseEncodeTypes,
       "tnAbsNodeOtLinePortHasPhaseEncodeDep": tnAbsNodeOtLinePortHasPhaseEncodeDep,
       "tnAbsNodeOtLinePortSamePhaseEncodePortId": tnAbsNodeOtLinePortSamePhaseEncodePortId,
       "tnAbsNodeOtLinePortMinDropPowerP2": tnAbsNodeOtLinePortMinDropPowerP2,
       "tnAbsNodeOtLinePortWaveTrackerCap": tnAbsNodeOtLinePortWaveTrackerCap,
       "tnAbsNodeOtLinePortSpareMinDropPowerP2": tnAbsNodeOtLinePortSpareMinDropPowerP2,
       "tnAbsNodeOtLinePortOtuSignalTypes": tnAbsNodeOtLinePortOtuSignalTypes,
       "tnAbsNodeOtLinePortTransponderString": tnAbsNodeOtLinePortTransponderString,
       "tnAbsNodeOtLinePortSupportedServiceWidths": tnAbsNodeOtLinePortSupportedServiceWidths,
       "tnAbsNodeConnectivityTable": tnAbsNodeConnectivityTable,
       "tnAbsNodeConnectivityEntry": tnAbsNodeConnectivityEntry,
       "tnAbsNodeConnectivityFromIfId": tnAbsNodeConnectivityFromIfId,
       "tnAbsNodeConnectivityToIfId": tnAbsNodeConnectivityToIfId,
       "tnAbsNodeConnectivityOpState": tnAbsNodeConnectivityOpState,
       "tnAbsNodeConf": tnAbsNodeConf,
       "tnAbsNodeGroups": tnAbsNodeGroups,
       "tnAbsNodeObjsGroup": tnAbsNodeObjsGroup,
       "tnAbsNodeSubnodeGroup": tnAbsNodeSubnodeGroup,
       "tnAbsNodeTeLinkGroup": tnAbsNodeTeLinkGroup,
       "tnAbsNodeOtsPortGroup": tnAbsNodeOtsPortGroup,
       "tnAbsNodeIfGroupGroup": tnAbsNodeIfGroupGroup,
       "tnAbsNodeOtLinePortGroup": tnAbsNodeOtLinePortGroup,
       "tnAbsNodeConnectivityGroup": tnAbsNodeConnectivityGroup,
       "tnAbsNodeCompliances": tnAbsNodeCompliances,
       "tnAbsNodeCompliance": tnAbsNodeCompliance}
)
