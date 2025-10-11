# SNMP MIB module (QTECH-ROUTER-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ROUTER-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:36 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechRouterQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106)
)
if mibBuilder.loadTexts:
    qtechRouterQoSMIB.setRevisions(
        ("2011-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechCosType(TextualConvention, Integer32):
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



class QtechQType(TextualConvention, Integer32):
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



class QtechQDirectionType(TextualConvention, Integer32):
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



class QtechLayerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-layer", 1),
          ("all-layer", 2))
    )



# MIB Managed Objects in the order of their OIDs

_QtechCBQoSMIBObjects_ObjectIdentity = ObjectIdentity
qtechCBQoSMIBObjects = _QtechCBQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1)
)
_QtechCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
qtechCBQoSIfStaticsObjects = _QtechCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1)
)
_QtechCBQoSIfCbwfqRunInfoTable_Object = MibTable
qtechCBQoSIfCbwfqRunInfoTable = _QtechCBQoSIfCbwfqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqRunInfoTable.setStatus("current")
_QtechCBQoSIfCbwfqRunInfoEntry_Object = MibTableRow
qtechCBQoSIfCbwfqRunInfoEntry = _QtechCBQoSIfCbwfqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1)
)
qtechCBQoSIfCbwfqRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfCbwfqPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqRunInfoEntry.setStatus("current")
_QtechCBQoSIfCbwfqPolicyIfIndex_Type = Integer32
_QtechCBQoSIfCbwfqPolicyIfIndex_Object = MibTableColumn
qtechCBQoSIfCbwfqPolicyIfIndex = _QtechCBQoSIfCbwfqPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 1),
    _QtechCBQoSIfCbwfqPolicyIfIndex_Type()
)
qtechCBQoSIfCbwfqPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqPolicyIfIndex.setStatus("current")
_QtechCBQoSIfCbwfqQueueSize_Type = Integer32
_QtechCBQoSIfCbwfqQueueSize_Object = MibTableColumn
qtechCBQoSIfCbwfqQueueSize = _QtechCBQoSIfCbwfqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 2),
    _QtechCBQoSIfCbwfqQueueSize_Type()
)
qtechCBQoSIfCbwfqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqQueueSize.setStatus("current")
_QtechCBQoSIfCbwfqDiscard_Type = Counter64
_QtechCBQoSIfCbwfqDiscard_Object = MibTableColumn
qtechCBQoSIfCbwfqDiscard = _QtechCBQoSIfCbwfqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 3),
    _QtechCBQoSIfCbwfqDiscard_Type()
)
qtechCBQoSIfCbwfqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqDiscard.setStatus("current")
_QtechCBQoSIfCbwfqEfQueueSize_Type = Integer32
_QtechCBQoSIfCbwfqEfQueueSize_Object = MibTableColumn
qtechCBQoSIfCbwfqEfQueueSize = _QtechCBQoSIfCbwfqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 4),
    _QtechCBQoSIfCbwfqEfQueueSize_Type()
)
qtechCBQoSIfCbwfqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqEfQueueSize.setStatus("current")
_QtechCBQoSIfCbwfqAfQueueSize_Type = Integer32
_QtechCBQoSIfCbwfqAfQueueSize_Object = MibTableColumn
qtechCBQoSIfCbwfqAfQueueSize = _QtechCBQoSIfCbwfqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 5),
    _QtechCBQoSIfCbwfqAfQueueSize_Type()
)
qtechCBQoSIfCbwfqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqAfQueueSize.setStatus("current")
_QtechCBQoSIfCbwfqBeQueueSize_Type = Integer32
_QtechCBQoSIfCbwfqBeQueueSize_Object = MibTableColumn
qtechCBQoSIfCbwfqBeQueueSize = _QtechCBQoSIfCbwfqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 6),
    _QtechCBQoSIfCbwfqBeQueueSize_Type()
)
qtechCBQoSIfCbwfqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqBeQueueSize.setStatus("current")
_QtechCBQoSIfCbwfqBeActiveQueueNum_Type = Integer32
_QtechCBQoSIfCbwfqBeActiveQueueNum_Object = MibTableColumn
qtechCBQoSIfCbwfqBeActiveQueueNum = _QtechCBQoSIfCbwfqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 7),
    _QtechCBQoSIfCbwfqBeActiveQueueNum_Type()
)
qtechCBQoSIfCbwfqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqBeActiveQueueNum.setStatus("current")
_QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Type = Integer32
_QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Object = MibTableColumn
qtechCBQoSIfCbwfqBeMaxActiveQueueNum = _QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 8),
    _QtechCBQoSIfCbwfqBeMaxActiveQueueNum_Type()
)
qtechCBQoSIfCbwfqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqBeMaxActiveQueueNum.setStatus("current")
_QtechCBQoSIfCbwfqBeTotalQueueNum_Type = Integer32
_QtechCBQoSIfCbwfqBeTotalQueueNum_Object = MibTableColumn
qtechCBQoSIfCbwfqBeTotalQueueNum = _QtechCBQoSIfCbwfqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 9),
    _QtechCBQoSIfCbwfqBeTotalQueueNum_Type()
)
qtechCBQoSIfCbwfqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqBeTotalQueueNum.setStatus("current")
_QtechCBQoSIfCbwfqAfAllocatedQueueNum_Type = Integer32
_QtechCBQoSIfCbwfqAfAllocatedQueueNum_Object = MibTableColumn
qtechCBQoSIfCbwfqAfAllocatedQueueNum = _QtechCBQoSIfCbwfqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 1, 1, 10),
    _QtechCBQoSIfCbwfqAfAllocatedQueueNum_Type()
)
qtechCBQoSIfCbwfqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCbwfqAfAllocatedQueueNum.setStatus("current")
_QtechCBQoSIfClassMatchRunInfoTable_Object = MibTable
qtechCBQoSIfClassMatchRunInfoTable = _QtechCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchRunInfoTable.setStatus("current")
_QtechCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
qtechCBQoSIfClassMatchRunInfoEntry = _QtechCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1)
)
qtechCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfClassMatchIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfClassMatchPolicyDirection"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfClassMatchClassIndex"),
)
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_QtechCBQoSIfClassMatchIfIndex_Type = Integer32
_QtechCBQoSIfClassMatchIfIndex_Object = MibTableColumn
qtechCBQoSIfClassMatchIfIndex = _QtechCBQoSIfClassMatchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 1),
    _QtechCBQoSIfClassMatchIfIndex_Type()
)
qtechCBQoSIfClassMatchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchIfIndex.setStatus("current")


class _QtechCBQoSIfClassMatchPolicyDirection_Type(Integer32):
    """Custom type qtechCBQoSIfClassMatchPolicyDirection based on Integer32"""
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


_QtechCBQoSIfClassMatchPolicyDirection_Type.__name__ = "Integer32"
_QtechCBQoSIfClassMatchPolicyDirection_Object = MibTableColumn
qtechCBQoSIfClassMatchPolicyDirection = _QtechCBQoSIfClassMatchPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 2),
    _QtechCBQoSIfClassMatchPolicyDirection_Type()
)
qtechCBQoSIfClassMatchPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchPolicyDirection.setStatus("current")
_QtechCBQoSIfClassMatchClassIndex_Type = Integer32
_QtechCBQoSIfClassMatchClassIndex_Object = MibTableColumn
qtechCBQoSIfClassMatchClassIndex = _QtechCBQoSIfClassMatchClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 3),
    _QtechCBQoSIfClassMatchClassIndex_Type()
)
qtechCBQoSIfClassMatchClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchClassIndex.setStatus("current")
_QtechCBQoSIfClassMatchedPackets_Type = Counter64
_QtechCBQoSIfClassMatchedPackets_Object = MibTableColumn
qtechCBQoSIfClassMatchedPackets = _QtechCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 4),
    _QtechCBQoSIfClassMatchedPackets_Type()
)
qtechCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchedPackets.setStatus("current")
_QtechCBQoSIfClassMatchedBytes_Type = Counter64
_QtechCBQoSIfClassMatchedBytes_Object = MibTableColumn
qtechCBQoSIfClassMatchedBytes = _QtechCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 5),
    _QtechCBQoSIfClassMatchedBytes_Type()
)
qtechCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfClassMatchedBytes.setStatus("current")
_QtechCBQosIfClassPassedPackets_Type = Counter64
_QtechCBQosIfClassPassedPackets_Object = MibTableColumn
qtechCBQosIfClassPassedPackets = _QtechCBQosIfClassPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 6),
    _QtechCBQosIfClassPassedPackets_Type()
)
qtechCBQosIfClassPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQosIfClassPassedPackets.setStatus("current")
_QtechCBQosIfClassDroppedPackets_Type = Counter64
_QtechCBQosIfClassDroppedPackets_Object = MibTableColumn
qtechCBQosIfClassDroppedPackets = _QtechCBQosIfClassDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 2, 1, 7),
    _QtechCBQosIfClassDroppedPackets_Type()
)
qtechCBQosIfClassDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQosIfClassDroppedPackets.setStatus("current")
_QtechCBQoSIfCarRunInfoTable_Object = MibTable
qtechCBQoSIfCarRunInfoTable = _QtechCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qtechCBQoSIfCarRunInfoTable.setStatus("current")
_QtechCBQoSIfCarRunInfoEntry_Object = MibTableRow
qtechCBQoSIfCarRunInfoEntry = _QtechCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1)
)
qtechCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfCarIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfCarPolicyDirection"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfCarClassIndex"),
)
if mibBuilder.loadTexts:
    qtechCBQoSIfCarRunInfoEntry.setStatus("current")
_QtechCBQoSIfCarIfIndex_Type = Integer32
_QtechCBQoSIfCarIfIndex_Object = MibTableColumn
qtechCBQoSIfCarIfIndex = _QtechCBQoSIfCarIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 1),
    _QtechCBQoSIfCarIfIndex_Type()
)
qtechCBQoSIfCarIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarIfIndex.setStatus("current")


class _QtechCBQoSIfCarPolicyDirection_Type(Integer32):
    """Custom type qtechCBQoSIfCarPolicyDirection based on Integer32"""
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


_QtechCBQoSIfCarPolicyDirection_Type.__name__ = "Integer32"
_QtechCBQoSIfCarPolicyDirection_Object = MibTableColumn
qtechCBQoSIfCarPolicyDirection = _QtechCBQoSIfCarPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 2),
    _QtechCBQoSIfCarPolicyDirection_Type()
)
qtechCBQoSIfCarPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarPolicyDirection.setStatus("current")
_QtechCBQoSIfCarClassIndex_Type = Integer32
_QtechCBQoSIfCarClassIndex_Object = MibTableColumn
qtechCBQoSIfCarClassIndex = _QtechCBQoSIfCarClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 3),
    _QtechCBQoSIfCarClassIndex_Type()
)
qtechCBQoSIfCarClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarClassIndex.setStatus("current")
_QtechCBQoSIfCarConformedPackets_Type = Counter64
_QtechCBQoSIfCarConformedPackets_Object = MibTableColumn
qtechCBQoSIfCarConformedPackets = _QtechCBQoSIfCarConformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 4),
    _QtechCBQoSIfCarConformedPackets_Type()
)
qtechCBQoSIfCarConformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarConformedPackets.setStatus("current")
_QtechCBQoSIfCarConformedBytes_Type = Counter64
_QtechCBQoSIfCarConformedBytes_Object = MibTableColumn
qtechCBQoSIfCarConformedBytes = _QtechCBQoSIfCarConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 5),
    _QtechCBQoSIfCarConformedBytes_Type()
)
qtechCBQoSIfCarConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarConformedBytes.setStatus("current")
_QtechCBQoSIfCarExceededPackets_Type = Counter64
_QtechCBQoSIfCarExceededPackets_Object = MibTableColumn
qtechCBQoSIfCarExceededPackets = _QtechCBQoSIfCarExceededPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 6),
    _QtechCBQoSIfCarExceededPackets_Type()
)
qtechCBQoSIfCarExceededPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarExceededPackets.setStatus("current")
_QtechCBQoSIfCarExceededBytes_Type = Counter64
_QtechCBQoSIfCarExceededBytes_Object = MibTableColumn
qtechCBQoSIfCarExceededBytes = _QtechCBQoSIfCarExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 7),
    _QtechCBQoSIfCarExceededBytes_Type()
)
qtechCBQoSIfCarExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarExceededBytes.setStatus("current")
_QtechCBQoSIfCarViolatedPackets_Type = Counter64
_QtechCBQoSIfCarViolatedPackets_Object = MibTableColumn
qtechCBQoSIfCarViolatedPackets = _QtechCBQoSIfCarViolatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 8),
    _QtechCBQoSIfCarViolatedPackets_Type()
)
qtechCBQoSIfCarViolatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarViolatedPackets.setStatus("current")
_QtechCBQoSIfCarViolatedBytes_Type = Counter64
_QtechCBQoSIfCarViolatedBytes_Object = MibTableColumn
qtechCBQoSIfCarViolatedBytes = _QtechCBQoSIfCarViolatedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 3, 1, 9),
    _QtechCBQoSIfCarViolatedBytes_Type()
)
qtechCBQoSIfCarViolatedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfCarViolatedBytes.setStatus("current")
_QtechCBQoSIfRemarkRunInfoTable_Object = MibTable
qtechCBQoSIfRemarkRunInfoTable = _QtechCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkRunInfoTable.setStatus("current")
_QtechCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
qtechCBQoSIfRemarkRunInfoEntry = _QtechCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4, 1)
)
qtechCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfRemarkIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfRemarkPolicyDirection"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfRemarkClassIndex"),
)
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkRunInfoEntry.setStatus("current")
_QtechCBQoSIfRemarkIfIndex_Type = Integer32
_QtechCBQoSIfRemarkIfIndex_Object = MibTableColumn
qtechCBQoSIfRemarkIfIndex = _QtechCBQoSIfRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4, 1, 1),
    _QtechCBQoSIfRemarkIfIndex_Type()
)
qtechCBQoSIfRemarkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkIfIndex.setStatus("current")


class _QtechCBQoSIfRemarkPolicyDirection_Type(Integer32):
    """Custom type qtechCBQoSIfRemarkPolicyDirection based on Integer32"""
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


_QtechCBQoSIfRemarkPolicyDirection_Type.__name__ = "Integer32"
_QtechCBQoSIfRemarkPolicyDirection_Object = MibTableColumn
qtechCBQoSIfRemarkPolicyDirection = _QtechCBQoSIfRemarkPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4, 1, 2),
    _QtechCBQoSIfRemarkPolicyDirection_Type()
)
qtechCBQoSIfRemarkPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkPolicyDirection.setStatus("current")
_QtechCBQoSIfRemarkClassIndex_Type = Integer32
_QtechCBQoSIfRemarkClassIndex_Object = MibTableColumn
qtechCBQoSIfRemarkClassIndex = _QtechCBQoSIfRemarkClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4, 1, 3),
    _QtechCBQoSIfRemarkClassIndex_Type()
)
qtechCBQoSIfRemarkClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkClassIndex.setStatus("current")
_QtechCBQoSIfRemarkedPackets_Type = Counter64
_QtechCBQoSIfRemarkedPackets_Object = MibTableColumn
qtechCBQoSIfRemarkedPackets = _QtechCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4, 1, 4),
    _QtechCBQoSIfRemarkedPackets_Type()
)
qtechCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkedPackets.setStatus("current")
_QtechCBQoSIfRemarkedBytes_Type = Counter64
_QtechCBQoSIfRemarkedBytes_Object = MibTableColumn
qtechCBQoSIfRemarkedBytes = _QtechCBQoSIfRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 4, 1, 5),
    _QtechCBQoSIfRemarkedBytes_Type()
)
qtechCBQoSIfRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfRemarkedBytes.setStatus("current")
_QtechCBQoSIfQueueRunInfoTable_Object = MibTable
qtechCBQoSIfQueueRunInfoTable = _QtechCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5)
)
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueRunInfoTable.setStatus("current")
_QtechCBQoSIfQueueRunInfoEntry_Object = MibTableRow
qtechCBQoSIfQueueRunInfoEntry = _QtechCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1)
)
qtechCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfQueueIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfQueuePolicyDirection"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfQueueClassIndex"),
)
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueRunInfoEntry.setStatus("current")
_QtechCBQoSIfQueueIfIndex_Type = Integer32
_QtechCBQoSIfQueueIfIndex_Object = MibTableColumn
qtechCBQoSIfQueueIfIndex = _QtechCBQoSIfQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 1),
    _QtechCBQoSIfQueueIfIndex_Type()
)
qtechCBQoSIfQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueIfIndex.setStatus("current")


class _QtechCBQoSIfQueuePolicyDirection_Type(Integer32):
    """Custom type qtechCBQoSIfQueuePolicyDirection based on Integer32"""
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


_QtechCBQoSIfQueuePolicyDirection_Type.__name__ = "Integer32"
_QtechCBQoSIfQueuePolicyDirection_Object = MibTableColumn
qtechCBQoSIfQueuePolicyDirection = _QtechCBQoSIfQueuePolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 2),
    _QtechCBQoSIfQueuePolicyDirection_Type()
)
qtechCBQoSIfQueuePolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueuePolicyDirection.setStatus("current")
_QtechCBQoSIfQueueClassIndex_Type = Integer32
_QtechCBQoSIfQueueClassIndex_Object = MibTableColumn
qtechCBQoSIfQueueClassIndex = _QtechCBQoSIfQueueClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 3),
    _QtechCBQoSIfQueueClassIndex_Type()
)
qtechCBQoSIfQueueClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueClassIndex.setStatus("current")
_QtechCBQoSIfQueueMatchedPackets_Type = Counter64
_QtechCBQoSIfQueueMatchedPackets_Object = MibTableColumn
qtechCBQoSIfQueueMatchedPackets = _QtechCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 4),
    _QtechCBQoSIfQueueMatchedPackets_Type()
)
qtechCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueMatchedPackets.setStatus("current")
_QtechCBQoSIfQueueMatchedBytes_Type = Counter64
_QtechCBQoSIfQueueMatchedBytes_Object = MibTableColumn
qtechCBQoSIfQueueMatchedBytes = _QtechCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 5),
    _QtechCBQoSIfQueueMatchedBytes_Type()
)
qtechCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueMatchedBytes.setStatus("current")
_QtechCBQoSIfQueueEnqueuedPackets_Type = Counter64
_QtechCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
qtechCBQoSIfQueueEnqueuedPackets = _QtechCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 6),
    _QtechCBQoSIfQueueEnqueuedPackets_Type()
)
qtechCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueEnqueuedPackets.setStatus("current")
_QtechCBQoSIfQueueEnqueuedBytes_Type = Counter64
_QtechCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
qtechCBQoSIfQueueEnqueuedBytes = _QtechCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 7),
    _QtechCBQoSIfQueueEnqueuedBytes_Type()
)
qtechCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueEnqueuedBytes.setStatus("current")
_QtechCBQoSIfQueueDiscardedPackets_Type = Counter64
_QtechCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
qtechCBQoSIfQueueDiscardedPackets = _QtechCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 8),
    _QtechCBQoSIfQueueDiscardedPackets_Type()
)
qtechCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueDiscardedPackets.setStatus("current")
_QtechCBQoSIfQueueDiscardedBytes_Type = Counter64
_QtechCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
qtechCBQoSIfQueueDiscardedBytes = _QtechCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 5, 1, 9),
    _QtechCBQoSIfQueueDiscardedBytes_Type()
)
qtechCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfQueueDiscardedBytes.setStatus("current")
_QtechCBQoSIfWredRunInfoTable_Object = MibTable
qtechCBQoSIfWredRunInfoTable = _QtechCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6)
)
if mibBuilder.loadTexts:
    qtechCBQoSIfWredRunInfoTable.setStatus("current")
_QtechCBQoSIfWredRunInfoEntry_Object = MibTableRow
qtechCBQoSIfWredRunInfoEntry = _QtechCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6, 1)
)
qtechCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfWredIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfWredClassIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechCBQoSIfWredClassValue"),
)
if mibBuilder.loadTexts:
    qtechCBQoSIfWredRunInfoEntry.setStatus("current")
_QtechCBQoSIfWredIfIndex_Type = Integer32
_QtechCBQoSIfWredIfIndex_Object = MibTableColumn
qtechCBQoSIfWredIfIndex = _QtechCBQoSIfWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6, 1, 1),
    _QtechCBQoSIfWredIfIndex_Type()
)
qtechCBQoSIfWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfWredIfIndex.setStatus("current")
_QtechCBQoSIfWredClassIndex_Type = Integer32
_QtechCBQoSIfWredClassIndex_Object = MibTableColumn
qtechCBQoSIfWredClassIndex = _QtechCBQoSIfWredClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6, 1, 2),
    _QtechCBQoSIfWredClassIndex_Type()
)
qtechCBQoSIfWredClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfWredClassIndex.setStatus("current")
_QtechCBQoSIfWredClassValue_Type = Integer32
_QtechCBQoSIfWredClassValue_Object = MibTableColumn
qtechCBQoSIfWredClassValue = _QtechCBQoSIfWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6, 1, 3),
    _QtechCBQoSIfWredClassValue_Type()
)
qtechCBQoSIfWredClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfWredClassValue.setStatus("current")
_QtechCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_QtechCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
qtechCBQoSIfWredRandomDiscardedPackets = _QtechCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6, 1, 4),
    _QtechCBQoSIfWredRandomDiscardedPackets_Type()
)
qtechCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_QtechCBQoSIfWredTailDiscardedPackets_Type = Counter64
_QtechCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
qtechCBQoSIfWredTailDiscardedPackets = _QtechCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 1, 1, 6, 1, 5),
    _QtechCBQoSIfWredTailDiscardedPackets_Type()
)
qtechCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCBQoSIfWredTailDiscardedPackets.setStatus("current")
_QtechIfQoSMIBObjects_ObjectIdentity = ObjectIdentity
qtechIfQoSMIBObjects = _QtechIfQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2)
)
_QtechIfQosPQRunInfoTable_Object = MibTable
qtechIfQosPQRunInfoTable = _QtechIfQosPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1)
)
if mibBuilder.loadTexts:
    qtechIfQosPQRunInfoTable.setStatus("current")
_QtechIfQosPQRunInfoEntry_Object = MibTableRow
qtechIfQosPQRunInfoEntry = _QtechIfQosPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1)
)
qtechIfQosPQRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosPQIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIfQosPQRunInfoEntry.setStatus("current")
_QtechIfQosPQIfIndex_Type = Integer32
_QtechIfQosPQIfIndex_Object = MibTableColumn
qtechIfQosPQIfIndex = _QtechIfQosPQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 1),
    _QtechIfQosPQIfIndex_Type()
)
qtechIfQosPQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQIfIndex.setStatus("current")


class _QtechIfQosPQListNum_Type(Integer32):
    """Custom type qtechIfQosPQListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QtechIfQosPQListNum_Type.__name__ = "Integer32"
_QtechIfQosPQListNum_Object = MibTableColumn
qtechIfQosPQListNum = _QtechIfQosPQListNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 2),
    _QtechIfQosPQListNum_Type()
)
qtechIfQosPQListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQListNum.setStatus("current")
_QtechIfQosPQIfName_Type = OctetString
_QtechIfQosPQIfName_Object = MibTableColumn
qtechIfQosPQIfName = _QtechIfQosPQIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 3),
    _QtechIfQosPQIfName_Type()
)
qtechIfQosPQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQIfName.setStatus("current")


class _QtechIfQosPQHighPkt_Type(Integer32):
    """Custom type qtechIfQosPQHighPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosPQHighPkt_Type.__name__ = "Integer32"
_QtechIfQosPQHighPkt_Object = MibTableColumn
qtechIfQosPQHighPkt = _QtechIfQosPQHighPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 4),
    _QtechIfQosPQHighPkt_Type()
)
qtechIfQosPQHighPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQHighPkt.setStatus("current")
_QtechIfQosPQHighDiscard_Type = Counter32
_QtechIfQosPQHighDiscard_Object = MibTableColumn
qtechIfQosPQHighDiscard = _QtechIfQosPQHighDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 5),
    _QtechIfQosPQHighDiscard_Type()
)
qtechIfQosPQHighDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQHighDiscard.setStatus("current")


class _QtechIfQosPQHighMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosPQHighMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosPQHighMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosPQHighMaxQueLen_Object = MibTableColumn
qtechIfQosPQHighMaxQueLen = _QtechIfQosPQHighMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 6),
    _QtechIfQosPQHighMaxQueLen_Type()
)
qtechIfQosPQHighMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQHighMaxQueLen.setStatus("current")


class _QtechIfQosPQMiddlePkt_Type(Integer32):
    """Custom type qtechIfQosPQMiddlePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosPQMiddlePkt_Type.__name__ = "Integer32"
_QtechIfQosPQMiddlePkt_Object = MibTableColumn
qtechIfQosPQMiddlePkt = _QtechIfQosPQMiddlePkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 7),
    _QtechIfQosPQMiddlePkt_Type()
)
qtechIfQosPQMiddlePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQMiddlePkt.setStatus("current")
_QtechIfQosPQMiddleDiscard_Type = Counter32
_QtechIfQosPQMiddleDiscard_Object = MibTableColumn
qtechIfQosPQMiddleDiscard = _QtechIfQosPQMiddleDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 8),
    _QtechIfQosPQMiddleDiscard_Type()
)
qtechIfQosPQMiddleDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQMiddleDiscard.setStatus("current")


class _QtechIfQosPQMiddleMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosPQMiddleMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosPQMiddleMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosPQMiddleMaxQueLen_Object = MibTableColumn
qtechIfQosPQMiddleMaxQueLen = _QtechIfQosPQMiddleMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 9),
    _QtechIfQosPQMiddleMaxQueLen_Type()
)
qtechIfQosPQMiddleMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQMiddleMaxQueLen.setStatus("current")


class _QtechIfQosPQNormalPkt_Type(Integer32):
    """Custom type qtechIfQosPQNormalPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosPQNormalPkt_Type.__name__ = "Integer32"
_QtechIfQosPQNormalPkt_Object = MibTableColumn
qtechIfQosPQNormalPkt = _QtechIfQosPQNormalPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 10),
    _QtechIfQosPQNormalPkt_Type()
)
qtechIfQosPQNormalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQNormalPkt.setStatus("current")
_QtechIfQosPQNormalDiscard_Type = Counter32
_QtechIfQosPQNormalDiscard_Object = MibTableColumn
qtechIfQosPQNormalDiscard = _QtechIfQosPQNormalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 11),
    _QtechIfQosPQNormalDiscard_Type()
)
qtechIfQosPQNormalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQNormalDiscard.setStatus("current")


class _QtechIfQosPQNormalMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosPQNormalMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosPQNormalMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosPQNormalMaxQueLen_Object = MibTableColumn
qtechIfQosPQNormalMaxQueLen = _QtechIfQosPQNormalMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 12),
    _QtechIfQosPQNormalMaxQueLen_Type()
)
qtechIfQosPQNormalMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQNormalMaxQueLen.setStatus("current")


class _QtechIfQosPQLowPkt_Type(Integer32):
    """Custom type qtechIfQosPQLowPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosPQLowPkt_Type.__name__ = "Integer32"
_QtechIfQosPQLowPkt_Object = MibTableColumn
qtechIfQosPQLowPkt = _QtechIfQosPQLowPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 13),
    _QtechIfQosPQLowPkt_Type()
)
qtechIfQosPQLowPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQLowPkt.setStatus("current")
_QtechIfQosPQLowDiscard_Type = Counter32
_QtechIfQosPQLowDiscard_Object = MibTableColumn
qtechIfQosPQLowDiscard = _QtechIfQosPQLowDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 14),
    _QtechIfQosPQLowDiscard_Type()
)
qtechIfQosPQLowDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQLowDiscard.setStatus("current")


class _QtechIfQosPQLowMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosPQLowMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosPQLowMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosPQLowMaxQueLen_Object = MibTableColumn
qtechIfQosPQLowMaxQueLen = _QtechIfQosPQLowMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 1, 1, 15),
    _QtechIfQosPQLowMaxQueLen_Type()
)
qtechIfQosPQLowMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosPQLowMaxQueLen.setStatus("current")
_QtechIfQosCQRunInfoTable_Object = MibTable
qtechIfQosCQRunInfoTable = _QtechIfQosCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2)
)
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoTable.setStatus("current")
_QtechIfQosCQRunInfoEntry_Object = MibTableRow
qtechIfQosCQRunInfoEntry = _QtechIfQosCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1)
)
qtechIfQosCQRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosCQRunInfoIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosCQRunInfoQueNum"),
)
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoEntry.setStatus("current")
_QtechIfQosCQRunInfoIfIndex_Type = Integer32
_QtechIfQosCQRunInfoIfIndex_Object = MibTableColumn
qtechIfQosCQRunInfoIfIndex = _QtechIfQosCQRunInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1, 1),
    _QtechIfQosCQRunInfoIfIndex_Type()
)
qtechIfQosCQRunInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoIfIndex.setStatus("current")


class _QtechIfQosCQRunInfoQueNum_Type(Integer32):
    """Custom type qtechIfQosCQRunInfoQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QtechIfQosCQRunInfoQueNum_Type.__name__ = "Integer32"
_QtechIfQosCQRunInfoQueNum_Object = MibTableColumn
qtechIfQosCQRunInfoQueNum = _QtechIfQosCQRunInfoQueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1, 2),
    _QtechIfQosCQRunInfoQueNum_Type()
)
qtechIfQosCQRunInfoQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoQueNum.setStatus("current")
_QtechIfQosCQRunInfoIfName_Type = OctetString
_QtechIfQosCQRunInfoIfName_Object = MibTableColumn
qtechIfQosCQRunInfoIfName = _QtechIfQosCQRunInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1, 3),
    _QtechIfQosCQRunInfoIfName_Type()
)
qtechIfQosCQRunInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoIfName.setStatus("current")


class _QtechIfQosCQRunInfoQuePkt_Type(Integer32):
    """Custom type qtechIfQosCQRunInfoQuePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosCQRunInfoQuePkt_Type.__name__ = "Integer32"
_QtechIfQosCQRunInfoQuePkt_Object = MibTableColumn
qtechIfQosCQRunInfoQuePkt = _QtechIfQosCQRunInfoQuePkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1, 4),
    _QtechIfQosCQRunInfoQuePkt_Type()
)
qtechIfQosCQRunInfoQuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoQuePkt.setStatus("current")
_QtechIfQosCQRunInfoQueDiscard_Type = Counter32
_QtechIfQosCQRunInfoQueDiscard_Object = MibTableColumn
qtechIfQosCQRunInfoQueDiscard = _QtechIfQosCQRunInfoQueDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1, 5),
    _QtechIfQosCQRunInfoQueDiscard_Type()
)
qtechIfQosCQRunInfoQueDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoQueDiscard.setStatus("current")


class _QtechIfQosCQRunInfoMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosCQRunInfoMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosCQRunInfoMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosCQRunInfoMaxQueLen_Object = MibTableColumn
qtechIfQosCQRunInfoMaxQueLen = _QtechIfQosCQRunInfoMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 2, 1, 6),
    _QtechIfQosCQRunInfoMaxQueLen_Type()
)
qtechIfQosCQRunInfoMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCQRunInfoMaxQueLen.setStatus("current")
_QtechIfQosWFQRunInfoTable_Object = MibTable
qtechIfQosWFQRunInfoTable = _QtechIfQosWFQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3)
)
if mibBuilder.loadTexts:
    qtechIfQosWFQRunInfoTable.setStatus("current")
_QtechIfQosWFQRunInfoEntry_Object = MibTableRow
qtechIfQosWFQRunInfoEntry = _QtechIfQosWFQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1)
)
qtechIfQosWFQRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosWFQIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIfQosWFQRunInfoEntry.setStatus("current")
_QtechIfQosWFQIfIndex_Type = Integer32
_QtechIfQosWFQIfIndex_Object = MibTableColumn
qtechIfQosWFQIfIndex = _QtechIfQosWFQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 1),
    _QtechIfQosWFQIfIndex_Type()
)
qtechIfQosWFQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQIfIndex.setStatus("current")
_QtechIfQosWFQIfName_Type = OctetString
_QtechIfQosWFQIfName_Object = MibTableColumn
qtechIfQosWFQIfName = _QtechIfQosWFQIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 2),
    _QtechIfQosWFQIfName_Type()
)
qtechIfQosWFQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQIfName.setStatus("current")


class _QtechIfQosWFQMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosWFQMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosWFQMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosWFQMaxQueLen_Object = MibTableColumn
qtechIfQosWFQMaxQueLen = _QtechIfQosWFQMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 3),
    _QtechIfQosWFQMaxQueLen_Type()
)
qtechIfQosWFQMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQMaxQueLen.setStatus("current")


class _QtechIfQosWFQTotalQueNum_Type(Integer32):
    """Custom type qtechIfQosWFQTotalQueNum based on Integer32"""
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


_QtechIfQosWFQTotalQueNum_Type.__name__ = "Integer32"
_QtechIfQosWFQTotalQueNum_Object = MibTableColumn
qtechIfQosWFQTotalQueNum = _QtechIfQosWFQTotalQueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 4),
    _QtechIfQosWFQTotalQueNum_Type()
)
qtechIfQosWFQTotalQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQTotalQueNum.setStatus("current")
_QtechIfQosWFQCurQueLen_Type = Integer32
_QtechIfQosWFQCurQueLen_Object = MibTableColumn
qtechIfQosWFQCurQueLen = _QtechIfQosWFQCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 5),
    _QtechIfQosWFQCurQueLen_Type()
)
qtechIfQosWFQCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQCurQueLen.setStatus("current")
_QtechIfQosWFQTotalDiscard_Type = Counter32
_QtechIfQosWFQTotalDiscard_Object = MibTableColumn
qtechIfQosWFQTotalDiscard = _QtechIfQosWFQTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 6),
    _QtechIfQosWFQTotalDiscard_Type()
)
qtechIfQosWFQTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQTotalDiscard.setStatus("current")


class _QtechIfQosWFQActiveQueNum_Type(Integer32):
    """Custom type qtechIfQosWFQActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosWFQActiveQueNum_Type.__name__ = "Integer32"
_QtechIfQosWFQActiveQueNum_Object = MibTableColumn
qtechIfQosWFQActiveQueNum = _QtechIfQosWFQActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 7),
    _QtechIfQosWFQActiveQueNum_Type()
)
qtechIfQosWFQActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQActiveQueNum.setStatus("current")


class _QtechIfQosWFQMaxActiveQueNum_Type(Integer32):
    """Custom type qtechIfQosWFQMaxActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechIfQosWFQMaxActiveQueNum_Type.__name__ = "Integer32"
_QtechIfQosWFQMaxActiveQueNum_Object = MibTableColumn
qtechIfQosWFQMaxActiveQueNum = _QtechIfQosWFQMaxActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 3, 1, 8),
    _QtechIfQosWFQMaxActiveQueNum_Type()
)
qtechIfQosWFQMaxActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWFQMaxActiveQueNum.setStatus("current")
_QtechIfQosWredRunInfoTable_Object = MibTable
qtechIfQosWredRunInfoTable = _QtechIfQosWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 4)
)
if mibBuilder.loadTexts:
    qtechIfQosWredRunInfoTable.setStatus("current")
_QtechIfQosWredRunInfoEntry_Object = MibTableRow
qtechIfQosWredRunInfoEntry = _QtechIfQosWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 4, 1)
)
qtechIfQosWredRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosWredIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosWredValue"),
)
if mibBuilder.loadTexts:
    qtechIfQosWredRunInfoEntry.setStatus("current")
_QtechIfQosWredIfIndex_Type = Integer32
_QtechIfQosWredIfIndex_Object = MibTableColumn
qtechIfQosWredIfIndex = _QtechIfQosWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 4, 1, 1),
    _QtechIfQosWredIfIndex_Type()
)
qtechIfQosWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWredIfIndex.setStatus("current")
_QtechIfQosWredValue_Type = Integer32
_QtechIfQosWredValue_Object = MibTableColumn
qtechIfQosWredValue = _QtechIfQosWredValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 4, 1, 2),
    _QtechIfQosWredValue_Type()
)
qtechIfQosWredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWredValue.setStatus("current")
_QtechIfQosWredRandomDiscardedPackets_Type = Counter64
_QtechIfQosWredRandomDiscardedPackets_Object = MibTableColumn
qtechIfQosWredRandomDiscardedPackets = _QtechIfQosWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 4, 1, 3),
    _QtechIfQosWredRandomDiscardedPackets_Type()
)
qtechIfQosWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWredRandomDiscardedPackets.setStatus("current")
_QtechIfQosWredTailDiscardedPackets_Type = Counter64
_QtechIfQosWredTailDiscardedPackets_Object = MibTableColumn
qtechIfQosWredTailDiscardedPackets = _QtechIfQosWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 4, 1, 4),
    _QtechIfQosWredTailDiscardedPackets_Type()
)
qtechIfQosWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosWredTailDiscardedPackets.setStatus("current")
_QtechIfQosCARTable_Object = MibTable
qtechIfQosCARTable = _QtechIfQosCARTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5)
)
if mibBuilder.loadTexts:
    qtechIfQosCARTable.setStatus("current")
_QtechIfQosCAREntry_Object = MibTableRow
qtechIfQosCAREntry = _QtechIfQosCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1)
)
qtechIfQosCAREntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosCARIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosCARPktDirection"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosCARindex"),
)
if mibBuilder.loadTexts:
    qtechIfQosCAREntry.setStatus("current")
_QtechIfQosCARIfIndex_Type = Integer32
_QtechIfQosCARIfIndex_Object = MibTableColumn
qtechIfQosCARIfIndex = _QtechIfQosCARIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 1),
    _QtechIfQosCARIfIndex_Type()
)
qtechIfQosCARIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARIfIndex.setStatus("current")
_QtechIfQosCARIfName_Type = OctetString
_QtechIfQosCARIfName_Object = MibTableColumn
qtechIfQosCARIfName = _QtechIfQosCARIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 2),
    _QtechIfQosCARIfName_Type()
)
qtechIfQosCARIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARIfName.setStatus("current")


class _QtechIfQosCARPktDirection_Type(Integer32):
    """Custom type qtechIfQosCARPktDirection based on Integer32"""
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


_QtechIfQosCARPktDirection_Type.__name__ = "Integer32"
_QtechIfQosCARPktDirection_Object = MibTableColumn
qtechIfQosCARPktDirection = _QtechIfQosCARPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 3),
    _QtechIfQosCARPktDirection_Type()
)
qtechIfQosCARPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARPktDirection.setStatus("current")


class _QtechIfQosCARType_Type(Integer32):
    """Custom type qtechIfQosCARType based on Integer32"""
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


_QtechIfQosCARType_Type.__name__ = "Integer32"
_QtechIfQosCARType_Object = MibTableColumn
qtechIfQosCARType = _QtechIfQosCARType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 4),
    _QtechIfQosCARType_Type()
)
qtechIfQosCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARType.setStatus("current")
_QtechIfQosCARListNum_Type = Integer32
_QtechIfQosCARListNum_Object = MibTableColumn
qtechIfQosCARListNum = _QtechIfQosCARListNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 5),
    _QtechIfQosCARListNum_Type()
)
qtechIfQosCARListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARListNum.setStatus("current")
_QtechIfQosCARindex_Type = Integer32
_QtechIfQosCARindex_Object = MibTableColumn
qtechIfQosCARindex = _QtechIfQosCARindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 6),
    _QtechIfQosCARindex_Type()
)
qtechIfQosCARindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARindex.setStatus("current")


class _QtechIfQosCARCIR_Type(Integer32):
    """Custom type qtechIfQosCARCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_QtechIfQosCARCIR_Type.__name__ = "Integer32"
_QtechIfQosCARCIR_Object = MibTableColumn
qtechIfQosCARCIR = _QtechIfQosCARCIR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 7),
    _QtechIfQosCARCIR_Type()
)
qtechIfQosCARCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARCIR.setStatus("current")


class _QtechIfQosCARBurstSize_Type(Integer32):
    """Custom type qtechIfQosCARBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_QtechIfQosCARBurstSize_Type.__name__ = "Integer32"
_QtechIfQosCARBurstSize_Object = MibTableColumn
qtechIfQosCARBurstSize = _QtechIfQosCARBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 8),
    _QtechIfQosCARBurstSize_Type()
)
qtechIfQosCARBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARBurstSize.setStatus("current")


class _QtechIfQosCARExcessBurstSize_Type(Integer32):
    """Custom type qtechIfQosCARExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_QtechIfQosCARExcessBurstSize_Type.__name__ = "Integer32"
_QtechIfQosCARExcessBurstSize_Object = MibTableColumn
qtechIfQosCARExcessBurstSize = _QtechIfQosCARExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 9),
    _QtechIfQosCARExcessBurstSize_Type()
)
qtechIfQosCARExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARExcessBurstSize.setStatus("current")


class _QtechIfQosCARConformAction_Type(Integer32):
    """Custom type qtechIfQosCARConformAction based on Integer32"""
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


_QtechIfQosCARConformAction_Type.__name__ = "Integer32"
_QtechIfQosCARConformAction_Object = MibTableColumn
qtechIfQosCARConformAction = _QtechIfQosCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 10),
    _QtechIfQosCARConformAction_Type()
)
qtechIfQosCARConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARConformAction.setStatus("current")


class _QtechIfQosCARExceedAction_Type(Integer32):
    """Custom type qtechIfQosCARExceedAction based on Integer32"""
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


_QtechIfQosCARExceedAction_Type.__name__ = "Integer32"
_QtechIfQosCARExceedAction_Object = MibTableColumn
qtechIfQosCARExceedAction = _QtechIfQosCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 11),
    _QtechIfQosCARExceedAction_Type()
)
qtechIfQosCARExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARExceedAction.setStatus("current")


class _QtechIfQosCARConformNewPrec_Type(Integer32):
    """Custom type qtechIfQosCARConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechIfQosCARConformNewPrec_Type.__name__ = "Integer32"
_QtechIfQosCARConformNewPrec_Object = MibTableColumn
qtechIfQosCARConformNewPrec = _QtechIfQosCARConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 12),
    _QtechIfQosCARConformNewPrec_Type()
)
qtechIfQosCARConformNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARConformNewPrec.setStatus("current")


class _QtechIfQosCARExceedNewPrec_Type(Integer32):
    """Custom type qtechIfQosCARExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechIfQosCARExceedNewPrec_Type.__name__ = "Integer32"
_QtechIfQosCARExceedNewPrec_Object = MibTableColumn
qtechIfQosCARExceedNewPrec = _QtechIfQosCARExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 13),
    _QtechIfQosCARExceedNewPrec_Type()
)
qtechIfQosCARExceedNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARExceedNewPrec.setStatus("current")
_QtechIfQosCARConformPkt_Type = Counter32
_QtechIfQosCARConformPkt_Object = MibTableColumn
qtechIfQosCARConformPkt = _QtechIfQosCARConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 14),
    _QtechIfQosCARConformPkt_Type()
)
qtechIfQosCARConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARConformPkt.setStatus("current")
_QtechIfQosCARConformByte_Type = Counter32
_QtechIfQosCARConformByte_Object = MibTableColumn
qtechIfQosCARConformByte = _QtechIfQosCARConformByte_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 15),
    _QtechIfQosCARConformByte_Type()
)
qtechIfQosCARConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARConformByte.setStatus("current")
_QtechIfQosCARExceedPkt_Type = Counter32
_QtechIfQosCARExceedPkt_Object = MibTableColumn
qtechIfQosCARExceedPkt = _QtechIfQosCARExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 16),
    _QtechIfQosCARExceedPkt_Type()
)
qtechIfQosCARExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARExceedPkt.setStatus("current")
_QtechIfQosCARExceedByte_Type = Counter32
_QtechIfQosCARExceedByte_Object = MibTableColumn
qtechIfQosCARExceedByte = _QtechIfQosCARExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 5, 1, 17),
    _QtechIfQosCARExceedByte_Type()
)
qtechIfQosCARExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosCARExceedByte.setStatus("current")
_QtechIfQosGTSTable_Object = MibTable
qtechIfQosGTSTable = _QtechIfQosGTSTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6)
)
if mibBuilder.loadTexts:
    qtechIfQosGTSTable.setStatus("current")
_QtechIfQosGTSEntry_Object = MibTableRow
qtechIfQosGTSEntry = _QtechIfQosGTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1)
)
qtechIfQosGTSEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosGTSIfIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosGTSType"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosGTSACLNum"),
)
if mibBuilder.loadTexts:
    qtechIfQosGTSEntry.setStatus("current")
_QtechIfQosGTSIfIndex_Type = Integer32
_QtechIfQosGTSIfIndex_Object = MibTableColumn
qtechIfQosGTSIfIndex = _QtechIfQosGTSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 1),
    _QtechIfQosGTSIfIndex_Type()
)
qtechIfQosGTSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSIfIndex.setStatus("current")
_QtechIfQosGTSIfName_Type = OctetString
_QtechIfQosGTSIfName_Object = MibTableColumn
qtechIfQosGTSIfName = _QtechIfQosGTSIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 2),
    _QtechIfQosGTSIfName_Type()
)
qtechIfQosGTSIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSIfName.setStatus("current")


class _QtechIfQosGTSType_Type(Integer32):
    """Custom type qtechIfQosGTSType based on Integer32"""
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


_QtechIfQosGTSType_Type.__name__ = "Integer32"
_QtechIfQosGTSType_Object = MibTableColumn
qtechIfQosGTSType = _QtechIfQosGTSType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 3),
    _QtechIfQosGTSType_Type()
)
qtechIfQosGTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSType.setStatus("current")


class _QtechIfQosGTSACLNum_Type(Integer32):
    """Custom type qtechIfQosGTSACLNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_QtechIfQosGTSACLNum_Type.__name__ = "Integer32"
_QtechIfQosGTSACLNum_Object = MibTableColumn
qtechIfQosGTSACLNum = _QtechIfQosGTSACLNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 4),
    _QtechIfQosGTSACLNum_Type()
)
qtechIfQosGTSACLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSACLNum.setStatus("current")


class _QtechIfQosGTSCIR_Type(Integer32):
    """Custom type qtechIfQosGTSCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_QtechIfQosGTSCIR_Type.__name__ = "Integer32"
_QtechIfQosGTSCIR_Object = MibTableColumn
qtechIfQosGTSCIR = _QtechIfQosGTSCIR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 5),
    _QtechIfQosGTSCIR_Type()
)
qtechIfQosGTSCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSCIR.setStatus("current")


class _QtechIfQosGTSBurstSize_Type(Integer32):
    """Custom type qtechIfQosGTSBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_QtechIfQosGTSBurstSize_Type.__name__ = "Integer32"
_QtechIfQosGTSBurstSize_Object = MibTableColumn
qtechIfQosGTSBurstSize = _QtechIfQosGTSBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 6),
    _QtechIfQosGTSBurstSize_Type()
)
qtechIfQosGTSBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSBurstSize.setStatus("current")


class _QtechIfQosGTSExcessBurstSize_Type(Integer32):
    """Custom type qtechIfQosGTSExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_QtechIfQosGTSExcessBurstSize_Type.__name__ = "Integer32"
_QtechIfQosGTSExcessBurstSize_Object = MibTableColumn
qtechIfQosGTSExcessBurstSize = _QtechIfQosGTSExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 7),
    _QtechIfQosGTSExcessBurstSize_Type()
)
qtechIfQosGTSExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSExcessBurstSize.setStatus("current")


class _QtechIfQosGTSMaxQueLen_Type(Integer32):
    """Custom type qtechIfQosGTSMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechIfQosGTSMaxQueLen_Type.__name__ = "Integer32"
_QtechIfQosGTSMaxQueLen_Object = MibTableColumn
qtechIfQosGTSMaxQueLen = _QtechIfQosGTSMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 8),
    _QtechIfQosGTSMaxQueLen_Type()
)
qtechIfQosGTSMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSMaxQueLen.setStatus("current")
_QtechIfQosGTSCurQueLen_Type = Integer32
_QtechIfQosGTSCurQueLen_Object = MibTableColumn
qtechIfQosGTSCurQueLen = _QtechIfQosGTSCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 9),
    _QtechIfQosGTSCurQueLen_Type()
)
qtechIfQosGTSCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSCurQueLen.setStatus("current")
_QtechIfQosGTSPassPkt_Type = Counter32
_QtechIfQosGTSPassPkt_Object = MibTableColumn
qtechIfQosGTSPassPkt = _QtechIfQosGTSPassPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 10),
    _QtechIfQosGTSPassPkt_Type()
)
qtechIfQosGTSPassPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSPassPkt.setStatus("current")
_QtechIfQosGTSPassByte_Type = Counter32
_QtechIfQosGTSPassByte_Object = MibTableColumn
qtechIfQosGTSPassByte = _QtechIfQosGTSPassByte_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 11),
    _QtechIfQosGTSPassByte_Type()
)
qtechIfQosGTSPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSPassByte.setStatus("current")
_QtechIfQosGTSDiscardPkt_Type = Counter32
_QtechIfQosGTSDiscardPkt_Object = MibTableColumn
qtechIfQosGTSDiscardPkt = _QtechIfQosGTSDiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 12),
    _QtechIfQosGTSDiscardPkt_Type()
)
qtechIfQosGTSDiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSDiscardPkt.setStatus("current")
_QtechIfQosGTSDiscardByte_Type = Counter32
_QtechIfQosGTSDiscardByte_Object = MibTableColumn
qtechIfQosGTSDiscardByte = _QtechIfQosGTSDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 6, 1, 13),
    _QtechIfQosGTSDiscardByte_Type()
)
qtechIfQosGTSDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosGTSDiscardByte.setStatus("current")
_QtechIfQosRTPIfQueueRunInfoTable_Object = MibTable
qtechIfQosRTPIfQueueRunInfoTable = _QtechIfQosRTPIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7)
)
if mibBuilder.loadTexts:
    qtechIfQosRTPIfQueueRunInfoTable.setStatus("current")
_QtechIfQosRTPIfQueueRunInfoEntry_Object = MibTableRow
qtechIfQosRTPIfQueueRunInfoEntry = _QtechIfQosRTPIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7, 1)
)
qtechIfQosRTPIfQueueRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosRTPIfApplyIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIfQosRTPIfQueueRunInfoEntry.setStatus("current")
_QtechIfQosRTPIfApplyIfIndex_Type = Integer32
_QtechIfQosRTPIfApplyIfIndex_Object = MibTableColumn
qtechIfQosRTPIfApplyIfIndex = _QtechIfQosRTPIfApplyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7, 1, 1),
    _QtechIfQosRTPIfApplyIfIndex_Type()
)
qtechIfQosRTPIfApplyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosRTPIfApplyIfIndex.setStatus("current")
_QtechIfQosRTPIfQueueSize_Type = Counter32
_QtechIfQosRTPIfQueueSize_Object = MibTableColumn
qtechIfQosRTPIfQueueSize = _QtechIfQosRTPIfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7, 1, 2),
    _QtechIfQosRTPIfQueueSize_Type()
)
qtechIfQosRTPIfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosRTPIfQueueSize.setStatus("current")
_QtechIfQosRTPIfQueueMaxSize_Type = Counter32
_QtechIfQosRTPIfQueueMaxSize_Object = MibTableColumn
qtechIfQosRTPIfQueueMaxSize = _QtechIfQosRTPIfQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7, 1, 3),
    _QtechIfQosRTPIfQueueMaxSize_Type()
)
qtechIfQosRTPIfQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosRTPIfQueueMaxSize.setStatus("current")
_QtechIfQosRTPIfQueueOutputs_Type = Counter32
_QtechIfQosRTPIfQueueOutputs_Object = MibTableColumn
qtechIfQosRTPIfQueueOutputs = _QtechIfQosRTPIfQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7, 1, 4),
    _QtechIfQosRTPIfQueueOutputs_Type()
)
qtechIfQosRTPIfQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosRTPIfQueueOutputs.setStatus("current")
_QtechIfQosRTPIfQueueDiscards_Type = Counter32
_QtechIfQosRTPIfQueueDiscards_Object = MibTableColumn
qtechIfQosRTPIfQueueDiscards = _QtechIfQosRTPIfQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 7, 1, 5),
    _QtechIfQosRTPIfQueueDiscards_Type()
)
qtechIfQosRTPIfQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosRTPIfQueueDiscards.setStatus("current")
_QtechIfQosFlowLimitRunInfoTable_Object = MibTable
qtechIfQosFlowLimitRunInfoTable = _QtechIfQosFlowLimitRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8)
)
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitRunInfoTable.setStatus("current")
_QtechIfQosFlowLimitRunInfoEntry_Object = MibTableRow
qtechIfQosFlowLimitRunInfoEntry = _QtechIfQosFlowLimitRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1)
)
qtechIfQosFlowLimitRunInfoEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosFlowLimitLabelNum"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechIfQosFlowLimitPktDirection"),
)
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitRunInfoEntry.setStatus("current")


class _QtechIfQosFlowLimitLabelNum_Type(Integer32):
    """Custom type qtechIfQosFlowLimitLabelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QtechIfQosFlowLimitLabelNum_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitLabelNum_Object = MibTableColumn
qtechIfQosFlowLimitLabelNum = _QtechIfQosFlowLimitLabelNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 1),
    _QtechIfQosFlowLimitLabelNum_Type()
)
qtechIfQosFlowLimitLabelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitLabelNum.setStatus("current")


class _QtechIfQosFlowLimitPktDirection_Type(Integer32):
    """Custom type qtechIfQosFlowLimitPktDirection based on Integer32"""
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


_QtechIfQosFlowLimitPktDirection_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitPktDirection_Object = MibTableColumn
qtechIfQosFlowLimitPktDirection = _QtechIfQosFlowLimitPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 2),
    _QtechIfQosFlowLimitPktDirection_Type()
)
qtechIfQosFlowLimitPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitPktDirection.setStatus("current")


class _QtechIfQosFlowLimitCIR_Type(Integer32):
    """Custom type qtechIfQosFlowLimitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_QtechIfQosFlowLimitCIR_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitCIR_Object = MibTableColumn
qtechIfQosFlowLimitCIR = _QtechIfQosFlowLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 3),
    _QtechIfQosFlowLimitCIR_Type()
)
qtechIfQosFlowLimitCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitCIR.setStatus("current")


class _QtechIfQosFlowLimitBurstSize_Type(Integer32):
    """Custom type qtechIfQosFlowLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_QtechIfQosFlowLimitBurstSize_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitBurstSize_Object = MibTableColumn
qtechIfQosFlowLimitBurstSize = _QtechIfQosFlowLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 4),
    _QtechIfQosFlowLimitBurstSize_Type()
)
qtechIfQosFlowLimitBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitBurstSize.setStatus("current")


class _QtechIfQosFlowLimitExcessBurstSize_Type(Integer32):
    """Custom type qtechIfQosFlowLimitExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_QtechIfQosFlowLimitExcessBurstSize_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitExcessBurstSize_Object = MibTableColumn
qtechIfQosFlowLimitExcessBurstSize = _QtechIfQosFlowLimitExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 5),
    _QtechIfQosFlowLimitExcessBurstSize_Type()
)
qtechIfQosFlowLimitExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitExcessBurstSize.setStatus("current")


class _QtechIfQosFlowLimitConformAction_Type(Integer32):
    """Custom type qtechIfQosFlowLimitConformAction based on Integer32"""
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


_QtechIfQosFlowLimitConformAction_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitConformAction_Object = MibTableColumn
qtechIfQosFlowLimitConformAction = _QtechIfQosFlowLimitConformAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 6),
    _QtechIfQosFlowLimitConformAction_Type()
)
qtechIfQosFlowLimitConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitConformAction.setStatus("current")


class _QtechIfQosFlowLimitExceedAction_Type(Integer32):
    """Custom type qtechIfQosFlowLimitExceedAction based on Integer32"""
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


_QtechIfQosFlowLimitExceedAction_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitExceedAction_Object = MibTableColumn
qtechIfQosFlowLimitExceedAction = _QtechIfQosFlowLimitExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 7),
    _QtechIfQosFlowLimitExceedAction_Type()
)
qtechIfQosFlowLimitExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitExceedAction.setStatus("current")


class _QtechIfQosFlowLimitConformNewPrec_Type(Integer32):
    """Custom type qtechIfQosFlowLimitConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QtechIfQosFlowLimitConformNewPrec_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitConformNewPrec_Object = MibTableColumn
qtechIfQosFlowLimitConformNewPrec = _QtechIfQosFlowLimitConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 8),
    _QtechIfQosFlowLimitConformNewPrec_Type()
)
qtechIfQosFlowLimitConformNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitConformNewPrec.setStatus("current")


class _QtechIfQosFlowLimitExceedNewPrec_Type(Integer32):
    """Custom type qtechIfQosFlowLimitExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QtechIfQosFlowLimitExceedNewPrec_Type.__name__ = "Integer32"
_QtechIfQosFlowLimitExceedNewPrec_Object = MibTableColumn
qtechIfQosFlowLimitExceedNewPrec = _QtechIfQosFlowLimitExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 9),
    _QtechIfQosFlowLimitExceedNewPrec_Type()
)
qtechIfQosFlowLimitExceedNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitExceedNewPrec.setStatus("current")
_QtechIfQosFlowLimitConformPkt_Type = Counter32
_QtechIfQosFlowLimitConformPkt_Object = MibTableColumn
qtechIfQosFlowLimitConformPkt = _QtechIfQosFlowLimitConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 10),
    _QtechIfQosFlowLimitConformPkt_Type()
)
qtechIfQosFlowLimitConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitConformPkt.setStatus("current")
_QtechIfQosFlowLimitConformByte_Type = Counter32
_QtechIfQosFlowLimitConformByte_Object = MibTableColumn
qtechIfQosFlowLimitConformByte = _QtechIfQosFlowLimitConformByte_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 11),
    _QtechIfQosFlowLimitConformByte_Type()
)
qtechIfQosFlowLimitConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitConformByte.setStatus("current")
_QtechIfQosFlowLimitExceedPkt_Type = Counter32
_QtechIfQosFlowLimitExceedPkt_Object = MibTableColumn
qtechIfQosFlowLimitExceedPkt = _QtechIfQosFlowLimitExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 12),
    _QtechIfQosFlowLimitExceedPkt_Type()
)
qtechIfQosFlowLimitExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitExceedPkt.setStatus("current")
_QtechIfQosFlowLimitExceedByte_Type = Counter32
_QtechIfQosFlowLimitExceedByte_Object = MibTableColumn
qtechIfQosFlowLimitExceedByte = _QtechIfQosFlowLimitExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 2, 8, 1, 13),
    _QtechIfQosFlowLimitExceedByte_Type()
)
qtechIfQosFlowLimitExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQosFlowLimitExceedByte.setStatus("current")
_QtechHQoSMIBObjects_ObjectIdentity = ObjectIdentity
qtechHQoSMIBObjects = _QtechHQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3)
)
_QtechHQoSScalarObjects_ObjectIdentity = ObjectIdentity
qtechHQoSScalarObjects = _QtechHQoSScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 1)
)


class _QtechHQoSNameType_Type(Integer32):
    """Custom type qtechHQoSNameType based on Integer32"""
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


_QtechHQoSNameType_Type.__name__ = "Integer32"
_QtechHQoSNameType_Object = MibScalar
qtechHQoSNameType = _QtechHQoSNameType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 1, 1),
    _QtechHQoSNameType_Type()
)
qtechHQoSNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSNameType.setStatus("current")


class _QtechHQoSNameFind_Type(OctetString):
    """Custom type qtechHQoSNameFind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSNameFind_Type.__name__ = "OctetString"
_QtechHQoSNameFind_Object = MibScalar
qtechHQoSNameFind = _QtechHQoSNameFind_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 1, 2),
    _QtechHQoSNameFind_Type()
)
qtechHQoSNameFind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSNameFind.setStatus("current")


class _QtechHQoSNameIndex_Type(Integer32):
    """Custom type qtechHQoSNameIndex based on Integer32"""
    defaultValue = 0


_QtechHQoSNameIndex_Type.__name__ = "Integer32"
_QtechHQoSNameIndex_Object = MibScalar
qtechHQoSNameIndex = _QtechHQoSNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 1, 3),
    _QtechHQoSNameIndex_Type()
)
qtechHQoSNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSNameIndex.setStatus("current")
_QtechHQoSUserQObjects_ObjectIdentity = ObjectIdentity
qtechHQoSUserQObjects = _QtechHQoSUserQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2)
)
_QtechHQoSUserQInIndexNext_Type = Integer32
_QtechHQoSUserQInIndexNext_Object = MibScalar
qtechHQoSUserQInIndexNext = _QtechHQoSUserQInIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 1),
    _QtechHQoSUserQInIndexNext_Type()
)
qtechHQoSUserQInIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserQInIndexNext.setStatus("current")
_QtechHQoSUserQOutIndexNext_Type = Integer32
_QtechHQoSUserQOutIndexNext_Object = MibScalar
qtechHQoSUserQOutIndexNext = _QtechHQoSUserQOutIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 2),
    _QtechHQoSUserQOutIndexNext_Type()
)
qtechHQoSUserQOutIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserQOutIndexNext.setStatus("current")
_QtechHQoSUserQTable_Object = MibTable
qtechHQoSUserQTable = _QtechHQoSUserQTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3)
)
if mibBuilder.loadTexts:
    qtechHQoSUserQTable.setStatus("current")
_QtechHQoSUserQEntry_Object = MibTableRow
qtechHQoSUserQEntry = _QtechHQoSUserQEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1)
)
qtechHQoSUserQEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSUserQIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSUserQEntry.setStatus("current")
_QtechHQoSUserQIndex_Type = Unsigned32
_QtechHQoSUserQIndex_Object = MibTableColumn
qtechHQoSUserQIndex = _QtechHQoSUserQIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 1),
    _QtechHQoSUserQIndex_Type()
)
qtechHQoSUserQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSUserQIndex.setStatus("current")


class _QtechHQoSUserQName_Type(OctetString):
    """Custom type qtechHQoSUserQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSUserQName_Type.__name__ = "OctetString"
_QtechHQoSUserQName_Object = MibTableColumn
qtechHQoSUserQName = _QtechHQoSUserQName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 2),
    _QtechHQoSUserQName_Type()
)
qtechHQoSUserQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQName.setStatus("current")
_QtechHQoSUserQDirection_Type = QtechQDirectionType
_QtechHQoSUserQDirection_Object = MibTableColumn
qtechHQoSUserQDirection = _QtechHQoSUserQDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 3),
    _QtechHQoSUserQDirection_Type()
)
qtechHQoSUserQDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQDirection.setStatus("current")
_QtechHQoSUserQRowStatus_Type = RowStatus
_QtechHQoSUserQRowStatus_Object = MibTableColumn
qtechHQoSUserQRowStatus = _QtechHQoSUserQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 4),
    _QtechHQoSUserQRowStatus_Type()
)
qtechHQoSUserQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQRowStatus.setStatus("current")


class _QtechHQoSUserQFlowQName_Type(OctetString):
    """Custom type qtechHQoSUserQFlowQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSUserQFlowQName_Type.__name__ = "OctetString"
_QtechHQoSUserQFlowQName_Object = MibTableColumn
qtechHQoSUserQFlowQName = _QtechHQoSUserQFlowQName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 5),
    _QtechHQoSUserQFlowQName_Type()
)
qtechHQoSUserQFlowQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQFlowQName.setStatus("current")
_QtechHQoSUserQFlowQIndex_Type = Unsigned32
_QtechHQoSUserQFlowQIndex_Object = MibTableColumn
qtechHQoSUserQFlowQIndex = _QtechHQoSUserQFlowQIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 6),
    _QtechHQoSUserQFlowQIndex_Type()
)
qtechHQoSUserQFlowQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserQFlowQIndex.setStatus("current")


class _QtechHQoSUserQGroupName_Type(OctetString):
    """Custom type qtechHQoSUserQGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSUserQGroupName_Type.__name__ = "OctetString"
_QtechHQoSUserQGroupName_Object = MibTableColumn
qtechHQoSUserQGroupName = _QtechHQoSUserQGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 7),
    _QtechHQoSUserQGroupName_Type()
)
qtechHQoSUserQGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQGroupName.setStatus("current")
_QtechHQoSUserQGroupIndex_Type = Unsigned32
_QtechHQoSUserQGroupIndex_Object = MibTableColumn
qtechHQoSUserQGroupIndex = _QtechHQoSUserQGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 8),
    _QtechHQoSUserQGroupIndex_Type()
)
qtechHQoSUserQGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserQGroupIndex.setStatus("current")


class _QtechHQoSUserQFlowMapName_Type(OctetString):
    """Custom type qtechHQoSUserQFlowMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSUserQFlowMapName_Type.__name__ = "OctetString"
_QtechHQoSUserQFlowMapName_Object = MibTableColumn
qtechHQoSUserQFlowMapName = _QtechHQoSUserQFlowMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 9),
    _QtechHQoSUserQFlowMapName_Type()
)
qtechHQoSUserQFlowMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQFlowMapName.setStatus("current")
_QtechHQoSUserQFlowMapIndex_Type = Unsigned32
_QtechHQoSUserQFlowMapIndex_Object = MibTableColumn
qtechHQoSUserQFlowMapIndex = _QtechHQoSUserQFlowMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 10),
    _QtechHQoSUserQFlowMapIndex_Type()
)
qtechHQoSUserQFlowMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserQFlowMapIndex.setStatus("current")


class _QtechHQoSUserQCIR_Type(Unsigned32):
    """Custom type qtechHQoSUserQCIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSUserQCIR_Type.__name__ = "Unsigned32"
_QtechHQoSUserQCIR_Object = MibTableColumn
qtechHQoSUserQCIR = _QtechHQoSUserQCIR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 11),
    _QtechHQoSUserQCIR_Type()
)
qtechHQoSUserQCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQCIR.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSUserQCIR.setUnits("kilobits per second")


class _QtechHQoSUserQPIR_Type(Unsigned32):
    """Custom type qtechHQoSUserQPIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_QtechHQoSUserQPIR_Type.__name__ = "Unsigned32"
_QtechHQoSUserQPIR_Object = MibTableColumn
qtechHQoSUserQPIR = _QtechHQoSUserQPIR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 2, 3, 1, 12),
    _QtechHQoSUserQPIR_Type()
)
qtechHQoSUserQPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserQPIR.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSUserQPIR.setUnits("kilobits per second")
_QtechHQoSUserGroupQObjects_ObjectIdentity = ObjectIdentity
qtechHQoSUserGroupQObjects = _QtechHQoSUserGroupQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3)
)
_QtechHQoSUserGroupQInIndexNext_Type = Integer32
_QtechHQoSUserGroupQInIndexNext_Object = MibScalar
qtechHQoSUserGroupQInIndexNext = _QtechHQoSUserGroupQInIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 1),
    _QtechHQoSUserGroupQInIndexNext_Type()
)
qtechHQoSUserGroupQInIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQInIndexNext.setStatus("current")
_QtechHQoSUserGroupQOutIndexNext_Type = Integer32
_QtechHQoSUserGroupQOutIndexNext_Object = MibScalar
qtechHQoSUserGroupQOutIndexNext = _QtechHQoSUserGroupQOutIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 2),
    _QtechHQoSUserGroupQOutIndexNext_Type()
)
qtechHQoSUserGroupQOutIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQOutIndexNext.setStatus("current")
_QtechHQoSUserGroupQTable_Object = MibTable
qtechHQoSUserGroupQTable = _QtechHQoSUserGroupQTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3)
)
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQTable.setStatus("current")
_QtechHQoSUserGroupQEntry_Object = MibTableRow
qtechHQoSUserGroupQEntry = _QtechHQoSUserGroupQEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3, 1)
)
qtechHQoSUserGroupQEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSUserGroupQIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQEntry.setStatus("current")
_QtechHQoSUserGroupQIndex_Type = Unsigned32
_QtechHQoSUserGroupQIndex_Object = MibTableColumn
qtechHQoSUserGroupQIndex = _QtechHQoSUserGroupQIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3, 1, 1),
    _QtechHQoSUserGroupQIndex_Type()
)
qtechHQoSUserGroupQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQIndex.setStatus("current")


class _QtechHQoSUserGroupQName_Type(OctetString):
    """Custom type qtechHQoSUserGroupQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSUserGroupQName_Type.__name__ = "OctetString"
_QtechHQoSUserGroupQName_Object = MibTableColumn
qtechHQoSUserGroupQName = _QtechHQoSUserGroupQName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3, 1, 2),
    _QtechHQoSUserGroupQName_Type()
)
qtechHQoSUserGroupQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQName.setStatus("current")
_QtechHQoSUserGroupQDirection_Type = QtechQDirectionType
_QtechHQoSUserGroupQDirection_Object = MibTableColumn
qtechHQoSUserGroupQDirection = _QtechHQoSUserGroupQDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3, 1, 3),
    _QtechHQoSUserGroupQDirection_Type()
)
qtechHQoSUserGroupQDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQDirection.setStatus("current")
_QtechHQoSUserGroupQRowStatus_Type = RowStatus
_QtechHQoSUserGroupQRowStatus_Object = MibTableColumn
qtechHQoSUserGroupQRowStatus = _QtechHQoSUserGroupQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3, 1, 4),
    _QtechHQoSUserGroupQRowStatus_Type()
)
qtechHQoSUserGroupQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQRowStatus.setStatus("current")


class _QtechHQoSUserGroupQShaping_Type(Unsigned32):
    """Custom type qtechHQoSUserGroupQShaping based on Unsigned32"""
    defaultValue = 10000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSUserGroupQShaping_Type.__name__ = "Unsigned32"
_QtechHQoSUserGroupQShaping_Object = MibTableColumn
qtechHQoSUserGroupQShaping = _QtechHQoSUserGroupQShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 3, 3, 1, 5),
    _QtechHQoSUserGroupQShaping_Type()
)
qtechHQoSUserGroupQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSUserGroupQShaping.setUnits("kilobits per second")
_QtechHQoSFlowQObjects_ObjectIdentity = ObjectIdentity
qtechHQoSFlowQObjects = _QtechHQoSFlowQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4)
)
_QtechHQoSFlowQIndexNext_Type = Integer32
_QtechHQoSFlowQIndexNext_Object = MibScalar
qtechHQoSFlowQIndexNext = _QtechHQoSFlowQIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 1),
    _QtechHQoSFlowQIndexNext_Type()
)
qtechHQoSFlowQIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSFlowQIndexNext.setStatus("current")
_QtechHQoSFlowQTable_Object = MibTable
qtechHQoSFlowQTable = _QtechHQoSFlowQTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSFlowQTable.setStatus("current")
_QtechHQoSFlowQEntry_Object = MibTableRow
qtechHQoSFlowQEntry = _QtechHQoSFlowQEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1)
)
qtechHQoSFlowQEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSFlowQIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSFlowQEntry.setStatus("current")
_QtechHQoSFlowQIndex_Type = Unsigned32
_QtechHQoSFlowQIndex_Object = MibTableColumn
qtechHQoSFlowQIndex = _QtechHQoSFlowQIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 1),
    _QtechHQoSFlowQIndex_Type()
)
qtechHQoSFlowQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSFlowQIndex.setStatus("current")


class _QtechHQoSFlowQName_Type(OctetString):
    """Custom type qtechHQoSFlowQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQName_Type.__name__ = "OctetString"
_QtechHQoSFlowQName_Object = MibTableColumn
qtechHQoSFlowQName = _QtechHQoSFlowQName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 2),
    _QtechHQoSFlowQName_Type()
)
qtechHQoSFlowQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQName.setStatus("current")
_QtechHQoSFlowQRowStatus_Type = RowStatus
_QtechHQoSFlowQRowStatus_Object = MibTableColumn
qtechHQoSFlowQRowStatus = _QtechHQoSFlowQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 3),
    _QtechHQoSFlowQRowStatus_Type()
)
qtechHQoSFlowQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQRowStatus.setStatus("current")


class _QtechHQoSFlowQBEQType_Type(QtechQType):
    """Custom type qtechHQoSFlowQBEQType based on QtechQType"""
    defaultValue = 2


_QtechHQoSFlowQBEQType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQBEQType_Object = MibTableColumn
qtechHQoSFlowQBEQType = _QtechHQoSFlowQBEQType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 4),
    _QtechHQoSFlowQBEQType_Type()
)
qtechHQoSFlowQBEQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQBEQType.setStatus("current")


class _QtechHQoSFlowQBEQWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQBEQWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQBEQWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQBEQWredWeight_Object = MibTableColumn
qtechHQoSFlowQBEQWredWeight = _QtechHQoSFlowQBEQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 5),
    _QtechHQoSFlowQBEQWredWeight_Type()
)
qtechHQoSFlowQBEQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQBEQWredWeight.setStatus("current")


class _QtechHQoSFlowQBEQWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQBEQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQBEQWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQBEQWredName_Object = MibTableColumn
qtechHQoSFlowQBEQWredName = _QtechHQoSFlowQBEQWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 6),
    _QtechHQoSFlowQBEQWredName_Type()
)
qtechHQoSFlowQBEQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQBEQWredName.setStatus("current")


class _QtechHQoSFlowQBEQDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQBEQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQBEQDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQBEQDepth_Object = MibTableColumn
qtechHQoSFlowQBEQDepth = _QtechHQoSFlowQBEQDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 7),
    _QtechHQoSFlowQBEQDepth_Type()
)
qtechHQoSFlowQBEQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQBEQDepth.setStatus("current")


class _QtechHQoSFlowQBEQShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQBEQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQBEQShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQBEQShaping_Object = MibTableColumn
qtechHQoSFlowQBEQShaping = _QtechHQoSFlowQBEQShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 8),
    _QtechHQoSFlowQBEQShaping_Type()
)
qtechHQoSFlowQBEQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQBEQShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQBEQShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQAF1QType_Type(QtechQType):
    """Custom type qtechHQoSFlowQAF1QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSFlowQAF1QType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQAF1QType_Object = MibTableColumn
qtechHQoSFlowQAF1QType = _QtechHQoSFlowQAF1QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 9),
    _QtechHQoSFlowQAF1QType_Type()
)
qtechHQoSFlowQAF1QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF1QType.setStatus("current")


class _QtechHQoSFlowQAF1QWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQAF1QWredWeight based on Integer32"""
    defaultValue = 10


_QtechHQoSFlowQAF1QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF1QWredWeight_Object = MibTableColumn
qtechHQoSFlowQAF1QWredWeight = _QtechHQoSFlowQAF1QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 10),
    _QtechHQoSFlowQAF1QWredWeight_Type()
)
qtechHQoSFlowQAF1QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF1QWredWeight.setStatus("current")


class _QtechHQoSFlowQAF1QWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQAF1QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQAF1QWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQAF1QWredName_Object = MibTableColumn
qtechHQoSFlowQAF1QWredName = _QtechHQoSFlowQAF1QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 11),
    _QtechHQoSFlowQAF1QWredName_Type()
)
qtechHQoSFlowQAF1QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF1QWredName.setStatus("current")


class _QtechHQoSFlowQAF1QDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQAF1QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQAF1QDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF1QDepth_Object = MibTableColumn
qtechHQoSFlowQAF1QDepth = _QtechHQoSFlowQAF1QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 12),
    _QtechHQoSFlowQAF1QDepth_Type()
)
qtechHQoSFlowQAF1QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF1QDepth.setStatus("current")


class _QtechHQoSFlowQAF1QShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQAF1QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQAF1QShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF1QShaping_Object = MibTableColumn
qtechHQoSFlowQAF1QShaping = _QtechHQoSFlowQAF1QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 13),
    _QtechHQoSFlowQAF1QShaping_Type()
)
qtechHQoSFlowQAF1QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF1QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF1QShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQAF2QType_Type(QtechQType):
    """Custom type qtechHQoSFlowQAF2QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSFlowQAF2QType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQAF2QType_Object = MibTableColumn
qtechHQoSFlowQAF2QType = _QtechHQoSFlowQAF2QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 14),
    _QtechHQoSFlowQAF2QType_Type()
)
qtechHQoSFlowQAF2QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF2QType.setStatus("current")


class _QtechHQoSFlowQAF2QWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQAF2QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQAF2QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF2QWredWeight_Object = MibTableColumn
qtechHQoSFlowQAF2QWredWeight = _QtechHQoSFlowQAF2QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 15),
    _QtechHQoSFlowQAF2QWredWeight_Type()
)
qtechHQoSFlowQAF2QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF2QWredWeight.setStatus("current")


class _QtechHQoSFlowQAF2QWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQAF2QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQAF2QWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQAF2QWredName_Object = MibTableColumn
qtechHQoSFlowQAF2QWredName = _QtechHQoSFlowQAF2QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 16),
    _QtechHQoSFlowQAF2QWredName_Type()
)
qtechHQoSFlowQAF2QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF2QWredName.setStatus("current")


class _QtechHQoSFlowQAF2QDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQAF2QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQAF2QDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF2QDepth_Object = MibTableColumn
qtechHQoSFlowQAF2QDepth = _QtechHQoSFlowQAF2QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 17),
    _QtechHQoSFlowQAF2QDepth_Type()
)
qtechHQoSFlowQAF2QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF2QDepth.setStatus("current")


class _QtechHQoSFlowQAF2QShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQAF2QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQAF2QShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF2QShaping_Object = MibTableColumn
qtechHQoSFlowQAF2QShaping = _QtechHQoSFlowQAF2QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 18),
    _QtechHQoSFlowQAF2QShaping_Type()
)
qtechHQoSFlowQAF2QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF2QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF2QShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQAF3QType_Type(QtechQType):
    """Custom type qtechHQoSFlowQAF3QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSFlowQAF3QType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQAF3QType_Object = MibTableColumn
qtechHQoSFlowQAF3QType = _QtechHQoSFlowQAF3QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 19),
    _QtechHQoSFlowQAF3QType_Type()
)
qtechHQoSFlowQAF3QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QType.setStatus("current")


class _QtechHQoSFlowQAF3QWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQAF3QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQAF3QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF3QWredWeight_Object = MibTableColumn
qtechHQoSFlowQAF3QWredWeight = _QtechHQoSFlowQAF3QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 20),
    _QtechHQoSFlowQAF3QWredWeight_Type()
)
qtechHQoSFlowQAF3QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QWredWeight.setStatus("current")


class _QtechHQoSFlowQAF3QWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQAF3QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQAF3QWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQAF3QWredName_Object = MibTableColumn
qtechHQoSFlowQAF3QWredName = _QtechHQoSFlowQAF3QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 21),
    _QtechHQoSFlowQAF3QWredName_Type()
)
qtechHQoSFlowQAF3QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QWredName.setStatus("current")


class _QtechHQoSFlowQAF3QDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQAF3QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQAF3QDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF3QDepth_Object = MibTableColumn
qtechHQoSFlowQAF3QDepth = _QtechHQoSFlowQAF3QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 22),
    _QtechHQoSFlowQAF3QDepth_Type()
)
qtechHQoSFlowQAF3QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QDepth.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QDepth.setUnits("kilobits per second")


class _QtechHQoSFlowQAF3QShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQAF3QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQAF3QShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF3QShaping_Object = MibTableColumn
qtechHQoSFlowQAF3QShaping = _QtechHQoSFlowQAF3QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 23),
    _QtechHQoSFlowQAF3QShaping_Type()
)
qtechHQoSFlowQAF3QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF3QShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQAF4QType_Type(QtechQType):
    """Custom type qtechHQoSFlowQAF4QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSFlowQAF4QType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQAF4QType_Object = MibTableColumn
qtechHQoSFlowQAF4QType = _QtechHQoSFlowQAF4QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 24),
    _QtechHQoSFlowQAF4QType_Type()
)
qtechHQoSFlowQAF4QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF4QType.setStatus("current")


class _QtechHQoSFlowQAF4QWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQAF4QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQAF4QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF4QWredWeight_Object = MibTableColumn
qtechHQoSFlowQAF4QWredWeight = _QtechHQoSFlowQAF4QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 25),
    _QtechHQoSFlowQAF4QWredWeight_Type()
)
qtechHQoSFlowQAF4QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF4QWredWeight.setStatus("current")


class _QtechHQoSFlowQAF4QWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQAF4QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQAF4QWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQAF4QWredName_Object = MibTableColumn
qtechHQoSFlowQAF4QWredName = _QtechHQoSFlowQAF4QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 26),
    _QtechHQoSFlowQAF4QWredName_Type()
)
qtechHQoSFlowQAF4QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF4QWredName.setStatus("current")


class _QtechHQoSFlowQAF4QDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQAF4QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQAF4QDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF4QDepth_Object = MibTableColumn
qtechHQoSFlowQAF4QDepth = _QtechHQoSFlowQAF4QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 27),
    _QtechHQoSFlowQAF4QDepth_Type()
)
qtechHQoSFlowQAF4QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF4QDepth.setStatus("current")


class _QtechHQoSFlowQAF4QShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQAF4QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_QtechHQoSFlowQAF4QShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQAF4QShaping_Object = MibTableColumn
qtechHQoSFlowQAF4QShaping = _QtechHQoSFlowQAF4QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 28),
    _QtechHQoSFlowQAF4QShaping_Type()
)
qtechHQoSFlowQAF4QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF4QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQAF4QShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQEFQType_Type(QtechQType):
    """Custom type qtechHQoSFlowQEFQType based on QtechQType"""
    defaultValue = 3


_QtechHQoSFlowQEFQType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQEFQType_Object = MibTableColumn
qtechHQoSFlowQEFQType = _QtechHQoSFlowQEFQType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 29),
    _QtechHQoSFlowQEFQType_Type()
)
qtechHQoSFlowQEFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQEFQType.setStatus("current")


class _QtechHQoSFlowQEFQWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQEFQWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQEFQWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQEFQWredWeight_Object = MibTableColumn
qtechHQoSFlowQEFQWredWeight = _QtechHQoSFlowQEFQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 30),
    _QtechHQoSFlowQEFQWredWeight_Type()
)
qtechHQoSFlowQEFQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQEFQWredWeight.setStatus("current")


class _QtechHQoSFlowQEFQWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQEFQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQEFQWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQEFQWredName_Object = MibTableColumn
qtechHQoSFlowQEFQWredName = _QtechHQoSFlowQEFQWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 31),
    _QtechHQoSFlowQEFQWredName_Type()
)
qtechHQoSFlowQEFQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQEFQWredName.setStatus("current")


class _QtechHQoSFlowQEFQDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQEFQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQEFQDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQEFQDepth_Object = MibTableColumn
qtechHQoSFlowQEFQDepth = _QtechHQoSFlowQEFQDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 32),
    _QtechHQoSFlowQEFQDepth_Type()
)
qtechHQoSFlowQEFQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQEFQDepth.setStatus("current")


class _QtechHQoSFlowQEFQShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQEFQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQEFQShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQEFQShaping_Object = MibTableColumn
qtechHQoSFlowQEFQShaping = _QtechHQoSFlowQEFQShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 33),
    _QtechHQoSFlowQEFQShaping_Type()
)
qtechHQoSFlowQEFQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQEFQShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQEFQShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQCS6QType_Type(QtechQType):
    """Custom type qtechHQoSFlowQCS6QType based on QtechQType"""
    defaultValue = 3


_QtechHQoSFlowQCS6QType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQCS6QType_Object = MibTableColumn
qtechHQoSFlowQCS6QType = _QtechHQoSFlowQCS6QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 34),
    _QtechHQoSFlowQCS6QType_Type()
)
qtechHQoSFlowQCS6QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS6QType.setStatus("current")


class _QtechHQoSFlowQCS6QWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQCS6QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQCS6QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQCS6QWredWeight_Object = MibTableColumn
qtechHQoSFlowQCS6QWredWeight = _QtechHQoSFlowQCS6QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 35),
    _QtechHQoSFlowQCS6QWredWeight_Type()
)
qtechHQoSFlowQCS6QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS6QWredWeight.setStatus("current")


class _QtechHQoSFlowQCS6QWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQCS6QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQCS6QWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQCS6QWredName_Object = MibTableColumn
qtechHQoSFlowQCS6QWredName = _QtechHQoSFlowQCS6QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 36),
    _QtechHQoSFlowQCS6QWredName_Type()
)
qtechHQoSFlowQCS6QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS6QWredName.setStatus("current")


class _QtechHQoSFlowQCS6QDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQCS6QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQCS6QDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQCS6QDepth_Object = MibTableColumn
qtechHQoSFlowQCS6QDepth = _QtechHQoSFlowQCS6QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 37),
    _QtechHQoSFlowQCS6QDepth_Type()
)
qtechHQoSFlowQCS6QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS6QDepth.setStatus("current")


class _QtechHQoSFlowQCS6QShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQCS6QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQCS6QShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQCS6QShaping_Object = MibTableColumn
qtechHQoSFlowQCS6QShaping = _QtechHQoSFlowQCS6QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 38),
    _QtechHQoSFlowQCS6QShaping_Type()
)
qtechHQoSFlowQCS6QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS6QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS6QShaping.setUnits("kilobits per second")


class _QtechHQoSFlowQCS7QType_Type(QtechQType):
    """Custom type qtechHQoSFlowQCS7QType based on QtechQType"""
    defaultValue = 3


_QtechHQoSFlowQCS7QType_Type.__name__ = "QtechQType"
_QtechHQoSFlowQCS7QType_Object = MibTableColumn
qtechHQoSFlowQCS7QType = _QtechHQoSFlowQCS7QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 39),
    _QtechHQoSFlowQCS7QType_Type()
)
qtechHQoSFlowQCS7QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS7QType.setStatus("current")


class _QtechHQoSFlowQCS7QWredWeight_Type(Integer32):
    """Custom type qtechHQoSFlowQCS7QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSFlowQCS7QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSFlowQCS7QWredWeight_Object = MibTableColumn
qtechHQoSFlowQCS7QWredWeight = _QtechHQoSFlowQCS7QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 40),
    _QtechHQoSFlowQCS7QWredWeight_Type()
)
qtechHQoSFlowQCS7QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS7QWredWeight.setStatus("current")


class _QtechHQoSFlowQCS7QWredName_Type(OctetString):
    """Custom type qtechHQoSFlowQCS7QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowQCS7QWredName_Type.__name__ = "OctetString"
_QtechHQoSFlowQCS7QWredName_Object = MibTableColumn
qtechHQoSFlowQCS7QWredName = _QtechHQoSFlowQCS7QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 41),
    _QtechHQoSFlowQCS7QWredName_Type()
)
qtechHQoSFlowQCS7QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS7QWredName.setStatus("current")


class _QtechHQoSFlowQCS7QDepth_Type(Integer32):
    """Custom type qtechHQoSFlowQCS7QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSFlowQCS7QDepth_Type.__name__ = "Integer32"
_QtechHQoSFlowQCS7QDepth_Object = MibTableColumn
qtechHQoSFlowQCS7QDepth = _QtechHQoSFlowQCS7QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 42),
    _QtechHQoSFlowQCS7QDepth_Type()
)
qtechHQoSFlowQCS7QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS7QDepth.setStatus("current")


class _QtechHQoSFlowQCS7QShaping_Type(Integer32):
    """Custom type qtechHQoSFlowQCS7QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSFlowQCS7QShaping_Type.__name__ = "Integer32"
_QtechHQoSFlowQCS7QShaping_Object = MibTableColumn
qtechHQoSFlowQCS7QShaping = _QtechHQoSFlowQCS7QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 4, 2, 1, 43),
    _QtechHQoSFlowQCS7QShaping_Type()
)
qtechHQoSFlowQCS7QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS7QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSFlowQCS7QShaping.setUnits("kilobits per second")
_QtechHQoSFlowMapObjects_ObjectIdentity = ObjectIdentity
qtechHQoSFlowMapObjects = _QtechHQoSFlowMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5)
)
_QtechHQoSFlowMapIndexNext_Type = Integer32
_QtechHQoSFlowMapIndexNext_Object = MibScalar
qtechHQoSFlowMapIndexNext = _QtechHQoSFlowMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 1),
    _QtechHQoSFlowMapIndexNext_Type()
)
qtechHQoSFlowMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapIndexNext.setStatus("current")
_QtechHQoSFlowMapTable_Object = MibTable
qtechHQoSFlowMapTable = _QtechHQoSFlowMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSFlowMapTable.setStatus("current")
_QtechHQoSFlowMapEntry_Object = MibTableRow
qtechHQoSFlowMapEntry = _QtechHQoSFlowMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1)
)
qtechHQoSFlowMapEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSFlowMapIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSFlowMapEntry.setStatus("current")
_QtechHQoSFlowMapIndex_Type = Unsigned32
_QtechHQoSFlowMapIndex_Object = MibTableColumn
qtechHQoSFlowMapIndex = _QtechHQoSFlowMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 1),
    _QtechHQoSFlowMapIndex_Type()
)
qtechHQoSFlowMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapIndex.setStatus("current")


class _QtechHQoSFlowMapName_Type(OctetString):
    """Custom type qtechHQoSFlowMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSFlowMapName_Type.__name__ = "OctetString"
_QtechHQoSFlowMapName_Object = MibTableColumn
qtechHQoSFlowMapName = _QtechHQoSFlowMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 2),
    _QtechHQoSFlowMapName_Type()
)
qtechHQoSFlowMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapName.setStatus("current")
_QtechHQoSFlowMapRowStatus_Type = RowStatus
_QtechHQoSFlowMapRowStatus_Object = MibTableColumn
qtechHQoSFlowMapRowStatus = _QtechHQoSFlowMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 3),
    _QtechHQoSFlowMapRowStatus_Type()
)
qtechHQoSFlowMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapRowStatus.setStatus("current")


class _QtechHQoSFlowMapBEQ2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapBEQ2PortQ based on QtechCosType"""
    defaultValue = 1


_QtechHQoSFlowMapBEQ2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapBEQ2PortQ_Object = MibTableColumn
qtechHQoSFlowMapBEQ2PortQ = _QtechHQoSFlowMapBEQ2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 4),
    _QtechHQoSFlowMapBEQ2PortQ_Type()
)
qtechHQoSFlowMapBEQ2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapBEQ2PortQ.setStatus("current")


class _QtechHQoSFlowMapAF1Q2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapAF1Q2PortQ based on QtechCosType"""
    defaultValue = 2


_QtechHQoSFlowMapAF1Q2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapAF1Q2PortQ_Object = MibTableColumn
qtechHQoSFlowMapAF1Q2PortQ = _QtechHQoSFlowMapAF1Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 5),
    _QtechHQoSFlowMapAF1Q2PortQ_Type()
)
qtechHQoSFlowMapAF1Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapAF1Q2PortQ.setStatus("current")


class _QtechHQoSFlowMapAF2Q2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapAF2Q2PortQ based on QtechCosType"""
    defaultValue = 3


_QtechHQoSFlowMapAF2Q2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapAF2Q2PortQ_Object = MibTableColumn
qtechHQoSFlowMapAF2Q2PortQ = _QtechHQoSFlowMapAF2Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 6),
    _QtechHQoSFlowMapAF2Q2PortQ_Type()
)
qtechHQoSFlowMapAF2Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapAF2Q2PortQ.setStatus("current")


class _QtechHQoSFlowMapAF3Q2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapAF3Q2PortQ based on QtechCosType"""
    defaultValue = 4


_QtechHQoSFlowMapAF3Q2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapAF3Q2PortQ_Object = MibTableColumn
qtechHQoSFlowMapAF3Q2PortQ = _QtechHQoSFlowMapAF3Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 7),
    _QtechHQoSFlowMapAF3Q2PortQ_Type()
)
qtechHQoSFlowMapAF3Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapAF3Q2PortQ.setStatus("current")


class _QtechHQoSFlowMapAF4Q2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapAF4Q2PortQ based on QtechCosType"""
    defaultValue = 5


_QtechHQoSFlowMapAF4Q2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapAF4Q2PortQ_Object = MibTableColumn
qtechHQoSFlowMapAF4Q2PortQ = _QtechHQoSFlowMapAF4Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 8),
    _QtechHQoSFlowMapAF4Q2PortQ_Type()
)
qtechHQoSFlowMapAF4Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapAF4Q2PortQ.setStatus("current")


class _QtechHQoSFlowMapEFQ2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapEFQ2PortQ based on QtechCosType"""
    defaultValue = 6


_QtechHQoSFlowMapEFQ2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapEFQ2PortQ_Object = MibTableColumn
qtechHQoSFlowMapEFQ2PortQ = _QtechHQoSFlowMapEFQ2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 9),
    _QtechHQoSFlowMapEFQ2PortQ_Type()
)
qtechHQoSFlowMapEFQ2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapEFQ2PortQ.setStatus("current")


class _QtechHQoSFlowMapCS6Q2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapCS6Q2PortQ based on QtechCosType"""
    defaultValue = 7


_QtechHQoSFlowMapCS6Q2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapCS6Q2PortQ_Object = MibTableColumn
qtechHQoSFlowMapCS6Q2PortQ = _QtechHQoSFlowMapCS6Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 10),
    _QtechHQoSFlowMapCS6Q2PortQ_Type()
)
qtechHQoSFlowMapCS6Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapCS6Q2PortQ.setStatus("current")


class _QtechHQoSFlowMapCS7Q2PortQ_Type(QtechCosType):
    """Custom type qtechHQoSFlowMapCS7Q2PortQ based on QtechCosType"""
    defaultValue = 8


_QtechHQoSFlowMapCS7Q2PortQ_Type.__name__ = "QtechCosType"
_QtechHQoSFlowMapCS7Q2PortQ_Object = MibTableColumn
qtechHQoSFlowMapCS7Q2PortQ = _QtechHQoSFlowMapCS7Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 5, 2, 1, 11),
    _QtechHQoSFlowMapCS7Q2PortQ_Type()
)
qtechHQoSFlowMapCS7Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSFlowMapCS7Q2PortQ.setStatus("current")
_QtechHQoSTClassifierObjects_ObjectIdentity = ObjectIdentity
qtechHQoSTClassifierObjects = _QtechHQoSTClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6)
)
_QtechHQoSTClassifierIndexNext_Type = Integer32
_QtechHQoSTClassifierIndexNext_Object = MibScalar
qtechHQoSTClassifierIndexNext = _QtechHQoSTClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 1),
    _QtechHQoSTClassifierIndexNext_Type()
)
qtechHQoSTClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierIndexNext.setStatus("current")
_QtechHQoSTClassifierTable_Object = MibTable
qtechHQoSTClassifierTable = _QtechHQoSTClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSTClassifierTable.setStatus("current")
_QtechHQoSTClassifierEntry_Object = MibTableRow
qtechHQoSTClassifierEntry = _QtechHQoSTClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1)
)
qtechHQoSTClassifierEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSTClassifierIndex"),
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSTClassifierInstance"),
)
if mibBuilder.loadTexts:
    qtechHQoSTClassifierEntry.setStatus("current")
_QtechHQoSTClassifierIndex_Type = Unsigned32
_QtechHQoSTClassifierIndex_Object = MibTableColumn
qtechHQoSTClassifierIndex = _QtechHQoSTClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 1),
    _QtechHQoSTClassifierIndex_Type()
)
qtechHQoSTClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierIndex.setStatus("current")
_QtechHQoSTClassifierInstance_Type = Unsigned32
_QtechHQoSTClassifierInstance_Object = MibTableColumn
qtechHQoSTClassifierInstance = _QtechHQoSTClassifierInstance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 2),
    _QtechHQoSTClassifierInstance_Type()
)
qtechHQoSTClassifierInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierInstance.setStatus("current")


class _QtechHQoSTClassifierName_Type(OctetString):
    """Custom type qtechHQoSTClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTClassifierName_Type.__name__ = "OctetString"
_QtechHQoSTClassifierName_Object = MibTableColumn
qtechHQoSTClassifierName = _QtechHQoSTClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 3),
    _QtechHQoSTClassifierName_Type()
)
qtechHQoSTClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierName.setStatus("current")


class _QtechHQoSTClassifierType_Type(Integer32):
    """Custom type qtechHQoSTClassifierType based on Integer32"""
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


_QtechHQoSTClassifierType_Type.__name__ = "Integer32"
_QtechHQoSTClassifierType_Object = MibTableColumn
qtechHQoSTClassifierType = _QtechHQoSTClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 4),
    _QtechHQoSTClassifierType_Type()
)
qtechHQoSTClassifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierType.setStatus("current")
_QtechHQoSTClassifierRowStatus_Type = RowStatus
_QtechHQoSTClassifierRowStatus_Object = MibTableColumn
qtechHQoSTClassifierRowStatus = _QtechHQoSTClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 5),
    _QtechHQoSTClassifierRowStatus_Type()
)
qtechHQoSTClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierRowStatus.setStatus("current")


class _QtechHQoSTClassifierMatchMask_Type(Bits):
    """Custom type qtechHQoSTClassifierMatchMask based on Bits"""
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

_QtechHQoSTClassifierMatchMask_Type.__name__ = "Bits"
_QtechHQoSTClassifierMatchMask_Object = MibTableColumn
qtechHQoSTClassifierMatchMask = _QtechHQoSTClassifierMatchMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 6),
    _QtechHQoSTClassifierMatchMask_Type()
)
qtechHQoSTClassifierMatchMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchMask.setStatus("current")


class _QtechHQoSTClassifierMatchV4Any_Type(TruthValue):
    """Custom type qtechHQoSTClassifierMatchV4Any based on TruthValue"""
    defaultValue = 2


_QtechHQoSTClassifierMatchV4Any_Type.__name__ = "TruthValue"
_QtechHQoSTClassifierMatchV4Any_Object = MibTableColumn
qtechHQoSTClassifierMatchV4Any = _QtechHQoSTClassifierMatchV4Any_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 7),
    _QtechHQoSTClassifierMatchV4Any_Type()
)
qtechHQoSTClassifierMatchV4Any.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV4Any.setStatus("current")


class _QtechHQoSTClassifierMatchV4AclID_Type(Integer32):
    """Custom type qtechHQoSTClassifierMatchV4AclID based on Integer32"""
    defaultValue = 0


_QtechHQoSTClassifierMatchV4AclID_Type.__name__ = "Integer32"
_QtechHQoSTClassifierMatchV4AclID_Object = MibTableColumn
qtechHQoSTClassifierMatchV4AclID = _QtechHQoSTClassifierMatchV4AclID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 8),
    _QtechHQoSTClassifierMatchV4AclID_Type()
)
qtechHQoSTClassifierMatchV4AclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV4AclID.setStatus("current")


class _QtechHQoSTClassifierV4AclName_Type(OctetString):
    """Custom type qtechHQoSTClassifierV4AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTClassifierV4AclName_Type.__name__ = "OctetString"
_QtechHQoSTClassifierV4AclName_Object = MibTableColumn
qtechHQoSTClassifierV4AclName = _QtechHQoSTClassifierV4AclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 9),
    _QtechHQoSTClassifierV4AclName_Type()
)
qtechHQoSTClassifierV4AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierV4AclName.setStatus("current")


class _QtechHQoSTClassifierMatchV4Dscp_Type(Integer32):
    """Custom type qtechHQoSTClassifierMatchV4Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QtechHQoSTClassifierMatchV4Dscp_Type.__name__ = "Integer32"
_QtechHQoSTClassifierMatchV4Dscp_Object = MibTableColumn
qtechHQoSTClassifierMatchV4Dscp = _QtechHQoSTClassifierMatchV4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 10),
    _QtechHQoSTClassifierMatchV4Dscp_Type()
)
qtechHQoSTClassifierMatchV4Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV4Dscp.setStatus("current")


class _QtechHQoSTClassifierMatchV4Tos_Type(Integer32):
    """Custom type qtechHQoSTClassifierMatchV4Tos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechHQoSTClassifierMatchV4Tos_Type.__name__ = "Integer32"
_QtechHQoSTClassifierMatchV4Tos_Object = MibTableColumn
qtechHQoSTClassifierMatchV4Tos = _QtechHQoSTClassifierMatchV4Tos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 11),
    _QtechHQoSTClassifierMatchV4Tos_Type()
)
qtechHQoSTClassifierMatchV4Tos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV4Tos.setStatus("current")


class _QtechHQoSTClassifierMatchV6Any_Type(TruthValue):
    """Custom type qtechHQoSTClassifierMatchV6Any based on TruthValue"""
    defaultValue = 2


_QtechHQoSTClassifierMatchV6Any_Type.__name__ = "TruthValue"
_QtechHQoSTClassifierMatchV6Any_Object = MibTableColumn
qtechHQoSTClassifierMatchV6Any = _QtechHQoSTClassifierMatchV6Any_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 12),
    _QtechHQoSTClassifierMatchV6Any_Type()
)
qtechHQoSTClassifierMatchV6Any.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV6Any.setStatus("current")
_QtechHQoSTClassifierMatchV6AclID_Type = Integer32
_QtechHQoSTClassifierMatchV6AclID_Object = MibTableColumn
qtechHQoSTClassifierMatchV6AclID = _QtechHQoSTClassifierMatchV6AclID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 13),
    _QtechHQoSTClassifierMatchV6AclID_Type()
)
qtechHQoSTClassifierMatchV6AclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV6AclID.setStatus("current")


class _QtechHQoSTClassifierV6AclName_Type(OctetString):
    """Custom type qtechHQoSTClassifierV6AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTClassifierV6AclName_Type.__name__ = "OctetString"
_QtechHQoSTClassifierV6AclName_Object = MibTableColumn
qtechHQoSTClassifierV6AclName = _QtechHQoSTClassifierV6AclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 14),
    _QtechHQoSTClassifierV6AclName_Type()
)
qtechHQoSTClassifierV6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierV6AclName.setStatus("current")


class _QtechHQoSTClassifierMatchV6Dscp_Type(Integer32):
    """Custom type qtechHQoSTClassifierMatchV6Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechHQoSTClassifierMatchV6Dscp_Type.__name__ = "Integer32"
_QtechHQoSTClassifierMatchV6Dscp_Object = MibTableColumn
qtechHQoSTClassifierMatchV6Dscp = _QtechHQoSTClassifierMatchV6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 15),
    _QtechHQoSTClassifierMatchV6Dscp_Type()
)
qtechHQoSTClassifierMatchV6Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchV6Dscp.setStatus("current")


class _QtechHQoSTClassifierMatchCos_Type(Integer32):
    """Custom type qtechHQoSTClassifierMatchCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechHQoSTClassifierMatchCos_Type.__name__ = "Integer32"
_QtechHQoSTClassifierMatchCos_Object = MibTableColumn
qtechHQoSTClassifierMatchCos = _QtechHQoSTClassifierMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 16),
    _QtechHQoSTClassifierMatchCos_Type()
)
qtechHQoSTClassifierMatchCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchCos.setStatus("current")


class _QtechHQoSTClassifierMatchExp_Type(Integer32):
    """Custom type qtechHQoSTClassifierMatchExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechHQoSTClassifierMatchExp_Type.__name__ = "Integer32"
_QtechHQoSTClassifierMatchExp_Object = MibTableColumn
qtechHQoSTClassifierMatchExp = _QtechHQoSTClassifierMatchExp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 17),
    _QtechHQoSTClassifierMatchExp_Type()
)
qtechHQoSTClassifierMatchExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchExp.setStatus("current")
_QtechHQoSTClassifierMatchSrcMac_Type = MacAddress
_QtechHQoSTClassifierMatchSrcMac_Object = MibTableColumn
qtechHQoSTClassifierMatchSrcMac = _QtechHQoSTClassifierMatchSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 18),
    _QtechHQoSTClassifierMatchSrcMac_Type()
)
qtechHQoSTClassifierMatchSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchSrcMac.setStatus("current")
_QtechHQoSTClassifierMatchDstMac_Type = MacAddress
_QtechHQoSTClassifierMatchDstMac_Object = MibTableColumn
qtechHQoSTClassifierMatchDstMac = _QtechHQoSTClassifierMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 6, 2, 1, 19),
    _QtechHQoSTClassifierMatchDstMac_Type()
)
qtechHQoSTClassifierMatchDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTClassifierMatchDstMac.setStatus("current")
_QtechHQoSTBehaviorObjects_ObjectIdentity = ObjectIdentity
qtechHQoSTBehaviorObjects = _QtechHQoSTBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7)
)
_QtechHQoSTBehaviorIndexNext_Type = Integer32
_QtechHQoSTBehaviorIndexNext_Object = MibScalar
qtechHQoSTBehaviorIndexNext = _QtechHQoSTBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 1),
    _QtechHQoSTBehaviorIndexNext_Type()
)
qtechHQoSTBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorIndexNext.setStatus("current")
_QtechHQoSTBehaviorTable_Object = MibTable
qtechHQoSTBehaviorTable = _QtechHQoSTBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorTable.setStatus("current")
_QtechHQoSTBehaviorEntry_Object = MibTableRow
qtechHQoSTBehaviorEntry = _QtechHQoSTBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1)
)
qtechHQoSTBehaviorEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSTBehaviorIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorEntry.setStatus("current")
_QtechHQoSTBehaviorIndex_Type = Unsigned32
_QtechHQoSTBehaviorIndex_Object = MibTableColumn
qtechHQoSTBehaviorIndex = _QtechHQoSTBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 1),
    _QtechHQoSTBehaviorIndex_Type()
)
qtechHQoSTBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorIndex.setStatus("current")


class _QtechHQoSTBehaviorName_Type(OctetString):
    """Custom type qtechHQoSTBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTBehaviorName_Type.__name__ = "OctetString"
_QtechHQoSTBehaviorName_Object = MibTableColumn
qtechHQoSTBehaviorName = _QtechHQoSTBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 2),
    _QtechHQoSTBehaviorName_Type()
)
qtechHQoSTBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorName.setStatus("current")
_QtechHQoSTBehaviorRowStatus_Type = RowStatus
_QtechHQoSTBehaviorRowStatus_Object = MibTableColumn
qtechHQoSTBehaviorRowStatus = _QtechHQoSTBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 3),
    _QtechHQoSTBehaviorRowStatus_Type()
)
qtechHQoSTBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorRowStatus.setStatus("current")


class _QtechHQoSTBehaviorMask_Type(Bits):
    """Custom type qtechHQoSTBehaviorMask based on Bits"""
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

_QtechHQoSTBehaviorMask_Type.__name__ = "Bits"
_QtechHQoSTBehaviorMask_Object = MibTableColumn
qtechHQoSTBehaviorMask = _QtechHQoSTBehaviorMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 4),
    _QtechHQoSTBehaviorMask_Type()
)
qtechHQoSTBehaviorMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorMask.setStatus("current")


class _QtechHQoSTBehaviorUserQName_Type(OctetString):
    """Custom type qtechHQoSTBehaviorUserQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTBehaviorUserQName_Type.__name__ = "OctetString"
_QtechHQoSTBehaviorUserQName_Object = MibTableColumn
qtechHQoSTBehaviorUserQName = _QtechHQoSTBehaviorUserQName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 5),
    _QtechHQoSTBehaviorUserQName_Type()
)
qtechHQoSTBehaviorUserQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorUserQName.setStatus("current")


class _QtechHQoSTBehaviorTCos_Type(QtechCosType):
    """Custom type qtechHQoSTBehaviorTCos based on QtechCosType"""
    defaultValue = 1


_QtechHQoSTBehaviorTCos_Type.__name__ = "QtechCosType"
_QtechHQoSTBehaviorTCos_Object = MibTableColumn
qtechHQoSTBehaviorTCos = _QtechHQoSTBehaviorTCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 6),
    _QtechHQoSTBehaviorTCos_Type()
)
qtechHQoSTBehaviorTCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorTCos.setStatus("current")


class _QtechHQoSTBehaviorTColor_Type(Integer32):
    """Custom type qtechHQoSTBehaviorTColor based on Integer32"""
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


_QtechHQoSTBehaviorTColor_Type.__name__ = "Integer32"
_QtechHQoSTBehaviorTColor_Object = MibTableColumn
qtechHQoSTBehaviorTColor = _QtechHQoSTBehaviorTColor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 7),
    _QtechHQoSTBehaviorTColor_Type()
)
qtechHQoSTBehaviorTColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorTColor.setStatus("current")


class _QtechHQoSTBehaviorRV4Dscp_Type(Integer32):
    """Custom type qtechHQoSTBehaviorRV4Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QtechHQoSTBehaviorRV4Dscp_Type.__name__ = "Integer32"
_QtechHQoSTBehaviorRV4Dscp_Object = MibTableColumn
qtechHQoSTBehaviorRV4Dscp = _QtechHQoSTBehaviorRV4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 8),
    _QtechHQoSTBehaviorRV4Dscp_Type()
)
qtechHQoSTBehaviorRV4Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorRV4Dscp.setStatus("current")


class _QtechHQoSTBehaviorRV4Tos_Type(Integer32):
    """Custom type qtechHQoSTBehaviorRV4Tos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechHQoSTBehaviorRV4Tos_Type.__name__ = "Integer32"
_QtechHQoSTBehaviorRV4Tos_Object = MibTableColumn
qtechHQoSTBehaviorRV4Tos = _QtechHQoSTBehaviorRV4Tos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 9),
    _QtechHQoSTBehaviorRV4Tos_Type()
)
qtechHQoSTBehaviorRV4Tos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorRV4Tos.setStatus("current")


class _QtechHQoSTBehaviorRV6Dscp_Type(Integer32):
    """Custom type qtechHQoSTBehaviorRV6Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechHQoSTBehaviorRV6Dscp_Type.__name__ = "Integer32"
_QtechHQoSTBehaviorRV6Dscp_Object = MibTableColumn
qtechHQoSTBehaviorRV6Dscp = _QtechHQoSTBehaviorRV6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 10),
    _QtechHQoSTBehaviorRV6Dscp_Type()
)
qtechHQoSTBehaviorRV6Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorRV6Dscp.setStatus("current")


class _QtechHQoSTBehaviorRVlanCos_Type(Integer32):
    """Custom type qtechHQoSTBehaviorRVlanCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechHQoSTBehaviorRVlanCos_Type.__name__ = "Integer32"
_QtechHQoSTBehaviorRVlanCos_Object = MibTableColumn
qtechHQoSTBehaviorRVlanCos = _QtechHQoSTBehaviorRVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 11),
    _QtechHQoSTBehaviorRVlanCos_Type()
)
qtechHQoSTBehaviorRVlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorRVlanCos.setStatus("current")


class _QtechHQoSTBehaviorRExp_Type(Integer32):
    """Custom type qtechHQoSTBehaviorRExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechHQoSTBehaviorRExp_Type.__name__ = "Integer32"
_QtechHQoSTBehaviorRExp_Object = MibTableColumn
qtechHQoSTBehaviorRExp = _QtechHQoSTBehaviorRExp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 12),
    _QtechHQoSTBehaviorRExp_Type()
)
qtechHQoSTBehaviorRExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorRExp.setStatus("current")


class _QtechHQoSTBehaviorSubPolicyName_Type(OctetString):
    """Custom type qtechHQoSTBehaviorSubPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTBehaviorSubPolicyName_Type.__name__ = "OctetString"
_QtechHQoSTBehaviorSubPolicyName_Object = MibTableColumn
qtechHQoSTBehaviorSubPolicyName = _QtechHQoSTBehaviorSubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 7, 2, 1, 13),
    _QtechHQoSTBehaviorSubPolicyName_Type()
)
qtechHQoSTBehaviorSubPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTBehaviorSubPolicyName.setStatus("current")
_QtechHQoSTPolicyObjects_ObjectIdentity = ObjectIdentity
qtechHQoSTPolicyObjects = _QtechHQoSTPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8)
)
_QtechHQoSTPolicyIndexNext_Type = Integer32
_QtechHQoSTPolicyIndexNext_Object = MibScalar
qtechHQoSTPolicyIndexNext = _QtechHQoSTPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 1),
    _QtechHQoSTPolicyIndexNext_Type()
)
qtechHQoSTPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyIndexNext.setStatus("current")
_QtechHQoSTPolicyTable_Object = MibTable
qtechHQoSTPolicyTable = _QtechHQoSTPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSTPolicyTable.setStatus("current")
_QtechHQoSTPolicyEntry_Object = MibTableRow
qtechHQoSTPolicyEntry = _QtechHQoSTPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 2, 1)
)
qtechHQoSTPolicyEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSTPolicyIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSTPolicyEntry.setStatus("current")
_QtechHQoSTPolicyIndex_Type = Unsigned32
_QtechHQoSTPolicyIndex_Object = MibTableColumn
qtechHQoSTPolicyIndex = _QtechHQoSTPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 2, 1, 1),
    _QtechHQoSTPolicyIndex_Type()
)
qtechHQoSTPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyIndex.setStatus("current")


class _QtechHQoSTPolicyName_Type(OctetString):
    """Custom type qtechHQoSTPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTPolicyName_Type.__name__ = "OctetString"
_QtechHQoSTPolicyName_Object = MibTableColumn
qtechHQoSTPolicyName = _QtechHQoSTPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 2, 1, 2),
    _QtechHQoSTPolicyName_Type()
)
qtechHQoSTPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyName.setStatus("current")
_QtechHQoSTPolicyRowStatus_Type = RowStatus
_QtechHQoSTPolicyRowStatus_Object = MibTableColumn
qtechHQoSTPolicyRowStatus = _QtechHQoSTPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 2, 1, 3),
    _QtechHQoSTPolicyRowStatus_Type()
)
qtechHQoSTPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyRowStatus.setStatus("current")
_QtechHQoSTPolicyMapIndexNext_Type = Integer32
_QtechHQoSTPolicyMapIndexNext_Object = MibScalar
qtechHQoSTPolicyMapIndexNext = _QtechHQoSTPolicyMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 3),
    _QtechHQoSTPolicyMapIndexNext_Type()
)
qtechHQoSTPolicyMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapIndexNext.setStatus("current")
_QtechHQoSTPolicyMapTable_Object = MibTable
qtechHQoSTPolicyMapTable = _QtechHQoSTPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4)
)
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapTable.setStatus("current")
_QtechHQoSTPolicyMapEntry_Object = MibTableRow
qtechHQoSTPolicyMapEntry = _QtechHQoSTPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1)
)
qtechHQoSTPolicyMapEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSTPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapEntry.setStatus("current")
_QtechHQoSTPolicyMapIndex_Type = Unsigned32
_QtechHQoSTPolicyMapIndex_Object = MibTableColumn
qtechHQoSTPolicyMapIndex = _QtechHQoSTPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 1),
    _QtechHQoSTPolicyMapIndex_Type()
)
qtechHQoSTPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapIndex.setStatus("current")


class _QtechHQoSTPolicyMapPolicyName_Type(OctetString):
    """Custom type qtechHQoSTPolicyMapPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTPolicyMapPolicyName_Type.__name__ = "OctetString"
_QtechHQoSTPolicyMapPolicyName_Object = MibTableColumn
qtechHQoSTPolicyMapPolicyName = _QtechHQoSTPolicyMapPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 2),
    _QtechHQoSTPolicyMapPolicyName_Type()
)
qtechHQoSTPolicyMapPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapPolicyName.setStatus("current")
_QtechHQoSTPolicyMapPolicyIndex_Type = Unsigned32
_QtechHQoSTPolicyMapPolicyIndex_Object = MibTableColumn
qtechHQoSTPolicyMapPolicyIndex = _QtechHQoSTPolicyMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 3),
    _QtechHQoSTPolicyMapPolicyIndex_Type()
)
qtechHQoSTPolicyMapPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapPolicyIndex.setStatus("current")


class _QtechHQoSTPolicyMapTClassfierName_Type(OctetString):
    """Custom type qtechHQoSTPolicyMapTClassfierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTPolicyMapTClassfierName_Type.__name__ = "OctetString"
_QtechHQoSTPolicyMapTClassfierName_Object = MibTableColumn
qtechHQoSTPolicyMapTClassfierName = _QtechHQoSTPolicyMapTClassfierName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 4),
    _QtechHQoSTPolicyMapTClassfierName_Type()
)
qtechHQoSTPolicyMapTClassfierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapTClassfierName.setStatus("current")
_QtechHQoSTPolicyMapTClassfierIndex_Type = Unsigned32
_QtechHQoSTPolicyMapTClassfierIndex_Object = MibTableColumn
qtechHQoSTPolicyMapTClassfierIndex = _QtechHQoSTPolicyMapTClassfierIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 5),
    _QtechHQoSTPolicyMapTClassfierIndex_Type()
)
qtechHQoSTPolicyMapTClassfierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapTClassfierIndex.setStatus("current")


class _QtechHQoSTPolicyMapTBehaviorName_Type(OctetString):
    """Custom type qtechHQoSTPolicyMapTBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSTPolicyMapTBehaviorName_Type.__name__ = "OctetString"
_QtechHQoSTPolicyMapTBehaviorName_Object = MibTableColumn
qtechHQoSTPolicyMapTBehaviorName = _QtechHQoSTPolicyMapTBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 6),
    _QtechHQoSTPolicyMapTBehaviorName_Type()
)
qtechHQoSTPolicyMapTBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapTBehaviorName.setStatus("current")
_QtechHQoSTPolicyMapTBehaviorIndex_Type = Unsigned32
_QtechHQoSTPolicyMapTBehaviorIndex_Object = MibTableColumn
qtechHQoSTPolicyMapTBehaviorIndex = _QtechHQoSTPolicyMapTBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 7),
    _QtechHQoSTPolicyMapTBehaviorIndex_Type()
)
qtechHQoSTPolicyMapTBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapTBehaviorIndex.setStatus("current")


class _QtechHQoSTPolicyMapPrecedence_Type(Unsigned32):
    """Custom type qtechHQoSTPolicyMapPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_QtechHQoSTPolicyMapPrecedence_Type.__name__ = "Unsigned32"
_QtechHQoSTPolicyMapPrecedence_Object = MibTableColumn
qtechHQoSTPolicyMapPrecedence = _QtechHQoSTPolicyMapPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 8),
    _QtechHQoSTPolicyMapPrecedence_Type()
)
qtechHQoSTPolicyMapPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapPrecedence.setStatus("current")
_QtechHQoSTPolicyMapRowStatus_Type = RowStatus
_QtechHQoSTPolicyMapRowStatus_Object = MibTableColumn
qtechHQoSTPolicyMapRowStatus = _QtechHQoSTPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 8, 4, 1, 9),
    _QtechHQoSTPolicyMapRowStatus_Type()
)
qtechHQoSTPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSTPolicyMapRowStatus.setStatus("current")
_QtechHQoSVoQObjects_ObjectIdentity = ObjectIdentity
qtechHQoSVoQObjects = _QtechHQoSVoQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 9)
)


class _QtechHQoSVoQEnable_Type(TruthValue):
    """Custom type qtechHQoSVoQEnable based on TruthValue"""
    defaultValue = 2


_QtechHQoSVoQEnable_Type.__name__ = "TruthValue"
_QtechHQoSVoQEnable_Object = MibScalar
qtechHQoSVoQEnable = _QtechHQoSVoQEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 9, 1),
    _QtechHQoSVoQEnable_Type()
)
qtechHQoSVoQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSVoQEnable.setStatus("current")
_QtechHQoSVoQDeviceTable_Object = MibTable
qtechHQoSVoQDeviceTable = _QtechHQoSVoQDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 9, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSVoQDeviceTable.setStatus("current")
_QtechHQoSVoQDeviceEntry_Object = MibTableRow
qtechHQoSVoQDeviceEntry = _QtechHQoSVoQDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 9, 2, 1)
)
qtechHQoSVoQDeviceEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSVoQDeviceId"),
)
if mibBuilder.loadTexts:
    qtechHQoSVoQDeviceEntry.setStatus("current")
_QtechHQoSVoQDeviceId_Type = Unsigned32
_QtechHQoSVoQDeviceId_Object = MibTableColumn
qtechHQoSVoQDeviceId = _QtechHQoSVoQDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 9, 2, 1, 1),
    _QtechHQoSVoQDeviceId_Type()
)
qtechHQoSVoQDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSVoQDeviceId.setStatus("current")
_QtechHQoSVoQDeviceCredit_Type = Unsigned32
_QtechHQoSVoQDeviceCredit_Object = MibTableColumn
qtechHQoSVoQDeviceCredit = _QtechHQoSVoQDeviceCredit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 9, 2, 1, 2),
    _QtechHQoSVoQDeviceCredit_Type()
)
qtechHQoSVoQDeviceCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSVoQDeviceCredit.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSVoQDeviceCredit.setUnits("Mbit/s")
_QtechHQoSPortQObjects_ObjectIdentity = ObjectIdentity
qtechHQoSPortQObjects = _QtechHQoSPortQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10)
)
_QtechHQoSPortQIndexNext_Type = Integer32
_QtechHQoSPortQIndexNext_Object = MibScalar
qtechHQoSPortQIndexNext = _QtechHQoSPortQIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 1),
    _QtechHQoSPortQIndexNext_Type()
)
qtechHQoSPortQIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSPortQIndexNext.setStatus("current")
_QtechHQoSPortQTable_Object = MibTable
qtechHQoSPortQTable = _QtechHQoSPortQTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2)
)
if mibBuilder.loadTexts:
    qtechHQoSPortQTable.setStatus("current")
_QtechHQoSPortQEntry_Object = MibTableRow
qtechHQoSPortQEntry = _QtechHQoSPortQEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1)
)
qtechHQoSPortQEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSPortQIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSPortQEntry.setStatus("current")
_QtechHQoSPortQIndex_Type = Unsigned32
_QtechHQoSPortQIndex_Object = MibTableColumn
qtechHQoSPortQIndex = _QtechHQoSPortQIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 1),
    _QtechHQoSPortQIndex_Type()
)
qtechHQoSPortQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSPortQIndex.setStatus("current")


class _QtechHQoSPortQName_Type(OctetString):
    """Custom type qtechHQoSPortQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQName_Type.__name__ = "OctetString"
_QtechHQoSPortQName_Object = MibTableColumn
qtechHQoSPortQName = _QtechHQoSPortQName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 2),
    _QtechHQoSPortQName_Type()
)
qtechHQoSPortQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQName.setStatus("current")
_QtechHQoSPortQRowStatus_Type = RowStatus
_QtechHQoSPortQRowStatus_Object = MibTableColumn
qtechHQoSPortQRowStatus = _QtechHQoSPortQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 3),
    _QtechHQoSPortQRowStatus_Type()
)
qtechHQoSPortQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQRowStatus.setStatus("current")


class _QtechHQoSPortQBEQType_Type(QtechQType):
    """Custom type qtechHQoSPortQBEQType based on QtechQType"""
    defaultValue = 2


_QtechHQoSPortQBEQType_Type.__name__ = "QtechQType"
_QtechHQoSPortQBEQType_Object = MibTableColumn
qtechHQoSPortQBEQType = _QtechHQoSPortQBEQType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 4),
    _QtechHQoSPortQBEQType_Type()
)
qtechHQoSPortQBEQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQBEQType.setStatus("current")


class _QtechHQoSPortQBEQWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQBEQWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQBEQWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQBEQWredWeight_Object = MibTableColumn
qtechHQoSPortQBEQWredWeight = _QtechHQoSPortQBEQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 5),
    _QtechHQoSPortQBEQWredWeight_Type()
)
qtechHQoSPortQBEQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQBEQWredWeight.setStatus("current")


class _QtechHQoSPortQBEQWredName_Type(OctetString):
    """Custom type qtechHQoSPortQBEQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQBEQWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQBEQWredName_Object = MibTableColumn
qtechHQoSPortQBEQWredName = _QtechHQoSPortQBEQWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 6),
    _QtechHQoSPortQBEQWredName_Type()
)
qtechHQoSPortQBEQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQBEQWredName.setStatus("current")


class _QtechHQoSPortQBEQDepth_Type(Integer32):
    """Custom type qtechHQoSPortQBEQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQBEQDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQBEQDepth_Object = MibTableColumn
qtechHQoSPortQBEQDepth = _QtechHQoSPortQBEQDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 7),
    _QtechHQoSPortQBEQDepth_Type()
)
qtechHQoSPortQBEQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQBEQDepth.setStatus("current")


class _QtechHQoSPortQBEQShaping_Type(Integer32):
    """Custom type qtechHQoSPortQBEQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQBEQShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQBEQShaping_Object = MibTableColumn
qtechHQoSPortQBEQShaping = _QtechHQoSPortQBEQShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 8),
    _QtechHQoSPortQBEQShaping_Type()
)
qtechHQoSPortQBEQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQBEQShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQBEQShaping.setUnits("kilobits per second")


class _QtechHQoSPortQAF1QType_Type(QtechQType):
    """Custom type qtechHQoSPortQAF1QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSPortQAF1QType_Type.__name__ = "QtechQType"
_QtechHQoSPortQAF1QType_Object = MibTableColumn
qtechHQoSPortQAF1QType = _QtechHQoSPortQAF1QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 9),
    _QtechHQoSPortQAF1QType_Type()
)
qtechHQoSPortQAF1QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF1QType.setStatus("current")


class _QtechHQoSPortQAF1QWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQAF1QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQAF1QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQAF1QWredWeight_Object = MibTableColumn
qtechHQoSPortQAF1QWredWeight = _QtechHQoSPortQAF1QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 10),
    _QtechHQoSPortQAF1QWredWeight_Type()
)
qtechHQoSPortQAF1QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF1QWredWeight.setStatus("current")


class _QtechHQoSPortQAF1QWredName_Type(OctetString):
    """Custom type qtechHQoSPortQAF1QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQAF1QWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQAF1QWredName_Object = MibTableColumn
qtechHQoSPortQAF1QWredName = _QtechHQoSPortQAF1QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 11),
    _QtechHQoSPortQAF1QWredName_Type()
)
qtechHQoSPortQAF1QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF1QWredName.setStatus("current")


class _QtechHQoSPortQAF1QDepth_Type(Integer32):
    """Custom type qtechHQoSPortQAF1QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQAF1QDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQAF1QDepth_Object = MibTableColumn
qtechHQoSPortQAF1QDepth = _QtechHQoSPortQAF1QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 12),
    _QtechHQoSPortQAF1QDepth_Type()
)
qtechHQoSPortQAF1QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF1QDepth.setStatus("current")


class _QtechHQoSPortQAF1QShaping_Type(Integer32):
    """Custom type qtechHQoSPortQAF1QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQAF1QShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQAF1QShaping_Object = MibTableColumn
qtechHQoSPortQAF1QShaping = _QtechHQoSPortQAF1QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 13),
    _QtechHQoSPortQAF1QShaping_Type()
)
qtechHQoSPortQAF1QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF1QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF1QShaping.setUnits("kilobits per second")


class _QtechHQoSPortQAF2QType_Type(QtechQType):
    """Custom type qtechHQoSPortQAF2QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSPortQAF2QType_Type.__name__ = "QtechQType"
_QtechHQoSPortQAF2QType_Object = MibTableColumn
qtechHQoSPortQAF2QType = _QtechHQoSPortQAF2QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 14),
    _QtechHQoSPortQAF2QType_Type()
)
qtechHQoSPortQAF2QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF2QType.setStatus("current")


class _QtechHQoSPortQAF2QWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQAF2QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_QtechHQoSPortQAF2QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQAF2QWredWeight_Object = MibTableColumn
qtechHQoSPortQAF2QWredWeight = _QtechHQoSPortQAF2QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 15),
    _QtechHQoSPortQAF2QWredWeight_Type()
)
qtechHQoSPortQAF2QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF2QWredWeight.setStatus("current")


class _QtechHQoSPortQAF2QWredName_Type(OctetString):
    """Custom type qtechHQoSPortQAF2QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQAF2QWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQAF2QWredName_Object = MibTableColumn
qtechHQoSPortQAF2QWredName = _QtechHQoSPortQAF2QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 16),
    _QtechHQoSPortQAF2QWredName_Type()
)
qtechHQoSPortQAF2QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF2QWredName.setStatus("current")


class _QtechHQoSPortQAF2QDepth_Type(Integer32):
    """Custom type qtechHQoSPortQAF2QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQAF2QDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQAF2QDepth_Object = MibTableColumn
qtechHQoSPortQAF2QDepth = _QtechHQoSPortQAF2QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 17),
    _QtechHQoSPortQAF2QDepth_Type()
)
qtechHQoSPortQAF2QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF2QDepth.setStatus("current")


class _QtechHQoSPortQAF2QShaping_Type(Integer32):
    """Custom type qtechHQoSPortQAF2QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQAF2QShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQAF2QShaping_Object = MibTableColumn
qtechHQoSPortQAF2QShaping = _QtechHQoSPortQAF2QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 18),
    _QtechHQoSPortQAF2QShaping_Type()
)
qtechHQoSPortQAF2QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF2QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF2QShaping.setUnits("kilobits per second")


class _QtechHQoSPortQAF3QType_Type(QtechQType):
    """Custom type qtechHQoSPortQAF3QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSPortQAF3QType_Type.__name__ = "QtechQType"
_QtechHQoSPortQAF3QType_Object = MibTableColumn
qtechHQoSPortQAF3QType = _QtechHQoSPortQAF3QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 19),
    _QtechHQoSPortQAF3QType_Type()
)
qtechHQoSPortQAF3QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF3QType.setStatus("current")


class _QtechHQoSPortQAF3QWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQAF3QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQAF3QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQAF3QWredWeight_Object = MibTableColumn
qtechHQoSPortQAF3QWredWeight = _QtechHQoSPortQAF3QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 20),
    _QtechHQoSPortQAF3QWredWeight_Type()
)
qtechHQoSPortQAF3QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF3QWredWeight.setStatus("current")


class _QtechHQoSPortQAF3QWredName_Type(OctetString):
    """Custom type qtechHQoSPortQAF3QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQAF3QWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQAF3QWredName_Object = MibTableColumn
qtechHQoSPortQAF3QWredName = _QtechHQoSPortQAF3QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 21),
    _QtechHQoSPortQAF3QWredName_Type()
)
qtechHQoSPortQAF3QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF3QWredName.setStatus("current")


class _QtechHQoSPortQAF3QDepth_Type(Integer32):
    """Custom type qtechHQoSPortQAF3QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQAF3QDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQAF3QDepth_Object = MibTableColumn
qtechHQoSPortQAF3QDepth = _QtechHQoSPortQAF3QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 22),
    _QtechHQoSPortQAF3QDepth_Type()
)
qtechHQoSPortQAF3QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF3QDepth.setStatus("current")


class _QtechHQoSPortQAF3QShaping_Type(Integer32):
    """Custom type qtechHQoSPortQAF3QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQAF3QShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQAF3QShaping_Object = MibTableColumn
qtechHQoSPortQAF3QShaping = _QtechHQoSPortQAF3QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 23),
    _QtechHQoSPortQAF3QShaping_Type()
)
qtechHQoSPortQAF3QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF3QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF3QShaping.setUnits("kilobits per second")


class _QtechHQoSPortQAF4QType_Type(QtechQType):
    """Custom type qtechHQoSPortQAF4QType based on QtechQType"""
    defaultValue = 2


_QtechHQoSPortQAF4QType_Type.__name__ = "QtechQType"
_QtechHQoSPortQAF4QType_Object = MibTableColumn
qtechHQoSPortQAF4QType = _QtechHQoSPortQAF4QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 24),
    _QtechHQoSPortQAF4QType_Type()
)
qtechHQoSPortQAF4QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF4QType.setStatus("current")


class _QtechHQoSPortQAF4QWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQAF4QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQAF4QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQAF4QWredWeight_Object = MibTableColumn
qtechHQoSPortQAF4QWredWeight = _QtechHQoSPortQAF4QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 25),
    _QtechHQoSPortQAF4QWredWeight_Type()
)
qtechHQoSPortQAF4QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF4QWredWeight.setStatus("current")


class _QtechHQoSPortQAF4QWredName_Type(OctetString):
    """Custom type qtechHQoSPortQAF4QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQAF4QWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQAF4QWredName_Object = MibTableColumn
qtechHQoSPortQAF4QWredName = _QtechHQoSPortQAF4QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 26),
    _QtechHQoSPortQAF4QWredName_Type()
)
qtechHQoSPortQAF4QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF4QWredName.setStatus("current")


class _QtechHQoSPortQAF4QDepth_Type(Integer32):
    """Custom type qtechHQoSPortQAF4QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQAF4QDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQAF4QDepth_Object = MibTableColumn
qtechHQoSPortQAF4QDepth = _QtechHQoSPortQAF4QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 27),
    _QtechHQoSPortQAF4QDepth_Type()
)
qtechHQoSPortQAF4QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF4QDepth.setStatus("current")


class _QtechHQoSPortQAF4QShaping_Type(Integer32):
    """Custom type qtechHQoSPortQAF4QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQAF4QShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQAF4QShaping_Object = MibTableColumn
qtechHQoSPortQAF4QShaping = _QtechHQoSPortQAF4QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 28),
    _QtechHQoSPortQAF4QShaping_Type()
)
qtechHQoSPortQAF4QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF4QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQAF4QShaping.setUnits("kilobits per second")


class _QtechHQoSPortQEFQType_Type(QtechQType):
    """Custom type qtechHQoSPortQEFQType based on QtechQType"""
    defaultValue = 3


_QtechHQoSPortQEFQType_Type.__name__ = "QtechQType"
_QtechHQoSPortQEFQType_Object = MibTableColumn
qtechHQoSPortQEFQType = _QtechHQoSPortQEFQType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 29),
    _QtechHQoSPortQEFQType_Type()
)
qtechHQoSPortQEFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQEFQType.setStatus("current")


class _QtechHQoSPortQEFQWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQEFQWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQEFQWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQEFQWredWeight_Object = MibTableColumn
qtechHQoSPortQEFQWredWeight = _QtechHQoSPortQEFQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 30),
    _QtechHQoSPortQEFQWredWeight_Type()
)
qtechHQoSPortQEFQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQEFQWredWeight.setStatus("current")


class _QtechHQoSPortQEFQWredName_Type(OctetString):
    """Custom type qtechHQoSPortQEFQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQEFQWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQEFQWredName_Object = MibTableColumn
qtechHQoSPortQEFQWredName = _QtechHQoSPortQEFQWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 31),
    _QtechHQoSPortQEFQWredName_Type()
)
qtechHQoSPortQEFQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQEFQWredName.setStatus("current")


class _QtechHQoSPortQEFQDepth_Type(Integer32):
    """Custom type qtechHQoSPortQEFQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQEFQDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQEFQDepth_Object = MibTableColumn
qtechHQoSPortQEFQDepth = _QtechHQoSPortQEFQDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 32),
    _QtechHQoSPortQEFQDepth_Type()
)
qtechHQoSPortQEFQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQEFQDepth.setStatus("current")


class _QtechHQoSPortQEFQShaping_Type(Integer32):
    """Custom type qtechHQoSPortQEFQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQEFQShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQEFQShaping_Object = MibTableColumn
qtechHQoSPortQEFQShaping = _QtechHQoSPortQEFQShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 33),
    _QtechHQoSPortQEFQShaping_Type()
)
qtechHQoSPortQEFQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQEFQShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQEFQShaping.setUnits("kilobits per second")


class _QtechHQoSPortQCS6QType_Type(QtechQType):
    """Custom type qtechHQoSPortQCS6QType based on QtechQType"""
    defaultValue = 3


_QtechHQoSPortQCS6QType_Type.__name__ = "QtechQType"
_QtechHQoSPortQCS6QType_Object = MibTableColumn
qtechHQoSPortQCS6QType = _QtechHQoSPortQCS6QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 34),
    _QtechHQoSPortQCS6QType_Type()
)
qtechHQoSPortQCS6QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS6QType.setStatus("current")


class _QtechHQoSPortQCS6QWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQCS6QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQCS6QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQCS6QWredWeight_Object = MibTableColumn
qtechHQoSPortQCS6QWredWeight = _QtechHQoSPortQCS6QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 35),
    _QtechHQoSPortQCS6QWredWeight_Type()
)
qtechHQoSPortQCS6QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS6QWredWeight.setStatus("current")


class _QtechHQoSPortQCS6QWredName_Type(OctetString):
    """Custom type qtechHQoSPortQCS6QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQCS6QWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQCS6QWredName_Object = MibTableColumn
qtechHQoSPortQCS6QWredName = _QtechHQoSPortQCS6QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 36),
    _QtechHQoSPortQCS6QWredName_Type()
)
qtechHQoSPortQCS6QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS6QWredName.setStatus("current")


class _QtechHQoSPortQCS6QDepth_Type(Integer32):
    """Custom type qtechHQoSPortQCS6QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQCS6QDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQCS6QDepth_Object = MibTableColumn
qtechHQoSPortQCS6QDepth = _QtechHQoSPortQCS6QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 37),
    _QtechHQoSPortQCS6QDepth_Type()
)
qtechHQoSPortQCS6QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS6QDepth.setStatus("current")


class _QtechHQoSPortQCS6QShaping_Type(Integer32):
    """Custom type qtechHQoSPortQCS6QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQCS6QShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQCS6QShaping_Object = MibTableColumn
qtechHQoSPortQCS6QShaping = _QtechHQoSPortQCS6QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 38),
    _QtechHQoSPortQCS6QShaping_Type()
)
qtechHQoSPortQCS6QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS6QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS6QShaping.setUnits("kilobits per second")


class _QtechHQoSPortQCS7QType_Type(QtechQType):
    """Custom type qtechHQoSPortQCS7QType based on QtechQType"""
    defaultValue = 3


_QtechHQoSPortQCS7QType_Type.__name__ = "QtechQType"
_QtechHQoSPortQCS7QType_Object = MibTableColumn
qtechHQoSPortQCS7QType = _QtechHQoSPortQCS7QType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 39),
    _QtechHQoSPortQCS7QType_Type()
)
qtechHQoSPortQCS7QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS7QType.setStatus("current")


class _QtechHQoSPortQCS7QWredWeight_Type(Integer32):
    """Custom type qtechHQoSPortQCS7QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_QtechHQoSPortQCS7QWredWeight_Type.__name__ = "Integer32"
_QtechHQoSPortQCS7QWredWeight_Object = MibTableColumn
qtechHQoSPortQCS7QWredWeight = _QtechHQoSPortQCS7QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 40),
    _QtechHQoSPortQCS7QWredWeight_Type()
)
qtechHQoSPortQCS7QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS7QWredWeight.setStatus("current")


class _QtechHQoSPortQCS7QWredName_Type(OctetString):
    """Custom type qtechHQoSPortQCS7QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSPortQCS7QWredName_Type.__name__ = "OctetString"
_QtechHQoSPortQCS7QWredName_Object = MibTableColumn
qtechHQoSPortQCS7QWredName = _QtechHQoSPortQCS7QWredName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 41),
    _QtechHQoSPortQCS7QWredName_Type()
)
qtechHQoSPortQCS7QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS7QWredName.setStatus("current")


class _QtechHQoSPortQCS7QDepth_Type(Integer32):
    """Custom type qtechHQoSPortQCS7QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QtechHQoSPortQCS7QDepth_Type.__name__ = "Integer32"
_QtechHQoSPortQCS7QDepth_Object = MibTableColumn
qtechHQoSPortQCS7QDepth = _QtechHQoSPortQCS7QDepth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 42),
    _QtechHQoSPortQCS7QDepth_Type()
)
qtechHQoSPortQCS7QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS7QDepth.setStatus("current")


class _QtechHQoSPortQCS7QShaping_Type(Integer32):
    """Custom type qtechHQoSPortQCS7QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSPortQCS7QShaping_Type.__name__ = "Integer32"
_QtechHQoSPortQCS7QShaping_Object = MibTableColumn
qtechHQoSPortQCS7QShaping = _QtechHQoSPortQCS7QShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 10, 2, 1, 43),
    _QtechHQoSPortQCS7QShaping_Type()
)
qtechHQoSPortQCS7QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS7QShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSPortQCS7QShaping.setUnits("kilobits per second")
_QtechHQoSIfAppObjects_ObjectIdentity = ObjectIdentity
qtechHQoSIfAppObjects = _QtechHQoSIfAppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11)
)
_QtechHQoSIfAppTable_Object = MibTable
qtechHQoSIfAppTable = _QtechHQoSIfAppTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1)
)
if mibBuilder.loadTexts:
    qtechHQoSIfAppTable.setStatus("current")
_QtechHQoSIfAppEntry_Object = MibTableRow
qtechHQoSIfAppEntry = _QtechHQoSIfAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1)
)
qtechHQoSIfAppEntry.setIndexNames(
    (0, "QTECH-ROUTER-QOS-MIB", "qtechHQoSIfAppIndex"),
)
if mibBuilder.loadTexts:
    qtechHQoSIfAppEntry.setStatus("current")
_QtechHQoSIfAppIndex_Type = InterfaceIndex
_QtechHQoSIfAppIndex_Object = MibTableColumn
qtechHQoSIfAppIndex = _QtechHQoSIfAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 1),
    _QtechHQoSIfAppIndex_Type()
)
qtechHQoSIfAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechHQoSIfAppIndex.setStatus("current")


class _QtechHQoSIfAppInPolicyName_Type(OctetString):
    """Custom type qtechHQoSIfAppInPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSIfAppInPolicyName_Type.__name__ = "OctetString"
_QtechHQoSIfAppInPolicyName_Object = MibTableColumn
qtechHQoSIfAppInPolicyName = _QtechHQoSIfAppInPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 2),
    _QtechHQoSIfAppInPolicyName_Type()
)
qtechHQoSIfAppInPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSIfAppInPolicyName.setStatus("current")
_QtechHQoSIfAppInPolicyIndex_Type = Unsigned32
_QtechHQoSIfAppInPolicyIndex_Object = MibTableColumn
qtechHQoSIfAppInPolicyIndex = _QtechHQoSIfAppInPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 3),
    _QtechHQoSIfAppInPolicyIndex_Type()
)
qtechHQoSIfAppInPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSIfAppInPolicyIndex.setStatus("current")


class _QtechHQoSIfAppInPolicyLayer_Type(QtechLayerType):
    """Custom type qtechHQoSIfAppInPolicyLayer based on QtechLayerType"""
    defaultValue = 2


_QtechHQoSIfAppInPolicyLayer_Type.__name__ = "QtechLayerType"
_QtechHQoSIfAppInPolicyLayer_Object = MibTableColumn
qtechHQoSIfAppInPolicyLayer = _QtechHQoSIfAppInPolicyLayer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 4),
    _QtechHQoSIfAppInPolicyLayer_Type()
)
qtechHQoSIfAppInPolicyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSIfAppInPolicyLayer.setStatus("current")


class _QtechHQoSIfAppOutPolicyName_Type(OctetString):
    """Custom type qtechHQoSIfAppOutPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSIfAppOutPolicyName_Type.__name__ = "OctetString"
_QtechHQoSIfAppOutPolicyName_Object = MibTableColumn
qtechHQoSIfAppOutPolicyName = _QtechHQoSIfAppOutPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 5),
    _QtechHQoSIfAppOutPolicyName_Type()
)
qtechHQoSIfAppOutPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSIfAppOutPolicyName.setStatus("current")
_QtechHQoSIfAppOutPolicyIndex_Type = Unsigned32
_QtechHQoSIfAppOutPolicyIndex_Object = MibTableColumn
qtechHQoSIfAppOutPolicyIndex = _QtechHQoSIfAppOutPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 6),
    _QtechHQoSIfAppOutPolicyIndex_Type()
)
qtechHQoSIfAppOutPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSIfAppOutPolicyIndex.setStatus("current")


class _QtechHQoSIfAppOutPolicyLayer_Type(QtechLayerType):
    """Custom type qtechHQoSIfAppOutPolicyLayer based on QtechLayerType"""
    defaultValue = 2


_QtechHQoSIfAppOutPolicyLayer_Type.__name__ = "QtechLayerType"
_QtechHQoSIfAppOutPolicyLayer_Object = MibTableColumn
qtechHQoSIfAppOutPolicyLayer = _QtechHQoSIfAppOutPolicyLayer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 7),
    _QtechHQoSIfAppOutPolicyLayer_Type()
)
qtechHQoSIfAppOutPolicyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSIfAppOutPolicyLayer.setStatus("current")


class _QtechHQoSIfAppPortQueueName_Type(OctetString):
    """Custom type qtechHQoSIfAppPortQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechHQoSIfAppPortQueueName_Type.__name__ = "OctetString"
_QtechHQoSIfAppPortQueueName_Object = MibTableColumn
qtechHQoSIfAppPortQueueName = _QtechHQoSIfAppPortQueueName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 8),
    _QtechHQoSIfAppPortQueueName_Type()
)
qtechHQoSIfAppPortQueueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSIfAppPortQueueName.setStatus("current")
_QtechHQoSIfAppPortQueueIndex_Type = Unsigned32
_QtechHQoSIfAppPortQueueIndex_Object = MibTableColumn
qtechHQoSIfAppPortQueueIndex = _QtechHQoSIfAppPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 9),
    _QtechHQoSIfAppPortQueueIndex_Type()
)
qtechHQoSIfAppPortQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechHQoSIfAppPortQueueIndex.setStatus("current")


class _QtechHQoSIfAppPortQueueShaping_Type(Integer32):
    """Custom type qtechHQoSIfAppPortQueueShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QtechHQoSIfAppPortQueueShaping_Type.__name__ = "Integer32"
_QtechHQoSIfAppPortQueueShaping_Object = MibTableColumn
qtechHQoSIfAppPortQueueShaping = _QtechHQoSIfAppPortQueueShaping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 106, 3, 11, 1, 1, 10),
    _QtechHQoSIfAppPortQueueShaping_Type()
)
qtechHQoSIfAppPortQueueShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechHQoSIfAppPortQueueShaping.setStatus("current")
if mibBuilder.loadTexts:
    qtechHQoSIfAppPortQueueShaping.setUnits("kilobits per second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ROUTER-QOS-MIB",
    **{"QtechCosType": QtechCosType,
       "QtechQType": QtechQType,
       "QtechQDirectionType": QtechQDirectionType,
       "QtechLayerType": QtechLayerType,
       "qtechRouterQoSMIB": qtechRouterQoSMIB,
       "qtechCBQoSMIBObjects": qtechCBQoSMIBObjects,
       "qtechCBQoSIfStaticsObjects": qtechCBQoSIfStaticsObjects,
       "qtechCBQoSIfCbwfqRunInfoTable": qtechCBQoSIfCbwfqRunInfoTable,
       "qtechCBQoSIfCbwfqRunInfoEntry": qtechCBQoSIfCbwfqRunInfoEntry,
       "qtechCBQoSIfCbwfqPolicyIfIndex": qtechCBQoSIfCbwfqPolicyIfIndex,
       "qtechCBQoSIfCbwfqQueueSize": qtechCBQoSIfCbwfqQueueSize,
       "qtechCBQoSIfCbwfqDiscard": qtechCBQoSIfCbwfqDiscard,
       "qtechCBQoSIfCbwfqEfQueueSize": qtechCBQoSIfCbwfqEfQueueSize,
       "qtechCBQoSIfCbwfqAfQueueSize": qtechCBQoSIfCbwfqAfQueueSize,
       "qtechCBQoSIfCbwfqBeQueueSize": qtechCBQoSIfCbwfqBeQueueSize,
       "qtechCBQoSIfCbwfqBeActiveQueueNum": qtechCBQoSIfCbwfqBeActiveQueueNum,
       "qtechCBQoSIfCbwfqBeMaxActiveQueueNum": qtechCBQoSIfCbwfqBeMaxActiveQueueNum,
       "qtechCBQoSIfCbwfqBeTotalQueueNum": qtechCBQoSIfCbwfqBeTotalQueueNum,
       "qtechCBQoSIfCbwfqAfAllocatedQueueNum": qtechCBQoSIfCbwfqAfAllocatedQueueNum,
       "qtechCBQoSIfClassMatchRunInfoTable": qtechCBQoSIfClassMatchRunInfoTable,
       "qtechCBQoSIfClassMatchRunInfoEntry": qtechCBQoSIfClassMatchRunInfoEntry,
       "qtechCBQoSIfClassMatchIfIndex": qtechCBQoSIfClassMatchIfIndex,
       "qtechCBQoSIfClassMatchPolicyDirection": qtechCBQoSIfClassMatchPolicyDirection,
       "qtechCBQoSIfClassMatchClassIndex": qtechCBQoSIfClassMatchClassIndex,
       "qtechCBQoSIfClassMatchedPackets": qtechCBQoSIfClassMatchedPackets,
       "qtechCBQoSIfClassMatchedBytes": qtechCBQoSIfClassMatchedBytes,
       "qtechCBQosIfClassPassedPackets": qtechCBQosIfClassPassedPackets,
       "qtechCBQosIfClassDroppedPackets": qtechCBQosIfClassDroppedPackets,
       "qtechCBQoSIfCarRunInfoTable": qtechCBQoSIfCarRunInfoTable,
       "qtechCBQoSIfCarRunInfoEntry": qtechCBQoSIfCarRunInfoEntry,
       "qtechCBQoSIfCarIfIndex": qtechCBQoSIfCarIfIndex,
       "qtechCBQoSIfCarPolicyDirection": qtechCBQoSIfCarPolicyDirection,
       "qtechCBQoSIfCarClassIndex": qtechCBQoSIfCarClassIndex,
       "qtechCBQoSIfCarConformedPackets": qtechCBQoSIfCarConformedPackets,
       "qtechCBQoSIfCarConformedBytes": qtechCBQoSIfCarConformedBytes,
       "qtechCBQoSIfCarExceededPackets": qtechCBQoSIfCarExceededPackets,
       "qtechCBQoSIfCarExceededBytes": qtechCBQoSIfCarExceededBytes,
       "qtechCBQoSIfCarViolatedPackets": qtechCBQoSIfCarViolatedPackets,
       "qtechCBQoSIfCarViolatedBytes": qtechCBQoSIfCarViolatedBytes,
       "qtechCBQoSIfRemarkRunInfoTable": qtechCBQoSIfRemarkRunInfoTable,
       "qtechCBQoSIfRemarkRunInfoEntry": qtechCBQoSIfRemarkRunInfoEntry,
       "qtechCBQoSIfRemarkIfIndex": qtechCBQoSIfRemarkIfIndex,
       "qtechCBQoSIfRemarkPolicyDirection": qtechCBQoSIfRemarkPolicyDirection,
       "qtechCBQoSIfRemarkClassIndex": qtechCBQoSIfRemarkClassIndex,
       "qtechCBQoSIfRemarkedPackets": qtechCBQoSIfRemarkedPackets,
       "qtechCBQoSIfRemarkedBytes": qtechCBQoSIfRemarkedBytes,
       "qtechCBQoSIfQueueRunInfoTable": qtechCBQoSIfQueueRunInfoTable,
       "qtechCBQoSIfQueueRunInfoEntry": qtechCBQoSIfQueueRunInfoEntry,
       "qtechCBQoSIfQueueIfIndex": qtechCBQoSIfQueueIfIndex,
       "qtechCBQoSIfQueuePolicyDirection": qtechCBQoSIfQueuePolicyDirection,
       "qtechCBQoSIfQueueClassIndex": qtechCBQoSIfQueueClassIndex,
       "qtechCBQoSIfQueueMatchedPackets": qtechCBQoSIfQueueMatchedPackets,
       "qtechCBQoSIfQueueMatchedBytes": qtechCBQoSIfQueueMatchedBytes,
       "qtechCBQoSIfQueueEnqueuedPackets": qtechCBQoSIfQueueEnqueuedPackets,
       "qtechCBQoSIfQueueEnqueuedBytes": qtechCBQoSIfQueueEnqueuedBytes,
       "qtechCBQoSIfQueueDiscardedPackets": qtechCBQoSIfQueueDiscardedPackets,
       "qtechCBQoSIfQueueDiscardedBytes": qtechCBQoSIfQueueDiscardedBytes,
       "qtechCBQoSIfWredRunInfoTable": qtechCBQoSIfWredRunInfoTable,
       "qtechCBQoSIfWredRunInfoEntry": qtechCBQoSIfWredRunInfoEntry,
       "qtechCBQoSIfWredIfIndex": qtechCBQoSIfWredIfIndex,
       "qtechCBQoSIfWredClassIndex": qtechCBQoSIfWredClassIndex,
       "qtechCBQoSIfWredClassValue": qtechCBQoSIfWredClassValue,
       "qtechCBQoSIfWredRandomDiscardedPackets": qtechCBQoSIfWredRandomDiscardedPackets,
       "qtechCBQoSIfWredTailDiscardedPackets": qtechCBQoSIfWredTailDiscardedPackets,
       "qtechIfQoSMIBObjects": qtechIfQoSMIBObjects,
       "qtechIfQosPQRunInfoTable": qtechIfQosPQRunInfoTable,
       "qtechIfQosPQRunInfoEntry": qtechIfQosPQRunInfoEntry,
       "qtechIfQosPQIfIndex": qtechIfQosPQIfIndex,
       "qtechIfQosPQListNum": qtechIfQosPQListNum,
       "qtechIfQosPQIfName": qtechIfQosPQIfName,
       "qtechIfQosPQHighPkt": qtechIfQosPQHighPkt,
       "qtechIfQosPQHighDiscard": qtechIfQosPQHighDiscard,
       "qtechIfQosPQHighMaxQueLen": qtechIfQosPQHighMaxQueLen,
       "qtechIfQosPQMiddlePkt": qtechIfQosPQMiddlePkt,
       "qtechIfQosPQMiddleDiscard": qtechIfQosPQMiddleDiscard,
       "qtechIfQosPQMiddleMaxQueLen": qtechIfQosPQMiddleMaxQueLen,
       "qtechIfQosPQNormalPkt": qtechIfQosPQNormalPkt,
       "qtechIfQosPQNormalDiscard": qtechIfQosPQNormalDiscard,
       "qtechIfQosPQNormalMaxQueLen": qtechIfQosPQNormalMaxQueLen,
       "qtechIfQosPQLowPkt": qtechIfQosPQLowPkt,
       "qtechIfQosPQLowDiscard": qtechIfQosPQLowDiscard,
       "qtechIfQosPQLowMaxQueLen": qtechIfQosPQLowMaxQueLen,
       "qtechIfQosCQRunInfoTable": qtechIfQosCQRunInfoTable,
       "qtechIfQosCQRunInfoEntry": qtechIfQosCQRunInfoEntry,
       "qtechIfQosCQRunInfoIfIndex": qtechIfQosCQRunInfoIfIndex,
       "qtechIfQosCQRunInfoQueNum": qtechIfQosCQRunInfoQueNum,
       "qtechIfQosCQRunInfoIfName": qtechIfQosCQRunInfoIfName,
       "qtechIfQosCQRunInfoQuePkt": qtechIfQosCQRunInfoQuePkt,
       "qtechIfQosCQRunInfoQueDiscard": qtechIfQosCQRunInfoQueDiscard,
       "qtechIfQosCQRunInfoMaxQueLen": qtechIfQosCQRunInfoMaxQueLen,
       "qtechIfQosWFQRunInfoTable": qtechIfQosWFQRunInfoTable,
       "qtechIfQosWFQRunInfoEntry": qtechIfQosWFQRunInfoEntry,
       "qtechIfQosWFQIfIndex": qtechIfQosWFQIfIndex,
       "qtechIfQosWFQIfName": qtechIfQosWFQIfName,
       "qtechIfQosWFQMaxQueLen": qtechIfQosWFQMaxQueLen,
       "qtechIfQosWFQTotalQueNum": qtechIfQosWFQTotalQueNum,
       "qtechIfQosWFQCurQueLen": qtechIfQosWFQCurQueLen,
       "qtechIfQosWFQTotalDiscard": qtechIfQosWFQTotalDiscard,
       "qtechIfQosWFQActiveQueNum": qtechIfQosWFQActiveQueNum,
       "qtechIfQosWFQMaxActiveQueNum": qtechIfQosWFQMaxActiveQueNum,
       "qtechIfQosWredRunInfoTable": qtechIfQosWredRunInfoTable,
       "qtechIfQosWredRunInfoEntry": qtechIfQosWredRunInfoEntry,
       "qtechIfQosWredIfIndex": qtechIfQosWredIfIndex,
       "qtechIfQosWredValue": qtechIfQosWredValue,
       "qtechIfQosWredRandomDiscardedPackets": qtechIfQosWredRandomDiscardedPackets,
       "qtechIfQosWredTailDiscardedPackets": qtechIfQosWredTailDiscardedPackets,
       "qtechIfQosCARTable": qtechIfQosCARTable,
       "qtechIfQosCAREntry": qtechIfQosCAREntry,
       "qtechIfQosCARIfIndex": qtechIfQosCARIfIndex,
       "qtechIfQosCARIfName": qtechIfQosCARIfName,
       "qtechIfQosCARPktDirection": qtechIfQosCARPktDirection,
       "qtechIfQosCARType": qtechIfQosCARType,
       "qtechIfQosCARListNum": qtechIfQosCARListNum,
       "qtechIfQosCARindex": qtechIfQosCARindex,
       "qtechIfQosCARCIR": qtechIfQosCARCIR,
       "qtechIfQosCARBurstSize": qtechIfQosCARBurstSize,
       "qtechIfQosCARExcessBurstSize": qtechIfQosCARExcessBurstSize,
       "qtechIfQosCARConformAction": qtechIfQosCARConformAction,
       "qtechIfQosCARExceedAction": qtechIfQosCARExceedAction,
       "qtechIfQosCARConformNewPrec": qtechIfQosCARConformNewPrec,
       "qtechIfQosCARExceedNewPrec": qtechIfQosCARExceedNewPrec,
       "qtechIfQosCARConformPkt": qtechIfQosCARConformPkt,
       "qtechIfQosCARConformByte": qtechIfQosCARConformByte,
       "qtechIfQosCARExceedPkt": qtechIfQosCARExceedPkt,
       "qtechIfQosCARExceedByte": qtechIfQosCARExceedByte,
       "qtechIfQosGTSTable": qtechIfQosGTSTable,
       "qtechIfQosGTSEntry": qtechIfQosGTSEntry,
       "qtechIfQosGTSIfIndex": qtechIfQosGTSIfIndex,
       "qtechIfQosGTSIfName": qtechIfQosGTSIfName,
       "qtechIfQosGTSType": qtechIfQosGTSType,
       "qtechIfQosGTSACLNum": qtechIfQosGTSACLNum,
       "qtechIfQosGTSCIR": qtechIfQosGTSCIR,
       "qtechIfQosGTSBurstSize": qtechIfQosGTSBurstSize,
       "qtechIfQosGTSExcessBurstSize": qtechIfQosGTSExcessBurstSize,
       "qtechIfQosGTSMaxQueLen": qtechIfQosGTSMaxQueLen,
       "qtechIfQosGTSCurQueLen": qtechIfQosGTSCurQueLen,
       "qtechIfQosGTSPassPkt": qtechIfQosGTSPassPkt,
       "qtechIfQosGTSPassByte": qtechIfQosGTSPassByte,
       "qtechIfQosGTSDiscardPkt": qtechIfQosGTSDiscardPkt,
       "qtechIfQosGTSDiscardByte": qtechIfQosGTSDiscardByte,
       "qtechIfQosRTPIfQueueRunInfoTable": qtechIfQosRTPIfQueueRunInfoTable,
       "qtechIfQosRTPIfQueueRunInfoEntry": qtechIfQosRTPIfQueueRunInfoEntry,
       "qtechIfQosRTPIfApplyIfIndex": qtechIfQosRTPIfApplyIfIndex,
       "qtechIfQosRTPIfQueueSize": qtechIfQosRTPIfQueueSize,
       "qtechIfQosRTPIfQueueMaxSize": qtechIfQosRTPIfQueueMaxSize,
       "qtechIfQosRTPIfQueueOutputs": qtechIfQosRTPIfQueueOutputs,
       "qtechIfQosRTPIfQueueDiscards": qtechIfQosRTPIfQueueDiscards,
       "qtechIfQosFlowLimitRunInfoTable": qtechIfQosFlowLimitRunInfoTable,
       "qtechIfQosFlowLimitRunInfoEntry": qtechIfQosFlowLimitRunInfoEntry,
       "qtechIfQosFlowLimitLabelNum": qtechIfQosFlowLimitLabelNum,
       "qtechIfQosFlowLimitPktDirection": qtechIfQosFlowLimitPktDirection,
       "qtechIfQosFlowLimitCIR": qtechIfQosFlowLimitCIR,
       "qtechIfQosFlowLimitBurstSize": qtechIfQosFlowLimitBurstSize,
       "qtechIfQosFlowLimitExcessBurstSize": qtechIfQosFlowLimitExcessBurstSize,
       "qtechIfQosFlowLimitConformAction": qtechIfQosFlowLimitConformAction,
       "qtechIfQosFlowLimitExceedAction": qtechIfQosFlowLimitExceedAction,
       "qtechIfQosFlowLimitConformNewPrec": qtechIfQosFlowLimitConformNewPrec,
       "qtechIfQosFlowLimitExceedNewPrec": qtechIfQosFlowLimitExceedNewPrec,
       "qtechIfQosFlowLimitConformPkt": qtechIfQosFlowLimitConformPkt,
       "qtechIfQosFlowLimitConformByte": qtechIfQosFlowLimitConformByte,
       "qtechIfQosFlowLimitExceedPkt": qtechIfQosFlowLimitExceedPkt,
       "qtechIfQosFlowLimitExceedByte": qtechIfQosFlowLimitExceedByte,
       "qtechHQoSMIBObjects": qtechHQoSMIBObjects,
       "qtechHQoSScalarObjects": qtechHQoSScalarObjects,
       "qtechHQoSNameType": qtechHQoSNameType,
       "qtechHQoSNameFind": qtechHQoSNameFind,
       "qtechHQoSNameIndex": qtechHQoSNameIndex,
       "qtechHQoSUserQObjects": qtechHQoSUserQObjects,
       "qtechHQoSUserQInIndexNext": qtechHQoSUserQInIndexNext,
       "qtechHQoSUserQOutIndexNext": qtechHQoSUserQOutIndexNext,
       "qtechHQoSUserQTable": qtechHQoSUserQTable,
       "qtechHQoSUserQEntry": qtechHQoSUserQEntry,
       "qtechHQoSUserQIndex": qtechHQoSUserQIndex,
       "qtechHQoSUserQName": qtechHQoSUserQName,
       "qtechHQoSUserQDirection": qtechHQoSUserQDirection,
       "qtechHQoSUserQRowStatus": qtechHQoSUserQRowStatus,
       "qtechHQoSUserQFlowQName": qtechHQoSUserQFlowQName,
       "qtechHQoSUserQFlowQIndex": qtechHQoSUserQFlowQIndex,
       "qtechHQoSUserQGroupName": qtechHQoSUserQGroupName,
       "qtechHQoSUserQGroupIndex": qtechHQoSUserQGroupIndex,
       "qtechHQoSUserQFlowMapName": qtechHQoSUserQFlowMapName,
       "qtechHQoSUserQFlowMapIndex": qtechHQoSUserQFlowMapIndex,
       "qtechHQoSUserQCIR": qtechHQoSUserQCIR,
       "qtechHQoSUserQPIR": qtechHQoSUserQPIR,
       "qtechHQoSUserGroupQObjects": qtechHQoSUserGroupQObjects,
       "qtechHQoSUserGroupQInIndexNext": qtechHQoSUserGroupQInIndexNext,
       "qtechHQoSUserGroupQOutIndexNext": qtechHQoSUserGroupQOutIndexNext,
       "qtechHQoSUserGroupQTable": qtechHQoSUserGroupQTable,
       "qtechHQoSUserGroupQEntry": qtechHQoSUserGroupQEntry,
       "qtechHQoSUserGroupQIndex": qtechHQoSUserGroupQIndex,
       "qtechHQoSUserGroupQName": qtechHQoSUserGroupQName,
       "qtechHQoSUserGroupQDirection": qtechHQoSUserGroupQDirection,
       "qtechHQoSUserGroupQRowStatus": qtechHQoSUserGroupQRowStatus,
       "qtechHQoSUserGroupQShaping": qtechHQoSUserGroupQShaping,
       "qtechHQoSFlowQObjects": qtechHQoSFlowQObjects,
       "qtechHQoSFlowQIndexNext": qtechHQoSFlowQIndexNext,
       "qtechHQoSFlowQTable": qtechHQoSFlowQTable,
       "qtechHQoSFlowQEntry": qtechHQoSFlowQEntry,
       "qtechHQoSFlowQIndex": qtechHQoSFlowQIndex,
       "qtechHQoSFlowQName": qtechHQoSFlowQName,
       "qtechHQoSFlowQRowStatus": qtechHQoSFlowQRowStatus,
       "qtechHQoSFlowQBEQType": qtechHQoSFlowQBEQType,
       "qtechHQoSFlowQBEQWredWeight": qtechHQoSFlowQBEQWredWeight,
       "qtechHQoSFlowQBEQWredName": qtechHQoSFlowQBEQWredName,
       "qtechHQoSFlowQBEQDepth": qtechHQoSFlowQBEQDepth,
       "qtechHQoSFlowQBEQShaping": qtechHQoSFlowQBEQShaping,
       "qtechHQoSFlowQAF1QType": qtechHQoSFlowQAF1QType,
       "qtechHQoSFlowQAF1QWredWeight": qtechHQoSFlowQAF1QWredWeight,
       "qtechHQoSFlowQAF1QWredName": qtechHQoSFlowQAF1QWredName,
       "qtechHQoSFlowQAF1QDepth": qtechHQoSFlowQAF1QDepth,
       "qtechHQoSFlowQAF1QShaping": qtechHQoSFlowQAF1QShaping,
       "qtechHQoSFlowQAF2QType": qtechHQoSFlowQAF2QType,
       "qtechHQoSFlowQAF2QWredWeight": qtechHQoSFlowQAF2QWredWeight,
       "qtechHQoSFlowQAF2QWredName": qtechHQoSFlowQAF2QWredName,
       "qtechHQoSFlowQAF2QDepth": qtechHQoSFlowQAF2QDepth,
       "qtechHQoSFlowQAF2QShaping": qtechHQoSFlowQAF2QShaping,
       "qtechHQoSFlowQAF3QType": qtechHQoSFlowQAF3QType,
       "qtechHQoSFlowQAF3QWredWeight": qtechHQoSFlowQAF3QWredWeight,
       "qtechHQoSFlowQAF3QWredName": qtechHQoSFlowQAF3QWredName,
       "qtechHQoSFlowQAF3QDepth": qtechHQoSFlowQAF3QDepth,
       "qtechHQoSFlowQAF3QShaping": qtechHQoSFlowQAF3QShaping,
       "qtechHQoSFlowQAF4QType": qtechHQoSFlowQAF4QType,
       "qtechHQoSFlowQAF4QWredWeight": qtechHQoSFlowQAF4QWredWeight,
       "qtechHQoSFlowQAF4QWredName": qtechHQoSFlowQAF4QWredName,
       "qtechHQoSFlowQAF4QDepth": qtechHQoSFlowQAF4QDepth,
       "qtechHQoSFlowQAF4QShaping": qtechHQoSFlowQAF4QShaping,
       "qtechHQoSFlowQEFQType": qtechHQoSFlowQEFQType,
       "qtechHQoSFlowQEFQWredWeight": qtechHQoSFlowQEFQWredWeight,
       "qtechHQoSFlowQEFQWredName": qtechHQoSFlowQEFQWredName,
       "qtechHQoSFlowQEFQDepth": qtechHQoSFlowQEFQDepth,
       "qtechHQoSFlowQEFQShaping": qtechHQoSFlowQEFQShaping,
       "qtechHQoSFlowQCS6QType": qtechHQoSFlowQCS6QType,
       "qtechHQoSFlowQCS6QWredWeight": qtechHQoSFlowQCS6QWredWeight,
       "qtechHQoSFlowQCS6QWredName": qtechHQoSFlowQCS6QWredName,
       "qtechHQoSFlowQCS6QDepth": qtechHQoSFlowQCS6QDepth,
       "qtechHQoSFlowQCS6QShaping": qtechHQoSFlowQCS6QShaping,
       "qtechHQoSFlowQCS7QType": qtechHQoSFlowQCS7QType,
       "qtechHQoSFlowQCS7QWredWeight": qtechHQoSFlowQCS7QWredWeight,
       "qtechHQoSFlowQCS7QWredName": qtechHQoSFlowQCS7QWredName,
       "qtechHQoSFlowQCS7QDepth": qtechHQoSFlowQCS7QDepth,
       "qtechHQoSFlowQCS7QShaping": qtechHQoSFlowQCS7QShaping,
       "qtechHQoSFlowMapObjects": qtechHQoSFlowMapObjects,
       "qtechHQoSFlowMapIndexNext": qtechHQoSFlowMapIndexNext,
       "qtechHQoSFlowMapTable": qtechHQoSFlowMapTable,
       "qtechHQoSFlowMapEntry": qtechHQoSFlowMapEntry,
       "qtechHQoSFlowMapIndex": qtechHQoSFlowMapIndex,
       "qtechHQoSFlowMapName": qtechHQoSFlowMapName,
       "qtechHQoSFlowMapRowStatus": qtechHQoSFlowMapRowStatus,
       "qtechHQoSFlowMapBEQ2PortQ": qtechHQoSFlowMapBEQ2PortQ,
       "qtechHQoSFlowMapAF1Q2PortQ": qtechHQoSFlowMapAF1Q2PortQ,
       "qtechHQoSFlowMapAF2Q2PortQ": qtechHQoSFlowMapAF2Q2PortQ,
       "qtechHQoSFlowMapAF3Q2PortQ": qtechHQoSFlowMapAF3Q2PortQ,
       "qtechHQoSFlowMapAF4Q2PortQ": qtechHQoSFlowMapAF4Q2PortQ,
       "qtechHQoSFlowMapEFQ2PortQ": qtechHQoSFlowMapEFQ2PortQ,
       "qtechHQoSFlowMapCS6Q2PortQ": qtechHQoSFlowMapCS6Q2PortQ,
       "qtechHQoSFlowMapCS7Q2PortQ": qtechHQoSFlowMapCS7Q2PortQ,
       "qtechHQoSTClassifierObjects": qtechHQoSTClassifierObjects,
       "qtechHQoSTClassifierIndexNext": qtechHQoSTClassifierIndexNext,
       "qtechHQoSTClassifierTable": qtechHQoSTClassifierTable,
       "qtechHQoSTClassifierEntry": qtechHQoSTClassifierEntry,
       "qtechHQoSTClassifierIndex": qtechHQoSTClassifierIndex,
       "qtechHQoSTClassifierInstance": qtechHQoSTClassifierInstance,
       "qtechHQoSTClassifierName": qtechHQoSTClassifierName,
       "qtechHQoSTClassifierType": qtechHQoSTClassifierType,
       "qtechHQoSTClassifierRowStatus": qtechHQoSTClassifierRowStatus,
       "qtechHQoSTClassifierMatchMask": qtechHQoSTClassifierMatchMask,
       "qtechHQoSTClassifierMatchV4Any": qtechHQoSTClassifierMatchV4Any,
       "qtechHQoSTClassifierMatchV4AclID": qtechHQoSTClassifierMatchV4AclID,
       "qtechHQoSTClassifierV4AclName": qtechHQoSTClassifierV4AclName,
       "qtechHQoSTClassifierMatchV4Dscp": qtechHQoSTClassifierMatchV4Dscp,
       "qtechHQoSTClassifierMatchV4Tos": qtechHQoSTClassifierMatchV4Tos,
       "qtechHQoSTClassifierMatchV6Any": qtechHQoSTClassifierMatchV6Any,
       "qtechHQoSTClassifierMatchV6AclID": qtechHQoSTClassifierMatchV6AclID,
       "qtechHQoSTClassifierV6AclName": qtechHQoSTClassifierV6AclName,
       "qtechHQoSTClassifierMatchV6Dscp": qtechHQoSTClassifierMatchV6Dscp,
       "qtechHQoSTClassifierMatchCos": qtechHQoSTClassifierMatchCos,
       "qtechHQoSTClassifierMatchExp": qtechHQoSTClassifierMatchExp,
       "qtechHQoSTClassifierMatchSrcMac": qtechHQoSTClassifierMatchSrcMac,
       "qtechHQoSTClassifierMatchDstMac": qtechHQoSTClassifierMatchDstMac,
       "qtechHQoSTBehaviorObjects": qtechHQoSTBehaviorObjects,
       "qtechHQoSTBehaviorIndexNext": qtechHQoSTBehaviorIndexNext,
       "qtechHQoSTBehaviorTable": qtechHQoSTBehaviorTable,
       "qtechHQoSTBehaviorEntry": qtechHQoSTBehaviorEntry,
       "qtechHQoSTBehaviorIndex": qtechHQoSTBehaviorIndex,
       "qtechHQoSTBehaviorName": qtechHQoSTBehaviorName,
       "qtechHQoSTBehaviorRowStatus": qtechHQoSTBehaviorRowStatus,
       "qtechHQoSTBehaviorMask": qtechHQoSTBehaviorMask,
       "qtechHQoSTBehaviorUserQName": qtechHQoSTBehaviorUserQName,
       "qtechHQoSTBehaviorTCos": qtechHQoSTBehaviorTCos,
       "qtechHQoSTBehaviorTColor": qtechHQoSTBehaviorTColor,
       "qtechHQoSTBehaviorRV4Dscp": qtechHQoSTBehaviorRV4Dscp,
       "qtechHQoSTBehaviorRV4Tos": qtechHQoSTBehaviorRV4Tos,
       "qtechHQoSTBehaviorRV6Dscp": qtechHQoSTBehaviorRV6Dscp,
       "qtechHQoSTBehaviorRVlanCos": qtechHQoSTBehaviorRVlanCos,
       "qtechHQoSTBehaviorRExp": qtechHQoSTBehaviorRExp,
       "qtechHQoSTBehaviorSubPolicyName": qtechHQoSTBehaviorSubPolicyName,
       "qtechHQoSTPolicyObjects": qtechHQoSTPolicyObjects,
       "qtechHQoSTPolicyIndexNext": qtechHQoSTPolicyIndexNext,
       "qtechHQoSTPolicyTable": qtechHQoSTPolicyTable,
       "qtechHQoSTPolicyEntry": qtechHQoSTPolicyEntry,
       "qtechHQoSTPolicyIndex": qtechHQoSTPolicyIndex,
       "qtechHQoSTPolicyName": qtechHQoSTPolicyName,
       "qtechHQoSTPolicyRowStatus": qtechHQoSTPolicyRowStatus,
       "qtechHQoSTPolicyMapIndexNext": qtechHQoSTPolicyMapIndexNext,
       "qtechHQoSTPolicyMapTable": qtechHQoSTPolicyMapTable,
       "qtechHQoSTPolicyMapEntry": qtechHQoSTPolicyMapEntry,
       "qtechHQoSTPolicyMapIndex": qtechHQoSTPolicyMapIndex,
       "qtechHQoSTPolicyMapPolicyName": qtechHQoSTPolicyMapPolicyName,
       "qtechHQoSTPolicyMapPolicyIndex": qtechHQoSTPolicyMapPolicyIndex,
       "qtechHQoSTPolicyMapTClassfierName": qtechHQoSTPolicyMapTClassfierName,
       "qtechHQoSTPolicyMapTClassfierIndex": qtechHQoSTPolicyMapTClassfierIndex,
       "qtechHQoSTPolicyMapTBehaviorName": qtechHQoSTPolicyMapTBehaviorName,
       "qtechHQoSTPolicyMapTBehaviorIndex": qtechHQoSTPolicyMapTBehaviorIndex,
       "qtechHQoSTPolicyMapPrecedence": qtechHQoSTPolicyMapPrecedence,
       "qtechHQoSTPolicyMapRowStatus": qtechHQoSTPolicyMapRowStatus,
       "qtechHQoSVoQObjects": qtechHQoSVoQObjects,
       "qtechHQoSVoQEnable": qtechHQoSVoQEnable,
       "qtechHQoSVoQDeviceTable": qtechHQoSVoQDeviceTable,
       "qtechHQoSVoQDeviceEntry": qtechHQoSVoQDeviceEntry,
       "qtechHQoSVoQDeviceId": qtechHQoSVoQDeviceId,
       "qtechHQoSVoQDeviceCredit": qtechHQoSVoQDeviceCredit,
       "qtechHQoSPortQObjects": qtechHQoSPortQObjects,
       "qtechHQoSPortQIndexNext": qtechHQoSPortQIndexNext,
       "qtechHQoSPortQTable": qtechHQoSPortQTable,
       "qtechHQoSPortQEntry": qtechHQoSPortQEntry,
       "qtechHQoSPortQIndex": qtechHQoSPortQIndex,
       "qtechHQoSPortQName": qtechHQoSPortQName,
       "qtechHQoSPortQRowStatus": qtechHQoSPortQRowStatus,
       "qtechHQoSPortQBEQType": qtechHQoSPortQBEQType,
       "qtechHQoSPortQBEQWredWeight": qtechHQoSPortQBEQWredWeight,
       "qtechHQoSPortQBEQWredName": qtechHQoSPortQBEQWredName,
       "qtechHQoSPortQBEQDepth": qtechHQoSPortQBEQDepth,
       "qtechHQoSPortQBEQShaping": qtechHQoSPortQBEQShaping,
       "qtechHQoSPortQAF1QType": qtechHQoSPortQAF1QType,
       "qtechHQoSPortQAF1QWredWeight": qtechHQoSPortQAF1QWredWeight,
       "qtechHQoSPortQAF1QWredName": qtechHQoSPortQAF1QWredName,
       "qtechHQoSPortQAF1QDepth": qtechHQoSPortQAF1QDepth,
       "qtechHQoSPortQAF1QShaping": qtechHQoSPortQAF1QShaping,
       "qtechHQoSPortQAF2QType": qtechHQoSPortQAF2QType,
       "qtechHQoSPortQAF2QWredWeight": qtechHQoSPortQAF2QWredWeight,
       "qtechHQoSPortQAF2QWredName": qtechHQoSPortQAF2QWredName,
       "qtechHQoSPortQAF2QDepth": qtechHQoSPortQAF2QDepth,
       "qtechHQoSPortQAF2QShaping": qtechHQoSPortQAF2QShaping,
       "qtechHQoSPortQAF3QType": qtechHQoSPortQAF3QType,
       "qtechHQoSPortQAF3QWredWeight": qtechHQoSPortQAF3QWredWeight,
       "qtechHQoSPortQAF3QWredName": qtechHQoSPortQAF3QWredName,
       "qtechHQoSPortQAF3QDepth": qtechHQoSPortQAF3QDepth,
       "qtechHQoSPortQAF3QShaping": qtechHQoSPortQAF3QShaping,
       "qtechHQoSPortQAF4QType": qtechHQoSPortQAF4QType,
       "qtechHQoSPortQAF4QWredWeight": qtechHQoSPortQAF4QWredWeight,
       "qtechHQoSPortQAF4QWredName": qtechHQoSPortQAF4QWredName,
       "qtechHQoSPortQAF4QDepth": qtechHQoSPortQAF4QDepth,
       "qtechHQoSPortQAF4QShaping": qtechHQoSPortQAF4QShaping,
       "qtechHQoSPortQEFQType": qtechHQoSPortQEFQType,
       "qtechHQoSPortQEFQWredWeight": qtechHQoSPortQEFQWredWeight,
       "qtechHQoSPortQEFQWredName": qtechHQoSPortQEFQWredName,
       "qtechHQoSPortQEFQDepth": qtechHQoSPortQEFQDepth,
       "qtechHQoSPortQEFQShaping": qtechHQoSPortQEFQShaping,
       "qtechHQoSPortQCS6QType": qtechHQoSPortQCS6QType,
       "qtechHQoSPortQCS6QWredWeight": qtechHQoSPortQCS6QWredWeight,
       "qtechHQoSPortQCS6QWredName": qtechHQoSPortQCS6QWredName,
       "qtechHQoSPortQCS6QDepth": qtechHQoSPortQCS6QDepth,
       "qtechHQoSPortQCS6QShaping": qtechHQoSPortQCS6QShaping,
       "qtechHQoSPortQCS7QType": qtechHQoSPortQCS7QType,
       "qtechHQoSPortQCS7QWredWeight": qtechHQoSPortQCS7QWredWeight,
       "qtechHQoSPortQCS7QWredName": qtechHQoSPortQCS7QWredName,
       "qtechHQoSPortQCS7QDepth": qtechHQoSPortQCS7QDepth,
       "qtechHQoSPortQCS7QShaping": qtechHQoSPortQCS7QShaping,
       "qtechHQoSIfAppObjects": qtechHQoSIfAppObjects,
       "qtechHQoSIfAppTable": qtechHQoSIfAppTable,
       "qtechHQoSIfAppEntry": qtechHQoSIfAppEntry,
       "qtechHQoSIfAppIndex": qtechHQoSIfAppIndex,
       "qtechHQoSIfAppInPolicyName": qtechHQoSIfAppInPolicyName,
       "qtechHQoSIfAppInPolicyIndex": qtechHQoSIfAppInPolicyIndex,
       "qtechHQoSIfAppInPolicyLayer": qtechHQoSIfAppInPolicyLayer,
       "qtechHQoSIfAppOutPolicyName": qtechHQoSIfAppOutPolicyName,
       "qtechHQoSIfAppOutPolicyIndex": qtechHQoSIfAppOutPolicyIndex,
       "qtechHQoSIfAppOutPolicyLayer": qtechHQoSIfAppOutPolicyLayer,
       "qtechHQoSIfAppPortQueueName": qtechHQoSIfAppPortQueueName,
       "qtechHQoSIfAppPortQueueIndex": qtechHQoSIfAppPortQueueIndex,
       "qtechHQoSIfAppPortQueueShaping": qtechHQoSIfAppPortQueueShaping}
)
