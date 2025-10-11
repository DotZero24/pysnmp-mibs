# SNMP MIB module (G6-STP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-STP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:16 2025
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

_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42)
)
_BridgeConfigTable_Object = MibTable
bridgeConfigTable = _BridgeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1)
)
if mibBuilder.loadTexts:
    bridgeConfigTable.setStatus("current")
_BridgeConfigEntry_Object = MibTableRow
bridgeConfigEntry = _BridgeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1)
)
bridgeConfigEntry.setIndexNames(
    (0, "G6-STP-MIB", "bridgeConfigIndex"),
)
if mibBuilder.loadTexts:
    bridgeConfigEntry.setStatus("current")


class _BridgeConfigIndex_Type(Integer32):
    """Custom type bridgeConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_BridgeConfigIndex_Type.__name__ = "Integer32"
_BridgeConfigIndex_Object = MibTableColumn
bridgeConfigIndex = _BridgeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 1),
    _BridgeConfigIndex_Type()
)
bridgeConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeConfigIndex.setStatus("current")


class _BridgeConfigMode_Type(Integer32):
    """Custom type bridgeConfigMode based on Integer32"""
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
          ("stp", 1),
          ("rstp", 2),
          ("mstp", 3))
    )


_BridgeConfigMode_Type.__name__ = "Integer32"
_BridgeConfigMode_Object = MibTableColumn
bridgeConfigMode = _BridgeConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 2),
    _BridgeConfigMode_Type()
)
bridgeConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigMode.setStatus("current")


class _BridgeConfigPriority_Type(Integer32):
    """Custom type bridgeConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigPriority_Type.__name__ = "Integer32"
_BridgeConfigPriority_Object = MibTableColumn
bridgeConfigPriority = _BridgeConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 3),
    _BridgeConfigPriority_Type()
)
bridgeConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigPriority.setStatus("current")


class _BridgeConfigHelloTime_Type(Integer32):
    """Custom type bridgeConfigHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigHelloTime_Type.__name__ = "Integer32"
_BridgeConfigHelloTime_Object = MibTableColumn
bridgeConfigHelloTime = _BridgeConfigHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 4),
    _BridgeConfigHelloTime_Type()
)
bridgeConfigHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigHelloTime.setStatus("current")


class _BridgeConfigMaxAge_Type(Integer32):
    """Custom type bridgeConfigMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigMaxAge_Type.__name__ = "Integer32"
_BridgeConfigMaxAge_Object = MibTableColumn
bridgeConfigMaxAge = _BridgeConfigMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 5),
    _BridgeConfigMaxAge_Type()
)
bridgeConfigMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigMaxAge.setStatus("current")


class _BridgeConfigForwardDelay_Type(Integer32):
    """Custom type bridgeConfigForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigForwardDelay_Type.__name__ = "Integer32"
_BridgeConfigForwardDelay_Object = MibTableColumn
bridgeConfigForwardDelay = _BridgeConfigForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 6),
    _BridgeConfigForwardDelay_Type()
)
bridgeConfigForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigForwardDelay.setStatus("current")


class _BridgeConfigTxHoldCount_Type(Integer32):
    """Custom type bridgeConfigTxHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigTxHoldCount_Type.__name__ = "Integer32"
_BridgeConfigTxHoldCount_Object = MibTableColumn
bridgeConfigTxHoldCount = _BridgeConfigTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 7),
    _BridgeConfigTxHoldCount_Type()
)
bridgeConfigTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigTxHoldCount.setStatus("current")


class _BridgeConfigIeeePathCostModel_Type(Integer32):
    """Custom type bridgeConfigIeeePathCostModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ms1998Compliant", 0),
          ("ms2004Compliant", 1))
    )


_BridgeConfigIeeePathCostModel_Type.__name__ = "Integer32"
_BridgeConfigIeeePathCostModel_Object = MibTableColumn
bridgeConfigIeeePathCostModel = _BridgeConfigIeeePathCostModel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 8),
    _BridgeConfigIeeePathCostModel_Type()
)
bridgeConfigIeeePathCostModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigIeeePathCostModel.setStatus("current")
_BridgeConfigMstpRegionName_Type = DisplayString
_BridgeConfigMstpRegionName_Object = MibTableColumn
bridgeConfigMstpRegionName = _BridgeConfigMstpRegionName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 9),
    _BridgeConfigMstpRegionName_Type()
)
bridgeConfigMstpRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigMstpRegionName.setStatus("current")


class _BridgeConfigMstpRevisionLevel_Type(Integer32):
    """Custom type bridgeConfigMstpRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigMstpRevisionLevel_Type.__name__ = "Integer32"
_BridgeConfigMstpRevisionLevel_Object = MibTableColumn
bridgeConfigMstpRevisionLevel = _BridgeConfigMstpRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 10),
    _BridgeConfigMstpRevisionLevel_Type()
)
bridgeConfigMstpRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigMstpRevisionLevel.setStatus("current")


class _BridgeConfigMstpMaxHops_Type(Integer32):
    """Custom type bridgeConfigMstpMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeConfigMstpMaxHops_Type.__name__ = "Integer32"
_BridgeConfigMstpMaxHops_Object = MibTableColumn
bridgeConfigMstpMaxHops = _BridgeConfigMstpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 11),
    _BridgeConfigMstpMaxHops_Type()
)
bridgeConfigMstpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigMstpMaxHops.setStatus("current")
_BridgeConfigMstpStpAgingTime_Type = Unsigned32
_BridgeConfigMstpStpAgingTime_Object = MibTableColumn
bridgeConfigMstpStpAgingTime = _BridgeConfigMstpStpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 1, 1, 12),
    _BridgeConfigMstpStpAgingTime_Type()
)
bridgeConfigMstpStpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfigMstpStpAgingTime.setStatus("current")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1)
)
portConfigEntry.setIndexNames(
    (0, "G6-STP-MIB", "portConfigPortIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")


class _PortConfigPortIndex_Type(Integer32):
    """Custom type portConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortConfigPortIndex_Type.__name__ = "Integer32"
_PortConfigPortIndex_Object = MibTableColumn
portConfigPortIndex = _PortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 1),
    _PortConfigPortIndex_Type()
)
portConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portConfigPortIndex.setStatus("current")


class _PortConfigEnable_Type(Integer32):
    """Custom type portConfigEnable based on Integer32"""
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


_PortConfigEnable_Type.__name__ = "Integer32"
_PortConfigEnable_Object = MibTableColumn
portConfigEnable = _PortConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 2),
    _PortConfigEnable_Type()
)
portConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigEnable.setStatus("current")


class _PortConfigPriority_Type(Integer32):
    """Custom type portConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortConfigPriority_Type.__name__ = "Integer32"
_PortConfigPriority_Object = MibTableColumn
portConfigPriority = _PortConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 3),
    _PortConfigPriority_Type()
)
portConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigPriority.setStatus("current")


class _PortConfigAdminP2pPort_Type(Integer32):
    """Custom type portConfigAdminP2pPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("forceFalse", 1),
          ("forceTrue", 2))
    )


_PortConfigAdminP2pPort_Type.__name__ = "Integer32"
_PortConfigAdminP2pPort_Object = MibTableColumn
portConfigAdminP2pPort = _PortConfigAdminP2pPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 4),
    _PortConfigAdminP2pPort_Type()
)
portConfigAdminP2pPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAdminP2pPort.setStatus("current")


class _PortConfigAdminEdgePort_Type(Integer32):
    """Custom type portConfigAdminEdgePort based on Integer32"""
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


_PortConfigAdminEdgePort_Type.__name__ = "Integer32"
_PortConfigAdminEdgePort_Object = MibTableColumn
portConfigAdminEdgePort = _PortConfigAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 5),
    _PortConfigAdminEdgePort_Type()
)
portConfigAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAdminEdgePort.setStatus("current")
_PortConfigAdminPathCost_Type = Unsigned32
_PortConfigAdminPathCost_Object = MibTableColumn
portConfigAdminPathCost = _PortConfigAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 6),
    _PortConfigAdminPathCost_Type()
)
portConfigAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAdminPathCost.setStatus("current")
_PortConfigProtocolMigration_Type = DisplayString
_PortConfigProtocolMigration_Object = MibTableColumn
portConfigProtocolMigration = _PortConfigProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 7),
    _PortConfigProtocolMigration_Type()
)
portConfigProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigProtocolMigration.setStatus("current")


class _PortConfigBridgeAssurance_Type(Integer32):
    """Custom type portConfigBridgeAssurance based on Integer32"""
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


_PortConfigBridgeAssurance_Type.__name__ = "Integer32"
_PortConfigBridgeAssurance_Object = MibTableColumn
portConfigBridgeAssurance = _PortConfigBridgeAssurance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 8),
    _PortConfigBridgeAssurance_Type()
)
portConfigBridgeAssurance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBridgeAssurance.setStatus("current")


class _PortConfigMstpDefaultPriority_Type(Integer32):
    """Custom type portConfigMstpDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortConfigMstpDefaultPriority_Type.__name__ = "Integer32"
_PortConfigMstpDefaultPriority_Object = MibTableColumn
portConfigMstpDefaultPriority = _PortConfigMstpDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 9),
    _PortConfigMstpDefaultPriority_Type()
)
portConfigMstpDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMstpDefaultPriority.setStatus("current")
_PortConfigMstpPortPriority_Type = DisplayString
_PortConfigMstpPortPriority_Object = MibTableColumn
portConfigMstpPortPriority = _PortConfigMstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 10),
    _PortConfigMstpPortPriority_Type()
)
portConfigMstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMstpPortPriority.setStatus("current")
_PortConfigMstpDefaultAdminPathCost_Type = Unsigned32
_PortConfigMstpDefaultAdminPathCost_Object = MibTableColumn
portConfigMstpDefaultAdminPathCost = _PortConfigMstpDefaultAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 11),
    _PortConfigMstpDefaultAdminPathCost_Type()
)
portConfigMstpDefaultAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMstpDefaultAdminPathCost.setStatus("current")
_PortConfigMstpPortAdminPathCost_Type = DisplayString
_PortConfigMstpPortAdminPathCost_Object = MibTableColumn
portConfigMstpPortAdminPathCost = _PortConfigMstpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 12),
    _PortConfigMstpPortAdminPathCost_Type()
)
portConfigMstpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMstpPortAdminPathCost.setStatus("current")


class _PortConfigBpduGuard_Type(Integer32):
    """Custom type portConfigBpduGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("dropAndEvent", 1),
          ("blockPort", 2))
    )


_PortConfigBpduGuard_Type.__name__ = "Integer32"
_PortConfigBpduGuard_Object = MibTableColumn
portConfigBpduGuard = _PortConfigBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 13),
    _PortConfigBpduGuard_Type()
)
portConfigBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBpduGuard.setStatus("current")


class _PortConfigBpduReceiveOnly_Type(Integer32):
    """Custom type portConfigBpduReceiveOnly based on Integer32"""
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


_PortConfigBpduReceiveOnly_Type.__name__ = "Integer32"
_PortConfigBpduReceiveOnly_Object = MibTableColumn
portConfigBpduReceiveOnly = _PortConfigBpduReceiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 14),
    _PortConfigBpduReceiveOnly_Type()
)
portConfigBpduReceiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBpduReceiveOnly.setStatus("current")


class _PortConfigRestrictTcn_Type(Integer32):
    """Custom type portConfigRestrictTcn based on Integer32"""
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


_PortConfigRestrictTcn_Type.__name__ = "Integer32"
_PortConfigRestrictTcn_Object = MibTableColumn
portConfigRestrictTcn = _PortConfigRestrictTcn_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 15),
    _PortConfigRestrictTcn_Type()
)
portConfigRestrictTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigRestrictTcn.setStatus("current")


class _PortConfigRestrictRoot_Type(Integer32):
    """Custom type portConfigRestrictRoot based on Integer32"""
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


_PortConfigRestrictRoot_Type.__name__ = "Integer32"
_PortConfigRestrictRoot_Object = MibTableColumn
portConfigRestrictRoot = _PortConfigRestrictRoot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 2, 1, 16),
    _PortConfigRestrictRoot_Type()
)
portConfigRestrictRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigRestrictRoot.setStatus("current")
_MstpGroupTable_Object = MibTable
mstpGroupTable = _MstpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 3)
)
if mibBuilder.loadTexts:
    mstpGroupTable.setStatus("current")
_MstpGroupEntry_Object = MibTableRow
mstpGroupEntry = _MstpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 3, 1)
)
mstpGroupEntry.setIndexNames(
    (0, "G6-STP-MIB", "mstpGroupIndex"),
)
if mibBuilder.loadTexts:
    mstpGroupEntry.setStatus("current")


class _MstpGroupIndex_Type(Integer32):
    """Custom type mstpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_MstpGroupIndex_Type.__name__ = "Integer32"
_MstpGroupIndex_Object = MibTableColumn
mstpGroupIndex = _MstpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 3, 1, 1),
    _MstpGroupIndex_Type()
)
mstpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpGroupIndex.setStatus("current")
_MstpGroupMstpId_Type = DisplayString
_MstpGroupMstpId_Object = MibTableColumn
mstpGroupMstpId = _MstpGroupMstpId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 3, 1, 2),
    _MstpGroupMstpId_Type()
)
mstpGroupMstpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGroupMstpId.setStatus("current")


class _MstpGroupBridgePriority_Type(Integer32):
    """Custom type mstpGroupBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpGroupBridgePriority_Type.__name__ = "Integer32"
_MstpGroupBridgePriority_Object = MibTableColumn
mstpGroupBridgePriority = _MstpGroupBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 3, 1, 3),
    _MstpGroupBridgePriority_Type()
)
mstpGroupBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGroupBridgePriority.setStatus("current")
_BridgeStatusTable_Object = MibTable
bridgeStatusTable = _BridgeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100)
)
if mibBuilder.loadTexts:
    bridgeStatusTable.setStatus("current")
_BridgeStatusEntry_Object = MibTableRow
bridgeStatusEntry = _BridgeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1)
)
bridgeStatusEntry.setIndexNames(
    (0, "G6-STP-MIB", "bridgeStatusIndex"),
)
if mibBuilder.loadTexts:
    bridgeStatusEntry.setStatus("current")


class _BridgeStatusIndex_Type(Integer32):
    """Custom type bridgeStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_BridgeStatusIndex_Type.__name__ = "Integer32"
_BridgeStatusIndex_Object = MibTableColumn
bridgeStatusIndex = _BridgeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 1),
    _BridgeStatusIndex_Type()
)
bridgeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeStatusIndex.setStatus("current")


class _BridgeStatusStpProtocol_Type(Integer32):
    """Custom type bridgeStatusStpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BridgeStatusStpProtocol_Type.__name__ = "Integer32"
_BridgeStatusStpProtocol_Object = MibTableColumn
bridgeStatusStpProtocol = _BridgeStatusStpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 2),
    _BridgeStatusStpProtocol_Type()
)
bridgeStatusStpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusStpProtocol.setStatus("current")


class _BridgeStatusHelloTime_Type(Integer32):
    """Custom type bridgeStatusHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusHelloTime_Type.__name__ = "Integer32"
_BridgeStatusHelloTime_Object = MibTableColumn
bridgeStatusHelloTime = _BridgeStatusHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 3),
    _BridgeStatusHelloTime_Type()
)
bridgeStatusHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusHelloTime.setStatus("current")


class _BridgeStatusMaxAge_Type(Integer32):
    """Custom type bridgeStatusMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusMaxAge_Type.__name__ = "Integer32"
_BridgeStatusMaxAge_Object = MibTableColumn
bridgeStatusMaxAge = _BridgeStatusMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 4),
    _BridgeStatusMaxAge_Type()
)
bridgeStatusMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusMaxAge.setStatus("current")


class _BridgeStatusHoldTime_Type(Integer32):
    """Custom type bridgeStatusHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusHoldTime_Type.__name__ = "Integer32"
_BridgeStatusHoldTime_Object = MibTableColumn
bridgeStatusHoldTime = _BridgeStatusHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 5),
    _BridgeStatusHoldTime_Type()
)
bridgeStatusHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusHoldTime.setStatus("current")


class _BridgeStatusForwardDelay_Type(Integer32):
    """Custom type bridgeStatusForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusForwardDelay_Type.__name__ = "Integer32"
_BridgeStatusForwardDelay_Object = MibTableColumn
bridgeStatusForwardDelay = _BridgeStatusForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 6),
    _BridgeStatusForwardDelay_Type()
)
bridgeStatusForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusForwardDelay.setStatus("current")


class _BridgeStatusRootPort_Type(Integer32):
    """Custom type bridgeStatusRootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusRootPort_Type.__name__ = "Integer32"
_BridgeStatusRootPort_Object = MibTableColumn
bridgeStatusRootPort = _BridgeStatusRootPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 7),
    _BridgeStatusRootPort_Type()
)
bridgeStatusRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusRootPort.setStatus("current")
_BridgeStatusRootCost_Type = Unsigned32
_BridgeStatusRootCost_Object = MibTableColumn
bridgeStatusRootCost = _BridgeStatusRootCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 8),
    _BridgeStatusRootCost_Type()
)
bridgeStatusRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusRootCost.setStatus("current")


class _BridgeStatusTopologyChanges_Type(Integer32):
    """Custom type bridgeStatusTopologyChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusTopologyChanges_Type.__name__ = "Integer32"
_BridgeStatusTopologyChanges_Object = MibTableColumn
bridgeStatusTopologyChanges = _BridgeStatusTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 9),
    _BridgeStatusTopologyChanges_Type()
)
bridgeStatusTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusTopologyChanges.setStatus("current")
_BridgeStatusLastTopologyChange_Type = Counter32
_BridgeStatusLastTopologyChange_Object = MibTableColumn
bridgeStatusLastTopologyChange = _BridgeStatusLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 10),
    _BridgeStatusLastTopologyChange_Type()
)
bridgeStatusLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusLastTopologyChange.setStatus("current")
_BridgeStatusMstpRegionName_Type = DisplayString
_BridgeStatusMstpRegionName_Object = MibTableColumn
bridgeStatusMstpRegionName = _BridgeStatusMstpRegionName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 11),
    _BridgeStatusMstpRegionName_Type()
)
bridgeStatusMstpRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusMstpRegionName.setStatus("current")


class _BridgeStatusMstiRevisionLevel_Type(Integer32):
    """Custom type bridgeStatusMstiRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusMstiRevisionLevel_Type.__name__ = "Integer32"
_BridgeStatusMstiRevisionLevel_Object = MibTableColumn
bridgeStatusMstiRevisionLevel = _BridgeStatusMstiRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 12),
    _BridgeStatusMstiRevisionLevel_Type()
)
bridgeStatusMstiRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusMstiRevisionLevel.setStatus("current")
_BridgeStatusCistInternalRootPathCost_Type = Unsigned32
_BridgeStatusCistInternalRootPathCost_Object = MibTableColumn
bridgeStatusCistInternalRootPathCost = _BridgeStatusCistInternalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 13),
    _BridgeStatusCistInternalRootPathCost_Type()
)
bridgeStatusCistInternalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusCistInternalRootPathCost.setStatus("current")
_BridgeStatusCistRegionalRootId_Type = DisplayString
_BridgeStatusCistRegionalRootId_Object = MibTableColumn
bridgeStatusCistRegionalRootId = _BridgeStatusCistRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 14),
    _BridgeStatusCistRegionalRootId_Type()
)
bridgeStatusCistRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusCistRegionalRootId.setStatus("current")
_BridgeStatusCistRegionalRootPriority_Type = Unsigned32
_BridgeStatusCistRegionalRootPriority_Object = MibTableColumn
bridgeStatusCistRegionalRootPriority = _BridgeStatusCistRegionalRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 15),
    _BridgeStatusCistRegionalRootPriority_Type()
)
bridgeStatusCistRegionalRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusCistRegionalRootPriority.setStatus("current")
_BridgeStatusCistRegionalRootMac_Type = MacAddress
_BridgeStatusCistRegionalRootMac_Object = MibTableColumn
bridgeStatusCistRegionalRootMac = _BridgeStatusCistRegionalRootMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 16),
    _BridgeStatusCistRegionalRootMac_Type()
)
bridgeStatusCistRegionalRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusCistRegionalRootMac.setStatus("current")


class _BridgeStatusMaxHops_Type(Integer32):
    """Custom type bridgeStatusMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeStatusMaxHops_Type.__name__ = "Integer32"
_BridgeStatusMaxHops_Object = MibTableColumn
bridgeStatusMaxHops = _BridgeStatusMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 17),
    _BridgeStatusMaxHops_Type()
)
bridgeStatusMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusMaxHops.setStatus("current")
_BridgeStatusMstpStpAgingTime_Type = Unsigned32
_BridgeStatusMstpStpAgingTime_Object = MibTableColumn
bridgeStatusMstpStpAgingTime = _BridgeStatusMstpStpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 100, 1, 18),
    _BridgeStatusMstpStpAgingTime_Type()
)
bridgeStatusMstpStpAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusMstpStpAgingTime.setStatus("current")
_PortStatusTable_Object = MibTable
portStatusTable = _PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101)
)
if mibBuilder.loadTexts:
    portStatusTable.setStatus("current")
_PortStatusEntry_Object = MibTableRow
portStatusEntry = _PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1)
)
portStatusEntry.setIndexNames(
    (0, "G6-STP-MIB", "portStatusPortIndex"),
)
if mibBuilder.loadTexts:
    portStatusEntry.setStatus("current")


class _PortStatusPortIndex_Type(Integer32):
    """Custom type portStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PortStatusPortIndex_Type.__name__ = "Integer32"
_PortStatusPortIndex_Object = MibTableColumn
portStatusPortIndex = _PortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 1),
    _PortStatusPortIndex_Type()
)
portStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatusPortIndex.setStatus("current")


class _PortStatusPort_Type(Integer32):
    """Custom type portStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortStatusPort_Type.__name__ = "Integer32"
_PortStatusPort_Object = MibTableColumn
portStatusPort = _PortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 2),
    _PortStatusPort_Type()
)
portStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusPort.setStatus("current")


class _PortStatusState_Type(Integer32):
    """Custom type portStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("blocking", 4),
          ("listening", 5),
          ("broken", 6))
    )


_PortStatusState_Type.__name__ = "Integer32"
_PortStatusState_Object = MibTableColumn
portStatusState = _PortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 3),
    _PortStatusState_Type()
)
portStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusState.setStatus("current")
_PortStatusLocalPortCost_Type = Unsigned32
_PortStatusLocalPortCost_Object = MibTableColumn
portStatusLocalPortCost = _PortStatusLocalPortCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 4),
    _PortStatusLocalPortCost_Type()
)
portStatusLocalPortCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLocalPortCost.setStatus("current")
_PortStatusDesignatedPortId_Type = DisplayString
_PortStatusDesignatedPortId_Object = MibTableColumn
portStatusDesignatedPortId = _PortStatusDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 5),
    _PortStatusDesignatedPortId_Type()
)
portStatusDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedPortId.setStatus("current")
_PortStatusDesignatedPort_Type = Unsigned32
_PortStatusDesignatedPort_Object = MibTableColumn
portStatusDesignatedPort = _PortStatusDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 6),
    _PortStatusDesignatedPort_Type()
)
portStatusDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedPort.setStatus("current")
_PortStatusDesignatedPortPriority_Type = Unsigned32
_PortStatusDesignatedPortPriority_Object = MibTableColumn
portStatusDesignatedPortPriority = _PortStatusDesignatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 7),
    _PortStatusDesignatedPortPriority_Type()
)
portStatusDesignatedPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedPortPriority.setStatus("current")
_PortStatusDesignatedCost_Type = Unsigned32
_PortStatusDesignatedCost_Object = MibTableColumn
portStatusDesignatedCost = _PortStatusDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 8),
    _PortStatusDesignatedCost_Type()
)
portStatusDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedCost.setStatus("current")
_PortStatusDesignatedRootId_Type = DisplayString
_PortStatusDesignatedRootId_Object = MibTableColumn
portStatusDesignatedRootId = _PortStatusDesignatedRootId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 9),
    _PortStatusDesignatedRootId_Type()
)
portStatusDesignatedRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedRootId.setStatus("current")
_PortStatusDesignatedRootMac_Type = MacAddress
_PortStatusDesignatedRootMac_Object = MibTableColumn
portStatusDesignatedRootMac = _PortStatusDesignatedRootMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 10),
    _PortStatusDesignatedRootMac_Type()
)
portStatusDesignatedRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedRootMac.setStatus("current")


class _PortStatusDesignatedRootPriority_Type(Integer32):
    """Custom type portStatusDesignatedRootPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortStatusDesignatedRootPriority_Type.__name__ = "Integer32"
_PortStatusDesignatedRootPriority_Object = MibTableColumn
portStatusDesignatedRootPriority = _PortStatusDesignatedRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 11),
    _PortStatusDesignatedRootPriority_Type()
)
portStatusDesignatedRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedRootPriority.setStatus("current")
_PortStatusDesignatedBridgeId_Type = DisplayString
_PortStatusDesignatedBridgeId_Object = MibTableColumn
portStatusDesignatedBridgeId = _PortStatusDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 12),
    _PortStatusDesignatedBridgeId_Type()
)
portStatusDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedBridgeId.setStatus("current")
_PortStatusDesignatedBridgeMac_Type = MacAddress
_PortStatusDesignatedBridgeMac_Object = MibTableColumn
portStatusDesignatedBridgeMac = _PortStatusDesignatedBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 13),
    _PortStatusDesignatedBridgeMac_Type()
)
portStatusDesignatedBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedBridgeMac.setStatus("current")


class _PortStatusDesignatedBridgePriority_Type(Integer32):
    """Custom type portStatusDesignatedBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortStatusDesignatedBridgePriority_Type.__name__ = "Integer32"
_PortStatusDesignatedBridgePriority_Object = MibTableColumn
portStatusDesignatedBridgePriority = _PortStatusDesignatedBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 14),
    _PortStatusDesignatedBridgePriority_Type()
)
portStatusDesignatedBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDesignatedBridgePriority.setStatus("current")
_PortStatusForwardTransition_Type = Unsigned32
_PortStatusForwardTransition_Object = MibTableColumn
portStatusForwardTransition = _PortStatusForwardTransition_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 15),
    _PortStatusForwardTransition_Type()
)
portStatusForwardTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusForwardTransition.setStatus("current")


class _PortStatusOperEdgePort_Type(Integer32):
    """Custom type portStatusOperEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PortStatusOperEdgePort_Type.__name__ = "Integer32"
_PortStatusOperEdgePort_Object = MibTableColumn
portStatusOperEdgePort = _PortStatusOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 16),
    _PortStatusOperEdgePort_Type()
)
portStatusOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusOperEdgePort.setStatus("current")


class _PortStatusOperP2pPort_Type(Integer32):
    """Custom type portStatusOperP2pPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PortStatusOperP2pPort_Type.__name__ = "Integer32"
_PortStatusOperP2pPort_Object = MibTableColumn
portStatusOperP2pPort = _PortStatusOperP2pPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 17),
    _PortStatusOperP2pPort_Type()
)
portStatusOperP2pPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusOperP2pPort.setStatus("current")


class _PortStatusRole_Type(Integer32):
    """Custom type portStatusRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("root", 1),
          ("designated", 2),
          ("alternate", 3),
          ("backup", 4),
          ("master", 5),
          ("disabled", 6))
    )


_PortStatusRole_Type.__name__ = "Integer32"
_PortStatusRole_Object = MibTableColumn
portStatusRole = _PortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 18),
    _PortStatusRole_Type()
)
portStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusRole.setStatus("current")


class _PortStatusInconsistentBridge_Type(Integer32):
    """Custom type portStatusInconsistentBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PortStatusInconsistentBridge_Type.__name__ = "Integer32"
_PortStatusInconsistentBridge_Object = MibTableColumn
portStatusInconsistentBridge = _PortStatusInconsistentBridge_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 101, 1, 19),
    _PortStatusInconsistentBridge_Type()
)
portStatusInconsistentBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusInconsistentBridge.setStatus("current")
_MstpStatusTableTable_Object = MibTable
mstpStatusTableTable = _MstpStatusTableTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102)
)
if mibBuilder.loadTexts:
    mstpStatusTableTable.setStatus("current")
_MstpStatusTableEntry_Object = MibTableRow
mstpStatusTableEntry = _MstpStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1)
)
mstpStatusTableEntry.setIndexNames(
    (0, "G6-STP-MIB", "mstpStatusTableIndex"),
)
if mibBuilder.loadTexts:
    mstpStatusTableEntry.setStatus("current")


class _MstpStatusTableIndex_Type(Integer32):
    """Custom type mstpStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_MstpStatusTableIndex_Type.__name__ = "Integer32"
_MstpStatusTableIndex_Object = MibTableColumn
mstpStatusTableIndex = _MstpStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 1),
    _MstpStatusTableIndex_Type()
)
mstpStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpStatusTableIndex.setStatus("current")


class _MstpStatusTableMstpId_Type(Integer32):
    """Custom type mstpStatusTableMstpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpStatusTableMstpId_Type.__name__ = "Integer32"
_MstpStatusTableMstpId_Object = MibTableColumn
mstpStatusTableMstpId = _MstpStatusTableMstpId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 2),
    _MstpStatusTableMstpId_Type()
)
mstpStatusTableMstpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTableMstpId.setStatus("current")


class _MstpStatusTablePort_Type(Integer32):
    """Custom type mstpStatusTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpStatusTablePort_Type.__name__ = "Integer32"
_MstpStatusTablePort_Object = MibTableColumn
mstpStatusTablePort = _MstpStatusTablePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 3),
    _MstpStatusTablePort_Type()
)
mstpStatusTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTablePort.setStatus("current")


class _MstpStatusTableState_Type(Integer32):
    """Custom type mstpStatusTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("blocking", 4),
          ("listening", 5),
          ("broken", 6))
    )


_MstpStatusTableState_Type.__name__ = "Integer32"
_MstpStatusTableState_Object = MibTableColumn
mstpStatusTableState = _MstpStatusTableState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 4),
    _MstpStatusTableState_Type()
)
mstpStatusTableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTableState.setStatus("current")


class _MstpStatusTablePortPriority_Type(Integer32):
    """Custom type mstpStatusTablePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MstpStatusTablePortPriority_Type.__name__ = "Integer32"
_MstpStatusTablePortPriority_Object = MibTableColumn
mstpStatusTablePortPriority = _MstpStatusTablePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 5),
    _MstpStatusTablePortPriority_Type()
)
mstpStatusTablePortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTablePortPriority.setStatus("current")
_MstpStatusTableInternalAdminPathCost_Type = Unsigned32
_MstpStatusTableInternalAdminPathCost_Object = MibTableColumn
mstpStatusTableInternalAdminPathCost = _MstpStatusTableInternalAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 6),
    _MstpStatusTableInternalAdminPathCost_Type()
)
mstpStatusTableInternalAdminPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTableInternalAdminPathCost.setStatus("current")
_MstpStatusTableForwardTransition_Type = Unsigned32
_MstpStatusTableForwardTransition_Object = MibTableColumn
mstpStatusTableForwardTransition = _MstpStatusTableForwardTransition_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 7),
    _MstpStatusTableForwardTransition_Type()
)
mstpStatusTableForwardTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTableForwardTransition.setStatus("current")


class _MstpStatusTableRole_Type(Integer32):
    """Custom type mstpStatusTableRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("root", 1),
          ("designated", 2),
          ("alternate", 3),
          ("backup", 4),
          ("master", 5),
          ("disabled", 6))
    )


_MstpStatusTableRole_Type.__name__ = "Integer32"
_MstpStatusTableRole_Object = MibTableColumn
mstpStatusTableRole = _MstpStatusTableRole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 102, 1, 8),
    _MstpStatusTableRole_Type()
)
mstpStatusTableRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpStatusTableRole.setStatus("current")
_MstpBridgeStatusTable_Object = MibTable
mstpBridgeStatusTable = _MstpBridgeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103)
)
if mibBuilder.loadTexts:
    mstpBridgeStatusTable.setStatus("current")
_MstpBridgeStatusEntry_Object = MibTableRow
mstpBridgeStatusEntry = _MstpBridgeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1)
)
mstpBridgeStatusEntry.setIndexNames(
    (0, "G6-STP-MIB", "mstpBridgeStatusIndex"),
)
if mibBuilder.loadTexts:
    mstpBridgeStatusEntry.setStatus("current")


class _MstpBridgeStatusIndex_Type(Integer32):
    """Custom type mstpBridgeStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_MstpBridgeStatusIndex_Type.__name__ = "Integer32"
_MstpBridgeStatusIndex_Object = MibTableColumn
mstpBridgeStatusIndex = _MstpBridgeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 1),
    _MstpBridgeStatusIndex_Type()
)
mstpBridgeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpBridgeStatusIndex.setStatus("current")


class _MstpBridgeStatusMstpId_Type(Integer32):
    """Custom type mstpBridgeStatusMstpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpBridgeStatusMstpId_Type.__name__ = "Integer32"
_MstpBridgeStatusMstpId_Object = MibTableColumn
mstpBridgeStatusMstpId = _MstpBridgeStatusMstpId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 2),
    _MstpBridgeStatusMstpId_Type()
)
mstpBridgeStatusMstpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusMstpId.setStatus("current")
_MstpBridgeStatusBridgePriority_Type = Unsigned32
_MstpBridgeStatusBridgePriority_Object = MibTableColumn
mstpBridgeStatusBridgePriority = _MstpBridgeStatusBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 3),
    _MstpBridgeStatusBridgePriority_Type()
)
mstpBridgeStatusBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusBridgePriority.setStatus("current")


class _MstpBridgeStatusRootPort_Type(Integer32):
    """Custom type mstpBridgeStatusRootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpBridgeStatusRootPort_Type.__name__ = "Integer32"
_MstpBridgeStatusRootPort_Object = MibTableColumn
mstpBridgeStatusRootPort = _MstpBridgeStatusRootPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 4),
    _MstpBridgeStatusRootPort_Type()
)
mstpBridgeStatusRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusRootPort.setStatus("current")
_MstpBridgeStatusRootCost_Type = Unsigned32
_MstpBridgeStatusRootCost_Object = MibTableColumn
mstpBridgeStatusRootCost = _MstpBridgeStatusRootCost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 5),
    _MstpBridgeStatusRootCost_Type()
)
mstpBridgeStatusRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusRootCost.setStatus("current")


class _MstpBridgeStatusMaxHops_Type(Integer32):
    """Custom type mstpBridgeStatusMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpBridgeStatusMaxHops_Type.__name__ = "Integer32"
_MstpBridgeStatusMaxHops_Object = MibTableColumn
mstpBridgeStatusMaxHops = _MstpBridgeStatusMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 6),
    _MstpBridgeStatusMaxHops_Type()
)
mstpBridgeStatusMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusMaxHops.setStatus("current")
_MstpBridgeStatusRegionalRootId_Type = DisplayString
_MstpBridgeStatusRegionalRootId_Object = MibTableColumn
mstpBridgeStatusRegionalRootId = _MstpBridgeStatusRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 7),
    _MstpBridgeStatusRegionalRootId_Type()
)
mstpBridgeStatusRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusRegionalRootId.setStatus("current")
_MstpBridgeStatusRegionalRootPriority_Type = Unsigned32
_MstpBridgeStatusRegionalRootPriority_Object = MibTableColumn
mstpBridgeStatusRegionalRootPriority = _MstpBridgeStatusRegionalRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 8),
    _MstpBridgeStatusRegionalRootPriority_Type()
)
mstpBridgeStatusRegionalRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusRegionalRootPriority.setStatus("current")
_MstpBridgeStatusRegionalRootMac_Type = MacAddress
_MstpBridgeStatusRegionalRootMac_Object = MibTableColumn
mstpBridgeStatusRegionalRootMac = _MstpBridgeStatusRegionalRootMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 9),
    _MstpBridgeStatusRegionalRootMac_Type()
)
mstpBridgeStatusRegionalRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusRegionalRootMac.setStatus("current")


class _MstpBridgeStatusTopologyChanges_Type(Integer32):
    """Custom type mstpBridgeStatusTopologyChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstpBridgeStatusTopologyChanges_Type.__name__ = "Integer32"
_MstpBridgeStatusTopologyChanges_Object = MibTableColumn
mstpBridgeStatusTopologyChanges = _MstpBridgeStatusTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 10),
    _MstpBridgeStatusTopologyChanges_Type()
)
mstpBridgeStatusTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusTopologyChanges.setStatus("current")
_MstpBridgeStatusLastTopologyChange_Type = Counter32
_MstpBridgeStatusLastTopologyChange_Object = MibTableColumn
mstpBridgeStatusLastTopologyChange = _MstpBridgeStatusLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 42, 103, 1, 11),
    _MstpBridgeStatusLastTopologyChange_Type()
)
mstpBridgeStatusLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpBridgeStatusLastTopologyChange.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-STP-MIB",
    **{"protocol": protocol,
       "stp": stp,
       "bridgeConfigTable": bridgeConfigTable,
       "bridgeConfigEntry": bridgeConfigEntry,
       "bridgeConfigIndex": bridgeConfigIndex,
       "bridgeConfigMode": bridgeConfigMode,
       "bridgeConfigPriority": bridgeConfigPriority,
       "bridgeConfigHelloTime": bridgeConfigHelloTime,
       "bridgeConfigMaxAge": bridgeConfigMaxAge,
       "bridgeConfigForwardDelay": bridgeConfigForwardDelay,
       "bridgeConfigTxHoldCount": bridgeConfigTxHoldCount,
       "bridgeConfigIeeePathCostModel": bridgeConfigIeeePathCostModel,
       "bridgeConfigMstpRegionName": bridgeConfigMstpRegionName,
       "bridgeConfigMstpRevisionLevel": bridgeConfigMstpRevisionLevel,
       "bridgeConfigMstpMaxHops": bridgeConfigMstpMaxHops,
       "bridgeConfigMstpStpAgingTime": bridgeConfigMstpStpAgingTime,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigPortIndex": portConfigPortIndex,
       "portConfigEnable": portConfigEnable,
       "portConfigPriority": portConfigPriority,
       "portConfigAdminP2pPort": portConfigAdminP2pPort,
       "portConfigAdminEdgePort": portConfigAdminEdgePort,
       "portConfigAdminPathCost": portConfigAdminPathCost,
       "portConfigProtocolMigration": portConfigProtocolMigration,
       "portConfigBridgeAssurance": portConfigBridgeAssurance,
       "portConfigMstpDefaultPriority": portConfigMstpDefaultPriority,
       "portConfigMstpPortPriority": portConfigMstpPortPriority,
       "portConfigMstpDefaultAdminPathCost": portConfigMstpDefaultAdminPathCost,
       "portConfigMstpPortAdminPathCost": portConfigMstpPortAdminPathCost,
       "portConfigBpduGuard": portConfigBpduGuard,
       "portConfigBpduReceiveOnly": portConfigBpduReceiveOnly,
       "portConfigRestrictTcn": portConfigRestrictTcn,
       "portConfigRestrictRoot": portConfigRestrictRoot,
       "mstpGroupTable": mstpGroupTable,
       "mstpGroupEntry": mstpGroupEntry,
       "mstpGroupIndex": mstpGroupIndex,
       "mstpGroupMstpId": mstpGroupMstpId,
       "mstpGroupBridgePriority": mstpGroupBridgePriority,
       "bridgeStatusTable": bridgeStatusTable,
       "bridgeStatusEntry": bridgeStatusEntry,
       "bridgeStatusIndex": bridgeStatusIndex,
       "bridgeStatusStpProtocol": bridgeStatusStpProtocol,
       "bridgeStatusHelloTime": bridgeStatusHelloTime,
       "bridgeStatusMaxAge": bridgeStatusMaxAge,
       "bridgeStatusHoldTime": bridgeStatusHoldTime,
       "bridgeStatusForwardDelay": bridgeStatusForwardDelay,
       "bridgeStatusRootPort": bridgeStatusRootPort,
       "bridgeStatusRootCost": bridgeStatusRootCost,
       "bridgeStatusTopologyChanges": bridgeStatusTopologyChanges,
       "bridgeStatusLastTopologyChange": bridgeStatusLastTopologyChange,
       "bridgeStatusMstpRegionName": bridgeStatusMstpRegionName,
       "bridgeStatusMstiRevisionLevel": bridgeStatusMstiRevisionLevel,
       "bridgeStatusCistInternalRootPathCost": bridgeStatusCistInternalRootPathCost,
       "bridgeStatusCistRegionalRootId": bridgeStatusCistRegionalRootId,
       "bridgeStatusCistRegionalRootPriority": bridgeStatusCistRegionalRootPriority,
       "bridgeStatusCistRegionalRootMac": bridgeStatusCistRegionalRootMac,
       "bridgeStatusMaxHops": bridgeStatusMaxHops,
       "bridgeStatusMstpStpAgingTime": bridgeStatusMstpStpAgingTime,
       "portStatusTable": portStatusTable,
       "portStatusEntry": portStatusEntry,
       "portStatusPortIndex": portStatusPortIndex,
       "portStatusPort": portStatusPort,
       "portStatusState": portStatusState,
       "portStatusLocalPortCost": portStatusLocalPortCost,
       "portStatusDesignatedPortId": portStatusDesignatedPortId,
       "portStatusDesignatedPort": portStatusDesignatedPort,
       "portStatusDesignatedPortPriority": portStatusDesignatedPortPriority,
       "portStatusDesignatedCost": portStatusDesignatedCost,
       "portStatusDesignatedRootId": portStatusDesignatedRootId,
       "portStatusDesignatedRootMac": portStatusDesignatedRootMac,
       "portStatusDesignatedRootPriority": portStatusDesignatedRootPriority,
       "portStatusDesignatedBridgeId": portStatusDesignatedBridgeId,
       "portStatusDesignatedBridgeMac": portStatusDesignatedBridgeMac,
       "portStatusDesignatedBridgePriority": portStatusDesignatedBridgePriority,
       "portStatusForwardTransition": portStatusForwardTransition,
       "portStatusOperEdgePort": portStatusOperEdgePort,
       "portStatusOperP2pPort": portStatusOperP2pPort,
       "portStatusRole": portStatusRole,
       "portStatusInconsistentBridge": portStatusInconsistentBridge,
       "mstpStatusTableTable": mstpStatusTableTable,
       "mstpStatusTableEntry": mstpStatusTableEntry,
       "mstpStatusTableIndex": mstpStatusTableIndex,
       "mstpStatusTableMstpId": mstpStatusTableMstpId,
       "mstpStatusTablePort": mstpStatusTablePort,
       "mstpStatusTableState": mstpStatusTableState,
       "mstpStatusTablePortPriority": mstpStatusTablePortPriority,
       "mstpStatusTableInternalAdminPathCost": mstpStatusTableInternalAdminPathCost,
       "mstpStatusTableForwardTransition": mstpStatusTableForwardTransition,
       "mstpStatusTableRole": mstpStatusTableRole,
       "mstpBridgeStatusTable": mstpBridgeStatusTable,
       "mstpBridgeStatusEntry": mstpBridgeStatusEntry,
       "mstpBridgeStatusIndex": mstpBridgeStatusIndex,
       "mstpBridgeStatusMstpId": mstpBridgeStatusMstpId,
       "mstpBridgeStatusBridgePriority": mstpBridgeStatusBridgePriority,
       "mstpBridgeStatusRootPort": mstpBridgeStatusRootPort,
       "mstpBridgeStatusRootCost": mstpBridgeStatusRootCost,
       "mstpBridgeStatusMaxHops": mstpBridgeStatusMaxHops,
       "mstpBridgeStatusRegionalRootId": mstpBridgeStatusRegionalRootId,
       "mstpBridgeStatusRegionalRootPriority": mstpBridgeStatusRegionalRootPriority,
       "mstpBridgeStatusRegionalRootMac": mstpBridgeStatusRegionalRootMac,
       "mstpBridgeStatusTopologyChanges": mstpBridgeStatusTopologyChanges,
       "mstpBridgeStatusLastTopologyChange": mstpBridgeStatusLastTopologyChange}
)
