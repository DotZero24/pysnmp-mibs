# SNMP MIB module (IEC-62439-3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/IEC-62439-3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:23:04 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

iec62439 = ModuleIdentity(
    (1, 0, 62439)
)
if mibBuilder.loadTexts:
    iec62439.setRevisions(
        ("2014-05-22 00:00",
         "2012-02-17 00:00",
         "2011-08-26 00:00",
         "2008-11-10 00:00",
         "2006-12-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SecondFraction(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Mrp_ObjectIdentity = ObjectIdentity
mrp = _Mrp_ObjectIdentity(
    (1, 0, 62439, 1)
)
_Prp_ObjectIdentity = ObjectIdentity
prp = _Prp_ObjectIdentity(
    (1, 0, 62439, 2)
)
_LinkRedundancyEntityNotifications_ObjectIdentity = ObjectIdentity
linkRedundancyEntityNotifications = _LinkRedundancyEntityNotifications_ObjectIdentity(
    (1, 0, 62439, 2, 20)
)
_LinkRedundancyEntityObjects_ObjectIdentity = ObjectIdentity
linkRedundancyEntityObjects = _LinkRedundancyEntityObjects_ObjectIdentity(
    (1, 0, 62439, 2, 21)
)
_LreConfiguration_ObjectIdentity = ObjectIdentity
lreConfiguration = _LreConfiguration_ObjectIdentity(
    (1, 0, 62439, 2, 21, 0)
)
_LreConfigurationGeneralGroup_ObjectIdentity = ObjectIdentity
lreConfigurationGeneralGroup = _LreConfigurationGeneralGroup_ObjectIdentity(
    (1, 0, 62439, 2, 21, 0, 0)
)
_LreManufacturerName_Type = DisplayString
_LreManufacturerName_Object = MibScalar
lreManufacturerName = _LreManufacturerName_Object(
    (1, 0, 62439, 2, 21, 0, 0, 1),
    _LreManufacturerName_Type()
)
lreManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreManufacturerName.setStatus("current")
_LreInterfaceCount_Type = Integer32
_LreInterfaceCount_Object = MibScalar
lreInterfaceCount = _LreInterfaceCount_Object(
    (1, 0, 62439, 2, 21, 0, 0, 2),
    _LreInterfaceCount_Type()
)
lreInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreInterfaceCount.setStatus("current")
_LreConfigurationInterfaceGroup_ObjectIdentity = ObjectIdentity
lreConfigurationInterfaceGroup = _LreConfigurationInterfaceGroup_ObjectIdentity(
    (1, 0, 62439, 2, 21, 0, 1)
)
_LreConfigurationInterfaces_ObjectIdentity = ObjectIdentity
lreConfigurationInterfaces = _LreConfigurationInterfaces_ObjectIdentity(
    (1, 0, 62439, 2, 21, 0, 1, 0)
)
_LreInterfaceConfigTable_Object = MibTable
lreInterfaceConfigTable = _LreInterfaceConfigTable_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1)
)
if mibBuilder.loadTexts:
    lreInterfaceConfigTable.setStatus("current")
_LreInterfaceConfigEntry_Object = MibTableRow
lreInterfaceConfigEntry = _LreInterfaceConfigEntry_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1)
)
lreInterfaceConfigEntry.setIndexNames(
    (0, "IEC-62439-3-MIB", "lreInterfaceConfigIndex"),
)
if mibBuilder.loadTexts:
    lreInterfaceConfigEntry.setStatus("current")
_LreInterfaceConfigIndex_Type = Unsigned32
_LreInterfaceConfigIndex_Object = MibTableColumn
lreInterfaceConfigIndex = _LreInterfaceConfigIndex_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 1),
    _LreInterfaceConfigIndex_Type()
)
lreInterfaceConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lreInterfaceConfigIndex.setStatus("current")
_LreRowStatus_Type = RowStatus
_LreRowStatus_Object = MibTableColumn
lreRowStatus = _LreRowStatus_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 2),
    _LreRowStatus_Type()
)
lreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lreRowStatus.setStatus("current")


class _LreNodeType_Type(Integer32):
    """Custom type lreNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prpmode1", 1),
          ("hsr", 2))
    )


_LreNodeType_Type.__name__ = "Integer32"
_LreNodeType_Object = MibTableColumn
lreNodeType = _LreNodeType_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 3),
    _LreNodeType_Type()
)
lreNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreNodeType.setStatus("current")
_LreNodeName_Type = DisplayString
_LreNodeName_Object = MibTableColumn
lreNodeName = _LreNodeName_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 4),
    _LreNodeName_Type()
)
lreNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreNodeName.setStatus("current")


class _LreVersionName_Type(OctetString):
    """Custom type lreVersionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LreVersionName_Type.__name__ = "OctetString"
_LreVersionName_Object = MibTableColumn
lreVersionName = _LreVersionName_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 5),
    _LreVersionName_Type()
)
lreVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreVersionName.setStatus("current")
_LreMacAddress_Type = MacAddress
_LreMacAddress_Object = MibTableColumn
lreMacAddress = _LreMacAddress_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 6),
    _LreMacAddress_Type()
)
lreMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreMacAddress.setStatus("current")


class _LrePortAdminStateA_Type(Integer32):
    """Custom type lrePortAdminStateA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_LrePortAdminStateA_Type.__name__ = "Integer32"
_LrePortAdminStateA_Object = MibTableColumn
lrePortAdminStateA = _LrePortAdminStateA_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 7),
    _LrePortAdminStateA_Type()
)
lrePortAdminStateA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrePortAdminStateA.setStatus("current")


class _LrePortAdminStateB_Type(Integer32):
    """Custom type lrePortAdminStateB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_LrePortAdminStateB_Type.__name__ = "Integer32"
_LrePortAdminStateB_Object = MibTableColumn
lrePortAdminStateB = _LrePortAdminStateB_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 8),
    _LrePortAdminStateB_Type()
)
lrePortAdminStateB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrePortAdminStateB.setStatus("current")


class _LreLinkStatusA_Type(Integer32):
    """Custom type lreLinkStatusA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_LreLinkStatusA_Type.__name__ = "Integer32"
_LreLinkStatusA_Object = MibTableColumn
lreLinkStatusA = _LreLinkStatusA_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 9),
    _LreLinkStatusA_Type()
)
lreLinkStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreLinkStatusA.setStatus("current")


class _LreLinkStatusB_Type(Integer32):
    """Custom type lreLinkStatusB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_LreLinkStatusB_Type.__name__ = "Integer32"
_LreLinkStatusB_Object = MibTableColumn
lreLinkStatusB = _LreLinkStatusB_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 10),
    _LreLinkStatusB_Type()
)
lreLinkStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreLinkStatusB.setStatus("current")


class _LreDuplicateDiscard_Type(Integer32):
    """Custom type lreDuplicateDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotDiscard", 1),
          ("discard", 2))
    )


_LreDuplicateDiscard_Type.__name__ = "Integer32"
_LreDuplicateDiscard_Object = MibTableColumn
lreDuplicateDiscard = _LreDuplicateDiscard_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 11),
    _LreDuplicateDiscard_Type()
)
lreDuplicateDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreDuplicateDiscard.setStatus("current")


class _LreTransparentReception_Type(Integer32):
    """Custom type lreTransparentReception based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("removeRCT", 1),
          ("passRCT", 2))
    )


_LreTransparentReception_Type.__name__ = "Integer32"
_LreTransparentReception_Object = MibTableColumn
lreTransparentReception = _LreTransparentReception_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 12),
    _LreTransparentReception_Type()
)
lreTransparentReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreTransparentReception.setStatus("current")


class _LreHsrLREMode_Type(Integer32):
    """Custom type lreHsrLREMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("modeh", 1),
          ("moden", 2),
          ("modet", 3),
          ("modeu", 4),
          ("modem", 5))
    )


_LreHsrLREMode_Type.__name__ = "Integer32"
_LreHsrLREMode_Object = MibTableColumn
lreHsrLREMode = _LreHsrLREMode_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 13),
    _LreHsrLREMode_Type()
)
lreHsrLREMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreHsrLREMode.setStatus("current")


class _LreSwitchingEndNode_Type(Integer32):
    """Custom type lreSwitchingEndNode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("nonbridgingnode", 1),
          ("bridgingunspecified", 2),
          ("prpnode", 3),
          ("hsrredboxsan", 4),
          ("hsrnode", 5),
          ("hsrredboxhsr", 6),
          ("hsrredboxprpa", 7),
          ("hsrredboxprpb", 8))
    )


_LreSwitchingEndNode_Type.__name__ = "Integer32"
_LreSwitchingEndNode_Object = MibTableColumn
lreSwitchingEndNode = _LreSwitchingEndNode_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 14),
    _LreSwitchingEndNode_Type()
)
lreSwitchingEndNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreSwitchingEndNode.setStatus("current")


class _LreRedBoxIdentity_Type(Integer32):
    """Custom type lreRedBoxIdentity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("id1a", 2),
          ("id1b", 3),
          ("id2a", 4),
          ("id2b", 5),
          ("id3a", 6),
          ("id3b", 7),
          ("id4a", 8),
          ("id4b", 9),
          ("id5a", 10),
          ("id5b", 11),
          ("id6a", 12),
          ("id6b", 13),
          ("id7a", 14),
          ("id7b", 15))
    )


_LreRedBoxIdentity_Type.__name__ = "Integer32"
_LreRedBoxIdentity_Object = MibTableColumn
lreRedBoxIdentity = _LreRedBoxIdentity_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 15),
    _LreRedBoxIdentity_Type()
)
lreRedBoxIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreRedBoxIdentity.setStatus("current")
_LreEvaluateSupervision_Type = TruthValue
_LreEvaluateSupervision_Object = MibTableColumn
lreEvaluateSupervision = _LreEvaluateSupervision_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 16),
    _LreEvaluateSupervision_Type()
)
lreEvaluateSupervision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreEvaluateSupervision.setStatus("current")


class _LreNodesTableClear_Type(Integer32):
    """Custom type lreNodesTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("clearNodeTable", 1))
    )


_LreNodesTableClear_Type.__name__ = "Integer32"
_LreNodesTableClear_Object = MibTableColumn
lreNodesTableClear = _LreNodesTableClear_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 17),
    _LreNodesTableClear_Type()
)
lreNodesTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreNodesTableClear.setStatus("current")


class _LreProxyNodeTableClear_Type(Integer32):
    """Custom type lreProxyNodeTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("clearProxyNodeTable", 1))
    )


_LreProxyNodeTableClear_Type.__name__ = "Integer32"
_LreProxyNodeTableClear_Object = MibTableColumn
lreProxyNodeTableClear = _LreProxyNodeTableClear_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 18),
    _LreProxyNodeTableClear_Type()
)
lreProxyNodeTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreProxyNodeTableClear.setStatus("current")


class _LreDupListResideMaxTime_Type(SecondFraction):
    """Custom type lreDupListResideMaxTime based on SecondFraction"""
    defaultValue = 26214


_LreDupListResideMaxTime_Type.__name__ = "SecondFraction"
_LreDupListResideMaxTime_Object = MibTableColumn
lreDupListResideMaxTime = _LreDupListResideMaxTime_Object(
    (1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 19),
    _LreDupListResideMaxTime_Type()
)
lreDupListResideMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreDupListResideMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    lreDupListResideMaxTime.setUnits("binaryFractionOfSecond")
_LreStatistics_ObjectIdentity = ObjectIdentity
lreStatistics = _LreStatistics_ObjectIdentity(
    (1, 0, 62439, 2, 21, 1)
)
_LreStatisticsInterfaceGroup_ObjectIdentity = ObjectIdentity
lreStatisticsInterfaceGroup = _LreStatisticsInterfaceGroup_ObjectIdentity(
    (1, 0, 62439, 2, 21, 1, 1)
)
_LreStatisticsInterfaces_ObjectIdentity = ObjectIdentity
lreStatisticsInterfaces = _LreStatisticsInterfaces_ObjectIdentity(
    (1, 0, 62439, 2, 21, 1, 1, 0)
)
_LreInterfaceStatsTable_Object = MibTable
lreInterfaceStatsTable = _LreInterfaceStatsTable_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    lreInterfaceStatsTable.setStatus("current")
_LreInterfaceStatsEntry_Object = MibTableRow
lreInterfaceStatsEntry = _LreInterfaceStatsEntry_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1)
)
lreInterfaceStatsEntry.setIndexNames(
    (0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    lreInterfaceStatsEntry.setStatus("current")
_LreInterfaceStatsIndex_Type = Unsigned32
_LreInterfaceStatsIndex_Object = MibTableColumn
lreInterfaceStatsIndex = _LreInterfaceStatsIndex_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 1),
    _LreInterfaceStatsIndex_Type()
)
lreInterfaceStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lreInterfaceStatsIndex.setStatus("current")
_LreCntTxA_Type = Counter32
_LreCntTxA_Object = MibTableColumn
lreCntTxA = _LreCntTxA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 2),
    _LreCntTxA_Type()
)
lreCntTxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntTxA.setStatus("current")
_LreCntTxB_Type = Counter32
_LreCntTxB_Object = MibTableColumn
lreCntTxB = _LreCntTxB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 3),
    _LreCntTxB_Type()
)
lreCntTxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntTxB.setStatus("current")
_LreCntTxC_Type = Counter32
_LreCntTxC_Object = MibTableColumn
lreCntTxC = _LreCntTxC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 4),
    _LreCntTxC_Type()
)
lreCntTxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntTxC.setStatus("current")
_LreCntErrWrongLanA_Type = Counter32
_LreCntErrWrongLanA_Object = MibTableColumn
lreCntErrWrongLanA = _LreCntErrWrongLanA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 5),
    _LreCntErrWrongLanA_Type()
)
lreCntErrWrongLanA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntErrWrongLanA.setStatus("current")
_LreCntErrWrongLanB_Type = Counter32
_LreCntErrWrongLanB_Object = MibTableColumn
lreCntErrWrongLanB = _LreCntErrWrongLanB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 6),
    _LreCntErrWrongLanB_Type()
)
lreCntErrWrongLanB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntErrWrongLanB.setStatus("current")
_LreCntErrWrongLanC_Type = Counter32
_LreCntErrWrongLanC_Object = MibTableColumn
lreCntErrWrongLanC = _LreCntErrWrongLanC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 7),
    _LreCntErrWrongLanC_Type()
)
lreCntErrWrongLanC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntErrWrongLanC.setStatus("current")
_LreCntRxA_Type = Counter32
_LreCntRxA_Object = MibTableColumn
lreCntRxA = _LreCntRxA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 8),
    _LreCntRxA_Type()
)
lreCntRxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntRxA.setStatus("current")
_LreCntRxB_Type = Counter32
_LreCntRxB_Object = MibTableColumn
lreCntRxB = _LreCntRxB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 9),
    _LreCntRxB_Type()
)
lreCntRxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntRxB.setStatus("current")
_LreCntRxC_Type = Counter32
_LreCntRxC_Object = MibTableColumn
lreCntRxC = _LreCntRxC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 10),
    _LreCntRxC_Type()
)
lreCntRxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntRxC.setStatus("current")
_LreCntErrorsA_Type = Counter32
_LreCntErrorsA_Object = MibTableColumn
lreCntErrorsA = _LreCntErrorsA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 11),
    _LreCntErrorsA_Type()
)
lreCntErrorsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntErrorsA.setStatus("current")
_LreCntErrorsB_Type = Counter32
_LreCntErrorsB_Object = MibTableColumn
lreCntErrorsB = _LreCntErrorsB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 12),
    _LreCntErrorsB_Type()
)
lreCntErrorsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntErrorsB.setStatus("current")
_LreCntErrorsC_Type = Counter32
_LreCntErrorsC_Object = MibTableColumn
lreCntErrorsC = _LreCntErrorsC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 13),
    _LreCntErrorsC_Type()
)
lreCntErrorsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntErrorsC.setStatus("current")
_LreCntNodes_Type = Integer32
_LreCntNodes_Object = MibTableColumn
lreCntNodes = _LreCntNodes_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 14),
    _LreCntNodes_Type()
)
lreCntNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntNodes.setStatus("current")
_LreCntProxyNodes_Type = Integer32
_LreCntProxyNodes_Object = MibTableColumn
lreCntProxyNodes = _LreCntProxyNodes_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 15),
    _LreCntProxyNodes_Type()
)
lreCntProxyNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntProxyNodes.setStatus("current")
_LreCntUniqueA_Type = Counter32
_LreCntUniqueA_Object = MibTableColumn
lreCntUniqueA = _LreCntUniqueA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 16),
    _LreCntUniqueA_Type()
)
lreCntUniqueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntUniqueA.setStatus("current")
_LreCntUniqueB_Type = Counter32
_LreCntUniqueB_Object = MibTableColumn
lreCntUniqueB = _LreCntUniqueB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 17),
    _LreCntUniqueB_Type()
)
lreCntUniqueB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntUniqueB.setStatus("current")
_LreCntUniqueC_Type = Counter32
_LreCntUniqueC_Object = MibTableColumn
lreCntUniqueC = _LreCntUniqueC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 18),
    _LreCntUniqueC_Type()
)
lreCntUniqueC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntUniqueC.setStatus("current")
_LreCntDuplicateA_Type = Counter32
_LreCntDuplicateA_Object = MibTableColumn
lreCntDuplicateA = _LreCntDuplicateA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 19),
    _LreCntDuplicateA_Type()
)
lreCntDuplicateA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntDuplicateA.setStatus("current")
_LreCntDuplicateB_Type = Counter32
_LreCntDuplicateB_Object = MibTableColumn
lreCntDuplicateB = _LreCntDuplicateB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 20),
    _LreCntDuplicateB_Type()
)
lreCntDuplicateB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntDuplicateB.setStatus("current")
_LreCntDuplicateC_Type = Counter32
_LreCntDuplicateC_Object = MibTableColumn
lreCntDuplicateC = _LreCntDuplicateC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 21),
    _LreCntDuplicateC_Type()
)
lreCntDuplicateC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntDuplicateC.setStatus("current")
_LreCntMultiA_Type = Counter32
_LreCntMultiA_Object = MibTableColumn
lreCntMultiA = _LreCntMultiA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 22),
    _LreCntMultiA_Type()
)
lreCntMultiA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntMultiA.setStatus("current")
_LreCntMultiB_Type = Counter32
_LreCntMultiB_Object = MibTableColumn
lreCntMultiB = _LreCntMultiB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 23),
    _LreCntMultiB_Type()
)
lreCntMultiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntMultiB.setStatus("current")
_LreCntMultiC_Type = Counter32
_LreCntMultiC_Object = MibTableColumn
lreCntMultiC = _LreCntMultiC_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 24),
    _LreCntMultiC_Type()
)
lreCntMultiC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntMultiC.setStatus("current")
_LreCntOwnRxA_Type = Counter32
_LreCntOwnRxA_Object = MibTableColumn
lreCntOwnRxA = _LreCntOwnRxA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 25),
    _LreCntOwnRxA_Type()
)
lreCntOwnRxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntOwnRxA.setStatus("current")
_LreCntOwnRxB_Type = Counter32
_LreCntOwnRxB_Object = MibTableColumn
lreCntOwnRxB = _LreCntOwnRxB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 26),
    _LreCntOwnRxB_Type()
)
lreCntOwnRxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreCntOwnRxB.setStatus("current")
_LreNodesTable_Object = MibTable
lreNodesTable = _LreNodesTable_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2)
)
if mibBuilder.loadTexts:
    lreNodesTable.setStatus("current")
_LreNodesEntry_Object = MibTableRow
lreNodesEntry = _LreNodesEntry_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2, 1)
)
lreNodesEntry.setIndexNames(
    (0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"),
    (0, "IEC-62439-3-MIB", "lreNodesIndex"),
)
if mibBuilder.loadTexts:
    lreNodesEntry.setStatus("current")
_LreNodesIndex_Type = Unsigned32
_LreNodesIndex_Object = MibTableColumn
lreNodesIndex = _LreNodesIndex_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 1),
    _LreNodesIndex_Type()
)
lreNodesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lreNodesIndex.setStatus("current")
_LreNodesMacAddress_Type = MacAddress
_LreNodesMacAddress_Object = MibTableColumn
lreNodesMacAddress = _LreNodesMacAddress_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 2),
    _LreNodesMacAddress_Type()
)
lreNodesMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreNodesMacAddress.setStatus("current")
_LreTimeLastSeenA_Type = TimeTicks
_LreTimeLastSeenA_Object = MibTableColumn
lreTimeLastSeenA = _LreTimeLastSeenA_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 3),
    _LreTimeLastSeenA_Type()
)
lreTimeLastSeenA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreTimeLastSeenA.setStatus("current")
_LreTimeLastSeenB_Type = TimeTicks
_LreTimeLastSeenB_Object = MibTableColumn
lreTimeLastSeenB = _LreTimeLastSeenB_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 4),
    _LreTimeLastSeenB_Type()
)
lreTimeLastSeenB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreTimeLastSeenB.setStatus("current")


class _LreRemNodeType_Type(Integer32):
    """Custom type lreRemNodeType based on Integer32"""
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
        *(("danp", 0),
          ("redboxp", 1),
          ("vdanp", 2),
          ("danh", 3),
          ("redboxh", 4),
          ("vdanh", 5))
    )


_LreRemNodeType_Type.__name__ = "Integer32"
_LreRemNodeType_Object = MibTableColumn
lreRemNodeType = _LreRemNodeType_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 5),
    _LreRemNodeType_Type()
)
lreRemNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreRemNodeType.setStatus("current")
_LreProxyNodeTable_Object = MibTable
lreProxyNodeTable = _LreProxyNodeTable_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 3)
)
if mibBuilder.loadTexts:
    lreProxyNodeTable.setStatus("current")
_LreProxyNodeEntry_Object = MibTableRow
lreProxyNodeEntry = _LreProxyNodeEntry_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 3, 1)
)
lreProxyNodeEntry.setIndexNames(
    (0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"),
    (0, "IEC-62439-3-MIB", "lreProxyNodeIndex"),
)
if mibBuilder.loadTexts:
    lreProxyNodeEntry.setStatus("current")
_LreProxyNodeIndex_Type = Unsigned32
_LreProxyNodeIndex_Object = MibTableColumn
lreProxyNodeIndex = _LreProxyNodeIndex_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 3, 1, 1),
    _LreProxyNodeIndex_Type()
)
lreProxyNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lreProxyNodeIndex.setStatus("current")
_LreProxyNodeMacAddress_Type = MacAddress
_LreProxyNodeMacAddress_Object = MibTableColumn
lreProxyNodeMacAddress = _LreProxyNodeMacAddress_Object(
    (1, 0, 62439, 2, 21, 1, 1, 0, 3, 1, 2),
    _LreProxyNodeMacAddress_Type()
)
lreProxyNodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lreProxyNodeMacAddress.setStatus("current")
_LinkRedundancyEntityConformance_ObjectIdentity = ObjectIdentity
linkRedundancyEntityConformance = _LinkRedundancyEntityConformance_ObjectIdentity(
    (1, 0, 62439, 2, 22)
)
_LinkRedundancyConformance_ObjectIdentity = ObjectIdentity
linkRedundancyConformance = _LinkRedundancyConformance_ObjectIdentity(
    (1, 0, 62439, 2, 22, 1)
)
_LreGroups_ObjectIdentity = ObjectIdentity
lreGroups = _LreGroups_ObjectIdentity(
    (1, 0, 62439, 2, 22, 1, 1)
)
_LinkRedundancyCompliances_ObjectIdentity = ObjectIdentity
linkRedundancyCompliances = _LinkRedundancyCompliances_ObjectIdentity(
    (1, 0, 62439, 2, 22, 2)
)
_Crp_ObjectIdentity = ObjectIdentity
crp = _Crp_ObjectIdentity(
    (1, 0, 62439, 3)
)
_Brp_ObjectIdentity = ObjectIdentity
brp = _Brp_ObjectIdentity(
    (1, 0, 62439, 4)
)
_Drp_ObjectIdentity = ObjectIdentity
drp = _Drp_ObjectIdentity(
    (1, 0, 62439, 5)
)
_Rrp_ObjectIdentity = ObjectIdentity
rrp = _Rrp_ObjectIdentity(
    (1, 0, 62439, 6)
)
_Ptp_ObjectIdentity = ObjectIdentity
ptp = _Ptp_ObjectIdentity(
    (1, 0, 62439, 7)
)

# Managed Objects groups

lreDefaultGrp = ObjectGroup(
    (1, 0, 62439, 2, 22, 1, 1, 1)
)
lreDefaultGrp.setObjects(
      *(("IEC-62439-3-MIB", "lreManufacturerName"),
        ("IEC-62439-3-MIB", "lreInterfaceCount"),
        ("IEC-62439-3-MIB", "lreRowStatus"),
        ("IEC-62439-3-MIB", "lreNodeType"),
        ("IEC-62439-3-MIB", "lreNodeName"),
        ("IEC-62439-3-MIB", "lreVersionName"),
        ("IEC-62439-3-MIB", "lreMacAddress"),
        ("IEC-62439-3-MIB", "lrePortAdminStateA"),
        ("IEC-62439-3-MIB", "lrePortAdminStateB"),
        ("IEC-62439-3-MIB", "lreLinkStatusA"),
        ("IEC-62439-3-MIB", "lreLinkStatusB"),
        ("IEC-62439-3-MIB", "lreDuplicateDiscard"),
        ("IEC-62439-3-MIB", "lreTransparentReception"),
        ("IEC-62439-3-MIB", "lreHsrLREMode"),
        ("IEC-62439-3-MIB", "lreSwitchingEndNode"),
        ("IEC-62439-3-MIB", "lreRedBoxIdentity"),
        ("IEC-62439-3-MIB", "lreEvaluateSupervision"),
        ("IEC-62439-3-MIB", "lreNodesTableClear"),
        ("IEC-62439-3-MIB", "lreProxyNodeTableClear"),
        ("IEC-62439-3-MIB", "lreDupListResideMaxTime"),
        ("IEC-62439-3-MIB", "lreCntTxA"),
        ("IEC-62439-3-MIB", "lreCntTxB"),
        ("IEC-62439-3-MIB", "lreCntTxC"),
        ("IEC-62439-3-MIB", "lreCntErrWrongLanA"),
        ("IEC-62439-3-MIB", "lreCntErrWrongLanB"),
        ("IEC-62439-3-MIB", "lreCntErrWrongLanC"),
        ("IEC-62439-3-MIB", "lreCntRxA"),
        ("IEC-62439-3-MIB", "lreCntRxB"),
        ("IEC-62439-3-MIB", "lreCntRxC"),
        ("IEC-62439-3-MIB", "lreCntErrorsA"),
        ("IEC-62439-3-MIB", "lreCntErrorsB"),
        ("IEC-62439-3-MIB", "lreCntErrorsC"),
        ("IEC-62439-3-MIB", "lreCntNodes"),
        ("IEC-62439-3-MIB", "lreCntProxyNodes"),
        ("IEC-62439-3-MIB", "lreCntUniqueA"),
        ("IEC-62439-3-MIB", "lreCntUniqueB"),
        ("IEC-62439-3-MIB", "lreCntUniqueC"),
        ("IEC-62439-3-MIB", "lreCntDuplicateA"),
        ("IEC-62439-3-MIB", "lreCntDuplicateB"),
        ("IEC-62439-3-MIB", "lreCntDuplicateC"),
        ("IEC-62439-3-MIB", "lreCntMultiA"),
        ("IEC-62439-3-MIB", "lreCntMultiB"),
        ("IEC-62439-3-MIB", "lreCntMultiC"),
        ("IEC-62439-3-MIB", "lreCntOwnRxA"),
        ("IEC-62439-3-MIB", "lreCntOwnRxB"),
        ("IEC-62439-3-MIB", "lreNodesMacAddress"),
        ("IEC-62439-3-MIB", "lreTimeLastSeenA"),
        ("IEC-62439-3-MIB", "lreTimeLastSeenB"),
        ("IEC-62439-3-MIB", "lreRemNodeType"),
        ("IEC-62439-3-MIB", "lreProxyNodeMacAddress"))
)
if mibBuilder.loadTexts:
    lreDefaultGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

linkRedundancyCompliance = ModuleCompliance(
    (1, 0, 62439, 2, 22, 2, 1)
)
linkRedundancyCompliance.setObjects(
    ("IEC-62439-3-MIB", "lreDefaultGrp")
)
if mibBuilder.loadTexts:
    linkRedundancyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEC-62439-3-MIB",
    **{"SecondFraction": SecondFraction,
       "iec62439": iec62439,
       "mrp": mrp,
       "prp": prp,
       "linkRedundancyEntityNotifications": linkRedundancyEntityNotifications,
       "linkRedundancyEntityObjects": linkRedundancyEntityObjects,
       "lreConfiguration": lreConfiguration,
       "lreConfigurationGeneralGroup": lreConfigurationGeneralGroup,
       "lreManufacturerName": lreManufacturerName,
       "lreInterfaceCount": lreInterfaceCount,
       "lreConfigurationInterfaceGroup": lreConfigurationInterfaceGroup,
       "lreConfigurationInterfaces": lreConfigurationInterfaces,
       "lreInterfaceConfigTable": lreInterfaceConfigTable,
       "lreInterfaceConfigEntry": lreInterfaceConfigEntry,
       "lreInterfaceConfigIndex": lreInterfaceConfigIndex,
       "lreRowStatus": lreRowStatus,
       "lreNodeType": lreNodeType,
       "lreNodeName": lreNodeName,
       "lreVersionName": lreVersionName,
       "lreMacAddress": lreMacAddress,
       "lrePortAdminStateA": lrePortAdminStateA,
       "lrePortAdminStateB": lrePortAdminStateB,
       "lreLinkStatusA": lreLinkStatusA,
       "lreLinkStatusB": lreLinkStatusB,
       "lreDuplicateDiscard": lreDuplicateDiscard,
       "lreTransparentReception": lreTransparentReception,
       "lreHsrLREMode": lreHsrLREMode,
       "lreSwitchingEndNode": lreSwitchingEndNode,
       "lreRedBoxIdentity": lreRedBoxIdentity,
       "lreEvaluateSupervision": lreEvaluateSupervision,
       "lreNodesTableClear": lreNodesTableClear,
       "lreProxyNodeTableClear": lreProxyNodeTableClear,
       "lreDupListResideMaxTime": lreDupListResideMaxTime,
       "lreStatistics": lreStatistics,
       "lreStatisticsInterfaceGroup": lreStatisticsInterfaceGroup,
       "lreStatisticsInterfaces": lreStatisticsInterfaces,
       "lreInterfaceStatsTable": lreInterfaceStatsTable,
       "lreInterfaceStatsEntry": lreInterfaceStatsEntry,
       "lreInterfaceStatsIndex": lreInterfaceStatsIndex,
       "lreCntTxA": lreCntTxA,
       "lreCntTxB": lreCntTxB,
       "lreCntTxC": lreCntTxC,
       "lreCntErrWrongLanA": lreCntErrWrongLanA,
       "lreCntErrWrongLanB": lreCntErrWrongLanB,
       "lreCntErrWrongLanC": lreCntErrWrongLanC,
       "lreCntRxA": lreCntRxA,
       "lreCntRxB": lreCntRxB,
       "lreCntRxC": lreCntRxC,
       "lreCntErrorsA": lreCntErrorsA,
       "lreCntErrorsB": lreCntErrorsB,
       "lreCntErrorsC": lreCntErrorsC,
       "lreCntNodes": lreCntNodes,
       "lreCntProxyNodes": lreCntProxyNodes,
       "lreCntUniqueA": lreCntUniqueA,
       "lreCntUniqueB": lreCntUniqueB,
       "lreCntUniqueC": lreCntUniqueC,
       "lreCntDuplicateA": lreCntDuplicateA,
       "lreCntDuplicateB": lreCntDuplicateB,
       "lreCntDuplicateC": lreCntDuplicateC,
       "lreCntMultiA": lreCntMultiA,
       "lreCntMultiB": lreCntMultiB,
       "lreCntMultiC": lreCntMultiC,
       "lreCntOwnRxA": lreCntOwnRxA,
       "lreCntOwnRxB": lreCntOwnRxB,
       "lreNodesTable": lreNodesTable,
       "lreNodesEntry": lreNodesEntry,
       "lreNodesIndex": lreNodesIndex,
       "lreNodesMacAddress": lreNodesMacAddress,
       "lreTimeLastSeenA": lreTimeLastSeenA,
       "lreTimeLastSeenB": lreTimeLastSeenB,
       "lreRemNodeType": lreRemNodeType,
       "lreProxyNodeTable": lreProxyNodeTable,
       "lreProxyNodeEntry": lreProxyNodeEntry,
       "lreProxyNodeIndex": lreProxyNodeIndex,
       "lreProxyNodeMacAddress": lreProxyNodeMacAddress,
       "linkRedundancyEntityConformance": linkRedundancyEntityConformance,
       "linkRedundancyConformance": linkRedundancyConformance,
       "lreGroups": lreGroups,
       "lreDefaultGrp": lreDefaultGrp,
       "linkRedundancyCompliances": linkRedundancyCompliances,
       "linkRedundancyCompliance": linkRedundancyCompliance,
       "crp": crp,
       "brp": brp,
       "drp": drp,
       "rrp": rrp,
       "ptp": ptp}
)
