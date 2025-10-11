# SNMP MIB module (G6-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:04 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83)
)


class _QosEnableQos_Type(Integer32):
    """Custom type qosEnableQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_QosEnableQos_Type.__name__ = "Integer32"
_QosEnableQos_Object = MibScalar
qosEnableQos = _QosEnableQos_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 1),
    _QosEnableQos_Type()
)
qosEnableQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEnableQos.setStatus("current")
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1)
)
configEntry.setIndexNames(
    (0, "G6-QOS-MIB", "configPortIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigPortIndex_Type(Integer32):
    """Custom type configPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_ConfigPortIndex_Type.__name__ = "Integer32"
_ConfigPortIndex_Object = MibTableColumn
configPortIndex = _ConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1, 1),
    _ConfigPortIndex_Type()
)
configPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configPortIndex.setStatus("current")


class _ConfigEnable802dot1p_Type(Integer32):
    """Custom type configEnable802dot1p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnable802dot1p_Type.__name__ = "Integer32"
_ConfigEnable802dot1p_Object = MibTableColumn
configEnable802dot1p = _ConfigEnable802dot1p_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1, 2),
    _ConfigEnable802dot1p_Type()
)
configEnable802dot1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnable802dot1p.setStatus("current")


class _ConfigEnableDiffserv_Type(Integer32):
    """Custom type configEnableDiffserv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableDiffserv_Type.__name__ = "Integer32"
_ConfigEnableDiffserv_Object = MibTableColumn
configEnableDiffserv = _ConfigEnableDiffserv_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1, 3),
    _ConfigEnableDiffserv_Type()
)
configEnableDiffserv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableDiffserv.setStatus("current")


class _ConfigPriorityScheme_Type(Integer32):
    """Custom type configPriorityScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("weighted", 0),
          ("strict", 1))
    )


_ConfigPriorityScheme_Type.__name__ = "Integer32"
_ConfigPriorityScheme_Object = MibTableColumn
configPriorityScheme = _ConfigPriorityScheme_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1, 4),
    _ConfigPriorityScheme_Type()
)
configPriorityScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPriorityScheme.setStatus("current")


class _ConfigForceDefaultPriorityQueue_Type(Integer32):
    """Custom type configForceDefaultPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigForceDefaultPriorityQueue_Type.__name__ = "Integer32"
_ConfigForceDefaultPriorityQueue_Object = MibTableColumn
configForceDefaultPriorityQueue = _ConfigForceDefaultPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1, 5),
    _ConfigForceDefaultPriorityQueue_Type()
)
configForceDefaultPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configForceDefaultPriorityQueue.setStatus("current")


class _ConfigDefaultPriorityQueue_Type(Integer32):
    """Custom type configDefaultPriorityQueue based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_ConfigDefaultPriorityQueue_Type.__name__ = "Integer32"
_ConfigDefaultPriorityQueue_Object = MibTableColumn
configDefaultPriorityQueue = _ConfigDefaultPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 2, 1, 6),
    _ConfigDefaultPriorityQueue_Type()
)
configDefaultPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDefaultPriorityQueue.setStatus("current")
_Ieee802dot1pPrioMappingTable_Object = MibTable
ieee802dot1pPrioMappingTable = _Ieee802dot1pPrioMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3)
)
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTable.setStatus("current")
_Ieee802dot1pPrioMappingEntry_Object = MibTableRow
ieee802dot1pPrioMappingEntry = _Ieee802dot1pPrioMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1)
)
ieee802dot1pPrioMappingEntry.setIndexNames(
    (0, "G6-QOS-MIB", "ieee802dot1pPrioMappingIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingEntry.setStatus("current")


class _Ieee802dot1pPrioMappingIndex_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Ieee802dot1pPrioMappingIndex_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingIndex_Object = MibTableColumn
ieee802dot1pPrioMappingIndex = _Ieee802dot1pPrioMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 1),
    _Ieee802dot1pPrioMappingIndex_Type()
)
ieee802dot1pPrioMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingIndex.setStatus("current")


class _Ieee802dot1pPrioMappingTag0_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag0 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag0_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag0_Object = MibTableColumn
ieee802dot1pPrioMappingTag0 = _Ieee802dot1pPrioMappingTag0_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 2),
    _Ieee802dot1pPrioMappingTag0_Type()
)
ieee802dot1pPrioMappingTag0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag0.setStatus("current")


class _Ieee802dot1pPrioMappingTag1_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag1 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag1_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag1_Object = MibTableColumn
ieee802dot1pPrioMappingTag1 = _Ieee802dot1pPrioMappingTag1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 3),
    _Ieee802dot1pPrioMappingTag1_Type()
)
ieee802dot1pPrioMappingTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag1.setStatus("current")


class _Ieee802dot1pPrioMappingTag2_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag2 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag2_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag2_Object = MibTableColumn
ieee802dot1pPrioMappingTag2 = _Ieee802dot1pPrioMappingTag2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 4),
    _Ieee802dot1pPrioMappingTag2_Type()
)
ieee802dot1pPrioMappingTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag2.setStatus("current")


class _Ieee802dot1pPrioMappingTag3_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag3 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag3_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag3_Object = MibTableColumn
ieee802dot1pPrioMappingTag3 = _Ieee802dot1pPrioMappingTag3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 5),
    _Ieee802dot1pPrioMappingTag3_Type()
)
ieee802dot1pPrioMappingTag3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag3.setStatus("current")


class _Ieee802dot1pPrioMappingTag4_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag4 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag4_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag4_Object = MibTableColumn
ieee802dot1pPrioMappingTag4 = _Ieee802dot1pPrioMappingTag4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 6),
    _Ieee802dot1pPrioMappingTag4_Type()
)
ieee802dot1pPrioMappingTag4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag4.setStatus("current")


class _Ieee802dot1pPrioMappingTag5_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag5 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag5_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag5_Object = MibTableColumn
ieee802dot1pPrioMappingTag5 = _Ieee802dot1pPrioMappingTag5_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 7),
    _Ieee802dot1pPrioMappingTag5_Type()
)
ieee802dot1pPrioMappingTag5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag5.setStatus("current")


class _Ieee802dot1pPrioMappingTag6_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag6 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag6_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag6_Object = MibTableColumn
ieee802dot1pPrioMappingTag6 = _Ieee802dot1pPrioMappingTag6_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 8),
    _Ieee802dot1pPrioMappingTag6_Type()
)
ieee802dot1pPrioMappingTag6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag6.setStatus("current")


class _Ieee802dot1pPrioMappingTag7_Type(Integer32):
    """Custom type ieee802dot1pPrioMappingTag7 based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_Ieee802dot1pPrioMappingTag7_Type.__name__ = "Integer32"
_Ieee802dot1pPrioMappingTag7_Object = MibTableColumn
ieee802dot1pPrioMappingTag7 = _Ieee802dot1pPrioMappingTag7_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 3, 1, 9),
    _Ieee802dot1pPrioMappingTag7_Type()
)
ieee802dot1pPrioMappingTag7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee802dot1pPrioMappingTag7.setStatus("current")
_DiffservPrioMappingTable_Object = MibTable
diffservPrioMappingTable = _DiffservPrioMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 4)
)
if mibBuilder.loadTexts:
    diffservPrioMappingTable.setStatus("current")
_DiffservPrioMappingEntry_Object = MibTableRow
diffservPrioMappingEntry = _DiffservPrioMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 4, 1)
)
diffservPrioMappingEntry.setIndexNames(
    (0, "G6-QOS-MIB", "diffservPrioMappingIndex"),
)
if mibBuilder.loadTexts:
    diffservPrioMappingEntry.setStatus("current")


class _DiffservPrioMappingIndex_Type(Integer32):
    """Custom type diffservPrioMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffservPrioMappingIndex_Type.__name__ = "Integer32"
_DiffservPrioMappingIndex_Object = MibTableColumn
diffservPrioMappingIndex = _DiffservPrioMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 4, 1, 1),
    _DiffservPrioMappingIndex_Type()
)
diffservPrioMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffservPrioMappingIndex.setStatus("current")


class _DiffservPrioMappingDscp_Type(Integer32):
    """Custom type diffservPrioMappingDscp based on Integer32"""
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
        *(("queue0", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3))
    )


_DiffservPrioMappingDscp_Type.__name__ = "Integer32"
_DiffservPrioMappingDscp_Object = MibTableColumn
diffservPrioMappingDscp = _DiffservPrioMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 4, 1, 2),
    _DiffservPrioMappingDscp_Type()
)
diffservPrioMappingDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservPrioMappingDscp.setStatus("current")
_RateShapingTable_Object = MibTable
rateShapingTable = _RateShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5)
)
if mibBuilder.loadTexts:
    rateShapingTable.setStatus("current")
_RateShapingEntry_Object = MibTableRow
rateShapingEntry = _RateShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1)
)
rateShapingEntry.setIndexNames(
    (0, "G6-QOS-MIB", "rateShapingPortIndex"),
)
if mibBuilder.loadTexts:
    rateShapingEntry.setStatus("current")


class _RateShapingPortIndex_Type(Integer32):
    """Custom type rateShapingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_RateShapingPortIndex_Type.__name__ = "Integer32"
_RateShapingPortIndex_Object = MibTableColumn
rateShapingPortIndex = _RateShapingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 1),
    _RateShapingPortIndex_Type()
)
rateShapingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateShapingPortIndex.setStatus("current")


class _RateShapingEgressBandwidthPercent_Type(Integer32):
    """Custom type rateShapingEgressBandwidthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RateShapingEgressBandwidthPercent_Type.__name__ = "Integer32"
_RateShapingEgressBandwidthPercent_Object = MibTableColumn
rateShapingEgressBandwidthPercent = _RateShapingEgressBandwidthPercent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 2),
    _RateShapingEgressBandwidthPercent_Type()
)
rateShapingEgressBandwidthPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingEgressBandwidthPercent.setStatus("current")


class _RateShapingIngressUnicastPercent_Type(Integer32):
    """Custom type rateShapingIngressUnicastPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RateShapingIngressUnicastPercent_Type.__name__ = "Integer32"
_RateShapingIngressUnicastPercent_Object = MibTableColumn
rateShapingIngressUnicastPercent = _RateShapingIngressUnicastPercent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 3),
    _RateShapingIngressUnicastPercent_Type()
)
rateShapingIngressUnicastPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingIngressUnicastPercent.setStatus("current")


class _RateShapingIngressMulticastPercent_Type(Integer32):
    """Custom type rateShapingIngressMulticastPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RateShapingIngressMulticastPercent_Type.__name__ = "Integer32"
_RateShapingIngressMulticastPercent_Object = MibTableColumn
rateShapingIngressMulticastPercent = _RateShapingIngressMulticastPercent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 4),
    _RateShapingIngressMulticastPercent_Type()
)
rateShapingIngressMulticastPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingIngressMulticastPercent.setStatus("current")


class _RateShapingIngressBroadcastPercent_Type(Integer32):
    """Custom type rateShapingIngressBroadcastPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RateShapingIngressBroadcastPercent_Type.__name__ = "Integer32"
_RateShapingIngressBroadcastPercent_Object = MibTableColumn
rateShapingIngressBroadcastPercent = _RateShapingIngressBroadcastPercent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 5),
    _RateShapingIngressBroadcastPercent_Type()
)
rateShapingIngressBroadcastPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingIngressBroadcastPercent.setStatus("current")


class _RateShapingIngressUser1Percent_Type(Integer32):
    """Custom type rateShapingIngressUser1Percent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RateShapingIngressUser1Percent_Type.__name__ = "Integer32"
_RateShapingIngressUser1Percent_Object = MibTableColumn
rateShapingIngressUser1Percent = _RateShapingIngressUser1Percent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 6),
    _RateShapingIngressUser1Percent_Type()
)
rateShapingIngressUser1Percent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingIngressUser1Percent.setStatus("current")


class _RateShapingIngressUser2Percent_Type(Integer32):
    """Custom type rateShapingIngressUser2Percent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RateShapingIngressUser2Percent_Type.__name__ = "Integer32"
_RateShapingIngressUser2Percent_Object = MibTableColumn
rateShapingIngressUser2Percent = _RateShapingIngressUser2Percent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 7),
    _RateShapingIngressUser2Percent_Type()
)
rateShapingIngressUser2Percent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingIngressUser2Percent.setStatus("current")


class _RateShapingUser1FrameTypes_Type(Integer32):
    """Custom type rateShapingUser1FrameTypes based on Integer32"""
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
        *(("disabled", 0),
          ("arp", 1),
          ("tcpControl", 2),
          ("arpAndTcpCtrl", 3))
    )


_RateShapingUser1FrameTypes_Type.__name__ = "Integer32"
_RateShapingUser1FrameTypes_Object = MibTableColumn
rateShapingUser1FrameTypes = _RateShapingUser1FrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 8),
    _RateShapingUser1FrameTypes_Type()
)
rateShapingUser1FrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingUser1FrameTypes.setStatus("current")


class _RateShapingUser2FrameTypes_Type(Integer32):
    """Custom type rateShapingUser2FrameTypes based on Integer32"""
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
        *(("disabled", 0),
          ("udpData", 1),
          ("tcpData", 2),
          ("udpAndTcpData", 3),
          ("nonUdpTcpData", 4))
    )


_RateShapingUser2FrameTypes_Type.__name__ = "Integer32"
_RateShapingUser2FrameTypes_Object = MibTableColumn
rateShapingUser2FrameTypes = _RateShapingUser2FrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 83, 5, 1, 9),
    _RateShapingUser2FrameTypes_Type()
)
rateShapingUser2FrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateShapingUser2FrameTypes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-QOS-MIB",
    **{"protocol": protocol,
       "qos": qos,
       "qosEnableQos": qosEnableQos,
       "configTable": configTable,
       "configEntry": configEntry,
       "configPortIndex": configPortIndex,
       "configEnable802dot1p": configEnable802dot1p,
       "configEnableDiffserv": configEnableDiffserv,
       "configPriorityScheme": configPriorityScheme,
       "configForceDefaultPriorityQueue": configForceDefaultPriorityQueue,
       "configDefaultPriorityQueue": configDefaultPriorityQueue,
       "ieee802dot1pPrioMappingTable": ieee802dot1pPrioMappingTable,
       "ieee802dot1pPrioMappingEntry": ieee802dot1pPrioMappingEntry,
       "ieee802dot1pPrioMappingIndex": ieee802dot1pPrioMappingIndex,
       "ieee802dot1pPrioMappingTag0": ieee802dot1pPrioMappingTag0,
       "ieee802dot1pPrioMappingTag1": ieee802dot1pPrioMappingTag1,
       "ieee802dot1pPrioMappingTag2": ieee802dot1pPrioMappingTag2,
       "ieee802dot1pPrioMappingTag3": ieee802dot1pPrioMappingTag3,
       "ieee802dot1pPrioMappingTag4": ieee802dot1pPrioMappingTag4,
       "ieee802dot1pPrioMappingTag5": ieee802dot1pPrioMappingTag5,
       "ieee802dot1pPrioMappingTag6": ieee802dot1pPrioMappingTag6,
       "ieee802dot1pPrioMappingTag7": ieee802dot1pPrioMappingTag7,
       "diffservPrioMappingTable": diffservPrioMappingTable,
       "diffservPrioMappingEntry": diffservPrioMappingEntry,
       "diffservPrioMappingIndex": diffservPrioMappingIndex,
       "diffservPrioMappingDscp": diffservPrioMappingDscp,
       "rateShapingTable": rateShapingTable,
       "rateShapingEntry": rateShapingEntry,
       "rateShapingPortIndex": rateShapingPortIndex,
       "rateShapingEgressBandwidthPercent": rateShapingEgressBandwidthPercent,
       "rateShapingIngressUnicastPercent": rateShapingIngressUnicastPercent,
       "rateShapingIngressMulticastPercent": rateShapingIngressMulticastPercent,
       "rateShapingIngressBroadcastPercent": rateShapingIngressBroadcastPercent,
       "rateShapingIngressUser1Percent": rateShapingIngressUser1Percent,
       "rateShapingIngressUser2Percent": rateShapingIngressUser2Percent,
       "rateShapingUser1FrameTypes": rateShapingUser1FrameTypes,
       "rateShapingUser2FrameTypes": rateShapingUser2FrameTypes}
)
