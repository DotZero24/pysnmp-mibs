# SNMP MIB module (ALU-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:29 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARObjs")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tNetworkIngressDot1pEntry,
 tNetworkPolicyEntry,
 tNetworkQueueEntry,
 tNetworkQueuePolicyEntry,
 tSapEgressEntry,
 tSapEgressQueueEntry,
 tSapIngressEntry,
 tSapIngressQueueEntry) = mibBuilder.importSymbols(
    "TIMETRA-QOS-MIB",
    "tNetworkIngressDot1pEntry",
    "tNetworkPolicyEntry",
    "tNetworkQueueEntry",
    "tNetworkQueuePolicyEntry",
    "tSapEgressEntry",
    "tSapEgressQueueEntry",
    "tSapIngressEntry",
    "tSapIngressQueueEntry")

(TBurstPercentOrDefault,
 TBurstSize,
 TBurstSizeBytes,
 TCIRRate,
 TItemDescription,
 TNamedItem,
 TPIRRate,
 TPolicyID,
 TQueueId,
 TRateType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TBurstPercentOrDefault",
    "TBurstSize",
    "TBurstSizeBytes",
    "TCIRRate",
    "TItemDescription",
    "TNamedItem",
    "TPIRRate",
    "TPolicyID",
    "TQueueId",
    "TRateType")


# MODULE-IDENTITY

aluQOSMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    aluQOSMIBModule.setRevisions(
        ("1908-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluIPsecStatsQueueId(TextualConvention, Integer32):
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
        *(("notUsed", 0),
          ("ipsec-decrypt-bestEffort", 1),
          ("ipsec-decrypt-expedited", 2),
          ("ipsec-encrypt-bestEffort", 3),
          ("ipsec-encrypt-expedited", 4))
    )



class AluSecQueueId(TextualConvention, Integer32):
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
        *(("notUsed", 0),
          ("bestEffort", 1),
          ("expedited", 2))
    )



class AluFabricProfilePolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class AluFabricProfileMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("destination", 2))
    )



class AluFabricProfileDestMdaRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )



class AluSapSchedulerCir(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10000000),
    )



class AluSystemAggregateRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )



class AluExtNetworkPolicyType(TextualConvention, Integer32):
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
        *(("default", 0),
          ("ipInterface", 1),
          ("ring", 2))
    )



class AluPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-62, 62),
        ValueRangeConstraint(127, 127),
    )



# MIB Managed Objects in the order of their OIDs

_AluQOSConformance_ObjectIdentity = ObjectIdentity
aluQOSConformance = _AluQOSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5)
)
_AluQOSCompliances_ObjectIdentity = ObjectIdentity
aluQOSCompliances = _AluQOSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1)
)
_AluQOSComp7705_ObjectIdentity = ObjectIdentity
aluQOSComp7705 = _AluQOSComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1)
)
_AluQOSGroups_ObjectIdentity = ObjectIdentity
aluQOSGroups = _AluQOSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2)
)
_AluQOSObjs_ObjectIdentity = ObjectIdentity
aluQOSObjs = _AluQOSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5)
)
_AluSapIngressQueueExtensionTable_Object = MibTable
aluSapIngressQueueExtensionTable = _AluSapIngressQueueExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    aluSapIngressQueueExtensionTable.setStatus("current")
_AluSapIngressQueueExtensionEntry_Object = MibTableRow
aluSapIngressQueueExtensionEntry = _AluSapIngressQueueExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    aluSapIngressQueueExtensionEntry.setStatus("current")


class _AluSapIngressQueueSlopePolicy_Type(TNamedItem):
    """Custom type aluSapIngressQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_AluSapIngressQueueSlopePolicy_Type.__name__ = "TNamedItem"
_AluSapIngressQueueSlopePolicy_Object = MibTableColumn
aluSapIngressQueueSlopePolicy = _AluSapIngressQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1, 1, 1),
    _AluSapIngressQueueSlopePolicy_Type()
)
aluSapIngressQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressQueueSlopePolicy.setStatus("current")


class _AluSapIngressQueuePktOffset_Type(AluPerPacketOffset):
    """Custom type aluSapIngressQueuePktOffset based on AluPerPacketOffset"""
    defaultValue = 127


_AluSapIngressQueuePktOffset_Type.__name__ = "AluPerPacketOffset"
_AluSapIngressQueuePktOffset_Object = MibTableColumn
aluSapIngressQueuePktOffset = _AluSapIngressQueuePktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1, 1, 2),
    _AluSapIngressQueuePktOffset_Type()
)
aluSapIngressQueuePktOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressQueuePktOffset.setStatus("current")
_AluSapEgressQueueExtensionTable_Object = MibTable
aluSapEgressQueueExtensionTable = _AluSapEgressQueueExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    aluSapEgressQueueExtensionTable.setStatus("current")
_AluSapEgressQueueExtensionEntry_Object = MibTableRow
aluSapEgressQueueExtensionEntry = _AluSapEgressQueueExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    aluSapEgressQueueExtensionEntry.setStatus("current")


class _AluSapEgressQueueSlopePolicy_Type(TNamedItem):
    """Custom type aluSapEgressQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_AluSapEgressQueueSlopePolicy_Type.__name__ = "TNamedItem"
_AluSapEgressQueueSlopePolicy_Object = MibTableColumn
aluSapEgressQueueSlopePolicy = _AluSapEgressQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2, 1, 1),
    _AluSapEgressQueueSlopePolicy_Type()
)
aluSapEgressQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressQueueSlopePolicy.setStatus("current")


class _AluSapEgressQueuePktOffset_Type(AluPerPacketOffset):
    """Custom type aluSapEgressQueuePktOffset based on AluPerPacketOffset"""
    defaultValue = 127


_AluSapEgressQueuePktOffset_Type.__name__ = "AluPerPacketOffset"
_AluSapEgressQueuePktOffset_Object = MibTableColumn
aluSapEgressQueuePktOffset = _AluSapEgressQueuePktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2, 1, 2),
    _AluSapEgressQueuePktOffset_Type()
)
aluSapEgressQueuePktOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressQueuePktOffset.setStatus("current")
_AluNetworkQueueExtensionTable_Object = MibTable
aluNetworkQueueExtensionTable = _AluNetworkQueueExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    aluNetworkQueueExtensionTable.setStatus("current")
_AluNetworkQueueExtensionEntry_Object = MibTableRow
aluNetworkQueueExtensionEntry = _AluNetworkQueueExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    aluNetworkQueueExtensionEntry.setStatus("current")


class _AluNetworkQueueSlopePolicy_Type(TNamedItem):
    """Custom type aluNetworkQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_AluNetworkQueueSlopePolicy_Type.__name__ = "TNamedItem"
_AluNetworkQueueSlopePolicy_Object = MibTableColumn
aluNetworkQueueSlopePolicy = _AluNetworkQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3, 1, 1),
    _AluNetworkQueueSlopePolicy_Type()
)
aluNetworkQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluNetworkQueueSlopePolicy.setStatus("current")


class _AluNetworkQueuePktOffset_Type(AluPerPacketOffset):
    """Custom type aluNetworkQueuePktOffset based on AluPerPacketOffset"""
    defaultValue = 127


_AluNetworkQueuePktOffset_Type.__name__ = "AluPerPacketOffset"
_AluNetworkQueuePktOffset_Object = MibTableColumn
aluNetworkQueuePktOffset = _AluNetworkQueuePktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3, 1, 2),
    _AluNetworkQueuePktOffset_Type()
)
aluNetworkQueuePktOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluNetworkQueuePktOffset.setStatus("current")
_AluFabricProfileTable_Object = MibTable
aluFabricProfileTable = _AluFabricProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    aluFabricProfileTable.setStatus("current")
_AluFabricProfileEntry_Object = MibTableRow
aluFabricProfileEntry = _AluFabricProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1)
)
aluFabricProfileEntry.setIndexNames(
    (0, "ALU-QOS-MIB", "aluFabricProfileIndex"),
)
if mibBuilder.loadTexts:
    aluFabricProfileEntry.setStatus("current")


class _AluFabricProfileIndex_Type(AluFabricProfilePolicyID):
    """Custom type aluFabricProfileIndex based on AluFabricProfilePolicyID"""
    subtypeSpec = AluFabricProfilePolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AluFabricProfileIndex_Type.__name__ = "AluFabricProfilePolicyID"
_AluFabricProfileIndex_Object = MibTableColumn
aluFabricProfileIndex = _AluFabricProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 1),
    _AluFabricProfileIndex_Type()
)
aluFabricProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluFabricProfileIndex.setStatus("current")
_AluFabricProfileRowStatus_Type = RowStatus
_AluFabricProfileRowStatus_Object = MibTableColumn
aluFabricProfileRowStatus = _AluFabricProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 2),
    _AluFabricProfileRowStatus_Type()
)
aluFabricProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRowStatus.setStatus("current")
_AluFabricProfileDescription_Type = TItemDescription
_AluFabricProfileDescription_Object = MibTableColumn
aluFabricProfileDescription = _AluFabricProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 3),
    _AluFabricProfileDescription_Type()
)
aluFabricProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileDescription.setStatus("current")


class _AluFabricProfileRateToMdaIndex1_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex1 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex1_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex1_Object = MibTableColumn
aluFabricProfileRateToMdaIndex1 = _AluFabricProfileRateToMdaIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 4),
    _AluFabricProfileRateToMdaIndex1_Type()
)
aluFabricProfileRateToMdaIndex1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex1.setStatus("current")


class _AluFabricProfileRateToMdaIndex2_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex2 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex2_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex2_Object = MibTableColumn
aluFabricProfileRateToMdaIndex2 = _AluFabricProfileRateToMdaIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 5),
    _AluFabricProfileRateToMdaIndex2_Type()
)
aluFabricProfileRateToMdaIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex2.setStatus("current")


class _AluFabricProfileRateToMdaIndex3_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex3 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex3_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex3_Object = MibTableColumn
aluFabricProfileRateToMdaIndex3 = _AluFabricProfileRateToMdaIndex3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 6),
    _AluFabricProfileRateToMdaIndex3_Type()
)
aluFabricProfileRateToMdaIndex3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex3.setStatus("current")


class _AluFabricProfileRateToMdaIndex4_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex4 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex4_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex4_Object = MibTableColumn
aluFabricProfileRateToMdaIndex4 = _AluFabricProfileRateToMdaIndex4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 7),
    _AluFabricProfileRateToMdaIndex4_Type()
)
aluFabricProfileRateToMdaIndex4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex4.setStatus("current")


class _AluFabricProfileRateToMdaIndex5_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex5 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex5_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex5_Object = MibTableColumn
aluFabricProfileRateToMdaIndex5 = _AluFabricProfileRateToMdaIndex5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 8),
    _AluFabricProfileRateToMdaIndex5_Type()
)
aluFabricProfileRateToMdaIndex5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex5.setStatus("current")


class _AluFabricProfileRateToMdaIndex6_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex6 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex6_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex6_Object = MibTableColumn
aluFabricProfileRateToMdaIndex6 = _AluFabricProfileRateToMdaIndex6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 9),
    _AluFabricProfileRateToMdaIndex6_Type()
)
aluFabricProfileRateToMdaIndex6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex6.setStatus("current")


class _AluFabricProfileRateToMdaIndex7_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex7 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex7_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex7_Object = MibTableColumn
aluFabricProfileRateToMdaIndex7 = _AluFabricProfileRateToMdaIndex7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 10),
    _AluFabricProfileRateToMdaIndex7_Type()
)
aluFabricProfileRateToMdaIndex7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex7.setStatus("current")


class _AluFabricProfileRateToMdaIndex8_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex8 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex8_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex8_Object = MibTableColumn
aluFabricProfileRateToMdaIndex8 = _AluFabricProfileRateToMdaIndex8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 11),
    _AluFabricProfileRateToMdaIndex8_Type()
)
aluFabricProfileRateToMdaIndex8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex8.setStatus("current")


class _AluFabricProfileRateToMdaIndex9_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex9 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex9_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex9_Object = MibTableColumn
aluFabricProfileRateToMdaIndex9 = _AluFabricProfileRateToMdaIndex9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 12),
    _AluFabricProfileRateToMdaIndex9_Type()
)
aluFabricProfileRateToMdaIndex9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex9.setStatus("current")


class _AluFabricProfileRateToMdaIndex10_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex10 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex10_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex10_Object = MibTableColumn
aluFabricProfileRateToMdaIndex10 = _AluFabricProfileRateToMdaIndex10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 13),
    _AluFabricProfileRateToMdaIndex10_Type()
)
aluFabricProfileRateToMdaIndex10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex10.setStatus("current")


class _AluFabricProfileRateToMdaIndex11_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex11 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex11_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex11_Object = MibTableColumn
aluFabricProfileRateToMdaIndex11 = _AluFabricProfileRateToMdaIndex11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 14),
    _AluFabricProfileRateToMdaIndex11_Type()
)
aluFabricProfileRateToMdaIndex11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex11.setStatus("current")


class _AluFabricProfileRateToMdaIndex12_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex12 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex12_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex12_Object = MibTableColumn
aluFabricProfileRateToMdaIndex12 = _AluFabricProfileRateToMdaIndex12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 15),
    _AluFabricProfileRateToMdaIndex12_Type()
)
aluFabricProfileRateToMdaIndex12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex12.setStatus("current")


class _AluFabricProfileRateToMdaIndex13_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex13 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex13_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex13_Object = MibTableColumn
aluFabricProfileRateToMdaIndex13 = _AluFabricProfileRateToMdaIndex13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 16),
    _AluFabricProfileRateToMdaIndex13_Type()
)
aluFabricProfileRateToMdaIndex13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex13.setStatus("current")


class _AluFabricProfileRateToMdaIndex14_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex14 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex14_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex14_Object = MibTableColumn
aluFabricProfileRateToMdaIndex14 = _AluFabricProfileRateToMdaIndex14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 17),
    _AluFabricProfileRateToMdaIndex14_Type()
)
aluFabricProfileRateToMdaIndex14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex14.setStatus("current")


class _AluFabricProfileRateToMdaIndex15_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex15 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex15_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex15_Object = MibTableColumn
aluFabricProfileRateToMdaIndex15 = _AluFabricProfileRateToMdaIndex15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 18),
    _AluFabricProfileRateToMdaIndex15_Type()
)
aluFabricProfileRateToMdaIndex15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex15.setStatus("current")


class _AluFabricProfileRateToMdaIndex16_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex16 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex16_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex16_Object = MibTableColumn
aluFabricProfileRateToMdaIndex16 = _AluFabricProfileRateToMdaIndex16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 19),
    _AluFabricProfileRateToMdaIndex16_Type()
)
aluFabricProfileRateToMdaIndex16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex16.setStatus("current")


class _AluFabricProfileRateToMdaIndex17_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex17 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex17_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex17_Object = MibTableColumn
aluFabricProfileRateToMdaIndex17 = _AluFabricProfileRateToMdaIndex17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 20),
    _AluFabricProfileRateToMdaIndex17_Type()
)
aluFabricProfileRateToMdaIndex17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex17.setStatus("current")


class _AluFabricProfileRateToMdaIndex18_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex18 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex18_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex18_Object = MibTableColumn
aluFabricProfileRateToMdaIndex18 = _AluFabricProfileRateToMdaIndex18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 21),
    _AluFabricProfileRateToMdaIndex18_Type()
)
aluFabricProfileRateToMdaIndex18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex18.setStatus("current")


class _AluFabricProfileRateToMdaIndex19_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex19 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex19_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex19_Object = MibTableColumn
aluFabricProfileRateToMdaIndex19 = _AluFabricProfileRateToMdaIndex19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 22),
    _AluFabricProfileRateToMdaIndex19_Type()
)
aluFabricProfileRateToMdaIndex19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex19.setStatus("current")


class _AluFabricProfileRateToMdaIndex20_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex20 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex20_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex20_Object = MibTableColumn
aluFabricProfileRateToMdaIndex20 = _AluFabricProfileRateToMdaIndex20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 23),
    _AluFabricProfileRateToMdaIndex20_Type()
)
aluFabricProfileRateToMdaIndex20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex20.setStatus("current")


class _AluFabricProfileRateToMdaIndex21_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex21 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex21_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex21_Object = MibTableColumn
aluFabricProfileRateToMdaIndex21 = _AluFabricProfileRateToMdaIndex21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 24),
    _AluFabricProfileRateToMdaIndex21_Type()
)
aluFabricProfileRateToMdaIndex21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex21.setStatus("current")


class _AluFabricProfileRateToMdaIndex22_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex22 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex22_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex22_Object = MibTableColumn
aluFabricProfileRateToMdaIndex22 = _AluFabricProfileRateToMdaIndex22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 25),
    _AluFabricProfileRateToMdaIndex22_Type()
)
aluFabricProfileRateToMdaIndex22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex22.setStatus("current")


class _AluFabricProfileRateToMdaIndex23_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex23 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex23_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex23_Object = MibTableColumn
aluFabricProfileRateToMdaIndex23 = _AluFabricProfileRateToMdaIndex23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 26),
    _AluFabricProfileRateToMdaIndex23_Type()
)
aluFabricProfileRateToMdaIndex23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex23.setStatus("current")


class _AluFabricProfileRateToMdaIndex24_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex24 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex24_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex24_Object = MibTableColumn
aluFabricProfileRateToMdaIndex24 = _AluFabricProfileRateToMdaIndex24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 27),
    _AluFabricProfileRateToMdaIndex24_Type()
)
aluFabricProfileRateToMdaIndex24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex24.setStatus("current")


class _AluFabricProfileRateToMdaIndex25_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex25 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex25_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex25_Object = MibTableColumn
aluFabricProfileRateToMdaIndex25 = _AluFabricProfileRateToMdaIndex25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 28),
    _AluFabricProfileRateToMdaIndex25_Type()
)
aluFabricProfileRateToMdaIndex25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex25.setStatus("current")


class _AluFabricProfileRateToMdaIndex26_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex26 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex26_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex26_Object = MibTableColumn
aluFabricProfileRateToMdaIndex26 = _AluFabricProfileRateToMdaIndex26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 29),
    _AluFabricProfileRateToMdaIndex26_Type()
)
aluFabricProfileRateToMdaIndex26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex26.setStatus("current")


class _AluFabricProfileRateToMdaIndex27_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex27 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex27_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex27_Object = MibTableColumn
aluFabricProfileRateToMdaIndex27 = _AluFabricProfileRateToMdaIndex27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 30),
    _AluFabricProfileRateToMdaIndex27_Type()
)
aluFabricProfileRateToMdaIndex27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex27.setStatus("current")


class _AluFabricProfileRateToMdaIndex28_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex28 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex28_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex28_Object = MibTableColumn
aluFabricProfileRateToMdaIndex28 = _AluFabricProfileRateToMdaIndex28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 31),
    _AluFabricProfileRateToMdaIndex28_Type()
)
aluFabricProfileRateToMdaIndex28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex28.setStatus("current")


class _AluFabricProfileRateToMdaIndex29_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex29 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex29_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex29_Object = MibTableColumn
aluFabricProfileRateToMdaIndex29 = _AluFabricProfileRateToMdaIndex29_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 32),
    _AluFabricProfileRateToMdaIndex29_Type()
)
aluFabricProfileRateToMdaIndex29.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex29.setStatus("current")


class _AluFabricProfileRateToMdaIndex30_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex30 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex30_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex30_Object = MibTableColumn
aluFabricProfileRateToMdaIndex30 = _AluFabricProfileRateToMdaIndex30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 33),
    _AluFabricProfileRateToMdaIndex30_Type()
)
aluFabricProfileRateToMdaIndex30.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex30.setStatus("current")


class _AluFabricProfileRateToMdaIndex31_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex31 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex31_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex31_Object = MibTableColumn
aluFabricProfileRateToMdaIndex31 = _AluFabricProfileRateToMdaIndex31_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 34),
    _AluFabricProfileRateToMdaIndex31_Type()
)
aluFabricProfileRateToMdaIndex31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex31.setStatus("current")


class _AluFabricProfileRateToMdaIndex32_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex32 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex32_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex32_Object = MibTableColumn
aluFabricProfileRateToMdaIndex32 = _AluFabricProfileRateToMdaIndex32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 35),
    _AluFabricProfileRateToMdaIndex32_Type()
)
aluFabricProfileRateToMdaIndex32.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex32.setStatus("current")
_AluFabricProfileLastChanged_Type = TimeStamp
_AluFabricProfileLastChanged_Object = MibTableColumn
aluFabricProfileLastChanged = _AluFabricProfileLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 36),
    _AluFabricProfileLastChanged_Type()
)
aluFabricProfileLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricProfileLastChanged.setStatus("current")


class _AluFabricProfileMode_Type(AluFabricProfileMode):
    """Custom type aluFabricProfileMode based on AluFabricProfileMode"""
    defaultValue = 1


_AluFabricProfileMode_Type.__name__ = "AluFabricProfileMode"
_AluFabricProfileMode_Object = MibTableColumn
aluFabricProfileMode = _AluFabricProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 37),
    _AluFabricProfileMode_Type()
)
aluFabricProfileMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileMode.setStatus("current")


class _AluFabricProfileAggregateRate_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileAggregateRate based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileAggregateRate_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileAggregateRate_Object = MibTableColumn
aluFabricProfileAggregateRate = _AluFabricProfileAggregateRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 38),
    _AluFabricProfileAggregateRate_Type()
)
aluFabricProfileAggregateRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileAggregateRate.setStatus("current")


class _AluFabricProfileMultipointRate_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileMultipointRate based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileMultipointRate_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileMultipointRate_Object = MibTableColumn
aluFabricProfileMultipointRate = _AluFabricProfileMultipointRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 39),
    _AluFabricProfileMultipointRate_Type()
)
aluFabricProfileMultipointRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileMultipointRate.setStatus("current")


class _AluFabricProfileUnshapedSapCir_Type(AluSapSchedulerCir):
    """Custom type aluFabricProfileUnshapedSapCir based on AluSapSchedulerCir"""
    defaultValue = 0


_AluFabricProfileUnshapedSapCir_Type.__name__ = "AluSapSchedulerCir"
_AluFabricProfileUnshapedSapCir_Object = MibTableColumn
aluFabricProfileUnshapedSapCir = _AluFabricProfileUnshapedSapCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 40),
    _AluFabricProfileUnshapedSapCir_Type()
)
aluFabricProfileUnshapedSapCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileUnshapedSapCir.setStatus("current")
if mibBuilder.loadTexts:
    aluFabricProfileUnshapedSapCir.setUnits("kbps")
_AluExtTSapEgressTable_Object = MibTable
aluExtTSapEgressTable = _AluExtTSapEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5)
)
if mibBuilder.loadTexts:
    aluExtTSapEgressTable.setStatus("current")
_AluExtTSapEgressEntry_Object = MibTableRow
aluExtTSapEgressEntry = _AluExtTSapEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    aluExtTSapEgressEntry.setStatus("current")


class _AluSapEgressPolicyType_Type(Integer32):
    """Custom type aluSapEgressPolicyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("standard", 2),
          ("mc-mlppp", 3))
    )


_AluSapEgressPolicyType_Type.__name__ = "Integer32"
_AluSapEgressPolicyType_Object = MibTableColumn
aluSapEgressPolicyType = _AluSapEgressPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5, 1, 1),
    _AluSapEgressPolicyType_Type()
)
aluSapEgressPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressPolicyType.setStatus("current")


class _AluSapEgressPktOffset_Type(AluPerPacketOffset):
    """Custom type aluSapEgressPktOffset based on AluPerPacketOffset"""
    defaultValue = 127


_AluSapEgressPktOffset_Type.__name__ = "AluPerPacketOffset"
_AluSapEgressPktOffset_Object = MibTableColumn
aluSapEgressPktOffset = _AluSapEgressPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5, 1, 2),
    _AluSapEgressPktOffset_Type()
)
aluSapEgressPktOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressPktOffset.setStatus("current")
_AluSystemQosConfig_ObjectIdentity = ObjectIdentity
aluSystemQosConfig = _AluSystemQosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6)
)


class _AluSystemAccessIngAggRate_Type(AluSystemAggregateRate):
    """Custom type aluSystemAccessIngAggRate based on AluSystemAggregateRate"""
    defaultValue = 0


_AluSystemAccessIngAggRate_Type.__name__ = "AluSystemAggregateRate"
_AluSystemAccessIngAggRate_Object = MibScalar
aluSystemAccessIngAggRate = _AluSystemAccessIngAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 1),
    _AluSystemAccessIngAggRate_Type()
)
aluSystemAccessIngAggRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSystemAccessIngAggRate.setStatus("current")


class _AluSystemNetworkIngAggRate_Type(AluSystemAggregateRate):
    """Custom type aluSystemNetworkIngAggRate based on AluSystemAggregateRate"""
    defaultValue = 0


_AluSystemNetworkIngAggRate_Type.__name__ = "AluSystemAggregateRate"
_AluSystemNetworkIngAggRate_Object = MibScalar
aluSystemNetworkIngAggRate = _AluSystemNetworkIngAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 2),
    _AluSystemNetworkIngAggRate_Type()
)
aluSystemNetworkIngAggRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSystemNetworkIngAggRate.setStatus("current")
_AluSystemQosLastChanged_Type = TimeStamp
_AluSystemQosLastChanged_Object = MibScalar
aluSystemQosLastChanged = _AluSystemQosLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 3),
    _AluSystemQosLastChanged_Type()
)
aluSystemQosLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSystemQosLastChanged.setStatus("current")


class _AluSystemIngUnshapedSapCir_Type(AluSapSchedulerCir):
    """Custom type aluSystemIngUnshapedSapCir based on AluSapSchedulerCir"""
    defaultValue = 0


_AluSystemIngUnshapedSapCir_Type.__name__ = "AluSapSchedulerCir"
_AluSystemIngUnshapedSapCir_Object = MibScalar
aluSystemIngUnshapedSapCir = _AluSystemIngUnshapedSapCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 4),
    _AluSystemIngUnshapedSapCir_Type()
)
aluSystemIngUnshapedSapCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSystemIngUnshapedSapCir.setStatus("current")
_AluExtNetworkPolicyTable_Object = MibTable
aluExtNetworkPolicyTable = _AluExtNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 7)
)
if mibBuilder.loadTexts:
    aluExtNetworkPolicyTable.setStatus("current")
_AluExtNetworkPolicyEntry_Object = MibTableRow
aluExtNetworkPolicyEntry = _AluExtNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    aluExtNetworkPolicyEntry.setStatus("current")


class _AluExtNetworkPolicyType_Type(AluExtNetworkPolicyType):
    """Custom type aluExtNetworkPolicyType based on AluExtNetworkPolicyType"""
    defaultValue = 1


_AluExtNetworkPolicyType_Type.__name__ = "AluExtNetworkPolicyType"
_AluExtNetworkPolicyType_Object = MibTableColumn
aluExtNetworkPolicyType = _AluExtNetworkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 7, 1, 1),
    _AluExtNetworkPolicyType_Type()
)
aluExtNetworkPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtNetworkPolicyType.setStatus("current")


class _AluExtNetworkPolicyDefActionQueue_Type(TQueueId):
    """Custom type aluExtNetworkPolicyDefActionQueue based on TQueueId"""
    defaultValue = 1

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AluExtNetworkPolicyDefActionQueue_Type.__name__ = "TQueueId"
_AluExtNetworkPolicyDefActionQueue_Object = MibTableColumn
aluExtNetworkPolicyDefActionQueue = _AluExtNetworkPolicyDefActionQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 7, 1, 2),
    _AluExtNetworkPolicyDefActionQueue_Type()
)
aluExtNetworkPolicyDefActionQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtNetworkPolicyDefActionQueue.setStatus("current")
_AluExtNetworkIngressDot1pTable_Object = MibTable
aluExtNetworkIngressDot1pTable = _AluExtNetworkIngressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 8)
)
if mibBuilder.loadTexts:
    aluExtNetworkIngressDot1pTable.setStatus("current")
_AluExtNetworkIngressDot1pEntry_Object = MibTableRow
aluExtNetworkIngressDot1pEntry = _AluExtNetworkIngressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    aluExtNetworkIngressDot1pEntry.setStatus("current")


class _AluExtNetworkRingDot1pQueue_Type(TQueueId):
    """Custom type aluExtNetworkRingDot1pQueue based on TQueueId"""
    defaultValue = 1

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AluExtNetworkRingDot1pQueue_Type.__name__ = "TQueueId"
_AluExtNetworkRingDot1pQueue_Object = MibTableColumn
aluExtNetworkRingDot1pQueue = _AluExtNetworkRingDot1pQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 8, 1, 1),
    _AluExtNetworkRingDot1pQueue_Type()
)
aluExtNetworkRingDot1pQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtNetworkRingDot1pQueue.setStatus("current")
_AluShaperPolicyTable_Object = MibTable
aluShaperPolicyTable = _AluShaperPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9)
)
if mibBuilder.loadTexts:
    aluShaperPolicyTable.setStatus("current")
_AluShaperPolicyEntry_Object = MibTableRow
aluShaperPolicyEntry = _AluShaperPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1)
)
aluShaperPolicyEntry.setIndexNames(
    (0, "ALU-QOS-MIB", "aluShaperPolicy"),
)
if mibBuilder.loadTexts:
    aluShaperPolicyEntry.setStatus("current")
_AluShaperPolicy_Type = TNamedItem
_AluShaperPolicy_Object = MibTableColumn
aluShaperPolicy = _AluShaperPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1, 1),
    _AluShaperPolicy_Type()
)
aluShaperPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluShaperPolicy.setStatus("current")
_AluShaperPolicyRowStatus_Type = RowStatus
_AluShaperPolicyRowStatus_Object = MibTableColumn
aluShaperPolicyRowStatus = _AluShaperPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1, 2),
    _AluShaperPolicyRowStatus_Type()
)
aluShaperPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperPolicyRowStatus.setStatus("current")
_AluShaperPolicyLastChanged_Type = TimeStamp
_AluShaperPolicyLastChanged_Object = MibTableColumn
aluShaperPolicyLastChanged = _AluShaperPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1, 3),
    _AluShaperPolicyLastChanged_Type()
)
aluShaperPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShaperPolicyLastChanged.setStatus("current")


class _AluShaperPolicyDescription_Type(TItemDescription):
    """Custom type aluShaperPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_AluShaperPolicyDescription_Type.__name__ = "TItemDescription"
_AluShaperPolicyDescription_Object = MibTableColumn
aluShaperPolicyDescription = _AluShaperPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1, 4),
    _AluShaperPolicyDescription_Type()
)
aluShaperPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperPolicyDescription.setStatus("current")


class _AluShaperPolicyUnshapedSapGroup_Type(TNamedItem):
    """Custom type aluShaperPolicyUnshapedSapGroup based on TNamedItem"""
    defaultValue = OctetString("default")


_AluShaperPolicyUnshapedSapGroup_Type.__name__ = "TNamedItem"
_AluShaperPolicyUnshapedSapGroup_Object = MibTableColumn
aluShaperPolicyUnshapedSapGroup = _AluShaperPolicyUnshapedSapGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1, 5),
    _AluShaperPolicyUnshapedSapGroup_Type()
)
aluShaperPolicyUnshapedSapGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperPolicyUnshapedSapGroup.setStatus("current")


class _AluShaperPolicyUnshapedIntfGroup_Type(TNamedItem):
    """Custom type aluShaperPolicyUnshapedIntfGroup based on TNamedItem"""
    defaultValue = OctetString("default")


_AluShaperPolicyUnshapedIntfGroup_Type.__name__ = "TNamedItem"
_AluShaperPolicyUnshapedIntfGroup_Object = MibTableColumn
aluShaperPolicyUnshapedIntfGroup = _AluShaperPolicyUnshapedIntfGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 9, 1, 6),
    _AluShaperPolicyUnshapedIntfGroup_Type()
)
aluShaperPolicyUnshapedIntfGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperPolicyUnshapedIntfGroup.setStatus("current")
_AluShaperGroupTable_Object = MibTable
aluShaperGroupTable = _AluShaperGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10)
)
if mibBuilder.loadTexts:
    aluShaperGroupTable.setStatus("current")
_AluShaperGroupEntry_Object = MibTableRow
aluShaperGroupEntry = _AluShaperGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1)
)
aluShaperGroupEntry.setIndexNames(
    (0, "ALU-QOS-MIB", "aluShaperPolicy"),
    (0, "ALU-QOS-MIB", "aluShaperGroup"),
)
if mibBuilder.loadTexts:
    aluShaperGroupEntry.setStatus("current")
_AluShaperGroup_Type = TNamedItem
_AluShaperGroup_Object = MibTableColumn
aluShaperGroup = _AluShaperGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 1),
    _AluShaperGroup_Type()
)
aluShaperGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluShaperGroup.setStatus("current")
_AluShaperGroupRowStatus_Type = RowStatus
_AluShaperGroupRowStatus_Object = MibTableColumn
aluShaperGroupRowStatus = _AluShaperGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 2),
    _AluShaperGroupRowStatus_Type()
)
aluShaperGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupRowStatus.setStatus("current")


class _AluShaperGroupDescription_Type(TItemDescription):
    """Custom type aluShaperGroupDescription based on TItemDescription"""
    defaultHexValue = ""


_AluShaperGroupDescription_Type.__name__ = "TItemDescription"
_AluShaperGroupDescription_Object = MibTableColumn
aluShaperGroupDescription = _AluShaperGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 3),
    _AluShaperGroupDescription_Type()
)
aluShaperGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupDescription.setStatus("current")


class _AluShaperGroupCIR_Type(TCIRRate):
    """Custom type aluShaperGroupCIR based on TCIRRate"""
    defaultValue = 0


_AluShaperGroupCIR_Type.__name__ = "TCIRRate"
_AluShaperGroupCIR_Object = MibTableColumn
aluShaperGroupCIR = _AluShaperGroupCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 4),
    _AluShaperGroupCIR_Type()
)
aluShaperGroupCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupCIR.setStatus("current")
if mibBuilder.loadTexts:
    aluShaperGroupCIR.setUnits("kbps")


class _AluShaperGroupPIR_Type(TPIRRate):
    """Custom type aluShaperGroupPIR based on TPIRRate"""
    defaultValue = -1


_AluShaperGroupPIR_Type.__name__ = "TPIRRate"
_AluShaperGroupPIR_Object = MibTableColumn
aluShaperGroupPIR = _AluShaperGroupPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 5),
    _AluShaperGroupPIR_Type()
)
aluShaperGroupPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupPIR.setStatus("current")
if mibBuilder.loadTexts:
    aluShaperGroupPIR.setUnits("kbps")
_AluShaperGroupLastChanged_Type = TimeStamp
_AluShaperGroupLastChanged_Object = MibTableColumn
aluShaperGroupLastChanged = _AluShaperGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 6),
    _AluShaperGroupLastChanged_Type()
)
aluShaperGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluShaperGroupLastChanged.setStatus("current")


class _AluShaperGroupCIRPercent_Type(Unsigned32):
    """Custom type aluShaperGroupCIRPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AluShaperGroupCIRPercent_Type.__name__ = "Unsigned32"
_AluShaperGroupCIRPercent_Object = MibTableColumn
aluShaperGroupCIRPercent = _AluShaperGroupCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 7),
    _AluShaperGroupCIRPercent_Type()
)
aluShaperGroupCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    aluShaperGroupCIRPercent.setUnits("hundredths of a percent")


class _AluShaperGroupPIRPercent_Type(Unsigned32):
    """Custom type aluShaperGroupPIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AluShaperGroupPIRPercent_Type.__name__ = "Unsigned32"
_AluShaperGroupPIRPercent_Object = MibTableColumn
aluShaperGroupPIRPercent = _AluShaperGroupPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 8),
    _AluShaperGroupPIRPercent_Type()
)
aluShaperGroupPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    aluShaperGroupPIRPercent.setUnits("hundredths of a percent")


class _AluShaperGroupRateType_Type(TRateType):
    """Custom type aluShaperGroupRateType based on TRateType"""
    defaultValue = 1


_AluShaperGroupRateType_Type.__name__ = "TRateType"
_AluShaperGroupRateType_Object = MibTableColumn
aluShaperGroupRateType = _AluShaperGroupRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 10, 1, 9),
    _AluShaperGroupRateType_Type()
)
aluShaperGroupRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluShaperGroupRateType.setStatus("current")
_AluSecurityQueuePolicyTable_Object = MibTable
aluSecurityQueuePolicyTable = _AluSecurityQueuePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 11)
)
if mibBuilder.loadTexts:
    aluSecurityQueuePolicyTable.setStatus("current")
_AluSecurityQueuePolicyEntry_Object = MibTableRow
aluSecurityQueuePolicyEntry = _AluSecurityQueuePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 11, 1)
)
aluSecurityQueuePolicyEntry.setIndexNames(
    (0, "ALU-QOS-MIB", "aluSecurityQueuePolicyIndex"),
)
if mibBuilder.loadTexts:
    aluSecurityQueuePolicyEntry.setStatus("current")
_AluSecurityQueuePolicyIndex_Type = TPolicyID
_AluSecurityQueuePolicyIndex_Object = MibTableColumn
aluSecurityQueuePolicyIndex = _AluSecurityQueuePolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 11, 1, 1),
    _AluSecurityQueuePolicyIndex_Type()
)
aluSecurityQueuePolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecurityQueuePolicyIndex.setStatus("current")
_AluSecurityQueuePolicyRowStatus_Type = RowStatus
_AluSecurityQueuePolicyRowStatus_Object = MibTableColumn
aluSecurityQueuePolicyRowStatus = _AluSecurityQueuePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 11, 1, 2),
    _AluSecurityQueuePolicyRowStatus_Type()
)
aluSecurityQueuePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueuePolicyRowStatus.setStatus("current")


class _AluSecurityQueuePolicyDescription_Type(TItemDescription):
    """Custom type aluSecurityQueuePolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecurityQueuePolicyDescription_Type.__name__ = "TItemDescription"
_AluSecurityQueuePolicyDescription_Object = MibTableColumn
aluSecurityQueuePolicyDescription = _AluSecurityQueuePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 11, 1, 3),
    _AluSecurityQueuePolicyDescription_Type()
)
aluSecurityQueuePolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueuePolicyDescription.setStatus("current")
_AluSecurityQueuePolicyLastChanged_Type = TimeStamp
_AluSecurityQueuePolicyLastChanged_Object = MibTableColumn
aluSecurityQueuePolicyLastChanged = _AluSecurityQueuePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 11, 1, 4),
    _AluSecurityQueuePolicyLastChanged_Type()
)
aluSecurityQueuePolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecurityQueuePolicyLastChanged.setStatus("current")
_AluSecurityQueueTable_Object = MibTable
aluSecurityQueueTable = _AluSecurityQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12)
)
if mibBuilder.loadTexts:
    aluSecurityQueueTable.setStatus("current")
_AluSecurityQueueEntry_Object = MibTableRow
aluSecurityQueueEntry = _AluSecurityQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1)
)
aluSecurityQueueEntry.setIndexNames(
    (0, "ALU-QOS-MIB", "aluSecurityQueuePolicyIndex"),
    (0, "ALU-QOS-MIB", "aluSecurityQueueIndex"),
)
if mibBuilder.loadTexts:
    aluSecurityQueueEntry.setStatus("current")
_AluSecurityQueueIndex_Type = AluSecQueueId
_AluSecurityQueueIndex_Object = MibTableColumn
aluSecurityQueueIndex = _AluSecurityQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 1),
    _AluSecurityQueueIndex_Type()
)
aluSecurityQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecurityQueueIndex.setStatus("current")


class _AluSecurityQueueCIR_Type(TCIRRate):
    """Custom type aluSecurityQueueCIR based on TCIRRate"""
    defaultValue = 0


_AluSecurityQueueCIR_Type.__name__ = "TCIRRate"
_AluSecurityQueueCIR_Object = MibTableColumn
aluSecurityQueueCIR = _AluSecurityQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 2),
    _AluSecurityQueueCIR_Type()
)
aluSecurityQueueCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueueCIR.setStatus("current")
if mibBuilder.loadTexts:
    aluSecurityQueueCIR.setUnits("kbps")


class _AluSecurityQueuePIR_Type(TPIRRate):
    """Custom type aluSecurityQueuePIR based on TPIRRate"""
    defaultValue = -1


_AluSecurityQueuePIR_Type.__name__ = "TPIRRate"
_AluSecurityQueuePIR_Object = MibTableColumn
aluSecurityQueuePIR = _AluSecurityQueuePIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 3),
    _AluSecurityQueuePIR_Type()
)
aluSecurityQueuePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueuePIR.setStatus("current")
if mibBuilder.loadTexts:
    aluSecurityQueuePIR.setUnits("kbps")


class _AluSecurityQueueCBS_Type(TBurstSize):
    """Custom type aluSecurityQueueCBS based on TBurstSize"""
    defaultValue = -1


_AluSecurityQueueCBS_Type.__name__ = "TBurstSize"
_AluSecurityQueueCBS_Object = MibTableColumn
aluSecurityQueueCBS = _AluSecurityQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 4),
    _AluSecurityQueueCBS_Type()
)
aluSecurityQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    aluSecurityQueueCBS.setUnits("kilo-bytes")


class _AluSecurityQueueMBSBytes_Type(TBurstSizeBytes):
    """Custom type aluSecurityQueueMBSBytes based on TBurstSizeBytes"""
    defaultValue = 500000


_AluSecurityQueueMBSBytes_Type.__name__ = "TBurstSizeBytes"
_AluSecurityQueueMBSBytes_Object = MibTableColumn
aluSecurityQueueMBSBytes = _AluSecurityQueueMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 5),
    _AluSecurityQueueMBSBytes_Type()
)
aluSecurityQueueMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueueMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    aluSecurityQueueMBSBytes.setUnits("bytes")


class _AluSecurityQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type aluSecurityQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = 10


_AluSecurityQueueHiPrioOnly_Type.__name__ = "TBurstPercentOrDefault"
_AluSecurityQueueHiPrioOnly_Object = MibTableColumn
aluSecurityQueueHiPrioOnly = _AluSecurityQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 6),
    _AluSecurityQueueHiPrioOnly_Type()
)
aluSecurityQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecurityQueueHiPrioOnly.setStatus("current")
_AluSecurityQueueLastChanged_Type = TimeStamp
_AluSecurityQueueLastChanged_Object = MibTableColumn
aluSecurityQueueLastChanged = _AluSecurityQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 12, 1, 7),
    _AluSecurityQueueLastChanged_Type()
)
aluSecurityQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecurityQueueLastChanged.setStatus("current")
_AluExtSapIngressTable_Object = MibTable
aluExtSapIngressTable = _AluExtSapIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 13)
)
if mibBuilder.loadTexts:
    aluExtSapIngressTable.setStatus("current")
_AluExtSapIngressEntry_Object = MibTableRow
aluExtSapIngressEntry = _AluExtSapIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 13, 1)
)
if mibBuilder.loadTexts:
    aluExtSapIngressEntry.setStatus("current")


class _AluSapIngressPktOffset_Type(AluPerPacketOffset):
    """Custom type aluSapIngressPktOffset based on AluPerPacketOffset"""
    defaultValue = 127


_AluSapIngressPktOffset_Type.__name__ = "AluPerPacketOffset"
_AluSapIngressPktOffset_Object = MibTableColumn
aluSapIngressPktOffset = _AluSapIngressPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 13, 1, 1),
    _AluSapIngressPktOffset_Type()
)
aluSapIngressPktOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressPktOffset.setStatus("current")
_AluExtNetworkQueuePolicyTable_Object = MibTable
aluExtNetworkQueuePolicyTable = _AluExtNetworkQueuePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 14)
)
if mibBuilder.loadTexts:
    aluExtNetworkQueuePolicyTable.setStatus("current")
_AluExtNetworkQueuePolicyEntry_Object = MibTableRow
aluExtNetworkQueuePolicyEntry = _AluExtNetworkQueuePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 14, 1)
)
if mibBuilder.loadTexts:
    aluExtNetworkQueuePolicyEntry.setStatus("current")


class _AluNetworkQueuePolicyPktOffset_Type(AluPerPacketOffset):
    """Custom type aluNetworkQueuePolicyPktOffset based on AluPerPacketOffset"""
    defaultValue = 127


_AluNetworkQueuePolicyPktOffset_Type.__name__ = "AluPerPacketOffset"
_AluNetworkQueuePolicyPktOffset_Object = MibTableColumn
aluNetworkQueuePolicyPktOffset = _AluNetworkQueuePolicyPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 14, 1, 1),
    _AluNetworkQueuePolicyPktOffset_Type()
)
aluNetworkQueuePolicyPktOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluNetworkQueuePolicyPktOffset.setStatus("current")
tSapIngressQueueEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluSapIngressQueueExtensionEntry")
)
aluSapIngressQueueExtensionEntry.setIndexNames(*tSapIngressQueueEntry.getIndexNames())
tSapEgressQueueEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluSapEgressQueueExtensionEntry")
)
aluSapEgressQueueExtensionEntry.setIndexNames(*tSapEgressQueueEntry.getIndexNames())
tNetworkQueueEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluNetworkQueueExtensionEntry")
)
aluNetworkQueueExtensionEntry.setIndexNames(*tNetworkQueueEntry.getIndexNames())
tSapEgressEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluExtTSapEgressEntry")
)
aluExtTSapEgressEntry.setIndexNames(*tSapEgressEntry.getIndexNames())
tNetworkPolicyEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluExtNetworkPolicyEntry")
)
aluExtNetworkPolicyEntry.setIndexNames(*tNetworkPolicyEntry.getIndexNames())
tNetworkIngressDot1pEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluExtNetworkIngressDot1pEntry")
)
aluExtNetworkIngressDot1pEntry.setIndexNames(*tNetworkIngressDot1pEntry.getIndexNames())
tSapIngressEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluExtSapIngressEntry")
)
aluExtSapIngressEntry.setIndexNames(*tSapIngressEntry.getIndexNames())
tNetworkQueuePolicyEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluExtNetworkQueuePolicyEntry")
)
aluExtNetworkQueuePolicyEntry.setIndexNames(*tNetworkQueuePolicyEntry.getIndexNames())

# Managed Objects groups

aluQosQueuePolicySlopePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 31)
)
aluQosQueuePolicySlopePolicyGroup.setObjects(
      *(("ALU-QOS-MIB", "aluSapIngressQueueSlopePolicy"),
        ("ALU-QOS-MIB", "aluSapEgressQueueSlopePolicy"),
        ("ALU-QOS-MIB", "aluNetworkQueueSlopePolicy"))
)
if mibBuilder.loadTexts:
    aluQosQueuePolicySlopePolicyGroup.setStatus("current")

aluQosFabricProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 32)
)
aluQosFabricProfileGroup.setObjects(
      *(("ALU-QOS-MIB", "aluFabricProfileRowStatus"),
        ("ALU-QOS-MIB", "aluFabricProfileDescription"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex1"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex2"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex3"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex4"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex5"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex6"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex7"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex8"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex9"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex10"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex11"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex12"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex13"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex14"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex15"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex16"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex17"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex18"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex19"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex20"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex21"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex22"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex23"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex24"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex25"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex26"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex27"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex28"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex29"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex30"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex31"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex32"),
        ("ALU-QOS-MIB", "aluFabricProfileLastChanged"),
        ("ALU-QOS-MIB", "aluFabricProfileMode"),
        ("ALU-QOS-MIB", "aluFabricProfileAggregateRate"))
)
if mibBuilder.loadTexts:
    aluQosFabricProfileGroup.setStatus("obsolete")

aluQosSapEgressPolicyTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 33)
)
aluQosSapEgressPolicyTypeGroup.setObjects(
    ("ALU-QOS-MIB", "aluSapEgressPolicyType")
)
if mibBuilder.loadTexts:
    aluQosSapEgressPolicyTypeGroup.setStatus("current")

aluQosFabricProfileGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 34)
)
aluQosFabricProfileGroupV4v0.setObjects(
      *(("ALU-QOS-MIB", "aluFabricProfileRowStatus"),
        ("ALU-QOS-MIB", "aluFabricProfileDescription"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex1"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex2"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex3"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex4"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex5"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex6"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex7"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex8"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex9"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex10"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex11"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex12"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex13"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex14"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex15"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex16"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex17"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex18"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex19"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex20"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex21"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex22"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex23"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex24"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex25"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex26"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex27"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex28"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex29"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex30"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex31"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex32"),
        ("ALU-QOS-MIB", "aluFabricProfileLastChanged"),
        ("ALU-QOS-MIB", "aluFabricProfileMode"),
        ("ALU-QOS-MIB", "aluFabricProfileAggregateRate"),
        ("ALU-QOS-MIB", "aluFabricProfileMultipointRate"))
)
if mibBuilder.loadTexts:
    aluQosFabricProfileGroupV4v0.setStatus("current")

aluSystemQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 35)
)
aluSystemQosGroup.setObjects(
      *(("ALU-QOS-MIB", "aluSystemAccessIngAggRate"),
        ("ALU-QOS-MIB", "aluSystemNetworkIngAggRate"),
        ("ALU-QOS-MIB", "aluSystemQosLastChanged"))
)
if mibBuilder.loadTexts:
    aluSystemQosGroup.setStatus("current")

aluHQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 36)
)
aluHQosGroup.setObjects(
      *(("ALU-QOS-MIB", "aluFabricProfileUnshapedSapCir"),
        ("ALU-QOS-MIB", "aluSystemIngUnshapedSapCir"))
)
if mibBuilder.loadTexts:
    aluHQosGroup.setStatus("current")

aluExtNetworkPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 37)
)
aluExtNetworkPolicyGroup.setObjects(
      *(("ALU-QOS-MIB", "aluExtNetworkPolicyType"),
        ("ALU-QOS-MIB", "aluExtNetworkPolicyDefActionQueue"),
        ("ALU-QOS-MIB", "aluExtNetworkRingDot1pQueue"))
)
if mibBuilder.loadTexts:
    aluExtNetworkPolicyGroup.setStatus("current")

aluQosShaperPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 38)
)
aluQosShaperPolicyGroup.setObjects(
      *(("ALU-QOS-MIB", "aluShaperPolicyRowStatus"),
        ("ALU-QOS-MIB", "aluShaperPolicyLastChanged"),
        ("ALU-QOS-MIB", "aluShaperPolicyDescription"),
        ("ALU-QOS-MIB", "aluShaperPolicyUnshapedSapGroup"),
        ("ALU-QOS-MIB", "aluShaperPolicyUnshapedIntfGroup"),
        ("ALU-QOS-MIB", "aluShaperGroupRowStatus"),
        ("ALU-QOS-MIB", "aluShaperGroupDescription"),
        ("ALU-QOS-MIB", "aluShaperGroupCIR"),
        ("ALU-QOS-MIB", "aluShaperGroupPIR"),
        ("ALU-QOS-MIB", "aluShaperGroupLastChanged"))
)
if mibBuilder.loadTexts:
    aluQosShaperPolicyGroup.setStatus("current")

aluSecurityQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 39)
)
aluSecurityQueueGroup.setObjects(
      *(("ALU-QOS-MIB", "aluSecurityQueuePolicyRowStatus"),
        ("ALU-QOS-MIB", "aluSecurityQueuePolicyDescription"),
        ("ALU-QOS-MIB", "aluSecurityQueuePolicyLastChanged"),
        ("ALU-QOS-MIB", "aluSecurityQueueCIR"),
        ("ALU-QOS-MIB", "aluSecurityQueuePIR"),
        ("ALU-QOS-MIB", "aluSecurityQueueCBS"),
        ("ALU-QOS-MIB", "aluSecurityQueueMBSBytes"),
        ("ALU-QOS-MIB", "aluSecurityQueueHiPrioOnly"),
        ("ALU-QOS-MIB", "aluSecurityQueueLastChanged"))
)
if mibBuilder.loadTexts:
    aluSecurityQueueGroup.setStatus("current")

aluExtQosV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 40)
)
aluExtQosV7v0Group.setObjects(
      *(("ALU-QOS-MIB", "aluSapIngressPktOffset"),
        ("ALU-QOS-MIB", "aluSapEgressPktOffset"),
        ("ALU-QOS-MIB", "aluNetworkQueuePolicyPktOffset"),
        ("ALU-QOS-MIB", "aluSapIngressQueuePktOffset"),
        ("ALU-QOS-MIB", "aluSapEgressQueuePktOffset"),
        ("ALU-QOS-MIB", "aluNetworkQueuePktOffset"))
)
if mibBuilder.loadTexts:
    aluExtQosV7v0Group.setStatus("current")

aluQosV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 41)
)
aluQosV9v0Group.setObjects(
      *(("ALU-QOS-MIB", "aluShaperGroupCIRPercent"),
        ("ALU-QOS-MIB", "aluShaperGroupPIRPercent"),
        ("ALU-QOS-MIB", "aluShaperGroupRateType"))
)
if mibBuilder.loadTexts:
    aluQosV9v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluQOSComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 1)
)
aluQOSComp7705V1v0.setObjects(
      *(("ALU-QOS-MIB", "aluQosQueuePolicySlopePolicyGroup"),
        ("ALU-QOS-MIB", "aluQosFabricProfileGroup"),
        ("ALU-QOS-MIB", "aluQosSapEgressPolicyTypeGroup"))
)
if mibBuilder.loadTexts:
    aluQOSComp7705V1v0.setStatus(
        "obsolete"
    )

aluQOSComp7705V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 2)
)
aluQOSComp7705V4v0.setObjects(
    ("ALU-QOS-MIB", "aluQosFabricProfileGroupV4v0")
)
if mibBuilder.loadTexts:
    aluQOSComp7705V4v0.setStatus(
        "obsolete"
    )

aluQOSComp7705V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 3)
)
aluQOSComp7705V5v0.setObjects(
      *(("ALU-QOS-MIB", "aluQosQueuePolicySlopePolicyGroup"),
        ("ALU-QOS-MIB", "aluQosFabricProfileGroup"),
        ("ALU-QOS-MIB", "aluQosSapEgressPolicyTypeGroup"),
        ("ALU-QOS-MIB", "aluQosFabricProfileGroupV4v0"),
        ("ALU-QOS-MIB", "aluSystemQosGroup"))
)
if mibBuilder.loadTexts:
    aluQOSComp7705V5v0.setStatus(
        "current"
    )

aluQOSComp7705V7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 4)
)
aluQOSComp7705V7v0.setObjects(
      *(("ALU-QOS-MIB", "aluHQosGroup"),
        ("ALU-QOS-MIB", "aluExtNetworkPolicyGroup"),
        ("ALU-QOS-MIB", "aluQosShaperPolicyGroup"),
        ("ALU-QOS-MIB", "aluSecurityQueueGroup"))
)
if mibBuilder.loadTexts:
    aluQOSComp7705V7v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-QOS-MIB",
    **{"AluIPsecStatsQueueId": AluIPsecStatsQueueId,
       "AluSecQueueId": AluSecQueueId,
       "AluFabricProfilePolicyID": AluFabricProfilePolicyID,
       "AluFabricProfileMode": AluFabricProfileMode,
       "AluFabricProfileDestMdaRate": AluFabricProfileDestMdaRate,
       "AluSapSchedulerCir": AluSapSchedulerCir,
       "AluSystemAggregateRate": AluSystemAggregateRate,
       "AluExtNetworkPolicyType": AluExtNetworkPolicyType,
       "AluPerPacketOffset": AluPerPacketOffset,
       "aluQOSMIBModule": aluQOSMIBModule,
       "aluQOSConformance": aluQOSConformance,
       "aluQOSCompliances": aluQOSCompliances,
       "aluQOSComp7705": aluQOSComp7705,
       "aluQOSComp7705V1v0": aluQOSComp7705V1v0,
       "aluQOSComp7705V4v0": aluQOSComp7705V4v0,
       "aluQOSComp7705V5v0": aluQOSComp7705V5v0,
       "aluQOSComp7705V7v0": aluQOSComp7705V7v0,
       "aluQOSGroups": aluQOSGroups,
       "aluQosQueuePolicySlopePolicyGroup": aluQosQueuePolicySlopePolicyGroup,
       "aluQosFabricProfileGroup": aluQosFabricProfileGroup,
       "aluQosSapEgressPolicyTypeGroup": aluQosSapEgressPolicyTypeGroup,
       "aluQosFabricProfileGroupV4v0": aluQosFabricProfileGroupV4v0,
       "aluSystemQosGroup": aluSystemQosGroup,
       "aluHQosGroup": aluHQosGroup,
       "aluExtNetworkPolicyGroup": aluExtNetworkPolicyGroup,
       "aluQosShaperPolicyGroup": aluQosShaperPolicyGroup,
       "aluSecurityQueueGroup": aluSecurityQueueGroup,
       "aluExtQosV7v0Group": aluExtQosV7v0Group,
       "aluQosV9v0Group": aluQosV9v0Group,
       "aluQOSObjs": aluQOSObjs,
       "aluSapIngressQueueExtensionTable": aluSapIngressQueueExtensionTable,
       "aluSapIngressQueueExtensionEntry": aluSapIngressQueueExtensionEntry,
       "aluSapIngressQueueSlopePolicy": aluSapIngressQueueSlopePolicy,
       "aluSapIngressQueuePktOffset": aluSapIngressQueuePktOffset,
       "aluSapEgressQueueExtensionTable": aluSapEgressQueueExtensionTable,
       "aluSapEgressQueueExtensionEntry": aluSapEgressQueueExtensionEntry,
       "aluSapEgressQueueSlopePolicy": aluSapEgressQueueSlopePolicy,
       "aluSapEgressQueuePktOffset": aluSapEgressQueuePktOffset,
       "aluNetworkQueueExtensionTable": aluNetworkQueueExtensionTable,
       "aluNetworkQueueExtensionEntry": aluNetworkQueueExtensionEntry,
       "aluNetworkQueueSlopePolicy": aluNetworkQueueSlopePolicy,
       "aluNetworkQueuePktOffset": aluNetworkQueuePktOffset,
       "aluFabricProfileTable": aluFabricProfileTable,
       "aluFabricProfileEntry": aluFabricProfileEntry,
       "aluFabricProfileIndex": aluFabricProfileIndex,
       "aluFabricProfileRowStatus": aluFabricProfileRowStatus,
       "aluFabricProfileDescription": aluFabricProfileDescription,
       "aluFabricProfileRateToMdaIndex1": aluFabricProfileRateToMdaIndex1,
       "aluFabricProfileRateToMdaIndex2": aluFabricProfileRateToMdaIndex2,
       "aluFabricProfileRateToMdaIndex3": aluFabricProfileRateToMdaIndex3,
       "aluFabricProfileRateToMdaIndex4": aluFabricProfileRateToMdaIndex4,
       "aluFabricProfileRateToMdaIndex5": aluFabricProfileRateToMdaIndex5,
       "aluFabricProfileRateToMdaIndex6": aluFabricProfileRateToMdaIndex6,
       "aluFabricProfileRateToMdaIndex7": aluFabricProfileRateToMdaIndex7,
       "aluFabricProfileRateToMdaIndex8": aluFabricProfileRateToMdaIndex8,
       "aluFabricProfileRateToMdaIndex9": aluFabricProfileRateToMdaIndex9,
       "aluFabricProfileRateToMdaIndex10": aluFabricProfileRateToMdaIndex10,
       "aluFabricProfileRateToMdaIndex11": aluFabricProfileRateToMdaIndex11,
       "aluFabricProfileRateToMdaIndex12": aluFabricProfileRateToMdaIndex12,
       "aluFabricProfileRateToMdaIndex13": aluFabricProfileRateToMdaIndex13,
       "aluFabricProfileRateToMdaIndex14": aluFabricProfileRateToMdaIndex14,
       "aluFabricProfileRateToMdaIndex15": aluFabricProfileRateToMdaIndex15,
       "aluFabricProfileRateToMdaIndex16": aluFabricProfileRateToMdaIndex16,
       "aluFabricProfileRateToMdaIndex17": aluFabricProfileRateToMdaIndex17,
       "aluFabricProfileRateToMdaIndex18": aluFabricProfileRateToMdaIndex18,
       "aluFabricProfileRateToMdaIndex19": aluFabricProfileRateToMdaIndex19,
       "aluFabricProfileRateToMdaIndex20": aluFabricProfileRateToMdaIndex20,
       "aluFabricProfileRateToMdaIndex21": aluFabricProfileRateToMdaIndex21,
       "aluFabricProfileRateToMdaIndex22": aluFabricProfileRateToMdaIndex22,
       "aluFabricProfileRateToMdaIndex23": aluFabricProfileRateToMdaIndex23,
       "aluFabricProfileRateToMdaIndex24": aluFabricProfileRateToMdaIndex24,
       "aluFabricProfileRateToMdaIndex25": aluFabricProfileRateToMdaIndex25,
       "aluFabricProfileRateToMdaIndex26": aluFabricProfileRateToMdaIndex26,
       "aluFabricProfileRateToMdaIndex27": aluFabricProfileRateToMdaIndex27,
       "aluFabricProfileRateToMdaIndex28": aluFabricProfileRateToMdaIndex28,
       "aluFabricProfileRateToMdaIndex29": aluFabricProfileRateToMdaIndex29,
       "aluFabricProfileRateToMdaIndex30": aluFabricProfileRateToMdaIndex30,
       "aluFabricProfileRateToMdaIndex31": aluFabricProfileRateToMdaIndex31,
       "aluFabricProfileRateToMdaIndex32": aluFabricProfileRateToMdaIndex32,
       "aluFabricProfileLastChanged": aluFabricProfileLastChanged,
       "aluFabricProfileMode": aluFabricProfileMode,
       "aluFabricProfileAggregateRate": aluFabricProfileAggregateRate,
       "aluFabricProfileMultipointRate": aluFabricProfileMultipointRate,
       "aluFabricProfileUnshapedSapCir": aluFabricProfileUnshapedSapCir,
       "aluExtTSapEgressTable": aluExtTSapEgressTable,
       "aluExtTSapEgressEntry": aluExtTSapEgressEntry,
       "aluSapEgressPolicyType": aluSapEgressPolicyType,
       "aluSapEgressPktOffset": aluSapEgressPktOffset,
       "aluSystemQosConfig": aluSystemQosConfig,
       "aluSystemAccessIngAggRate": aluSystemAccessIngAggRate,
       "aluSystemNetworkIngAggRate": aluSystemNetworkIngAggRate,
       "aluSystemQosLastChanged": aluSystemQosLastChanged,
       "aluSystemIngUnshapedSapCir": aluSystemIngUnshapedSapCir,
       "aluExtNetworkPolicyTable": aluExtNetworkPolicyTable,
       "aluExtNetworkPolicyEntry": aluExtNetworkPolicyEntry,
       "aluExtNetworkPolicyType": aluExtNetworkPolicyType,
       "aluExtNetworkPolicyDefActionQueue": aluExtNetworkPolicyDefActionQueue,
       "aluExtNetworkIngressDot1pTable": aluExtNetworkIngressDot1pTable,
       "aluExtNetworkIngressDot1pEntry": aluExtNetworkIngressDot1pEntry,
       "aluExtNetworkRingDot1pQueue": aluExtNetworkRingDot1pQueue,
       "aluShaperPolicyTable": aluShaperPolicyTable,
       "aluShaperPolicyEntry": aluShaperPolicyEntry,
       "aluShaperPolicy": aluShaperPolicy,
       "aluShaperPolicyRowStatus": aluShaperPolicyRowStatus,
       "aluShaperPolicyLastChanged": aluShaperPolicyLastChanged,
       "aluShaperPolicyDescription": aluShaperPolicyDescription,
       "aluShaperPolicyUnshapedSapGroup": aluShaperPolicyUnshapedSapGroup,
       "aluShaperPolicyUnshapedIntfGroup": aluShaperPolicyUnshapedIntfGroup,
       "aluShaperGroupTable": aluShaperGroupTable,
       "aluShaperGroupEntry": aluShaperGroupEntry,
       "aluShaperGroup": aluShaperGroup,
       "aluShaperGroupRowStatus": aluShaperGroupRowStatus,
       "aluShaperGroupDescription": aluShaperGroupDescription,
       "aluShaperGroupCIR": aluShaperGroupCIR,
       "aluShaperGroupPIR": aluShaperGroupPIR,
       "aluShaperGroupLastChanged": aluShaperGroupLastChanged,
       "aluShaperGroupCIRPercent": aluShaperGroupCIRPercent,
       "aluShaperGroupPIRPercent": aluShaperGroupPIRPercent,
       "aluShaperGroupRateType": aluShaperGroupRateType,
       "aluSecurityQueuePolicyTable": aluSecurityQueuePolicyTable,
       "aluSecurityQueuePolicyEntry": aluSecurityQueuePolicyEntry,
       "aluSecurityQueuePolicyIndex": aluSecurityQueuePolicyIndex,
       "aluSecurityQueuePolicyRowStatus": aluSecurityQueuePolicyRowStatus,
       "aluSecurityQueuePolicyDescription": aluSecurityQueuePolicyDescription,
       "aluSecurityQueuePolicyLastChanged": aluSecurityQueuePolicyLastChanged,
       "aluSecurityQueueTable": aluSecurityQueueTable,
       "aluSecurityQueueEntry": aluSecurityQueueEntry,
       "aluSecurityQueueIndex": aluSecurityQueueIndex,
       "aluSecurityQueueCIR": aluSecurityQueueCIR,
       "aluSecurityQueuePIR": aluSecurityQueuePIR,
       "aluSecurityQueueCBS": aluSecurityQueueCBS,
       "aluSecurityQueueMBSBytes": aluSecurityQueueMBSBytes,
       "aluSecurityQueueHiPrioOnly": aluSecurityQueueHiPrioOnly,
       "aluSecurityQueueLastChanged": aluSecurityQueueLastChanged,
       "aluExtSapIngressTable": aluExtSapIngressTable,
       "aluExtSapIngressEntry": aluExtSapIngressEntry,
       "aluSapIngressPktOffset": aluSapIngressPktOffset,
       "aluExtNetworkQueuePolicyTable": aluExtNetworkQueuePolicyTable,
       "aluExtNetworkQueuePolicyEntry": aluExtNetworkQueuePolicyEntry,
       "aluNetworkQueuePolicyPktOffset": aluNetworkQueuePolicyPktOffset}
)
