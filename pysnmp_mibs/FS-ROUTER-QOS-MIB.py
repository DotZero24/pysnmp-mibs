# SNMP MIB module (FS-ROUTER-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ROUTER-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:18 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

fsRouterQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106)
)
if mibBuilder.loadTexts:
    fsRouterQoSMIB.setRevisions(
        ("2011-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSCosType(TextualConvention, Integer32):
    status = "current"
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
        *(("cos-be", 1),
          ("cos-af1", 2),
          ("cos-af2", 3),
          ("cos-af3", 4),
          ("cos-af4", 5),
          ("cos-ef", 6),
          ("cos-cs6", 7),
          ("cos-cs7", 8))
    )



class FSQType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("q-lpq", 1),
          ("q-wfq", 2),
          ("q-pq", 3))
    )



class FSQDirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d-input", 1),
          ("d-output", 2))
    )



class FSLayerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l3-layer", 0),
          ("link-layer", 1),
          ("all-layer", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsCBQoSMIBObjects_ObjectIdentity = ObjectIdentity
fsCBQoSMIBObjects = _FsCBQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1)
)
_FsCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
fsCBQoSIfStaticsObjects = _FsCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1)
)
_FsCBQoSIfCbwfqRunInfoTable_Object = MibTable
fsCBQoSIfCbwfqRunInfoTable = _FsCBQoSIfCbwfqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqRunInfoTable.setStatus("current")
_FsCBQoSIfCbwfqRunInfoEntry_Object = MibTableRow
fsCBQoSIfCbwfqRunInfoEntry = _FsCBQoSIfCbwfqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1)
)
fsCBQoSIfCbwfqRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfCbwfqPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqRunInfoEntry.setStatus("current")
_FsCBQoSIfCbwfqPolicyIfIndex_Type = Integer32
_FsCBQoSIfCbwfqPolicyIfIndex_Object = MibTableColumn
fsCBQoSIfCbwfqPolicyIfIndex = _FsCBQoSIfCbwfqPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 1),
    _FsCBQoSIfCbwfqPolicyIfIndex_Type()
)
fsCBQoSIfCbwfqPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqPolicyIfIndex.setStatus("current")
_FsCBQoSIfCbwfqQueueSize_Type = Integer32
_FsCBQoSIfCbwfqQueueSize_Object = MibTableColumn
fsCBQoSIfCbwfqQueueSize = _FsCBQoSIfCbwfqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 2),
    _FsCBQoSIfCbwfqQueueSize_Type()
)
fsCBQoSIfCbwfqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqQueueSize.setStatus("current")
_FsCBQoSIfCbwfqDiscard_Type = Counter64
_FsCBQoSIfCbwfqDiscard_Object = MibTableColumn
fsCBQoSIfCbwfqDiscard = _FsCBQoSIfCbwfqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 3),
    _FsCBQoSIfCbwfqDiscard_Type()
)
fsCBQoSIfCbwfqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqDiscard.setStatus("current")
_FsCBQoSIfCbwfqEfQueueSize_Type = Integer32
_FsCBQoSIfCbwfqEfQueueSize_Object = MibTableColumn
fsCBQoSIfCbwfqEfQueueSize = _FsCBQoSIfCbwfqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 4),
    _FsCBQoSIfCbwfqEfQueueSize_Type()
)
fsCBQoSIfCbwfqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqEfQueueSize.setStatus("current")
_FsCBQoSIfCbwfqAfQueueSize_Type = Integer32
_FsCBQoSIfCbwfqAfQueueSize_Object = MibTableColumn
fsCBQoSIfCbwfqAfQueueSize = _FsCBQoSIfCbwfqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 5),
    _FsCBQoSIfCbwfqAfQueueSize_Type()
)
fsCBQoSIfCbwfqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqAfQueueSize.setStatus("current")
_FsCBQoSIfCbwfqBeQueueSize_Type = Integer32
_FsCBQoSIfCbwfqBeQueueSize_Object = MibTableColumn
fsCBQoSIfCbwfqBeQueueSize = _FsCBQoSIfCbwfqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 6),
    _FsCBQoSIfCbwfqBeQueueSize_Type()
)
fsCBQoSIfCbwfqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqBeQueueSize.setStatus("current")
_FsCBQoSIfCbwfqBeActiveQueueNum_Type = Integer32
_FsCBQoSIfCbwfqBeActiveQueueNum_Object = MibTableColumn
fsCBQoSIfCbwfqBeActiveQueueNum = _FsCBQoSIfCbwfqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 7),
    _FsCBQoSIfCbwfqBeActiveQueueNum_Type()
)
fsCBQoSIfCbwfqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqBeActiveQueueNum.setStatus("current")
_FsCBQoSIfCbwfqBeMaxActiveQueueNum_Type = Integer32
_FsCBQoSIfCbwfqBeMaxActiveQueueNum_Object = MibTableColumn
fsCBQoSIfCbwfqBeMaxActiveQueueNum = _FsCBQoSIfCbwfqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 8),
    _FsCBQoSIfCbwfqBeMaxActiveQueueNum_Type()
)
fsCBQoSIfCbwfqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqBeMaxActiveQueueNum.setStatus("current")
_FsCBQoSIfCbwfqBeTotalQueueNum_Type = Integer32
_FsCBQoSIfCbwfqBeTotalQueueNum_Object = MibTableColumn
fsCBQoSIfCbwfqBeTotalQueueNum = _FsCBQoSIfCbwfqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 9),
    _FsCBQoSIfCbwfqBeTotalQueueNum_Type()
)
fsCBQoSIfCbwfqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqBeTotalQueueNum.setStatus("current")
_FsCBQoSIfCbwfqAfAllocatedQueueNum_Type = Integer32
_FsCBQoSIfCbwfqAfAllocatedQueueNum_Object = MibTableColumn
fsCBQoSIfCbwfqAfAllocatedQueueNum = _FsCBQoSIfCbwfqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 10),
    _FsCBQoSIfCbwfqAfAllocatedQueueNum_Type()
)
fsCBQoSIfCbwfqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqAfAllocatedQueueNum.setStatus("current")
_FsCBQoSIfCbwfqPass_Type = Counter64
_FsCBQoSIfCbwfqPass_Object = MibTableColumn
fsCBQoSIfCbwfqPass = _FsCBQoSIfCbwfqPass_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 11),
    _FsCBQoSIfCbwfqPass_Type()
)
fsCBQoSIfCbwfqPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqPass.setStatus("current")


class _FsCBQoSIfCbwfqDroppedRateIn5Min_Type(Integer32):
    """Custom type fsCBQoSIfCbwfqDroppedRateIn5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsCBQoSIfCbwfqDroppedRateIn5Min_Type.__name__ = "Integer32"
_FsCBQoSIfCbwfqDroppedRateIn5Min_Object = MibTableColumn
fsCBQoSIfCbwfqDroppedRateIn5Min = _FsCBQoSIfCbwfqDroppedRateIn5Min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 12),
    _FsCBQoSIfCbwfqDroppedRateIn5Min_Type()
)
fsCBQoSIfCbwfqDroppedRateIn5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqDroppedRateIn5Min.setStatus("current")
_FsCBQoSIfCbwfqPassBytes_Type = Counter64
_FsCBQoSIfCbwfqPassBytes_Object = MibTableColumn
fsCBQoSIfCbwfqPassBytes = _FsCBQoSIfCbwfqPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 13),
    _FsCBQoSIfCbwfqPassBytes_Type()
)
fsCBQoSIfCbwfqPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqPassBytes.setStatus("current")
_FsCBQoSIfCbwfqDiscardBytes_Type = Counter64
_FsCBQoSIfCbwfqDiscardBytes_Object = MibTableColumn
fsCBQoSIfCbwfqDiscardBytes = _FsCBQoSIfCbwfqDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 1, 1, 14),
    _FsCBQoSIfCbwfqDiscardBytes_Type()
)
fsCBQoSIfCbwfqDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCbwfqDiscardBytes.setStatus("current")
_FsCBQoSIfClassMatchRunInfoTable_Object = MibTable
fsCBQoSIfClassMatchRunInfoTable = _FsCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchRunInfoTable.setStatus("current")
_FsCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
fsCBQoSIfClassMatchRunInfoEntry = _FsCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1)
)
fsCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfClassMatchIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfClassMatchPolicyDirection"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfClassMatchClassIndex"),
)
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_FsCBQoSIfClassMatchIfIndex_Type = Integer32
_FsCBQoSIfClassMatchIfIndex_Object = MibTableColumn
fsCBQoSIfClassMatchIfIndex = _FsCBQoSIfClassMatchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 1),
    _FsCBQoSIfClassMatchIfIndex_Type()
)
fsCBQoSIfClassMatchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchIfIndex.setStatus("current")


class _FsCBQoSIfClassMatchPolicyDirection_Type(Integer32):
    """Custom type fsCBQoSIfClassMatchPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_FsCBQoSIfClassMatchPolicyDirection_Type.__name__ = "Integer32"
_FsCBQoSIfClassMatchPolicyDirection_Object = MibTableColumn
fsCBQoSIfClassMatchPolicyDirection = _FsCBQoSIfClassMatchPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 2),
    _FsCBQoSIfClassMatchPolicyDirection_Type()
)
fsCBQoSIfClassMatchPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchPolicyDirection.setStatus("current")
_FsCBQoSIfClassMatchClassIndex_Type = Integer32
_FsCBQoSIfClassMatchClassIndex_Object = MibTableColumn
fsCBQoSIfClassMatchClassIndex = _FsCBQoSIfClassMatchClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 3),
    _FsCBQoSIfClassMatchClassIndex_Type()
)
fsCBQoSIfClassMatchClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchClassIndex.setStatus("current")
_FsCBQoSIfClassMatchedPackets_Type = Counter64
_FsCBQoSIfClassMatchedPackets_Object = MibTableColumn
fsCBQoSIfClassMatchedPackets = _FsCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 4),
    _FsCBQoSIfClassMatchedPackets_Type()
)
fsCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchedPackets.setStatus("current")
_FsCBQoSIfClassMatchedBytes_Type = Counter64
_FsCBQoSIfClassMatchedBytes_Object = MibTableColumn
fsCBQoSIfClassMatchedBytes = _FsCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 5),
    _FsCBQoSIfClassMatchedBytes_Type()
)
fsCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassMatchedBytes.setStatus("current")
_FsCBQosIfClassPassedPackets_Type = Counter64
_FsCBQosIfClassPassedPackets_Object = MibTableColumn
fsCBQosIfClassPassedPackets = _FsCBQosIfClassPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 6),
    _FsCBQosIfClassPassedPackets_Type()
)
fsCBQosIfClassPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQosIfClassPassedPackets.setStatus("current")
_FsCBQosIfClassDroppedPackets_Type = Counter64
_FsCBQosIfClassDroppedPackets_Object = MibTableColumn
fsCBQosIfClassDroppedPackets = _FsCBQosIfClassDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 7),
    _FsCBQosIfClassDroppedPackets_Type()
)
fsCBQosIfClassDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQosIfClassDroppedPackets.setStatus("current")


class _FsCBQoSIfPolicyName_Type(OctetString):
    """Custom type fsCBQoSIfPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsCBQoSIfPolicyName_Type.__name__ = "OctetString"
_FsCBQoSIfPolicyName_Object = MibTableColumn
fsCBQoSIfPolicyName = _FsCBQoSIfPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 8),
    _FsCBQoSIfPolicyName_Type()
)
fsCBQoSIfPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfPolicyName.setStatus("current")


class _FsCBQoSIfClassName_Type(OctetString):
    """Custom type fsCBQoSIfClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsCBQoSIfClassName_Type.__name__ = "OctetString"
_FsCBQoSIfClassName_Object = MibTableColumn
fsCBQoSIfClassName = _FsCBQoSIfClassName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 9),
    _FsCBQoSIfClassName_Type()
)
fsCBQoSIfClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassName.setStatus("current")
_FsCBQoSIfClassPassBytes_Type = Counter64
_FsCBQoSIfClassPassBytes_Object = MibTableColumn
fsCBQoSIfClassPassBytes = _FsCBQoSIfClassPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 10),
    _FsCBQoSIfClassPassBytes_Type()
)
fsCBQoSIfClassPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassPassBytes.setStatus("current")
_FsCBQoSIfClassDiscardBytes_Type = Counter64
_FsCBQoSIfClassDiscardBytes_Object = MibTableColumn
fsCBQoSIfClassDiscardBytes = _FsCBQoSIfClassDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 2, 1, 11),
    _FsCBQoSIfClassDiscardBytes_Type()
)
fsCBQoSIfClassDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfClassDiscardBytes.setStatus("current")
_FsCBQoSIfCarRunInfoTable_Object = MibTable
fsCBQoSIfCarRunInfoTable = _FsCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsCBQoSIfCarRunInfoTable.setStatus("current")
_FsCBQoSIfCarRunInfoEntry_Object = MibTableRow
fsCBQoSIfCarRunInfoEntry = _FsCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1)
)
fsCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfCarIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfCarPolicyDirection"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfCarClassIndex"),
)
if mibBuilder.loadTexts:
    fsCBQoSIfCarRunInfoEntry.setStatus("current")
_FsCBQoSIfCarIfIndex_Type = Integer32
_FsCBQoSIfCarIfIndex_Object = MibTableColumn
fsCBQoSIfCarIfIndex = _FsCBQoSIfCarIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 1),
    _FsCBQoSIfCarIfIndex_Type()
)
fsCBQoSIfCarIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarIfIndex.setStatus("current")


class _FsCBQoSIfCarPolicyDirection_Type(Integer32):
    """Custom type fsCBQoSIfCarPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_FsCBQoSIfCarPolicyDirection_Type.__name__ = "Integer32"
_FsCBQoSIfCarPolicyDirection_Object = MibTableColumn
fsCBQoSIfCarPolicyDirection = _FsCBQoSIfCarPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 2),
    _FsCBQoSIfCarPolicyDirection_Type()
)
fsCBQoSIfCarPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarPolicyDirection.setStatus("current")
_FsCBQoSIfCarClassIndex_Type = Integer32
_FsCBQoSIfCarClassIndex_Object = MibTableColumn
fsCBQoSIfCarClassIndex = _FsCBQoSIfCarClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 3),
    _FsCBQoSIfCarClassIndex_Type()
)
fsCBQoSIfCarClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarClassIndex.setStatus("current")
_FsCBQoSIfCarConformedPackets_Type = Counter64
_FsCBQoSIfCarConformedPackets_Object = MibTableColumn
fsCBQoSIfCarConformedPackets = _FsCBQoSIfCarConformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 4),
    _FsCBQoSIfCarConformedPackets_Type()
)
fsCBQoSIfCarConformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarConformedPackets.setStatus("current")
_FsCBQoSIfCarConformedBytes_Type = Counter64
_FsCBQoSIfCarConformedBytes_Object = MibTableColumn
fsCBQoSIfCarConformedBytes = _FsCBQoSIfCarConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 5),
    _FsCBQoSIfCarConformedBytes_Type()
)
fsCBQoSIfCarConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarConformedBytes.setStatus("current")
_FsCBQoSIfCarExceededPackets_Type = Counter64
_FsCBQoSIfCarExceededPackets_Object = MibTableColumn
fsCBQoSIfCarExceededPackets = _FsCBQoSIfCarExceededPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 6),
    _FsCBQoSIfCarExceededPackets_Type()
)
fsCBQoSIfCarExceededPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarExceededPackets.setStatus("current")
_FsCBQoSIfCarExceededBytes_Type = Counter64
_FsCBQoSIfCarExceededBytes_Object = MibTableColumn
fsCBQoSIfCarExceededBytes = _FsCBQoSIfCarExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 7),
    _FsCBQoSIfCarExceededBytes_Type()
)
fsCBQoSIfCarExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarExceededBytes.setStatus("current")
_FsCBQoSIfCarViolatedPackets_Type = Counter64
_FsCBQoSIfCarViolatedPackets_Object = MibTableColumn
fsCBQoSIfCarViolatedPackets = _FsCBQoSIfCarViolatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 8),
    _FsCBQoSIfCarViolatedPackets_Type()
)
fsCBQoSIfCarViolatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarViolatedPackets.setStatus("current")
_FsCBQoSIfCarViolatedBytes_Type = Counter64
_FsCBQoSIfCarViolatedBytes_Object = MibTableColumn
fsCBQoSIfCarViolatedBytes = _FsCBQoSIfCarViolatedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 3, 1, 9),
    _FsCBQoSIfCarViolatedBytes_Type()
)
fsCBQoSIfCarViolatedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfCarViolatedBytes.setStatus("current")
_FsCBQoSIfRemarkRunInfoTable_Object = MibTable
fsCBQoSIfRemarkRunInfoTable = _FsCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkRunInfoTable.setStatus("current")
_FsCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
fsCBQoSIfRemarkRunInfoEntry = _FsCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4, 1)
)
fsCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfRemarkIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfRemarkPolicyDirection"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfRemarkClassIndex"),
)
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkRunInfoEntry.setStatus("current")
_FsCBQoSIfRemarkIfIndex_Type = Integer32
_FsCBQoSIfRemarkIfIndex_Object = MibTableColumn
fsCBQoSIfRemarkIfIndex = _FsCBQoSIfRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4, 1, 1),
    _FsCBQoSIfRemarkIfIndex_Type()
)
fsCBQoSIfRemarkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkIfIndex.setStatus("current")


class _FsCBQoSIfRemarkPolicyDirection_Type(Integer32):
    """Custom type fsCBQoSIfRemarkPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_FsCBQoSIfRemarkPolicyDirection_Type.__name__ = "Integer32"
_FsCBQoSIfRemarkPolicyDirection_Object = MibTableColumn
fsCBQoSIfRemarkPolicyDirection = _FsCBQoSIfRemarkPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4, 1, 2),
    _FsCBQoSIfRemarkPolicyDirection_Type()
)
fsCBQoSIfRemarkPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkPolicyDirection.setStatus("current")
_FsCBQoSIfRemarkClassIndex_Type = Integer32
_FsCBQoSIfRemarkClassIndex_Object = MibTableColumn
fsCBQoSIfRemarkClassIndex = _FsCBQoSIfRemarkClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4, 1, 3),
    _FsCBQoSIfRemarkClassIndex_Type()
)
fsCBQoSIfRemarkClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkClassIndex.setStatus("current")
_FsCBQoSIfRemarkedPackets_Type = Counter64
_FsCBQoSIfRemarkedPackets_Object = MibTableColumn
fsCBQoSIfRemarkedPackets = _FsCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4, 1, 4),
    _FsCBQoSIfRemarkedPackets_Type()
)
fsCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkedPackets.setStatus("current")
_FsCBQoSIfRemarkedBytes_Type = Counter64
_FsCBQoSIfRemarkedBytes_Object = MibTableColumn
fsCBQoSIfRemarkedBytes = _FsCBQoSIfRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 4, 1, 5),
    _FsCBQoSIfRemarkedBytes_Type()
)
fsCBQoSIfRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfRemarkedBytes.setStatus("current")
_FsCBQoSIfQueueRunInfoTable_Object = MibTable
fsCBQoSIfQueueRunInfoTable = _FsCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsCBQoSIfQueueRunInfoTable.setStatus("current")
_FsCBQoSIfQueueRunInfoEntry_Object = MibTableRow
fsCBQoSIfQueueRunInfoEntry = _FsCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1)
)
fsCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfQueueIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfQueuePolicyDirection"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfQueueClassIndex"),
)
if mibBuilder.loadTexts:
    fsCBQoSIfQueueRunInfoEntry.setStatus("current")
_FsCBQoSIfQueueIfIndex_Type = Integer32
_FsCBQoSIfQueueIfIndex_Object = MibTableColumn
fsCBQoSIfQueueIfIndex = _FsCBQoSIfQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 1),
    _FsCBQoSIfQueueIfIndex_Type()
)
fsCBQoSIfQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueIfIndex.setStatus("current")


class _FsCBQoSIfQueuePolicyDirection_Type(Integer32):
    """Custom type fsCBQoSIfQueuePolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_FsCBQoSIfQueuePolicyDirection_Type.__name__ = "Integer32"
_FsCBQoSIfQueuePolicyDirection_Object = MibTableColumn
fsCBQoSIfQueuePolicyDirection = _FsCBQoSIfQueuePolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 2),
    _FsCBQoSIfQueuePolicyDirection_Type()
)
fsCBQoSIfQueuePolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueuePolicyDirection.setStatus("current")
_FsCBQoSIfQueueClassIndex_Type = Integer32
_FsCBQoSIfQueueClassIndex_Object = MibTableColumn
fsCBQoSIfQueueClassIndex = _FsCBQoSIfQueueClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 3),
    _FsCBQoSIfQueueClassIndex_Type()
)
fsCBQoSIfQueueClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueClassIndex.setStatus("current")
_FsCBQoSIfQueueMatchedPackets_Type = Counter64
_FsCBQoSIfQueueMatchedPackets_Object = MibTableColumn
fsCBQoSIfQueueMatchedPackets = _FsCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 4),
    _FsCBQoSIfQueueMatchedPackets_Type()
)
fsCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueMatchedPackets.setStatus("current")
_FsCBQoSIfQueueMatchedBytes_Type = Counter64
_FsCBQoSIfQueueMatchedBytes_Object = MibTableColumn
fsCBQoSIfQueueMatchedBytes = _FsCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 5),
    _FsCBQoSIfQueueMatchedBytes_Type()
)
fsCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueMatchedBytes.setStatus("current")
_FsCBQoSIfQueueEnqueuedPackets_Type = Counter64
_FsCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
fsCBQoSIfQueueEnqueuedPackets = _FsCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 6),
    _FsCBQoSIfQueueEnqueuedPackets_Type()
)
fsCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueEnqueuedPackets.setStatus("current")
_FsCBQoSIfQueueEnqueuedBytes_Type = Counter64
_FsCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
fsCBQoSIfQueueEnqueuedBytes = _FsCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 7),
    _FsCBQoSIfQueueEnqueuedBytes_Type()
)
fsCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueEnqueuedBytes.setStatus("current")
_FsCBQoSIfQueueDiscardedPackets_Type = Counter64
_FsCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
fsCBQoSIfQueueDiscardedPackets = _FsCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 8),
    _FsCBQoSIfQueueDiscardedPackets_Type()
)
fsCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueDiscardedPackets.setStatus("current")
_FsCBQoSIfQueueDiscardedBytes_Type = Counter64
_FsCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
fsCBQoSIfQueueDiscardedBytes = _FsCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 5, 1, 9),
    _FsCBQoSIfQueueDiscardedBytes_Type()
)
fsCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfQueueDiscardedBytes.setStatus("current")
_FsCBQoSIfWredRunInfoTable_Object = MibTable
fsCBQoSIfWredRunInfoTable = _FsCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fsCBQoSIfWredRunInfoTable.setStatus("current")
_FsCBQoSIfWredRunInfoEntry_Object = MibTableRow
fsCBQoSIfWredRunInfoEntry = _FsCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6, 1)
)
fsCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfWredIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfWredClassIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsCBQoSIfWredClassValue"),
)
if mibBuilder.loadTexts:
    fsCBQoSIfWredRunInfoEntry.setStatus("current")
_FsCBQoSIfWredIfIndex_Type = Integer32
_FsCBQoSIfWredIfIndex_Object = MibTableColumn
fsCBQoSIfWredIfIndex = _FsCBQoSIfWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6, 1, 1),
    _FsCBQoSIfWredIfIndex_Type()
)
fsCBQoSIfWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfWredIfIndex.setStatus("current")
_FsCBQoSIfWredClassIndex_Type = Integer32
_FsCBQoSIfWredClassIndex_Object = MibTableColumn
fsCBQoSIfWredClassIndex = _FsCBQoSIfWredClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6, 1, 2),
    _FsCBQoSIfWredClassIndex_Type()
)
fsCBQoSIfWredClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfWredClassIndex.setStatus("current")
_FsCBQoSIfWredClassValue_Type = Integer32
_FsCBQoSIfWredClassValue_Object = MibTableColumn
fsCBQoSIfWredClassValue = _FsCBQoSIfWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6, 1, 3),
    _FsCBQoSIfWredClassValue_Type()
)
fsCBQoSIfWredClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfWredClassValue.setStatus("current")
_FsCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_FsCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
fsCBQoSIfWredRandomDiscardedPackets = _FsCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6, 1, 4),
    _FsCBQoSIfWredRandomDiscardedPackets_Type()
)
fsCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_FsCBQoSIfWredTailDiscardedPackets_Type = Counter64
_FsCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
fsCBQoSIfWredTailDiscardedPackets = _FsCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 1, 1, 6, 1, 5),
    _FsCBQoSIfWredTailDiscardedPackets_Type()
)
fsCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCBQoSIfWredTailDiscardedPackets.setStatus("current")
_FsIfQoSMIBObjects_ObjectIdentity = ObjectIdentity
fsIfQoSMIBObjects = _FsIfQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2)
)
_FsIfQosPQRunInfoTable_Object = MibTable
fsIfQosPQRunInfoTable = _FsIfQosPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1)
)
if mibBuilder.loadTexts:
    fsIfQosPQRunInfoTable.setStatus("current")
_FsIfQosPQRunInfoEntry_Object = MibTableRow
fsIfQosPQRunInfoEntry = _FsIfQosPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1)
)
fsIfQosPQRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosPQIfIndex"),
)
if mibBuilder.loadTexts:
    fsIfQosPQRunInfoEntry.setStatus("current")
_FsIfQosPQIfIndex_Type = Integer32
_FsIfQosPQIfIndex_Object = MibTableColumn
fsIfQosPQIfIndex = _FsIfQosPQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 1),
    _FsIfQosPQIfIndex_Type()
)
fsIfQosPQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQIfIndex.setStatus("current")


class _FsIfQosPQListNum_Type(Integer32):
    """Custom type fsIfQosPQListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsIfQosPQListNum_Type.__name__ = "Integer32"
_FsIfQosPQListNum_Object = MibTableColumn
fsIfQosPQListNum = _FsIfQosPQListNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 2),
    _FsIfQosPQListNum_Type()
)
fsIfQosPQListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQListNum.setStatus("current")
_FsIfQosPQIfName_Type = OctetString
_FsIfQosPQIfName_Object = MibTableColumn
fsIfQosPQIfName = _FsIfQosPQIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 3),
    _FsIfQosPQIfName_Type()
)
fsIfQosPQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQIfName.setStatus("current")


class _FsIfQosPQHighPkt_Type(Integer32):
    """Custom type fsIfQosPQHighPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosPQHighPkt_Type.__name__ = "Integer32"
_FsIfQosPQHighPkt_Object = MibTableColumn
fsIfQosPQHighPkt = _FsIfQosPQHighPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 4),
    _FsIfQosPQHighPkt_Type()
)
fsIfQosPQHighPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQHighPkt.setStatus("current")
_FsIfQosPQHighDiscard_Type = Counter32
_FsIfQosPQHighDiscard_Object = MibTableColumn
fsIfQosPQHighDiscard = _FsIfQosPQHighDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 5),
    _FsIfQosPQHighDiscard_Type()
)
fsIfQosPQHighDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQHighDiscard.setStatus("current")


class _FsIfQosPQHighMaxQueLen_Type(Integer32):
    """Custom type fsIfQosPQHighMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosPQHighMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosPQHighMaxQueLen_Object = MibTableColumn
fsIfQosPQHighMaxQueLen = _FsIfQosPQHighMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 6),
    _FsIfQosPQHighMaxQueLen_Type()
)
fsIfQosPQHighMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQHighMaxQueLen.setStatus("current")


class _FsIfQosPQMiddlePkt_Type(Integer32):
    """Custom type fsIfQosPQMiddlePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosPQMiddlePkt_Type.__name__ = "Integer32"
_FsIfQosPQMiddlePkt_Object = MibTableColumn
fsIfQosPQMiddlePkt = _FsIfQosPQMiddlePkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 7),
    _FsIfQosPQMiddlePkt_Type()
)
fsIfQosPQMiddlePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQMiddlePkt.setStatus("current")
_FsIfQosPQMiddleDiscard_Type = Counter32
_FsIfQosPQMiddleDiscard_Object = MibTableColumn
fsIfQosPQMiddleDiscard = _FsIfQosPQMiddleDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 8),
    _FsIfQosPQMiddleDiscard_Type()
)
fsIfQosPQMiddleDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQMiddleDiscard.setStatus("current")


class _FsIfQosPQMiddleMaxQueLen_Type(Integer32):
    """Custom type fsIfQosPQMiddleMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosPQMiddleMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosPQMiddleMaxQueLen_Object = MibTableColumn
fsIfQosPQMiddleMaxQueLen = _FsIfQosPQMiddleMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 9),
    _FsIfQosPQMiddleMaxQueLen_Type()
)
fsIfQosPQMiddleMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQMiddleMaxQueLen.setStatus("current")


class _FsIfQosPQNormalPkt_Type(Integer32):
    """Custom type fsIfQosPQNormalPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosPQNormalPkt_Type.__name__ = "Integer32"
_FsIfQosPQNormalPkt_Object = MibTableColumn
fsIfQosPQNormalPkt = _FsIfQosPQNormalPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 10),
    _FsIfQosPQNormalPkt_Type()
)
fsIfQosPQNormalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQNormalPkt.setStatus("current")
_FsIfQosPQNormalDiscard_Type = Counter32
_FsIfQosPQNormalDiscard_Object = MibTableColumn
fsIfQosPQNormalDiscard = _FsIfQosPQNormalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 11),
    _FsIfQosPQNormalDiscard_Type()
)
fsIfQosPQNormalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQNormalDiscard.setStatus("current")


class _FsIfQosPQNormalMaxQueLen_Type(Integer32):
    """Custom type fsIfQosPQNormalMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosPQNormalMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosPQNormalMaxQueLen_Object = MibTableColumn
fsIfQosPQNormalMaxQueLen = _FsIfQosPQNormalMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 12),
    _FsIfQosPQNormalMaxQueLen_Type()
)
fsIfQosPQNormalMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQNormalMaxQueLen.setStatus("current")


class _FsIfQosPQLowPkt_Type(Integer32):
    """Custom type fsIfQosPQLowPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosPQLowPkt_Type.__name__ = "Integer32"
_FsIfQosPQLowPkt_Object = MibTableColumn
fsIfQosPQLowPkt = _FsIfQosPQLowPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 13),
    _FsIfQosPQLowPkt_Type()
)
fsIfQosPQLowPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQLowPkt.setStatus("current")
_FsIfQosPQLowDiscard_Type = Counter32
_FsIfQosPQLowDiscard_Object = MibTableColumn
fsIfQosPQLowDiscard = _FsIfQosPQLowDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 14),
    _FsIfQosPQLowDiscard_Type()
)
fsIfQosPQLowDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQLowDiscard.setStatus("current")


class _FsIfQosPQLowMaxQueLen_Type(Integer32):
    """Custom type fsIfQosPQLowMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosPQLowMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosPQLowMaxQueLen_Object = MibTableColumn
fsIfQosPQLowMaxQueLen = _FsIfQosPQLowMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 1, 1, 15),
    _FsIfQosPQLowMaxQueLen_Type()
)
fsIfQosPQLowMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosPQLowMaxQueLen.setStatus("current")
_FsIfQosCQRunInfoTable_Object = MibTable
fsIfQosCQRunInfoTable = _FsIfQosCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2)
)
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoTable.setStatus("current")
_FsIfQosCQRunInfoEntry_Object = MibTableRow
fsIfQosCQRunInfoEntry = _FsIfQosCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1)
)
fsIfQosCQRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosCQRunInfoIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosCQRunInfoQueNum"),
)
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoEntry.setStatus("current")
_FsIfQosCQRunInfoIfIndex_Type = Integer32
_FsIfQosCQRunInfoIfIndex_Object = MibTableColumn
fsIfQosCQRunInfoIfIndex = _FsIfQosCQRunInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1, 1),
    _FsIfQosCQRunInfoIfIndex_Type()
)
fsIfQosCQRunInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoIfIndex.setStatus("current")


class _FsIfQosCQRunInfoQueNum_Type(Integer32):
    """Custom type fsIfQosCQRunInfoQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsIfQosCQRunInfoQueNum_Type.__name__ = "Integer32"
_FsIfQosCQRunInfoQueNum_Object = MibTableColumn
fsIfQosCQRunInfoQueNum = _FsIfQosCQRunInfoQueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1, 2),
    _FsIfQosCQRunInfoQueNum_Type()
)
fsIfQosCQRunInfoQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoQueNum.setStatus("current")
_FsIfQosCQRunInfoIfName_Type = OctetString
_FsIfQosCQRunInfoIfName_Object = MibTableColumn
fsIfQosCQRunInfoIfName = _FsIfQosCQRunInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1, 3),
    _FsIfQosCQRunInfoIfName_Type()
)
fsIfQosCQRunInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoIfName.setStatus("current")


class _FsIfQosCQRunInfoQuePkt_Type(Integer32):
    """Custom type fsIfQosCQRunInfoQuePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosCQRunInfoQuePkt_Type.__name__ = "Integer32"
_FsIfQosCQRunInfoQuePkt_Object = MibTableColumn
fsIfQosCQRunInfoQuePkt = _FsIfQosCQRunInfoQuePkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1, 4),
    _FsIfQosCQRunInfoQuePkt_Type()
)
fsIfQosCQRunInfoQuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoQuePkt.setStatus("current")
_FsIfQosCQRunInfoQueDiscard_Type = Counter32
_FsIfQosCQRunInfoQueDiscard_Object = MibTableColumn
fsIfQosCQRunInfoQueDiscard = _FsIfQosCQRunInfoQueDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1, 5),
    _FsIfQosCQRunInfoQueDiscard_Type()
)
fsIfQosCQRunInfoQueDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoQueDiscard.setStatus("current")


class _FsIfQosCQRunInfoMaxQueLen_Type(Integer32):
    """Custom type fsIfQosCQRunInfoMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosCQRunInfoMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosCQRunInfoMaxQueLen_Object = MibTableColumn
fsIfQosCQRunInfoMaxQueLen = _FsIfQosCQRunInfoMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 2, 1, 6),
    _FsIfQosCQRunInfoMaxQueLen_Type()
)
fsIfQosCQRunInfoMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCQRunInfoMaxQueLen.setStatus("current")
_FsIfQosWFQRunInfoTable_Object = MibTable
fsIfQosWFQRunInfoTable = _FsIfQosWFQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3)
)
if mibBuilder.loadTexts:
    fsIfQosWFQRunInfoTable.setStatus("current")
_FsIfQosWFQRunInfoEntry_Object = MibTableRow
fsIfQosWFQRunInfoEntry = _FsIfQosWFQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1)
)
fsIfQosWFQRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosWFQIfIndex"),
)
if mibBuilder.loadTexts:
    fsIfQosWFQRunInfoEntry.setStatus("current")
_FsIfQosWFQIfIndex_Type = Integer32
_FsIfQosWFQIfIndex_Object = MibTableColumn
fsIfQosWFQIfIndex = _FsIfQosWFQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 1),
    _FsIfQosWFQIfIndex_Type()
)
fsIfQosWFQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQIfIndex.setStatus("current")
_FsIfQosWFQIfName_Type = OctetString
_FsIfQosWFQIfName_Object = MibTableColumn
fsIfQosWFQIfName = _FsIfQosWFQIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 2),
    _FsIfQosWFQIfName_Type()
)
fsIfQosWFQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQIfName.setStatus("current")


class _FsIfQosWFQMaxQueLen_Type(Integer32):
    """Custom type fsIfQosWFQMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosWFQMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosWFQMaxQueLen_Object = MibTableColumn
fsIfQosWFQMaxQueLen = _FsIfQosWFQMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 3),
    _FsIfQosWFQMaxQueLen_Type()
)
fsIfQosWFQMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQMaxQueLen.setStatus("current")


class _FsIfQosWFQTotalQueNum_Type(Integer32):
    """Custom type fsIfQosWFQTotalQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("a16", 16),
          ("a32", 32),
          ("a64", 64),
          ("a128", 128),
          ("a256", 256),
          ("a512", 512),
          ("a1024", 1024),
          ("a2048", 2048),
          ("a4096", 4096))
    )


_FsIfQosWFQTotalQueNum_Type.__name__ = "Integer32"
_FsIfQosWFQTotalQueNum_Object = MibTableColumn
fsIfQosWFQTotalQueNum = _FsIfQosWFQTotalQueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 4),
    _FsIfQosWFQTotalQueNum_Type()
)
fsIfQosWFQTotalQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQTotalQueNum.setStatus("current")
_FsIfQosWFQCurQueLen_Type = Integer32
_FsIfQosWFQCurQueLen_Object = MibTableColumn
fsIfQosWFQCurQueLen = _FsIfQosWFQCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 5),
    _FsIfQosWFQCurQueLen_Type()
)
fsIfQosWFQCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQCurQueLen.setStatus("current")
_FsIfQosWFQTotalDiscard_Type = Counter32
_FsIfQosWFQTotalDiscard_Object = MibTableColumn
fsIfQosWFQTotalDiscard = _FsIfQosWFQTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 6),
    _FsIfQosWFQTotalDiscard_Type()
)
fsIfQosWFQTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQTotalDiscard.setStatus("current")


class _FsIfQosWFQActiveQueNum_Type(Integer32):
    """Custom type fsIfQosWFQActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosWFQActiveQueNum_Type.__name__ = "Integer32"
_FsIfQosWFQActiveQueNum_Object = MibTableColumn
fsIfQosWFQActiveQueNum = _FsIfQosWFQActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 7),
    _FsIfQosWFQActiveQueNum_Type()
)
fsIfQosWFQActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQActiveQueNum.setStatus("current")


class _FsIfQosWFQMaxActiveQueNum_Type(Integer32):
    """Custom type fsIfQosWFQMaxActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsIfQosWFQMaxActiveQueNum_Type.__name__ = "Integer32"
_FsIfQosWFQMaxActiveQueNum_Object = MibTableColumn
fsIfQosWFQMaxActiveQueNum = _FsIfQosWFQMaxActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 3, 1, 8),
    _FsIfQosWFQMaxActiveQueNum_Type()
)
fsIfQosWFQMaxActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWFQMaxActiveQueNum.setStatus("current")
_FsIfQosWredRunInfoTable_Object = MibTable
fsIfQosWredRunInfoTable = _FsIfQosWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 4)
)
if mibBuilder.loadTexts:
    fsIfQosWredRunInfoTable.setStatus("current")
_FsIfQosWredRunInfoEntry_Object = MibTableRow
fsIfQosWredRunInfoEntry = _FsIfQosWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 4, 1)
)
fsIfQosWredRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosWredIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosWredValue"),
)
if mibBuilder.loadTexts:
    fsIfQosWredRunInfoEntry.setStatus("current")
_FsIfQosWredIfIndex_Type = Integer32
_FsIfQosWredIfIndex_Object = MibTableColumn
fsIfQosWredIfIndex = _FsIfQosWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 4, 1, 1),
    _FsIfQosWredIfIndex_Type()
)
fsIfQosWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWredIfIndex.setStatus("current")
_FsIfQosWredValue_Type = Integer32
_FsIfQosWredValue_Object = MibTableColumn
fsIfQosWredValue = _FsIfQosWredValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 4, 1, 2),
    _FsIfQosWredValue_Type()
)
fsIfQosWredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWredValue.setStatus("current")
_FsIfQosWredRandomDiscardedPackets_Type = Counter64
_FsIfQosWredRandomDiscardedPackets_Object = MibTableColumn
fsIfQosWredRandomDiscardedPackets = _FsIfQosWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 4, 1, 3),
    _FsIfQosWredRandomDiscardedPackets_Type()
)
fsIfQosWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWredRandomDiscardedPackets.setStatus("current")
_FsIfQosWredTailDiscardedPackets_Type = Counter64
_FsIfQosWredTailDiscardedPackets_Object = MibTableColumn
fsIfQosWredTailDiscardedPackets = _FsIfQosWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 4, 1, 4),
    _FsIfQosWredTailDiscardedPackets_Type()
)
fsIfQosWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosWredTailDiscardedPackets.setStatus("current")
_FsIfQosCARTable_Object = MibTable
fsIfQosCARTable = _FsIfQosCARTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5)
)
if mibBuilder.loadTexts:
    fsIfQosCARTable.setStatus("current")
_FsIfQosCAREntry_Object = MibTableRow
fsIfQosCAREntry = _FsIfQosCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1)
)
fsIfQosCAREntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosCARIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosCARPktDirection"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosCARindex"),
)
if mibBuilder.loadTexts:
    fsIfQosCAREntry.setStatus("current")
_FsIfQosCARIfIndex_Type = Integer32
_FsIfQosCARIfIndex_Object = MibTableColumn
fsIfQosCARIfIndex = _FsIfQosCARIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 1),
    _FsIfQosCARIfIndex_Type()
)
fsIfQosCARIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARIfIndex.setStatus("current")
_FsIfQosCARIfName_Type = OctetString
_FsIfQosCARIfName_Object = MibTableColumn
fsIfQosCARIfName = _FsIfQosCARIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 2),
    _FsIfQosCARIfName_Type()
)
fsIfQosCARIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARIfName.setStatus("current")


class _FsIfQosCARPktDirection_Type(Integer32):
    """Custom type fsIfQosCARPktDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("outout", 2))
    )


_FsIfQosCARPktDirection_Type.__name__ = "Integer32"
_FsIfQosCARPktDirection_Object = MibTableColumn
fsIfQosCARPktDirection = _FsIfQosCARPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 3),
    _FsIfQosCARPktDirection_Type()
)
fsIfQosCARPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARPktDirection.setStatus("current")


class _FsIfQosCARType_Type(Integer32):
    """Custom type fsIfQosCARType based on Integer32"""
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
        *(("acl", 1),
          ("dscp", 2),
          ("qos-group", 3),
          ("default", 4))
    )


_FsIfQosCARType_Type.__name__ = "Integer32"
_FsIfQosCARType_Object = MibTableColumn
fsIfQosCARType = _FsIfQosCARType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 4),
    _FsIfQosCARType_Type()
)
fsIfQosCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARType.setStatus("current")
_FsIfQosCARListNum_Type = Integer32
_FsIfQosCARListNum_Object = MibTableColumn
fsIfQosCARListNum = _FsIfQosCARListNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 5),
    _FsIfQosCARListNum_Type()
)
fsIfQosCARListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARListNum.setStatus("current")
_FsIfQosCARindex_Type = Integer32
_FsIfQosCARindex_Object = MibTableColumn
fsIfQosCARindex = _FsIfQosCARindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 6),
    _FsIfQosCARindex_Type()
)
fsIfQosCARindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARindex.setStatus("current")


class _FsIfQosCARCIR_Type(Integer32):
    """Custom type fsIfQosCARCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_FsIfQosCARCIR_Type.__name__ = "Integer32"
_FsIfQosCARCIR_Object = MibTableColumn
fsIfQosCARCIR = _FsIfQosCARCIR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 7),
    _FsIfQosCARCIR_Type()
)
fsIfQosCARCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARCIR.setStatus("current")


class _FsIfQosCARBurstSize_Type(Integer32):
    """Custom type fsIfQosCARBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_FsIfQosCARBurstSize_Type.__name__ = "Integer32"
_FsIfQosCARBurstSize_Object = MibTableColumn
fsIfQosCARBurstSize = _FsIfQosCARBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 8),
    _FsIfQosCARBurstSize_Type()
)
fsIfQosCARBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARBurstSize.setStatus("current")


class _FsIfQosCARExcessBurstSize_Type(Integer32):
    """Custom type fsIfQosCARExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_FsIfQosCARExcessBurstSize_Type.__name__ = "Integer32"
_FsIfQosCARExcessBurstSize_Object = MibTableColumn
fsIfQosCARExcessBurstSize = _FsIfQosCARExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 9),
    _FsIfQosCARExcessBurstSize_Type()
)
fsIfQosCARExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARExcessBurstSize.setStatus("current")


class _FsIfQosCARConformAction_Type(Integer32):
    """Custom type fsIfQosCARConformAction based on Integer32"""
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
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_FsIfQosCARConformAction_Type.__name__ = "Integer32"
_FsIfQosCARConformAction_Object = MibTableColumn
fsIfQosCARConformAction = _FsIfQosCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 10),
    _FsIfQosCARConformAction_Type()
)
fsIfQosCARConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARConformAction.setStatus("current")


class _FsIfQosCARExceedAction_Type(Integer32):
    """Custom type fsIfQosCARExceedAction based on Integer32"""
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
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_FsIfQosCARExceedAction_Type.__name__ = "Integer32"
_FsIfQosCARExceedAction_Object = MibTableColumn
fsIfQosCARExceedAction = _FsIfQosCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 11),
    _FsIfQosCARExceedAction_Type()
)
fsIfQosCARExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARExceedAction.setStatus("current")


class _FsIfQosCARConformNewPrec_Type(Integer32):
    """Custom type fsIfQosCARConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsIfQosCARConformNewPrec_Type.__name__ = "Integer32"
_FsIfQosCARConformNewPrec_Object = MibTableColumn
fsIfQosCARConformNewPrec = _FsIfQosCARConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 12),
    _FsIfQosCARConformNewPrec_Type()
)
fsIfQosCARConformNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARConformNewPrec.setStatus("current")


class _FsIfQosCARExceedNewPrec_Type(Integer32):
    """Custom type fsIfQosCARExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsIfQosCARExceedNewPrec_Type.__name__ = "Integer32"
_FsIfQosCARExceedNewPrec_Object = MibTableColumn
fsIfQosCARExceedNewPrec = _FsIfQosCARExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 13),
    _FsIfQosCARExceedNewPrec_Type()
)
fsIfQosCARExceedNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARExceedNewPrec.setStatus("current")
_FsIfQosCARConformPkt_Type = Counter32
_FsIfQosCARConformPkt_Object = MibTableColumn
fsIfQosCARConformPkt = _FsIfQosCARConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 14),
    _FsIfQosCARConformPkt_Type()
)
fsIfQosCARConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARConformPkt.setStatus("current")
_FsIfQosCARConformByte_Type = Counter32
_FsIfQosCARConformByte_Object = MibTableColumn
fsIfQosCARConformByte = _FsIfQosCARConformByte_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 15),
    _FsIfQosCARConformByte_Type()
)
fsIfQosCARConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARConformByte.setStatus("current")
_FsIfQosCARExceedPkt_Type = Counter32
_FsIfQosCARExceedPkt_Object = MibTableColumn
fsIfQosCARExceedPkt = _FsIfQosCARExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 16),
    _FsIfQosCARExceedPkt_Type()
)
fsIfQosCARExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARExceedPkt.setStatus("current")
_FsIfQosCARExceedByte_Type = Counter32
_FsIfQosCARExceedByte_Object = MibTableColumn
fsIfQosCARExceedByte = _FsIfQosCARExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 5, 1, 17),
    _FsIfQosCARExceedByte_Type()
)
fsIfQosCARExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosCARExceedByte.setStatus("current")
_FsIfQosGTSTable_Object = MibTable
fsIfQosGTSTable = _FsIfQosGTSTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6)
)
if mibBuilder.loadTexts:
    fsIfQosGTSTable.setStatus("current")
_FsIfQosGTSEntry_Object = MibTableRow
fsIfQosGTSEntry = _FsIfQosGTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1)
)
fsIfQosGTSEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosGTSIfIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosGTSType"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosGTSACLNum"),
)
if mibBuilder.loadTexts:
    fsIfQosGTSEntry.setStatus("current")
_FsIfQosGTSIfIndex_Type = Integer32
_FsIfQosGTSIfIndex_Object = MibTableColumn
fsIfQosGTSIfIndex = _FsIfQosGTSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 1),
    _FsIfQosGTSIfIndex_Type()
)
fsIfQosGTSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSIfIndex.setStatus("current")
_FsIfQosGTSIfName_Type = OctetString
_FsIfQosGTSIfName_Object = MibTableColumn
fsIfQosGTSIfName = _FsIfQosGTSIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 2),
    _FsIfQosGTSIfName_Type()
)
fsIfQosGTSIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSIfName.setStatus("current")


class _FsIfQosGTSType_Type(Integer32):
    """Custom type fsIfQosGTSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acl", 1),
          ("all", 2))
    )


_FsIfQosGTSType_Type.__name__ = "Integer32"
_FsIfQosGTSType_Object = MibTableColumn
fsIfQosGTSType = _FsIfQosGTSType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 3),
    _FsIfQosGTSType_Type()
)
fsIfQosGTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSType.setStatus("current")


class _FsIfQosGTSACLNum_Type(Integer32):
    """Custom type fsIfQosGTSACLNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_FsIfQosGTSACLNum_Type.__name__ = "Integer32"
_FsIfQosGTSACLNum_Object = MibTableColumn
fsIfQosGTSACLNum = _FsIfQosGTSACLNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 4),
    _FsIfQosGTSACLNum_Type()
)
fsIfQosGTSACLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSACLNum.setStatus("current")


class _FsIfQosGTSCIR_Type(Integer32):
    """Custom type fsIfQosGTSCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_FsIfQosGTSCIR_Type.__name__ = "Integer32"
_FsIfQosGTSCIR_Object = MibTableColumn
fsIfQosGTSCIR = _FsIfQosGTSCIR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 5),
    _FsIfQosGTSCIR_Type()
)
fsIfQosGTSCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSCIR.setStatus("current")


class _FsIfQosGTSBurstSize_Type(Integer32):
    """Custom type fsIfQosGTSBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_FsIfQosGTSBurstSize_Type.__name__ = "Integer32"
_FsIfQosGTSBurstSize_Object = MibTableColumn
fsIfQosGTSBurstSize = _FsIfQosGTSBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 6),
    _FsIfQosGTSBurstSize_Type()
)
fsIfQosGTSBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSBurstSize.setStatus("current")


class _FsIfQosGTSExcessBurstSize_Type(Integer32):
    """Custom type fsIfQosGTSExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_FsIfQosGTSExcessBurstSize_Type.__name__ = "Integer32"
_FsIfQosGTSExcessBurstSize_Object = MibTableColumn
fsIfQosGTSExcessBurstSize = _FsIfQosGTSExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 7),
    _FsIfQosGTSExcessBurstSize_Type()
)
fsIfQosGTSExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSExcessBurstSize.setStatus("current")


class _FsIfQosGTSMaxQueLen_Type(Integer32):
    """Custom type fsIfQosGTSMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsIfQosGTSMaxQueLen_Type.__name__ = "Integer32"
_FsIfQosGTSMaxQueLen_Object = MibTableColumn
fsIfQosGTSMaxQueLen = _FsIfQosGTSMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 8),
    _FsIfQosGTSMaxQueLen_Type()
)
fsIfQosGTSMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSMaxQueLen.setStatus("current")
_FsIfQosGTSCurQueLen_Type = Integer32
_FsIfQosGTSCurQueLen_Object = MibTableColumn
fsIfQosGTSCurQueLen = _FsIfQosGTSCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 9),
    _FsIfQosGTSCurQueLen_Type()
)
fsIfQosGTSCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSCurQueLen.setStatus("current")
_FsIfQosGTSPassPkt_Type = Counter32
_FsIfQosGTSPassPkt_Object = MibTableColumn
fsIfQosGTSPassPkt = _FsIfQosGTSPassPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 10),
    _FsIfQosGTSPassPkt_Type()
)
fsIfQosGTSPassPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSPassPkt.setStatus("current")
_FsIfQosGTSPassByte_Type = Counter32
_FsIfQosGTSPassByte_Object = MibTableColumn
fsIfQosGTSPassByte = _FsIfQosGTSPassByte_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 11),
    _FsIfQosGTSPassByte_Type()
)
fsIfQosGTSPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSPassByte.setStatus("current")
_FsIfQosGTSDiscardPkt_Type = Counter32
_FsIfQosGTSDiscardPkt_Object = MibTableColumn
fsIfQosGTSDiscardPkt = _FsIfQosGTSDiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 12),
    _FsIfQosGTSDiscardPkt_Type()
)
fsIfQosGTSDiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSDiscardPkt.setStatus("current")
_FsIfQosGTSDiscardByte_Type = Counter32
_FsIfQosGTSDiscardByte_Object = MibTableColumn
fsIfQosGTSDiscardByte = _FsIfQosGTSDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 6, 1, 13),
    _FsIfQosGTSDiscardByte_Type()
)
fsIfQosGTSDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosGTSDiscardByte.setStatus("current")
_FsIfQosRTPIfQueueRunInfoTable_Object = MibTable
fsIfQosRTPIfQueueRunInfoTable = _FsIfQosRTPIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7)
)
if mibBuilder.loadTexts:
    fsIfQosRTPIfQueueRunInfoTable.setStatus("current")
_FsIfQosRTPIfQueueRunInfoEntry_Object = MibTableRow
fsIfQosRTPIfQueueRunInfoEntry = _FsIfQosRTPIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7, 1)
)
fsIfQosRTPIfQueueRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosRTPIfApplyIfIndex"),
)
if mibBuilder.loadTexts:
    fsIfQosRTPIfQueueRunInfoEntry.setStatus("current")
_FsIfQosRTPIfApplyIfIndex_Type = Integer32
_FsIfQosRTPIfApplyIfIndex_Object = MibTableColumn
fsIfQosRTPIfApplyIfIndex = _FsIfQosRTPIfApplyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7, 1, 1),
    _FsIfQosRTPIfApplyIfIndex_Type()
)
fsIfQosRTPIfApplyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosRTPIfApplyIfIndex.setStatus("current")
_FsIfQosRTPIfQueueSize_Type = Counter32
_FsIfQosRTPIfQueueSize_Object = MibTableColumn
fsIfQosRTPIfQueueSize = _FsIfQosRTPIfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7, 1, 2),
    _FsIfQosRTPIfQueueSize_Type()
)
fsIfQosRTPIfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosRTPIfQueueSize.setStatus("current")
_FsIfQosRTPIfQueueMaxSize_Type = Counter32
_FsIfQosRTPIfQueueMaxSize_Object = MibTableColumn
fsIfQosRTPIfQueueMaxSize = _FsIfQosRTPIfQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7, 1, 3),
    _FsIfQosRTPIfQueueMaxSize_Type()
)
fsIfQosRTPIfQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosRTPIfQueueMaxSize.setStatus("current")
_FsIfQosRTPIfQueueOutputs_Type = Counter32
_FsIfQosRTPIfQueueOutputs_Object = MibTableColumn
fsIfQosRTPIfQueueOutputs = _FsIfQosRTPIfQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7, 1, 4),
    _FsIfQosRTPIfQueueOutputs_Type()
)
fsIfQosRTPIfQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosRTPIfQueueOutputs.setStatus("current")
_FsIfQosRTPIfQueueDiscards_Type = Counter32
_FsIfQosRTPIfQueueDiscards_Object = MibTableColumn
fsIfQosRTPIfQueueDiscards = _FsIfQosRTPIfQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 7, 1, 5),
    _FsIfQosRTPIfQueueDiscards_Type()
)
fsIfQosRTPIfQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosRTPIfQueueDiscards.setStatus("current")
_FsIfQosFlowLimitRunInfoTable_Object = MibTable
fsIfQosFlowLimitRunInfoTable = _FsIfQosFlowLimitRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8)
)
if mibBuilder.loadTexts:
    fsIfQosFlowLimitRunInfoTable.setStatus("current")
_FsIfQosFlowLimitRunInfoEntry_Object = MibTableRow
fsIfQosFlowLimitRunInfoEntry = _FsIfQosFlowLimitRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1)
)
fsIfQosFlowLimitRunInfoEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosFlowLimitLabelNum"),
    (0, "FS-ROUTER-QOS-MIB", "fsIfQosFlowLimitPktDirection"),
)
if mibBuilder.loadTexts:
    fsIfQosFlowLimitRunInfoEntry.setStatus("current")


class _FsIfQosFlowLimitLabelNum_Type(Integer32):
    """Custom type fsIfQosFlowLimitLabelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsIfQosFlowLimitLabelNum_Type.__name__ = "Integer32"
_FsIfQosFlowLimitLabelNum_Object = MibTableColumn
fsIfQosFlowLimitLabelNum = _FsIfQosFlowLimitLabelNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 1),
    _FsIfQosFlowLimitLabelNum_Type()
)
fsIfQosFlowLimitLabelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitLabelNum.setStatus("current")


class _FsIfQosFlowLimitPktDirection_Type(Integer32):
    """Custom type fsIfQosFlowLimitPktDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_FsIfQosFlowLimitPktDirection_Type.__name__ = "Integer32"
_FsIfQosFlowLimitPktDirection_Object = MibTableColumn
fsIfQosFlowLimitPktDirection = _FsIfQosFlowLimitPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 2),
    _FsIfQosFlowLimitPktDirection_Type()
)
fsIfQosFlowLimitPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitPktDirection.setStatus("current")


class _FsIfQosFlowLimitCIR_Type(Integer32):
    """Custom type fsIfQosFlowLimitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_FsIfQosFlowLimitCIR_Type.__name__ = "Integer32"
_FsIfQosFlowLimitCIR_Object = MibTableColumn
fsIfQosFlowLimitCIR = _FsIfQosFlowLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 3),
    _FsIfQosFlowLimitCIR_Type()
)
fsIfQosFlowLimitCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitCIR.setStatus("current")


class _FsIfQosFlowLimitBurstSize_Type(Integer32):
    """Custom type fsIfQosFlowLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_FsIfQosFlowLimitBurstSize_Type.__name__ = "Integer32"
_FsIfQosFlowLimitBurstSize_Object = MibTableColumn
fsIfQosFlowLimitBurstSize = _FsIfQosFlowLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 4),
    _FsIfQosFlowLimitBurstSize_Type()
)
fsIfQosFlowLimitBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitBurstSize.setStatus("current")


class _FsIfQosFlowLimitExcessBurstSize_Type(Integer32):
    """Custom type fsIfQosFlowLimitExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_FsIfQosFlowLimitExcessBurstSize_Type.__name__ = "Integer32"
_FsIfQosFlowLimitExcessBurstSize_Object = MibTableColumn
fsIfQosFlowLimitExcessBurstSize = _FsIfQosFlowLimitExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 5),
    _FsIfQosFlowLimitExcessBurstSize_Type()
)
fsIfQosFlowLimitExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitExcessBurstSize.setStatus("current")


class _FsIfQosFlowLimitConformAction_Type(Integer32):
    """Custom type fsIfQosFlowLimitConformAction based on Integer32"""
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
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_FsIfQosFlowLimitConformAction_Type.__name__ = "Integer32"
_FsIfQosFlowLimitConformAction_Object = MibTableColumn
fsIfQosFlowLimitConformAction = _FsIfQosFlowLimitConformAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 6),
    _FsIfQosFlowLimitConformAction_Type()
)
fsIfQosFlowLimitConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitConformAction.setStatus("current")


class _FsIfQosFlowLimitExceedAction_Type(Integer32):
    """Custom type fsIfQosFlowLimitExceedAction based on Integer32"""
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
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_FsIfQosFlowLimitExceedAction_Type.__name__ = "Integer32"
_FsIfQosFlowLimitExceedAction_Object = MibTableColumn
fsIfQosFlowLimitExceedAction = _FsIfQosFlowLimitExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 7),
    _FsIfQosFlowLimitExceedAction_Type()
)
fsIfQosFlowLimitExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitExceedAction.setStatus("current")


class _FsIfQosFlowLimitConformNewPrec_Type(Integer32):
    """Custom type fsIfQosFlowLimitConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIfQosFlowLimitConformNewPrec_Type.__name__ = "Integer32"
_FsIfQosFlowLimitConformNewPrec_Object = MibTableColumn
fsIfQosFlowLimitConformNewPrec = _FsIfQosFlowLimitConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 8),
    _FsIfQosFlowLimitConformNewPrec_Type()
)
fsIfQosFlowLimitConformNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitConformNewPrec.setStatus("current")


class _FsIfQosFlowLimitExceedNewPrec_Type(Integer32):
    """Custom type fsIfQosFlowLimitExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIfQosFlowLimitExceedNewPrec_Type.__name__ = "Integer32"
_FsIfQosFlowLimitExceedNewPrec_Object = MibTableColumn
fsIfQosFlowLimitExceedNewPrec = _FsIfQosFlowLimitExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 9),
    _FsIfQosFlowLimitExceedNewPrec_Type()
)
fsIfQosFlowLimitExceedNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitExceedNewPrec.setStatus("current")
_FsIfQosFlowLimitConformPkt_Type = Counter32
_FsIfQosFlowLimitConformPkt_Object = MibTableColumn
fsIfQosFlowLimitConformPkt = _FsIfQosFlowLimitConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 10),
    _FsIfQosFlowLimitConformPkt_Type()
)
fsIfQosFlowLimitConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitConformPkt.setStatus("current")
_FsIfQosFlowLimitConformByte_Type = Counter32
_FsIfQosFlowLimitConformByte_Object = MibTableColumn
fsIfQosFlowLimitConformByte = _FsIfQosFlowLimitConformByte_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 11),
    _FsIfQosFlowLimitConformByte_Type()
)
fsIfQosFlowLimitConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitConformByte.setStatus("current")
_FsIfQosFlowLimitExceedPkt_Type = Counter32
_FsIfQosFlowLimitExceedPkt_Object = MibTableColumn
fsIfQosFlowLimitExceedPkt = _FsIfQosFlowLimitExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 12),
    _FsIfQosFlowLimitExceedPkt_Type()
)
fsIfQosFlowLimitExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitExceedPkt.setStatus("current")
_FsIfQosFlowLimitExceedByte_Type = Counter32
_FsIfQosFlowLimitExceedByte_Object = MibTableColumn
fsIfQosFlowLimitExceedByte = _FsIfQosFlowLimitExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 2, 8, 1, 13),
    _FsIfQosFlowLimitExceedByte_Type()
)
fsIfQosFlowLimitExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQosFlowLimitExceedByte.setStatus("current")
_FsHQoSMIBObjects_ObjectIdentity = ObjectIdentity
fsHQoSMIBObjects = _FsHQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3)
)
_FsHQoSScalarObjects_ObjectIdentity = ObjectIdentity
fsHQoSScalarObjects = _FsHQoSScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 1)
)


class _FsHQoSNameType_Type(Integer32):
    """Custom type fsHQoSNameType based on Integer32"""
    defaultValue = 0

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
        *(("unknownName", 0),
          ("userQNameIn", 1),
          ("userQNameOut", 2),
          ("userGroupQInName", 3),
          ("userGroupQOutName", 4),
          ("flowQName", 5),
          ("flowMapName", 6),
          ("trafficClassifierName", 7),
          ("trafficBehaviorName", 8),
          ("trafficPolicyName", 9),
          ("portQName", 10))
    )


_FsHQoSNameType_Type.__name__ = "Integer32"
_FsHQoSNameType_Object = MibScalar
fsHQoSNameType = _FsHQoSNameType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 1, 1),
    _FsHQoSNameType_Type()
)
fsHQoSNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSNameType.setStatus("current")


class _FsHQoSNameFind_Type(OctetString):
    """Custom type fsHQoSNameFind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSNameFind_Type.__name__ = "OctetString"
_FsHQoSNameFind_Object = MibScalar
fsHQoSNameFind = _FsHQoSNameFind_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 1, 2),
    _FsHQoSNameFind_Type()
)
fsHQoSNameFind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSNameFind.setStatus("current")


class _FsHQoSNameIndex_Type(Integer32):
    """Custom type fsHQoSNameIndex based on Integer32"""
    defaultValue = 0


_FsHQoSNameIndex_Type.__name__ = "Integer32"
_FsHQoSNameIndex_Object = MibScalar
fsHQoSNameIndex = _FsHQoSNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 1, 3),
    _FsHQoSNameIndex_Type()
)
fsHQoSNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSNameIndex.setStatus("current")
_FsHQoSUserQObjects_ObjectIdentity = ObjectIdentity
fsHQoSUserQObjects = _FsHQoSUserQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2)
)
_FsHQoSUserQInIndexNext_Type = Integer32
_FsHQoSUserQInIndexNext_Object = MibScalar
fsHQoSUserQInIndexNext = _FsHQoSUserQInIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 1),
    _FsHQoSUserQInIndexNext_Type()
)
fsHQoSUserQInIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserQInIndexNext.setStatus("current")
_FsHQoSUserQOutIndexNext_Type = Integer32
_FsHQoSUserQOutIndexNext_Object = MibScalar
fsHQoSUserQOutIndexNext = _FsHQoSUserQOutIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 2),
    _FsHQoSUserQOutIndexNext_Type()
)
fsHQoSUserQOutIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserQOutIndexNext.setStatus("current")
_FsHQoSUserQTable_Object = MibTable
fsHQoSUserQTable = _FsHQoSUserQTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3)
)
if mibBuilder.loadTexts:
    fsHQoSUserQTable.setStatus("current")
_FsHQoSUserQEntry_Object = MibTableRow
fsHQoSUserQEntry = _FsHQoSUserQEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1)
)
fsHQoSUserQEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSUserQIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSUserQEntry.setStatus("current")
_FsHQoSUserQIndex_Type = Unsigned32
_FsHQoSUserQIndex_Object = MibTableColumn
fsHQoSUserQIndex = _FsHQoSUserQIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 1),
    _FsHQoSUserQIndex_Type()
)
fsHQoSUserQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSUserQIndex.setStatus("current")


class _FsHQoSUserQName_Type(OctetString):
    """Custom type fsHQoSUserQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSUserQName_Type.__name__ = "OctetString"
_FsHQoSUserQName_Object = MibTableColumn
fsHQoSUserQName = _FsHQoSUserQName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 2),
    _FsHQoSUserQName_Type()
)
fsHQoSUserQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQName.setStatus("current")
_FsHQoSUserQDirection_Type = FSQDirectionType
_FsHQoSUserQDirection_Object = MibTableColumn
fsHQoSUserQDirection = _FsHQoSUserQDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 3),
    _FsHQoSUserQDirection_Type()
)
fsHQoSUserQDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQDirection.setStatus("current")
_FsHQoSUserQRowStatus_Type = RowStatus
_FsHQoSUserQRowStatus_Object = MibTableColumn
fsHQoSUserQRowStatus = _FsHQoSUserQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 4),
    _FsHQoSUserQRowStatus_Type()
)
fsHQoSUserQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQRowStatus.setStatus("current")


class _FsHQoSUserQFlowQName_Type(OctetString):
    """Custom type fsHQoSUserQFlowQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSUserQFlowQName_Type.__name__ = "OctetString"
_FsHQoSUserQFlowQName_Object = MibTableColumn
fsHQoSUserQFlowQName = _FsHQoSUserQFlowQName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 5),
    _FsHQoSUserQFlowQName_Type()
)
fsHQoSUserQFlowQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQFlowQName.setStatus("current")
_FsHQoSUserQFlowQIndex_Type = Unsigned32
_FsHQoSUserQFlowQIndex_Object = MibTableColumn
fsHQoSUserQFlowQIndex = _FsHQoSUserQFlowQIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 6),
    _FsHQoSUserQFlowQIndex_Type()
)
fsHQoSUserQFlowQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserQFlowQIndex.setStatus("current")


class _FsHQoSUserQGroupName_Type(OctetString):
    """Custom type fsHQoSUserQGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSUserQGroupName_Type.__name__ = "OctetString"
_FsHQoSUserQGroupName_Object = MibTableColumn
fsHQoSUserQGroupName = _FsHQoSUserQGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 7),
    _FsHQoSUserQGroupName_Type()
)
fsHQoSUserQGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQGroupName.setStatus("current")
_FsHQoSUserQGroupIndex_Type = Unsigned32
_FsHQoSUserQGroupIndex_Object = MibTableColumn
fsHQoSUserQGroupIndex = _FsHQoSUserQGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 8),
    _FsHQoSUserQGroupIndex_Type()
)
fsHQoSUserQGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserQGroupIndex.setStatus("current")


class _FsHQoSUserQFlowMapName_Type(OctetString):
    """Custom type fsHQoSUserQFlowMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSUserQFlowMapName_Type.__name__ = "OctetString"
_FsHQoSUserQFlowMapName_Object = MibTableColumn
fsHQoSUserQFlowMapName = _FsHQoSUserQFlowMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 9),
    _FsHQoSUserQFlowMapName_Type()
)
fsHQoSUserQFlowMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQFlowMapName.setStatus("current")
_FsHQoSUserQFlowMapIndex_Type = Unsigned32
_FsHQoSUserQFlowMapIndex_Object = MibTableColumn
fsHQoSUserQFlowMapIndex = _FsHQoSUserQFlowMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 10),
    _FsHQoSUserQFlowMapIndex_Type()
)
fsHQoSUserQFlowMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserQFlowMapIndex.setStatus("current")


class _FsHQoSUserQCIR_Type(Unsigned32):
    """Custom type fsHQoSUserQCIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSUserQCIR_Type.__name__ = "Unsigned32"
_FsHQoSUserQCIR_Object = MibTableColumn
fsHQoSUserQCIR = _FsHQoSUserQCIR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 11),
    _FsHQoSUserQCIR_Type()
)
fsHQoSUserQCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQCIR.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSUserQCIR.setUnits("kilobits per second")


class _FsHQoSUserQPIR_Type(Unsigned32):
    """Custom type fsHQoSUserQPIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_FsHQoSUserQPIR_Type.__name__ = "Unsigned32"
_FsHQoSUserQPIR_Object = MibTableColumn
fsHQoSUserQPIR = _FsHQoSUserQPIR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 2, 3, 1, 12),
    _FsHQoSUserQPIR_Type()
)
fsHQoSUserQPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserQPIR.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSUserQPIR.setUnits("kilobits per second")
_FsHQoSUserGroupQObjects_ObjectIdentity = ObjectIdentity
fsHQoSUserGroupQObjects = _FsHQoSUserGroupQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3)
)
_FsHQoSUserGroupQInIndexNext_Type = Integer32
_FsHQoSUserGroupQInIndexNext_Object = MibScalar
fsHQoSUserGroupQInIndexNext = _FsHQoSUserGroupQInIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 1),
    _FsHQoSUserGroupQInIndexNext_Type()
)
fsHQoSUserGroupQInIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQInIndexNext.setStatus("current")
_FsHQoSUserGroupQOutIndexNext_Type = Integer32
_FsHQoSUserGroupQOutIndexNext_Object = MibScalar
fsHQoSUserGroupQOutIndexNext = _FsHQoSUserGroupQOutIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 2),
    _FsHQoSUserGroupQOutIndexNext_Type()
)
fsHQoSUserGroupQOutIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQOutIndexNext.setStatus("current")
_FsHQoSUserGroupQTable_Object = MibTable
fsHQoSUserGroupQTable = _FsHQoSUserGroupQTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3)
)
if mibBuilder.loadTexts:
    fsHQoSUserGroupQTable.setStatus("current")
_FsHQoSUserGroupQEntry_Object = MibTableRow
fsHQoSUserGroupQEntry = _FsHQoSUserGroupQEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3, 1)
)
fsHQoSUserGroupQEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSUserGroupQIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSUserGroupQEntry.setStatus("current")
_FsHQoSUserGroupQIndex_Type = Unsigned32
_FsHQoSUserGroupQIndex_Object = MibTableColumn
fsHQoSUserGroupQIndex = _FsHQoSUserGroupQIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3, 1, 1),
    _FsHQoSUserGroupQIndex_Type()
)
fsHQoSUserGroupQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQIndex.setStatus("current")


class _FsHQoSUserGroupQName_Type(OctetString):
    """Custom type fsHQoSUserGroupQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSUserGroupQName_Type.__name__ = "OctetString"
_FsHQoSUserGroupQName_Object = MibTableColumn
fsHQoSUserGroupQName = _FsHQoSUserGroupQName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3, 1, 2),
    _FsHQoSUserGroupQName_Type()
)
fsHQoSUserGroupQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQName.setStatus("current")
_FsHQoSUserGroupQDirection_Type = FSQDirectionType
_FsHQoSUserGroupQDirection_Object = MibTableColumn
fsHQoSUserGroupQDirection = _FsHQoSUserGroupQDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3, 1, 3),
    _FsHQoSUserGroupQDirection_Type()
)
fsHQoSUserGroupQDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQDirection.setStatus("current")
_FsHQoSUserGroupQRowStatus_Type = RowStatus
_FsHQoSUserGroupQRowStatus_Object = MibTableColumn
fsHQoSUserGroupQRowStatus = _FsHQoSUserGroupQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3, 1, 4),
    _FsHQoSUserGroupQRowStatus_Type()
)
fsHQoSUserGroupQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQRowStatus.setStatus("current")


class _FsHQoSUserGroupQShaping_Type(Unsigned32):
    """Custom type fsHQoSUserGroupQShaping based on Unsigned32"""
    defaultValue = 10000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSUserGroupQShaping_Type.__name__ = "Unsigned32"
_FsHQoSUserGroupQShaping_Object = MibTableColumn
fsHQoSUserGroupQShaping = _FsHQoSUserGroupQShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 3, 3, 1, 5),
    _FsHQoSUserGroupQShaping_Type()
)
fsHQoSUserGroupQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSUserGroupQShaping.setUnits("kilobits per second")
_FsHQoSFlowQObjects_ObjectIdentity = ObjectIdentity
fsHQoSFlowQObjects = _FsHQoSFlowQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4)
)
_FsHQoSFlowQIndexNext_Type = Integer32
_FsHQoSFlowQIndexNext_Object = MibScalar
fsHQoSFlowQIndexNext = _FsHQoSFlowQIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 1),
    _FsHQoSFlowQIndexNext_Type()
)
fsHQoSFlowQIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSFlowQIndexNext.setStatus("current")
_FsHQoSFlowQTable_Object = MibTable
fsHQoSFlowQTable = _FsHQoSFlowQTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2)
)
if mibBuilder.loadTexts:
    fsHQoSFlowQTable.setStatus("current")
_FsHQoSFlowQEntry_Object = MibTableRow
fsHQoSFlowQEntry = _FsHQoSFlowQEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1)
)
fsHQoSFlowQEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSFlowQIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSFlowQEntry.setStatus("current")
_FsHQoSFlowQIndex_Type = Unsigned32
_FsHQoSFlowQIndex_Object = MibTableColumn
fsHQoSFlowQIndex = _FsHQoSFlowQIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 1),
    _FsHQoSFlowQIndex_Type()
)
fsHQoSFlowQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSFlowQIndex.setStatus("current")


class _FsHQoSFlowQName_Type(OctetString):
    """Custom type fsHQoSFlowQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQName_Type.__name__ = "OctetString"
_FsHQoSFlowQName_Object = MibTableColumn
fsHQoSFlowQName = _FsHQoSFlowQName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 2),
    _FsHQoSFlowQName_Type()
)
fsHQoSFlowQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQName.setStatus("current")
_FsHQoSFlowQRowStatus_Type = RowStatus
_FsHQoSFlowQRowStatus_Object = MibTableColumn
fsHQoSFlowQRowStatus = _FsHQoSFlowQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 3),
    _FsHQoSFlowQRowStatus_Type()
)
fsHQoSFlowQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQRowStatus.setStatus("current")


class _FsHQoSFlowQBEQType_Type(FSQType):
    """Custom type fsHQoSFlowQBEQType based on FSQType"""
    defaultValue = 2


_FsHQoSFlowQBEQType_Type.__name__ = "FSQType"
_FsHQoSFlowQBEQType_Object = MibTableColumn
fsHQoSFlowQBEQType = _FsHQoSFlowQBEQType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 4),
    _FsHQoSFlowQBEQType_Type()
)
fsHQoSFlowQBEQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQBEQType.setStatus("current")


class _FsHQoSFlowQBEQWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQBEQWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQBEQWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQBEQWredWeight_Object = MibTableColumn
fsHQoSFlowQBEQWredWeight = _FsHQoSFlowQBEQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 5),
    _FsHQoSFlowQBEQWredWeight_Type()
)
fsHQoSFlowQBEQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQBEQWredWeight.setStatus("current")


class _FsHQoSFlowQBEQWredName_Type(OctetString):
    """Custom type fsHQoSFlowQBEQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQBEQWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQBEQWredName_Object = MibTableColumn
fsHQoSFlowQBEQWredName = _FsHQoSFlowQBEQWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 6),
    _FsHQoSFlowQBEQWredName_Type()
)
fsHQoSFlowQBEQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQBEQWredName.setStatus("current")


class _FsHQoSFlowQBEQDepth_Type(Integer32):
    """Custom type fsHQoSFlowQBEQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQBEQDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQBEQDepth_Object = MibTableColumn
fsHQoSFlowQBEQDepth = _FsHQoSFlowQBEQDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 7),
    _FsHQoSFlowQBEQDepth_Type()
)
fsHQoSFlowQBEQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQBEQDepth.setStatus("current")


class _FsHQoSFlowQBEQShaping_Type(Integer32):
    """Custom type fsHQoSFlowQBEQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQBEQShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQBEQShaping_Object = MibTableColumn
fsHQoSFlowQBEQShaping = _FsHQoSFlowQBEQShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 8),
    _FsHQoSFlowQBEQShaping_Type()
)
fsHQoSFlowQBEQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQBEQShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQBEQShaping.setUnits("kilobits per second")


class _FsHQoSFlowQAF1QType_Type(FSQType):
    """Custom type fsHQoSFlowQAF1QType based on FSQType"""
    defaultValue = 2


_FsHQoSFlowQAF1QType_Type.__name__ = "FSQType"
_FsHQoSFlowQAF1QType_Object = MibTableColumn
fsHQoSFlowQAF1QType = _FsHQoSFlowQAF1QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 9),
    _FsHQoSFlowQAF1QType_Type()
)
fsHQoSFlowQAF1QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF1QType.setStatus("current")


class _FsHQoSFlowQAF1QWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQAF1QWredWeight based on Integer32"""
    defaultValue = 10


_FsHQoSFlowQAF1QWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQAF1QWredWeight_Object = MibTableColumn
fsHQoSFlowQAF1QWredWeight = _FsHQoSFlowQAF1QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 10),
    _FsHQoSFlowQAF1QWredWeight_Type()
)
fsHQoSFlowQAF1QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF1QWredWeight.setStatus("current")


class _FsHQoSFlowQAF1QWredName_Type(OctetString):
    """Custom type fsHQoSFlowQAF1QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQAF1QWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQAF1QWredName_Object = MibTableColumn
fsHQoSFlowQAF1QWredName = _FsHQoSFlowQAF1QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 11),
    _FsHQoSFlowQAF1QWredName_Type()
)
fsHQoSFlowQAF1QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF1QWredName.setStatus("current")


class _FsHQoSFlowQAF1QDepth_Type(Integer32):
    """Custom type fsHQoSFlowQAF1QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQAF1QDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQAF1QDepth_Object = MibTableColumn
fsHQoSFlowQAF1QDepth = _FsHQoSFlowQAF1QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 12),
    _FsHQoSFlowQAF1QDepth_Type()
)
fsHQoSFlowQAF1QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF1QDepth.setStatus("current")


class _FsHQoSFlowQAF1QShaping_Type(Integer32):
    """Custom type fsHQoSFlowQAF1QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQAF1QShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQAF1QShaping_Object = MibTableColumn
fsHQoSFlowQAF1QShaping = _FsHQoSFlowQAF1QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 13),
    _FsHQoSFlowQAF1QShaping_Type()
)
fsHQoSFlowQAF1QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF1QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF1QShaping.setUnits("kilobits per second")


class _FsHQoSFlowQAF2QType_Type(FSQType):
    """Custom type fsHQoSFlowQAF2QType based on FSQType"""
    defaultValue = 2


_FsHQoSFlowQAF2QType_Type.__name__ = "FSQType"
_FsHQoSFlowQAF2QType_Object = MibTableColumn
fsHQoSFlowQAF2QType = _FsHQoSFlowQAF2QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 14),
    _FsHQoSFlowQAF2QType_Type()
)
fsHQoSFlowQAF2QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF2QType.setStatus("current")


class _FsHQoSFlowQAF2QWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQAF2QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQAF2QWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQAF2QWredWeight_Object = MibTableColumn
fsHQoSFlowQAF2QWredWeight = _FsHQoSFlowQAF2QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 15),
    _FsHQoSFlowQAF2QWredWeight_Type()
)
fsHQoSFlowQAF2QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF2QWredWeight.setStatus("current")


class _FsHQoSFlowQAF2QWredName_Type(OctetString):
    """Custom type fsHQoSFlowQAF2QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQAF2QWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQAF2QWredName_Object = MibTableColumn
fsHQoSFlowQAF2QWredName = _FsHQoSFlowQAF2QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 16),
    _FsHQoSFlowQAF2QWredName_Type()
)
fsHQoSFlowQAF2QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF2QWredName.setStatus("current")


class _FsHQoSFlowQAF2QDepth_Type(Integer32):
    """Custom type fsHQoSFlowQAF2QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQAF2QDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQAF2QDepth_Object = MibTableColumn
fsHQoSFlowQAF2QDepth = _FsHQoSFlowQAF2QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 17),
    _FsHQoSFlowQAF2QDepth_Type()
)
fsHQoSFlowQAF2QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF2QDepth.setStatus("current")


class _FsHQoSFlowQAF2QShaping_Type(Integer32):
    """Custom type fsHQoSFlowQAF2QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQAF2QShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQAF2QShaping_Object = MibTableColumn
fsHQoSFlowQAF2QShaping = _FsHQoSFlowQAF2QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 18),
    _FsHQoSFlowQAF2QShaping_Type()
)
fsHQoSFlowQAF2QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF2QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF2QShaping.setUnits("kilobits per second")


class _FsHQoSFlowQAF3QType_Type(FSQType):
    """Custom type fsHQoSFlowQAF3QType based on FSQType"""
    defaultValue = 2


_FsHQoSFlowQAF3QType_Type.__name__ = "FSQType"
_FsHQoSFlowQAF3QType_Object = MibTableColumn
fsHQoSFlowQAF3QType = _FsHQoSFlowQAF3QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 19),
    _FsHQoSFlowQAF3QType_Type()
)
fsHQoSFlowQAF3QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QType.setStatus("current")


class _FsHQoSFlowQAF3QWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQAF3QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQAF3QWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQAF3QWredWeight_Object = MibTableColumn
fsHQoSFlowQAF3QWredWeight = _FsHQoSFlowQAF3QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 20),
    _FsHQoSFlowQAF3QWredWeight_Type()
)
fsHQoSFlowQAF3QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QWredWeight.setStatus("current")


class _FsHQoSFlowQAF3QWredName_Type(OctetString):
    """Custom type fsHQoSFlowQAF3QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQAF3QWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQAF3QWredName_Object = MibTableColumn
fsHQoSFlowQAF3QWredName = _FsHQoSFlowQAF3QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 21),
    _FsHQoSFlowQAF3QWredName_Type()
)
fsHQoSFlowQAF3QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QWredName.setStatus("current")


class _FsHQoSFlowQAF3QDepth_Type(Integer32):
    """Custom type fsHQoSFlowQAF3QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQAF3QDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQAF3QDepth_Object = MibTableColumn
fsHQoSFlowQAF3QDepth = _FsHQoSFlowQAF3QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 22),
    _FsHQoSFlowQAF3QDepth_Type()
)
fsHQoSFlowQAF3QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QDepth.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QDepth.setUnits("kilobits per second")


class _FsHQoSFlowQAF3QShaping_Type(Integer32):
    """Custom type fsHQoSFlowQAF3QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQAF3QShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQAF3QShaping_Object = MibTableColumn
fsHQoSFlowQAF3QShaping = _FsHQoSFlowQAF3QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 23),
    _FsHQoSFlowQAF3QShaping_Type()
)
fsHQoSFlowQAF3QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF3QShaping.setUnits("kilobits per second")


class _FsHQoSFlowQAF4QType_Type(FSQType):
    """Custom type fsHQoSFlowQAF4QType based on FSQType"""
    defaultValue = 2


_FsHQoSFlowQAF4QType_Type.__name__ = "FSQType"
_FsHQoSFlowQAF4QType_Object = MibTableColumn
fsHQoSFlowQAF4QType = _FsHQoSFlowQAF4QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 24),
    _FsHQoSFlowQAF4QType_Type()
)
fsHQoSFlowQAF4QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF4QType.setStatus("current")


class _FsHQoSFlowQAF4QWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQAF4QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQAF4QWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQAF4QWredWeight_Object = MibTableColumn
fsHQoSFlowQAF4QWredWeight = _FsHQoSFlowQAF4QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 25),
    _FsHQoSFlowQAF4QWredWeight_Type()
)
fsHQoSFlowQAF4QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF4QWredWeight.setStatus("current")


class _FsHQoSFlowQAF4QWredName_Type(OctetString):
    """Custom type fsHQoSFlowQAF4QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQAF4QWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQAF4QWredName_Object = MibTableColumn
fsHQoSFlowQAF4QWredName = _FsHQoSFlowQAF4QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 26),
    _FsHQoSFlowQAF4QWredName_Type()
)
fsHQoSFlowQAF4QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF4QWredName.setStatus("current")


class _FsHQoSFlowQAF4QDepth_Type(Integer32):
    """Custom type fsHQoSFlowQAF4QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQAF4QDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQAF4QDepth_Object = MibTableColumn
fsHQoSFlowQAF4QDepth = _FsHQoSFlowQAF4QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 27),
    _FsHQoSFlowQAF4QDepth_Type()
)
fsHQoSFlowQAF4QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF4QDepth.setStatus("current")


class _FsHQoSFlowQAF4QShaping_Type(Integer32):
    """Custom type fsHQoSFlowQAF4QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_FsHQoSFlowQAF4QShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQAF4QShaping_Object = MibTableColumn
fsHQoSFlowQAF4QShaping = _FsHQoSFlowQAF4QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 28),
    _FsHQoSFlowQAF4QShaping_Type()
)
fsHQoSFlowQAF4QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF4QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQAF4QShaping.setUnits("kilobits per second")


class _FsHQoSFlowQEFQType_Type(FSQType):
    """Custom type fsHQoSFlowQEFQType based on FSQType"""
    defaultValue = 3


_FsHQoSFlowQEFQType_Type.__name__ = "FSQType"
_FsHQoSFlowQEFQType_Object = MibTableColumn
fsHQoSFlowQEFQType = _FsHQoSFlowQEFQType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 29),
    _FsHQoSFlowQEFQType_Type()
)
fsHQoSFlowQEFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQEFQType.setStatus("current")


class _FsHQoSFlowQEFQWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQEFQWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQEFQWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQEFQWredWeight_Object = MibTableColumn
fsHQoSFlowQEFQWredWeight = _FsHQoSFlowQEFQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 30),
    _FsHQoSFlowQEFQWredWeight_Type()
)
fsHQoSFlowQEFQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQEFQWredWeight.setStatus("current")


class _FsHQoSFlowQEFQWredName_Type(OctetString):
    """Custom type fsHQoSFlowQEFQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQEFQWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQEFQWredName_Object = MibTableColumn
fsHQoSFlowQEFQWredName = _FsHQoSFlowQEFQWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 31),
    _FsHQoSFlowQEFQWredName_Type()
)
fsHQoSFlowQEFQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQEFQWredName.setStatus("current")


class _FsHQoSFlowQEFQDepth_Type(Integer32):
    """Custom type fsHQoSFlowQEFQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQEFQDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQEFQDepth_Object = MibTableColumn
fsHQoSFlowQEFQDepth = _FsHQoSFlowQEFQDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 32),
    _FsHQoSFlowQEFQDepth_Type()
)
fsHQoSFlowQEFQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQEFQDepth.setStatus("current")


class _FsHQoSFlowQEFQShaping_Type(Integer32):
    """Custom type fsHQoSFlowQEFQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQEFQShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQEFQShaping_Object = MibTableColumn
fsHQoSFlowQEFQShaping = _FsHQoSFlowQEFQShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 33),
    _FsHQoSFlowQEFQShaping_Type()
)
fsHQoSFlowQEFQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQEFQShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQEFQShaping.setUnits("kilobits per second")


class _FsHQoSFlowQCS6QType_Type(FSQType):
    """Custom type fsHQoSFlowQCS6QType based on FSQType"""
    defaultValue = 3


_FsHQoSFlowQCS6QType_Type.__name__ = "FSQType"
_FsHQoSFlowQCS6QType_Object = MibTableColumn
fsHQoSFlowQCS6QType = _FsHQoSFlowQCS6QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 34),
    _FsHQoSFlowQCS6QType_Type()
)
fsHQoSFlowQCS6QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS6QType.setStatus("current")


class _FsHQoSFlowQCS6QWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQCS6QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQCS6QWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQCS6QWredWeight_Object = MibTableColumn
fsHQoSFlowQCS6QWredWeight = _FsHQoSFlowQCS6QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 35),
    _FsHQoSFlowQCS6QWredWeight_Type()
)
fsHQoSFlowQCS6QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS6QWredWeight.setStatus("current")


class _FsHQoSFlowQCS6QWredName_Type(OctetString):
    """Custom type fsHQoSFlowQCS6QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQCS6QWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQCS6QWredName_Object = MibTableColumn
fsHQoSFlowQCS6QWredName = _FsHQoSFlowQCS6QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 36),
    _FsHQoSFlowQCS6QWredName_Type()
)
fsHQoSFlowQCS6QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS6QWredName.setStatus("current")


class _FsHQoSFlowQCS6QDepth_Type(Integer32):
    """Custom type fsHQoSFlowQCS6QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQCS6QDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQCS6QDepth_Object = MibTableColumn
fsHQoSFlowQCS6QDepth = _FsHQoSFlowQCS6QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 37),
    _FsHQoSFlowQCS6QDepth_Type()
)
fsHQoSFlowQCS6QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS6QDepth.setStatus("current")


class _FsHQoSFlowQCS6QShaping_Type(Integer32):
    """Custom type fsHQoSFlowQCS6QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQCS6QShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQCS6QShaping_Object = MibTableColumn
fsHQoSFlowQCS6QShaping = _FsHQoSFlowQCS6QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 38),
    _FsHQoSFlowQCS6QShaping_Type()
)
fsHQoSFlowQCS6QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS6QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS6QShaping.setUnits("kilobits per second")


class _FsHQoSFlowQCS7QType_Type(FSQType):
    """Custom type fsHQoSFlowQCS7QType based on FSQType"""
    defaultValue = 3


_FsHQoSFlowQCS7QType_Type.__name__ = "FSQType"
_FsHQoSFlowQCS7QType_Object = MibTableColumn
fsHQoSFlowQCS7QType = _FsHQoSFlowQCS7QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 39),
    _FsHQoSFlowQCS7QType_Type()
)
fsHQoSFlowQCS7QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS7QType.setStatus("current")


class _FsHQoSFlowQCS7QWredWeight_Type(Integer32):
    """Custom type fsHQoSFlowQCS7QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSFlowQCS7QWredWeight_Type.__name__ = "Integer32"
_FsHQoSFlowQCS7QWredWeight_Object = MibTableColumn
fsHQoSFlowQCS7QWredWeight = _FsHQoSFlowQCS7QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 40),
    _FsHQoSFlowQCS7QWredWeight_Type()
)
fsHQoSFlowQCS7QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS7QWredWeight.setStatus("current")


class _FsHQoSFlowQCS7QWredName_Type(OctetString):
    """Custom type fsHQoSFlowQCS7QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowQCS7QWredName_Type.__name__ = "OctetString"
_FsHQoSFlowQCS7QWredName_Object = MibTableColumn
fsHQoSFlowQCS7QWredName = _FsHQoSFlowQCS7QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 41),
    _FsHQoSFlowQCS7QWredName_Type()
)
fsHQoSFlowQCS7QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS7QWredName.setStatus("current")


class _FsHQoSFlowQCS7QDepth_Type(Integer32):
    """Custom type fsHQoSFlowQCS7QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSFlowQCS7QDepth_Type.__name__ = "Integer32"
_FsHQoSFlowQCS7QDepth_Object = MibTableColumn
fsHQoSFlowQCS7QDepth = _FsHQoSFlowQCS7QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 42),
    _FsHQoSFlowQCS7QDepth_Type()
)
fsHQoSFlowQCS7QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS7QDepth.setStatus("current")


class _FsHQoSFlowQCS7QShaping_Type(Integer32):
    """Custom type fsHQoSFlowQCS7QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSFlowQCS7QShaping_Type.__name__ = "Integer32"
_FsHQoSFlowQCS7QShaping_Object = MibTableColumn
fsHQoSFlowQCS7QShaping = _FsHQoSFlowQCS7QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 4, 2, 1, 43),
    _FsHQoSFlowQCS7QShaping_Type()
)
fsHQoSFlowQCS7QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS7QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSFlowQCS7QShaping.setUnits("kilobits per second")
_FsHQoSFlowMapObjects_ObjectIdentity = ObjectIdentity
fsHQoSFlowMapObjects = _FsHQoSFlowMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5)
)
_FsHQoSFlowMapIndexNext_Type = Integer32
_FsHQoSFlowMapIndexNext_Object = MibScalar
fsHQoSFlowMapIndexNext = _FsHQoSFlowMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 1),
    _FsHQoSFlowMapIndexNext_Type()
)
fsHQoSFlowMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSFlowMapIndexNext.setStatus("current")
_FsHQoSFlowMapTable_Object = MibTable
fsHQoSFlowMapTable = _FsHQoSFlowMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2)
)
if mibBuilder.loadTexts:
    fsHQoSFlowMapTable.setStatus("current")
_FsHQoSFlowMapEntry_Object = MibTableRow
fsHQoSFlowMapEntry = _FsHQoSFlowMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1)
)
fsHQoSFlowMapEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSFlowMapIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSFlowMapEntry.setStatus("current")
_FsHQoSFlowMapIndex_Type = Unsigned32
_FsHQoSFlowMapIndex_Object = MibTableColumn
fsHQoSFlowMapIndex = _FsHQoSFlowMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 1),
    _FsHQoSFlowMapIndex_Type()
)
fsHQoSFlowMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSFlowMapIndex.setStatus("current")


class _FsHQoSFlowMapName_Type(OctetString):
    """Custom type fsHQoSFlowMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSFlowMapName_Type.__name__ = "OctetString"
_FsHQoSFlowMapName_Object = MibTableColumn
fsHQoSFlowMapName = _FsHQoSFlowMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 2),
    _FsHQoSFlowMapName_Type()
)
fsHQoSFlowMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapName.setStatus("current")
_FsHQoSFlowMapRowStatus_Type = RowStatus
_FsHQoSFlowMapRowStatus_Object = MibTableColumn
fsHQoSFlowMapRowStatus = _FsHQoSFlowMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 3),
    _FsHQoSFlowMapRowStatus_Type()
)
fsHQoSFlowMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapRowStatus.setStatus("current")


class _FsHQoSFlowMapBEQ2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapBEQ2PortQ based on FSCosType"""
    defaultValue = 1


_FsHQoSFlowMapBEQ2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapBEQ2PortQ_Object = MibTableColumn
fsHQoSFlowMapBEQ2PortQ = _FsHQoSFlowMapBEQ2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 4),
    _FsHQoSFlowMapBEQ2PortQ_Type()
)
fsHQoSFlowMapBEQ2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapBEQ2PortQ.setStatus("current")


class _FsHQoSFlowMapAF1Q2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapAF1Q2PortQ based on FSCosType"""
    defaultValue = 2


_FsHQoSFlowMapAF1Q2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapAF1Q2PortQ_Object = MibTableColumn
fsHQoSFlowMapAF1Q2PortQ = _FsHQoSFlowMapAF1Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 5),
    _FsHQoSFlowMapAF1Q2PortQ_Type()
)
fsHQoSFlowMapAF1Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapAF1Q2PortQ.setStatus("current")


class _FsHQoSFlowMapAF2Q2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapAF2Q2PortQ based on FSCosType"""
    defaultValue = 3


_FsHQoSFlowMapAF2Q2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapAF2Q2PortQ_Object = MibTableColumn
fsHQoSFlowMapAF2Q2PortQ = _FsHQoSFlowMapAF2Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 6),
    _FsHQoSFlowMapAF2Q2PortQ_Type()
)
fsHQoSFlowMapAF2Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapAF2Q2PortQ.setStatus("current")


class _FsHQoSFlowMapAF3Q2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapAF3Q2PortQ based on FSCosType"""
    defaultValue = 4


_FsHQoSFlowMapAF3Q2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapAF3Q2PortQ_Object = MibTableColumn
fsHQoSFlowMapAF3Q2PortQ = _FsHQoSFlowMapAF3Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 7),
    _FsHQoSFlowMapAF3Q2PortQ_Type()
)
fsHQoSFlowMapAF3Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapAF3Q2PortQ.setStatus("current")


class _FsHQoSFlowMapAF4Q2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapAF4Q2PortQ based on FSCosType"""
    defaultValue = 5


_FsHQoSFlowMapAF4Q2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapAF4Q2PortQ_Object = MibTableColumn
fsHQoSFlowMapAF4Q2PortQ = _FsHQoSFlowMapAF4Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 8),
    _FsHQoSFlowMapAF4Q2PortQ_Type()
)
fsHQoSFlowMapAF4Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapAF4Q2PortQ.setStatus("current")


class _FsHQoSFlowMapEFQ2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapEFQ2PortQ based on FSCosType"""
    defaultValue = 6


_FsHQoSFlowMapEFQ2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapEFQ2PortQ_Object = MibTableColumn
fsHQoSFlowMapEFQ2PortQ = _FsHQoSFlowMapEFQ2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 9),
    _FsHQoSFlowMapEFQ2PortQ_Type()
)
fsHQoSFlowMapEFQ2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapEFQ2PortQ.setStatus("current")


class _FsHQoSFlowMapCS6Q2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapCS6Q2PortQ based on FSCosType"""
    defaultValue = 7


_FsHQoSFlowMapCS6Q2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapCS6Q2PortQ_Object = MibTableColumn
fsHQoSFlowMapCS6Q2PortQ = _FsHQoSFlowMapCS6Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 10),
    _FsHQoSFlowMapCS6Q2PortQ_Type()
)
fsHQoSFlowMapCS6Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapCS6Q2PortQ.setStatus("current")


class _FsHQoSFlowMapCS7Q2PortQ_Type(FSCosType):
    """Custom type fsHQoSFlowMapCS7Q2PortQ based on FSCosType"""
    defaultValue = 8


_FsHQoSFlowMapCS7Q2PortQ_Type.__name__ = "FSCosType"
_FsHQoSFlowMapCS7Q2PortQ_Object = MibTableColumn
fsHQoSFlowMapCS7Q2PortQ = _FsHQoSFlowMapCS7Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 5, 2, 1, 11),
    _FsHQoSFlowMapCS7Q2PortQ_Type()
)
fsHQoSFlowMapCS7Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSFlowMapCS7Q2PortQ.setStatus("current")
_FsHQoSTClassifierObjects_ObjectIdentity = ObjectIdentity
fsHQoSTClassifierObjects = _FsHQoSTClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6)
)
_FsHQoSTClassifierIndexNext_Type = Integer32
_FsHQoSTClassifierIndexNext_Object = MibScalar
fsHQoSTClassifierIndexNext = _FsHQoSTClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 1),
    _FsHQoSTClassifierIndexNext_Type()
)
fsHQoSTClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSTClassifierIndexNext.setStatus("current")
_FsHQoSTClassifierTable_Object = MibTable
fsHQoSTClassifierTable = _FsHQoSTClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2)
)
if mibBuilder.loadTexts:
    fsHQoSTClassifierTable.setStatus("current")
_FsHQoSTClassifierEntry_Object = MibTableRow
fsHQoSTClassifierEntry = _FsHQoSTClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1)
)
fsHQoSTClassifierEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSTClassifierIndex"),
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSTClassifierInstance"),
)
if mibBuilder.loadTexts:
    fsHQoSTClassifierEntry.setStatus("current")
_FsHQoSTClassifierIndex_Type = Unsigned32
_FsHQoSTClassifierIndex_Object = MibTableColumn
fsHQoSTClassifierIndex = _FsHQoSTClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 1),
    _FsHQoSTClassifierIndex_Type()
)
fsHQoSTClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSTClassifierIndex.setStatus("current")
_FsHQoSTClassifierInstance_Type = Unsigned32
_FsHQoSTClassifierInstance_Object = MibTableColumn
fsHQoSTClassifierInstance = _FsHQoSTClassifierInstance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 2),
    _FsHQoSTClassifierInstance_Type()
)
fsHQoSTClassifierInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSTClassifierInstance.setStatus("current")


class _FsHQoSTClassifierName_Type(OctetString):
    """Custom type fsHQoSTClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTClassifierName_Type.__name__ = "OctetString"
_FsHQoSTClassifierName_Object = MibTableColumn
fsHQoSTClassifierName = _FsHQoSTClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 3),
    _FsHQoSTClassifierName_Type()
)
fsHQoSTClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierName.setStatus("current")


class _FsHQoSTClassifierType_Type(Integer32):
    """Custom type fsHQoSTClassifierType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tc-or", 1),
          ("tc-and", 2))
    )


_FsHQoSTClassifierType_Type.__name__ = "Integer32"
_FsHQoSTClassifierType_Object = MibTableColumn
fsHQoSTClassifierType = _FsHQoSTClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 4),
    _FsHQoSTClassifierType_Type()
)
fsHQoSTClassifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierType.setStatus("current")
_FsHQoSTClassifierRowStatus_Type = RowStatus
_FsHQoSTClassifierRowStatus_Object = MibTableColumn
fsHQoSTClassifierRowStatus = _FsHQoSTClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 5),
    _FsHQoSTClassifierRowStatus_Type()
)
fsHQoSTClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierRowStatus.setStatus("current")


class _FsHQoSTClassifierMatchMask_Type(Bits):
    """Custom type fsHQoSTClassifierMatchMask based on Bits"""
    namedValues = NamedValues(
        *(("tc-v4-any", 0),
          ("tc-v4-aclID", 1),
          ("tc-v4-aclName", 2),
          ("tc-v4-dscp", 3),
          ("tc-v4-tos", 4),
          ("tc-v6-any", 5),
          ("tc-v6-aclID", 6),
          ("tc-v6-aclName", 7),
          ("tc-v6-dscp", 8),
          ("tc-vlan-cos", 9),
          ("tc-exp", 10),
          ("tc-srcmac", 11),
          ("tc-dstmac", 12))
    )

_FsHQoSTClassifierMatchMask_Type.__name__ = "Bits"
_FsHQoSTClassifierMatchMask_Object = MibTableColumn
fsHQoSTClassifierMatchMask = _FsHQoSTClassifierMatchMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 6),
    _FsHQoSTClassifierMatchMask_Type()
)
fsHQoSTClassifierMatchMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchMask.setStatus("current")


class _FsHQoSTClassifierMatchV4Any_Type(TruthValue):
    """Custom type fsHQoSTClassifierMatchV4Any based on TruthValue"""
    defaultValue = 2


_FsHQoSTClassifierMatchV4Any_Type.__name__ = "TruthValue"
_FsHQoSTClassifierMatchV4Any_Object = MibTableColumn
fsHQoSTClassifierMatchV4Any = _FsHQoSTClassifierMatchV4Any_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 7),
    _FsHQoSTClassifierMatchV4Any_Type()
)
fsHQoSTClassifierMatchV4Any.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV4Any.setStatus("current")


class _FsHQoSTClassifierMatchV4AclID_Type(Integer32):
    """Custom type fsHQoSTClassifierMatchV4AclID based on Integer32"""
    defaultValue = 0


_FsHQoSTClassifierMatchV4AclID_Type.__name__ = "Integer32"
_FsHQoSTClassifierMatchV4AclID_Object = MibTableColumn
fsHQoSTClassifierMatchV4AclID = _FsHQoSTClassifierMatchV4AclID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 8),
    _FsHQoSTClassifierMatchV4AclID_Type()
)
fsHQoSTClassifierMatchV4AclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV4AclID.setStatus("current")


class _FsHQoSTClassifierV4AclName_Type(OctetString):
    """Custom type fsHQoSTClassifierV4AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTClassifierV4AclName_Type.__name__ = "OctetString"
_FsHQoSTClassifierV4AclName_Object = MibTableColumn
fsHQoSTClassifierV4AclName = _FsHQoSTClassifierV4AclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 9),
    _FsHQoSTClassifierV4AclName_Type()
)
fsHQoSTClassifierV4AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierV4AclName.setStatus("current")


class _FsHQoSTClassifierMatchV4Dscp_Type(Integer32):
    """Custom type fsHQoSTClassifierMatchV4Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsHQoSTClassifierMatchV4Dscp_Type.__name__ = "Integer32"
_FsHQoSTClassifierMatchV4Dscp_Object = MibTableColumn
fsHQoSTClassifierMatchV4Dscp = _FsHQoSTClassifierMatchV4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 10),
    _FsHQoSTClassifierMatchV4Dscp_Type()
)
fsHQoSTClassifierMatchV4Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV4Dscp.setStatus("current")


class _FsHQoSTClassifierMatchV4Tos_Type(Integer32):
    """Custom type fsHQoSTClassifierMatchV4Tos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsHQoSTClassifierMatchV4Tos_Type.__name__ = "Integer32"
_FsHQoSTClassifierMatchV4Tos_Object = MibTableColumn
fsHQoSTClassifierMatchV4Tos = _FsHQoSTClassifierMatchV4Tos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 11),
    _FsHQoSTClassifierMatchV4Tos_Type()
)
fsHQoSTClassifierMatchV4Tos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV4Tos.setStatus("current")


class _FsHQoSTClassifierMatchV6Any_Type(TruthValue):
    """Custom type fsHQoSTClassifierMatchV6Any based on TruthValue"""
    defaultValue = 2


_FsHQoSTClassifierMatchV6Any_Type.__name__ = "TruthValue"
_FsHQoSTClassifierMatchV6Any_Object = MibTableColumn
fsHQoSTClassifierMatchV6Any = _FsHQoSTClassifierMatchV6Any_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 12),
    _FsHQoSTClassifierMatchV6Any_Type()
)
fsHQoSTClassifierMatchV6Any.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV6Any.setStatus("current")
_FsHQoSTClassifierMatchV6AclID_Type = Integer32
_FsHQoSTClassifierMatchV6AclID_Object = MibTableColumn
fsHQoSTClassifierMatchV6AclID = _FsHQoSTClassifierMatchV6AclID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 13),
    _FsHQoSTClassifierMatchV6AclID_Type()
)
fsHQoSTClassifierMatchV6AclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV6AclID.setStatus("current")


class _FsHQoSTClassifierV6AclName_Type(OctetString):
    """Custom type fsHQoSTClassifierV6AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTClassifierV6AclName_Type.__name__ = "OctetString"
_FsHQoSTClassifierV6AclName_Object = MibTableColumn
fsHQoSTClassifierV6AclName = _FsHQoSTClassifierV6AclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 14),
    _FsHQoSTClassifierV6AclName_Type()
)
fsHQoSTClassifierV6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierV6AclName.setStatus("current")


class _FsHQoSTClassifierMatchV6Dscp_Type(Integer32):
    """Custom type fsHQoSTClassifierMatchV6Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsHQoSTClassifierMatchV6Dscp_Type.__name__ = "Integer32"
_FsHQoSTClassifierMatchV6Dscp_Object = MibTableColumn
fsHQoSTClassifierMatchV6Dscp = _FsHQoSTClassifierMatchV6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 15),
    _FsHQoSTClassifierMatchV6Dscp_Type()
)
fsHQoSTClassifierMatchV6Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchV6Dscp.setStatus("current")


class _FsHQoSTClassifierMatchCos_Type(Integer32):
    """Custom type fsHQoSTClassifierMatchCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsHQoSTClassifierMatchCos_Type.__name__ = "Integer32"
_FsHQoSTClassifierMatchCos_Object = MibTableColumn
fsHQoSTClassifierMatchCos = _FsHQoSTClassifierMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 16),
    _FsHQoSTClassifierMatchCos_Type()
)
fsHQoSTClassifierMatchCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchCos.setStatus("current")


class _FsHQoSTClassifierMatchExp_Type(Integer32):
    """Custom type fsHQoSTClassifierMatchExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsHQoSTClassifierMatchExp_Type.__name__ = "Integer32"
_FsHQoSTClassifierMatchExp_Object = MibTableColumn
fsHQoSTClassifierMatchExp = _FsHQoSTClassifierMatchExp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 17),
    _FsHQoSTClassifierMatchExp_Type()
)
fsHQoSTClassifierMatchExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchExp.setStatus("current")
_FsHQoSTClassifierMatchSrcMac_Type = MacAddress
_FsHQoSTClassifierMatchSrcMac_Object = MibTableColumn
fsHQoSTClassifierMatchSrcMac = _FsHQoSTClassifierMatchSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 18),
    _FsHQoSTClassifierMatchSrcMac_Type()
)
fsHQoSTClassifierMatchSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchSrcMac.setStatus("current")
_FsHQoSTClassifierMatchDstMac_Type = MacAddress
_FsHQoSTClassifierMatchDstMac_Object = MibTableColumn
fsHQoSTClassifierMatchDstMac = _FsHQoSTClassifierMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 6, 2, 1, 19),
    _FsHQoSTClassifierMatchDstMac_Type()
)
fsHQoSTClassifierMatchDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTClassifierMatchDstMac.setStatus("current")
_FsHQoSTBehaviorObjects_ObjectIdentity = ObjectIdentity
fsHQoSTBehaviorObjects = _FsHQoSTBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7)
)
_FsHQoSTBehaviorIndexNext_Type = Integer32
_FsHQoSTBehaviorIndexNext_Object = MibScalar
fsHQoSTBehaviorIndexNext = _FsHQoSTBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 1),
    _FsHQoSTBehaviorIndexNext_Type()
)
fsHQoSTBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorIndexNext.setStatus("current")
_FsHQoSTBehaviorTable_Object = MibTable
fsHQoSTBehaviorTable = _FsHQoSTBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2)
)
if mibBuilder.loadTexts:
    fsHQoSTBehaviorTable.setStatus("current")
_FsHQoSTBehaviorEntry_Object = MibTableRow
fsHQoSTBehaviorEntry = _FsHQoSTBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1)
)
fsHQoSTBehaviorEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSTBehaviorIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSTBehaviorEntry.setStatus("current")
_FsHQoSTBehaviorIndex_Type = Unsigned32
_FsHQoSTBehaviorIndex_Object = MibTableColumn
fsHQoSTBehaviorIndex = _FsHQoSTBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 1),
    _FsHQoSTBehaviorIndex_Type()
)
fsHQoSTBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorIndex.setStatus("current")


class _FsHQoSTBehaviorName_Type(OctetString):
    """Custom type fsHQoSTBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTBehaviorName_Type.__name__ = "OctetString"
_FsHQoSTBehaviorName_Object = MibTableColumn
fsHQoSTBehaviorName = _FsHQoSTBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 2),
    _FsHQoSTBehaviorName_Type()
)
fsHQoSTBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorName.setStatus("current")
_FsHQoSTBehaviorRowStatus_Type = RowStatus
_FsHQoSTBehaviorRowStatus_Object = MibTableColumn
fsHQoSTBehaviorRowStatus = _FsHQoSTBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 3),
    _FsHQoSTBehaviorRowStatus_Type()
)
fsHQoSTBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorRowStatus.setStatus("current")


class _FsHQoSTBehaviorMask_Type(Bits):
    """Custom type fsHQoSTBehaviorMask based on Bits"""
    namedValues = NamedValues(
        *(("user-queue", 0),
          ("set-cos", 1),
          ("set-color", 2),
          ("remark-v4-dscp", 3),
          ("remark-v4-tos", 4),
          ("remark-v6-dscp", 5),
          ("remark-vlan-cos", 6),
          ("remark-exp", 7),
          ("sub-policy", 8))
    )

_FsHQoSTBehaviorMask_Type.__name__ = "Bits"
_FsHQoSTBehaviorMask_Object = MibTableColumn
fsHQoSTBehaviorMask = _FsHQoSTBehaviorMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 4),
    _FsHQoSTBehaviorMask_Type()
)
fsHQoSTBehaviorMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorMask.setStatus("current")


class _FsHQoSTBehaviorUserQName_Type(OctetString):
    """Custom type fsHQoSTBehaviorUserQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTBehaviorUserQName_Type.__name__ = "OctetString"
_FsHQoSTBehaviorUserQName_Object = MibTableColumn
fsHQoSTBehaviorUserQName = _FsHQoSTBehaviorUserQName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 5),
    _FsHQoSTBehaviorUserQName_Type()
)
fsHQoSTBehaviorUserQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorUserQName.setStatus("current")
_FsHQoSTBehaviorUserQDir_Type = FSQDirectionType
_FsHQoSTBehaviorUserQDir_Object = MibTableColumn
fsHQoSTBehaviorUserQDir = _FsHQoSTBehaviorUserQDir_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 6),
    _FsHQoSTBehaviorUserQDir_Type()
)
fsHQoSTBehaviorUserQDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorUserQDir.setStatus("current")


class _FsHQoSTBehaviorTCos_Type(FSCosType):
    """Custom type fsHQoSTBehaviorTCos based on FSCosType"""
    defaultValue = 1


_FsHQoSTBehaviorTCos_Type.__name__ = "FSCosType"
_FsHQoSTBehaviorTCos_Object = MibTableColumn
fsHQoSTBehaviorTCos = _FsHQoSTBehaviorTCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 7),
    _FsHQoSTBehaviorTCos_Type()
)
fsHQoSTBehaviorTCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorTCos.setStatus("current")


class _FsHQoSTBehaviorTColor_Type(Integer32):
    """Custom type fsHQoSTBehaviorTColor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_FsHQoSTBehaviorTColor_Type.__name__ = "Integer32"
_FsHQoSTBehaviorTColor_Object = MibTableColumn
fsHQoSTBehaviorTColor = _FsHQoSTBehaviorTColor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 8),
    _FsHQoSTBehaviorTColor_Type()
)
fsHQoSTBehaviorTColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorTColor.setStatus("current")


class _FsHQoSTBehaviorRV4Dscp_Type(Integer32):
    """Custom type fsHQoSTBehaviorRV4Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsHQoSTBehaviorRV4Dscp_Type.__name__ = "Integer32"
_FsHQoSTBehaviorRV4Dscp_Object = MibTableColumn
fsHQoSTBehaviorRV4Dscp = _FsHQoSTBehaviorRV4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 9),
    _FsHQoSTBehaviorRV4Dscp_Type()
)
fsHQoSTBehaviorRV4Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorRV4Dscp.setStatus("current")


class _FsHQoSTBehaviorRV4Tos_Type(Integer32):
    """Custom type fsHQoSTBehaviorRV4Tos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsHQoSTBehaviorRV4Tos_Type.__name__ = "Integer32"
_FsHQoSTBehaviorRV4Tos_Object = MibTableColumn
fsHQoSTBehaviorRV4Tos = _FsHQoSTBehaviorRV4Tos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 10),
    _FsHQoSTBehaviorRV4Tos_Type()
)
fsHQoSTBehaviorRV4Tos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorRV4Tos.setStatus("current")


class _FsHQoSTBehaviorRV6Dscp_Type(Integer32):
    """Custom type fsHQoSTBehaviorRV6Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsHQoSTBehaviorRV6Dscp_Type.__name__ = "Integer32"
_FsHQoSTBehaviorRV6Dscp_Object = MibTableColumn
fsHQoSTBehaviorRV6Dscp = _FsHQoSTBehaviorRV6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 11),
    _FsHQoSTBehaviorRV6Dscp_Type()
)
fsHQoSTBehaviorRV6Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorRV6Dscp.setStatus("current")


class _FsHQoSTBehaviorRVlanCos_Type(Integer32):
    """Custom type fsHQoSTBehaviorRVlanCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsHQoSTBehaviorRVlanCos_Type.__name__ = "Integer32"
_FsHQoSTBehaviorRVlanCos_Object = MibTableColumn
fsHQoSTBehaviorRVlanCos = _FsHQoSTBehaviorRVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 12),
    _FsHQoSTBehaviorRVlanCos_Type()
)
fsHQoSTBehaviorRVlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorRVlanCos.setStatus("current")


class _FsHQoSTBehaviorRExp_Type(Integer32):
    """Custom type fsHQoSTBehaviorRExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsHQoSTBehaviorRExp_Type.__name__ = "Integer32"
_FsHQoSTBehaviorRExp_Object = MibTableColumn
fsHQoSTBehaviorRExp = _FsHQoSTBehaviorRExp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 13),
    _FsHQoSTBehaviorRExp_Type()
)
fsHQoSTBehaviorRExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorRExp.setStatus("current")


class _FsHQoSTBehaviorSubPolicyName_Type(OctetString):
    """Custom type fsHQoSTBehaviorSubPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTBehaviorSubPolicyName_Type.__name__ = "OctetString"
_FsHQoSTBehaviorSubPolicyName_Object = MibTableColumn
fsHQoSTBehaviorSubPolicyName = _FsHQoSTBehaviorSubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 7, 2, 1, 14),
    _FsHQoSTBehaviorSubPolicyName_Type()
)
fsHQoSTBehaviorSubPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTBehaviorSubPolicyName.setStatus("current")
_FsHQoSTPolicyObjects_ObjectIdentity = ObjectIdentity
fsHQoSTPolicyObjects = _FsHQoSTPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8)
)
_FsHQoSTPolicyIndexNext_Type = Integer32
_FsHQoSTPolicyIndexNext_Object = MibScalar
fsHQoSTPolicyIndexNext = _FsHQoSTPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 1),
    _FsHQoSTPolicyIndexNext_Type()
)
fsHQoSTPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSTPolicyIndexNext.setStatus("current")
_FsHQoSTPolicyTable_Object = MibTable
fsHQoSTPolicyTable = _FsHQoSTPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 2)
)
if mibBuilder.loadTexts:
    fsHQoSTPolicyTable.setStatus("current")
_FsHQoSTPolicyEntry_Object = MibTableRow
fsHQoSTPolicyEntry = _FsHQoSTPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 2, 1)
)
fsHQoSTPolicyEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSTPolicyIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSTPolicyEntry.setStatus("current")
_FsHQoSTPolicyIndex_Type = Unsigned32
_FsHQoSTPolicyIndex_Object = MibTableColumn
fsHQoSTPolicyIndex = _FsHQoSTPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 2, 1, 1),
    _FsHQoSTPolicyIndex_Type()
)
fsHQoSTPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSTPolicyIndex.setStatus("current")


class _FsHQoSTPolicyName_Type(OctetString):
    """Custom type fsHQoSTPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTPolicyName_Type.__name__ = "OctetString"
_FsHQoSTPolicyName_Object = MibTableColumn
fsHQoSTPolicyName = _FsHQoSTPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 2, 1, 2),
    _FsHQoSTPolicyName_Type()
)
fsHQoSTPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyName.setStatus("current")
_FsHQoSTPolicyRowStatus_Type = RowStatus
_FsHQoSTPolicyRowStatus_Object = MibTableColumn
fsHQoSTPolicyRowStatus = _FsHQoSTPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 2, 1, 3),
    _FsHQoSTPolicyRowStatus_Type()
)
fsHQoSTPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyRowStatus.setStatus("current")
_FsHQoSTPolicyMapIndexNext_Type = Integer32
_FsHQoSTPolicyMapIndexNext_Object = MibScalar
fsHQoSTPolicyMapIndexNext = _FsHQoSTPolicyMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 3),
    _FsHQoSTPolicyMapIndexNext_Type()
)
fsHQoSTPolicyMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapIndexNext.setStatus("current")
_FsHQoSTPolicyMapTable_Object = MibTable
fsHQoSTPolicyMapTable = _FsHQoSTPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4)
)
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapTable.setStatus("current")
_FsHQoSTPolicyMapEntry_Object = MibTableRow
fsHQoSTPolicyMapEntry = _FsHQoSTPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1)
)
fsHQoSTPolicyMapEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSTPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapEntry.setStatus("current")
_FsHQoSTPolicyMapIndex_Type = Unsigned32
_FsHQoSTPolicyMapIndex_Object = MibTableColumn
fsHQoSTPolicyMapIndex = _FsHQoSTPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 1),
    _FsHQoSTPolicyMapIndex_Type()
)
fsHQoSTPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapIndex.setStatus("current")


class _FsHQoSTPolicyMapPolicyName_Type(OctetString):
    """Custom type fsHQoSTPolicyMapPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTPolicyMapPolicyName_Type.__name__ = "OctetString"
_FsHQoSTPolicyMapPolicyName_Object = MibTableColumn
fsHQoSTPolicyMapPolicyName = _FsHQoSTPolicyMapPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 2),
    _FsHQoSTPolicyMapPolicyName_Type()
)
fsHQoSTPolicyMapPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapPolicyName.setStatus("current")
_FsHQoSTPolicyMapPolicyIndex_Type = Unsigned32
_FsHQoSTPolicyMapPolicyIndex_Object = MibTableColumn
fsHQoSTPolicyMapPolicyIndex = _FsHQoSTPolicyMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 3),
    _FsHQoSTPolicyMapPolicyIndex_Type()
)
fsHQoSTPolicyMapPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapPolicyIndex.setStatus("current")


class _FsHQoSTPolicyMapTClassfierName_Type(OctetString):
    """Custom type fsHQoSTPolicyMapTClassfierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTPolicyMapTClassfierName_Type.__name__ = "OctetString"
_FsHQoSTPolicyMapTClassfierName_Object = MibTableColumn
fsHQoSTPolicyMapTClassfierName = _FsHQoSTPolicyMapTClassfierName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 4),
    _FsHQoSTPolicyMapTClassfierName_Type()
)
fsHQoSTPolicyMapTClassfierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapTClassfierName.setStatus("current")
_FsHQoSTPolicyMapTClassfierIndex_Type = Unsigned32
_FsHQoSTPolicyMapTClassfierIndex_Object = MibTableColumn
fsHQoSTPolicyMapTClassfierIndex = _FsHQoSTPolicyMapTClassfierIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 5),
    _FsHQoSTPolicyMapTClassfierIndex_Type()
)
fsHQoSTPolicyMapTClassfierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapTClassfierIndex.setStatus("current")


class _FsHQoSTPolicyMapTBehaviorName_Type(OctetString):
    """Custom type fsHQoSTPolicyMapTBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSTPolicyMapTBehaviorName_Type.__name__ = "OctetString"
_FsHQoSTPolicyMapTBehaviorName_Object = MibTableColumn
fsHQoSTPolicyMapTBehaviorName = _FsHQoSTPolicyMapTBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 6),
    _FsHQoSTPolicyMapTBehaviorName_Type()
)
fsHQoSTPolicyMapTBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapTBehaviorName.setStatus("current")
_FsHQoSTPolicyMapTBehaviorIndex_Type = Unsigned32
_FsHQoSTPolicyMapTBehaviorIndex_Object = MibTableColumn
fsHQoSTPolicyMapTBehaviorIndex = _FsHQoSTPolicyMapTBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 7),
    _FsHQoSTPolicyMapTBehaviorIndex_Type()
)
fsHQoSTPolicyMapTBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapTBehaviorIndex.setStatus("current")


class _FsHQoSTPolicyMapPrecedence_Type(Unsigned32):
    """Custom type fsHQoSTPolicyMapPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FsHQoSTPolicyMapPrecedence_Type.__name__ = "Unsigned32"
_FsHQoSTPolicyMapPrecedence_Object = MibTableColumn
fsHQoSTPolicyMapPrecedence = _FsHQoSTPolicyMapPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 8),
    _FsHQoSTPolicyMapPrecedence_Type()
)
fsHQoSTPolicyMapPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapPrecedence.setStatus("current")
_FsHQoSTPolicyMapRowStatus_Type = RowStatus
_FsHQoSTPolicyMapRowStatus_Object = MibTableColumn
fsHQoSTPolicyMapRowStatus = _FsHQoSTPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 8, 4, 1, 9),
    _FsHQoSTPolicyMapRowStatus_Type()
)
fsHQoSTPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSTPolicyMapRowStatus.setStatus("current")
_FsHQoSVoQObjects_ObjectIdentity = ObjectIdentity
fsHQoSVoQObjects = _FsHQoSVoQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 9)
)


class _FsHQoSVoQEnable_Type(TruthValue):
    """Custom type fsHQoSVoQEnable based on TruthValue"""
    defaultValue = 2


_FsHQoSVoQEnable_Type.__name__ = "TruthValue"
_FsHQoSVoQEnable_Object = MibScalar
fsHQoSVoQEnable = _FsHQoSVoQEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 9, 1),
    _FsHQoSVoQEnable_Type()
)
fsHQoSVoQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSVoQEnable.setStatus("current")
_FsHQoSVoQDeviceTable_Object = MibTable
fsHQoSVoQDeviceTable = _FsHQoSVoQDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 9, 2)
)
if mibBuilder.loadTexts:
    fsHQoSVoQDeviceTable.setStatus("current")
_FsHQoSVoQDeviceEntry_Object = MibTableRow
fsHQoSVoQDeviceEntry = _FsHQoSVoQDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 9, 2, 1)
)
fsHQoSVoQDeviceEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSVoQDeviceId"),
)
if mibBuilder.loadTexts:
    fsHQoSVoQDeviceEntry.setStatus("current")
_FsHQoSVoQDeviceId_Type = Unsigned32
_FsHQoSVoQDeviceId_Object = MibTableColumn
fsHQoSVoQDeviceId = _FsHQoSVoQDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 9, 2, 1, 1),
    _FsHQoSVoQDeviceId_Type()
)
fsHQoSVoQDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSVoQDeviceId.setStatus("current")
_FsHQoSVoQDeviceCredit_Type = Unsigned32
_FsHQoSVoQDeviceCredit_Object = MibTableColumn
fsHQoSVoQDeviceCredit = _FsHQoSVoQDeviceCredit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 9, 2, 1, 2),
    _FsHQoSVoQDeviceCredit_Type()
)
fsHQoSVoQDeviceCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSVoQDeviceCredit.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSVoQDeviceCredit.setUnits("Mbit/s")
_FsHQoSPortQObjects_ObjectIdentity = ObjectIdentity
fsHQoSPortQObjects = _FsHQoSPortQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10)
)
_FsHQoSPortQIndexNext_Type = Integer32
_FsHQoSPortQIndexNext_Object = MibScalar
fsHQoSPortQIndexNext = _FsHQoSPortQIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 1),
    _FsHQoSPortQIndexNext_Type()
)
fsHQoSPortQIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSPortQIndexNext.setStatus("current")
_FsHQoSPortQTable_Object = MibTable
fsHQoSPortQTable = _FsHQoSPortQTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2)
)
if mibBuilder.loadTexts:
    fsHQoSPortQTable.setStatus("current")
_FsHQoSPortQEntry_Object = MibTableRow
fsHQoSPortQEntry = _FsHQoSPortQEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1)
)
fsHQoSPortQEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSPortQIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSPortQEntry.setStatus("current")
_FsHQoSPortQIndex_Type = Unsigned32
_FsHQoSPortQIndex_Object = MibTableColumn
fsHQoSPortQIndex = _FsHQoSPortQIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 1),
    _FsHQoSPortQIndex_Type()
)
fsHQoSPortQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSPortQIndex.setStatus("current")


class _FsHQoSPortQName_Type(OctetString):
    """Custom type fsHQoSPortQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQName_Type.__name__ = "OctetString"
_FsHQoSPortQName_Object = MibTableColumn
fsHQoSPortQName = _FsHQoSPortQName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 2),
    _FsHQoSPortQName_Type()
)
fsHQoSPortQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQName.setStatus("current")
_FsHQoSPortQRowStatus_Type = RowStatus
_FsHQoSPortQRowStatus_Object = MibTableColumn
fsHQoSPortQRowStatus = _FsHQoSPortQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 3),
    _FsHQoSPortQRowStatus_Type()
)
fsHQoSPortQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQRowStatus.setStatus("current")


class _FsHQoSPortQBEQType_Type(FSQType):
    """Custom type fsHQoSPortQBEQType based on FSQType"""
    defaultValue = 2


_FsHQoSPortQBEQType_Type.__name__ = "FSQType"
_FsHQoSPortQBEQType_Object = MibTableColumn
fsHQoSPortQBEQType = _FsHQoSPortQBEQType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 4),
    _FsHQoSPortQBEQType_Type()
)
fsHQoSPortQBEQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQBEQType.setStatus("current")


class _FsHQoSPortQBEQWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQBEQWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQBEQWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQBEQWredWeight_Object = MibTableColumn
fsHQoSPortQBEQWredWeight = _FsHQoSPortQBEQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 5),
    _FsHQoSPortQBEQWredWeight_Type()
)
fsHQoSPortQBEQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQBEQWredWeight.setStatus("current")


class _FsHQoSPortQBEQWredName_Type(OctetString):
    """Custom type fsHQoSPortQBEQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQBEQWredName_Type.__name__ = "OctetString"
_FsHQoSPortQBEQWredName_Object = MibTableColumn
fsHQoSPortQBEQWredName = _FsHQoSPortQBEQWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 6),
    _FsHQoSPortQBEQWredName_Type()
)
fsHQoSPortQBEQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQBEQWredName.setStatus("current")


class _FsHQoSPortQBEQDepth_Type(Integer32):
    """Custom type fsHQoSPortQBEQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQBEQDepth_Type.__name__ = "Integer32"
_FsHQoSPortQBEQDepth_Object = MibTableColumn
fsHQoSPortQBEQDepth = _FsHQoSPortQBEQDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 7),
    _FsHQoSPortQBEQDepth_Type()
)
fsHQoSPortQBEQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQBEQDepth.setStatus("current")


class _FsHQoSPortQBEQShaping_Type(Integer32):
    """Custom type fsHQoSPortQBEQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQBEQShaping_Type.__name__ = "Integer32"
_FsHQoSPortQBEQShaping_Object = MibTableColumn
fsHQoSPortQBEQShaping = _FsHQoSPortQBEQShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 8),
    _FsHQoSPortQBEQShaping_Type()
)
fsHQoSPortQBEQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQBEQShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQBEQShaping.setUnits("kilobits per second")


class _FsHQoSPortQAF1QType_Type(FSQType):
    """Custom type fsHQoSPortQAF1QType based on FSQType"""
    defaultValue = 2


_FsHQoSPortQAF1QType_Type.__name__ = "FSQType"
_FsHQoSPortQAF1QType_Object = MibTableColumn
fsHQoSPortQAF1QType = _FsHQoSPortQAF1QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 9),
    _FsHQoSPortQAF1QType_Type()
)
fsHQoSPortQAF1QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF1QType.setStatus("current")


class _FsHQoSPortQAF1QWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQAF1QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQAF1QWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQAF1QWredWeight_Object = MibTableColumn
fsHQoSPortQAF1QWredWeight = _FsHQoSPortQAF1QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 10),
    _FsHQoSPortQAF1QWredWeight_Type()
)
fsHQoSPortQAF1QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF1QWredWeight.setStatus("current")


class _FsHQoSPortQAF1QWredName_Type(OctetString):
    """Custom type fsHQoSPortQAF1QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQAF1QWredName_Type.__name__ = "OctetString"
_FsHQoSPortQAF1QWredName_Object = MibTableColumn
fsHQoSPortQAF1QWredName = _FsHQoSPortQAF1QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 11),
    _FsHQoSPortQAF1QWredName_Type()
)
fsHQoSPortQAF1QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF1QWredName.setStatus("current")


class _FsHQoSPortQAF1QDepth_Type(Integer32):
    """Custom type fsHQoSPortQAF1QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQAF1QDepth_Type.__name__ = "Integer32"
_FsHQoSPortQAF1QDepth_Object = MibTableColumn
fsHQoSPortQAF1QDepth = _FsHQoSPortQAF1QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 12),
    _FsHQoSPortQAF1QDepth_Type()
)
fsHQoSPortQAF1QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF1QDepth.setStatus("current")


class _FsHQoSPortQAF1QShaping_Type(Integer32):
    """Custom type fsHQoSPortQAF1QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQAF1QShaping_Type.__name__ = "Integer32"
_FsHQoSPortQAF1QShaping_Object = MibTableColumn
fsHQoSPortQAF1QShaping = _FsHQoSPortQAF1QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 13),
    _FsHQoSPortQAF1QShaping_Type()
)
fsHQoSPortQAF1QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF1QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQAF1QShaping.setUnits("kilobits per second")


class _FsHQoSPortQAF2QType_Type(FSQType):
    """Custom type fsHQoSPortQAF2QType based on FSQType"""
    defaultValue = 2


_FsHQoSPortQAF2QType_Type.__name__ = "FSQType"
_FsHQoSPortQAF2QType_Object = MibTableColumn
fsHQoSPortQAF2QType = _FsHQoSPortQAF2QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 14),
    _FsHQoSPortQAF2QType_Type()
)
fsHQoSPortQAF2QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF2QType.setStatus("current")


class _FsHQoSPortQAF2QWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQAF2QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_FsHQoSPortQAF2QWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQAF2QWredWeight_Object = MibTableColumn
fsHQoSPortQAF2QWredWeight = _FsHQoSPortQAF2QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 15),
    _FsHQoSPortQAF2QWredWeight_Type()
)
fsHQoSPortQAF2QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF2QWredWeight.setStatus("current")


class _FsHQoSPortQAF2QWredName_Type(OctetString):
    """Custom type fsHQoSPortQAF2QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQAF2QWredName_Type.__name__ = "OctetString"
_FsHQoSPortQAF2QWredName_Object = MibTableColumn
fsHQoSPortQAF2QWredName = _FsHQoSPortQAF2QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 16),
    _FsHQoSPortQAF2QWredName_Type()
)
fsHQoSPortQAF2QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF2QWredName.setStatus("current")


class _FsHQoSPortQAF2QDepth_Type(Integer32):
    """Custom type fsHQoSPortQAF2QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQAF2QDepth_Type.__name__ = "Integer32"
_FsHQoSPortQAF2QDepth_Object = MibTableColumn
fsHQoSPortQAF2QDepth = _FsHQoSPortQAF2QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 17),
    _FsHQoSPortQAF2QDepth_Type()
)
fsHQoSPortQAF2QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF2QDepth.setStatus("current")


class _FsHQoSPortQAF2QShaping_Type(Integer32):
    """Custom type fsHQoSPortQAF2QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQAF2QShaping_Type.__name__ = "Integer32"
_FsHQoSPortQAF2QShaping_Object = MibTableColumn
fsHQoSPortQAF2QShaping = _FsHQoSPortQAF2QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 18),
    _FsHQoSPortQAF2QShaping_Type()
)
fsHQoSPortQAF2QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF2QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQAF2QShaping.setUnits("kilobits per second")


class _FsHQoSPortQAF3QType_Type(FSQType):
    """Custom type fsHQoSPortQAF3QType based on FSQType"""
    defaultValue = 2


_FsHQoSPortQAF3QType_Type.__name__ = "FSQType"
_FsHQoSPortQAF3QType_Object = MibTableColumn
fsHQoSPortQAF3QType = _FsHQoSPortQAF3QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 19),
    _FsHQoSPortQAF3QType_Type()
)
fsHQoSPortQAF3QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF3QType.setStatus("current")


class _FsHQoSPortQAF3QWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQAF3QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQAF3QWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQAF3QWredWeight_Object = MibTableColumn
fsHQoSPortQAF3QWredWeight = _FsHQoSPortQAF3QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 20),
    _FsHQoSPortQAF3QWredWeight_Type()
)
fsHQoSPortQAF3QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF3QWredWeight.setStatus("current")


class _FsHQoSPortQAF3QWredName_Type(OctetString):
    """Custom type fsHQoSPortQAF3QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQAF3QWredName_Type.__name__ = "OctetString"
_FsHQoSPortQAF3QWredName_Object = MibTableColumn
fsHQoSPortQAF3QWredName = _FsHQoSPortQAF3QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 21),
    _FsHQoSPortQAF3QWredName_Type()
)
fsHQoSPortQAF3QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF3QWredName.setStatus("current")


class _FsHQoSPortQAF3QDepth_Type(Integer32):
    """Custom type fsHQoSPortQAF3QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQAF3QDepth_Type.__name__ = "Integer32"
_FsHQoSPortQAF3QDepth_Object = MibTableColumn
fsHQoSPortQAF3QDepth = _FsHQoSPortQAF3QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 22),
    _FsHQoSPortQAF3QDepth_Type()
)
fsHQoSPortQAF3QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF3QDepth.setStatus("current")


class _FsHQoSPortQAF3QShaping_Type(Integer32):
    """Custom type fsHQoSPortQAF3QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQAF3QShaping_Type.__name__ = "Integer32"
_FsHQoSPortQAF3QShaping_Object = MibTableColumn
fsHQoSPortQAF3QShaping = _FsHQoSPortQAF3QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 23),
    _FsHQoSPortQAF3QShaping_Type()
)
fsHQoSPortQAF3QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF3QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQAF3QShaping.setUnits("kilobits per second")


class _FsHQoSPortQAF4QType_Type(FSQType):
    """Custom type fsHQoSPortQAF4QType based on FSQType"""
    defaultValue = 2


_FsHQoSPortQAF4QType_Type.__name__ = "FSQType"
_FsHQoSPortQAF4QType_Object = MibTableColumn
fsHQoSPortQAF4QType = _FsHQoSPortQAF4QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 24),
    _FsHQoSPortQAF4QType_Type()
)
fsHQoSPortQAF4QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF4QType.setStatus("current")


class _FsHQoSPortQAF4QWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQAF4QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQAF4QWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQAF4QWredWeight_Object = MibTableColumn
fsHQoSPortQAF4QWredWeight = _FsHQoSPortQAF4QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 25),
    _FsHQoSPortQAF4QWredWeight_Type()
)
fsHQoSPortQAF4QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF4QWredWeight.setStatus("current")


class _FsHQoSPortQAF4QWredName_Type(OctetString):
    """Custom type fsHQoSPortQAF4QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQAF4QWredName_Type.__name__ = "OctetString"
_FsHQoSPortQAF4QWredName_Object = MibTableColumn
fsHQoSPortQAF4QWredName = _FsHQoSPortQAF4QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 26),
    _FsHQoSPortQAF4QWredName_Type()
)
fsHQoSPortQAF4QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF4QWredName.setStatus("current")


class _FsHQoSPortQAF4QDepth_Type(Integer32):
    """Custom type fsHQoSPortQAF4QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQAF4QDepth_Type.__name__ = "Integer32"
_FsHQoSPortQAF4QDepth_Object = MibTableColumn
fsHQoSPortQAF4QDepth = _FsHQoSPortQAF4QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 27),
    _FsHQoSPortQAF4QDepth_Type()
)
fsHQoSPortQAF4QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF4QDepth.setStatus("current")


class _FsHQoSPortQAF4QShaping_Type(Integer32):
    """Custom type fsHQoSPortQAF4QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQAF4QShaping_Type.__name__ = "Integer32"
_FsHQoSPortQAF4QShaping_Object = MibTableColumn
fsHQoSPortQAF4QShaping = _FsHQoSPortQAF4QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 28),
    _FsHQoSPortQAF4QShaping_Type()
)
fsHQoSPortQAF4QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQAF4QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQAF4QShaping.setUnits("kilobits per second")


class _FsHQoSPortQEFQType_Type(FSQType):
    """Custom type fsHQoSPortQEFQType based on FSQType"""
    defaultValue = 3


_FsHQoSPortQEFQType_Type.__name__ = "FSQType"
_FsHQoSPortQEFQType_Object = MibTableColumn
fsHQoSPortQEFQType = _FsHQoSPortQEFQType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 29),
    _FsHQoSPortQEFQType_Type()
)
fsHQoSPortQEFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQEFQType.setStatus("current")


class _FsHQoSPortQEFQWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQEFQWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQEFQWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQEFQWredWeight_Object = MibTableColumn
fsHQoSPortQEFQWredWeight = _FsHQoSPortQEFQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 30),
    _FsHQoSPortQEFQWredWeight_Type()
)
fsHQoSPortQEFQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQEFQWredWeight.setStatus("current")


class _FsHQoSPortQEFQWredName_Type(OctetString):
    """Custom type fsHQoSPortQEFQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQEFQWredName_Type.__name__ = "OctetString"
_FsHQoSPortQEFQWredName_Object = MibTableColumn
fsHQoSPortQEFQWredName = _FsHQoSPortQEFQWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 31),
    _FsHQoSPortQEFQWredName_Type()
)
fsHQoSPortQEFQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQEFQWredName.setStatus("current")


class _FsHQoSPortQEFQDepth_Type(Integer32):
    """Custom type fsHQoSPortQEFQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQEFQDepth_Type.__name__ = "Integer32"
_FsHQoSPortQEFQDepth_Object = MibTableColumn
fsHQoSPortQEFQDepth = _FsHQoSPortQEFQDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 32),
    _FsHQoSPortQEFQDepth_Type()
)
fsHQoSPortQEFQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQEFQDepth.setStatus("current")


class _FsHQoSPortQEFQShaping_Type(Integer32):
    """Custom type fsHQoSPortQEFQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQEFQShaping_Type.__name__ = "Integer32"
_FsHQoSPortQEFQShaping_Object = MibTableColumn
fsHQoSPortQEFQShaping = _FsHQoSPortQEFQShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 33),
    _FsHQoSPortQEFQShaping_Type()
)
fsHQoSPortQEFQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQEFQShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQEFQShaping.setUnits("kilobits per second")


class _FsHQoSPortQCS6QType_Type(FSQType):
    """Custom type fsHQoSPortQCS6QType based on FSQType"""
    defaultValue = 3


_FsHQoSPortQCS6QType_Type.__name__ = "FSQType"
_FsHQoSPortQCS6QType_Object = MibTableColumn
fsHQoSPortQCS6QType = _FsHQoSPortQCS6QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 34),
    _FsHQoSPortQCS6QType_Type()
)
fsHQoSPortQCS6QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS6QType.setStatus("current")


class _FsHQoSPortQCS6QWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQCS6QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQCS6QWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQCS6QWredWeight_Object = MibTableColumn
fsHQoSPortQCS6QWredWeight = _FsHQoSPortQCS6QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 35),
    _FsHQoSPortQCS6QWredWeight_Type()
)
fsHQoSPortQCS6QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS6QWredWeight.setStatus("current")


class _FsHQoSPortQCS6QWredName_Type(OctetString):
    """Custom type fsHQoSPortQCS6QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQCS6QWredName_Type.__name__ = "OctetString"
_FsHQoSPortQCS6QWredName_Object = MibTableColumn
fsHQoSPortQCS6QWredName = _FsHQoSPortQCS6QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 36),
    _FsHQoSPortQCS6QWredName_Type()
)
fsHQoSPortQCS6QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS6QWredName.setStatus("current")


class _FsHQoSPortQCS6QDepth_Type(Integer32):
    """Custom type fsHQoSPortQCS6QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQCS6QDepth_Type.__name__ = "Integer32"
_FsHQoSPortQCS6QDepth_Object = MibTableColumn
fsHQoSPortQCS6QDepth = _FsHQoSPortQCS6QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 37),
    _FsHQoSPortQCS6QDepth_Type()
)
fsHQoSPortQCS6QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS6QDepth.setStatus("current")


class _FsHQoSPortQCS6QShaping_Type(Integer32):
    """Custom type fsHQoSPortQCS6QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQCS6QShaping_Type.__name__ = "Integer32"
_FsHQoSPortQCS6QShaping_Object = MibTableColumn
fsHQoSPortQCS6QShaping = _FsHQoSPortQCS6QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 38),
    _FsHQoSPortQCS6QShaping_Type()
)
fsHQoSPortQCS6QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS6QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQCS6QShaping.setUnits("kilobits per second")


class _FsHQoSPortQCS7QType_Type(FSQType):
    """Custom type fsHQoSPortQCS7QType based on FSQType"""
    defaultValue = 3


_FsHQoSPortQCS7QType_Type.__name__ = "FSQType"
_FsHQoSPortQCS7QType_Object = MibTableColumn
fsHQoSPortQCS7QType = _FsHQoSPortQCS7QType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 39),
    _FsHQoSPortQCS7QType_Type()
)
fsHQoSPortQCS7QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS7QType.setStatus("current")


class _FsHQoSPortQCS7QWredWeight_Type(Integer32):
    """Custom type fsHQoSPortQCS7QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_FsHQoSPortQCS7QWredWeight_Type.__name__ = "Integer32"
_FsHQoSPortQCS7QWredWeight_Object = MibTableColumn
fsHQoSPortQCS7QWredWeight = _FsHQoSPortQCS7QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 40),
    _FsHQoSPortQCS7QWredWeight_Type()
)
fsHQoSPortQCS7QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS7QWredWeight.setStatus("current")


class _FsHQoSPortQCS7QWredName_Type(OctetString):
    """Custom type fsHQoSPortQCS7QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSPortQCS7QWredName_Type.__name__ = "OctetString"
_FsHQoSPortQCS7QWredName_Object = MibTableColumn
fsHQoSPortQCS7QWredName = _FsHQoSPortQCS7QWredName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 41),
    _FsHQoSPortQCS7QWredName_Type()
)
fsHQoSPortQCS7QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS7QWredName.setStatus("current")


class _FsHQoSPortQCS7QDepth_Type(Integer32):
    """Custom type fsHQoSPortQCS7QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsHQoSPortQCS7QDepth_Type.__name__ = "Integer32"
_FsHQoSPortQCS7QDepth_Object = MibTableColumn
fsHQoSPortQCS7QDepth = _FsHQoSPortQCS7QDepth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 42),
    _FsHQoSPortQCS7QDepth_Type()
)
fsHQoSPortQCS7QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS7QDepth.setStatus("current")


class _FsHQoSPortQCS7QShaping_Type(Integer32):
    """Custom type fsHQoSPortQCS7QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSPortQCS7QShaping_Type.__name__ = "Integer32"
_FsHQoSPortQCS7QShaping_Object = MibTableColumn
fsHQoSPortQCS7QShaping = _FsHQoSPortQCS7QShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 10, 2, 1, 43),
    _FsHQoSPortQCS7QShaping_Type()
)
fsHQoSPortQCS7QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHQoSPortQCS7QShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSPortQCS7QShaping.setUnits("kilobits per second")
_FsHQoSIfAppObjects_ObjectIdentity = ObjectIdentity
fsHQoSIfAppObjects = _FsHQoSIfAppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11)
)
_FsHQoSIfAppTable_Object = MibTable
fsHQoSIfAppTable = _FsHQoSIfAppTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1)
)
if mibBuilder.loadTexts:
    fsHQoSIfAppTable.setStatus("current")
_FsHQoSIfAppEntry_Object = MibTableRow
fsHQoSIfAppEntry = _FsHQoSIfAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1)
)
fsHQoSIfAppEntry.setIndexNames(
    (0, "FS-ROUTER-QOS-MIB", "fsHQoSIfAppIndex"),
)
if mibBuilder.loadTexts:
    fsHQoSIfAppEntry.setStatus("current")
_FsHQoSIfAppIndex_Type = InterfaceIndex
_FsHQoSIfAppIndex_Object = MibTableColumn
fsHQoSIfAppIndex = _FsHQoSIfAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 1),
    _FsHQoSIfAppIndex_Type()
)
fsHQoSIfAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHQoSIfAppIndex.setStatus("current")


class _FsHQoSIfAppInPolicyName_Type(OctetString):
    """Custom type fsHQoSIfAppInPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSIfAppInPolicyName_Type.__name__ = "OctetString"
_FsHQoSIfAppInPolicyName_Object = MibTableColumn
fsHQoSIfAppInPolicyName = _FsHQoSIfAppInPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 2),
    _FsHQoSIfAppInPolicyName_Type()
)
fsHQoSIfAppInPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSIfAppInPolicyName.setStatus("current")
_FsHQoSIfAppInPolicyIndex_Type = Unsigned32
_FsHQoSIfAppInPolicyIndex_Object = MibTableColumn
fsHQoSIfAppInPolicyIndex = _FsHQoSIfAppInPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 3),
    _FsHQoSIfAppInPolicyIndex_Type()
)
fsHQoSIfAppInPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSIfAppInPolicyIndex.setStatus("current")


class _FsHQoSIfAppInPolicyLayer_Type(FSLayerType):
    """Custom type fsHQoSIfAppInPolicyLayer based on FSLayerType"""
    defaultValue = 0


_FsHQoSIfAppInPolicyLayer_Type.__name__ = "FSLayerType"
_FsHQoSIfAppInPolicyLayer_Object = MibTableColumn
fsHQoSIfAppInPolicyLayer = _FsHQoSIfAppInPolicyLayer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 4),
    _FsHQoSIfAppInPolicyLayer_Type()
)
fsHQoSIfAppInPolicyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSIfAppInPolicyLayer.setStatus("current")


class _FsHQoSIfAppOutPolicyName_Type(OctetString):
    """Custom type fsHQoSIfAppOutPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSIfAppOutPolicyName_Type.__name__ = "OctetString"
_FsHQoSIfAppOutPolicyName_Object = MibTableColumn
fsHQoSIfAppOutPolicyName = _FsHQoSIfAppOutPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 5),
    _FsHQoSIfAppOutPolicyName_Type()
)
fsHQoSIfAppOutPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSIfAppOutPolicyName.setStatus("current")
_FsHQoSIfAppOutPolicyIndex_Type = Unsigned32
_FsHQoSIfAppOutPolicyIndex_Object = MibTableColumn
fsHQoSIfAppOutPolicyIndex = _FsHQoSIfAppOutPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 6),
    _FsHQoSIfAppOutPolicyIndex_Type()
)
fsHQoSIfAppOutPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSIfAppOutPolicyIndex.setStatus("current")


class _FsHQoSIfAppOutPolicyLayer_Type(FSLayerType):
    """Custom type fsHQoSIfAppOutPolicyLayer based on FSLayerType"""
    defaultValue = 0


_FsHQoSIfAppOutPolicyLayer_Type.__name__ = "FSLayerType"
_FsHQoSIfAppOutPolicyLayer_Object = MibTableColumn
fsHQoSIfAppOutPolicyLayer = _FsHQoSIfAppOutPolicyLayer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 7),
    _FsHQoSIfAppOutPolicyLayer_Type()
)
fsHQoSIfAppOutPolicyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSIfAppOutPolicyLayer.setStatus("current")


class _FsHQoSIfAppPortQueueName_Type(OctetString):
    """Custom type fsHQoSIfAppPortQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsHQoSIfAppPortQueueName_Type.__name__ = "OctetString"
_FsHQoSIfAppPortQueueName_Object = MibTableColumn
fsHQoSIfAppPortQueueName = _FsHQoSIfAppPortQueueName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 8),
    _FsHQoSIfAppPortQueueName_Type()
)
fsHQoSIfAppPortQueueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSIfAppPortQueueName.setStatus("current")
_FsHQoSIfAppPortQueueIndex_Type = Unsigned32
_FsHQoSIfAppPortQueueIndex_Object = MibTableColumn
fsHQoSIfAppPortQueueIndex = _FsHQoSIfAppPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 9),
    _FsHQoSIfAppPortQueueIndex_Type()
)
fsHQoSIfAppPortQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHQoSIfAppPortQueueIndex.setStatus("current")


class _FsHQoSIfAppPortQueueShaping_Type(Integer32):
    """Custom type fsHQoSIfAppPortQueueShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FsHQoSIfAppPortQueueShaping_Type.__name__ = "Integer32"
_FsHQoSIfAppPortQueueShaping_Object = MibTableColumn
fsHQoSIfAppPortQueueShaping = _FsHQoSIfAppPortQueueShaping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 3, 11, 1, 1, 10),
    _FsHQoSIfAppPortQueueShaping_Type()
)
fsHQoSIfAppPortQueueShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHQoSIfAppPortQueueShaping.setStatus("current")
if mibBuilder.loadTexts:
    fsHQoSIfAppPortQueueShaping.setUnits("kilobits per second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ROUTER-QOS-MIB",
    **{"FSCosType": FSCosType,
       "FSQType": FSQType,
       "FSQDirectionType": FSQDirectionType,
       "FSLayerType": FSLayerType,
       "fsRouterQoSMIB": fsRouterQoSMIB,
       "fsCBQoSMIBObjects": fsCBQoSMIBObjects,
       "fsCBQoSIfStaticsObjects": fsCBQoSIfStaticsObjects,
       "fsCBQoSIfCbwfqRunInfoTable": fsCBQoSIfCbwfqRunInfoTable,
       "fsCBQoSIfCbwfqRunInfoEntry": fsCBQoSIfCbwfqRunInfoEntry,
       "fsCBQoSIfCbwfqPolicyIfIndex": fsCBQoSIfCbwfqPolicyIfIndex,
       "fsCBQoSIfCbwfqQueueSize": fsCBQoSIfCbwfqQueueSize,
       "fsCBQoSIfCbwfqDiscard": fsCBQoSIfCbwfqDiscard,
       "fsCBQoSIfCbwfqEfQueueSize": fsCBQoSIfCbwfqEfQueueSize,
       "fsCBQoSIfCbwfqAfQueueSize": fsCBQoSIfCbwfqAfQueueSize,
       "fsCBQoSIfCbwfqBeQueueSize": fsCBQoSIfCbwfqBeQueueSize,
       "fsCBQoSIfCbwfqBeActiveQueueNum": fsCBQoSIfCbwfqBeActiveQueueNum,
       "fsCBQoSIfCbwfqBeMaxActiveQueueNum": fsCBQoSIfCbwfqBeMaxActiveQueueNum,
       "fsCBQoSIfCbwfqBeTotalQueueNum": fsCBQoSIfCbwfqBeTotalQueueNum,
       "fsCBQoSIfCbwfqAfAllocatedQueueNum": fsCBQoSIfCbwfqAfAllocatedQueueNum,
       "fsCBQoSIfCbwfqPass": fsCBQoSIfCbwfqPass,
       "fsCBQoSIfCbwfqDroppedRateIn5Min": fsCBQoSIfCbwfqDroppedRateIn5Min,
       "fsCBQoSIfCbwfqPassBytes": fsCBQoSIfCbwfqPassBytes,
       "fsCBQoSIfCbwfqDiscardBytes": fsCBQoSIfCbwfqDiscardBytes,
       "fsCBQoSIfClassMatchRunInfoTable": fsCBQoSIfClassMatchRunInfoTable,
       "fsCBQoSIfClassMatchRunInfoEntry": fsCBQoSIfClassMatchRunInfoEntry,
       "fsCBQoSIfClassMatchIfIndex": fsCBQoSIfClassMatchIfIndex,
       "fsCBQoSIfClassMatchPolicyDirection": fsCBQoSIfClassMatchPolicyDirection,
       "fsCBQoSIfClassMatchClassIndex": fsCBQoSIfClassMatchClassIndex,
       "fsCBQoSIfClassMatchedPackets": fsCBQoSIfClassMatchedPackets,
       "fsCBQoSIfClassMatchedBytes": fsCBQoSIfClassMatchedBytes,
       "fsCBQosIfClassPassedPackets": fsCBQosIfClassPassedPackets,
       "fsCBQosIfClassDroppedPackets": fsCBQosIfClassDroppedPackets,
       "fsCBQoSIfPolicyName": fsCBQoSIfPolicyName,
       "fsCBQoSIfClassName": fsCBQoSIfClassName,
       "fsCBQoSIfClassPassBytes": fsCBQoSIfClassPassBytes,
       "fsCBQoSIfClassDiscardBytes": fsCBQoSIfClassDiscardBytes,
       "fsCBQoSIfCarRunInfoTable": fsCBQoSIfCarRunInfoTable,
       "fsCBQoSIfCarRunInfoEntry": fsCBQoSIfCarRunInfoEntry,
       "fsCBQoSIfCarIfIndex": fsCBQoSIfCarIfIndex,
       "fsCBQoSIfCarPolicyDirection": fsCBQoSIfCarPolicyDirection,
       "fsCBQoSIfCarClassIndex": fsCBQoSIfCarClassIndex,
       "fsCBQoSIfCarConformedPackets": fsCBQoSIfCarConformedPackets,
       "fsCBQoSIfCarConformedBytes": fsCBQoSIfCarConformedBytes,
       "fsCBQoSIfCarExceededPackets": fsCBQoSIfCarExceededPackets,
       "fsCBQoSIfCarExceededBytes": fsCBQoSIfCarExceededBytes,
       "fsCBQoSIfCarViolatedPackets": fsCBQoSIfCarViolatedPackets,
       "fsCBQoSIfCarViolatedBytes": fsCBQoSIfCarViolatedBytes,
       "fsCBQoSIfRemarkRunInfoTable": fsCBQoSIfRemarkRunInfoTable,
       "fsCBQoSIfRemarkRunInfoEntry": fsCBQoSIfRemarkRunInfoEntry,
       "fsCBQoSIfRemarkIfIndex": fsCBQoSIfRemarkIfIndex,
       "fsCBQoSIfRemarkPolicyDirection": fsCBQoSIfRemarkPolicyDirection,
       "fsCBQoSIfRemarkClassIndex": fsCBQoSIfRemarkClassIndex,
       "fsCBQoSIfRemarkedPackets": fsCBQoSIfRemarkedPackets,
       "fsCBQoSIfRemarkedBytes": fsCBQoSIfRemarkedBytes,
       "fsCBQoSIfQueueRunInfoTable": fsCBQoSIfQueueRunInfoTable,
       "fsCBQoSIfQueueRunInfoEntry": fsCBQoSIfQueueRunInfoEntry,
       "fsCBQoSIfQueueIfIndex": fsCBQoSIfQueueIfIndex,
       "fsCBQoSIfQueuePolicyDirection": fsCBQoSIfQueuePolicyDirection,
       "fsCBQoSIfQueueClassIndex": fsCBQoSIfQueueClassIndex,
       "fsCBQoSIfQueueMatchedPackets": fsCBQoSIfQueueMatchedPackets,
       "fsCBQoSIfQueueMatchedBytes": fsCBQoSIfQueueMatchedBytes,
       "fsCBQoSIfQueueEnqueuedPackets": fsCBQoSIfQueueEnqueuedPackets,
       "fsCBQoSIfQueueEnqueuedBytes": fsCBQoSIfQueueEnqueuedBytes,
       "fsCBQoSIfQueueDiscardedPackets": fsCBQoSIfQueueDiscardedPackets,
       "fsCBQoSIfQueueDiscardedBytes": fsCBQoSIfQueueDiscardedBytes,
       "fsCBQoSIfWredRunInfoTable": fsCBQoSIfWredRunInfoTable,
       "fsCBQoSIfWredRunInfoEntry": fsCBQoSIfWredRunInfoEntry,
       "fsCBQoSIfWredIfIndex": fsCBQoSIfWredIfIndex,
       "fsCBQoSIfWredClassIndex": fsCBQoSIfWredClassIndex,
       "fsCBQoSIfWredClassValue": fsCBQoSIfWredClassValue,
       "fsCBQoSIfWredRandomDiscardedPackets": fsCBQoSIfWredRandomDiscardedPackets,
       "fsCBQoSIfWredTailDiscardedPackets": fsCBQoSIfWredTailDiscardedPackets,
       "fsIfQoSMIBObjects": fsIfQoSMIBObjects,
       "fsIfQosPQRunInfoTable": fsIfQosPQRunInfoTable,
       "fsIfQosPQRunInfoEntry": fsIfQosPQRunInfoEntry,
       "fsIfQosPQIfIndex": fsIfQosPQIfIndex,
       "fsIfQosPQListNum": fsIfQosPQListNum,
       "fsIfQosPQIfName": fsIfQosPQIfName,
       "fsIfQosPQHighPkt": fsIfQosPQHighPkt,
       "fsIfQosPQHighDiscard": fsIfQosPQHighDiscard,
       "fsIfQosPQHighMaxQueLen": fsIfQosPQHighMaxQueLen,
       "fsIfQosPQMiddlePkt": fsIfQosPQMiddlePkt,
       "fsIfQosPQMiddleDiscard": fsIfQosPQMiddleDiscard,
       "fsIfQosPQMiddleMaxQueLen": fsIfQosPQMiddleMaxQueLen,
       "fsIfQosPQNormalPkt": fsIfQosPQNormalPkt,
       "fsIfQosPQNormalDiscard": fsIfQosPQNormalDiscard,
       "fsIfQosPQNormalMaxQueLen": fsIfQosPQNormalMaxQueLen,
       "fsIfQosPQLowPkt": fsIfQosPQLowPkt,
       "fsIfQosPQLowDiscard": fsIfQosPQLowDiscard,
       "fsIfQosPQLowMaxQueLen": fsIfQosPQLowMaxQueLen,
       "fsIfQosCQRunInfoTable": fsIfQosCQRunInfoTable,
       "fsIfQosCQRunInfoEntry": fsIfQosCQRunInfoEntry,
       "fsIfQosCQRunInfoIfIndex": fsIfQosCQRunInfoIfIndex,
       "fsIfQosCQRunInfoQueNum": fsIfQosCQRunInfoQueNum,
       "fsIfQosCQRunInfoIfName": fsIfQosCQRunInfoIfName,
       "fsIfQosCQRunInfoQuePkt": fsIfQosCQRunInfoQuePkt,
       "fsIfQosCQRunInfoQueDiscard": fsIfQosCQRunInfoQueDiscard,
       "fsIfQosCQRunInfoMaxQueLen": fsIfQosCQRunInfoMaxQueLen,
       "fsIfQosWFQRunInfoTable": fsIfQosWFQRunInfoTable,
       "fsIfQosWFQRunInfoEntry": fsIfQosWFQRunInfoEntry,
       "fsIfQosWFQIfIndex": fsIfQosWFQIfIndex,
       "fsIfQosWFQIfName": fsIfQosWFQIfName,
       "fsIfQosWFQMaxQueLen": fsIfQosWFQMaxQueLen,
       "fsIfQosWFQTotalQueNum": fsIfQosWFQTotalQueNum,
       "fsIfQosWFQCurQueLen": fsIfQosWFQCurQueLen,
       "fsIfQosWFQTotalDiscard": fsIfQosWFQTotalDiscard,
       "fsIfQosWFQActiveQueNum": fsIfQosWFQActiveQueNum,
       "fsIfQosWFQMaxActiveQueNum": fsIfQosWFQMaxActiveQueNum,
       "fsIfQosWredRunInfoTable": fsIfQosWredRunInfoTable,
       "fsIfQosWredRunInfoEntry": fsIfQosWredRunInfoEntry,
       "fsIfQosWredIfIndex": fsIfQosWredIfIndex,
       "fsIfQosWredValue": fsIfQosWredValue,
       "fsIfQosWredRandomDiscardedPackets": fsIfQosWredRandomDiscardedPackets,
       "fsIfQosWredTailDiscardedPackets": fsIfQosWredTailDiscardedPackets,
       "fsIfQosCARTable": fsIfQosCARTable,
       "fsIfQosCAREntry": fsIfQosCAREntry,
       "fsIfQosCARIfIndex": fsIfQosCARIfIndex,
       "fsIfQosCARIfName": fsIfQosCARIfName,
       "fsIfQosCARPktDirection": fsIfQosCARPktDirection,
       "fsIfQosCARType": fsIfQosCARType,
       "fsIfQosCARListNum": fsIfQosCARListNum,
       "fsIfQosCARindex": fsIfQosCARindex,
       "fsIfQosCARCIR": fsIfQosCARCIR,
       "fsIfQosCARBurstSize": fsIfQosCARBurstSize,
       "fsIfQosCARExcessBurstSize": fsIfQosCARExcessBurstSize,
       "fsIfQosCARConformAction": fsIfQosCARConformAction,
       "fsIfQosCARExceedAction": fsIfQosCARExceedAction,
       "fsIfQosCARConformNewPrec": fsIfQosCARConformNewPrec,
       "fsIfQosCARExceedNewPrec": fsIfQosCARExceedNewPrec,
       "fsIfQosCARConformPkt": fsIfQosCARConformPkt,
       "fsIfQosCARConformByte": fsIfQosCARConformByte,
       "fsIfQosCARExceedPkt": fsIfQosCARExceedPkt,
       "fsIfQosCARExceedByte": fsIfQosCARExceedByte,
       "fsIfQosGTSTable": fsIfQosGTSTable,
       "fsIfQosGTSEntry": fsIfQosGTSEntry,
       "fsIfQosGTSIfIndex": fsIfQosGTSIfIndex,
       "fsIfQosGTSIfName": fsIfQosGTSIfName,
       "fsIfQosGTSType": fsIfQosGTSType,
       "fsIfQosGTSACLNum": fsIfQosGTSACLNum,
       "fsIfQosGTSCIR": fsIfQosGTSCIR,
       "fsIfQosGTSBurstSize": fsIfQosGTSBurstSize,
       "fsIfQosGTSExcessBurstSize": fsIfQosGTSExcessBurstSize,
       "fsIfQosGTSMaxQueLen": fsIfQosGTSMaxQueLen,
       "fsIfQosGTSCurQueLen": fsIfQosGTSCurQueLen,
       "fsIfQosGTSPassPkt": fsIfQosGTSPassPkt,
       "fsIfQosGTSPassByte": fsIfQosGTSPassByte,
       "fsIfQosGTSDiscardPkt": fsIfQosGTSDiscardPkt,
       "fsIfQosGTSDiscardByte": fsIfQosGTSDiscardByte,
       "fsIfQosRTPIfQueueRunInfoTable": fsIfQosRTPIfQueueRunInfoTable,
       "fsIfQosRTPIfQueueRunInfoEntry": fsIfQosRTPIfQueueRunInfoEntry,
       "fsIfQosRTPIfApplyIfIndex": fsIfQosRTPIfApplyIfIndex,
       "fsIfQosRTPIfQueueSize": fsIfQosRTPIfQueueSize,
       "fsIfQosRTPIfQueueMaxSize": fsIfQosRTPIfQueueMaxSize,
       "fsIfQosRTPIfQueueOutputs": fsIfQosRTPIfQueueOutputs,
       "fsIfQosRTPIfQueueDiscards": fsIfQosRTPIfQueueDiscards,
       "fsIfQosFlowLimitRunInfoTable": fsIfQosFlowLimitRunInfoTable,
       "fsIfQosFlowLimitRunInfoEntry": fsIfQosFlowLimitRunInfoEntry,
       "fsIfQosFlowLimitLabelNum": fsIfQosFlowLimitLabelNum,
       "fsIfQosFlowLimitPktDirection": fsIfQosFlowLimitPktDirection,
       "fsIfQosFlowLimitCIR": fsIfQosFlowLimitCIR,
       "fsIfQosFlowLimitBurstSize": fsIfQosFlowLimitBurstSize,
       "fsIfQosFlowLimitExcessBurstSize": fsIfQosFlowLimitExcessBurstSize,
       "fsIfQosFlowLimitConformAction": fsIfQosFlowLimitConformAction,
       "fsIfQosFlowLimitExceedAction": fsIfQosFlowLimitExceedAction,
       "fsIfQosFlowLimitConformNewPrec": fsIfQosFlowLimitConformNewPrec,
       "fsIfQosFlowLimitExceedNewPrec": fsIfQosFlowLimitExceedNewPrec,
       "fsIfQosFlowLimitConformPkt": fsIfQosFlowLimitConformPkt,
       "fsIfQosFlowLimitConformByte": fsIfQosFlowLimitConformByte,
       "fsIfQosFlowLimitExceedPkt": fsIfQosFlowLimitExceedPkt,
       "fsIfQosFlowLimitExceedByte": fsIfQosFlowLimitExceedByte,
       "fsHQoSMIBObjects": fsHQoSMIBObjects,
       "fsHQoSScalarObjects": fsHQoSScalarObjects,
       "fsHQoSNameType": fsHQoSNameType,
       "fsHQoSNameFind": fsHQoSNameFind,
       "fsHQoSNameIndex": fsHQoSNameIndex,
       "fsHQoSUserQObjects": fsHQoSUserQObjects,
       "fsHQoSUserQInIndexNext": fsHQoSUserQInIndexNext,
       "fsHQoSUserQOutIndexNext": fsHQoSUserQOutIndexNext,
       "fsHQoSUserQTable": fsHQoSUserQTable,
       "fsHQoSUserQEntry": fsHQoSUserQEntry,
       "fsHQoSUserQIndex": fsHQoSUserQIndex,
       "fsHQoSUserQName": fsHQoSUserQName,
       "fsHQoSUserQDirection": fsHQoSUserQDirection,
       "fsHQoSUserQRowStatus": fsHQoSUserQRowStatus,
       "fsHQoSUserQFlowQName": fsHQoSUserQFlowQName,
       "fsHQoSUserQFlowQIndex": fsHQoSUserQFlowQIndex,
       "fsHQoSUserQGroupName": fsHQoSUserQGroupName,
       "fsHQoSUserQGroupIndex": fsHQoSUserQGroupIndex,
       "fsHQoSUserQFlowMapName": fsHQoSUserQFlowMapName,
       "fsHQoSUserQFlowMapIndex": fsHQoSUserQFlowMapIndex,
       "fsHQoSUserQCIR": fsHQoSUserQCIR,
       "fsHQoSUserQPIR": fsHQoSUserQPIR,
       "fsHQoSUserGroupQObjects": fsHQoSUserGroupQObjects,
       "fsHQoSUserGroupQInIndexNext": fsHQoSUserGroupQInIndexNext,
       "fsHQoSUserGroupQOutIndexNext": fsHQoSUserGroupQOutIndexNext,
       "fsHQoSUserGroupQTable": fsHQoSUserGroupQTable,
       "fsHQoSUserGroupQEntry": fsHQoSUserGroupQEntry,
       "fsHQoSUserGroupQIndex": fsHQoSUserGroupQIndex,
       "fsHQoSUserGroupQName": fsHQoSUserGroupQName,
       "fsHQoSUserGroupQDirection": fsHQoSUserGroupQDirection,
       "fsHQoSUserGroupQRowStatus": fsHQoSUserGroupQRowStatus,
       "fsHQoSUserGroupQShaping": fsHQoSUserGroupQShaping,
       "fsHQoSFlowQObjects": fsHQoSFlowQObjects,
       "fsHQoSFlowQIndexNext": fsHQoSFlowQIndexNext,
       "fsHQoSFlowQTable": fsHQoSFlowQTable,
       "fsHQoSFlowQEntry": fsHQoSFlowQEntry,
       "fsHQoSFlowQIndex": fsHQoSFlowQIndex,
       "fsHQoSFlowQName": fsHQoSFlowQName,
       "fsHQoSFlowQRowStatus": fsHQoSFlowQRowStatus,
       "fsHQoSFlowQBEQType": fsHQoSFlowQBEQType,
       "fsHQoSFlowQBEQWredWeight": fsHQoSFlowQBEQWredWeight,
       "fsHQoSFlowQBEQWredName": fsHQoSFlowQBEQWredName,
       "fsHQoSFlowQBEQDepth": fsHQoSFlowQBEQDepth,
       "fsHQoSFlowQBEQShaping": fsHQoSFlowQBEQShaping,
       "fsHQoSFlowQAF1QType": fsHQoSFlowQAF1QType,
       "fsHQoSFlowQAF1QWredWeight": fsHQoSFlowQAF1QWredWeight,
       "fsHQoSFlowQAF1QWredName": fsHQoSFlowQAF1QWredName,
       "fsHQoSFlowQAF1QDepth": fsHQoSFlowQAF1QDepth,
       "fsHQoSFlowQAF1QShaping": fsHQoSFlowQAF1QShaping,
       "fsHQoSFlowQAF2QType": fsHQoSFlowQAF2QType,
       "fsHQoSFlowQAF2QWredWeight": fsHQoSFlowQAF2QWredWeight,
       "fsHQoSFlowQAF2QWredName": fsHQoSFlowQAF2QWredName,
       "fsHQoSFlowQAF2QDepth": fsHQoSFlowQAF2QDepth,
       "fsHQoSFlowQAF2QShaping": fsHQoSFlowQAF2QShaping,
       "fsHQoSFlowQAF3QType": fsHQoSFlowQAF3QType,
       "fsHQoSFlowQAF3QWredWeight": fsHQoSFlowQAF3QWredWeight,
       "fsHQoSFlowQAF3QWredName": fsHQoSFlowQAF3QWredName,
       "fsHQoSFlowQAF3QDepth": fsHQoSFlowQAF3QDepth,
       "fsHQoSFlowQAF3QShaping": fsHQoSFlowQAF3QShaping,
       "fsHQoSFlowQAF4QType": fsHQoSFlowQAF4QType,
       "fsHQoSFlowQAF4QWredWeight": fsHQoSFlowQAF4QWredWeight,
       "fsHQoSFlowQAF4QWredName": fsHQoSFlowQAF4QWredName,
       "fsHQoSFlowQAF4QDepth": fsHQoSFlowQAF4QDepth,
       "fsHQoSFlowQAF4QShaping": fsHQoSFlowQAF4QShaping,
       "fsHQoSFlowQEFQType": fsHQoSFlowQEFQType,
       "fsHQoSFlowQEFQWredWeight": fsHQoSFlowQEFQWredWeight,
       "fsHQoSFlowQEFQWredName": fsHQoSFlowQEFQWredName,
       "fsHQoSFlowQEFQDepth": fsHQoSFlowQEFQDepth,
       "fsHQoSFlowQEFQShaping": fsHQoSFlowQEFQShaping,
       "fsHQoSFlowQCS6QType": fsHQoSFlowQCS6QType,
       "fsHQoSFlowQCS6QWredWeight": fsHQoSFlowQCS6QWredWeight,
       "fsHQoSFlowQCS6QWredName": fsHQoSFlowQCS6QWredName,
       "fsHQoSFlowQCS6QDepth": fsHQoSFlowQCS6QDepth,
       "fsHQoSFlowQCS6QShaping": fsHQoSFlowQCS6QShaping,
       "fsHQoSFlowQCS7QType": fsHQoSFlowQCS7QType,
       "fsHQoSFlowQCS7QWredWeight": fsHQoSFlowQCS7QWredWeight,
       "fsHQoSFlowQCS7QWredName": fsHQoSFlowQCS7QWredName,
       "fsHQoSFlowQCS7QDepth": fsHQoSFlowQCS7QDepth,
       "fsHQoSFlowQCS7QShaping": fsHQoSFlowQCS7QShaping,
       "fsHQoSFlowMapObjects": fsHQoSFlowMapObjects,
       "fsHQoSFlowMapIndexNext": fsHQoSFlowMapIndexNext,
       "fsHQoSFlowMapTable": fsHQoSFlowMapTable,
       "fsHQoSFlowMapEntry": fsHQoSFlowMapEntry,
       "fsHQoSFlowMapIndex": fsHQoSFlowMapIndex,
       "fsHQoSFlowMapName": fsHQoSFlowMapName,
       "fsHQoSFlowMapRowStatus": fsHQoSFlowMapRowStatus,
       "fsHQoSFlowMapBEQ2PortQ": fsHQoSFlowMapBEQ2PortQ,
       "fsHQoSFlowMapAF1Q2PortQ": fsHQoSFlowMapAF1Q2PortQ,
       "fsHQoSFlowMapAF2Q2PortQ": fsHQoSFlowMapAF2Q2PortQ,
       "fsHQoSFlowMapAF3Q2PortQ": fsHQoSFlowMapAF3Q2PortQ,
       "fsHQoSFlowMapAF4Q2PortQ": fsHQoSFlowMapAF4Q2PortQ,
       "fsHQoSFlowMapEFQ2PortQ": fsHQoSFlowMapEFQ2PortQ,
       "fsHQoSFlowMapCS6Q2PortQ": fsHQoSFlowMapCS6Q2PortQ,
       "fsHQoSFlowMapCS7Q2PortQ": fsHQoSFlowMapCS7Q2PortQ,
       "fsHQoSTClassifierObjects": fsHQoSTClassifierObjects,
       "fsHQoSTClassifierIndexNext": fsHQoSTClassifierIndexNext,
       "fsHQoSTClassifierTable": fsHQoSTClassifierTable,
       "fsHQoSTClassifierEntry": fsHQoSTClassifierEntry,
       "fsHQoSTClassifierIndex": fsHQoSTClassifierIndex,
       "fsHQoSTClassifierInstance": fsHQoSTClassifierInstance,
       "fsHQoSTClassifierName": fsHQoSTClassifierName,
       "fsHQoSTClassifierType": fsHQoSTClassifierType,
       "fsHQoSTClassifierRowStatus": fsHQoSTClassifierRowStatus,
       "fsHQoSTClassifierMatchMask": fsHQoSTClassifierMatchMask,
       "fsHQoSTClassifierMatchV4Any": fsHQoSTClassifierMatchV4Any,
       "fsHQoSTClassifierMatchV4AclID": fsHQoSTClassifierMatchV4AclID,
       "fsHQoSTClassifierV4AclName": fsHQoSTClassifierV4AclName,
       "fsHQoSTClassifierMatchV4Dscp": fsHQoSTClassifierMatchV4Dscp,
       "fsHQoSTClassifierMatchV4Tos": fsHQoSTClassifierMatchV4Tos,
       "fsHQoSTClassifierMatchV6Any": fsHQoSTClassifierMatchV6Any,
       "fsHQoSTClassifierMatchV6AclID": fsHQoSTClassifierMatchV6AclID,
       "fsHQoSTClassifierV6AclName": fsHQoSTClassifierV6AclName,
       "fsHQoSTClassifierMatchV6Dscp": fsHQoSTClassifierMatchV6Dscp,
       "fsHQoSTClassifierMatchCos": fsHQoSTClassifierMatchCos,
       "fsHQoSTClassifierMatchExp": fsHQoSTClassifierMatchExp,
       "fsHQoSTClassifierMatchSrcMac": fsHQoSTClassifierMatchSrcMac,
       "fsHQoSTClassifierMatchDstMac": fsHQoSTClassifierMatchDstMac,
       "fsHQoSTBehaviorObjects": fsHQoSTBehaviorObjects,
       "fsHQoSTBehaviorIndexNext": fsHQoSTBehaviorIndexNext,
       "fsHQoSTBehaviorTable": fsHQoSTBehaviorTable,
       "fsHQoSTBehaviorEntry": fsHQoSTBehaviorEntry,
       "fsHQoSTBehaviorIndex": fsHQoSTBehaviorIndex,
       "fsHQoSTBehaviorName": fsHQoSTBehaviorName,
       "fsHQoSTBehaviorRowStatus": fsHQoSTBehaviorRowStatus,
       "fsHQoSTBehaviorMask": fsHQoSTBehaviorMask,
       "fsHQoSTBehaviorUserQName": fsHQoSTBehaviorUserQName,
       "fsHQoSTBehaviorUserQDir": fsHQoSTBehaviorUserQDir,
       "fsHQoSTBehaviorTCos": fsHQoSTBehaviorTCos,
       "fsHQoSTBehaviorTColor": fsHQoSTBehaviorTColor,
       "fsHQoSTBehaviorRV4Dscp": fsHQoSTBehaviorRV4Dscp,
       "fsHQoSTBehaviorRV4Tos": fsHQoSTBehaviorRV4Tos,
       "fsHQoSTBehaviorRV6Dscp": fsHQoSTBehaviorRV6Dscp,
       "fsHQoSTBehaviorRVlanCos": fsHQoSTBehaviorRVlanCos,
       "fsHQoSTBehaviorRExp": fsHQoSTBehaviorRExp,
       "fsHQoSTBehaviorSubPolicyName": fsHQoSTBehaviorSubPolicyName,
       "fsHQoSTPolicyObjects": fsHQoSTPolicyObjects,
       "fsHQoSTPolicyIndexNext": fsHQoSTPolicyIndexNext,
       "fsHQoSTPolicyTable": fsHQoSTPolicyTable,
       "fsHQoSTPolicyEntry": fsHQoSTPolicyEntry,
       "fsHQoSTPolicyIndex": fsHQoSTPolicyIndex,
       "fsHQoSTPolicyName": fsHQoSTPolicyName,
       "fsHQoSTPolicyRowStatus": fsHQoSTPolicyRowStatus,
       "fsHQoSTPolicyMapIndexNext": fsHQoSTPolicyMapIndexNext,
       "fsHQoSTPolicyMapTable": fsHQoSTPolicyMapTable,
       "fsHQoSTPolicyMapEntry": fsHQoSTPolicyMapEntry,
       "fsHQoSTPolicyMapIndex": fsHQoSTPolicyMapIndex,
       "fsHQoSTPolicyMapPolicyName": fsHQoSTPolicyMapPolicyName,
       "fsHQoSTPolicyMapPolicyIndex": fsHQoSTPolicyMapPolicyIndex,
       "fsHQoSTPolicyMapTClassfierName": fsHQoSTPolicyMapTClassfierName,
       "fsHQoSTPolicyMapTClassfierIndex": fsHQoSTPolicyMapTClassfierIndex,
       "fsHQoSTPolicyMapTBehaviorName": fsHQoSTPolicyMapTBehaviorName,
       "fsHQoSTPolicyMapTBehaviorIndex": fsHQoSTPolicyMapTBehaviorIndex,
       "fsHQoSTPolicyMapPrecedence": fsHQoSTPolicyMapPrecedence,
       "fsHQoSTPolicyMapRowStatus": fsHQoSTPolicyMapRowStatus,
       "fsHQoSVoQObjects": fsHQoSVoQObjects,
       "fsHQoSVoQEnable": fsHQoSVoQEnable,
       "fsHQoSVoQDeviceTable": fsHQoSVoQDeviceTable,
       "fsHQoSVoQDeviceEntry": fsHQoSVoQDeviceEntry,
       "fsHQoSVoQDeviceId": fsHQoSVoQDeviceId,
       "fsHQoSVoQDeviceCredit": fsHQoSVoQDeviceCredit,
       "fsHQoSPortQObjects": fsHQoSPortQObjects,
       "fsHQoSPortQIndexNext": fsHQoSPortQIndexNext,
       "fsHQoSPortQTable": fsHQoSPortQTable,
       "fsHQoSPortQEntry": fsHQoSPortQEntry,
       "fsHQoSPortQIndex": fsHQoSPortQIndex,
       "fsHQoSPortQName": fsHQoSPortQName,
       "fsHQoSPortQRowStatus": fsHQoSPortQRowStatus,
       "fsHQoSPortQBEQType": fsHQoSPortQBEQType,
       "fsHQoSPortQBEQWredWeight": fsHQoSPortQBEQWredWeight,
       "fsHQoSPortQBEQWredName": fsHQoSPortQBEQWredName,
       "fsHQoSPortQBEQDepth": fsHQoSPortQBEQDepth,
       "fsHQoSPortQBEQShaping": fsHQoSPortQBEQShaping,
       "fsHQoSPortQAF1QType": fsHQoSPortQAF1QType,
       "fsHQoSPortQAF1QWredWeight": fsHQoSPortQAF1QWredWeight,
       "fsHQoSPortQAF1QWredName": fsHQoSPortQAF1QWredName,
       "fsHQoSPortQAF1QDepth": fsHQoSPortQAF1QDepth,
       "fsHQoSPortQAF1QShaping": fsHQoSPortQAF1QShaping,
       "fsHQoSPortQAF2QType": fsHQoSPortQAF2QType,
       "fsHQoSPortQAF2QWredWeight": fsHQoSPortQAF2QWredWeight,
       "fsHQoSPortQAF2QWredName": fsHQoSPortQAF2QWredName,
       "fsHQoSPortQAF2QDepth": fsHQoSPortQAF2QDepth,
       "fsHQoSPortQAF2QShaping": fsHQoSPortQAF2QShaping,
       "fsHQoSPortQAF3QType": fsHQoSPortQAF3QType,
       "fsHQoSPortQAF3QWredWeight": fsHQoSPortQAF3QWredWeight,
       "fsHQoSPortQAF3QWredName": fsHQoSPortQAF3QWredName,
       "fsHQoSPortQAF3QDepth": fsHQoSPortQAF3QDepth,
       "fsHQoSPortQAF3QShaping": fsHQoSPortQAF3QShaping,
       "fsHQoSPortQAF4QType": fsHQoSPortQAF4QType,
       "fsHQoSPortQAF4QWredWeight": fsHQoSPortQAF4QWredWeight,
       "fsHQoSPortQAF4QWredName": fsHQoSPortQAF4QWredName,
       "fsHQoSPortQAF4QDepth": fsHQoSPortQAF4QDepth,
       "fsHQoSPortQAF4QShaping": fsHQoSPortQAF4QShaping,
       "fsHQoSPortQEFQType": fsHQoSPortQEFQType,
       "fsHQoSPortQEFQWredWeight": fsHQoSPortQEFQWredWeight,
       "fsHQoSPortQEFQWredName": fsHQoSPortQEFQWredName,
       "fsHQoSPortQEFQDepth": fsHQoSPortQEFQDepth,
       "fsHQoSPortQEFQShaping": fsHQoSPortQEFQShaping,
       "fsHQoSPortQCS6QType": fsHQoSPortQCS6QType,
       "fsHQoSPortQCS6QWredWeight": fsHQoSPortQCS6QWredWeight,
       "fsHQoSPortQCS6QWredName": fsHQoSPortQCS6QWredName,
       "fsHQoSPortQCS6QDepth": fsHQoSPortQCS6QDepth,
       "fsHQoSPortQCS6QShaping": fsHQoSPortQCS6QShaping,
       "fsHQoSPortQCS7QType": fsHQoSPortQCS7QType,
       "fsHQoSPortQCS7QWredWeight": fsHQoSPortQCS7QWredWeight,
       "fsHQoSPortQCS7QWredName": fsHQoSPortQCS7QWredName,
       "fsHQoSPortQCS7QDepth": fsHQoSPortQCS7QDepth,
       "fsHQoSPortQCS7QShaping": fsHQoSPortQCS7QShaping,
       "fsHQoSIfAppObjects": fsHQoSIfAppObjects,
       "fsHQoSIfAppTable": fsHQoSIfAppTable,
       "fsHQoSIfAppEntry": fsHQoSIfAppEntry,
       "fsHQoSIfAppIndex": fsHQoSIfAppIndex,
       "fsHQoSIfAppInPolicyName": fsHQoSIfAppInPolicyName,
       "fsHQoSIfAppInPolicyIndex": fsHQoSIfAppInPolicyIndex,
       "fsHQoSIfAppInPolicyLayer": fsHQoSIfAppInPolicyLayer,
       "fsHQoSIfAppOutPolicyName": fsHQoSIfAppOutPolicyName,
       "fsHQoSIfAppOutPolicyIndex": fsHQoSIfAppOutPolicyIndex,
       "fsHQoSIfAppOutPolicyLayer": fsHQoSIfAppOutPolicyLayer,
       "fsHQoSIfAppPortQueueName": fsHQoSIfAppPortQueueName,
       "fsHQoSIfAppPortQueueIndex": fsHQoSIfAppPortQueueIndex,
       "fsHQoSIfAppPortQueueShaping": fsHQoSIfAppPortQueueShaping}
)
