# SNMP MIB module (INFINET-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:06 2025
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

(wanflex,) = mibBuilder.importSymbols(
    "INFINET-MIB",
    "wanflex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

iwBrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8)
)
if mibBuilder.loadTexts:
    iwBrMIB.setRevisions(
        ("2014-03-13 07:18",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class Timeout(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class BridgeGroupIdOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_IwBrMIBObjects_ObjectIdentity = ObjectIdentity
iwBrMIBObjects = _IwBrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1)
)
_IwBrBase_ObjectIdentity = ObjectIdentity
iwBrBase = _IwBrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 1)
)
_IwBrBaseAddress_Type = MacAddress
_IwBrBaseAddress_Object = MibScalar
iwBrBaseAddress = _IwBrBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 1, 1),
    _IwBrBaseAddress_Type()
)
iwBrBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBaseAddress.setStatus("current")
_IwBrBasePorts_Type = Integer32
_IwBrBasePorts_Object = MibScalar
iwBrBasePorts = _IwBrBasePorts_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 1, 2),
    _IwBrBasePorts_Type()
)
iwBrBasePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBasePorts.setStatus("current")


class _IwBrBaseType_Type(Integer32):
    """Custom type iwBrBaseType based on Integer32"""
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
          ("transparent-only", 2),
          ("sourceroute-only", 3),
          ("srt", 4))
    )


_IwBrBaseType_Type.__name__ = "Integer32"
_IwBrBaseType_Object = MibScalar
iwBrBaseType = _IwBrBaseType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 1, 3),
    _IwBrBaseType_Type()
)
iwBrBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBaseType.setStatus("current")
_IwBrLocalTag_Type = Integer32
_IwBrLocalTag_Object = MibScalar
iwBrLocalTag = _IwBrLocalTag_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 1, 4),
    _IwBrLocalTag_Type()
)
iwBrLocalTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrLocalTag.setStatus("current")
_IwBrStp_ObjectIdentity = ObjectIdentity
iwBrStp = _IwBrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2)
)


class _IwBrStpProtoSpec_Type(Integer32):
    """Custom type iwBrStpProtoSpec based on Integer32"""
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
          ("decLb100", 2),
          ("ieee8021d", 3))
    )


_IwBrStpProtoSpec_Type.__name__ = "Integer32"
_IwBrStpProtoSpec_Object = MibScalar
iwBrStpProtoSpec = _IwBrStpProtoSpec_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 1),
    _IwBrStpProtoSpec_Type()
)
iwBrStpProtoSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpProtoSpec.setStatus("current")


class _IwBrStpPriority_Type(Integer32):
    """Custom type iwBrStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IwBrStpPriority_Type.__name__ = "Integer32"
_IwBrStpPriority_Object = MibScalar
iwBrStpPriority = _IwBrStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 2),
    _IwBrStpPriority_Type()
)
iwBrStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrStpPriority.setStatus("current")
_IwBrStpTimeSinceTopoChange_Type = TimeTicks
_IwBrStpTimeSinceTopoChange_Object = MibScalar
iwBrStpTimeSinceTopoChange = _IwBrStpTimeSinceTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 3),
    _IwBrStpTimeSinceTopoChange_Type()
)
iwBrStpTimeSinceTopoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpTimeSinceTopoChange.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpTimeSinceTopoChange.setUnits("centi-seconds")
_IwBrStpTopChanges_Type = Counter32
_IwBrStpTopChanges_Object = MibScalar
iwBrStpTopChanges = _IwBrStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 4),
    _IwBrStpTopChanges_Type()
)
iwBrStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpTopChanges.setStatus("current")
_IwBrStpMaxAge_Type = Timeout
_IwBrStpMaxAge_Object = MibScalar
iwBrStpMaxAge = _IwBrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 5),
    _IwBrStpMaxAge_Type()
)
iwBrStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpMaxAge.setUnits("centi-seconds")
_IwBrStpHelloTime_Type = Timeout
_IwBrStpHelloTime_Object = MibScalar
iwBrStpHelloTime = _IwBrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 6),
    _IwBrStpHelloTime_Type()
)
iwBrStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpHelloTime.setUnits("centi-seconds")
_IwBrStpHoldTime_Type = Integer32
_IwBrStpHoldTime_Object = MibScalar
iwBrStpHoldTime = _IwBrStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 7),
    _IwBrStpHoldTime_Type()
)
iwBrStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpHoldTime.setUnits("centi-seconds")
_IwBrStpForwardDelay_Type = Timeout
_IwBrStpForwardDelay_Object = MibScalar
iwBrStpForwardDelay = _IwBrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 8),
    _IwBrStpForwardDelay_Type()
)
iwBrStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrStpForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpForwardDelay.setUnits("centi-seconds")


class _IwBrStpBridgeMaxAge_Type(Timeout):
    """Custom type iwBrStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_IwBrStpBridgeMaxAge_Type.__name__ = "Timeout"
_IwBrStpBridgeMaxAge_Object = MibScalar
iwBrStpBridgeMaxAge = _IwBrStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 9),
    _IwBrStpBridgeMaxAge_Type()
)
iwBrStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrStpBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpBridgeMaxAge.setUnits("centi-seconds")


class _IwBrStpBridgeHelloTime_Type(Timeout):
    """Custom type iwBrStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_IwBrStpBridgeHelloTime_Type.__name__ = "Timeout"
_IwBrStpBridgeHelloTime_Object = MibScalar
iwBrStpBridgeHelloTime = _IwBrStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 10),
    _IwBrStpBridgeHelloTime_Type()
)
iwBrStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrStpBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpBridgeHelloTime.setUnits("centi-seconds")


class _IwBrStpBridgeForwardDelay_Type(Timeout):
    """Custom type iwBrStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_IwBrStpBridgeForwardDelay_Type.__name__ = "Timeout"
_IwBrStpBridgeForwardDelay_Object = MibScalar
iwBrStpBridgeForwardDelay = _IwBrStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 2, 11),
    _IwBrStpBridgeForwardDelay_Type()
)
iwBrStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrStpBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    iwBrStpBridgeForwardDelay.setUnits("centi-seconds")
_IwBrPorts_ObjectIdentity = ObjectIdentity
iwBrPorts = _IwBrPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3)
)
_IwBrPortTable_Object = MibTable
iwBrPortTable = _IwBrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    iwBrPortTable.setStatus("current")
_IwBrPortEntry_Object = MibTableRow
iwBrPortEntry = _IwBrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1)
)
iwBrPortEntry.setIndexNames(
    (0, "INFINET-BRIDGE-MIB", "iwBrPortGrpId"),
    (0, "INFINET-BRIDGE-MIB", "iwBrPortId"),
)
if mibBuilder.loadTexts:
    iwBrPortEntry.setStatus("current")
_IwBrPortGrpId_Type = BridgeGroupIdOrZero
_IwBrPortGrpId_Object = MibTableColumn
iwBrPortGrpId = _IwBrPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 1),
    _IwBrPortGrpId_Type()
)
iwBrPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortGrpId.setStatus("current")
_IwBrPortId_Type = InterfaceIndex
_IwBrPortId_Object = MibTableColumn
iwBrPortId = _IwBrPortId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 2),
    _IwBrPortId_Type()
)
iwBrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortId.setStatus("current")


class _IwBrPortStpPrio_Type(Integer32):
    """Custom type iwBrPortStpPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IwBrPortStpPrio_Type.__name__ = "Integer32"
_IwBrPortStpPrio_Object = MibTableColumn
iwBrPortStpPrio = _IwBrPortStpPrio_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 3),
    _IwBrPortStpPrio_Type()
)
iwBrPortStpPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrPortStpPrio.setStatus("current")


class _IwBrPortStpState_Type(Integer32):
    """Custom type iwBrPortStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_IwBrPortStpState_Type.__name__ = "Integer32"
_IwBrPortStpState_Object = MibTableColumn
iwBrPortStpState = _IwBrPortStpState_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 4),
    _IwBrPortStpState_Type()
)
iwBrPortStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpState.setStatus("current")


class _IwBrPortStpRole_Type(Integer32):
    """Custom type iwBrPortStpRole based on Integer32"""
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
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backup", 5))
    )


_IwBrPortStpRole_Type.__name__ = "Integer32"
_IwBrPortStpRole_Object = MibTableColumn
iwBrPortStpRole = _IwBrPortStpRole_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 5),
    _IwBrPortStpRole_Type()
)
iwBrPortStpRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpRole.setStatus("current")
_IwBrPortStpDesCost_Type = Integer32
_IwBrPortStpDesCost_Object = MibTableColumn
iwBrPortStpDesCost = _IwBrPortStpDesCost_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 6),
    _IwBrPortStpDesCost_Type()
)
iwBrPortStpDesCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpDesCost.setStatus("current")
_IwBrPortStpDesBridge_Type = BridgeId
_IwBrPortStpDesBridge_Object = MibTableColumn
iwBrPortStpDesBridge = _IwBrPortStpDesBridge_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 7),
    _IwBrPortStpDesBridge_Type()
)
iwBrPortStpDesBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpDesBridge.setStatus("current")


class _IwBrPortStpDesPort_Type(Integer32):
    """Custom type iwBrPortStpDesPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IwBrPortStpDesPort_Type.__name__ = "Integer32"
_IwBrPortStpDesPort_Object = MibTableColumn
iwBrPortStpDesPort = _IwBrPortStpDesPort_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 8),
    _IwBrPortStpDesPort_Type()
)
iwBrPortStpDesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpDesPort.setStatus("current")
_IwBrPortStpFwdTransitions_Type = Counter32
_IwBrPortStpFwdTransitions_Object = MibTableColumn
iwBrPortStpFwdTransitions = _IwBrPortStpFwdTransitions_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 9),
    _IwBrPortStpFwdTransitions_Type()
)
iwBrPortStpFwdTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpFwdTransitions.setStatus("current")


class _IwBrPortStpPathCost32_Type(Integer32):
    """Custom type iwBrPortStpPathCost32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_IwBrPortStpPathCost32_Type.__name__ = "Integer32"
_IwBrPortStpPathCost32_Object = MibTableColumn
iwBrPortStpPathCost32 = _IwBrPortStpPathCost32_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 10),
    _IwBrPortStpPathCost32_Type()
)
iwBrPortStpPathCost32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrPortStpPathCost32.setStatus("current")


class _IwBrPortVlanAlteration_Type(Integer32):
    """Custom type iwBrPortVlanAlteration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_IwBrPortVlanAlteration_Type.__name__ = "Integer32"
_IwBrPortVlanAlteration_Object = MibTableColumn
iwBrPortVlanAlteration = _IwBrPortVlanAlteration_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 3, 1, 1, 11),
    _IwBrPortVlanAlteration_Type()
)
iwBrPortVlanAlteration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrPortVlanAlteration.setStatus("current")
_IwBrDb_ObjectIdentity = ObjectIdentity
iwBrDb = _IwBrDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4)
)
_IwBrDbEntryDiscards_Type = Counter32
_IwBrDbEntryDiscards_Object = MibScalar
iwBrDbEntryDiscards = _IwBrDbEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 1),
    _IwBrDbEntryDiscards_Type()
)
iwBrDbEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbEntryDiscards.setStatus("current")


class _IwBrDbAgingTime_Type(Integer32):
    """Custom type iwBrDbAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_IwBrDbAgingTime_Type.__name__ = "Integer32"
_IwBrDbAgingTime_Object = MibScalar
iwBrDbAgingTime = _IwBrDbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 2),
    _IwBrDbAgingTime_Type()
)
iwBrDbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrDbAgingTime.setStatus("current")
_IwBrDbTable_Object = MibTable
iwBrDbTable = _IwBrDbTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3)
)
if mibBuilder.loadTexts:
    iwBrDbTable.setStatus("current")
_IwBrDbEntry_Object = MibTableRow
iwBrDbEntry = _IwBrDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1)
)
iwBrDbEntry.setIndexNames(
    (0, "INFINET-BRIDGE-MIB", "iwBrDbGroupId"),
    (0, "INFINET-BRIDGE-MIB", "iwBrDbAddress"),
)
if mibBuilder.loadTexts:
    iwBrDbEntry.setStatus("current")
_IwBrDbGroupId_Type = BridgeGroupIdOrZero
_IwBrDbGroupId_Object = MibTableColumn
iwBrDbGroupId = _IwBrDbGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 1),
    _IwBrDbGroupId_Type()
)
iwBrDbGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbGroupId.setStatus("current")
_IwBrDbAddress_Type = MacAddress
_IwBrDbAddress_Object = MibTableColumn
iwBrDbAddress = _IwBrDbAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 2),
    _IwBrDbAddress_Type()
)
iwBrDbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbAddress.setStatus("current")
_IwBrDbPort_Type = InterfaceIndex
_IwBrDbPort_Object = MibTableColumn
iwBrDbPort = _IwBrDbPort_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 3),
    _IwBrDbPort_Type()
)
iwBrDbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbPort.setStatus("current")


class _IwBrDbStatus_Type(Integer32):
    """Custom type iwBrDbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("learned", 3),
          ("self", 4))
    )


_IwBrDbStatus_Type.__name__ = "Integer32"
_IwBrDbStatus_Object = MibTableColumn
iwBrDbStatus = _IwBrDbStatus_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 4),
    _IwBrDbStatus_Type()
)
iwBrDbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbStatus.setStatus("current")
_IwBrDbGwMac_Type = MacAddress
_IwBrDbGwMac_Object = MibTableColumn
iwBrDbGwMac = _IwBrDbGwMac_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 5),
    _IwBrDbGwMac_Type()
)
iwBrDbGwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbGwMac.setStatus("current")


class _IwBrDbGwType_Type(Integer32):
    """Custom type iwBrDbGwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("broadcast", 1),
          ("gateway", 2))
    )


_IwBrDbGwType_Type.__name__ = "Integer32"
_IwBrDbGwType_Object = MibTableColumn
iwBrDbGwType = _IwBrDbGwType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 6),
    _IwBrDbGwType_Type()
)
iwBrDbGwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbGwType.setStatus("current")


class _IwBrDbCost_Type(Integer32):
    """Custom type iwBrDbCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrDbCost_Type.__name__ = "Integer32"
_IwBrDbCost_Object = MibTableColumn
iwBrDbCost = _IwBrDbCost_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 7),
    _IwBrDbCost_Type()
)
iwBrDbCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbCost.setStatus("current")
_IwBrDbUseCnt_Type = Counter32
_IwBrDbUseCnt_Object = MibTableColumn
iwBrDbUseCnt = _IwBrDbUseCnt_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 8),
    _IwBrDbUseCnt_Type()
)
iwBrDbUseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbUseCnt.setStatus("current")
_IwBrDbDead_Type = Gauge32
_IwBrDbDead_Object = MibTableColumn
iwBrDbDead = _IwBrDbDead_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 9),
    _IwBrDbDead_Type()
)
iwBrDbDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbDead.setStatus("current")
_IwBrDbTrunkVLANId_Type = BridgeGroupIdOrZero
_IwBrDbTrunkVLANId_Object = MibTableColumn
iwBrDbTrunkVLANId = _IwBrDbTrunkVLANId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 10),
    _IwBrDbTrunkVLANId_Type()
)
iwBrDbTrunkVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbTrunkVLANId.setStatus("current")


class _IwBrDbGroupOrder_Type(Integer32):
    """Custom type iwBrDbGroupOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_IwBrDbGroupOrder_Type.__name__ = "Integer32"
_IwBrDbGroupOrder_Object = MibTableColumn
iwBrDbGroupOrder = _IwBrDbGroupOrder_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 4, 3, 1, 11),
    _IwBrDbGroupOrder_Type()
)
iwBrDbGroupOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrDbGroupOrder.setStatus("current")
_IwBrGrp_ObjectIdentity = ObjectIdentity
iwBrGrp = _IwBrGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5)
)
_IwBrGrpTable_Object = MibTable
iwBrGrpTable = _IwBrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1)
)
if mibBuilder.loadTexts:
    iwBrGrpTable.setStatus("current")
_IwBrGrpEntry_Object = MibTableRow
iwBrGrpEntry = _IwBrGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1)
)
iwBrGrpEntry.setIndexNames(
    (0, "INFINET-BRIDGE-MIB", "iwBrGrpId"),
)
if mibBuilder.loadTexts:
    iwBrGrpEntry.setStatus("current")
_IwBrGrpId_Type = BridgeGroupIdOrZero
_IwBrGrpId_Object = MibTableColumn
iwBrGrpId = _IwBrGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 1),
    _IwBrGrpId_Type()
)
iwBrGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpId.setStatus("current")


class _IwBrGrpType_Type(Integer32):
    """Custom type iwBrGrpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("trunk", 1))
    )


_IwBrGrpType_Type.__name__ = "Integer32"
_IwBrGrpType_Object = MibTableColumn
iwBrGrpType = _IwBrGrpType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 2),
    _IwBrGrpType_Type()
)
iwBrGrpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpType.setStatus("current")


class _IwBrGrpUsChan_Type(Integer32):
    """Custom type iwBrGrpUsChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("chan1", 1),
          ("chan2", 2))
    )


_IwBrGrpUsChan_Type.__name__ = "Integer32"
_IwBrGrpUsChan_Object = MibTableColumn
iwBrGrpUsChan = _IwBrGrpUsChan_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 3),
    _IwBrGrpUsChan_Type()
)
iwBrGrpUsChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpUsChan.setStatus("current")


class _IwBrGrpDsChan_Type(Integer32):
    """Custom type iwBrGrpDsChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("chan1", 1),
          ("chan2", 2))
    )


_IwBrGrpDsChan_Type.__name__ = "Integer32"
_IwBrGrpDsChan_Object = MibTableColumn
iwBrGrpDsChan = _IwBrGrpDsChan_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 4),
    _IwBrGrpDsChan_Type()
)
iwBrGrpDsChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDsChan.setStatus("current")
_IwBrGrpInTrunk_Type = BridgeGroupIdOrZero
_IwBrGrpInTrunk_Object = MibTableColumn
iwBrGrpInTrunk = _IwBrGrpInTrunk_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 5),
    _IwBrGrpInTrunk_Type()
)
iwBrGrpInTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpInTrunk.setStatus("current")


class _IwBrGrpUncoupled_Type(Integer32):
    """Custom type iwBrGrpUncoupled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("uncoupled", 1))
    )


_IwBrGrpUncoupled_Type.__name__ = "Integer32"
_IwBrGrpUncoupled_Object = MibTableColumn
iwBrGrpUncoupled = _IwBrGrpUncoupled_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 6),
    _IwBrGrpUncoupled_Type()
)
iwBrGrpUncoupled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpUncoupled.setStatus("current")


class _IwBrGrpFlgSTP_Type(Integer32):
    """Custom type iwBrGrpFlgSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("stp", 1))
    )


_IwBrGrpFlgSTP_Type.__name__ = "Integer32"
_IwBrGrpFlgSTP_Object = MibTableColumn
iwBrGrpFlgSTP = _IwBrGrpFlgSTP_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 7),
    _IwBrGrpFlgSTP_Type()
)
iwBrGrpFlgSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpFlgSTP.setStatus("current")


class _IwBrGrpFlgIGMP_Type(Integer32):
    """Custom type iwBrGrpFlgIGMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("igmp", 1))
    )


_IwBrGrpFlgIGMP_Type.__name__ = "Integer32"
_IwBrGrpFlgIGMP_Object = MibTableColumn
iwBrGrpFlgIGMP = _IwBrGrpFlgIGMP_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 8),
    _IwBrGrpFlgIGMP_Type()
)
iwBrGrpFlgIGMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpFlgIGMP.setStatus("current")


class _IwBrGrpFlgRptr_Type(Integer32):
    """Custom type iwBrGrpFlgRptr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("repeater", 1))
    )


_IwBrGrpFlgRptr_Type.__name__ = "Integer32"
_IwBrGrpFlgRptr_Object = MibTableColumn
iwBrGrpFlgRptr = _IwBrGrpFlgRptr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 9),
    _IwBrGrpFlgRptr_Type()
)
iwBrGrpFlgRptr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpFlgRptr.setStatus("current")


class _IwBrGrpFlgAdmin_Type(Integer32):
    """Custom type iwBrGrpFlgAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("admin", 1))
    )


_IwBrGrpFlgAdmin_Type.__name__ = "Integer32"
_IwBrGrpFlgAdmin_Object = MibTableColumn
iwBrGrpFlgAdmin = _IwBrGrpFlgAdmin_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 10),
    _IwBrGrpFlgAdmin_Type()
)
iwBrGrpFlgAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpFlgAdmin.setStatus("current")


class _IwBrGrpFlgAct_Type(Integer32):
    """Custom type iwBrGrpFlgAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_IwBrGrpFlgAct_Type.__name__ = "Integer32"
_IwBrGrpFlgAct_Object = MibTableColumn
iwBrGrpFlgAct = _IwBrGrpFlgAct_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 11),
    _IwBrGrpFlgAct_Type()
)
iwBrGrpFlgAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpFlgAct.setStatus("current")


class _IwBrGrpFlgOper_Type(Integer32):
    """Custom type iwBrGrpFlgOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-operative", 0),
          ("operative", 1))
    )


_IwBrGrpFlgOper_Type.__name__ = "Integer32"
_IwBrGrpFlgOper_Object = MibTableColumn
iwBrGrpFlgOper = _IwBrGrpFlgOper_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 12),
    _IwBrGrpFlgOper_Type()
)
iwBrGrpFlgOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwBrGrpFlgOper.setStatus("current")


class _IwBrGrpInfo_Type(DisplayString):
    """Custom type iwBrGrpInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IwBrGrpInfo_Type.__name__ = "DisplayString"
_IwBrGrpInfo_Object = MibTableColumn
iwBrGrpInfo = _IwBrGrpInfo_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 13),
    _IwBrGrpInfo_Type()
)
iwBrGrpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpInfo.setStatus("current")
_IwBrGrpForwarded_Type = Counter32
_IwBrGrpForwarded_Object = MibTableColumn
iwBrGrpForwarded = _IwBrGrpForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 14),
    _IwBrGrpForwarded_Type()
)
iwBrGrpForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpForwarded.setStatus("current")
_IwBrGrpFlooded_Type = Counter32
_IwBrGrpFlooded_Object = MibTableColumn
iwBrGrpFlooded = _IwBrGrpFlooded_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 15),
    _IwBrGrpFlooded_Type()
)
iwBrGrpFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpFlooded.setStatus("current")
_IwBrGrpDropSTPL_Type = Counter32
_IwBrGrpDropSTPL_Object = MibTableColumn
iwBrGrpDropSTPL = _IwBrGrpDropSTPL_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 16),
    _IwBrGrpDropSTPL_Type()
)
iwBrGrpDropSTPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropSTPL.setStatus("current")
_IwBrGrpDropUNRD_Type = Counter32
_IwBrGrpDropUNRD_Object = MibTableColumn
iwBrGrpDropUNRD = _IwBrGrpDropUNRD_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 17),
    _IwBrGrpDropUNRD_Type()
)
iwBrGrpDropUNRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropUNRD.setStatus("current")
_IwBrGrpDropFWRL_Type = Counter32
_IwBrGrpDropFWRL_Object = MibTableColumn
iwBrGrpDropFWRL = _IwBrGrpDropFWRL_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 18),
    _IwBrGrpDropFWRL_Type()
)
iwBrGrpDropFWRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropFWRL.setStatus("current")
_IwBrGrpDropLOOP_Type = Counter32
_IwBrGrpDropLOOP_Object = MibTableColumn
iwBrGrpDropLOOP = _IwBrGrpDropLOOP_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 19),
    _IwBrGrpDropLOOP_Type()
)
iwBrGrpDropLOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropLOOP.setStatus("current")
_IwBrGrpDropNOBG_Type = Counter32
_IwBrGrpDropNOBG_Object = MibTableColumn
iwBrGrpDropNOBG = _IwBrGrpDropNOBG_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 20),
    _IwBrGrpDropNOBG_Type()
)
iwBrGrpDropNOBG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropNOBG.setStatus("current")
_IwBrGrpDropLCNA_Type = Counter32
_IwBrGrpDropLCNA_Object = MibTableColumn
iwBrGrpDropLCNA = _IwBrGrpDropLCNA_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 21),
    _IwBrGrpDropLCNA_Type()
)
iwBrGrpDropLCNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropLCNA.setStatus("current")
_IwBrGrpDropJOIN_Type = Counter32
_IwBrGrpDropJOIN_Object = MibTableColumn
iwBrGrpDropJOIN = _IwBrGrpDropJOIN_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 22),
    _IwBrGrpDropJOIN_Type()
)
iwBrGrpDropJOIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropJOIN.setStatus("current")
_IwBrGrpDropSDPS_Type = Counter32
_IwBrGrpDropSDPS_Object = MibTableColumn
iwBrGrpDropSDPS = _IwBrGrpDropSDPS_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 23),
    _IwBrGrpDropSDPS_Type()
)
iwBrGrpDropSDPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDropSDPS.setStatus("current")
_IwBrGrpStpRoot_Type = BridgeId
_IwBrGrpStpRoot_Object = MibTableColumn
iwBrGrpStpRoot = _IwBrGrpStpRoot_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 24),
    _IwBrGrpStpRoot_Type()
)
iwBrGrpStpRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpStpRoot.setStatus("current")


class _IwBrGrpStpRootPort_Type(Integer32):
    """Custom type iwBrGrpStpRootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrGrpStpRootPort_Type.__name__ = "Integer32"
_IwBrGrpStpRootPort_Object = MibTableColumn
iwBrGrpStpRootPort = _IwBrGrpStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 25),
    _IwBrGrpStpRootPort_Type()
)
iwBrGrpStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpStpRootPort.setStatus("current")


class _IwBrPortStpPVer_Type(Integer32):
    """Custom type iwBrPortStpPVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("rstp", 2))
    )


_IwBrPortStpPVer_Type.__name__ = "Integer32"
_IwBrPortStpPVer_Object = MibTableColumn
iwBrPortStpPVer = _IwBrPortStpPVer_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 26),
    _IwBrPortStpPVer_Type()
)
iwBrPortStpPVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrPortStpPVer.setStatus("current")


class _IwBrGrpDefaultAction_Type(Integer32):
    """Custom type iwBrGrpDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IwBrGrpDefaultAction_Type.__name__ = "Integer32"
_IwBrGrpDefaultAction_Object = MibTableColumn
iwBrGrpDefaultAction = _IwBrGrpDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 27),
    _IwBrGrpDefaultAction_Type()
)
iwBrGrpDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpDefaultAction.setStatus("current")


class _IwBrGrpXVlan_Type(Integer32):
    """Custom type iwBrGrpXVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xvlan", 1),
          ("unset", 2))
    )


_IwBrGrpXVlan_Type.__name__ = "Integer32"
_IwBrGrpXVlan_Object = MibTableColumn
iwBrGrpXVlan = _IwBrGrpXVlan_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 28),
    _IwBrGrpXVlan_Type()
)
iwBrGrpXVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpXVlan.setStatus("current")


class _IwBrGrpPermittedVLAN_Type(Integer32):
    """Custom type iwBrGrpPermittedVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4095, 2147483647),
    )


_IwBrGrpPermittedVLAN_Type.__name__ = "Integer32"
_IwBrGrpPermittedVLAN_Object = MibTableColumn
iwBrGrpPermittedVLAN = _IwBrGrpPermittedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 5, 1, 1, 29),
    _IwBrGrpPermittedVLAN_Type()
)
iwBrGrpPermittedVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrGrpPermittedVLAN.setStatus("current")
_IwBrRules_ObjectIdentity = ObjectIdentity
iwBrRules = _IwBrRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6)
)
_IwBrRuleTable_Object = MibTable
iwBrRuleTable = _IwBrRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    iwBrRuleTable.setStatus("current")
_IwBrRuleEntry_Object = MibTableRow
iwBrRuleEntry = _IwBrRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1)
)
iwBrRuleEntry.setIndexNames(
    (0, "INFINET-BRIDGE-MIB", "iwBrRuleGrpId"),
    (0, "INFINET-BRIDGE-MIB", "iwBrRulePriority"),
)
if mibBuilder.loadTexts:
    iwBrRuleEntry.setStatus("current")


class _IwBrRuleGrpId_Type(Integer32):
    """Custom type iwBrRuleGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_IwBrRuleGrpId_Type.__name__ = "Integer32"
_IwBrRuleGrpId_Object = MibTableColumn
iwBrRuleGrpId = _IwBrRuleGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 1),
    _IwBrRuleGrpId_Type()
)
iwBrRuleGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleGrpId.setStatus("current")


class _IwBrRulePriority_Type(Integer32):
    """Custom type iwBrRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IwBrRulePriority_Type.__name__ = "Integer32"
_IwBrRulePriority_Object = MibTableColumn
iwBrRulePriority = _IwBrRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 2),
    _IwBrRulePriority_Type()
)
iwBrRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRulePriority.setStatus("current")


class _IwBrRuleAction_Type(Integer32):
    """Custom type iwBrRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IwBrRuleAction_Type.__name__ = "Integer32"
_IwBrRuleAction_Object = MibTableColumn
iwBrRuleAction = _IwBrRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 3),
    _IwBrRuleAction_Type()
)
iwBrRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleAction.setStatus("current")


class _IwBrRuleMatchList_Type(Integer32):
    """Custom type iwBrRuleMatchList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrRuleMatchList_Type.__name__ = "Integer32"
_IwBrRuleMatchList_Object = MibTableColumn
iwBrRuleMatchList = _IwBrRuleMatchList_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 4),
    _IwBrRuleMatchList_Type()
)
iwBrRuleMatchList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleMatchList.setStatus("current")


class _IwBrRuleVlanList_Type(Integer32):
    """Custom type iwBrRuleVlanList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrRuleVlanList_Type.__name__ = "Integer32"
_IwBrRuleVlanList_Object = MibTableColumn
iwBrRuleVlanList = _IwBrRuleVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 5),
    _IwBrRuleVlanList_Type()
)
iwBrRuleVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleVlanList.setStatus("current")


class _IwBrRuleIfaceList_Type(Integer32):
    """Custom type iwBrRuleIfaceList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrRuleIfaceList_Type.__name__ = "Integer32"
_IwBrRuleIfaceList_Object = MibTableColumn
iwBrRuleIfaceList = _IwBrRuleIfaceList_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 6),
    _IwBrRuleIfaceList_Type()
)
iwBrRuleIfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleIfaceList.setStatus("current")


class _IwBrRuleSrcList_Type(Integer32):
    """Custom type iwBrRuleSrcList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrRuleSrcList_Type.__name__ = "Integer32"
_IwBrRuleSrcList_Object = MibTableColumn
iwBrRuleSrcList = _IwBrRuleSrcList_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 7),
    _IwBrRuleSrcList_Type()
)
iwBrRuleSrcList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleSrcList.setStatus("current")


class _IwBrRuleDstList_Type(Integer32):
    """Custom type iwBrRuleDstList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrRuleDstList_Type.__name__ = "Integer32"
_IwBrRuleDstList_Object = MibTableColumn
iwBrRuleDstList = _IwBrRuleDstList_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 8),
    _IwBrRuleDstList_Type()
)
iwBrRuleDstList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleDstList.setStatus("current")


class _IwBrRuleProtoList_Type(Integer32):
    """Custom type iwBrRuleProtoList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IwBrRuleProtoList_Type.__name__ = "Integer32"
_IwBrRuleProtoList_Object = MibTableColumn
iwBrRuleProtoList = _IwBrRuleProtoList_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 1, 1, 9),
    _IwBrRuleProtoList_Type()
)
iwBrRuleProtoList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrRuleProtoList.setStatus("current")
_IwBrListTable_Object = MibTable
iwBrListTable = _IwBrListTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 2)
)
if mibBuilder.loadTexts:
    iwBrListTable.setStatus("current")
_IwBrListEntry_Object = MibTableRow
iwBrListEntry = _IwBrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 2, 1)
)
iwBrListEntry.setIndexNames(
    (0, "INFINET-BRIDGE-MIB", "iwBrListId"),
)
if mibBuilder.loadTexts:
    iwBrListEntry.setStatus("current")


class _IwBrListId_Type(Integer32):
    """Custom type iwBrListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IwBrListId_Type.__name__ = "Integer32"
_IwBrListId_Object = MibTableColumn
iwBrListId = _IwBrListId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 2, 1, 1),
    _IwBrListId_Type()
)
iwBrListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrListId.setStatus("current")


class _IwBrListType_Type(Integer32):
    """Custom type iwBrListType based on Integer32"""
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
        *(("iface", 1),
          ("mac", 2),
          ("numrange", 3),
          ("match", 4))
    )


_IwBrListType_Type.__name__ = "Integer32"
_IwBrListType_Object = MibTableColumn
iwBrListType = _IwBrListType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 2, 1, 2),
    _IwBrListType_Type()
)
iwBrListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrListType.setStatus("current")


class _IwBrListName_Type(DisplayString):
    """Custom type iwBrListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IwBrListName_Type.__name__ = "DisplayString"
_IwBrListName_Object = MibTableColumn
iwBrListName = _IwBrListName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 2, 1, 3),
    _IwBrListName_Type()
)
iwBrListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrListName.setStatus("current")
_IwBrListValues_Type = DisplayString
_IwBrListValues_Object = MibTableColumn
iwBrListValues = _IwBrListValues_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 6, 2, 1, 4),
    _IwBrListValues_Type()
)
iwBrListValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrListValues.setStatus("current")
_IwBrBlackList_ObjectIdentity = ObjectIdentity
iwBrBlackList = _IwBrBlackList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7)
)
_IwBrBlackListTable_Object = MibTable
iwBrBlackListTable = _IwBrBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7, 1)
)
if mibBuilder.loadTexts:
    iwBrBlackListTable.setStatus("current")
_IwBrBlackListEntry_Object = MibTableRow
iwBrBlackListEntry = _IwBrBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7, 1, 1)
)
iwBrBlackListEntry.setIndexNames(
    (0, "INFINET-BRIDGE-MIB", "iwBrBlackListGrpId"),
    (0, "INFINET-BRIDGE-MIB", "iwBrBlackListDstMac"),
)
if mibBuilder.loadTexts:
    iwBrBlackListEntry.setStatus("current")


class _IwBrBlackListGrpId_Type(Integer32):
    """Custom type iwBrBlackListGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_IwBrBlackListGrpId_Type.__name__ = "Integer32"
_IwBrBlackListGrpId_Object = MibTableColumn
iwBrBlackListGrpId = _IwBrBlackListGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7, 1, 1, 1),
    _IwBrBlackListGrpId_Type()
)
iwBrBlackListGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBlackListGrpId.setStatus("current")
_IwBrBlackListDstMac_Type = MacAddress
_IwBrBlackListDstMac_Object = MibTableColumn
iwBrBlackListDstMac = _IwBrBlackListDstMac_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7, 1, 1, 2),
    _IwBrBlackListDstMac_Type()
)
iwBrBlackListDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBlackListDstMac.setStatus("current")
_IwBrBlackListSrcMac_Type = MacAddress
_IwBrBlackListSrcMac_Object = MibTableColumn
iwBrBlackListSrcMac = _IwBrBlackListSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7, 1, 1, 3),
    _IwBrBlackListSrcMac_Type()
)
iwBrBlackListSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBlackListSrcMac.setStatus("current")


class _IwBrBlackListTime_Type(Unsigned32):
    """Custom type iwBrBlackListTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IwBrBlackListTime_Type.__name__ = "Unsigned32"
_IwBrBlackListTime_Object = MibTableColumn
iwBrBlackListTime = _IwBrBlackListTime_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 1, 7, 1, 1, 4),
    _IwBrBlackListTime_Type()
)
iwBrBlackListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwBrBlackListTime.setStatus("current")
_IwBrMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
iwBrMIBNotificationsPrefix = _IwBrMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 2)
)
_IwBrMIBNotifications_ObjectIdentity = ObjectIdentity
iwBrMIBNotifications = _IwBrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 2, 0)
)
_IwBrMIBConformance_ObjectIdentity = ObjectIdentity
iwBrMIBConformance = _IwBrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 3)
)

# Managed Objects groups

iwBrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 8, 3, 2)
)
iwBrMIBGroup.setObjects(
      *(("INFINET-BRIDGE-MIB", "iwBrBaseAddress"),
        ("INFINET-BRIDGE-MIB", "iwBrBasePorts"),
        ("INFINET-BRIDGE-MIB", "iwBrBaseType"),
        ("INFINET-BRIDGE-MIB", "iwBrLocalTag"),
        ("INFINET-BRIDGE-MIB", "iwBrStpProtoSpec"),
        ("INFINET-BRIDGE-MIB", "iwBrStpPriority"),
        ("INFINET-BRIDGE-MIB", "iwBrStpTimeSinceTopoChange"),
        ("INFINET-BRIDGE-MIB", "iwBrStpTopChanges"),
        ("INFINET-BRIDGE-MIB", "iwBrStpMaxAge"),
        ("INFINET-BRIDGE-MIB", "iwBrStpHelloTime"),
        ("INFINET-BRIDGE-MIB", "iwBrStpHoldTime"),
        ("INFINET-BRIDGE-MIB", "iwBrStpForwardDelay"),
        ("INFINET-BRIDGE-MIB", "iwBrStpBridgeMaxAge"),
        ("INFINET-BRIDGE-MIB", "iwBrStpBridgeHelloTime"),
        ("INFINET-BRIDGE-MIB", "iwBrStpBridgeForwardDelay"),
        ("INFINET-BRIDGE-MIB", "iwBrPortGrpId"),
        ("INFINET-BRIDGE-MIB", "iwBrPortId"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpPrio"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpState"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpRole"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpDesCost"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpDesBridge"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpDesPort"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpFwdTransitions"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpPathCost32"),
        ("INFINET-BRIDGE-MIB", "iwBrPortVlanAlteration"),
        ("INFINET-BRIDGE-MIB", "iwBrDbEntryDiscards"),
        ("INFINET-BRIDGE-MIB", "iwBrDbAgingTime"),
        ("INFINET-BRIDGE-MIB", "iwBrDbGroupId"),
        ("INFINET-BRIDGE-MIB", "iwBrDbAddress"),
        ("INFINET-BRIDGE-MIB", "iwBrDbPort"),
        ("INFINET-BRIDGE-MIB", "iwBrDbStatus"),
        ("INFINET-BRIDGE-MIB", "iwBrDbGwMac"),
        ("INFINET-BRIDGE-MIB", "iwBrDbGwType"),
        ("INFINET-BRIDGE-MIB", "iwBrDbCost"),
        ("INFINET-BRIDGE-MIB", "iwBrDbUseCnt"),
        ("INFINET-BRIDGE-MIB", "iwBrDbDead"),
        ("INFINET-BRIDGE-MIB", "iwBrDbTrunkVLANId"),
        ("INFINET-BRIDGE-MIB", "iwBrDbGroupOrder"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpId"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpType"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpUsChan"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDsChan"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpInTrunk"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpUncoupled"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlgSTP"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlgIGMP"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlgRptr"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlgAdmin"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlgAct"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlgOper"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpInfo"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpForwarded"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpFlooded"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropSTPL"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropUNRD"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropFWRL"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropLOOP"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropNOBG"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropLCNA"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropJOIN"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDropSDPS"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpStpRoot"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpStpRootPort"),
        ("INFINET-BRIDGE-MIB", "iwBrPortStpPVer"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpDefaultAction"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpXVlan"),
        ("INFINET-BRIDGE-MIB", "iwBrGrpPermittedVLAN"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleGrpId"),
        ("INFINET-BRIDGE-MIB", "iwBrRulePriority"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleAction"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleMatchList"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleVlanList"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleIfaceList"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleSrcList"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleDstList"),
        ("INFINET-BRIDGE-MIB", "iwBrRuleProtoList"),
        ("INFINET-BRIDGE-MIB", "iwBrListId"),
        ("INFINET-BRIDGE-MIB", "iwBrListType"),
        ("INFINET-BRIDGE-MIB", "iwBrListName"),
        ("INFINET-BRIDGE-MIB", "iwBrListValues"),
        ("INFINET-BRIDGE-MIB", "iwBrBlackListGrpId"),
        ("INFINET-BRIDGE-MIB", "iwBrBlackListDstMac"),
        ("INFINET-BRIDGE-MIB", "iwBrBlackListSrcMac"),
        ("INFINET-BRIDGE-MIB", "iwBrBlackListTime"))
)
if mibBuilder.loadTexts:
    iwBrMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-BRIDGE-MIB",
    **{"BridgeId": BridgeId,
       "Timeout": Timeout,
       "BridgeGroupIdOrZero": BridgeGroupIdOrZero,
       "iwBrMIB": iwBrMIB,
       "iwBrMIBObjects": iwBrMIBObjects,
       "iwBrBase": iwBrBase,
       "iwBrBaseAddress": iwBrBaseAddress,
       "iwBrBasePorts": iwBrBasePorts,
       "iwBrBaseType": iwBrBaseType,
       "iwBrLocalTag": iwBrLocalTag,
       "iwBrStp": iwBrStp,
       "iwBrStpProtoSpec": iwBrStpProtoSpec,
       "iwBrStpPriority": iwBrStpPriority,
       "iwBrStpTimeSinceTopoChange": iwBrStpTimeSinceTopoChange,
       "iwBrStpTopChanges": iwBrStpTopChanges,
       "iwBrStpMaxAge": iwBrStpMaxAge,
       "iwBrStpHelloTime": iwBrStpHelloTime,
       "iwBrStpHoldTime": iwBrStpHoldTime,
       "iwBrStpForwardDelay": iwBrStpForwardDelay,
       "iwBrStpBridgeMaxAge": iwBrStpBridgeMaxAge,
       "iwBrStpBridgeHelloTime": iwBrStpBridgeHelloTime,
       "iwBrStpBridgeForwardDelay": iwBrStpBridgeForwardDelay,
       "iwBrPorts": iwBrPorts,
       "iwBrPortTable": iwBrPortTable,
       "iwBrPortEntry": iwBrPortEntry,
       "iwBrPortGrpId": iwBrPortGrpId,
       "iwBrPortId": iwBrPortId,
       "iwBrPortStpPrio": iwBrPortStpPrio,
       "iwBrPortStpState": iwBrPortStpState,
       "iwBrPortStpRole": iwBrPortStpRole,
       "iwBrPortStpDesCost": iwBrPortStpDesCost,
       "iwBrPortStpDesBridge": iwBrPortStpDesBridge,
       "iwBrPortStpDesPort": iwBrPortStpDesPort,
       "iwBrPortStpFwdTransitions": iwBrPortStpFwdTransitions,
       "iwBrPortStpPathCost32": iwBrPortStpPathCost32,
       "iwBrPortVlanAlteration": iwBrPortVlanAlteration,
       "iwBrDb": iwBrDb,
       "iwBrDbEntryDiscards": iwBrDbEntryDiscards,
       "iwBrDbAgingTime": iwBrDbAgingTime,
       "iwBrDbTable": iwBrDbTable,
       "iwBrDbEntry": iwBrDbEntry,
       "iwBrDbGroupId": iwBrDbGroupId,
       "iwBrDbAddress": iwBrDbAddress,
       "iwBrDbPort": iwBrDbPort,
       "iwBrDbStatus": iwBrDbStatus,
       "iwBrDbGwMac": iwBrDbGwMac,
       "iwBrDbGwType": iwBrDbGwType,
       "iwBrDbCost": iwBrDbCost,
       "iwBrDbUseCnt": iwBrDbUseCnt,
       "iwBrDbDead": iwBrDbDead,
       "iwBrDbTrunkVLANId": iwBrDbTrunkVLANId,
       "iwBrDbGroupOrder": iwBrDbGroupOrder,
       "iwBrGrp": iwBrGrp,
       "iwBrGrpTable": iwBrGrpTable,
       "iwBrGrpEntry": iwBrGrpEntry,
       "iwBrGrpId": iwBrGrpId,
       "iwBrGrpType": iwBrGrpType,
       "iwBrGrpUsChan": iwBrGrpUsChan,
       "iwBrGrpDsChan": iwBrGrpDsChan,
       "iwBrGrpInTrunk": iwBrGrpInTrunk,
       "iwBrGrpUncoupled": iwBrGrpUncoupled,
       "iwBrGrpFlgSTP": iwBrGrpFlgSTP,
       "iwBrGrpFlgIGMP": iwBrGrpFlgIGMP,
       "iwBrGrpFlgRptr": iwBrGrpFlgRptr,
       "iwBrGrpFlgAdmin": iwBrGrpFlgAdmin,
       "iwBrGrpFlgAct": iwBrGrpFlgAct,
       "iwBrGrpFlgOper": iwBrGrpFlgOper,
       "iwBrGrpInfo": iwBrGrpInfo,
       "iwBrGrpForwarded": iwBrGrpForwarded,
       "iwBrGrpFlooded": iwBrGrpFlooded,
       "iwBrGrpDropSTPL": iwBrGrpDropSTPL,
       "iwBrGrpDropUNRD": iwBrGrpDropUNRD,
       "iwBrGrpDropFWRL": iwBrGrpDropFWRL,
       "iwBrGrpDropLOOP": iwBrGrpDropLOOP,
       "iwBrGrpDropNOBG": iwBrGrpDropNOBG,
       "iwBrGrpDropLCNA": iwBrGrpDropLCNA,
       "iwBrGrpDropJOIN": iwBrGrpDropJOIN,
       "iwBrGrpDropSDPS": iwBrGrpDropSDPS,
       "iwBrGrpStpRoot": iwBrGrpStpRoot,
       "iwBrGrpStpRootPort": iwBrGrpStpRootPort,
       "iwBrPortStpPVer": iwBrPortStpPVer,
       "iwBrGrpDefaultAction": iwBrGrpDefaultAction,
       "iwBrGrpXVlan": iwBrGrpXVlan,
       "iwBrGrpPermittedVLAN": iwBrGrpPermittedVLAN,
       "iwBrRules": iwBrRules,
       "iwBrRuleTable": iwBrRuleTable,
       "iwBrRuleEntry": iwBrRuleEntry,
       "iwBrRuleGrpId": iwBrRuleGrpId,
       "iwBrRulePriority": iwBrRulePriority,
       "iwBrRuleAction": iwBrRuleAction,
       "iwBrRuleMatchList": iwBrRuleMatchList,
       "iwBrRuleVlanList": iwBrRuleVlanList,
       "iwBrRuleIfaceList": iwBrRuleIfaceList,
       "iwBrRuleSrcList": iwBrRuleSrcList,
       "iwBrRuleDstList": iwBrRuleDstList,
       "iwBrRuleProtoList": iwBrRuleProtoList,
       "iwBrListTable": iwBrListTable,
       "iwBrListEntry": iwBrListEntry,
       "iwBrListId": iwBrListId,
       "iwBrListType": iwBrListType,
       "iwBrListName": iwBrListName,
       "iwBrListValues": iwBrListValues,
       "iwBrBlackList": iwBrBlackList,
       "iwBrBlackListTable": iwBrBlackListTable,
       "iwBrBlackListEntry": iwBrBlackListEntry,
       "iwBrBlackListGrpId": iwBrBlackListGrpId,
       "iwBrBlackListDstMac": iwBrBlackListDstMac,
       "iwBrBlackListSrcMac": iwBrBlackListSrcMac,
       "iwBrBlackListTime": iwBrBlackListTime,
       "iwBrMIBNotificationsPrefix": iwBrMIBNotificationsPrefix,
       "iwBrMIBNotifications": iwBrMIBNotifications,
       "iwBrMIBConformance": iwBrMIBConformance,
       "iwBrMIBGroup": iwBrMIBGroup}
)
