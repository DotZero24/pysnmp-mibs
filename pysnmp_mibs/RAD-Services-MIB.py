# SNMP MIB module (RAD-Services-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-Services-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:58 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(VlanIdOrAnyOrNone,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrAnyOrNone",
    "VlanIdOrNone")

(radGen,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radGen")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

services = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class ProfileMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1p", 2),
          ("tos", 3),
          ("dscp", 4),
          ("ipPrecedence", 5),
          ("userPorts", 6),
          ("internalCos", 7),
          ("dei", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Wfq_ObjectIdentity = ObjectIdentity
wfq = _Wfq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1)
)
_WfqTable_Object = MibTable
wfqTable = _WfqTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wfqTable.setStatus("current")
_WfqEntry_Object = MibTableRow
wfqEntry = _WfqEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1)
)
wfqEntry.setIndexNames(
    (0, "RAD-Services-MIB", "wfqCnfgIdx"),
    (0, "RAD-Services-MIB", "wfqPrtIdx"),
    (0, "RAD-Services-MIB", "wfqTblIdx"),
    (0, "RAD-Services-MIB", "wfqQueueIdx"),
)
if mibBuilder.loadTexts:
    wfqEntry.setStatus("current")


class _WfqCnfgIdx_Type(Integer32):
    """Custom type wfqCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfqCnfgIdx_Type.__name__ = "Integer32"
_WfqCnfgIdx_Object = MibTableColumn
wfqCnfgIdx = _WfqCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 1),
    _WfqCnfgIdx_Type()
)
wfqCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfqCnfgIdx.setStatus("current")
_WfqPrtIdx_Type = Integer32
_WfqPrtIdx_Object = MibTableColumn
wfqPrtIdx = _WfqPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 2),
    _WfqPrtIdx_Type()
)
wfqPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfqPrtIdx.setStatus("current")
_WfqTblIdx_Type = Integer32
_WfqTblIdx_Object = MibTableColumn
wfqTblIdx = _WfqTblIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 3),
    _WfqTblIdx_Type()
)
wfqTblIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfqTblIdx.setStatus("current")
_WfqQueueIdx_Type = Integer32
_WfqQueueIdx_Object = MibTableColumn
wfqQueueIdx = _WfqQueueIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 4),
    _WfqQueueIdx_Type()
)
wfqQueueIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfqQueueIdx.setStatus("current")
_WfqRowStatus_Type = RowStatus
_WfqRowStatus_Object = MibTableColumn
wfqRowStatus = _WfqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 5),
    _WfqRowStatus_Type()
)
wfqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqRowStatus.setStatus("current")


class _WfqWeightValue_Type(Integer32):
    """Custom type wfqWeightValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfqWeightValue_Type.__name__ = "Integer32"
_WfqWeightValue_Object = MibTableColumn
wfqWeightValue = _WfqWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 6),
    _WfqWeightValue_Type()
)
wfqWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqWeightValue.setStatus("current")
if mibBuilder.loadTexts:
    wfqWeightValue.setUnits("%")


class _WfqSchedulingMode_Type(Integer32):
    """Custom type wfqSchedulingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_WfqSchedulingMode_Type.__name__ = "Integer32"
_WfqSchedulingMode_Object = MibTableColumn
wfqSchedulingMode = _WfqSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 7),
    _WfqSchedulingMode_Type()
)
wfqSchedulingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqSchedulingMode.setStatus("current")
_WfqMinRateAbsolute_Type = Unsigned32
_WfqMinRateAbsolute_Object = MibTableColumn
wfqMinRateAbsolute = _WfqMinRateAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 8),
    _WfqMinRateAbsolute_Type()
)
wfqMinRateAbsolute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqMinRateAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    wfqMinRateAbsolute.setUnits("Kbps")
_WfqMaxPacketSize_Type = Unsigned32
_WfqMaxPacketSize_Object = MibTableColumn
wfqMaxPacketSize = _WfqMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 1, 1, 1, 9),
    _WfqMaxPacketSize_Type()
)
wfqMaxPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqMaxPacketSize.setStatus("current")
_DscpMapping_ObjectIdentity = ObjectIdentity
dscpMapping = _DscpMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 2)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 2, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "RAD-Services-MIB", "dscpMappingCnfgIdx"),
    (0, "RAD-Services-MIB", "dscpMappingDscpIdx"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")


class _DscpMappingCnfgIdx_Type(Integer32):
    """Custom type dscpMappingCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DscpMappingCnfgIdx_Type.__name__ = "Integer32"
_DscpMappingCnfgIdx_Object = MibTableColumn
dscpMappingCnfgIdx = _DscpMappingCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 2, 1, 1, 1),
    _DscpMappingCnfgIdx_Type()
)
dscpMappingCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dscpMappingCnfgIdx.setStatus("current")
_DscpMappingDscpIdx_Type = Dscp
_DscpMappingDscpIdx_Object = MibTableColumn
dscpMappingDscpIdx = _DscpMappingDscpIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 2, 1, 1, 2),
    _DscpMappingDscpIdx_Type()
)
dscpMappingDscpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dscpMappingDscpIdx.setStatus("current")
_DscpMappingRegenPriority_Type = Integer32
_DscpMappingRegenPriority_Object = MibTableColumn
dscpMappingRegenPriority = _DscpMappingRegenPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 2, 1, 1, 3),
    _DscpMappingRegenPriority_Type()
)
dscpMappingRegenPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMappingRegenPriority.setStatus("current")
_IfTeQos_ObjectIdentity = ObjectIdentity
ifTeQos = _IfTeQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3)
)
_IfTeQosTable_Object = MibTable
ifTeQosTable = _IfTeQosTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ifTeQosTable.setStatus("current")
_IfTeQosEntry_Object = MibTableRow
ifTeQosEntry = _IfTeQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1)
)
ifTeQosEntry.setIndexNames(
    (0, "RAD-Services-MIB", "ifTeQosIdx1"),
    (0, "RAD-Services-MIB", "ifTeQosIdx2"),
    (0, "RAD-Services-MIB", "ifTeQosIdx3"),
)
if mibBuilder.loadTexts:
    ifTeQosEntry.setStatus("current")
_IfTeQosIdx1_Type = Integer32
_IfTeQosIdx1_Object = MibTableColumn
ifTeQosIdx1 = _IfTeQosIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1, 1),
    _IfTeQosIdx1_Type()
)
ifTeQosIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTeQosIdx1.setStatus("current")
_IfTeQosIdx2_Type = Integer32
_IfTeQosIdx2_Object = MibTableColumn
ifTeQosIdx2 = _IfTeQosIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1, 2),
    _IfTeQosIdx2_Type()
)
ifTeQosIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTeQosIdx2.setStatus("current")
_IfTeQosIdx3_Type = Integer32
_IfTeQosIdx3_Object = MibTableColumn
ifTeQosIdx3 = _IfTeQosIdx3_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1, 3),
    _IfTeQosIdx3_Type()
)
ifTeQosIdx3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTeQosIdx3.setStatus("current")
_IfTeQosParam_Type = OctetString
_IfTeQosParam_Object = MibTableColumn
ifTeQosParam = _IfTeQosParam_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1, 4),
    _IfTeQosParam_Type()
)
ifTeQosParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTeQosParam.setStatus("current")
_IfTeQosParam2_Type = OctetString
_IfTeQosParam2_Object = MibTableColumn
ifTeQosParam2 = _IfTeQosParam2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1, 5),
    _IfTeQosParam2_Type()
)
ifTeQosParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTeQosParam2.setStatus("current")


class _IfTeQosStatus_Type(Integer32):
    """Custom type ifTeQosStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_IfTeQosStatus_Type.__name__ = "Integer32"
_IfTeQosStatus_Object = MibTableColumn
ifTeQosStatus = _IfTeQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 3, 1, 1, 6),
    _IfTeQosStatus_Type()
)
ifTeQosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTeQosStatus.setStatus("current")
_PortQos_ObjectIdentity = ObjectIdentity
portQos = _PortQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4)
)
_PrtPriorityTable_Object = MibTable
prtPriorityTable = _PrtPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 1)
)
if mibBuilder.loadTexts:
    prtPriorityTable.setStatus("current")
_PrtPriorityEntry_Object = MibTableRow
prtPriorityEntry = _PrtPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 1, 1)
)
prtPriorityEntry.setIndexNames(
    (0, "RAD-Services-MIB", "prtPriorityIdx1"),
    (0, "RAD-Services-MIB", "prtPriorityPrtIdx"),
    (0, "RAD-Services-MIB", "prtPriorityIdx"),
)
if mibBuilder.loadTexts:
    prtPriorityEntry.setStatus("current")


class _PrtPriorityIdx1_Type(Integer32):
    """Custom type prtPriorityIdx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtPriorityIdx1_Type.__name__ = "Integer32"
_PrtPriorityIdx1_Object = MibTableColumn
prtPriorityIdx1 = _PrtPriorityIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 1, 1, 1),
    _PrtPriorityIdx1_Type()
)
prtPriorityIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtPriorityIdx1.setStatus("current")


class _PrtPriorityPrtIdx_Type(Integer32):
    """Custom type prtPriorityPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrtPriorityPrtIdx_Type.__name__ = "Integer32"
_PrtPriorityPrtIdx_Object = MibTableColumn
prtPriorityPrtIdx = _PrtPriorityPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 1, 1, 2),
    _PrtPriorityPrtIdx_Type()
)
prtPriorityPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtPriorityPrtIdx.setStatus("current")


class _PrtPriorityIdx_Type(Integer32):
    """Custom type prtPriorityIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrtPriorityIdx_Type.__name__ = "Integer32"
_PrtPriorityIdx_Object = MibTableColumn
prtPriorityIdx = _PrtPriorityIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 1, 1, 3),
    _PrtPriorityIdx_Type()
)
prtPriorityIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtPriorityIdx.setStatus("current")
_PrtPriorityIngressRateLimit_Type = Integer32
_PrtPriorityIngressRateLimit_Object = MibTableColumn
prtPriorityIngressRateLimit = _PrtPriorityIngressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 1, 1, 4),
    _PrtPriorityIngressRateLimit_Type()
)
prtPriorityIngressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPriorityIngressRateLimit.setStatus("current")
_PrtQosTable_Object = MibTable
prtQosTable = _PrtQosTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2)
)
if mibBuilder.loadTexts:
    prtQosTable.setStatus("current")
_PrtQosEntry_Object = MibTableRow
prtQosEntry = _PrtQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1)
)
prtQosEntry.setIndexNames(
    (0, "RAD-Services-MIB", "prtQosIdx"),
    (0, "RAD-Services-MIB", "prtQosPrtIdx"),
    (0, "RAD-Services-MIB", "prtQosDirection"),
)
if mibBuilder.loadTexts:
    prtQosEntry.setStatus("current")
_PrtQosIdx_Type = Unsigned32
_PrtQosIdx_Object = MibTableColumn
prtQosIdx = _PrtQosIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 1),
    _PrtQosIdx_Type()
)
prtQosIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtQosIdx.setStatus("current")
_PrtQosPrtIdx_Type = Unsigned32
_PrtQosPrtIdx_Object = MibTableColumn
prtQosPrtIdx = _PrtQosPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 2),
    _PrtQosPrtIdx_Type()
)
prtQosPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtQosPrtIdx.setStatus("current")


class _PrtQosDirection_Type(Integer32):
    """Custom type prtQosDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ingress", 2),
          ("egress", 3))
    )


_PrtQosDirection_Type.__name__ = "Integer32"
_PrtQosDirection_Object = MibTableColumn
prtQosDirection = _PrtQosDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 3),
    _PrtQosDirection_Type()
)
prtQosDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtQosDirection.setStatus("current")


class _PrtQosRateLimitPacketType_Type(Integer32):
    """Custom type prtQosRateLimitPacketType based on Integer32"""
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
        *(("all", 1),
          ("bcastAndMcastAndFloodedUcast", 2),
          ("bcastAndMcast", 3),
          ("bcast", 4))
    )


_PrtQosRateLimitPacketType_Type.__name__ = "Integer32"
_PrtQosRateLimitPacketType_Object = MibTableColumn
prtQosRateLimitPacketType = _PrtQosRateLimitPacketType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 4),
    _PrtQosRateLimitPacketType_Type()
)
prtQosRateLimitPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtQosRateLimitPacketType.setStatus("current")
_PrtQosRateLimitCIR_Type = Unsigned32
_PrtQosRateLimitCIR_Object = MibTableColumn
prtQosRateLimitCIR = _PrtQosRateLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 5),
    _PrtQosRateLimitCIR_Type()
)
prtQosRateLimitCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtQosRateLimitCIR.setStatus("current")
_PrtQosRateLimitCBS_Type = Unsigned32
_PrtQosRateLimitCBS_Object = MibTableColumn
prtQosRateLimitCBS = _PrtQosRateLimitCBS_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 6),
    _PrtQosRateLimitCBS_Type()
)
prtQosRateLimitCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtQosRateLimitCBS.setStatus("current")
_PrtQosRateLimitEIR_Type = Unsigned32
_PrtQosRateLimitEIR_Object = MibTableColumn
prtQosRateLimitEIR = _PrtQosRateLimitEIR_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 7),
    _PrtQosRateLimitEIR_Type()
)
prtQosRateLimitEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtQosRateLimitEIR.setStatus("current")
_PrtQosRateLimitEBS_Type = Unsigned32
_PrtQosRateLimitEBS_Object = MibTableColumn
prtQosRateLimitEBS = _PrtQosRateLimitEBS_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 4, 2, 1, 8),
    _PrtQosRateLimitEBS_Type()
)
prtQosRateLimitEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtQosRateLimitEBS.setStatus("current")
_PrtTrafficClass_ObjectIdentity = ObjectIdentity
prtTrafficClass = _PrtTrafficClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 5)
)
_PortTrafficClassTable_Object = MibTable
portTrafficClassTable = _PortTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 5, 1)
)
if mibBuilder.loadTexts:
    portTrafficClassTable.setStatus("current")
_PortTrafficClassEntry_Object = MibTableRow
portTrafficClassEntry = _PortTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 5, 1, 1)
)
portTrafficClassEntry.setIndexNames(
    (0, "RAD-Services-MIB", "portTrafficClassIdx1"),
    (0, "RAD-Services-MIB", "portTrafficClassPortIdx"),
)
if mibBuilder.loadTexts:
    portTrafficClassEntry.setStatus("current")


class _PortTrafficClassIdx1_Type(Integer32):
    """Custom type portTrafficClassIdx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortTrafficClassIdx1_Type.__name__ = "Integer32"
_PortTrafficClassIdx1_Object = MibTableColumn
portTrafficClassIdx1 = _PortTrafficClassIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 5, 1, 1, 1),
    _PortTrafficClassIdx1_Type()
)
portTrafficClassIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portTrafficClassIdx1.setStatus("current")


class _PortTrafficClassPortIdx_Type(Integer32):
    """Custom type portTrafficClassPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortTrafficClassPortIdx_Type.__name__ = "Integer32"
_PortTrafficClassPortIdx_Object = MibTableColumn
portTrafficClassPortIdx = _PortTrafficClassPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 5, 1, 1, 2),
    _PortTrafficClassPortIdx_Type()
)
portTrafficClassPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portTrafficClassPortIdx.setStatus("current")


class _PortTrafficClass_Type(Integer32):
    """Custom type portTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortTrafficClass_Type.__name__ = "Integer32"
_PortTrafficClass_Object = MibTableColumn
portTrafficClass = _PortTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 5, 1, 1, 3),
    _PortTrafficClass_Type()
)
portTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrafficClass.setStatus("current")
_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("current")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6, 1)
)
serviceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-Services-MIB", "flowIndex"),
    (0, "RAD-Services-MIB", "serviceIndex"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("current")
_FlowIndex_Type = Unsigned32
_FlowIndex_Object = MibTableColumn
flowIndex = _FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6, 1, 1),
    _FlowIndex_Type()
)
flowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowIndex.setStatus("current")
_ServiceIndex_Type = Unsigned32
_ServiceIndex_Object = MibTableColumn
serviceIndex = _ServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6, 1, 2),
    _ServiceIndex_Type()
)
serviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceIndex.setStatus("current")
_ServiceRowStatus_Type = RowStatus
_ServiceRowStatus_Object = MibTableColumn
serviceRowStatus = _ServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6, 1, 3),
    _ServiceRowStatus_Type()
)
serviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceRowStatus.setStatus("current")
_ServiceName_Type = SnmpAdminString
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6, 1, 4),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")
_ServiceBwProfileId_Type = Unsigned32
_ServiceBwProfileId_Object = MibTableColumn
serviceBwProfileId = _ServiceBwProfileId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 6, 1, 5),
    _ServiceBwProfileId_Type()
)
serviceBwProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceBwProfileId.setStatus("current")
_EvcCosTable_Object = MibTable
evcCosTable = _EvcCosTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7)
)
if mibBuilder.loadTexts:
    evcCosTable.setStatus("current")
_EvcCosEntry_Object = MibTableRow
evcCosEntry = _EvcCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7, 1)
)
evcCosEntry.setIndexNames(
    (0, "RAD-Services-MIB", "evcCosCnfgIdx"),
    (0, "RAD-Services-MIB", "evcCosEvcIdx"),
)
if mibBuilder.loadTexts:
    evcCosEntry.setStatus("current")


class _EvcCosCnfgIdx_Type(Unsigned32):
    """Custom type evcCosCnfgIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EvcCosCnfgIdx_Type.__name__ = "Unsigned32"
_EvcCosCnfgIdx_Object = MibTableColumn
evcCosCnfgIdx = _EvcCosCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7, 1, 1),
    _EvcCosCnfgIdx_Type()
)
evcCosCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evcCosCnfgIdx.setStatus("current")


class _EvcCosEvcIdx_Type(Unsigned32):
    """Custom type evcCosEvcIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EvcCosEvcIdx_Type.__name__ = "Unsigned32"
_EvcCosEvcIdx_Object = MibTableColumn
evcCosEvcIdx = _EvcCosEvcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7, 1, 2),
    _EvcCosEvcIdx_Type()
)
evcCosEvcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evcCosEvcIdx.setStatus("current")
_EvcCosRowStatus_Type = RowStatus
_EvcCosRowStatus_Object = MibTableColumn
evcCosRowStatus = _EvcCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7, 1, 3),
    _EvcCosRowStatus_Type()
)
evcCosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    evcCosRowStatus.setStatus("current")
_EvcCosEvcName_Type = SnmpAdminString
_EvcCosEvcName_Object = MibTableColumn
evcCosEvcName = _EvcCosEvcName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7, 1, 5),
    _EvcCosEvcName_Type()
)
evcCosEvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    evcCosEvcName.setStatus("current")
_EvcCosSpVlanId_Type = Unsigned32
_EvcCosSpVlanId_Object = MibTableColumn
evcCosSpVlanId = _EvcCosSpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 7, 1, 6),
    _EvcCosSpVlanId_Type()
)
evcCosSpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    evcCosSpVlanId.setStatus("current")
_ServiceStatTable_Object = MibTable
serviceStatTable = _ServiceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8)
)
if mibBuilder.loadTexts:
    serviceStatTable.setStatus("current")
_ServiceStatEntry_Object = MibTableRow
serviceStatEntry = _ServiceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1)
)
serviceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-Services-MIB", "flowIndex"),
    (0, "RAD-Services-MIB", "serviceIndex"),
    (0, "RAD-Services-MIB", "serviceStatDirection"),
)
if mibBuilder.loadTexts:
    serviceStatEntry.setStatus("current")


class _ServiceStatDirection_Type(Integer32):
    """Custom type serviceStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2),
          ("notApplicable", 255))
    )


_ServiceStatDirection_Type.__name__ = "Integer32"
_ServiceStatDirection_Object = MibTableColumn
serviceStatDirection = _ServiceStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 1),
    _ServiceStatDirection_Type()
)
serviceStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceStatDirection.setStatus("current")
_SrvForwardGreenPackets_Type = Counter32
_SrvForwardGreenPackets_Object = MibTableColumn
srvForwardGreenPackets = _SrvForwardGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 2),
    _SrvForwardGreenPackets_Type()
)
srvForwardGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardGreenPackets.setStatus("current")
_SrvForwardGreenPacketsOverflow_Type = Counter32
_SrvForwardGreenPacketsOverflow_Object = MibTableColumn
srvForwardGreenPacketsOverflow = _SrvForwardGreenPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 3),
    _SrvForwardGreenPacketsOverflow_Type()
)
srvForwardGreenPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardGreenPacketsOverflow.setStatus("current")
_SrvForwardYellowPackets_Type = Counter32
_SrvForwardYellowPackets_Object = MibTableColumn
srvForwardYellowPackets = _SrvForwardYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 4),
    _SrvForwardYellowPackets_Type()
)
srvForwardYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardYellowPackets.setStatus("current")
_SrvForwardYellowPacketsOverflow_Type = Counter32
_SrvForwardYellowPacketsOverflow_Object = MibTableColumn
srvForwardYellowPacketsOverflow = _SrvForwardYellowPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 5),
    _SrvForwardYellowPacketsOverflow_Type()
)
srvForwardYellowPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardYellowPacketsOverflow.setStatus("current")
_SrvDiscardGreenPackets_Type = Counter32
_SrvDiscardGreenPackets_Object = MibTableColumn
srvDiscardGreenPackets = _SrvDiscardGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 6),
    _SrvDiscardGreenPackets_Type()
)
srvDiscardGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardGreenPackets.setStatus("current")
_SrvDiscardGreenPacketsOverflow_Type = Counter32
_SrvDiscardGreenPacketsOverflow_Object = MibTableColumn
srvDiscardGreenPacketsOverflow = _SrvDiscardGreenPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 7),
    _SrvDiscardGreenPacketsOverflow_Type()
)
srvDiscardGreenPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardGreenPacketsOverflow.setStatus("current")
_SrvDiscardYellowRedPackets_Type = Counter32
_SrvDiscardYellowRedPackets_Object = MibTableColumn
srvDiscardYellowRedPackets = _SrvDiscardYellowRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 8),
    _SrvDiscardYellowRedPackets_Type()
)
srvDiscardYellowRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowRedPackets.setStatus("current")
_SrvDiscardYellowRedPacketsOverflow_Type = Counter32
_SrvDiscardYellowRedPacketsOverflow_Object = MibTableColumn
srvDiscardYellowRedPacketsOverflow = _SrvDiscardYellowRedPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 9),
    _SrvDiscardYellowRedPacketsOverflow_Type()
)
srvDiscardYellowRedPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowRedPacketsOverflow.setStatus("current")
_SrvForwardGreenBytes_Type = Counter32
_SrvForwardGreenBytes_Object = MibTableColumn
srvForwardGreenBytes = _SrvForwardGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 10),
    _SrvForwardGreenBytes_Type()
)
srvForwardGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardGreenBytes.setStatus("current")
_SrvForwardGreenBytesOverflow_Type = Counter32
_SrvForwardGreenBytesOverflow_Object = MibTableColumn
srvForwardGreenBytesOverflow = _SrvForwardGreenBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 11),
    _SrvForwardGreenBytesOverflow_Type()
)
srvForwardGreenBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardGreenBytesOverflow.setStatus("current")
_SrvForwardYellowBytes_Type = Counter32
_SrvForwardYellowBytes_Object = MibTableColumn
srvForwardYellowBytes = _SrvForwardYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 12),
    _SrvForwardYellowBytes_Type()
)
srvForwardYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardYellowBytes.setStatus("current")
_SrvForwardYellowBytesOverflow_Type = Counter32
_SrvForwardYellowBytesOverflow_Object = MibTableColumn
srvForwardYellowBytesOverflow = _SrvForwardYellowBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 13),
    _SrvForwardYellowBytesOverflow_Type()
)
srvForwardYellowBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvForwardYellowBytesOverflow.setStatus("current")
_SrvDiscardGreenBytes_Type = Counter32
_SrvDiscardGreenBytes_Object = MibTableColumn
srvDiscardGreenBytes = _SrvDiscardGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 14),
    _SrvDiscardGreenBytes_Type()
)
srvDiscardGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardGreenBytes.setStatus("current")
_SrvDiscardGreenBytesOverflow_Type = Counter32
_SrvDiscardGreenBytesOverflow_Object = MibTableColumn
srvDiscardGreenBytesOverflow = _SrvDiscardGreenBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 15),
    _SrvDiscardGreenBytesOverflow_Type()
)
srvDiscardGreenBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardGreenBytesOverflow.setStatus("current")
_SrvDiscardYellowRedBytes_Type = Counter32
_SrvDiscardYellowRedBytes_Object = MibTableColumn
srvDiscardYellowRedBytes = _SrvDiscardYellowRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 16),
    _SrvDiscardYellowRedBytes_Type()
)
srvDiscardYellowRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowRedBytes.setStatus("current")
_SrvDiscardYellowRedBytesOverflow_Type = Counter32
_SrvDiscardYellowRedBytesOverflow_Object = MibTableColumn
srvDiscardYellowRedBytesOverflow = _SrvDiscardYellowRedBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 17),
    _SrvDiscardYellowRedBytesOverflow_Type()
)
srvDiscardYellowRedBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowRedBytesOverflow.setStatus("current")


class _SrvResetStatsCmd_Type(Integer32):
    """Custom type srvResetStatsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SrvResetStatsCmd_Type.__name__ = "Integer32"
_SrvResetStatsCmd_Object = MibTableColumn
srvResetStatsCmd = _SrvResetStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 18),
    _SrvResetStatsCmd_Type()
)
srvResetStatsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvResetStatsCmd.setStatus("current")
_SrvDiscardYellowPackets_Type = Counter32
_SrvDiscardYellowPackets_Object = MibTableColumn
srvDiscardYellowPackets = _SrvDiscardYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 19),
    _SrvDiscardYellowPackets_Type()
)
srvDiscardYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowPackets.setStatus("current")
_SrvDiscardYellowPacketsOverflow_Type = Counter32
_SrvDiscardYellowPacketsOverflow_Object = MibTableColumn
srvDiscardYellowPacketsOverflow = _SrvDiscardYellowPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 20),
    _SrvDiscardYellowPacketsOverflow_Type()
)
srvDiscardYellowPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowPacketsOverflow.setStatus("current")
_SrvDiscardYellowBytes_Type = Counter32
_SrvDiscardYellowBytes_Object = MibTableColumn
srvDiscardYellowBytes = _SrvDiscardYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 21),
    _SrvDiscardYellowBytes_Type()
)
srvDiscardYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowBytes.setStatus("current")
_SrvDiscardYellowBytesOverflow_Type = Counter32
_SrvDiscardYellowBytesOverflow_Object = MibTableColumn
srvDiscardYellowBytesOverflow = _SrvDiscardYellowBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 22),
    _SrvDiscardYellowBytesOverflow_Type()
)
srvDiscardYellowBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardYellowBytesOverflow.setStatus("current")
_SrvDiscardRedPackets_Type = Counter32
_SrvDiscardRedPackets_Object = MibTableColumn
srvDiscardRedPackets = _SrvDiscardRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 23),
    _SrvDiscardRedPackets_Type()
)
srvDiscardRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardRedPackets.setStatus("current")
_SrvDiscardRedPacketsOverflow_Type = Counter32
_SrvDiscardRedPacketsOverflow_Object = MibTableColumn
srvDiscardRedPacketsOverflow = _SrvDiscardRedPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 24),
    _SrvDiscardRedPacketsOverflow_Type()
)
srvDiscardRedPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardRedPacketsOverflow.setStatus("current")
_SrvDiscardRedBytes_Type = Counter32
_SrvDiscardRedBytes_Object = MibTableColumn
srvDiscardRedBytes = _SrvDiscardRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 25),
    _SrvDiscardRedBytes_Type()
)
srvDiscardRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardRedBytes.setStatus("current")
_SrvDiscardRedBytesOverflow_Type = Counter32
_SrvDiscardRedBytesOverflow_Object = MibTableColumn
srvDiscardRedBytesOverflow = _SrvDiscardRedBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 8, 1, 26),
    _SrvDiscardRedBytesOverflow_Type()
)
srvDiscardRedBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiscardRedBytesOverflow.setStatus("current")
_MappingProfileObjects_ObjectIdentity = ObjectIdentity
mappingProfileObjects = _MappingProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9)
)
_FlowMappingProfileTable_Object = MibTable
flowMappingProfileTable = _FlowMappingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1)
)
if mibBuilder.loadTexts:
    flowMappingProfileTable.setStatus("current")
_FlowMappingProfileEntry_Object = MibTableRow
flowMappingProfileEntry = _FlowMappingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1)
)
flowMappingProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "flowMappingProfileIndex"),
    (0, "RAD-Services-MIB", "flowMappingProfilePriority"),
)
if mibBuilder.loadTexts:
    flowMappingProfileEntry.setStatus("current")
_FlowMappingProfileIndex_Type = Unsigned32
_FlowMappingProfileIndex_Object = MibTableColumn
flowMappingProfileIndex = _FlowMappingProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 1),
    _FlowMappingProfileIndex_Type()
)
flowMappingProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowMappingProfileIndex.setStatus("current")
_FlowMappingProfilePriority_Type = Integer32
_FlowMappingProfilePriority_Object = MibTableColumn
flowMappingProfilePriority = _FlowMappingProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 2),
    _FlowMappingProfilePriority_Type()
)
flowMappingProfilePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowMappingProfilePriority.setStatus("current")
_FlowMappingProfileRowStatus_Type = RowStatus
_FlowMappingProfileRowStatus_Object = MibTableColumn
flowMappingProfileRowStatus = _FlowMappingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 3),
    _FlowMappingProfileRowStatus_Type()
)
flowMappingProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMappingProfileRowStatus.setStatus("current")
_FlowMappingProfileNumOfMaps_Type = Unsigned32
_FlowMappingProfileNumOfMaps_Object = MibTableColumn
flowMappingProfileNumOfMaps = _FlowMappingProfileNumOfMaps_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 4),
    _FlowMappingProfileNumOfMaps_Type()
)
flowMappingProfileNumOfMaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMappingProfileNumOfMaps.setStatus("current")
_FlowMappingProfileMapIndex_Type = Unsigned32
_FlowMappingProfileMapIndex_Object = MibTableColumn
flowMappingProfileMapIndex = _FlowMappingProfileMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 5),
    _FlowMappingProfileMapIndex_Type()
)
flowMappingProfileMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMappingProfileMapIndex.setStatus("deprecated")
_FlowMappingProfileName_Type = SnmpAdminString
_FlowMappingProfileName_Object = MibTableColumn
flowMappingProfileName = _FlowMappingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 6),
    _FlowMappingProfileName_Type()
)
flowMappingProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMappingProfileName.setStatus("current")


class _FlowMappingProfileCondition_Type(Integer32):
    """Custom type flowMappingProfileCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("or", 2),
          ("and", 3))
    )


_FlowMappingProfileCondition_Type.__name__ = "Integer32"
_FlowMappingProfileCondition_Object = MibTableColumn
flowMappingProfileCondition = _FlowMappingProfileCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 1, 1, 7),
    _FlowMappingProfileCondition_Type()
)
flowMappingProfileCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowMappingProfileCondition.setStatus("current")
_QosFlowMappingTable_Object = MibTable
qosFlowMappingTable = _QosFlowMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2)
)
if mibBuilder.loadTexts:
    qosFlowMappingTable.setStatus("current")
_QosFlowMappingEntry_Object = MibTableRow
qosFlowMappingEntry = _QosFlowMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1)
)
qosFlowMappingEntry.setIndexNames(
    (0, "RAD-Services-MIB", "qosFlowMappingIdx1"),
    (0, "RAD-Services-MIB", "qosFlowMappingIdx2"),
    (0, "RAD-Services-MIB", "qosFlowMappingIdx3"),
)
if mibBuilder.loadTexts:
    qosFlowMappingEntry.setStatus("current")
_QosFlowMappingIdx1_Type = Unsigned32
_QosFlowMappingIdx1_Object = MibTableColumn
qosFlowMappingIdx1 = _QosFlowMappingIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 1),
    _QosFlowMappingIdx1_Type()
)
qosFlowMappingIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosFlowMappingIdx1.setStatus("current")
_QosFlowMappingIdx2_Type = Unsigned32
_QosFlowMappingIdx2_Object = MibTableColumn
qosFlowMappingIdx2 = _QosFlowMappingIdx2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 2),
    _QosFlowMappingIdx2_Type()
)
qosFlowMappingIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosFlowMappingIdx2.setStatus("current")
_QosFlowMappingIdx3_Type = Unsigned32
_QosFlowMappingIdx3_Object = MibTableColumn
qosFlowMappingIdx3 = _QosFlowMappingIdx3_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 3),
    _QosFlowMappingIdx3_Type()
)
qosFlowMappingIdx3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosFlowMappingIdx3.setStatus("current")
_QosFlowMappingRowStatus_Type = RowStatus
_QosFlowMappingRowStatus_Object = MibTableColumn
qosFlowMappingRowStatus = _QosFlowMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 4),
    _QosFlowMappingRowStatus_Type()
)
qosFlowMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingRowStatus.setStatus("current")


class _QosFlowMappingCriteria_Type(Bits):
    """Custom type qosFlowMappingCriteria based on Bits"""
    namedValues = NamedValues(
        *(("ieee802dot1p", 0),
          ("tos", 1),
          ("dscp", 2),
          ("vlanId", 3),
          ("macSrcAddr", 4),
          ("macDestAddr", 5),
          ("ipSrcAddr", 6),
          ("ipDestAddr", 7),
          ("tcpSrcPort", 8),
          ("tcpDestPort", 9),
          ("udpSrcPort", 10),
          ("udpDestPort", 11),
          ("ipPrecedence", 12),
          ("innerIeee802dot1p", 13),
          ("innerVlanId", 14),
          ("untagged", 15),
          ("nonIP", 16),
          ("etherType", 17),
          ("myMac", 18),
          ("myIp", 19))
    )

_QosFlowMappingCriteria_Type.__name__ = "Bits"
_QosFlowMappingCriteria_Object = MibTableColumn
qosFlowMappingCriteria = _QosFlowMappingCriteria_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 5),
    _QosFlowMappingCriteria_Type()
)
qosFlowMappingCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingCriteria.setStatus("current")
_QosFlowMappingIeee802dot1p_Type = Unsigned32
_QosFlowMappingIeee802dot1p_Object = MibTableColumn
qosFlowMappingIeee802dot1p = _QosFlowMappingIeee802dot1p_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 6),
    _QosFlowMappingIeee802dot1p_Type()
)
qosFlowMappingIeee802dot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingIeee802dot1p.setStatus("current")
_QosFlowMappingTos_Type = Unsigned32
_QosFlowMappingTos_Object = MibTableColumn
qosFlowMappingTos = _QosFlowMappingTos_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 7),
    _QosFlowMappingTos_Type()
)
qosFlowMappingTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingTos.setStatus("current")
_QosFlowMappingFromDscp_Type = Unsigned32
_QosFlowMappingFromDscp_Object = MibTableColumn
qosFlowMappingFromDscp = _QosFlowMappingFromDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 8),
    _QosFlowMappingFromDscp_Type()
)
qosFlowMappingFromDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromDscp.setStatus("current")
_QosFlowMappingToDscp_Type = Unsigned32
_QosFlowMappingToDscp_Object = MibTableColumn
qosFlowMappingToDscp = _QosFlowMappingToDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 9),
    _QosFlowMappingToDscp_Type()
)
qosFlowMappingToDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToDscp.setStatus("current")
_QosFlowMappingFromVlanId_Type = Unsigned32
_QosFlowMappingFromVlanId_Object = MibTableColumn
qosFlowMappingFromVlanId = _QosFlowMappingFromVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 10),
    _QosFlowMappingFromVlanId_Type()
)
qosFlowMappingFromVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromVlanId.setStatus("current")
_QosFlowMappingToVlanId_Type = Unsigned32
_QosFlowMappingToVlanId_Object = MibTableColumn
qosFlowMappingToVlanId = _QosFlowMappingToVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 11),
    _QosFlowMappingToVlanId_Type()
)
qosFlowMappingToVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToVlanId.setStatus("current")
_QosFlowMappingFromSrcMacAddr_Type = MacAddress
_QosFlowMappingFromSrcMacAddr_Object = MibTableColumn
qosFlowMappingFromSrcMacAddr = _QosFlowMappingFromSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 12),
    _QosFlowMappingFromSrcMacAddr_Type()
)
qosFlowMappingFromSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromSrcMacAddr.setStatus("current")
_QosFlowMappingToSrcMacAddr_Type = MacAddress
_QosFlowMappingToSrcMacAddr_Object = MibTableColumn
qosFlowMappingToSrcMacAddr = _QosFlowMappingToSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 13),
    _QosFlowMappingToSrcMacAddr_Type()
)
qosFlowMappingToSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToSrcMacAddr.setStatus("current")
_QosFlowMappingFromDestMacAddr_Type = MacAddress
_QosFlowMappingFromDestMacAddr_Object = MibTableColumn
qosFlowMappingFromDestMacAddr = _QosFlowMappingFromDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 14),
    _QosFlowMappingFromDestMacAddr_Type()
)
qosFlowMappingFromDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromDestMacAddr.setStatus("current")
_QosFlowMappingToDestMacAddr_Type = MacAddress
_QosFlowMappingToDestMacAddr_Object = MibTableColumn
qosFlowMappingToDestMacAddr = _QosFlowMappingToDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 15),
    _QosFlowMappingToDestMacAddr_Type()
)
qosFlowMappingToDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToDestMacAddr.setStatus("current")
_QosFlowMappingFromSrcIpAddr_Type = IpAddress
_QosFlowMappingFromSrcIpAddr_Object = MibTableColumn
qosFlowMappingFromSrcIpAddr = _QosFlowMappingFromSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 16),
    _QosFlowMappingFromSrcIpAddr_Type()
)
qosFlowMappingFromSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromSrcIpAddr.setStatus("deprecated")
_QosFlowMappingToSrcIpAddr_Type = IpAddress
_QosFlowMappingToSrcIpAddr_Object = MibTableColumn
qosFlowMappingToSrcIpAddr = _QosFlowMappingToSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 17),
    _QosFlowMappingToSrcIpAddr_Type()
)
qosFlowMappingToSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToSrcIpAddr.setStatus("deprecated")
_QosFlowMappingFromDestIpAddr_Type = IpAddress
_QosFlowMappingFromDestIpAddr_Object = MibTableColumn
qosFlowMappingFromDestIpAddr = _QosFlowMappingFromDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 18),
    _QosFlowMappingFromDestIpAddr_Type()
)
qosFlowMappingFromDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromDestIpAddr.setStatus("deprecated")
_QosFlowMappingToDestIpAddr_Type = IpAddress
_QosFlowMappingToDestIpAddr_Object = MibTableColumn
qosFlowMappingToDestIpAddr = _QosFlowMappingToDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 19),
    _QosFlowMappingToDestIpAddr_Type()
)
qosFlowMappingToDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToDestIpAddr.setStatus("deprecated")
_QosFlowMappingFromTcpSrcPort_Type = Unsigned32
_QosFlowMappingFromTcpSrcPort_Object = MibTableColumn
qosFlowMappingFromTcpSrcPort = _QosFlowMappingFromTcpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 20),
    _QosFlowMappingFromTcpSrcPort_Type()
)
qosFlowMappingFromTcpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromTcpSrcPort.setStatus("current")
_QosFlowMappingToTcpSrcPort_Type = Unsigned32
_QosFlowMappingToTcpSrcPort_Object = MibTableColumn
qosFlowMappingToTcpSrcPort = _QosFlowMappingToTcpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 21),
    _QosFlowMappingToTcpSrcPort_Type()
)
qosFlowMappingToTcpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToTcpSrcPort.setStatus("current")
_QosFlowMappingFromTcpDestPort_Type = Unsigned32
_QosFlowMappingFromTcpDestPort_Object = MibTableColumn
qosFlowMappingFromTcpDestPort = _QosFlowMappingFromTcpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 22),
    _QosFlowMappingFromTcpDestPort_Type()
)
qosFlowMappingFromTcpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromTcpDestPort.setStatus("current")
_QosFlowMappingToTcpDestPort_Type = Unsigned32
_QosFlowMappingToTcpDestPort_Object = MibTableColumn
qosFlowMappingToTcpDestPort = _QosFlowMappingToTcpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 23),
    _QosFlowMappingToTcpDestPort_Type()
)
qosFlowMappingToTcpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToTcpDestPort.setStatus("current")
_QosFlowMappingFromUdpSrcPort_Type = Unsigned32
_QosFlowMappingFromUdpSrcPort_Object = MibTableColumn
qosFlowMappingFromUdpSrcPort = _QosFlowMappingFromUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 24),
    _QosFlowMappingFromUdpSrcPort_Type()
)
qosFlowMappingFromUdpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromUdpSrcPort.setStatus("current")
_QosFlowMappingToUdpSrcPort_Type = Unsigned32
_QosFlowMappingToUdpSrcPort_Object = MibTableColumn
qosFlowMappingToUdpSrcPort = _QosFlowMappingToUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 25),
    _QosFlowMappingToUdpSrcPort_Type()
)
qosFlowMappingToUdpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToUdpSrcPort.setStatus("current")
_QosFlowMappingFromUdpDestPort_Type = Unsigned32
_QosFlowMappingFromUdpDestPort_Object = MibTableColumn
qosFlowMappingFromUdpDestPort = _QosFlowMappingFromUdpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 26),
    _QosFlowMappingFromUdpDestPort_Type()
)
qosFlowMappingFromUdpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromUdpDestPort.setStatus("current")
_QosFlowMappingToUdpDestPort_Type = Unsigned32
_QosFlowMappingToUdpDestPort_Object = MibTableColumn
qosFlowMappingToUdpDestPort = _QosFlowMappingToUdpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 27),
    _QosFlowMappingToUdpDestPort_Type()
)
qosFlowMappingToUdpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToUdpDestPort.setStatus("current")
_QosFlowMappingFromIpPrecedence_Type = Unsigned32
_QosFlowMappingFromIpPrecedence_Object = MibTableColumn
qosFlowMappingFromIpPrecedence = _QosFlowMappingFromIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 28),
    _QosFlowMappingFromIpPrecedence_Type()
)
qosFlowMappingFromIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromIpPrecedence.setStatus("current")
_QosFlowMappingToIpPrecedence_Type = Unsigned32
_QosFlowMappingToIpPrecedence_Object = MibTableColumn
qosFlowMappingToIpPrecedence = _QosFlowMappingToIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 29),
    _QosFlowMappingToIpPrecedence_Type()
)
qosFlowMappingToIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToIpPrecedence.setStatus("current")
_QosFlowMappingInnerIeee802dot1p_Type = Unsigned32
_QosFlowMappingInnerIeee802dot1p_Object = MibTableColumn
qosFlowMappingInnerIeee802dot1p = _QosFlowMappingInnerIeee802dot1p_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 30),
    _QosFlowMappingInnerIeee802dot1p_Type()
)
qosFlowMappingInnerIeee802dot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingInnerIeee802dot1p.setStatus("current")
_QosFlowMappingFromInnerVlanId_Type = Unsigned32
_QosFlowMappingFromInnerVlanId_Object = MibTableColumn
qosFlowMappingFromInnerVlanId = _QosFlowMappingFromInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 31),
    _QosFlowMappingFromInnerVlanId_Type()
)
qosFlowMappingFromInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingFromInnerVlanId.setStatus("current")
_QosFlowMappingToInnerVlanId_Type = Unsigned32
_QosFlowMappingToInnerVlanId_Object = MibTableColumn
qosFlowMappingToInnerVlanId = _QosFlowMappingToInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 32),
    _QosFlowMappingToInnerVlanId_Type()
)
qosFlowMappingToInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingToInnerVlanId.setStatus("current")
_QosFlowMappingEtherType_Type = Unsigned32
_QosFlowMappingEtherType_Object = MibTableColumn
qosFlowMappingEtherType = _QosFlowMappingEtherType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 9, 2, 1, 33),
    _QosFlowMappingEtherType_Type()
)
qosFlowMappingEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosFlowMappingEtherType.setStatus("current")
_CosProfileTable_Object = MibTable
cosProfileTable = _CosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10)
)
if mibBuilder.loadTexts:
    cosProfileTable.setStatus("current")
_CosProfileEntry_Object = MibTableRow
cosProfileEntry = _CosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10, 1)
)
cosProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "cosProfileIndex"),
)
if mibBuilder.loadTexts:
    cosProfileEntry.setStatus("current")
_CosProfileIndex_Type = Unsigned32
_CosProfileIndex_Object = MibTableColumn
cosProfileIndex = _CosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10, 1, 1),
    _CosProfileIndex_Type()
)
cosProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cosProfileIndex.setStatus("current")
_CosProfileRowStatus_Type = RowStatus
_CosProfileRowStatus_Object = MibTableColumn
cosProfileRowStatus = _CosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10, 1, 2),
    _CosProfileRowStatus_Type()
)
cosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosProfileRowStatus.setStatus("current")
_CosProfileCosMethod_Type = ProfileMethod
_CosProfileCosMethod_Object = MibTableColumn
cosProfileCosMethod = _CosProfileCosMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10, 1, 3),
    _CosProfileCosMethod_Type()
)
cosProfileCosMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosProfileCosMethod.setStatus("current")
_CosProfileName_Type = SnmpAdminString
_CosProfileName_Object = MibTableColumn
cosProfileName = _CosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10, 1, 4),
    _CosProfileName_Type()
)
cosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosProfileName.setStatus("current")


class _CosProfileCosMapping_Type(OctetString):
    """Custom type cosProfileCosMapping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CosProfileCosMapping_Type.__name__ = "OctetString"
_CosProfileCosMapping_Object = MibTableColumn
cosProfileCosMapping = _CosProfileCosMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 10, 1, 5),
    _CosProfileCosMapping_Type()
)
cosProfileCosMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosProfileCosMapping.setStatus("current")
_QueueProfileObjects_ObjectIdentity = ObjectIdentity
queueProfileObjects = _QueueProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11)
)
_QProfileTable_Object = MibTable
qProfileTable = _QProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1)
)
if mibBuilder.loadTexts:
    qProfileTable.setStatus("current")
_QProfileEntry_Object = MibTableRow
qProfileEntry = _QProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1, 1)
)
qProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "qProfileIndex"),
)
if mibBuilder.loadTexts:
    qProfileEntry.setStatus("current")
_QProfileIndex_Type = Unsigned32
_QProfileIndex_Object = MibTableColumn
qProfileIndex = _QProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1, 1, 1),
    _QProfileIndex_Type()
)
qProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qProfileIndex.setStatus("current")
_QProfileRowStatus_Type = RowStatus
_QProfileRowStatus_Object = MibTableColumn
qProfileRowStatus = _QProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1, 1, 2),
    _QProfileRowStatus_Type()
)
qProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qProfileRowStatus.setStatus("current")
_QProfileName_Type = SnmpAdminString
_QProfileName_Object = MibTableColumn
qProfileName = _QProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1, 1, 3),
    _QProfileName_Type()
)
qProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qProfileName.setStatus("current")
_QProfileNumberOfInternalQ_Type = Unsigned32
_QProfileNumberOfInternalQ_Object = MibTableColumn
qProfileNumberOfInternalQ = _QProfileNumberOfInternalQ_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1, 1, 4),
    _QProfileNumberOfInternalQ_Type()
)
qProfileNumberOfInternalQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qProfileNumberOfInternalQ.setStatus("current")
_QProfileInternalQProfile_Type = OctetString
_QProfileInternalQProfile_Object = MibTableColumn
qProfileInternalQProfile = _QProfileInternalQProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 1, 1, 5),
    _QProfileInternalQProfile_Type()
)
qProfileInternalQProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qProfileInternalQProfile.setStatus("current")
_QInternalProfileTable_Object = MibTable
qInternalProfileTable = _QInternalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2)
)
if mibBuilder.loadTexts:
    qInternalProfileTable.setStatus("current")
_QInternalProfileEntry_Object = MibTableRow
qInternalProfileEntry = _QInternalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1)
)
qInternalProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "qInternalProfileIndex"),
)
if mibBuilder.loadTexts:
    qInternalProfileEntry.setStatus("current")
_QInternalProfileIndex_Type = Unsigned32
_QInternalProfileIndex_Object = MibTableColumn
qInternalProfileIndex = _QInternalProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 1),
    _QInternalProfileIndex_Type()
)
qInternalProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qInternalProfileIndex.setStatus("current")
_QInternalProfileRowStatus_Type = RowStatus
_QInternalProfileRowStatus_Object = MibTableColumn
qInternalProfileRowStatus = _QInternalProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 2),
    _QInternalProfileRowStatus_Type()
)
qInternalProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileRowStatus.setStatus("current")


class _QInternalProfileScheduling_Type(Integer32):
    """Custom type qInternalProfileScheduling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wfq", 1),
          ("strict", 2),
          ("bestEffort", 3))
    )


_QInternalProfileScheduling_Type.__name__ = "Integer32"
_QInternalProfileScheduling_Object = MibTableColumn
qInternalProfileScheduling = _QInternalProfileScheduling_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 3),
    _QInternalProfileScheduling_Type()
)
qInternalProfileScheduling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileScheduling.setStatus("current")
_QInternalProfileWFQWeight_Type = Unsigned32
_QInternalProfileWFQWeight_Object = MibTableColumn
qInternalProfileWFQWeight = _QInternalProfileWFQWeight_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 4),
    _QInternalProfileWFQWeight_Type()
)
qInternalProfileWFQWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileWFQWeight.setStatus("current")
_QInternalProfileQueueLength_Type = Unsigned32
_QInternalProfileQueueLength_Object = MibTableColumn
qInternalProfileQueueLength = _QInternalProfileQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 5),
    _QInternalProfileQueueLength_Type()
)
qInternalProfileQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileQueueLength.setStatus("current")
_QInternalProfileWredStartDropThresh_Type = Unsigned32
_QInternalProfileWredStartDropThresh_Object = MibTableColumn
qInternalProfileWredStartDropThresh = _QInternalProfileWredStartDropThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 6),
    _QInternalProfileWredStartDropThresh_Type()
)
qInternalProfileWredStartDropThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileWredStartDropThresh.setStatus("deprecated")
_QInternalProfileWredDropAllThresh_Type = Unsigned32
_QInternalProfileWredDropAllThresh_Object = MibTableColumn
qInternalProfileWredDropAllThresh = _QInternalProfileWredDropAllThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 7),
    _QInternalProfileWredDropAllThresh_Type()
)
qInternalProfileWredDropAllThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileWredDropAllThresh.setStatus("deprecated")
_QInternalProfileWredDropProbability_Type = Unsigned32
_QInternalProfileWredDropProbability_Object = MibTableColumn
qInternalProfileWredDropProbability = _QInternalProfileWredDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 8),
    _QInternalProfileWredDropProbability_Type()
)
qInternalProfileWredDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileWredDropProbability.setStatus("deprecated")
_QInternalProfileRateLimit_Type = Unsigned32
_QInternalProfileRateLimit_Object = MibTableColumn
qInternalProfileRateLimit = _QInternalProfileRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 9),
    _QInternalProfileRateLimit_Type()
)
qInternalProfileRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileRateLimit.setStatus("current")
_QInternalProfileShaperProfile_Type = Unsigned32
_QInternalProfileShaperProfile_Object = MibTableColumn
qInternalProfileShaperProfile = _QInternalProfileShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 10),
    _QInternalProfileShaperProfile_Type()
)
qInternalProfileShaperProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileShaperProfile.setStatus("current")
_QInternalProfileWredProfile_Type = Unsigned32
_QInternalProfileWredProfile_Object = MibTableColumn
qInternalProfileWredProfile = _QInternalProfileWredProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 11),
    _QInternalProfileWredProfile_Type()
)
qInternalProfileWredProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileWredProfile.setStatus("current")


class _QInternalProfileFrameBuffers_Type(Unsigned32):
    """Custom type qInternalProfileFrameBuffers based on Unsigned32"""
    defaultValue = 511

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_QInternalProfileFrameBuffers_Type.__name__ = "Unsigned32"
_QInternalProfileFrameBuffers_Object = MibTableColumn
qInternalProfileFrameBuffers = _QInternalProfileFrameBuffers_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 2, 1, 13),
    _QInternalProfileFrameBuffers_Type()
)
qInternalProfileFrameBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qInternalProfileFrameBuffers.setStatus("current")
_QueueGroupTable_Object = MibTable
queueGroupTable = _QueueGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3)
)
if mibBuilder.loadTexts:
    queueGroupTable.setStatus("current")
_QueueGroupEntry_Object = MibTableRow
queueGroupEntry = _QueueGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1)
)
queueGroupEntry.setIndexNames(
    (0, "RAD-Services-MIB", "queueGroupName"),
    (0, "RAD-Services-MIB", "queueGroupQBlockLevel"),
    (0, "RAD-Services-MIB", "queueGroupQBlockIdx"),
)
if mibBuilder.loadTexts:
    queueGroupEntry.setStatus("current")


class _QueueGroupName_Type(SnmpAdminString):
    """Custom type queueGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QueueGroupName_Type.__name__ = "SnmpAdminString"
_QueueGroupName_Object = MibTableColumn
queueGroupName = _QueueGroupName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 1),
    _QueueGroupName_Type()
)
queueGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueGroupName.setStatus("current")
_QueueGroupQBlockLevel_Type = Unsigned32
_QueueGroupQBlockLevel_Object = MibTableColumn
queueGroupQBlockLevel = _QueueGroupQBlockLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 2),
    _QueueGroupQBlockLevel_Type()
)
queueGroupQBlockLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueGroupQBlockLevel.setStatus("current")
_QueueGroupQBlockIdx_Type = Unsigned32
_QueueGroupQBlockIdx_Object = MibTableColumn
queueGroupQBlockIdx = _QueueGroupQBlockIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 3),
    _QueueGroupQBlockIdx_Type()
)
queueGroupQBlockIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueGroupQBlockIdx.setStatus("current")
_QueueGroupRowStatus_Type = RowStatus
_QueueGroupRowStatus_Object = MibTableColumn
queueGroupRowStatus = _QueueGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 4),
    _QueueGroupRowStatus_Type()
)
queueGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queueGroupRowStatus.setStatus("current")
_QueueGroupQBlockProfile_Type = Unsigned32
_QueueGroupQBlockProfile_Object = MibTableColumn
queueGroupQBlockProfile = _QueueGroupQBlockProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 5),
    _QueueGroupQBlockProfile_Type()
)
queueGroupQBlockProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queueGroupQBlockProfile.setStatus("current")
_QueueGroupQBlockShaperProfile_Type = Unsigned32
_QueueGroupQBlockShaperProfile_Object = MibTableColumn
queueGroupQBlockShaperProfile = _QueueGroupQBlockShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 6),
    _QueueGroupQBlockShaperProfile_Type()
)
queueGroupQBlockShaperProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queueGroupQBlockShaperProfile.setStatus("current")


class _QueueGroupPointToQBlock_Type(SnmpAdminString):
    """Custom type queueGroupPointToQBlock based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QueueGroupPointToQBlock_Type.__name__ = "SnmpAdminString"
_QueueGroupPointToQBlock_Object = MibTableColumn
queueGroupPointToQBlock = _QueueGroupPointToQBlock_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 7),
    _QueueGroupPointToQBlock_Type()
)
queueGroupPointToQBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queueGroupPointToQBlock.setStatus("current")
_QueueGroupPointToInternalQueue_Type = Unsigned32
_QueueGroupPointToInternalQueue_Object = MibTableColumn
queueGroupPointToInternalQueue = _QueueGroupPointToInternalQueue_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 8),
    _QueueGroupPointToInternalQueue_Type()
)
queueGroupPointToInternalQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queueGroupPointToInternalQueue.setStatus("current")


class _QueueGroupQBlockName_Type(SnmpAdminString):
    """Custom type queueGroupQBlockName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QueueGroupQBlockName_Type.__name__ = "SnmpAdminString"
_QueueGroupQBlockName_Object = MibTableColumn
queueGroupQBlockName = _QueueGroupQBlockName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 11, 3, 1, 9),
    _QueueGroupQBlockName_Type()
)
queueGroupQBlockName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queueGroupQBlockName.setStatus("current")
_MarkingProfileTable_Object = MibTable
markingProfileTable = _MarkingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12)
)
if mibBuilder.loadTexts:
    markingProfileTable.setStatus("current")
_MarkingProfileEntry_Object = MibTableRow
markingProfileEntry = _MarkingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1)
)
markingProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "markingProfileIndex"),
)
if mibBuilder.loadTexts:
    markingProfileEntry.setStatus("current")
_MarkingProfileIndex_Type = Unsigned32
_MarkingProfileIndex_Object = MibTableColumn
markingProfileIndex = _MarkingProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 1),
    _MarkingProfileIndex_Type()
)
markingProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    markingProfileIndex.setStatus("current")
_MarkingProfileRowStatus_Type = RowStatus
_MarkingProfileRowStatus_Object = MibTableColumn
markingProfileRowStatus = _MarkingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 2),
    _MarkingProfileRowStatus_Type()
)
markingProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileRowStatus.setStatus("current")
_MarkingProfileName_Type = SnmpAdminString
_MarkingProfileName_Object = MibTableColumn
markingProfileName = _MarkingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 3),
    _MarkingProfileName_Type()
)
markingProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileName.setStatus("current")


class _MarkingSpVlanPBit_Type(OctetString):
    """Custom type markingSpVlanPBit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(192, 192),
    )
    fixed_length = 192


_MarkingSpVlanPBit_Type.__name__ = "OctetString"
_MarkingSpVlanPBit_Object = MibTableColumn
markingSpVlanPBit = _MarkingSpVlanPBit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 4),
    _MarkingSpVlanPBit_Type()
)
markingSpVlanPBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingSpVlanPBit.setStatus("current")
_MarkingProfileMethod_Type = ProfileMethod
_MarkingProfileMethod_Object = MibTableColumn
markingProfileMethod = _MarkingProfileMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 5),
    _MarkingProfileMethod_Type()
)
markingProfileMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileMethod.setStatus("current")


class _MarkingProfileColorAware_Type(Bits):
    """Custom type markingProfileColorAware based on Bits"""
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1),
          ("red", 2))
    )

_MarkingProfileColorAware_Type.__name__ = "Bits"
_MarkingProfileColorAware_Object = MibTableColumn
markingProfileColorAware = _MarkingProfileColorAware_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 6),
    _MarkingProfileColorAware_Type()
)
markingProfileColorAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileColorAware.setStatus("current")


class _MarkingProfileDeiAware_Type(Integer32):
    """Custom type markingProfileDeiAware based on Integer32"""
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
        *(("aware", 1),
          ("notAware", 2),
          ("alwaysGreen", 3),
          ("alwaysYellow", 4),
          ("byPolicer", 5))
    )


_MarkingProfileDeiAware_Type.__name__ = "Integer32"
_MarkingProfileDeiAware_Object = MibTableColumn
markingProfileDeiAware = _MarkingProfileDeiAware_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 7),
    _MarkingProfileDeiAware_Type()
)
markingProfileDeiAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileDeiAware.setStatus("current")


class _MarkingProfileDeiColor_Type(OctetString):
    """Custom type markingProfileDeiColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(192, 192),
    )
    fixed_length = 192


_MarkingProfileDeiColor_Type.__name__ = "OctetString"
_MarkingProfileDeiColor_Object = MibTableColumn
markingProfileDeiColor = _MarkingProfileDeiColor_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 8),
    _MarkingProfileDeiColor_Type()
)
markingProfileDeiColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileDeiColor.setStatus("current")


class _MarkingProfileDscpColor_Type(OctetString):
    """Custom type markingProfileDscpColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_MarkingProfileDscpColor_Type.__name__ = "OctetString"
_MarkingProfileDscpColor_Object = MibTableColumn
markingProfileDscpColor = _MarkingProfileDscpColor_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 9),
    _MarkingProfileDscpColor_Type()
)
markingProfileDscpColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileDscpColor.setStatus("current")


class _MarkingProfileMarkedField_Type(ProfileMethod):
    """Custom type markingProfileMarkedField based on ProfileMethod"""
    defaultValue = 2


_MarkingProfileMarkedField_Type.__name__ = "ProfileMethod"
_MarkingProfileMarkedField_Object = MibTableColumn
markingProfileMarkedField = _MarkingProfileMarkedField_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 12, 1, 10),
    _MarkingProfileMarkedField_Type()
)
markingProfileMarkedField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markingProfileMarkedField.setStatus("current")
_WredProfileTable_Object = MibTable
wredProfileTable = _WredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13)
)
if mibBuilder.loadTexts:
    wredProfileTable.setStatus("current")
_WredProfileEntry_Object = MibTableRow
wredProfileEntry = _WredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1)
)
wredProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "wredProfileIndex"),
    (0, "RAD-Services-MIB", "wredProfileColor"),
)
if mibBuilder.loadTexts:
    wredProfileEntry.setStatus("current")
_WredProfileIndex_Type = Unsigned32
_WredProfileIndex_Object = MibTableColumn
wredProfileIndex = _WredProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 1),
    _WredProfileIndex_Type()
)
wredProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wredProfileIndex.setStatus("current")


class _WredProfileColor_Type(Integer32):
    """Custom type wredProfileColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("yellow", 3),
          ("red", 4))
    )


_WredProfileColor_Type.__name__ = "Integer32"
_WredProfileColor_Object = MibTableColumn
wredProfileColor = _WredProfileColor_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 2),
    _WredProfileColor_Type()
)
wredProfileColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wredProfileColor.setStatus("current")
_WredProfileRowStatus_Type = RowStatus
_WredProfileRowStatus_Object = MibTableColumn
wredProfileRowStatus = _WredProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 3),
    _WredProfileRowStatus_Type()
)
wredProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredProfileRowStatus.setStatus("current")
_WredProfileName_Type = SnmpAdminString
_WredProfileName_Object = MibTableColumn
wredProfileName = _WredProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 4),
    _WredProfileName_Type()
)
wredProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredProfileName.setStatus("current")
_WredProfileMinThreshold_Type = Unsigned32
_WredProfileMinThreshold_Object = MibTableColumn
wredProfileMinThreshold = _WredProfileMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 5),
    _WredProfileMinThreshold_Type()
)
wredProfileMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredProfileMinThreshold.setStatus("current")
_WredProfileMaxThreshold_Type = Unsigned32
_WredProfileMaxThreshold_Object = MibTableColumn
wredProfileMaxThreshold = _WredProfileMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 6),
    _WredProfileMaxThreshold_Type()
)
wredProfileMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredProfileMaxThreshold.setStatus("current")
_WredProfileMaxProbability_Type = Unsigned32
_WredProfileMaxProbability_Object = MibTableColumn
wredProfileMaxProbability = _WredProfileMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 13, 1, 7),
    _WredProfileMaxProbability_Type()
)
wredProfileMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredProfileMaxProbability.setStatus("current")
_SviTable_Object = MibTable
sviTable = _SviTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 14)
)
if mibBuilder.loadTexts:
    sviTable.setStatus("current")
_SviEntry_Object = MibTableRow
sviEntry = _SviEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 14, 1)
)
sviEntry.setIndexNames(
    (0, "RAD-Services-MIB", "sviIndex"),
)
if mibBuilder.loadTexts:
    sviEntry.setStatus("current")
_SviIndex_Type = Integer32
_SviIndex_Object = MibTableColumn
sviIndex = _SviIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 14, 1, 1),
    _SviIndex_Type()
)
sviIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sviIndex.setStatus("current")


class _SviBoundToType_Type(Integer32):
    """Custom type sviBoundToType based on Integer32"""
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
        *(("none", 1),
          ("bridge", 2),
          ("pw", 3),
          ("router", 4),
          ("twamp", 5))
    )


_SviBoundToType_Type.__name__ = "Integer32"
_SviBoundToType_Object = MibTableColumn
sviBoundToType = _SviBoundToType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 14, 1, 5),
    _SviBoundToType_Type()
)
sviBoundToType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sviBoundToType.setStatus("current")
_CosInternalProfileTable_Object = MibTable
cosInternalProfileTable = _CosInternalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15)
)
if mibBuilder.loadTexts:
    cosInternalProfileTable.setStatus("current")
_CosInternalProfileEntry_Object = MibTableRow
cosInternalProfileEntry = _CosInternalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1)
)
cosInternalProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "cosInternalProfileIndex"),
)
if mibBuilder.loadTexts:
    cosInternalProfileEntry.setStatus("current")
_CosInternalProfileIndex_Type = Unsigned32
_CosInternalProfileIndex_Object = MibTableColumn
cosInternalProfileIndex = _CosInternalProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 1),
    _CosInternalProfileIndex_Type()
)
cosInternalProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cosInternalProfileIndex.setStatus("current")
_CosInternalProfileRowStatus_Type = RowStatus
_CosInternalProfileRowStatus_Object = MibTableColumn
cosInternalProfileRowStatus = _CosInternalProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 2),
    _CosInternalProfileRowStatus_Type()
)
cosInternalProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosInternalProfileRowStatus.setStatus("current")
_CosInternalProfileCosMethod_Type = ProfileMethod
_CosInternalProfileCosMethod_Object = MibTableColumn
cosInternalProfileCosMethod = _CosInternalProfileCosMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 3),
    _CosInternalProfileCosMethod_Type()
)
cosInternalProfileCosMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosInternalProfileCosMethod.setStatus("current")
_CosInternalProfileName_Type = SnmpAdminString
_CosInternalProfileName_Object = MibTableColumn
cosInternalProfileName = _CosInternalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 4),
    _CosInternalProfileName_Type()
)
cosInternalProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosInternalProfileName.setStatus("current")


class _CosInternalProfileCosMapping_Type(OctetString):
    """Custom type cosInternalProfileCosMapping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CosInternalProfileCosMapping_Type.__name__ = "OctetString"
_CosInternalProfileCosMapping_Object = MibTableColumn
cosInternalProfileCosMapping = _CosInternalProfileCosMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 5),
    _CosInternalProfileCosMapping_Type()
)
cosInternalProfileCosMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosInternalProfileCosMapping.setStatus("current")


class _CosInternalProfileUntaggedMapping_Type(Unsigned32):
    """Custom type cosInternalProfileUntaggedMapping based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CosInternalProfileUntaggedMapping_Type.__name__ = "Unsigned32"
_CosInternalProfileUntaggedMapping_Object = MibTableColumn
cosInternalProfileUntaggedMapping = _CosInternalProfileUntaggedMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 6),
    _CosInternalProfileUntaggedMapping_Type()
)
cosInternalProfileUntaggedMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosInternalProfileUntaggedMapping.setStatus("current")


class _CosInternalProfileNonIpMapping_Type(Unsigned32):
    """Custom type cosInternalProfileNonIpMapping based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CosInternalProfileNonIpMapping_Type.__name__ = "Unsigned32"
_CosInternalProfileNonIpMapping_Object = MibTableColumn
cosInternalProfileNonIpMapping = _CosInternalProfileNonIpMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 15, 1, 7),
    _CosInternalProfileNonIpMapping_Type()
)
cosInternalProfileNonIpMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cosInternalProfileNonIpMapping.setStatus("current")
_ColorMappingProfileTable_Object = MibTable
colorMappingProfileTable = _ColorMappingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16)
)
if mibBuilder.loadTexts:
    colorMappingProfileTable.setStatus("current")
_ColorMappingProfileEntry_Object = MibTableRow
colorMappingProfileEntry = _ColorMappingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16, 1)
)
colorMappingProfileEntry.setIndexNames(
    (0, "RAD-Services-MIB", "colorMappingProfileIndex"),
)
if mibBuilder.loadTexts:
    colorMappingProfileEntry.setStatus("current")
_ColorMappingProfileIndex_Type = Unsigned32
_ColorMappingProfileIndex_Object = MibTableColumn
colorMappingProfileIndex = _ColorMappingProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16, 1, 1),
    _ColorMappingProfileIndex_Type()
)
colorMappingProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    colorMappingProfileIndex.setStatus("current")
_ColorMappingProfileRowStatus_Type = RowStatus
_ColorMappingProfileRowStatus_Object = MibTableColumn
colorMappingProfileRowStatus = _ColorMappingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16, 1, 2),
    _ColorMappingProfileRowStatus_Type()
)
colorMappingProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    colorMappingProfileRowStatus.setStatus("current")
_ColorMappingProfileMethod_Type = ProfileMethod
_ColorMappingProfileMethod_Object = MibTableColumn
colorMappingProfileMethod = _ColorMappingProfileMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16, 1, 3),
    _ColorMappingProfileMethod_Type()
)
colorMappingProfileMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    colorMappingProfileMethod.setStatus("current")
_ColorMappingProfileName_Type = SnmpAdminString
_ColorMappingProfileName_Object = MibTableColumn
colorMappingProfileName = _ColorMappingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16, 1, 4),
    _ColorMappingProfileName_Type()
)
colorMappingProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    colorMappingProfileName.setStatus("current")


class _ColorMappingProfileMapping_Type(OctetString):
    """Custom type colorMappingProfileMapping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ColorMappingProfileMapping_Type.__name__ = "OctetString"
_ColorMappingProfileMapping_Object = MibTableColumn
colorMappingProfileMapping = _ColorMappingProfileMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 16, 1, 5),
    _ColorMappingProfileMapping_Type()
)
colorMappingProfileMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    colorMappingProfileMapping.setStatus("current")
_PortClassifierObjects_ObjectIdentity = ObjectIdentity
portClassifierObjects = _PortClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17)
)
_PortClassifierScalarObjects_ObjectIdentity = ObjectIdentity
portClassifierScalarObjects = _PortClassifierScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 1)
)
_PortClassifierRemainingActions_Type = Unsigned32
_PortClassifierRemainingActions_Object = MibScalar
portClassifierRemainingActions = _PortClassifierRemainingActions_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 1, 1),
    _PortClassifierRemainingActions_Type()
)
portClassifierRemainingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierRemainingActions.setStatus("current")
_PortClassifierTable_Object = MibTable
portClassifierTable = _PortClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 2)
)
if mibBuilder.loadTexts:
    portClassifierTable.setStatus("current")
_PortClassifierEntry_Object = MibTableRow
portClassifierEntry = _PortClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 2, 1)
)
portClassifierEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portClassifierEntry.setStatus("current")
_PortClassifierRowStatus_Type = RowStatus
_PortClassifierRowStatus_Object = MibTableColumn
portClassifierRowStatus = _PortClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 2, 1, 1),
    _PortClassifierRowStatus_Type()
)
portClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierRowStatus.setStatus("current")
_PortClassifierNumberOfActions_Type = Unsigned32
_PortClassifierNumberOfActions_Object = MibTableColumn
portClassifierNumberOfActions = _PortClassifierNumberOfActions_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 2, 1, 2),
    _PortClassifierNumberOfActions_Type()
)
portClassifierNumberOfActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierNumberOfActions.setStatus("current")
_PortClassifierHighSequenceNumber_Type = Unsigned32
_PortClassifierHighSequenceNumber_Object = MibTableColumn
portClassifierHighSequenceNumber = _PortClassifierHighSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 2, 1, 3),
    _PortClassifierHighSequenceNumber_Type()
)
portClassifierHighSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierHighSequenceNumber.setStatus("current")


class _PortClassifierResequenceCmd_Type(Unsigned32):
    """Custom type portClassifierResequenceCmd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PortClassifierResequenceCmd_Type.__name__ = "Unsigned32"
_PortClassifierResequenceCmd_Object = MibTableColumn
portClassifierResequenceCmd = _PortClassifierResequenceCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 2, 1, 4),
    _PortClassifierResequenceCmd_Type()
)
portClassifierResequenceCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierResequenceCmd.setStatus("current")
_PortClassifierActionTable_Object = MibTable
portClassifierActionTable = _PortClassifierActionTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3)
)
if mibBuilder.loadTexts:
    portClassifierActionTable.setStatus("current")
_PortClassifierActionEntry_Object = MibTableRow
portClassifierActionEntry = _PortClassifierActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1)
)
portClassifierActionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-Services-MIB", "portClassifierActionIndex"),
)
if mibBuilder.loadTexts:
    portClassifierActionEntry.setStatus("current")
_PortClassifierActionIndex_Type = Unsigned32
_PortClassifierActionIndex_Object = MibTableColumn
portClassifierActionIndex = _PortClassifierActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 1),
    _PortClassifierActionIndex_Type()
)
portClassifierActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portClassifierActionIndex.setStatus("current")
_PortClassifierActionRowStatus_Type = RowStatus
_PortClassifierActionRowStatus_Object = MibTableColumn
portClassifierActionRowStatus = _PortClassifierActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 2),
    _PortClassifierActionRowStatus_Type()
)
portClassifierActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionRowStatus.setStatus("current")


class _PortClassifierActionSequenceNumber_Type(Unsigned32):
    """Custom type portClassifierActionSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PortClassifierActionSequenceNumber_Type.__name__ = "Unsigned32"
_PortClassifierActionSequenceNumber_Object = MibTableColumn
portClassifierActionSequenceNumber = _PortClassifierActionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 3),
    _PortClassifierActionSequenceNumber_Type()
)
portClassifierActionSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionSequenceNumber.setStatus("current")


class _PortClassifierActionType_Type(Integer32):
    """Custom type portClassifierActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match", 1),
          ("drop", 2))
    )


_PortClassifierActionType_Type.__name__ = "Integer32"
_PortClassifierActionType_Object = MibTableColumn
portClassifierActionType = _PortClassifierActionType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 4),
    _PortClassifierActionType_Type()
)
portClassifierActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionType.setStatus("current")


class _PortClassifierActionFlowName_Type(SnmpAdminString):
    """Custom type portClassifierActionFlowName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_PortClassifierActionFlowName_Type.__name__ = "SnmpAdminString"
_PortClassifierActionFlowName_Object = MibTableColumn
portClassifierActionFlowName = _PortClassifierActionFlowName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 5),
    _PortClassifierActionFlowName_Type()
)
portClassifierActionFlowName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionFlowName.setStatus("current")
_PortClassifierActionFlowIndex1_Type = Unsigned32
_PortClassifierActionFlowIndex1_Object = MibTableColumn
portClassifierActionFlowIndex1 = _PortClassifierActionFlowIndex1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 6),
    _PortClassifierActionFlowIndex1_Type()
)
portClassifierActionFlowIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierActionFlowIndex1.setStatus("current")
_PortClassifierActionFlowIndex2_Type = Unsigned32
_PortClassifierActionFlowIndex2_Object = MibTableColumn
portClassifierActionFlowIndex2 = _PortClassifierActionFlowIndex2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 7),
    _PortClassifierActionFlowIndex2_Type()
)
portClassifierActionFlowIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierActionFlowIndex2.setStatus("current")


class _PortClassifierActionCos_Type(Unsigned32):
    """Custom type portClassifierActionCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_PortClassifierActionCos_Type.__name__ = "Unsigned32"
_PortClassifierActionCos_Object = MibTableColumn
portClassifierActionCos = _PortClassifierActionCos_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 8),
    _PortClassifierActionCos_Type()
)
portClassifierActionCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionCos.setStatus("current")


class _PortClassifierActionCosMapProfile_Type(Unsigned32):
    """Custom type portClassifierActionCosMapProfile based on Unsigned32"""
    defaultValue = 0


_PortClassifierActionCosMapProfile_Type.__name__ = "Unsigned32"
_PortClassifierActionCosMapProfile_Object = MibTableColumn
portClassifierActionCosMapProfile = _PortClassifierActionCosMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 9),
    _PortClassifierActionCosMapProfile_Type()
)
portClassifierActionCosMapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionCosMapProfile.setStatus("current")
_PortClassifierActionHits_Type = Counter64
_PortClassifierActionHits_Object = MibTableColumn
portClassifierActionHits = _PortClassifierActionHits_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 10),
    _PortClassifierActionHits_Type()
)
portClassifierActionHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierActionHits.setStatus("current")


class _PortClassifierActionCriteria_Type(Bits):
    """Custom type portClassifierActionCriteria based on Bits"""
    namedValues = NamedValues(
        *(("dstMacAddress", 0),
          ("srcMacAddress", 1),
          ("outerEtherType", 2),
          ("outerVlanId", 3),
          ("outerPbit", 4),
          ("outerDei", 5),
          ("innerEtherType", 6),
          ("innerVlanId", 7),
          ("innerPbit", 8),
          ("tos", 9),
          ("dscp", 10),
          ("ipPrecedence", 11),
          ("protocol", 12),
          ("srcIPAddress", 13),
          ("dstIPAddress", 14),
          ("tcpSrcPort", 15),
          ("tcpDstPort", 16),
          ("udpSrcPort", 17),
          ("udpDstPort", 18),
          ("untagged", 19))
    )

_PortClassifierActionCriteria_Type.__name__ = "Bits"
_PortClassifierActionCriteria_Object = MibTableColumn
portClassifierActionCriteria = _PortClassifierActionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 11),
    _PortClassifierActionCriteria_Type()
)
portClassifierActionCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionCriteria.setStatus("current")
_PortClassifierActionDstMacAddressLow_Type = MacAddress
_PortClassifierActionDstMacAddressLow_Object = MibTableColumn
portClassifierActionDstMacAddressLow = _PortClassifierActionDstMacAddressLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 12),
    _PortClassifierActionDstMacAddressLow_Type()
)
portClassifierActionDstMacAddressLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionDstMacAddressLow.setStatus("current")
_PortClassifierActionDstMacAddressHigh_Type = MacAddress
_PortClassifierActionDstMacAddressHigh_Object = MibTableColumn
portClassifierActionDstMacAddressHigh = _PortClassifierActionDstMacAddressHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 13),
    _PortClassifierActionDstMacAddressHigh_Type()
)
portClassifierActionDstMacAddressHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionDstMacAddressHigh.setStatus("current")
_PortClassifierActionSrcMacAddressLow_Type = MacAddress
_PortClassifierActionSrcMacAddressLow_Object = MibTableColumn
portClassifierActionSrcMacAddressLow = _PortClassifierActionSrcMacAddressLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 14),
    _PortClassifierActionSrcMacAddressLow_Type()
)
portClassifierActionSrcMacAddressLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionSrcMacAddressLow.setStatus("current")
_PortClassifierActionSrcMacAddressHigh_Type = MacAddress
_PortClassifierActionSrcMacAddressHigh_Object = MibTableColumn
portClassifierActionSrcMacAddressHigh = _PortClassifierActionSrcMacAddressHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 15),
    _PortClassifierActionSrcMacAddressHigh_Type()
)
portClassifierActionSrcMacAddressHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionSrcMacAddressHigh.setStatus("current")


class _PortClassifierActionOuterEtherType_Type(OctetString):
    """Custom type portClassifierActionOuterEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_PortClassifierActionOuterEtherType_Type.__name__ = "OctetString"
_PortClassifierActionOuterEtherType_Object = MibTableColumn
portClassifierActionOuterEtherType = _PortClassifierActionOuterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 16),
    _PortClassifierActionOuterEtherType_Type()
)
portClassifierActionOuterEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionOuterEtherType.setStatus("current")
_PortClassifierActionOuterVlanIdLow_Type = VlanIdOrAnyOrNone
_PortClassifierActionOuterVlanIdLow_Object = MibTableColumn
portClassifierActionOuterVlanIdLow = _PortClassifierActionOuterVlanIdLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 17),
    _PortClassifierActionOuterVlanIdLow_Type()
)
portClassifierActionOuterVlanIdLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionOuterVlanIdLow.setStatus("current")
_PortClassifierActionOuterVlanIdHigh_Type = VlanIdOrAnyOrNone
_PortClassifierActionOuterVlanIdHigh_Object = MibTableColumn
portClassifierActionOuterVlanIdHigh = _PortClassifierActionOuterVlanIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 18),
    _PortClassifierActionOuterVlanIdHigh_Type()
)
portClassifierActionOuterVlanIdHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionOuterVlanIdHigh.setStatus("current")


class _PortClassifierActionOuterPbitLow_Type(Unsigned32):
    """Custom type portClassifierActionOuterPbitLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortClassifierActionOuterPbitLow_Type.__name__ = "Unsigned32"
_PortClassifierActionOuterPbitLow_Object = MibTableColumn
portClassifierActionOuterPbitLow = _PortClassifierActionOuterPbitLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 19),
    _PortClassifierActionOuterPbitLow_Type()
)
portClassifierActionOuterPbitLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionOuterPbitLow.setStatus("current")


class _PortClassifierActionOuterPbitHigh_Type(Unsigned32):
    """Custom type portClassifierActionOuterPbitHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortClassifierActionOuterPbitHigh_Type.__name__ = "Unsigned32"
_PortClassifierActionOuterPbitHigh_Object = MibTableColumn
portClassifierActionOuterPbitHigh = _PortClassifierActionOuterPbitHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 20),
    _PortClassifierActionOuterPbitHigh_Type()
)
portClassifierActionOuterPbitHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionOuterPbitHigh.setStatus("current")


class _PortClassifierActionOuterDei_Type(Unsigned32):
    """Custom type portClassifierActionOuterDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortClassifierActionOuterDei_Type.__name__ = "Unsigned32"
_PortClassifierActionOuterDei_Object = MibTableColumn
portClassifierActionOuterDei = _PortClassifierActionOuterDei_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 21),
    _PortClassifierActionOuterDei_Type()
)
portClassifierActionOuterDei.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionOuterDei.setStatus("current")


class _PortClassifierActionInnerEtherType_Type(OctetString):
    """Custom type portClassifierActionInnerEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_PortClassifierActionInnerEtherType_Type.__name__ = "OctetString"
_PortClassifierActionInnerEtherType_Object = MibTableColumn
portClassifierActionInnerEtherType = _PortClassifierActionInnerEtherType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 22),
    _PortClassifierActionInnerEtherType_Type()
)
portClassifierActionInnerEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionInnerEtherType.setStatus("current")
_PortClassifierActionInnerVlanIdLow_Type = VlanIdOrAnyOrNone
_PortClassifierActionInnerVlanIdLow_Object = MibTableColumn
portClassifierActionInnerVlanIdLow = _PortClassifierActionInnerVlanIdLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 23),
    _PortClassifierActionInnerVlanIdLow_Type()
)
portClassifierActionInnerVlanIdLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionInnerVlanIdLow.setStatus("current")
_PortClassifierActionInnerVlanIdHigh_Type = VlanIdOrAnyOrNone
_PortClassifierActionInnerVlanIdHigh_Object = MibTableColumn
portClassifierActionInnerVlanIdHigh = _PortClassifierActionInnerVlanIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 24),
    _PortClassifierActionInnerVlanIdHigh_Type()
)
portClassifierActionInnerVlanIdHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionInnerVlanIdHigh.setStatus("current")


class _PortClassifierActionInnerPbitLow_Type(Unsigned32):
    """Custom type portClassifierActionInnerPbitLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortClassifierActionInnerPbitLow_Type.__name__ = "Unsigned32"
_PortClassifierActionInnerPbitLow_Object = MibTableColumn
portClassifierActionInnerPbitLow = _PortClassifierActionInnerPbitLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 25),
    _PortClassifierActionInnerPbitLow_Type()
)
portClassifierActionInnerPbitLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionInnerPbitLow.setStatus("current")


class _PortClassifierActionInnerPbitHigh_Type(Unsigned32):
    """Custom type portClassifierActionInnerPbitHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortClassifierActionInnerPbitHigh_Type.__name__ = "Unsigned32"
_PortClassifierActionInnerPbitHigh_Object = MibTableColumn
portClassifierActionInnerPbitHigh = _PortClassifierActionInnerPbitHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 26),
    _PortClassifierActionInnerPbitHigh_Type()
)
portClassifierActionInnerPbitHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionInnerPbitHigh.setStatus("current")


class _PortClassifierActionTosLow_Type(Unsigned32):
    """Custom type portClassifierActionTosLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortClassifierActionTosLow_Type.__name__ = "Unsigned32"
_PortClassifierActionTosLow_Object = MibTableColumn
portClassifierActionTosLow = _PortClassifierActionTosLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 27),
    _PortClassifierActionTosLow_Type()
)
portClassifierActionTosLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionTosLow.setStatus("current")


class _PortClassifierActionTosHigh_Type(Unsigned32):
    """Custom type portClassifierActionTosHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortClassifierActionTosHigh_Type.__name__ = "Unsigned32"
_PortClassifierActionTosHigh_Object = MibTableColumn
portClassifierActionTosHigh = _PortClassifierActionTosHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 28),
    _PortClassifierActionTosHigh_Type()
)
portClassifierActionTosHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionTosHigh.setStatus("current")


class _PortClassifierActionProtocol_Type(Unsigned32):
    """Custom type portClassifierActionProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortClassifierActionProtocol_Type.__name__ = "Unsigned32"
_PortClassifierActionProtocol_Object = MibTableColumn
portClassifierActionProtocol = _PortClassifierActionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 29),
    _PortClassifierActionProtocol_Type()
)
portClassifierActionProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionProtocol.setStatus("current")
_PortClassifierActionSrcIPAddressType_Type = InetAddressType
_PortClassifierActionSrcIPAddressType_Object = MibTableColumn
portClassifierActionSrcIPAddressType = _PortClassifierActionSrcIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 30),
    _PortClassifierActionSrcIPAddressType_Type()
)
portClassifierActionSrcIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionSrcIPAddressType.setStatus("current")
_PortClassifierActionSrcIPAddress_Type = InetAddress
_PortClassifierActionSrcIPAddress_Object = MibTableColumn
portClassifierActionSrcIPAddress = _PortClassifierActionSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 31),
    _PortClassifierActionSrcIPAddress_Type()
)
portClassifierActionSrcIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionSrcIPAddress.setStatus("current")
_PortClassifierActionSrcIPAddressPrefixLength_Type = InetAddressPrefixLength
_PortClassifierActionSrcIPAddressPrefixLength_Object = MibTableColumn
portClassifierActionSrcIPAddressPrefixLength = _PortClassifierActionSrcIPAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 32),
    _PortClassifierActionSrcIPAddressPrefixLength_Type()
)
portClassifierActionSrcIPAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionSrcIPAddressPrefixLength.setStatus("current")
_PortClassifierActionDstIPAddressType_Type = InetAddressType
_PortClassifierActionDstIPAddressType_Object = MibTableColumn
portClassifierActionDstIPAddressType = _PortClassifierActionDstIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 33),
    _PortClassifierActionDstIPAddressType_Type()
)
portClassifierActionDstIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionDstIPAddressType.setStatus("current")
_PortClassifierActionDstIPAddress_Type = InetAddress
_PortClassifierActionDstIPAddress_Object = MibTableColumn
portClassifierActionDstIPAddress = _PortClassifierActionDstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 34),
    _PortClassifierActionDstIPAddress_Type()
)
portClassifierActionDstIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionDstIPAddress.setStatus("current")
_PortClassifierActionDstIPAddressPrefixLength_Type = InetAddressPrefixLength
_PortClassifierActionDstIPAddressPrefixLength_Object = MibTableColumn
portClassifierActionDstIPAddressPrefixLength = _PortClassifierActionDstIPAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 35),
    _PortClassifierActionDstIPAddressPrefixLength_Type()
)
portClassifierActionDstIPAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionDstIPAddressPrefixLength.setStatus("current")
_PortClassifierActionTcpSrcPortLow_Type = InetPortNumber
_PortClassifierActionTcpSrcPortLow_Object = MibTableColumn
portClassifierActionTcpSrcPortLow = _PortClassifierActionTcpSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 36),
    _PortClassifierActionTcpSrcPortLow_Type()
)
portClassifierActionTcpSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionTcpSrcPortLow.setStatus("current")
_PortClassifierActionTcpSrcPortHigh_Type = InetPortNumber
_PortClassifierActionTcpSrcPortHigh_Object = MibTableColumn
portClassifierActionTcpSrcPortHigh = _PortClassifierActionTcpSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 37),
    _PortClassifierActionTcpSrcPortHigh_Type()
)
portClassifierActionTcpSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionTcpSrcPortHigh.setStatus("current")
_PortClassifierActionTcpDstPortLow_Type = InetPortNumber
_PortClassifierActionTcpDstPortLow_Object = MibTableColumn
portClassifierActionTcpDstPortLow = _PortClassifierActionTcpDstPortLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 38),
    _PortClassifierActionTcpDstPortLow_Type()
)
portClassifierActionTcpDstPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionTcpDstPortLow.setStatus("current")
_PortClassifierActionTcpDstPortHigh_Type = InetPortNumber
_PortClassifierActionTcpDstPortHigh_Object = MibTableColumn
portClassifierActionTcpDstPortHigh = _PortClassifierActionTcpDstPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 39),
    _PortClassifierActionTcpDstPortHigh_Type()
)
portClassifierActionTcpDstPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionTcpDstPortHigh.setStatus("current")
_PortClassifierActionUdpSrcPortLow_Type = InetPortNumber
_PortClassifierActionUdpSrcPortLow_Object = MibTableColumn
portClassifierActionUdpSrcPortLow = _PortClassifierActionUdpSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 40),
    _PortClassifierActionUdpSrcPortLow_Type()
)
portClassifierActionUdpSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionUdpSrcPortLow.setStatus("current")
_PortClassifierActionUdpSrcPortHigh_Type = InetPortNumber
_PortClassifierActionUdpSrcPortHigh_Object = MibTableColumn
portClassifierActionUdpSrcPortHigh = _PortClassifierActionUdpSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 41),
    _PortClassifierActionUdpSrcPortHigh_Type()
)
portClassifierActionUdpSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionUdpSrcPortHigh.setStatus("current")
_PortClassifierActionUdpDstPortLow_Type = InetPortNumber
_PortClassifierActionUdpDstPortLow_Object = MibTableColumn
portClassifierActionUdpDstPortLow = _PortClassifierActionUdpDstPortLow_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 42),
    _PortClassifierActionUdpDstPortLow_Type()
)
portClassifierActionUdpDstPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionUdpDstPortLow.setStatus("current")
_PortClassifierActionUdpDstPortHigh_Type = InetPortNumber
_PortClassifierActionUdpDstPortHigh_Object = MibTableColumn
portClassifierActionUdpDstPortHigh = _PortClassifierActionUdpDstPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 3, 1, 43),
    _PortClassifierActionUdpDstPortHigh_Type()
)
portClassifierActionUdpDstPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierActionUdpDstPortHigh.setStatus("current")
_PortClassifierCommentTable_Object = MibTable
portClassifierCommentTable = _PortClassifierCommentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 4)
)
if mibBuilder.loadTexts:
    portClassifierCommentTable.setStatus("current")
_PortClassifierCommentEntry_Object = MibTableRow
portClassifierCommentEntry = _PortClassifierCommentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 4, 1)
)
portClassifierCommentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-Services-MIB", "portClassifierCommentIndex"),
)
if mibBuilder.loadTexts:
    portClassifierCommentEntry.setStatus("current")
_PortClassifierCommentIndex_Type = Unsigned32
_PortClassifierCommentIndex_Object = MibTableColumn
portClassifierCommentIndex = _PortClassifierCommentIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 4, 1, 1),
    _PortClassifierCommentIndex_Type()
)
portClassifierCommentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portClassifierCommentIndex.setStatus("current")
_PortClassifierCommentRowStatus_Type = RowStatus
_PortClassifierCommentRowStatus_Object = MibTableColumn
portClassifierCommentRowStatus = _PortClassifierCommentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 4, 1, 2),
    _PortClassifierCommentRowStatus_Type()
)
portClassifierCommentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierCommentRowStatus.setStatus("current")


class _PortClassifierCommentSequenceNumber_Type(Unsigned32):
    """Custom type portClassifierCommentSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PortClassifierCommentSequenceNumber_Type.__name__ = "Unsigned32"
_PortClassifierCommentSequenceNumber_Object = MibTableColumn
portClassifierCommentSequenceNumber = _PortClassifierCommentSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 4, 1, 3),
    _PortClassifierCommentSequenceNumber_Type()
)
portClassifierCommentSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierCommentSequenceNumber.setStatus("current")


class _PortClassifierCommentDescr_Type(SnmpAdminString):
    """Custom type portClassifierCommentDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_PortClassifierCommentDescr_Type.__name__ = "SnmpAdminString"
_PortClassifierCommentDescr_Object = MibTableColumn
portClassifierCommentDescr = _PortClassifierCommentDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 4, 1, 4),
    _PortClassifierCommentDescr_Type()
)
portClassifierCommentDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portClassifierCommentDescr.setStatus("current")
_PortClassifierInvTable_Object = MibTable
portClassifierInvTable = _PortClassifierInvTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 5)
)
if mibBuilder.loadTexts:
    portClassifierInvTable.setStatus("current")
_PortClassifierInvEntry_Object = MibTableRow
portClassifierInvEntry = _PortClassifierInvEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 5, 1)
)
portClassifierInvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-Services-MIB", "portClassifierInvSequenceNumber"),
)
if mibBuilder.loadTexts:
    portClassifierInvEntry.setStatus("current")
_PortClassifierInvSequenceNumber_Type = Unsigned32
_PortClassifierInvSequenceNumber_Object = MibTableColumn
portClassifierInvSequenceNumber = _PortClassifierInvSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 5, 1, 1),
    _PortClassifierInvSequenceNumber_Type()
)
portClassifierInvSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portClassifierInvSequenceNumber.setStatus("current")


class _PortClassifierInvType_Type(Integer32):
    """Custom type portClassifierInvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("action", 1),
          ("comment", 2))
    )


_PortClassifierInvType_Type.__name__ = "Integer32"
_PortClassifierInvType_Object = MibTableColumn
portClassifierInvType = _PortClassifierInvType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 5, 1, 2),
    _PortClassifierInvType_Type()
)
portClassifierInvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierInvType.setStatus("current")
_PortClassifierInvPointer_Type = Unsigned32
_PortClassifierInvPointer_Object = MibTableColumn
portClassifierInvPointer = _PortClassifierInvPointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 3, 17, 5, 1, 3),
    _PortClassifierInvPointer_Type()
)
portClassifierInvPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClassifierInvPointer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-Services-MIB",
    **{"Dscp": Dscp,
       "ProfileMethod": ProfileMethod,
       "services": services,
       "wfq": wfq,
       "wfqTable": wfqTable,
       "wfqEntry": wfqEntry,
       "wfqCnfgIdx": wfqCnfgIdx,
       "wfqPrtIdx": wfqPrtIdx,
       "wfqTblIdx": wfqTblIdx,
       "wfqQueueIdx": wfqQueueIdx,
       "wfqRowStatus": wfqRowStatus,
       "wfqWeightValue": wfqWeightValue,
       "wfqSchedulingMode": wfqSchedulingMode,
       "wfqMinRateAbsolute": wfqMinRateAbsolute,
       "wfqMaxPacketSize": wfqMaxPacketSize,
       "dscpMapping": dscpMapping,
       "dscpMappingTable": dscpMappingTable,
       "dscpMappingEntry": dscpMappingEntry,
       "dscpMappingCnfgIdx": dscpMappingCnfgIdx,
       "dscpMappingDscpIdx": dscpMappingDscpIdx,
       "dscpMappingRegenPriority": dscpMappingRegenPriority,
       "ifTeQos": ifTeQos,
       "ifTeQosTable": ifTeQosTable,
       "ifTeQosEntry": ifTeQosEntry,
       "ifTeQosIdx1": ifTeQosIdx1,
       "ifTeQosIdx2": ifTeQosIdx2,
       "ifTeQosIdx3": ifTeQosIdx3,
       "ifTeQosParam": ifTeQosParam,
       "ifTeQosParam2": ifTeQosParam2,
       "ifTeQosStatus": ifTeQosStatus,
       "portQos": portQos,
       "prtPriorityTable": prtPriorityTable,
       "prtPriorityEntry": prtPriorityEntry,
       "prtPriorityIdx1": prtPriorityIdx1,
       "prtPriorityPrtIdx": prtPriorityPrtIdx,
       "prtPriorityIdx": prtPriorityIdx,
       "prtPriorityIngressRateLimit": prtPriorityIngressRateLimit,
       "prtQosTable": prtQosTable,
       "prtQosEntry": prtQosEntry,
       "prtQosIdx": prtQosIdx,
       "prtQosPrtIdx": prtQosPrtIdx,
       "prtQosDirection": prtQosDirection,
       "prtQosRateLimitPacketType": prtQosRateLimitPacketType,
       "prtQosRateLimitCIR": prtQosRateLimitCIR,
       "prtQosRateLimitCBS": prtQosRateLimitCBS,
       "prtQosRateLimitEIR": prtQosRateLimitEIR,
       "prtQosRateLimitEBS": prtQosRateLimitEBS,
       "prtTrafficClass": prtTrafficClass,
       "portTrafficClassTable": portTrafficClassTable,
       "portTrafficClassEntry": portTrafficClassEntry,
       "portTrafficClassIdx1": portTrafficClassIdx1,
       "portTrafficClassPortIdx": portTrafficClassPortIdx,
       "portTrafficClass": portTrafficClass,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "flowIndex": flowIndex,
       "serviceIndex": serviceIndex,
       "serviceRowStatus": serviceRowStatus,
       "serviceName": serviceName,
       "serviceBwProfileId": serviceBwProfileId,
       "evcCosTable": evcCosTable,
       "evcCosEntry": evcCosEntry,
       "evcCosCnfgIdx": evcCosCnfgIdx,
       "evcCosEvcIdx": evcCosEvcIdx,
       "evcCosRowStatus": evcCosRowStatus,
       "evcCosEvcName": evcCosEvcName,
       "evcCosSpVlanId": evcCosSpVlanId,
       "serviceStatTable": serviceStatTable,
       "serviceStatEntry": serviceStatEntry,
       "serviceStatDirection": serviceStatDirection,
       "srvForwardGreenPackets": srvForwardGreenPackets,
       "srvForwardGreenPacketsOverflow": srvForwardGreenPacketsOverflow,
       "srvForwardYellowPackets": srvForwardYellowPackets,
       "srvForwardYellowPacketsOverflow": srvForwardYellowPacketsOverflow,
       "srvDiscardGreenPackets": srvDiscardGreenPackets,
       "srvDiscardGreenPacketsOverflow": srvDiscardGreenPacketsOverflow,
       "srvDiscardYellowRedPackets": srvDiscardYellowRedPackets,
       "srvDiscardYellowRedPacketsOverflow": srvDiscardYellowRedPacketsOverflow,
       "srvForwardGreenBytes": srvForwardGreenBytes,
       "srvForwardGreenBytesOverflow": srvForwardGreenBytesOverflow,
       "srvForwardYellowBytes": srvForwardYellowBytes,
       "srvForwardYellowBytesOverflow": srvForwardYellowBytesOverflow,
       "srvDiscardGreenBytes": srvDiscardGreenBytes,
       "srvDiscardGreenBytesOverflow": srvDiscardGreenBytesOverflow,
       "srvDiscardYellowRedBytes": srvDiscardYellowRedBytes,
       "srvDiscardYellowRedBytesOverflow": srvDiscardYellowRedBytesOverflow,
       "srvResetStatsCmd": srvResetStatsCmd,
       "srvDiscardYellowPackets": srvDiscardYellowPackets,
       "srvDiscardYellowPacketsOverflow": srvDiscardYellowPacketsOverflow,
       "srvDiscardYellowBytes": srvDiscardYellowBytes,
       "srvDiscardYellowBytesOverflow": srvDiscardYellowBytesOverflow,
       "srvDiscardRedPackets": srvDiscardRedPackets,
       "srvDiscardRedPacketsOverflow": srvDiscardRedPacketsOverflow,
       "srvDiscardRedBytes": srvDiscardRedBytes,
       "srvDiscardRedBytesOverflow": srvDiscardRedBytesOverflow,
       "mappingProfileObjects": mappingProfileObjects,
       "flowMappingProfileTable": flowMappingProfileTable,
       "flowMappingProfileEntry": flowMappingProfileEntry,
       "flowMappingProfileIndex": flowMappingProfileIndex,
       "flowMappingProfilePriority": flowMappingProfilePriority,
       "flowMappingProfileRowStatus": flowMappingProfileRowStatus,
       "flowMappingProfileNumOfMaps": flowMappingProfileNumOfMaps,
       "flowMappingProfileMapIndex": flowMappingProfileMapIndex,
       "flowMappingProfileName": flowMappingProfileName,
       "flowMappingProfileCondition": flowMappingProfileCondition,
       "qosFlowMappingTable": qosFlowMappingTable,
       "qosFlowMappingEntry": qosFlowMappingEntry,
       "qosFlowMappingIdx1": qosFlowMappingIdx1,
       "qosFlowMappingIdx2": qosFlowMappingIdx2,
       "qosFlowMappingIdx3": qosFlowMappingIdx3,
       "qosFlowMappingRowStatus": qosFlowMappingRowStatus,
       "qosFlowMappingCriteria": qosFlowMappingCriteria,
       "qosFlowMappingIeee802dot1p": qosFlowMappingIeee802dot1p,
       "qosFlowMappingTos": qosFlowMappingTos,
       "qosFlowMappingFromDscp": qosFlowMappingFromDscp,
       "qosFlowMappingToDscp": qosFlowMappingToDscp,
       "qosFlowMappingFromVlanId": qosFlowMappingFromVlanId,
       "qosFlowMappingToVlanId": qosFlowMappingToVlanId,
       "qosFlowMappingFromSrcMacAddr": qosFlowMappingFromSrcMacAddr,
       "qosFlowMappingToSrcMacAddr": qosFlowMappingToSrcMacAddr,
       "qosFlowMappingFromDestMacAddr": qosFlowMappingFromDestMacAddr,
       "qosFlowMappingToDestMacAddr": qosFlowMappingToDestMacAddr,
       "qosFlowMappingFromSrcIpAddr": qosFlowMappingFromSrcIpAddr,
       "qosFlowMappingToSrcIpAddr": qosFlowMappingToSrcIpAddr,
       "qosFlowMappingFromDestIpAddr": qosFlowMappingFromDestIpAddr,
       "qosFlowMappingToDestIpAddr": qosFlowMappingToDestIpAddr,
       "qosFlowMappingFromTcpSrcPort": qosFlowMappingFromTcpSrcPort,
       "qosFlowMappingToTcpSrcPort": qosFlowMappingToTcpSrcPort,
       "qosFlowMappingFromTcpDestPort": qosFlowMappingFromTcpDestPort,
       "qosFlowMappingToTcpDestPort": qosFlowMappingToTcpDestPort,
       "qosFlowMappingFromUdpSrcPort": qosFlowMappingFromUdpSrcPort,
       "qosFlowMappingToUdpSrcPort": qosFlowMappingToUdpSrcPort,
       "qosFlowMappingFromUdpDestPort": qosFlowMappingFromUdpDestPort,
       "qosFlowMappingToUdpDestPort": qosFlowMappingToUdpDestPort,
       "qosFlowMappingFromIpPrecedence": qosFlowMappingFromIpPrecedence,
       "qosFlowMappingToIpPrecedence": qosFlowMappingToIpPrecedence,
       "qosFlowMappingInnerIeee802dot1p": qosFlowMappingInnerIeee802dot1p,
       "qosFlowMappingFromInnerVlanId": qosFlowMappingFromInnerVlanId,
       "qosFlowMappingToInnerVlanId": qosFlowMappingToInnerVlanId,
       "qosFlowMappingEtherType": qosFlowMappingEtherType,
       "cosProfileTable": cosProfileTable,
       "cosProfileEntry": cosProfileEntry,
       "cosProfileIndex": cosProfileIndex,
       "cosProfileRowStatus": cosProfileRowStatus,
       "cosProfileCosMethod": cosProfileCosMethod,
       "cosProfileName": cosProfileName,
       "cosProfileCosMapping": cosProfileCosMapping,
       "queueProfileObjects": queueProfileObjects,
       "qProfileTable": qProfileTable,
       "qProfileEntry": qProfileEntry,
       "qProfileIndex": qProfileIndex,
       "qProfileRowStatus": qProfileRowStatus,
       "qProfileName": qProfileName,
       "qProfileNumberOfInternalQ": qProfileNumberOfInternalQ,
       "qProfileInternalQProfile": qProfileInternalQProfile,
       "qInternalProfileTable": qInternalProfileTable,
       "qInternalProfileEntry": qInternalProfileEntry,
       "qInternalProfileIndex": qInternalProfileIndex,
       "qInternalProfileRowStatus": qInternalProfileRowStatus,
       "qInternalProfileScheduling": qInternalProfileScheduling,
       "qInternalProfileWFQWeight": qInternalProfileWFQWeight,
       "qInternalProfileQueueLength": qInternalProfileQueueLength,
       "qInternalProfileWredStartDropThresh": qInternalProfileWredStartDropThresh,
       "qInternalProfileWredDropAllThresh": qInternalProfileWredDropAllThresh,
       "qInternalProfileWredDropProbability": qInternalProfileWredDropProbability,
       "qInternalProfileRateLimit": qInternalProfileRateLimit,
       "qInternalProfileShaperProfile": qInternalProfileShaperProfile,
       "qInternalProfileWredProfile": qInternalProfileWredProfile,
       "qInternalProfileFrameBuffers": qInternalProfileFrameBuffers,
       "queueGroupTable": queueGroupTable,
       "queueGroupEntry": queueGroupEntry,
       "queueGroupName": queueGroupName,
       "queueGroupQBlockLevel": queueGroupQBlockLevel,
       "queueGroupQBlockIdx": queueGroupQBlockIdx,
       "queueGroupRowStatus": queueGroupRowStatus,
       "queueGroupQBlockProfile": queueGroupQBlockProfile,
       "queueGroupQBlockShaperProfile": queueGroupQBlockShaperProfile,
       "queueGroupPointToQBlock": queueGroupPointToQBlock,
       "queueGroupPointToInternalQueue": queueGroupPointToInternalQueue,
       "queueGroupQBlockName": queueGroupQBlockName,
       "markingProfileTable": markingProfileTable,
       "markingProfileEntry": markingProfileEntry,
       "markingProfileIndex": markingProfileIndex,
       "markingProfileRowStatus": markingProfileRowStatus,
       "markingProfileName": markingProfileName,
       "markingSpVlanPBit": markingSpVlanPBit,
       "markingProfileMethod": markingProfileMethod,
       "markingProfileColorAware": markingProfileColorAware,
       "markingProfileDeiAware": markingProfileDeiAware,
       "markingProfileDeiColor": markingProfileDeiColor,
       "markingProfileDscpColor": markingProfileDscpColor,
       "markingProfileMarkedField": markingProfileMarkedField,
       "wredProfileTable": wredProfileTable,
       "wredProfileEntry": wredProfileEntry,
       "wredProfileIndex": wredProfileIndex,
       "wredProfileColor": wredProfileColor,
       "wredProfileRowStatus": wredProfileRowStatus,
       "wredProfileName": wredProfileName,
       "wredProfileMinThreshold": wredProfileMinThreshold,
       "wredProfileMaxThreshold": wredProfileMaxThreshold,
       "wredProfileMaxProbability": wredProfileMaxProbability,
       "sviTable": sviTable,
       "sviEntry": sviEntry,
       "sviIndex": sviIndex,
       "sviBoundToType": sviBoundToType,
       "cosInternalProfileTable": cosInternalProfileTable,
       "cosInternalProfileEntry": cosInternalProfileEntry,
       "cosInternalProfileIndex": cosInternalProfileIndex,
       "cosInternalProfileRowStatus": cosInternalProfileRowStatus,
       "cosInternalProfileCosMethod": cosInternalProfileCosMethod,
       "cosInternalProfileName": cosInternalProfileName,
       "cosInternalProfileCosMapping": cosInternalProfileCosMapping,
       "cosInternalProfileUntaggedMapping": cosInternalProfileUntaggedMapping,
       "cosInternalProfileNonIpMapping": cosInternalProfileNonIpMapping,
       "colorMappingProfileTable": colorMappingProfileTable,
       "colorMappingProfileEntry": colorMappingProfileEntry,
       "colorMappingProfileIndex": colorMappingProfileIndex,
       "colorMappingProfileRowStatus": colorMappingProfileRowStatus,
       "colorMappingProfileMethod": colorMappingProfileMethod,
       "colorMappingProfileName": colorMappingProfileName,
       "colorMappingProfileMapping": colorMappingProfileMapping,
       "portClassifierObjects": portClassifierObjects,
       "portClassifierScalarObjects": portClassifierScalarObjects,
       "portClassifierRemainingActions": portClassifierRemainingActions,
       "portClassifierTable": portClassifierTable,
       "portClassifierEntry": portClassifierEntry,
       "portClassifierRowStatus": portClassifierRowStatus,
       "portClassifierNumberOfActions": portClassifierNumberOfActions,
       "portClassifierHighSequenceNumber": portClassifierHighSequenceNumber,
       "portClassifierResequenceCmd": portClassifierResequenceCmd,
       "portClassifierActionTable": portClassifierActionTable,
       "portClassifierActionEntry": portClassifierActionEntry,
       "portClassifierActionIndex": portClassifierActionIndex,
       "portClassifierActionRowStatus": portClassifierActionRowStatus,
       "portClassifierActionSequenceNumber": portClassifierActionSequenceNumber,
       "portClassifierActionType": portClassifierActionType,
       "portClassifierActionFlowName": portClassifierActionFlowName,
       "portClassifierActionFlowIndex1": portClassifierActionFlowIndex1,
       "portClassifierActionFlowIndex2": portClassifierActionFlowIndex2,
       "portClassifierActionCos": portClassifierActionCos,
       "portClassifierActionCosMapProfile": portClassifierActionCosMapProfile,
       "portClassifierActionHits": portClassifierActionHits,
       "portClassifierActionCriteria": portClassifierActionCriteria,
       "portClassifierActionDstMacAddressLow": portClassifierActionDstMacAddressLow,
       "portClassifierActionDstMacAddressHigh": portClassifierActionDstMacAddressHigh,
       "portClassifierActionSrcMacAddressLow": portClassifierActionSrcMacAddressLow,
       "portClassifierActionSrcMacAddressHigh": portClassifierActionSrcMacAddressHigh,
       "portClassifierActionOuterEtherType": portClassifierActionOuterEtherType,
       "portClassifierActionOuterVlanIdLow": portClassifierActionOuterVlanIdLow,
       "portClassifierActionOuterVlanIdHigh": portClassifierActionOuterVlanIdHigh,
       "portClassifierActionOuterPbitLow": portClassifierActionOuterPbitLow,
       "portClassifierActionOuterPbitHigh": portClassifierActionOuterPbitHigh,
       "portClassifierActionOuterDei": portClassifierActionOuterDei,
       "portClassifierActionInnerEtherType": portClassifierActionInnerEtherType,
       "portClassifierActionInnerVlanIdLow": portClassifierActionInnerVlanIdLow,
       "portClassifierActionInnerVlanIdHigh": portClassifierActionInnerVlanIdHigh,
       "portClassifierActionInnerPbitLow": portClassifierActionInnerPbitLow,
       "portClassifierActionInnerPbitHigh": portClassifierActionInnerPbitHigh,
       "portClassifierActionTosLow": portClassifierActionTosLow,
       "portClassifierActionTosHigh": portClassifierActionTosHigh,
       "portClassifierActionProtocol": portClassifierActionProtocol,
       "portClassifierActionSrcIPAddressType": portClassifierActionSrcIPAddressType,
       "portClassifierActionSrcIPAddress": portClassifierActionSrcIPAddress,
       "portClassifierActionSrcIPAddressPrefixLength": portClassifierActionSrcIPAddressPrefixLength,
       "portClassifierActionDstIPAddressType": portClassifierActionDstIPAddressType,
       "portClassifierActionDstIPAddress": portClassifierActionDstIPAddress,
       "portClassifierActionDstIPAddressPrefixLength": portClassifierActionDstIPAddressPrefixLength,
       "portClassifierActionTcpSrcPortLow": portClassifierActionTcpSrcPortLow,
       "portClassifierActionTcpSrcPortHigh": portClassifierActionTcpSrcPortHigh,
       "portClassifierActionTcpDstPortLow": portClassifierActionTcpDstPortLow,
       "portClassifierActionTcpDstPortHigh": portClassifierActionTcpDstPortHigh,
       "portClassifierActionUdpSrcPortLow": portClassifierActionUdpSrcPortLow,
       "portClassifierActionUdpSrcPortHigh": portClassifierActionUdpSrcPortHigh,
       "portClassifierActionUdpDstPortLow": portClassifierActionUdpDstPortLow,
       "portClassifierActionUdpDstPortHigh": portClassifierActionUdpDstPortHigh,
       "portClassifierCommentTable": portClassifierCommentTable,
       "portClassifierCommentEntry": portClassifierCommentEntry,
       "portClassifierCommentIndex": portClassifierCommentIndex,
       "portClassifierCommentRowStatus": portClassifierCommentRowStatus,
       "portClassifierCommentSequenceNumber": portClassifierCommentSequenceNumber,
       "portClassifierCommentDescr": portClassifierCommentDescr,
       "portClassifierInvTable": portClassifierInvTable,
       "portClassifierInvEntry": portClassifierInvEntry,
       "portClassifierInvSequenceNumber": portClassifierInvSequenceNumber,
       "portClassifierInvType": portClassifierInvType,
       "portClassifierInvPointer": portClassifierInvPointer}
)
