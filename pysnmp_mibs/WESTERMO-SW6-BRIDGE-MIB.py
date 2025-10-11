# SNMP MIB module (WESTERMO-SW6-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-SW6-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:25 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8)
)
if mibBuilder.loadTexts:
    rstp.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1)
)
_CfgRstpBridge_ObjectIdentity = ObjectIdentity
cfgRstpBridge = _CfgRstpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1)
)


class _CfgRstpBridgeEnabled_Type(Integer32):
    """Custom type cfgRstpBridgeEnabled based on Integer32"""
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


_CfgRstpBridgeEnabled_Type.__name__ = "Integer32"
_CfgRstpBridgeEnabled_Object = MibScalar
cfgRstpBridgeEnabled = _CfgRstpBridgeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1, 1),
    _CfgRstpBridgeEnabled_Type()
)
cfgRstpBridgeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpBridgeEnabled.setStatus("current")


class _CfgRstpBridgePriority_Type(Integer32):
    """Custom type cfgRstpBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_CfgRstpBridgePriority_Type.__name__ = "Integer32"
_CfgRstpBridgePriority_Object = MibScalar
cfgRstpBridgePriority = _CfgRstpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1, 2),
    _CfgRstpBridgePriority_Type()
)
cfgRstpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpBridgePriority.setStatus("current")


class _CfgRstpBridgeHelloTime_Type(Integer32):
    """Custom type cfgRstpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_CfgRstpBridgeHelloTime_Type.__name__ = "Integer32"
_CfgRstpBridgeHelloTime_Object = MibScalar
cfgRstpBridgeHelloTime = _CfgRstpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1, 3),
    _CfgRstpBridgeHelloTime_Type()
)
cfgRstpBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRstpBridgeHelloTime.setStatus("current")


class _CfgRstpBridgeForwardDelay_Type(Integer32):
    """Custom type cfgRstpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_CfgRstpBridgeForwardDelay_Type.__name__ = "Integer32"
_CfgRstpBridgeForwardDelay_Object = MibScalar
cfgRstpBridgeForwardDelay = _CfgRstpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1, 4),
    _CfgRstpBridgeForwardDelay_Type()
)
cfgRstpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpBridgeForwardDelay.setStatus("current")


class _CfgRstpBridgeMaxAge_Type(Integer32):
    """Custom type cfgRstpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_CfgRstpBridgeMaxAge_Type.__name__ = "Integer32"
_CfgRstpBridgeMaxAge_Object = MibScalar
cfgRstpBridgeMaxAge = _CfgRstpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1, 5),
    _CfgRstpBridgeMaxAge_Type()
)
cfgRstpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpBridgeMaxAge.setStatus("current")


class _CfgRstpBridgeTransmitHoldCount_Type(Integer32):
    """Custom type cfgRstpBridgeTransmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CfgRstpBridgeTransmitHoldCount_Type.__name__ = "Integer32"
_CfgRstpBridgeTransmitHoldCount_Object = MibScalar
cfgRstpBridgeTransmitHoldCount = _CfgRstpBridgeTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 1, 6),
    _CfgRstpBridgeTransmitHoldCount_Type()
)
cfgRstpBridgeTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpBridgeTransmitHoldCount.setStatus("current")
_CfgRstpPort_ObjectIdentity = ObjectIdentity
cfgRstpPort = _CfgRstpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2)
)
_CfgRstpPortTable_Object = MibTable
cfgRstpPortTable = _CfgRstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfgRstpPortTable.setStatus("current")
_CfgRstpPortTableEntry_Object = MibTableRow
cfgRstpPortTableEntry = _CfgRstpPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1)
)
cfgRstpPortTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-BRIDGE-MIB", "cfgRstpPortIndex"),
)
if mibBuilder.loadTexts:
    cfgRstpPortTableEntry.setStatus("current")


class _CfgRstpPortIndex_Type(Integer32):
    """Custom type cfgRstpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_CfgRstpPortIndex_Type.__name__ = "Integer32"
_CfgRstpPortIndex_Object = MibTableColumn
cfgRstpPortIndex = _CfgRstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1, 1),
    _CfgRstpPortIndex_Type()
)
cfgRstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgRstpPortIndex.setStatus("current")


class _CfgRstpPortEnabled_Type(Integer32):
    """Custom type cfgRstpPortEnabled based on Integer32"""
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


_CfgRstpPortEnabled_Type.__name__ = "Integer32"
_CfgRstpPortEnabled_Object = MibTableColumn
cfgRstpPortEnabled = _CfgRstpPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1, 2),
    _CfgRstpPortEnabled_Type()
)
cfgRstpPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpPortEnabled.setStatus("current")


class _CfgRstpPortName_Type(DisplayString):
    """Custom type cfgRstpPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgRstpPortName_Type.__name__ = "DisplayString"
_CfgRstpPortName_Object = MibTableColumn
cfgRstpPortName = _CfgRstpPortName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1, 3),
    _CfgRstpPortName_Type()
)
cfgRstpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRstpPortName.setStatus("current")


class _CfgRstpPortPriority_Type(Integer32):
    """Custom type cfgRstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_CfgRstpPortPriority_Type.__name__ = "Integer32"
_CfgRstpPortPriority_Object = MibTableColumn
cfgRstpPortPriority = _CfgRstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1, 4),
    _CfgRstpPortPriority_Type()
)
cfgRstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpPortPriority.setStatus("current")


class _CfgRstpPortPathCost_Type(Integer32):
    """Custom type cfgRstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5000000),
    )


_CfgRstpPortPathCost_Type.__name__ = "Integer32"
_CfgRstpPortPathCost_Object = MibTableColumn
cfgRstpPortPathCost = _CfgRstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1, 5),
    _CfgRstpPortPathCost_Type()
)
cfgRstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpPortPathCost.setStatus("current")


class _CfgRstpPortAutoEdge_Type(Integer32):
    """Custom type cfgRstpPortAutoEdge based on Integer32"""
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


_CfgRstpPortAutoEdge_Type.__name__ = "Integer32"
_CfgRstpPortAutoEdge_Object = MibTableColumn
cfgRstpPortAutoEdge = _CfgRstpPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 1, 2, 1, 1, 6),
    _CfgRstpPortAutoEdge_Type()
)
cfgRstpPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRstpPortAutoEdge.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 10000)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 10000, 1)
)
_GroupConfiguration_ObjectIdentity = ObjectIdentity
groupConfiguration = _GroupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 10000, 1, 1)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 10000, 2)
)

# Managed Objects groups

groupConfigRstp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 10000, 1, 1, 1)
)
groupConfigRstp.setObjects(
      *(("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpBridgeEnabled"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpBridgePriority"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpBridgeHelloTime"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpBridgeForwardDelay"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpBridgeMaxAge"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpBridgeTransmitHoldCount"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpPortEnabled"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpPortName"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpPortPriority"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpPortPathCost"),
        ("WESTERMO-SW6-BRIDGE-MIB", "cfgRstpPortAutoEdge"))
)
if mibBuilder.loadTexts:
    groupConfigRstp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 8, 10000, 2, 1)
)
compliance.setObjects(
    ("WESTERMO-SW6-BRIDGE-MIB", "groupConfigRstp")
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-SW6-BRIDGE-MIB",
    **{"rstp": rstp,
       "configuration": configuration,
       "cfgRstpBridge": cfgRstpBridge,
       "cfgRstpBridgeEnabled": cfgRstpBridgeEnabled,
       "cfgRstpBridgePriority": cfgRstpBridgePriority,
       "cfgRstpBridgeHelloTime": cfgRstpBridgeHelloTime,
       "cfgRstpBridgeForwardDelay": cfgRstpBridgeForwardDelay,
       "cfgRstpBridgeMaxAge": cfgRstpBridgeMaxAge,
       "cfgRstpBridgeTransmitHoldCount": cfgRstpBridgeTransmitHoldCount,
       "cfgRstpPort": cfgRstpPort,
       "cfgRstpPortTable": cfgRstpPortTable,
       "cfgRstpPortTableEntry": cfgRstpPortTableEntry,
       "cfgRstpPortIndex": cfgRstpPortIndex,
       "cfgRstpPortEnabled": cfgRstpPortEnabled,
       "cfgRstpPortName": cfgRstpPortName,
       "cfgRstpPortPriority": cfgRstpPortPriority,
       "cfgRstpPortPathCost": cfgRstpPortPathCost,
       "cfgRstpPortAutoEdge": cfgRstpPortAutoEdge,
       "conformance": conformance,
       "groups": groups,
       "groupConfiguration": groupConfiguration,
       "groupConfigRstp": groupConfigRstp,
       "compliances": compliances,
       "compliance": compliance}
)
